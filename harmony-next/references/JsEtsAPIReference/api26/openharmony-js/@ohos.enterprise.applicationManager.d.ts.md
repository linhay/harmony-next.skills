# @ohos.enterprise.applicationManager.d.ts

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
 * @file Application Management
 * @kit MDMKit
 */
import type Want from './@ohos.app.ability.Want';
import common from './@ohos.enterprise.common';
import statistics from './@ohos.net.statistics';
/**
 * This module provides application management capabilities, including managing the application running blocklist,
 * application running trustlist, auto-startup application list, keep-alive application list, non-stoppable application
 * list, background freeze-exempt application list, notification trustlist, and cross-device application trustlist. It
 * is suitable for enterprise device management scenarios, enabling control over application running permissions, auto-
 * startup management, keep-alive application management, and more, thereby enhancing enterprise device security and
 * compliance.
 *
 * > **NOTE**
 * >
 * > The APIs of this module can be called only by a device administrator application that is enabled. For details, see
 * > [MDM Kit Development](docroot://mdm/mdm-kit-guide.md). The
 * > [applicationManager.isAppKioskAllowed]{@link applicationManager.isAppKioskAllowed} API is available to all
 * > applications.
 *
 * @syscap SystemCapability.Customization.EnterpriseDeviceManager
 * @since 12
 */
