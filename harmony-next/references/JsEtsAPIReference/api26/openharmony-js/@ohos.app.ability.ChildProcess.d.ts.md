# @ohos.app.ability.ChildProcess.d.ts

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
import type { ChildProcessArgs } from './@ohos.app.ability.ChildProcessArgs';
/**
 * ChildProcess is the base class for you to customize child processes. When starting a child process through
 * [childProcessManager]{@link @ohos.app.ability.childProcessManager:childProcessManager}, you must inherit this class
 * and override the entrypoint method.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @stagemodelonly
 * @since 11
 */
declare class ChildProcess {
    /**
     * Entrypoint method of the child process. This callback is triggered when the child process is started through
     * [childProcessManager]{@link @ohos.app.ability.childProcessManager:childProcessManager}.
     *
     * @param { ChildProcessArgs } [args] - Parameters transferred to the child process.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 11
     */
    onStart(args?: ChildProcessArgs): void;
}
export default ChildProcess;

```
