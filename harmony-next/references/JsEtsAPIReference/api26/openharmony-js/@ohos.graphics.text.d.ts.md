# @ohos.graphics.text.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2024 Huawei Device Co., Ltd.
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
 * @kit ArkGraphics2D
 */
import type drawing from './@ohos.graphics.drawing';
import type common2D from './@ohos.graphics.common2D';
/**
 * The Text module provides a set of APIs for text layout and font management. It aims to deliver high-quality
 * typesetting through features like character-to-glyph conversion, kerning, line breaking, alignment, and text
 * measurement. Additionally, it provides font management capabilities, including font registration, font descriptors,
 * and font collection management.
 *
 * This module provides the following classes for creating complex text paragraphs:
 *
 * - [TextStyle]{@link text.TextStyle}: defines the font type, size, spacing, and other text properties.
 * - [FontCollection]{@link text.FontCollection}: manages a collection of different fonts.
 * - [FontDescriptor]{@link text.FontDescriptor}: provides information about font descriptors.
 * - [ParagraphStyle]{@link text.ParagraphStyle}: controls line break and word break strategies for the entire
 * paragraph.
 * - [ParagraphBuilder]{@link text.ParagraphBuilder}: used to create different paragraph objects.
 * - [Paragraph]{@link text.Paragraph}: created by calling [build()]{@link text.ParagraphBuilder.build} of the
 * **ParagraphBuilder** class.
 * - [LineTypeset]{@link text.LineTypeset}: created by calling
 * [buildLineTypeset()]{@link text.ParagraphBuilder.buildLineTypeset} of the **ParagraphBuilder** class.
 * - [TextLine]{@link text.TextLine}: paragraph text on a line-by-line basis, obtained by calling
 * [getTextLines()]{@link text.Paragraph.getTextLines} of the **Paragraph** class.
 * - [Run]{@link text.Run}: text typesetting unit, obtained by calling
 * [getGlyphRuns()]{@link text.TextLine.getGlyphRuns} of the **TextLine** class.
 *
 * @syscap SystemCapability.Graphics.Drawing
 * @crossplatform [since 24]
 * @form [since 22]
 * @atomicservice [since 22]
 * @since 12
 */
