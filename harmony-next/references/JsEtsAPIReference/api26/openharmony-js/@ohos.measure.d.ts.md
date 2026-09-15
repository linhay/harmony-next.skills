# @ohos.measure.d.ts

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
 * The **measure** module provides APIs for measuring text metrics, such as text height and width.
 *
 * > **NOTE**
 * >
 * > - This module cannot be used in the file declaration of the [UIAbility]{@link @ohos.app.ability.UIAbility}. In
 * > other words, the APIs of this module can be used only after a component instance is created; they cannot be called
 * > in the lifecycle of the UIAbility.
 * >
 * > - To perform more complex text measurements, you are advised to call the corresponding graphics measurement API,
 * > specifically [Paragraph]{@link @ohos.graphics.text:text.ParagraphStyle}.
 * >
 * > - Avoid using [ApplicationContext.setFontSizeScale]{@link ApplicationContext:ApplicationContext#setFontSizeScale}
 * > during text measurement API calls. To ensure timing consistency and the accuracy of measurement results, manually
 * > listen for font scale changes.
 * >
 * > - For measuring text after truncation, direct use of the string length for truncation may lead to inaccuracies.
 * > This is because certain Unicode characters (for example, emojis) have code points with a length greater than 1, and
 * > truncating by string length can split these multi-code-point characters, resulting in incorrect text display or
 * > measurement errors. As such, you are advised to perform iterative processing based on Unicode code points during
 * > truncation.
 *
 * @file Text Measurement
 * @kit ArkUI
 */
/**
 * Provides attributes of the measured text.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @crossplatform [since 11]
 * @atomicservice [since 12]
 * @since 9
 */
export interface MeasureOptions {
    /**
     * Content of the measured text.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 9
     */
    textContent: string | Resource;
    /**
     * Layout width of the measured text.
     *
     * **NOTE**
     *
     * The default unit is vp. The value cannot be a percentage. If this parameter is not set, the value of
     * **SizeOptions** is the maximum width allowed for the single-line text.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 10
     */
    constraintWidth?: number | string | Resource;
    /**
     * Font size of the text to be measured. When **fontSize** is of the number type, the unit is vp.
     *
     * Default value: **16**
     *
     * **NOTE**
     *
     * The value cannot be a percentage.
     *
     * Since API version 12, the fp unit is used when **fontSize** is of the number type.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 9
     */
    fontSize?: number | string | Resource;
    /**
     * Font style of the measured text.
     *
     * Default value: **FontStyle.Normal**
     *
     * Value range for the number type: [0, 1], with intervals of 1, corresponding to the values in the **FontStyle** enum
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 9
     */
    fontStyle?: number | FontStyle;
    /**
     * Font width of the measured text. For the number type, the value ranges from 100 to 900, at an interval of 100. A
     * larger value indicates a heavier font weight. The default value is **400**. For the string type, only strings of
     * the number type are supported, for example, **400**, **"bold"**, **"bolder"**, **"lighter"**, **"regular"**, and
     * **"medium"**, which correspond to the enumerated values in **FontWeight**.
     *
     * Default value: **FontWeight.Normal**
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 9
     */
    fontWeight?: number | string | FontWeight;
    /**
     * Font family of the measured text. Default value: **'HarmonyOS Sans'**
     *
     * Only the default font is supported.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 9
     */
    fontFamily?: string | Resource;
    /**
     * Letter spacing of the measured text.
     *
     * Default value: **0**
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 9
     */
    letterSpacing?: number | string;
    /**
     * Horizontal alignment mode of the measured text.
     *
     * Default value: **TextAlign.Start**
     *
     * Value range for the number type: [0, 3], with intervals of 1, corresponding to the values in the **TextAlign** enum
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 10
     */
    textAlign?: number | TextAlign;
    /**
     * Display mode when the measured text is too long.
     *
     * Default value: **1**
     *
     * Value range for the number type: [0, 3], with intervals of 1, corresponding to the values in the **TextOverflow**
     * enum
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 10
     */
    overflow?: number | TextOverflow;
    /**
     * Maximum number of lines in the measured text.
     *
     * Value range: [0, *INT32_MAX*]
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 10
     */
    maxLines?: number;
    /**
     * Line height of the measured text.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 10
     */
    lineHeight?: number | string | Resource;
    /**
     * Baseline offset of the measured text.
     *
     * Default value: **0**
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 10
     */
    baselineOffset?: number | string;
    /**
     * Case of the measured text.
     *
     * Default value: **TextCase.Normal**
     *
     * Value range for the number type: [0, 2], with intervals of 1, corresponding to the values in the **TextCase** enum
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 10
     */
    textCase?: number | TextCase;
    /**
     * Indentation of the first line. Default value: **0**.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice [since 12]
     * @since 11
     */
    textIndent?: number | string;
    /**
     * Line break rule.
     *
     * Default value: **WordBreak.BREAK_WORD**
     *
     * **NOTE**
     *
     * When used with **{overflow: TextOverflow.Ellipsis}** and **maxLines**, **WordBreak.BREAK_ALL** can insert line
     * breaks between letters when overflow occurs and display excess content with an ellipsis (...).
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice [since 12]
     * @since 11
     */
    wordBreak?: WordBreak;
}
/**
 * Defines the Measure interface.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @crossplatform [since 12]
 * @atomicservice [since 12]
 * @since 9
 */
export default class MeasureText {
    /**
     * Measures the single-line display width of the specified text. For multi-line text (separated by newline characters
     * **\n**), this API returns the width of the longest line.
     *
     * > **NOTE**
     * >
     * > - Since API version 12, you can use the
     * > [getMeasureUtils](docroot://reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getmeasureutils12) API in
     * > [UIContext]{@link @ohos.arkui.UIContext} to obtain the [MeasureUtils]{@link @ohos.arkui.UIContext} object
     * > associated with the current UI context.
     * >
     * > - **measureText** always measures single-line text width. Layout constraints in **options** (**constraintWidth**,
     * > **maxLines**, and more) do not affect results. For layout-constrained width measurement, use
     * > [measureTextSize](docroot://reference/apis-arkui/arkts-apis-uicontext-measureutils.md#measuretextsize12).
     *
     * @param { MeasureOptions } options - Information about the measured text.
     * @returns { number } Text width.
     *     <br>Unit: px
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @crossplatform [since 11]
     * @atomicservice [since 12]
     * @since 9
     * @deprecated since 18
     * @useinstead ohos.arkui.UIContext.MeasureUtils#measureText
     */
    static measureText(options: MeasureOptions): number;
    /**
     * Measures the width and height of the given text.
     *
     * > **NOTE**
     * >
     * > - Since API version 12, you can use the
     * > [getMeasureUtils](docroot://reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getmeasureutils12) API in
     * > [UIContext]{@link @ohos.arkui.UIContext} to obtain the [MeasureUtils]{@link @ohos.arkui.UIContext} object
     * > associated with the current UI context.
     *
     * @param { MeasureOptions } options - Information about the measured text.
     * @returns { SizeOptions } Layout width and height occupied by the text.
     *     <br>**NOTE**
     *     <br>The return values for text width and height are both in px.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform [since 11]
     * @atomicservice [since 12]
     * @since 10
     * @deprecated since 18
     * @useinstead ohos.arkui.UIContext.MeasureUtils#measureTextSize
     */
    static measureTextSize(options: MeasureOptions): SizeOptions;
}

```
