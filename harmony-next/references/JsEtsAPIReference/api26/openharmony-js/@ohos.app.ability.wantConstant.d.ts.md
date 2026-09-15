# @ohos.app.ability.wantConstant.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022-2024 Huawei Device Co., Ltd.
 * Licensed under the Apache License, Version 2.0 (the "License"),
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
/**
 * The wantConstant module provides the actions, entities, and flags used in Want objects.
 *
 * @syscap SystemCapability.Ability.AbilityBase
 * @atomicservice [since 11]
 * @since 9
 */
declare namespace wantConstant {
    /**
     * Defines **Params** (specifying the action that can be performed) in the Want.
     *
     * @syscap SystemCapability.Ability.AbilityBase
     * @atomicservice [since 11]
     * @since 9
     */
    export enum Params {
        /**
         * Whether redirection back across mission stacks is supported.
         *
         * This parameter controls the redirection-back logic across applications, altering the application transition
         * behavior when the user presses the back button. For example, if UIAbility A is currently displayed and UIAbility
         * B is launched with this parameter set to **true**, exiting UIAbility B will return to UIAbility A. If this
         * parameter is not set, the system defaults to returning to the home screen. Note that this parameter is only
         * supported for system applications and does not take effect for third-party applications.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @atomicservice [since 11]
         * @since 9
         */
        ABILITY_BACK_TO_OTHER_MISSION_STACK = 'ability.params.backToOtherMissionStack',
        /**
         * Whether the ability has been restarted due to a fault.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @atomicservice [since 11]
         * @since 10
         */
        ABILITY_RECOVERY_RESTART = 'ohos.ability.params.abilityRecoveryRestart',
        /**
         * Title for sharing in an atomic service.
         *
         * You can set the sharing title using this field in the
         * [onShare]{@link ./@ohos.app.ability.UIAbility:UIAbility.onShare} callback.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @atomicservice [since 11]
         * @since 10
         */
        CONTENT_TITLE_KEY = 'ohos.extra.param.key.contentTitle',
        /**
         * Content abstract for sharing in an atomic service.
         *
         * You can set the sharing abstract using this field in the
         * [onShare]{@link ./@ohos.app.ability.UIAbility:UIAbility.onShare} callback.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @atomicservice [since 11]
         * @since 10
         */
        SHARE_ABSTRACT_KEY = 'ohos.extra.param.key.shareAbstract',
        /**
         * URL link for sharing in an atomic service.
         *
         * You can set the URL link using this field in the
         * [onShare]{@link ./@ohos.app.ability.UIAbility:UIAbility.onShare} callback.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @atomicservice [since 11]
         * @since 10
         */
        SHARE_URL_KEY = 'ohos.extra.param.key.shareUrl',
        /**
         * Whether to migrate the page stack information during cross-device migration. The default value is **true**,
         * indicating that the page stack information is automatically migrated during cross-device migration.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @atomicservice [since 11]
         * @since 10
         */
        SUPPORT_CONTINUE_PAGE_STACK_KEY = 'ohos.extra.param.key.supportContinuePageStack',
        /**
         * Whether the source application exits during cross-device migration. The default value is** true**, indicating
         * that the source application automatically exits during cross-device migration.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @atomicservice [since 11]
         * @since 10
         */
        SUPPORT_CONTINUE_SOURCE_EXIT_KEY = 'ohos.extra.param.key.supportContinueSourceExit',
        /**
         * Display mode of the [EmbeddableUIAbility]{@link ./@ohos.app.ability.EmbeddableUIAbility:EmbeddableUIAbility}.
         * The value is an enumerated value of [ShowMode]{@link ShowMode}.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @atomicservice
         * @since 12
         */
        SHOW_MODE_KEY = 'ohos.extra.param.key.showMode',
        /**
         * List of file URIs authorized to the target. The value must be an array of file URIs of the string type. For
         * details about how to obtain the file URI, see [fileUri]{@link ./@ohos.file.fileuri:fileUri.getUriFromPath}. This
         * field must be used in conjunction with file URI
         * [read/write flag]{@link Flags}.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @atomicservice
         * @since 12
         */
        PARAMS_STREAM = 'ability.params.stream',
        /**
         * Index of an application clone.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @atomicservice
         * @since 12
         */
        APP_CLONE_INDEX_KEY = 'ohos.extra.param.key.appCloneIndex',
        /**
         * Request code
         *
         * that uniquely identifies the caller of
         * [startAbilityForResult]{@link ./application/UIAbilityContext:UIAbilityContext.startabilityforresult} or
         * [openLink]{@link ./application/UIAbilityContext:UIAbilityContext.openLink}. When either of the APIs is called to
         *  start an ability, the target ability returns the result to the caller based on the request code.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @atomicservice
         * @since 12
         */
        CALLER_REQUEST_CODE = 'ohos.extra.param.key.callerRequestCode',
        /**
         * Page path for an atomic service.
         *
         * If page redirection in an atomic service is implemented using [router](docroot://ui/arkts-routing.md), you can use
         * this parameter to specify the target page, for example, **library/ets/pages/menu**.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @atomicservice
         * @since 12
         */
        PAGE_PATH = 'ohos.param.atomicservice.pagePath',
        /**
         * Router name for page redirection in an atomic service.
         *
         * If page redirection in an atomic service is implemented using
         * [Navigation](docroot://ui/arkts-navigation-architecture.md), you can use **ROUTER_NAME**, **PAGE_SOURCE_FILE**, and
         * **BUILD_FUNCTION** together to specify the target page.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @atomicservice
         * @since 12
         */
        ROUTER_NAME = 'ohos.param.atomicservice.routerName',
        /**
         * Source file for the page in an atomic service.
         *
         * If page redirection in an atomic service is implemented using
         * [Navigation](docroot://ui/arkts-navigation-architecture.md), you can use **ROUTER_NAME**, **PAGE_SOURCE_FILE**, and
         * **BUILD_FUNCTION** together to specify the target page.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @atomicservice
         * @since 12
         */
        PAGE_SOURCE_FILE = 'ohos.param.atomicservice.pageSourceFile',
        /**
         * Build function for the page in an atomic service.
         *
         * If page redirection in an atomic service is implemented using
         * [Navigation](docroot://ui/arkts-navigation-architecture.md), you can use **ROUTER_NAME**, **PAGE_SOURCE_FILE**, and
         * **BUILD_FUNCTION** together to specify the target page.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @atomicservice
         * @since 12
         */
        BUILD_FUNCTION = 'ohos.param.atomicservice.buildFunction',
        /**
         * Sub-package name for an atomic service. Application packages can be developed with multiple modules, and each
         * package may include one or multiple HAPs or HSPs. To enhance the launch speed, atomic services restrict the size
         * of HAP and HSP files and optimize the startup process. This modular development approach is known as sub-
         * packaging.
         *
         * When you open an atomic service, you can use this parameter to activate the specific sub-package.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @atomicservice
         * @since 12
         */
        SUB_PACKAGE_NAME = 'ohos.param.atomicservice.subpackageName',
        /**
         * Specific application instance.
         *
         * When you create [multiple instances](docroot://quick-start/multiInstance.md) of an application, the system assigns a
         * unique ID to each instance. During application transitions, you can use this parameter to specify which created
         * application instance you want to transition to.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 14
         */
        APP_INSTANCE_KEY = 'ohos.extra.param.key.appInstance',
        /**
         * Whether to create an application instance. The default value is **false**, indicating that no new application
         * instance is created.
         *
         * You can set this parameter to **true** to launch a new application instance. Note that the application to be
         * launched must support multiple instances. For details, see
         * [Creating an Application Multi-Instance](docroot://quick-start/multiInstance.md).
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 14
         */
        CREATE_APP_INSTANCE_KEY = 'ohos.extra.param.key.createAppInstance',
        /**
         * Clone index of the caller.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 14
         */
        CALLER_APP_CLONE_INDEX = 'ohos.param.callerAppCloneIndex',
        /**
         * The target ability is a plugin ability.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 19
         */
        DESTINATION_PLUGIN_ABILITY = 'ohos.params.pluginAbility',
        /**
         * Filter list of applications for implicit launch.
         *
         * Only applications in the list are matched during implicit launch. The value is an array of
         * [AppIdentifier]{@link ./bundleManager/BundleInfo:BundleInfo.AppIdentifier} of the string type. The filter list
         * supports a maximum of 50 applications. Passing an empty array will have no effect.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @atomicservice
         * @since 17
         */
        APP_LAUNCH_TRUSTLIST = 'ohos.params.appLaunchTrustList',
        /**
         * Page stack information of the atomic service being launched. This parameter takes effect only when the caller is
         * a UIAbilityContext and the callee is an atomic service.
         *
         * For example, if an atomic service contains a home page and a second page, and you want to directly launch the
         * second page, you can pass the page stack information of the second page through this field when launching the
         * atomic service.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @atomicservice
         * @since 20
         */
        ATOMIC_SERVICE_SHARE_ROUTER = 'ohos.params.atomicservice.shareRouter',
        /**
         * Reason for launching the application.
         *
         * The caller must be a system application and must request the ohos.permission.SET_LAUNCH_REASON_MESSAGE
         * permission. The following values are supported:
         *
         * **ReasonMessage_SystemShare**: The application is launched through system sharing.
         *
         * **ReasonMessage_DesktopShortcut**: The application is launched through a home screen shortcut.
         *
         * **ReasonMessage_Notification**: The application is launched through a notification.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @atomicservice
         * @since 18
         */
        LAUNCH_REASON_MESSAGE = 'ohos.params.launchReasonMessage',
        /**
         * Unique identifier for file sharing based on [UDMF]{@link ./@ohos.data.unifiedDataChannel:unifiedDataChannel}.
         * This field can only be set by system applications, but third-party applications can read it.
         *
         * If the Want contains a URI authorization flag (for example, [FLAG_AUTH_READ_URI_PERMISSION]{@link Flags} or
         * [FLAG_AUTH_WRITE_URI_PERMISSION]{@link Flags}) and the **PARAMS_STREAM** field is also present, this field does
         * not take effect.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @atomicservice
         * @since 20
         */
        ABILITY_UNIFIED_DATA_KEY = 'ohos.param.ability.udKey'
    }
    /**
     * Enumerates the common preset keywords of the [Want.flags]{@link ./@ohos.app.ability.Want:Want} field. You can use
     * these predefined keywords to set or retrieve additional flag information carried in application transitions.
     *
     * @syscap SystemCapability.Ability.AbilityBase
     * @atomicservice [since 11]
     * @since 9
     */
    export enum Flags {
        /**
         * Temporarily grants the receiver read permission for the URI.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @atomicservice [since 11]
         * @since 9
         */
        FLAG_AUTH_READ_URI_PERMISSION = 0x00000001,
        /**
         * Temporarily grants the receiver write permission for the URI.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @atomicservice [since 11]
         * @since 9
         */
        FLAG_AUTH_WRITE_URI_PERMISSION = 0x00000002,
        /**
         * The URI can be persisted by the receiver. It takes effect only on 2-in-1 devices and tablets.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 12
         */
        FLAG_AUTH_PERSISTABLE_URI_PERMISSION = 0x00000040,
        /**
         * Enables on-demand installation when launching an atomic service.
         *
         * - If enabled, the system automatically installs the atomic service if it is not already installed before
         * proceeding with the launch.
         * - If disabled, the launch fails if the atomic service is not installed.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @atomicservice [since 11]
         * @since 9
         */
        FLAG_INSTALL_ON_DEMAND = 0x00000800,
        /**
         * In multi-device collaboration scenario, the caller application must initiate a request through the DMS, with this
         *  flag included in the **Flags** field, in order to invoke the lifecycle callback
         * [onCollaborate()]{@link ./@ohos.app.ability.UIAbility:UIAbility.onCollaborate}
         * of the target application.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 18
         */
        FLAG_ABILITY_ON_COLLABORATE = 0x00002000,
        /**
         * Disables the "No available applications" prompt during implicit application launches.
         *
         * When [launching an application implicitly](docroot://application-models/app-startup-overview.md), a prompt saying "No
         *  available applications" will appear if no matching application is found. You can use this flag to prevent this
         * prompt from appearing.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 11
         */
        FLAG_START_WITHOUT_TIPS = 0x40000000
    }
    /**
     * Enumerates the display modes of an
     * [EmbeddableUIAbility]{@link ./@ohos.app.ability.EmbeddableUIAbility:EmbeddableUIAbility} when it is launched.
     *
     * @syscap SystemCapability.Ability.AbilityBase
     * @atomicservice
     * @since 12
     */
    export enum ShowMode {
        /**
         * An independent window is used to show the ability startup.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @atomicservice
         * @since 12
         */
        WINDOW = 0,
        /**
         * An embedded full-screen is used to show the ability startup.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @atomicservice
         * @since 12
         */
        EMBEDDED_FULL = 1,
        /**
         * An embedded half-screen is used to show the ability startup.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        EMBEDDED_HALF = 2
    }
    /**
     * Enumerates the action constants of the Want object. **action** specifies the operation to execute.
     *
     * @syscap SystemCapability.Ability.AbilityBase
     * @stagemodelonly
     * @since 26.0.0
     */
    export enum Action {
        /**
         * Action of launching the UI for sending a message to a specified recipient.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @stagemodelonly
         * @since 26.0.0
         */
        ACTION_SEND_TO_DATA = 'ohos.want.action.sendToData'
    }
}
export default wantConstant;

```
