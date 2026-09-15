# @ohos.usbManager.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2023-2024 Huawei Device Co., Ltd.
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
 * @kit BasicServicesKit
 */
import { AsyncCallback } from './@ohos.base';
/**
 * The **usbManager** module provides USB device management functions, including USB device list query, bulk data
 * transfer, control transfer, and permission control on the host side as well as USB interface management,
 * and function switch and query on the device side.
 *
 * > **NOTE**
 * >
 * > Perform the following steps when using the APIs with the [usbManager.USBDevicePipe]{@link usbManager.USBDevicePipe} parameter:
 * > **Before use**:
 * > 1. Call [usbManager.getDevices]{@link usbManager.getDevices()} to obtain the USB device list.
 * > 2. Call [usbManager.requestRight]{@link usbManager.requestRight(deviceName: string)} to request the temporary device access permission.
 * > 3. Call [usbManager.connectDevice]{@link usbManager.connectDevice(device: USBDevice)} to obtain [usbManager.USBDevicePipe]{@link usbManager.USBDevicePipe} as an input parameter.
 * > **After use**:
 * > Call [usbManager.closePipe]{@link usbManager.closePipe(USBDevicePipe: pipe)} to close a USB device pipe.
 * >
 *
 * @syscap SystemCapability.USB.USBManager
 * @since 9
 */
