# @ohos.app.ability.ChildProcessArgs.d.ts

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
/**
 * The module describes the parameters transferred to the child process. When starting a child process through
 * [childProcessManager]{@link @ohos.app.ability.childProcessManager:childProcessManager}, you can transfer parameters
 * to the child process through **ChildProcessArgs**.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @stagemodelonly
 * @since 12
 */
export interface ChildProcessArgs {
    /**
     * Custom parameters to be transparently transmitted to the child process. The parameters can be obtained through
     * **args.entryParams** in [ChildProcess.onStart]{@link @ohos.app.ability.ChildProcess:ChildProcess.onStart}. The
     * maximum data volume supported by **entryParams** is 150 KB.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 12
     */
    entryParams?: string;
    /**
     * File Descriptor (FD) handles, which are used for communication between the main process and child process. They are
     * passed to the child process in the form of key-value pairs, where **key** is a custom string and **value** is a DF
     * handle. The FD handles can be obtained through **args.fds** in
     * [ChildProcess.onStart]{@link @ohos.app.ability.ChildProcess:ChildProcess.onStart}.
     *
     * <b>NOTE</b>
     *
     * - **fds** supports a maximum of 16 groups. In each group, **key** contains a maximum of 20 characters.
     * - The ID of a handle passed to the child process may change, but the handle always points to the same file.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 12
     */
    fds?: Record<string, number>;
}

```
