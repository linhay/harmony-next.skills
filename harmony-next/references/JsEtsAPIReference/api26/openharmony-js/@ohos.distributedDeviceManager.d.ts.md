# @ohos.distributedDeviceManager.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2023-2025 Huawei Device Co., Ltd.
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
 * @kit DistributedServiceKit
 */
import type { AsyncCallback, Callback } from './@ohos.base';
/**
 * The **distributedDeviceManager** module provides APIs for distributed device management.
 * Applications can call the APIs to:
 *
 * - Subscribe to or unsubscribe from device state changes.
 * - Discover devices nearby.
 * - Authenticate or deauthenticate a device.
 * - Query the trusted device list.
 * - Query local device information, including the device name, type, and ID.
 *
 * @syscap SystemCapability.DistributedHardware.DeviceManager
 * @since 10
 */
declare namespace distributedDeviceManager {
    /**
     * Represents the basic information about a distributed device.
     *
     * @syscap SystemCapability.DistributedHardware.DeviceManager
     * @since 10
     */
    interface DeviceBasicInfo {
        /**
         * Device ID. The value is the result of obfuscating the udid-hash (hash value of the UDID), **appid**, and salt
         * using the SHA-256 algorithm.
         *
         * @syscap SystemCapability.DistributedHardware.DeviceManager
         * @since 10
         */
        deviceId: string;
        /**
         * Device name.
         *
         * @syscap SystemCapability.DistributedHardware.DeviceManager
         * @since 10
         */
        deviceName: string;
        /**
         * [Device type]{@link distributedDeviceManager.DeviceManager.getDeviceType}.
         *
         * @syscap SystemCapability.DistributedHardware.DeviceManager
         * @since 10
         */
        deviceType: string;
        /**
         * Network ID of the device.
         *
         * @syscap SystemCapability.DistributedHardware.DeviceManager
         * @since 10
         */
        networkId?: string;
    }
    /**
     * Enumerates the device states.
     *
     * @syscap SystemCapability.DistributedHardware.DeviceManager
     * @since 10
     */
    enum DeviceStateChange {
        /**
         * The device state is unknown after the device goes online. Before the device state changes to available,
         * distributed services cannot be used.
         *
         * @syscap SystemCapability.DistributedHardware.DeviceManager
         * @since 10
         */
        UNKNOWN = 0,
        /**
         * The information between devices has been synchronized in the Distributed Data Service (DDS) module, and the
         * device is ready for running distributed services.
         *
         * @syscap SystemCapability.DistributedHardware.DeviceManager
         * @since 10
         */
        AVAILABLE = 1,
        /**
         * The device goes offline, and the device state is unknown.
         *
         * @syscap SystemCapability.DistributedHardware.DeviceManager
         * @since 10
         */
        UNAVAILABLE = 2
    }
    /**
     * Creates a **DeviceManager** instance. The **DeviceManager** instance is the entry for invoking the APIs for
     * distributed device management. It can be used to obtain information about trusted devices and local devices.
     *
     * @param { string } bundleName - Bundle name of the application. The value is a string of 1 to 255 characters.
     * @returns { DeviceManager } **DeviceManager** instance created.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter type;
     *     3. Parameter verification failed.
     * @syscap SystemCapability.DistributedHardware.DeviceManager
     * @since 10
     */
    function createDeviceManager(bundleName: string): DeviceManager;
    /**
     * Releases a **DeviceManager** instance that is no longer used.
     *
     * @param { DeviceManager } deviceManager - **DeviceManager** instance to release.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types;
     *     3. Parameter verification failed.
     * @throws { BusinessError } 11600101 - Failed to execute the function.
     * @syscap SystemCapability.DistributedHardware.DeviceManager
     * @since 10
     */
    function releaseDeviceManager(deviceManager: DeviceManager): void;
    /**
     * Provides APIs to obtain information about trusted devices and local devices. Before calling any API in
     * **DeviceManager**, you must use **createDeviceManager** to create a **DeviceManager** instance, for example,
     * **dmInstance**.
     *
     * @syscap SystemCapability.DistributedHardware.DeviceManager
     * @since 10
     */
    interface DeviceManager {
        /**
         * Obtains all trusted devices synchronously.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @returns { Array<DeviceBasicInfo> } List of trusted devices obtained.
         * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
         *     required to call the API.
         * @throws { BusinessError } 11600101 - Failed to execute the function.
         * @syscap SystemCapability.DistributedHardware.DeviceManager
         * @since 10
         */
        getAvailableDeviceListSync(): Array<DeviceBasicInfo>;
        /**
         * Obtains all trusted devices. This API uses an asynchronous callback to return the result.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { AsyncCallback<Array<DeviceBasicInfo>> } callback - Callback used to return the list of trusted devices.
         * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
         *     required to call the API.
         * @throws { BusinessError } 11600101 - Failed to execute the function.
         * @syscap SystemCapability.DistributedHardware.DeviceManager
         * @since 10
         */
        getAvailableDeviceList(callback: AsyncCallback<Array<DeviceBasicInfo>>): void;
        /**
         * Obtains all trusted devices. This API uses a promise to return the result.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @returns { Promise<Array<DeviceBasicInfo>> } Promise used to return the result.
         * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
         *     required to call the API.
         * @throws { BusinessError } 11600101 - Failed to execute the function.
         * @syscap SystemCapability.DistributedHardware.DeviceManager
         * @since 10
         */
        getAvailableDeviceList(): Promise<Array<DeviceBasicInfo>>;
        /**
         * Obtains the network ID of the local device.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @returns { string } Network ID of the local device obtained.
         * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
         *     required to call the API.
         * @throws { BusinessError } 11600101 - Failed to execute the function.
         * @syscap SystemCapability.DistributedHardware.DeviceManager
         * @since 10
         */
        getLocalDeviceNetworkId(): string;
        /**
         * Obtains the local device name.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @returns { string } Name of the local device obtained.
         * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
         *     required to call the API.
         * @throws { BusinessError } 11600101 - Failed to execute the function.
         * @syscap SystemCapability.DistributedHardware.DeviceManager
         * @since 10
         */
        getLocalDeviceName(): string;
        /**
         * Obtains the local device type.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @returns { number } <!--RP1-->Local device type obtained.<!--RP1End-->
         * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
         *     required to call the API.
         * @throws { BusinessError } 11600101 - Failed to execute the function.
         * @syscap SystemCapability.DistributedHardware.DeviceManager
         * @since 10
         */
        getLocalDeviceType(): number;
        /**
         * Obtains the local device ID. The value is the result of obfuscating the udid-hash (hash value of the UDID),
         * **appid**, and salt using the SHA-256 algorithm.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @returns { string } Local device ID obtained.
         * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
         *     required to call the API.
         * @throws { BusinessError } 11600101 - Failed to execute the function.
         * @syscap SystemCapability.DistributedHardware.DeviceManager
         * @since 10
         */
        getLocalDeviceId(): string;
        /**
         * Obtains the device name based on the network ID of the specified device.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { string } networkId - Network ID of the device. The value is a string of 1 to 255 characters.
         * @returns { string } Device name obtained.
         * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
         *     required to call the API.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameter type;
         *     3. Parameter verification failed;
         *     4. The size of specified networkId is greater than 255.
         * @throws { BusinessError } 11600101 - Failed to execute the function.
         * @syscap SystemCapability.DistributedHardware.DeviceManager
         * @since 10
         */
        getDeviceName(networkId: string): string;
        /**
         * Obtains the device type based on the network ID of the specified device.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { string } networkId - Network ID of the device. The value is a string of 1 to 255 characters.
         * @returns { number } <!--RP2-->Device type obtained.<!--RP2End-->
         * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
         *     required to call the API.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameter type;
         *     3. Parameter verification failed;
         *     4. The size of specified networkId is greater than 255.
         * @throws { BusinessError } 11600101 - Failed to execute the function.
         * @syscap SystemCapability.DistributedHardware.DeviceManager
         * @since 10
         */
        getDeviceType(networkId: string): number;
        /**
         * Starts to discover devices nearby. The discovery process takes 2 minutes. A maximum of 99 devices can be
         * discovered. In Wi-Fi scenarios, only the devices in the same LAN can be discovered.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { object } discoverParam - Identifier of the device to discover. It specifies the type of the target to
         *     discover.
         *     <br>**discoverTargetType**: The default discovery target is device. The value is **1**.
         * @param { object } filterOptions - Options for filtering the devices to discover. The default value is
         *     **undefined**, which means to discover offline devices. The options include the following:
         *     <br>- **availableStatus(0-1)**: status of the device to discover.
         *     The value **0** means the device is untrusted.
         *     <br>- **0**: The device is offline. The client needs to call **bindTarget** to bind the device.
         *     <br>- **1**: The device is online and can be connected.
         *     <br>**discoverDistance(0-100)**: distance of the device to discover, in cm.
         *     This parameter is not used in Wi-Fi scenarios.
         *     <br>**authenticationStatus(0-1)**: authentication status of the device to discover.
         *     <br>- **0**: The device is not authenticated.
         *     <br>The value **1** means the device has been authenticated.
         *     <br>- **authorizationType(0-2)**: authorization type of the device to discover.
         *     <br>- **0**: The device is authenticated by a temporarily agreed session key.
         *     <br>- **1**: The device is authenticated by a key of the same account.
         *     <br>- **2**: The device is authenticated by a credential key of different accounts.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameter type;
         *     3. Parameter verification failed.
         * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
         *     required to call the API.
         * @throws { BusinessError } 11600104 - Discovery unavailable.
         * @throws { BusinessError } 11600101 - Failed to execute the function.
         * @syscap SystemCapability.DistributedHardware.DeviceManager
         * @since 10
         */
        startDiscovering(discoverParam: {
            [key: string]: Object;
        }, filterOptions?: {
            [key: string]: Object;
        }): void;
        /**
         * Stops device discovery.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
         *     required to call the API.
         * @throws { BusinessError } 11600101 - Failed to execute the function.
         * @syscap SystemCapability.DistributedHardware.DeviceManager
         * @since 10
         */
        stopDiscovering(): void;
        /**
         * Binds a device. This API uses an asynchronous callback to return the result.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { string } deviceId - Device ID. The value is a string of 1 to 255 characters.
         * @param { object } bindParam - Authentication parameters.
         *     You can determine the key-value pair to be passed in. By default, the following keys are carried:
         *     <br>**bindType**: binding type, which is mandatory.
         *     <br>The value **1** means PIN authentication.
         *     <br>**targetPkgName**: bundle name of the target to bind.
         *     <br>**appName**: application that attempts to bind the target.
         *     <br>**appOperation**: reason for the application to bind the target.
         *     <br>**customDescription**: detailed description of the operation.
         * @param { AsyncCallback<{deviceId: string;}> } callback - Callback used to return the authentication result.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameter type;
         *     3. Parameter verification failed;
         *     4. The size of specified deviceId is greater than 255.
         * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
         *     required to call the API.
         * @throws { BusinessError } 11600101 - Failed to execute the function.
         * @throws { BusinessError } 11600103 - Authentication unavailable.
         * @syscap SystemCapability.DistributedHardware.DeviceManager
         * @since 10
         */
        bindTarget(deviceId: string, bindParam: {
            [key: string]: Object;
        }, callback: AsyncCallback<{
            deviceId: string;
        }>): void;
        /**
         * Unbinds a device.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { string } deviceId - Device ID. The value is a string of 1 to 255 characters.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameter type;
         *     3. Parameter verification failed;
         *     4. The size of specified deviceId is greater than 255.
         * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
         *     required to call the API.
         * @throws { BusinessError } 11600101 - Failed to execute the function.
         * @syscap SystemCapability.DistributedHardware.DeviceManager
         * @since 10
         */
        unbindTarget(deviceId: string): void;
        /**
         * Subscribes to the device state changes. The application (identified by the bundle name) will be notified when the
         * device state changes. This API uses an asynchronous callback to return the result.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { 'deviceStateChange' } type - Event type. The value **'deviceStateChange'** indicates device state
         *     changes.
         * @param { Callback<{ action: DeviceStateChange; device: DeviceBasicInfo; }> } callback - Callback used to return
         *     the device information and state.
         * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
         *     required to call the API.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameter type;
         *     3. Parameter verification failed;
         *     4. The size of specified type is greater than 255.
         * @syscap SystemCapability.DistributedHardware.DeviceManager
         * @since 10
         */
        on(type: 'deviceStateChange', callback: Callback<{
            action: DeviceStateChange;
            device: DeviceBasicInfo;
        }>): void;
        /**
         * Unsubscribes from the device state changes. This API uses an asynchronous callback to return the result.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { 'deviceStateChange' } type - Event type. The value **'deviceStateChange'** indicates device state
         *     changes.
         * @param { Callback<{ action: DeviceStateChange; device: DeviceBasicInfo; }> } callback - Callback to unregister.
         * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
         *     required to call the API.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameter type;
         *     3. Parameter verification failed;
         *     4. The size of specified type is greater than 255.
         * @syscap SystemCapability.DistributedHardware.DeviceManager
         * @since 10
         */
        off(type: 'deviceStateChange', callback?: Callback<{
            action: DeviceStateChange;
            device: DeviceBasicInfo;
        }>): void;
        /**
         * Subscribes to the **'discoverSuccess'** event. The application will be notified when a device is successfully
         * discovered. This API uses an asynchronous callback to return the result.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { 'discoverSuccess' } type - Event type, which has a fixed value of **'discoverSuccess'**.
         * @param { Callback<{ device: DeviceBasicInfo; }> } callback - Callback invoked when a device is successfully
         *     discovered.
         * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
         *     required to call the API.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameter type;
         *     3. Parameter verification failed;
         *     4. The size of specified type is greater than 255.
         * @syscap SystemCapability.DistributedHardware.DeviceManager
         * @since 10
         */
        on(type: 'discoverSuccess', callback: Callback<{
            device: DeviceBasicInfo;
        }>): void;
        /**
         * Unsubscribes from the **'discoverSuccess'** event. This API uses an asynchronous callback to return the result.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { 'discoverSuccess' } type - Event type, which has a fixed value of **'discoverSuccess'**.
         * @param { Callback<{ device: DeviceBasicInfo; }> } callback - Callback to unregister.
         * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
         *     required to call the API.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameter type;
         *     3. Parameter verification failed;
         *     4. The size of specified type is greater than 255.
         * @syscap SystemCapability.DistributedHardware.DeviceManager
         * @since 10
         */
        off(type: 'discoverSuccess', callback?: Callback<{
            device: DeviceBasicInfo;
        }>): void;
        /**
         * Subscribes to device name changes. The application will be notified when the name of a device is changed. This
         * API uses an asynchronous callback to return the result.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { 'deviceNameChange' } type - Event type, which has a fixed value of **deviceNameChange**.
         * @param { Callback<{ deviceName: string; }> } callback - Callback used to return the device name change.
         * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
         *     required to call the API.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameter type;
         *     3. Parameter verification failed;
         *     4. The size of specified type is greater than 255.
         * @syscap SystemCapability.DistributedHardware.DeviceManager
         * @since 10
         */
        on(type: 'deviceNameChange', callback: Callback<{
            deviceName: string;
        }>): void;
        /**
         * Unsubscribes from the device name changes. This API uses an asynchronous callback to return the result.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { 'deviceNameChange' } type - Event type, which has a fixed value of **deviceNameChange**.
         * @param { Callback<{ deviceName: string; }> } callback - Callback to unregister.
         * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
         *     required to call the API.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameter type;
         *     3. Parameter verification failed;
         *     4. The size of specified type is greater than 255.
         * @syscap SystemCapability.DistributedHardware.DeviceManager
         * @since 10
         */
        off(type: 'deviceNameChange', callback?: Callback<{
            deviceName: string;
        }>): void;
        /**
         * Subscribes to the **'discoverFailure'** event. The application will be notified when a device fails to be
         * discovered. This API uses an asynchronous callback to return the result.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { 'discoverFailure' } type - Event type, which has a fixed value of **'discoverFailure'**.
         * @param { Callback<{ reason: number}> } callback - Callback invoked when a device fails to be discovered.
         * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
         *     required to call the API.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameter type;
         *     3. Parameter verification failed;
         *     4. The size of specified type is greater than 255.
         * @syscap SystemCapability.DistributedHardware.DeviceManager
         * @since 10
         */
        on(type: 'discoverFailure', callback: Callback<{
            reason: number;
        }>): void;
        /**
         * Unsubscribes from the **'discoverFailure'** event. This API uses an asynchronous callback to return the result.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { 'discoverFailure' } type - Event type, which has a fixed value of **'discoverFailure'**.
         * @param { Callback<{ reason: number}> } callback - Callback to unregister.
         * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
         *     required to call the API.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameter type;
         *     3. Parameter verification failed;
         *     4. The size of specified type is greater than 255.
         * @syscap SystemCapability.DistributedHardware.DeviceManager
         * @since 10
         */
        off(type: 'discoverFailure', callback?: Callback<{
            reason: number;
        }>): void;
        /**
         * Subscribes to the dead events of the **DeviceManager** service. The application will be notified when the
         * **DeviceManager** service is terminated unexpectedly. This API uses an asynchronous callback to return the
         * result.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { 'serviceDie' } type - Event type, which has a fixed value of **'serviceDie'**.
         * @param { Callback<{}> } callback - Callback invoked when the **DeviceManager** service is terminated
         *     unexpectedly.
         * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
         *     required to call the API.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameter type;
         *     3. Parameter verification failed;
         *     4. The size of specified type is greater than 255.
         * @syscap SystemCapability.DistributedHardware.DeviceManager
         * @since 10
         */
        on(type: 'serviceDie', callback?: Callback<{}>): void;
        /**
         * Unsubscribes from the dead events of the **DeviceManager** service. This API uses an asynchronous callback to
         * return the result.
         *
         * @permission ohos.permission.DISTRIBUTED_DATASYNC
         * @param { 'serviceDie' } type - Event type, which has a fixed value of **'serviceDie'**.
         * @param { Callback<{}> } callback - Callback to unregister.
         * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
         *     required to call the API.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameter type;
         *     3. Parameter verification failed;
         *     4. The size of specified type is greater than 255.
         * @syscap SystemCapability.DistributedHardware.DeviceManager
         * @since 10
         */
        off(type: 'serviceDie', callback?: Callback<{}>): void;
    }
}
export default distributedDeviceManager;

```
