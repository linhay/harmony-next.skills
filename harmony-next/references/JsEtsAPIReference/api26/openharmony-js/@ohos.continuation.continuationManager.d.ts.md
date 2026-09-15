# @ohos.continuation.continuationManager.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022-2026 Huawei Device Co., Ltd.
 * Licensed under the Apache License, Version 2.0 (the "License"),
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
 * @kit AbilityKit
 */
import { Callback } from './@ohos.base';
import { AsyncCallback } from './@ohos.base';
import type { ContinuationResult as _ContinuationResult } from './continuation/continuationResult';
import type { ContinuationExtraParams as _ContinuationExtraParams } from './continuation/continuationExtraParams';
/**
 * The continuationManager module provides the continuation/collaboration management entry. You can use the APIs of this
 *  module to connect to and cancel the continuation/collaboration management service, subscribe to and unsubscribe from
 *  device connection events, start the device selection module, and update the device connection state.
 *
 *
 * @syscap SystemCapability.Ability.DistributedAbilityManager
 * @stagemodelonly
 * @atomicservice [since 11]
 * @since 8
 * @deprecated since 22
 * @useinstead @ohos.distributedDeviceManager:distributedDeviceManager
 */
declare namespace continuationManager {
    /**
     * Subscribes to device connection events. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.DISTRIBUTED_DATASYNC
     * @param { 'deviceSelected' } type - Event type. The value is fixed at **deviceSelected**.
     * @param { number } token - Token obtained after the registration of the continuation management service.
     * @param { Callback<Array<ContinuationResult>> } callback - Callback invoked when a device is selected from the device
     *     list provided by the device selection module. This callback returns the device ID, type, and name.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 16600001 - The system ability works abnormally.
     * @throws { BusinessError } 16600002 - The specified token or callback is not registered.
     * @throws { BusinessError } 16600004 - The specified callback has been registered.
     * @syscap SystemCapability.Ability.DistributedAbilityManager
     * @stagemodelonly
     * @atomicservice [since 11]
     * @since 9
     * @deprecated since 22
     * @useinstead @ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.on(type: 'deviceStateChange', callback: Callback<{ action: DeviceStateChange; device: DeviceBasicInfo; }>)
     */
    function on(type: 'deviceSelected', token: number, callback: Callback<Array<ContinuationResult>>): void;
    /**
     * Unsubscribes from device connection events.
     *
     * @permission ohos.permission.DISTRIBUTED_DATASYNC
     * @param { 'deviceSelected' } type - Event type. The value is fixed at **deviceSelected**.
     * @param { number } token - Token obtained after the registration of the continuation management service.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 16600001 - The system ability works abnormally.
     * @throws { BusinessError } 16600002 - The specified token or callback is not registered.
     * @throws { BusinessError } 16600004 - The specified callback has been registered.
     * @syscap SystemCapability.Ability.DistributedAbilityManager
     * @stagemodelonly
     * @atomicservice [since 11]
     * @since 9
     * @deprecated since 22
     * @useinstead @ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.off(type: 'deviceStateChange', callback?: Callback<{ action: DeviceStateChange; device: DeviceBasicInfo; }>)
     */
    function off(type: 'deviceSelected', token: number): void;
    /**
     * Subscribes to device disconnection events. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.DISTRIBUTED_DATASYNC
     * @param { 'deviceUnselected' } type - Event type. The value is fixed at **deviceUnselected**.
     * @param { number } token - Token obtained after the registration of the continuation management service.
     * @param { Callback<Array<ContinuationResult>> } callback - Callback invoked when a device is unselected from the device
     *     list provided by the device selection module. This callback returns the device ID, type, and name.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 16600001 - The system ability works abnormally.
     * @throws { BusinessError } 16600002 - The specified token or callback is not registered.
     * @throws { BusinessError } 16600004 - The specified callback has been registered.
     * @syscap SystemCapability.Ability.DistributedAbilityManager
     * @stagemodelonly
     * @atomicservice [since 11]
     * @since 9
     * @deprecated since 22
     * @useinstead @ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.on(type: 'deviceStateChange', callback: Callback<{ action: DeviceStateChange; device: DeviceBasicInfo; }>)
     */
    function on(type: 'deviceUnselected', token: number, callback: Callback<Array<ContinuationResult>>): void;
    /**
     * Unsubscribes from device disconnection events.
     *
     * @permission ohos.permission.DISTRIBUTED_DATASYNC
     * @param { 'deviceUnselected' } type - Event type. The value is fixed at **deviceUnselected**.
     * @param { number } token - Token obtained after the registration of the continuation management service.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 16600001 - The system ability works abnormally.
     * @throws { BusinessError } 16600002 - The specified token or callback is not registered.
     * @throws { BusinessError } 16600004 - The specified callback has been registered.
     * @syscap SystemCapability.Ability.DistributedAbilityManager
     * @stagemodelonly
     * @atomicservice [since 11]
     * @since 9
     * @deprecated since 22
     * @useinstead @ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.off(type: 'deviceStateChange', callback?: Callback<{ action: DeviceStateChange; device: DeviceBasicInfo; }>)
     */
    function off(type: 'deviceUnselected', token: number): void;
    /**
     * Subscribes to device connection events. This API uses an asynchronous callback to return the result.
     *
     * @param { 'deviceConnect' } type - Event type. The value is fixed at **deviceConnect**.
     * @param { Callback<ContinuationResult> } callback - Callback invoked when a device is selected from the device list
     *     provided by the device selection module. This callback returns the device ID, type, and name.
     * @syscap SystemCapability.Ability.DistributedAbilityManager
     * @stagemodelonly
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.on(type: 'deviceStateChange', callback: Callback<{ action: DeviceStateChange; device: DeviceBasicInfo; }>)
     */
    function on(type: 'deviceConnect', callback: Callback<ContinuationResult>): void;
    /**
     * Unsubscribes from device connection events. This API uses an asynchronous callback to return the result.
     * @param { 'deviceConnect' } type - Event type. The value is fixed at **deviceConnect**.
     * @param { Callback<ContinuationResult> } [callback] - Callback invoked when a device is selected from the device list
     *     provided by the device selection module. This callback returns the device ID, type, and name.
     * @syscap SystemCapability.Ability.DistributedAbilityManager
     * @stagemodelonly
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.off(type: 'deviceStateChange', callback?: Callback<{ action: DeviceStateChange; device: DeviceBasicInfo; }>)
     */
    function off(type: 'deviceConnect', callback?: Callback<ContinuationResult>): void;
    /**
     * Subscribes to device disconnection events. This API uses an asynchronous callback to return the result.
     *
     * @param { 'deviceDisconnect' } type - Event type. The value is fixed at **deviceDisconnect**.
     * @param { Callback<string> } callback - Callback invoked when a device is unselected from the device list provided by the
     *     device selection module. This callback returns the device ID.
     * @syscap SystemCapability.Ability.DistributedAbilityManager
     * @stagemodelonly
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.on(type: 'deviceStateChange', callback: Callback<{ action: DeviceStateChange; device: DeviceBasicInfo; }>)
     */
    function on(type: 'deviceDisconnect', callback: Callback<string>): void;
    /**
     * Unsubscribes from device disconnection events. This API uses an asynchronous callback to return the result.
     *
     * @param { 'deviceDisconnect' } type - Event type. The value is fixed at **deviceDisconnect**.
     * @param { Callback<string> } [callback] - Callback invoked when a device is unselected from the device list provided by
     *     the device selection module. This callback returns the device ID.
     * @syscap SystemCapability.Ability.DistributedAbilityManager
     * @stagemodelonly
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.off(type: 'deviceStateChange', callback?: Callback<{ action: DeviceStateChange; device: DeviceBasicInfo; }>)
     */
    function off(type: 'deviceDisconnect', callback?: Callback<string>): void;
    /**
     * Registers the continuation management service and obtains a token. This API does not involve any filter parameters
     * and uses an asynchronous callback to return the result.
     *
     * @param { AsyncCallback<number> } callback - Callback used to return the token generated after the continuation
     *     management service is connected.
     * @syscap SystemCapability.Ability.DistributedAbilityManager
     * @stagemodelonly
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.on(type: 'deviceStateChange', callback: Callback<{ action: DeviceStateChange; device: DeviceBasicInfo; }>)
     */
    function register(callback: AsyncCallback<number>): void;
    /**
     * Registers the continuation management service and obtains a token. This API uses an asynchronous callback to return
     *  the result.
     *
     * @param { ContinuationExtraParams } options - Extra parameters used to filter the list of available devices.
     * @param { AsyncCallback<number> } callback - Callback used to return the token generated after the continuation
     *     management service is connected.
     * @syscap SystemCapability.Ability.DistributedAbilityManager
     * @stagemodelonly
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.on(type: 'deviceStateChange', callback: Callback<{ action: DeviceStateChange; device: DeviceBasicInfo; }>)
     */
    function register(options: ContinuationExtraParams, callback: AsyncCallback<number>): void;
    /**
     * Registers the continuation management service and obtains a token. This API uses a promise to return the result.
     *
     * @param { ContinuationExtraParams } [options] - Extra parameters used to filter the list of available devices. This
     *     parameter can be null.
     * @returns { Promise<number> } Promise used to return the token generated after the continuation management service is
     *     connected.
     * @syscap SystemCapability.Ability.DistributedAbilityManager
     * @stagemodelonly
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.on(type: 'deviceStateChange', callback: Callback<{ action: DeviceStateChange; device: DeviceBasicInfo; }>)
     */
    function register(options?: ContinuationExtraParams): Promise<number>;
    /**
     * Unregisters the continuation management service. This API uses an asynchronous callback to return the result.
     *
     * @param { number } token - Token obtained after the registration of the continuation management service.
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the unregistration is successful,
     *     **err** is **undefined**; otherwise, **err** is an error object.
     * @syscap SystemCapability.Ability.DistributedAbilityManager
     * @stagemodelonly
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.off(type: 'deviceStateChange', callback?: Callback<{ action: DeviceStateChange; device: DeviceBasicInfo; }>)
     */
    function unregister(token: number, callback: AsyncCallback<void>): void;
    /**
     * Unregisters the continuation management service. This API uses a promise to return the result.
     *
     * @param { number } token - Token obtained after the registration of the continuation management service.
     * @returns { Promise<void> } Promise used to return the result.
     * @syscap SystemCapability.Ability.DistributedAbilityManager
     * @stagemodelonly
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.off(type: 'deviceStateChange', callback?: Callback<{ action: DeviceStateChange; device: DeviceBasicInfo; }>)
     */
    function unregister(token: number): Promise<void>;
    /**
     * Instructs the device selection module to update the device connection state. This API uses an asynchronous callback
     *  to return the result.
     *
     * @param { number } token - Token obtained after the registration of the continuation management service.
     * @param { string } deviceId - Device ID.
     * @param { DeviceConnectState } status - Device connection state.
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the state is updated, **err** is
     *     **undefined**; otherwise, **err** is an error object.
     * @syscap SystemCapability.Ability.DistributedAbilityManager
     * @stagemodelonly
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.getAvailableDeviceListSync
     */
    function updateConnectStatus(token: number, deviceId: string, status: DeviceConnectState, callback: AsyncCallback<void>): void;
    /**
     * Instructs the device selection module to update the device connection state. This API uses a promise to return the
     * result.
     *
     * @param { number } token - Token obtained after the registration of the continuation management service.
     * @param { string } deviceId - Device ID.
     * @param { DeviceConnectState } status - Device connection state.
     * @returns { Promise<void> } Promise used to return the result.
     * @syscap SystemCapability.Ability.DistributedAbilityManager
     * @stagemodelonly
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.getAvailableDeviceListSync
     */
    function updateConnectStatus(token: number, deviceId: string, status: DeviceConnectState): Promise<void>;
    /**
     * Starts the device selection module to show the list of available devices on the network. This API does not involve
     * any filter parameters and uses an asynchronous callback to return the result.
     *
     * @param { number } token - Token obtained after the registration of the continuation management service.
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the module is started, **err** is
     *     **undefined**; otherwise, **err** is an error object.
     * @syscap SystemCapability.Ability.DistributedAbilityManager
     * @stagemodelonly
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.startDiscovering(discoverParam: { [key: string]: Object; }, filterOptions?: { [key: string]: Object; })
     */
    function startDeviceManager(token: number, callback: AsyncCallback<void>): void;
    /**
     * Starts the device selection module to show the list of available devices on the network. This API uses an
     * asynchronous callback to return the result.
     *
     * @param { number } token - Token obtained after the registration of the continuation management service.
     * @param { ContinuationExtraParams } options - Extra parameters used to filter the list of available devices.
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the module is started, **err** is
     *     **undefined**; otherwise, **err** is an error object.
     * @syscap SystemCapability.Ability.DistributedAbilityManager
     * @stagemodelonly
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.startDiscovering(discoverParam: { [key: string]: Object; }, filterOptions?: { [key: string]: Object; })
     */
    function startDeviceManager(token: number, options: ContinuationExtraParams, callback: AsyncCallback<void>): void;
    /**
     * Starts the device selection module to show the list of available devices on the network. This API uses a promise to
     *  return the result.
     *
     * @param { number } token - Token obtained after the registration of the continuation management service.
     * @param { ContinuationExtraParams } [options] - Extra parameters used to filter the list of available devices. This
     *     parameter can be null.
     * @returns { Promise<void> } Promise used to return the result.
     * @syscap SystemCapability.Ability.DistributedAbilityManager
     * @stagemodelonly
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.distributedDeviceManager:distributedDeviceManager.DeviceManager.startDiscovering(discoverParam: { [key: string]: Object; }, filterOptions?: { [key: string]: Object; })
     */
    function startDeviceManager(token: number, options?: ContinuationExtraParams): Promise<void>;
    /**
     * Registers the continuation management service and obtains a token. This API does not involve any filter parameters
     * and uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.DISTRIBUTED_DATASYNC
     * @param { AsyncCallback<number> } callback - Callback used to return the token generated after the continuation
     *     management service is connected.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 16600001 - The system ability works abnormally.
     * @throws { BusinessError } 16600003 - The number of token registration times has reached the upper limit.
     * @syscap SystemCapability.Ability.DistributedAbilityManager
     * @stagemodelonly
     * @atomicservice [since 11]
     * @since 9
     * @deprecated since 22
     */
    function registerContinuation(callback: AsyncCallback<number>): void;
    /**
     * Registers the continuation management service and obtains a token. This API uses an asynchronous callback to return
     *  the result.
     *
     * @permission ohos.permission.DISTRIBUTED_DATASYNC
     * @param { ContinuationExtraParams } options - Extra parameters used to filter the list of available devices.
     * @param { AsyncCallback<number> } callback - Callback used to return the token generated after the continuation
     *     management service is connected.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 16600001 - The system ability works abnormally.
     * @throws { BusinessError } 16600003 - The number of token registration times has reached the upper limit.
     * @syscap SystemCapability.Ability.DistributedAbilityManager
     * @stagemodelonly
     * @atomicservice [since 11]
     * @since 9
     * @deprecated since 22
     */
    function registerContinuation(options: ContinuationExtraParams, callback: AsyncCallback<number>): void;
    /**
     * Registers the continuation management service and obtains a token. This API uses a promise to return the result.
     *
     * @permission ohos.permission.DISTRIBUTED_DATASYNC
     * @param { ContinuationExtraParams } [options] - Extra parameters used to filter the list of available devices. This
     *     parameter can be null.
     * @returns { Promise<number> } Promise used to return the token generated after the continuation management service is
     *     connected.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Incorrect parameter types;
     *     <br>2. Parameter verification failed;
     * @throws { BusinessError } 16600001 - The system ability works abnormally.
     * @throws { BusinessError } 16600003 - The number of token registration times has reached the upper limit.
     * @syscap SystemCapability.Ability.DistributedAbilityManager
     * @stagemodelonly
     * @atomicservice [since 11]
     * @since 9
     * @deprecated since 22
     */
    function registerContinuation(options?: ContinuationExtraParams): Promise<number>;
    /**
     * Unregisters the continuation management service. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.DISTRIBUTED_DATASYNC
     * @param { number } token - Token obtained after the registration of the continuation management service.
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the unregistration is successful,
     *     **err** is **undefined**; otherwise, **err** is an error object.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 16600001 - The system ability works abnormally.
     * @throws { BusinessError } 16600002 - The specified token or callback is not registered.
     * @syscap SystemCapability.Ability.DistributedAbilityManager
     * @stagemodelonly
     * @atomicservice [since 11]
     * @since 9
     * @deprecated since 22
     */
    function unregisterContinuation(token: number, callback: AsyncCallback<void>): void;
    /**
     * Unregisters the continuation management service. This API uses a promise to return the result.
     *
     * @permission ohos.permission.DISTRIBUTED_DATASYNC
     * @param { number } token - Token obtained after the registration of the continuation management service.
     * @returns { Promise<void> } Promise used to return the result.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 16600001 - The system ability works abnormally.
     * @throws { BusinessError } 16600002 - The specified token or callback is not registered.
     * @syscap SystemCapability.Ability.DistributedAbilityManager
     * @stagemodelonly
     * @atomicservice [since 11]
     * @since 9
     * @deprecated since 22
     */
    function unregisterContinuation(token: number): Promise<void>;
    /**
     * Instructs the device selection module to update the device connection state. This API uses an asynchronous callback
     *  to return the result.
     *
     * @permission ohos.permission.DISTRIBUTED_DATASYNC
     * @param { number } token - Token obtained after the registration of the continuation management service.
     * @param { string } deviceId - Device ID.
     * @param { DeviceConnectState } status - Device connection state.
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the state is updated, **err** is
     *     **undefined**; otherwise, **err** is an error object.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 16600001 - The system ability works abnormally.
     * @throws { BusinessError } 16600002 - The specified token or callback is not registered.
     * @syscap SystemCapability.Ability.DistributedAbilityManager
     * @stagemodelonly
     * @atomicservice [since 11]
     * @since 9
     * @deprecated since 22
     */
    function updateContinuationState(token: number, deviceId: string, status: DeviceConnectState, callback: AsyncCallback<void>): void;
    /**
     * Instructs the device selection module to update the device connection state. This API uses a promise to return the
     * result.
     *
     * @permission ohos.permission.DISTRIBUTED_DATASYNC
     * @param { number } token - Token obtained after the registration of the continuation management service.
     * @param { string } deviceId - Device ID.
     * @param { DeviceConnectState } status - Device connection state.
     * @returns { Promise<void> } Promise used to return the result.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 16600001 - The system ability works abnormally.
     * @throws { BusinessError } 16600002 - The specified token or callback is not registered.
     * @syscap SystemCapability.Ability.DistributedAbilityManager
     * @stagemodelonly
     * @atomicservice [since 11]
     * @since 9
     * @deprecated since 22
     */
    function updateContinuationState(token: number, deviceId: string, status: DeviceConnectState): Promise<void>;
    /**
     * Starts the device selection module to show the list of available devices on the network. This API does not involve
     * any filter parameters and uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.DISTRIBUTED_DATASYNC
     * @param { number } token - Token obtained after the registration of the continuation management service.
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the module is started, **err** is
     *     **undefined**; otherwise, **err** is an error object.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 16600001 - The system ability works abnormally.
     * @throws { BusinessError } 16600002 - The specified token or callback is not registered.
     * @syscap SystemCapability.Ability.DistributedAbilityManager
     * @stagemodelonly
     * @atomicservice [since 11]
     * @since 9
     * @deprecated since 22
     */
    function startContinuationDeviceManager(token: number, callback: AsyncCallback<void>): void;
    /**
     * Starts the device selection module to show the list of available devices on the network. This API uses an
     * asynchronous callback to return the result.
     *
     * @permission ohos.permission.DISTRIBUTED_DATASYNC
     * @param { number } token - Token obtained after the registration of the continuation management service.
     * @param { ContinuationExtraParams } options - Extra parameters used to filter the list of available devices.
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the module is started, **err** is
     *     **undefined**; otherwise, **err** is an error object.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 16600001 - The system ability works abnormally.
     * @throws { BusinessError } 16600002 - The specified token or callback is not registered.
     * @syscap SystemCapability.Ability.DistributedAbilityManager
     * @stagemodelonly
     * @atomicservice [since 11]
     * @since 9
     * @deprecated since 22
     */
    function startContinuationDeviceManager(token: number, options: ContinuationExtraParams, callback: AsyncCallback<void>): void;
    /**
     * Starts the device selection module to show the list of available devices on the network. This API uses a promise to
     *  return the result.
     *
     * @permission ohos.permission.DISTRIBUTED_DATASYNC
     * @param { number } token - Token obtained after the registration of the continuation management service.
     * @param { ContinuationExtraParams } [options] - Extra parameters used to filter the list of available devices. This
     *     parameter can be null.
     * @returns { Promise<void> } Promise used to return the result.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Incorrect parameter types;
     *     <br>2. Parameter verification failed;
     * @throws { BusinessError } 16600001 - The system ability works abnormally.
     * @throws { BusinessError } 16600002 - The specified token or callback is not registered.
     * @syscap SystemCapability.Ability.DistributedAbilityManager
     * @stagemodelonly
     * @atomicservice [since 11]
     * @since 9
     * @deprecated since 22
     */
    function startContinuationDeviceManager(token: number, options?: ContinuationExtraParams): Promise<void>;
    /**
     * Device connection state.
     *
     * @syscap SystemCapability.Ability.DistributedAbilityManager
     * @stagemodelonly
     * @atomicservice [since 11]
     * @since 8
     * @deprecated since 22
     */
    export enum DeviceConnectState {
        /**
         * The device is in the initial state.
         *
         * @syscap SystemCapability.Ability.DistributedAbilityManager
         * @stagemodelonly
         * @atomicservice [since 11]
         * @since 8
         * @deprecated since 22
         */
        IDLE = 0,
        /**
         * The device is being connected.
         *
         * @syscap SystemCapability.Ability.DistributedAbilityManager
         * @stagemodelonly
         * @atomicservice [since 11]
         * @since 8
         * @deprecated since 22
         */
        CONNECTING = 1,
        /**
         * The device is connected.
         *
         * @syscap SystemCapability.Ability.DistributedAbilityManager
         * @stagemodelonly
         * @atomicservice [since 11]
         * @since 8
         * @deprecated since 22
         */
        CONNECTED = 2,
        /**
         * The device is being disconnected.
         *
         * @syscap SystemCapability.Ability.DistributedAbilityManager
         * @stagemodelonly
         * @atomicservice [since 11]
         * @since 8
         * @deprecated since 22
         */
        DISCONNECTING = 3
    }
    /**
     * Enumerates the continuation modes provided by the device selection module.
     *
     * @syscap SystemCapability.Ability.DistributedAbilityManager
     * @stagemodelonly
     * @atomicservice [since 11]
     * @since 8
     * @deprecated since 22
     */
    export enum ContinuationMode {
        /**
         * Single-choice mode.
         *
         * @syscap SystemCapability.Ability.DistributedAbilityManager
         * @stagemodelonly
         * @atomicservice [since 11]
         * @since 8
         * @deprecated since 22
         */
        COLLABORATION_SINGLE = 0,
        /**
         * Multi-choice mode.
         *
         * @syscap SystemCapability.Ability.DistributedAbilityManager
         * @stagemodelonly
         * @atomicservice [since 11]
         * @since 8
         * @deprecated since 22
         */
        COLLABORATION_MULTIPLE = 1
    }
    /**
     * Defines the device information returned by the continuation management entry.
     *
     * @syscap SystemCapability.Ability.DistributedAbilityManager
     * @stagemodelonly
     * @atomicservice [since 11]
     * @since 10
     * @deprecated since 22
     * @useinstead @ohos.distributedDeviceManager:distributedDeviceManager.DeviceBasicInfo
     */
    export type ContinuationResult = _ContinuationResult;
    /**
     * Defines the extra parameters required by the device selection module in the continuation management entry.
     *
     * @syscap SystemCapability.Ability.DistributedAbilityManager
     * @stagemodelonly
     * @atomicservice [since 11]
     * @since 10
     * @deprecated since 22
     * @useinstead @ohos.distributedDeviceManager:distributedDeviceManager.DeviceBasicInfo
     */
    export type ContinuationExtraParams = _ContinuationExtraParams;
}
export default continuationManager;

```
