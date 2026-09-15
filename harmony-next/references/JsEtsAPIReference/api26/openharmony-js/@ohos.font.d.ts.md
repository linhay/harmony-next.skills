# @ohos.font.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022-2024 Huawei Device Co., Ltd.
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
 * @file Custom Font Registration
 * @kit ArkUI
 */
/**
 * The **font** module provides APIs for registering custom fonts.
 *
 * > **NOTE**
 * >
 * > - The functionality of this module depends on UI context. This means that the APIs of this module cannot be used
 * > where [the UI context is ambiguous](docroot://ui/arkts-global-interface.md#ambiguous-ui-context). For details, see
 * > [UIContext]{@link @ohos.arkui.UIContext}.
 * >
 * > - You are advised to use the [loadFontSync]{@link @ohos.graphics.text:text.FontCollection#loadFontSync} API of the
 * > font engine to register custom fonts.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @crossplatform [since 12]
 * @atomicservice [since 11]
 * @since 9
 */
declare namespace font {
    /**
     * Information about the custom font to register.
     *
     * > **NOTE**
     * >
     * > Directly using **font** can lead to the issue of
     * > [ambiguous UI context](docroot://ui/arkts-global-interface.md#ambiguous-ui-context). To avoid this, obtain the
     * > [Font]{@link @ohos.arkui.UIContext} object associated with the current UI context by using the
     * > [getFont](docroot://reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getfont) API in
     * > [UIContext]{@link @ohos.arkui.UIContext}.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @crossplatform [since 12]
     * @atomicservice [since 11]
     * @since 9
     */
    interface FontOptions {
        /**
         * Name of the custom font to register.
         *
         * @type { string } [since 9 - 9]
         * @type { string | Resource } [since 10]
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        familyName: string | Resource;
        /**
         * Path of the custom font file to register.
         *
         * **NOTE**
         *
         * If the font file to specify is a resource located within the system sandbox directory, you are advised to use a
         * string with the **file://** path prefix. Ensure the target file exists in the sandbox path and has read
         * permissions granted.
         *
         * @type { string } [since 9 - 9]
         * @type { string | Resource } [since 10]
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        familySrc: string | Resource;
    }
    /**
     * Information about the system font.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform [since 12]
     * @atomicservice [since 11]
     * @since 10
     */
    interface FontInfo {
        /**
         * File path of the system font.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        path: string;
        /**
         * PostScript name of the system font.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        postScriptName: string;
        /**
         * Name of the system font.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        fullName: string;
        /**
         * Family of the system font.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        family: string;
        /**
         * Subfamily of the system font.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        subfamily: string;
        /**
         * Weight of the system font.
         *
         * Value range: [100, 900], with intervals of 100, corresponding to the values in the
         * [FontWeight]{@link @ohos.graphics.text:text.FontWeight} enum
         *
         * Default value: **100**
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        weight: number;
        /**
         * Width of the system font.
         *
         * Value range: [1, 9], with intervals of 1, corresponding to the values in the
         * [FontWidth]{@link @ohos.graphics.text:text.FontWidth} enum
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        width: number;
        /**
         * Whether the system font is italic.
         *
         * Default value: **false**
         *
         * **true**: The system font is italic. **false**: The system font is not italic.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        italic: boolean;
        /**
         * Whether the system font is monospaced.
         *
         * Default value: **false**
         *
         * **true**: The system font is monospaced. **false**: The system font is not monospaced.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        monoSpace: boolean;
        /**
         * Whether the system font supports symbols.
         *
         * Default value: **false**
         *
         * **true**: The system font supports symbols. **false**: The system font does not support symbols.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        symbolic: boolean;
    }
    /**
     * UI font configuration of the system.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 11
     */
    interface UIFontConfig {
        /**
         * Path to the system font file.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 11
         */
        fontDir: Array<string>;
        /**
         * List of supported generic font families.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 11
         */
        generic: Array<UIFontGenericInfo>;
        /**
         * List of fallback generic font families.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 11
         */
        fallbackGroups: Array<UIFontFallbackGroupInfo>;
    }
    /**
     * UI font configuration of the system.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 11
     */
    interface UIFontGenericInfo {
        /**
         * Font family name, which is the value of **family** specified in the font file.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 11
         */
        family: string;
        /**
         * Font alias configuration information.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 11
         */
        alias: Array<UIFontAliasInfo>;
        /**
         * Weight of the font when displayed, which corresponds to the original weight.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 11
         */
        adjust: Array<UIFontAdjustInfo>;
    }
    /**
     * UI font configuration of the system.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 11
     */
    interface UIFontAliasInfo {
        /**
         * Alias name.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 11
         */
        name: string;
        /**
         * Weight of the fonts included in the font family. If the value is greater than 0, the font family contains only
         * the fonts with the specified weight. If the value is 0, the font family contains all fonts.
         *
         * Valid values are **0**, **100**, **400**, **700**, and **900**.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 11
         */
        weight: number;
    }
    /**
     * UI font configuration of the system.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 11
     */
    interface UIFontAdjustInfo {
        /**
         * Original weight of the font.
         *
         * Valid values are **50**, **80**, **100**, and **200**.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 11
         */
        weight: number;
        /**
         * Weight of the font displayed in the application.
         *
         * Valid values are **100**, **400**, **700**, and **900**.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 11
         */
        to: number;
    }
    /**
     * UI font configuration of the system.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 11
     */
    interface UIFontFallbackGroupInfo {
        /**
         * Name of the font family corresponding to the fallback fonts.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 11
         */
        fontSetName: string;
        /**
         * Fallback fonts for the font family. If **fontSetName** is **""**, it indicates that the fonts can be used as
         * fallback fonts for all font families.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 11
         */
        fallback: Array<UIFontFallbackInfo>;
    }
    /**
     * UI font configuration of the system.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 11
     */
    interface UIFontFallbackInfo {
        /**
         * Language supported by the font family. The language format is BCP 47.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 11
         */
        language: string;
        /**
         * Font family name, which is the value of **family** specified in the font file.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 11
         */
        family: string;
    }
    /**
     * Registers a custom font with the font manager.
     *
     * This API is asynchronous and does not support concurrent calls.
     *
     * > **NOTE**
     * >
     * > - Since API version 10, you can use the
     * > [getFont](docroot://reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getfont) API in
     * > [UIContext]{@link @ohos.arkui.UIContext} to obtain the [Font]{@link @ohos.arkui.UIContext} object associated with
     * > the current UI context.
     *
     * @param { FontOptions } options - Information about the custom font to register.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @crossplatform [since 12]
     * @atomicservice [since 11]
     * @since 9
     * @deprecated since 18
     * @useinstead ohos.arkui.UIContext.Font#registerFont
     */
    function registerFont(options: FontOptions): void;
    /**
     * Obtains this system font list.
     *
     * This API only takes effect on PCs/2-in-1 devices and returns an empty array on other devices.
     *
     * You are advised to use the
     * [getSystemFontFullNamesByType]{@link @ohos.graphics.text:text.getSystemFontFullNamesByType} API to obtain the
     * latest system-supported font list data.
     *
     * > **NOTE**
     * >
     * > - Since API version 10, you can use the
     * > [getFont](docroot://reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getfont) API in
     * > [UIContext]{@link @ohos.arkui.UIContext} to obtain the [Font]{@link @ohos.arkui.UIContext} object associated with
     * > the current UI context.
     *
     * @returns { Array<string> } List of supported fonts.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform [since 12]
     * @atomicservice [since 11]
     * @since 10
     * @deprecated since 18
     * @useinstead ohos.arkui.UIContext.Font#getSystemFontList
     */
    function getSystemFontList(): Array<string>;
    /**
     * Obtains information about a system font based on the font name.
     *
     * > **NOTE**
     * >
     * > - Since API version 10, you can use the
     * > [getFont](docroot://reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getfont) API in
     * > [UIContext]{@link @ohos.arkui.UIContext} to obtain the [Font]{@link @ohos.arkui.UIContext} object associated with
     * > the current UI context.
     *
     * @param { string } fontName - System font name.
     * @returns { FontInfo } Information about the system font.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform [since 12]
     * @atomicservice [since 11]
     * @since 10
     * @deprecated since 18
     * @useinstead ohos.arkui.UIContext.Font#getFontByName
     */
    function getFontByName(fontName: string): FontInfo;
    /**
     * Obtains the UI font configuration information in the system font configuration file.
     *
     * This API can only obtain the information in the configuration file. If the UI context is not clear, **undefined**
     * may be returned. If you want to obtain the full font configuration information, you are advised to use the
     * [getSystemFontFullNamesByType]{@link @ohos.graphics.text:text.getSystemFontFullNamesByType} API of the font engine.
     *
     * @returns { UIFontConfig } Returns the ui font config
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 11
     */
    function getUIFontConfig(): UIFontConfig;
}
export default font;

```
