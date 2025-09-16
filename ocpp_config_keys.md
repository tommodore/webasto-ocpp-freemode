```markdown
# OCPP Configuration Keys Reference

This file provides a reference table of common OCPP 1.6 configuration keys for the Webasto Unite (Vestel EVC04) wallbox, including `FreeModeActive`, as used with the `webasto-ocpp-freemode` script. These keys can be set using the `ocpp_central.py` script via the `--key` and `--value` arguments. Not all keys may be supported or writable on every firmware version (e.g., `v3.187.0-1.0.156.0-v7.0.47`). Verify support with your wallbox’s web interface logs or Webasto support.

## Configuration Keys Table

| Key | Possible Values | Description | Supported by Webasto Unite |
|-----|-----------------|-------------|----------------------------|
| `FreeModeActive` | `true`, `false` | Enables plug-and-charge mode without authorization (e.g., RFID). Set to `true` for free charging. | Yes (tested on firmware `v3.187.0-1.0.156.0-v7.0.47`) |
| `FreeModeRFID` | `true`, `false` | Allows RFID-based authorization in free mode. Set to `true` to require RFID even in free mode. | Likely (listed in web interface) |
| `AllowOfflineTxForUnknownId` | `true`, `false` | Allows charging for unknown identifiers when offline. | Likely (listed in web interface) |
| `AuthorizationCacheEnabled` | `true`, `false` | Enables caching of authorization data for offline use. | Likely (listed in web interface) |
| `AuthorizeRemoteTxRequests` | `true`, `false` | Requires authorization for remote transaction requests. Set to `false` to bypass for remote starts. | Likely (listed in web interface) |
| `BlinkRepeat` | Integer (e.g., `0`, `1`, `2`) | Number of times to repeat LED blinking for status indication. | Likely (listed in web interface) |
| `ChargeProfileMaxStackLevel` | Integer (e.g., `4`) | Maximum number of charging profiles that can be stacked. | Likely (listed in web interface) |
| `ChargingScheduleAllowedChargingRateUnit` | Comma-separated list (e.g., `Current,Power`) | Allowed units for charging schedules (e.g., Amps or Watts). | Likely (listed in web interface) |
| `ChargingScheduleMaxPeriods` | Integer (e.g., `5`) | Maximum number of periods in a charging schedule. | Likely (listed in web interface) |
| `ClockAlignedDataInterval` | Integer (seconds, e.g., `900`) | Interval for clock-aligned meter value reporting. | Likely (listed in web interface) |
| `ConnectionTimeOut` | Integer (seconds, e.g., `30`) | Timeout for establishing a connection to the central system. | Likely (listed in web interface) |
| `ConnectorPhaseRotation` | String (e.g., `RST`, `RTS`) | Phase rotation configuration for connectors. | Likely (listed in web interface) |
| `ConnectorPhaseRotationMaxLength` | Integer (e.g., `3`) | Maximum length of phase rotation configuration string. | Likely (listed in web interface) |
| `BootNotificationAfterConnectionLoss` | `true`, `false` | Sends BootNotification after reconnecting from a connection loss. | Likely (listed in web interface) |
| `CentralSmartChargingWithNoTripping` | `true`, `false` | Enables smart charging without tripping breakers. | Likely (listed in web interface) |
| `ConnectorSwitch3to1PhaseSupported` | `true`, `false` | Supports switching between 3-phase and 1-phase charging. | Likely (listed in web interface) |
| `ContinueChargingAfterPowerLoss` | `true`, `false` | Continues charging after a power loss. | Likely (listed in web interface) |
| `CTStationCurrentInformationInterval` | Integer (seconds, e.g., `60`) | Interval for current transformer (CT) data reporting. | Likely (listed in web interface) |
| `NewTransactionAfterPowerLoss` | `true`, `false` | Starts a new transaction after power loss. | Likely (listed in web interface) |
| `DailyReboot` | `true`, `false` | Enables daily reboot of the wallbox. | Likely (listed in web interface) |
| `DailyRebootTime` | Time string (e.g., `03:00`) | Time of day for daily reboot (HH:MM format). | Likely (listed in web interface) |
| `DailyRebootType` | String (e.g., `Hard`, `Soft`) | Type of daily reboot (hard or soft reset). | Likely (listed in web interface) |
| `GetConfigurationMaxKeys` | Integer (e.g., `50`) | Maximum number of keys returned in a GetConfiguration response. | Likely (listed in web interface) |
| `HeartbeatInterval` | Integer (seconds, e.g., `300`) | Interval for sending heartbeat messages to the central system. | Likely (listed in web interface) |
| `InstallationErrorEnable` | `true`, `false` | Enables reporting of installation errors. | Likely (listed in web interface) |
| `LEDTimeoutEnable` | `true`, `false` | Enables LED timeout for status indication. | Likely (listed in web interface) |
| `LightIntensity` | Integer (e.g., `0` to `100`) | LED brightness intensity (percentage). | Likely (listed in web interface) |
| `LocalAuthListEnabled` | `true`, `false` | Enables local authorization list for offline use. | Likely (listed in web interface) |
| `LocalAuthListMaxLength` | Integer (e.g., `500`) | Maximum number of entries in the local authorization list. | Likely (listed in web interface) |
| `LocalAuthorizeOffline` | `true`, `false` | Allows offline authorization using the local list. | Likely (listed in web interface) |
| `LocalPreAuthorize` | `true`, `false` | Allows pre-authorization locally before charging. | Likely (listed in web interface) |
| `MaxChargingProfilesInstalled` | Integer (e.g., `10`) | Maximum number of charging profiles that can be installed. | Likely (listed in web interface) |
| `MaxEnergyOnInvalidId` | Integer (Wh, e.g., `0`) | Maximum energy allowed for an invalid ID. | Likely (listed in web interface) |
| `MaxPowerChargeComplete` | Integer (W, e.g., `22000`) | Maximum power allowed when charging is complete. | Likely (listed in web interface) |
| `MaxTimeChargeComplete` | Integer (seconds, e.g., `3600`) | Maximum time allowed after charging is complete. | Likely (listed in web interface) |
| `MeterValuesAlignedData` | Comma-separated list (e.g., `Energy.Active.Import.Register`) | Data items to include in aligned meter values. | Likely (listed in web interface) |
| `MeterValuesAlignedDataMaxLength` | Integer (e.g., `8`) | Maximum number of aligned data items. | Likely (listed in web interface) |
| `MeterValuesSampledData` | Comma-separated list (e.g., `Current.Import,Voltage`) | Data items to include in sampled meter values. | Likely (listed in web interface) |
| `MeterValuesSampledDataMaxLength` | Integer (e.g., `8`) | Maximum number of sampled data items. | Likely (listed in web interface) |
| `MeterValueSampleInterval` | Integer (seconds, e.g., `60`) | Interval for sampling meter values. | Likely (listed in web interface) |
| `MinimumStatusDuration` | Integer (seconds, e.g., `10`) | Minimum duration for status updates. | Likely (listed in web interface) |
| `NumberOfConnectors` | Integer (e.g., `1`) | Number of connectors on the charge point. | Likely (listed in web interface) |
| `OcppSecurityProfile` | Integer (e.g., `0`, `1`, `2`) | Security profile level (0: none, 1: basic, 2: secure). | Likely (listed in web interface) |
| `RandomDelayOnDailyRebootEnabled` | `true`, `false` | Enables random delay for daily reboots. | Likely (listed in web interface) |
| `ReserveConnectorZeroSupported` | `true`, `false` | Supports reserving connector zero. | Likely (listed in web interface) |
| `RfidEndianness` | String (e.g., `Big`, `Little`) | Endianness for RFID data. | Likely (listed in web interface) |
| `ResetRetries` | Integer (e.g., `3`) | Number of retry attempts for resets. | Likely (listed in web interface) |
| `SendDataTransferMeterConfigurationForNonEichrecht` | `true`, `false` | Sends meter configuration data for non-Eichrecht meters. | Likely (listed in web interface) |
| `SendLocalListMaxLength` | Integer (e.g., `500`) | Maximum length of the local authorization list to send. | Likely (listed in web interface) |
| `SendTotalPowerValue` | `true`, `false` | Sends total power value in meter data. | Likely (listed in web interface) |
| `StopTransactionOnEVSideDisconnect` | `true`, `false` | Stops transaction when EV disconnects. | Likely (listed in web interface) |
| `StopTransactionOnInvalidId` | `true`, `false` | Stops transaction on invalid ID. | Likely (listed in web interface) |
| `StopTxnAlignedData` | Comma-separated list (e.g., `Energy.Active.Import.Register`) | Data items to include in stop transaction aligned data. | Likely (listed in web interface) |
| `StopTxnAlignedDataMaxLength` | Integer (e.g., `8`) | Maximum number of stop transaction aligned data items. | Likely (listed in web interface) |
| `StopTxnSampledData` | Comma-separated list (e.g., `Current.Import`) | Data items to include in stop transaction sampled data. | Likely (listed in web interface) |
| `StopTxnSampledDataMaxLength` | Integer (e.g., `8`) | Maximum number of stop transaction sampled data items. | Likely (listed in web interface) |
| `SupportedFeatureProfiles` | Comma-separated list (e.g., `Core,FirmwareManagement`) | Supported OCPP feature profiles. | Likely (listed in web interface) |
| `SupportedFeatureProfilesMaxLength` | Integer (e.g., `4`) | Maximum number of supported feature profiles. | Likely (listed in web interface) |
| `TransactionMessageAttempts` | Integer (e.g., `3`) | Number of attempts for transaction messages. | Likely (listed in web interface) |
| `TransactionMessageRetryInterval` | Integer (seconds, e.g., `60`) | Interval between transaction message retries. | Likely (listed in web interface) |
| `UKSmartChargingEnabled` | `true`, `false` | Enables UK smart charging regulations. | Likely (listed in web interface) |
| `UnlockConnectorOnEVSideDisconnect` | `true`, `false` | Unlocks connector when EV disconnects. | Likely (listed in web interface) |
| `WebSocketPingInterval` | Integer (seconds, e.g., `60`) | Interval for websocket ping messages. | Likely (listed in web interface) |

## Notes

- **Supported Keys**: The table lists keys from the Webasto Unite web interface and standard OCPP 1.6 keys. “Likely” support is based on their presence in the web interface; test with the `ocpp_central.py` script to confirm writability.
- **Firmware**: Tested with firmware `v3.187.0-1.0.156.0-v7.0.47`. Some keys may be read-only due to Eichrecht compliance or firmware restrictions.
- **Usage**: Use the `ocpp_central.py` script to set keys:
  ```bash
  python3 ocpp_central.py --key <key> --value <value>
  ```
  Example: `python3 ocpp_central.py --key FreeModeActive --value true`
- **Verification**: If a key is rejected (e.g., `NotSupported` or `Rejected`), check with Webasto support (provide firmware version and serial number `7000730623000085`).
- **Missing Keys**: `AuthorizationKey` is listed in the web interface but omitted here as it’s typically sensitive (used for OCPP security profile authentication).

## References

- [OCPP 1.6 Specification](https://www.openchargealliance.org/protocols/ocpp-16/)
- [Webasto Unite Manual](https://www.webasto-charging.com/)
```