declare namespace usbManager {
    /**
     * Obtains the list of USB devices connected to the host.
     *
     * > **NOTE**
     * >
     * > Third-party applications are not allowed to obtain the device serial number from the **serial** field. They need to
     * > request permission using [usbManager.requestRight]{@link usbManager.requestRight(deviceName: string)}
     * > and then initiate a control transfer to obtain it.
     *
     * @returns { Array<Readonly<USBDevice>> } USB device list.
     * @throws { BusinessError } 801 - Capability not supported. [since 18]
     * @syscap SystemCapability.USB.USBManager
     * @since 9
     */
    function getDevices(): Array<Readonly<USBDevice>>;
    /**
     * Connects to the USB device based on the device information returned by **getDevices()**. If the USB service is
     * abnormal, **undefined** may be returned. Check whether the return value of the API is empty.
     *
     * 1. Call [usbManager.getDevices]{@link usbManager.getDevices()} to obtain the USB device list.
     * 2. Call [usbManager.requestRight]{@link usbManager.requestRight(deviceName: string)} to request the device access permission.
     *
     * @param { USBDevice } device - USB device. The **busNum** and **devAddress** parameters obtained by
     *     [usbManager.getDevices]{@link usbManager.getDevices()} are used to determine a USB device. Other parameters are passed transparently.
     * @returns { Readonly<USBDevicePipe> } USB device pipe for data transfer.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *
     *     <br>1.Mandatory parameters are left unspecified.
     *
     *     <br>2.Incorrect parameter types.
     * @throws { BusinessError } 801 - Capability not supported. [since 18]
     * @throws { BusinessError } 14400001 - Access right denied. Call requestRight to get the USBDevicePipe access right first.
     * @syscap SystemCapability.USB.USBManager
     * @since 9
     */
    function connectDevice(device: USBDevice): Readonly<USBDevicePipe>;
    /**
     * Checks whether the application has the permission to access the device.
     * Checks whether the user, for example, the application or system, has the device access permissions. The value **
     * true** is returned if the user has the device access permissions; the value **false** is returned otherwise.
     *
     * @param { string } deviceName - Device name, which comes from the USB device name obtained by [usbManager.getDevices]{@link usbManager.getDevices()}.
     * @returns { boolean } Returns **true** if the application has the permission to access the device; returns **false**
     *     otherwise.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *
     *     <br>1.Mandatory parameters are left unspecified.
     *
     *     <br>2.Incorrect parameter types.
     * @throws { BusinessError } 801 - Capability not supported. [since 18]
     * @syscap SystemCapability.USB.USBManager
     * @since 9
     */
    function hasRight(deviceName: string): boolean;
    /**
     * Requests the temporary device access permission for the application. This API uses a promise to return the result.
     * System applications are granted the device access permission by default, and you do not need to apply for the
     * permission separately.
     *
     * @param { string } deviceName - Device name, which comes from the USB device name obtained by [usbManager.getDevices]{@link usbManager.getDevices()}.
     * @returns { Promise<boolean> } Promise used to return the result. The value **true** indicates that the temporary device
     *     access permissions are granted; and the value **false** indicates the opposite.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *
     *     <br>1.Mandatory parameters are left unspecified.
     *
     *     <br>2.Incorrect parameter types.
     * @throws { BusinessError } 801 - Capability not supported. [since 18]
     * @syscap SystemCapability.USB.USBManager
     * @since 9
     */
    function requestRight(deviceName: string): Promise<boolean>;
    /**
     * Removes the device access permission for the application. System applications are granted the device access
     * permission by default, and calling this API will not revoke the permission.
     *
     * @param { string } deviceName - Device name, which comes from the USB device name obtained by [usbManager.getDevices]{@link usbManager.getDevices()}.
     * @returns { boolean } Permission removal result. The value **true** indicates that the access permission is removed
     *     successfully; and the value **false** indicates the opposite.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *
     *     <br>1.Mandatory parameters are left unspecified.
     *
     *     <br>2.Incorrect parameter types.
     * @throws { BusinessError } 801 - Capability not supported. [since 18]
     * @syscap SystemCapability.USB.USBManager
     * @since 9
     */
    function removeRight(deviceName: string): boolean;
    /**
     * Claims a USB device interface.
     *
     * > **NOTE**
     * >
     * > In USB programming, **claimInterface** is a common operation, which indicates that an application requests the
     * > operating system to release a USB interface from the kernel driver and hand over the USB interface to a user
     * > space program for control.<br>
     * > > All the **claim** communication interfaces used below refer to the claim interface operations.
     *
     * @param { USBDevicePipe } pipe - Bus address and device address, which are obtained by calling
     *     [usbManager.connectDevice]{@link usbManager.connectDevice(device: USBDevice)}.
     * @param { USBInterface } iface - Index of the target USB interface. You can use [usbManager.getDevices]{@link usbManager.getDevices()}
     *     to obtain device information and identify the USB interface based on the ID.
     * @param { boolean } [force] - Whether to forcibly claim a USB interface. The default value is **false**, which means not
     *     to forcibly claim a USB interface. You can set the value as required.
     * @returns { number } Returns **0** if the **claim** interface is called successfully; returns an error code otherwise. The
     *     error codes are as follows:
     *
     *     - 88080389: The service is not started. Possible causes: 1. No device is inserted. 2. The service exits abnormally.
     *
     *     - 88080486: The service is being initialized. Try again later.
     *
     *     - 88080488: No device access permission. Call the [usbManager.requestRight]{@link usbManager.requestRight(deviceName: string)} API to request authorization.
     *
     *     - -1: The driver is abnormal.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *
     *     <br>1.Mandatory parameters are left unspecified.
     *
     *     <br>2.Incorrect parameter types.
     * @throws { BusinessError } 801 - Capability not supported. [since 18]
     * @syscap SystemCapability.USB.USBManager
     * @since 9
     */
    function claimInterface(pipe: USBDevicePipe, iface: USBInterface, force?: boolean): number;
    /**
     * Releases the claimed communication interface.
     *
     * > **NOTE**
     * >
     * > Before calling this API, call the
     * > [usbManager.claimInterface]{@link usbManager.claimInterface(pipe: USBDevicePipe, iface: USBInterface, force?: boolean)}
     * >  API to claim a communication interface.
     *
     * @param { USBDevicePipe } pipe - Bus address and device address, which are obtained by calling
     *     [usbManager.connectDevice]{@link usbManager.connectDevice(device: USBDevice)}.
     * @param { USBInterface } iface - Index of the target USB interface. You can use [usbManager.getDevices]{@link usbManager.getDevices()}
     *     to obtain device information and identify the USB interface based on the ID.
     * @returns { number } Returns **0** if the USB interface is successfully released; returns an error code otherwise. The error
     *     codes are as follows:
     *
     *     - 88080389: The service is not started. Possible causes: 1. No device is inserted. 2. The service exits abnormally.
     *
     *     - 88080486: The service is being initialized. Try again later.
     *
     *     - 88080488: No device access permission. Call the [usbManager.requestRight]{@link usbManager.requestRight(deviceName: string)} API to request authorization.
     *
     *     - -1: The driver is abnormal.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *
     *     <br>1.Mandatory parameters are left unspecified.
     *
     *     <br>2.Incorrect parameter types.
     * @throws { BusinessError } 801 - Capability not supported. [since 18]
     * @syscap SystemCapability.USB.USBManager
     * @since 9
     */
    function releaseInterface(pipe: USBDevicePipe, iface: USBInterface): number;
    /**
     * Sets the device configuration.
     *
     * @param { USBDevicePipe } pipe - Bus address and device address, which are obtained by calling
     *     [usbManager.connectDevice]{@link usbManager.connectDevice(device: USBDevice)}.
     * @param { USBConfiguration } config - USB configuration. You can use [usbManager.getDevices]{@link usbManager.getDevices()}
     *     to obtain device information and identify the USB configuration based on the ID.
     * @returns { number } Returns **0** if the USB configuration is successfully set; returns an error code otherwise. The error
     *     codes are as follows:
     *
     *     - 88080389: The service is not started. Possible causes: 1. No device is inserted. 2. The service exits abnormally.
     *
     *     - 88080486: The service is being initialized. Try again later.
     *
     *     - 88080488: No device access permission. Call the [usbManager.requestRight]{@link usbManager.requestRight(deviceName: string)} API to request authorization.
     *
     *     - -1: The driver is abnormal.
     *
     *     - -17: I/O failure.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *
     *     <br>1.Mandatory parameters are left unspecified.
     *
     *     <br>2.Incorrect parameter types.
     * @throws { BusinessError } 801 - Capability not supported. [since 18]
     * @syscap SystemCapability.USB.USBManager
     * @since 9
     */
    function setConfiguration(pipe: USBDevicePipe, config: USBConfiguration): number;
    /**
     * Sets a USB interface.
     *
     * > **NOTE**
     * >
     * > A USB interface may have multiple selection modes and supports dynamic switching. It is used to reset the
     * > endpoint to match the transmission type during data transmission.
     * >
     * > Before calling this API, call the
     * > [usbManager.claimInterface]{@link usbManager.claimInterface(pipe: USBDevicePipe, iface: USBInterface, force?: boolean)}
     * >  API to claim a communication interface.
     *
     * @param { USBDevicePipe } pipe - Bus address and device address, which are obtained by calling
     *     [usbManager.connectDevice]{@link usbManager.connectDevice(device: USBDevice)}.
     * @param { USBInterface } iface - USB interface. You can use [usbManager.getDevices]{@link usbManager.getDevices()}
     *     to obtain device information and identify the USB interface based on its **id** and **alternateSetting**.
     * @returns { number } Returns **0** if the USB interface is successfully set; returns an error code otherwise. The error
     *     codes are as follows:
     *
     *     - 88080389: The service is not started. Possible causes: 1. No device is inserted. 2. The service exits abnormally.
     *
     *     - 88080486: The service is being initialized. Try again later.
     *
     *     - 88080488: No device access permission. Call the [usbManager.requestRight]{@link usbManager.requestRight(deviceName: string)} API to request authorization.
     *
     *     - -1: The driver is abnormal.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *
     *     <br>1.Mandatory parameters are left unspecified.
     *
     *     <br>2.Incorrect parameter types.
     * @throws { BusinessError } 801 - Capability not supported. [since 18]
     * @syscap SystemCapability.USB.USBManager
     * @since 9
     */
    function setInterface(pipe: USBDevicePipe, iface: USBInterface): number;
    /**
     * Obtains a raw USB descriptor. If the USB service is abnormal, **undefined** may be returned. Check whether the
     * return value of the API is empty.
     *
     * @param { USBDevicePipe } pipe - Bus address and device address, which are obtained by calling
     *     [usbManager.connectDevice]{@link usbManager.connectDevice(device: USBDevice)}.
     * @returns { Uint8Array } Returns a raw USB descriptor if the operation is successful; returns **undefined** otherwise.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *
     *     <br>1.Mandatory parameters are left unspecified.
     *
     *     <br>2.Incorrect parameter types.
     * @throws { BusinessError } 801 - Capability not supported. [since 18]
     * @syscap SystemCapability.USB.USBManager
     * @since 9
     */
    function getRawDescriptor(pipe: USBDevicePipe): Uint8Array;
    /**
     * Obtains a file descriptor.
     *
     * @param { USBDevicePipe } pipe - Bus address and device address, which are obtained by calling
     *     [usbManager.connectDevice]{@link usbManager.connectDevice(device: USBDevice)}.
     * @returns { number } Returns the file descriptor corresponding to the device if this API is successfully called; returns an error code otherwise.
     *     The error codes are as follows:
     *
     *     - 88080486: The service is being initialized. Try again later.
     *
     *     - 88080488: No device access permission. Call the [usbManager.requestRight]{@link usbManager.requestRight(deviceName: string)} API to request authorization.
     *
     *     - -1: The driver is abnormal.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *
     *     <br>1.Mandatory parameters are left unspecified.
     *
     *     <br>2.Incorrect parameter types.
     * @throws { BusinessError } 801 - Capability not supported. [since 18]
     * @syscap SystemCapability.USB.USBManager
     * @since 9
     */
    function getFileDescriptor(pipe: USBDevicePipe): number;
    /**
     * Performs control transfer. This API uses a promise to return the result.
     *
     * @param { USBDevicePipe } pipe - USB device pipe, which is obtained by calling [usbManager.connectDevice]{@link usbManager.connectDevice(device: USBDevice)}.
     * @param { USBControlParams } controlparam - Control transfer parameters. Set the parameters as required. For details, see
     *     the USB protocol.
     * @param { number } [timeout] - Timeout interval, Unit: milliseconds. This parameter is optional. If the control transfer is
     *     complete within the specified time, the size of the transferred or received data block is returned; otherwise, a
     *     timeout error is returned. The default value is **0**, indicating that the system waits infinitely until the control
     *     transfer is complete. Set this parameter as required.
     * @returns { Promise<number> } Promise used to return the result, which is the size of the transferred or received data
     *     block if the transfer is successful. If the API call fails, the following error codes are returned:
     *
     *     - -1: The driver is abnormal.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *
     *     <br>1.Mandatory parameters are left unspecified.
     *
     *     <br>2.Incorrect parameter types.
     * @syscap SystemCapability.USB.USBManager
     * @since 9
     * @deprecated since 12
     * @useinstead usbManager.usbControlTransfer(pipe: USBDevicePipe, requestparam: USBDeviceRequestParams, timeout?: int)
     */
    function controlTransfer(pipe: USBDevicePipe, controlparam: USBControlParams, timeout?: number): Promise<number>;
    /**
     * Performs control transfer. This API uses a promise to return the result.
     *
     * @param { USBDevicePipe } pipe - USB device pipe, which is obtained by calling [usbManager.connectDevice]{@link usbManager.connectDevice(device: USBDevice)}.
     * @param { USBDeviceRequestParams } requestparam - Control transfer parameters. Set the parameters as required. For
     *     details, see the USB protocol.
     * @param { number } [timeout] - Timeout interval.Unit: milliseconds. This parameter is optional. If the control transfer is
     *     complete within the specified time, the size of the transferred or received data block is returned; otherwise, a
     *     timeout error is returned. The default value is **0**, indicating that the system waits infinitely until the control
     *     transfer is complete. Set this parameter as required.
     * @returns { Promise<number> } Promise used to return the result, which is the size of the transferred or received data block
     *     if the transfer is successful. If the API call fails, the following error codes are returned:
     *
     *     - -1: The driver is abnormal.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *
     *     <br>1.Mandatory parameters are left unspecified.
     *
     *     <br>2.Incorrect parameter types.
     * @throws { BusinessError } 801 - Capability not supported. [since 18]
     * @syscap SystemCapability.USB.USBManager
     * @since 12
     */
    function usbControlTransfer(pipe: USBDevicePipe, requestparam: USBDeviceRequestParams, timeout?: number): Promise<number>;
    /**
     * Performs bulk transfer. This API uses a promise to return the result.
     *
     * > **NOTE**
     * >
     * > The total size of data (including **pipe**, **endpoint**, **buffer**, and **timeout**) to be transferred in a
     * > single bulk transfer must be less than 200 KB. Otherwise, the transfer fails and **-1** is returned.
     * >
     * > Before calling this API, call the
     * > [usbManager.claimInterface]{@link usbManager.claimInterface(pipe: USBDevicePipe, iface: USBInterface, force?: boolean)}
     * >  API to claim a communication interface.
     *
     * @param { USBDevicePipe } pipe - USB device pipe, which is obtained by calling [usbManager.connectDevice]{@link usbManager.connectDevice(device: USBDevice)}.
     * @param { USBEndpoint } endpoint - USB endpoint, which is used to determine the USB interface for data transfer. You need
     *     to call [usbManager.getDevices]{@link usbManager.getDevices()} to obtain the device information list and endpoint. Wherein, **address** is used to determine
     *     the endpoint address, **direction** is used to determine the endpoint direction, and **interfaceId** is used to
     *     determine the USB interface to which the endpoint belongs. Other parameters are passed transparently.
     * @param { Uint8Array } buffer - Buffer for writing or reading data.
     * @param { number } [timeout] - Timeout interval.Unit: milliseconds. This parameter is optional. If the bulk transfer is
     *     complete within the specified time, the size of the transferred or received data block is returned; otherwise, a
     *     timeout error is returned. The default value is **0**, indicating that the system waits infinitely until the control
     *     transfer is complete. Set this parameter as required.
     * @returns { Promise<number> } Promise used to return the result, which is the size of the transferred or received data block
     *     if the transfer is successful. If the API call fails, the following error codes are returned:
     *
     *     - -1: The driver is abnormal.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *
     *     <br>1.Mandatory parameters are left unspecified.
     *
     *     <br>2.Incorrect parameter types.
     * @throws { BusinessError } 801 - Capability not supported. [since 18]
     * @syscap SystemCapability.USB.USBManager
     * @since 9
     */
    function bulkTransfer(pipe: USBDevicePipe, endpoint: USBEndpoint, buffer: Uint8Array, timeout?: number): Promise<number>;
    /**
     * Resets a USB peripheral.
     *
     * > **NOTE**
     * >
     * > Previous configurations and APIs will be reset. Ensure that the related services have been completed before
     * > calling this API.
     *
     * @param { USBDevicePipe } pipe - Bus address and device address, which are obtained by calling
     *     [usbManager.connectDevice]{@link usbManager.connectDevice(device: USBDevice)}.
     * @returns { boolean } Returns **true** if the device is reset successfully; returns **false** otherwise.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 14400001 - Access right denied. Call requestRight to get the USBDevicePipe access right first.
     * @throws { BusinessError } 14400004 -Service exception. Possible causes: 1. No accessory is plugged in.
     * @throws { BusinessError } 14400008 - No such device(it may have been disconnected)
     * @throws { BusinessError } 14400010 - Other USB error. Possible causes:
     *
     *     <br>1.Unrecognized discard error code.
     * @throws { BusinessError } 14400013 - The USBDevicePipe validity check failed. Possible causes:
     *
     *     <br>1.The input parameters fail the validation check.
     *
     *     <br>2.The call chain used to obtain the input parameters is not reasonable.
     * @syscap SystemCapability.USB.USBManager
     * @since 20
     */
    function resetUsbDevice(pipe: USBDevicePipe): boolean;
    /**
     * Closes a USB device pipe.
     *
     * 1. Call [usbManager.getDevices]{@link usbManager.getDevices()} to obtain the USB device list.
     * 2. Call [usbManager.requestRight]{@link usbManager.requestRight(deviceName: string)} to request the device access permission.
     * 3. Call [usbManager.connectDevice]{@link usbManager.connectDevice(device: USBDevice)} to obtain **devicepipe** as an input parameter.
     *
     * @param { USBDevicePipe } pipe - USB device pipe, which is used to determine the message control channel. You need to
     *     call [usbManager.connectDevice]{@link usbManager.connectDevice(device: USBDevice)} to obtain its value.
     * @returns { number } Returns **0** if the USB device pipe is closed successfully; returns an error code otherwise. The error
     *     codes are as follows:
     *
     *     - 22: The service is abnormal.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *
     *     <br>1.Mandatory parameters are left unspecified.
     *
     *     <br>2.Incorrect parameter types.
     * @throws { BusinessError } 801 - Capability not supported. [since 18]
     * @syscap SystemCapability.USB.USBManager
     * @since 9
     */
    function closePipe(pipe: USBDevicePipe): number;
    /**
     * Checks whether the application has the permission to access the USB accessory.
     * You need to call [usbManager.getAccessoryList]{@link usbManager.getAccessoryList()} to obtain the accessory list
     * and use [USBAccessory]{@link usbManager.USBAccessory} as a parameter.
     *
     * @param { USBAccessory } accessory - USB accessory, which is obtained through
     *     [getAccessoryList]{@link usbManager.getAccessoryList()}.
     * @returns { boolean } The value **true** indicates that the application has the permission to access the USB accessory; *
     *     *false** indicates the opposite.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *
     *     <br>1. Mandatory parameters are left unspecified.
     *
     *     <br>2. Incorrect parameter types.
     * @throws { BusinessError } 801 - Capability not supported. [since 18]
     * @throws { BusinessError } 14401001 - The target USBAccessory not matched.
     * @throws { BusinessError } 14400004 - Service exception. Possible causes:
     *
     *     <br>1. No accessory is plugged in.
     * @throws { BusinessError } 14400005 - Database operation exception.
     * @syscap SystemCapability.USB.USBManager
     * @since 14
     */
    function hasAccessoryRight(accessory: USBAccessory): boolean;
    /**
     * Requests the permission to access a USB accessory for a specified application. This API uses a promise to return
     * the result.
     * You need to call [usbManager.getAccessoryList]{@link usbManager.getAccessoryList()} to obtain the accessory list
     * and use [USBAccessory]{@link usbManager.USBAccessory} as a parameter.
     *
     * @param { USBAccessory } accessory - USB accessory, which is obtained through
     *     [getAccessoryList]{@link usbManager.getAccessoryList()}.
     * @returns { Promise<boolean> } Promise used to return the application result. The value **true** indicates that the
     *     device access permissions are granted; **false** indicates the opposite.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *
     *     <br>1. Mandatory parameters are left unspecified.
     *
     *     <br>2. Incorrect parameter types.
     * @throws { BusinessError } 801 - Capability not supported. [since 18]
     * @throws { BusinessError } 14401001 - The target USBAccessory not matched.
     * @throws { BusinessError } 14400004 - Service exception. Possible causes:
     *
     *     <br>1. No accessory is plugged in.
     * @throws { BusinessError } 14400005 - Database operation exception.
     * @syscap SystemCapability.USB.USBManager
     * @since 14
     */
    function requestAccessoryRight(accessory: USBAccessory): Promise<boolean>;
    /**
     * Cancels the permission of the current application to access USB accessories.
     * You need to call [usbManager.getAccessoryList]{@link usbManager.getAccessoryList()} to obtain the accessory list
     * and use [USBAccessory]{@link usbManager.USBAccessory} as a parameter.
     *
     * @param { USBAccessory } accessory - USB accessory, which is obtained through
     *     [getAccessoryList]{@link usbManager.getAccessoryList()}.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *
     *     <br>1. Mandatory parameters are left unspecified.
     *
     *     <br>2. Incorrect parameter types.
     * @throws { BusinessError } 801 - Capability not supported. [since 18]
     * @throws { BusinessError } 14401001 - The target USBAccessory not matched.
     * @throws { BusinessError } 14400004 - Service exception. Possible causes:
     *
     *     <br>1. No accessory is plugged in.
     * @throws { BusinessError } 14400005 - Database operation exception.
     * @syscap SystemCapability.USB.USBManager
     * @since 14
     */
    function cancelAccessoryRight(accessory: USBAccessory): void;
    /**
     * Obtains the list of USB accessories connected to the host.
     *
     * @returns { Array<Readonly<USBAccessory>> } List of USB accessories (read-only). Currently, only one USB accessory is
     *     contained in the list.
     * @throws { BusinessError } 801 - Capability not supported. [since 18]
     * @throws { BusinessError } 14400004 - Service exception. Possible causes:
     *
     *     <br>1. No accessory is plugged in.
     * @syscap SystemCapability.USB.USBManager
     * @since 14
     */
    function getAccessoryList(): Array<Readonly<USBAccessory>>;
    /**
     * Obtains the accessory handle and opens the accessory file descriptor. Then, the host can communicate with the
     * accessory through the **read** and **write** APIs provided by Core File Kit.
     * You need to call [usbManager.getAccessoryList]{@link usbManager.getAccessoryList()} to obtain the accessory list
     * and use [USBAccessory]{@link usbManager.USBAccessory} as a parameter.
     *
     * @param { USBAccessory } accessory - USB accessory, which is obtained through
     *     [getAccessoryList]{@link usbManager.getAccessoryList()}.
     * @returns { USBAccessoryHandle } USB accessory handle.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *
     *     <br>1. Mandatory parameters are left unspecified.
     *
     *     <br>2. Incorrect parameter types.
     * @throws { BusinessError } 801 - Capability not supported. [since 18]
     * @throws { BusinessError } 14400001 - Access right denied. Call requestRight to get the USBDevicePipe access right first.
     * @throws { BusinessError } 14400004 - Service exception. Possible causes:
     *
     *     <br>1. No accessory is plugged in.
     * @throws { BusinessError } 14401001 - The target USBAccessory not matched.
     * @throws { BusinessError } 14401002 - Failed to open the native accessory node.
     * @throws { BusinessError } 14401003 - Cannot reopen the accessory.
     * @syscap SystemCapability.USB.USBManager
     * @since 14
     */
    function openAccessory(accessory: USBAccessory): USBAccessoryHandle;
    /**
     * Closes the accessory file descriptor.
     * You need to call [usbManager.openAccessory]{@link usbManager.openAccessory(accessory: USBAccessory)} to obtain the
     * accessory list and use [USBAccessoryHandle]{@link usbManager.USBAccessoryHandle} as a parameter.
     *
     * @param { USBAccessoryHandle } accessoryHandle - USB accessory handle, which is obtained through
     *     [openAccessory]{@link usbManager.openAccessory(accessory: USBAccessory)}.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *
     *     <br>1. Mandatory parameters are left unspecified.
     *
     *     <br>2. Incorrect parameter types.
     * @throws { BusinessError } 801 - Capability not supported. [since 18]
     * @throws { BusinessError } 14400004 - Service exception. Possible causes:
     *
     *     <br>1. No accessory is plugged in.
     * @syscap SystemCapability.USB.USBManager
     * @since 14
     */
    function closeAccessory(accessoryHandle: USBAccessoryHandle): void;
    /**
     * Describes the USB endpoint from which data is sent or received. You can obtain the USB endpoint through
     * [USBInterface]{@link usbManager.USBInterface}.
     *
     * > **NOTE**
     * >
     * > The host controller schedules the endpoint based on the endpoint type.
     * >
     * > The transmission characteristics are determined by the type during protocol layer packaging.
     *
     * @syscap SystemCapability.USB.USBManager
     * @since 9
     */
    interface USBEndpoint {
        /**
         * Endpoint address.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         */
        address: number;
        /**
         * Endpoint attributes.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         */
        attributes: number;
        /**
         * Endpoint interval.Unit: milliseconds.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         */
        interval: number;
        /**
         * Maximum size of data packets on the endpoint.Unit: bytes.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         */
        maxPacketSize: number;
        /**
         * Endpoint direction.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         */
        direction: USBRequestDirection;
        /**
         * Endpoint number.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         */
        number: number;
        /**
         * Endpoint type. For details, see [UsbEndpointTransferType]{@link usbManager.UsbEndpointTransferType}.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         */
        type: number;
        /**
         * Unique ID of the interface to which the endpoint belongs.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         */
        interfaceId: number;
    }
    /**
     * Describes a USB interface. One [USBConfiguration]{@link usbManager.USBConfiguration} object can contain multiple *
     * *USBInterface** instances, each providing a specific function.
     *
     * @syscap SystemCapability.USB.USBManager
     * @since 9
     */
    interface USBInterface {
        /**
         * Unique ID of the USB interface.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         */
        id: number;
        /**
         * Interface protocol.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         */
        protocol: number;
        /**
         * Device type.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         */
        clazz: number;
        /**
         * Device subclass.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         */
        subClass: number;
        /**
         * Settings for alternating between descriptors of the same USB interface. The value size indicates the number of
         * optional modes. The value 0 indicates that no optional mode is supported.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         */
        alternateSetting: number;
        /**
         * Interface name.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         */
        name: string;
        /**
         * Endpoints that belong to the USB interface.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         */
        endpoints: Array<USBEndpoint>;
    }
    /**
     * Describes the USB configuration. One [USBDevice]{@link usbManager.USBDevice} can contain multiple **USBConfig**
     * instances.
     *
     * @syscap SystemCapability.USB.USBManager
     * @since 9
     */
    interface USBConfiguration {
        /**
         * Unique ID of the USB configuration.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         */
        id: number;
        /**
         * Configuration attributes.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         */
        attributes: number;
        /**
         * Maximum power consumption.Unit: mA.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         */
        maxPower: number;
        /**
         * Configuration name, which can be left empty.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         */
        name: string;
        /**
         * Whether remote wakeup is supported. **true** if supported, **false otherwise.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         */
        isRemoteWakeup: boolean;
        /**
         * Whether an independent power supply is supported. **true** if supported, **false otherwise.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         */
        isSelfPowered: boolean;
        /**
         * Supported interface attributes.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         */
        interfaces: Array<USBInterface>;
    }
    /**
     * Describes the USB device information.
     *
     * @syscap SystemCapability.USB.USBManager
     * @since 9
     */
    interface USBDevice {
        /**
         * Bus address.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         */
        busNum: number;
        /**
         * Device address.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         */
        devAddress: number;
        /**
         * Sequence number.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         */
        serial: string;
        /**
         * Device name.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         */
        name: string;
        /**
         * Device manufacturer.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         */
        manufacturerName: string;
        /**
         * Product name.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         */
        productName: string;
        /**
         * Version number.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         */
        version: string;
        /**
         * Vendor ID.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         */
        vendorId: number;
        /**
         * Product ID.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         */
        productId: number;
        /**
         * Device class.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         */
        clazz: number;
        /**
         * Device subclass.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         */
        subClass: number;
        /**
         * Device protocol code.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         */
        protocol: number;
        /**
         * Device configuration descriptor information.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         */
        configs: Array<USBConfiguration>;
    }
    /**
     * Describes a USB device pipe, which is used to determine a USB device.
     *
     * @syscap SystemCapability.USB.USBManager
     * @since 9
     */
    interface USBDevicePipe {
        /**
         * Bus address.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         */
        busNum: number;
        /**
         * Device address.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         */
        devAddress: number;
    }
    /**
     * Describes control transfer parameters.
     *
     * @syscap SystemCapability.USB.USBManager
     * @since 12
     */
    interface USBDeviceRequestParams {
        /**
         * Control request type.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 12
         */
        bmRequestType: number;
        /**
         * Request type.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 12
         */
        bRequest: number;
        /**
         * Request parameter.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 12
         */
        wValue: number;
        /**
         * Index of the request parameter.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 12
         */
        wIndex: number;
        /**
         * Length of the requested data.Unit: bytes.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 12
         */
        wLength: number;
        /**
         * Buffer for writing or reading data.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 12
         */
        data: Uint8Array;
    }
    /**
     * Enumerates request target types.
     *
     * @syscap SystemCapability.USB.USBManager
     * @since 9
     */
    export enum USBRequestTargetType {
        /**
         * Device.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         */
        USB_REQUEST_TARGET_DEVICE = 0,
        /**
         * Interface.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         */
        USB_REQUEST_TARGET_INTERFACE = 1,
        /**
         * Endpoint.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         */
        USB_REQUEST_TARGET_ENDPOINT = 2,
        /**
         * Others.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         */
        USB_REQUEST_TARGET_OTHER = 3
    }
    /**
     * Enumerates control request types.
     *
     * @syscap SystemCapability.USB.USBManager
     * @since 9
     */
    export enum USBControlRequestType {
        /**
         * Standard.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         */
        USB_REQUEST_TYPE_STANDARD = 0,
        /**
         * Class.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         */
        USB_REQUEST_TYPE_CLASS = 1,
        /**
         * Vendor.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         */
        USB_REQUEST_TYPE_VENDOR = 2
    }
    /**
     * Enumerates request directions.
     *
     * @syscap SystemCapability.USB.USBManager
     * @since 9
     */
    export enum USBRequestDirection {
        /**
         * Request for writing data from the host to the device.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         */
        USB_REQUEST_DIR_TO_DEVICE = 0,
        /**
         * Request for reading data from the device to the host.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         */
        USB_REQUEST_DIR_FROM_DEVICE = 0x80
    }
    /**
     * Describes the USB accessory information.
     *
     * @syscap SystemCapability.USB.USBManager
     * @since 14
     */
    interface USBAccessory {
        /**
         * Manufacturer of an accessory.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 14
         */
        manufacturer: string;
        /**
         * Product type of an accessory.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 14
         */
        product: string;
        /**
         * Description of an accessory.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 14
         */
        description: string;
        /**
         * Version of an accessory.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 14
         */
        version: string;
        /**
         * SN of an accessory.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 14
         */
        serialNumber: string;
    }
    /**
     * Describes the USB accessory handle.
     *
     * @syscap SystemCapability.USB.USBManager
     * @since 14
     */
    interface USBAccessoryHandle {
        /**
         * Accessory file descriptor. A valid **accessoryFd** is a positive integer.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 14
         */
        accessoryFd: number;
    }
    /**
     * Enumerates USB transfer flags.
     *
     * @syscap SystemCapability.USB.USBManager
     * @since 18
     */
    export enum UsbTransferFlags {
        /**
         * Reports short frames as errors.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 18
         */
        USB_TRANSFER_SHORT_NOT_OK = 0,
        /**
         * Automatically releases the transfer buffer.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 18
         */
        USB_TRANSFER_FREE_BUFFER = 1,
        /**
         * Automatically transfers after the callback is complete.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 18
         */
        USB_TRANSFER_FREE_TRANSFER = 2,
        /**
         * Adds an additional data packet to the transfer.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 18
         */
        USB_TRANSFER_ADD_ZERO_PACKET = 3
    }
    /**
     * Enumerates the status code returned after data processing is complete.
     *
     * @syscap SystemCapability.USB.USBManager
     * @since 18
     */
    export enum UsbTransferStatus {
        /**
         * Transfer completed.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 18
         */
        TRANSFER_COMPLETED = 0,
        /**
         * Transfer failed.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 18
         */
        TRANSFER_ERROR = 1,
        /**
         * Transfer timeout.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 18
         */
        TRANSFER_TIMED_OUT = 2,
        /**
         * Transfer canceled.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 18
         */
        TRANSFER_CANCELED = 3,
        /**
         * Transfer stalled (at bulk/interrupt endpoint).
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 18
         */
        TRANSFER_STALL = 4,
        /**
         * Device disconnected.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 18
         */
        TRANSFER_NO_DEVICE = 5,
        /**
         * Data overflow.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 18
         */
        TRANSFER_OVERFLOW = 6
    }
    /**
     * Enumerates USB transfer types.
     *
     * @syscap SystemCapability.USB.USBManager
     * @since 18
     */
    export enum UsbEndpointTransferType {
        /**
         * Real-time transfer.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 18
         */
        TRANSFER_TYPE_ISOCHRONOUS = 0x1,
        /**
         * Performs bulk transfer.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 18
         */
        TRANSFER_TYPE_BULK = 0x2,
        /**
         * Interrupt transfer.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 18
         */
        TRANSFER_TYPE_INTERRUPT = 0x3
    }
    /**
     * Describes packet information returned in real time by the transfer callback.
     *
     * @syscap SystemCapability.USB.USBManager
     * @since 18
     */
    interface UsbIsoPacketDescriptor {
        /**
         * Expected length of data to be read or written.Unit: bytes.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 18
         */
        length: number;
        /**
         * Actual length of data to be read or written.Unit: bytes.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 18
         */
        actualLength: number;
        /**
         * Status returned by callback.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 18
         */
        status: UsbTransferStatus;
    }
    /**
     * As a USB data transfer interface, it is required for a client to initiate a transfer request.
     *
     * @syscap SystemCapability.USB.USBManager
     * @since 18
     */
    interface UsbDataTransferParams {
        /**
         * Bus address and device address, which are obtained by calling
         * [usbManager.connectDevice]{@link usbManager.connectDevice(device: USBDevice)}.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 18
         */
        devPipe: USBDevicePipe;
        /**
         * USB transfer flag.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 18
         */
        flags: UsbTransferFlags;
        /**
         * Endpoint address, which is a positive integer.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 18
         */
        endpoint: number;
        /**
         * Transfer type.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 18
         */
        type: UsbEndpointTransferType;
        /**
         * Timeout interval, Unit: milliseconds.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 18
         */
        timeout: number;
        /**
         * Expected length of the data buffer.Unit: bytes. The value must be a non-negative number.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 18
         */
        length: number;
        /**
         * Information returned by the callback.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 18
         */
        callback: AsyncCallback<SubmitTransferCallback>;
        /**
         * User data.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 18
         */
        userData: Uint8Array;
        /**
         * Buffer, which is used to store data for read or write requests.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 18
         */
        buffer: Uint8Array;
        /**
         * Number of data packets during real-time transfer, used only for I/Os with real-time transfer endpoints. The value
         *  must be a non-negative integer.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 18
         */
        isoPacketCount: number;
    }
    /**
     * Requests a USB data transfer.
     *
     * > **NOTE**
     * >
     * > This API uses an asynchronous callback to return the result.
     * >
     * > Before calling this API, call the
     * > [usbManager.claimInterface]{@link usbManager.claimInterface(pipe: USBDevicePipe, iface: USBInterface, force?: boolean)}
     * >  API to claim a communication interface.
     *
     * @param { UsbDataTransferParams } transfer - As a USB data transfer interface, it is required for a client to initiate a
     *     transfer request.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 14400001 - Access right denied. Call requestRight to get the USBDevicePipe access right first.
     * @throws { BusinessError } 14400007 - Resource busy. Possible causes:
     *
     *     <br>1. The transfer has already been submitted.
     *
     *     <br>2. The interface is claimed by another program or driver.
     * @throws { BusinessError } 14400008 - No such device (it may have been disconnected).
     * @throws { BusinessError } 14400009 - Insufficient memory. Possible causes:
     *
     *     <br>1. Memory allocation failed.
     * @throws { BusinessError } 14400012 - Transmission I/O error.
     * @syscap SystemCapability.USB.USBManager
     * @since 18
     */
    function usbSubmitTransfer(transfer: UsbDataTransferParams): void;
    /**
     * Cancels an asynchronous USB data transfer request.
     *
     * > **NOTE**
     * >
     * > This API is used to proactively cancel an unfinished USB data transfer request (for example, the one submitted by
     * > **usbSubmitTransfer**).
     * > Before calling this API, call the
     * > [usbManager.claimInterface]{@link usbManager.claimInterface(pipe: USBDevicePipe, iface: USBInterface, force?: boolean)}
     * >  API to claim a communication interface.
     *
     * @param { UsbDataTransferParams } transfer - Only the [USBDevicePipe]{@link usbManager.USBDevicePipe} and
     *     [USBEndpoint]{@link usbManager.USBEndpoint} parameters should be specified in this API.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 14400001 - Access right denied. Call requestRight to get the USBDevicePipe access right first.
     * @throws { BusinessError } 14400008 - No such device (it may have been disconnected).
     * @throws { BusinessError } 14400010 - Other USB error. Possible causes:
     *
     *     <br>1.Unrecognized discard error code.
     * @throws { BusinessError } 14400011 - The transfer is not in progress, or is already complete or cancelled.
     * @syscap SystemCapability.USB.USBManager
     * @since 18
     */
    function usbCancelTransfer(transfer: UsbDataTransferParams): void;
    /**
    * Transfers USB data packets in an asynchronous manner.
    *
    * @syscap SystemCapability.USB.USBManager
    * @since 18
    */
    interface SubmitTransferCallback {
        /**
         * Status after reading or writing is complete.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 18
         */
        status: UsbTransferStatus;
        /**
         * Packet information transferred in real time.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 18
         */
        isoPacketDescs: Array<Readonly<UsbIsoPacketDescriptor>>;
        /**
         * Actual length of data to be read or written.Unit: bytes.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 18
         */
        actualLength: number;
    }
    /**
     * Describes control transfer parameters.
     *
     * @syscap SystemCapability.USB.USBManager
     * @since 9
     * @deprecated since 18
     * @useinstead usbManager.USBDeviceRequestParams
     */
    interface USBControlParams {
        /**
         * Index of the request parameter.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         * @deprecated since 18
         * @useinstead usbManager.USBDeviceRequestParams
         */
        index: number;
        /**
         * Control request type.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         * @deprecated since 18
         * @useinstead usbManager.USBDeviceRequestParams
         */
        reqType: USBControlRequestType;
        /**
         * Request target type.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         * @deprecated since 18
         * @useinstead usbManager.USBDeviceRequestParams
         */
        target: USBRequestTargetType;
        /**
         * Request parameter.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         * @deprecated since 18
         * @useinstead usbManager.USBDeviceRequestParams
         */
        value: number;
        /**
         * Request type.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         * @deprecated since 18
         * @useinstead usbManager.USBDeviceRequestParams
         */
        request: number;
        /**
         * Buffer for writing or reading data.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 9
         * @deprecated since 18
         * @useinstead usbManager.USBDeviceRequestParams
         */
        data: Uint8Array;
    }
}
export default usbManager;

```
