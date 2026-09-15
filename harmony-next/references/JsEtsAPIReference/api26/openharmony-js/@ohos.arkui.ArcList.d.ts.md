# @ohos.arkui.ArcList.d.ts

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
 * Represents the callback triggered when a child component enters or leaves the visible area
 * of the **ArcList** component.
 *
 * @param { number } start - Index of the first child component in the visible area of the
 *     **ArcList** component.
 * @param { number } end - Index of the last child component in the visible area of the
 *     **ArcList** component.
 * @param { number } center - Index of the center child component in the visible area of the
 *     **ArcList** component.
 * @syscap SystemCapability.ArkUI.ArkUI.Circle
 * @crossplatform
 * @atomicservice
 * @since 18
 */
declare type ArcScrollIndexHandler = (start: number, end: number, center: number) => void;
/**
 * Provides basic parameters for creating an **ArcList** component.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Circle
 * @crossplatform
 * @atomicservice
 * @since 18
 */
declare interface ArkListOptions {
    /**
     * Item displayed at the beginning of the viewport when the **ArcList** component is loaded
     * for the first time, that is, the first item to be displayed.<br/>Default value: **0**<br/>
     * **NOTE**<br/>If the set value is a negative number or is greater than the index of the last
     * item, the value is invalid. In this case, the default value will be used.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    initialIndex?: number;
    /**
     * Controller of the scrollable component. After being bound to **ArcList**, the controller
     * can control the scrolling of **ArcList**.<br/>**NOTE**<br/>The scroller cannot be bound to
     * other scrollable components.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    scroller?: Scroller;
    /**
     * Header component.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    header?: ComponentContent;
}
/**
 * The **ArcList** component is a circular layout container that displays a series of list items
 * in an arc shape. It is suitable for presenting homogeneous data, such as images and text,
 * in a continuous, multi-row format.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Circle
 * @crossplatform
 * @atomicservice
 * @since 18
 */
export interface ArcListInterface {
    /**
     * Creates an **ArcList** component instance with specified configuration options.
     *
     * @param { ArkListOptions } [options]
     * @returns { ArcListAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    (options?: ArkListOptions): ArcListAttribute;
}
/**
 * The **ArcListItem** component is used to display individual child components in an
 * [ArcList]{@link @ohos.arkui.ArcList} component and must be used in conjunction with **ArcList**.
 *
 * > **NOTE**
 *
 * > - This component can be used only as a child of [ArcList]{@link @ohos.arkui.ArcList}.
 * >
 * > - When this component is used with
 * > [LazyForEach](docroot://ui/rendering-control/arkts-rendering-control-lazyforeach.md), its child components are
 * > created when it is created. When this component is used with
 * > [if/else](docroot://ui/rendering-control/arkts-rendering-control-ifelse.md) or
 * > [ForEach](docroot://ui/rendering-control/arkts-rendering-control-foreach.md), or when the parent component is
 * > [ArcList]{@link @ohos.arkui.ArcList}, its child components are created when it is laid out.
 * >
 * > - This component can be used on phones, PCs, 2-in-1 devices, tablets, TVs, and wearables. In API version 22 and
 * > earlier versions, a compilation warning will be reported when this component is used on phones, PCs, 2-in-1 devices
 * > , tablets, and TVs, but the component can still run properly.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Circle
 * @crossplatform
 * @atomicservice
 * @since 18
 * @noninterop
 */
export interface ArcListItemInterface {
    /**
     * Creates an item for the **ArcList** component.
     *
     * @returns { ArcListItemAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    (): ArcListItemAttribute;
}
/**
 * In addition to the [universal attributes]{@link common}, the
 * following attributes are supported.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Circle
 * @crossplatform
 * @atomicservice
 * @since 18
 */
export declare class ArcListAttribute extends CommonMethod<ArcListAttribute> {
    /**
     * Sets the sensitivity of the digital crown's event response.
     *
     * @param { Optional<CrownSensitivity> } sensitivity - Sensitivity of the digital crown's
     *     event response.<br/>Default value: **CrownSensitivity.MEDIUM**, indicating moderate
     *     response speed.
     * @returns { ArcListAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    digitalCrownSensitivity(sensitivity: Optional<CrownSensitivity>): ArcListAttribute;
    /**
     * Sets the spacing between list items.
     *
     * @param { Optional<LengthMetrics> } space - Spacing between list items.<br/>
     *     Default value: **LengthMetrics.vp(0)**.<br/>Child components of **ArcList** whose
     *     visibility attribute is set to **None** are not displayed, but the spacing above and
     *     below them still takes effect.
     * @returns { ArcListAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    space(space: Optional<LengthMetrics>): ArcListAttribute;
    /**
     * Sets the state of the scrollbar.
     *
     * @param { Optional<BarState> } status - State of the scrollbar.<br/>
     *     Default value: **BarState.Auto**
     * @returns { ArcListAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    scrollBar(status: Optional<BarState>): ArcListAttribute;
    /**
     * Sets the color of the scrollbar.
     *
     * @param { Optional<ColorMetrics> } color - Color of the scrollbar.<br/>
     *     Default value: **ColorMetrics.numeric(0xA9FFFFFF)**
     * @returns { ArcListAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    scrollBarColor(color: Optional<ColorMetrics>): ArcListAttribute;
    /**
     * Sets the width of the scrollbar. Once the width is set, the scrollbar will use this
     * width in its pressed state.
     *
     * @param { Optional<LengthMetrics> } width - Width of the scrollbar.<br/>
     *     Default value: **LengthMetrics.vp(24)**.<br/>Minimum value: **LengthMetrics.vp(4)**<br>Unit: vp
     * @returns { ArcListAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    scrollBarWidth(width: Optional<LengthMetrics>): ArcListAttribute;
    /**
     * Sets the number of arc list items to be preloaded (cached). In a lazy loading scenario,
     * only the content equivalent to **cachedCount** outside the visible area of the arc list is
     * preloaded. In a non-lazy loading scenario, all items are loaded at once. For both lazy and
     * non-lazy loading, only the content within the visible area of the arc list plus the content
     * equivalent to **cachedCount** outside the visible area is laid out.
     * When **cachedCount** is set for the arc list, the system preloads and lays out the
     * **cachedCount**-specified number of rows of arc list items both above and below the
     * currently visible area of the arc list.
     *
     * @param { Optional<number> } count - Number of list items to preload.<br/>
     *     Default value: number of nodes visible on the screen, with the maximum value of 16.<br/>
     *     Value range: [0, +∞)
     * @returns { ArcListAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    cachedCount(count: Optional<number>): ArcListAttribute;
    /**
     * Sets whether to enable chained animations, which provide a visually connected, or
     * "chained," effect when the **ArcList** component is scrolled or its top or bottom edge is
     * dragged.
     * The list items are separated with even space, and one item animation starts after the
     * previous animation during basic sliding interactions. The chained animation effect is
     * similar with spring physics.
     * For chained animations to work properly, the edge scrolling effect of the **ArcList**
     * component must be set to **EdgeEffect.Spring**.
     *
     * @param { Optional<boolean> } enable - Whether to enable chained animations.<br/>
     *     **false** (default): Chained animations are disabled. **true**: Chained animations are
     *     enabled.
     * @returns { ArcListAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    chainAnimation(enable: Optional<boolean>): ArcListAttribute;
    /**
     * Sets the size information of the child components of the **ArcList** component along the
     * main axis.
     *
     * @param { Optional<ChildrenMainSize> } size - Precise size information for all child
     *     components along the main axis. This ensures accurate scrolling positions in scenarios
     *     where child components have varying sizes, are added or removed, or when APIs like
     *     **scrollToIndex** are used. It guarantees that **scrollTo** can accurately navigate to
     *     the specified position, **currentOffset** or **offset** can accurately reflect the
     *     current scrolling position, and the built-in scrollbar can move smoothly without any
     *     jumps or abrupt changes. The **offset** API is added from API version 23.<br/>
     *     **NOTE**<br/>The provided sizes must match the actual sizes of the child components.
     *     Any changes to the sizes, or any additions or removals of child components, must be
     *     notified to the **ArcList** component through the **ChildrenMainSize** object.
     * @returns { ArcListAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    childrenMainSize(size: Optional<ChildrenMainSize>): ArcListAttribute;
    /**
     * Sets whether to enable scroll gestures.
     *
     * @param { Optional<boolean> } enable - Whether to enable scroll gestures. With the value
     *     **true**, scrolling via finger or mouse is enabled. With the value **false**, scrolling
     *     via finger or mouse is disabled, but this does not affect the scrolling APIs of the
     *     **Scroller**.<br/>Default value: **true**
     * @returns { ArcListAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    enableScrollInteraction(enable: Optional<boolean>): ArcListAttribute;
    /**
     * Sets whether to enable the edge fading effect.
     *
     * @param { Optional<boolean> } enable - Whether to enable the edge fading effect.<br/>
     *     When **fadingEdge** is set to **true**, it overrides the **.overlay()** attribute of
     *     the component.<br/>With **fadingEdge** set to **true**, avoid setting background-related
     *     attributes on the component, as this may affect the display of the fading effect.<br/>
     *     When **fadingEdge** is set to **true**, the component is clipped to the boundary. If the
     *     **clip** attribute of the component is set to **false**, the setting does not take
     *     effect.<br/>With the value **true**, the edge fading effect is enabled. With the value
     *     **false**, the edge fading effect is disabled.<br/>Default value: **false**.
     * @returns { ArcListAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    fadingEdge(enable: Optional<boolean>): ArcListAttribute;
    /**
     * Sets the friction coefficient. It applies only to gestures in the scrolling area, and it
     * affects only the inertial scrolling process. If this attribute is set to a value less than
     * or equal to 0, the default value is used.
     *
     * @param { Optional<number> } friction - Friction coefficient.<br/>
     *     Default value: **0.8**<br/>Value range: (0, +∞)
     * @returns { ArcListAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    friction(friction: Optional<number>): ArcListAttribute;
    /**
     * Sets the maximum initial speed for inertial scrolling after a fling gesture. If this
     * attribute is set to a value less than or equal to 0, the default value is used.
     *
     * @param { Optional<number> } speed - Maximum initial speed for inertial scrolling.<br/>
     *     Default value: **9000**.<br/>Unit: vp/s.<br/>Value range: (0, +∞)
     * @returns { ArcListAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    flingSpeedLimit(speed: Optional<number>): ArcListAttribute;
    /**
     * Triggered when a child component enters or leaves the visible area of the **ArcList**
     * component. This event is triggered during initialization of the **ArcList** component and
     * when the index of the first or last child component in the visible area changes, or when
     * the center child component changes.
     * If the edge scrolling effect of the **ArcList** component is set to spring, this event is
     * not triggered during continued scrolling at the edge or during the bounce-back process.
     *
     * @param { Optional<ArcScrollIndexHandler> } handler - Callback triggered when a child
     *     component enters or leaves the visible area of the **ArcList** component.
     * @returns { ArcListAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    onScrollIndex(handler: Optional<ArcScrollIndexHandler>): ArcListAttribute;
    /**
     * Triggered when the list reaches the start position.
     * This event is triggered during initialization of the **ArcList** component if
     * **initialIndex** is set to **0**, and whenever the list scrolls to the start position.
     * If the edge scrolling effect is set to spring, this event is triggered when scrolling past
     * the start position and again when bouncing back to it.
     *
     * @param { Optional<VoidCallback> } handler - Callback triggered when the list reaches the
     *     start position.
     * @returns { ArcListAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    onReachStart(handler: Optional<VoidCallback>): ArcListAttribute;
    /**
     * Triggered when the list reaches the end position.
     * If the edge scrolling effect is set to spring, this event is triggered when scrolling past
     * the end position and again when bouncing back to it.
     *
     * @param { Optional<VoidCallback> } handler - Callback triggered when the list reaches the
     *     end position.
     * @returns { ArcListAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    onReachEnd(handler: Optional<VoidCallback>): ArcListAttribute;
    /**
     * Triggered when the list starts scrolling initiated by the user's finger dragging the list
     * or its scrollbar. This event is also triggered when the animation contained in the
     * scrolling triggered by **Scroller** starts.
     *
     * @param { Optional<VoidCallback> } handler - Callback triggered when the list starts
     *     scrolling.
     * @returns { ArcListAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    onScrollStart(handler: Optional<VoidCallback>): ArcListAttribute;
    /**
     * Triggered when the list stops scrolling after the user's finger leaves the screen.
     * This event is also triggered when the animation contained in the scrolling triggered by
     * **Scroller** stops.
     *
     * @param { Optional<VoidCallback> } handler - Callback triggered when the list stops
     *     scrolling.
     * @returns { ArcListAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    onScrollStop(handler: Optional<VoidCallback>): ArcListAttribute;
    /**
     * Triggered before each frame during list scrolling. The callback returns the offset amount
     * by which the list will scroll and the current scroll state. The returned offset is a
     * calculated value, not the actual offset.
     *
     * @param { Optional<OnWillScrollCallback> } handler - Callback triggered before each frame
     *     during list scrolling.
     * @returns { ArcListAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    onWillScroll(handler: Optional<OnWillScrollCallback>): ArcListAttribute;
    /**
     * Triggered when the list scrolls. The return value is the offset amount by which the list
     * has scrolled and the current scroll state.
     *
     * @param { Optional<OnScrollCallback> } handler - Callback triggered when the list scrolls.
     * @returns { ArcListAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    onDidScroll(handler: Optional<OnScrollCallback>): ArcListAttribute;
}
/**
 * In addition to the [universal attributes]{@link common}, the following attributes are
 * supported.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Circle
 * @crossplatform
 * @atomicservice
 * @since 18
 * @noninterop
 */
export declare class ArcListItemAttribute extends CommonMethod<ArcListItemAttribute> {
    /**
     * Sets whether to enable auto-scaling for the **ArcListItem** component.
     *
     * @param { Optional<boolean> } enable - Whether to enable auto-scaling.<br>**true**: Enable auto-scaling.<br>
     *     **false**: Disable auto-scaling.<br>Default value: **true**.
     * @returns { ArcListItemAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    autoScale(enable: Optional<boolean>): ArcListItemAttribute;
    /**
     * Sets the swipe action item displayed when the **ArcListItem** component is swiped out from the screen edge.
     *
     * @param { Optional<SwipeActionOptions> } options - Swipe action item displayed when the **ArcListItem** component is
     *     swiped out from the screen edge.
     * @returns { ArcListItemAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    swipeAction(options: Optional<SwipeActionOptions>): ArcListItemAttribute;
}
/**
 * Defines ArcList Component instance.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Circle
 * @crossplatform
 * @atomicservice
 * @since 18
 * @noninterop
 */
export declare const ArcListInstance: ArcListAttribute;
/**
 * Defines ArcListItem Component instance.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Circle
 * @crossplatform
 * @atomicservice
 * @since 18
 * @noninterop
 */
export declare const ArcListItemInstance: ArcListItemAttribute;
/**
 * The **ArcList** component is a circular layout container that displays a series of list items
 * in an arc shape. It is suitable for presenting homogeneous data, such as images and text,
 * in a continuous, multi-row format.
 *
 * > **NOTE**
 *
 * > - This component is supported since API version 18. Updates will be marked with a
 * > superscript to indicate their earliest API version.
 * >
 * > - This component can be used on phones, PCs, 2-in-1 devices, tablets, TVs, and wearables.
 * > In API version 22 and earlier versions, a compilation warning will be reported when this
 * > component is used on phones, PCs, 2-in-1 devices, tablets, and TVs, but the component can
 * > still run properly.
 *
 * ###### Child Components
 *
 * Only the [ArcListItem]{@link @ohos.arkui.ArcList} component is supported.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Circle
 * @crossplatform
 * @atomicservice
 * @uicomponent [since 19]
 * @since 18
 * @noninterop
 */
export declare const ArcList: ArcListInterface;
/**
 * The **ArcListItem** component is used to display individual child components in an
 * [ArcList]{@link @ohos.arkui.ArcList} component and must be used in conjunction with **ArcList**.
 *
 * > **NOTE**
 *
 * > - This component can be used only as a child of [ArcList]{@link @ohos.arkui.ArcList}.
 * >
 * > - When this component is used with
 * > [LazyForEach](docroot://ui/rendering-control/arkts-rendering-control-lazyforeach.md), its child components are
 * > created when it is created. When this component is used with
 * > [if/else](docroot://ui/rendering-control/arkts-rendering-control-ifelse.md) or
 * > [ForEach](docroot://ui/rendering-control/arkts-rendering-control-foreach.md), or when the parent component is
 * > [ArcList]{@link @ohos.arkui.ArcList}, its child components are created when it is laid out.
 * >
 * > - This component can be used on phones, PCs, 2-in-1 devices, tablets, TVs, and wearables. In API version 22 and
 * > earlier versions, a compilation warning will be reported when this component is used on phones, PCs, 2-in-1 devices
 * > , tablets, and TVs, but the component can still run properly.
 *
 * ###### Child Components
 *
 * This component can contain a single child component.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Circle
 * @crossplatform
 * @atomicservice
 * @uicomponent [since 19]
 * @since 18
 * @noninterop
 */
export declare const ArcListItem: ArcListItemInterface;

```
