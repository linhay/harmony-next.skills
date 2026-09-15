# @ohos.app.ability.application.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2024 Huawei Device Co., Ltd.
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
import ApplicationContext from './application/ApplicationContext';
import Context from './application/Context';
/**
 * You can use this module to create a [Context](docroot://application-models/application-context-stage.md).
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @stagemodelonly
 * @atomicservice
 * @since 12
 */
declare namespace application {
    /**
     * Enumerates the preloading types of the current application process.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 22
     */
    export enum AppPreloadType {
        /**
         * No preloading has taken place, or the preloaded data has been cleared.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @stagemodelonly
         * @since 22
         */
        UNSPECIFIED = 0,
        /**
         * Preloads the process up to the point of process creation completion.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @stagemodelonly
         * @since 22
         */
        TYPE_CREATE_PROCESS = 1,
        /**
         * Preloads the process up to the point of [AbilityStage]{@link @ohos.app.ability.AbilityStage:AbilityStage}
         * creation completion.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @stagemodelonly
         * @since 22
         */
        TYPE_CREATE_ABILITY_STAGE = 2,
        /**
         * Preloads the process up to the point of [WindowStage]{@link @ohos.window} creation completion.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @stagemodelonly
         * @since 22
         */
        TYPE_CREATE_WINDOW_STAGE = 3,
        /**
         * Preloads the process up to the point of [onBackground]{@link @ohos.app.ability.UIAbility:UIAbility#onBackground}
         * execution completion.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @stagemodelonly
         * @since 23
         */
        TYPE_CREATE_BACKGROUND_ABILITY = 4
    }
    /**
     * Creates the context for a module. The
     * [resourceManager.Configuration]{@link @ohos.resourceManager:resourceManager.Configuration} in the created module
     * context inherits from the input context, making it convenient for you to access
     * [application resources across HAP/HSP packages](docroot://quick-start/resource-categories-and-access.md#cross-haphsp-resources)
     * . This API uses a promise to return the result.
     *
     * > **NOTE**
     * >
     * > Creating a module context involves resource querying and initialization, which can be time-consuming. In
     * > scenarios where application fluidity is critical, avoid frequently or repeatedly calling the
     * > **createModuleContext** API to create multiple context instances, as this may negatively impact user experience.
     *
     * @param { Context } context - Application context.
     * @param { string } moduleName - Module name.
     * @returns { Promise<Context> } Promise used to return the context created.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Mandatory parameters are left unspecified;
     *     2.Incorrect parameter types.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 12
     */
    export function createModuleContext(context: Context, moduleName: string): Promise<Context>;
    /**
     * Creates the context of a plugin under the current application based on the context, plugin bundle name, and plugin
     * module name, so as to obtain the basic information about the plugin. This API uses a promise to return the result.
     *
     * @param { Context } context - Application context.
     * @param { string } pluginBundleName - Bundle name of the plugin.
     * @param { string } pluginModuleName - Module name of the plugin.
     * @returns { Promise<Context> } Promise used to return the context created.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 19
     */
    export function createPluginModuleContext(context: Context, pluginBundleName: string, pluginModuleName: string): Promise<Context>;
    /**
     * Obtains the application context. This API provides context access independent of the base class **Context**.
     * Repeated calls to this API generate a new ApplicationContext object.
     *
     * @returns { ApplicationContext } Application context.
     * @throws { BusinessError } 16000050 - Internal error.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 14
     */
    export function getApplicationContext(): ApplicationContext;
    /**
     * Obtains the application context. This API provides context access independent of the base class **Context**.
     * Repeated calls to this API obtain the same ApplicationContext instance.
     *
     * @returns { ApplicationContext } Application context.
     * @throws { BusinessError } 16000050 - Internal error. Possible causes: Memory operation error.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 23
     */
    export function getApplicationContextInstance(): ApplicationContext;
    /**
     * Adds the current process into the
     * [candidate master process](docroot://application-models/ability-terminology.md#candidate-master-process) list. This
     *  API uses a promise to return the result.
     * When the [master process](docroot://application-models/ability-terminology.md#master-process) is destroyed and a
     * UIAbility or UIExtensionAbility with **isolationProcess** set to **true** is restarted, the system takes
     * corresponding actions based on whether there is a candidate master process.
     *
     * - If a candidate master process exists, the system sets the process at the head of the candidate master process
     * list as the new master process and triggers the
     * [onNewProcessRequest]{@link @ohos.app.ability.AbilityStage:AbilityStage#onNewProcessRequest} callback.
     * - If no candidate master process exists, the system performs the following operations based on the component type:
     *   - For a UIAbility, the system creates an empty process as the master process.
     *   - For a UIExtensionAbility, the system first tries to reuse an existing UIExtensionAbility process as the new
     * master process. If no available process exists, it creates an empty process as the master process.
     * This API can be properly called on PCs/2-in-1 devices and tablets. If it is called on other devices, error code 801
     *  is returned.
     *
     * > **NOTE**
     * >
     * > If the current process is already the
     * > [master process](docroot://application-models/ability-terminology.md#master-process), calling this API has no
     * > effect and does not generate an error code.
     * >
     * > A process can be set as a candidate master process only if it is currently running a component with
     * > **isolationProcess** set to **true** or has previously as the main process.
     * >
     * >
     * > The **isolationProcess** field can be set to **true** in the
     * > [module.json5](docroot://quick-start/module-configuration-file.md) file, but only for the UIExtensionAbility of
     * > the sys/commonUI type.
     *
     * <!--DelEnd-->
     *
     * @param { boolean } insertToHead - Whether to add the current process to the head of the candidate master process list.
     *     **true** to add the current process to the head of the list, **false** to add the current process to the tail of the
     *     list.
     * @returns { Promise<void> } Promise that returns no result.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 16000115 - The current process cannot be set as a candidate master process.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 20
     */
    export function promoteCurrentToCandidateMasterProcess(insertToHead: boolean): Promise<void>;
    /**
     * Removes the current process from the candidate master process list. This API uses a promise to return the result.
     * This API can be properly called on PCs/2-in-1 devices and tablets. If it is called on other devices, error code 801
     *  is returned.
     * **System capability**: SystemCapability.Ability.AbilityRuntime.Core
     *
     * @returns { Promise<void> } Promise that returns no result.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 16000116 - The current process is already a master process and does not support cancellation.
     * @throws { BusinessError } 16000117 - The current process is not a candidate master process and does not support
     *     cancellation.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 20
     */
    export function demoteCurrentFromCandidateMasterProcess(): Promise<void>;
    /**
     * Relinquishes the [master-process](docroot://application-models/ability-terminology.md#master-process) role from the
     *  current process. This API uses a promise to return the result.
     * This API can be properly called only on 2-in-1 devices and tablets. If it is called on other device types, error
     * code 801 is returned.
     *
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 16000118 - Not a master process.
     * @throws { BusinessError } 16000119 - Cannot exit because there is an unfinished request.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 21
     */
    export function exitMasterProcessRole(): Promise<void>;
    /**
     * Obtains the preloading type of the current application process.
     *
     * > **NOTE**
     * >
     * > - This API can return the actual preloading type only if it is called before the first execution of
     * > [AbilityStage.onCreate]{@link @ohos.app.ability.AbilityStage:AbilityStage#onCreate}.
     * >
     * > - Once the AbilityStage creation finishes, the preloaded data of the application is cleared. Any subsequent calls
     * >  will return **UNSPECIFIED** instead of the original preloading type.
     *
     * @returns { AppPreloadType } Obtains the preloading type of the current application process.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 22
     */
    export function getAppPreloadType(): AppPreloadType;
}
export default application;

```
