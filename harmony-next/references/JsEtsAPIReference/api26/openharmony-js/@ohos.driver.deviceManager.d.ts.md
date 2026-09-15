# @ohos.driver.deviceManager.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2023 Huawei Device Co., Ltd.
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
 * @kit DriverDevelopmentKit
 */
import type { AsyncCallback } from './@ohos.base';
import type rpc from './@ohos.rpc';
/**
 * The **deviceManager** module provides APIs for managing peripheral devices, including querying the peripheral device
 * list and binding or unbinding a peripheral device.
 *
 * @syscap SystemCapability.Driver.ExternalDevice
 * @since 10
 */
declare namespace deviceManager {
    /**
     * Queries the list of peripheral devices. If the device has no peripheral device connected, an empty list is
     * returned.
     *
     * @permission ohos.permission.ACCESS_EXTENSIONAL_DEVICE_DRIVER
     * @param { number } busType - Device bus type specified by [BusType]{@link deviceManager.BusType}. If this parameter is
     *     left empty, all types of devices are searched.
     * @returns { Array<Readonly<Device>> } List of peripheral devices obtained.
     * @throws { BusinessError } 201 - The permission check failed.
     * @throws { BusinessError } 22900001 - ExternalDeviceManager service exception or busType parameter error.
     * @syscap SystemCapability.Driver.ExternalDevice
     * @since 10
     */
    function queryDevices(busType?: number): Array<Readonly<Device>>;
    /**
     * Binds a peripheral device based on the device information returned by **queryDevices()**.
     * You need to use [deviceManager.queryDevices()]{@link deviceManager.queryDevices} to obtain the peripheral device
     * information and device.
     *
     * @permission ohos.permission.ACCESS_EXTENSIONAL_DEVICE_DRIVER
     * @param { number } deviceId - Device ID, which can be obtained via **queryDevices()**.
     * @param { AsyncCallback<number> } onDisconnect - Callback used to return the result. When the bound device is
     *     disconnected, the value of **err** is **undefined** and the value of **data** is the ID of the unbound device.
     *     Otherwise, **err** is an error object.
     * @param { AsyncCallback<{ deviceId: number, remote: rpc.IRemoteObject}> } callback - Callback used to return the
     *     result. When the device is bound successfully, **err** is **undefined**, and **data** contains the device ID
     *     and the bound device driver communication object. Otherwise, **err** is an error object.
     * @throws { BusinessError } 201 - The permission check failed.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2
     *     .Incorrect parameter types.
     *     3.Parameter verification failed.
     * @throws { BusinessError } 22900001 - ExternalDeviceManager service exception.
     * @syscap SystemCapability.Driver.ExternalDevice
     * @since 10
     * @deprecated since 19
     * @useinstead deviceManager.bindDriverWithDeviceId(deviceId: long, onDisconnect: AsyncCallback<long>)
     */
    function bindDevice(deviceId: number, onDisconnect: AsyncCallback<number>, callback: AsyncCallback<{
        deviceId: number;
        remote: rpc.IRemoteObject;
    }>): void;
    /**
     * Binds a peripheral device based on the device information returned by **queryDevices()**.
     * You need to use [deviceManager.queryDevices()]{@link deviceManager.queryDevices} to obtain the peripheral device
     * information and device.
     *
     * @permission ohos.permission.ACCESS_EXTENSIONAL_DEVICE_DRIVER
     * @param { number } deviceId - Device ID, which can be obtained via **queryDevices()**.
     * @param { AsyncCallback<number> } onDisconnect - Callback used to return the result. When the bound device is
     *     disconnected, the value of **err** is **undefined** and the value of **data** is the ID of the unbound device.
     *     Otherwise, **err** is an error object.
     * @param { AsyncCallback<RemoteDeviceDriver> } callback - Callback used to return the result. When the device driver
     *     is successfully bound, **err** is **undefined** and **data** is a
     *     [RemoteDeviceDriver]{@link deviceManager.RemoteDeviceDriver} object that contains the device ID and remote
     *     object. Otherwise, **err** is an error object.
     * @throws { BusinessError } 201 - The permission check failed.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified.
     *     2.Incorrect parameter types.
     *     3.Parameter verification failed.
     * @throws { BusinessError } 22900001 - ExternalDeviceManager service exception.
     * @syscap SystemCapability.Driver.ExternalDevice
     * @since 11
     * @deprecated since 19
     * @useinstead deviceManager.bindDriverWithDeviceId(deviceId: long, onDisconnect: AsyncCallback<long>)
     */
    function bindDeviceDriver(deviceId: number, onDisconnect: AsyncCallback<number>, callback: AsyncCallback<RemoteDeviceDriver>): void;
    /**
     * Binds a peripheral device based on the device information returned by **queryDevices()**. This API uses a promise
     * to return the result.
     * You need to use [deviceManager.queryDevices]{@link deviceManager.queryDevices} to obtain the peripheral device
     * information and device.
     *
     * @permission ohos.permission.ACCESS_EXTENSIONAL_DEVICE_DRIVER
     * @param { number } deviceId - Device ID, which can be obtained via **queryDevices()**.
     * @param { AsyncCallback<number> } onDisconnect - Callback used to return the result. When the bound device is
     *     disconnected, the value of **err** is **undefined** and the value of **data** is the ID of the unbound device.
     *     Otherwise, **err** is an error object.
     * @returns { Promise<{ deviceId: number, remote: rpc.IRemoteObject}> } Promise used to return an object containing
     *     the device ID and **IRemoteObject**.
     * @throws { BusinessError } 201 - The permission check failed.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified.
     *     2.Incorrect parameter types.
     *     3.Parameter verification failed.
     * @throws { BusinessError } 22900001 - ExternalDeviceManager service exception.
     * @syscap SystemCapability.Driver.ExternalDevice
     * @since 10
     * @deprecated since 19
     * @useinstead deviceManager.bindDriverWithDeviceId(deviceId: long, onDisconnect: AsyncCallback<long>)
     */
    function bindDevice(deviceId: number, onDisconnect: AsyncCallback<number>): Promise<{
        deviceId: number;
        remote: rpc.IRemoteObject;
    }>;
    /**
     * Binds a peripheral device based on the device information returned by **queryDevices()**. This API uses a promise
     * to return the result.
     * You need to use [deviceManager.queryDevices]{@link deviceManager.queryDevices} to obtain the peripheral device
     * information and device.
     *
     * @permission ohos.permission.ACCESS_EXTENSIONAL_DEVICE_DRIVER
     * @param { number } deviceId - Device ID, which can be obtained via **queryDevices()**.
     * @param { AsyncCallback<number> } onDisconnect - Callback used to return the result. When the bound device is
     *     disconnected, the value of **err** is **undefined** and the value of **data** is the ID of the unbound device.
     *     Otherwise, **err** is an error object.
     * @returns { Promise<RemoteDeviceDriver> } Promise used to return a **RemoteDeviceDriver** object.
     * @throws { BusinessError } 201 - The permission check failed.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified.
     *     2.Incorrect parameter types.
     *     3.Parameter verification failed.
     * @throws { BusinessError } 22900001 - ExternalDeviceManager service exception.
     * @syscap SystemCapability.Driver.ExternalDevice
     * @since 11
     * @deprecated since 19
     * @useinstead deviceManager.bindDriverWithDeviceId(deviceId: long, onDisconnect: AsyncCallback<long>)
     */
    function bindDeviceDriver(deviceId: number, onDisconnect: AsyncCallback<number>): Promise<RemoteDeviceDriver>;
    /**
     * Unbinds a peripheral device.
     *
     * @permission ohos.permission.ACCESS_EXTENSIONAL_DEVICE_DRIVER
     * @param { number } deviceId - Device ID, which can be obtained via **queryDevices()**.
     * @param { AsyncCallback<number> } callback - Callback used to return the result. When the bound device is
     *     disconnected, the value of **err** is **undefined** and the value of **data** is the ID of the unbound device.
     *     Otherwise, **err** is an error object.
     * @throws { BusinessError } 201 - The permission check failed.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified.
     *     2.Incorrect parameter types.
     * @throws { BusinessError } 22900001 - ExternalDeviceManager service exception.
     * @syscap SystemCapability.Driver.ExternalDevice
     * @since 10
     * @deprecated since 19
     * @useinstead deviceManager.unbindDriverWithDeviceId(deviceId: long)
     */
    function unbindDevice(deviceId: number, callback: AsyncCallback<number>): void;
    /**
     * Unbinds a peripheral device. This API uses a promise to return the result.
     *
     * @permission ohos.permission.ACCESS_EXTENSIONAL_DEVICE_DRIVER
     * @param { number } deviceId - Device ID, which can be obtained via **queryDevices()**.
     * @returns { Promise<number> } Promise used to return the ID of the unbound device.
     * @throws { BusinessError } 201 - The permission check failed.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified.
     *     2.Incorrect parameter types.
     *     3.Parameter verification failed.
     * @throws { BusinessError } 22900001 - ExternalDeviceManager service exception.
     * @syscap SystemCapability.Driver.ExternalDevice
     * @since 10
     * @deprecated since 19
     * @useinstead deviceManager.unbindDriverWithDeviceId(deviceId: long)
     */
    function unbindDevice(deviceId: number): Promise<number>;
    /**
     * Binds a peripheral device based on the device information returned by **queryDevices()**. This API uses a promise
     * to return the result.
     * You need to use [deviceManager.queryDevices]{@link deviceManager.queryDevices} to obtain the peripheral device
     * list.
     *
     * @permission ohos.permission.ACCESS_DDK_DRIVERS
     * @param { number } deviceId - Device ID, which can be obtained via **queryDevices()**.
     * @param { AsyncCallback<number> } onDisconnect - Callback used to return the result. When the bound device is
     *     disconnected, the value of **err** is **undefined** and the value of **data** is the ID of the unbound device.
     *     Otherwise, **err** is an error object.
     * @returns { Promise<RemoteDeviceDriver> } Promise used to return a **RemoteDeviceDriver** object.
     * @throws { BusinessError } 201 - The permission check failed.
     * @throws { BusinessError } 26300001 - ExternalDeviceManager service exception.
     * @throws { BusinessError } 26300002 - The driver service does not allow any client to bind.
     * @syscap SystemCapability.Driver.ExternalDevice
     * @since 19
     */
    function bindDriverWithDeviceId(deviceId: number, onDisconnect: AsyncCallback<number>): Promise<RemoteDeviceDriver>;
    /**
     * Unbinds a peripheral device. This API uses a promise to return the result.
     *
     * @permission ohos.permission.ACCESS_DDK_DRIVERS
     * @param { number } deviceId - Device ID, which can be obtained via [queryDevices]{@link deviceManager.queryDevices}.
     * @returns { Promise<number> } Promise used to return the ID of the unbound device.
     * @throws { BusinessError } 201 - The permission check failed.
     * @throws { BusinessError } 26300001 - ExternalDeviceManager service exception.
     * @throws { BusinessError } 26300003 - There is no binding relationship.
     * @syscap SystemCapability.Driver.ExternalDevice
     * @since 19
     */
    function unbindDriverWithDeviceId(deviceId: number): Promise<number>;
    /**
     * Enumerates the device bus types.
     *
     * @syscap SystemCapability.Driver.ExternalDevice
     * @since 10
     */
    export enum BusType {
        /**
         * USB bus.
         *
         * @syscap SystemCapability.Driver.ExternalDevice
         * @since 10
         */
        USB = 1
    }
    /**
     * Represents the peripheral device information.
     *
     * @syscap SystemCapability.Driver.ExternalDevice
     * @since 10
     */
    interface Device {
        /**
         * Bus type.
         *
         * @syscap SystemCapability.Driver.ExternalDevice
         * @since 10
         */
        busType: BusType;
        /**
         * ID of the peripheral device.
         *
         * @syscap SystemCapability.Driver.ExternalDevice
         * @since 10
         */
        deviceId: number;
        /**
         * Description of the peripheral device.
         *
         * @syscap SystemCapability.Driver.ExternalDevice
         * @since 10
         */
        description: string;
    }
    /**
     * USB device information, which is inherited from [Device]{@link deviceManager.queryDevices}.
     *
     * @syscap SystemCapability.Driver.ExternalDevice
     * @since 10
     */
    interface USBDevice extends Device {
        /**
         * Vendor ID of the USB device.
         *
         * @syscap SystemCapability.Driver.ExternalDevice
         * @since 10
         */
        vendorId: number;
        /**
         * Product ID of the USB device.
         *
         * @syscap SystemCapability.Driver.ExternalDevice
         * @since 10
         */
        productId: number;
    }
    /**
     * Represents information about a remote device driver.
     *
     * @syscap SystemCapability.Driver.ExternalDevice
     * @since 11
     */
    interface RemoteDeviceDriver {
        /**
         * ID of the peripheral device.
         *
         * @syscap SystemCapability.Driver.ExternalDevice
         * @since 11
         */
        deviceId: number;
        /**
         * Remote driver object.
         *
         * @syscap SystemCapability.Driver.ExternalDevice
         * @since 11
         */
        remote: rpc.IRemoteObject;
    }
}
export default deviceManager;

```
