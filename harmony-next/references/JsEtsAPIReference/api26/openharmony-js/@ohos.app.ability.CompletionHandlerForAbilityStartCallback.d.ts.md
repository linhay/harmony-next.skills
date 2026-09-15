# @ohos.app.ability.CompletionHandlerForAbilityStartCallback.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2025 Huawei Device Co., Ltd.
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
 * **CompletionHandlerForAbilityStartCallback** is an optional parameter of
 * [AbilityStartCallback]{@link ./application/AbilityStartCallback}. It provides callback results for launching ability
 * components of specific types through the vertical panel.
 *
 * @file
 * @kit AbilityKit
 */
/**
 * Defines the callback for successful ability launches.
 *
 * @param { string } name - Name of the launched ability or system operation.
 *
 *     The ability component name is in the format of '[bundleName]#[moduleName]#[abilityName]'.
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @stagemodelonly
 * @atomicservice
 * @since 21
 */
export type OnRequestSuccessFn = (name: string) => void;
/**
 * Defines the callback for failed ability launches.
 *
 * @param { string } name - Name of the launched ability or system operation.
 *     The ability component name is in the format of '[bundleName]#[moduleName]#[abilityName]'. If the user cancels the
 *     launch automatically, this parameter is empty.
 * @param { AbilityStartFailureCode } failureCode - Error code of the failure cause.
 * @param { string } failureMessage - Description of the failure cause.
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @stagemodelonly
 * @atomicservice
 * @since 21
 */
export type OnRequestFailureFn = (name: string, failureCode: AbilityStartFailureCode, failureMessage: string) => void;
/**
 * CompletionHandlerForAbilityStartCallback provides two callback functions, **onRequestSuccess** and
 * **onRequestFailure**, which are invoked when launching the specified ability succeeds or fails, respectively.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @stagemodelonly
 * @atomicservice
 * @since 21
 */
export class CompletionHandlerForAbilityStartCallback {
    /**
     * Callback invoked when the specified ability is successfully launched.
     *
     * This API can be used in atomic services since API version 21.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 21
     */
    onRequestSuccess?: OnRequestSuccessFn;
    /**
     * Callback invoked when launching the specified ability fails.
     *
     * This API can be used in atomic services since API version 21.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 21
     */
    onRequestFailure?: OnRequestFailureFn;
}
/**
 * Enumerates the specific error codes for ability launch failures.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @stagemodelonly
 * @atomicservice
 * @since 21
 */
export enum AbilityStartFailureCode {
    /**
     * The ability cannot be launched due to a system error (for example, a crash in starting the picker).
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 21
     */
    FAILURE_CODE_SYSTEM_MALFUNCTION = 0,
    /**
     * The user canceled the operation.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 21
     */
    FAILURE_CODE_USER_CANCEL = 1
}

```
