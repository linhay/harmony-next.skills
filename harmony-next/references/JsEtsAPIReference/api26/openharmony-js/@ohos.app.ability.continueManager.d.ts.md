# @ohos.app.ability.continueManager.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2025-2026 Huawei Device Co., Ltd.
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
import { AsyncCallback } from './@ohos.base';
import Context from './application/Context';
/**
 * The continueManager module provides capabilities for managing cross-device application migration. For example, it
 * allows you to obtain the result of quickly launching the target application during the cross-device migration
 * process.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Mission
 * @stagemodelonly
 * @since 18
 */
declare namespace continueManager {
    /**
     * Registers a callback to obtain the quick start result when an application is launched quickly. This API uses an
     * asynchronous callback to return the result.
     *
     * @param { 'prepareContinue' } type - The value is fixed at **prepareContinue**.
     * @param { Context } context - Context of the ability.
     * @param { AsyncCallback<ContinueResultInfo> } callback - Callback used to return the result. If obtaining the quick start
     *     result is successful, **err** is undefined, and **ContinueResultInfo** is the obtained quick startup result.
     *     Otherwise, **err** is an error object.
     * @throws { BusinessError } 16300501 - the system ability work abnormally.
     * @syscap SystemCapability.Ability.AbilityRuntime.Mission
     * @stagemodelonly
     * @since 18
     */
    function on(type: 'prepareContinue', context: Context, callback: AsyncCallback<ContinueResultInfo>): void;
    /**
     * Unregisters the callback used to obtain the quick start result when an application is launched quickly. This API
     * uses an asynchronous callback to return the result.
     *
     * @param { 'prepareContinue' } type - The value is fixed at **prepareContinue**.
     * @param { Context } context - Context of the ability.
     * @param { AsyncCallback<ContinueResultInfo> } callback - Callback used to return the result. If the callback is
     *     unregistered, **err** is undefined, and **ContinueResultInfo** is the callback unregistration result. Otherwise,
     *     **err** is an error object.
     * @throws { BusinessError } 16300501 - the system ability work abnormally.
     * @syscap SystemCapability.Ability.AbilityRuntime.Mission
     * @stagemodelonly
     * @since 18
     */
    function off(type: 'prepareContinue', context: Context, callback?: AsyncCallback<ContinueResultInfo>): void;
    /**
     * Describes the quick start result returned by the callback.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Mission
     * @stagemodelonly
     * @since 18
     */
    interface ContinueResultInfo {
        /**
         * Status code of the operation result.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Mission
         * @stagemodelonly
         * @since 18
         */
        resultState: ContinueStateCode;
        /**
         * Description of the operation result.
         *
         * This API can be used only in the stage model.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Mission
         * @stagemodelonly
         * @since 18
         */
        resultInfo?: string;
    }
    /**
     * Enumerates the status codes of the quick start result.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Mission
     * @stagemodelonly
     * @since 18
     */
    enum ContinueStateCode {
        /**
         * Operation succeeded.
         *
         * This API can be used only in the stage model.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Mission
         * @stagemodelonly
         * @since 18
         */
        SUCCESS = 0,
        /**
         * Operation failed.
         *
         * This API can be used only in the stage model.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Mission
         * @stagemodelonly
         * @since 18
         */
        SYSTEM_ERROR = 1
    }
}
export default continueManager;

```
