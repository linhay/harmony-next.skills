# @ohos.enterprise.adminManager.d.ts

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
 * @file Administrator Permission Management
 * @kit MDMKit
 */
import common from '@ohos.app.ability.common';
import type Want from './@ohos.app.ability.Want';
/**
 * The **adminManager** module provides administrator permission management capabilities for enterprise MDM
 * applications, including enabling or disabling administrator permissions, subscribing to events, delegating
 * applications, and granting permissions.
 *
 * > **NOTE**
 * >
 * > The APIs of this module can be called only by a device administrator application. For details, see
 * > [MDM Kit Development](docroot://mdm/mdm-kit-guide.md).
 *
 * @syscap SystemCapability.Customization.EnterpriseDeviceManager
 * @since 12
 */
declare namespace adminManager {
    /**
     * Defines the policy type for the trustlist or blocklist.
     *
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 20
     */
    export enum Policy {
        /**
         * Blocklist.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 20
         */
        BLOCK_LIST = 0,
        /**
         * Trustlist.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 20
         */
        TRUST_LIST = 1
    }
    /**
     * Enumerates the types of device administrator applications.
     *
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @since 15
     */
    export enum AdminType {
        /**
         * BYOD device administrator application.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @since 15
         */
        ADMIN_TYPE_BYOD = 0x02
    }
    /**
     * Enumerates the system management events that can be subscribed to.
     *
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @since 12
     */
    export enum ManagedEvent {
        /**
         * An application is installed.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @since 12
         */
        MANAGED_EVENT_BUNDLE_ADDED = 0,
        /**
         * An application is uninstalled.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @since 12
         */
        MANAGED_EVENT_BUNDLE_REMOVED = 1,
        /**
         * An application is started.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @since 12
         */
        MANAGED_EVENT_APP_START = 2,
        /**
         * An application is stopped.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @since 12
         */
        MANAGED_EVENT_APP_STOP = 3,
        /**
         * The system is updated.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @since 12
         */
        MANAGED_EVENT_SYSTEM_UPDATE = 4,
        /**
         * An account is created.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @since 18
         */
        MANAGED_EVENT_ACCOUNT_ADDED = 5,
        /**
         * An account is switched.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @since 18
         */
        MANAGED_EVENT_ACCOUNT_SWITCHED = 6,
        /**
         * An account is removed.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @since 18
         */
        MANAGED_EVENT_ACCOUNT_REMOVED = 7,
        /**
         * The startup wizard is complete.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 24
         */
        MANAGED_EVENT_STARTUP_GUIDE_COMPLETED = 8,
        /**
         * Device startup is complete.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 24
         */
        MANAGED_EVENT_BOOT_COMPLETED = 9,
        /**
         * Application update event.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        MANAGED_EVENT_BUNDLE_UPDATED = 10,
        /**
         * Policy change event. Only super device administrator applications can subscribe to this event. If other types of
         * device administrator applications attempt to subscribe, error code 9200002 is returned.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        MANAGED_EVENT_POLICIES_CHANGED = 11
    }
    /**
     * Disables a device administrator application for the specified user. This API uses a promise to return the result.
     * After this API is called successfully, the specified device administrator application will be deactivated and no
     * longer have the device management capability.
     *
     * @permission ohos.permission.MANAGE_ENTERPRISE_DEVICE_ADMIN [since 12 - 19]
     * @permission ohos.permission.MANAGE_ENTERPRISE_DEVICE_ADMIN or
     *     ohos.permission.START_PROVISIONING_MESSAGE [since 20 - 22]
     * @permission ohos.permission.MANAGE_ENTERPRISE_DEVICE_ADMIN or ohos.permission.START_PROVISIONING_MESSAGE
     *     or ohos.permission.ENTERPRISE_DEACTIVATE_DEVICE_ADMIN [since 23]
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application. When deactivating the BYOD device
     *     administrator application, you can pass only the **EnterpriseAdminExtensionAbility** component of the current
     *     application.
     * @param { number } [userId] - User ID, which must be greater than or equal to 0.
     *     <br> - If **userId** is passed in, this API applies to the specified user.
     *     <br> - If **userId** is not passed in, this API applies to the current user.
     * @returns { Promise<void> } Promise that returns no value. If the operation fails, an error object will be thrown.
     * @throws { BusinessError } 9200005 - Failed to deactivate the administrator application of the device.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 12
     */
    function disableAdmin(admin: Want, userId?: number): Promise<void>;
    /**
     * Checks whether the current application is activated as a BYOD device administrator application based on the
     * **EnterpriseAdminExtensionAbility** component.
     *
     * @permission ohos.permission.START_PROVISIONING_MESSAGE
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application. Only the
     *     **EnterpriseAdminExtensionAbility** component of the current application can be passed.
     * @returns { boolean } The value **true** indicates the application is activated as a BYOD device administrator
     *     application, and the value **false** indicates the opposite.
     * @throws { BusinessError } 9200012 - Parameter verification failed.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 20
     */
    function isByodAdmin(admin: Want): boolean;
    /**
     * Subscribes to system management events. After the call is successful, the device administrator application will
     * receive a notification when a subscribed system management event occurs.
     *
     * Since API version 26.0.0, error code 9200002 is returned when a non-super device administrator application calls
     * this API to subscribe to the [MANAGED_EVENT_POLICIES_CHANGED]{@link adminManager.ManagedEvent} event.
     *
     * @permission ohos.permission.ENTERPRISE_SUBSCRIBE_MANAGED_EVENT
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { Array<ManagedEvent> } managedEvents - Array of system management events to be subscribed to. Each element
     *     in the array is a value from the [ManagedEvent]{@link adminManager.ManagedEvent} enumeration. Multiple event
     *     types can be subscribed to, such as application installation/uninstallation/start/stop events, system update
     *     events, and more.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the
     *     device. [since 26.0.0]
     * @throws { BusinessError } 9200008 - The specified system event is invalid.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 12
     */
    function subscribeManagedEventSync(admin: Want, managedEvents: Array<ManagedEvent>): void;
    /**
     * Unsubscribes from system management events. After the API is successfully called, no notifications for the
     * unsubscribed system management events will be received.
     *
     * @permission ohos.permission.ENTERPRISE_SUBSCRIBE_MANAGED_EVENT
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { Array<ManagedEvent> } managedEvents - Array of system management events to be unsubscribed from. Each
     *     element in the array is a value from the [ManagedEvent]{@link adminManager.ManagedEvent} enumeration. The input
     *     event types must be the same as those passed during subscription.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200008 - The specified system event is invalid.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 12
     */
    function unsubscribeManagedEventSync(admin: Want, managedEvents: Array<ManagedEvent>): void;
    /**
     * Delegates other applications to set device management policies. The applications must request the permissions
     * required.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_DELEGATED_POLICY
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { string } bundleName - Bundle name of the delegated application. The distribution type of the delegated
     *     application must be **enterprise_normal** or **enterprise_mdm**. You can call the
     *     [getBundleInfoForSelf]{@link @ohos.bundle.bundleManager:bundleManager.getBundleInfoForSelf} API to query the
     *     [BundleInfo]{@link ./bundleManager/BundleInfo} of the application, where
     *     **BundleInfo.appInfo.appDistributionType** indicates the distribution type.
     * @param { Array<string> } policies -
     *     [Delegable policy list](docroot://mdm/mdm-kit-appendix.md#delegable-policy-list).
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200009 - Failed to grant the permission to the application.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 14
     */
    function setDelegatedPolicies(admin: Want, bundleName: string, policies: Array<string>): void;
    /**
     * Queries the list of policies that can be accessed by the delegated application.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_DELEGATED_POLICY
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { string } bundleName - Bundle name of the delegated application. The distribution type of the delegated
     *     application must be **enterprise_normal** or **enterprise_mdm**. You can call the
     *     [getBundleInfoForSelf]{@link @ohos.bundle.bundleManager:bundleManager.getBundleInfoForSelf} API to query the
     *     [BundleInfo]{@link ./bundleManager/BundleInfo} of the application, where
     *     **BundleInfo.appInfo.appDistributionType** indicates the distribution type.
     * @returns { Array<string> } Delegation policy list.
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
    function getDelegatedPolicies(admin: Want, bundleName: string): Array<string>;
    /**
     * Queries the delegated applications that can access a delegation policy and output the list of delegated
     * applications.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_DELEGATED_POLICY
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { string } policy - Delegation policy.
     * @returns { Array<string> } List of delegated applications.
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
    function getDelegatedBundleNames(admin: Want, policy: string): Array<string>;
    /**
     * Enables the device administrator application to open a page for the BYOD administrator to perform activation.
     *
     * @permission ohos.permission.START_PROVISIONING_MESSAGE
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { AdminType } type - Type of the activated device administrator application. Only the **ADMIN_TYPE_BYOD**
     *     type is supported.
     * @param { common.Context } context - Context information of the administrator application.
     * @param { Record<string, string> } parameters - Custom parameters. The key value must contain **activateId** and may
     *     optionally include **customizedInfo** and **localDeactivationPolicy**.
     *     <br>- **activateId**: project activation ID.
     *     <br>- **customizedInfo**: enterprise-defined information.
     *     <br>- **localDeactivationPolicy**: local deactivation delay (unit: hour). This parameter is supported since API
     *     version 22.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 15
     */
    function startAdminProvision(admin: Want, type: AdminType, context: common.Context, parameters: Record<string, string>): void;
    /**
     * Enables a [DA](docroot://mdm/mdm-kit-term.md#device-admin-da) application by a
     * [SDA](docroot://mdm/mdm-kit-term.md#super-device-admin-sda) application. This API uses a promise to return the
     * result. After the API is successfully called, the specified DA application is enabled and granted device management
     * capabilities. This API can be called only by super device administrator applications.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_DEVICE_ADMIN
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @returns { Promise<void> } Promise that returns no value. If the operation fails, an error object will be thrown.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200003 - The administrator ability component is invalid.
     * @throws { BusinessError } 9200004 - Failed to activate the administrator application of the device.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 801 - Capability not supported.
     *     Failed to call the API due to limited device capabilities.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 23
     */
    function enableDeviceAdmin(admin: Want): Promise<void>;
    /**
     * Disables a [DA](docroot://mdm/mdm-kit-term.md#device-admin-da) application by a
     * [SDA](docroot://mdm/mdm-kit-term.md#super-device-admin-sda) application. This API uses a promise to return the
     * result. After this API is called successfully, the specified device administrator application is disabled and no
     * longer has the device management capability. This API can be called only by super device administrator
     * applications.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_DEVICE_ADMIN
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @returns { Promise<void> } Promise that returns no value. If the operation fails, an error object will be thrown.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200005 - Failed to deactivate the administrator application of the device.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 801 - Capability not supported.
     *     Failed to call the API due to limited device capabilities.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 23
     */
    function disableDeviceAdmin(admin: Want): Promise<void>;
    /**
     * Allows an MDM application to enable itself in scenarios where it is not pre-enabled on the enterprise device. This
     * API supports enablement of the MDM application itself only, and cannot be used to enable other MDM applications.
     * The supported enablement types include super device administrator application and normal device administrator
     * application.
     *
     * @permission ohos.permission.ENTERPRISE_ACTIVATE_DEVICE_ADMIN
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { string } credential - Enablement credential.
     * @throws { BusinessError } 9200003 - The administrator ability component is invalid.
     * @throws { BusinessError } 9200004 - Failed to activate the administrator application of the device.
     * @throws { BusinessError } 9200012 - Parameter verification failed.
     * @throws { BusinessError } 9200017 - The self-activation credential of the enterprise device administrator
     *     is invalid.
     * @throws { BusinessError } 9200018 - This device is not an enterprise device.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 801 - Capability not supported.
     *     Failed to call the API due to limited device capabilities.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function enableSelfDeviceAdmin(admin: Want, credential: string): void;
}
export default adminManager;

```
