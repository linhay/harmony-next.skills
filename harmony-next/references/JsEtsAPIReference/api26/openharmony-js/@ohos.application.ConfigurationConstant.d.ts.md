# @ohos.application.ConfigurationConstant.d.ts

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
 * @kit API10LessDeprecatedModules
 */
/**
 * The ConfigurationConstant module provides the enumerated values of the environment configuration information.
 *
 * @syscap SystemCapability.Ability.AbilityBase
 * @since 8
 * @deprecated since 9
 * @useinstead ohos.app.ability.ConfigurationConstant/ConfigurationConstant
 */
declare namespace ConfigurationConstant {
    /**
     * Enumerates the color modes.
     *
     * @syscap SystemCapability.Ability.AbilityBase
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.app.ability.ConfigurationConstant/ConfigurationConstant#ColorMode
     */
    export enum ColorMode {
        /**
         * Unspecified color mode.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.app.ability.ConfigurationConstant/ConfigurationConstant.ColorMode#COLOR_MODE_NOT_SET
         */
        COLOR_MODE_NOT_SET = -1,
        /**
         * Dark mode.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.app.ability.ConfigurationConstant/ConfigurationConstant.ColorMode#COLOR_MODE_DARK
         */
        COLOR_MODE_DARK = 0,
        /**
         * Light mode.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.app.ability.ConfigurationConstant/ConfigurationConstant.ColorMode#COLOR_MODE_LIGHT
         */
        COLOR_MODE_LIGHT = 1
    }
}
export default ConfigurationConstant;

```
