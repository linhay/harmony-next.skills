# @ohos.app.appstartup.startupManager.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2024 Huawei Device Co., Ltd.
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
import StartupConfig from './@ohos.app.appstartup.StartupConfig';
import common from './@ohos.app.ability.common';
/**
 * The module provides the capability to manage startup tasks in
 * [AppStartup](docroot://application-models/app-startup.md). The APIs of this module can be called only on the main
 * thread.
 *
 * > **NOTE**
 * >
 * > This module supports .so file preloading since API version 18.
 *
 * @syscap SystemCapability.Ability.AppStartup
 * @stagemodelonly
 * @since 12
 */
declare namespace startupManager {
    /**
     * Runs startup tasks or loads .so files.
     *
     * > **NOTE**
     * >
     * > This API cannot be used to run startup tasks defined in a feature-type HAP. To run those tasks, use
     * > [startupManager.run]{@link startupManager.run(startupTasks: Array<string>, context: common.AbilityStageContext, config: StartupConfig)}
     * > .
     *
     * @param { Array<string> } startupTasks - Array of [StartupTask]{@link @ohos.app.appstartup.StartupTask:StartupTask}
     *     names or names of .so files to be preloaded.
     * @param { StartupConfig } [config] - Configuration for the timeout duration and listener of startup tasks in
     *     AppStartup.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 16000050 - Internal error.
     * @throws { BusinessError } 28800001 - Startup task or its dependency not found.
     * @throws { BusinessError } 28800002 - The startup tasks have circular dependencies.
     * @throws { BusinessError } 28800003 - An error occurred while running the startup tasks.
     * @throws { BusinessError } 28800004 - Running startup tasks timeout.
     * @syscap SystemCapability.Ability.AppStartup
     * @stagemodelonly
     * @since 12
     */
    function run(startupTasks: Array<string>, config?: StartupConfig): Promise<void>;
    /**
     * Runs startup tasks or loads .so files. You can specify
     * [AbilityStageContext]{@link ./application/AbilityStageContext:AbilityStageContext} for loading startup tasks. This
     * API uses a promise to return the result.
     *
     * @param { Array<string> } startupTasks - Array of [StartupTask]{@link @ohos.app.appstartup.StartupTask:StartupTask}
     *     names or names of .so files to be preloaded.
     * @param { common.AbilityStageContext } context - AbilityStage context that executes the
     *     [StartupTask]{@link @ohos.app.appstartup.StartupTask:StartupTask}. It is passed as an input parameter to
     *     [init]{@link @ohos.app.appstartup.StartupTask:StartupTask#init(context: AbilityStageContext)} of the task.
     * @param { StartupConfig } config - Configuration for the timeout duration and listener of startup tasks in
     *     AppStartup.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 16000050 - Internal error.
     * @throws { BusinessError } 28800001 - Startup task or its dependency not found.
     * @throws { BusinessError } 28800002 - The startup tasks have circular dependencies.
     * @throws { BusinessError } 28800003 - An error occurred while running the startup tasks.
     * @throws { BusinessError } 28800004 - Running startup tasks timeout.
     * @syscap SystemCapability.Ability.AppStartup
     * @stagemodelonly
     * @since 20
     */
    function run(startupTasks: Array<string>, context: common.AbilityStageContext, config: StartupConfig): Promise<void>;
    /**
     * Removes all startup task results.
     * If there are preloading tasks for .so files, the corresponding .so files is set to the unloaded state. However, .so
     * files that have already been loaded in the cache will not be removed.
     *
     * @syscap SystemCapability.Ability.AppStartup
     * @stagemodelonly
     * @since 12
     */
    function removeAllStartupTaskResults(): void;
    /**
     * Obtains the execution result of a startup task or .so file preloading task.
     *
     * @param { string } startupTask - Name of the [StartupTask]{@link @ohos.app.appstartup.StartupTask:StartupTask} or
     *     name of the .so file to be preloaded.
     * @returns { Object } Execution result of
     *     [init]{@link @ohos.app.appstartup.StartupTask:StartupTask#init(context: AbilityStageContext)} of the startup
     *     task if a startup task name is passed.
     *     <br>undefined if a .so file name is passed.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types.
     * @syscap SystemCapability.Ability.AppStartup
     * @stagemodelonly
     * @since 12
     */
    function getStartupTaskResult(startupTask: string): Object;
    /**
     * Checks whether a startup task or .so file preloading task is initialized.
     *
     * @param { string } startupTask - Name of the [StartupTask]{@link @ohos.app.appstartup.StartupTask:StartupTask} or
     *     name of the .so file to be preloaded.
     * @returns { boolean } Check result for whether the task is initialized. **true** if initialized, **false**
     *     otherwise.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types.
     * @syscap SystemCapability.Ability.AppStartup
     * @stagemodelonly
     * @since 12
     */
    function isStartupTaskInitialized(startupTask: string): boolean;
    /**
     * Removes the initialization result of a startup task or .so file preloading task.
     *
     * - If a startup task name is passed, the initialization result of that startup task is removed.
     * - If a .so file is passed, the .so file is set to the unloaded state, but the loaded .so file in the cache is not
     * removed.
     *
     * @param { string } startupTask - Name of the [StartupTask]{@link @ohos.app.appstartup.StartupTask:StartupTask} or
     *     name of the .so file to be preloaded.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types.
     * @syscap SystemCapability.Ability.AppStartup
     * @stagemodelonly
     * @since 12
     */
    function removeStartupTaskResult(startupTask: string): void;
}
export default startupManager;

```
