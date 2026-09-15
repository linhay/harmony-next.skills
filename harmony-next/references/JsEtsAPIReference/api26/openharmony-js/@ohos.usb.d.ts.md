# @ohos.usb.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2021-2023 Huawei Device Co., Ltd.
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
 * @file USB Manager
 * @kit BasicServicesKit
 */
/**
 * The **usb** module provides USB device management functions, including USB device list query, bulk data transfer,
 * control transfer, and permission control.
 *
 * > **NOTE**
 * >
 * > The initial APIs of this module are supported since API version 8. Newly added APIs will be marked with
 * > a superscript to indicate their earliest API version.
 * > The APIs provided by this module are no longer maintained since API version 9. You are advised to use
 * > [@ohos.usbManager]{@link @ohos.usbManager:usbManager}.
 *
 * @syscap SystemCapability.USB.USBManager
 * @since 8
 * @deprecated since 9
 * @useinstead @ohos.usbManager:usbManager
 */
declare namespace usb {
    /**
     * Obtains the USB device list.
     *
     * @returns { Array<Readonly<USBDevice>> } USB device list.
     * @syscap SystemCapability.USB.USBManager
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.usbManager:usbManager.getDevices
     */
    function getDevices(): Array<Readonly<USBDevice>>;
    /**
     * Connects to a USB device.
     *
     * Before you do this, call [usb.getDevices]{@link usb.getDevices} to obtain the USB device list, and then call
     * [usb.requestRight]{@link usb.requestRight} to request the device access permission.
     *
     * @param { USBDevice } device - USB device information.
     * @returns { Readonly<USBDevicePipe> } USB device pipe for data transfer.
     * @syscap SystemCapability.USB.USBManager
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.usbManager:usbManager.connectDevice
     */
    function connectDevice(device: USBDevice): Readonly<USBDevicePipe>;
    /**
     * Checks whether the application has the permission to access the device.
     *
     * @param { string } deviceName - Device name.
     * @returns { boolean } Returns **true** if the application has the permission to access the device; returns **false**
     *     otherwise.
     * @syscap SystemCapability.USB.USBManager
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.usbManager:usbManager.hasRight
     */
    function hasRight(deviceName: string): boolean;
    /**
     * Requests the temporary permission for the application to access a USB device. This API uses a promise to return the
     * result. System applications are granted the device access permission by default, and you do not need to apply for
     * the permission separately.
     *
     * @param { string } deviceName - Device name.
     * @returns { Promise<boolean> } Promise used to return the result. The value **true** indicates that the temporary
     *     device access permissions are granted; and the value **false** indicates the opposite.
     * @syscap SystemCapability.USB.USBManager
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.usbManager:usbManager.requestRight
     */
    function requestRight(deviceName: string): Promise<boolean>;
    /**
     * Claims a USB interface.
     *
     * Before you do this, call [usb.getDevices]{@link usb.getDevices} to obtain the USB device list and USB interfaces,
     * call [usb.requestRight]{@link usb.requestRight} to request the device access permission, and call
     * [usb.connectDevice]{@link usb.connectDevice} to obtain **devicepipe** as an input parameter.
     *
     * @param { USBDevicePipe } pipe - Device pipe, which is used to determine the bus number and device address.
     * @param { USBInterface } iface - USB interface, which is used to determine the index of the interface to claim.
     * @param { boolean } [force] - Whether to forcibly claim the USB interface. The default value is **false**,
     *     indicating not to forcibly claim the USB interface.
     * @returns { number } Returns **0** if the USB interface is successfully claimed; returns an error code otherwise.
     * @syscap SystemCapability.USB.USBManager
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.usbManager:usbManager.claimInterface
     */
    function claimInterface(pipe: USBDevicePipe, iface: USBInterface, force?: boolean): number;
    /**
     * Releases a USB interface.
     *
     * Before you do this, ensure that you have claimed the interface by calling
     * [usb.claimInterface]{@link usb.claimInterface}.
     *
     * @param { USBDevicePipe } pipe - Device pipe, which is used to determine the bus number and device address.
     * @param { USBInterface } iface - USB interface, which is used to determine the index of the interface to release.
     * @returns { number } Returns **0** if the USB interface is successfully released; returns an error code otherwise.
     * @syscap SystemCapability.USB.USBManager
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.usbManager:usbManager.releaseInterface
     */
    function releaseInterface(pipe: USBDevicePipe, iface: USBInterface): number;
    /**
     * Sets the device configuration.
     *
     * Before you do this, call [usb.getDevices]{@link usb.getDevices} to obtain the USB device list and device
     * configuration, call [usb.requestRight]{@link usb.requestRight} to request the device access permission, and call
     * [usb.connectDevice]{@link usb.connectDevice} to obtain **devicepipe** as an input parameter.
     *
     * @param { USBDevicePipe } pipe - Device pipe, which is used to determine the bus number and device address.
     * @param { USBConfig } config - USB configuration to set.
     * @returns { number } Returns **0** if the USB configuration is successfully set; returns an error code otherwise.
     * @syscap SystemCapability.USB.USBManager
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.usbManager:usbManager.setConfiguration
     */
    function setConfiguration(pipe: USBDevicePipe, config: USBConfig): number;
    /**
     * Sets a USB interface.
     *
     * Before you do this, call [usb.getDevices]{@link usb.getDevices} to obtain the USB device list and interfaces, call
     * [usb.requestRight]{@link usb.requestRight} to request the device access permission, call
     * [usb.connectDevice]{@link usb.connectDevice} to obtain **devicepipe** as an input parameter, and call
     * [usb.claimInterface]{@link usb.claimInterface} to claim the USB interface.
     *
     * @param { USBDevicePipe } pipe - Device pipe, which is used to determine the bus number and device address.
     * @param { USBInterface } iface - USB interface to set.
     * @returns { number } Returns **0** if the USB interface is successfully set; returns an error code otherwise.
     * @syscap SystemCapability.USB.USBManager
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.usbManager:usbManager.setInterface
     */
    function setInterface(pipe: USBDevicePipe, iface: USBInterface): number;
    /**
     * Obtains the raw USB descriptor.
     *
     * Before you do this, call [usb.getDevices]{@link usb.getDevices} to obtain the USB device list, call
     * [usb.requestRight]{@link usb.requestRight} to request the device access permission, and call
     * [usb.connectDevice]{@link usb.connectDevice} to obtain **devicepipe** as an input parameter.
     *
     * @param { USBDevicePipe } pipe - Device pipe, which is used to determine the bus number and device address.
     * @returns { Uint8Array } Returns the raw USB descriptor if the operation is successful; returns **undefined**
     *     otherwise.
     * @syscap SystemCapability.USB.USBManager
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.usbManager:usbManager.getRawDescriptor
     */
    function getRawDescriptor(pipe: USBDevicePipe): Uint8Array;
    /**
     * Obtains the file descriptor.
     *
     * Before you do this, call [usb.getDevices]{@link usb.getDevices} to obtain the USB device list, call
     * [usb.requestRight]{@link usb.requestRight} to request the device access permission, and call
     * [usb.connectDevice]{@link usb.connectDevice} to obtain **devicepipe** as an input parameter.
     *
     * @param { USBDevicePipe } pipe - Device pipe, which is used to determine the bus number and device address.
     * @returns { number } Returns the file descriptor of the USB device if the operation is successful; returns **-1**
     *     otherwise.
     * @syscap SystemCapability.USB.USBManager
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.usbManager:usbManager.getFileDescriptor
     */
    function getFileDescriptor(pipe: USBDevicePipe): number;
    /**
     * Performs control transfer.
     *
     * Before you do this, call [usb.getDevices]{@link usb.getDevices} to obtain the USB device list, call
     * [usb.requestRight]{@link usb.requestRight} to request the device access permission, and call
     * [usb.connectDevice]{@link usb.connectDevice} to obtain **devicepipe** as an input parameter.
     *
     * @param { USBDevicePipe } pipe - USB device pipe, which is used to determine the USB device.
     * @param { USBControlParams } controlparam - Control transfer parameters.
     * @param { number } [timeout] - Timeout duration in ms. This parameter is optional. The default value is **0**,
     *     indicating no timeout.
     * @returns { Promise<number> } Promise used to return the result, which is the size of the transmitted or received
     *     data block if the transfer is successful, or **-1** if an exception has occurred.
     * @syscap SystemCapability.USB.USBManager
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.usbManager:usbManager.controlTransfer
     */
    function controlTransfer(pipe: USBDevicePipe, controlparam: USBControlParams, timeout?: number): Promise<number>;
    /**
     * Performs bulk transfer.
     *
     * Before you do this, call [usb.getDevices]{@link usb.getDevices} to obtain the USB device list and endpoints, call
     * [usb.requestRight]{@link usb.requestRight} to request the device access permission, call
     * [usb.connectDevice]{@link usb.connectDevice} to obtain **devicepipe** as an input parameter, and call
     * [usb.claimInterface]{@link usb.claimInterface} to claim the USB interface.
     *
     * @param { USBDevicePipe } pipe - USB device pipe, which is used to determine the USB device.
     * @param { USBEndpoint } endpoint - USB endpoint, which is used to determine the USB port for data transfer.
     * @param { Uint8Array } buffer - Buffer for writing or reading data.
     * @param { number } [timeout] - Timeout duration in ms. This parameter is optional. The default value is **0**,
     *     indicating no timeout.
     * @returns { Promise<number> } Promise used to return the result, which is the size of the transmitted or received
     *     data block if the transfer is successful, or **-1** if an exception has occurred.
     * @syscap SystemCapability.USB.USBManager
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.usbManager:usbManager.bulkTransfer
     */
    function bulkTransfer(pipe: USBDevicePipe, endpoint: USBEndpoint, buffer: Uint8Array, timeout?: number): Promise<number>;
    /**
     * Closes a USB device pipe.
     *
     * Before you do this, call [usb.getDevices]{@link usb.getDevices} to obtain the USB device list, call
     * [usb.requestRight]{@link usb.requestRight} to request the device access permission, and call
     * [usb.connectDevice]{@link usb.connectDevice} to obtain **devicepipe** as an input parameter.
     *
     * @param { USBDevicePipe } pipe - USB device pipe.
     * @returns { number } Returns **0** if the USB device pipe is closed successfully; returns an error code otherwise.
     * @syscap SystemCapability.USB.USBManager
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.usbManager:usbManager.closePipe
     */
    function closePipe(pipe: USBDevicePipe): number;
    /**
     * Represents the USB endpoint from which data is sent or received. You can obtain the USB endpoint through
     * [USBInterface]{@link usb.USBInterface}.
     *
     * @syscap SystemCapability.USB.USBManager
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.usbManager:usbManager.USBEndpoint
     */
    interface USBEndpoint {
        /**
         * Endpoint address.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBEndpoint.address
         */
        address: number;
        /**
         * Endpoint attributes.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBEndpoint.attributes
         */
        attributes: number;
        /**
         * Endpoint interval.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBEndpoint.interval
         */
        interval: number;
        /**
         * Maximum size of data packets on the endpoint.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBEndpoint.maxPacketSize
         */
        maxPacketSize: number;
        /**
         * Endpoint direction.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBEndpoint.direction
         */
        direction: USBRequestDirection;
        /**
         * Endpoint number.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBEndpoint.number
         */
        number: number;
        /**
         * Endpoint type.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBEndpoint.type
         */
        type: number;
        /**
         * Unique ID of the interface to which the endpoint belongs.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBEndpoint.interfaceId
         */
        interfaceId: number;
    }
    /**
     * Represents a USB interface. One [USBConfig]{@link usb.USBConfig} can contain multiple **USBInterface** instances,
     * each providing a specific function.
     *
     * @syscap SystemCapability.USB.USBManager
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.usbManager:usbManager.USBInterface
     */
    interface USBInterface {
        /**
         * Unique ID of the USB interface.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBInterface.id
         */
        id: number;
        /**
         * Interface protocol.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBInterface.protocol
         */
        protocol: number;
        /**
         * Device type.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBInterface.clazz
         */
        clazz: number;
        /**
         * Device subclass.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBInterface.subClass
         */
        subClass: number;
        /**
         * Settings for alternating between descriptors of the same USB interface.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBInterface.alternateSetting
         */
        alternateSetting: number;
        /**
         * Interface name.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBInterface.name
         */
        name: string;
        /**
         * Endpoints that belong to the USB interface.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBInterface.endpoints
         */
        endpoints: Array<USBEndpoint>;
    }
    /**
     * Represents the USB configuration. One [USBDevice]{@link usb.USBDevice} can contain multiple **USBConfig**
     * instances.
     *
     * @syscap SystemCapability.USB.USBManager
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.usbManager:usbManager.USBConfiguration
     */
    interface USBConfig {
        /**
         * Unique ID of the USB configuration.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBConfiguration.id
         */
        id: number;
        /**
         * Configuration attributes.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBConfiguration.attributes
         */
        attributes: number;
        /**
         * Maximum power consumption, in mA.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBConfiguration.maxPower
         */
        maxPower: number;
        /**
         * Configuration name, which can be left empty.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBConfiguration.name
         */
        name: string;
        /**
         * Support for remote wakeup.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBConfiguration.isRemoteWakeup
         */
        isRemoteWakeup: boolean;
        /**
         * Support for independent power supplies.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBConfiguration.isSelfPowered
         */
        isSelfPowered: boolean;
        /**
         * Supported interface attributes.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBConfiguration.interfaces
         */
        interfaces: Array<USBInterface>;
    }
    /**
     * Represents the USB device information.
     *
     * @syscap SystemCapability.USB.USBManager
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.usbManager:usbManager.USBDevice
     */
    interface USBDevice {
        /**
         * Bus address.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBDevice.busNum
         */
        busNum: number;
        /**
         * Device address.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBDevice.devAddress
         */
        devAddress: number;
        /**
         * Sequence number.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBDevice.serial
         */
        serial: string;
        /**
         * Device name.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBDevice.name
         */
        name: string;
        /**
         * Device manufacturer.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBDevice.manufacturerName
         */
        manufacturerName: string;
        /**
         * Product name.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBDevice.productName
         */
        productName: string;
        /**
         * Version.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBDevice.version
         */
        version: string;
        /**
         * Vendor ID.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBDevice.vendorId
         */
        vendorId: number;
        /**
         * Product ID.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBDevice.productId
         */
        productId: number;
        /**
         * Device class.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBDevice.clazz
         */
        clazz: number;
        /**
         * Device subclass.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBDevice.subClass
         */
        subClass: number;
        /**
         * Device protocol code.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBDevice.protocol
         */
        protocol: number;
        /**
         * Device configuration descriptor information.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBDevice.configs
         */
        configs: Array<USBConfig>;
    }
    /**
     * Represents a USB device pipe, which is used to determine a USB device.
     *
     * @syscap SystemCapability.USB.USBManager
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.usbManager:usbManager.USBDevicePipe
     */
    interface USBDevicePipe {
        /**
         * Bus address.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBDevicePipe.busNum
         */
        busNum: number;
        /**
         * Device address.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBDevicePipe.devAddress
         */
        devAddress: number;
    }
    /**
     * Represents control transfer parameters.
     *
     * @syscap SystemCapability.USB.USBManager
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.usbManager:usbManager.USBControlParams
     */
    interface USBControlParams {
        /**
         * Request type.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBControlParams.request
         */
        request: number;
        /**
         * Request target type.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBControlParams.target
         */
        target: USBRequestTargetType;
        /**
         * Control request type.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBControlParams.reqType
         */
        reqType: USBControlRequestType;
        /**
         * Request parameter value.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBControlParams.value
         */
        value: number;
        /**
         * Index of the request parameter value.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBControlParams.index
         */
        index: number;
        /**
         * Buffer for writing or reading data.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBControlParams.data
         */
        data: Uint8Array;
    }
    /**
     * Enumerates request target types.
     *
     * @syscap SystemCapability.USB.USBManager
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.usbManager:usbManager.USBRequestTargetType
     */
    export enum USBRequestTargetType {
        /**
         * Device.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBRequestTargetType.USB_REQUEST_TARGET_DEVICE
         */
        USB_REQUEST_TARGET_DEVICE = 0,
        /**
         * Interface.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBRequestTargetType.USB_REQUEST_TARGET_INTERFACE
         */
        USB_REQUEST_TARGET_INTERFACE = 1,
        /**
         * Endpoint.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBRequestTargetType.USB_REQUEST_TARGET_ENDPOINT
         */
        USB_REQUEST_TARGET_ENDPOINT = 2,
        /**
         * Other.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBRequestTargetType.USB_REQUEST_TARGET_OTHER
         */
        USB_REQUEST_TARGET_OTHER = 3
    }
    /**
     * Enumerates control request types.
     *
     * @syscap SystemCapability.USB.USBManager
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.usbManager:usbManager.USBControlRequestType
     */
    export enum USBControlRequestType {
        /**
         * Standard.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBControlRequestType.USB_REQUEST_TYPE_STANDARD
         */
        USB_REQUEST_TYPE_STANDARD = 0,
        /**
         * Class.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBControlRequestType.USB_REQUEST_TYPE_CLASS
         */
        USB_REQUEST_TYPE_CLASS = 1,
        /**
         * Vendor.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBControlRequestType.USB_REQUEST_TYPE_VENDOR
         */
        USB_REQUEST_TYPE_VENDOR = 2
    }
    /**
     * Enumerates request directions.
     *
     * @syscap SystemCapability.USB.USBManager
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.usbManager:usbManager.USBRequestDirection
     */
    export enum USBRequestDirection {
        /**
         * Request for writing data from the host to the device.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBRequestDirection.USB_REQUEST_DIR_TO_DEVICE
         */
        USB_REQUEST_DIR_TO_DEVICE = 0,
        /**
         * Request for reading data from the device to the host.
         *
         * @syscap SystemCapability.USB.USBManager
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.usbManager:usbManager.USBRequestDirection.USB_REQUEST_DIR_FROM_DEVICE
         */
        USB_REQUEST_DIR_FROM_DEVICE = 0x80
    }
}
export default usb;

```
