# @ohos.multimodalInput.mouseEvent.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022-2025 Huawei Device Co., Ltd.
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
 * The **mouseEvent** module provides mouse events reported by a device. It is inherited from
 * [InputEvent]{@link @ohos.multimodalInput.inputEvent:InputEvent}.
 *
 * @file Mouse Event
 * @kit InputKit
 */
import type { InputEvent } from './@ohos.multimodalInput.inputEvent';
import type { KeyCode } from './@ohos.multimodalInput.keyCode';
/**
 * Enumerates mouse event types.
 *
 * @syscap SystemCapability.MultimodalInput.Input.Core
 * @since 9
 */
export declare enum Action {
    /**
     * Canceled. The down event of the mouse is interrupted unexpectedly and does not close normally. For example, the
     * **CANCEL** event is triggered when the mouse button is pressed but not released, the window transitions to the
     * background, or an abnormal destruction occurs.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    CANCEL = 0,
    /**
     * Moving of the mouse pointer.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    MOVE = 1,
    /**
     * Mouse button press.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    BUTTON_DOWN = 2,
    /**
     * Mouse button release.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    BUTTON_UP = 3,
    /**
     * Beginning of the mouse axis event.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    AXIS_BEGIN = 4,
    /**
     * Updating of the mouse axis event.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    AXIS_UPDATE = 5,
    /**
     * Mouse axis event ended.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    AXIS_END = 6,
    /**
     * Touchpad press.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 11
     */
    ACTION_DOWN = 7,
    /**
     * Touchpad release.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 11
     */
    ACTION_UP = 8
}
/**
 * Enumerates mouse buttons.
 *
 * @syscap SystemCapability.MultimodalInput.Input.Core
 * @since 9
 */
