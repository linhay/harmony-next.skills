# @ohos.app.ability.ChildProcessOptions.d.ts

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
 * The module describes the startup configuration of a child process. When starting a child process through
 * [childProcessManager]{@link @ohos.app.ability.childProcessManager:childProcessManager}, you can configure the startup
 * configuration of the child process through **ChildProcessOptions**.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @stagemodelonly
 * @since 12
 */
export interface ChildProcessOptions {
    /**
     * Controls the sandbox isolation level and network access permissions of the child process. **true** if the child
     * process runs in an independent sandbox environment and cannot access the network; **false** if the child process
     * shares the sandbox and network environment with the main process. The default value is **false**.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 12
     */
    isolationMode?: boolean;
    /**
     * Whether the child process uses an independent UID. **true** if the child process uses an independent UID; **false**
     * if the child process and the main process share the same UID. The default value is **false**. This parameter is
     * valid only when **isolationMode** is set to **true**.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 21
     */
    isolationUid?: boolean;
}

```
