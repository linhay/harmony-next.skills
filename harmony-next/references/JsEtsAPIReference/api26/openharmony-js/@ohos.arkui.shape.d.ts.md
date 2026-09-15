# @ohos.arkui.shape.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (C) 2024 Huawei Device Co., Ltd.
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
 * Describes the size of a shape.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @form
 * @atomicservice
 * @since 12
 */
interface ShapeSize {
    /**
     * Width of the shape.
     *
     * When the parameter type is number, the valid value range is
     * [0, +∞). When the parameter type is string, the value must conform to the [Length]{@link Length} type specification.
     *
     * Unit: vp.
     *
     * If the value is invalid, 0 vp is used.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @form
     * @atomicservice
     * @since 12
     */
    width?: number | string;
    /**
     * Height of the shape.
     *
     * When the parameter type is number, the valid value range is
     * [0, +∞). When the parameter type is string, the value must conform to the [Length]{@link Length} type specification.
     *
     * Unit: vp.
     *
     * If the value is invalid, 0 vp is used.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @form
     * @atomicservice
     * @since 12
     */
    height?: number | string;
}
/**
 * Represents the parameter of the constructor used to create a **RectShape** object.
 *
 * This API inherits from [ShapeSize]{@link ShapeSize}.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @form
 * @atomicservice
 * @since 12
 */
interface RectShapeOptions extends ShapeSize {
    /**
     * Radius of the rectangle border corners.
     *
     * When the parameter type is number, the valid value range is
     * [0, +∞). When the parameter type is string, the value must conform to the [Length]{@link Length} type specification.
     *
     * Unit: vp.
     *
     * If the value is invalid, 0 vp is used.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @form
     * @atomicservice
     * @since 12
     */
    radius?: number | string | Array<number | string>;
}
/**
 * Represents the parameter of the constructor used to create a **RectShape** object with rounded corners.
 *
 * This API inherits from [ShapeSize]{@link ShapeSize}.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @form
 * @atomicservice
 * @since 12
 */
interface RoundRectShapeOptions extends ShapeSize {
    /**
     * Radius width of the rectangle border corners.
     *
     * When the parameter type is number, the valid value range is
     * [0, +∞). When the parameter type is string, the value must conform to the [Length]{@link Length} type specification.
     *
     * Unit: vp.
     *
     * If the value is invalid, 0 vp is used.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @form
     * @atomicservice
     * @since 12
     */
    radiusWidth?: number | string;
    /**
     * Radius height of the rectangle border corners.
     *
     * When the parameter type is number, the valid value range is
     * [0, +∞). When the parameter type is string, the value must conform to the [Length]{@link Length} type specification.
     *
     * Unit: vp.
     *
     * If the value is invalid, 0 vp is used.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @form
     * @atomicservice
     * @since 12
     */
    radiusHeight?: number | string;
}
/**
 * Represents the parameter of the constructor used to create a **PathShape** object.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @form
 * @atomicservice
 * @since 12
 */
interface PathShapeOptions {
    /**
     * Path drawing commands. For more about the commands, see [commands]{@link PathAttribute#commands}.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @form
     * @atomicservice
     * @since 12
     */
    commands?: string;
}
/**
 * Implements the common shape methods.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @form
 * @atomicservice
 * @since 12
 */
declare class CommonShapeMethod<T> {
    /**
     * Sets the coordinate offset relative to the component's layout position.
     *
     * @param { Position } offset - Coordinate offset relative to the component's layout position.
     * @returns { T } Current object.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @form
     * @atomicservice
     * @since 12
     */
    offset(offset: Position): T;
    /**
     * Sets the fill color of this shape, which determines its opacity, with black representing full transparency and
     * white representing full opacity.
     *
     * @param { ResourceColor } color - Fill color of the shape, which represents the opacity of the fill area. The black
     *     color indicates full transparency, while white indicates full opacity.
     * @returns { T } Current object.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @form
     * @atomicservice
     * @since 12
     */
    fill(color: ResourceColor): T;
    /**
     * Sets the position of the shape.
     *
     * @param { Position } position - Position of the shape.
     * @returns { T } Current object.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @form
     * @atomicservice
     * @since 12
     */
    position(position: Position): T;
}
/**
 * This API inherits from [CommonShapeMethod]{@link CommonShapeMethod}.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @form
 * @atomicservice
 * @since 12
 */
