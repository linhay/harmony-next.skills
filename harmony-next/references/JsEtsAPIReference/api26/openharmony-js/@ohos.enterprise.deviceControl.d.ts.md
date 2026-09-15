# @ohos.enterprise.deviceControl.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022-2024 Huawei Device Co., Ltd.
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
 * @file Device Control Management
 * @kit MDMKit
 */
import type Want from './@ohos.app.ability.Want';
/**
 * This module provides device control capabilities for enterprise device management scenarios. Administrators can
 * remotely control devices through this module, including operations such as device restart, shutdown, screen lock, and
 * factory reset, helping enterprises achieve unified device management and security control.
 *
 * > **NOTE**
 * >
 * > The APIs of this module can be called only by a device administrator application that is enabled. For details, see
 * > [MDM Kit Development](docroot://mdm/mdm-kit-guide.md).
 *
 * @syscap SystemCapability.Customization.EnterpriseDeviceManager
 * @since 12
 */
declare namespace deviceControl {
    /**
     * Defines the device operation.
     *
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    enum Operation {
        /**
         * Disk erasure. After this API is called, the device immediately performs a disk erasure operation. Once completed,
         * all data on the device will be erased and cannot be recovered. To protect against data loss caused by potential
         * application attacks, enterprises should implement robust security measures for their applications. It is support
         * only on PCs/2-in-1 devices.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        DISK_ERASURE = 0
    }
    /**
     * Allows administrators to perform operations such as factory reset, restart, shutdown, and screen lock on devices.
     * For example, in enterprise device management scenarios, administrators can remotely control employee devices to
     * perform factory reset, restart, shutdown, or screen lock operations.
     *
     * @permission ohos.permission.ENTERPRISE_OPERATE_DEVICE
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { string } operate - Operation to be performed, which can be any of the following: Only the following
     *     operations are supported:
     *     <br>- **resetFactory**: restore device factory settings. After this API is called, the device will be restored
     *     to factory settings immediately. Once the restoration is complete, all device data will be erased and cannot be
     *     restored. To protect against data loss caused by potential application attacks, enterprises should implement
     *     robust security measures for their applications. If factory reset has been disabled via
     *     [setDisallowedPolicy]{@link @ohos.enterprise.restrictions:restrictions.setDisallowedPolicy}, enable it first.
     *     <br>- **reboot**: restart devices.
     *     <br>- **shutDown**: shut down devices.
     *     <br>- **lockScreen**: lock the device screen.
     * @param { string } [addition] - Additional parameter for the operation. This parameter is reserved and
     *     does not need to be passed.
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
    function operateDevice(admin: Want, operate: string, addition?: string): void;
    /**
     * Allows the administrator to operate devices, for example, erasing disks.
     *
     * @permission ohos.permission.ENTERPRISE_OPERATE_DEVICE
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { Operation } operation - Operation to be performed, which can be any of the following:
     * @param { string } [addition] - Additional parameter for the operation. When the operation type is disk erasure, the
     *     additional parameter is the sandbox path of the image. If a message needs to be displayed to the user after the
     *     disk erasure is successfully completed, this parameter can be set to deliver the information. The image size
     *     must be less than 5 KB (a QR code image is recommended). The length limit is 1024 bytes.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200010 - A conflict policy has been configured.
     * @throws { BusinessError } 9200012 - Parameter verification failed.
     * @throws { BusinessError } 9201048 - Failed to operate the device.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 801 - Capability not supported.
     *     Failed to call the API due to limited device capabilities.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function operateDevice(admin: Want, operation: Operation, addition?: string): void;
}
export default deviceControl;

```
