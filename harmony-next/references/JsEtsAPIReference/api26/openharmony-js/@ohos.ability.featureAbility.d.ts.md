# @ohos.ability.featureAbility.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2021-2023 Huawei Device Co., Ltd.
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
/**
 * # Constraints
 *
 * The APIs of the FeatureAbility module can be called only by PageAbilities.
 */
import { AsyncCallback } from './@ohos.base';
import Want from './@ohos.app.ability.Want';
import { StartAbilityParameter } from './ability/startAbilityParameter';
import { AbilityResult } from './ability/abilityResult';
import { AppVersionInfo as _AppVersionInfo } from './app/appVersionInfo';
import { Context as _Context } from './app/context';
import { DataAbilityHelper } from './ability/dataAbilityHelper';
import { ConnectOptions } from './ability/connectOptions';
import { ProcessInfo as _ProcessInfo } from './app/processInfo';
import window from './@ohos.window';
/**
 * The FeatureAbility module provides APIs that enable user interaction. You can use the APIs to start or terminate an
 * ability, obtain a dataAbilityHelper object, obtain the window corresponding to the current ability, and connect to or
 * disconnect from a ServiceAbility.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
 * @famodelonly
 * @since 6
 */
declare namespace featureAbility {
    /**
     * Obtains the Want corresponding to the ability to start. This API uses an asynchronous callback to return the
     * result.
     *
     * @param { AsyncCallback<Want> } callback - Callback used to return the Want.
     * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
     * @famodelonly
     * @since 6
     */
    function getWant(callback: AsyncCallback<Want>): void;
    /**
     * Obtains the Want corresponding to the ability to start. This API uses a promise to return the result.
     *
     * @returns { Promise<Want> } Promise used to return the Want.
     * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
     * @famodelonly
     * @since 6
     */
    function getWant(): Promise<Want>;
    /**
     * Starts an ability. This API uses an asynchronous callback to return the result.
     *
     * > **NOTE**
     * >
     * > For details about the startup rules for the components in the FA model, see
     * > [Component Startup Rules (FA Model)](docroot://application-models/component-startup-rules-fa.md).
     *
     * @param { StartAbilityParameter } parameter - Ability to start.
     * @param { AsyncCallback<number> } callback - Callback used to return the result. If the operation is successful,
     *     **err** is **undefined** and **data** is **0**; otherwise, **err** is a non-zero value.
     * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
     * @famodelonly
     * @since 6
     */
    function startAbility(parameter: StartAbilityParameter, callback: AsyncCallback<number>): void;
    /**
     * Starts an ability. This API uses a promise to return the result.
     *
     * > **NOTE**
     * >
     * > For details about the startup rules for the components in the FA model, see
     * > [Component Startup Rules (FA Model)](docroot://application-models/component-startup-rules-fa.md).
     *
     * @param { StartAbilityParameter } parameter - Ability to start.
     * @returns { Promise<number> } Promise used to return the result. If the operation is successful, **0** is returned;
     *     otherwise, a non-zero value is returned.
     * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
     * @famodelonly
     * @since 6
     */
    function startAbility(parameter: StartAbilityParameter): Promise<number>;
    /**
     * Obtains the application context.
     *
     * @returns { Context } Application context.
     * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
     * @famodelonly
     * @since 6
     */
    function getContext(): Context;
    /**
     * Starts an ability. This API uses an asynchronous callback to return the result. The following situations may be
     * possible for a started ability:
     *
     * - Normally, you can call
     * [terminateSelfWithResult]{@link featureAbility.terminateSelfWithResult(parameter: AbilityResult, callback: AsyncCallback<void>)}
     * to terminate the ability. The result is returned to the caller.
     * - If an exception occurs, for example, the ability is killed, an exception message, in which **resultCode** is
     * **-1**, is returned to the caller.
     * - If different applications call this API to start an ability that uses the singleton mode and then call
     * [terminateSelfWithResult]{@link featureAbility.terminateSelfWithResult(parameter: AbilityResult, callback: AsyncCallback<void>)}
     * to terminate the ability, the normal result is returned to the last caller, and an exception message, in which
     * **resultCode** is **-1**, is returned to others.
     *
     * > **NOTE**
     * >
     * > For details about the startup rules for the components in the FA model, see
     * > [Component Startup Rules (FA Model)](docroot://application-models/component-startup-rules-fa.md).
     *
     * @param { StartAbilityParameter } parameter - Ability to start.
     * @param { AsyncCallback<AbilityResult> } callback - Callback used to return the result. If the operation is
     *     successful, **err** is **undefined** and **data** is an AbilityResult object; otherwise, err is an error
     *     object.
     * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
     * @famodelonly
     * @since 7
     */
    function startAbilityForResult(parameter: StartAbilityParameter, callback: AsyncCallback<AbilityResult>): void;
    /**
     * Starts an ability. This API uses a promise to return the result. The following situations may be possible for a
     * started ability:
     *
     * - Normally, you can call
     * [terminateSelfWithResult]{@link featureAbility.terminateSelfWithResult(parameter: AbilityResult, callback: AsyncCallback<void>)}
     * to terminate the ability. The result is returned to the caller.
     * - If an exception occurs, for example, the ability is killed, an exception message, in which **resultCode** is
     * **-1**, is returned to the caller.
     * - If different applications call this API to start an ability that uses the singleton mode and then call
     * [terminateSelfWithResult]{@link featureAbility.terminateSelfWithResult(parameter: AbilityResult, callback: AsyncCallback<void>)}
     * to terminate the ability, the normal result is returned to the last caller, and an exception message, in which
     * **resultCode** is **-1**, is returned to others.
     *
     * > **NOTE**
     * >
     * > For details about the startup rules for the components in the FA model, see
     * > [Component Startup Rules (FA Model)](docroot://application-models/component-startup-rules-fa.md).
     *
     * @param { StartAbilityParameter } parameter - Ability to start.
     * @returns { Promise<AbilityResult> } Promise used to return the result.
     * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
     * @famodelonly
     * @since 7
     */
    function startAbilityForResult(parameter: StartAbilityParameter): Promise<AbilityResult>;
    /**
     * Terminates this ability. This API uses an asynchronous callback to return the result. If the ability is started by
     * calling
     * [startAbilityForResult]{@link featureAbility.startAbilityForResult(parameter: StartAbilityParameter, callback: AsyncCallback<AbilityResult>)}
     * , the result is returned to the caller when **terminateSelfWithResult** is called. Otherwise, no result is returned
     * to the caller when **terminateSelfWithResult** is called.
     *
     * @param { AbilityResult } parameter - Result returned after the ability is terminated.
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
     *     **err** is **undefined**; otherwise, **err** is an error object.
     * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
     * @famodelonly
     * @since 7
     */
    function terminateSelfWithResult(parameter: AbilityResult, callback: AsyncCallback<void>): void;
    /**
     * Terminates this ability. This API uses a promise to return the result. If the ability is started by calling
     * [startAbilityForResult]{@link featureAbility.startAbilityForResult(parameter: StartAbilityParameter, callback: AsyncCallback<AbilityResult>)}
     * , the result is returned to the caller when **terminateSelfWithResult** is called. Otherwise, no result is returned
     * to the caller when **terminateSelfWithResult** is called.
     *
     * @param { AbilityResult } parameter - Result returned after the ability is terminated.
     * @returns { Promise<void> } Promise that returns no value.
     * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
     * @famodelonly
     * @since 7
     */
    function terminateSelfWithResult(parameter: AbilityResult): Promise<void>;
    /**
     * Terminates this ability. This API uses an asynchronous callback to return the result.
     *
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
     *     **err** is **undefined**; otherwise, **err** is an error object.
     * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
     * @famodelonly
     * @since 7
     */
    function terminateSelf(callback: AsyncCallback<void>): void;
    /**
     * Terminates this ability. This API uses a promise to return the result.
     *
     * @returns { Promise<void> } Promise that returns no value.
     * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
     * @famodelonly
     * @since 7
     */
    function terminateSelf(): Promise<void>;
    /**
     * Obtains a dataAbilityHelper object.
     *
     * > **NOTE**
     * >
     * > For details about the startup rules for the components in the FA model, see
     * > [Component Startup Rules (FA Model)](docroot://application-models/component-startup-rules-fa.md).
     * >
     * > To access a DataAbility of another application, the target application must be configured with associated startup
     * > (**AssociateWakeUp** set to **true**).
     *
     * @param { string } uri - URI of the file to open.
     * @returns { DataAbilityHelper } A utility class used to help other abilities access the Data ability.
     * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
     * @famodelonly
     * @since 7
     */
    function acquireDataAbilityHelper(uri: string): DataAbilityHelper;
    /**
     * Checks whether the main window of this ability has the focus. This API uses an asynchronous callback to return the
     * result.
     *
     * @param { AsyncCallback<boolean> } callback - Callback used to return the result.<br>If the main window has the
     *     focus, **true** is returned. Otherwise, **false** is returned.
     * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
     * @famodelonly
     * @since 7
     */
    function hasWindowFocus(callback: AsyncCallback<boolean>): void;
    /**
     * Checks whether the main window of this ability has the focus. This API uses a promise to return the result.
     *
     * @returns { Promise<boolean> } Promise used to return the result. If the main window has the focus, **true** is
     *     returned. Otherwise, **false** is returned.
     * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
     * @famodelonly
     * @since 7
     */
    function hasWindowFocus(): Promise<boolean>;
    /**
     * Connects this ability to a ServiceAbility.
     *
     * > **NOTE**
     * >
     * > For details about the startup rules for the components in the FA model, see
     * > [Component Startup Rules (FA Model)](docroot://application-models/component-startup-rules-fa.md).
     * > > To connect to a ServiceAbility of another application, the target application must be configured with
     * > associated startup (**AssociateWakeUp** set to **true**).
     *
     * @param { Want } request - ServiceAbility to connect.
     * @param { ConnectOptions } options - Connection options.
     * @returns { number } ID of the connected ServiceAbility. The ID starts from 0 and is incremented by 1 each time a
     *     connection is set up.
     * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
     * @famodelonly
     * @since 7
     */
    function connectAbility(request: Want, options: ConnectOptions): number;
    /**
     * Disconnects this ability from a specific ServiceAbility. This API uses an asynchronous callback to return the
     * result.
     *
     * @param { number } connection - ID of the ServiceAbility to disconnect.
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the disconnection is successful,
     *     **err** is **undefined**. Otherwise, **err** is an error object.
     * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
     * @famodelonly
     * @since 7
     */
    function disconnectAbility(connection: number, callback: AsyncCallback<void>): void;
    /**
     * Disconnects this ability from a specific ServiceAbility. This API uses a promise to return the result.
     *
     * @param { number } connection - ID of the ServiceAbility to disconnect.
     * @returns { Promise<void> } Promise that returns no value.
     * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
     * @famodelonly
     * @since 7
     */
    function disconnectAbility(connection: number): Promise<void>;
    /**
     * Obtains the window corresponding to this ability. This API uses an asynchronous callback to return the result.
     *
     * @param { AsyncCallback<window.Window> } callback - Callback used to return the window.
     * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
     * @famodelonly
     * @since 7
     */
    function getWindow(callback: AsyncCallback<window.Window>): void;
    /**
     * Obtains the window corresponding to this ability. This API uses a promise to return the result.
     *
     * @returns { Promise<window.Window> } Promise used to return the window.
     * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
     * @famodelonly
     * @since 7
     */
    function getWindow(): Promise<window.Window>;
    /**
     * Defines the window configuration corresponding to this ability. The configuration is obtained through
     * **featureAbility.AbilityWindowConfiguration**.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
     * @famodelonly
     * @since 7
     */
    export enum AbilityWindowConfiguration {
        /**
         * The PageAbility is in an undefined window display mode.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
         * @famodelonly
         * @since 7
         */
        WINDOW_MODE_UNDEFINED = 0,
        /**
         * The PageAbility is in full screen mode.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
         * @famodelonly
         * @since 7
         */
        WINDOW_MODE_FULLSCREEN = 1,
        /**
         * The left screen in horizontal direction or the upper screen in vertical direction is the primary window.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
         * @famodelonly
         * @since 7
         */
        WINDOW_MODE_SPLIT_PRIMARY = 100,
        /**
         * The right screen in horizontal direction or the lower screen in vertical direction is the secondary window.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
         * @famodelonly
         * @since 7
         */
        WINDOW_MODE_SPLIT_SECONDARY = 101,
        /**
         * The PageAbility is displayed in floating window mode.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
         * @famodelonly
         * @since 7
         */
        WINDOW_MODE_FLOATING = 102
    }
    /**
     * Defines the window property corresponding to this ability. The **abilityStartSetting** property is an object
     * defined in the format of [**key: string]: any**, where **key** is an enumerated value of **
     * AbilityStartSetting** and **value** is an enumerated value of **AbilityWindowConfiguration**.
     *
     * The value is obtained through **featureAbility.AbilityStartSetting**.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
     * @famodelonly
     * @since 7
     */
    export enum AbilityStartSetting {
        /**
         * Ability window size.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
         * @famodelonly
         * @since 7
         */
        BOUNDS_KEY = 'abilityBounds',
        /**
         * Ability window display mode.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
         * @famodelonly
         * @since 7
         */
        WINDOW_MODE_KEY = 'windowMode',
        /**
         * Display device ID.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
         * @famodelonly
         * @since 7
         */
        DISPLAY_ID_KEY = 'displayId'
    }
    /**
     * Enumerates the error codes that may be returned when an ability is started.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
     * @famodelonly
     * @since 7
     */
    export enum ErrorCode {
        /**
         * No error.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
         * @famodelonly
         * @since 7
         */
        NO_ERROR = 0,
        /**
         * Invalid parameter.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
         * @famodelonly
         * @since 7
         */
        INVALID_PARAMETER = -1,
        /**
         * The ability is not found.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
         * @famodelonly
         * @since 7
         */
        ABILITY_NOT_FOUND = -2,
        /**
         * Permission denied.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
         * @famodelonly
         * @since 7
         */
        PERMISSION_DENY = -3
    }
    /**
     * Enumerates the operation types of a DataAbility. The DataAbility can use an enumerated value to specify the
     * operation type when operating data in batches.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
     * @famodelonly
     * @since 7
     */
    export enum DataAbilityOperationType {
        /**
         * Insert operation.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
         * @famodelonly
         * @since 7
         */
        TYPE_INSERT = 1,
        /**
         * Update operation.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
         * @famodelonly
         * @since 7
         */
        TYPE_UPDATE = 2,
        /**
         * Deletion operation.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
         * @famodelonly
         * @since 7
         */
        TYPE_DELETE = 3,
        /**
         * Assert operation.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
         * @famodelonly
         * @since 7
         */
        TYPE_ASSERT = 4
    }
    /**
     * Defines the Context module.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @famodelonly
     * @since 9
     */
    export type Context = _Context;
    /**
     * Defines an AppVersionInfo object.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @famodelonly
     * @since 9
     */
    export type AppVersionInfo = _AppVersionInfo;
    /**
     * Defines a ProcessInfo object.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @famodelonly
     * @since 9
     */
    export type ProcessInfo = _ProcessInfo;
}
export default featureAbility;

```
