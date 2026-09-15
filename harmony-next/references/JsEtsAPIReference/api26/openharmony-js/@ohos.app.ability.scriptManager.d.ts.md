# @ohos.app.ability.scriptManager.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2026 Huawei Device Co., Ltd.
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
import Context from './application/Context';
/**
 * Namespace for managing and organizing script information.
 *
 * @namespace scriptManager
 * @syscap SystemCapability.Ability.AgentRuntime.Core
 * @stagemodelonly
 * @atomicservice
 * @since 26.0.0
 */
declare namespace scriptManager {
    /**
     * arkTS script info.
     *
     * @syscap SystemCapability.Ability.AgentRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    interface ArkTSScriptInfo {
        /**
         * Request code for identifying the current operation
         *
         * @syscap SystemCapability.Ability.AgentRuntime.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        readonly requestCode: string;
        /**
         * The context of the bound ability.
         *
         * @syscap SystemCapability.Ability.AgentRuntime.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        readonly context: Context;
    }
    /**
     * Result of arkTS script execution.
     *
     * @syscap SystemCapability.Ability.AgentRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    interface ExecuteResult {
        /**
         * Indicates result code.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Ability.AgentRuntime.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        code: number;
        /**
         * Indicates execute result.
         *
         * @syscap SystemCapability.Ability.AgentRuntime.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        result?: Record<string, Object>;
        /**
         * Indicates the URIs will be authorized to the caller.
         *
         * @type { ?Array<string> }
         * @syscap SystemCapability.Ability.AgentRuntime.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        uris?: Array<string>;
        /**
         * Indicates the URIs read and write permissions which consistent with {@link Want#flags},
         * flags must be one of {@link wantConstant#Flags#FLAG_AUTH_READ_URI_PERMISSION},
         * {@link wantConstant#Flags#FLAG_AUTH_WRITE_URI_PERMISSION},
         * {@link wantConstant#Flags#FLAG_AUTH_READ_URI_PERMISSION}|
         * {@link wantConstant#Flags#FLAG_AUTH_WRITE_URI_PERMISSION}.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Ability.AgentRuntime.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        flags?: number;
    }
    /**
     * complete arkTS script for in-app skills.
     *
     * @param { Context } context - Ability context, Used for temporary file authorization.
     * @param { string } requestCode - Identifying the current operation. It is from ArkTSScriptInfo.requestCode.
     * @param { ExecuteResult } result - The result of arkTS script execution.
     * @returns { Promise<void> } - The promise returned by the function.
     * @throws { BusinessError } 16000020 - The context is not ability context.
     * @throws { BusinessError } 16000003 - The specified ID does not exist.
     * @throws { BusinessError } 16000050 - Internal error. Possible causes: 1. Connect to system service failed;
     *     2.Send restart message to system service failed;
     *     3.System service failed to communicate with dependency module.
     * @syscap SystemCapability.Ability.AgentRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    function completeArkTSScriptInApp(context: Context, requestCode: string, result: ExecuteResult): Promise<void>;
}
export default scriptManager;

```
