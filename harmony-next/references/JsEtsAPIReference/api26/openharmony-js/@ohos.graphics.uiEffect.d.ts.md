# @ohos.graphics.uiEffect.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
* Copyright (c) 2024 Huawei Device Co., Ltd.
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
 * @file
 * @kit ArkGraphics2D
 */
/**
 * This module provides basic capabilities for component effects, including blur, brightening, and more.
 * Effects are categorized into the Filter and VisualEffect classes, and effects of the same class can be cascaded
 * under an instance of that effect class. Using this module, you can quickly implement complex visual effects without
 * needing to master underlying image processing algorithms, reducing development complexity and improving
 * user experience.
 * In actual development, blur can be used for background blurring, and brightening can be used for
 * bright screen display, etc.
 *
 * - [Filter]{@link uiEffect.Filter}: Used to add specified Filter effects to a component.
 * - [VisualEffect]{@link uiEffect.VisualEffect}: Used to add specified VisualEffect effects to a component.
 *
 * @syscap SystemCapability.Graphics.Drawing
 * @form [since 22]
 * @since 12
 */
declare namespace uiEffect {
    /**
     * Filter effect class, used to apply corresponding effects to specified components.
     * Before calling Filter methods, you need to first create a Filter instance through createFilter.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @since 12
     */
    interface Filter {
        /**
         * Adds a blur effect to the component.
         *
         * @param { number } blurRadius - Blur radius, in px. The value must be greater than or equal to 0.
         *     A larger blur radius results in a stronger blur effect. When the blur radius is 0, there is no blur effect.
         *     If a negative number is passed in, it is automatically corrected to 0.
         * @returns { Filter } - Returns the Filter with the blur effect attached, supporting chained calls
         *     to add other effects.
         * @syscap SystemCapability.Graphics.Drawing
         * @since 12
         */
        blur(blurRadius: number): Filter;
        /**
         * Adds an HDR (High Dynamic Range) brightening effect to the component content.
         * Nesting is not recommended, as forced nesting may cause overexposure.
         *
         * The brightening effect requires the HDR rendering pipeline to be enabled to take effect.
         * In some scenarios, HDR cannot be enabled even if an attempt is made to trigger the HDR rendering pipeline,
         * for example, when the device hardware specifications do not support HDR.
         *
         * The maximum supported brightness boost multiple is calculated as the device's current maximum brightness
         * divided by its SDR reference white luminance.
         *
         * > **NOTE**
         * >
         * > Using the HDR brightening effect incurs certain performance and power consumption overhead.
         * > It is recommended to use it in scenarios where HDR images or videos already exist.
         *
         * @permission ohos.permission.HDR_BRIGHTNESS
         * @param { number } ratio - Brightening ratio. The value range is [1.0, the maximum brightening ratio supported by
         *     the current device]. Values less than 1.0 are treated as 1.0; a value equal to 1.0 means no processing;
         *     values greater than 1.0 attempt to trigger the HDR rendering pipeline;
         *     values exceeding the maximum ratio are treated as the maximum ratio.
         * @returns { Filter } - Returns the Filter with the HDR brightening effect attached,
         *     supporting chained calls to add other effects.
         * @throws { BusinessError } 201 - Permission verification failed.
         *     The application does not have the permission required to call the API.
         * @syscap SystemCapability.Graphics.Drawing
         * @since 24
         */
        hdrBrightnessRatio(ratio: number): Filter;
    }
    /**
     * VisualEffect class, used to apply background color blending, border lighting, color gradient, and other
     * effects to a component. Before calling VisualEffect methods, you need to first create a VisualEffect instance
     * through createEffect.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @form [since 22]
     * @since 12
     */
    interface VisualEffect {
    }
    /**
     * Creates a Filter instance for adding multiple filter effects to a component.
     *
     * @returns { Filter } Returns a Filter instance, which supports adding multiple filter effects.
     * @syscap SystemCapability.Graphics.Drawing
     * @since 12
     */
    function createFilter(): Filter;
    /**
     * Creates a VisualEffect instance for adding multiple VisualEffect effects to a component.
     *
     * @returns { VisualEffect } Returns a VisualEffect instance, which supports adding multiple VisualEffect effects.
     * @syscap SystemCapability.Graphics.Drawing
     * @form [since 24]
     * @since 12
     */
    function createEffect(): VisualEffect;
}
export default uiEffect;

```