export declare enum Button {
    /**
     * Left button.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    LEFT = 0,
    /**
     * Middle button.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    MIDDLE = 1,
    /**
     * Right button
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    RIGHT = 2,
    /**
     * Side button.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    SIDE = 3,
    /**
     * Extended button.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    EXTRA = 4,
    /**
     * Forward button.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    FORWARD = 5,
    /**
     * Back button.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    BACK = 6,
    /**
     * Task button.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    TASK = 7
}
/**
 * Enumerates mouse axis types.
 *
 * @syscap SystemCapability.MultimodalInput.Input.Core
 * @since 9
 */
export declare enum Axis {
    /**
     * Vertical scroll axis of the mouse.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    SCROLL_VERTICAL = 0,
    /**
     * Horizontal scroll axis of the mouse.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    SCROLL_HORIZONTAL = 1,
    /**
     * Pinch axis of the mouse.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    PINCH = 2
}
/**
 * Defines the mouse axis type and axis value.
 *
 * @syscap SystemCapability.MultimodalInput.Input.Core
 * @since 9
 */
export declare interface AxisValue {
    /**
     * Mouse axis type.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    axis: Axis;
    /**
     * Mouse axis value.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    value: number;
}
/**
 * Enumerates tool types.
 *
 * @syscap SystemCapability.MultimodalInput.Input.Core
 * @since 11
 */
export declare enum ToolType {
    /**
     * Unknown type.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 11
     */
    UNKNOWN = 0,
    /**
     * Mouse.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 11
     */
    MOUSE = 1,
    /**
     * Joystick.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 11
     */
    JOYSTICK = 2,
    /**
     * Touchpad.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 11
     */
    TOUCHPAD = 3
}
/**
 * Defines the mouse event.
 *
 * @syscap SystemCapability.MultimodalInput.Input.Core
 * @since 9
 */
export declare interface MouseEvent extends InputEvent {
    /**
     * Enumerates mouse event types.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    action: Action;
    /**
     * X coordinate of the mouse event in the relative coordinate system with the upper left corner of the specified
     * screen as the origin, in px. Currently, the value can only be an integer.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    screenX: number;
    /**
     * Y coordinate of the mouse event in the relative coordinate system with the upper left corner of the specified
     * screen as the origin, in px. Currently, the value can only be an integer.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    screenY: number;
    /**
     * X coordinate in the relative coordinate system with the upper left corner of the window where the mouse is located
     * as the origin, in px. Currently, the value can only be an integer.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    windowX: number;
    /**
     * Y coordinate in the relative coordinate system with the upper left corner of the window where the mouse is located
     * as the origin, in px. Currently, the value can only be an integer.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    windowY: number;
    /**
     * X coordinate offset of the current mouse event relative to the previous event, in px. Currently, the value can only
     * be an integer.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    rawDeltaX: number;
    /**
     * Y coordinate offset of the current mouse event relative to the previous event, in px. Currently, the value can only
     * be an integer.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    rawDeltaY: number;
    /**
     * Enumerates mouse buttons.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    button: Button;
    /**
     * Button being pressed.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    pressedButtons: Button[];
    /**
     * Defines the mouse axis type and axis value.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    axes: AxisValue[];
    /**
     * List of pressed keys.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    pressedKeys: KeyCode[];
    /**
     * Whether ctrlKey is being pressed.
     *
     * The value **true** indicates that the key is pressed, and the value **false** indicates the opposite.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    ctrlKey: boolean;
    /**
     * Whether altKey is being pressed.
     *
     * The value **true** indicates that the key is pressed, and the value **false** indicates the opposite.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    altKey: boolean;
    /**
     * Whether shiftKey is being pressed.
     *
     * The value **true** indicates that the key is pressed, and the value **false** indicates the opposite.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    shiftKey: boolean;
    /**
     * Whether logoKey is being pressed.
     *
     * The value **true** indicates that the key is pressed, and the value **false** indicates the opposite.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    logoKey: boolean;
    /**
     * Whether fnKey is being pressed.
     *
     * The value **true** indicates that the key is pressed, and the value **false** indicates the opposite.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    fnKey: boolean;
    /**
     * Whether capsLock is enabled.
     *
     * The value **true** indicates that capsLock is enabled, and the value **false** indicates the opposite.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    capsLock: boolean;
    /**
     * Whether numLock is enabled.
     *
     * The value **true** indicates that numLock is enabled, and the value **false** indicates the opposite.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    numLock: boolean;
    /**
     * Whether scrollLock is enabled.
     *
     * The value **true** indicates that scrollLock is enabled, and the value **false** indicates the opposite.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    scrollLock: boolean;
    /**
     * Tool type.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 11
     */
    toolType: ToolType;
    /**
     * X coordinate of the mouse event in the global coordinate system with the upper left corner of the primary screen as
     * the origin, in px. When this parameter is used as an input parameter, it is mandatory and supports only integers if
     * [MouseEventData.useGlobalCoordinate]{@link @ohos.multimodalInput.inputEventClient:inputEventClient.MouseEventData}
     * is set to **true**. If **MouseEventData.useGlobalCoordinate** is set to **false**, this parameter is optional, and
     * the X coordinate in the relative coordinate system with the upper left corner of the specified screen as the origin
     * is used to calculate the injected event. When this parameter is used as an output parameter, it is reported by the
     * system.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 20
     */
    globalX?: number;
    /**
     * Y coordinate of the mouse event in the global coordinate system with the upper left corner of the primary screen as
     * the origin, in px. When this parameter is used as an input parameter, it is mandatory and supports only integers if
     * [MouseEventData.useGlobalCoordinate]{@link @ohos.multimodalInput.inputEventClient:inputEventClient.MouseEventData}
     * is set to **true**. If **MouseEventData.useGlobalCoordinate** is set to **false**, this parameter is optional, and
     * the Y coordinate in the relative coordinate system with the upper left corner of the specified screen as the origin
     * is used to calculate the injected event. When this parameter is used as an output parameter, it is reported by the
     * system.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 20
     */
    globalY?: number;
}

```
