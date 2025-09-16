webasto-ocpp-freemode
A Python script to enable FreeModeActive (plug-and-charge mode) on Webasto Unite (Vestel EVC04) wallboxes using the Open Charge Point Protocol (OCPP 1.6). This script acts as a temporary OCPP central system to send a ChangeConfiguration message, useful when the setting is greyed out in the wallbox’s web interface.
Tested with Webasto Unite firmware v3.187.0-1.0.156.0-v7.0.47 and Home Assistant’s OCPP integration (lbbrhzn/ocpp).
Prerequisites

Python 3.6+ (tested with Python 3.13; Python 3.11 or 3.12 recommended for compatibility).
Python packages: ocpp and websockets.
Network access: Your computer must be on the same network as the wallbox, with port 9000 open.
Wallbox configuration: Access to the wallbox’s web interface to set the central system address.
Charge point ID: Typically wallbox or as configured in the web interface (Ladepunkt-ID).

Installation

Clone the repository:
git clone https://github.com/<your_github_username>/webasto-ocpp-freemode.git
cd webasto-ocpp-freemode


Set up a virtual environment (optional but recommended):
python3 -m venv myenv
source myenv/bin/activate


Install dependencies:
pip install ocpp websockets



Usage

Run the script:
python3 ocpp_central.py

The script starts a websocket server on ws://0.0.0.0:9000.

Configure the wallbox:

Access the wallbox’s web interface via its IP address.
Set the Zentrale Systemadresse (Central System Address) to ws://<your_computer_ip>:9000/<charge_point_id>.
Replace <your_computer_ip> with your computer’s IP (e.g., 192.168.1.100). Find it with:ifconfig | grep "inet " | grep -v 127.0.0.1


Replace <charge_point_id> with your wallbox’s charge point ID (e.g., wallbox).
Example: ws://192.168.1.100:9000/wallbox.


Save and reboot the wallbox (via web interface or power cycle).


Monitor the output:

The script will log when the wallbox connects and whether the FreeModeActive change is accepted:Temporary OCPP central system running on ws://0.0.0.0:9000
Charge point connected: wallbox
Charge point connected.
Sending ChangeConfiguration...
Configuration change accepted!




Revert to Home Assistant:

Once you see “Configuration change accepted!”, revert the central system address to your Home Assistant OCPP address (e.g., ws://homeassistant.local:9000/wallbox).
Save and reboot the wallbox.
Stop the script with Ctrl+C.


Verify:

Test plug-and-charge (no RFID needed) to confirm FreeModeActive is enabled.
The web interface may still show the setting greyed out (UI limitation), but the functionality should work.
Restart the Home Assistant OCPP integration if stopped: Settings > Integrations > OCPP > Start.



Troubleshooting

ConnectionResetError or ConnectionClosedError:

Ensure port 9000 is open: lsof -i :9000.
Allow port 9000 in your firewall (System Settings > Network > Firewall on macOS).
Verify the wallbox’s central system address includes the charge point ID (e.g., /wallbox).
Ping the wallbox: ping <wallbox_ip>.


Configuration Rejected:

If you see “Configuration change rejected: ” (e.g., NotSupported or Rejected), your firmware may lock FreeModeActive due to Eichrecht compliance.
Contact Webasto support with firmware version v3.187.0-1.0.156.0-v7.0.47 and serial number 7000730623000085 to confirm or request an update.


No Connection:

Double-check your computer’s IP and the charge point ID.
If using OCPP 2.0.1 (check web interface), update ocpp_central.py:
Replace from ocpp.v16 with from ocpp.v201.
Change subprotocols=["ocpp1.6"] to ["ocpp2.0.1"].
Test @on('BootNotification') vs @on('boot_notification').




Python 3.13 Issues:

If errors persist, try Python 3.11:brew install python@3.11
python3.11 -m venv myenv
source myenv/bin/activate
pip install ocpp websockets
python3 ocpp_central.py





Notes

Firmware: The script was tested with Webasto Unite firmware v3.187.0-1.0.156.0-v7.0.47. Other versions may behave differently.
Home Assistant: This script is a workaround until the lbbrhzn/ocpp integration supports arbitrary ChangeConfiguration calls. Consider opening a feature request at https://github.com/lbbrhzn/ocpp.
Safety: Avoid active charging sessions during configuration changes.
License: MIT License (see LICENSE file).

Contributing
Contributions are welcome! Please open an issue or pull request on GitHub.
License
This project is licensed under the MIT License.
