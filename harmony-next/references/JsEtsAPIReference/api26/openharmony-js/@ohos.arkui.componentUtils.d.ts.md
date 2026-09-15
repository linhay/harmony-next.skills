# @ohos.arkui.componentUtils.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2023-2024 Huawei Device Co., Ltd.
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
 * @kit ArkUI
 */
/**
 * The **componentUtils** module provides API for obtaining the coordinates and size of the drawing area of a component.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform [since 12]
 * @atomicservice [since 11]
 * @since 10
 */
declare namespace componentUtils {
    /**
     * Implements a **ComponentInfo** object, which provides the size, position, translation, scaling, rotation, and
     * affine matrix information of the component.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform [since 12]
     * @atomicservice [since 11]
     * @since 10
     */
    interface ComponentInfo {
        /**
         * Component size.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        size: Size;
        /**
         * Offset of the component relative to the parent component.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        localOffset: Offset;
        /**
         * Offset of the component relative to the window.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        windowOffset: Offset;
        /**
         * Offset of the component relative to the screen.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        screenOffset: Offset;
        /**
         * Translation of the component.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        translate: TranslateResult;
        /**
         * Scaling of the component.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        scale: ScaleResult;
        /**
         * Rotation of the component.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        rotate: RotateResult;
        /**
         * Affine matrix of the component, which is a 4x4 matrix object created based on the input parameter.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        transform: Matrix4Result;
    }
    /**
     * Defines the size property.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform [since 12]
     * @atomicservice [since 11]
     * @since 10
     */
    interface Size {
        /**
         * Component width.
         *
         * Unit: px
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        width: number;
        /**
         * Component height.
         *
         * Unit: px
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        height: number;
    }
    /**
     * Defines the offset property.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform [since 12]
     * @atomicservice [since 11]
     * @since 10
     */
    interface Offset {
        /**
         * X-coordinate.
         *
         * Unit: px
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        x: number;
        /**
         * Y-coordinate.
         *
         * Unit: px
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        y: number;
    }
    /**
     * Translation Result
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform [since 12]
     * @atomicservice [since 11]
     * @since 10
     */
    interface TranslateResult {
        /**
         * Translation distance along the x-axis.
         *
         * Unit: vp
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        x: number;
        /**
         * Translation distance along the y-axis.
         *
         * Unit: vp
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        y: number;
        /**
         * Translation distance along the z-axis.
         *
         * Unit: vp
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        z: number;
    }
    /**
     * Scale Result
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform [since 12]
     * @atomicservice [since 11]
     * @since 10
     */
    interface ScaleResult {
        /**
         * Scale factor along the x-axis.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        x: number;
        /**
         * Scale factor along the y-axis.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        y: number;
        /**
         * Scale factor along the z-axis.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        z: number;
        /**
         * X-coordinate of the center point.
         *
         * Unit: vp
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        centerX: number;
        /**
         * Y-coordinate of the center point.
         *
         * Unit: vp
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        centerY: number;
    }
    /**
     * Rotation Result.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform [since 12]
     * @atomicservice [since 11]
     * @since 10
     */
    interface RotateResult {
        /**
         * X-coordinate of the rotation vector.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        x: number;
        /**
         * Y-coordinate of the rotation vector.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        y: number;
        /**
         * Z coordinate of the rotation vector.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        z: number;
        /**
         * X-coordinate of the center point.
         *
         * Unit: vp
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        centerX: number;
        /**
         * Y-coordinate of the center point.
         *
         * Unit: vp
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        centerY: number;
        /**
         * Rotation angle.
         *
         * Unit: deg
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        angle: number;
    }
    /**
     * The matrix is column-first fourth-order matrix.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform [since 12]
     * @atomicservice [since 11]
     * @since 10
     */
    type Matrix4Result = [
        number,
        number,
        number,
        number,
        number,
        number,
        number,
        number,
        number,
        number,
        number,
        number,
        number,
        number,
        number,
        number
    ];
    /**
     * Obtains a **ComponentInfo** object based on the component ID and synchronously returns the geometric properties of
     * the component.
     *
     * > **NOTE**
     * >
     * > - Since API version 10, you can use the
     * > [getComponentUtils]{@link @ohos.arkui.UIContext:UIContext#getComponentUtils} API in
     * > [UIContext]{@link @ohos.arkui.UIContext} to obtain the [ComponentUtils]{@link @ohos.arkui.UIContext} object
     * > associated with the current UI context. This API provides access to component coordinates and size information
     * > after the target component completes layout. It is recommended that you invoke this API within
     * > [layout completion callbacks]{@link @ohos.arkui.inspector:inspector}. Note that dynamically created components
     * > must be mounted to the component tree before this API can obtain their information, as unmounted components are
     * > not measured or laid out by the UI framework. Always ensure that component mounting precedes information
     * > retrieval attempts.
     *
     * @param {string} id - Component ID.
     * @returns {ComponentInfo} **ComponentInfo** object, which provides the size, position, translation, scaling,
     *     rotation, and affine matrix information of the component.
     * @throws { BusinessError } 100001 - UI execution context not found.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice [since 11]
     * @since 10
     * @deprecated since 18
     * @useinstead ohos.arkui.UIContext.ComponentUtils#getRectangleById
     */
    function getRectangleById(id: string): ComponentInfo;
}
export default componentUtils;

```
