# @ohos.app.ability.autoFillManager.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2023-2026 Huawei Device Co., Ltd.
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
import type { UIContext } from './@ohos.arkui.UIContext';
import type * as _ViewData from './application/ViewData';
import type * as _PageNodeInfo from './application/PageNodeInfo';
import { AutoFillType } from './application/AutoFillType';
import type * as _AutoFillRequest from './application/AutoFillRequest';
import type * as _AutoFillRect from './application/AutoFillRect';
import { AutoFillTriggerType } from './application/AutoFillTriggerType';
import { FillFailureResult as _FillFailureResult } from './application/AutoFillRequest';
/**
 * The autoFillManager module provides APIs for saving accounts and passwords.
 *
 * Unlike the system's auto-save feature that triggers during page transitions, this feature requires manual activation
 * by the user. For example, the user must input their account and password on a website and click the **Save** button
 * to initiate the saving process.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
 * @stagemodelonly
 * @atomicservice [since 12]
 * @since 11
 */
declare namespace autoFillManager {
    /**
     * Called when auto fill request is successfully handled.
     *
     * @param { ViewData } viewData - Indicates the ui context where the filling operation will be performed.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    type OnFillSuccessFn = (viewData: ViewData) => void;
    /**
     * Called when auto fill request is failed to be handled.
     *
     * @param { FillFailureResult } result - Indicates the ui context where the filling operation will be performed.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    type OnFillFailureFn = (result: FillFailureResult) => void;
    /**
     * Implements callbacks triggered when auto-save is complete.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @atomicservice [since 12]
     * @since 11
     */
    export interface AutoSaveCallback {
        /**
         * Called when auto save request is successfully handled.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
         * @stagemodelonly
         * @atomicservice [since 12]
         * @since 11
         */
        onSuccess(): void;
        /**
         * Called when auto save request is failed to be handled.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
         * @stagemodelonly
         * @atomicservice [since 12]
         * @since 11
         */
        onFailure(): void;
    }
    /**
     * Auto fill callback.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    export interface AutoFillCallback {
        /**
         * Called when auto fill request is successfully handled.
         * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        onSuccess: OnFillSuccessFn;
        /**
         * Called when auto fill request is failed to be handled.
         * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        onFailure: OnFillFailureFn;
    }
    /**
     * Requests to automatically save the widget data. This API uses an asynchronous callback to return the result.
     * If the current widget does not support widget switching, you can call this API to save historical widget input
     * data. The callback is triggered when the auto-save request is complete.
     *
     * @param { UIContext } context - UI context in which the auto-save operation will be performed.
     * @param { AutoSaveCallback } [callback] - Implements callbacks triggered when auto-save is complete.
     * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Get instance id failed;
     *     <br>2. Parse instance id failed; 3. The second parameter is not of type callback.
     * @throws { BusinessError } 16000050 - Internal error.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @atomicservice [since 12]
     * @since 11
     */
    export function requestAutoSave(context: UIContext, callback?: AutoSaveCallback): void;
    /**
     * Trigger an auto save request.
     *
     * @param { UIContext } context - Indicates the ui context where the save operation will be performed.
     * @param { SaveRequest } request - Indicates the struct of automatic save request.
     * @param { AutoSaveCallback } [callback] - Indicates the callback that used to receive the result.
     * @throws { BusinessError } 16000050 - Internal error.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    export function requestAutoSave(context: UIContext, request: SaveRequest, callback?: AutoSaveCallback): void;
    /**
     * Trigger an auto fill request.
     *
     * @param { UIContext } context - Indicates the ui context where the filling operation will be performed.
     * @param { FillRequest } request - Indicates the struct of automatic filling request.
     * @param { AutoFillCallback } [callback] - Indicates the callback that used to receive the result.
     * @throws { BusinessError } 16000050 - Internal error.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    export function requestAutoFill(context: UIContext, request: FillRequest, callback?: AutoFillCallback): void;
    /**
     * Defines the view data used for auto-fill.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    export type ViewData = _ViewData.default;
    /**
     * Defines the page node information used for auto-fill.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    export type PageNodeInfo = _PageNodeInfo.default;
    /**
       * The enum of auto fill type.
       *
       * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
       * @stagemodelonly
       * @atomicservice
       * @since 26.0.0
       */
    export { AutoFillType };
    /**
     * Defines the information about an auto-fill request.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    export type FillRequest = _AutoFillRequest.FillRequest;
    /**
     * Defines the information about an auto-save request.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    export type SaveRequest = _AutoFillRequest.SaveRequest;
    /**
     * The interface of filling failure result.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    export type FillFailureResult = _FillFailureResult;
    /**
     * Defines the rectangle used for auto-fill.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    export type AutoFillRect = _AutoFillRect.default;
    /**
     * The enum of auto fill trigget type.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    export { AutoFillTriggerType };
}
export default autoFillManager;

```
