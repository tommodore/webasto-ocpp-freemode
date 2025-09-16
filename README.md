webasto-ocpp-freemode
A configurable Python script to set OCPP configuration keys (e.g., FreeModeActive for plug-and-charge mode) on Webasto Unite (Vestel EVC04) wallboxes using the Open Charge Point Protocol (OCPP 1.6 or 2.0.1). The script acts as a temporary OCPP central system to send a ChangeConfiguration message, useful when settings are greyed out in the wallbox’s web interface.
Tested with Webasto Unite firmware v3.187.0-1.0.156.0-v7.0.47 and Home Assistant’s OCPP integration (lbbrhzn/ocpp).
Features

Set any OCPP configuration key (e.g., FreeModeActive=true for plug-and-charge).
Supports OCPP 1.6 and 2.0.1.
Configurable via command-line arguments for host, port, charge point ID, key, and value.
Detailed logging for debugging.

Prerequisites

Python 3.6+ (tested with Python 3.13; Python 3.11 or 3.12 recommended for compatibility).
Python packages: ocpp and websockets.
Network access: Your computer must be on the same network as the wallbox, with the specified port (default: 9000) open.
Wallbox configuration: Access to the wallbox’s web interface to set the central system address.
Charge point ID: Typically wallbox or as configured in the web interface (Ladepunkt-ID).

Installation

Clone the repository:
git clone <https://github.com/><your_github_username>/webasto-ocpp-freemode.git
cd webasto-ocpp-freemode

Set up a virtual environment (recommended):
python3 -m venv myenv
source myenv/bin/activate

Install dependencies:
pip install ocpp websockets

Usage

Run the script with default settings (sets FreeModeActive=true for charge point wallbox on 0.0.0.0:9000 with OCPP 1.6):
python3 ocpp_central.py

Customize parameters (example):
python3 ocpp_central.py --host 192.168.1.100 --port 9000 --charge-point-id wallbox --ocpp-version 1.6 --key FreeModeActive --value true

Available arguments:

--host: Server IP (default: 0.0.0.0).
--port: Server port (default: 9000).
--charge-point-id: Charge point ID (default: wallbox).
--ocpp-version: OCPP version (1.6 or 2.0.1, default: 1.6).
--key: Configuration key (default: FreeModeActive).
--value: Configuration value (default: true).

Configure the wallbox:

Access the wallbox’s web interface via its IP address.
Set the Zentrale Systemadresse (Central System Address) to ws://<your_computer_ip>:<port>/<charge_point_id>.
Example: ws://192.168.1.100:9000/wallbox.
Find your computer’s IP:ifconfig | grep "inet " | grep -v 127.0.0.1

Save and reboot the wallbox (via web interface or power cycle).

Monitor the output:

The script logs connection and configuration status:2025-09-16 10:00:00,000 - INFO - Starting OCPP central system on ws://0.0.0.0:9000 with subprotocol ocpp1.6
2025-09-16 10:00:05,000 - INFO - Charge point connecting: wallbox
2025-09-16 10:00:05,100 - INFO - Charge point connected: wallbox (vendor: WEBASTO, model: UNITE)
2025-09-16 10:00:05,200 - INFO - Sending ChangeConfiguration for FreeModeActive=true
2025-09-16 10:00:05,300 - INFO - Configuration change accepted!

Revert to Home Assistant:

After seeing “Configuration change accepted!”, revert the central system address to your Home Assistant OCPP address (e.g., ws://homeassistant.local:9000/wallbox).
Save and reboot the wallbox.
Stop the script with Ctrl+C.

Verify:

Test plug-and-charge (no RFID needed) to confirm FreeModeActive is enabled.
The web interface may show the setting greyed out (UI limitation), but the functionality should work.
Restart the Home Assistant OCPP integration if stopped: Settings > Integrations > OCPP > Start.

Troubleshooting

ConnectionResetError or ConnectionClosedError:

Ensure the specified port (e.g., 9000) is open: lsof -i :9000.
Allow the port in your firewall (macOS: System Settings > Network > Firewall).
Verify the central system address includes the charge point ID (e.g., /wallbox).
Ping the wallbox: ping <wallbox_ip>.

Configuration Rejected:

If you see “Configuration change rejected: ” (e.g., NotSupported or Rejected), the firmware may lock the key (e.g., due to Eichrecht compliance).
Contact Webasto support with firmware version v3.187.0-1.0.156.0-v7.0.47 and serial number 7000730623000085.

No Connection:

Double-check the --host, --port, and --charge-point-id arguments.
For OCPP 2.0.1, use --ocpp-version 2.0.1:python3 ocpp_central.py --ocpp-version 2.0.1

Python 3.13 Issues:

If errors occur, try Python 3.11:brew install python@3.11
python3.11 -m venv myenv
source myenv/bin/activate
pip install ocpp websockets
python3 ocpp_central.py

Notes

Firmware: Tested with Webasto Unite firmware v3.187.0-1.0.156.0-v7.0.47. Other versions may vary.
Home Assistant: This script is a workaround until lbbrhzn/ocpp supports arbitrary ChangeConfiguration calls. Consider requesting this feature at <https://github.com/lbbrhzn/ocpp>.
Safety: Avoid active charging sessions during configuration changes.
License: MIT License (see LICENSE file).

Contributing
Contributions are welcome! Please open an issue or pull request on GitHub.
License
This project is licensed under the MIT License.
