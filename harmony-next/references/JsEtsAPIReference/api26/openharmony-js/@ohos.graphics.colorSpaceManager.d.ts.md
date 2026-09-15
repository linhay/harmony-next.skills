# @ohos.graphics.colorSpaceManager.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
* Copyright (C) 2022-2023 Huawei Device Co., Ltd.
* Licensed under the Apache License, Version 2.0 (the "License");
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at
*
* http://www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.
*/
/**
 * @file Color Space Management
 * @kit ArkGraphics2D
 */
/**
 * This module provides basic capabilities for managing abstract color space objects, including creating criterion color
 * space objects (such as sRGB, DCI-P3, and BT2020) and custom color space objects, as well as obtaining attributes such
 * as the color space type, white point value, and gamma value. It is suitable for scenarios where color consistency
 * needs to be ensured, such as image processing, video rendering, and cross-device color display. It helps you
 * implement accurate color management and conversion, improving user experience in color display.
 *
 * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
 * @crossplatform [since 11]
 * @atomicservice [since 12]
 * @since 9
 */
declare namespace colorSpaceManager {
    /**
     * Enumerates the color space types.
     *
     * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
     * @crossplatform [since 11]
     * @atomicservice [since 12]
     * @since 9
     */
    enum ColorSpace {
        /**
         * Unknown type.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        UNKNOWN = 0,
        /**
         * Adobe RGB (1998).
         *
         * The conversion function is of the Adobe RGB (1998) type.
         *
         * The encoding range is of the Full type.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        ADOBE_RGB_1998 = 1,
        /**
         * DCI-P3.
         *
         * The conversion function is of the Gamma 2.6 type.
         *
         * The encoding range is of the Full type.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        DCI_P3 = 2,
        /**
         * Display P3.
         *
         * The conversion function is of the SRGB type.
         *
         * The encoding range is of the Full type.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        DISPLAY_P3 = 3,
        /**
         * SRGB.
         *
         * The conversion function is of the SRGB type.
         *
         * The encoding range is of the Full type.
         *
         * This is the default color space type.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        SRGB = 4,
        /**
         * BT709.
         *
         * The conversion function is of the BT709 type.
         *
         * The encoding range is of the Full type.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        BT709 = 6,
        /**
         * BT601_P.
         *
         * The conversion function is of the BT709 type.
         *
         * The encoding range is of the Full type.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        BT601_EBU = 7,
        /**
         * BT601_N.
         *
         * The conversion function is of the BT709 type.
         *
         * The encoding range is of the Full type.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        BT601_SMPTE_C = 8,
        /**
         * BT2020.
         *
         * The conversion function is of the HLG type.
         *
         * The encoding range is of the Full type.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        BT2020_HLG = 9,
        /**
         * BT2020.
         *
         * The conversion function is of the PQ type.
         *
         * The encoding range is of the Full type.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        BT2020_PQ = 10,
        /**
         * Display P3.
         *
         * The conversion function is of the HLG type.
         *
         * The encoding range is of the Full type.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        P3_HLG = 11,
        /**
         * Display P3.
         *
         * The conversion function is of the PQ type.
         *
         * The encoding range is of the Full type.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        P3_PQ = 12,
        /**
         * Adobe RGB (1998).
         *
         * The conversion function is of the Adobe RGB (1998) type.
         *
         * The encoding range is of the Limit type.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        ADOBE_RGB_1998_LIMIT = 13,
        /**
         * Display P3.
         *
         * The conversion function is of the SRGB type.
         *
         * The encoding range is of the Limit type.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        DISPLAY_P3_LIMIT = 14,
        /**
         * SRGB.
         *
         * The conversion function is of the SRGB type.
         *
         * The encoding range is of the Limit type.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        SRGB_LIMIT = 15,
        /**
         * BT709.
         *
         * The conversion function is of the BT709 type.
         *
         * The encoding range is of the Limit type.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        BT709_LIMIT = 16,
        /**
         * BT601_P.
         *
         * The conversion function is of the BT709 type.
         *
         * The encoding range is of the Limit type.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        BT601_EBU_LIMIT = 17,
        /**
         * BT601_N.
         *
         * The conversion function is of the BT709 type.
         *
         * The encoding range is of the Limit type.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        BT601_SMPTE_C_LIMIT = 18,
        /**
         * BT2020.
         *
         * The conversion function is of the HLG type.
         *
         * The encoding range is of the Limit type.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        BT2020_HLG_LIMIT = 19,
        /**
         * BT2020.
         *
         * The conversion function is of the PQ type.
         *
         * The encoding range is of the Limit type.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        BT2020_PQ_LIMIT = 20,
        /**
         * Display P3.
         *
         * The conversion function is of the HLG type.
         *
         * The encoding range is of the Limit type.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        P3_HLG_LIMIT = 21,
        /**
         * Display P3.
         *
         * The conversion function is of the PQ type.
         *
         * The encoding range is of the Limit type.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        P3_PQ_LIMIT = 22,
        /**
         * Display P3.
         *
         * The conversion function is of the Linear type.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        LINEAR_P3 = 23,
        /**
         * SRGB.
         *
         * The conversion function is of the Linear type.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        LINEAR_SRGB = 24,
        /**
         * Same as that of LINEAR_SRGB.
         *
         * BT709.
         *
         * The conversion function is of the Linear type.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        LINEAR_BT709 = LINEAR_SRGB,
        /**
         * BT2020.
         *
         * The conversion function is of the Linear type.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        LINEAR_BT2020 = 25,
        /**
         * Same as that of SRGB.
         *
         * SRGB.
         *
         * The conversion function is of the SRGB type.
         *
         * The encoding range is of the Full type.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        DISPLAY_SRGB = SRGB,
        /**
         * Same as that of DISPLAY_P3.
         *
         * Display P3.
         *
         * The conversion function is of the SRGB type.
         *
         * The encoding range is of the Full type.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        DISPLAY_P3_SRGB = DISPLAY_P3,
        /**
         * Same as that of P3_HLG.
         *
         * Display P3.
         *
         * The conversion function is of the HLG type.
         *
         * The encoding range is of the Full type.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        DISPLAY_P3_HLG = P3_HLG,
        /**
         * Same as that of P3_PQ.
         *
         * Display P3.
         *
         * The conversion function is of the PQ type.
         *
         * The encoding range is of the Full type.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        DISPLAY_P3_PQ = P3_PQ,
        /**
         * BT2020.
         *
         * The conversion function is of the LOG type.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @since 18
         */
        H_LOG = 26,
        /**
         * DISPLAY BT2020.
         *
         * The conversion function is of the SRGB type.
         *
         * The encoding range is of the Full type.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @since 20
         */
        DISPLAY_BT2020_SRGB = 27,
        /**
         * Custom type.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        CUSTOM = 5
    }
    /**
     * The three primary colors (red, green, blue) and white as defined by the color space standard, whose positions in
     * the color space are represented by (x, y) coordinates based on real-world chromaticity.
     *
     * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
     * @crossplatform [since 11]
     * @since 9
     */
    interface ColorSpacePrimaries {
        /**
         * X coordinate of the red color in the color space.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @crossplatform [since 11]
         * @since 9
         */
        redX: number;
        /**
         * Y coordinate of the red color in the color space.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @crossplatform [since 11]
         * @since 9
         */
        redY: number;
        /**
         * X coordinate of the green color in the color space.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @crossplatform [since 11]
         * @since 9
         */
        greenX: number;
        /**
         * Y coordinate of the green color in the color space.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @crossplatform [since 11]
         * @since 9
         */
        greenY: number;
        /**
         * X coordinate of the blue color in the color space.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @crossplatform [since 11]
         * @since 9
         */
        blueX: number;
        /**
         * Y coordinate of the blue color in the color space.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @crossplatform [since 11]
         * @since 9
         */
        blueY: number;
        /**
         * X coordinate of the white point in the color space.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @crossplatform [since 11]
         * @since 9
         */
        whitePointX: number;
        /**
         * Y coordinate of the white point in the color space.
         *
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @crossplatform [since 11]
         * @since 9
         */
        whitePointY: number;
    }
    /**
     * Implements management of color space objects.
     *
     * Before calling any of the following APIs, you must use [create()]{@link colorSpaceManager.create} to create a color
     * space manager.
     *
     * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
     * @crossplatform [since 11]
     * @since 9
     */
    interface ColorSpaceManager {
        /**
         * Obtains the color space type.
         *
         * @returns { ColorSpace } Color space type.
         * @throws { BusinessError } 18600001 - The parameter value is abnormal. [since 9 - 22]
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @crossplatform [since 11]
         * @since 9
         */
        getColorSpaceName(): ColorSpace;
        /**
         * Obtains the coordinates of the white point in the color space.
         *
         * @returns { Array<number> } Coordinates [x, y] of the white point.
         * @throws { BusinessError } 18600001 - The parameter value is abnormal. [since 9 - 22]
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @crossplatform [since 11]
         * @since 9
         */
        getWhitePoint(): Array<number>;
        /**
         * Obtains the gamma of the color space.
         *
         * @returns { number } Gamma of the color space.
         * @throws { BusinessError } 18600001 - The parameter value is abnormal. [since 9 - 22]
         * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
         * @crossplatform [since 11]
         * @since 9
         */
        getGamma(): number;
    }
    /**
     * Creates a standard color space object.
     *
     * @param { ColorSpace } colorSpaceName - Type of the color space.
     *     <br>**UNKNOWN** and **CUSTOM** cannot be used when creating standard color space objects.
     * @returns { ColorSpaceManager } Color space object created.
     * @throws { BusinessError } 401 - Parameter error. Possible cause: 1.Incorrect parameter type.
     *     2.Parameter verification failed.
     * @throws { BusinessError } 18600001 - The parameter value is abnormal.
     * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
     * @crossplatform [since 11]
     * @since 9
     */
    function create(colorSpaceName: ColorSpace): ColorSpaceManager;
    /**
     * Creates a custom color space object.
     *
     * @param { ColorSpacePrimaries } primaries - Primaries of the color space.
     * @param { number } gamma - Gamma value of the color space, which is a floating point number greater than 0.
     * @returns { ColorSpaceManager } Color space object created.
     *     <br>The color space type is **CUSTOM** of [ColorSpace]{@link colorSpaceManager.ColorSpace}.
     * @throws { BusinessError } 401 - Parameter error. Possible cause: 1.Incorrect parameter type.
     *     2.Parameter verification failed.
     * @throws { BusinessError } 18600001 - The parameter value is abnormal.
     * @syscap SystemCapability.Graphic.Graphic2D.ColorManager.Core
     * @crossplatform [since 11]
     * @since 9
     */
    function create(primaries: ColorSpacePrimaries, gamma: number): ColorSpaceManager;
}
export default colorSpaceManager;

```
