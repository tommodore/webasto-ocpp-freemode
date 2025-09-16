import argparse
import asyncio
import logging
import websockets
from datetime import datetime, timezone
from ocpp.routing import on
from ocpp.v16 import ChargePoint as cp_v16, call as call_v16, call_result as call_result_v16
from ocpp.v16.enums import RegistrationStatus as RegistrationStatus_v16
from ocpp.v201 import ChargePoint as cp_v201, call as call_v201, call_result as call_result_v201
from ocpp.v201.enums import RegistrationStatusType as RegistrationStatus_v201

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class MyCentral:
    def __init__(self, charge_point_id, connection, ocpp_version, config_key, config_value):
        if ocpp_version == "1.6":
            self.cp = cp_v16(charge_point_id, connection)
            self.call = call_v16
            self.call_result = call_result_v16
            self.RegistrationStatus = RegistrationStatus_v16
            self.boot_action = "BootNotification"
        elif ocpp_version == "2.0.1":
            self.cp = cp_v201(charge_point_id, connection)
            self.call = call_v201
            self.call_result = call_result_v201
            self.RegistrationStatus = RegistrationStatus_v201
            self.boot_action = "BootNotification"
        else:
            raise ValueError("Unsupported OCPP version. Use '1.6' or '2.0.1'.")
        self.config_key = config_key
        self.config_value = config_value

    async def send_change_config(self):
        logger.info("Sending ChangeConfiguration for %s=%s", self.config_key, self.config_value)
        change_config_payload = self.call.ChangeConfiguration(key=self.config_key, value=self.config_value)
        try:
            response = await self.cp.call(change_config_payload)
            if response.status.lower() == 'accepted':
                logger.info("Configuration change accepted!")
            else:
                logger.error("Configuration change rejected: %s", response.status)
        except Exception as e:
            logger.error("Error sending ChangeConfiguration: %s", e)

    @on('BootNotification')
    async def on_boot_notification(self, charge_point_vendor, charge_point_model, **kwargs):
        logger.info("Charge point connected: %s (vendor: %s, model: %s)", self.cp.charge_point_id, charge_point_vendor, charge_point_model)
        asyncio.create_task(self.send_change_config())  # Send asynchronously
        current_time = datetime.now(tz=timezone.utc).replace(tzinfo=None).isoformat() + 'Z'
        return self.call_result.BootNotification(
            current_time=current_time,
            interval=300,
            status=self.RegistrationStatus.accepted,
        )

    async def start(self):
        await self.cp.start()

async def handle_connection(connection: websockets.ServerConnection, charge_point_id: str, ocpp_version: str, config_key: str, config_value: str):
    """Handle a new charge point connection."""
    actual_charge_point_id = connection.request.path.strip('/') or charge_point_id
    if actual_charge_point_id != charge_point_id:
        logger.warning("Charge point ID mismatch: expected %s, got %s", charge_point_id, actual_charge_point_id)
    logger.info("Charge point connecting: %s", actual_charge_point_id)
    charge_point = MyCentral(actual_charge_point_id, connection, ocpp_version, config_key, config_value)
    await charge_point.start()

async def main(host: str, port: int, charge_point_id: str, ocpp_version: str, config_key: str, config_value: str):
    """Start the OCPP central system server."""
    subprotocol = "ocpp" + ocpp_version
    logger.info("Starting OCPP central system on ws://%s:%s with subprotocol %s", host, port, subprotocol)
    server = await websockets.serve(
        lambda conn: handle_connection(conn, charge_point_id, ocpp_version, config_key, config_value),
        host,
        port,
        subprotocols=[subprotocol]
    )
    await server.wait_closed()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="OCPP central system to set charge point configuration (e.g., FreeModeActive).")
    parser.add_argument("--host", default="0.0.0.0", help="Host IP to bind the server (default: 0.0.0.0)")
    parser.add_argument("--port", type=int, default=9000, help="Port for the OCPP server (default: 9000)")
    parser.add_argument("--charge-point-id", default="wallbox", help="Expected charge point ID (default: wallbox)")
    parser.add_argument("--ocpp-version", default="1.6", choices=["1.6", "2.0.1"], help="OCPP version (default: 1.6)")
    parser.add_argument("--key", default="FreeModeActive", help="Configuration key to set (default: FreeModeActive)")
    parser.add_argument("--value", default="true", help="Value for the configuration key (default: true)")
    args = parser.parse_args()

    try:
        asyncio.run(main(args.host, args.port, args.charge_point_id, args.ocpp_version, args.key, args.value))
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
    except Exception as e:
        logger.error("Server failed: %s", e)
