# @ohos.app.ability.Configuration.d.ts

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
import ConfigurationConstant from './@ohos.app.ability.ConfigurationConstant';
/**
 * The module defines the environment variables for the application runtime, including language, dark/light color mode,
 * screen orientation, and font size. You can subscribe to these environment variables to adapt to different user
 * preferences and enhance the interaction experience.
 *
 * @syscap SystemCapability.Ability.AbilityBase
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
export interface Configuration {
    /**
     * Current language of the application, for example, **zh** (Chinese) or **en** (English).
     *
     * You can
     * [set the application language](../../application-models/subscribe-system-environment-variable-changes.md#setting-application-language)
     * .
     *
     * For details about the value range, see
     * [getSystemLanguages](../apis-localization-kit/js-apis-i18n.md#getsystemlanguages9).
     *
     * @syscap SystemCapability.Ability.AbilityBase
     * @crossplatform [since 18]
     * @atomicservice [since 11]
     * @since 9
     */
    language?: string;
    /**
     * Dark/Light color mode of the application. The light color mode is used by default.
     *
     * You can
     * [set the dark/light color mode for an application or a component](../../application-models/subscribe-system-environment-variable-changes.md#setting-darklight-color-mode)
     * .
     *
     * The options are as follows:
     *
     * - **COLOR_MODE_NOT_SET**: The color mode is not set.
     * - **COLOR_MODE_LIGHT**: light mode.
     * - **COLOR_MODE_DARK**: dark mode.
     *
     * @syscap SystemCapability.Ability.AbilityBase
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    colorMode?: ConfigurationConstant.ColorMode;
    /**
     * Screen orientation of the application.
     *
     * The options are as follows:
     *
     * - **DIRECTION_NOT_SET**: The screen orientation is not set.
     * - **DIRECTION_HORIZONTAL**: horizontal direction.
     * - **DIRECTION_VERTICAL**: vertical direction.
     *
     * You can subscribe to changes to this environment variable in the [UIAbility](./js-apis-app-ability-uiAbility.md)
     * and [UIExtensionAbility](./js-apis-app-ability-uiExtensionAbility.md), but not in the
     * [ApplicationContext](./js-apis-inner-application-applicationContext.md) or
     * [AbilityStage](./js-apis-app-ability-abilityStage.md).
     *
     * @syscap SystemCapability.Ability.AbilityBase
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    direction?: ConfigurationConstant.Direction;
    /**
     * Screen density.
     *
     * The options are as follows:
     *
     * - **SCREEN_DENSITY_NOT_SET**: The pixel density is not set.
     * - **SCREEN_DENSITY_SDPI**: 120.
     * - **SCREEN_DENSITY_MDPI**: 160.
     * - **SCREEN_DENSITY_LDPI**: 240.
     * - **SCREEN_DENSITY_XLDPI**: 320.
     * - **SCREEN_DENSITY_XXLDPI**: 480.
     * - **SCREEN_DENSITY_XXXLDPI**: 640.
     *
     * The font size is positively correlated with the screen pixel density. By monitoring changes in the screen pixel
     * density, you can detect adjustments in the font size. Typically, for the same physical size, the higher the screen
     * pixel density, the larger the font display effect.
     *
     * You can subscribe to changes to this environment variable in the [UIAbility](./js-apis-app-ability-uiAbility.md)
     * and [UIExtensionAbility](./js-apis-app-ability-uiExtensionAbility.md), but not in the
     * [ApplicationContext](./js-apis-inner-application-applicationContext.md) or
     * [AbilityStage](./js-apis-app-ability-abilityStage.md).
     *
     * @syscap SystemCapability.Ability.AbilityBase
     * @crossplatform [since 18]
     * @atomicservice [since 11]
     * @since 9
     */
    screenDensity?: ConfigurationConstant.ScreenDensity;
    /**
     * ID of the display where the application is located.
     *
     * You can subscribe to changes to this environment variable in the [UIAbility](./js-apis-app-ability-uiAbility.md)
     * and [UIExtensionAbility](./js-apis-app-ability-uiExtensionAbility.md), but not in the
     * [ApplicationContext](./js-apis-inner-application-applicationContext.md) or
     * [AbilityStage](./js-apis-app-ability-abilityStage.md).
     *
     * @type { ?number } [since 9 - 10]
     * @type { ?number } [since 11]
     * @syscap SystemCapability.Ability.AbilityBase
     * @atomicservice [since 11]
     * @since 9
     */
    displayId?: number;
    /**
     * Whether a pointer device, such as a keyboard, mouse, or touchpad, is connected. **true** if connected, **false**
     * otherwise.
     *
     * @syscap SystemCapability.Ability.AbilityBase
     * @atomicservice [since 11]
     * @since 9
     */
    hasPointerDevice?: boolean;
    /**
     * Unique ID of the font.
     *
     * @syscap SystemCapability.Ability.AbilityBase
     * @atomicservice
     * @since 14
     */
    fontId?: string;
    /**
     * Font size scale ratio. The value is a non-negative number. The default value is **1**.
     *
     * You can
     * [set the font size for an application](../../application-models/subscribe-system-environment-variable-changes.md#setting-font-size)
     * .
     *
     * @type { ?number } [since 12 - 17]
     * @type { ?number } [since 18]
     * @syscap SystemCapability.Ability.AbilityBase
     * @crossplatform [since 18]
     * @atomicservice
     * @since 12
     */
    fontSizeScale?: number;
    /**
     * Font weight scale ratio. The value is a non-negative number. The default value is **1**.
     *
     * @syscap SystemCapability.Ability.AbilityBase
     * @crossplatform [since 26.0.0]
     * @atomicservice
     * @since 12
     */
    fontWeightScale?: number;
    /**
     * Mobile country code.
     *
     * @syscap SystemCapability.Ability.AbilityBase
     * @atomicservice
     * @since 12
     */
    mcc?: string;
    /**
     * Mobile network code.
     *
     * @syscap SystemCapability.Ability.AbilityBase
     * @atomicservice
     * @since 12
     */
    mnc?: string;
    /**
     * Locale.
     *
     * The application automatically adjusts its behavior based on the current locale to meet the localization
     * requirements of users. This property can be set by configuring the system language, system region, and
     * application preferred language.
     *
     * @syscap SystemCapability.Ability.AbilityBase
     * @atomicservice
     * @since 20
     */
    locale?: Intl.Locale;
}

```
