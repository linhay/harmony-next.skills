# @ohos.arkui.ArcSwiper.d.ts

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
 * @kit ArkUI
 */
/**
 * Defines the callback to notify the application when the animation stops playing.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Circle
 * @crossplatform
 * @atomicservice
 * @since 18
 */
declare type FinishAnimationHandler = () => void;
/**
 * Implements the controller of the **ArcSwiper** component. You can bind this object to the **ArcSwiper** component and
 * use it to control page switching.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Circle
 * @crossplatform
 * @atomicservice
 * @since 18
 */
export class ArcSwiperController {
    /**
     * A constructor used to create an **ArcSwiperController** instance.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    constructor();
    /**
     * Turns to the next page. Page turning occurs with the animation, whose duration is specified by
     * [duration]{@link ArcSwiperAttribute#duration}.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    showNext();
    /**
     * Turns to the previous page. Page turning occurs with the animation, whose duration is specified by
     * [duration]{@link ArcSwiperAttribute#duration}.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    showPrevious();
    /**
     * Stops an animation.
     *
     * @param { FinishAnimationHandler } handler - Callback invoked when the animation stops.<br>If no value is provided,
     *     no callback is performed.
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    finishAnimation(handler?: FinishAnimationHandler);
}
/**
 * Declare the direction of arc indicator.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Circle
 * @crossplatform
 * @atomicservice
 * @since 18
 */
export enum ArcDirection {
    /**
     * 3 o'clock direction.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    THREE_CLOCK_DIRECTION = 0,
    /**
     * 6 o'clock direction.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    SIX_CLOCK_DIRECTION = 1,
    /**
     * 9 o'clock direction.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    NINE_CLOCK_DIRECTION = 2
}
/**
 * Describes the properties and behavior of the arc dot navigation indicator.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Circle
 * @crossplatform
 * @atomicservice
 * @since 18
 * @noninterop
 */
export class ArcDotIndicator {
    /**
     * A constructor used to create an **ArcDotIndicator** instance.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    constructor();
    /**
     * Sets the direction of the arc navigation indicator.
     *
     * @param { Optional<ArcDirection> } direction - Direction of the arc navigation indicator.<br>Default value:
     *     **ArcDirection.SIX_CLOCK_DIRECTION** (6 o'clock direction)
     * @returns { ArcDotIndicator } Properties and functionality of the arc navigation indicator.
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    arcDirection(direction: Optional<ArcDirection>): ArcDotIndicator;
    /**
     * Sets the color of the unselected navigation points in the arc navigation indicator.
     *
     * @param { Optional<ResourceColor> } color - Color of the unselected navigation points in the arc navigation
     *     indicator.<br>Default value: **'#A9FFFFFF'**
     * @returns { ArcDotIndicator } Properties and functionality of the arc navigation indicator.
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    itemColor(color: Optional<ResourceColor>): ArcDotIndicator;
    /**
     * Sets the color of the selected navigation point in the arc navigation indicator.
     *
     * @param { Optional<ResourceColor> } color - Color of the selected navigation point in the arc navigation indicator.<
     *     br>Default value: **#FF5EA1FF**
     * @returns { ArcDotIndicator } Properties and functionality of the arc navigation indicator.
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    selectedItemColor(color: Optional<ResourceColor>): ArcDotIndicator;
    /**
     * Sets the color of the arc navigation indicator when it is long-pressed.
     *
     * @param { Optional<ResourceColor> } color - Color of the arc navigation indicator when it is long-pressed.<br>
     *     Default value: **'#FF404040'**
     * @returns { ArcDotIndicator } Properties and functionality of the arc navigation indicator.
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    backgroundColor(color: Optional<ResourceColor>): ArcDotIndicator;
    /**
     * Sets the mask gradient color of the arc navigation indicator.
     *
     * @param { Optional<LinearGradient> } color - Mask gradient color of the arc navigation indicator.<br>Default start
     *     color: **'#00000000'**<br>Default end color: **'#FF000000'**
     * @returns { ArcDotIndicator } Properties and functionality of the arc navigation indicator.
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    maskColor(color: Optional<LinearGradient>): ArcDotIndicator;
}
/**
 * Provide an interface for ArcSwiper.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Circle
 * @crossplatform
 * @atomicservice
 * @since 18
 * @noninterop
 */
interface ArcSwiperInterface {
    /**
     * Creates an **ArcSwiper** component.
     *
     * @param { ArcSwiperController } controller - Controller bound to the component to control the page turning.
     * @returns { ArcSwiperAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    (controller?: ArcSwiperController): ArcSwiperAttribute;
}
/**
 * Defines the callback to notify the application when the index of the currently displayed element changes.
 *
 * @param { number } index - Index of the currently displayed element. The index is zero-based.
 * @syscap SystemCapability.ArkUI.ArkUI.Circle
 * @crossplatform
 * @atomicservice
 * @since 18
 */
declare type IndexChangedHandler = (index: number) => void;
/**
 * Defines the callback triggered when the page transition animation starts.
 *
 * @param { number } index - Index of the currently displayed element before the animation starts (not the final index
 *     after the animation ends).
 * @param { number } targetIndex - Index of the target element to switch to.
 * @param { SwiperAnimationEvent } event - Extra information of the animation, including the offset of the currently
 *     displayed element and target element relative to the start position of the **ArcSwiper** along the main axis, and
 *     the hands-off velocity.
 * @syscap SystemCapability.ArkUI.ArkUI.Circle
 * @crossplatform
 * @atomicservice
 * @since 18
 */
declare type AnimationStartHandler = (index: number, targetIndex: number, event: SwiperAnimationEvent) => void;
/**
 * Defines the callback triggered when the page transition animation ends.
 *
 * @param { number } index - Index of the currently displayed element.
 * @param { SwiperAnimationEvent } event - Extra information of the animation, which is the offset of the currently
 *     displayed element relative to the start position of the **ArcSwiper** along the main axis.
 * @syscap SystemCapability.ArkUI.ArkUI.Circle
 * @crossplatform
 * @atomicservice
 * @since 18
 */
declare type AnimationEndHandler = (index: number, event: SwiperAnimationEvent) => void;
/**
 * Defines the callback triggered on a frame-by-frame basis during a swipe-based page turn.
 *
 * @param { number } index - Index of the currently displayed element.
 * @param { SwiperAnimationEvent } event - Extra information of the animation, which is the offset of the currently
 *     displayed element relative to the start position of the **ArcSwiper** along the main axis.
 * @syscap SystemCapability.ArkUI.ArkUI.Circle
 * @crossplatform
 * @atomicservice
 * @since 18
 */
declare type GestureSwipeHandler = (index: number, event: SwiperAnimationEvent) => void;
/**
 * Provides the information about the custom page transition animation.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Circle
 * @crossplatform
 * @atomicservice
 * @since 18
 */
declare interface SwiperContentAnimatedTransition {
    /**
     * Timeout for the custom page transition animation. The timeout timer starts when the default animation (page
     * scrolling) reaches the point where the first frame is moved out of the viewport. If you do not call the
     * [finishTransition]{@link SwiperContentTransitionProxy.finishTransition} API of
     * [SwiperContentTransitionProxy]{@link SwiperContentTransitionProxy} before the timer expires, the component
     * considers that the custom animation of the page ends and immediately removes the page node from the render tree.
     * The unit is ms. The default value is **0**.
     *
     * @default 0 ms
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    timeout?: number;
    /**
     * Content of the custom page transition animation.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    transition: Callback<SwiperContentTransitionProxy>;
}
/**
 * Implements the proxy object returned during the execution of the custom page transition animation of the
 * **ArcSwiper** component. You can use this object to obtain the page information in the custom animation viewport. You
 * can also call the **finishTransition** API of this object to notify the **ArcSwiper** component that the custom
 * animation has finished playing.
 *
 * > **NOTE**
 *
 * > - For example, when the index of the currently selected child component is 0, during a transition animation from
 * > page 0 to page 1, the callback is triggered for all pages within the viewport on every frame. When pages 0 and 1
 * > are both in the viewport, the callback is triggered twice per frame. The first callback has **selectedIndex** as
 * > **0**, **index** as **0**, **position** as the ratio of how much page 0 has moved relative to its position before
 * > the animation started on the current frame, and **mainAxisLength** as the length of page 0 on the main axis. The
 * > second callback has **selectedIndex** as **0**, **index** as **1**, **position** as the ratio of how much page 1
 * > has moved relative to page 0 before the animation started on the current frame, and **mainAxisLength** as the
 * > length of page 1 on the main axis.
 * >
 * > - If the animation curve is a spring interpolation curve, during the transition animation from page 0 to page 1,
 * > due to the position and velocity when the user lifts their finger off the screen, animation may overshoot and slide
 * > past to page 2, then bounce back to page 1. Throughout this process, a callback is triggered for pages 1 and 2
 * > within the viewport on every frame.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Circle
 * @crossplatform
 * @atomicservice
 * @since 18
 */
declare interface SwiperContentTransitionProxy {
    /**
     * Index of the currently selected page.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    selectedIndex: number;
    /**
     * Index of a page in the viewport.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    index: number;
    /**
     * Position of the page specified by **index** relative to the start position of the **ArcSwiper** main axis (start
     * position of the page corresponding to **selectedIndex**).
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    position: number;
    /**
     * Length of the page specified by **index** along the main axis.
     * Unit: vp.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    mainAxisLength: number;
    /**
     * Notifies the **ArcSwiper** component that the custom animation has finished playing.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    finishTransition(): void;
}
/**
 * In addition to the [universal attributes]{@link common}, the following attributes are supported.
 *
 * In addition to the [universal events]{@link common}, the following events are supported.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Circle
 * @crossplatform
 * @atomicservice
 * @since 18
 * @noninterop
 */
declare class ArcSwiperAttribute extends CommonMethod<ArcSwiperAttribute> {
    /**
     * Sets the index of the child component currently displayed in the container. If the value is less than 0 or greater
     * than or equal to the number of child components, the default value **0** is used.
     *
     * @param { Optional<number> } index - Index of the child component currently displayed in the container.<br>If
     *     **index** is set to **undefined**, the value **0** is used.
     * @returns { ArcSwiperAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    index(index: Optional<number>): ArcSwiperAttribute;
    /**
     * Sets the style of the arc dot navigation indicator.
     *
     * @param { Optional<ArcDotIndicator | boolean> } style - Style of the arc dot navigation indicator.<br> -
     *     **ArcDotIndicator**: properties and behavior of the arc dot navigation indicator.<br> - **boolean**: whether to
     *     enable the arc dot navigation indicator. **true** to enable, **false** otherwise.<br> Default value: **true**<
     *     br> Default type: **ArcDotIndicator**
     * @returns { ArcSwiperAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    indicator(style: Optional<ArcDotIndicator | boolean>): ArcSwiperAttribute;
    /**
     * Sets the duration of the animation for child component switching.
     *
     * @param { Optional<number> } duration - Duration of the autoplay for child component switching.<br>Default value:
     *     **400**<br>Unit: ms
     * @returns { ArcSwiperAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    duration(duration: Optional<number>): ArcSwiperAttribute;
    /**
     * Sets whether vertical swiping is used.
     *
     * @param { Optional<boolean> } isVertical - Whether vertical swiping is used.<br>The value **true** means vertical
     *     swiping, and **false** means horizontal swiping.<br>Default value: **false**
     * @returns { ArcSwiperAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    vertical(isVertical: Optional<boolean>): ArcSwiperAttribute;
    /**
     * Sets whether to disable the swipe feature.
     *
     * @param { Optional<boolean> } disabled - Whether to disable the swipe feature. The value **true** means to disable
     *     the feature, and **false** means the opposite.<br>Default value: **false**
     * @returns { ArcSwiperAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    disableSwipe(disabled: Optional<boolean>): ArcSwiperAttribute;
    /**
     * Sets the sensitivity to the digital crown rotation.
     *
     * @param { Optional<CrownSensitivity> } sensitivity - Sensitivity to the digital crown rotation.<br>Default value:
     *     **CrownSensitivity.MEDIUM**.
     * @returns { ArcSwiperAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    digitalCrownSensitivity(sensitivity: Optional<CrownSensitivity>): ArcSwiperAttribute;
    /**
     * Triggered when the index of the currently displayed child component changes. The return value is the index of the
     * currently displayed child component.
     *
     * When the **ArcSwiper** component is used together with
     * [LazyForEach](docroot://ui/rendering-control/arkts-rendering-control-lazyforeach.md), the subpage UI update cannot
     * be triggered in the **onChange** event.
     *
     * @param { Optional<IndexChangedHandler> } handler - Callback for the index of the currently displayed element.
     * @returns { ArcSwiperAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    onChange(handler: Optional<IndexChangedHandler>): ArcSwiperAttribute;
    /**
     * Triggered when the page transition animation starts.
     *
     * @param { Optional<AnimationStartHandler> } handler - Triggered when the page transition animation starts.
     * @returns { ArcSwiperAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    onAnimationStart(handler: Optional<AnimationStartHandler>): ArcSwiperAttribute;
    /**
     * Triggered when the page transition animation ends.
     *
     * This event is triggered when the page transition animation of the **ArcSwiper** component ends, whether it is
     * caused by gesture interruption or by calling **finishAnimation** through
     * [SwiperController]{@link SwiperController}. The **index** parameter indicates the index after the animation ends.
     * When the **ArcSwiper** component contains multiple columns, the index is of the leftmost element.
     *
     * @param { Optional<AnimationEndHandler> } handler - Triggered when the page transition animation ends.
     * @returns { ArcSwiperAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    onAnimationEnd(handler: Optional<AnimationEndHandler>): ArcSwiperAttribute;
    /**
     * Triggered on a frame-by-frame basis when the page is turned by a swipe.
     *
     * @param { Optional<GestureSwipeHandler> } handler - Triggered on a frame-by-frame basis when the page is turned by a
     *     swipe.
     * @returns { ArcSwiperAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    onGestureSwipe(handler: Optional<GestureSwipeHandler>): ArcSwiperAttribute;
    /**
     * Sets the effect used when the scroll boundary is reached. For details about the supported effects, see
     * [EdgeEffect]{@link EdgeEffect}. The setting does not take effect when configured using the controller API.
     *
     * @param {  Optional<EdgeEffect> } edgeEffect - Effect used when the component is at one of the edges.<br>Default
     *     value: **EdgeEffect.Spring**
     * @returns { ArcSwiperAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    effectMode(edgeEffect: Optional<EdgeEffect>): ArcSwiperAttribute;
    /**
     * Defines a custom page transition animation. During finger-following swipes and post-release transition animations,
     * this triggers a frame-by-frame callback for all pages in the viewport, allowing you to customize animations by
     * modifying properties like opacity, scale, and translation.
     *
     * During finger-following swipes and post-release transition animations, the
     * [SwiperContentTransitionProxy]{@link SwiperContentTransitionProxy} callback is invoked for all pages in the
     * viewport on a frame-by-frame basis. For example, when there are two pages whose subscripts are 0 and 1 in the
     * viewport, two callbacks whose indexes are 0 and 1 are invoked in each frame.
     *
     * @param { Optional<SwiperContentAnimatedTransition> } transition - Information about the custom page transition
     *     animation.
     * @returns { ArcSwiperAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    customContentTransition(transition: Optional<SwiperContentAnimatedTransition>): ArcSwiperAttribute;
    /**
     * Sets whether to disable the transition animation.
     *
     * @param { Optional<boolean> } disabled - Whether to disable the transition animation.<br>**true**: Disable the
     *     animation effect. **false**: Do not disable the animation effect.<br>If the input parameter is invalid, the
     *     value **false** is used.
     * @returns { ArcSwiperAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    disableTransitionAnimation(disabled: Optional<boolean>): ArcSwiperAttribute;
}
/**
 * Defines the ArcSwiper Component that can provide the ability for sub components to swipe and display.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Circle
 * @crossplatform
 * @atomicservice
 * @uicomponent [since 19]
 * @since 18
 * @noninterop
 */
declare let ArcSwiper: ArcSwiperInterface;
/**
 * Defines ArcSwiper Component instance.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Circle
 * @crossplatform
 * @atomicservice
 * @since 18
 * @noninterop
 */
declare let ArcSwiperInstance: ArcSwiperAttribute;

```
