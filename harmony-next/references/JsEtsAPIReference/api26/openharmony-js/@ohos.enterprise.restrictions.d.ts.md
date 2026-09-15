# @ohos.enterprise.restrictions.d.ts

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
 * @file Restrictions
 * @kit MDMKit
 */
import type Want from '@ohos.app.ability.Want';
/**
 * This **restrictions** module provides APIs for disallowing general features of devices. You can globally disable and
 * re-enable features such as Bluetooth, HDC, USB, Wi-Fi, cellular data, camera, and microphone.
 *
 * **Use cases**
 *
 * - In enterprise device management scenarios, administrators need to restrict functions on employee devices to prevent
 * data leaks or unauthorized use.
 * - In Bring Your Own Device (BYOD) scenarios, the enterprise space needs to restrict device functions to comply with
 * enterprise security policies.
 * - In device security control scenarios, specific functions need to be disabled to protect sensitive enterprise
 * information.
 *
 * **Problems that can be solved**
 *
 * - Prevent employees from transferring sensitive enterprise data via Bluetooth, USB, or other means.
 * - Restrict device debugging capabilities (HDC) to enhance device security.
 * - Control network access (Wi-Fi, cellular data, and so on) to comply with enterprise network policies.
 * - Manage device multimedia capabilities (camera, microphone, and so on) to protect privacy and enterprise
 * confidentiality
 *
 * **Benefits**
 *
 * - Enhance enterprise device security and reduces the risk of data leaks.
 * - Meet compliance requirements and align with security audit standards.
 * - Enable fine-grained device function control, balancing security and user experience.
 *
 * > **NOTE**
 * >
 * > The APIs of this module can be called only by a device administrator application that is enabled. For details, see
 * > [MDM Kit Development](docroot://mdm/mdm-kit-guide.md).
 *
 * @syscap SystemCapability.Customization.EnterpriseDeviceManager
 * @since 12
 */
