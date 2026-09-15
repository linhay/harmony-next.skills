# @ohos.arkui.ArcScrollBar.d.ts

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
 * Represents the parameters used to construct an **ArcScrollBar** component.
 *
 * > **NOTE**
 * >
 * > **ArcScrollBar** must be bound to a scrollable component through **scroller** to achieve synchronization. Only a
 * > one-to-one binding is allowed between **ArcScrollBar** and a scrollable component.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Circle
 * @crossplatform
 * @atomicservice
 * @since 18
 */
declare interface ArcScrollBarOptions {
    /**
     * Scroller, which can be bound to scrollable components for scrolling control.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    scroller: Scroller;
    /**
     * State of the scrollbar.<br/>Default value: **BarState.Auto**
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    state?: BarState;
}
/**
 * The **ArcScrollBar** component is designed to be used together with scrollable components such as
 * [ArcList]{@link @ohos.arkui.ArcList}, [List]{@link list},
 * [Grid]{@link grid}, [Scroll]{@link scroll}, and
 * [WaterFlow]{@link water_flow}.
 *
 * > **NOTE**
 * >
 * > - This component is supported since API version 18. Updates will be marked with a superscript to indicate their
 * > earliest API version.
 * >
 * > - When the width and height of the **ArcScrollBar** component are not set, the **maxSize** value specified in its
 * > parent component [LayoutConstraint]{@link FrameNode:LayoutConstraint} is used as the width and height. If
 * > the parent component of the **ArcScrollBar** component contains scrollable components, such as
 * > [ArcList]{@link @ohos.arkui.ArcList}, [List]{@link list},
 * > [Grid]{@link grid}, [Scroll]{@link scroll}, or
 * > [WaterFlow]{@link water_flow}, you are advised to set the width and height of the
 * > **ArcScrollBar** component. Otherwise, the width and height of the component may be infinite.
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
export interface ArcScrollBarInterface {
    /**
     * A constructor used to create an **ArcScrollBar** instance.
     *
     * @param { ArcScrollBarOptions } options - Parameters of the **ArcScrollBar** component.
     * @returns { ArcScrollBarAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Circle
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    (options: ArcScrollBarOptions): ArcScrollBarAttribute;
}
/**
 * Defines the arc scroll bar attribute functions.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Circle
 * @crossplatform
 * @atomicservice
 * @since 18
 * @noninterop
 */
export declare class ArcScrollBarAttribute extends CommonMethod<ArcScrollBarAttribute> {
}
/**
 * Defines ArcScrollBar Component instance.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Circle
 * @crossplatform
 * @atomicservice
 * @since 18
 * @noninterop
 */
export declare const ArcScrollBarInstance: ArcScrollBarAttribute;
/**
 * The **ArcScrollBar** component is designed to be used together with scrollable components such as
 * [ArcList]{@link @ohos.arkui.ArcList}, [List]{@link list},
 * [Grid]{@link grid}, [Scroll]{@link scroll}, and
 * [WaterFlow]{@link water_flow}.
 *
 * > **NOTE**
 * >
 * > - This component is supported since API version 18. Updates will be marked with a superscript to indicate their
 * > earliest API version.
 * >
 * > - When the width and height of the **ArcScrollBar** component are not set, the **maxSize** value specified in its
 * > parent component [LayoutConstraint]{@link FrameNode:LayoutConstraint} is used as the width and height. If
 * > the parent component of the **ArcScrollBar** component contains scrollable components, such as
 * > [ArcList]{@link @ohos.arkui.ArcList}, [List]{@link list},
 * > [Grid]{@link grid}, [Scroll]{@link scroll}, or
 * > [WaterFlow]{@link water_flow}, you are advised to set the width and height of the
 * > **ArcScrollBar** component. Otherwise, the width and height of the component may be infinite.
 * >
 * > - This component can be used on phones, PCs, 2-in-1 devices, tablets, TVs, and wearables. In API version 22 and
 * > earlier versions, a compilation warning will be reported when this component is used on phones, PCs, 2-in-1 devices
 * > , tablets, and TVs, but the component can still run properly.
 *
 * ###### Child Components
 *
 * Not supported
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Circle
 * @crossplatform
 * @atomicservice
 * @uicomponent
 * @since 18
 * @noninterop
 */
export declare const ArcScrollBar: ArcScrollBarInterface;

```
