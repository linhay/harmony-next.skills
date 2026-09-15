# @ohos.app.ability.systemConfiguration.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2026 Huawei Device Co., Ltd.
 * Licensed under the Apache License, Version 2.0 (the "License"),
 * you may not use this file except in compliance with the License.
 * You may obtain an copy of the License at
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
import ConfigurationConstant from './@ohos.app.ability.ConfigurationConstant';
/**
 * The class of a system configuration.
 *
 * @namespace systemConfiguration
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @stagemodelonly
 * @atomicservice
 * @since 24
 */
declare namespace systemConfiguration {
    /**
     * Defines an OnColorModeUpdatedFn function.
     *
     * @typedef { function }
     * @param { ConfigurationConstant.ColorMode } colorMode - Indicates the system's light or dark color mode
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 24
     */
    type OnColorModeUpdatedFn = (colorMode: ConfigurationConstant.ColorMode) => void;
    /**
     * Defines an OnFontSizeScaleUpdatedFn function.
     *
     * @typedef { function }
     * @param { number } fontSizeScale - Indicates the system's font size
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 24
     */
    type OnFontSizeScaleUpdatedFn = (fontSizeScale: number) => void;
    /**
     * Defines an OnFontWeightScaleUpdatedFn function.
     *
     * @typedef { function }
     * @param { number } fontWeightScale - Indicates the system's font weight
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 24
     */
    type OnFontWeightScaleUpdatedFn = (fontWeightScale: number) => void;
    /**
     * Defines an OnMCCUpdatedFn function.
     *
     * @typedef { function }
     * @param { string } mcc - Indicates the mobile country code
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 24
     */
    type OnMCCUpdatedFn = (mcc: string) => void;
    /**
     * Defines an OnMNCUpdatedFn function.
     *
     * @typedef { function }
     * @param { string } mnc - Indicates the mobile network code
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 24
     */
    type OnMNCUpdatedFn = (mnc: string) => void;
    /**
     * Defines an OnLanguageUpdatedFn function.
     *
     * @typedef { function }
     * @param { string } language - Indicates the system's language
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 24
     */
    type OnLanguageUpdatedFn = (language: string) => void;
    /**
     * Defines an OnFontIdUpdatedFn function.
     *
     * @typedef { function }
     * @param { string } fontId - Indicates the font type of the system
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 24
     */
    type OnFontIdUpdatedFn = (fontId: string) => void;
    /**
     * Defines an OnHasPointerDeviceUpdatedFn function.
     *
     * @typedef { function }
     * @param { boolean } hasPointerDevice - Indicates whether a pointing device is connected,
     *     such as a mouse, keyboard, or touchpad
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 24
     */
    type OnHasPointerDeviceUpdatedFn = (hasPointerDevice: boolean) => void;
    /**
     * Defines an OnLocaleUpdatedFn function.
     *
     * @typedef { function }
     * @param { string } locale - Indicates the locale settings. The application will automatically adjust
     *     its behavior based on the current locale to meet the user's localization requirements. This property
     *     can be configured by setting the system language, system region, and application language preferences
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 24
     */
    type OnLocaleUpdatedFn = (locale: string) => void;
    /**
     * System configuration updated callback.
     *
     * @typedef UpdatedCallback
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 24
     */
    interface UpdatedCallback {
        /**
         * Called when system's color mode is updated.
         *
         * @type { ?OnColorModeUpdatedFn }
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        onColorModeUpdated?: OnColorModeUpdatedFn;
        /**
         * Called when system's font size is updated.
         *
         * @type { ?OnFontSizeScaleUpdatedFn }
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        onFontSizeScaleUpdated?: OnFontSizeScaleUpdatedFn;
        /**
         * Called when system's font weight is updated.
         *
         * @type { ?OnFontWeightScaleUpdatedFn }
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        onFontWeightScaleUpdated?: OnFontWeightScaleUpdatedFn;
        /**
         * Called when mobile country code is updated.
         *
         * @type { ?OnMCCUpdatedFn }
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        onMCCUpdated?: OnMCCUpdatedFn;
        /**
         * Called when mobile network code is updated.
         *
         * @type { ?OnMNCUpdatedFn }
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        onMNCUpdated?: OnMNCUpdatedFn;
        /**
         * Called when system's language is updated.
         *
         * @type { ?OnLanguageUpdatedFn }
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        onLanguageUpdated?: OnLanguageUpdatedFn;
        /**
         * Called when system's font style is updated.
         *
         * @type { ?OnFontIdUpdatedFn }
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        onFontIdUpdated?: OnFontIdUpdatedFn;
        /**
         * Called when a pointing device is connected, such as a mouse, keyboard, or touchpad.
         *
         * @type { ?OnHasPointerDeviceUpdatedFn }
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        onHasPointerDeviceUpdated?: OnHasPointerDeviceUpdatedFn;
        /**
         * Called when locale info is updated.
         *
         * @type { ?OnLocaleUpdatedFn }
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        onLocaleUpdated?: OnLocaleUpdatedFn;
    }
}
export default systemConfiguration;

```
