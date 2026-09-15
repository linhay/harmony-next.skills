# @ohos.app.ability.abilityDelegatorRegistry.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022-2023 Huawei Device Co., Ltd.
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
 * @kit TestKit
 */
import { AbilityDelegator as _AbilityDelegator } from './application/AbilityDelegator';
import { AbilityDelegatorArgs as _AbilityDelegatorArgs } from './application/abilityDelegatorArgs';
import { AbilityMonitor as _AbilityMonitor } from './application/AbilityMonitor';
import { AbilityStageMonitor as _AbilityStageMonitor } from './application/AbilityStageMonitor';
import { ShellCmdResult as _ShellCmdResult } from './application/shellCmdResult';
/**
 * **AbilityDelegatorRegistry**, a module of the automatic test framework, is used to obtain
 * [AbilityDelegator]{@link application/AbilityDelegator:AbilityDelegator} and
 * [AbilityDelegatorArgs]{@link application/abilityDelegatorArgs:AbilityDelegatorArgs} objects. **AbilityDelegator**
 * provides APIs for creating [AbilityMonitor]{@link application/AbilityMonitor:AbilityMonitor} objects, which can be
 * used to listen for ability lifecycle changes. **AbilityDelegatorArgs** provides APIs for obtaining test parameters.
 *
 * > **NOTE**
 * >
 * > The APIs of this module can be used only in [JsUnit](docroot://application-test/unittest-guidelines.md).
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare namespace abilityDelegatorRegistry {
    /**
     * Obtains an [AbilityDelegator]{@link application/AbilityDelegator:AbilityDelegator} object.
     *
     * @returns { AbilityDelegator } [AbilityDelegator]{@link application/AbilityDelegator:AbilityDelegator} object, which can
     *     be used to schedule the functionalities of the test framework.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    function getAbilityDelegator(): AbilityDelegator;
    /**
     * Obtains an [AbilityDelegatorArgs]{@link application/abilityDelegatorArgs:AbilityDelegatorArgs} object.
     *
     * @returns { AbilityDelegatorArgs } [AbilityDelegatorArgs]{@link application/abilityDelegatorArgs:AbilityDelegatorArgs}
     *     object, which can be used to obtain test parameters.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    function getArguments(): AbilityDelegatorArgs;
    /**
     * Enumerates the ability lifecycle states. It can be used in
     * [getAbilityState(ability)]{@link application/AbilityDelegator:AbilityDelegator.getAbilityState} of
     * [AbilityDelegator]{@link application/AbilityDelegator:AbilityDelegator} to return different ability lifecycle
     * states.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    export enum AbilityLifecycleState {
        /**
         * The ability is in an invalid state.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        UNINITIALIZED = 0,
        /**
         * The ability is created.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        CREATE = 1,
        /**
         * The ability is running in the foreground.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        FOREGROUND = 2,
        /**
         * The ability is running in the background.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        BACKGROUND = 3,
        /**
         * The ability is destroyed.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        DESTROY = 4
    }
    /**
     * Represents the **AbilityDelegator** module.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    export type AbilityDelegator = _AbilityDelegator;
    /**
     * Represents the **AbilityDelegatorArgs** module.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    export type AbilityDelegatorArgs = _AbilityDelegatorArgs;
    /**
     * Represents the **AbilityMonitor** module.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    export type AbilityMonitor = _AbilityMonitor;
    /**
     * Represents the **ShellCmdResult** module.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @atomicservice [since 11]
     * @since 9
     */
    export type ShellCmdResult = _ShellCmdResult;
    /**
     * Represents the **AbilityStageMonitor** module.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @crossplatform
     * @atomicservice
     * @since 14
     */
    export type AbilityStageMonitor = _AbilityStageMonitor;
}
export default abilityDelegatorRegistry;

```
