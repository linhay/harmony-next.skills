# @ohos.app.ability.childProcessManager.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2023-2024 Huawei Device Co., Ltd.
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
import type { AsyncCallback } from './@ohos.base';
import type { ChildProcessArgs } from './@ohos.app.ability.ChildProcessArgs';
import type { ChildProcessOptions } from './@ohos.app.ability.ChildProcessOptions';
/**
 * The childProcessManager module provides the child process management capability. Currently, it provides APIs to
 * create and start a child process
 * The created child process will exit when the parent process exits and cannot run independently.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @since 11
 */
declare namespace childProcessManager {
    /**
     * Enumerates the child process start modes.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 11
     */
    export const enum StartMode {
        /**
         * The child process is forked from the application process. The child process started in this mode inherits the
         * resources of the parent process and cannot use Binder IPC to communicate with other processes. Otherwise, the
         * child process will crash.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @stagemodelonly
         * @since 11
         */
        SELF_FORK = 0,
        /**
         * The child process is forked from AppSpawn. The child process started in this mode does not inherit the resources
         * of the parent process and can use Binder IPC to communicate with other processes.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @stagemodelonly
         * @since 11
         */
        APP_SPAWN_FORK = 1
    }
    /**
     * Starts an [ArkTS child process](docroot://application-models/ability-terminology.md#arkts-child-process). This API
     * uses a promise to return the result.
     * This API can be properly called on PCs/2-in-1 devices and tablets. If it is called on other devices, error code 160
     * 00061 is returned.
     *
     * > **NOTE**
     * >
     * > If the child process is created successfully, its PID is returned, and its
     * > [ChildProcess.onStart]{@link @ohos.app.ability.ChildProcess:ChildProcess#onStart} function is executed. Once the
     * > function is done, the child process is automatically destroyed.
     * >
     * > The child process started by calling this API does not support asynchronous ArkTS API calls. It supports only
     * > synchronous ArkTS API calls.
     *
     * @param { string } srcEntry - Path of the source file of the child process relative to the root directory **src/main**.
     *     The source file can be stored only in the module of the entry type. For example, if the source file of a child
     *     process is **src/main/ets/process/DemoProcess.ets** in the entry module, then **srcEntry** is **./ets/process/
     *     DemoProcess.ets**.<br>In addition, ensure that the source file of the child process is referenced by other files to
     *     prevent it from being optimized by the build tool. (For details, see the sample code below.)
     * @param { StartMode } startMode - Start mode of the child process.
     * @returns { Promise<number> } Promise used to return the PID of the child process.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
     * @throws { BusinessError } 16000050 - Internal error.
     * @throws { BusinessError } 16000061 - Operation not supported.
     * @throws { BusinessError } 16000062 - The number of child processes exceeds the upper limit.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 11
     */
    function startChildProcess(srcEntry: string, startMode: StartMode): Promise<number>;
    /**
     * Starts an [ArkTS child process](docroot://application-models/ability-terminology.md#arkts-child-process). This API
     * uses an asynchronous callback to return the result.
     * This API can be properly called on PCs/2-in-1 devices and tablets. If it is called on other devices, error code 160
     * 00061 is returned.
     *
     * > **NOTE**
     * >
     * > If the child process is created successfully, its PID is returned, and its
     * > [ChildProcess.onStart]{@link @ohos.app.ability.ChildProcess:ChildProcess#onStart} function is executed. Once the
     * > function is done, the child process is automatically destroyed.
     * >
     * > The child process started by calling this API does not support asynchronous ArkTS API calls. It supports only
     * > synchronous ArkTS API calls.
     *
     * @param { string } srcEntry - Path of the source file of the child process relative to the root directory **src/main**.
     *     The source file can be stored only in the module of the entry type. For example, if the source file of a child
     *     process is **src/main/ets/process/DemoProcess.ets** in the entry module, then **srcEntry** is **./ets/process/
     *     DemoProcess.ets**.<br>In addition, ensure that the source file of the child process is referenced by other files to
     *     prevent it from being optimized by the build tool. (For details, see the sample code below.)
     * @param { StartMode } startMode - Start mode of the child process.
     * @param { AsyncCallback<number> } callback - Callback used to return the result. If the subprocess is started, **err** is
     *     **undefined** and **data** is the PID of the child process. Otherwise, **data** is an error object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
     * @throws { BusinessError } 16000050 - Internal error.
     * @throws { BusinessError } 16000061 - Operation not supported.
     * @throws { BusinessError } 16000062 - The number of child processes exceeds the upper limit.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 11
     */
    function startChildProcess(srcEntry: string, startMode: StartMode, callback: AsyncCallback<number>): void;
    /**
     * Starts an [ArkTS child process](docroot://application-models/ability-terminology.md#arkts-child-process). This API
     * uses a promise to return the result.
     * This API can be properly called on PCs/2-in-1 devices and tablets. If it is called on other devices, error code 801
     *  is returned.
     *
     * > **NOTE**
     * >
     * > The child process started by calling this API does not inherit the resources of the parent process. If the child
     * > process is created successfully, its PID is returned, and its
     * > [ChildProcess.onStart]{@link @ohos.app.ability.ChildProcess:ChildProcess#onStart} function is executed. After the
     * >  function is done, the child process is not automatically destroyed. Instead, it must be destroyed by calling
     * > [process.abort]{@link @ohos.process:process.abort}. After the process that calls this API is destroyed, the
     * > created child process is also destroyed.
     *
     * @param { string } srcEntry - Path of the source file of the child process relative to the root directory **src/main**.
     *     The source file cannot be stored in the module of the HAR type. The value consists of a module name, a slash (/),
     *     and a file path. For example, if the child process file is **src/main/ets/process/DemoProcess.ets** in module1, then
     *     **srcEntry** is **module1/ets/process/DemoProcess.ets**.<br>In addition, ensure that the source file of the child
     *     process is referenced by other files to prevent it from being optimized by the build tool. (For details, see the
     *     sample code below.)
     * @param { ChildProcessArgs } args - Parameters transferred to the child process.
     * @param { ChildProcessOptions } [options] - Startup configuration of the child process.
     * @returns { Promise<number> } Promise used to return the PID of the child process.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 16000050 - Internal error.
     * @throws { BusinessError } 16000061 - Operation not supported.
     * @throws { BusinessError } 16000062 - The number of child processes exceeds the upper limit. [since 13]
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 12
     */
    function startArkChildProcess(srcEntry: string, args: ChildProcessArgs, options?: ChildProcessOptions): Promise<number>;
    /**
     * Starts a [native child process](docroot://application-models/ability-terminology.md#native-child-process). This API
     *  uses a promise to return the result.
     * This API can be properly called on PCs/2-in-1 devices and tablets. If it is called on other devices, error code 801
     *  is returned.
     *
     * > **NOTE**
     * >
     * > The child process started by calling this API does not inherit the resources of the parent process. After the
     * > child process is created, its PID is returned, the dynamic link library file specified in the parameters is
     * > loaded, and the entry function of the child process is executed. Once the entry function is done, the child
     * > process is automatically destroyed. After the process that calls this API is destroyed, the created child process
     * >  is also destroyed.
     *
     * @param { string } entryPoint - The symbol and entry function of the dynamic link library called in the child process are
     *     separated by a colon (:), for example, **libentry.so:Main**.
     * @param { ChildProcessArgs } args - Parameters transferred to the child process.
     * @param { ChildProcessOptions } [options] - Startup configuration of the child process.
     * @returns { Promise<number> } Promise used to return the PID of the child process.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call the API due to limited device capabilities.
     * @throws { BusinessError } 16000050 - Internal error.
     * @throws { BusinessError } 16000061 - Operation not supported.
     * @throws { BusinessError } 16000062 - The number of child processes exceeds the upper limit.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 13
     */
    function startNativeChildProcess(entryPoint: string, args: ChildProcessArgs, options?: ChildProcessOptions): Promise<number>;
    /**
     * Checks whether the caller is allowed to create ark child processes on this device.
     * Some devices may not support creating ark child processes, so it is recommended to use this interface to
     * verify support beforehand.
     *
     * @returns { boolean }
     *     - `true`: The caller is allowed to create ark child processes.
     *     - `false`: The caller is not allowed to create ark child processes.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    function isArkChildProcessSupported(): boolean;
    /**
     * Checks whether the caller is allowed to create native child processes on this device.
     * Some devices may not support creating native child processes, so it is recommended to use this interface to
     * verify support beforehand.
     *
     * @returns { boolean }
     *     - `true`: The caller is allowed to create native child processes.
     *     - `false`: The caller is not allowed to create native child processes.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    function isNativeChildProcessSupported(): boolean;
}
export default childProcessManager;

```
