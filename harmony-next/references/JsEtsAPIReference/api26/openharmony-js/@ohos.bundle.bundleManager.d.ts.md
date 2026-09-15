# @ohos.bundle.bundleManager.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022-2026 Huawei Device Co., Ltd.
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
 * @kit AbilityKit
 */
import { AsyncCallback } from './@ohos.base';
import { Metadata as _Metadata } from './bundleManager/Metadata';
import { ElementName as _ElementName } from './bundleManager/ElementName';
import Want from './@ohos.app.ability.Want';
import type { ApplicationInfo as _ApplicationInfo, ModuleMetadata as _ModuleMetadata } from './bundleManager/ApplicationInfo';
import * as _AbilityInfo from './bundleManager/AbilityInfo';
import * as _BundleInfo from './bundleManager/BundleInfo';
import * as _HapModuleInfo from './bundleManager/HapModuleInfo';
import * as _ExtensionAbilityInfo from './bundleManager/ExtensionAbilityInfo';
import * as _Skill from './bundleManager/Skill';
/**
 * The module provides APIs for obtaining application information, including
 * [bundle information]{@link bundleManager/BundleInfo},
 * [application information]{@link bundleManager/ApplicationInfo},
 * [ability information]{@link bundleManager/AbilityInfo} (information about a UIAbility), and
 * [ExtensionAbility information]{@link bundleManager/ExtensionAbilityInfo:ExtensionAbilityInfo}.
 *
 * @syscap SystemCapability.BundleManager.BundleFramework.Core
 * @crossplatform [since 12]
 * @atomicservice [since 11]
 * @since 9
 */
