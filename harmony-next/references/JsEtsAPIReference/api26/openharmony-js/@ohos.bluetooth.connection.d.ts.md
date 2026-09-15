# @ohos.bluetooth.connection.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (C) 2023-2024 Huawei Device Co., Ltd.
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
/**
 * @file
 * @kit ConnectivityKit
 */
import type { AsyncCallback, Callback } from './@ohos.base';
import type constant from './@ohos.bluetooth.constant';
import type common from './@ohos.bluetooth.common';
/**
 * Provides methods to operate or manage Bluetooth.
 *
 * @syscap SystemCapability.Communication.Bluetooth.Core
 * @stagemodelonly
 * @crossplatform [since 13]
 * @atomicservice [since 12]
 * @since 10
 */
declare namespace connection {
    /**
     * Indicate the profile connection state.
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @crossplatform [since 13]
     * @since 10
     */
    type ProfileConnectionState = constant.ProfileConnectionState;
    /**
     * Indicate the profile id.
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @crossplatform [since 13]
     * @since 10
     */
    type ProfileId = constant.ProfileId;
    /**
     * Indicate the profile uuid.
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @crossplatform [since 13]
     * @since 12
     */
    type ProfileUuids = constant.ProfileUuids;
    /**
     * Indicate the major class of a bluetooth device.
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @crossplatform [since 13]
     * @since 10
     */
    type MajorClass = constant.MajorClass;
    /**
     * Indicate the major minor class of a bluetooth device.
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @crossplatform [since 13]
     * @since 10
     */
    type MajorMinorClass = constant.MajorMinorClass;
    /**
     * Bluetooth device address.
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 21
     */
    type BluetoothAddress = common.BluetoothAddress;
    /**
     * Get the profile connection state of the current device.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH
     * @param { ProfileId } [profileId] - Indicate the profile id. This is an optional parameter.
     *     With profileId, returns the current connection state of this profile, {@link ProfileConnectionState}.
     *     Without profileId, if any profile is connected, {@link ProfileConnectionState#STATE_CONNECTED} is returned.
     *     Otherwise, {@link ProfileConnectionState#STATE_DISCONNECTED} is returned.
     * @returns { ProfileConnectionState } Returns the connection state.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Invalid parameter. Possible causes: 1. Incorrect parameter types.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 2900001 - Service stopped.
     * @throws { BusinessError } 2900003 - Bluetooth disabled.
     * @throws { BusinessError } 2900004 - Profile not supported.
     * @throws { BusinessError } 2900099 - Operation failed.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @crossplatform [since 13]
     * @since 10
     */
    function getProfileConnectionState(profileId?: ProfileId): ProfileConnectionState;
    /**
     * Starts pairing with a remote Bluetooth device.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH
     * @param { string } deviceId - Indicates device ID. For example, "11:22:33:AA:BB:FF".
     * @param { AsyncCallback<void> } callback - the callback of pairDevice.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 2900001 - Service stopped.
     * @throws { BusinessError } 2900003 - Bluetooth disabled.
     * @throws { BusinessError } 2900099 - Operation failed.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @crossplatform [since 13]
     * @atomicservice [since 12]
     * @since 10
     */
    function pairDevice(deviceId: string, callback: AsyncCallback<void>): void;
    /**
     * Starts pairing with a remote Bluetooth device.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH
     * @param { string } deviceId - Indicates device ID. For example, "11:22:33:AA:BB:FF".
     * @returns { Promise<void> } Returns the promise object.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 2900001 - Service stopped.
     * @throws { BusinessError } 2900003 - Bluetooth disabled.
     * @throws { BusinessError } 2900099 - Operation failed.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @crossplatform [since 13]
     * @atomicservice [since 12]
     * @since 10
     */
    function pairDevice(deviceId: string): Promise<void>;
    /**
     * Starts pairing with a remote Bluetooth device.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH
     * @param { BluetoothAddress } deviceId - Indicates address of peer device.
     * @returns { Promise<void> } Returns the promise object.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 2900001 - Service stopped.
     * @throws { BusinessError } 2900003 - Bluetooth disabled.
     * @throws { BusinessError } 2900099 - Operation failed.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @crossplatform
     * @since 21
     */
    function pairDevice(deviceId: BluetoothAddress): Promise<void>;
    /**
     * Obtains the name of a peer Bluetooth device.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH
     * @param { string } deviceId - Indicates device ID. For example, "11:22:33:AA:BB:FF".
     * @returns { string } Returns the device name in character string format.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 2900001 - Service stopped.
     * @throws { BusinessError } 2900003 - Bluetooth disabled.
     * @throws { BusinessError } 2900099 - Operation failed.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @crossplatform [since 13]
     * @atomicservice [since 12]
     * @since 10
     */
    function getRemoteDeviceName(deviceId: string): string;
    /**
     * Obtains the name or alias of the Bluetooth peer device.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH
     * @param { string } deviceId - Indicates device ID. For example, "11:22:33:AA:BB:FF".
     * @param { boolean } [alias] - Indicates whether to obtain the device alias. If the parameter is not provided, the
     *     device alias is obtained by default.
     * @returns { string } Returns the device name in character string format.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 2900001 - Service stopped.
     * @throws { BusinessError } 2900003 - Bluetooth disabled.
     * @throws { BusinessError } 2900099 - Failed to obtain the name or alias of the peer Bluetooth device.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @atomicservice
     * @since 16
     */
    function getRemoteDeviceName(deviceId: string, alias?: boolean): string;
    /**
     * Obtains the class of a peer Bluetooth device.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH [since 10 - 17]
     * @param { string } deviceId - Indicates device ID. For example, "11:22:33:AA:BB:FF".
     * @returns { DeviceClass } The class of the remote device.
     * @throws { BusinessError } 201 - Permission denied. [since 10 - 17]
     * @throws { BusinessError } 401 - Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 2900001 - Service stopped.
     * @throws { BusinessError } 2900003 - Bluetooth disabled.
     * @throws { BusinessError } 2900099 - Operation failed.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @crossplatform [since 13]
     * @since 10
     */
    function getRemoteDeviceClass(deviceId: string): DeviceClass;
    /**
     * Get the transport of the bluetooth device.
     *
     * @param { string } deviceId - Indicates device ID. For example, "11:22:33:AA:BB:FF".
     * @returns { BluetoothTransport } The transport of bluetooth device.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 2900001 - Service stopped.
     * @throws { BusinessError } 2900003 - Bluetooth disabled.
     * @throws { BusinessError } 2900099 - Get transport failed.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 20
     */
    function getRemoteDeviceTransport(deviceId: string): BluetoothTransport;
    /**
     * Obtains the Bluetooth local name of a device.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH
     * @returns { string } Returns the name the device.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 2900001 - Service stopped.
     * @throws { BusinessError } 2900099 - Operation failed.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @crossplatform [since 13]
     * @since 10
     */
    function getLocalName(): string;
    /**
     * Obtains the list of Bluetooth devices that have been paired with the current device.
     * On API 26.0.0 and above, if the application has ohos.permission.GET_BLUETOOTH_PEERS_MAC,
     * the type of the peer device address is real.
     * Otherwise, the type of the peer device address is virtual.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH [since 10 - 24]
     * @permission ohos.permission.ACCESS_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and
     *     ohos.permission.GET_BLUETOOTH_PEERS_MAC) [since 26.0.0]
     * @returns { Array<string> } Returns a list of paired Bluetooth devices's address.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 2900001 - Service stopped.
     * @throws { BusinessError } 2900003 - Bluetooth disabled.
     * @throws { BusinessError } 2900099 - Operation failed.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @crossplatform [since 13]
     * @atomicservice [since 12]
     * @since 10
     */
    function getPairedDevices(): Array<string>;
    /**
     * Obtains the pair state of a specified device.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH
     * @param { string } deviceId - Indicates device ID. For example, "11:22:33:AA:BB:FF".
     * @returns { BondState } Returns the pair state.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 2900001 - Service stopped.
     * @throws { BusinessError } 2900003 - Bluetooth disabled.
     * @throws { BusinessError } 2900099 - Operation failed.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @crossplatform [since 13]
     * @atomicservice [since 12]
     * @since 11
     */
    function getPairState(deviceId: string): BondState;
    /**
     * Sets the confirmation of pairing with a certain device.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH
     * @param { string } deviceId - Indicates device ID. For example, "11:22:33:AA:BB:FF".
     * @param { boolean } accept - Indicates whether to accept the pairing request, {@code true} indicates accept or
     *     {@code false} otherwise.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 2900001 - Service stopped.
     * @throws { BusinessError } 2900003 - Bluetooth disabled.
     * @throws { BusinessError } 2900099 - Operation failed.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 10
     */
    function setDevicePairingConfirmation(deviceId: string, accept: boolean): void;
    /**
     * Set the pin during pairing when the pin type is PIN_TYPE_ENTER_PIN_CODE.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH
     * @param { string } deviceId - Indicates device ID. For example, "11:22:33:AA:BB:FF".
     * @param { string } code - The pin code entered by the user.
     * @param { AsyncCallback<void> } callback - the callback of setDevicePinCode.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 2900001 - Service stopped.
     * @throws { BusinessError } 2900003 - Bluetooth disabled.
     * @throws { BusinessError } 2900099 - Operation failed.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 10
     */
    function setDevicePinCode(deviceId: string, code: string, callback: AsyncCallback<void>): void;
    /**
     * Set the pin during pairing when the pin type is PIN_TYPE_ENTER_PIN_CODE.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH
     * @param { string } deviceId - Indicates device ID. For example, "11:22:33:AA:BB:FF".
     * @param { string } code - The pin code entered by the user.
     * @returns { Promise<void> } Returns the promise object.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 2900001 - Service stopped.
     * @throws { BusinessError } 2900003 - Bluetooth disabled.
     * @throws { BusinessError } 2900099 - Operation failed.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 10
     */
    function setDevicePinCode(deviceId: string, code: string): Promise<void>;
    /**
     * Sets the Bluetooth friendly name of a device. It is used only by system applications for security.
     * If a non-system application invokes the interface, exception 801 is thrown.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH
     * @param { string } name - Indicates a valid Bluetooth name.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 2900001 - Service stopped.
     * @throws { BusinessError } 2900003 - Bluetooth disabled.
     * @throws { BusinessError } 2900099 - Operation failed.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 10
     * @deprecated since 12
     */
    function setLocalName(name: string): void;
    /**
     * Sets the Bluetooth scan mode for a device.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH
     * @param { ScanMode } mode - Indicates the Bluetooth scan mode to set.
     * @param { number } duration - Indicates the duration in seconds, in which the host is discoverable.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 2900001 - Service stopped.
     * @throws { BusinessError } 2900003 - Bluetooth disabled.
     * @throws { BusinessError } 2900099 - Operation failed.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 10
     */
    function setBluetoothScanMode(mode: ScanMode, duration: number): void;
    /**
     * Obtains the Bluetooth scanning mode of a device.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH
     * @returns { ScanMode } Returns the Bluetooth scanning mode.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 2900001 - Service stopped.
     * @throws { BusinessError } 2900003 - Bluetooth disabled.
     * @throws { BusinessError } 2900099 - Operation failed.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @crossplatform [since 13]
     * @since 10
     */
    function getBluetoothScanMode(): ScanMode;
    /**
     * Starts scanning Bluetooth devices.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 2900001 - Service stopped.
     * @throws { BusinessError } 2900003 - Bluetooth disabled.
     * @throws { BusinessError } 2900099 - Operation failed.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @crossplatform [since 13]
     * @atomicservice [since 12]
     * @since 10
     */
    function startBluetoothDiscovery(): void;
    /**
     * Stops Bluetooth device scanning.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 2900001 - Service stopped.
     * @throws { BusinessError } 2900003 - Bluetooth disabled.
     * @throws { BusinessError } 2900099 - Operation failed.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @crossplatform [since 13]
     * @atomicservice [since 12]
     * @since 10
     */
    function stopBluetoothDiscovery(): void;
    /**
     * Check if bluetooth is discovering.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH
     * @returns { boolean } Returns {@code true} if the local device is discovering; returns {@code false} otherwise.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 2900001 - Service stopped.
     * @throws { BusinessError } 2900003 - Bluetooth disabled.
     * @throws { BusinessError } 2900099 - Operation failed.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @crossplatform [since 13]
     * @since 11
     */
    function isBluetoothDiscovering(): boolean;
    /**
     * Obtains the profile UUIDs supported by the remote device.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH
     * @param { string } deviceId - Indicates device ID. For example, "11:22:33:AA:BB:FF".
     * @param { AsyncCallback<Array<ProfileUuids>> } callback - the callback of getRemoteProfileUuids.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Invalid parameter.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 2900001 - Service stopped.
     * @throws { BusinessError } 2900003 - Bluetooth disabled.
     * @throws { BusinessError } 2900099 - Operation failed.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @crossplatform [since 13]
     * @since 12
     */
    function getRemoteProfileUuids(deviceId: string, callback: AsyncCallback<Array<ProfileUuids>>): void;
    /**
     * Obtains the profile UUIDs supported by the remote device.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH
     * @param { string } deviceId - Indicates device ID. For example, "11:22:33:AA:BB:FF".
     * @returns { Promise<Array<ProfileUuids>> } Returns the promise object.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Invalid parameter.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 2900001 - Service stopped.
     * @throws { BusinessError } 2900003 - Bluetooth disabled.
     * @throws { BusinessError } 2900099 - Operation failed.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @crossplatform [since 13]
     * @since 12
     */
    function getRemoteProfileUuids(deviceId: string): Promise<Array<ProfileUuids>>;
    /**
     * Connects all allowed bluetooth profiles between the local and remote device.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH
     * @param { string } deviceId - Indicates device ID. For example, "11:22:33:AA:BB:FF".
     * @param { AsyncCallback<void> } callback - the callback result.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 2900001 - Service stopped.
     * @throws { BusinessError } 2900003 - Bluetooth disabled.
     * @throws { BusinessError } 2900099 - Operation failed.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 16
     */
    function connectAllowedProfiles(deviceId: string, callback: AsyncCallback<void>): void;
    /**
     * Connects all allowed bluetooth profiles between the local and remote device.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH
     * @param { string } deviceId - Indicates device ID. For example, "11:22:33:AA:BB:FF".
     * @returns { Promise<void> } Returns the promise object.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 2900001 - Service stopped.
     * @throws { BusinessError } 2900003 - Bluetooth disabled.
     * @throws { BusinessError } 2900099 - Operation failed.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 16
     */
    function connectAllowedProfiles(deviceId: string): Promise<void>;
    /**
     * Get remote device battery information.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH
     * @param { string } deviceId - Indicates device ID. For example, "11:22:33:AA:BB:FF".
     * @returns { Promise<BatteryInfo> } Returns battery info.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 2900001 - Service stopped.
     * @throws { BusinessError } 2900003 - Bluetooth disabled.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 12
     */
    function getRemoteDeviceBatteryInfo(deviceId: string): Promise<BatteryInfo>;
    /**
     * Disconnects all allowed bluetooth profiles between the local and remote device.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH
     * @param { string } deviceId - Indicates device ID. For example, "11:22:33:AA:BB:FF".
     * @returns { Promise<void> } Returns the promise object.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 801 - Capability not supported.
     *     Failed to call the API when the short-range chip is not inserted on 2in1 device.
     * @throws { BusinessError } 2900001 - Service stopped.
     * @throws { BusinessError } 2900003 - Bluetooth disabled.
     * @throws { BusinessError } 2900099 - Operation failed.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    function disconnectAllowedProfiles(deviceId: string): Promise<void>;
    /**
     * Modify remote device name.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH
     * @param { string } deviceId - Indicates device ID. For example, "11:22:33:AA:BB:FF".
     * @param { string } name - New device name. Max length is 64 bytes.
     * @returns { Promise<void> } Returns the promise object.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 2900001 - Service stopped.
     * @throws { BusinessError } 2900003 - Bluetooth disabled.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @atomicservice
     * @since 12
     */
    function setRemoteDeviceName(deviceId: string, name: string): Promise<void>;
    /**
     * Get latest connection time of device.
     *
     * @param { string } deviceId - Indicates device ID. For example, "11:22:33:AA:BB:FF".
     * @returns { Promise<number> } Returns latest connection time.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 2900001 - Service stopped.
     * @throws { BusinessError } 2900003 - Bluetooth disabled.
     * @throws { BusinessError } 2900099 - Operation failed.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 15
     */
    function getLastConnectionTime(deviceId: string): Promise<number>;
    /**
     * Obtain the virtual address of the corresponding device based on the hash value of the real address.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH
     * @param { HashAlgorithmType } algorithmType - Indicate the hash algorithm type.
     * @param { string } hashValue - Indicate the hash value of the device MAC address.
     * @returns { string } Returns the virtual mac address. For example, "11:22:33:AA:BB:FF".
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 801 - Capability not supported.
     *     Failed to call the API when the short-range chip is not inserted on 2in1 device.
     * @throws { BusinessError } 2900003 - Bluetooth disabled.
     * @throws { BusinessError } 2900015 - Parameter format mismatch with specification.
     * @throws { BusinessError } 2900016 - Device unpaired.
     * @throws { BusinessError } 2900099 - Internal system error. For example, IPC error.
     *     Detailed error messages can be used to assist in locating the problem.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 24
     */
    function getVirtualAddressByHash(algorithmType: HashAlgorithmType, hashValue: string): string;
    /**
     * Subscribe the event reported when a remote Bluetooth device is discovered.
     * On API 26.0.0 and above, if the application has ohos.permission.GET_BLUETOOTH_PEERS_MAC,
     * the type of the peer device address is real.
     * Otherwise, the type of the peer device address is virtual.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH [since 10 - 24]
     * @permission ohos.permission.ACCESS_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and
     *     ohos.permission.GET_BLUETOOTH_PEERS_MAC) [since 26.0.0]
     * @param { 'bluetoothDeviceFind' } type - Type of the discovering event to listen for.
     * @param { Callback<Array<string>> } callback - Callback used to listen for the discovering event.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed. [since 10 - 24]
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 2900099 - Operation failed.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @crossplatform [since 13]
     * @atomicservice [since 12]
     * @since 10
     */
    function on(type: 'bluetoothDeviceFind', callback: Callback<Array<string>>): void;
    /**
     * Unsubscribe the event reported when a remote Bluetooth device is discovered.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH
     * @param { 'bluetoothDeviceFind' } type - Type of the discovering event to listen for.
     * @param { Callback<Array<string>> } callback - Callback used to listen for the discovering event.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 2900099 - Operation failed.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @crossplatform [since 13]
     * @atomicservice [since 12]
     * @since 10
     */
    function off(type: 'bluetoothDeviceFind', callback?: Callback<Array<string>>): void;
    /**
     * Subscribe the event reported when a remote Bluetooth device is discovered.
     * On API 26.0.0 and above, if the application has ohos.permission.GET_BLUETOOTH_PEERS_MAC,
     * the type of the peer device address is real.
     * Otherwise, the type of the peer device address is virtual.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH [since 18 - 24]
     * @permission ohos.permission.ACCESS_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and
     *     ohos.permission.GET_BLUETOOTH_PEERS_MAC) [since 26.0.0]
     * @param { 'discoveryResult' } type - Type of the discovering event to listen for.
     * @param { Callback<Array<DiscoveryResult>> } callback - Callback used to listen for the discovering event.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed. [since 18 - 24]
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 2900099 - Operation failed.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 18
     */
    function on(type: 'discoveryResult', callback: Callback<Array<DiscoveryResult>>): void;
    /**
     * Unsubscribe the event reported when a remote Bluetooth device is discovered.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH
     * @param { 'discoveryResult' } type - Type of the discovering event to listen for.
     * @param { Callback<Array<DiscoveryResult>> } callback - Callback used to listen for the discovering event.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 2900099 - Operation failed.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 18
     */
    function off(type: 'discoveryResult', callback?: Callback<Array<DiscoveryResult>>): void;
    /**
     * Subscribe the event reported when a remote Bluetooth device is bonded.
     * On API 26.0.0 and above, if the application has ohos.permission.GET_BLUETOOTH_PEERS_MAC,
     * the type of the peer device address is real.
     * Otherwise, the type of the peer device address is virtual.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH [since 10 - 24]
     * @permission ohos.permission.ACCESS_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and
     *     ohos.permission.GET_BLUETOOTH_PEERS_MAC) [since 26.0.0]
     * @param { 'bondStateChange' } type - Type of the bond state event to listen for.
     * @param { Callback<BondStateParam> } callback - Callback used to listen for the bond state event.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed. [since 10 - 24]
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 2900099 - Operation failed.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @crossplatform [since 13]
     * @since 10
     */
    function on(type: 'bondStateChange', callback: Callback<BondStateParam>): void;
    /**
     * Unsubscribe the event reported when a remote Bluetooth device is bonded.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH
     * @param { 'bondStateChange' } type - Type of the bond state event to listen for.
     * @param { Callback<BondStateParam> } callback - Callback used to listen for the bond state event.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 2900099 - Operation failed.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @crossplatform [since 13]
     * @since 10
     */
    function off(type: 'bondStateChange', callback?: Callback<BondStateParam>): void;
    /**
     * Subscribe the event of a pairing request from a remote Bluetooth device.
     * On API 26.0.0 and above, if the application has ohos.permission.GET_BLUETOOTH_PEERS_MAC,
     * the type of the peer device address is real.
     * Otherwise, the type of the peer device address is virtual.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH [since 10 - 24]
     * @permission ohos.permission.ACCESS_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and
     *     ohos.permission.GET_BLUETOOTH_PEERS_MAC) [since 26.0.0]
     * @param { 'pinRequired' } type - Type of the pairing request event to listen for.
     * @param { Callback<PinRequiredParam> } callback - Callback used to listen for the pairing request event.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed. [since 10 - 24]
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 2900099 - Operation failed.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 10
     */
    function on(type: 'pinRequired', callback: Callback<PinRequiredParam>): void;
    /**
     * Unsubscribe the event of a pairing request from a remote Bluetooth device.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH
     * @param { 'pinRequired' } type - Type of the pairing request event to listen for.
     * @param { Callback<PinRequiredParam> } callback - Callback used to listen for the pairing request event.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 2900099 - Operation failed.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 10
     */
    function off(type: 'pinRequired', callback?: Callback<PinRequiredParam>): void;
    /**
     * Subscribe the event of battery state changed from a remote device.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH
     * @param { 'batteryChange' } type - Type of the battery event to listen for.
     * @param { Callback<BatteryInfo> } callback - Callback used to listen.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 2900099 - Operation failed.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 12
     */
    function on(type: 'batteryChange', callback: Callback<BatteryInfo>): void;
    /**
     * Unsubscribe the event of battery state changed from a remote device.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH
     * @param { 'batteryChange' } type - Type of the battery event to listen for.
     * @param { Callback<BatteryInfo> } callback - Callback used to listen.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 2900099 - Operation failed.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 12
     */
    function off(type: 'batteryChange', callback?: Callback<BatteryInfo>): void;
    /**
     * Subscribe to an event indicating that the scanning mode of the local device has changed.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH
     * @param { Callback<ScanMode> } callback - Callback used to listen.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 2900099 - Operation failed.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 23
     */
    function onScanModeChange(callback: Callback<ScanMode>): void;
    /**
     * Unsubscribe to an event indicating that the scanning mode of the local device has changed.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH
     * @param { Callback<ScanMode> } [callback] - Callback used to listen.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 2900099 - Operation failed.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 23
     */
    function offScanModeChange(callback?: Callback<ScanMode>): void;
    /**
     * Subscribe the event of acl state changed from a remote device.
     * If the application has ohos.permission.GET_BLUETOOTH_PEERS_MAC, the type of the peer device address is real.
     * Otherwise, the type of the peer device address is virtual.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and
     *     ohos.permission.GET_BLUETOOTH_PEERS_MAC)
     * @param { Callback<AclStateResult> } callback - Callback used to listen.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 801 - Capability not supported.
     *     Failed to call the API when the short-range chip is not inserted on 2in1 device.
     * @throws { BusinessError } 2900099 - Internal system error. For example, IPC error.
     *     Detailed error messages can be used to assist in locating the problem.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    function onAclStateChange(callback: Callback<AclStateResult>): void;
    /**
     * Unsubscribe the event of acl state changed from a remote device.
     * If the application has ohos.permission.GET_BLUETOOTH_PEERS_MAC, the type of the peer device address is real.
     * Otherwise, the type of the peer device address is virtual.
     *
     * @permission ohos.permission.ACCESS_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and
     *     ohos.permission.GET_BLUETOOTH_PEERS_MAC)
     * @param { Callback<AclStateResult> } [callback] - Callback used to listen.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 801 - Capability not supported.
     *     Failed to call the API when the short-range chip is not inserted on 2in1 device.
     * @throws { BusinessError } 2900099 - Internal system error. For example, IPC error.
     *     Detailed error messages can be used to assist in locating the problem.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    function offAclStateChange(callback?: Callback<AclStateResult>): void;
    /**
     * Describes the class of a bluetooth device.
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @crossplatform [since 13]
     * @since 10
     */
    interface BondStateParam {
        /**
         * Address of a Bluetooth device.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @crossplatform [since 13]
         * @since 10
         */
        deviceId: string;
        /**
         * Profile connection state of the device.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @crossplatform [since 13]
         * @since 10
         */
        state: BondState;
        /**
         * Cause of unbond.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @crossplatform [since 13]
         * @since 12
         */
        cause: UnbondCause;
        /**
         * Cause message of unbond.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        causeMessage?: string;
    }
    /**
     * Describes the bond key param.
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 10
     */
    interface PinRequiredParam {
        /**
         * ID of the device to pair.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 10
         */
        deviceId: string;
        /**
         * Key for the device pairing.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 10
         */
        pinCode: string;
    }
    /**
     * Describes the class of a bluetooth device.
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @crossplatform [since 13]
     * @since 10
     */
    interface DeviceClass {
        /**
         * Major classes of Bluetooth devices.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @crossplatform [since 13]
         * @since 10
         */
        majorClass: MajorClass;
        /**
         * Major and minor classes of Bluetooth devices.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @crossplatform [since 13]
         * @since 10
         */
        majorMinorClass: MajorMinorClass;
        /**
         * Class of the device.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @crossplatform [since 13]
         * @since 10
         */
        classOfDevice: number;
    }
    /**
     * Enum for the transport of a remote device
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 10
     */
    enum BluetoothTransport {
        /**
         * The value of bluetooth transport BR/EDR.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 10
         */
        TRANSPORT_BR_EDR = 0,
        /**
         * The value of bluetooth transport LE.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 10
         */
        TRANSPORT_LE = 1,
        /**
         * The value of bluetooth transport DUAL.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 20
         */
        TRANSPORT_DUAL = 2,
        /**
         * The unknown bluetooth transport.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 20
         */
        TRANSPORT_UNKNOWN = 3
    }
    /**
     * The enum of BR scan mode.
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @crossplatform [since 13]
     * @since 10
     */
    enum ScanMode {
        /**
         * Indicates the scan mode is none
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @crossplatform [since 13]
         * @since 10
         */
        SCAN_MODE_NONE = 0,
        /**
         * Indicates the scan mode is connectable
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @crossplatform [since 13]
         * @since 10
         */
        SCAN_MODE_CONNECTABLE = 1,
        /**
         * Indicates the scan mode is general discoverable
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 10
         */
        SCAN_MODE_GENERAL_DISCOVERABLE = 2,
        /**
         * Indicates the scan mode is limited discoverable
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 10
         */
        SCAN_MODE_LIMITED_DISCOVERABLE = 3,
        /**
         * Indicates the scan mode is connectable and general discoverable
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @crossplatform [since 13]
         * @since 10
         */
        SCAN_MODE_CONNECTABLE_GENERAL_DISCOVERABLE = 4,
        /**
         * Indicates the scan mode is connectable and limited discoverable
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 10
         */
        SCAN_MODE_CONNECTABLE_LIMITED_DISCOVERABLE = 5
    }
    /**
     * The enum of bond state.
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @crossplatform [since 13]
     * @atomicservice [since 12]
     * @since 10
     */
    enum BondState {
        /**
         * Indicate the bond state is invalid
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @crossplatform [since 13]
         * @atomicservice [since 12]
         * @since 10
         */
        BOND_STATE_INVALID = 0,
        /**
         * Indicate the bond state is bonding
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @crossplatform [since 13]
         * @atomicservice [since 12]
         * @since 10
         */
        BOND_STATE_BONDING = 1,
        /**
         * Indicate the bond state is bonded
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @crossplatform [since 13]
         * @atomicservice [since 12]
         * @since 10
         */
        BOND_STATE_BONDED = 2
    }
    /**
     * Describes the contents of the discovery results
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 18
     */
    interface DiscoveryResult {
        /**
         * Identify of the discovery device
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 18
         */
        deviceId: string;
        /**
         * RSSI of the remote device
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 18
         */
        rssi: number;
        /**
         * The local name of the device
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 18
         */
        deviceName: string;
        /**
         * The class of the device
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 18
         */
        deviceClass: DeviceClass;
    }
    /**
     * Describes the contents of the battery information.
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 12
     */
    interface BatteryInfo {
        /**
         * Electricity value of the general device. {@code -1} means no power information.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 12
         */
        batteryLevel: number;
        /**
         * Electricity value of the left ear. {@code -1} means no power information.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 12
         */
        leftEarBatteryLevel: number;
        /**
         * The charge state of the left ear.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 12
         */
        leftEarChargeState: DeviceChargeState;
        /**
         * Electricity value of the right ear. {@code -1} means no power information.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 12
         */
        rightEarBatteryLevel: number;
        /**
         * The charge state of the right ear.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 12
         */
        rightEarChargeState: DeviceChargeState;
        /**
         * Electricity value of the box. {@code -1} means no power information.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 12
         */
        boxBatteryLevel: number;
        /**
         * The charge state of the box.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 12
         */
        boxChargeState: DeviceChargeState;
    }
    /**
     * Enum for the charge state.
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 12
     */
    enum DeviceChargeState {
        /**
         * Not support super charge, and not charged.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 12
         */
        DEVICE_NORMAL_CHARGE_NOT_CHARGED = 0,
        /**
         * Not support super charge, and in charging.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 12
         */
        DEVICE_NORMAL_CHARGE_IN_CHARGING = 1,
        /**
         * Support super charge, and not charged.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 12
         */
        DEVICE_SUPER_CHARGE_NOT_CHARGED = 2,
        /**
         * Support super charge, and in charging.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 12
         */
        DEVICE_SUPER_CHARGE_IN_CHARGING = 3
    }
    /**
     * Enum for cause of unbond.
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @crossplatform [since 13]
     * @since 12
     */
    enum UnbondCause {
        /**
         * User proactively removed device.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @crossplatform [since 13]
         * @since 12
         */
        USER_REMOVED = 0,
        /**
         * Remote device shut down.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 12
         */
        REMOTE_DEVICE_DOWN = 1,
        /**
         * Wrong PIN code.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 12
         */
        AUTH_FAILURE = 2,
        /**
         * Remote device rejected.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 12
         */
        AUTH_REJECTED = 3,
        /**
         * Internal error.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 12
         */
        INTERNAL_ERROR = 4
    }
    /**
     * Enum for the hash algorithm type.
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 24
     */
    enum HashAlgorithmType {
        /**
         * SHA256 hash algorithm
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 24
         */
        HASH_ALGORITHM_SHA256 = 0
    }
    /**
     * Acl state change result.
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    interface AclStateResult {
        /**
         * The virtual address of a Bluetooth device. For example, "11:22:33:AA:BB:FF".
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        deviceId: string;
        /**
         * Acl state of the device.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        state: AclState;
    }
    /**
     * The enum of acl state.
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    export enum AclState {
        /**
         * acl is connected
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        STATE_CONNECTED = 0,
        /**
         * acl is disconnected
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        STATE_DISCONNECTED = 1
    }
}
export default connection;

```
