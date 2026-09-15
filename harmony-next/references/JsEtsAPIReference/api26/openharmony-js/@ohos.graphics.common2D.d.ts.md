# @ohos.graphics.common2D.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2023 Huawei Device Co., Ltd.
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
/**
 * This module defines some common data types in the 2D graphics field.
 *
 * > **NOTE**
 * >
 * > - This module uses the physical pixel unit, px.
 *
 * @syscap SystemCapability.Graphics.Drawing
 * @crossplatform [since 20]
 * @atomicservice [since 22]
 * @since 11
 */
declare namespace common2D {
    /**
     * Describes a color in ARGB format.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 20]
     * @atomicservice [since 22]
     * @since 11
     */
    interface Color {
        /**
         * Alpha component of the color. The value is an integer ranging from 0 to 255.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 20]
         * @atomicservice [since 22]
         * @since 11
         */
        alpha: number;
        /**
         * Red component of the color. The value is an integer ranging from 0 to 255.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 20]
         * @atomicservice [since 22]
         * @since 11
         */
        red: number;
        /**
         * Green component of the color. The value is an integer ranging from 0 to 255.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 20]
         * @atomicservice [since 22]
         * @since 11
         */
        green: number;
        /**
         * Blue component of the color. The value is an integer ranging from 0 to 255.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 20]
         * @atomicservice [since 22]
         * @since 11
         */
        blue: number;
    }
    /**
     * Describes a rectangle, which can be defined by two coordinate points: upper left corner point and lower right
     * corner point.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 20]
     * @atomicservice [since 22]
     * @since 11
     */
    interface Rect {
        /**
         * X coordinate of the upper left corner of the rectangle. The value is a floating point number.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 20]
         * @atomicservice [since 22]
         * @since 11
         */
        left: number;
        /**
         * Y coordinate of the upper left corner of the rectangle. The value is a floating point number.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 20]
         * @atomicservice [since 22]
         * @since 11
         */
        top: number;
        /**
         * X coordinate of the lower right corner of the rectangle. The value is a floating point number.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 20]
         * @atomicservice [since 22]
         * @since 11
         */
        right: number;
        /**
         * Y coordinate of the lower right corner of the rectangle. The value is a floating point number.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 20]
         * @atomicservice [since 22]
         * @since 11
         */
        bottom: number;
    }
    /**
     * Describes a coordinate point.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 20]
     * @atomicservice [since 22]
     * @since 12
     */
    interface Point {
        /**
         * Horizontal coordinate. The value is a floating point number.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 20]
         * @atomicservice [since 22]
         * @since 12
         */
        x: number;
        /**
         * Vertical coordinate. The value is a floating point number.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 20]
         * @atomicservice [since 22]
         * @since 12
         */
        y: number;
    }
    /**
     * Describes a 3D coordinate point. It inherits from [Point]{@link common2D.Point}.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform [since 20]
     * @since 12
     */
    interface Point3d extends Point {
        /**
         * Z-axis coordinate. The value is a floating point number.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform [since 20]
         * @since 12
         */
        z: number;
    }
    /**
     * Describes a color in ARGB format.
     *
     * @syscap SystemCapability.Graphics.Drawing
     * @crossplatform
     * @since 20
     */
    interface Color4f {
        /**
         * Alpha component of the color. The value is a floating point number ranging from 0.0 to 1.0.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform
         * @since 20
         */
        alpha: number;
        /**
         * Red component of the color. The value is a floating point number ranging from 0.0 to 1.0.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform
         * @since 20
         */
        red: number;
        /**
         * Green component of the color. The value is a floating point number ranging from 0.0 to 1.0.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform
         * @since 20
         */
        green: number;
        /**
         * Blue component of the color. The value is a floating point number ranging from 0.0 to 1.0.
         *
         * @syscap SystemCapability.Graphics.Drawing
         * @crossplatform
         * @since 20
         */
        blue: number;
    }
}
export default common2D;

```
