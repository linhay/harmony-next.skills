# @ohos.ability.ability.d.ts

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
 * @kit AbilityKit
 */
import { DataAbilityHelper as _DataAbilityHelper } from './ability/dataAbilityHelper';
import { PacMap as _PacMap } from './ability/dataAbilityHelper';
import { DataAbilityOperation as _DataAbilityOperation } from './ability/dataAbilityOperation';
import { DataAbilityResult as _DataAbilityResult } from './ability/dataAbilityResult';
import { AbilityResult as _AbilityResult } from './ability/abilityResult';
import { ConnectOptions as _ConnectOptions } from './ability/connectOptions';
import { StartAbilityParameter as _StartAbilityParameter } from './ability/startAbilityParameter';
/**
 * The module provides all level-2 module APIs for developers to export.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
 * @famodelonly [since 9 - 10]
 * @since 9
 */
declare namespace ability {
    /**
     * Defines the level-2 module DataAbilityHelper.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
     * @famodelonly
     * @since 9
     */
    export type DataAbilityHelper = _DataAbilityHelper;
    /**
     * Defines the level-2 module PacMap.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
     * @famodelonly [since 9 - 10]
     * @since 9
     */
    export type PacMap = _PacMap;
    /**
     * Defines the level-2 module DataAbilityOperation.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
     * @famodelonly
     * @since 9
     */
    export type DataAbilityOperation = _DataAbilityOperation;
    /**
     * Defines the level-2 module DataAbilityResult.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
     * @famodelonly
     * @since 9
     */
    export type DataAbilityResult = _DataAbilityResult;
    /**
     * Defines the level-2 module AbilityResult.
     *
     * @syscap SystemCapability.Ability.AbilityBase
     * @famodelonly
     * @since 9
     */
    export type AbilityResult = _AbilityResult;
    /**
     * Defines the level-2 module ConnectOptions.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @famodelonly
     * @since 9
     */
    export type ConnectOptions = _ConnectOptions;
    /**
     * Defines the level-2 module StartAbilityParameter.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
     * @famodelonly
     * @since 9
     */
    export type StartAbilityParameter = _StartAbilityParameter;
}
export default ability;

```
