# @ohos.enterprise.usbManager.d.ts

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
 * @file USB Management
 * @kit MDMKit
 */
import type Want from './@ohos.app.ability.Want';
/**
 * The **usbManager** module provides APIs for USB management.
 *
 * > **NOTE**
 * >
 * > The APIs of this module can be called only by a device administrator application that is enabled. For details, see
 * > [MDM Kit Development](docroot://mdm/mdm-kit-guide.md).
 * >
 * > The global restriction policy is provided by **restrictions**. To disable USB globally, see
 * > [@ohos.enterprise.restrictions (restriction policy)]{@link @ohos.enterprise.restrictions:restrictions}.
 *
 * @syscap SystemCapability.Customization.EnterpriseDeviceManager
 * @since 12
 */
declare namespace usbManager {
    /**
     * Enumerates the USB storage device access policies.
     *
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 12
     */
    export enum UsbPolicy {
        /**
         * Read and write.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        READ_WRITE = 0,
        /**
         * Read only.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        READ_ONLY = 1,
        /**
         * Disabled.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        DISABLED = 2
    }
    /**
     * Represents the USB device identity information.
     *
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 12
     */
    export interface UsbDeviceId {
        /**
         * Vendor ID.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        vendorId: number;
        /**
         * Product ID.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        productId: number;
    }
    /**
     * Enumerates USB descriptors.
     *
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 14
     */
    enum Descriptor {
        /**
         * Interface descriptor.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 14
         */
        INTERFACE = 0,
        /**
         * Device descriptor.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 14
         */
        DEVICE = 1
    }
    /**
     * Represents the USB device type information.
     *
     * You can obtain the list of USB devices connected to the host device through the
     * [getDevices]{@link @ohos.usbManager:usbManager.getDevices} API, and then find the type of the current device in the
     * returned list.
     *
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 14
     */
    export interface UsbDeviceType {
        /**
         * Type code.
         *
         * First, determine the type of descriptor to pass in based on this value. If the descriptor is **DEVICE**, this
         * field takes the value of the **USBDevice.clazz** field; if the descriptor is **INTERFACE**, this field takes the
         * value of the **USBDevice.configs.interfaces.clazz** field.
         *
         * If the field value is 255 (indicating the device's type code is a vendor-defined code), calling the
         * [addDisallowedUsbDevices]{@link addDisallowedUsbDevices} or
         * [removeDisallowedUsbDevices]{@link removeDisallowedUsbDevices} API to enable or disable the device
         * will not take effect. If the field value is not defined in
         * [defined-class-codes](https://www.usb.org/defined-class-codes), calling the
         * [addDisallowedUsbDevices]{@link addDisallowedUsbDevices} or
         * [removeDisallowedUsbDevices]{@link removeDisallowedUsbDevices} API to enable or disable the device
         * will also not take effect.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 14
         */
        baseClass: number;
        /**
         * Subtype code.
         *
         * First, determine the type of descriptor to pass in based on the value of baseClass. If the descriptor is
         * **DEVICE**, this field takes the value of the **USBDevice.subClass** field; if the descriptor is **INTERFACE**,
         * this field takes the value of the **USBDevice.configs.interfaces.subClass** field.
         *
         * If the field value is 255 (indicating that the subtype code of the device is a vendor-defined code), calling the
         * [addDisallowedUsbDevices]{@link addDisallowedUsbDevices} or
         * [removeDisallowedUsbDevices]{@link removeDisallowedUsbDevices} API to enable or disable the device
         * will not take effect. If the field value is not defined in
         * [defined-class-codes](https://www.usb.org/defined-class-codes), calling the
         * [addDisallowedUsbDevices]{@link addDisallowedUsbDevices} or
         * [removeDisallowedUsbDevices]{@link removeDisallowedUsbDevices} API to enable or disable the device
         * will also not take effect.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 14
         */
        subClass: number;
        /**
         * Protocol code.
         *
         * First, determine the type of descriptor to pass in based on the value of baseClass. If the descriptor is
         * **DEVICE**, this field takes the value of the **USBDevice.protocol** field; if the descriptor is **INTERFACE**,
         * this field takes the value of the **USBDevice.configs.interfaces.protocol** field.
         *
         * If the field value is 255 (indicating the device's protocol code is a vendor-defined code), calling the
         * [addDisallowedUsbDevices]{@link addDisallowedUsbDevices} or
         * [removeDisallowedUsbDevices]{@link removeDisallowedUsbDevices} API to enable or disable the device
         * will not take effect. If the field value is not defined in
         * [defined-class-codes](https://www.usb.org/defined-class-codes), calling the
         * [addDisallowedUsbDevices]{@link addDisallowedUsbDevices} or
         * [removeDisallowedUsbDevices]{@link removeDisallowedUsbDevices} API to enable or disable the device
         * will also not take effect.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 14
         */
        protocol: number;
        /**
         * USB descriptor.
         *
         * If the value of **USBDevice.clazz** is **0**, you need to find the value of
         * **USBDevice.configs.interfaces.clazz** in the Base Class column in
         * [defined-class-codes](https://www.usb.org/defined-class-codes). The Descriptor Usage column in the row where the
         * search result is located indicates the descriptor type to be transferred. If the value of Descriptor Usage is
         * **Both**, both types can be transferred. If device-level disabling is required, transfer **DEVICE**. If interface
         * -level disabling is required, transfer **INTERFACE**.
         *
         * If the value of **USBDevice.clazz** is **255** (indicating the device's type code is a vendor-defined code),
         * calling the [addDisallowedUsbDevices]{@link addDisallowedUsbDevices} or
         * [removeDisallowedUsbDevices]{@link removeDisallowedUsbDevices} API to enable or disable the device
         * will not take effect. If the value of **USBDevice.clazz** is another value, search for the value in the Base
         * Class column of [defined-class-codes](https://www.usb.org/defined-class-codes). The Descriptor Usage column in
         * the row where the search result is located indicates the descriptor type to be transferred. If the value of
         * Descriptor Usage is **Both**, both types can be transferred. If device-level disabling is required, transfer
         * **DEVICE**. If interface-level disabling is required, transfer **INTERFACE**.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 14
         */
        descriptor: Descriptor;
    }
    /**
     * USB device type information. Partial field matching is supported.
     *
     * - Compared with [UsbDeviceType]{@link usbManager.UsbDeviceType}, the **subClass**, **protocol**, and **descriptor**
     * parameters in this API are optional, allowing for more flexible USB device disabling policies.
     * - Only the matching based on the **baseClass** parameter is supported.
     * - Multiple parameters can be configured. All parameters must be satisfied simultaneously for a match.
     * - You can obtain the list of USB devices connected to the host device through the
     * [getDevices]{@link @ohos.usbManager:usbManager.getDevices} API, and then find the type of the current device in the
     * returned list.
     *
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    export interface PermissiveUsbDeviceType {
        /**
         * Type code. The value range is [0, 255].
         * If **descriptor** is **DEVICE**, this parameter takes the value of the **USBDevice.clazz** parameter; if
         * **descriptor** is **INTERFACE**, this parameter takes the value of the **USBDevice.configs.interfaces.clazz**
         * parameter.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        baseClass: number;
        /**
         * Subtype code. The value range is [0, 255].
         * If **descriptor** is **DEVICE**, this parameter takes the value of the **USBDevice.subClass** parameter; if
         * **descriptor** is **INTERFACE**, this parameter takes the value of the **USBDevice.configs.interfaces.subClass**
         * parameter.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        subClass?: number;
        /**
         * Protocol code. The value range is [0, 255].
         * If **descriptor** is **DEVICE**, this parameter takes the value of the **USBDevice.protocol** parameter; if
         * **descriptor** is **INTERFACE**, this parameter takes the value of the **USBDevice.configs.interfaces.protocol**
         * parameter.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        protocol?: number;
        /**
         * USB descriptor.
         * If **USBDevice.clazz** is **0**, locate the value of **USBDevice.configs.interfaces.clazz** in the **Base Class**
         * column of the [defined-class-codes](https://www.usb.org/defined-class-codes) table. The **Descriptor Usage**
         * column of the corresponding row indicates the descriptor type to be passed. (If **Descriptor Usage** is **Both**,
         * either type can be passed. You can pass **DEVICE** for device-level disabling, or **INTERFACE** for interface-
         * level disabling.) If **USBDevice.clazz** is other than **0**, locate that value in the **Base Class** column of
         * the [defined-class-codes](https://www.usb.org/defined-class-codes) table. The **Descriptor Usage** column of the
         * corresponding row indicates the descriptor type to be passed. (If **Descriptor Usage** is **Both**, either type
         * can be passed. Pass **DEVICE** for device-level disabling, or **INTERFACE** for interface-level disabling.).
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        descriptor?: Descriptor;
    }
    /**
     * Adds allowed USB devices.
     *
     * Use cases:
     *
     * - Restrict access to only specific USB devices in enterprise security management scenarios.
     * - Enable device administrators to precisely control which USB devices can be recognized and used.
     * - Work with the [removeAllowedUsbDevices]{@link usbManager.removeAllowedUsbDevices} API to implement dynamic
     * management of USB devices.
     *
     * A policy conflict is reported when this API is called in the following scenarios:
     *
     * 1. The USB capability or the USB-to-serial capability of the device has been disabled via [setDisallowedPolicy]{@link @ohos.enterprise.restrictions:restrictions.setDisallowedPolicy}.
     * 2. The USB storage device access policy has been disabled using the [setUsbStorageDeviceAccessPolicy]{@link usbManager.setUsbStorageDeviceAccessPolicy} API.
     * 3. Disallowed USB device types have been added using the [addDisallowedUsbDevices]{@link usbManager.addDisallowedUsbDevices} API.
     * 4. Disallowed USB device types have been added via [addDisallowedPermissiveUsbDevices]{@link usbManager.addDisallowedPermissiveUsbDevices}.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_USB
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { Array<UsbDeviceId> } usbDeviceIds - USB device IDs, which can be obtained through
     *     [getDevices]{@link @ohos.usbManager:usbManager.getDevices}. The maximum number of USB devices is 1,000. If
     *     there are already 300 USB device IDs, only 700 more can be added.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200007 - The system ability works abnormally.
     * @throws { BusinessError } 9200010 - A conflict policy has been configured.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 12
     */
    function addAllowedUsbDevices(admin: Want, usbDeviceIds: Array<UsbDeviceId>): void;
    /**
     * Removes allowed USB devices.
     *
     * Use cases:
     *
     * - Revoke access permissions for certain USB devices in enterprise security management scenarios.
     * - Enable device administrators to dynamically adjust the list of allowed USB devices.
     * - Remove USB devices from the trustlist when they are no longer needed or pose a security risk.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_USB
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { Array<UsbDeviceId> } usbDeviceIds - USB device IDs, which can be obtained through
     *     [getDevices]{@link @ohos.usbManager:usbManager.getDevices}.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 12
     */
    function removeAllowedUsbDevices(admin: Want, usbDeviceIds: Array<UsbDeviceId>): void;
    /**
     * Obtains allowed USB devices.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_USB
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @returns { Array<UsbDeviceId> } Allowed USB devices obtained.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 12
     */
    function getAllowedUsbDevices(admin: Want): Array<UsbDeviceId>;
    /**
     * Obtains allowed USB devices.
     *
     * Use cases:
     *
     * - Retrieve the existing policy for evaluation before making any modifications.
     * - Display the current USB storage device access control status on the management page.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_USB
     * @param { Want | null } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the.
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.<br>If the device has multiple MDM
     *     applications, you can pass **admin** to query the corresponding policies. If **null** is passed, the policies
     *     that actually take effect on the device are returned.
     * @returns { Array<UsbDeviceId> } Array of device IDs in the USB device trustlist.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function getAllowedUsbDevices(admin: Want | null): Array<UsbDeviceId>;
    /**
     * Sets the USB storage device (baseClass = 0x08) access policy.
     *
     * > **NOTE**
     * >
     * > Before calling the API, read and write operations on the USB storage device should be suspended to ensure
     * > operational stability and data integrity. Otherwise, unexpected exceptions may occur.
     * > A policy conflict occurs when you set the USB storage device access policy to read, write, or read-only in the
     * > following scenarios:
     *
     * 1. The USB capability of the device has been disabled via [setDisallowedPolicy]{@link @ohos.enterprise.restrictions:restrictions.setDisallowedPolicy}.
     * 2. The USB storage device has been disallowed to use through [addDisallowedUsbDevices]{@link usbManager.addDisallowedUsbDevices}.
     * 3. The USB storage write capability has been disabled for specific users via [setDisallowedPolicyForAccount]{@link @ohos.enterprise.restrictions:restrictions.setDisallowedPolicyForAccount}.
     *
     * A policy conflict is reported if the USB storage device access policy is disabled by calling this API in the
     * following scenarios:
     *
     * 1. The USB capability of the device has been disabled via [setDisallowedPolicy]{@link @ohos.enterprise.restrictions:restrictions.setDisallowedPolicy}.
     * 2. The available USB devices have been added through [addAllowedUsbDevices]{@link usbManager.addAllowedUsbDevices}.
     * 3. The USB storage write capability has been disabled for specific users via [setDisallowedPolicyForAccount]{@link @ohos.enterprise.restrictions:restrictions.setDisallowedPolicyForAccount}.
     *
     * You can disable a USB storage device by calling this API or
     * [addDisallowedUsbDevices]{@link addDisallowedUsbDevices}. The latter is recommended.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_USB [since 12 - 24]
     * @permission ohos.permission.ENTERPRISE_MANAGE_USB or ohos.permission.PERSONAL_MANAGE_RESTRICTIONS [since 26.0.0]
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { UsbPolicy } usbPolicy - Access policy of the USB storage device.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200007 - The system ability works abnormally.
     * @throws { BusinessError } 9200010 - A conflict policy has been configured.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 12
     */
    function setUsbStorageDeviceAccessPolicy(admin: Want, usbPolicy: UsbPolicy): void;
    /**
     * Obtains the access policy of the USB storage device.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_USB [since 12 - 24]
     * @permission ohos.permission.ENTERPRISE_MANAGE_USB or ohos.permission.PERSONAL_MANAGE_RESTRICTIONS [since 26.0.0]
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @returns { UsbPolicy } Access policy of the USB storage device.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 12
     */
    function getUsbStorageDeviceAccessPolicy(admin: Want): UsbPolicy;
    /**
     * Obtains the USB storage device (baseClass = 0x08) access policy.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_USB or ohos.permission.PERSONAL_MANAGE_RESTRICTIONS
     * @param { Want | null } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the.
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.<br>If the device has multiple MDM
     *     applications, you can pass **admin** to query the corresponding policies. If **null** is passed, the policies
     *     that actually take effect on the device are returned.
     * @returns { UsbPolicy } Access policy of the USB storage device. The value **READ_WRITE** indicates that the USB
     *     storage device can be read and written. The value **READ_ONLY** indicates that the USB storage device can only
     *     be read. The value **DISABLED** indicates that access to the USB storage device cannot be accessed.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function getUsbStorageDeviceAccessPolicy(admin: Want | null): UsbPolicy;
    /**
     * Adds disallowed USB device types.
     *
     * Use cases:
     *
     * - Disable specific types of USB devices in enterprise security management scenarios.
     * - Prevent data leaks by disabling USB storage device types.
     * - Enable device administrators to prohibit the use of certain USB device types based on security policies.
     * - Work with the [removeDisallowedUsbDevices]{@link usbManager.removeDisallowedUsbDevices} API to implement dynamic
     * management of USB device types.
     *
     * > **NOTE**
     * >
     * > The [addDisallowedPermissiveUsbDevices]{@link usbManager.addDisallowedPermissiveUsbDevices} API is recommended.
     * > A policy conflict is reported when this API is called in the following scenarios:
     *
     * 1. The USB capability of the device has been disabled via [setDisallowedPolicy]{@link @ohos.enterprise.restrictions:restrictions.setDisallowedPolicy}.
     * 2. The available USB devices have been added through [addAllowedUsbDevices]{@link usbManager.addAllowedUsbDevices}.
     * 3. The USB storage write capability has been disabled for specific users via [setDisallowedPolicyForAccount]{@link @ohos.enterprise.restrictions:restrictions.setDisallowedPolicyForAccount}.
     * 4. Disallowed USB device types have been added via [addDisallowedPermissiveUsbDevices]{@link usbManager.addDisallowedPermissiveUsbDevices}.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_USB
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { Array<UsbDeviceType> } usbDevices - Array of the USB devices to be added, which can be obtained through
     *     [getDevices]{@link @ohos.usbManager:usbManager.getDevices}. The maximum number of USB devices is 200. If there
     *     are already 100 USB device IDs, only 100 more can be added.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200010 - A conflict policy has been configured.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 14
     */
    function addDisallowedUsbDevices(admin: Want, usbDevices: Array<UsbDeviceType>): void;
    /**
     * Removes the disallowed USB device types.
     *
     * Use cases:
     *
     * - Lifts the restriction on certain USB device types in enterprise security management scenarios.
     * - Enable device administrators to dynamically adjust the list of disallowed USB device types.
     * - Remove USB device types from the blocklist when they no longer pose a security risk.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_USB
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { Array<UsbDeviceType> } usbDevices - Array of the USB devices to be removed, which can be obtained through
     *     [getDevices]{@link @ohos.usbManager:usbManager.getDevices}.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 14
     */
    function removeDisallowedUsbDevices(admin: Want, usbDevices: Array<UsbDeviceType>): void;
    /**
     * Obtains the disallowed USB device types.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_USB
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @returns { Array<UsbDeviceType> } Disallowed USB device types obtained.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 14
     */
    function getDisallowedUsbDevices(admin: Want): Array<UsbDeviceType>;
    /**
     * Obtains the disallowed USB device types.
     *
     * Use cases:
     *
     * - Retrieve the current list of disallowed USB device types for review by the device administrator.
     * - Obtain the existing blocklist for comparison before making any modifications.
     * - Display the current USB device type restriction policy configuration on the management page.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_USB
     * @param { Want | null } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the.
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.<br>If the device has multiple MDM
     *     applications, you can pass **admin** to query the corresponding policies. If **null** is passed, the policies
     *     that actually take effect on the device are returned.
     * @returns { Array<UsbDeviceType> } Disallowed USB device types obtained.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function getDisallowedUsbDevices(admin: Want | null): Array<UsbDeviceType>;
    /**
     * Adds disallowed USB device types. Unlike the [addDisallowedUsbDevices]{@link usbManager.addDisallowedUsbDevices}
     * API, this API does not require matching based on the [defined-class-codes](https://www.usb.org/defined-class-codes)
     * standard. This API takes effect immediately on connected USB devices without requiring re-plugging. For example, if
     * a USB wired headset is in normal use and this API is called to disable it, the headset will become unavailable
     * immediately.
     *
     * A policy conflict is reported when this API is called in the following scenarios:
     *
     * 1. Disallowed USB device types have been added using the [addDisallowedUsbDevices]{@link usbManager.addDisallowedUsbDevices} API.
     * 2. The USB capability of the device has been disabled via [setDisallowedPolicy]{@link @ohos.enterprise.restrictions:restrictions.setDisallowedPolicy}.
     * 3. The available USB devices have been added through [addAllowedUsbDevices]{@link usbManager.addAllowedUsbDevices}.
     * 4. The USB storage write capability has been disabled for specific users via [setDisallowedPolicyForAccount]{@link @ohos.enterprise.restrictions:restrictions.setDisallowedPolicyForAccount}.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_USB
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { Array<PermissiveUsbDeviceType> } usbDevices - Array of USB device types to be added. Partial field
     *     matching is supported. The array can have a maximum of 1000 elements. If there are already 500 USB device IDs
     *     in the array, only 500 more can be added.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200010 - A conflict policy has been configured.
     * @throws { BusinessError } 9200012 - Parameter verification failed.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function addDisallowedPermissiveUsbDevices(admin: Want, usbDevices: Array<PermissiveUsbDeviceType>): void;
    /**
     * Removes the USB device types that have been disallowed via
     * [addDisallowedPermissiveUsbDevices]{@link usbManager.addDisallowedPermissiveUsbDevices}. The removed USB device
     * types can be used normally.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_USB
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { Array<PermissiveUsbDeviceType> } usbDevices - Array of USB device types to be removed.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200012 - Parameter verification failed.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function removeDisallowedPermissiveUsbDevices(admin: Want, usbDevices: Array<PermissiveUsbDeviceType>): void;
    /**
     * Obtains the USB device types that have been disallowed via
     * [addDisallowedPermissiveUsbDevices]{@link usbManager.addDisallowedPermissiveUsbDevices}.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_USB
     * @param { Want | null } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the.
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.<br>If the device has multiple MDM
     *     applications, you can pass **admin** to query the corresponding policies. If **null** is passed, the policies
     *     that actually take effect on the device are returned.
     * @returns { Array<PermissiveUsbDeviceType> } Array of disallowed USB device types.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function getDisallowedPermissiveUsbDevices(admin: Want | null): Array<PermissiveUsbDeviceType>;
}
export default usbManager;

```