declare namespace bundleManager {
    /**
     * Enumerates the bundle flags, which indicate the type of bundle information to obtain.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @crossplatform [since 20]
     * @atomicservice [since 11]
     * @since 9
     */
    enum BundleFlag {
        /**
         * Used to obtain the default bundle information. The obtained information does not contain information about the
         * signature, application, HAP module, ability, ExtensionAbility, or permission.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @crossplatform [since 20]
         * @atomicservice [since 11]
         * @since 9
         */
        GET_BUNDLE_INFO_DEFAULT = 0x00000000,
        /**
         * Used to obtain the bundle information with application information. The obtained information does not contain
         * information about the signature, HAP module, ability, ExtensionAbility, or permission.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @crossplatform [since 20]
         * @atomicservice [since 11]
         * @since 9
         */
        GET_BUNDLE_INFO_WITH_APPLICATION = 0x00000001,
        /**
         * Used to obtain the bundle information with HAP module information. The obtained information does not contain
         * information about the signature, application, ability, ExtensionAbility, or permission.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @crossplatform [since 20]
         * @atomicservice [since 11]
         * @since 9
         */
        GET_BUNDLE_INFO_WITH_HAP_MODULE = 0x00000002,
        /**
         * Used to obtain the bundle information with ability information. The obtained information does not contain
         * information about the signature, application, ExtensionAbility, or permission. It must be used together with
         * **GET_BUNDLE_INFO_WITH_HAP_MODULE**.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @crossplatform [since 20]
         * @atomicservice [since 11]
         * @since 9
         */
        GET_BUNDLE_INFO_WITH_ABILITY = 0x00000004,
        /**
         * Used to obtain the bundle information with ExtensionAbility information. The obtained information does not
         * contain information about the signature, application, ability, or permission. It must be used together with
         * **GET_BUNDLE_INFO_WITH_HAP_MODULE**.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @atomicservice [since 11]
         * @since 9
         */
        GET_BUNDLE_INFO_WITH_EXTENSION_ABILITY = 0x00000008,
        /**
         * Used to obtain the bundle information with permission information. The obtained information does not contain
         * information about the signature, application, HAP module, ability, or ExtensionAbility.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @crossplatform [since 20]
         * @atomicservice [since 11]
         * @since 9
         */
        GET_BUNDLE_INFO_WITH_REQUESTED_PERMISSION = 0x00000010,
        /**
         * Used to obtain the metadata contained in the application, module, ability, or ExtensionAbility information. It
         * must be used together with **GET_BUNDLE_INFO_WITH_APPLICATION**, **GET_BUNDLE_INFO_WITH_HAP_MODULE**,
         * **GET_BUNDLE_INFO_WITH_ABILITY**, and **GET_BUNDLE_INFO_WITH_EXTENSION_ABILITY**.
         *
         * - To obtain the metadata contained in the application information, it must be used together with
         * **GET_BUNDLE_INFO_WITH_APPLICATION**.
         * - To obtain the metadata contained in the module information, it must be used together with
         * **GET_BUNDLE_INFO_WITH_HAP_MODULE**.
         * - To obtain the metadata contained in the ability information, it must be used together with
         * **GET_BUNDLE_INFO_WITH_HAP_MODULE** and **GET_BUNDLE_INFO_WITH_ABILITY**.
         * - To obtain the metadata contained in the ExtensionAbility information, it must be used together with
         * **GET_BUNDLE_INFO_WITH_HAP_MODULE** and **GET_BUNDLE_INFO_WITH_EXTENSION_ABILITY**.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @crossplatform [since 20]
         * @atomicservice [since 11]
         * @since 9
         */
        GET_BUNDLE_INFO_WITH_METADATA = 0x00000020,
        /**
         * Used to obtain the information about disabled bundles and abilities of a bundle. The obtained information does
         * not contain information about the signature, application, HAP module, ability, ExtensionAbility, or permission.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @crossplatform [since 20]
         * @atomicservice [since 11]
         * @since 9
         */
        GET_BUNDLE_INFO_WITH_DISABLE = 0x00000040,
        /**
         * Used to obtain the bundle information with signature information. The obtained information does not contain
         * information about the application, HAP module, ability, ExtensionAbility, or permission.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @crossplatform [since 20]
         * @atomicservice [since 11]
         * @since 9
         */
        GET_BUNDLE_INFO_WITH_SIGNATURE_INFO = 0x00000080,
        /**
         * Used to obtain the bundle information with the file context menu configuration. It must be used together with
         * **GET_BUNDLE_INFO_WITH_HAP_MODULE**.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @atomicservice
         * @since 11
         */
        GET_BUNDLE_INFO_WITH_MENU = 0x00000100,
        /**
         * Used to obtain the bundle information with the router map. It must be used together with
         * **GET_BUNDLE_INFO_WITH_HAP_MODULE**.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @atomicservice
         * @since 12
         */
        GET_BUNDLE_INFO_WITH_ROUTER_MAP = 0x00000200,
        /**
         * Used to obtain the bundle information with the skills. It must be used together with
         * **GET_BUNDLE_INFO_WITH_HAP_MODULE**, **GET_BUNDLE_INFO_WITH_ABILITY**, and
         * **GET_BUNDLE_INFO_WITH_EXTENSION_ABILITY**.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @atomicservice
         * @since 12
         */
        GET_BUNDLE_INFO_WITH_SKILL = 0x00000800,
        /**
         * Used to obtain the bundle information with the HAP module information. It is valid only for
         * bundleInfo.hapModulesInfo corresponding to the entry module. If the entry module does not exist, the
         * bundleInfo.hapModulesInfo list is empty. The obtained bundle information does not contain information about the
         * signature, application, ability, ExtensionAbility, or permission.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @atomicservice
         * @since 23
         */
        GET_BUNDLE_INFO_WITH_ENTRY_MODULE = 0x00010000
    }
    /**
     * Enumerates the ability flags, which indicate the type of ability information to obtain.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @atomicservice
     * @since 20
     */
    enum AbilityFlag {
        /**
         * Used to obtain the default [ability information]{@link bundleManager/AbilityInfo}, which does not contain
         * permissions, metadata, or ability information of disabled abilities. <!--Del-->You can use
         * [setAbilityEnabled]{@link @ohos.bundle.bundleManager:bundleManager.setAbilityEnabled(info: AbilityInfo, isEnabled: boolean, callback: AsyncCallback<void>)}
         * to set the ability enabling status and use
         * [isAbilityEnabled]{@link @ohos.bundle.bundleManager:bundleManager.isAbilityEnabled(info: AbilityInfo)} to obtain
         * the ability enabling status.<!--DelEnd-->
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @atomicservice
         * @since 20
         */
        GET_ABILITY_INFO_DEFAULT = 0x00000000,
        /**
         * Used to obtain the ability information containing permissions.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @atomicservice
         * @since 20
         */
        GET_ABILITY_INFO_WITH_PERMISSION = 0x00000001,
        /**
         * Used to obtain the ability information containing application information.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @atomicservice
         * @since 20
         */
        GET_ABILITY_INFO_WITH_APPLICATION = 0x00000002,
        /**
         * Used to obtain the ability information containing metadata.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @atomicservice
         * @since 20
         */
        GET_ABILITY_INFO_WITH_METADATA = 0x00000004,
        /**
         * Used to obtain the ability information of disabled abilities.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @atomicservice
         * @since 20
         */
        GET_ABILITY_INFO_WITH_DISABLE = 0x00000008,
        /**
         * Used to obtain the ability information of system applications.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @atomicservice
         * @since 20
         */
        GET_ABILITY_INFO_ONLY_SYSTEM_APP = 0x00000010,
        /**
         * Used to obtain the ability information that passes <!--RP3-->
         * [domain name verification](docroot://application-models/app-linking-startup.md#working-principles)<!--RP3End-->.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @atomicservice
         * @since 20
         */
        GET_ABILITY_INFO_WITH_APP_LINKING = 0x00000040,
        /**
         * Used to obtain the ability information containing skills.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @atomicservice
         * @since 20
         */
        GET_ABILITY_INFO_WITH_SKILL = 0x00000080
    }
    /**
     * Enumerates the types of ExtensionAbility components.
     *
     * <!--RP2--><!--RP2End-->
     *
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @atomicservice [since 11]
     * @since 9
     */
    export enum ExtensionAbilityType {
        /**
         * [FormExtensionAbility]{@link @ohos.app.form.FormExtensionAbility}: provides APIs for widget development.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @atomicservice [since 11]
         * @since 9
         */
        FORM = 0,
        /**
         * [WorkSchedulerExtensionAbility]{@link @ohos.WorkSchedulerExtensionAbility}: provides extended capabilities
         * related to deferred tasks, enabling applications to execute non-real-time tasks when the system is idle.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @since 9
         */
        WORK_SCHEDULER = 1,
        /**
         * [InputMethodExtensionAbility]{@link @ohos.InputMethodExtensionAbility:InputMethodExtensionAbility}: provides
         * extended capabilities related to input method applications.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @since 9
         */
        INPUT_METHOD = 2,
        /**
         * [ServiceExtensionAbility]{@link @ohos.app.ability.ServiceExtensionAbility:ServiceExtensionAbility}: provides
         * extended capabilities related to background services.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @since 9
         */
        SERVICE = 3,
        /**
         * AccessibilityExtensionAbility: provides extended capabilities related to accessibility services,
         * supporting access and operation of the foreground UI.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @since 9
         */
        ACCESSIBILITY = 4,
        /**
         * [DataShareExtensionAbility]{@link @ohos.application.DataShareExtensionAbility}: provides extended capabilities
         * related to data sharing, providing data reading and writing services.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @since 9
         */
        DATA_SHARE = 5,
        /**
         * FileShareExtensionAbility: provides extended capabilities related to file sharing between applications. This
         * ability is reserved and supported only by system applications.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @since 9
         */
        FILE_SHARE = 6,
        /**
         * [StaticSubscriberExtensionAbility]{@link @ohos.application.StaticSubscriberExtensionAbility:StaticSubscriberExtensionAbility}
         * : provides extended capabilities related to static broadcast, used to handle static events such as startup
         * events.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @since 9
         */
        STATIC_SUBSCRIBER = 7,
        /**
         * WallpaperExtensionAbility: provides extended capabilities to implement wallpapers displayed on home screen. This
         * ability is reserved and supported only by system applications.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @since 9
         */
        WALLPAPER = 8,
        /**
         * [BackupExtensionAbility]{@link @ohos.application.BackupExtensionAbility}: provides extended capabilities for data
         * backup and restore.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @since 9
         */
        BACKUP = 9,
        /**
         * [WindowExtensionAbility]{@link @ohos.application.WindowExtensionAbility}: provides extended capabilities that
         * allow system applications to pull up and embed UIs of other applications.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @since 9
         */
        WINDOW = 10,
        /**
         * [EnterpriseAdminExtensionAbility]{@link @ohos.enterprise.EnterpriseAdminExtensionAbility:EnterpriseAdminExtensionAbility}
         * : provides extended capabilities for processing enterprise management events, such as application installation
         * events on devices and events indicating too many incorrect screen-lock password attempts.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @since 9
         */
        ENTERPRISE_ADMIN = 11,
        /**
         * ThumbnailExtensionAbility: provides extended capabilities for offering thumbnails for files. This ability is
         * reserved and supported only by system applications.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @since 9
         */
        THUMBNAIL = 13,
        /**
         * PreviewExtensionAbility: provides extended capabilities for file preview so that other applications can be
         * embedded and displayed in the current application. This ability is reserved and supported only by system
         * applications.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @since 9
         */
        PREVIEW = 14,
        /**
         * PrintExtensionAbility: provides extended capabilities for printing photos and documents in office scenarios. This
         * ability is supported only by system applications.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @since 10
         */
        PRINT = 15,
        /**
         * [ShareExtensionAbility]{@link @ohos.app.ability.ShareExtensionAbility:ShareExtensionAbility}: provides sharing
         * service templates based on the UIExtensionAbility.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @since 10
         */
        SHARE = 16,
        /**
         * PushExtensionAbility: provides extended capabilities for pushing scenario-specific messages. This ability is
         * reserved and supported only by system applications.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @since 10
         */
        PUSH = 17,
        /**
         * [DriverExtensionAbility]{@link @ohos.app.ability.DriverExtensionAbility}: provides extended capabilities for the
         * peripheral driver. When an application configures an ExtensionAbility of the driver type, it is recognized as a
         * driver application. Driver applications do not differentiate between users during installation, uninstall, and
         * recovery. Moreover, when a new user account is created, the existing driver applications on the device are
         * installed for that user. For example, when a sub-user is created, the driver applications already installed by
         * the primary user is automatically installed for the sub-user. If a driver application is uninstalled for a sub-
         * user, it is also removed for the primary user.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @since 10
         */
        DRIVER = 18,
        /**
         * [ActionExtensionAbility]{@link @ohos.app.ability.ActionExtensionAbility:ActionExtensionAbility}: provides custom
         * action service templates based on the UIExtensionAbility.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @since 10
         */
        ACTION = 19,
        /**
         * AdsServiceExtensionAbility: provides background customized ad services for external systems. This ability is
         * supported only by system applications.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @since 11
         */
        ADS_SERVICE = 20,
        /**
         * [EmbeddedUIExtensionAbility]{@link @ohos.app.ability.EmbeddedUIExtensionAbility:EmbeddedUIExtensionAbility}:
         * provides extended capabilities for the embeddable UI across process.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @since 12
         */
        EMBEDDED_UI = 21,
        /**
         * InsightIntentUIExtensionAbility: provides extended capabilities that enable applications to be called by Celia
         * intents so as to be displayed in windows.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @since 12
         */
        INSIGHT_INTENT_UI = 22,
        /**
         * [FenceExtensionAbility]{@link @ohos.app.ability.FenceExtensionAbility:FenceExtensionAbility}: provides geofence-
         * related capabilities. It inherits from ExtensionAbility.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @since 18
         */
        FENCE = 24,
        /**
         * CallerInfoQueryExtensionAbility: provides the capability of querying incoming and outgoing call information.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @since 19
         */
        CALLER_INFO_QUERY = 25,
        /**
         * AssetAccelerationExtensionAbility: provides extended capabilities of pre-downloading background resources when
         * the device is idle.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @since 18
         */
        ASSET_ACCELERATION = 26,
        /**
         * [FormEditExtensionAbility]{@link @ohos.app.form.FormEditExtensionAbility:FormEditExtensionAbility}: provides
         * extended capabilities related to widget editing. It inherits from UIExtensionAbility.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @since 18
         */
        FORM_EDIT = 27,
        /**
         * [DistributedExtensionAbility]{@link @ohos.application.DistributedExtensionAbility:DistributedExtensionAbility}:
         * provides extended capabilities for distributed services and lifecycle callbacks for creation, destruction, and
         * connection of the DistributedExtensionAbility.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @since 20
         */
        DISTRIBUTED = 28,
        /**
         * [AppServiceExtensionAbility]{@link @ohos.app.ability.AppServiceExtensionAbility:AppServiceExtensionAbility}:
         * provides backend service capabilities for enterprise common applications.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @since 20
         */
        APP_SERVICE = 29,
        /**
         * [LiveFormExtensionAbility]{@link @ohos.app.form.LiveFormExtensionAbility}: provides extended capabilities for
         * interactive widgets, and provides lifecycle callbacks for creating and destroying interactive widgets.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @atomicservice
         * @since 20
         */
        LIVE_FORM = 30,
        /**
         * SelectionExtensionAbility: provides extended capabilities for text selection popup.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @stagemodelonly
         * @since 24
         */
        SELECTION = 31,
        /**
         * [WebNativeMessagingExtensionAbility]{@link @ohos.web.WebNativeMessagingExtensionAbility}: provides extended
         * capabilities for web native message communication.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @since 21
         */
        WEB_NATIVE_MESSAGING = 32,
        /**
         * [FaultLogExtensionAbility]{@link @ohos.hiviewdfx.FaultLogExtensionAbility:FaultLogExtensionAbility}: provides
         * extended capabilities for delayed fault notifications.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @since 21
         */
        FAULT_LOG = 33,
        /**
         * [NotificationSubscriberExtensionAbility]{@link @ohos.application.NotificationSubscriberExtensionAbility:NotificationSubscriberExtensionAbility}
         * : provides extended capabilities for notification subscription.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @since 22
         */
        NOTIFICATION_SUBSCRIBER = 34,
        /**
         * [CryptoExtensionAbility](docroot://security/UniversalKeystoreKit/huks-extension-ability-support-dev.md): provides
         * extended capabilities for external key management.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @since 22
         */
        CRYPTO = 35,
        /**
         * [PartnerAgentExtensionAbility]{@link @ohos.FusionConnectivity.PartnerAgentExtensionAbility}: provides the device
         * discovery and device offline notification functions based on Bluetooth.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @stagemodelonly
         * @since 23
         */
        PARTNER_AGENT = 36,
        /**
         * AgentExtensionAbility: provides extended capabilities for agents, including lifecycle callback APIs for agent
         * service creation, destruction, connection and disconnection, as well as callback APIs for receiving data sent
         * by clients and security authentication.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @stagemodelonly
         * @since 24
         */
        AGENT = 37,
        /**
         * AgentUIExtensionAbility: provides the Agent UI display capability on the access device.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @stagemodelonly
         * @since 24
         */
        AGENT_UI = 38,
        /**
         * Indicates extension info with type of the modular object extension.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        MODULAR_OBJECT = 39,
        /**
         * The ability type is not specified. <!--Del-->It can be used in
         * [queryExtensionAbilityInfo]{@link @ohos.bundle.bundleManager:bundleManager.queryExtensionAbilityInfo(want: Want, extensionAbilityType: ExtensionAbilityType, extensionAbilityFlags: number, userId: number, callback: AsyncCallback<Array<ExtensionAbilityInfo>>)}
         * to obtain ExtensionAbility components of all types.<!--DelEnd-->
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @since 9
         */
        UNSPECIFIED = 255
    }
    /**
     * Enumerates the permission grant states.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @crossplatform [since 20]
     * @atomicservice [since 11]
     * @since 9
     */
    export enum PermissionGrantState {
        /**
         * Permission denied.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @crossplatform [since 20]
         * @atomicservice [since 11]
         * @since 9
         */
        PERMISSION_DENIED = -1,
        /**
         * Permission granted.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @crossplatform [since 20]
         * @atomicservice [since 11]
         * @since 9
         */
        PERMISSION_GRANTED = 0
    }
    /**
     * Enumerates the window modes supported by the ability.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @crossplatform [since 20]
     * @atomicservice [since 11]
     * @since 9
     */
    export enum SupportWindowMode {
        /**
         * A window in full-screen mode is supported.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @crossplatform [since 20]
         * @atomicservice [since 11]
         * @since 9
         */
        FULL_SCREEN = 0,
        /**
         * A window in split-screen mode is supported.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @crossplatform [since 20]
         * @atomicservice [since 11]
         * @since 9
         */
        SPLIT = 1,
        /**
         * A floating window is supported.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @crossplatform [since 20]
         * @atomicservice [since 11]
         * @since 9
         */
        FLOATING = 2
    }
    /**
     * Enumerates the [launch types](docroot://application-models/uiability-launch-type.md) of the UIAbility.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    export enum LaunchType {
        /**
         * The UIAbility can have only one instance.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        SINGLETON = 0,
        /**
         * The UIAbility can have multiple instances.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        MULTITON = 1,
        /**
         * The UIAbility can have one or multiple instances, depending on the internal service of the ability.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @crossplatform [since 20]
         * @atomicservice [since 11]
         * @since 9
         */
        SPECIFIED = 2
    }
    /**
     * Enumerates the types of ability components.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @FAModelOnly
     * @since 9
     */
    export enum AbilityType {
        /**
         * Ability that has the UI. FA developed using the Page template to provide the capability of interacting with
         * users.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @FAModelOnly
         * @since 9
         */
        PAGE = 1,
        /**
         * Ability of the background service type, without the UI. PA developed using the Service template to provide the
         * capability of running tasks in the background.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @FAModelOnly
         * @since 9
         */
        SERVICE = 2,
        /**
         * PA developed using the Data template to provide unified data access for external systems.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @FAModelOnly
         * @since 9
         */
        DATA = 3
    }
    /**
     * Enumerates the display orientations of the ability. It is applicable only to
     * [PageAbility](docroot://application-models/pageability-overview.md) in the FA model.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @crossplatform [since 20]
     * @atomicservice [since 11]
     * @since 9
     */
    export enum DisplayOrientation {
        /**
         * Unspecified. The orientation is determined by the system.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @crossplatform [since 20]
         * @atomicservice [since 11]
         * @since 9
         */
        UNSPECIFIED = 0,
        /**
         * Landscape.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @crossplatform [since 20]
         * @atomicservice [since 11]
         * @since 9
         */
        LANDSCAPE = 1,
        /**
         * Portrait.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @crossplatform [since 20]
         * @atomicservice [since 11]
         * @since 9
         */
        PORTRAIT = 2,
        /**
         * The last display orientation is used.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @crossplatform [since 20]
         * @atomicservice [since 11]
         * @since 9
         */
        FOLLOW_RECENT = 3,
        /**
         * Reverse landscape.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @crossplatform [since 20]
         * @atomicservice [since 11]
         * @since 9
         */
        LANDSCAPE_INVERTED = 4,
        /**
         * Reverse portrait.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @crossplatform [since 20]
         * @atomicservice [since 11]
         * @since 9
         */
        PORTRAIT_INVERTED = 5,
        /**
         * Automatically rotates when the sensor changes to landscape or portrait mode.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @crossplatform [since 20]
         * @atomicservice [since 11]
         * @since 9
         */
        AUTO_ROTATION = 6,
        /**
         * Automatically rotates when the sensor changes to landscape mode.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @crossplatform [since 20]
         * @atomicservice [since 11]
         * @since 9
         */
        AUTO_ROTATION_LANDSCAPE = 7,
        /**
         * Automatically rotates when the sensor changes to portrait mode.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @crossplatform [since 20]
         * @atomicservice [since 11]
         * @since 9
         */
        AUTO_ROTATION_PORTRAIT = 8,
        /**
         * Switched-determined auto rotation.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @crossplatform [since 20]
         * @atomicservice [since 11]
         * @since 9
         */
        AUTO_ROTATION_RESTRICTED = 9,
        /**
         * Switched-determined auto rotation in the horizontal direction.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @crossplatform [since 20]
         * @atomicservice [since 11]
         * @since 9
         */
        AUTO_ROTATION_LANDSCAPE_RESTRICTED = 10,
        /**
         * Switched-determined auto rotation in the vertical direction.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @crossplatform [since 20]
         * @atomicservice [since 11]
         * @since 9
         */
        AUTO_ROTATION_PORTRAIT_RESTRICTED = 11,
        /**
         * Locked.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @crossplatform [since 20]
         * @atomicservice [since 11]
         * @since 9
         */
        LOCKED = 12,
        /**
         * Auto rotation controlled by the switch and determined by the system.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @atomicservice
         * @since 12
         */
        AUTO_ROTATION_UNSPECIFIED = 13,
        /**
         * Following the orientation of the home screen.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @atomicservice
         * @since 12
         */
        FOLLOW_DESKTOP = 14
    }
    /**
     * Enumerates the module types.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @crossplatform [since 20]
     * @atomicservice [since 11]
     * @since 9
     */
    export enum ModuleType {
        /**
         * Main module of and entry to the application, providing the basic application functionality.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @crossplatform [since 20]
         * @atomicservice [since 11]
         * @since 9
         */
        ENTRY = 1,
        /**
         * Dynamic feature module of the application, extending the application functionality. This type of HAP can be
         * installed based on user needs and device types.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @crossplatform [since 20]
         * @atomicservice [since 11]
         * @since 9
         */
        FEATURE = 2,
        /**
         * [Dynamic shared library](docroot://quick-start/in-app-hsp.md) of the application.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @crossplatform [since 20]
         * @atomicservice [since 11]
         * @since 9
         */
        SHARED = 3
    }
    /**
     * Enumerates the bundle types.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @atomicservice [since 11]
     * @since 9
     */
    export enum BundleType {
        /**
         * The bundle is an application.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @atomicservice [since 11]
         * @since 9
         */
        APP = 0,
        /**
         * The bundle is an atomic service.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @atomicservice [since 11]
         * @since 9
         */
        ATOMIC_SERVICE = 1
    }
    /**
     * Defines the version compatibility type of the dynamic shared library.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @atomicservice [since 11]
     * @since 10
     */
    export enum CompatiblePolicy {
        /**
         * The shared library is backward compatible.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @atomicservice [since 11]
         * @since 10
         */
        BACKWARD_COMPATIBILITY = 1
    }
    /**
     * Enumerates the types of the multi-app mode.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @since 12
     */
    export enum MultiAppModeType {
        /**
         * Unspecified. It is the default value of
         * [multiAppMode](docroot://quick-start/app-configuration-file.md#multiappmode).
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @since 12
         */
        UNSPECIFIED = 0,
        /**
         * [Multi-instance mode](docroot://quick-start/multiInstance.md). A resident process does not support this value.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @since 12
         */
        MULTI_INSTANCE = 1,
        /**
         * [App clone mode](docroot://quick-start/app-clone.md)
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.Core
         * @since 12
         */
        APP_CLONE = 2
    }
    /**
     * Obtains the bundle information of the current application based on the given bundle flags. This API uses a promise
     * to return the result.
     *
     * @param { number } bundleFlags - Type of the bundle information to obtain.
     * @returns { Promise<BundleInfo> } Promise used to return the bundle information.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types.
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @crossplatform [since 20]
     * @atomicservice [since 11]
     * @since 9
     */
    function getBundleInfoForSelf(bundleFlags: number): Promise<BundleInfo>;
    /**
     * Obtains the bundle information of the current application based on the given bundle flags. This API uses an
     * asynchronous callback to return the result.
     *
     * @param { number } bundleFlags - Type of the bundle information to obtain.
     * @param { AsyncCallback<BundleInfo> } callback - [Callback]{@link @ohos.base:AsyncCallback} used to return the
     *     result. If the information is successfully obtained, **err** is **null** and **data** is the bundle information
     *     of the current application. Otherwise, **err** is an error object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types.
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @crossplatform [since 20]
     * @atomicservice [since 11]
     * @since 9
     */
    function getBundleInfoForSelf(bundleFlags: number, callback: AsyncCallback<BundleInfo>): void;
    /**
     * Obtains the bundle information of the current application based on the given bundle flags. This API returns the
     * result synchronously.
     *
     * @param { number } bundleFlags - Type of the bundle information to obtain.
     * @returns { BundleInfo } Bundle information obtained.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types.
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @crossplatform [since 20]
     * @atomicservice [since 11]
     * @since 10
     */
    function getBundleInfoForSelfSync(bundleFlags: number): BundleInfo;
    /**
     * Obtains the bundle information based on the given bundle name and bundle flags. This API uses an asynchronous
     * callback to return the result.
     *
     * No permission is required for obtaining the caller's own information.
     *
     * @permission ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO
     * @param { string } bundleName - Bundle name.
     * @param { number } bundleFlags - Type of the bundle information to obtain.
     * @param { AsyncCallback<BundleInfo> } callback - [Callback]{@link @ohos.base:AsyncCallback} used to return the
     *     result. If the information is successfully obtained, **err** is **null** and **data** is the bundle
     *     information. Otherwise, **err** is an error object.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types.
     * @throws { BusinessError } 17700001 - The specified bundleName is not found.
     * @throws { BusinessError } 17700026 - The specified bundle is disabled.
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @since 14
     */
    function getBundleInfo(bundleName: string, bundleFlags: number, callback: AsyncCallback<BundleInfo>): void;
    /**
     * Obtains the [BundleInfo]{@link bundleManager/BundleInfo} based on the given bundle name, bundle flags, and user
     * ID. This API uses an asynchronous callback to return the result.
     *
     * No permission is required for obtaining the caller's own information.
     *
     * @permission ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO
     * @param { string } bundleName - Bundle name.
     * @param { number } bundleFlags - Type of the bundle information to obtain.
     * @param { number } userId - User ID, which can be obtained by calling
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId(callback: AsyncCallback<number>)}
     *     .
     * @param { AsyncCallback<BundleInfo> } callback - [Callback]{@link @ohos.base:AsyncCallback} used to return the
     *     result. If the information is successfully obtained, **err** is **null** and **data** is the bundle
     *     information. Otherwise, **err** is an error object.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types.
     * @throws { BusinessError } 17700001 - The specified bundleName is not found.
     * @throws { BusinessError } 17700004 - The specified user ID is not found.
     * @throws { BusinessError } 17700026 - The specified bundle is disabled.
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @since 14
     */
    function getBundleInfo(bundleName: string, bundleFlags: number, userId: number, callback: AsyncCallback<BundleInfo>): void;
    /**
     * Obtains the bundle information based on the given bundle name, bundle flags, and user ID. This API uses a promise
     * to return the result.
     *
     * No permission is required for obtaining the caller's own information.
     *
     * @permission ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO
     * @param { string } bundleName - Bundle name.
     * @param { number } bundleFlags - Type of the bundle information to obtain.
     * @param { number } [userId] - User ID, which can be obtained by calling
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId(callback: AsyncCallback<number>)}
     *     . The default value is the user ID of the caller. The value must be greater than or equal to 0.
     * @returns { Promise<BundleInfo> } Promise used to return the bundle information obtained.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types.
     * @throws { BusinessError } 17700001 - The specified bundleName is not found.
     * @throws { BusinessError } 17700004 - The specified user ID is not found.
     * @throws { BusinessError } 17700026 - The specified bundle is disabled.
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @since 14
     */
    function getBundleInfo(bundleName: string, bundleFlags: number, userId?: number): Promise<BundleInfo>;
    /**
     * Obtains the ability information based on the given resource identifier and ability flag. This API uses a promise to
     * return the result.
     *
     * @permission ohos.permission.GET_ABILITY_INFO
     * @param { string } uri - URI of the resource. The value is the same as that of the
     *     [uris field under skills in the module.json5 file](docroot://quick-start/module-configuration-file.md#skills).
     * @param { number } abilityFlags - [Ability flag]{@link @ohos.bundle.bundleManager:bundleManager.AbilityFlag},
     *     indicating the ability information to be obtained.
     * @returns { Promise<Array<AbilityInfo>> } Promise used to return an array of ability information.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 17700003 - The ability is not found.
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @atomicservice
     * @since 20
     */
    function getAbilityInfo(uri: string, abilityFlags: number): Promise<Array<AbilityInfo>>;
    /**
     * Obtains the bundle name based on the given UID. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO
     * @param { number } uid - UID of the application.
     * @param { AsyncCallback<string> } callback - [Callback]{@link @ohos.base:AsyncCallback} used to return the result.
     *     If the information is successfully obtained, **err** is **null** and **data** is the bundle name. Otherwise,
     *     **err** is an error object.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types.
     * @throws { BusinessError } 17700021 - The uid is not found.
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @since 14
     */
    function getBundleNameByUid(uid: number, callback: AsyncCallback<string>): void;
    /**
     * Obtains the bundle name based on the given UID. This API uses a promise to return the result.
     *
     * @permission ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO
     * @param { number } uid - UID of the application.
     * @returns { Promise<string> } Promise used to return the bundle name obtained.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types.
     * @throws { BusinessError } 17700021 - The uid is not found.
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @since 14
     */
    function getBundleNameByUid(uid: number): Promise<string>;
    /**
     * Obtains the bundle name based on the given UID. This API returns the result synchronously.
     *
     * @permission ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO
     * @param { number } uid - UID of the application.
     * @returns { string } Bundle name obtained.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types.
     * @throws { BusinessError } 17700021 - The uid is not found.
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @since 14
     */
    function getBundleNameByUidSync(uid: number): string;
    /**
     * Clears the application cache. This API uses a promise to return the result.
     *
     * @returns { Promise<void> } Promise that returns no value.
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @atomicservice
     * @since 21
     */
    function cleanBundleCacheFilesForSelf(): Promise<void>;
    /**
     * Obtains the Want used to launch the bundle based on the given bundle name and user ID. This API returns the result
     * synchronously.
     *
     * @permission ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or
     *     (ohos.permission.GET_BUNDLE_INFO_PRIVILEGED and ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS)
     * @param { string } bundleName - Bundle name.
     * @param { number } [userId] - User ID, which can be obtained by calling
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId(callback: AsyncCallback<number>)}
     *     . The default value is the user ID of the caller. The value must be greater than or equal to 0.
     * @returns { Want } Want object.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.
     * @throws { BusinessError } 17700001 - The specified bundle is not found.
     * @throws { BusinessError } 17700004 - The specified user id is not found.
     * @throws { BusinessError } 17700026 - The specified bundle is disabled.
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @since 24
     */
    function getLaunchWantForBundleSync(bundleName: string, userId?: number): Want;
    /**
     * Obtains the **Want** parameters of the
     * [entry UIAbility](docroot://quick-start/application-package-glossary.md#uiability) of the current application.
     *
     * @returns { Want } Want object that contains only the bundle name and ability name.
     * @throws { BusinessError } 17700072 - The launch want is not found.
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @atomicservice
     * @since 13
     */
    function getLaunchWant(): Want;
    /**
     * Obtains the JSON string array of the current application's configuration file based on the given module name,
     * ability name, and metadata name (name configured under **metadata** in
     * [abilities](docroot://quick-start/module-configuration-file.md#abilities) of the **module.json5** file). This API
     * uses an asynchronous callback to return the result.
     *
     * > NOTE
     * >
     * > If the profile uses the resource reference format, the return value retains this format (for example,
     * > **$string:res_id**). You can obtain the referenced resources through related APIs of the
     * > [resource manager module]{@link @ohos.resourceManager:resourceManager}.
     *
     * @param { string } moduleName - Module name.
     * @param { string } abilityName - Name of the UIAbility component.
     * @param { string } metadataName - [Metadata name](docroot://quick-start/module-configuration-file.md#metadata) of
     *     the UIAbility component, that is, **name** of the **metadata** tag under
     *     [abilities](docroot://quick-start/module-configuration-file.md#abilities) in the **module.json5** file.
     * @param { AsyncCallback<Array<string>> } callback - [Callback]{@link @ohos.base:AsyncCallback} used to return the
     *     result. If the information is successfully obtained, **err** is **null** and **data** is **Array<string>**.
     *     Otherwise, **err** is an error object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types.
     * @throws { BusinessError } 17700002 - The specified moduleName is not existed.
     * @throws { BusinessError } 17700003 - The specified abilityName is not existed.
     * @throws { BusinessError } 17700024 - Failed to get the profile because there is no profile in the HAP.
     * @throws { BusinessError } 17700029 - The specified ability is disabled.
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @atomicservice [since 11]
     * @since 9
     */
    function getProfileByAbility(moduleName: string, abilityName: string, metadataName: string, callback: AsyncCallback<Array<string>>): void;
    /**
     * Obtains the JSON string array of the current application's configuration file based on the given module name,
     * ability name, and metadata name (name configured under **metadata** in
     * [abilities](docroot://quick-start/module-configuration-file.md#abilities) of the **module.json5** file). This API
     * uses a promise to return the result.
     *
     * > NOTE
     * >
     * > If the profile uses the resource reference format, the return value retains this format (for example,
     * > **$string:res_id**). You can obtain the referenced resources through related APIs of the
     * > [resource manager module]{@link @ohos.resourceManager:resourceManager}.
     *
     * @param { string } moduleName - Module name.
     * @param { string } abilityName - Name of the UIAbility component.
     * @param { string } [metadataName] - Metadata name of the UIAbility component, that is, **name** of the **metadata**
     *     tag under [abilities](docroot://quick-start/module-configuration-file.md#abilities) in the **module.json5**
     *     file. The default value is null.
     * @returns { Promise<Array<string>> } Promise used to return the array of JSON strings obtained.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types.
     * @throws { BusinessError } 17700002 - The specified moduleName is not existed.
     * @throws { BusinessError } 17700003 - The specified abilityName is not existed.
     * @throws { BusinessError } 17700024 - Failed to get the profile because there is no profile in the HAP.
     * @throws { BusinessError } 17700029 - The specified ability is disabled.
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @atomicservice [since 11]
     * @since 9
     */
    function getProfileByAbility(moduleName: string, abilityName: string, metadataName?: string): Promise<Array<string>>;
    /**
     * Obtains the JSON string array of the current application's configuration file based on the given module name,
     * ability name, and metadata name (name configured in
     * [metadata](docroot://quick-start/module-configuration-file.md#metadata) of the **module.json5** file). This API
     * returns the result synchronously. The result value is a string array.
     *
     * @param { string } moduleName - Module name.
     * @param { string } abilityName - Name of the UIAbility component.
     * @param { string } [metadataName] - Metadata name of the UIAbility component, that is, **name** of the **metadata**
     *     tag under [abilities](docroot://quick-start/module-configuration-file.md#abilities) in the **module.json5**
     *     file. The default value is null.
     * @returns { Array<string> } An array of JSON strings.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types.
     * @throws { BusinessError } 17700002 - The specified moduleName is not existed.
     * @throws { BusinessError } 17700003 - The specified abilityName is not existed.
     * @throws { BusinessError } 17700024 - Failed to get the profile because there is no profile in the HAP.
     * @throws { BusinessError } 17700029 - The specified ability is disabled.
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @atomicservice [since 11]
     * @since 10
     */
    function getProfileByAbilitySync(moduleName: string, abilityName: string, metadataName?: string): Array<string>;
    /**
     * Obtains the JSON string array of the current application's configuration file based on the given module name,
     * ExtensionAbility name, and metadata name (name configured in
     * [metadata](docroot://quick-start/module-configuration-file.md#metadata) of the **module.json5** file). This API
     * uses an asynchronous callback to return the result.
     *
     * @param { string } moduleName - Module name.
     * @param { string } extensionAbilityName - Name of the ExtensionAbility component.
     * @param { string } metadataName - Metadata name of the ExtensionAbility component, that is, **name** of the
     *     **metadata** tag under
     *     [extensionAbilities](docroot://quick-start/module-configuration-file.md#extensionabilities) in the
     *     **module.json5** file.
     * @param { AsyncCallback<Array<string>> } callback - [Callback]{@link @ohos.base:AsyncCallback} used to return the
     *     result. If the information is successfully obtained, **err** is **null** and **data** is **Array<string>**.
     *     Otherwise, **err** is an error object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types.
     * @throws { BusinessError } 17700002 - The specified moduleName is not existed.
     * @throws { BusinessError } 17700003 - The specified extensionAbilityName not existed.
     * @throws { BusinessError } 17700024 - Failed to get the profile because there is no profile in the HAP.
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @atomicservice [since 11]
     * @since 9
     */
    function getProfileByExtensionAbility(moduleName: string, extensionAbilityName: string, metadataName: string, callback: AsyncCallback<Array<string>>): void;
    /**
     * Obtains the JSON string array of the current application's configuration file based on the given module name,
     * ExtensionAbility name, and metadata name (name configured in
     * [metadata](docroot://quick-start/module-configuration-file.md#metadata) of the **module.json5** file). This API
     * uses a promise to return the result.
     *
     * @param { string } moduleName - Module name.
     * @param { string } extensionAbilityName - Name of the ExtensionAbility component.
     * @param { string } [metadataName] - Metadata name of the ExtensionAbility component, that is, **name** of the
     *     **metadata** tag under
     *     [extensionAbilities](docroot://quick-start/module-configuration-file.md#extensionabilities) in the
     *     **module.json5** file. The default value is null.
     * @returns { Promise<Array<string>> } Promise used to return the array of JSON strings obtained.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types.
     * @throws { BusinessError } 17700002 - The specified moduleName is not existed.
     * @throws { BusinessError } 17700003 - The specified extensionAbilityName not existed.
     * @throws { BusinessError } 17700024 - Failed to get the profile because there is no profile in the HAP.
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @atomicservice [since 11]
     * @since 9
     */
    function getProfileByExtensionAbility(moduleName: string, extensionAbilityName: string, metadataName?: string): Promise<Array<string>>;
    /**
     * Obtains the JSON string array of the current application's configuration file based on the given module name,
     * ExtensionAbility name, and metadata name (name configured in
     * [metadata](docroot://quick-start/module-configuration-file.md#metadata) of the **module.json5** file). This API
     * returns the result synchronously. The result value is a string array.
     *
     * @param { string } moduleName - Module name.
     * @param { string } extensionAbilityName - Name of the ExtensionAbility component.
     * @param { string } [metadataName] - Metadata name of the ExtensionAbility component, that is, **name** of the
     *     **metadata** tag under
     *     [extensionAbilities](docroot://quick-start/module-configuration-file.md#extensionabilities) in the
     *     **module.json5** file. The default value is null.
     * @returns { Array<string> } An array of JSON strings.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types.
     * @throws { BusinessError } 17700002 - The specified moduleName is not existed.
     * @throws { BusinessError } 17700003 - The specified extensionAbilityName not existed.
     * @throws { BusinessError } 17700024 - Failed to get the profile because there is no profile in the HAP.
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @atomicservice [since 11]
     * @since 10
     */
    function getProfileByExtensionAbilitySync(moduleName: string, extensionAbilityName: string, metadataName?: string): Array<string>;
    /**
     * Obtains the bundle information based on the given bundle name, bundle flags, and user ID. This API returns the
     * result synchronously.
     *
     * No permission is required for obtaining the caller's own information.
     *
     * @permission ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO
     * @param { string } bundleName - Bundle name.
     * @param { number } bundleFlags - Type of the bundle information to obtain.
     * @param { number } userId - User ID, which can be obtained by calling
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId(callback: AsyncCallback<number>)}
     *     .
     * @returns { BundleInfo } Bundle information obtained.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types.
     * @throws { BusinessError } 17700001 - The specified bundleName is not found.
     * @throws { BusinessError } 17700004 - The specified user ID is not found.
     * @throws { BusinessError } 17700026 - The specified bundle is disabled.
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @since 14
     */
    function getBundleInfoSync(bundleName: string, bundleFlags: number, userId: number): BundleInfo;
    /**
     * Obtains the bundle information for the caller's user based on the given bundle name and bundle flags. This API
     * returns the result synchronously.
     *
     * No permission is required for obtaining the caller's own information.
     *
     * @permission ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO
     * @param { string } bundleName - Bundle name.
     * @param { number } bundleFlags - Type of the bundle information to obtain.
     * @returns { BundleInfo } Bundle information obtained.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types.
     * @throws { BusinessError } 17700001 - The specified bundleName is not found.
     * @throws { BusinessError } 17700026 - The specified bundle is disabled.
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @since 14
     */
    function getBundleInfoSync(bundleName: string, bundleFlags: number): BundleInfo;
    /**
     * Queries the alternate icon information configured in the alternateIcons in the app.json5
     * of the current application. This API uses a promise to return the result.
     *
     * @returns { Promise<Array<AlternateIconInfo>> } Promise used to return the list of alternate
     *     icons of the current application.
     * @throws { BusinessError } 17700311 - Failed to obtain the alternate icon.
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    function getAlternateIcons(): Promise<Array<AlternateIconInfo>>;
    /**
     * Sets the alternate icon of the caller based on the given alternate icon name.
     * This API uses a promise to return the result.
     *
     * @param { string } alternateIconName - Name of the alternate icon to be set.
     *     The alternate icon name must be in the name field of alternateIcons in app.json5.
     *     If alternateIconName is left empty, the alternate icon is canceled.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 17700308 - The alternateIconName must match the name field under alternateIcons
     *     in the app.json5 file.
     * @throws { BusinessError } 17700309 - No alternate icon is enabled.
     * @throws { BusinessError } 17700310 - Failed to set the alternate icon.
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    function setAlternateIcon(alternateIconName: string): Promise<void>;
    /**
     * Checks whether the target application can be accessed based on the provided link. The scheme specified in the link
     * must be configured in the **querySchemes** field of the
     * [module.json5](docroot://quick-start/module-configuration-file.md) file.
     *
     * @param { string } link - Link to check.
     * @returns { boolean } Check result for whether the link can be opened. **true** if it can be opened, **false**
     *     otherwise.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types.
     * @throws { BusinessError } 17700055 - The specified link is invalid.
     * @throws { BusinessError } 17700056 - The scheme of the specified link is not in the querySchemes.
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @atomicservice
     * @since 12
     */
    function canOpenLink(link: string): boolean;
    /**
     * Obtains the [signature information]{@link bundleManager/BundleInfo:SignatureInfo} of an application based on the
     * given UID.
     *
     * @permission ohos.permission.GET_SIGNATURE_INFO
     * @param { number } uid - UID of the application.
     * @returns { SignatureInfo } SignatureInfo object.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 17700021 - The uid is not found.
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @since 18
     */
    function getSignatureInfo(uid: number): SignatureInfo;
    /**
     * Obtains the bundle name and clone index of a cloned application based on the given UID. This API uses a promise to
     * return the result.
     *
     * @permission ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO
     * @param { number } uid - UID of the application.
     * @returns { Promise<AppCloneIdentity> } Promise used to return the application clone index.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types.
     * @throws { BusinessError } 17700021 - The uid is not found.
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @since 14
     */
    function getAppCloneIdentity(uid: number): Promise<AppCloneIdentity>;
    /**
     * Obtains the installation path of a specified plugin in the current
     * [application sandbox](docroot://file-management/app-sandbox-directory.md).
     *
     * @param { string } pluginBundleName - Bundle name of the target plugin.
     * @returns { string } Installation path of the target plugin in the current application sandbox.
     * @throws { BusinessError } 17700001 - The specified bundleName is not found.
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @since 22
     */
    function getPluginBundlePathForSelf(pluginBundleName: string): string;
    /**
     * Obtains all the bundle information in the system based on the given bundle flags.
     * This API uses a promise to return the result.
     *
     * @permission ohos.permission.ENTERPRISE_GET_INSTALLED_BUNDLE_LIST
     * @param { number } bundleFlags - Information contained in the returned BundleInfo. For
     *     details, see {@link BundleFlag}.
     * @returns { Promise<Array<BundleInfo>> } Promise used to return the list of
     *     installed applications.
     * @throws { BusinessError } 201 - Permission denied.
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    function getInstalledBundleList(bundleFlags: number): Promise<Array<BundleInfo>>;
    /**
     * Obtains the name of an application with the specified package name and clone index.
     * This API uses a promise to return the result.
     *
     * @permission ohos.permission.GET_BUNDLE_INFO_PRIVILEGED
     * @param { string } bundleName - Bundle name of the application.
     * @param { number } appIndex - Index of the application. The value ranges from 0 to 5.
     *     The value 0 indicates the main application, and the values 1 to 5 indicate the indexes of application clones.
     * @returns { Promise<string> } Promise used to return the result. If the operation is successful, the application
     *     name is returned. Otherwise, an error object is returned.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 17700001 - The specified bundle is not found.
     * @throws { BusinessError } 17700061 - The specified app index is invalid.
     * @syscap SystemCapability.BundleManager.BundleFramework.Resource
     * @stagemodelonly
     * @since 26.0.0
     */
    function getApplicationLabel(bundleName: string, appIndex: number): Promise<string>;
    /**
     * Defines the application information.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @crossplatform [since 20]
     * @atomicservice [since 11]
     * @since 9
     */
    export type ApplicationInfo = _ApplicationInfo;
    /**
     * Defines the metadata of a module.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @crossplatform [since 20]
     * @atomicservice [since 11]
     * @since 10
     */
    export type ModuleMetadata = _ModuleMetadata;
    /**
     * Defines the metadata.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @crossplatform [since 20]
     * @atomicservice [since 11]
     * @since 9
     */
    export type Metadata = _Metadata;
    /**
     * Defines the bundle information.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @crossplatform [since 20]
     * @atomicservice [since 11]
     * @since 9
     */
    export type BundleInfo = _BundleInfo.BundleInfo;
    /**
     * Defines the use scenario and timing for using the permission.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @crossplatform [since 20]
     * @atomicservice [since 11]
     * @since 9
     */
    export type UsedScene = _BundleInfo.UsedScene;
    /**
     * Defines the detailed information of the permissions to request from the system.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @crossplatform [since 20]
     * @atomicservice [since 11]
     * @since 9
     */
    export type ReqPermissionDetail = _BundleInfo.ReqPermissionDetail;
    /**
     * Defines the signature information of the bundle.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @crossplatform [since 20]
     * @atomicservice [since 11]
     * @since 9
     */
    export type SignatureInfo = _BundleInfo.SignatureInfo;
    /**
     * Describes the identity information of an application clone.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @since 15
     */
    export type AppCloneIdentity = _BundleInfo.AppCloneIdentity;
    /**
     * Defines the module information.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @crossplatform [since 20]
     * @atomicservice [since 11]
     * @since 9
     */
    export type HapModuleInfo = _HapModuleInfo.HapModuleInfo;
    /**
     * Defines the preloaded module information in the atomic service.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @atomicservice [since 11]
     * @since 9
     */
    export type PreloadItem = _HapModuleInfo.PreloadItem;
    /**
     * Defines the information about the dynamic shared libraries on which the module depends.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @atomicservice [since 11]
     * @since 9
     */
    export type Dependency = _HapModuleInfo.Dependency;
    /**
     * Defines the router table configuration of the module.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @atomicservice
     * @since 12
     */
    export type RouterItem = _HapModuleInfo.RouterItem;
    /**
     * Defines the user-defined data in the routing table configuration of the module.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @atomicservice
     * @since 12
     */
    export type DataItem = _HapModuleInfo.DataItem;
    /**
     * Defines the ability information.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @crossplatform [since 20]
     * @atomicservice [since 11]
     * @since 9
     */
    export type AbilityInfo = _AbilityInfo.AbilityInfo;
    /**
     * Defines the window size.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @crossplatform [since 20]
     * @atomicservice [since 11]
     * @since 9
     */
    export type WindowSize = _AbilityInfo.WindowSize;
    /**
     * Defines the ExtensionAbility information.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @atomicservice [since 11]
     * @since 9
     */
    export type ExtensionAbilityInfo = _ExtensionAbilityInfo.ExtensionAbilityInfo;
    /**
     * Defines the element name.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @atomicservice [since 11]
     * @since 9
     */
    export type ElementName = _ElementName;
    /**
     * Defines the skill information.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @atomicservice
     * @since 12
     */
    export type Skill = _Skill.Skill;
    /**
     * Defines the SkillUri information.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @atomicservice
     * @since 12
     */
    export type SkillUrl = _Skill.SkillUri;
    /**
     * Describes the alternate icon information of an application.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    export type AlternateIconInfo = _BundleInfo.AlternateIconInfo;
}
export default bundleManager;

```
