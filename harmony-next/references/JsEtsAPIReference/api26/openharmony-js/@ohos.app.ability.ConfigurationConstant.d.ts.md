# @ohos.app.ability.ConfigurationConstant.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022-2025 Huawei Device Co., Ltd.
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
/**
 * The ConfigurationConstant module provides preset enumerated values related to
 * [Configuration]{@link @ohos.app.ability.Configuration:Configuration} operations.
 *
 * @syscap SystemCapability.Ability.AbilityBase
 * @crossplatform [since 12]
 * @atomicservice [since 11]
 * @since 9
 */
declare namespace ConfigurationConstant {
    /**
     * Enumerates the dark/light color modes, which are used in the
     * [Configuration.colorMode]{@link @ohos.app.ability.Configuration:Configuration} field. You can use these predefined
     * enumerated values to set or obtain the dark/light color mode of the system or application.
     *
     * @syscap SystemCapability.Ability.AbilityBase
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    export enum ColorMode {
        /**
         * Unspecified color mode.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        COLOR_MODE_NOT_SET = -1,
        /**
         * Dark mode.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        COLOR_MODE_DARK = 0,
        /**
         * Light mode.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        COLOR_MODE_LIGHT = 1
    }
    /**
     * Enumerates the screen directions, which are used in the
     * [Configuration.direction]{@link @ohos.app.ability.Configuration:Configuration} field. You can use these predefined
     * enumerated values to set or obtain the screen direction of the system or application.
     *
     * @syscap SystemCapability.Ability.AbilityBase
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    export enum Direction {
        /**
         * Unspecified direction.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        DIRECTION_NOT_SET = -1,
        /**
         * Vertical direction.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        DIRECTION_VERTICAL = 0,
        /**
         * Horizontal direction.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        DIRECTION_HORIZONTAL = 1
    }
    /**
     * Enumerates the pixel densities of the screen, which are used in the
     * [Configuration.screenDensity]{@link @ohos.app.ability.Configuration:Configuration} field. You can use these
     * predefined enumerated values to set or obtain the pixel density of the screen.
     *
     * The font size is positively correlated with the screen pixel density. By monitoring changes in the screen pixel
     * density, you can detect adjustments in the font size. Typically, for the same physical size, the higher the screen
     * pixel density, the larger the font display effect.
     *
     * @syscap SystemCapability.Ability.AbilityBase
     * @crossplatform [since 18]
     * @atomicservice [since 11]
     * @since 9
     */
    export enum ScreenDensity {
        /**
         * The screen pixel density is not set.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 9
         */
        SCREEN_DENSITY_NOT_SET = 0,
        /**
         * The pixel density of the screen is 'SDPI'.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 9
         */
        SCREEN_DENSITY_SDPI = 120,
        /**
         * The pixel density of the screen is 'MDPI'.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 9
         */
        SCREEN_DENSITY_MDPI = 160,
        /**
         * The pixel density of the screen is 'LDPI'.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 9
         */
        SCREEN_DENSITY_LDPI = 240,
        /**
         * The pixel density of the screen is 'XLDPI'.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 9
         */
        SCREEN_DENSITY_XLDPI = 320,
        /**
         * The pixel density of the screen is 'XXLDPI'.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 9
         */
        SCREEN_DENSITY_XXLDPI = 480,
        /**
         * The pixel density of the screen is 'XXXLDPI'.
         *
         * @syscap SystemCapability.Ability.AbilityBase
         * @crossplatform [since 18]
         * @atomicservice [since 11]
         * @since 9
         */
        SCREEN_DENSITY_XXXLDPI = 640
    }
}
export default ConfigurationConstant;

```
