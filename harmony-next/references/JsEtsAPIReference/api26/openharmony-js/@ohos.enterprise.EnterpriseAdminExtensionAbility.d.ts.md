# @ohos.enterprise.EnterpriseAdminExtensionAbility.d.ts

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
 * @file EnterpriseAdminExtensionAbility
 * @kit MDMKit
 */
import type systemManager from './@ohos.enterprise.systemManager';
import common from './@ohos.enterprise.common';
import EnterpriseAdminExtensionContext from './application/EnterpriseAdminExtensionContext';
/**
 * This module provides the
 * [enterprise device management extension ability](docroot://mdm/mdm-kit-term.md#enterpriseadminextensionability) and
 * is the core component of the enterprise device administrator application.
 *
 * **Main functions**:
 *
 * - Provides lifecycle management capabilities for device administrator applications (enabling, disabling, startup, and
 * so on).
 * - Provides application lifecycle event listening capabilities (installation, uninstallation, startup, stop, update).
 * - Provides system account management event listening capabilities (account addition, switch, removal).
 * - Provides system-level event callbacks for Kiosk mode, key events, log collection, and system updates.
 * - Provides policy change event listening capabilities.
 *
 * **Use cases:** Enterprise device administrator application development, enterprise application lifecycle management,
 * device security control, account management, and device O&M monitoring.
 *
 * To have the capabilities provided by this module, for example, to receive a notification when a device administrator
 * application is enabled or disabled, you need to create an **EnterpriseAdminExtensionAbility** instance for the device
 * administrator application and overload related APIs.
 *
 * @syscap SystemCapability.Customization.EnterpriseDeviceManager
 * @stagemodelonly
 * @since 12
 */
