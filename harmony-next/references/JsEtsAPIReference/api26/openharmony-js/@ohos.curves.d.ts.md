# @ohos.curves.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2021-2023 Huawei Device Co., Ltd.
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
 * @kit ArkUI
 */
/**
 * The **Curves** module provides APIs for interpolation calculation to create step, cubic Bezier, and spring curves.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 7
 */
declare namespace curves {
    /**
     * Defines an interpolation curve. For details about the curves and animations, see <!--RP1-->
     * [Bezier Curve](docroot://../design/ux-design/animation-attributes.md)<!--RP1End-->.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 7
     */
    enum Curve {
        /**
         * Linear. Indicates that the animation has the same velocity from start to finish.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        Linear,
        /**
         * Ease. Indicates that the animation starts at a low speed, then speeds up, and slows down before the end,
         * CubicBezier(0.25, 0.1, 0.25, 1.0).
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        Ease,
        /**
         * EaseIn. Indicates that the animation starts at a low speed, Cubic Bezier (0.42, 0.0, 1.0, 1.0).
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        EaseIn,
        /**
         * EaseOut. Indicates that the animation ends at low speed, CubicBezier (0.0, 0.0, 0.58, 1.0).
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        EaseOut,
        /**
         * EaseInOut. Indicates that the animation starts and ends at low speed, CubicBezier (0.42, 0.0, 0.58, 1.0).
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        EaseInOut,
        /**
         * FastOutSlowIn. Standard curve, cubic-bezier (0.4, 0.0, 0.2, 1.0).
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        FastOutSlowIn,
        /**
         * LinearOutSlowIn. Deceleration curve, cubic-bezier (0.0, 0.0, 0.2, 1.0).
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        LinearOutSlowIn,
        /**
         * FastOutLinearIn. Acceleration curve, cubic-bezier (0.4, 0.0, 1.0, 1.0).
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        FastOutLinearIn,
        /**
         * ExtremeDeceleration. Abrupt curve, cubic-bezier (0.0, 0.0, 0.0, 1.0).
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        ExtremeDeceleration,
        /**
         * Sharp. Sharp curves, cubic-bezier (0.33, 0.0, 0.67, 1.0).
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        Sharp,
        /**
         * Rhythm. Rhythmic curve, cubic-bezier (0.7, 0.0, 0.2, 1.0).
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        Rhythm,
        /**
         * Smooth. Smooth curves, cubic-bezier (0.4, 0.0, 0.4, 1.0).
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        Smooth,
        /**
         * Friction. Damping curves, CubicBezier (0.2, 0.0, 0.2, 1.0).
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        Friction
    }
    /**
     * Represents a curve object. Different types of curve objects can be created using APIs in this module, including
     * [curves.cubicBezierCurve]{@link curves.cubicBezierCurve} and
     * [curves.interpolatingSpring]{@link curves.interpolatingSpring}. The curve object provides interpolation
     * functionality through its member method [interpolate]{@link curves.ICurve.interpolate}.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    interface ICurve {
        /**
         * Calculates the interpolated value along the curve at the specified normalized time point.
         *
         * @param { number } fraction - Current normalized time.<br>Value range: [0, 1].<br>**NOTE**<br>A value less than 0
         *     is treated as **0**. A value greater than 1 is treated as **1**.
         * @returns { number } Curve interpolation corresponding to the normalized time point.
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        interpolate(fraction: number): number;
    }
    /**
     * Implements initialization for the interpolation curve, which is used to create an interpolation curve based on the
     * input parameter.
     *
     * @param { Curve } [curve] - Curve type.<br>Default value: **Curve.Linear**
     * @returns { ICurve } Interpolation curve.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    function initCurve(curve?: Curve): ICurve;
    /**
     * Implements initialization for the interpolation curve, which is used to create an interpolation curve based on the
     * input parameter.
     *
     * @param { Curve } [curve] - Curve type.<br>Default value: **Curve.Linear**
     * @returns { string } Interpolation curve object.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @since 7
     * @deprecated since 9
     * @useinstead initCurve
     */
    function init(curve?: Curve): string;
    /**
     * Creates a step curve.
     *
     * @param { number } count - Number of steps. The value must be a positive integer.<br>Value range:
     *     [1, +∞)<br>**NOTE**<br>A value less than 1 evaluates to the value **1**.
     * @param { boolean } end - Whether the step change occurs at the start or end of each interval.<br>- **true**: The
     *     step change occurs at the end of each interval.<br>- **false**: The step change occurs at the start of each
     *     interval.
     * @returns { ICurve } Interpolation curve.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    function stepsCurve(count: number, end: boolean): ICurve;
    /**
     * Creates a custom curve.
     *
     * @param { function } interpolate - Custom interpolation callback.<br>**fraction**: input x value for interpolation
     *     when the animation starts. Value range: [0, 1].<br>The return value is the y value of the curve. Value range:
     *     [0, 1].<br>**NOTE**<br>If **fraction** is **0**, the return value **0** corresponds to the animation start
     *     point; any other return value means that the animation jumps at the start point.<br>If **fraction** is **1**,
     *     the return value **1** corresponds to the animation end point; any other return value means that the end value
     *     of the animation is not the value of the state variable, which will result in an effect of transition from that
     *     end value to the value of the state variable.
     * @returns { ICurve } Interpolation curve.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice [since 11]
     * @since 10
     */
    function customCurve(interpolate: (fraction: number) => number): ICurve;
    /**
     * Creates a step curve.
     *
     * @param { number } count - Number of steps. The value must be a positive integer.
     * @param { boolean } end - Whether the step change occurs at the start or end of each interval.<br>- **true**: The
     *     step change occurs at the end of each interval.<br>- **false**: The step change occurs at the start of each
     *     interval.
     * @returns { string } Steps curve object.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @since 7
     * @deprecated since 9
     * @useinstead stepsCurve
     */
    function steps(count: number, end: boolean): string;
    /**
     * Creates a cubic Bezier curve, with x-coordinates automatically normalized between 0 and 1.
     *
     * @param { number } x1 - X coordinate of the first point on the Bezier curve.<br>Value range: [0, 1]<br>**NOTE**<br>A
     *     value less than 0 is treated as **0**. A value greater than 1 is treated as **1**.
     * @param { number } y1 - Y coordinate of the first point on the Bezier curve.<br>Value range: (-∞, +∞)
     * @param { number } x2 - X coordinate of the second point on the Bezier curve.<br>Value range: [0, 1]<br>**NOTE**<br>
     *     A value less than 0 is treated as **0**. A value greater than 1 is treated as **1**.
     * @param { number } y2 - Y coordinate of the second point on the Bezier curve.<br>Value range: (-∞, +∞)
     * @returns { ICurve } Interpolation curve.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    function cubicBezierCurve(x1: number, y1: number, x2: number, y2: number): ICurve;
    /**
     * Creates a cubic Bézier curve. The curve values must be between 0 and 1.
     *
     * @param { number } x1 -Value range [0, 1].
     *     Note: If the value is less than 0, 0 is used. If the value is greater than 1, 1 is used.
     * @param { number } y1 -Value range (-∞, +∞).
     * @param { number } x2 -Value range [0, 1].
     *     Note: If the value is less than 0, 0 is used. If the value is greater than 1, 1 is used.
     * @param { number } y2 -Value range (-∞, +∞).
     * @returns { string } Cubic Bézier curve object.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @since 7
     * @deprecated since 9
     * @useinstead cubicBezierCurve
     */
    function cubicBezier(x1: number, y1: number, x2: number, y2: number): string;
    /**
     * Creates a spring curve. The curve shape is subject to the spring parameters, and the animation duration is subject
     * to the **duration** parameter in **animation** and **animateTo**.
     *
     * @param { number } velocity - Initial velocity. It is applied by external factors to the spring animation,
     *     designed to help ensure the smooth transition from the previous motion state. The velocity is the normalized
     *     velocity, and its value is equal to the actual velocity at the beginning of the animation divided by the
     *     animation attribute change value.Value range: (-∞, +∞).
     * @param { number } mass - Mass, which influences the inertia in the spring system. The greater the mass,
     *     the greater the amplitude of the oscillation, and the slower the speed of restoring to the equilibrium
     *     position.
     *     Value range: (0, +∞).
     *     <p>**NOTE**:
     *     <br>If this parameter is set to a value less than or equal to 0, the value 1 is used.
     *     </p>
     * @param { number } stiffness - Stiffness.It is the degree to which an object deforms by resisting the force
     *     applied. In an elastic system, the greater the stiffness, the stronger the ability to resist deformation,
     *     and the faster the speed of restoring to the equilibrium position.Value range: (0, +∞).
     *     <p>**NOTE**:
     *     <br>If this parameter is set to a value less than or equal to 0, the value 1 is used.
     *     </p>
     * @param { number } damping -Damping. It is used to describe the oscillation and attenuation of the system
     *     after being disturbed. The larger the damping, the smaller the number of oscillations of elastic motion,
     *     and the smaller the oscillation amplitude.Value range: (0, +∞).
     *     <p>**NOTE**:
     *     <br>If this parameter is set to a value less than or equal to 0, the value 1 is used.
     *     </p>
     * @returns { ICurve } Interpolation curve.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    function springCurve(velocity: number, mass: number, stiffness: number, damping: number): ICurve;
    /**
     * Constructs a spring curve object.
     *
     * @param { number } velocity - Initial velocity. It is applied by external factors to the spring animation, designed
     *     to help ensure the smooth transition from the previous motion state.
     * @param { number } mass - Mass, which influences the inertia in the spring system. The greater the mass, the greater
     *     the amplitude of the oscillation, and the slower the speed of restoring to the equilibrium position.
     * @param { number } stiffness - Stiffness. It is the degree to which an object deforms by resisting the force
     *     applied. In an elastic system, the greater the stiffness, the stronger the ability to resist deformation, and
     *     the faster the speed of restoring to the equilibrium position.
     * @param { number } damping - Damping. It is a pure number and has no real physical meaning. It is used to describe
     *     the oscillation and attenuation of the system after being disturbed. The larger the damping, the smaller the
     *     number of oscillations of elastic motion, and the smaller the oscillation amplitude.
     * @returns { string } Spring curve object.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @since 7
     * @deprecated since 9
     * @useinstead springCurve
     */
    function spring(velocity: number, mass: number, stiffness: number, damping: number): string;
    /**
     * Creates a spring animation curve. If multiple spring animations are applied to the same attribute of an object,
     * each animation replaces their predecessor and inherits the velocity.
     *
     * @param { number } [response] - Duration of one complete oscillation.<br>Default value: **0.55**<br>Unit: second<br>
     *     Value range: (0, +∞)<br>**NOTE**<br>If this parameter is set to a value less than or equal to 0, the default
     *     value **0.55** is used.
     * @param { number } [dampingFraction] - Damping coefficient.<br>**0**: undamped. In this case, the spring oscillates
     *     forever.<br>> 0 and < 1: underdamped. In this case, the spring overshoots the equilibrium position.<br>**1**:
     *     critically damped.<br>> 1: overdamped. In this case, the spring approaches equilibrium gradually.<br>Default
     *     value: **0.825**<br>Unit: second<br>Value range:
     *     [0, +∞)<br>**NOTE**<br>A value less than 0 evaluates to the default value **0.825**.
     * @param { number } [overlapDuration] - Duration for animations to overlap, in seconds. When animations overlap, the
     *     **response** values of these animations will transit smoothly over this duration if they are different.<br>
     *     Default value: **0**<br>Unit: second<br>Value range:
     *     [0, +∞)<br> **NOTE**<br>A value less than 0 evaluates to the default value **0**.<br>
     *     The spring animation curve is physics-based. Its duration depends on the **springMotion** parameters and
     *     the previous velocity, rather than the **duration** parameter in [animation]{@link common},
     *     [animateTo]{@link common}, or [pageTransition]{@link page_transition}. The time cannot be normalized.
     *     Therefore, the interpolation cannot be obtained using the **interpolate** function of the curve.
     * @returns { ICurve } Curve.
     *     <br>**NOTE**
     *     <br>The spring animation curve is physics-based. Its duration depends on the **springMotion** parameters
     *     and the previous velocity, rather than the **duration** parameter in [animation]{@link common},
     *     [animateTo]{@link common}, or [pageTransition]{@link page_transition}. The time cannot be normalized.
     *     Therefore, the interpolation cannot be obtained using the [interpolate]{@link curves.ICurve.interpolate}
     *     function of the curve.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    function springMotion(response?: number, dampingFraction?: number, overlapDuration?: number): ICurve;
    /**
     * Creates a responsive spring animation curve. It is a special case of [springMotion]{@link curves.springMotion},
     * with the only difference in the default values. It can be used together with **springMotion**.
     *
     * @param { number } [response] - See **response** in **springMotion**.<br>Default value: **0.15**<br>Unit: second<br>
     *     Value range: (0, +∞)<br>**NOTE**<br>If this parameter is set to a value less than or equal to 0, the default
     *     value **0.15** is used.
     * @param { number } [dampingFraction] - See **dampingFraction** in **springMotion**.<br>Default value: **0.86**<br>
     *     Unit: second<br>Value range:
     *     [0, +∞)<br>**NOTE**<br>A value less than 0 evaluates to the default value **0.86**.
     * @param { number } [overlapDuration] - See **overlapDuration** in **springMotion**.<br>Default value: **0.25**<br>
     *     Unit: second<br>Value range:
     *     [0, +∞)<br>**NOTE**<br>A value less than 0 evaluates to the default value **0.25**.<br>**ResponsiveSpringMotion** is a special case of **springMotion**, with the only difference in the default values. To apply custom settings for a spring animation, you are advised to use **springMotion**. When using **responsiveSpringMotion**, you are advised to retain the default settings.<br>The duration of the responsive spring animation depends on the **responsiveSpringMotion** parameters and the previous velocity, rather than the duration parameter in [animation]{@link common}, [animateTo]{@link common}, or [pageTransition]{@link page_transition}. In addition, the interpolation cannot be obtained using the **interpolate** function of the curve.
     * @returns { ICurve } Curve.
     *     <br>**NOTE**
     *     <br>1. To apply custom settings for a spring animation, you are advised to use **springMotion**. When using
     *     **responsiveSpringMotion**, you are advised to retain the default settings.
     *     <br>2. The duration of the responsive spring animation depends on the **responsiveSpringMotion** parameters and the
     *     previous velocity, rather than the duration parameter in [animation]{@link common}, [animateTo]{@link common},
     *     or [pageTransition]{@link page_transition}. In addition, the interpolation cannot be obtained using the
     *     [interpolate]{@link curves.ICurve.interpolate} function of the curve.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    function responsiveSpringMotion(response?: number, dampingFraction?: number, overlapDuration?: number): ICurve;
    /**
     * Creates an interpolating spring curve animated from 0 to 1. The actual animation value is calculated based on the
     * curve. The animation duration is subject to the curve parameters, rather than the **duration** parameter in
     * **animation** or **animateTo**.
     *
     * @param { number } velocity - Initial velocity. It is applied by external factors to the spring animation,
     *     designed to help ensure the smooth transition from the previous motion state.
     *     The velocity is the normalized velocity, and its value is equal to the actual velocity at the beginning of
     *     the animation divided by the animation attribute change value.<br>Value range: (-∞, +∞).
     * @param { number } mass - Mass, which influences the inertia in the spring system. The greater the mass,
     *     the greater the amplitude of the oscillation, and the slower the speed of restoring to the equilibrium
     *     position.
     *     <br>Value range: (0, +∞).
     *     <p>**NOTE**:
     *     <br>If this parameter is set to a value less than or equal to 0, the value **1** is used.
     *     </p>
     * @param { number } stiffness - Stiffness. It is the degree to which an object deforms by resisting
     *     the force applied. In an elastic system, the greater the stiffness, the stronger the ability to resist
     *     deformation, and the faster the speed of restoring to the equilibrium position.<br>Value range: (0, +∞).
     *     <p>**NOTE**:
     *     <br>If this parameter is set to a value less than or equal to 0, the value **1** is used.
     *     </p>
     * @param { number } damping - Damping. It is used to describe the oscillation and attenuation of the system
     *     after being disturbed. The larger the damping, the smaller the number of oscillations of elastic motion,
     *     and the smaller the oscillation amplitude.<br>Value range: (0, +∞)<br>
     *     <p>**NOTE**:
     *     <br>If this parameter is set to a value less than or equal to 0, the value **1** is used.
     *     </p>
     * @returns { ICurve } Curve.
     *     <br>Note: The spring animation curve is physics-based. Its duration depends on the **interpolatingSpring**
     *     parameters, rather than the **duration** parameter in [animation]{@link common}, [animateTo]{@link common}, or
     *     [pageTransition]{@link page_transition}. The time cannot be normalized. Therefore, the interpolation cannot be
     *     obtained using the [interpolate]{@link curves.ICurve.interpolate} function of the curve.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice [since 11]
     * @since 10
     */
    function interpolatingSpring(velocity: number, mass: number, stiffness: number, damping: number): ICurve;
}
export default curves;

```
