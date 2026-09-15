# @ohos.app.ability.dialogRequest.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022-2023 Huawei Device Co., Ltd.
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
import Want from './@ohos.app.ability.Want';
/**
 * The dialogRequest module provides APIs related to modal dialog box processing, including obtaining the request
 * information (used to bind a modal dialog box) and request callback (used to set the request result).
 *
 * A modal dialog box is a system-level dialog box that blocks interactions such as mouse clicks, keyboard input, and
 * touch events on the underlying page. The page can only be interacted with after the modal dialog box is closed.
 *
 * > **NOTE**
 * >
 * > - The APIs provided by this module are used in ServiceExtensionAbilities. For a ServiceExtensionAbility that
 * > implements modal dialog boxes, you can use the APIs to obtain the request information and request callback and
 * > return the request result.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @since 9
 */
declare namespace dialogRequest {
    /**
     * Defines the location attributes of a modal dialog box.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 10
     */
    export interface WindowRect {
        /**
         * X-coordinate of the upper left corner of the dialog box.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @stagemodelonly
         * @since 10
         */
        left: number;
        /**
         * Y-coordinate of the upper left corner of the dialog box.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @stagemodelonly
         * @since 10
         */
        top: number;
        /**
         * Width of the dialog box, in px.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @stagemodelonly
         * @since 10
         */
        width: number;
        /**
         * Height of the dialog box, in px.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @stagemodelonly
         * @since 10
         */
        height: number;
    }
    /**
     * Defines the request information, which is used as an input parameter for binding the modal dialog box.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @since 9
     */
    export interface RequestInfo {
        /**
         * Location attributes of a modal dialog box.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @stagemodelonly
         * @since 10
         */
        windowRect?: WindowRect;
    }
    /**
     * Enumerates the result codes of the request for the modal dialog box.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @since 9
     */
    export enum ResultCode {
        /**
         * The request succeeds.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @since 9
         */
        RESULT_OK = 0,
        /**
         * The request fails.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @since 9
         */
        RESULT_CANCEL = 1
    }
    /**
     * Defines the result of the request for the modal dialog box. It contains **ResultCode** and **ResultWant**.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 9
     */
    export interface RequestResult {
        /**
         * Result code of the request.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @stagemodelonly
         * @since 9
         */
        result: ResultCode;
        /**
         * Want information, such as the ability name and bundle name.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @stagemodelonly
         * @since 10
         */
        want?: Want;
    }
    /**
     * Provides a callback for setting the modal dialog box request result.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 9
     */
    export interface RequestCallback {
        /**
         * Sets the result of the request for the modal dialog box.
         *
         * @param { RequestResult } result - Request result to set.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
         * @stagemodelonly
         * @since 9
         */
        setRequestResult(result: RequestResult): void;
    }
    /**
     * > **NOTE**
     * >
     * > This API can be used by a ServiceExtensionAbility. If the ServiceExtensionAbility implements modal dialog boxes,
     * > the request information can be obtained from Want. If this API is used in other scenarios, no return value is
     * > obtained.
     *
     * Obtains the request information from Want.
     *
     * @param { Want } want - Want passed in the request for a modal dialog box.
     * @returns { RequestInfo } RequestInfo object obtained, which is used to bind a modal dialog box.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @since 9
     */
    function getRequestInfo(want: Want): RequestInfo;
    /**
     * Obtains the request callback from Want.
     *
     * > **NOTE**
     * >
     * > This API can be used by a ServiceExtensionAbility. If the ServiceExtensionAbility implements modal dialog boxes,
     * > the request callback can be obtained from Want. If this API is used in other scenarios, no return value is
     * > obtained.
     *
     * @param { Want } want - Want passed in the request for a modal dialog box.
     * @returns { RequestCallback } RequestCallback object obtained, which is used to set the return result.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @since 9
     */
    function getRequestCallback(want: Want): RequestCallback;
}
export default dialogRequest;

```
