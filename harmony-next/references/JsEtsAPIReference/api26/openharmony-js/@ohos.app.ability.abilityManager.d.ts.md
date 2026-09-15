# @ohos.app.ability.abilityManager.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022-2024 Huawei Device Co., Ltd.
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
import { AbilityRunningInfo as _AbilityRunningInfo } from './application/AbilityRunningInfo';
import Context from './application/Context';
import * as _AbilityStateData from './application/AbilityStateData';
/**
 * The AbilityManager module provides APIs for obtaining, adding, and updating ability information and running status
 * information.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @atomicservice [since 20]
 * @since 9
 */
declare namespace abilityManager {
    /**
     * Enumerates the ability states. This enum can be used together with
     * [AbilityRunningInfo]{@link ./application/AbilityRunningInfo:AbilityRunningInfo} to return the ability state.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @since 14
     */
    export enum AbilityState {
        /**
         * The ability is in the initial state.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @since 14
         */
        INITIAL = 0,
        /**
         * The ability has the focus.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @since 14
         */
        FOCUS = 2,
        /**
         * The ability is in the foreground state.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @since 14
         */
        FOREGROUND = 9,
        /**
         * The ability is in the background state.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @since 14
         */
        BACKGROUND = 10,
        /**
         * The ability is in the state of being switched to the foreground.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @since 14
         */
        FOREGROUNDING = 11,
        /**
         * The ability is in the state of being switched to the background.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @since 14
         */
        BACKGROUNDING = 12
    }
    /**
     * Obtains the UIAbility running information. This API uses a promise to return the result.
     *
     * > **NOTE**
     * >
     * > If the application has requested the ohos.permission.GET_RUNNING_INFO permission, it can obtain the UIAbility
     * > running information of all applications; otherwise, it can obtain the UIAbility running information of the
     * > current application.
     *
     * @permission ohos.permission.GET_RUNNING_INFO
     * @returns { Promise<Array<AbilityRunningInfo>> } Promise used to return the UIAbility running information. You can
     *     perform error handling or other custom processing.
     * @throws { BusinessError } 16000050 - Internal error.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @since 14
     */
    function getAbilityRunningInfos(): Promise<Array<AbilityRunningInfo>>;
    /**
     * Restarts the current atomic service.
     *
     * > **NOTE**
     * >
     * > - Currently, atomic services can be started only in an independent window.
     * >
     * > - If you call this API,
     * > [ApplicationContext.restartApp()]{@link ./application/ApplicationContext:ApplicationContext/restartApp}, or
     * > [UIAbilityContext.restartApp()]{@link ./application/UIAbilityContext:UIAbilityContext.restartApp} within 3 seconds
     * > after a successful call to this API, the system returns error code 16000064.
     *
     * @param { Context } context - Context of the ability.<br>Note: Currently, only
     *     [UIAbilityContext]{@link ./application/UIAbilityContext:UIAbilityContext} is supported.<br>
     * @throws { BusinessError } 16000050 - Internal error. Possible causes: 1. Connect to system service failed;
     *     2.Send restart message to system service failed; 3.System service failed to communicate with dependency module.
     * @throws { BusinessError } 16000053 - The ability is not on the top of the UI.
     * @throws { BusinessError } 16000064 - Restart too frequently. Try again at least 3s later.
     * @throws { BusinessError } 16000086 - The context is not UIAbilityContext.
     * @throws { BusinessError } 16000090 - The caller is not an atomic service.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    function restartSelfAtomicService(context: Context): void;
    /**
     * Indicates whether the current device supports EmbeddedUIExtensionAbility.
     *
     * @returns { boolean } Returns {@code true} if EmbeddedUIExtensionAbility is supported,
     *     returns {@code false} otherwise.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    function isEmbeddedUIExtensionSupported(): boolean;
    /**
     * Defines the level-2 module AbilityRunningInfo.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @since 14
     */
    export type AbilityRunningInfo = _AbilityRunningInfo;
    /**
     * Defines the level-2 module AbilityStateData.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @since 14
     */
    export type AbilityStateData = _AbilityStateData.default;
}
export default abilityManager;

```
