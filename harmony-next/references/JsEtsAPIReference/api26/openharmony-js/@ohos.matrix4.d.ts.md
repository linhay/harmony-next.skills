# @ohos.matrix4.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2020-2023 Huawei Device Co., Ltd.
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
 * Provides matrix transformation capabilities for components, including translation, rotation, and scaling. For
 * details, see [Transformation]{@link common}.
 *
 * **Matrix4** can be used in the following scenarios:
 *
 * In [Transformation]{@link common}, the [transform]{@link CommonMethod#transform(transform: Optional<object>)} API
 * uses the **Matrix4** object to display the matrix transformation in two-dimensional transformation, and the
 * [transform3D]{@link CommonMethod#transform3D} API uses the **Matrix4** object to set the three-dimensional
 * transformation matrix for a component.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 7
 */
declare namespace matrix4 {
    /**
     * Describes the translation parameters.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 7
     */
    interface TranslateOption {
        /**
         * Translation distance along the x-axis.
         *
         * Unit: px
         *
         * Default value: **0**
         *
         * Value range: (-∞, +∞)
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        x?: number;
        /**
         * Translation distance along the y-axis.
         *
         * Unit: px
         *
         * Default value: **0**
         *
         * Value range: (-∞, +∞)
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        y?: number;
        /**
         * Translation distance along the z-axis.
         *
         * Unit: px
         *
         * Default value: **0**
         *
         * Value range: (-∞, +∞)
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        z?: number;
    }
    /**
     * Describes the scale parameters.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 7
     */
    interface ScaleOption {
        /**
         * Scaling multiple along the x-axis. x > 1: The image is scaled up along the x-axis.
         *
         * 0 < x < 1: The image is scaled down along the x-axis.
         *
         * x < 0: The image is scaled in the reverse direction along the x-axis.
         *
         * Default value: **1**
         *
         * Value range: (-∞, +∞)
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        x?: number;
        /**
         * Scaling multiple along the y-axis. y > 1: The image is scaled up along the y-axis.
         *
         * 0 < y < 1: The image is scaled down along the y-axis.
         *
         * y < 0: The image is scaled in the reverse direction along the y-axis.
         *
         * Default value: **1**
         *
         * Value range: (-∞, +∞)
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        y?: number;
        /**
         * Scaling multiple along the z-axis. z > 1: The image is scaled up along the z-axis.
         *
         * 0 < z < 1: The image is scaled down along the z-axis.
         *
         * z < 0: The image is scaled in the reverse direction along the z-axis.
         *
         * Default value: **1**
         *
         * Value range: (-∞, +∞)
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        z?: number;
        /**
         * X-coordinate of the center point.
         *
         * Unit: px
         *
         * Default value: X-coordinate of the component center
         *
         * Value range: (-∞, +∞)
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        centerX?: number;
        /**
         * Y-coordinate of the center point.
         *
         * Unit: px
         *
         * Default value: Y-coordinate of the component center
         *
         * Value range: (-∞, +∞)
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        centerY?: number;
    }
    /**
     * Describes the rotation parameters.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 7
     */
    interface RotateOption {
        /**
         * X-coordinate of the rotation axis vector.
         *
         * Default value: **0**
         *
         * Value range: (-∞, +∞)
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        x?: number;
        /**
         * Y-coordinate of the rotation axis vector.
         *
         * Default value: **0**
         *
         * Value range: (-∞, +∞)
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        y?: number;
        /**
         * Z-coordinate of the rotation axis vector.
         *
         * Default value: **0**
         *
         * Value range: (-∞, +∞)
         *
         * **NOTE**
         *
         * The rotation axis vector is valid only when at least one of **x**, **y**, and **z** is not 0.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        z?: number;
        /**
         * Additional x-axis offset of the transformation center relative to the component's anchor.
         *
         * Unit: px
         *
         * Default value: **0**
         *
         * **NOTE**
         *
         * The value **0** indicates that the transformation center coincides with the component's x-axis anchor. For
         * details about the implementation, see
         * [Example 3: Implementing Rotation Around a Center Point](docroot://reference/apis-arkui/arkui-ts/ts-universal-attributes-transformation.md#example-3-implementing-rotation-around-a-center-point).
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        centerX?: number;
        /**
         * Additional y-axis offset of the transformation center relative to the component's anchor.
         *
         * Unit: px
         *
         * Default value: **0**
         *
         * **NOTE**
         *
         * The value **0** indicates that the transformation center coincides with the component's y-axis anchor. For
         * details about the implementation, see
         * [Example 3: Implementing Rotation Around a Center Point](docroot://reference/apis-arkui/arkui-ts/ts-universal-attributes-transformation.md#example-3-implementing-rotation-around-a-center-point).
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        centerY?: number;
        /**
         * Rotation angle.
         *
         * Default value: **0**
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        angle?: number;
    }
    /**
     * Defines the data structure of a coordinate point.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    export interface Point {
        /**
         * X-coordinate.
         *
         * Value range: (-∞, +∞)
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        x: number;
        /**
         * Y-coordinate.
         *
         * Value range: (-∞, +∞)
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        y: number;
    }
    /**
     * Describes the configuration options for polygon-to-polygon transformation mapping.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    export interface PolyToPolyOptions {
        /**
         * Coordinates of the source point.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        src: Array<Point>;
        /**
         * Start index of the source point coordinates.
         *
         * Default value: **0**.
         *
         * Value range: [0, +∞).
         *
         * @default 0
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        srcIndex?: number;
        /**
         * Coordinates of the destination point.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        dst: Array<Point>;
        /**
         * Start index of the destination point coordinates.
         *
         * Default value: **src.length/2**.
         *
         * Value range: [0, +∞).
         *
         * @default src.Length/2
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        dstIndex?: number;
        /**
         * Number of used points. **0**: returns an identity matrix. **1**: returns a translation matrix. 2-4: returns a
         * transformation matrix.
         *
         * Default value: **0**.
         *
         * Value range: [0, +∞).
         *
         * @default 0
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        pointCount?: number;
    }
    /**
     * Implements a **Matrix4Transit** object.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 7
     */
    interface Matrix4Transit {
        /**
         * Copies this matrix object.
         *
         * @returns { Matrix4Transit } Copy object of the current matrix.
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        copy(): Matrix4Transit;
        /**
         * Inverts this matrix object. The matrix that calls this API will be changed.
         *
         * @returns { Matrix4Transit } Inverse matrix object of the current matrix.
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        invert(): Matrix4Transit;
        /**
         * Combines the effects of two matrices to generate a new matrix object. The matrix that calls this API will be
         * changed.
         *
         * @param { Matrix4Transit } options - Matrix object to be combined.
         * @returns { Matrix4Transit } Object after matrix combination.
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        combine(options: Matrix4Transit): Matrix4Transit;
        /**
         * Translates this matrix object along the x, y, and z axes. The matrix that calls this API will be changed.
         *
         * @param { TranslateOption } options - Translation configuration.
         * @returns { Matrix4Transit } Matrix object after the translation.
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        translate(options: TranslateOption): Matrix4Transit;
        /**
         * Scales this matrix object along the x, y, and z axes. The matrix that calls this API will be changed.
         *
         * @param { ScaleOption } options - Scaling configuration.
         * @returns { Matrix4Transit } Matrix object after the scaling.
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        scale(options: ScaleOption): Matrix4Transit;
        /**
         * Skews this matrix object along the x and y axes. The matrix that calls this API will be changed.
         *
         * @param { number } x - Amount of skewing on the x-axis.
         * @param { number } y - Amount of skewing on the y-axis.
         * @returns { Matrix4Transit } Matrix object after the skewing.
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        skew(x: number, y: number): Matrix4Transit;
        /**
         * Rotates this matrix object along the x, y, and z axes. The matrix that calls this API will be changed.
         *
         * @param { RotateOption } options - Rotation configuration.
         * @returns { Matrix4Transit } Matrix object after the rotation.
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        rotate(options: RotateOption): Matrix4Transit;
        /**
         * Applies the current transformation effect to a coordinate point.
         *
         * @param { [ number, number ] } options - Point to be transformed.
         * @returns { [ number, number ] } Point object after matrix transformation
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        transformPoint(options: [
            number,
            number
        ]): [
            number,
            number
        ];
        /**
         * Maps the vertex coordinates of a polygon to those of another polygon.
         *
         * @param { PolyToPolyOptions } options - Parameters for mapping.
         * @returns { Matrix4Transit } Matrix object after the mapping.
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        setPolyToPoly(options: PolyToPolyOptions): Matrix4Transit;
    }
    /**
     * Matrix constructor, which is used to create a 4 x 4 matrix with the input parameters. Column-major order is used.
     *
     * @param {
     *
     *     [number,number,number,number,number,number,number,number,number,number,number,number,number,number,number,number]
     *     } options - A number array whose length is 16 (4 x 4). For details, see **4 x 4 matrix description**.<br>Value
     *     range of each number: (-∞, +∞)<br>Default value:<br>[1, 0, 0, 0,<br>0, 1, 0, 0,<br>0, 0, 1, 0,<br>0, 0, 0, 1]
     * @returns { Matrix4Transit } 4 x 4 matrix object created based on the input parameters.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 7
     */
    function init(options: [
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
    ]): Matrix4Transit;
    /**
     * Constructs an identity matrix.
     *
     * @returns { Matrix4Transit } Identity matrix object.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 7
     */
    function identity(): Matrix4Transit;
    /**
     * Copies this matrix object.
     *
     * @returns { Matrix4Transit } Copy object of the current matrix.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @since 7
     * @deprecated since 10
     * @useinstead Matrix4Transit.copy
     */
    function copy(): Matrix4Transit;
    /**
     * Inverts this matrix object.
     *
     * @returns { Matrix4Transit } Inverse matrix object of the current matrix.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @since 7
     * @deprecated since 10
     * @useinstead Matrix4Transit.invert
     */
    function invert(): Matrix4Transit;
    /**
     * Combines the effects of two matrices to generate a new matrix object.
     *
     * @param { Matrix4Transit } options - Matrix object to be combined.
     * @returns { Matrix4Transit } Matrix object after combination.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @since 7
     * @deprecated since 10
     * @useinstead Matrix4Transit.combine
     */
    function combine(options: Matrix4Transit): Matrix4Transit;
    /**
     * Translates this matrix object along the x, y, and z axes.
     *
     * @param { TranslateOption } options - Translation configuration.
     * @returns { Matrix4Transit } Matrix object after translation.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @since 7
     * @deprecated since 10
     * @useinstead Matrix4Transit.translate
     */
    function translate(options: TranslateOption): Matrix4Transit;
    /**
     * Scales this matrix object along the x, y, and z axes.
     *
     * @param { ScaleOption } options - Scaling configuration.
     * @returns { Matrix4Transit } Matrix object after scaling.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @since 7
     * @deprecated since 10
     * @useinstead Matrix4Transit.scale
     */
    function scale(options: ScaleOption): Matrix4Transit;
    /**
     * Rotates this matrix object along the x, y, and z axes.
     *
     * @param { RotateOption } options - Rotation configuration.
     * @returns { Matrix4Transit } Matrix object after rotation.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @since 7
     * @deprecated since 10
     * @useinstead Matrix4Transit.rotate
     */
    function rotate(options: RotateOption): Matrix4Transit;
    /**
     * Applies the current transformation effect to a coordinate point.
     *
     * @param { [ number, number ] } options - Point to be transformed.
     * @returns { [ number, number ] } Point object after matrix transformation
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @since 7
     * @deprecated since 10
     * @useinstead Matrix4Transit.transformPoint
     */
    function transformPoint(options: [
        number,
        number
    ]): [
        number,
        number
    ];
}
export default matrix4;

```
