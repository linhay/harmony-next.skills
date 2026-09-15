# @ohos.enterprise.locationManager.d.ts

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
 * @file Location Service Management
 * @kit MDMKit
 */
import type Want from './@ohos.app.ability.Want';
/**
 * The **locationManager** module provides location service management capabilities for devices, including setting and
 * obtaining the location service policy.
 *
 * **Use cases:**
 * This module is applicable to enterprise device management scenarios, where administrators can centrally manage
 * location service policies for devices.
 *
 * > **NOTE**
 * >
 * > The APIs of this module can be called only by a device administrator application that is enabled. For details, see
 * > [MDM Kit Development](docroot://mdm/mdm-kit-guide.md).
 *
 * @syscap SystemCapability.Customization.EnterpriseDeviceManager
 * @stagemodelonly
 * @since 12
 */
declare namespace locationManager {
    /**
     * Enumerates the location service policies.
     *
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 12
     */
    export enum LocationPolicy {
        /**
         * Default policy. The location service is not restricted and can be controlled by the user.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        DEFAULT_LOCATION_SERVICE = 0,
        /**
         * The location service is disabled. This policy applies to scenarios where the location service needs to be
         * disabled, such as confidential areas and conference rooms.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        DISALLOW_LOCATION_SERVICE = 1,
        /**
         * The location service is forcibly enabled. This policy applies to scenarios where the location service needs to be
         * available, such as logistics tracking and field management.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 12
         */
        FORCE_OPEN_LOCATION_SERVICE = 2
    }
    /**
     * Sets a location service policy. This API can be used in enterprise management and control scenarios. For example,
     * you can disable the location service in confidential areas to protect information security, or forcibly enable the
     * location service in logistics and distribution applications to track device locations.
     *
     * > **NOTE**
     * >
     * > - Disabled: Set this option when privacy protection or power saving is required.
     * >
     * > - Forced on: Set this option in scenarios such as device security tracking and asset management.
     * >
     * > - Default: This option removes policy restrictions and allows the user to control the setting independently.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_LOCATION
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { LocationPolicy } policy - Location service policy to set. The value can be any of the following:
     *     <br>- **0**: The default policy is used.
     *     <br>- **1**: The location service is disabled.
     *     <br>- **2**: The location service is forcibly on.
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
    function setLocationPolicy(admin: Want, policy: LocationPolicy): void;
    /**
     * Queries the location service policy.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_LOCATION
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @returns { LocationPolicy } Enumerated value of the location service policy. **0**: The default policy is used.
     *     **1**: The location service is disabled. **2**: The location service is forcibly enabled.
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
    function getLocationPolicy(admin: Want): LocationPolicy;
    /**
     * Queries the location service policy. This API can be used in enterprise device administrator applications to check
     * the current location service policy state of the device, for policy compliance verification or state confirmation
     * before policy adjustment. It is suitable for scenarios such as confirming the current policy configuration, reading
     * the policy state when the device administrator application starts, and checking the policy when troubleshooting
     * location service issues.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_LOCATION
     * @param { Want | null } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the.
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.<br>If the device has multiple MDM
     *     applications, you can pass **admin** to query the corresponding policies. If **null** is passed, the policies
     *     that actually take effect on the device are returned.
     * @returns { LocationPolicy } Enumerated value of the location service policy. **0**: The default policy is used.
     *     **1**: The location service is disabled. **2**: The location service is forcibly on.
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
    function getLocationPolicy(admin: Want | null): LocationPolicy;
}
export default locationManager;

```
