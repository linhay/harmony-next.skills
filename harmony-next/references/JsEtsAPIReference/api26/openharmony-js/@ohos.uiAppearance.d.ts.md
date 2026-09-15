# @ohos.uiAppearance.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2025 Huawei Device Co., Ltd.
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
 * @file UI Appearance
 * @kit ArkUI
 */
/**
 * This module provides basic capabilities for obtaining system appearance configurations, including color mode (dark/
 * light) settings, font size scale factors, and font weight scale factors.
 *
 * > **NOTE**
 *
 * @syscap SystemCapability.ArkUI.UiAppearance
 * @since 20
 */
declare namespace uiAppearance {
    /**
     * Enumerates the color modes.
     *
     *
     * @syscap SystemCapability.ArkUI.UiAppearance
     * @since 20
     */
    enum DarkMode {
        /**
         * Always display with dark mode.
         *
         * @syscap SystemCapability.ArkUI.UiAppearance
         * @since 20
         */
        ALWAYS_DARK = 0,
        /**
         * Always display with light mode.
         *
         * @syscap SystemCapability.ArkUI.UiAppearance
         * @since 20
         */
        ALWAYS_LIGHT = 1
    }
    /**
     * Obtains the current system dark mode configuration.
     *
     * <!--Del-->
     *
     * > **NOTE**
     *
     * > This API is a system API in API version 19 and earlier. Using this API requires the
     * > [ohos.permission.UPDATE_CONFIGURATION](docroot://security/AccessToken/permissions-for-system-apps.md#ohospermissionupdate_configuration)
     * > permission.
     *
     * <!--DelEnd-->
     *
     * @returns { DarkMode } current dark-mode.
     * @throws { BusinessError } 500001 - Internal error.
     * @syscap SystemCapability.ArkUI.UiAppearance
     * @crossplatform [since 26.0.0]
     * @since 20
     */
    function getDarkMode(): DarkMode;
    /**
     * Obtains the current font size scale factor.
     *
     * <!--Del-->
     *
     * > **NOTE**
     *
     * > This API is a system API in API version 19 and earlier. Using this API requires the
     * > [ohos.permission.UPDATE_CONFIGURATION](docroot://security/AccessToken/permissions-for-system-apps.md#ohospermissionupdate_configuration)
     * > permission.
     *
     * <!--DelEnd-->
     *
     * @returns { number } current font-scale.
     * @throws { BusinessError } 500001 - Internal error.
     * @syscap SystemCapability.ArkUI.UiAppearance
     * @crossplatform [since 26.0.0]
     * @since 20
     */
    function getFontScale(): number;
    /**
     * Obtains the current font weight scale factor.
     *
     * <!--Del-->
     *
     * > **NOTE**
     *
     * > This API is a system API in API version 19 and earlier. Using this API requires the
     * > [ohos.permission.UPDATE_CONFIGURATION](docroot://security/AccessToken/permissions-for-system-apps.md#ohospermissionupdate_configuration)
     * > permission.
     *
     * <!--DelEnd-->
     *
     * @returns { number } current font-weight-scale.
     * @throws { BusinessError } 500001 - Internal error.
     * @syscap SystemCapability.ArkUI.UiAppearance
     * @since 20
     */
    function getFontWeightScale(): number;
}
export default uiAppearance;

```
