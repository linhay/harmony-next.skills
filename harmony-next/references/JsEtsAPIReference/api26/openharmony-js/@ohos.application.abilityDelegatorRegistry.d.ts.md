# @ohos.application.abilityDelegatorRegistry.d.ts

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
 * @kit API10LessDeprecatedModules
 */
import { AbilityDelegator } from './application/AbilityDelegator';
import { AbilityDelegatorArgs } from './application/abilityDelegatorArgs';
/**
 * The **AbilityDelegatorRegistry** module provides APIs for storing global registers of the registered
 * [AbilityDelegator]{@link ./application/AbilityDelegator:AbilityDelegator} and
 * [AbilityDelegatorArgs]{@link ./application/abilityDelegatorArgs:AbilityDelegatorArgs} objects, including obtaining
 * the **AbilityDelegator** and **AbilityDelegatorArgs** objects. The APIs can be used only in the test framework.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @since 8
 * @deprecated since 9
 * @useinstead @ohos.app.ability.abilityDelegatorRegistry:abilityDelegatorRegistry
 */
declare namespace abilityDelegatorRegistry {
    /**
     * Obtains the **AbilityDelegator** object of the application.
     *
     * @returns { AbilityDelegator } [AbilityDelegator]{@link ./application/AbilityDelegator:AbilityDelegator} object,
     *     which can be used to schedule functions related to the test framework.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.app.ability.abilityDelegatorRegistry:abilityDelegatorRegistry.getAbilityDelegator
     */
    function getAbilityDelegator(): AbilityDelegator;
    /**
     * Obtains the **AbilityDelegatorArgs** object of the application.
     *
     * @returns { AbilityDelegatorArgs }
     *     [AbilityDelegatorArgs]{@link ./application/abilityDelegatorArgs:AbilityDelegatorArgs} object, which can be used
     *     to obtain test parameters.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.app.ability.abilityDelegatorRegistry:abilityDelegatorRegistry.getArguments
     */
    function getArguments(): AbilityDelegatorArgs;
    /**
     * Enumerates the ability lifecycle states.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.app.ability.abilityDelegatorRegistry:abilityDelegatorRegistry.AbilityLifecycleState
     */
    export enum AbilityLifecycleState {
        /**
         * The ability is in an invalid state.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.app.ability.abilityDelegatorRegistry:abilityDelegatorRegistry.AbilityLifecycleState.UNINITIALIZED
         */
        UNINITIALIZED = 0,
        /**
         * The ability is created.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.app.ability.abilityDelegatorRegistry:abilityDelegatorRegistry.AbilityLifecycleState.CREATE
         */
        CREATE = 1,
        /**
         * The ability is running in the foreground.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.app.ability.abilityDelegatorRegistry:abilityDelegatorRegistry.AbilityLifecycleState.FOREGROUND
         */
        FOREGROUND = 2,
        /**
         * The ability is running in the background.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.app.ability.abilityDelegatorRegistry:abilityDelegatorRegistry.AbilityLifecycleState.BACKGROUND
         */
        BACKGROUND = 3,
        /**
         * The ability is destroyed.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.app.ability.abilityDelegatorRegistry:abilityDelegatorRegistry.AbilityLifecycleState.DESTROY
         */
        DESTROY = 4
    }
}
export default abilityDelegatorRegistry;

```
