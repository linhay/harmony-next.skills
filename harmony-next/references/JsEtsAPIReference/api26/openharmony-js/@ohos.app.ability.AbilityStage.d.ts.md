# @ohos.app.ability.AbilityStage.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022-2023 Huawei Device Co., Ltd.
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
import AbilityConstant from './@ohos.app.ability.AbilityConstant';
import AbilityStageContext from './application/AbilityStageContext';
import Want from './@ohos.app.ability.Want';
import { Configuration } from './@ohos.app.ability.Configuration';
/**
 * AbilityStage is a [module](docroot://quick-start/application-package-overview.md#multi-module-design-mechanism)-level
 * component manager. It is used for initializing operations such as resource preloading and thread creation at the
 * module level, as well as maintaining the application state under the module. An AbilityStage instance corresponds to
 * a module.
 *
 * When the [HAP](docroot://quick-start/hap-package.md) or [HSP](docroot://quick-start/in-app-hsp.md) of an application
 * is first loaded, an AbilityStage instance is created. If a module contains both AbilityStage and other components (
 * like UIAbility or ExtensionAbility), the AbilityStage instance is created before the other component instances.
 *
 * An AbilityStage has the lifecycle callbacks [onCreate()]{@link AbilityStage.onCreate} and
 * [onDestroy()]{@link AbilityStage.onDestroy}, and the event callbacks
 * [onAcceptWant()]{@link AbilityStage.onAcceptWant},
 * [onConfigurationUpdate()]{@link AbilityStage.onConfigurationUpdate}, and
 * [onMemoryLevel()]{@link AbilityStage.onMemoryLevel}.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @stagemodelonly
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare class AbilityStage {
    /**
     * Context of an AbilityStage.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    context: AbilityStageContext;
    /**
     * Called when an AbilityStage instance is created. Such an instance is automatically created by the system before it
     * loads the first Ability instance of the module.
     *
     * You can initialize the module (for example, preload resources or create threads) in this callback. This API returns
     * the result synchronously and does not support asynchronous callbacks.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    onCreate(): void;
    /**
     * Called when a UIAbility with the launch mode set to
     * [specified](docroot://application-models/uiability-launch-type.md#specified) is launched. This API returns a string
     * representing the unique ID of the UIAbility instance. This API returns the result synchronously and does not
     * support asynchronous callbacks.
     *
     * If a UIAbility instance with the same ID already exists in the system, that instance is reused. Otherwise, a new
     * instance is created.
     *
     * > **NOTE**
     * >
     * > Starting from API version 20, this callback is not triggered when
     * > [AbilityStage.onAcceptWantAsync]{@link AbilityStage.onAcceptWantAsync} is implemented.
     *
     * @param { Want } want - Want type parameter that includes the launch parameters provided by the caller, such as the
     *     ability name and bundle name.
     * @returns { string } ID of the UIAbility. If a UIAbility with the same ID has been launched, that UIAbility is
     *     reused. Otherwise, a new instance is created and launched.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice [since 11]
     * @since 9
     */
    onAcceptWant(want: Want): string;
    /**
     * Called when a UIAbility with the launch mode set to
     * [specified](docroot://application-models/uiability-launch-type.md#specified) is launched. This API returns a string
     * representing the unique ID of the UIAbility instance. This API uses a promise to return the result.
     *
     * If a UIAbility instance with the same ID already exists in the system, that instance is reused. Otherwise, a new
     * instance is created.
     *
     * @param { Want } want - Want information about the target UIAbility, such as the UIAbility name and bundle name.
     * @returns { Promise<string> } Promise used to return a string that uniquely identifies the UIAbility instance
     *     launched. If a UIAbility instance with the same ID already exists in the system, that instance is reused.
     *     Otherwise, a new instance is created.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    onAcceptWantAsync(want: Want): Promise<string>;
    /**
     * Called when a UIAbility<!--Del--> or UIExtensionAbility<!--DelEnd-->, which is configured to run in an independent
     * process (with **isolationProcess** set to **true** in the
     * [module.json5](docroot://quick-start/module-configuration-file.md) file), is launched. This API returns a string
     * representing the unique process ID. This API returns the result synchronously and does not support asynchronous
     * callbacks.
     *
     * If the application already has a process with the same ID, the UIAbility<!--Del--> or UIExtensionAbility<!--DelEnd-
     * -> runs in that process. Otherwise, a new process is created.
     *
     * If you implement both **onNewProcessRequest** and [onAcceptWant]{@link AbilityStage.onAcceptWant}, the system first
     * invokes the **onNewProcessRequest** callback, and then the **onAcceptWant** callback.
     *
     * <!--Del-->
     *
     * The **isolationProcess** field can be set to **true** in the
     * [module.json5](docroot://quick-start/module-configuration-file.md) file, but only for the UIExtensionAbility of the
     * sys/commonUI type.
     *
     * <!--DelEnd-->
     *
     * > **NOTE**
     * >
     * > - In API version 19 and earlier, only a UIAbility can be launched in the specified process. <!--Del-->Starting
     * > from API version 20, a UIExtensionAbility can also be launched in the specified process.<!--DelEnd-->
     * >
     * > - Starting from API version 20, this callback is not executed when
     * > [AbilityStage.onNewProcessRequestAsync]{@link AbilityStage.onNewProcessRequestAsync} is implemented.
     *
     * @param { Want } want - Want type parameter that includes the launch parameters provided by the caller, such as the
     *     UIAbility<!--Del--> or UIExtensionAbility<!--DelEnd--> name and bundle name.
     * @returns { string } Custom process identifier. If the process with this identifier has been created, the ability
     *     runs in the process. Otherwise, a new process is created and the ability runs in it.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 11
     */
    onNewProcessRequest(want: Want): string;
    /**
     * Called when a UIAbility<!--Del--> or UIExtensionAbility<!--DelEnd-->, which is configured to run in an independent
     * process (with **isolationProcess** set to **true** in the
     * [module.json5](docroot://quick-start/module-configuration-file.md) file), is launched. This API returns a string
     * representing the unique process ID. This API uses a promise to return the result.
     *
     * If the application already has a process with the same ID, the UIAbility<!--Del--> or UIExtensionAbility<!--DelEnd-
     * -> runs in that process. Otherwise, a new process is created.
     *
     * <!--Del-->
     *
     * The **isolationProcess** field can be set to **true** in the
     * [module.json5](docroot://quick-start/module-configuration-file.md) file, but only for the UIExtensionAbility of the
     * sys/commonUI type.
     *
     * <!--DelEnd-->
     *
     * @param { Want } want - Want type parameter that includes the launch parameters provided by the caller, such as the
     *     UIAbility<!--Del--> or UIExtensionAbility<!--DelEnd--> name and bundle name.
     * @returns { Promise<string> } Promise used to return a string representing the process ID. If the application
     *     already has a process with the same ID, the UIAbility<!--Del--> or UIExtensionAbility<!--DelEnd--> runs in that
     *     process. Otherwise, a new process is created.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    onNewProcessRequestAsync(want: Want): Promise<string>;
    /**
     * Called when the system global configuration (such as the system language and dark/light color mode) changes. All
     * the configuration items are defined in the [Configuration]{@link @ohos.app.ability.Configuration:Configuration}
     * class. This API returns the result synchronously and does not support asynchronous callbacks.
     *
     * > **NOTE**
     * >
     * > There are certain restrictions when this callback is actually triggered. For example, if you set the application
     * > language by calling [setLanguage]{@link ./application/ApplicationContext:ApplicationContext.setLanguage}, the
     * > system does not trigger the **onConfigurationUpdate** callback even if the system language changes. For details,
     * > see [When to Use](docroot://application-models/subscribe-system-environment-variable-changes.md#when-to-use).
     *
     * @param { Configuration } newConfig - Callback invoked when the global configuration is updated. The global
     *     configuration indicates the configuration of the environment where the application is running and includes the
     *     language and color mode.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    onConfigurationUpdate(newConfig: Configuration): void;
    /**
     * Listens for changes in the system memory level status. Called when the available memory of the entire device
     * changes to a specified level. You can implement this callback to promptly release non-essential resources (such as
     * cached data or temporary objects) upon receiving a memory shortage event, thereby preventing the application
     * process from being forcibly terminated by the system.
     *
     * This API returns the result synchronously and does not support asynchronous callbacks.
     *
     * > **NOTE**
     * >
     * > Releasing UI components in the **onMemoryLevel** callback may block the main thread tasks of the current process.
     * > Therefore, you are advised not to release UI components in this callback.
     *
     * @param { AbilityConstant.MemoryLevel } level - Memory level that indicates the memory usage status. When the
     *     specified memory level is reached, a callback will be invoked and the system will start adjustment.<br>**NOTE**
     *     <br>The trigger conditions may differ across various devices. For example, on a standard device with 12 GB of
     *     memory:<br>- A callback with value 0 is triggered when available memory drops between 1700 MB and 1800 MB.<br>-
     *     A callback with value 1 is triggered when available memory drops between 1600 MB and 1700 MB.<br>- A callback
     *     with value 2 is triggered when available memory falls below 1600 MB.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @crossplatform [since 26.0.0]
     * @atomicservice [since 11]
     * @since 9
     */
    onMemoryLevel(level: AbilityConstant.MemoryLevel): void;
    /**
     * Called when the last Ability instance of the corresponding module exits. This API is called during the normal
     * lifecycle. If the application exits abnormally or is terminated, this API is not called. This API returns the
     * result synchronously and does not support asynchronous callbacks.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 12
     */
    onDestroy(): void;
    /**
     * Called when the application is closed by the user, allowing the user to choose between immediate termination or
     * cancellation. This API returns the result synchronously and does not support asynchronous callbacks.
     *
     * > **NOTE**
     * >
     * > - The API is called only when the application exits under normal circumstances (for example, when the application
     * > is closed through the doc bar or tray, or when the application shuts down along with the device). It will not be
     * > called if the application is terminated forcibly.
     * >
     * > - This API is not executed when
     * > [AbilityStage.onPrepareTerminationAsync]{@link AbilityStage.onPrepareTerminationAsync} is implemented.
     *
     * @permission ohos.permission.PREPARE_APP_TERMINATE
     * @returns { AbilityConstant.PrepareTermination } The user's choice.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 15
     */
    onPrepareTermination(): AbilityConstant.PrepareTermination;
    /**
     * Called when the application is closed by the user, allowing the user to choose between immediate termination or
     * cancellation. This API uses a promise to return the result.
     *
     * > **NOTE**
     * >
     * > - The API is called only when the application exits under normal circumstances (for example, when the application
     * > is closed through the doc bar or tray, or when the application shuts down along with the device). It will not be
     * > called if the application is terminated forcibly.
     * >
     * > - If an asynchronous callback crashes, it will be handled as a timeout. If the application does not respond
     * > within 10 seconds, it will be terminated forcibly.
     *
     * @permission ohos.permission.PREPARE_APP_TERMINATE
     * @returns { Promise<AbilityConstant.PrepareTermination> } Promise used to return the user's choice.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 15
     */
    onPrepareTerminationAsync(): Promise<AbilityConstant.PrepareTermination>;
    /**
     * Called when the process is launched from HyperSnap.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 24
     */
    onLaunchFromHyperSnap(): void;
    /**
     * Called when the ability stage is about to create the first ability.
     * If both this method and {@link onAboutToCreateAbilityAsync} are overridden,
     * only {@link onAboutToCreateAbilityAsync} takes effect.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 24
     */
    onAboutToCreateAbility(): void;
    /**
     * Called when the ability stage is about to create the first ability. This API uses a promise to return the result.
     * Subsequent lifecycle callbacks will be suspended until the returned Promise is resolved.
     * If both {@link onAboutToCreateAbility} and this method are overridden, only this method takes effect.
     *
     * @returns { Promise<void> } Promise that returns no value.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    onAboutToCreateAbilityAsync(): Promise<void>;
}
export default AbilityStage;

```