declare class BaseShape<T> extends CommonShapeMethod<T> {
    /**
     * Sets the width of a shape.
     *
     * @param { Length } width - Width of the shape.<br>Unit: vp.<br>If the value is invalid, 0 vp is used.
     * @returns { T } Current object.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @form
     * @atomicservice
     * @since 12
     */
    width(width: Length): T;
    /**
     * Sets the height of a shape.
     *
     * @param { Length } height - Height of the shape.<br>Unit: vp.<br>If the value is invalid, 0 vp is used.
     * @returns { T } Current object.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @form
     * @atomicservice
     * @since 12
     */
    height(height: Length): T;
    /**
     * Sets the size of a shape.
     *
     * @param { SizeOptions } size - Size of the shape.
     * @returns { T } Current object.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @form
     * @atomicservice
     * @since 12
     */
    size(size: SizeOptions): T;
}
/**
 * Represents a rectangle shape used in the **clipShape** and **maskShape** APIs.
 *
 * This API inherits from [BaseShape]{@link BaseShape}.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @form
 * @atomicservice
 * @since 12
 */
export declare class RectShape extends BaseShape<RectShape> {
    /**
     * A constructor used to create a **RectShape** object.
     *
     * @param { RectShapeOptions | RoundRectShapeOptions } options - Rectangle parameters.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @form
     * @atomicservice
     * @since 12
     */
    constructor(options?: RectShapeOptions | RoundRectShapeOptions);
    /**
     * Sets the radius width of the rectangle border corners.
     *
     * @param { number | string } rWidth - Radius width of the rectangle border corners.<br> When the parameter type is
     *     number, the valid value range is
     *     [0, +∞). When the parameter type is string, the value must conform to the [Length]{@link Length} type specification.<br>Unit: vp.<br>If the value is invalid, 0 vp is used.
     * @returns { RectShape } **RectShape** object.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @form
     * @atomicservice
     * @since 12
     */
    radiusWidth(rWidth: number | string): RectShape;
    /**
     * Sets the radius height of the rectangle border corners.
     *
     * @param { number | string } rHeight - Radius height of the rectangle border corners.<br> When the parameter type is
     *     number, the valid value range is
     *     [0, +∞). When the parameter type is string, the value must conform to the [Length]{@link Length} type specification.<br>Unit: vp.<br>If the value is invalid, 0 vp is used.
     * @returns { RectShape } **RectShape** object.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @form
     * @atomicservice
     * @since 12
     */
    radiusHeight(rHeight: number | string): RectShape;
    /**
     * Sets the radius of the rectangle border corners.
     *
     * @param { number | string | Array<number | string> } radius - Radius of the rectangle border corners. When an array
     *     is provided, it should contain exactly four elements, corresponding to the radius of the upper left, upper
     *     right, lower left, and lower right corners of the rectangle, respectively. If more than four elements are
     *     contained, only the first four are accepted.<br> When the parameter type is number, the valid value range is
     *     [0, +∞). When the parameter type is string, the value must conform to the [Length]{@link Length} type specification.<br>Unit: vp.<br>If the value is invalid, 0 vp is used.
     * @returns { RectShape } **RectShape** object.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @form
     * @atomicservice
     * @since 12
     */
    radius(radius: number | string | Array<number | string>): RectShape;
}
/**
 * Represents a circle shape used in the **clipShape** and **maskShape** APIs.
 *
 * This API inherits from [BaseShape]{@link BaseShape}.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @form
 * @atomicservice
 * @since 12
 */
export declare class CircleShape extends BaseShape<CircleShape> {
    /**
     * A constructor used to create a **CircleShape** object.
     *
     * @param { ShapeSize } options - Size of the shape.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @form
     * @atomicservice
     * @since 12
     */
    constructor(options?: ShapeSize);
}
/**
 * Represents an ellipse shape used in the **clipShape** and **maskShape** APIs.
 *
 * This API inherits from [BaseShape]{@link BaseShape}.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @form
 * @atomicservice
 * @since 12
 */
export declare class EllipseShape extends BaseShape<EllipseShape> {
    /**
     * A constructor used to create a **EllipseShape** object.
     *
     * @param { ShapeSize } options - Size of the shape.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @form
     * @atomicservice
     * @since 12
     */
    constructor(options?: ShapeSize);
}
/**
 * Represents a path used in the **clipShape** and **maskShape** APIs.
 *
 * This API inherits from [CommonShapeMethod]{@link CommonShapeMethod}.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @form
 * @atomicservice
 * @since 12
 */
export declare class PathShape extends CommonShapeMethod<PathShape> {
    /**
     * A constructor used to create a **PathShape** object.
     *
     * @param { PathShapeOptions } options - Path parameters.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @form
     * @atomicservice
     * @since 12
     */
    constructor(options?: PathShapeOptions);
    /**
     * Sets the path drawing commands.
     *
     * @param { string } commands - Path drawing commands.
     * @returns { PathShape } **PathShape** object.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @form
     * @atomicservice
     * @since 12
     */
    commands(commands: string): PathShape;
}

```
