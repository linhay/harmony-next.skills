# @ohos.multimodalInput.touchEvent.d.ts

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
 * The **touchEvent** module provides touch events reported by a device. It is inherited from
 * [InputEvent]{@link @ohos.multimodalInput.inputEvent:InputEvent}.
 *
 * @file Touch Event
 * @kit InputKit
 */
import type { InputEvent } from './@ohos.multimodalInput.inputEvent';
/**
 * Enumerates the touch event types.
 *
 * @syscap SystemCapability.MultimodalInput.Input.Core
 * @since 9
 */
export declare enum Action {
    /**
     * Touch canceled. The **DOWN** event of the touchscreen is interrupted unexpectedly and does not close normally. For
     * example, the **CANCEL** event is triggered when the finger is pressed but not lifted, the screen is rotated or
     * folded, or a new hover occurs.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    CANCEL = 0,
    /**
     * Touch down.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    DOWN = 1,
    /**
     * Touch moved.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    MOVE = 2,
    /**
     * Touch up.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    UP = 3,
    /**
     * Drag started.
     *
     * **Since**: 26.0.0
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    PULL_DOWN = 4,
    /**
     * Dragging.
     *
     * **Since**: 26.0.0
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    PULL_MOVE = 5,
    /**
     * Drag ended.
     *
     * **Since**: 26.0.0
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    PULL_UP = 6
}
/**
 * Enumerates touch tool types.
 *
 * @syscap SystemCapability.MultimodalInput.Input.Core
 * @since 9
 */
export declare enum ToolType {
    /**
     * Finger.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    FINGER = 0,
    /**
     * Stylus.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    PEN = 1,
    /**
     * Eraser.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    RUBBER = 2,
    /**
     * Brush.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    BRUSH = 3,
    /**
     * Pencil.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    PENCIL = 4,
    /**
     * Air brush.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    AIRBRUSH = 5,
    /**
     * Mouse.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    MOUSE = 6,
    /**
     * Lens.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    LENS = 7
}
/**
 * Enumerates touch sources. Currently, only the touchscreen and touchpad are supported.
 *
 * @syscap SystemCapability.MultimodalInput.Input.Core
 * @since 9
 */
export declare enum SourceType {
    /**
     * Touchscreen.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    TOUCH_SCREEN = 0,
    /**
     * Stylus.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    PEN = 1,
    /**
     * Touchpad.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    TOUCH_PAD = 2
}
/**
 * Defines the touch point information.
 *
 * @syscap SystemCapability.MultimodalInput.Input.Core
 * @since 9
 */
export declare interface Touch {
    /**
     * Touch event ID.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    id: number;
    /**
     * Press timestamp, in microseconds (μs) since the system starts.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    pressedTime: number;
    /**
     * X coordinate of the touch event in the relative coordinate system with the upper-left corner of the specified
     * screen as the origin. Currently, only integers are supported. The unit is pixels.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    screenX: number;
    /**
     * Y coordinate of the touch event in the relative coordinate system with the upper-left corner of the specified
     * screen as the origin. Currently, only integers are supported. The unit is pixels.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    screenY: number;
    /**
     * X coordinate in the relative coordinate system with the upper-left corner of the window where the touch is located
     * as the origin. Currently, only integers are supported. The unit is pixels.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    windowX: number;
    /**
     * Y coordinate in the relative coordinate system with the upper-left corner of the window where the touch is located
     * as the origin. Currently, only integers are supported. The unit is pixels.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    windowY: number;
    /**
     * Pressure value. The value range is [0.0, 1.0]. The value **0.0** indicates that the pressure is not supported.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    pressure: number;
    /**
     * Width of the touch area, in pixels. The value can only be an integer.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    width: number;
    /**
     * Height of the touch area, in pixels. The value can only be an integer.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    height: number;
    /**
     * Angle relative to the YZ plane, in degrees. The value range is [-90, 90]. A positive value indicates a rightward
     * tilt.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    tiltX: number;
    /**
     * Angle relative to the XZ plane, in degrees. The value range is [-90, 90]. A positive value indicates a downward
     * tilt.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    tiltY: number;
    /**
     * X coordinate of the tool area center in the relative coordinate system with the upper-left corner of the specified
     * screen as the origin. Currently, only integers are supported. The unit is pixels.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    toolX: number;
    /**
     * Y coordinate of the tool area center in the relative coordinate system with the upper-left corner of the specified
     * screen as the origin. Currently, only integers are supported. The unit is pixels.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    toolY: number;
    /**
     * Width of the tool area, in pixels. The value can only be an integer.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    toolWidth: number;
    /**
     * Height of the tool area, in pixels. The value can only be an integer.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    toolHeight: number;
    /**
     * X coordinate of the input device. Currently, only integers are supported. The unit is pixels.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    rawX: number;
    /**
     * Y coordinate of the input device. Currently, only integers are supported. The unit is pixels.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    rawY: number;
    /**
     * Tool type.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    toolType: ToolType;
    /**
     * X coordinate of the touch event in the global coordinate system with the upper-left corner of the primary screen as
     * the origin, in px. <!--Del--> When being used as an input parameter, this parameter is mandatory if the value of
     * [TouchEventData.useGlobalCoordinate]{@link @ohos.multimodalInput.inputEventClient:inputEventClient.TouchEventData}
     * is **true**, and its value can only be an integer. Otherwise, you do not need to set this parameter. In this case,
     * the X coordinate of the relative coordinate system with the upper left corner of the specified screen as the origin
     * is used to calculate the injected event. <!--DelEnd-->When being used as an output parameter, its value is reported
     * by the system.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 20
     */
    globalX?: number;
    /**
     * Y coordinate of the touch event in the global coordinate system with the upper-left corner of the primary screen as
     * the origin, in px. <!--Del--> When being used as an input parameter, this parameter is mandatory if the value of
     * [TouchEventData.useGlobalCoordinate]{@link @ohos.multimodalInput.inputEventClient:inputEventClient.TouchEventData}
     * is **true**, and its value can only be an integer. Otherwise, you do not need to set this parameter. In this case,
     * the Y coordinate of the relative coordinate system with the upper left corner of the specified screen as the origin
     * is used to calculate the injected event. <!--DelEnd-->When being used as an output parameter, its value is reported
     * by the system.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 20
     */
    globalY?: number;
}
/**
 * Defines a touch event.
 *
 * @syscap SystemCapability.MultimodalInput.Input.Core
 * @since 9
 */
export declare interface TouchEvent extends InputEvent {
    /**
     * Event type.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    action: Action;
    /**
     * Current touch point.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    touch: Touch;
    /**
     * All touch points.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    touches: Touch[];
    /**
     * Device type of the touch source.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Core
     * @since 9
     */
    sourceType: SourceType;
}

```