declare namespace applicationManager {
    /**
     * Defines the features of the kiosk mode.
     *
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 20
     */
    enum KioskFeature {
        /**
         * Allow access to the notification center (by swiping down from the upper left corner with one finger).
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 20
         */
        ALLOW_NOTIFICATION_CENTER = 1,
        /**
         * Allow access to the control panel (by swiping down from the upper right corner with one finger).
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 20
         */
        ALLOW_CONTROL_CENTER = 2,
        /**
         * Allow access to the recent task bar (by swiping up from the bottom with one finger and holding).
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 24
         */
        ALLOW_GESTURE_CONTROL = 3,
        /**
         * Allow access to the side dock (by swiping inward from the edge with one finger and holding).
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 24
         */
        ALLOW_SIDE_DOCK = 4
    }
    /**
     * Describes information about an application in the shortcut bar.
     *
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 24
     */
    interface DockInfo {
        /**
         * Bundle name of the application.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 24
         */
        bundleName: string;
        /**
         * Ability name of the application.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 24
         */
        abilityName: string;
        /**
         * Location index of the application in the shortcut bar.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 24
         */
        index: number;
    }
    /**
     * Distributed service type.
     *
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    enum ServiceType {
        /**
         * Collaboration service. Applications allowed to use the collaboration service can launch pages of other
         * applications across devices and transmit data to them by using the APIs in
         * [UIAbilityContext]{@link ./application/UIAbilityContext:UIAbilityContext} or
         * [UIExtensionContext]{@link ./application/UIExtensionContext:UIExtensionContext}, or by using the method in
         * [Cross-Device UIAbility Connection Development](docroot://distributedservice/abilityconnectmanager-guidelines.md).
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        COLLABORATION_SERVICE = 0
    }
    /**
     * Application bundle statistics.
     *
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    interface BundleStatsInfo {
        /**
         * Bundle name of the application.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        bundleName: string;
        /**
         * Index of the application clone. The value is an integer greater than or equal to 0.
         * You can call [getAppCloneIdentity]{@link @ohos.bundle.bundleManager:bundleManager.getAppCloneIdentity} of @
         * ohos.bundle.bundleManager to obtain the index.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        appIndex: number;
        /**
         * Total duration that the ability runs in the foreground, in milliseconds.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        abilityInFgTotalTime: number;
    }
    /**
     * Defines the application window state information.
     *
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    interface WindowStateInfo {
        /**
         * Application window ID.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        windowId: number;
        /**
         * Application window name.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        name: string;
        /**
         * Application window state.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        state: WindowState;
        /**
         * Whether the application window is displayed on the bottom dock. For application on the bottom dock on tablets in
         * PC mode and PCs/2-in-1 devices. For other devices, **false** is returned.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        isOnDock: boolean;
    }
    /**
     * Enumerates application window states.
     *
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    enum WindowState {
        /**
         * The window has been created but is currently unavailable.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        DISCONNECT = 0,
        /**
         * The window has been created and is available for use.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        CONNECT = 1,
        /**
         * Foreground state, indicating that the window has entered the foreground display. This is a transitional state.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        FOREGROUND = 2,
        /**
         * Foreground active state, indicating that the window is currently displayed in the foreground.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        ACTIVE = 3,
        /**
         * Foreground inactive state, indicating that the window is about to enter the background. This is a transitional
         * state.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        INACTIVE = 4,
        /**
         * Background state, indicating that the window has been moved to the background and is not visible.
         *
         * @syscap SystemCapability.Customization.EnterpriseDeviceManager
         * @stagemodelonly
         * @since 26.0.0
         */
        BACKGROUND = 5
    }
    /**
     * Adds applications to the application running blocklist. Applications added to the blocklist are not allowed to run
     * under the current or specified user. Since API version 21, if the application running trustlist
     * [addAllowedRunningBundles]{@link applicationManager.addAllowedRunningBundles} is not empty, the application running
     * blocklist cannot be added via this API. Otherwise, the error code 9200010 is reported.
     *
     * > **NOTE**
     * >
     * > If a specified application is running, the system will immediately terminate the application process once it is
     * > added to the blocklist.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { Array<string> } appIds - IDs of the applications to add.
     *     <br>**Note**: From API version 21 onwards, the
     *     [appId](docroot://quick-start/common-problem-of-application.md#what-is-appid) and
     *     [appIdentifier](docroot://quick-start/common-problem-of-application.md#what-is-appidentifier) of the app can be
     *     passed. **appIdentifier** is recommended. In API version 20 and earlier versions, only **appId** can be passed.
     *     <br>Value range:
     *     <br> The total number of entries in this list for a single user must not exceed 200. For example, if 50 entries
     *     have been set for user 100 and none for user 101, user 100 can add 150 more entries, while user 101 can add up
     *     to 200 entries.
     * @param { number } [accountId] - Account ID, which must be greater than or equal to 0.
     *     <br> You can call
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()} of @
     *     ohos.account.osAccount to obtain the ID.
     *     <br> - If **accountId** is passed in, this API applies to the specified user.
     *     <br> - If **accountId** is not passed in, this API applies to the current user.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 9200010 - A conflict policy has been configured. [since 21]
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 12
     */
    function addDisallowedRunningBundlesSync(admin: Want, appIds: Array<string>, accountId?: number): void;
    /**
     * Removes applications from the application running blocklist of the current or specified user. After an application
     * is removed, it is allowed to run under the current or specified user.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { Array<string> } appIds - IDs of the applications to add.
     *     <br>Note: Since API version 21, elements in the array can use **appId** and **appIdentifier**. Only the input
     *     **appId** or **appIdentifier** is removed. **appIdentifier** or **appId** of the same app will not be removed.
     *     In API version 20 and earlier versions, only **appId** can be transferred.
     * @param { number } [accountId] - Account ID, which must be greater than or equal to 0.
     *     <br> You can call
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()} of @
     *     ohos.account.osAccount to obtain the ID.
     *     <br> - If **accountId** is passed in, this API applies to the specified user.
     *     <br> - If **accountId** is not passed in, this API applies to the current user.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @StageModelOnly
     * @since 12
     */
    function removeDisallowedRunningBundlesSync(admin: Want, appIds: Array<string>, accountId?: number): void;
    /**
     * Obtains applications that are not allowed to run by the current user or specified user.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { number } [accountId] - Account ID, which must be greater than or equal to 0.
     *     <br> You can call
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()} of @
     *     ohos.account.osAccount to obtain the ID.
     *     <br> - If **accountId** is passed in, this API applies to the specified
     *     user.
     *     <br> - If **accountId** is not passed in, this API applies to the current user.
     * @returns { Array<string> } Applications that are not allowed to run by the current user or specified user.
     *     <br>Note: For API version 20 and earlier versions, the return value is the **appId** list. In API version 21
     *     and
     *     later versions, the return value is the **appId** or **appIdentifier** list.
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
    function getDisallowedRunningBundlesSync(admin: Want, accountId?: number): Array<string>;
    /**
     * Obtains the application running blocklist of the current user or specified user.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want | null } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the.
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.<br>If the device has multiple MDM
     *     applications, you can pass **admin** to query the corresponding policies. If **null** is passed, the policies
     *     that actually take effect on the device are returned.
     * @param { number } [accountId] - Account ID, which must be greater than or equal to 0.
     *     <br> You can call
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()}
     *     of @ohos.account.osAccount to obtain the ID.
     *     <br> - If **accountId** is passed in, this API applies to the specified user.
     *     <br> - If **accountId** is not passed in, this API applies to the current user.
     * @returns { Array<string> } Application running blocklist of the current user or specified user.
     *     <br>Note: the return value is the **appId** or **appIdentifier** list.
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
    function getDisallowedRunningBundlesSync(admin: Want | null, accountId?: number): Array<string>;
    /**
     * Adds applications to the application running trustlist. Only applications in the trustlist are allowed to run under
     * the specified user.
     *
     * > **NOTE**
     * >
     * > 1. Most APIs provided by MDM Kit are available only to MDM applications. When using this API, add the MDM
     * > application to the application running trustlist. Otherwise, the MDM application will be prohibited from running,
     * > blocking the API call. For details about whether the API is open only to MDM applications, see the module
     * > description.
     * >
     * > 2. If the application running blocklist is not empty, this API cannot be used to add applications to the running
     * > trustlist. Otherwise, the error code 9200010 is reported. APIs related to the application running blocklist
     * > include [addDisallowedRunningBundlesSync]{@link applicationManager.addDisallowedRunningBundlesSync},
     * > [addDisallowedRunningBundles]{@link applicationManager.addDisallowedRunningBundles},
     * > [addDisallowedRunningBundles]{@link applicationManager.addDisallowedRunningBundles}, and
     * > [addDisallowedRunningBundles]{@link applicationManager.addDisallowedRunningBundles}.
     * >
     * > 3. This API only takes effect for third-party applications. System applications are not subject to this list and
     * > are allowed to run by default.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { Array<string> } appIdentifiers - Array of application
     *     [unique identifiers](docroot://quick-start/common-problem-of-application.md#what-is-appidentifier). You can
     *     obtain **bundleInfo.signatureInfo.appIdentifier** through the
     *     [bundleManager.getInstalledBundleList]{@link @ohos.enterprise.bundleManager:bundleManager.getInstalledBundleList}
     *     API.
     *     <br>Value range:
     *     <br> - The total number of entries in this list for a single user must not exceed 200. For example, if 50
     *     entries have been set for user 100 and none for user 101, user 100 can add 150 more entries, while user 101 can
     *     add up to 200 entries.
     * @param { number } accountId - Account ID, which must be greater than or equal to 0.
     *     <br> You can call
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()} of @
     *     ohos.account.osAccount to obtain the ID.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200010 - A conflict policy has been configured.
     * @throws { BusinessError } 9200012 - Parameter verification failed.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 21
     */
    function addAllowedRunningBundles(admin: Want, appIdentifiers: Array<string>, accountId: number): void;
    /**
     * Removes applications from the application running trustlist of the specified user. After an application is removed,
     * it is not allowed to run under the current or specified user.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { Array<string> } appIdentifiers - Array of unique identifiers of an app. You can obtain
     *     **bundleInfo.signatureInfo.appIdentifier** through the
     *     [bundleManager.getInstalledBundleList]{@link @ohos.enterprise.bundleManager:bundleManager.getInstalledBundleList}
     *     API. Value range: The array length cannot exceed 200.
     * @param { number } accountId - Account ID, which must be greater than or equal to 0.
     *     <br> You can call
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()} of @
     *     ohos.account.osAccount to obtain the ID.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200012 - Parameter verification failed.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 21
     */
    function removeAllowedRunningBundles(admin: Want, appIdentifiers: Array<string>, accountId: number): void;
    /**
     * Obtains the list of applications allowed to run by a specified user.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { number } accountId - Account ID.
     *     <br>The value must be an integer greater than or equal to 0.
     *     <br> You can call
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()}
     *     of @ohos.account.osAccount to obtain the ID.
     * @returns { Array<string> } List of applications allowed to run by a specified user.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 21
     */
    function getAllowedRunningBundles(admin: Want, accountId: number): Array<string>;
    /**
     * Obtains the application running trustlist of a specified user.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want | null } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the.
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.<br>If the device has multiple MDM
     *     applications, you can pass **admin** to query the corresponding policies. If **null** is passed, the policies
     *     that actually take effect on the device are returned.
     * @param { number } accountId - Account ID, which must be greater than or equal to 0.
     *     <br> You can call
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()}
     *     of @ohos.account.osAccount to obtain the ID.
     * @returns { Array<string> } List of applications allowed to run by a specified user.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function getAllowedRunningBundles(admin: Want | null, accountId: number): Array<string>;
    /**
     * Adds the auto-start applications for the current user. Applications added to the auto-start list via this API
     * cannot be manually disabled for auto-start by users on the device. However, they can be
     * removed from the auto-start list using the [removeAutoStartApps]{@link applicationManager.removeAutoStartApps} API.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { Array<Want> } autoStartApps - Array of auto-start applications. The maximum array length is 10. For
     *     example, if there are already 5 applications in the list, a maximum of 5 more can be added via this API.
     *     **Want** must contain **bundleName** and **abilityName**. The ability can be UIAbility or
     *     ServiceExtensionAbility. If the value of **exported** in the
     *     [abilities](docroot://quick-start/module-configuration-file.md#abilities) tag is **false**, the ability cannot
     *     be started. Since API version 24, you can specify whether to hide the UI when applications automatically start
     *     upon device startup by setting **isHiddenStart** in the **parameters** attribute of Want. The value **true**
     *     indicates that yes, and the value **false** indicates no. The default value is **false**. If the **true** value
     *     is used, the applications must be integrated with the status bar. Otherwise, the auto-
     *     start setting fails. (If only one application is set to hide the UI upon auto-start but the application is not
     *     integrated with the status bar, error 401 is reported. This API returns success as long as one application is
     *     successfully set.) After the setting is successful, the applications do not display the UI but their UI
     *     processes exist. The capability of hiding the UI is available only on PCs/2-in-1 devices and tablets in PC
     *     mode.
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
    function addAutoStartApps(admin: Want, autoStartApps: Array<Want>): void;
    /**
     * Adds a list of applications that automatically start upon device startup for a specified user, and sets whether to
     * prohibit the user from manually canceling application auto-start.
     *
     * Applications can be added to the auto-start list via this API and the
     * [addAutoStartApps]{@link applicationManager.addAutoStartApps} API. Settings from both APIs can take effect
     * simultaneously. For a single user, the auto-start list supports a maximum of 10 applications. For example, if there
     * are already 3 applications in the current list, a maximum of 7 more can be added for the user via this API.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { Array<Want> } autoStartApps - Array of auto-start applications. The array can contain a maximum of 10
     *     applications. **Want** must contain **bundleName** and **abilityName**. The ability can be UIAbility or
     *     ServiceExtensionAbility. If the value of **exported** in the
     *     [abilities](docroot://quick-start/module-configuration-file.md#abilities) tag is **false**, the ability cannot
     *     be started. Since API version 24, you can specify whether to hide the UI when applications automatically start
     *     upon device startup by setting **isHiddenStart** in the **parameters** attribute of Want. The value **true**
     *     indicates that yes, and the value **false** indicates no. The default value is **false**. If the **true** value
     *     is used, the applications must be integrated with the status bar. Otherwise, the auto-
     *     start setting fails. (If only one application is set to hide the UI upon auto-start but the application is not
     *     integrated with the status bar, error 401 is reported. This API returns success as long as one application is
     *     successfully set.) After the setting is successful, the applications do not display the UI but their UI
     *     processes exist. The capability of hiding the UI is available only on PCs/2-in-1 devices and tablets in PC
     *     mode.
     * @param { number } accountId - Account ID, which must be greater than or equal to 0.
     *     <br> You can call
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()} of @
     *     ohos.account.osAccount to obtain the ID.
     * @param { boolean } disallowModify - Whether to prohibit the user from manually disabling application auto-start.
     *     The value **true** indicates yes and the value **false** indicates no.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 20
     */
    function addAutoStartApps(admin: Want, autoStartApps: Array<Want>, accountId: number, disallowModify: boolean): void;
    /**
     * Checks whether a specified user is prohibited from canceling application auto-start.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { Want } autoStartApp - Auto-start applications to add. **Want** must contain **bundleName** and
     *     **abilityName**.
     * @param { number } accountId - Account ID, which must be greater than or equal to 0.
     *     <br> You can call
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()} of @
     *     ohos.account.osAccount to obtain the ID.
     * @returns { boolean } Whether the user is prohibited from canceling application auto-startup. The value **true**
     *     indicates yes and the value **false** indicates no.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 20
     */
    function isModifyAutoStartAppsDisallowed(admin: Want, autoStartApp: Want, accountId: number): boolean;
    /**
     * Removes the auto-start applications for the current user. After the deletion, the applications will no longer
     * automatically start upon system boot.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { Array<Want> } autoStartApps - Array of auto-start applications. **Want** must contain **bundleName** and
     *     **abilityName**. The ability can be UIAbility or ServiceExtensionAbility. If the value of **exported** in the
     *     [abilities](docroot://quick-start/module-configuration-file.md#abilities) tag is **false**, the ability cannot
     *     be started.
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
    function removeAutoStartApps(admin: Want, autoStartApps: Array<Want>): void;
    /**
     * Removes the specified application from the auto-start application list of a specified user.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { Array<Want> } autoStartApps - Array of auto-start applications. **Want** must contain **bundleName** and
     *     **abilityName**.
     * @param { number } accountId - Account ID, which must be greater than or equal to 0.
     *     <br> You can call
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()} of @
     *     ohos.account.osAccount to obtain the ID.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 20
     */
    function removeAutoStartApps(admin: Want, autoStartApps: Array<Want>, accountId: number): void;
    /**
     * Checks the auto-start applications for the current user.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @returns { Array<Want> } List of the auto-start applications obtained. Since API version 24, the setting of whether
     *     the UI is hidden can be returned.
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
    function getAutoStartApps(admin: Want): Array<Want>;
    /**
     * Checks the auto-start applications for the current user.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want | null } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the.
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.<br>If the device has multiple MDM
     *     applications, you can pass **admin** to query the corresponding policies. If **null** is passed, the policies
     *     that actually take effect on the device are returned.
     * @returns { Array<Want> } List of the auto-start applications obtained.
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
    function getAutoStartApps(admin: Want | null): Array<Want>;
    /**
     * Checks the auto-start applications for the specified user.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { number } accountId - Account ID, which must be greater than or equal to 0.
     *     <br> You can call
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()} of @
     *     ohos.account.osAccount to obtain the ID.
     * @returns { Array<Want> } List of the auto-start applications obtained. Since API version 24, the setting of whether
     *     the UI is hidden can be returned.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 20
     */
    function getAutoStartApps(admin: Want, accountId: number): Array<Want>;
    /**
     * Checks the auto-start applications for the specified user.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want | null } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the.
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.<br>If the device has multiple MDM
     *     applications, you can pass **admin** to query the corresponding policies. If **null** is passed, the policies
     *     that actually take effect on the device are returned.
     * @param { number } accountId - Account ID, which must be greater than or equal to 0.
     *     <br> You can call
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()} of @
     *     ohos.account.osAccount to obtain the ID.
     * @returns { Array<Want> } List of the auto-start applications obtained.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function getAutoStartApps(admin: Want | null, accountId: number): Array<Want>;
    /**
     * Adds applications to the keep-alive list; once added, the application processes will be kept alive automatically.
     * After the device is powered on or the application is killed, the system will proactively restart these application
     * processes.
     *
     * For applications added to the keep-alive list via this API, users cannot manually revoke their keep-alive status on
     * the device. However, you can call the
     * [removeKeepAliveApps]{@link applicationManager.removeKeepAliveApps} API to remove them from the keep-alive list.
     *
     * If applications are disallowed to run by calling
     * [addDisallowedRunningBundlesSync]{@link applicationManager.addDisallowedRunningBundlesSync}, they cannot be kept
     * alive. Otherwise, error code 9200010 will be reported.
     *
     * To use similar functions on phones or tablets, call
     * [addUserNonStopApps]{@link applicationManager.addUserNonStopApps} or
     * [addFreezeExemptedApps]{@link applicationManager.addFreezeExemptedApps}. For details, see the relevant documents.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { Array<string> } bundleNames - Array of application bundle names, which specifies the applications to be
     *     kept alive. A maximum of 5 applications are supported.
     * @param { number } accountId - Account ID, which must be greater than or equal to 0.
     *     <br> You can call
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()} of @
     *     ohos.account.osAccount to obtain the ID.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200010 - A conflict policy has been configured.
     * @throws { BusinessError } 9201005 - Add keep alive applications failed.
     * @throws { BusinessError } 201 - Permission verification failed.The application does not have the permission
     *     required to call the API
     * @throws { BusinessError } 401 - Parameter error.Possible causes: 1.Mandatory parameters are left unspecified;
     *     2.Incorrect parameter types;3.Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call the API due to limited device
     *     capabilities.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 14
     */
    function addKeepAliveApps(admin: Want, bundleNames: Array<string>, accountId: number): void;
    /**
     * Adds applications to the keep-alive list; once added, the application processes will be kept alive automatically.
     * You can also set whether to disable manual keep-alive cancellation. After the device is powered on or the
     * application is killed, the system will proactively restart these application processes.
     *
     * Applications can be added to the keep-alive list via this API and the
     * [addKeepAliveApps]{@link applicationManager.addKeepAliveApps} API. Settings from both APIs can take effect
     * simultaneously. For a single user, the keep-alive list supports a maximum of 5 applications. For example, if there
     * are already 3 applications in the current list, a maximum of 2 more can be added for the user via this API.
     *
     * If applications are disallowed to run by calling
     * [addDisallowedRunningBundlesSync]{@link applicationManager.addDisallowedRunningBundlesSync}, they cannot be kept
     * alive. Otherwise, error code 9200010 will be reported.
     *
     * To use similar functions on phones or tablets, call
     * [addUserNonStopApps]{@link applicationManager.addUserNonStopApps} or
     * [addFreezeExemptedApps]{@link applicationManager.addFreezeExemptedApps}. For details, see the relevant documents.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { Array<string> } bundleNames - Array of application bundle names, which specifies the applications to be
     *     kept alive. A maximum of 5 applications are supported.
     *     <br>Applications must be installed under user 1 (a user who supports single-instance running of third-party
     *     applications) and have integrated
     *     [background services](docroot://application-models/app-service-extension-ability.md#implementing-a-background-service).
     *     Otherwise, the error code 9201005 will be reported.
     * @param { number } accountId - Account ID, which must be greater than or equal to 0.
     *     <br> You can call
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()} of @
     *     ohos.account.osAccount to obtain the ID.
     * @param { boolean } disallowModify - Whether to restrict users from manually canceling the keep-alive status. The
     *     value **true** indicates that users are not allowed to manually cancel the keep-alive status, and the value
     *     **false** indicates the opposite.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200010 - A conflict policy has been configured.
     * @throws { BusinessError } 9201005 - Add keep alive applications failed.
     * @throws { BusinessError } 201 - Permission verification failed.The application does not have the permission
     *     required to call the API
     * @throws { BusinessError } 801 - Capability not supported. Failed to call the API due to limited device
     *     capabilities.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 20
     */
    function addKeepAliveApps(admin: Want, bundleNames: Array<string>, accountId: number, disallowModify: boolean): void;
    /**
     * Checks whether the application is forbidden to cancel the keep-alive status.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { number } accountId - Account ID, which must be greater than or equal to 0.
     *     <br> You can call
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()} of @
     *     ohos.account.osAccount to obtain the ID.
     * @param { string } bundleName - Bundle name.
     * @returns { boolean } Whether to restrict users from manually canceling the keep-alive status. The value **true**
     *     indicates that users are not allowed to manually cancel the keep-alive status, and the value **false**
     *     indicates the opposite.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 20
     */
    function isModifyKeepAliveAppsDisallowed(admin: Want, accountId: number, bundleName: string): boolean;
    /**
     * Removes a specified application from the keep-alive list.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { Array<string> } bundleNames - Application bundle name array, which specifies the applications to be kept
     *     alive. A maximum of five applications are supported.
     * @param { number } accountId - Account ID, which must be greater than or equal to 0.
     *     <br> You can call
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()} of @
     *     ohos.account.osAccount to obtain the ID.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed.The application does not have the permission
     *     required to call the API
     * @throws { BusinessError } 401 - Parameter error.Possible causes: 1.Mandatory parameters are left unspecified;
     *     2.Incorrect parameter types;3.Parameter verification failed.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 14
     */
    function removeKeepAliveApps(admin: Want, bundleNames: Array<string>, accountId: number): void;
    /**
     * Obtains the bundle name of the keep-alive application.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { number } accountId - Account ID, which must be greater than or equal to 0.
     *     <br> You can call
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()} of @
     *     ohos.account.osAccount to obtain the ID.
     * @returns { Array<string> } Bundle name of the application kept alive for the specified user.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed.The application does not have the permission
     *     required to call the API
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types;3. Parameter verification failed.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 14
     */
    function getKeepAliveApps(admin: Want, accountId: number): Array<string>;
    /**
     * Obtains the bundle name of the keep-alive application.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want | null } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the.
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.<br>If the device has multiple MDM
     *     applications, you can pass **admin** to query the corresponding policies. If **null** is passed, the policies
     *     that actually take effect on the device are returned.
     * @param { number } accountId - Account ID, which must be greater than or equal to 0.
     *     <br> You can call
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()} of @
     *     ohos.account.osAccount to obtain the ID.
     * @returns { Array<string> } Bundle name of the application kept alive for the specified user.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed.The application does not have the permission
     *     required to call the API
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types;3. Parameter verification failed.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function getKeepAliveApps(admin: Want | null, accountId: number): Array<string>;
    /**
     * Sets applications allowed to run in kiosk mode.
     *
     * Kiosk mode is a system-level runtime mode that restricts a device to a single application or a set of applications.
     * It controls the lock screen, status bar, gestures, and key features to prevent users from launching other
     * applications or performing other operations on the device.
     *
     * @permission ohos.permission.ENTERPRISE_SET_KIOSK
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { Array<string> } appIdentifiers - Array of
     *     [unique identifiers]{@link ./bundleManager/BundleInfo:SignatureInfo} of an application. You can call the
     *     [bundleManager.getBundleInfo]{@link @ohos.bundle.bundleManager:bundleManager.getBundleInfo} API to obtain the
     *     **bundleInfo.signatureInfo.appIdentifier**. In case of repeated configuration, the newly configured array will
     *     overwrite the old one, with a maximum limit of 200 entries.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed.The application does not have the permission
     *     required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 20
     */
    function setAllowedKioskApps(admin: Want, appIdentifiers: Array<string>): void;
    /**
     * Obtains the applications allowed to run in kiosk mode.
     *
     * @permission ohos.permission.ENTERPRISE_SET_KIOSK
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @returns { Array<string> } List of [unique identifiers]{@link ./bundleManager/BundleInfo:SignatureInfo} of an
     *     application that can run in kiosk mode.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed.The application does not have the permission
     *     required to call the API
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 20
     */
    function getAllowedKioskApps(admin: Want): Array<string>;
    /**
     * Obtains the applications allowed to run in kiosk mode.
     *
     * @permission ohos.permission.ENTERPRISE_SET_KIOSK
     * @param { Want | null } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the.
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.<br>If the device has multiple MDM
     *     applications, you can pass **admin** to query the corresponding policies. If **null** is passed, the policies
     *     that actually take effect on the device are returned.
     * @returns { Array<string> } List of [unique identifiers]{@link ./bundleManager/BundleInfo:SignatureInfo} of an
     *     application that can run in kiosk mode.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed.The application does not have the permission
     *     required to call the API
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function getAllowedKioskApps(admin: Want | null): Array<string>;
    /**
     * Checks whether an application is allowed to run in kiosk mode.
     *
     * @param { string } appIdentifier - [Unique identifiers]{@link ./bundleManager/BundleInfo:SignatureInfo} of an
     *     application. You can call the
     *     [bundleManager.getBundleInfo]{@link @ohos.bundle.bundleManager:bundleManager.getBundleInfo} API to obtain the
     *     **bundleInfo.signatureInfo.appIdentifier**.
     * @returns { boolean } The value **true** means the application can run in kiosk mode; the value **false** means the
     *     opposite.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 20
     */
    function isAppKioskAllowed(appIdentifier: string): boolean;
    /**
     * Sets the features of the kiosk mode. You can use this API to control whether the notification center and control
     * panel can be accessed in kiosk mode.
     *
     * Since API version 24, you can set whether to allow users to swipe up from the bottom to access the recent taskbar
     * and swipe left or right to display the side dock.
     *
     * In non-kiosk mode, this API can be called normally but does not take effect. The settings will take effect after
     * kiosk mode is enabled.
     *
     * @permission ohos.permission.ENTERPRISE_SET_KIOSK
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { Array<KioskFeature> } features - Feature set of the Kiosk mode. (Since API version 24, swiping up from the
     *     bottom to access the recent taskbar and swiping left or right to display the side dock are supported.)
     *     <br> If an empty array is passed, the system will clear all previously delivered features and restore the kiosk
     *     mode to its default state. To be specific, abilities such as the notification center, control panel, recent
     *     task bar, and side dock are disabled.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200012 - Parameter verification failed.
     * @throws { BusinessError } 201 - Permission verification failed.The application does not have the permission
     *     required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 20
     */
    function setKioskFeatures(admin: Want, features: Array<KioskFeature>): void;
    /**
     * Clears all application data.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { string } bundleName - Bundle name of the application whose data needs to be cleared.
     * @param { number } appIndex - Index of the application clone. The value is an integer greater than or equal to 0.
     *     <br> You can call [getAppCloneIdentity]{@link @ohos.bundle.bundleManager:bundleManager.getAppCloneIdentity}
     *     of @ohos.bundle.bundleManager to obtain the index.
     * @param { number } accountId - Account ID. The value is an integer greater than or equal to 0.
     *     <br> You can call
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()}
     *     of @ohos.account.osAccount to obtain the ID.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed.The application does not have the permission
     *     required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 20
     */
    function clearUpApplicationData(admin: Want, bundleName: string, appIndex: number, accountId: number): void;
    /**
     * Adds applications to the non-stoppable application list for a specified user. This policy only applies to installed
     * applications. If the parameter list contains uninstalled applications, error code 9200012 will be returned. If an
     * application in the list is uninstalled after the policy is set, the uninstalled application will be removed from
     * the list. Adding an application that already exists in the list will return success, but the application will not
     * be added repeatedly to the policy list.
     *
     * On phones and tablets, non-stoppable applications cannot be closed by swiping up in the task center. After a user
     * taps the application name in **Settings** > **Apps & services** to go to the details page, the forcible stop button
     * is unavailable, and the disable button does not take effect.
     *
     * On PCs/2-in-1 devices, after a user taps the application name in **Settings** > **Apps & services** to go to the
     * details page, the forcible stop button is unavailable, and the disable button does not take effect.
     *
     * Since API version 26.0.0, if you call
     * [setDisallowedPolicyForAccount]{@link @ohos.enterprise.restrictions:restrictions.setDisallowedPolicyForAccount} to
     * disable [SUPER_HUB]{@link @ohos.enterprise.restrictions:restrictions.FeatureForAccount} and then call this API to
     * add SuperHub to the non-stoppable application list, a policy conflict occurs and error code 9200010 is reported.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { Array<common.ApplicationInstance> } applicationInstances - Array of non-stoppable applications. A maximum
     *     of 10 applications can be added to the non-stoppable application list. This limit is not divided among users.
     *     Specifically, the total number of such applications added by all users cannot exceed 10. For example, if there
     *     are already 3 applications in the current list, a maximum of 7 more can be added for a specified user via this
     *     API.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200010 - A conflict policy has been configured. [since 26.0.0]
     * @throws { BusinessError } 9200012 - Parameter verification failed.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 22
     */
    function addUserNonStopApps(admin: Want, applicationInstances: Array<common.ApplicationInstance>): void;
    /**
     * Removes the non-stoppable application list for a specified user. After the removal, the user can stop the
     * applications on the device. If the parameter list includes uninstalled applications, the removal will still
     * succeed. Installed applications will be removed from the list, while uninstalled ones will not impact the removal
     * process.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { Array<common.ApplicationInstance> } applicationInstances - Array of non-stoppable applications.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200012 - Parameter verification failed.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 22
     */
    function removeUserNonStopApps(admin: Want, applicationInstances: Array<common.ApplicationInstance>): void;
    /**
     * Obtains the non-stoppable application list of all users on the current device.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @returns { Array<common.ApplicationInstance> } Array of non-stoppable applications.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 22
     */
    function getUserNonStopApps(admin: Want): Array<common.ApplicationInstance>;
    /**
     * Obtains the non-stoppable application list of all users on the current device.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want | null } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the.
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.<br>If the device has multiple MDM
     *     applications, you can pass **admin** to query the corresponding policies. If **null** is passed, the policies
     *     that actually take effect on the device are returned.
     * @returns { Array<common.ApplicationInstance> } Array of non-stoppable applications.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function getUserNonStopApps(admin: Want | null): Array<common.ApplicationInstance>;
    /**
     * Adds applications to the background freeze-exempt application list for a specified user. This policy applies only
     * to installed applications. If the parameter list contains uninstalled applications, error code 9200012 will be
     * returned. If an application in the list is uninstalled after the policy is set, the uninstalled application will be
     * removed from the list. Adding an application that already exists in the list will return success, but the
     * application will not be added repeatedly to the policy list.
     *
     * Freezing operations include suspending the target application, and managing software resource agents, hardware
     * resource agents, and high-power consumption.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { Array<common.ApplicationInstance> } applicationInstances - Array of the background freeze-exempt
     *     application list. A maximum of 10 applications can be added to the list. This limit is not divided among users.
     *     Specifically, the total number of such applications added by all users cannot exceed 10. For example, if there
     *     are already 3 applications in the current list, a maximum of 7 more can be added for a specified user via this
     *     API.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200012 - Parameter verification failed.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 22
     */
    function addFreezeExemptedApps(admin: Want, applicationInstances: Array<common.ApplicationInstance>): void;
    /**
     * Removes the background freeze-exempt application list for a specified user. After the removal, the applications can
     * be frozen by the system. If the parameter list includes uninstalled applications, the removal will still succeed.
     * Installed applications will be removed from the list, while uninstalled ones will not impact the removal process.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { Array<common.ApplicationInstance> } applicationInstances - Array of the background freeze-exempt
     *     application list.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200012 - Parameter verification failed.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 22
     */
    function removeFreezeExemptedApps(admin: Want, applicationInstances: Array<common.ApplicationInstance>): void;
    /**
     * Obtains the background freeze-exempt application list of all users on the current device.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @returns { Array<common.ApplicationInstance> } Array of the background freeze-exempt application list.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 22
     */
    function getFreezeExemptedApps(admin: Want): Array<common.ApplicationInstance>;
    /**
     * Obtains the background freeze-exempt application list of all users on the current device.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want | null } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the.
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.<br>If the device has multiple MDM
     *     applications, you can pass **admin** to query the corresponding policies. If **null** is passed, the policies
     *     that actually take effect on the device are returned.
     * @returns { Array<common.ApplicationInstance> } Array of the background freeze-exempt application list.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function getFreezeExemptedApps(admin: Want | null): Array<common.ApplicationInstance>;
    /**
     * Sets whether to disable the Ability component of a specified application (system application or third-party
     * application). Currently, only the UIAbility type is supported. After the UIAbility type is disabled, the UI of the
     * Ability component cannot be started.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { string } bundleName - App bundle name.
     * @param { number } accountId - Account ID. The value is an integer greater than or equal to 0.
     *     <br> You can call
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()} of @
     *     ohos.account.osAccount to obtain the ID.
     * @param { string } abilityName - Name of the ability to be disabled or enabled. Currently, only UIAbility is
     *     supported.
     * @param { boolean } isDisabled - Whether to disable the ability. **true**: Disable the ability. **false**: Enable
     *     the ability.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200012 - Parameter verification failed.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 23
     */
    function setAbilityDisabled(admin: Want, bundleName: string, accountId: number, abilityName: string, isDisabled: boolean): void;
    /**
     * Checks whether the Ability component of a specified application (system application or third-party application) is
     * disabled.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { string } bundleName - App bundle name.
     * @param { number } accountId - Account ID.
     *     <br>The value must be an integer greater than or equal to 0.
     *     <br> You can call
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()}
     *     of @ohos.account.osAccount to obtain the ID.
     * @param { string } abilityName - Name of the ability to be disabled or enabled. Currently, only UIAbility is
     *     supported.
     * @returns { boolean } Whether the ability is disabled. **true**: The ability is disabled. **false**: The ability is
     *     not disabled.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200012 - Parameter verification failed.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 23
     */
    function isAbilityDisabled(admin: Want, bundleName: string, accountId: number, abilityName: string): boolean;
    /**
     * Checks whether the Ability component of a specified application (system application or third-party application) is
     * disabled.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want | null } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the.
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.<br>If the device has multiple MDM
     *     applications, you can pass **admin** to query the corresponding policies. If **null** is passed, the policies
     *     that actually take effect on the device are returned.
     * @param { string } bundleName - App bundle name.
     * @param { number } accountId - Account ID. The value is an integer greater than or equal to 0.
     *     <br> You can call
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()} of @
     *     ohos.account.osAccount to obtain the ID.
     * @param { string } abilityName - Name of the ability to be disabled or enabled. Currently, only UIAbility is
     *     supported.
     * @returns { boolean } Whether the ability is disabled. **true**: The ability is disabled. **false**: The ability is
     *     not disabled.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200012 - Parameter verification failed.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function isAbilityDisabled(admin: Want | null, bundleName: string, accountId: number, abilityName: string): boolean;
    /**
     * Adds an application to the bottom shortcut bar of a PC/2-in-1 device based on the location index. Then users can
     * tap the application icon in the shortcut bar to directly launch the application. The application icon is the
     * default icon displayed on the home screen.
     *
     * > **NOTE**
     * >
     * > 1. If location 0 or 1 is already occupied by the application center or task center, adding an application to that
     * > location returns error code 9201019. If that location is occupied by another app, the addition succeeds.
     * >
     * > 2. The following applications cannot be added to the shortcut bar using this API: Application Center, Task
     * > Center, Files, and Recycle Bin.
     * >
     * > 3. Only applications with an entry (that is, an icon) can be added.
     * >
     * > 4. Only the shortcut bar of the current user can be configured. Each user's shortcut bar can contain a maximum of
     * > 100 applications.
     * >
     * > 5. When a new application is inserted into an occupied location, the new application will directly take that
     * > location, and the original application along with all subsequent applications will shift back by one location.
     * >
     * > 6. If the **index** parameter is not passed or the passed value is greater than the number of applications in the
     * > shortcut bar, the new application is added to the end of the shortcut bar by default.
     * >
     * > 7. After an application is added to the shortcut bar using this API, users can manually remove the application or
     * > adjust its position.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { string } bundleName - Bundle name of the application.
     * @param { string } abilityName - Ability name of the application. Only the application entry ability is supported.
     * @param { number } [index] - Location index of the application in the shortcut bar. The value range is
     *     [0, 100). The default value is 99.
     *     <br>Value range: [0,100).
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200012 - Parameter verification failed.
     * @throws { BusinessError } 9200015 - The ability does not exist.
     * @throws { BusinessError } 9201013 - The number of applications in the Dock has reached the maximum.
     * @throws { BusinessError } 9201014 - The application is already in the Dock.
     * @throws { BusinessError } 9201015 - The application is not installed.
     * @throws { BusinessError } 9201018 - The application is inoperable.
     * @throws { BusinessError } 9201019 - The location is inoperable.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 801 - Capability not supported.
     *     Failed to call the API due to limited device capabilities.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 24
     */
    function addDockApp(admin: Want, bundleName: string, abilityName: string, index?: number): void;
    /**
     * Removes an application from the shortcut bar.
     *
     * > **NOTE**
     * >
     * > The following applications cannot be removed from the shortcut bar using this API: Application Center, Task
     * > Center, Files, and Recycle Bin. Otherwise, error code 9201018 will be reported.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { string } bundleName - Bundle name of the application.
     * @param { string } abilityName - Ability name of the application.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9201016 - The application has not been added to the Dock.
     * @throws { BusinessError } 9201018 - The application is inoperable.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 801 - Capability not supported.
     *     Failed to call the API due to limited device capabilities.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 24
     */
    function removeDockApp(admin: Want, bundleName: string, abilityName: string): void;
    /**
     * Obtains the list of applications in the shortcut bar currently.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @returns { Array<DockInfo> } Array of application information in the shortcut bar.
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
    function getDockApps(admin: Want): Array<DockInfo>;
    /**
     * Adds the cross-device application trustlist for a specific distributed service for a specified user. Applications
     * in the trustlist can use the specific distributed service to transfer data across devices without being subject to
     * the restrictions imposed by
     * [setDisallowedPolicyForAccount]{@link @ohos.enterprise.restrictions:restrictions.setDisallowedPolicyForAccount}.
     *
     * Currently, the following distributed service type is supported:
     * [collaboration service]{@link applicationManager.ServiceType}.
     *
     * > **NOTE**
     * >
     * > 1. Before calling this API to set the application list allowed to use a specific distributed service, you must
     * > have already disabled one-way data transmission between devices (which is used for transferring data to other
     * > devices) via
     * > [setDisallowedPolicyForAccount]{@link @ohos.enterprise.restrictions:restrictions.setDisallowedPolicyForAccount}.
     * > Otherwise, error code 9201043 is thrown.
     *
     * > 2. When one-way data transmission between devices is re-enabled, the application list allowed to use the specific
     * > distributed service that was set via this API is automatically cleared.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { Array<string> } appIdentifiers - Array of
     *     [unique identifiers]{@link ./bundleManager/BundleInfo:SignatureInfo} of an application. You can call the
     *     [bundleManager.getBundleInfo]{@link @ohos.bundle.bundleManager:bundleManager.getBundleInfo} API to obtain the
     *     **bundleInfo.signatureInfo.appIdentifier**. The total number of applications in the array cannot exceed 200.
     * @param { ServiceType } serviceType - Distributed service type.
     * @param { number } accountId - Account ID. The value is an integer greater than or equal to 0.
     *     <br> You can call
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()} of @
     *     ohos.account.osAccount to obtain the ID.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200012 - Parameter verification failed.
     * @throws { BusinessError } 9201043 - Prerequisites for the API call have not been satisfied. For example,
     *     distributed outgoing transmission is not disallowed before adding the distributed bidirectional collaboration
     *     trustlist.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function addAllowedDistributeAbilityConnBundles(admin: Want, appIdentifiers: Array<string>, serviceType: ServiceType, accountId: number): void;
    /**
     * Removes the cross-device application trustlist for a specific distributed service for a specified user. After the
     * trustlist is removed, if there are still remaining applications in the list, only those applications can use the
     * specific distributed service to transmit data across devices without being subject to the restrictions imposed by
     * [setDisallowedPolicyForAccount]{@link @ohos.enterprise.restrictions:restrictions.setDisallowedPolicyForAccount}. If
     * the list has been removed and there are no remaining applications, no applications under the specified user are
     * allowed to use the specific distributed service for cross-device data transmission.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { Array<string> } appIdentifiers - Array of
     *     [unique identifiers]{@link ./bundleManager/BundleInfo:SignatureInfo} of an application. You can call the
     *     [bundleManager.getBundleInfo]{@link @ohos.bundle.bundleManager:bundleManager.getBundleInfo} API to obtain the
     *     **bundleInfo.signatureInfo.appIdentifier**. The total number of applications in the array cannot exceed 200.
     * @param { ServiceType } serviceType - Distributed service type.
     * @param { number } accountId - Account ID. The value is an integer greater than or equal to 0.
     *     <br> You can call
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()} of @
     *     ohos.account.osAccount to obtain the ID.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200012 - Parameter verification failed.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function removeAllowedDistributeAbilityConnBundles(admin: Want, appIdentifiers: Array<string>, serviceType: ServiceType, accountId: number): void;
    /**
     * Obtains the cross-device application trustlist for a specific distributed service under a specified user.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want | null } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the.
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.<br>If the device has multiple MDM
     *     applications, you can pass **admin** to query the corresponding policies. If **null** is passed, the policies
     *     that actually take effect on the device are returned.
     * @param { ServiceType } serviceType - Distributed service type.
     * @param { number } accountId - Account ID. The value is an integer greater than or equal to 0.
     *     <br> You can call
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()} of @
     *     ohos.account.osAccount to obtain the ID.
     * @returns { Array<string> } Array of [unique identifiers]{@link ./bundleManager/BundleInfo:SignatureInfo} for
     *     applications allowed to use a specific distributed service under the specified user.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200012 - Parameter verification failed.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function getAllowedDistributeAbilityConnBundles(admin: Want | null, serviceType: ServiceType, accountId: number): Array<string>;
    /**
     * Adds applications to the notification trustlist. After the notification trustlist is set, applications not in the
     * trustlist cannot send notifications.
     *
     * > **NOTE**
     * >
     * > 1. If both the Kiosk mode and the notification trustlist policy are set, applications in the Kiosk mode and those
     * > in the notification trustlist can send notifications.
     *
     * > 2. If the device notification capability has been disabled via
     * > [setDisallowedPolicy]{@link @ohos.enterprise.restrictions:restrictions.setDisallowedPolicy}, calling this API to
     * > set the notification trustlist will trigger error code 9200010.
     *
     * > 3. The notification trustlist does not apply to system services, which can always send notifications. System
     * > applications are controlled by the notification trustlist.
     *
     * > 4. Cross-user settings are supported. The settings take effect immediately.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { Array<string> } bundleNames - Application bundle name array, which specifies the applications that are
     *     allowed to send notifications. A maximum of 200 applications are supported.
     * @param { number } accountId - Account ID, which must be greater than or equal to 0.
     *     <br>You can call
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()} of @
     *     ohos.account.osAccount to obtain the ID.
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
    function addAllowedNotificationBundles(admin: Want, bundleNames: Array<string>, accountId: number): void;
    /**
     * Removes applications from the notification trustlist.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { Array<string> } bundleNames - Application bundle name array, which specifies the applications to be
     *     removed.
     * @param { number } accountId - Account ID, which must be greater than or equal to 0.
     *     <br> You can call
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()} of @
     *     ohos.account.osAccount to obtain the ID.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200012 - Parameter verification failed.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function removeAllowedNotificationBundles(admin: Want, bundleNames: Array<string>, accountId: number): void;
    /**
     * Obtains the list of applications that are allowed to send notifications.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want | null } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the.
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.<br>If the device has multiple MDM
     *     applications, you can pass **admin** to query the corresponding policies. If **null** is passed, the policies
     *     that actually take effect on the device are returned.
     * @param { number } accountId - Account ID, which must be greater than or equal to 0.
     *     <br>You can call
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()} of @
     *     ohos.account.osAccount to obtain the ID.
     * @returns { Array<string> } Array of bundle names of applications that are allowed to send notifications.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200012 - Parameter verification failed.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function getAllowedNotificationBundles(admin: Want | null, accountId: number): Array<string>;
    /**
     * Adds applications to the home screen icon hide list.
     *
     * > **NOTE**
     * >
     * > 1. This API can only hide home screen icons for applications of the current user. Hiding application widgets are
     * > not supported.
     * >
     * > 2. If a hidden application has clones, the clones are hidden synchronously.
     * >
     * > 3. Not all applications on the home screen can be added to the hidden list. Otherwise, all applications will
     * > still be displayed on the home screen.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { Array<string> } bundleNames - Application bundle name array, which specifies the applications to be
     *     hidden. A maximum of 500 applications are supported.
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
    function addHideLauncherIcon(admin: Want, bundleNames: Array<string>): void;
    /**
     * Removes applications from the home screen icon hide list.
     *
     * > **NOTE**
     * >
     * > After unhiding, applications will be placed in the first available slot starting from the second screen of the
     * > home screen. If no empty slot is found on screens 2 to 18, it will search for an empty slot on the first screen.
     * > If no empty slot is available on the first screen, a small folder will be created at the position of the first
     * > application on the second screen to contain the applications.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { Array<string> } bundleNames - Application bundle name array, which specifies the applications to be
     *     unhidden. A maximum of 500 applications are supported.
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
    function removeHideLauncherIcon(admin: Want, bundleNames: Array<string>): void;
    /**
     * Queries the list of applications whose home screen icons are hidden for the current user.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want | null } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the.
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.<br>If the device has multiple MDM
     *     applications, you can pass **admin** to query the corresponding policies. If **null** is passed, the policies
     *     that actually take effect on the device are returned.
     * @returns { Array<string> } List of applications whose home screen icons are hidden for the current user.
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
    function getHideLauncherIcon(admin: Want | null): Array<string>;
    /**
     * Queries the data usage of a specified application within a specified period for the current user. This API uses a
     * promise to return the result.
     *
     * > **NOTE**
     * >
     * > The input network type (**networkInfo.type**) can only be **connection.NetBearType.BEARER_CELLULAR** or
     * > **connection.NetBearType.BEARER_WIFI**. If any other value is passed, the API returns error code 9200012.
     * >
     * > The input start time (**networkInfo.startTime**) and end time (**networkInfo.endTime**) are second-level
     * > timestamps. If the input start time and end time are negative numbers or the start time is later than the end
     * > time, the API returns error code 9200012.
     * >
     * > If the input user ID (**accountId**) is not the ID of the current user, the API returns error code 9200012.
     * >
     * > It is advised that the query interval (end time – start time) be 1 to 30 days. If the interval is too short, the
     * > query result may be inaccurate. If the interval is too long, the query will take a long time.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { string } bundleName - Bundle name of the application.
     * @param { number } appIndex - Index of the application clone. The value is an integer greater than or equal to 0.
     *     <br> You can call [getAppCloneIdentity]{@link @ohos.bundle.bundleManager:bundleManager.getAppCloneIdentity}
     *     of @ohos.bundle.bundleManager to obtain the index.
     * @param { number } accountId - Account ID. The value is an integer greater than or equal to 0.
     *     <br> You can call
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()}
     *     of @ohos.account.osAccount to obtain the ID.
     * @param { statistics.NetworkInfo } networkInfo - Network information.
     * @returns { Promise<statistics.NetStatsInfo> } Promise used to return the historical traffic information object.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200012 - Parameter verification failed.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function queryTrafficStats(admin: Want, bundleName: string, appIndex: number, accountId: number, networkInfo: statistics.NetworkInfo): Promise<statistics.NetStatsInfo>;
    /**
     * Queries the accumulated foreground runtime statistics of applications under a specified user account within a given
     * time period. The minimum query granularity is one day. The API requires the start time (**startTime**), end time (
     * **endTime**), and target user account ID (**accountId**) to be passed in. **startTime** and **endTime** are
     * millisecond-level timestamps. The caller can pass custom values. The default value of **startTime** is 00:00:00.000
     * of the current day, and the default of **endTime** is 24:00:00.000 of the current day (that is, 00:00:00 of the
     * following day). The API returns an array of **BundleStatsInfo**, where each element contains the bundle name of an
     * application, its clone index, and the foreground usage duration (in milliseconds) within the specified time period.
     * If **startTime** is set to **0**, the query starts from the device's first boot time. If **startTime** is later
     * than **endTime**, the API returns error code 9200012.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { number } startTime - Query start time, in milliseconds (timestamp).
     *     <br>Value range: [0, +∞).
     * @param { number } endTime - Query end time, in milliseconds (timestamp).
     *     <br>Value range: [0, +∞).
     * @param { number } accountId - Account ID. The value is an integer greater than or equal to 0.
     *     <br> You can call
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId()} of @
     *     ohos.account.osAccount to obtain the ID.
     * @returns { Array<BundleStatsInfo> } Array of application bundle statistics.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200012 - Parameter verification failed.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function queryBundleStatsInfos(admin: Want, startTime: number, endTime: number, accountId: number): Array<BundleStatsInfo>;
    /**
     * Queries the window state information list of the specified application. It can retrieve information such as whether
     * the application is in the bottom dock and whether the application window is currently displayed in the foreground.
     *
     * @permission ohos.permission.ENTERPRISE_MANAGE_APPLICATION
     * @param { Want } admin - EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the
     *     EnterpriseAdminExtensionAbility and the bundle name of the application.
     * @param { string } bundleName - Bundle name of the application.
     * @param { number } appIndex - Index of the application clone. The value is an integer greater than or equal to 0.
     *     <br> You can call [getAppCloneIdentity]{@link @ohos.bundle.bundleManager:bundleManager.getAppCloneIdentity}
     *     of @ohos.bundle.bundleManager to obtain the index.
     * @returns { Array<WindowStateInfo> } Array of the application window state information.
     * @throws { BusinessError } 9200001 - The application is not an administrator application of the device.
     * @throws { BusinessError } 9200002 - The administrator application does not have permission to manage the device.
     * @throws { BusinessError } 9200012 - Parameter verification failed.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function getApplicationWindowStates(admin: Want, bundleName: string, appIndex: number): Array<WindowStateInfo>;
}
export default applicationManager;

```
