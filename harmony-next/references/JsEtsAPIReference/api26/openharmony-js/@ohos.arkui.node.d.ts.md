# @ohos.arkui.node.d.ts

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
 * @kit ArkUI
 */
/**
 * Export NodeRenderType, RenderOptions, BuilderNode, which is used to create a node trees by builder function and
 * manage the update of the tree.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice [since 12]
 * @since 11
 */
export { NodeRenderType, RenderOptions, BuilderNode } from './arkui/BuilderNode';
/**
 * Export BuildOptions which is used to create a node trees by builder function and manage the update of the tree.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 12
 */
export { BuildOptions } from './arkui/BuilderNode';
/**
 * Export InputEventType which refers to the event type used for posting.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 20
 */
export { InputEventType } from './arkui/BuilderNode';
/**
 * Export ReactiveBuilderNode, which is used to create a node trees by builder function and manage the update of the
 * tree.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 22
 */
export { ReactiveBuilderNode } from './arkui/BuilderNode';
/**
 * Export NodeController, which defines the controller of node container. Provides lifecycle callbacks for the
 * associated NodeContainer and methods to control the child node of the NodeContainer.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice [since 12]
 * @since 11
 */
export { NodeController } from './arkui/NodeController';
/**
 * Export FrameNode. FrameNode defines a basic type of node which contains a RenderNode.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice [since 12]
 * @since 11
 */
export { FrameNode, LayoutConstraint, ExpandMode, UIState } from './arkui/FrameNode';
/**
 * Export ChildrenCountMode.
 * Specifies how to count children when querying number of child nodes.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @atomicservice
 * @since 26.0.0
 */
export { ChildrenCountMode } from './arkui/FrameNode';
/**
 * Export typeNode, NodeAdapter.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 12
 */
export { typeNode, NodeAdapter } from './arkui/FrameNode';
/**
 * Export Graphics. Defines the basic types related to the Graphics.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice [since 12]
 * @since 11
 */
export { DrawContext, Size, Offset, Position, Pivot, Scale, Translation, Matrix4, Rotation, Frame, RoundRect, Circle, CommandPath, ShapeMask, ShapeClip, BorderRadiuses, CornerRadius, Rect, Edges, edgeColors, edgeWidths, borderStyles, borderRadiuses, LengthMetricsUnit } from './arkui/Graphics';
/**
 * Export Graphics. Defines the basic types related to the Graphics.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 12
 */
export { LengthUnit, SizeT, LengthMetrics, ColorMetrics } from './arkui/Graphics';
/**
 * Export Graphics. Defines the blur effect to the Graphics.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @atomicservice
 * @since 26.0.0
 */
export { BackgroundBlur, ContentBlur, ForegroundBlur } from './arkui/Graphics';
/**
 * Export RenderNode. RenderNode contains node tree operations and render property operations on node.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice [since 12]
 * @since 11
 */
export { RenderNode } from './arkui/RenderNode';
/**
 * Export XComponentNode, which extends FrameNode.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice [since 12]
 * @since 11
 */
export { XComponentNode } from './arkui/XComponentNode';
/**
 * Export Content.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 12
 */
export { Content } from './arkui/Content';
/**
 * Export ComponentContent, ComponentContentBase.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 12
 */
export { ComponentContent, ComponentContentBase } from './arkui/ComponentContent';
/**
 * Export ReactiveComponentContent.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 22
 */
export { ReactiveComponentContent } from './arkui/ComponentContent';
/**
 * Export NodeContent.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 12
 */
export { NodeContent } from './arkui/NodeContent';

```