declare namespace restrictions {
    /**
     * Enumerates device features.
     *
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 24
     */
    enum FeatureForDevice {
        /**
         * Wi-Fi P2P (peer-to-peer connection), which allows devices to directly connect to each other without an access
         * point. Once this feature is disallowed, devices cannot be connected through Wi-Fi P2P, affecting application
         * functions that require direct Wi-Fi connections, such as file transfer, online gaming, and screen sharing.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 24
         */
        WIFI_P2P = 0,
        /**
         * Local input.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        LOCAL_INPUT = 2,
        /**
         * Traffic redirection.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        TRAFFIC_REDIRECTION = 5,
        /**
         * Create a file dump. After this capability is disabled, file dumps cannot be created through the task manager.
         * Currently, this capability is supported only on PCs/2-in-1 devices.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        CORE_DUMP = 6,
        /**
         * RS-232 serial port control policy. If this capability is disabled, data cannot be transmitted via the RS-232
         * serial port. Currently, this capability is supported only on PCs/2-in-1 devices. (some devices do not support the
         * RS-232 serial port).
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        RS232 = 7,
        /**
         * Disk erasure capability. Once disabled, the "Disk Erasure" entry will be grayed out. Currently, this capability
         * is supported only on PCs/2-in-1 devices.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        DISK_ERASURE = 8,
        /**
         * Device Bluetooth capability. If a Bluetooth device blocklist or trustlist is configured via
         * [addDisallowedBluetoothDevices]{@link @ohos.enterprise.bluetoothManager:bluetoothManager.addDisallowedBluetoothDevices}
         * or
         * [addAllowedBluetoothDevices]{@link @ohos.enterprise.bluetoothManager:bluetoothManager.addAllowedBluetoothDevices},
         * disabling Bluetooth via this API takes priority. The blocklist or trustlist will only take effect after Bluetooth
         * is re-enabled.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        BLUETOOTH = 9,
        /**
         * Device capability to modify system time.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        MODIFY_DATE_TIME = 10,
        /**
         * Device printing capability. When the device printing capability has been disabled, enabling printing for a
         * specific user via the [setDisallowedPolicyForAccount]{@link restrictions.setDisallowedPolicyForAccount} API will
         * not take effect. The printing capability remains disabled for that user.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        PRINTER = 11,
        /**
         * Capability for other devices to connect to and debug this device via HDC. Disabling this capability prevents
         * external devices from connecting or debugging via HDC.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        HDC = 12,
        /**
         * Device microphone capability.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        MICROPHONE = 13,
        /**
         * Device fingerprint authentication capability. Enable device fingerprint authentication will trigger a policy
         * conflict if fingerprint authentication has already been disabled for a user via
         * [setDisallowedPolicyForAccount]{@link restrictions.setDisallowedPolicyForAccount}.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        FINGERPRINT = 14,
        /**
         * Device USB capability. Disabling this capability prohibits the use of external USB devices (the device cannot act
         * as a USB host to connect external devices).
         *
         * If the device USB capability is disabled in any of the following scenarios, a policy conflict will be reported:
         *
         * 1. A list of allowed USB devices has been configured via the
         * [addAllowedUsbDevices]{@link @ohos.enterprise.usbManager:usbManager.addAllowedUsbDevices} API.
         * 2. USB storage device access policy has been set to read-only or disabled via the
         * [setUsbStorageDeviceAccessPolicy]{@link @ohos.enterprise.usbManager:usbManager.setUsbStorageDeviceAccessPolicy} API.
         * 3. Specific USB device types have been blocked via the
         * [addDisallowedUsbDevices]{@link @ohos.enterprise.usbManager:usbManager.addDisallowedUsbDevices} API.
         * 4. USB storage write has been disabled for specific users via the [setDisallowedPolicyForAccount]{@link restrictions.setDisallowedPolicyForAccount} API.
         * 5. USB-to-serial conversion ([USB_SERIAL]{@link restrictions.FeatureForDevice}) is disabled.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        USB = 15,
        /**
         * Device Wi-Fi capability.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        WIFI = 16,
        /**
         * Network tethering capability (the ability to share the device's internet connection with other devices, that is,
         * hotspot sharing).
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        TETHERING = 17,
        /**
         * Capability of freezing inactive users. When this capability is disabled, non-**UIAbility** processes will
         * generally not be frozen, and background tasks requested by **UIAbility** (such as transient tasks, continuous
         * tasks, deferred tasks, or energy efficiency resources) will also not be frozen. Currently, this capability is
         * supported only on PCs/2-in-1 devices. When the system switches to the enterprise space user, the personal space
         * users are inactive users.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        INACTIVE_USER_FREEZE = 18,
        /**
         * Device camera capability.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        CAMERA = 19,
        /**
         * Media Transfer Protocol (MTP) client capability (including read and write capabilities), currently supported only
         * on PC/2-in-1 devices. MTP allows users to linearly access media files on mobile devices. A policy conflict occurs
         * when you disable the MTP client capability after MTP client write has been disabled for specific users via
         * [setDisallowedPolicyForAccount]{@link restrictions.setDisallowedPolicyForAccount}.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        MTP_CLIENT = 20,
        /**
         * MTP server capability, currently supported only on phone and tablets.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        MTP_SERVER = 21,
        /**
         * Samba client capability, currently supported only on PC/2-in-1 devices.
         *
         * Samba is a free software that implements the SMB protocol on Linux and UNIX systems, consisting of both server
         * and client programs. Server Message Block (SMB) is a communication protocol for sharing files and printers over
         * the local area network (LAN). It provides resource-sharing services, such as files and printers, among different
         * computers within the LAN. As a client/server protocol, SMB allows clients to access shared resources hosted on
         * servers.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        SAMBA_CLIENT = 22,
        /**
         * Samba server capability, currently supported only on PC/2-in-1 devices.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        SAMBA_SERVER = 23,
        /**
         * Backup and restore capability. If this feature is disabled, the **Settings** > **System** > **Backup & Restore**
         * and **Settings** > **Cloud** options will be dimmed. Currently, this feature is supported only on phones and
         * tablets. To completely disable the backup and restore capability, you are advised to call
         * [applicationManager.addDisallowedRunningBundlesSync]{@link @ohos.enterprise.applicationManager:applicationManager.addDisallowedRunningBundlesSync}
         * to disable applications with this feature, such as Backup & Restore, HiSuite, and Cloud.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        BACKUP_AND_RESTORE = 24,
        /**
         * Device maintenance mode capability.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        MAINTENANCE_MODE = 25,
        /**
         * Multimedia Messaging Service (MMS) capability to receive and send multimedia messages. Currently, this feature is
         * supported only on smartphones and tablets.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        MMS = 26,
        /**
         * Short Messaging Service (SMS) capability to receive and send SMS messages. Currently, this feature is supported
         * only on smartphones and tablets.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        SMS = 27,
        /**
         * Cellular data capability, which is supported only on smartphones and tablets.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        MOBILE_DATA = 28,
        /**
         * Airplane mode capability, which is supported only on smartphones and tablets.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        AIRPLANE_MODE = 29,
        /**
         * Virtual Private Network (VPN) capability.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        VPN = 30,
        /**
         * Device notification capability. After this capability is disabled, notifications sent by system applications and
         * third-party applications will not be displayed. However, notification capabilities for system services are not
         * affected. If you disable the device-level notification capability after an allowed notification bundle has
         * already been set via
         * [addAllowedNotificationBundles]{@link @ohos.enterprise.applicationManager:applicationManager.addAllowedNotificationBundles},
         * error code 9200010 will be reported.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        NOTIFICATION = 31,
        /**
         * Near Field Communication (NFC) capability, which is supported only on phones and tablets.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        NFC = 32,
        /**
         * Privacy space creation capability, which is supported only on smartphones and tablets. This setting does not
         * affect existing private spaces.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        PRIVATE_SPACE = 33,
        /**
         * Call capability. Disabling this feature blocks incoming or outgoing calls. Currently, this feature is supported
         * only on smartphones and tablets.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        TELEPHONE_CALL = 34,
        /**
         * [Application clone capability](docroot://quick-start/app-clone.md). When this feature is disabled, new
         * application clones cannot be created. This feature is invalid for the application clone that has been created.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        APP_CLONE = 35,
        /**
         * External storage capability. Disabling this feature prohibits the use of external storage and unmounts currently
         * connected external storage. If files are in use during unmounting, unmounting may fail with error code 9200013.
         *
         * After external storage is disabled and then enabled again, you need to manually reconnect the external storage.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        EXTERNAL_STORAGE_CARD = 36,
        /**
         * Random MAC address capability for Wi-Fi connections. When this feature is disabled, only the device's physical
         * MAC address can be used for Wi-Fi connections.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        RANDOM_MAC = 37,
        /**
         * Device audio playback capability. When this feature is disabled, media playback will be muted, while
         * [cellular calls](docroot://media/audio/audio-call-overview.md) remain unaffected.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        UNMUTE_DEVICE = 38,
        /**
         * Capability of the device to debug other devices through HDC. Currently, this feature can be set only for PCs/2-in
         * -1 devices. Disabling this capability prevents debugging smartphones, tablets, PCs, smart watches, and other
         * devices via HDC.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        HDC_REMOTE = 39,
        /**
         * Device virtualization service capability, which refers to the system capability of running other operating system
         * platforms (such as Linux and Windows) through virtualization technology by leveraging the redundancy of the
         * device's hardware resources. If this capability is disabled, it is advised to uninstall all applications related
         * to the virtualization service and prohibit their reinstallation.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        VIRTUAL_SERVICE = 40,
        /**
         * Device USB-to-serial port capability. After the capability is disabled, external USB-to-serial port devices will
         * be unavailable. Disabling the USB-to-Serial capability in any of the following scenario will trigger a policy
         * conflict:
         *
         * 1. A list of allowed USB devices has been configured via the
         * [addAllowedUsbDevices]{@link @ohos.enterprise.usbManager:usbManager.addAllowedUsbDevices} API.
         * 2. The device ([USB]{@link restrictions.FeatureForDevice}) capability has been disabled.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        USB_SERIAL = 41,
        /**
         * Screenshot capability. After this capability is disabled, screenshots cannot be taken.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        SCREEN_SHOT = 42,
        /**
         * Screen recording capability. After this capability is disabled, screen recording cannot be performed.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        SCREEN_RECORD = 43,
        /**
         * [Key export](docroot://security/UniversalKeystoreKit/huks-export-key-arkts.md) recovery capability. Currently, it
         * is supported only on PCs/2-in-1 devices.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        DISK_RECOVERY_KEY = 44,
        /**
         * NearLink capability.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        NEAR_LINK = 45,
        /**
         * Developer mode. Disabling this feature takes effect after the device is restarted.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        DEVELOPER_MODE = 46,
        /**
         * Factory reset capability.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        RESET_FACTORY = 47,
        /**
         * Remote desktop capability.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        REMOTE_DESK = 48,
        /**
         * Remote diagnosis capability.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        REMOTE_DIAGNOSIS = 49,
        /**
         * Public network system upgrade capability.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        OTA_UPDATE = 50
    }
    /**
     * Enumerates the features that can be disabled or enabled for a specified user.
     *
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    enum FeatureForAccount {
        /**
         * System multi-window. Currently, this feature is available only on phones and tablets. Once disabled, the system
         * multi-window feature (split-screen, one-click split-screen, Multi-Window, and floating window) cannot be used. If
         * the feature is currently active, the current usage remains unaffected. However, it cannot be used once closed.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        MULTI_WINDOW = 0,
        /**
         * [Distributed management service](docroot://distributedservice/distributedservice-kit-intro.md#working-principles).
         * Once disabled, functions such as discovery, authentication, query, and listening in the distributed device
         * management service cannot be used.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        DISTRIBUTED_TRANSMISSION = 1,
        /**
         * SuperHub. Currently, this feature is available only on phones and tablets. Once disabled, the SuperHub feature
         * cannot be used. If SuperHub is currently active, the current usage remains unaffected. However, it cannot be used
         * once closed.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        SUPER_HUB = 2,
        /**
         * Device fingerprint authentication capability. Currently, this feature is supported only on PCs/2-in-1 devices.
         * The rules for using this capability are as follows:
         *
         * 1. After the device fingerprint authentication capability ([FeatureForDevice.FINGERPRINT]{@link restrictions.FeatureForDevice})
         * is disabled, disabling this capability for a specific user will result in a policy conflict.
         * 2. After the device fingerprint authentication capability is disabled or enabled for a specific user, disabling
         * this capability ([FeatureForDevice.FINGERPRINT]{@link restrictions.FeatureForDevice}) globally will override the
         * user-specific policy. Subsequently, re-enabling this capability ([FeatureForDevice.FINGERPRINT]{@link restrictions.FeatureForDevice})
         * globally will allow all users to use device fingerprint authentication.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        FINGERPRINT = 3,
        /**
         * Device printing capability. If the device printing capability is disabled for a specific user, it remains
         * disabled for that user even if the device printing capability (
         * [FeatureForDevice.PRINTER]{@link restrictions.FeatureForDevice}) capability is enabled globally.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        PRINT = 4,
        /**
         * MTP client capability (including read and write capabilities). Currently, it is supported only on PC/2-in-1
         * devices. MTP allows users to linearly access media files on mobile devices. After the device MTP client
         * capability ([FeatureForDevice.MTP_CLIENT]{@link restrictions.FeatureForDevice}) is disabled, disabling the MTP
         * client write capability for a specific user will result in a policy conflict.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        MTP_CLIENT = 5,
        /**
         * USB storage device write capability. Currently, it is supported only on enterprise PCs/2-in-1 devices.
         *
         * Disabling the USB storage device write capability for a specific user in any of the following scenarios will
         * result in a policy conflict:
         *
         * 1. The device USB capability ([FeatureForDevice.USB]{@link restrictions.FeatureForDevice}) has been disabled.
         * 2. USB storage device access policy has been set to read-only or disabled via the
         * [setUsbStorageDeviceAccessPolicy]{@link @ohos.enterprise.usbManager:usbManager.setUsbStorageDeviceAccessPolicy} API.
         * 3. Storage USB devices have been disabled via the [addDisallowedUsbDevices]{@link @ohos.enterprise.usbManager:usbManager.addDisallowedUsbDevices} API.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        USB_STORAGE_DEVICE_WRITE = 6,
        /**
         * [Key export](docroot://security/UniversalKeystoreKit/huks-export-key-arkts.md) recovery capability. Currently, it
         * is supported only on PCs/2-in-1 devices.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        DISK_RECOVERY_KEY = 7,
        /**
         * superuser do (execution with superuser privileges). Currently, it is supported only on PCs/2-in-1 devices. If
         * this feature is disabled, neither enterprise spaces nor personal spaces can perform operations with superuser
         * privileges.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        SUDO = 8,
        /**
         * Distributed one-way data transmission between devices (only data transmission to other devices is supported).
         * Disabling distributed one-way data transmission capability between devices after the distributed management
         * service ([DISTRIBUTED_TRANSMISSION]{@link restrictions.FeatureForAccount}) has been disabled will result in a
         * policy conflict.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        DISTRIBUTED_TRANSMISSION_OUTGOING = 9,
        /**
         * File open acceleration capability, providing applications with the ability to sense the file open acceleration
         * status. By integrating the corresponding APIs, apps can detect the acceleration status of files, and further
         * implement features such as displaying unique UI identifiers for accelerated files, thereby optimizing user
         * experience of file opening. Currently, this feature is supported only on PCs/2-in-1 devices.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        OPEN_FILE_BOOST = 10
    }
    /**
     * Enumerates device setting items.
     *
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    enum SettingsForDevice {
        /**
         * APN configuration, currently supported only on phones and tablets.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        SET_APN = 0,
        /**
         * Opens the power menu by long-pressing the power button. Currently, this item is supported only on phones and
         * tablets.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        POWER_LONG_PRESS = 1,
        /**
         * Changes the Ethernet IP address. Currently, this item is supported only on PCs/2-in-1 devices.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        SET_ETHERNET_IP = 2,
        /**
         * Changes the device name configuration. Currently, this item is supported only on PCs/2-in-1 devices, phones, and
         * tablets. When it is disabled, the device name cannot be modified in the following settings: **About**,
         * **Bluetooth**, and **More connectivity options** > **NearLink** on PCs/2-in-1 devices, and **About**,
         * **Bluetooth**, and **Personal hotspot** on smartphones and tablets.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        SET_DEVICE_NAME = 3,
        /**
         * Changes the screen lock password. Currently, this item is supported only on PCs/2-in-1 devices, phones, and
         * tablets.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        SET_BIOMETRICS_AND_SCREEN_LOCK = 4
    }
    /**
     * Enumerates user setting items.
     *
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    enum SettingsForAccount {
        /**
         * Modifies the wallpaper, including both the lock screen wallpaper and the home screen wallpaper.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        MODIFY_WALLPAPER = 0
    }
    /**
     * Disallows a feature.
     *
     * > **NOTE**
     * >
     * > This API applies a device-level restriction policy that affects all users of the device. To set a restriction
     * > policy for a specific user, use the
     * > [setDisallowedPolicyForAccount]{@link restrictions.setDisallowedPolicyForAccount} API.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_RESTRICTIONS [since 12 - 14]
     * @permission ohos.permission.ENTERPRISE_MANAGE_RESTRICTIONS or
     *     ohos.permission.PERSONAL_MANAGE_RESTRICTIONS [since 15 - 19]
     * @permission ohos.permission.ENTERPRISE_MANAGE_RESTRICTIONS or ohos.permission.PERSONAL_MANAGE_RESTRICTIONS or
     *     ohos.permission.ENTERPRISE_MANAGE_NETWORK [since 20]
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { string } feature - For features that can be set, see Table 1.
     *     <br> **Note:** Since API version 15, applications granted with the ohos.permission.PERSONAL_MANAGE_RESTRICTIONS
     *     permission and activated as the [BDA](docroot://mdm/mdm-kit-term.md#byod-device-admin-bdabyod) via
     *     [startAdminProvision]{@link @ohos.enterprise.adminManager:adminManager.startAdminProvision} can use this API to
     *     set the following features: bluetooth, hdc, microphone, usb, wifi, tethering, and camera.
     *     Since API version 26.0.0, this API can also be used to set the mtpServer feature.
     * @param { boolean } disallow - Whether to disallow the feature. The value **true** means to disallow the feature;
     *     the value **false** means the opposite.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 9200013 - The enterprise management policy has been successfully set,
     *     but the function has not taken effect in real time. [since 21]
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 12
     * @deprecated since 26.0.0
     * @useinstead restrictions.setDisallowedPolicy(admin: Want, feature: FeatureForDevice, disallow: boolean)
     */
    function setDisallowedPolicy(admin: Want, feature: string, disallow: boolean): void;
    /**
     * Queries whether a feature is disabled.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_RESTRICTIONS [since 12 - 14]
     * @permission ohos.permission.ENTERPRISE_MANAGE_RESTRICTIONS or
     *     ohos.permission.PERSONAL_MANAGE_RESTRICTIONS [since 15 - 19]
     * @permission ohos.permission.ENTERPRISE_MANAGE_RESTRICTIONS or ohos.permission.PERSONAL_MANAGE_RESTRICTIONS or
     *     ohos.permission.ENTERPRISE_MANAGE_NETWORK [since 20]
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application. [since 12 - 19]
     * @param { Want | null } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application. [since 20]
     * @param { string } feature - For features that can be queried, see Table 2.
     *     <br> **Note:** Since API version 15, applications granted with the ohos.permission.PERSONAL_MANAGE_RESTRICTIONS
     *     permission and activated as the [BDA](docroot://mdm/mdm-kit-term.md#byod-device-admin-bdabyod) via
     *     [startAdminProvision]{@link @ohos.enterprise.adminManager:adminManager.startAdminProvision} can use this API to
     *     obtain the status of the following features: bluetooth, hdc, microphone, usb, wifi, tethering, and camera.
     *     Since API version 26.0.0, this API can also be used to obtain the status of the mtpServer feature.
     * @returns { boolean } The value **true** means the feature is disallowed; the value **false** means the opposite.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 12
     * @deprecated since 26.0.0
     * @useinstead restrictions.getDisallowedPolicy(admin: Want | null, feature: FeatureForDevice)
     */
    function getDisallowedPolicy(admin: Want | null, feature: string): boolean;
    /**
     * Disallows a feature for a specified user.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_RESTRICTIONS
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { string } feature - Feature to set.
     *     <br>- **fingerprint**: device fingerprint authentication capability. Currently, this feature is supported only
     *     on PCs/2-in-1 devices. The rules for using this parameter are as follows:
     *     <br>1. If the device fingerprint authentication capability has been disabled through the
     *     [setDisallowedPolicy]{@link restrictions.setDisallowedPolicy} API, calling this API with this parameter passed
     *     will throw a policy conflict.
     *     <br>2. After the device fingerprint authentication capability is enabled or disabled via this API for a
     *     specified user, any subsequent action via the [setDisallowedPolicy]{@link restrictions.setDisallowedPolicy} API
     *     will override the previous setting. If [setDisallowedPolicy]{@link restrictions.setDisallowedPolicy} enables
     *     the capability, all users gain access to the device fingerprint authentication.
     *     <br>- **print**<sup>20+</sup>: device printing capability, which is supported only on PCs/2-in-1 devices for
     *     API versions earlier than 23, and on PCs/2-in-1 devices, smartphones, and tablets for API version 23 and later
     *     versions. If the device printing capability is disabled via this API, it remains disabled for specific users
     *     even if the [setDisallowedPolicy]{@link restrictions.setDisallowedPolicy} API is used to enable it for those
     *     users.
     *     <br>- **mtpClient**<sup>20+</sup>: Media Transfer Protocol (MTP) client capability (write only). Currently,
     *     this feature is supported only on PCs/2-in-1 devices. MTP allows users to linearly access media files on mobile
     *     devices. A policy conflict error will occur if this API is used to disable the MTP client capability after MTP
     *     client write has been disabled for specific users via the
     *     [setDisallowedPolicy]{@link restrictions.setDisallowedPolicy} API.
     *     <br>- **usbStorageDeviceWrite**<sup>20+</sup>: USB storage device write capability. Currently, this feature is
     *     supported only on enterprise PCs/2-in-1 devices.
     *     <br>  If the USB storage device write permission of a user is disabled via this API in any of the following
     *     situations, a policy conflict will be reported:
     *     <br>  1. The device USB capability has been disabled via the
     *     [setDisallowedPolicy]{@link restrictions.setDisallowedPolicy} API.
     *     <br>  2. USB storage device access policy has been set to read-only or disabled via the
     *     [setUsbStorageDeviceAccessPolicy]{@link @ohos.enterprise.usbManager:usbManager.setUsbStorageDeviceAccessPolicy}
     *     API.
     *     <br>  3. Storage USB devices have been disabled via the
     *     [addDisallowedUsbDevices]{@link @ohos.enterprise.usbManager:usbManager.addDisallowedUsbDevices} API.
     *     <br>- **diskRecoveryKey**<sup>20+</sup>: recovery
     *     [key export](docroot://security/UniversalKeystoreKit/huks-export-key-arkts.md) capability. Currently, this
     *     feature is supported only on PCs/2-in-1 devices.
     *     <br>- **sudo**<sup>20+</sup>: superuser do (execution with superuser privileges). Currently, this feature is
     *     supported only on PCs/2-in-1 devices. If this feature is disabled, neither enterprise spaces nor personal
     *     spaces can perform operations with superuser privileges.
     *     <br>- **distributedTransmissionOutgoing**<sup>20+</sup>: distributed one-way data transmission between devices
     *     (only data transmission to other devices is supported). A policy conflict occurs if this API is used to disable
     *     distributed one-way data transmission between devices after the distributed service has already been disabled
     *     via the [setDisallowedPolicyForAccount]{@link restrictions.setDisallowedPolicyForAccount} API.
     *     <br>- **openFileBoost**<sup>23+</sup>: file opening acceleration capability, which
     *     provides the file opening acceleration status awareness capability for apps. By integrating the corresponding
     *     APIs, apps can detect the acceleration status of files, and further implement features such as displaying
     *     unique UI identifiers for accelerated files, thereby optimizing user experience of file opening. Currently,
     *     this feature is supported only on PCs/2-in-1 devices.
     * @param { boolean } disallow - Whether to disallow the feature. The value **true** means to disallow the feature;
     *     the value **false** means the opposite.
     * @param { number } accountId - User ID, which must be greater than or equal to 0.
     *     <br>**accountId** can be obtained via APIs such as
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()}.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200010 - A conflict policy has been configured.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 14
     * @deprecated since 26.0.0
     * @useinstead restrictions.setDisallowedPolicyForAccount(admin: Want, feature: FeatureForAccount, disallow: boolean, accountId: number)
     */
    function setDisallowedPolicyForAccount(admin: Want, feature: string, disallow: boolean, accountId: number): void;
    /**
     * Obtains the status of a feature for a specified user.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_RESTRICTIONS
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application. [since 14 - 19]
     * @param { Want | null } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application. [since 20]
     * @param { string } feature - Feature to set.
     *     <br>- **fingerprint**: device fingerprint authentication capability. Currently, this feature is supported only
     *     on PCs/2-in-1 devices. Note that when
     *     [setDisallowedPolicyForAccount]{@link restrictions.setDisallowedPolicyForAccount} is used to disable or enable
     *     the device fingerprint authentication capability for a specified user, any subsequent action via the
     *     [setDisallowedPolicy]{@link restrictions.setDisallowedPolicy} API will override the previous setting. The value
     *     **false** will be returned.
     *     <br>- **mtpClient**<sup>20+</sup>: Media Transfer Protocol (MTP) client capability (write only). Currently,
     *     this feature is supported only on PCs/2-in-1 devices. MTP allows users to linearly access media files on mobile
     *     devices.
     *     <br>- **usbStorageDeviceWrite**<sup>20+</sup>: USB storage device write capability. Currently, this feature is
     *     supported only on enterprise PCs/2-in-1 devices.
     *     <br>- **diskRecoveryKey**<sup>20+</sup>: recovery
     *     [key export](docroot://security/UniversalKeystoreKit/huks-export-key-arkts.md) capability. Currently, this
     *     feature is supported only on PCs/2-in-1 devices.
     *     <br>- **sudo**<sup>20+</sup>: superuser do (execution with superuser privileges). Currently, this feature is
     *     supported only on PCs/2-in-1 devices. If this feature is disabled, neither enterprise spaces nor personal
     *     spaces can perform operations with superuser privileges.
     *     <br>- **distributedTransmissionOutgoing**<sup>20+</sup>: one-way data transmission between devices (only data
     *     transmission to other devices is supported).
     *     <br>- **print**<sup>20+</sup>: device printing capability, which is supported only on PCs/2-in-1 devices for
     *     API versions earlier than 23, and on PCs/2-in-1 devices, smartphones, and tablets for API version 23 and later
     *     versions. If printing is disabled via the [setDisallowedPolicy]{@link restrictions.setDisallowedPolicy} API, it
     *     remains disabled even if the [setDisallowedPolicyForAccount]{@link restrictions.setDisallowedPolicyForAccount}
     *     API is used to enable it for specific users.
     *     <br>- **openFileBoost**<sup>23+</sup>: file opening acceleration capability, which
     *     provides the file opening acceleration status awareness capability for apps. By integrating the corresponding
     *     APIs, apps can detect the acceleration status of files, and further implement features such as displaying
     *     unique UI identifiers for accelerated files, thereby optimizing user experience of file opening. Currently,
     *     this feature is supported only on PCs/2-in-1 devices.
     * @param { number } accountId - User ID, which must be greater than or equal to 0.
     *     <br>**accountId** can be obtained via APIs such as
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()}.
     * @returns { boolean } The value **true** means the feature is disabled; the value **false** means the opposite.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 14
     * @deprecated since 26.0.0
     * @useinstead restrictions.getDisallowedPolicyForAccount(admin: Want | null, feature: FeatureForAccount, accountId: number)
     */
    function getDisallowedPolicyForAccount(admin: Want | null, feature: string, accountId: number): boolean;
    /**
     * Adds a list of applications that are not allowed to use a feature for a specified user.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_RESTRICTIONS
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { string } feature - Feature to set.
     *     <br>- **snapshotSkip**: screen snapshot capability.
     * @param { Array<string> } list - App bundle name list.
     * @param { number } accountId - User ID, which must be greater than or equal to 0.
     *     <br>**accountId** can be obtained via APIs such as
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()}.
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
    function addDisallowedListForAccount(admin: Want, feature: string, list: Array<string>, accountId: number): void;
    /**
     * Removes the list of applications that are not allowed to use a feature for a specified user.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_RESTRICTIONS
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { string } feature - Feature to set.
     *     <br>- **snapshotSkip**: screen snapshot capability.
     * @param { Array<string> } list - List of content such as the bundle names.
     * @param { number } accountId - User ID, which must be greater than or equal to 0.
     *     <br>**accountId** can be obtained via APIs such as
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()}.
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
    function removeDisallowedListForAccount(admin: Want, feature: string, list: Array<string>, accountId: number): void;
    /**
     * Obtains the list of applications that are not allowed to use a feature for a specified user.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_RESTRICTIONS
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { string } feature - Feature to set.
     *     <br>- **snapshotSkip**: screen snapshot capability.
     * @param { number } accountId - User ID, which must be greater than or equal to 0.
     *     <br>**accountId** can be obtained via APIs such as
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()}.
     * @returns { Array<string> } List of applications that have been added by the user and for which a certain feature is
     *     disabled.
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
    function getDisallowedListForAccount(admin: Want, feature: string, accountId: number): Array<string>;
    /**
     * Sets restrictions on user behaviors.
     *
     * @permission ohos.permission.ENTERPRISE_SET_USER_RESTRICTION
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { string } settingsItem - Behavior name. Only the following values are supported. If other values are
     *     passed, an error will be reported.
     *     <br>- **setApn**: APN configuration, currently supported only on smartphones and tablets.
     *     <br>- **powerLongPress**: capability to open the power menu by long-pressing the power button. Currently, only
     *     smartphones and tablets are supported.
     *     <br>- **setEthernetIp**: Ethernet IP address configuration, currently supported only on PCs/2-in-1 devices.
     *     <br>- **setDeviceName**: device name configuration, currently supported only on PCs/2-in-1 devices,
     *     smartphones, and tablets. When it is disabled, the device name cannot be modified in the following settings:
     *     **About**, **Bluetooth**, and **More connectivity options** > **NearLink** on PCs/2-in-1 devices, and
     *     **About**, **Bluetooth**, and **Personal hotspot** on smartphones and tablets.
     *     <br>- **setBiometricsAndScreenLock**: screen lock password configuration, currently supported only on PCs/2-in-
     *     1 devices, smartphones, and tablets.
     * @param { boolean } restricted - Whether to disable the action. The value **true** means to disable the action, and
     *     **false** means the opposite.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 20
     * @deprecated since 26.0.0
     * @useinstead restrictions.setUserRestriction(admin: Want, settingsItem: SettingsForDevice, restricted: boolean)
     */
    function setUserRestriction(admin: Want, settingsItem: string, restricted: boolean): void;
    /**
     * Obtains the disabled status of a setting item.
     *
     * @permission ohos.permission.ENTERPRISE_SET_USER_RESTRICTION
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { string } settingsItem - Setting item.
     *     <br>- **setEthernetIp**: Ethernet IP address configuration, currently supported only on PCs/2-in-1 devices.
     *     <br>- **setDeviceName**: device name configuration, currently supported only on PCs/2-in-1 devices,
     *     smartphones, and tablets. When it is disabled, the device name cannot be modified in the following settings:
     *     **About**, **Bluetooth**, and **More connectivity options** > **NearLink** on PCs/2-in-1 devices, and
     *     **About**, **Bluetooth**, and **Personal hotspot** on smartphones and tablets.
     *     <br>- **setBiometricsAndScreenLock**: screen lock password configuration, currently supported only on PCs/2-in-
     *     1 devices, smartphones, and tablets.
     * @returns { boolean } Disabled status of the specified setting item. The value **true** means the item is disabled;
     *     the value **false** means the opposite.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 20
     * @deprecated since 26.0.0
     * @useinstead restrictions.getUserRestricted(admin: Want, settingsItem: SettingsForDevice)
     */
    function getUserRestricted(admin: Want, settingsItem: string): boolean;
    /**
     * Sets restrictions on specified user behaviors.
     *
     * @permission ohos.permission.ENTERPRISE_SET_USER_RESTRICTION
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { string } settingsItem - User behavior.
     *     <br>- **modifyWallpaper**: Modify the wallpaper, including the lock screen wallpaper and home screen wallpaper.
     * @param { number } accountId - User ID, which must be greater than or equal to 0.
     *     <br>The value should be an integer.
     *     <br>**accountId** can be obtained via APIs such as
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()}.
     * @param { boolean } restricted - Whether to disable the action. The value **true** means to disable the action, and
     *     **false** means the opposite.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 801 - Capability not supported.
     *     Failed to call the API due to limited device capabilities.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 23
     * @deprecated since 26.0.0
     * @useinstead restrictions.setUserRestrictionForAccount(admin: Want, settingsItem: SettingsForAccount, accountId: int, restricted: boolean)
     */
    function setUserRestrictionForAccount(admin: Want, settingsItem: string, accountId: number, restricted: boolean): void;
    /**
     * Obtains the disabled status of a setting item for a specified user.
     *
     * @permission ohos.permission.ENTERPRISE_SET_USER_RESTRICTION
     * @param { Want | null } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the.
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.<br>If the device has multiple MDM
     *     applications, you can pass **admin** to query the corresponding policies. If **null** is passed, the policies
     *     that actually take effect on the device are returned.
     * @param { string } settingsItem - Setting item.
     *     <br>- **modifyWallpaper**: Modify the wallpaper, including the lock screen wallpaper and home screen wallpaper.
     * @param { number } accountId - User ID, which must be greater than or equal to 0.
     *     <br>The value should be an integer.
     *     <br>**accountId** can be obtained via APIs such as
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()}.
     * @returns { boolean } Disabled status of the specified setting item. The value **true** means the item is disabled;
     *     the value **false** means the opposite.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 801 - Capability not supported.
     *     Failed to call the API due to limited device capabilities.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 23
     * @deprecated since 26.0.0
     * @useinstead restrictions.getUserRestrictedForAccount(admin: Want | null, settingsItem: SettingsForAccount, accountId: int)
     */
    function getUserRestrictedForAccount(admin: Want | null, settingsItem: string, accountId: number): boolean;
    /**
     * Enables or disables a specified device feature. Once disabled, the feature cannot be used.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_RESTRICTIONS or ohos.permission.PERSONAL_MANAGE_RESTRICTIONS
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { FeatureForDevice } feature - Device feature to be enabled or disabled.
     *     <br> **Note:** An application granted with the ohos.permission.PERSONAL_MANAGE_RESTRICTIONS permission and
     *     activated as the [BDA](docroot://mdm/mdm-kit-term.md#byod-device-admin-bdabyod) via
     *     [startAdminProvision]{@link @ohos.enterprise.adminManager:adminManager.startAdminProvision} can use this API to
     *     set the [FeatureForDevice.WIFI_P2P]{@link restrictions.FeatureForDevice} feature.
     * @param { boolean } disallow - Whether to disallow the feature. The value **true** means to disallow the feature;
     *     the value **false** means the opposite.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200010 - A conflict policy has been configured.
     * @throws { BusinessError } 9200013 - The enterprise management policy has been successfully set,
     *     but the function has not taken effect in real time.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 801 - Capability not supported.
     *     Failed to call the API due to limited device capabilities.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 24
     */
    function setDisallowedPolicy(admin: Want, feature: FeatureForDevice, disallow: boolean): void;
    /**
     * Queries whether a specified device feature is disabled.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_RESTRICTIONS or ohos.permission.PERSONAL_MANAGE_RESTRICTIONS
     * @param { Want | null } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the.
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.<br>If the device has multiple MDM
     *     applications, you can pass **admin** to query the corresponding policies. If **null** is passed, the policies
     *     that actually take effect on the device are returned.
     * @param { FeatureForDevice } feature - Device feature to be queried.
     * @returns { boolean } The value **true** indicates the device feature is disabled, and the value **false** indicates
     *     the opposite.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 801 - Capability not supported.
     *     Failed to call the API due to limited device capabilities.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 24
     */
    function getDisallowedPolicy(admin: Want | null, feature: FeatureForDevice): boolean;
    /**
     * Disallows a feature for a specified user.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_RESTRICTIONS
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { FeatureForAccount } feature - User feature to be disabled or enabled.
     *     <br>If SuperHub has been added to the user's list of non-disableable applications through the
     *     [addUserNonStopApps]{@link @ohos.enterprise.applicationManager:applicationManager.addUserNonStopApps} API,
     *     setting this parameter to **SUPER_HUB** will cause a policy conflict and error code 9200010 will be reported.
     *     In this case, call the
     *     [removeUserNonStopApps]{@link @ohos.enterprise.applicationManager:applicationManager.removeUserNonStopApps} API
     *     to remove SuperHub from the user's list of non-disableable applications to resolve the conflict.
     *     <br>When **feature** is **DISTRIBUTED_TRANSMISSION**, if the capability of distributed one-way data
     *     transmission between devices has been disabled via the
     *     [setDisallowedPolicyForAccount]{@link restrictions.setDisallowedPolicyForAccount} API, calling this API to
     *     disable the distributed management service will result in a policy conflict and error code 9200010 will be
     *     reported. You can call the [setDisallowedPolicyForAccount]{@link restrictions.setDisallowedPolicyForAccount}
     *     API to enable distributed one-way data transmission between devices to resolve the conflict.
     * @param { boolean } disallow - Whether to disallow the feature. The value **true** means to disallow the feature;
     *     the value **false** means the opposite.
     * @param { number } accountId - User ID, which must be greater than or equal to 0.
     *     <br>**accountId** can be obtained via APIs such as
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()}.
     *     <br>When **feature** is set to **SUPER_HUB**, this parameter can only be set to the ID of the current user.
     *     Otherwise, error code 9200012 will be reported.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200010 - A conflict policy has been configured.
     * @throws { BusinessError } 9200012 - Parameter verification failed.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 801 - Capability not supported.
     *     Failed to call the API due to limited device capabilities.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function setDisallowedPolicyForAccount(admin: Want, feature: FeatureForAccount, disallow: boolean, accountId: number): void;
    /**
     * Obtains the status of a feature for a specified user.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_RESTRICTIONS
     * @param { Want | null } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the.
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.<br>If the device has multiple MDM
     *     applications, you can pass **admin** to query the corresponding policies. If **null** is passed, the policies
     *     that actually take effect on the device are returned.
     * @param { FeatureForAccount } feature - User feature to be queried.
     * @param { number } accountId - User ID, which must be greater than or equal to 0.
     *     <br>**accountId** can be obtained via APIs such as
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()}.
     * @returns { boolean } The value **true** means the feature is disabled; the value **false** means the opposite.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200012 - Parameter verification failed.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 801 - Capability not supported.
     *     Failed to call the API due to limited device capabilities.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function getDisallowedPolicyForAccount(admin: Want | null, feature: FeatureForAccount, accountId: number): boolean;
    /**
     * Restricts users from modifying specified device setting items.
     *
     * @permission ohos.permission.ENTERPRISE_SET_USER_RESTRICTION
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { SettingsForDevice } settingsItem - Device setting items to be restricted from modification.
     * @param { boolean } restricted - The value **true** means to disable the action, and **false** means the opposite.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 801 - Capability not supported.
     *     Failed to call the API due to limited device capabilities.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function setUserRestriction(admin: Want, settingsItem: SettingsForDevice, restricted: boolean): void;
    /**
     * Obtains the disabled status of the specified device setting item.
     *
     * @permission ohos.permission.ENTERPRISE_SET_USER_RESTRICTION
     * @param { Want | null } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the.
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.<br>If the device has multiple MDM
     *     applications, you can pass **admin** to query the corresponding policies. If **null** is passed, the policies
     *     that actually take effect on the device are returned.
     * @param { SettingsForDevice } settingsItem - Device setting item to be queried.
     * @returns { boolean } Disabled status of the specified device setting item. The value **true** means the item is
     *     disabled; the value **false** means the opposite.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 801 - Capability not supported.
     *     Failed to call the API due to limited device capabilities.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function getUserRestricted(admin: Want | null, settingsItem: SettingsForDevice): boolean;
    /**
     * Restricts a specified user from modifying specified setting items.
     *
     * @permission ohos.permission.ENTERPRISE_SET_USER_RESTRICTION
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { SettingsForAccount } settingsItem - User setting items to be restricted from modification.
     * @param { number } accountId - User ID, which must be greater than or equal to 0.
     *     <br>The value should be an integer.
     *     <br>**accountId** can be obtained via APIs such as
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()}.
     * @param { boolean } restricted - The value **true** means to disable the action, and **false** means the opposite.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200012 - Parameter verification failed.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 801 - Capability not supported.
     *     Failed to call the API due to limited device capabilities.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function setUserRestrictionForAccount(admin: Want, settingsItem: SettingsForAccount, accountId: number, restricted: boolean): void;
    /**
     * Obtains the disabled status of a setting item for a specified user.
     *
     * @permission ohos.permission.ENTERPRISE_SET_USER_RESTRICTION
     * @param { Want | null } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the.
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.<br>If the device has multiple MDM
     *     applications, you can pass **admin** to query the corresponding policies. If **null** is passed, the policies
     *     that actually take effect on the device are returned.
     * @param { SettingsForAccount } settingsItem - User setting item to be queried.
     * @param { number } accountId - User ID, which must be greater than or equal to 0.
     *     <br>The value should be an integer.
     *     <br>**accountId** can be obtained via APIs such as
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()}.
     * @returns { boolean } Disabled status of the specified user setting item. The value **true** means the item is
     *     disabled; the value **false** means the opposite.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200012 - Parameter verification failed.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 801 - Capability not supported.
     *     Failed to call the API due to limited device capabilities.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function getUserRestrictedForAccount(admin: Want | null, settingsItem: SettingsForAccount, accountId: number): boolean;
}
export default restrictions;

```