export default class EnterpriseAdminExtensionAbility {
    /**
     * Context of **EnterpriseAdminExtensionAbility**. It inherits from
     * [ExtensionContext]{@link ./application/ExtensionContext:ExtensionContext}.
     *
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 23
     */
    context: EnterpriseAdminExtensionContext;
    /**
     * Called when the device administrator application is enabled. After an enterprise administrator or employee deploys
     * and enables the device administrator application, the system notifies the device administrator application that the
     * admin permission has been granted. The device administrator application can initialize policies within this
     * callback. No registration is required. This callback is triggered by default after the device administrator
     * application is enabled.
     *
     * Differences from onDeviceAdminEnabled:
     *
     * - **onAdminEnabled**: Triggered when the device administrator application itself is enabled, and used for the
     * device administrator application to initialize its own policies.
     * - **onDeviceAdminEnabled**: Triggered when a super device administrator application listens for the enabling of a
     * normal device administrator application, and used for the super device administrator application to manage normal
     * device administrator applications.
     *
     * You should choose the appropriate method based on the application type and listening scenario: normal device
     * administrator applications should use **onAdminEnabled**, while super device administrator applications listening
     * for the enabling of other applications should use **onDeviceAdminEnabled**.
     *
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 12
     */
    onAdminEnabled(): void;
    /**
     * Called when the device administrator application is disabled. After an enterprise administrator or employee
     * disables the device administrator application, the system notifies the application that the admin permission has
     * been revoked. The device administrator application can use this callback to notify the enterprise administrator
     * that the device is no longer under management. No registration is required. This callback is triggered by default
     * after the device administrator application is disabled.
     *
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 12
     */
    onAdminDisabled(): void;
    /**
     * Called only for the super device administrator application when the device administrator application is enabled.
     * After an enterprise administrator or employee deploys and enables the device administrator application, the system
     * notifies the super device administrator application that the admin permission has been granted. The super device
     * administrator application can initialize policies within this callback. No registration is required. This callback
     * is triggered by default after the device administrator application is enabled.
     *
     * @param { string } bundleName - Bundle name of the application enabled.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 23
     */
    onDeviceAdminEnabled(bundleName: string): void;
    /**
     * Called only for the super device administrator application when the device administrator application is disabled.
     * After an enterprise administrator or employee disables the device administrator application, the system notifies
     * the super device administrator application that the admin permission has been revoked. The super device
     * administrator application can use this callback to notify the enterprise administrator that the device is no longer
     * under management. No registration is required. This callback is triggered by default after the device administrator
     * application is disabled.
     *
     * @param { string } bundleName - Bundle name of the application disabled.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 23
     */
    onDeviceAdminDisabled(bundleName: string): void;
    /**
     * Called when applications are installed. The application bundle name is included. You should register the
     * **MANAGED_EVENT_BUNDLE_ADDED** event through
     * [adminManager.subscribeManagedEventSync]{@link @ohos.enterprise.adminManager:adminManager.subscribeManagedEventSync}.
     * The enterprise administrator application can subscribe to application installation events. When an application is
     * installed on an enterprise device, the device administrator application reports the event in this callback to
     * notify the enterprise administrator.
     *
     * @param { string } bundleName - Bundle name of the application installed.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 12
     */
    onBundleAdded(bundleName: string): void;
    /**
     * Called when applications are uninstalled. The application bundle name is included. You should register the
     * **MANAGED_EVENT_BUNDLE_REMOVED** event through
     * [adminManager.subscribeManagedEventSync]{@link @ohos.enterprise.adminManager:adminManager.subscribeManagedEventSync}.
     * The enterprise administrator application can subscribe to application uninstallation events. When an application is
     * uninstalled from an enterprise device, the device administrator application reports the event in this callback to
     * notify the enterprise administrator.
     *
     * @param { string } bundleName - Bundle name of the application uninstalled.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 12
     */
    onBundleRemoved(bundleName: string): void;
    /**
     * Called when an application is started. You should register the **MANAGED_EVENT_APP_START** event through
     * [adminManager.subscribeManagedEventSync]{@link @ohos.enterprise.adminManager:adminManager.subscribeManagedEventSync}.
     * The enterprise administrator application can subscribe to application start events. When an application is started
     * on an enterprise device, the device administrator application reports the event in this callback to notify the
     * enterprise administrator.
     *
     * @param { string } bundleName - Bundle name of the application started.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 12
     */
    onAppStart(bundleName: string): void;
    /**
     * Called when an application is stopped. You should register the **MANAGED_EVENT_APP_STOP** event through
     * [adminManager.subscribeManagedEventSync]{@link @ohos.enterprise.adminManager:adminManager.subscribeManagedEventSync}.
     * The enterprise administrator application can subscribe to application stop events. When an application is stopped
     * on an enterprise device, the device administrator application reports the event in this callback to notify the
     * enterprise administrator.
     *
     * @param { string } bundleName - Bundle name of the application stopped.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 12
     */
    onAppStop(bundleName: string): void;
    /**
     * Called to report a system update event. You should register the **MANAGED_EVENT_SYSTEM_UPDATE** event through
     * [adminManager.subscribeManagedEventSync]{@link @ohos.enterprise.adminManager:adminManager.subscribeManagedEventSync}.
     * The enterprise administrator application can subscribe to application update events. When an application is updated
     * on an enterprise device, the device administrator application reports the event in this callback to notify the
     * enterprise administrator.
     *
     * @param { systemManager.SystemUpdateInfo } systemUpdateInfo - System update information, which is used to notify the
     *     device administrator application of the system version update information.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 12
     */
    onSystemUpdate(systemUpdateInfo: systemManager.SystemUpdateInfo): void;
    /**
     * Called when EnterpriseAdminExtensionAbility starts.
     *
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 12
     */
    onStart(): void;
    /**
     * Called when a system account is added. You should register the **MANAGED_EVENT_ACCOUNT_ADDED** event through
     * [adminManager.subscribeManagedEventSync]{@link @ohos.enterprise.adminManager:adminManager.subscribeManagedEventSync}.
     * The enterprise administrator application can subscribe to system account add events. When a system account is added
     * to an enterprise device, the device administrator application reports the event in this callback to notify the
     * enterprise administrator.
     *
     * @param { number } accountId - Account ID added.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 18
     */
    onAccountAdded(accountId: number): void;
    /**
     * Called when the system account is switched. You should register the **MANAGED_EVENT_ACCOUNT_SWITCHED** event
     * through
     * [adminManager.subscribeManagedEventSync]{@link @ohos.enterprise.adminManager:adminManager.subscribeManagedEventSync}.
     * The enterprise administrator application can subscribe to system account switch events. When a system account is
     * switched, the device administrator application reports the event in this callback to notify the enterprise
     * administrator.
     *
     * @param { number } accountId - Account ID switched.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 18
     */
    onAccountSwitched(accountId: number): void;
    /**
     * Called when the system account is removed. You should register the **MANAGED_EVENT_ACCOUNT_REMOVED** event through
     * [adminManager.subscribeManagedEventSync]{@link @ohos.enterprise.adminManager:adminManager.subscribeManagedEventSync}.
     * The enterprise administrator application can subscribe to system account removal events. When a system account is
     * removed, the device administrator application reports the event in this callback to notify the enterprise
     * administrator.
     *
     * @param { number } accountId - Account ID removed.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 18
     */
    onAccountRemoved(accountId: number): void;
    /**
     * Called when applications are uninstalled. The application bundle name and account ID are included. You should
     * register the **MANAGED_EVENT_BUNDLE_REMOVED** event through
     * [adminManager.subscribeManagedEventSync]{@link @ohos.enterprise.adminManager:adminManager.subscribeManagedEventSync}.
     * The enterprise administrator application can subscribe to application uninstallation events. When an application is
     * uninstalled from an enterprise device, the device administrator application reports the event in this callback to
     * notify the enterprise administrator.
     *
     * @param { string } bundleName - Bundle name of the application uninstalled.
     * @param { number } accountId - Account ID of the application uninstalled.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 14
     */
    onBundleRemoved(bundleName: string, accountId: number): void;
    /**
     * Called when applications are installed. The application bundle name and account ID are included. You should
     * register the **MANAGED_EVENT_BUNDLE_ADDED** event through
     * [adminManager.subscribeManagedEventSync]{@link @ohos.enterprise.adminManager:adminManager.subscribeManagedEventSync}.
     * The enterprise administrator application can subscribe to application installation events. When an application is
     * installed on an enterprise device, the device administrator application reports the event in this callback to
     * notify the enterprise administrator.
     *
     * @param { string } bundleName - Bundle name of the application installed.
     * @param { number } accountId - Account ID of the application installed.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 14
     */
    onBundleAdded(bundleName: string, accountId: number): void;
    /**
     * Callback for application update events. The callback contains the application package name and user ID. You can
     * receive this callback only after you register the **MANAGED_EVENT_BUNDLE_UPDATED** event through the
     * [adminManager.subscribeManagedEventSync]{@link @ohos.enterprise.adminManager:adminManager.subscribeManagedEventSync}
     * API. In enterprise device management scenarios, the device administrator application can subscribe to application
     * update events of all users. When an application update event is triggered, the device administrator application of
     * the current user is notified. Then the device administrator application can report the event in this callback
     * function to notify the enterprise administrator under the main user.
     *
     * @param { string } bundleName - Package name of the updated application belongs.
     * @param { number } accountId - ID of the user to which the updated application belongs.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    onBundleUpdated(bundleName: string, accountId: number): void;
    /**
     * Called when an application enters the kiosk mode. This callback contains the application bundle name and account
     * ID.
     *
     * Kiosk mode is a system-level runtime mode that restricts a device to a single application or a set of applications.
     * It controls the lock screen, status bar, gestures, and key features to prevent users from launching other
     * applications or performing other operations on the device.
     *
     * @param { string } bundleName - Bundle name of the application that enters the kiosk mode.
     * @param { number } accountId - Account ID of the application that enters the kiosk mode.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 20
     */
    onKioskModeEntering(bundleName: string, accountId: number): void;
    /**
     * Called when an application exits the kiosk mode. This callback contains the application bundle name and account ID.
     *
     * @param { string } bundleName - Bundle name of the application that exits the kiosk mode.
     * @param { number } accountId - Account ID of the application that exits the kiosk mode.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 20
     */
    onKioskModeExiting(bundleName: string, accountId: number): void;
    /**
     * Called when an application is installed via the
     * [bundleManager.installMarketApps]{@link @ohos.enterprise.bundleManager:bundleManager.installMarketApps} API. This
     * callback contains the application bundle name and installation result.
     *
     * @param { string } bundleName - Application bundle name on AppGallery.
     * @param { common.InstallationResult } result - Installation status of an application on AppGallery, including the
     *     installation success or failure.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 22
     */
    onMarketAppInstallResult(bundleName: string, result: common.InstallationResult): void;
    /**
     * Callback for the startup wizard completion event. You can receive this callback only after you register the
     * **MANAGED_EVENT_STARTUP_GUIDE_COMPLETED** event through the
     * [adminManager.subscribeManagedEventSync]{@link @ohos.enterprise.adminManager:adminManager.subscribeManagedEventSync}
     * API. The device administrator application can subscribe to startup wizard completion events. When the initial
     * switch to a sub-user (only on PCs), OTA upgrade, and first-time startup wizard are complete on an enterprise
     * device, the device administrator application reports the event in this callback to notify the enterprise
     * administrator.
     *
     * @param { common.StartupScene } scene - Specific scenario type that triggers the callback in the device setup wizard
     *     completion scenario, such as user setup completion (**USER_SETUP**), OTA upgrade completion (**OTA**), or
     *     device provisioning completion (**DEVICE_PROVISION**). You can execute corresponding service logic based on
     *     different scenarios.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 24
     */
    onStartupGuideCompleted(scene: common.StartupScene): void;
    /**
     * Callback for the device startup completion event. You can receive this callback only after you register the
     * **MANAGED_EVENT_BOOT_COMPLETED** event through the
     * [adminManager.subscribeManagedEventSync]{@link @ohos.enterprise.adminManager:adminManager.subscribeManagedEventSync}
     * API. The enterprise administrator application can subscribe to device startup completion events. When an enterprise
     * device has finished starting up, the device administrator application reports the event in this callback to notify
     * the enterprise administrator.
     *
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 24
     */
    onDeviceBootCompleted(): void;
    /**
     * Callback triggered upon completion of log collection, after a log collection task is successfully created via the
     * [systemManager.startCollectLog]{@link @ohos.enterprise.systemManager:systemManager.startCollectLog} API. It
     * contains the log collection result.
     *
     * > **NOTE**
     * >
     * > When log collection succeeds, the app must access the sandbox directory (**\/data/edm/log**) in its
     * > **EnterpriseAdminExtensionAbility** to retrieve the logs. For details about how to obtain logs, see the following
     * > sample code. After the app obtains the logs, you are advised to call
     * > [systemManager.finishLogCollected]{@link @ohos.enterprise.systemManager:systemManager.finishLogCollected} to
     * > remove the collected logs.
     *
     * @param { common.Result } result - Log collection result, used to indicate whether log collection was successful.
     *     Common values are **SUCCESS** or **FAIL**. You can use this result to determine whether to proceed with
     *     subsequent log retrieval operations.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 23
     */
    onLogCollected(result: common.Result): void;
    /**
     * Defines the [key event]{@link @ohos.enterprise.systemManager:systemManager.KeyEvent} callback. The MDM application
     * needs to deliver key event handling policies via the
     * [systemManager.addKeyEventPolicies]{@link @ohos.enterprise.systemManager:systemManager.addKeyEventPolicies} API.
     * When a system key event is triggered, if the event matches the delivered policy, this callback will be invoked. The
     * callback parameter [keyEvent]{@link @ohos.enterprise.systemManager:systemManager.KeyEvent} contains information
     * about currently triggered key events, which are introduced below.
     *
     * Single-key event. When a single key on the device is triggered, the
     * [onKeyEvent]{@link EnterpriseAdminExtensionAbility#onKeyEvent} callback will be invoked twice (once on key press
     * and once on key release). You can determine whether the key is pressed or released based on the **keyAction**
     * property in [keyEvent]{@link @ohos.enterprise.systemManager:systemManager.KeyEvent}. The **keyItems** property in
     * [keyEvent]{@link @ohos.enterprise.systemManager:systemManager.KeyEvent} can be ignored for single-key events.
     *
     * Combined-key event. Only the power button, volume up button, and volume down button can be combined. When a user
     * presses a key combination, the callback for the subsequently pressed key will carry information about all currently
     * pressed keys via the **keyItems** property in
     * [keyEvent]{@link @ohos.enterprise.systemManager:systemManager.KeyEvent}. All other response logic is consistent
     * with that of single-key events.
     *
     * Long-press event. When a single key or key combination is pressed for an extended period, the
     * [onKeyEvent]{@link EnterpriseAdminExtensionAbility#onKeyEvent} callback will be triggered continuously at an
     * interval of 50 ms (the actual interval may be slightly longer depending on system status and performance). For each
     * callback event, the **actionTime** property in
     * [keyEvent]{@link @ohos.enterprise.systemManager:systemManager.KeyEvent} remains the same as the **actionTime**
     * property in the [keyEvent]{@link @ohos.enterprise.systemManager:systemManager.KeyEvent} of the initial key press
     * callback. All other response logic is consistent with that of single-key and combined key events.
     *
     * @param { systemManager.KeyEvent } keyEvent - Information about the current key event, including the key code (
     *     **keyCode**), key action (**keyAction**, such as press or release), trigger time (**actionTime**), and list of
     *     pressed keys (**keyItems**). This information is used to identify and process key operations performed by the
     *     user.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 23
     */
    onKeyEvent(keyEvent: systemManager.KeyEvent): void;
    /**
     * Defines the policy change event. The super device administrator application can receive this callback after
     * registering the MANAGED_EVENT_POLICIES_CHANGED event via
     * [adminManager.subscribeManagedEventSync]{@link @ohos.enterprise.adminManager:adminManager.subscribeManagedEventSync}.
     * In the enterprise device management scenario, when any MDM application calls an API in
     * [Policy Change Reporting List](docroot://mdm/mdm-kit-appendix.md#policy-change-reporting-list), the system notifies
     * the super device administrator application of the current user.
     *
     * @param { common.PolicyChangedEvent } event - Policy change event, which contains detailed information about the
     *     policy change, such as the changed bundle name (**bundleName**), changed function name (**functionName**),
     *     changed parameters (**parameters**), and change time (**time**). The super device administrator application can
     *     perform policy audit or synchronization based on this information.
     * @syscap SystemCapability.Customization.EnterpriseDeviceManager
     * @stagemodelonly
     * @since 26.0.0
     */
    onAdminPolicyChanged(event: common.PolicyChangedEvent): void;
}

```