declare namespace text {
    /**
     * Enumerates the text alignment modes.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @atomicservice [since 22]
     * @since 12
     */
    enum TextAlign {
        /**
         * Left-aligned.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        LEFT = 0,
        /**
         * Right-aligned.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        RIGHT = 1,
        /**
         * Center-aligned.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        CENTER = 2,
        /**
         * Justified, which means that each line (except the last line) is stretched so that every line has equal width, and
         * the left and right margins are straight.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        JUSTIFY = 3,
        /**
         * Aligned with the start position, which depends on [TextDirection]{@link text.TextDirection}.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        START = 4,
        /**
         * Aligned with the end position, which depends on [TextDirection]{@link text.TextDirection}.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        END = 5
    }
    /**
     * Enumerates the vertical alignment modes of text.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @atomicservice [since 22]
     * @since 20
     */
    enum TextVerticalAlign {
        /**
         * Aligned to the baseline.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 20
         */
        BASELINE = 0,
        /**
         * Bottom-aligned.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 20
         */
        BOTTOM = 1,
        /**
         * Center-aligned.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 20
         */
        CENTER = 2,
        /**
         * Top-aligned.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 20
         */
        TOP = 3
    }
    /**
     * Enumerates the text directions.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @atomicservice [since 22]
     * @since 12
     */
    enum TextDirection {
        /**
         * Right to left (RTL).
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        RTL = 0,
        /**
         * Left to right (LTR).
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        LTR = 1
    }
    /**
     * Enumerates the text break strategies.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @atomicservice [since 22]
     * @since 12
     */
    enum BreakStrategy {
        /**
         * Fills the current line as much as possible without adding hyphens.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        GREEDY = 0,
        /**
         * Optimizes layout and may add hyphens when necessary.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        HIGH_QUALITY = 1,
        /**
         * Ensures consistent line width in a paragraph, adding hyphens if needed.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        BALANCED = 2
    }
    /**
     * Enumerates the word break types.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @atomicservice [since 22]
     * @since 12
     */
    enum WordBreak {
        /**
         * Default mode that break words based on language-specific conventions.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        NORMAL = 0,
        /**
         * Allows breaks within any character in non-CJK text. (CJK means Chinese, Japanese, and Korean.) This value is
         * suitable for Asian text that contains some non-Asian text. For example, it can be used to break consecutive
         * English characters.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        BREAK_ALL = 1,
        /**
         * For non-CJK text, breaks lines between any two characters. If a line contains break points (such as whitespace
         * characters), the line breaks at the break points first to keep words intact. If the entire line has no break
         * points, the line breaks between any two characters. For CJK text, this strategy behaves the same as NORMAL.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        BREAK_WORD = 2,
        /**
         * Attempts to break words at the end of a line using a hyphen. If a hyphen cannot be added, it behaves like
         * **BREAK_WORD**.
         *
         * When using this word break strategy, you need to use the `locale` attribute in [TextStyle]{@link text.TextStyle}
         * to define the language environment, which affects the word break effect.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 18
         */
        BREAK_HYPHEN = 3
    }
    /**
     * Describes a text decoration.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @atomicservice [since 22]
     * @since 12
     */
    interface Decoration {
        /**
         * Type of the decoration. The default value is **NONE**.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        textDecoration?: TextDecorationType;
        /**
         * Color of the decoration. The default value is the text color.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        color?: common2D.Color;
        /**
         * Style of the decoration. The default value is **SOLID**.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        decorationStyle?: TextDecorationStyle;
        /**
         * Scale factor for the thickness of the decoration line. The value is a floating point number. The default value is
         * **1.0**. If the value is less than or equal to 0, no decoration line is drawn.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        decorationThicknessScale?: number;
    }
    /**
     * Enumerates the text decoration types.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @atomicservice [since 22]
     * @since 12
     */
    enum TextDecorationType {
        /**
         * No decoration is used.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        NONE = 0,
        /**
         * An underline is used for decoration.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        UNDERLINE = 1,
        /**
         * An overline is used for decoration.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        OVERLINE = 2,
        /**
         * A strikethrough is used for decoration.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        LINE_THROUGH = 4
    }
    /**
     * Enumerates the text decoration styles.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @atomicservice [since 22]
     * @since 12
     */
    enum TextDecorationStyle {
        /**
         * Solid style.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        SOLID = 0,
        /**
         * Double style.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        DOUBLE = 1,
        /**
         * Dotted style.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        DOTTED = 2,
        /**
         * Dashed style.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        DASHED = 3,
        /**
         * Wavy style.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        WAVY = 4
    }
    /**
     * Enumerates the font weights.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @atomicservice [since 22]
     * @since 12
     */
    enum FontWeight {
        /**
         * Font weight W100.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        W100 = 0,
        /**
         * Font weight W200.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        W200 = 1,
        /**
         * Font weight W300.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        W300 = 2,
        /**
         * Font weight W400.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        W400 = 3,
        /**
         * Font weight W500.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        W500 = 4,
        /**
         * Font weight W600.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        W600 = 5,
        /**
         * Font weight W700.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        W700 = 6,
        /**
         * Font weight W800.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        W800 = 7,
        /**
         * Font weight W900.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        W900 = 8
    }
    /**
     * Enumerates the font styles.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @atomicservice [since 22]
     * @since 12
     */
    enum FontStyle {
        /**
         * Normal.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        NORMAL = 0,
        /**
         * Italic. If no italic version is available for the current font, the oblique version will be used instead.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        ITALIC = 1,
        /**
         * Oblique. If no oblique version is available for the current font, the italic version will be used instead.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        OBLIQUE = 2
    }
    /**
     * Enumerates the font widths.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @atomicservice [since 22]
     * @since 12
     */
    enum FontWidth {
        /**
         * Ultra condensed.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        ULTRA_CONDENSED = 1,
        /**
         * Extra condensed.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        EXTRA_CONDENSED = 2,
        /**
         * Condensed.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        CONDENSED = 3,
        /**
         * Semi condensed.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        SEMI_CONDENSED = 4,
        /**
         * Normal.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        NORMAL = 5,
        /**
         * Semi expanded.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        SEMI_EXPANDED = 6,
        /**
         * Expanded.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        EXPANDED = 7,
        /**
         * Extra expanded.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        EXTRA_EXPANDED = 8,
        /**
         * Ultra expanded.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        ULTRA_EXPANDED = 9
    }
    /**
     * Enumerates the text height modifier patterns.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @atomicservice [since 22]
     * @since 12
     */
    enum TextHeightBehavior {
        /**
         * Allows the first line of the paragraph to rise and the last line to drop.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        ALL = 0x0,
        /**
         * Prevents the first line of a paragraph from rising.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        DISABLE_FIRST_ASCENT = 0x1,
        /**
         * Prevents the last line of a paragraph from dropping.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        DISABLE_LAST_ASCENT = 0x2,
        /**
         * Prevents the first line of the paragraph to rise and the last line to drop.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        DISABLE_ALL = 0x1 | 0x2
    }
    /**
     * Enumerates the text baseline types.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @atomicservice [since 22]
     * @since 12
     */
    enum TextBaseline {
        /**
         * Alphabetic baseline, where the letters in Latin alphabets sit on.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        ALPHABETIC = 0,
        /**
         * Ideographic baseline, where the baseline is at the bottom of the text area. It is usually used for CJK text.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        IDEOGRAPHIC = 1
    }
    /**
     * Enumerates the ellipsis styles.
     *
     * **EllipsisMode.START** and **EllipsisMode.MIDDLE** take effect only when text overflows in a single line.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @atomicservice [since 22]
     * @since 12
     */
    enum EllipsisMode {
        /**
         * Ellipsis at the beginning. This enumerated value is valid only when **maxLines** is set to **1** in
         * [ParagraphStyle]{@link text.ParagraphStyle}.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        START = 0,
        /**
         * Ellipsis in the middle. This enumerated value is valid only when **maxLines** is set to **1** in
         * [ParagraphStyle]{@link text.ParagraphStyle}.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        MIDDLE = 1,
        /**
         * Ellipsis at the end. This enumerated value is valid when **maxLines** is set to any value in
         * [ParagraphStyle]{@link text.ParagraphStyle}.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        END = 2,
        /**
         * Ellipsis at the beginning. This enumerated value is valid when **maxLines** is set to any value in
         * [ParagraphStyle]{@link text.ParagraphStyle}.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @atomicservice
         * @since 24
         */
        MULTILINE_START = 3,
        /**
         * Ellipsis in the middle. This enumerated value is valid when **maxLines** is set to any value in
         * [ParagraphStyle]{@link text.ParagraphStyle}.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @atomicservice
         * @since 24
         */
        MULTILINE_MIDDLE = 4
    }
    /**
     * Represents a text shadow.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @atomicservice [since 22]
     * @since 12
     */
    interface TextShadow {
        /**
         * Color of the text shadow. The default value is black Color(255, 0, 0, 0).
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        color?: common2D.Color;
        /**
         * Offset position of the text shadow relative to the current text. The horizontal and vertical coordinates must be
         * greater than or equal to 0, in physical pixels (px). The default value is common2D.Point(0, 0).
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        point?: common2D.Point;
        /**
         * Blur radius, a floating-point value in physical pixels (px), with a default value of **0.0**.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        blurRadius?: number;
    }
    /**
     * Describes the style of a rectangle.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @atomicservice [since 22]
     * @since 12
     */
    interface RectStyle {
        /**
         * Color of the rectangle.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        color: common2D.Color;
        /**
         * Upper left radius of the rectangle, in physical pixels (px).
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        leftTopRadius: number;
        /**
         * Upper right radius of the rectangle, in physical pixels (px).
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        rightTopRadius: number;
        /**
         * Lower right radius of the rectangle, in physical pixels (px).
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        rightBottomRadius: number;
        /**
         * Lower left radius of the rectangle, in physical pixels (px).
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        leftBottomRadius: number;
    }
    /**
     * Enumerates the line height scaling base.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @atomicservice [since 22]
     * @since 21
     */
    enum LineHeightStyle {
        /**
         * Uses the font size as the scaling base. The line height is calculated as follows:
         * [TextStyle]{@link text.TextStyle}.fontSize * [TextStyle]{@link text.TextStyle}.heightScale.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @atomicservice [since 22]
         * @since 21
         */
        FONT_SIZE = 0,
        /**
         * Uses the font height as the scaling base. The line height is calculated as follows: the height of the shaped
         * glyph * [TextStyle]{@link text.TextStyle}.heightScale.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @atomicservice [since 22]
         * @since 21
         */
        FONT_HEIGHT = 1
    }
    /**
     * Describes a font feature.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @atomicservice [since 22]
     * @since 12
     */
    interface FontFeature {
        /**
         * Keyword identifier in the font feature key-value pair, such as 'liga' (standard ligature), 'kern' (kerning
         * adjustment), etc.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        name: string;
        /**
         * Value in the font feature key-value pair.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        value: number;
    }
    /**
     * Describes a font variation.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @atomicservice [since 22]
     * @since 12
     */
    interface FontVariation {
        /**
         * Keyword identifier in the variable font property key-value pair, such as 'wght' (weight), 'wdth' (width), and '
         * ital' (italic).
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        axis: string;
        /**
         * Value in the font variation key-value pair.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        value: number;
        /**
         * Whether to normalize. If the value is **true**, the value range of the value field is -1 to 1, which maps the
         * minimum value to the maximum value configured in the font file. The value **0** indicates the default value
         * configured in the font file. If the value is **false**, the value range of the value field is the adjustable
         * range supported by the font file itself. The default value is **false**.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @atomicservice
         * @since 24
         */
        isNormalized?: boolean;
    }
    /**
     * Enumerates the text badges.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @atomicservice [since 22]
     * @since 20
     */
    enum TextBadgeType {
        /**
         * Disables the superscript and subscript.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 20
         */
        TEXT_BADGE_NONE = 0,
        /**
         * Enables the superscript.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 20
         */
        TEXT_SUPERSCRIPT = 1,
        /**
         * Enables the subscript.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 20
         */
        TEXT_SUBSCRIPT = 2
    }
    /**
     * Represents a text style, which controls the visual appearance attributes of text, including font, color, font size,
     * spacing, decoration lines, and shadows. TextStyle is applied to subsequently added text content through the
     * [pushStyle]{@link text.ParagraphBuilder.pushStyle} method of [ParagraphBuilder]{@link text.ParagraphBuilder}, and
     * works together with [ParagraphStyle]{@link text.ParagraphStyle} (which controls paragraph-level attributes). Within
     * the same paragraph, you can call pushStyle multiple times to apply different styles to different text segments.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @atomicservice [since 22]
     * @since 12
     */
    interface TextStyle {
        /**
         * Text decoration. By default, no decoration is used.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        decoration?: Decoration;
        /**
         * Text color. The default color is white.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        color?: common2D.Color;
        /**
         * Font weight. The default value is W400. Before <!--RP1-->OpenHarmony 6.1<!--RP1End-->, only variable fonts in
         * system fonts support font weight adjustment. Since <!--RP1-->OpenHarmony 6.1<!--RP1End-->, variable fonts in both
         * system fonts and third-party registered fonts support font weight adjustment. For non-variable fonts, setting a
         * font weight value less than semi-bold (W600) results in no change in font thickness, while setting a font weight
         * value greater than or equal to semi-bold (W600) may trigger a pseudo-bold effect.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        fontWeight?: FontWeight;
        /**
         * Font style. The default value is **NORMAL**.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        fontStyle?: FontStyle;
        /**
         * Text baseline type. The default value is **ALPHABETIC**.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        baseline?: TextBaseline;
        /**
         * List of font family names. The default value is empty, which matches the system font. When using a custom font,
         * specify the name used when loading the font in this list. When set together with fontTypefaces, fontTypefaces
         * takes precedence and fontFamilies does not take effect.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        fontFamilies?: Array<string>;
        /**
         * Font size, a floating-point value with a default value of **14.0**, measured in physical pixels (px).
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        fontSize?: number;
        /**
         * Character spacing, a floating-point value in physical pixels (px) with a default value of **0.0**. A positive
         * value widens the character gap, while a negative value narrows it.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        letterSpacing?: number;
        /**
         * Word spacing, a floating-point value in physical pixels (px) with a default value of **0.0**.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        wordSpacing?: number;
        /**
         * Maximum line height, in physical pixels (px). If the line height is scaled, the maximum line height takes effect
         * when [TextStyle]{@link text.TextStyle}.heightScale is greater than 0. The value is a positive floating point
         * number. The default value is **Number.MAX_VALUE**.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @atomicservice [since 22]
         * @since 21
         */
        lineHeightMaximum?: number;
        /**
         * Minimum line height, in physical pixels (px). If the line height is scaled, the minimum line height takes effect
         * when [TextStyle]{@link text.TextStyle}.heightScale is greater than 0. The value is a non-negative floating point
         * number. The default value is **0**.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @atomicservice [since 22]
         * @since 21
         */
        lineHeightMinimum?: number;
        /**
         * Scaling base style of the line height. The default value is **FONT_SIZE**.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @atomicservice [since 22]
         * @since 21
         */
        lineHeightStyle?: LineHeightStyle;
        /**
         * Scale factor of the line height. The value is a floating point number. The default value is **1.0**. This
         * parameter is valid only when **heightOnly** is set to** true**.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        heightScale?: number;
        /**
         * Whether half leading is enabled. Half leading is the leading split in half and applied equally to the top and
         * bottom edges. The value **true** means that half leading is enabled, and **false** means the opposite. The
         * default value is **false**.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        halfLeading?: boolean;
        /**
         * The value **true** means the text box height is set based on the font size and heightScale, and **false** means
         * the text box height is set based on the line height and line spacing. The default value is **false**.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        heightOnly?: boolean;
        /**
         * Ellipsis text. When the ellipsis takes effect, this field value replaces the ellipsis portion. The default value
         * is an empty string, which uses the system default ellipsis … (U+2026). When configured together with the tab
         * attribute of ParagraphStyle, the tab attribute does not take effect.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        ellipsis?: string;
        /**
         * Ellipsis type. The default value is **END**, indicating that the ellipsis is at the end of a line.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        ellipsisMode?: EllipsisMode;
        /**
         * Language type. For example, **'en-Latn'** indicates English (Latin script), **'zh-Hans'** indicates Simplified
         * Chinese, and **'zh-Hant'** indicates Traditional Chinese. Supports two-segment language tags in the language-
         * script format, where language complies with the ISO 639-1 standard and script complies with the ISO 15924
         * standard. If the locale is not specified, set to an empty string, or set to **undefined**, the default locale is
         * **'zh-Hans'**.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        locale?: string;
        /**
         * Vertical offset distance of the text baseline, in physical pixels (px). The default value is **0.0**.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        baselineShift?: number;
        /**
         * Array of text font features. Pass this parameter when you need to enable or disable specific font features (such
         * as ligatures, kerning adjustment, etc.).
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        fontFeatures?: Array<FontFeature>;
        /**
         * Array of text shadows. Pass this parameter when you need to add shadow effects to text.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        textShadows?: Array<TextShadow>;
        /**
         * Text rectangle style. Pass this parameter when you need to add a background rectangle to text (such as setting
         * the background color, rounded corners, etc.).
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        backgroundRect?: RectStyle;
        /**
         * Array of variable font properties. Pass this parameter when you need to adjust the variable axis parameters of a
         * variable font (such as the font weight axis, font width axis, etc.).
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        fontVariations?: Array<FontVariation>;
        /**
         * Sets whether to use superscript or subscript in text layout. **TEXT_SUPERSCRIPT** indicates that superscript is
         * enabled, and **TEXT_SUBSCRIPT** indicates that subscript is enabled. The default value is **TEXT_BADGE_NONE**,
         * indicating that neither superscript nor subscript is enabled.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 20
         */
        badgeType?: TextBadgeType;
        /**
         * Font width. The default value is **NORMAL**.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @atomicservice [since 22]
         * @since 21
         */
        fontWidth?: FontWidth;
        /**
         * Edge processing mode for drawing texts. The default value is **ANTI_ALIAS**.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        fontEdging?: drawing.FontEdging;
        /**
         * Array of specified typesetting font objects, used to prioritize the specified font objects for text shaping and
         * skip the font matching process. When a font object in the array cannot shape some characters, the unshaped
         * characters will be shaped using the system font. The default value is an empty array, indicating that no font
         * object is specified and the default font matching process is used.
         *
         * When fontTypefaces is set together with [TextStyle]{@link text.TextStyle}.fontFamilies, fontTypefaces takes
         * precedence.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        fontTypefaces?: Array<drawing.Typeface>;
    }
    /**
     * Represents a font collection, which manages the font resources required for text typesetting. FontCollection
     * provides font matching and glyph lookup capabilities for [ParagraphBuilder]{@link text.ParagraphBuilder}, and
     * serves as a fundamental component of the text typesetting pipeline. It provides a global instance (
     * [getGlobalInstance]{@link text.FontCollection.getGlobalInstance}) and local instances (
     * [getLocalInstance]{@link text.FontCollection.getLocalInstance}). Fonts loaded by the global instance are shared
     * within the app, making it suitable for common app scenarios. Local instances are independent of each other, and
     * fonts loaded by a local instance take effect only for that instance without affecting others, making them
     * recommended for widget scenarios. Custom fonts can be loaded through
     * [loadFontSync]{@link text.FontCollection.loadFontSync} or [loadFont]{@link text.FontCollection.loadFont}.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @form [since 22]
     * @atomicservice [since 22]
     * @since 12
     */
    class FontCollection {
        /**
         * Obtains a global **FontCollection** instance.
         *
         * @returns { FontCollection } Global FontCollection instance object of the app, which can be used to manage font
         *     loading, unloading, typesetting, and other operations.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        static getGlobalInstance(): FontCollection;
        /**
         * Obtains the local **FontCollection** instance. This API is recommended for widgets.
         *
         * @returns { FontCollection } Local FontCollection instance object, recommended for widget scenarios. It can be
         *     used to manage font loading, unloading, and typesetting operations.
         * @static
         * @syscap SystemCapability.Graphics.Drawing
         * @form
         * @atomicservice
         * @since 22
         */
        static getLocalInstance(): FontCollection;
        /**
         * Loads a custom font. This API returns the result synchronously. In this API, **name** specifies the alias of the
         * font, and the custom font effect can be displayed only when the value of **name** is set in **fontFamilies** in
         * **[TextStyle]{@link text.TextStyle}**. The supported font file formats are TTF and OTF.
         *
         * @param { string } name - Name of the font to be called after the font is loaded.
         * @param { string | Resource } path - Path of the font file to be imported. The path must be in the format of "
         *     **file://** + Absolute path of the font file" or **$rawfile** (a file path relative to the
         *     **resources/rawfile** directory in the project, which includes the font file name).
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @form [since 22]
         * @atomicservice [since 22]
         * @since 12
         */
        loadFontSync(name: string, path: string | Resource): void;
        /**
         * Loads the custom font. This API uses a promise to return the result. In this API, **name** specifies the alias of
         * the font, and the custom font effect can be displayed only when the value of **name** is set in **fontFamilies**
         * in **[TextStyle]{@link text.TextStyle}**. The supported font file formats are TTF and OTF.
         *
         * @param { string } name - Name of the font. Any string is acceptable.
         * @param { string | Resource } path - Path of the font file to be loaded. The path must be in the format of "
         *     **file://** + Absolute path of the font file" or **$rawfile** (a file path relative to the
         *     **resources/rawfile** directory in the project, which includes the font file name).
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @form [since 22]
         * @atomicservice [since 22]
         * @since 18
         */
        loadFont(name: string, path: string | Resource): Promise<void>;
        /**
         * Loads a custom font. This API returns the result synchronously. In this API, **name** specifies the alias of the
         * font, and the custom font effect can be displayed only when the value of **name** is set in **fontFamilies** in
         * **[TextStyle]{@link text.TextStyle}**. The supported font file formats are TTF, OTF, and TTC.
         *
         * @param { string } name - Name of the font. Any string is acceptable.
         * @param { string | Resource } path - Path of the font file to load. Two formats are supported: "file:// + absolute
         *     path of the font file" or $rawfile('font file path').
         * @param { number } [index] - Font index to be loaded when the font file format is TTC. The default value is **0**,
         *     indicating that the first font of the TTC file is loaded.
         *     <br>The index value of a non-TTC file is meaningless. If an index is specified, the value can only be **0**.
         * @throws { BusinessError } 25900001 - Parameter error.
         * @throws { BusinessError } 25900002 - File not found.
         * @throws { BusinessError } 25900003 - Failed to open the file.
         * @throws { BusinessError } 25900004 - File seek failed.
         * @throws { BusinessError } 25900005 - Failed to get the file size.
         * @throws { BusinessError } 25900006 - Failed to read the file.
         * @throws { BusinessError } 25900007 - Empty file.
         * @throws { BusinessError } 25900008 - Corrupted file.
         * @syscap SystemCapability.Graphics.Drawing
         * @form
         * @atomicservice
         * @since 23
         */
        loadFontSyncWithCheck(name: string, path: string | Resource, index?: number): void;
        /**
         * Loads a custom font. This API uses a promise to return the result. In this API, **name** specifies the alias of
         * the font, and the custom font effect can be displayed only when the value of **name** is set in **fontFamilies**
         * in **[TextStyle]{@link text.TextStyle}**. The supported font file formats are TTF, OTF, and TTC.
         *
         * @param { string } name - Name of the font. Any string is acceptable.
         * @param { string | Resource } path - Path of the font file to load. Two formats are supported: "file:// + absolute
         *     path of the font file" or $rawfile('font file path').
         * @param { number } [index] - Font index to be loaded when the font file format is TTC. The default value is **0**,
         *     indicating that the first font of the TTC file is loaded.
         *     <br>The index value of a non-TTC file is meaningless. If an index is specified, the value can only be **0**.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 25900001 - Parameter error.
         * @throws { BusinessError } 25900002 - File not found.
         * @throws { BusinessError } 25900003 - Failed to open the file.
         * @throws { BusinessError } 25900004 - File seek failed.
         * @throws { BusinessError } 25900005 - Failed to get the file size.
         * @throws { BusinessError } 25900006 - Failed to read the file.
         * @throws { BusinessError } 25900007 - Empty file.
         * @throws { BusinessError } 25900008 - Corrupted file.
         * @syscap SystemCapability.Graphics.Drawing
         * @form
         * @atomicservice
         * @since 23
         */
        loadFontWithCheck(name: string, path: string | Resource, index?: number): Promise<void>;
        /**
         * Uninstalls a specified custom font. This API is synchronous.
         *
         * After this API is called to unload a custom font corresponding to a font alias, the custom font is no longer
         * available.
         *
         * All layout objects that use the font alias must be destroyed and recreated.
         *
         * - Unloading a non-existent font alias does not produce any effect and does not throw an error.
         * - This operation only affects future font usage.
         * - Unloading a font that is currently in use may lead to text rendering exceptions (such as garbled characters or
         * missing glyphs).
         *
         * @param { string } name - Font alias to be unregistered, which is the same as the alias used for loading the font.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @form [since 22]
         * @atomicservice [since 22]
         * @since 20
         */
        unloadFontSync(name: string): void;
        /**
         * Uninstalls a specified custom font. This API uses a promise to return the result.
         *
         * After this API is called to unload a custom font corresponding to a font alias, the custom font is no longer
         * available.
         *
         * All layout objects that use the font alias must be destroyed and recreated.
         *
         * - Unloading a non-existent font alias does not produce any effect and does not throw an error.
         * - This operation only affects future font usage.
         * - Unloading a font that is currently in use may lead to text rendering exceptions (such as garbled characters or
         * missing glyphs).
         *
         * @param { string } name - Alias of the font to be uninstalled, which is the same as the alias used when the font
         *     is loaded.
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @form [since 22]
         * @atomicservice [since 22]
         * @since 20
         */
        unloadFont(name: string): Promise<void>;
        /**
         * Clears the font typesetting cache. The font typesetting cache has a memory limit and an automatic clearing
         * mechanism. It occupies limited memory. You are not advised to clear it unless there are special memory
         * requirements.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @form [since 22]
         * @atomicservice [since 22]
         * @since 12
         */
        clearCaches(): void;
        /**
         * Sets whether to enable the typesetting paragraph caching. Typesetting paragraph caching can accelerate the
         * typesetting of repeated text, but it will occupy extra memory. Before this API is called, the system enables
         * typesetting paragraph caching by default.
         *
         * @param { boolean } enable - Whether to enable the typesetting paragraph caching. **true** to enable; **false**
         *     otherwise.
         * @syscap SystemCapability.Graphics.Drawing
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        setParagraphCachesEnabled(enable: boolean): void;
    }
    /**
     * Describes the strut style, which determines the line spacing, baseline alignment mode, and other properties related
     * to the line height when drawing texts. The strut style is disabled by default.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @atomicservice [since 22]
     * @since 12
     */
    interface StrutStyle {
        /**
         * Array of font families. By default, the array is empty, indicating that all system fonts are matched.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        fontFamilies?: Array<string>;
        /**
         * Font style. The default value is **NORMAL**.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        fontStyle?: FontStyle;
        /**
         * Font width. The default value is **NORMAL**.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        fontWidth?: FontWidth;
        /**
         * Font weight. The default value is **W400**. Before <!--RP1-->OpenHarmony 6.1<!--RP1End-->, only variable fonts in
         * system fonts support font weight adjustment. Since <!--RP1-->OpenHarmony 6.1<!--RP1End-->, both system fonts and
         * variable fonts in third-party registered fonts support font weight adjustment. For non-variable fonts, the font
         * thickness does not change when the font weight value is set to less than **W600**, and a faux bold effect may be
         * triggered when the font weight value is set to **W600** or greater.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        fontWeight?: FontWeight;
        /**
         * Font size, a floating-point value with a default value of **14.0**, measured in physical pixels (px).
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        fontSize?: number;
        /**
         * Scale factor of the line height. The value is a floating point number. The default value is **1.0**.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        height?: number;
        /**
         * Custom line spacing applied to the strut, a floating-point value in physical pixels (px), with a default value of
         * **-1.0**.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        leading?: number;
        /**
         * Whether to forcibly use the strut height for all lines. The value **true** means to forcibly use the strut height
         * for all lines, and **false** means the opposite. The default value is **false**.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        forceHeight?: boolean;
        /**
         * Whether to enable the strut style. The value **true** means to enable the strut style, and **false** means the
         * opposite. The default value is **false**.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        enabled?: boolean;
        /**
         * Whether to override the height. The value **true** means to override the height, and **false** means the
         * opposite. The default value is **false**.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        heightOverride?: boolean;
        /**
         * Whether half leading is enabled. Half leading is the leading split in half and applied equally to the top and
         * bottom edges. The value **true** means that half leading is enabled, and **false** means the opposite. The
         * default value is **false**.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        halfLeading?: boolean;
    }
    /**
     * Represents a paragraph style, which controls the overall layout behavior of a paragraph, including attributes such
     * as alignment, line break strategy, and maximum number of lines. ParagraphStyle serves as a required parameter of
     * the [ParagraphBuilder]{@link text.ParagraphBuilder} constructor, and works together with
     * [TextStyle]{@link text.TextStyle} (which controls text-level styles) to determine the final typesetting result of
     * the paragraph.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @atomicservice [since 22]
     * @since 12
     */
    interface ParagraphStyle {
        /**
         * Text style applied to the paragraph. The default value is the initial text style.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        textStyle?: TextStyle;
        /**
         * Text direction. The default value is **LTR**.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        textDirection?: TextDirection;
        /**
         * Text alignment mode. The default value is **START**. This parameter is invalid when the **tab** parameter is
         * configured.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        align?: TextAlign;
        /**
         * Word break type. The default value is **BREAK_WORD**.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        wordBreak?: WordBreak;
        /**
         * Maximum number of lines. The value is an integer. The default value is **1e9**.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        maxLines?: number;
        /**
         * Text break strategy. The default value is **GREEDY**.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        breakStrategy?: BreakStrategy;
        /**
         * Strut style. The default value is the initial **StrutStyle** object.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        strutStyle?: StrutStyle;
        /**
         * Text height modifier pattern. The default value is **ALL**.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        textHeightBehavior?: TextHeightBehavior;
        /**
         * Alignment mode and position of the text after the tab character in a paragraph. By default, the tab character is
         * replaced with a space. This parameter is invalid when it is used together with the **align** parameter or the
         * **ellipsis** parameter in [TextStyle]{@link text.TextStyle}.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 18
         */
        tab?: TextTab;
        /**
         * Whether to consider the alignment impact of trailing spaces during text layout. The value **true** indicates that
         * the alignment impact of trailing spaces is ignored, and the value **false** indicates that the alignment impact
         * of trailing spaces is considered. The default value is **false**.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 20
         */
        trailingSpaceOptimized?: boolean;
        /**
         * Sets whether to enable automatic spacing during text typography. **true** indicates that the automatic spacing
         * feature is enabled. In this case, automatic spacing applies between CJK (Chinese, Japanese, and Korean) and
         * Western characters (Latin, Cyrillic, and Greek), between CJK and digits, between CJK and copyright symbols,
         * between copyright symbols and digits, and between copyright symbols and Western characters. **false** (default)
         * indicates that the automatic spacing feature is disabled.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 20
         */
        autoSpace?: boolean;
        /**
         * Text vertical alignment mode. The default value is BASELINE, which means text baseline alignment. This attribute
         * takes effect when line height scaling is enabled (that is, when [TextStyle]{@link text.TextStyle}'s heightScale
         * is set) or when text in different font sizes is mixed in a line (that is, when
         * [TextStyle]{@link text.TextStyle}'s fontSize is set). If there is superscript or subscript text in the line
         * (that is, text with [TextStyle]{@link text.TextStyle}'s badgeType attribute set), the superscript or subscript
         * text participates in vertical alignment in the same way as normal text.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 20
         */
        verticalAlign?: TextVerticalAlign;
        /**
         * Line spacing, in physical pixels (px). The default value is **0**. lineSpacing is not restricted by
         * lineHeightMaximum and lineHeightMinimum in [TextStyle]{@link text.TextStyle}. The last line retains line spacing
         * by default. You can disable line spacing for the last line by setting
         * [ParagraphStyle]{@link text.ParagraphStyle}'s textHeightBehavior to DISABLE_ALL or DISABLE_LAST_ASCENT.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @atomicservice [since 22]
         * @since 21
         */
        lineSpacing?: number;
        /**
         * Sets whether to use punctuation compression at the beginning of a line in text layout. **true** means yes;
         * **false** otherwise. The default value is **false**.
         *
         * **NOTE**
         *
         * 1. The font file must support the ss08 feature in [FontFeature]{@link text.FontFeature}.
         * Otherwise, compression cannot be performed.
         * 2. Only the punctuations within the punctuation compression range at the beginning of a line
         * are in the scope of this feature.
         *
         * Punctuation range at the beginning of a line.
         * | Punctuation| Unicode Code Point| Unicode Name|
         * |---------|---------|-------------|
         * | 「| U+300C | LEFT CORNER BRACKET |
         * | 『| U+300E | LEFT WHITE CORNER BRACKET |
         * | " | U+201C | LEFT DOUBLE QUOTATION MARK |
         * | ' | U+2018 | LEFT SINGLE QUOTATION MARK |
         * | （| U+FF08 | FULLWIDTH LEFT PARENTHESIS |
         * | 《| U+300A | LEFT DOUBLE ANGLE BRACKET |
         * | 〈| U+3008 | LEFT ANGLE BRACKET |
         * | 【| U+3010 | LEFT BLACK LENTICULAR BRACKET |
         * | 〖| U+3016 | LEFT WHITE LENTICULAR BRACKET |
         * | 〔| U+3014 | LEFT TORTOISE SHELL BRACKET |
         * | ［| U+FF3B | FULLWIDTH LEFT SQUARE BRACKET |
         * | ｛| U+FF5B | FULLWIDTH LEFT CURLY BRACKET |
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @atomicservice
         * @since 23
         */
        compressHeadPunctuation?: boolean;
        /**
         * Sets whether to use padding at the beginning and end of a line in text layout. **true** means yes; **false**
         * otherwise. The default value is **false**.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @atomicservice
         * @since 23
         */
        includeFontPadding?: boolean;
        /**
         * Sets whether to enable line height rollback during text layout. If the set line height is less than the actual
         * line height, the line height is rolled back to the actual line height. **true** means yes; **false** otherwise.
         * The default value is **false**.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @atomicservice
         * @since 23
         */
        fallbackLineSpacing?: boolean;
        /**
         * First line indent of the paragraph. The indent value must be greater than or equal to 0, in physical pixels (px).
         * The default value is **0**.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        firstLineHeadIndent?: number;
        /**
         * Array of tail indents. Each element in the array represents the indent value of one line. When the actual number
         * of text lines exceeds the number of elements in the indent array, the indent of the excess lines is the last
         * value in the array. All indent values must be greater than or equal to 0, in physical pixels (px). The default
         * value is an empty array.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        tailIndents?: Array<number>;
        /**
         * Array of head indents. Each element in the array represents the indent value of one line. When the actual number
         * of text lines exceeds the number of elements in the indent array, the indent of the excess lines is the last
         * value in the array. All indent values must be greater than or equal to 0, in physical pixels (px). The default
         * value is an empty array.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        headIndents?: Array<number>;
        /**
         * Whether to enable orphan character optimization during text typesetting. Orphan character optimization improves
         * text layout by handling isolated characters (the first character of the last line of a paragraph) more
         * efficiently. When enabled, it adjusts line break points to avoid isolated characters as much as possible. The
         * orphan character optimization feature takes effect only when [wordBreak]{@link text.WordBreak} is not BREAK_ALL
         * and the locale of the first [TextStyle]{@link text.TextStyle} of the text to be typeset is "zh-Hans" or "zh-Hant"
         * . The value **true** enables orphan character optimization, and **false** disables it. The default value is
         * **false**.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        orphanCharOptimization?: boolean;
        /**
         * Whether to enable end-of-line punctuation hanging during text typesetting. The value **true** enables end-of-line
         * punctuation hanging, allowing a single punctuation mark at the end of a line to exceed the typesetting width
         * without wrapping. The value **false** disables end-of-line punctuation hanging. The default value is **false**.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        punctuationOverflow?: boolean;
    }
    /**
     * Enumerates the vertical alignment modes of a placeholder relative to the surrounding text.
     *
     * ![PlaceholderAlignment.png](docroot://reference/apis-arkgraphics2d/figures/PlaceholderAlignment.png)
     *
     * > **NOTE**
     * >
     * > The figure shows the last three alignment modes. The first three alignment modes are similar in text baseline
     * > alignment, with the comparison reference being the text baseline, indicated by the green line.
     * >
     * > ![Baseline.png](docroot://reference/apis-arkgraphics2d/figures/Baseline.png)
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @atomicservice [since 22]
     * @since 12
     */
    enum PlaceholderAlignment {
        /**
         * Aligns the baseline of the placeholder to the baseline of the text.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        OFFSET_AT_BASELINE = 0,
        /**
         * Aligns the bottom edge of the placeholder to the baseline of the text.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        ABOVE_BASELINE = 1,
        /**
         * Aligns the top edge of the placeholder to the baseline of the text.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        BELOW_BASELINE = 2,
        /**
         * Aligns the top edge of the placeholder to the top edge of the text.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        TOP_OF_ROW_BOX = 3,
        /**
         * Aligns the bottom edge of the placeholder to the bottom edge of the text.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        BOTTOM_OF_ROW_BOX = 4,
        /**
         * Center-aligned.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        CENTER_OF_ROW_BOX = 5,
        /**
         * Aligns with the text baseline.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 20
         */
        FOLLOW_PARAGRAPH = 6
    }
    /**
     * Describes the placeholder style.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @atomicservice [since 22]
     * @since 12
     */
    interface PlaceholderSpan {
        /**
         * Width of the placeholder, in units of px. The value is a floating point number.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        width: number;
        /**
         * Height of the placeholder, in units of px. The value is a floating point number.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        height: number;
        /**
         * Vertical alignment of the placeholder relative to the surrounding text.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        align: PlaceholderAlignment;
        /**
         * Type of the text baseline.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        baseline: TextBaseline;
        /**
         * Offset to the text baseline, in units of px. The value is a floating point number.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        baselineOffset: number;
    }
    /**
     * Describes a left-closed and right-open interval.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @atomicservice [since 22]
     * @since 12
     */
    interface Range {
        /**
         * Index of the leftmost point of the interval. The value is an integer.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        start: number;
        /**
         * Index of the rightmost point of the interval. The value is an integer.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        end: number;
    }
    /**
     * Enumerates the font types, which can be combined through bitwise OR operations.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @atomicservice [since 22]
     * @since 14
     */
    enum SystemFontType {
        /**
         * All font types, including the system font type, style font type, and user-installed font type.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 14
         */
        ALL = 1 << 0,
        /**
         * System font type.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 14
         */
        GENERIC = 1 << 1,
        /**
         * Style font type. The style font type is designed for 2-in-1 devices.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @atomicservice [since 22]
         * @since 14
         */
        STYLISH = 1 << 2,
        /**
         * Font type that has been installed.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @atomicservice [since 22]
         * @since 14
         */
        INSTALLED = 1 << 3,
        /**
         * Custom font type.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 18
         */
        CUSTOMIZED = 1 << 4
    }
    /**
     * Represents the font variable axis information.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @atomicservice
     * @since 24
     */
    interface FontVariationAxis {
        /**
         * Keyword identifier of the font variable axis.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @atomicservice
         * @since 24
         */
        key: string;
        /**
         * Minimum value of the font variable axis.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @atomicservice
         * @since 24
         */
        minValue: number;
        /**
         * Maximum value of the font variable axis.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @atomicservice
         * @since 24
         */
        maxValue: number;
        /**
         * Default value of the font variable axis.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @atomicservice
         * @since 24
         */
        defaultValue: number;
        /**
         * Flag of the font variable axis, which is used to indicate whether a variable axis should be hidden from users.
         * The value can be **0** or **1**. The value **0** indicates that the axis is visible to users, and the value **1**
         * indicates that the axis should be hidden.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @atomicservice
         * @since 24
         */
        flags: number;
        /**
         * English name of the font variable axis.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @atomicservice
         * @since 24
         */
        name: string;
        /**
         * Localized name of the font variable axis, which can be empty.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @atomicservice
         * @since 24
         */
        localName: string;
    }
    /**
     * Font variable instance information, which stores preset variable font style information.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @atomicservice
     * @since 24
     */
    interface FontVariationInstance {
        /**
         * English name of the font variable instance.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @atomicservice
         * @since 24
         */
        name: string;
        /**
         * Localized name of the font variable instance, which can be empty.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @atomicservice
         * @since 24
         */
        localName: string;
        /**
         * Array of font variations.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @atomicservice
         * @since 24
         */
        coordinates: Array<FontVariation>;
    }
    /**
     * Describes the font descriptor information.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @atomicservice [since 22]
     * @since 14
     */
    interface FontDescriptor {
        /**
         * Absolute path of the font. Any string that complies with the system restrictions is acceptable. The default value
         * is an empty string.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 14
         */
        path?: string;
        /**
         * Unique name of the font. Any string is acceptable. The default value is an empty string.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 14
         */
        postScriptName?: string;
        /**
         * Font name. Any string is acceptable. The default value is an empty string.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 14
         */
        fullName?: string;
        /**
         * Family name of the font. Any string is acceptable. The default value is an empty string.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 14
         */
        fontFamily?: string;
        /**
         * Subfamily name of the font. Any string is acceptable. The default value is an empty string.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 14
         */
        fontSubfamily?: string;
        /**
         * Font weight. The default value is **0**.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 14
         */
        weight?: FontWeight;
        /**
         * Font width. The value is an integer ranging from 1 to 9. The default value is **0**.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 14
         */
        width?: number;
        /**
         * Whether the font is italic. The value **0** means that the font is not italic, and **1** means the opposite. The
         * default value is **0**.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 14
         */
        italic?: number;
        /**
         * Whether the font is monospaced. The value **true** means that the font is monospaced, and **false** means the
         * opposite. The default value is **false**.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 14
         */
        monoSpace?: boolean;
        /**
         * Whether the font is symbolic. The value **true** means that the font is symbolic, and **false** means the
         * opposite.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 14
         */
        symbolic?: boolean;
        /**
         * Extracts the unique font ID based on the system language configuration. If the font file does not contain the
         * configuration corresponding to the current language, the information corresponding to **en** is used.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @atomicservice
         * @since 23
         */
        localPostscriptName?: string;
        /**
         * Extracts the full font name based on the system language configuration. If the font file does not contain the
         * configuration corresponding to the current language, the information corresponding to **en** is used.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @atomicservice
         * @since 23
         */
        localFullName?: string;
        /**
         * Extracts the font family name based on the system language configuration. If the font file does not contain the
         * configuration corresponding to the current language, the information corresponding to **en** is used.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @atomicservice
         * @since 23
         */
        localFamilyName?: string;
        /**
         * Extracts the font subfamily name based on the system language configuration. If the font file does not contain
         * the configuration corresponding to the current language, the information corresponding to **en** is used.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @atomicservice
         * @since 23
         */
        localSubFamilyName?: string;
        /**
         * Font version. Any string is acceptable. The default value is an empty string.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @atomicservice
         * @since 23
         */
        version?: string;
        /**
         * Font manufacturer information. Any string is acceptable. The default value is an empty string.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @atomicservice
         * @since 23
         */
        manufacture?: string;
        /**
         * Font copyright information. Any string is acceptable. The default value is an empty string.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @atomicservice
         * @since 23
         */
        copyright?: string;
        /**
         * Font trademark information. Any string is acceptable. The default value is an empty string.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @atomicservice
         * @since 23
         */
        trademark?: string;
        /**
         * Font license information. Any string is acceptable. The default value is an empty string.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @atomicservice
         * @since 23
         */
        license?: string;
        /**
         * Font variable axis record array, which is used to describe the variable axis information supported by the font.
         * For non-variable fonts, this field is **undefined**.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @atomicservice
         * @since 24
         */
        variationAxisRecords?: Array<FontVariationAxis>;
        /**
         * Font variable instance record array, which is used to describe the variable instance information supported by the
         * font. For non-variable fonts, this field is **undefined**.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @atomicservice
         * @since 24
         */
        variationInstanceRecords?: Array<FontVariationInstance>;
        /**
         * Font index. This parameter is valid only when the font file is in TTC format. The value is **0** for the TTF
         * format.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        index?: number;
        /**
         * List of languages supported by the font. The default value is an empty array. Each element in the array is a
         * language tag string in BCP 47 format (such as 'en' and 'zh-Hans'), indicating the writing languages supported by
         * the font.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        languages?: Array<string>;
        /**
         * Array of OpenType feature tags supported by the font. The default value is an empty array. Each element in the
         * array is a feature tag string (such as 'liga' for standard ligatures and 'kern' for kerning adjustment),
         * indicating the font features supported by the font.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        fontFeatures?: Array<string>;
    }
    /**
     * Implements a carrier that stores the text content and style. You can perform operations such as layout and drawing.
     *
     * Before calling any of the following APIs, you must use [build()]{@link text.ParagraphBuilder.build} of the
     * [ParagraphBuilder]{@link text.ParagraphBuilder} class to create a **Paragraph** object.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @atomicservice [since 22]
     * @since 12
     */
    class Paragraph {
        /**
         * Performs layout with the given height and width and calculates the positions of all glyphs.
         *
         * @param { TextRectSize } size - Constrained height and width, in physical pixels (px).
         * @returns { TextLayoutResult } Actual size after layout and character range after typesetting.
         * @syscap SystemCapability.Graphics.Drawing
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        layoutWithConstraints(size: TextRectSize): TextLayoutResult;
        /**
         * Performs layout and calculates the positions of all glyphs.
         *
         * @param { number } width - Maximum width of a single line, in units of px. The value is a floating point number.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        layoutSync(width: number): void;
        /**
         * Performs layout and calculates the positions of all glyphs. This API uses a promise to return the result.
         *
         * @param { number } width - Maximum width of a single line, in units of px. The value is a floating point number.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 18
         */
        layout(width: number): Promise<void>;
        /**
         * Draws text on the canvas with (x, y) as the upper-left corner. You must call
         * [layout()]{@link text.Paragraph.layout} for typesetting before calling this API; otherwise, the text content
         * cannot be displayed correctly.
         *
         * @param { drawing.Canvas } canvas - Target canvas.
         * @param { number } x - Horizontal coordinate of the upper left corner, which is a floating-point value, in
         *     physical pixels (px).
         * @param { number } y - Vertical coordinate of the upper left corner, which is a floating-point value, in physical
         *     pixels (px).
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        paint(canvas: drawing.Canvas, x: number, y: number): void;
        /**
         * Draws text along a path on the canvas. You must call [layout()]{@link text.Paragraph.layout} for typesetting
         * before calling this API; otherwise, the text content cannot be displayed correctly.
         *
         * @param { drawing.Canvas } canvas - Target canvas.
         * @param { drawing.Path } path - Path along which the text is drawn.
         * @param { number } hOffset - Offset along the path direction. Positive values extend forward from the path start
         *     point, and negative values extend backward. Unit: physical pixels (px).
         * @param { number } vOffset - Offset along the vertical direction of the path. Positive values extend to the right
         *     along the path, and negative values extend to the left. Unit: physical pixels (px).
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        paintOnPath(canvas: drawing.Canvas, path: drawing.Path, hOffset: number, vOffset: number): void;
        /**
         * Obtains the maximum width of the line in the text.
         *
         * @returns { number } Maximum line width, in units of px. The value is a floating point number.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        getMaxWidth(): number;
        /**
         * Obtains the total height of the text.
         *
         * @returns { number } Total height, in units of px. The value is a floating point number.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        getHeight(): number;
        /**
         * Obtains the longest line in the text.
         *
         * @returns { number } Longest line, in units of px. The value is a floating point number.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        getLongestLine(): number;
        /**
         * Obtains the width of the longest line, including its indentation, in the text. You are advised to round up the
         * return value. If the text content is empty, **0** is returned.
         *
         * @returns { number } Width of the longest line, including its indentation. The value is a floating point number,
         *     in px.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 13
         */
        getLongestLineWithIndent(): number;
        /**
         * Obtains the minimum intrinsic width of the paragraph.
         *
         * @returns { number } Minimum intrinsic width, in units of px. The value is a floating point number.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        getMinIntrinsicWidth(): number;
        /**
         * Obtains the maximum intrinsic width of the paragraph.
         *
         * @returns { number } Maximum intrinsic width, in units of px. The value is a floating point number.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        getMaxIntrinsicWidth(): number;
        /**
         * Obtains the alphabetic baseline.
         *
         * @returns { number } Alphabetic baseline, in units of px. The value is a floating point number.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        getAlphabeticBaseline(): number;
        /**
         * Obtains the ideographic baseline.
         *
         * @returns { number } Baseline position under ideographic characters, a floating point number in physical pixels (
         *     px).
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        getIdeographicBaseline(): number;
        /**
         * Obtains the rectangles occupied by the characters in the range of the text under the given rectangle width and
         * height.
         *
         * @param { Range } range - Range of the text.
         * @param { RectWidthStyle } widthStyle - Width of the rectangle.
         * @param { RectHeightStyle } heightStyle - Height of the rectangle.
         * @returns { Array<TextBox> } Array holding the rectangles obtained.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        getRectsForRange(range: Range, widthStyle: RectWidthStyle, heightStyle: RectHeightStyle): Array<TextBox>;
        /**
         * Obtains the rectangles occupied by all placeholders in the text.
         *
         * @returns { Array<TextBox> } Array holding the rectangles obtained.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        getRectsForPlaceholders(): Array<TextBox>;
        /**
         * Obtains the position of a glyph closest to the given coordinates.
         *
         * @param { number } x - Horizontal coordinate, which is a floating-point value in physical pixels (px).
         * @param { number } y - Vertical coordinate, which is a floating-point value in physical pixels (px).
         * @returns { PositionWithAffinity } Position of the glyph.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        getGlyphPositionAtCoordinate(x: number, y: number): PositionWithAffinity;
        /**
         * Obtains the range of the word where the glyph with a given offset is located.
         *
         * @param { number } offset - Offset of the glyph. The value is an integer.
         * @returns { Range } Range of the word.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        getWordBoundary(offset: number): Range;
        /**
         * Obtains the number of text lines.
         *
         * @returns { number } Number of text lines. The value is an integer.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        getLineCount(): number;
        /**
         * Obtains the height of a given line.
         *
         * @param { number } line - Index of the text line, which is an integer ranging from 0 to
         *     [getLineCount]{@link text.Paragraph.getLineCount}-1.
         * @returns { number } Line height, in physical pixels (px).
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        getLineHeight(line: number): number;
        /**
         * Obtains the width of a given line.
         *
         * @param { number } line - Text line index, which is an integer ranging from 0 to
         *     [getLineCount]{@link text.Paragraph.getLineCount}-1.
         * @returns { number } Line width, in physical pixels (px).
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        getLineWidth(line: number): number;
        /**
         * Checks whether the number of lines in the paragraph exceeds the maximum.
         *
         * @returns { boolean } Check result. The value **true** means that the number of lines exceeds the maximum, and
         *     **false** means the opposite.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        didExceedMaxLines(): boolean;
        /**
         * Obtains all the text lines.
         *
         * @returns { Array<TextLine> } Array of text lines.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        getTextLines(): Array<TextLine>;
        /**
         * Obtains the actually visible text range in the specified line, excluding any overflow ellipsis.
         *
         * @param { number } lineNumber - Line number of the text range, starting from 0. This API can only be used to obtain
         *     the bounds of existing lines. That is, the line number must start from 0, and the maximum line index is the
         *     number of text lines – 1. The number of text lines can be obtained via the
         *     [getLineCount]{@link text.Paragraph.getLineCount} API.
         * @param { boolean } includeSpaces - Whether spaces are included. The value **true** means that spaces are
         *     contained, and **false** means the opposite.
         * @returns { Range } Text range obtained. If the line index is invalid, **start** and **end** are both **0**.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        getActualTextRange(lineNumber: number, includeSpaces: boolean): Range;
        /**
         * Obtains an array of line measurement information.
         *
         * @returns { Array<LineMetrics> } Array of line measurement information.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        getLineMetrics(): Array<LineMetrics>;
        /**
         * Obtains the line measurement information of a line.
         *
         * @param { number } lineNumber - Number of the line for which metric information is to be queried. Line numbers start
         *     from 0, and the maximum line index is the number of text lines minus 1. The number of text lines can be
         *     obtained through the [getLineCount]{@link text.Paragraph.getLineCount} API.
         * @returns { LineMetrics | undefined } **LineMetrics** object containing the measurement information if the
         *     specified line number is valid and the measurement information exists. If the line number is invalid or the
         *     measurement information cannot be obtained, **undefined** is returned.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        getLineMetrics(lineNumber: number): LineMetrics | undefined;
        /**
         * Updates the color of the entire text span. This API call also updates the decoration color if it hasn't been set
         * yet.
         *
         * @param { common2D.Color } color - Updated font color.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 20
         */
        updateColor(color: common2D.Color): void;
        /**
         * Updates the decoration line of the entire text span.
         *
         * @param { Decoration } decoration - Updated decoration line.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 20
         */
        updateDecoration(decoration: Decoration): void;
        /**
         * Obtains the character range corresponding to the specified glyph range.
         *
         * @param { Range } glyphRange - Glyph range.
         * @param { drawing.TextEncoding } encoding - Text encoding type. Currently, only UTF-8 and UTF-16 encoding types
         *     are supported. For UTF-8 encoding, the returned character range indicates the byte range. For UTF-16
         *     encoding, the returned character range indicates the UTF-16 encoding unit range.
         * @returns { Array<Range> } Character range. If the array contains one element, it indicates the character range.
         *     If the array contains two elements, the first element indicates the character range, and the second element
         *     indicates the actual glyph range.
         * @throws { BusinessError } 25900001 - Parameter error. Possible causes: Incorrect parameter range.
         * @syscap SystemCapability.Graphics.Drawing
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        getCharacterRangeForGlyphRange(glyphRange: Range, encoding: drawing.TextEncoding): Array<Range>;
        /**
         * Obtains the glyph range corresponding to the specified character range.
         *
         * @param { Range } characterRange - Character range.
         * @param { drawing.TextEncoding } encoding - Text encoding type. Currently, only UTF-8 and UTF-16 encoding types
         *     are supported. For UTF-8 encoding, the returned actual character range indicates the byte range. For UTF-16
         *     encoding, the returned actual character range indicates the UTF-16 encoding unit range.
         * @returns { Array<Range> } Glyph range. The array contains two elements. The first element indicates the glyph
         *     range, and the second element indicates the actual character range.
         * @throws { BusinessError } 25900001 - Parameter error. Possible causes: Incorrect parameter range.
         * @syscap SystemCapability.Graphics.Drawing
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        getGlyphRangeForCharacterRange(characterRange: Range, encoding: drawing.TextEncoding): Array<Range>;
        /**
         * Obtains the character position information closest to the given coordinates.
         *
         * @param { number } x - Horizontal coordinate in the text layout area, in physical pixels (px). X offset relative
         *     to the top-left corner of the text layout area, with the right direction as positive. Supports floating-point
         *     values and accepts negative values, which indicate positions to the left of the text layout area. If the
         *     coordinates are beyond the text layout area, the nearest character position is returned. It can be obtained
         *     through a touch event or click event.
         * @param { number } y - Vertical coordinate in the text layout area, in physical pixels (px). Y offset relative to
         *     the top-left corner of the text layout area, with the downward direction as positive. Supports floating-point
         *     values and accepts negative values, which indicate positions above the text layout area. If the coordinates
         *     are beyond the text layout area, the nearest character position is returned. It can be obtained through a
         *     touch event or click event.
         * @param { drawing.TextEncoding } encoding - Text encoding type. Currently, only UTF-8 and UTF-16 encoding types
         *     are supported. For UTF-8 encoding, the returned character position indicates the byte offset. For UTF-16
         *     encoding, the returned character position indicates the UTF-16 encoding unit offset.
         * @returns { PositionWithAffinity } Character position.
         * @throws { BusinessError } 25900001 - Parameter error. Possible causes: Incorrect parameter range.
         * @syscap SystemCapability.Graphics.Drawing
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        getCharacterPositionAtCoordinate(x: number, y: number, encoding: drawing.TextEncoding): PositionWithAffinity;
        /**
         * Obtains the text processing status of a paragraph.
         *
         * @returns { TextProcessState } Text processing status of a paragraph.
         * @syscap SystemCapability.Graphics.Drawing
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        getProcessState(): TextProcessState;
        /**
         * Obtains the text display status of a paragraph.
         *
         * @returns { TextDisplayState } Text display status of a paragraph.
         * @syscap SystemCapability.Graphics.Drawing
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        getTextDisplayState(): TextDisplayState;
        /**
         * Obtains the style configuration of a paragraph.
         *
         * @returns { ParagraphStyle } Style configuration of the paragraph.
         *     <br>The `textStyle.color`, `textStyle.textShadows.color`, `textStyle.backgroundRect.color`, and
         *     `textStyle.decoration.color` properties return a 32-bit unsigned integer color value. Example: The return
         *     value `4278190080` corresponds to the pure black hexadecimal color value `0xFF000000`, which is equivalent to
         *     the [common2D.Color]{@link @ohos.graphics.common2D:common2D.Color} object parameters: alpha=255, red=0, green
         *     =0, blue=0. The example provides the numberToRGBA conversion method as a reference.
         * @syscap SystemCapability.Graphics.Drawing
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        getParagraphStyle(): ParagraphStyle;
        /**
         * Obtains the range of text that is visible on the screen in a paragraph. Excludes text that is not displayed due
         * to truncation by the maximum line count (the maxLines attribute of [ParagraphStyle]{@link text.ParagraphStyle})
         * or replacement in ellipsis mode ([EllipsisMode]{@link text.EllipsisMode}).
         *
         * **NOTE**
         *
         * The returned range depends on the specific truncation of the paragraph
         * (for example, whether the maximum number of lines or ellipsis is set):
         *
         * | Scenario| Description|
         * |---|---|
         * | Text is not truncated.| The range includes all typeset text.|
         * | Only maxLines truncation is set (no ellipsis).| the text from the first line to the end of the maxLines line.|
         * | EllipsisMode.END| The range is the text before the ellipsis.|
         * | EllipsisMode.START| The value is the text after the ellipsis.|
         * | EllipsisMode.MIDDLE| the text range before and after the ellipsis is returned.|
         * | EllipsisMode.MULTILINE_START| the text range before and after the ellipsis is returned.|
         * | EllipsisMode.MULTILINE_MIDDLE| the text range before and after the ellipsis is returned.|
         *
         * @returns { Array<Range> } Array of the visible text range of a paragraph. The range is the index of the UTF-16
         *     encoding unit.
         * @syscap SystemCapability.Graphics.Drawing
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        getVisibleTextRanges(): Array<Range>;
        /**
         * Sets whether to force reuse of the rasterization result. If this API is not called, the system allows updating
         * the rasterization result by default.
         *
         * This API is suitable for scenarios where the text content remains unchanged but
         * [paint]{@link text.Paragraph.paint} needs to be called multiple times for drawing. By reusing the rasterization
         * result, repeated rasterization calculations can be avoided to improve drawing performance. After this setting is
         * applied, it takes effect the next time [paint]{@link text.Paragraph.paint} is called for drawing.
         *
         * @param { boolean } isForce - Whether to force reuse of the rasterization result. The value **true** means to
         *     force reuse of the rasterization result, and **false** means to allow updating the rasterization result.
         * @syscap SystemCapability.Graphics.Drawing
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        forceReuseRasterResult(isForce: boolean): void;
    }
    /**
     * Implements a carrier that stores the text content and style. It can be used to compute layout details for
     * individual lines of text.
     *
     * Before calling any of the following APIs, you must use
     * [buildLineTypeset()]{@link text.ParagraphBuilder.buildLineTypeset} in the
     * [ParagraphBuilder]{@link text.ParagraphBuilder} class to create a **LineTypeset** object.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @atomicservice [since 22]
     * @since 18
     */
    class LineTypeset {
        /**
         * Obtains the number of characters that can fit in the layout from the specified position within a limited width.
         *
         * @param { number } startIndex - Start position (inclusive) for calculation. The value is an integer in the range
         *     [0, total number of text characters). If the parameter is out of range, an exception is thrown.
         * @param { number } width - Layout width. The value is a floating point number greater than 0, in px.
         * @returns { number } Number of characters.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 18
         */
        getLineBreak(startIndex: number, width: number): number;
        /**
         * Generates a text line object based on the specified layout range.
         *
         * @param { number } startIndex - Start position for layout calculation. The value is an integer in the range
         *     [0, total number of text characters).
         * @param { number } count - Number of characters from the specified start position. The value is an integer in the
         *     range [0, total number of text characters). The sum of **startIndex** and **count** cannot be greater than
         *     the total number of text characters. If **count** is **0**, the layout range is
         *     [startIndex, position of the last character in the text]. You can use
         *     [getLineBreak]{@link text.LineTypeset.getLineBreak} to obtain the number of characters that can fit in the
         *     layout.
         * @returns { TextLine } **TextLine** object generated based on the characters in the text range.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 18
         */
        createLine(startIndex: number, count: number): TextLine;
    }
    /**
     * Rectangular area of the text, indicating the rectangular space occupied by the text during layout.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @atomicservice [since 22]
     * @since 12
     */
    interface TextBox {
        /**
         * Rectangular area information, in physical pixels (px).
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        rect: common2D.Rect;
        /**
         * Text direction.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        direction: TextDirection;
    }
    /**
     * Describes the position and affinity of a glyph.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @atomicservice [since 22]
     * @since 12
     */
    interface PositionWithAffinity {
        /**
         * Index of the glyph relative to the paragraph. The value is an integer.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        position: number;
        /**
         * Affinity of the position.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        affinity: Affinity;
    }
    /**
     * Enumerates the rectangle width styles.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @atomicservice [since 22]
     * @since 12
     */
    enum RectWidthStyle {
        /**
         * If **letterSpacing** is not set, the rectangle conforms tightly to the text it contains. However, if
         * **letterSpacing** is set, a gap is introduced between the rectangle and text.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        TIGHT = 0,
        /**
         * The rectangle's width is extended to align with the widest rectangle across all lines.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        MAX = 1
    }
    /**
     * Enumerates the rectangle height styles.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @atomicservice [since 22]
     * @since 12
     */
    enum RectHeightStyle {
        /**
         * Tight style.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        TIGHT = 0,
        /**
         * Extends the height to match the highest rectangle in all lines.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        MAX = 1,
        /**
         * Includes half of the line spacing to both the top and bottom of the rectangle.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        INCLUDE_LINE_SPACE_MIDDLE = 2,
        /**
         * Includes the line spacing to the top of the rectangle.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        INCLUDE_LINE_SPACE_TOP = 3,
        /**
         * Includes the line spacing to the bottom of the rectangle.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        INCLUDE_LINE_SPACE_BOTTOM = 4,
        /**
         * Sets the height according to the strut style.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        STRUT = 5
    }
    /**
     * Enumerates the affinity modes.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @atomicservice [since 22]
     * @since 12
     */
    enum Affinity {
        /**
         * The position has affinity for the upstream side of the text position.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        UPSTREAM = 0,
        /**
         * The position has affinity for the downstream side of the text position.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        DOWNSTREAM = 1
    }
    /**
     * Implements a paragraph builder that uses the builder pattern to construct paragraph objects. Developers initialize
     * ParagraphBuilder by passing [ParagraphStyle]{@link text.ParagraphStyle} and
     * [FontCollection]{@link text.FontCollection} to the constructor, then set the text style through
     * [pushStyle]{@link text.ParagraphBuilder.pushStyle}, add text content through
     * [addText]{@link text.ParagraphBuilder.addText}, and finally call [build()]{@link text.ParagraphBuilder.build} to
     * generate a [Paragraph]{@link text.Paragraph} object for typesetting and drawing.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @atomicservice [since 22]
     * @since 12
     */
    class ParagraphBuilder {
        /**
         * A constructor used to create a **ParagraphBuilder** object.
         *
         * @param { ParagraphStyle } paragraphStyle - Paragraph style.
         * @param { FontCollection } fontCollection - Font collection object that provides font resources required for text
         *     typesetting, used for glyph matching and text rendering during paragraph construction.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        constructor(paragraphStyle: ParagraphStyle, fontCollection: FontCollection);
        /**
         * Applies a new style to the current text blob.
         *
         * > **NOTE**
         * >
         * > When you update the style of the current text blob, all text added afterward will use this new style.
         *
         * @param { TextStyle } textStyle - Text style, which describes various visual attributes of text, such as font,
         *     font size, color, font weight, word spacing, line spacing, decoration (such as underline and strikethrough),
         *     and text shadow.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        pushStyle(textStyle: TextStyle): void;
        /**
         * Restores the previous text style.
         *
         * > **NOTE**
         * >
         * > This method must be called after [pushStyle()]{@link text.ParagraphBuilder.pushStyle}. After it is called,
         * > subsequently added text will use the text style before the pop operation. If the style stack is empty, the
         * > textStyle in [ParagraphStyle]{@link text.ParagraphStyle} will be used as the default style.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        popStyle(): void;
        /**
         * Inserts a text string into the paragraph being built.
         *
         * @param { string } text - Exact text string inserted into the paragraph. If an invalid Unicode character is
         *     provided, it is displayed as �.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        addText(text: string): void;
        /**
         * Inserts a placeholder when building a text paragraph. After insertion, the placeholder occupies the corresponding
         * space in paragraph typesetting according to the specified width, height, and alignment, and affects text line
         * breaking and layout.
         *
         * @param { PlaceholderSpan } placeholderSpan - Placeholder span, which describes the size, alignment, baseline
         *     type, and baseline offset of the placeholder.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        addPlaceholder(placeholderSpan: PlaceholderSpan): void;
        /**
         * Builds a paragraph and generates a paragraph object that can be used for subsequent typesetting and rendering.
         * After build() is called, a new ParagraphBuilder instance must be created to build text again.
         *
         * @returns { Paragraph } **Paragraph** object that can be used for subsequent rendering.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        build(): Paragraph;
        /**
         * Builds a line typesetter and generates a LineTypeset object that can be used for line-by-line typesetting
         * calculation.
         *
         * @returns { LineTypeset } **LineTypeset** object that can be used for subsequent rendering.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 18
         */
        buildLineTypeset(): LineTypeset;
        /**
         * Inserts a symbol into the paragraph being built.
         *
         * @param { number } symbolId - Symbol code to insert. The value is a hexadecimal number in the range 0xF0000-0xF0C97.
         *     For details about the configurable symbol codes (unicode values in the list view), see
         *     [HarmonyOS Symbol](https://developer.huawei.com/consumer/en/design/harmonyos-symbol/).
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        addSymbol(symbolId: number): void;
    }
    /**
     * Describes the typographic boundaries of a text line. These boundaries depend on the typographic font and font size,
     * but not on the characters themselves. For example, for the string " a b " (which has a space before "a" and a space
     * after "b"), the typographic boundaries include the spaces at the beginning and end of the line. Similarly, the
     * strings "j" and "E" have identical typographic boundaries, independent of the characters themselves.
     *
     * > **NOTE**
     * >
     * > The figure shows the text line typesetting parameters: width (the width of the text line including left and right
     * > spaces), ascent (the highest point of the ascent), descent (the lowest point of the descent), leading (line
     * > spacing), top (the highest point of the current line), baseline (the character baseline), bottom (the lowest
     * > point of the current line), and next line top (the highest point of the next line).
     * >
     * > ![Typographic.png](docroot://reference/apis-arkgraphics2d/figures/Typographic.png)
     * >
     * > The figure shows the typesetting boundaries for the string " a b ".
     * >
     * > ![TypographicBounds.png](docroot://reference/apis-arkgraphics2d/figures/TypographicBounds.png)
     * >
     * > The figure shows the typesetting boundaries for the string "j" or "E".
     * >
     * > !
     * > [TypographicBounds-Character.png](docroot://reference/apis-arkgraphics2d/figures/TypographicBounds-Character.png)
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @atomicservice [since 22]
     * @since 18
     */
    interface TypographicBounds {
        /**
         * Ascent height of a text line, which is a floating-point value in physical pixels (px).
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 18
         */
        ascent: number;
        /**
         * Descent height of a text line, which is a floating-point value in physical pixels (px).
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 18
         */
        descent: number;
        /**
         * Leading of a text line, which is a floating-point value in physical pixels (px).
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 18
         */
        leading: number;
        /**
         * Total width of the layout boundary, which is a floating-point value in physical pixels (px).
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 18
         */
        width: number;
    }
    /**
     * Defines the callback used to receive the offset and index of each character in a text line object as its
     * parameters.
     *
     * @param { number } offset - Offset of each character in the text line, which is a floating-point value, in physical
     *     pixels (px).
     * @param { number } index - Index of each character in a text line. The value is an integer.
     * @param { boolean } leadingEdge - Whether the cursor is located at the front of the character. The value **true**
     *     means that the cursor is located at the front of the character, that is, the offset does not contain the
     *     character width. The value **false** means that the cursor is located at the rear of the character, that is,
     *     the offset contains the character width.
     * @returns { boolean } Whether to stop calling the callback. The value **true** means to stop calling the callback,
     *     and **false** means to continue calling the callback.
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @atomicservice [since 22]
     * @since 18
     */
    type CaretOffsetsCallback = (offset: number, index: number, leadingEdge: boolean) => boolean;
    /**
     * Implements a carrier that describes the basic text line structure of a paragraph.
     *
     * Before calling any of the following APIs, you must use [getTextLines()]{@link text.Paragraph.getTextLines} of the
     * [Paragraph]{@link text.Paragraph} class or [createLine()]{@link text.LineTypeset.createLine} of the
     * [LineTypeset]{@link text.LineTypeset} class to create a **TextLine** object.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @atomicservice [since 22]
     * @since 12
     */
    class TextLine {
        /**
         * Obtains the number of glyphs in this text line.
         *
         * @returns { number } Number of glyphs. The value is an integer.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        getGlyphCount(): number;
        /**
         * Obtains the range of the text in this text line in the entire paragraph.
         *
         * @returns { Range } Range of the text in this text line in the entire paragraph.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        getTextRange(): Range;
        /**
         * Obtains the array of glyph runs in the text line.
         *
         * @returns { Array<Run> } Array of the runs obtained.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        getGlyphRuns(): Array<Run>;
        /**
         * Paints this text line on the canvas with the coordinate point (x, y) as the upper left corner.
         *
         * @param { drawing.Canvas } canvas - Target canvas.
         * @param { number } x - Horizontal coordinate of the upper left corner, which is a floating-point value, in
         *     physical pixels (px).
         * @param { number } y - Vertical coordinate of the upper left corner, which is a floating-point value, in physical
         *     pixels (px).
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        paint(canvas: drawing.Canvas, x: number, y: number): void;
        /**
         * Creates a truncated text line object.
         *
         * @param { number } width - Line width after truncation, which is a floating-point value in physical pixels (px).
         * @param { EllipsisMode } ellipsisMode - Ellipsis mode. Currently, only **START** and **END** are supported.
         * @param { string } ellipsis - String used to mark truncation.
         * @returns { TextLine } Truncated text line object.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 18
         */
        createTruncatedLine(width: number, ellipsisMode: EllipsisMode, ellipsis: string): TextLine;
        /**
         * Obtains the typographic boundaries of the text line. These boundaries depend on the typographic font and font
         * size, but not on the characters themselves. For example, for the string " a b " (which has a space before "a" and
         * a space after "b"), the typographic boundaries include the spaces at the beginning and end of the line.
         * Similarly, the strings "j" and "E" have identical typographic boundaries, independent of the characters
         * themselves.
         *
         * > **NOTE**
         * >
         * > The figure shows the typesetting boundaries for the string " a b ".
         * >
         * > ![TypographicBounds.png](docroot://reference/apis-arkgraphics2d/figures/TypographicBounds.png)
         * >
         * > The figure shows the typesetting boundaries for the string "j" or "E".
         * >
         * > !
         * > [TypographicBounds-Character.png](docroot://reference/apis-arkgraphics2d/figures/TypographicBounds-Character.png)
         *
         * @returns { TypographicBounds } Describes the typographic boundaries of a text line.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 18
         */
        getTypographicBounds(): TypographicBounds;
        /**
         * Obtains the image boundaries of this text line. The image boundaries, equivalent to visual boundaries, depend on
         * the font, font size, and characters. For example, for the string " a b " (which has a space before "a" and a
         * space after "b"), only "a b" is visible to users, and therefore the image boundaries do not include these spaces
         * at the beginning and end of the line. For the strings "j" and "E", their image boundaries are different.
         * Specifically, the width of the boundary for "j" is narrower than that for "E", and the height of the boundary for
         * "j" is taller than that for "E".
         *
         * > **NOTE**
         * >
         * > The figure shows the image boundaries for the string " a b ".
         * >
         * > ![ImageBounds.png](docroot://reference/apis-arkgraphics2d/figures/ImageBounds.png)
         * >
         * > The figure shows the image boundaries for the string "j" or "E".
         * >
         * > ![ImageBounds-Character.png](docroot://reference/apis-arkgraphics2d/figures/ImageBounds-Character.png)
         *
         * @returns { common2D.Rect } Image boundary of a text line, in physical pixels (px).
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 18
         */
        getImageBounds(): common2D.Rect;
        /**
         * Obtains the width of the spaces at the end of this text line.
         *
         * @returns { number } Width of trailing whitespace characters in the text line, which is a floating-point value, in
         *     physical pixels (px).
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 18
         */
        getTrailingSpaceWidth(): number;
        /**
         * Obtains the index of a character at the specified position in the original string.
         *
         * @param { common2D.Point } point - Coordinate position for finding the character index. The coordinates are
         *     relative to the top-left origin of the text line, in physical pixels (px). x indicates the horizontal
         *     coordinate, and y indicates the vertical coordinate.
         * @returns { number } Index of the character in the text line. The value is an integer.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 18
         */
        getStringIndexForPosition(point: common2D.Point): number;
        /**
         * Obtains the offset of a character with the specified index in this text line.
         *
         * @param { number } index - Index of the character. The value is an integer.
         * @returns { number } Offset at the given string index, which is a floating-point value, in physical pixels (px).
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 18
         */
        getOffsetForStringIndex(index: number): number;
        /**
         * Enumerates the offset and index of each character in a text line.
         *
         * @param { CaretOffsetsCallback } callback - Custom function, which contains the offset and index of each character
         *     in the text line.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 18
         */
        enumerateCaretOffsets(callback: CaretOffsetsCallback): void;
        /**
         * Obtains the offset of this text line after alignment based on the alignment factor and alignment width.
         *
         * @param { number } alignmentFactor - Alignment factor, which determines how text is aligned. The value is a
         *     floating point number. A value less than or equal to 0.0 means that the text is left-aligned; a value between
         *     0.0 and 0.5 means that the text is slightly left-aligned; the value 0.5 means that the text is centered; a
         *     value between 0.5 and 1 means that the text is slightly right-aligned; a value greater than or equal to 1.0
         *     means that the text is right-aligned.
         * @param { number } alignmentWidth - Alignment width, namely the width of the text line, which is a floating-point
         *     value, in physical pixels (px). If the width is less than the actual width of the text line, **0** is
         *     returned.
         * @returns { number } Calculated offset required for alignment, which is a floating-point value, in physical pixels
         *     (px).
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 18
         */
        getAlignmentOffset(alignmentFactor: number, alignmentWidth: number): number;
    }
    /**
     * Represents a text typesetting unit, which is a continuous text segment with the same style attributes. Run is
     * obtained through the [getGlyphRuns()]{@link text.TextLine.getGlyphRuns} API of the [TextLine]{@link text.TextLine}
     * class.
     *
     * Before calling any of the following APIs, you must use [getGlyphRuns()]{@link text.TextLine.getGlyphRuns} of the
     * [TextLine]{@link text.TextLine} class to create a **Run** object.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @atomicservice [since 22]
     * @since 12
     */
    class Run {
        /**
         * Obtains the number of glyphs in this run.
         *
         * @returns { number } Number of glyphs. The value is an integer.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        getGlyphCount(): number;
        /**
         * Obtains the index of each glyph in this run.
         *
         * @returns { Array<number> } Array holding the index of each glyph in the run.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        getGlyphs(): Array<number>;
        /**
         * Obtains the index of each glyph in the specified range of this run.
         *
         * @param { Range } range - Range of glyph indices to obtain. **range.start** indicates the starting position of the
         *     range, and **range.end** indicates the length of the range. When **range.end** is **0**, glyphs are fetched
         *     from **range.start** to the end of the rendered block. If **range.end** or **range.start** is set to a
         *     negative value, **null**, or **undefined**, **undefined** is returned.
         * @returns { Array<number> } Array holding the index of each glyph in the run.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 18
         */
        getGlyphs(range: Range): Array<number>;
        /**
         * Obtains the position of each glyph relative to the respective line in this run.
         *
         * @returns { Array<common2D.Point> } Array holding the position of each glyph relative to the respective line in
         *     the run.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        getPositions(): Array<common2D.Point>;
        /**
         * Obtains the position array of each glyph relative to the respective line within the specified range of this run.
         *
         * @param { Range } range - Range of the glyphs, where **range.start** indicates the start position of the range,
         *     and **range.end** indicates the length of the range. If the length is **0**, the range is from
         *     **range.start** to the end of the run. If **range.end** or **range.start** is set to a negative value,
         *     **null**, or **undefined**, **undefined** is returned.
         * @returns { Array<common2D.Point> } Array holding the position of each glyph relative to the respective line in
         *     the run.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 18
         */
        getPositions(range: Range): Array<common2D.Point>;
        /**
         * Obtains the offset of each glyph in this run relative to its index.
         *
         * @returns { Array<common2D.Point> } Array holding the offset of each glyph in the run relative to its index.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        getOffsets(): Array<common2D.Point>;
        /**
         * Obtains the **Font** object of this run.
         *
         * @returns { drawing.Font } **Font** object of this run.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        getFont(): drawing.Font;
        /**
         * Paints this run on the canvas with the coordinate point (x, y) as the upper left corner.
         *
         * @param { drawing.Canvas } canvas - Target canvas.
         * @param { number } x - Horizontal coordinate of the upper left corner, which is a floating-point value, in
         *     physical pixels (px).
         * @param { number } y - Vertical coordinate of the upper left corner, which is a floating-point value, in physical
         *     pixels (px).
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        paint(canvas: drawing.Canvas, x: number, y: number): void;
        /**
         * Obtains an array of character indices for glyphs within a specified range of this run, where the indices are
         * offsets relative to the entire paragraph.
         *
         * @param { Range } [range] - Range of character indices to be obtained. **range.start** indicates the starting
         *     position of the range, and **range.end** indicates the range length. If the length is 0, characters are
         *     retrieved from **range.start** to the end of the rendered block. If **range.end** or **range.start** is set
         *     to a negative value, **null**, or **undefined**, **undefined** is returned. If this parameter is not passed,
         *     the entire run is obtained.
         * @returns { Array<number> } Array of character indices.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 18
         */
        getStringIndices(range?: Range): Array<number>;
        /**
         * Obtains the range of glyphs generated by this run.
         *
         * @returns { Range } Range of the glyphs, where **start** indicates the start position of the range, which is the
         *     index relative to the entire paragraph, and **end** indicates the length of the range.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 18
         */
        getStringRange(): Range;
        /**
         * Obtains the typographic boundaries of the typographic unit. These boundaries are associated with the typographic
         * font and font size, but not with the characters. For example, for the string " a b " (which has a space before "a
         * " and a space after "b"), the typographic boundaries include the spaces at the beginning and end of the line.
         *
         * > **NOTE**
         * >
         * > The figure shows the typesetting boundaries for the string " a b ".
         * >
         * > ![TypographicBounds.png](docroot://reference/apis-arkgraphics2d/figures/TypographicBounds.png)
         * >
         * > The figure shows the typesetting boundaries for the string "j" or "E".
         * >
         * > !
         * > [TypographicBounds-Character.png](docroot://reference/apis-arkgraphics2d/figures/TypographicBounds-Character.png)
         *
         * @returns { TypographicBounds } Typographic boundaries of the run.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 18
         */
        getTypographicBounds(): TypographicBounds;
        /**
         * Obtains the image boundaries of the typographic unit. Equivalent to visual boundaries, these boundaries are
         * associated with the typographic font, font size, and characters. For example, for the string " a b " (which has a
         * space before "a" and a space after "b"), only "a b" is visible to users, and therefore the image boundaries do
         * not include these spaces at the beginning and end of the line.
         *
         * > **NOTE**
         * >
         * > The figure shows the image boundaries for the string " a b ".
         * >
         * > ![ImageBounds.png](docroot://reference/apis-arkgraphics2d/figures/ImageBounds.png)
         * >
         * > The figure shows the image boundaries for the string "j" or "E".
         * >
         * > ![ImageBounds-Character.png](docroot://reference/apis-arkgraphics2d/figures/ImageBounds-Character.png)
         *
         * @returns { common2D.Rect } Image boundary of the layout unit, in physical pixels (px).
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 18
         */
        getImageBounds(): common2D.Rect;
        /**
         * Obtains the text direction of the run.
         *
         * @returns { TextDirection } Obtains the text direction of the run.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 20
         */
        getTextDirection(): TextDirection;
        /**
         * Obtains the glyph width array of each glyph within the specified range of the run.
         *
         * @param { Range } range - Range of the glyph position to be obtained. **range.start** indicates the start position
         *     of the range, and **range.end** indicates the range length. If the length is **0**, the range starts from
         *     **range.start** and ends at the end of the run. If **range.end** or **range.start** is set to a negative
         *     value, **null**, or **undefined**, **undefined** is returned.
         * @returns { Array<common2D.Point> } Returns the glyph width array of each glyph in the run unit relative to the
         *     horizontal direction. In [common2D.Point]{@link @ohos.graphics.common2D:common2D.Point}, the x value
         *     represents the glyph width of each glyph relative to the horizontal direction, in physical pixels (px). The y
         *     value is a reserved field and returns **0** by default.
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 20
         */
        getAdvances(range: Range): Array<common2D.Point>;
        /**
         * Obtains the text style of this typesetting unit.
         *
         * @returns { TextStyle } Text style of this typesetting unit.
         *     <br>**Note:**
         *     <br>1. The `textStyle.color`, `textStyle.textShadows.color`, `textStyle.backgroundRect.color`, and
         *     `textStyle.decoration.color` attributes: return a 32-bit unsigned integer color value. Example: The return
         *     value `4278190080` corresponds to the solid black hexadecimal color value `0xFF000000`, which is equivalent
         *     to the [common2D.Color]{@link @ohos.graphics.common2D:common2D.Color} object parameters: alpha=255, red=0,
         *     green=0, blue=0. The example provides a numberToRGBA conversion method for reference.
         *     <br>2. `textStyle.ellipsis` and `textStyle.ellipsisMode` are paragraph attributes and cannot be obtained
         *     through this API. Use [getParagraphStyle()]{@link text.Paragraph.getParagraphStyle} instead.
         * @syscap SystemCapability.Graphics.Drawing
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        getTextStyle(): TextStyle;
    }
    /**
     * Describes the layout information and measurement information of a run of text in a text line.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @atomicservice [since 22]
     * @since 12
     */
    interface RunMetrics {
        /**
         * Text style.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        textStyle: TextStyle;
        /**
         * Font measurement information.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        fontMetrics: drawing.FontMetrics;
    }
    /**
     * Describes the measurement information of a single line of text in the text layout.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @atomicservice [since 22]
     * @since 12
     */
    interface LineMetrics {
        /**
         * Start index of the line in the text buffer.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        startIndex: number;
        /**
         * End index of the line in the text buffer.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        endIndex: number;
        /**
         * Text ascent height, which refers to the distance from the baseline to the top of characters, in physical pixels (
         * px).
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        ascent: number;
        /**
         * Text descent height, which refers to the distance from the baseline to the bottom of characters, in physical
         * pixels (px).
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        descent: number;
        /**
         * Height of the current line, in physical pixels (px). The calculation method is `Math.round(ascent + descent)`.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        height: number;
        /**
         * Width of a line, in physical pixels (px).
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        width: number;
        /**
         * Left edge position of a line, in physical pixels (px). The right edge is the value of **left** plus the value of
         * **width**.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        left: number;
        /**
         * Y coordinate of the baseline in the line relative to the top of the paragraph, in physical pixels (px).
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        baseline: number;
        /**
         * Line number, starting from 0.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        lineNumber: number;
        /**
         * Height from the top to the current line, in physical pixels (px).
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        topHeight: number;
        /**
         * Mapping between the text index range and the associated font measurement information.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 12
         */
        runMetrics: Map<number, RunMetrics>;
    }
    /**
     * Obtains the full names of all fonts of the specified type. This API uses a promise to return the result.
     *
     * @param { SystemFontType } fontType - Font type.
     * @returns { Promise<Array<string>> } Promise used to return the full names of all fonts of the specified type.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @atomicservice [since 22]
     * @since 14
     */
    function getSystemFontFullNamesByType(fontType: SystemFontType): Promise<Array<string>>;
    /**
     * Obtains the paths of all font files of a specified font type.
     *
     * @param { SystemFontType } fontType - Font type.
     * @returns { Array<string> } List of font file paths.
     * @syscap SystemCapability.Graphics.Drawing
     * @atomicservice
     * @since 23
     */
    function getFontPathsByType(fontType: SystemFontType): Array<string>;
    /**
     * Obtains the font descriptor based on the font name and type. This API uses a promise to return the result.
     *
     * A font descriptor is a data structure that describes font features. It contains details of the font appearance and
     * properties.
     *
     * @param { string } fullName - Font name. It is obtained with
     *     [getSystemFontFullNamesByType]{@link text.getSystemFontFullNamesByType} called.
     * @param { SystemFontType } fontType - Font type.
     * @returns { Promise<FontDescriptor> } Promise used to return the font descriptor.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types.
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @atomicservice [since 22]
     * @since 14
     */
    function getFontDescriptorByFullName(fullName: string, fontType: SystemFontType): Promise<FontDescriptor>;
    /**
     * Obtains all system font descriptors that match the provided font descriptor. This API uses a promise to return the
     * result.
     *
     * @param { FontDescriptor } desc - Font descriptor to match against. If this parameter is left unspecified, all
     *     system font descriptors are returned. If a specific value is provided, the matching is performed based on the
     *     value provided. If the matching fails, an empty array is returned.
     * @returns { Promise<Array<FontDescriptor>> } Promise used to return all matched system font descriptors.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @atomicservice [since 22]
     * @since 18
     */
    function matchFontDescriptors(desc: FontDescriptor): Promise<Array<FontDescriptor>>;
    /**
     * Implements a paragraph-style text tab, which stores the alignment mode and position.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @atomicservice [since 22]
     * @since 18
     */
    interface TextTab {
        /**
         * Text alignment method after the tab character in a paragraph. It supports the LEFT (left alignment), RIGHT (right
         * alignment), and CENTER (center alignment) alignment methods of [TextAlign]{@link text.TextAlign}. Unlisted enum
         * values are treated as left alignment, with left alignment as the default.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 18
         */
        alignment: TextAlign;
        /**
         * Alignment position of the text following the tab character. The value is a floating point number, in px. The
         * minimum value is 1.0. When the value is less than 1.0, the tab character is replaced with a space.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 18
         */
        location: number;
    }
    /**
     * Enumerates the high contrast types for text rendering.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @atomicservice [since 22]
     * @since 20
     */
    enum TextHighContrast {
        /**
         * Follows the high contrast mode for text rendering in the system settings.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 26.0.0]
         * @atomicservice [since 22]
         * @since 20
         */
        TEXT_FOLLOW_SYSTEM_HIGH_CONTRAST = 0,
        /**
         * Disables the high contrast mode for text rendering in the application. This mode takes precedence over the one
         * based on system settings.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 20
         */
        TEXT_APP_DISABLE_HIGH_CONTRAST = 1,
        /**
         * Enables the high contrast mode for text rendering in the application. The priority of this mode is higher than
         * the mode following the system settings.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 20
         */
        TEXT_APP_ENABLE_HIGH_CONTRAST = 2
    }
    /**
     * Sets the high contrast mode for text rendering.
     *
     * The setting of this API takes effect for the entire process, and all pages in the process share the same mode.
     *
     * You can call this API to set the high contrast mode, or enable or disable the high contrast mode by toggling the
     * switch on the system settings screen. This API is used to set the high contrast mode for text rendering. The
     * setting of this API takes precedence over the one based on system settings.
     *
     * This API does not take effect for text drawn by the app through APIs such as Canvas. It only takes effect for text
     * rendered using system text components.
     *
     * @param { TextHighContrast } action - High contrast mode for text rendering.
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @atomicservice [since 22]
     * @since 20
     */
    function setTextHighContrast(action: TextHighContrast): void;
    /**
     * Enumerates the modes for displaying undefined text glyphs.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @atomicservice [since 22]
     * @since 20
     */
    enum TextUndefinedGlyphDisplay {
        /**
         * Follows the internal .notdef glyph design of the font, which can be an empty box, space, or custom symbol.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 20
         */
        USE_DEFAULT = 0,
        /**
         * Always uses explicit tofu blocks to replace undefined glyphs, overriding the default behavior of fonts. It is
         * suitable for debugging missing characters or forcing a uniform display of missing symbols.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 24]
         * @atomicservice [since 22]
         * @since 20
         */
        USE_TOFU = 1
    }
    /**
     * Enumerates text processing states.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    enum TextProcessState {
        /**
         * Initial state, indicating that text processing has not started.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        INIT = 0,
        /**
         * Index generated state, indicating that the text index has been generated.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        INDEXED = 1,
        /**
         * Shaped state, indicating that the text has been shaped.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        SHAPED = 2,
        /**
         * Line-wrapped state. The text has been line-wrapped.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        LINE_BROKEN = 3,
        /**
         * Formatted state, indicating that the text has been formatted.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        FORMATTED = 4,
        /**
         * Drawn state, indicating that the text has been drawn.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        PAINT = 5,
        /**
         * Updated property state. The text properties have been updated.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        UPDATE_ATTRIBUTE = 6
    }
    /**
     * Enumerates text display states. Native result after text typesetting, which is irrelevant to external display
     * factors such as external canvas cropping and screen overflow.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    enum TextDisplayState {
        /**
         * Unknown display state, which is the default state.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        UNKNOWN = 0,
        /**
         * Complete display state, in which the text is not truncated or omitted and all content is displayed normally.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        ALL = 1,
        /**
         * Cropping display state, in which the part of the text that exceeds the typesetting area is directly cropped and
         * hidden.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        CLIP = 2,
        /**
         * Ellipsized display state, in which part of the content is replaced by specified characters (such as ellipsis '...
         * ') when the text exceeds the typesetting area.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        OMITTED = 3
    }
    /**
     * Represents the text rectangle size, which is used to describe the width and height of the text rectangle. It is a
     * floating-point value in physical pixels (px).
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @stagemodelonly
     * @atomicservice
     * @since 24
     */
    interface TextRectSize {
        /**
         * Width of the text rectangle, which is a floating-point value in physical pixels (px).
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        width: number;
        /**
         * Height of the text rectangle, which is a floating-point value in physical pixels (px).
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        height: number;
    }
    /**
     * Represents the text layout result.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @stagemodelonly
     * @atomicservice
     * @since 24
     */
    interface TextLayoutResult {
        /**
         * Array of character ranges that can be completely displayed after text layout calculation.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        fitStrRange: Array<Range>;
        /**
         * Rectangle size of the paragraph after layout.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        correctRect: TextRectSize;
    }
    /**
     * Sets the glyph type to be used when characters are mapped to the .notdef (undefined) glyph.
     *
     * After this API is called, any subsequently rendered text containing undefined glyphs will be displayed according to
     * this setting.
     *
     * This setting affects how to display undefined characters in the font:
     *
     * - The default behavior follows the .notdef glyph design of the font.
     * - After this feature is enabled, characters without glyphs are displayed as a tofu block.
     *
     * @param { TextUndefinedGlyphDisplay } noGlyphShow - Display mode of characters that cannot be shaped.
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 24]
     * @atomicservice [since 22]
     * @since 20
     */
    function setTextUndefinedGlyphDisplay(noGlyphShow: TextUndefinedGlyphDisplay): void;
    /**
     * Obtains an array of font descriptors by font file path. This API uses a promise to return the result.
     *
     * > **NOTE**
     * >
     * > - An empty array is returned if the font file is not found, the font file path is invalid, the font file does not
     * > have the required permission, or the file is not in the font format.
     * >
     * > - The **weight** field in [FontDescriptor]{@link text.FontDescriptor} does not exactly correspond to the weight
     * > value in the font file. Instead, the actual weight value in the font file is rounded off and mapped to the
     * > [FontWeight]{@link text.FontWeight} enum value. For example, the weight value 350 in the font file is mapped to 4
     * > 00, and the corresponding enum value is W400.
     *
     * @param { string | Resource } path - Path of the font file to query. Two formats are supported:<br/>1. Absolute path
     *     of the font file starting with "file://", for example, "file:///system/fonts/test.ttf".<br/>2. File in the
     *     project's resources/rawfile directory, in the format of $rawfile('file name'), for example, $rawfile('test.ttf'
     *     ).
     * @returns { Promise<Array<FontDescriptor>> } Promise used to return all font descriptors. If the font file cannot be
     *     found, the path is invalid, the font file does not have the required permission, or the file is not a font
     *     file, an empty array is returned.
     * @syscap SystemCapability.Graphics.Drawing
     * @atomicservice
     * @since 22
     */
    function getFontDescriptorsFromPath(path: string | Resource): Promise<Array<FontDescriptor>>;
    /**
     * Checks whether the system supports the specified font file. You can use this API to verify the availability of a
     * font file before loading a custom font, preventing text rendering exceptions caused by unsupported fonts.
     *
     * @param { string | Resource } fontURL - Path of the font file to be checked. The path must be in the format of "
     *     **file://** + Absolute path of the font file" or **$rawfile** (a file path relative to the
     *     **resources/rawfile** directory in the project, which includes the font file name).
     * @returns { boolean } Whether the system supports the specified font file. **true** means yes; **false** otherwise.
     * @syscap SystemCapability.Graphics.Drawing
     * @atomicservice
     * @since 23
     */
    function isFontSupported(fontURL: string | Resource): boolean;
    /**
     * Obtains an array of font Unicode by font file path. This API uses a promise to return the result.
     *
     * An empty array is returned if the font file is not found, the font file path is invalid, the font file does not
     * have the required permission, or the file is not in the font format.
     *
     * @param { string | Resource } path - Path of the font file to query, which must be "file:// + absolute path of the
     *     font file" or $rawfile('file name in the resources/rawfile directory of the project').
     * @param { number } index - Index of the font to load when the font file format is ttc/otc. The value ranges from 0 to
     *     count-1, where count is the number of fonts contained in the font file. For non-ttc/otc files, the index can
     *     only be 0. If this parameter is negative or exceeds the actual index range of the font file, an empty array is
     *     returned.
     * @returns { Promise<Array<number>> } Promise used to return the Unicode array corresponding to the font file.
     * @syscap SystemCapability.Graphics.Drawing
     * @atomicservice
     * @since 23
     */
    function getFontUnicodeSet(path: string | Resource, index: number): Promise<Array<number>>;
    /**
     * Obtains the number of font files contained in a font file based on the font file path.
     *
     * Returns **0** if the font file is not found, the font file path is invalid, the font file does not have the
     * required permission, or the file is not in the font format.
     *
     * @param { string | Resource } path - Path of the font file to query, which must be "file:// + absolute path of the
     *     font file" or $rawfile('file name in the resources/rawfile directory of the project').
     * @returns { number } Number of fonts.
     * @syscap SystemCapability.Graphics.Drawing
     * @stagemodelonly
     * @atomicservice
     * @since 23
     */
    function getFontCount(path: string | Resource): number;
}
export default text;

```
