# @ohos.enterprise.browser.d.ts

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
 * @file Browser Management
 * @kit MDMKit
 */
import type Want from './@ohos.app.ability.Want';
/**
 * The **browser** module provides browser management, including setting, canceling, and obtaining browser policies. It
 * is applicable to scenarios such as enterprise device management, employee online behavior management, and security
 * compliance audit.
 *
 * Browser policies are a collection of rules and settings that govern how a browser behaves, ensuring security,
 * compliance, performance optimization, and a consistent user experience.
 *
 * > **NOTE**
 * >
 * > The APIs of this module can be called only by a device administrator application that is enabled. For details, see
 * > [MDM Kit Development](docroot://mdm/mdm-kit-guide.md).
 *
 * @syscap SystemCapability.Customization.EnterpriseDeviceManager
 * @since 12
 */
declare namespace browser {
    /**
     * Sets a browser sub-policy for a specified browser. This API is applicable to scenarios where an enterprise needs to
     * manage employees' browser behavior in a unified manner.
     *
     * @permission ohos.permission.ENTERPRISE_SET_BROWSER_POLICY
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { string } appId - Application ID, which uniquely identifies an application. This ID is used to specify the
     *     browser. For details, see
     *     [What Is appid](docroot://quick-start/common-problem-of-application.md#what-is-appid).
     * @param { string } policyName - Browser sub-policy name, which is agreed upon by the API caller and the specified
     *     browser. If the value is an empty string, the browser policy corresponding to **appId** is to be set.
     * @param { string } policyValue - Browser sub-policy value, which is agreed upon by the API caller and the specified
     *     browser. If the value is an empty string, the policy corresponding to the policy name is removed.
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
    function setPolicySync(admin: Want, appId: string, policyName: string, policyValue: string): void;
    /**
     * Obtains the browser policy by app ID.
     *
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { string } appId - Application ID, which is used to specify the browser.
     * @returns { string } Browser policy obtained.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 12
     */
    function getPoliciesSync(admin: Want, appId: string): string;
    /**
     * Obtains the policy set for a specified browser based on **appid**. This API is applicable to scenarios where the
     * current browser policy configuration needs to be queried, for example, displaying policy details in an enterprise
     * device administrator application and verifying whether a policy has taken effect.
     *
     * @param { Want | null } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the.
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.<br>If the device has multiple MDM
     *     applications, you can pass **admin** to query the corresponding policies. If **null** is passed, the policies
     *     that actually take effect on the device are returned.
     * @param { string } appId - Application ID, which is used to specify the browser. For details, see
     *     [What is appId?](docroot://quick-start/common-problem-of-application.md#what-is-appid).
     * @returns { string } Browser policy obtained.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function getPoliciesSync(admin: Want | null, appId: string): string;
    /**
     * Sets a browser policy for a specified browser. This API is applicable to scenarios where an enterprise needs to
     * manage employees' browser behavior in a unified manner, such as configuring browser security policies. After the
     * setting is successful, the system common event
     * [COMMON_EVENT_MANAGED_BROWSER_POLICY_CHANGED](docroot://reference/apis-basic-services-kit/common_event/commonEventManager-definitions.md#common_event_managed_browser_policy_changed)
     * is released.
     *
     * > **NOTE**
     * >
     * > In multi-MDM application scenarios, once a policy for a specific browser is configured and takes effect by the
     * > first admin, it can no longer be configured by other admins.
     *
     * @permission ohos.permission.ENTERPRISE_SET_BROWSER_POLICY
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { string } bundleName - Application bundle name, which is used to specify the browser. It uniquely
     *     identifies an application.
     * @param { string } policyName - Browser policy name, which is agreed upon by the API caller and the specified
     *     browser.
     * @param { string } policyValue - Browser policy value. If the value is an empty string, the policy corresponding to
     *     the policy name is removed.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 15
     */
    function setManagedBrowserPolicy(admin: Want, bundleName: string, policyName: string, policyValue: string): void;
    /**
     * Obtains the policy of a specified browser based on the application bundle name. This API is applicable to scenarios
     * where the current browser policy configuration needs to be queried, for example, displaying policy details in an
     * enterprise device administrator application and verifying whether a policy has taken effect.
     *
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { string } bundleName - Application bundle name, which is used to specify the browser.
     * @returns { ArrayBuffer } Browser policy obtained.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 15
     */
    function getManagedBrowserPolicy(admin: Want, bundleName: string): ArrayBuffer;
    /**
     * Obtains the browser policy version of the current device.
     *
     * @returns { string } Browser policy version.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 15
     */
    function getSelfManagedBrowserPolicyVersion(): string;
    /**
     * Obtains the browser policy of the current device.
     *
     * @returns { ArrayBuffer } Browser policy obtained.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 15
     */
    function getSelfManagedBrowserPolicy(): ArrayBuffer;
}
export default browser;

```
