# @ohos.arkui.components.ArkDynamicLayout.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2026 Huawei Device Co., Ltd.
 * Licensed under the Apache License, Version 2.0 (the "License"),
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
import { LayoutAlgorithm } from './arkui/LayoutAlgorithm';
/**
 * Defines the dynamic layout container.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @form
 * @atomicservice
 * @since 24
 */
export interface DynamicLayoutInterface {
    /**
     * Defines the dynamic layout container.
     *
     * @param { LayoutAlgorithm } algorithm - Layout algorithm of the dynamic layout component. If an invalid value is
     *     used, the child components are stacked and arranged according to
     *     [StackLayoutAlgorithm](docroot://reference/apis-arkui/js-apis-arkui-layoutAlgorithm.md#stacklayoutalgorithm).
     * @returns { DynamicLayoutAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @form
     * @atomicservice
     * @since 24
     */
    (algorithm: LayoutAlgorithm): DynamicLayoutAttribute;
}
/**
 * The [universal attributes]{@link CommonMethod} are supported.
 *
 * > **NOTE**
 * >
 * > - When the layout algorithm is [RowLayoutAlgorithm]{@link ./arkui/LayoutAlgorithm:RowLayoutAlgorithm} or
 * > [ColumnLayoutAlgorithm]{@link ./arkui/LayoutAlgorithm:ColumnLayoutAlgorithm},
 * > the [Flex layout](docroot://reference/apis-arkui/arkui-ts/ts-universal-attributes-flex-layout.md) attributes set
 * > for child components take effect.
 * >
 * > - When the layout algorithm is [StackLayoutAlgorithm]{@link ./arkui/LayoutAlgorithm:StackLayoutAlgorithm},
 * > the [layoutGravity]{@link CommonMethod#layoutGravity} attribute set for child components takes effect.
 * >
 * > - When the layout algorithm is
 * > [CustomLayoutAlgorithm]{@link ./arkui/LayoutAlgorithm:CustomLayoutAlgorithm},
 * > the [setMeasuredSize]{@link ./arkui/FrameNode:FrameNode#setMeasuredSize} method of the
 * > [FrameNode]{@link ./arkui/FrameNode:FrameNode} component of **DynamicLayout** has a higher priority than the
 * > [sizing]{@link CommonMethod#size} and [border styling]{@link CommonMethod#border} attributes. The
 * > [measure]{@link ./arkui/FrameNode:FrameNode#measure} and [layout]{@link ./arkui/FrameNode:FrameNode#layout} methods
 * > of the child component [FrameNode]{@link ./arkui/FrameNode:FrameNode} have a higher priority than the
 * > [ignoreLayoutSafeArea]{@link CommonMethod#ignoreLayoutSafeArea} attribute.
 *
 * The [universal events](docroot://reference/apis-arkui/arkui-ts/ts-component-general-events.md) are supported.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @form
 * @atomicservice
 * @since 24
 */
export declare class DynamicLayoutAttribute extends CommonMethod<DynamicLayoutAttribute> {
}
/**
 * Defines the dynamic layout container component, which supports dynamically switching between different layout
 * algorithms at runtime without changing the status of child components.
 * > **Child Components**
 * >
 * > Child components are supported.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @form
 * @atomicservice
 * @uicomponent
 * @since 24
 */
export declare const DynamicLayout: DynamicLayoutInterface;
/**
 * Defines DynamicLayout Component instance.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @form
 * @atomicservice
 * @uicomponent
 * @since 24
 */
export declare const DynamicLayoutInstance: DynamicLayoutAttribute;

```
