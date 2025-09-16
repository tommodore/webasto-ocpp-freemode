import asyncio
import websockets
from datetime import datetime, timezone
from ocpp.v16 import ChargePoint as cp
from ocpp.v16 import call, call_result
from ocpp.routing import on
from ocpp.v16.enums import RegistrationStatus

class MyCentral(cp):
    async def send_change_config(self):
        await asyncio.sleep(1)  # Short delay to stabilize connection after BootNotification response
        print("Sending ChangeConfiguration...")
        change_config_payload = call.ChangeConfiguration(key="FreeModeActive", value="true")
        response = await self.call(change_config_payload)
        if response.status == 'Accepted':
            print("Configuration change accepted!")
        else:
            print(f"Configuration change rejected: {response.status}")

    @on('BootNotification')  # CamelCase to match wallbox action
    async def on_boot_notification(self, charge_point_vendor, charge_point_model, **kwargs):
        print("Charge point connected.")
        asyncio.create_task(self.send_change_config())  # Send asynchronously after responding
        current_time = datetime.now(tz=timezone.utc).replace(tzinfo=None).isoformat() + 'Z'  # Fixed format: YYYY-MM-DDThh:mm:ssZ
        return call_result.BootNotification(
            current_time=current_time,
            interval=300,
            status=RegistrationStatus.accepted,
        )

async def handle_connection(connection: websockets.ServerConnection):
    """
    For every new connection, create a new ChargePoint instance,
    and start listening for messages.
    """
    charge_point_id = connection.request.path.strip('/') or "cp1"  # Fallback if empty
    print(f"Charge point connected: {charge_point_id}")
    charge_point = MyCentral(charge_point_id, connection)
    await charge_point.start()

async def main():
    server = await websockets.serve(
        handle_connection,
        "0.0.0.0",
        9000,
        subprotocols=["ocpp1.6"]
    )
    print("Temporary OCPP central system running on ws://0.0.0.0:9000")
    await server.wait_closed()  # Keep the server running

if __name__ == "__main__":
    asyncio.run(main())
