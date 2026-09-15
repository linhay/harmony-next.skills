# @ohos.multimodalInput.inputEventClient.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (C) 2021-2026 Huawei Device Co., Ltd.
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
 * @file Input Event Injection
 * @kit InputKit
 */
import { Button, Axis } from './@ohos.multimodalInput.mouseEvent';
import { KeyCode } from './@ohos.multimodalInput.keyCode';
/**
 * The **inputEventClient** module provides the capability of injecting key, mouse/touchpad, and touchscreen events.
 *
 * @syscap SystemCapability.MultimodalInput.Input.InputSimulator
 * @since 26.0.0
 */
declare namespace inputEventClient {
    /**
     * Provides the capability of simulating key operations. The simulated key operation sequence must meet the following
     * requirements:
     *
     * 1. A key can only be pressed when it is in the released state, or when it is the most recently pressed key and
     * has not been released.
     * 2. A key can only be released after it has been pressed.
     * 3. A maximum of five keys can be pressed and held simultaneously.
     *
     * @syscap SystemCapability.MultimodalInput.Input.InputSimulator
     * @stagemodelonly
     * @since 26.0.0
     */
    interface KeyboardController {
        /**
         * Presses a key. This API uses a promise to return the result.
         *
         * @permission ohos.permission.CONTROL_DEVICE
         * @param { KeyCode } keyCode - Key code of the key to be pressed.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 201 - Permission verification failed.
         *     The application does not have the permission required to call the API.
         * @throws { BusinessError } 4300001 - The key is already pressed and is not the most recently
         *     pressed key.
         * @throws { BusinessError } 3800001 - Input service exception.
         * @syscap SystemCapability.MultimodalInput.Input.InputSimulator
         * @stagemodelonly
         * @since 26.0.0
         */
        pressKey(keyCode: KeyCode): Promise<void>;
        /**
         * Releases a key. This API uses a promise to return the result.
         *
         * @permission ohos.permission.CONTROL_DEVICE
         * @param { KeyCode } keyCode - Key code of the key to be released.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 201 - Permission verification failed.
         *     The application does not have the permission required to call the API.
         * @throws { BusinessError } 4300001 - The key is not pressed.
         * @throws { BusinessError } 3800001 - Input service exception.
         * @syscap SystemCapability.MultimodalInput.Input.InputSimulator
         * @stagemodelonly
         * @since 26.0.0
         */
        releaseKey(keyCode: KeyCode): Promise<void>;
    }
    /**
     * Creates a keyboard controller for simulating key operations. This API uses a promise to return the result.
     *
     * @permission ohos.permission.CONTROL_DEVICE
     * @returns { Promise<KeyboardController> } Promise used to return the keyboard controller instance.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 3800001 - Input service exception.
     * @syscap SystemCapability.MultimodalInput.Input.InputSimulator
     * @stagemodelonly
     * @since 26.0.0
     */
    function createKeyboardController(): Promise<KeyboardController>;
    /**
     * Provides the capability of simulating mouse operations. The simulated mouse operation sequence must meet the
     * following requirements:
     *
     * 1. A mouse button can be pressed only when it is in the released state.
     * 2. A mouse button can only be released after it has been pressed.
     * 3. A valid axis event sequence must begin with a **beginAxis** call, followed by zero or more **updateAxis** calls,
     * and end with an **endAxis** call.
     * 4. Only one axis event sequence can be in progress at a time.
     *
     * @syscap SystemCapability.MultimodalInput.Input.InputSimulator
     * @stagemodelonly
     * @since 26.0.0
     */
    interface MouseController {
        /**
         * Moves the mouse cursor to the specified display coordinates. This API uses a promise to return the result.
         *
         * @permission ohos.permission.CONTROL_DEVICE
         * @param { number } displayId - ID of the target display.
         * @param { number } displayX - X coordinate relative to the left edge of the display, in px. If the value exceeds the
         *     valid range of the display, the actual coordinate will be clamped to the valid range [0, display width - 1].
         * @param { number } displayY - Y coordinate relative to the top edge of the display, in px. If the value exceeds the
         *     valid range of the display, the actual coordinate will be clamped to the valid range [0, display height - 1].
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 201 - Permission verification failed.
         *     The application does not have the permission required to call the API.
         * @throws { BusinessError } 4300002 - The display does not exist.
         * @throws { BusinessError } 3800001 - Input service exception.
         * @syscap SystemCapability.MultimodalInput.Input.InputSimulator
         * @stagemodelonly
         * @since 26.0.0
         */
        moveTo(displayId: number, displayX: number, displayY: number): Promise<void>;
        /**
         * Presses a mouse button. This API uses a promise to return the result.
         *
         * @permission ohos.permission.CONTROL_DEVICE
         * @param { Button } button - Mouse button to be pressed.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 201 - Permission verification failed.
         *     The application does not have the permission required to call the API.
         * @throws { BusinessError } 4300001 - The mouse button is already pressed.
         * @throws { BusinessError } 3800001 - Input service exception.
         * @syscap SystemCapability.MultimodalInput.Input.InputSimulator
         * @stagemodelonly
         * @since 26.0.0
         */
        pressButton(button: Button): Promise<void>;
        /**
         * Release a mouse button. This API uses a promise to return the result.
         *
         * @permission ohos.permission.CONTROL_DEVICE
         * @param { Button } button - Mouse button to be released.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 201 - Permission verification failed.
         *     The application does not have the permission required to call the API.
         * @throws { BusinessError } 4300001 - The mouse button is not pressed.
         * @throws { BusinessError } 3800001 - Input service exception.
         * @syscap SystemCapability.MultimodalInput.Input.InputSimulator
         * @stagemodelonly
         * @since 26.0.0
         */
        releaseButton(button: Button): Promise<void>;
        /**
         * Starts an axis event. This API uses a promise to return the result.
         *
         * @permission ohos.permission.CONTROL_DEVICE
         * @param { Axis } axis - Axis type.
         * @param { number } value - Axis value.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 201 - Permission verification failed.
         *     The application does not have the permission required to call the API.
         * @throws { BusinessError } 4300001 - The axis event is in progress.
         * @throws { BusinessError } 3800001 - Input service exception.
         * @syscap SystemCapability.MultimodalInput.Input.InputSimulator
         * @stagemodelonly
         * @since 26.0.0
         */
        beginAxis(axis: Axis, value: number): Promise<void>;
        /**
         * Updates an axis event. This API uses a promise to return the result.
         *
         * @permission ohos.permission.CONTROL_DEVICE
         * @param { Axis } axis - Axis type.
         * @param { number } value - Axis value.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 201 - Permission verification failed.
         *     The application does not have the permission required to call the API.
         * @throws { BusinessError } 4300001 - The axis event is not in progress.
         * @throws { BusinessError } 3800001 - Input service exception.
         * @syscap SystemCapability.MultimodalInput.Input.InputSimulator
         * @stagemodelonly
         * @since 26.0.0
         */
        updateAxis(axis: Axis, value: number): Promise<void>;
        /**
         * Ends an axis event. This API uses a promise to return the result.
         *
         * @permission ohos.permission.CONTROL_DEVICE
         * @param { Axis } axis - Axis type.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 201 - Permission verification failed.
         *     The application does not have the permission required to call the API.
         * @throws { BusinessError } 4300001 - The axis event is not in progress.
         * @throws { BusinessError } 3800001 - Input service exception.
         * @syscap SystemCapability.MultimodalInput.Input.InputSimulator
         * @stagemodelonly
         * @since 26.0.0
         */
        endAxis(axis: Axis): Promise<void>;
    }
    /**
     * Creates a mouse controller for simulating mouse operations. This API uses a promise to return the result.
     *
     * @permission ohos.permission.CONTROL_DEVICE
     * @returns { Promise<MouseController> } Promise used to return the mouse controller instance.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 3800001 - Input service exception.
     * @syscap SystemCapability.MultimodalInput.Input.InputSimulator
     * @stagemodelonly
     * @since 26.0.0
     */
    function createMouseController(): Promise<MouseController>;
    /**
     * Represents information about a single touch point on the display.
     *
     * @syscap SystemCapability.MultimodalInput.Input.InputSimulator
     * @stagemodelonly
     * @since 26.0.0
     */
    interface TouchPoint {
        /**
         * Unique ID of a touch point. The value must be an integer in the range of [0, 9].
         *
         * @syscap SystemCapability.MultimodalInput.Input.InputSimulator
         * @stagemodelonly
         * @since 26.0.0
         */
        id: number;
        /**
         * Unique ID of the display where the touch point is located. The value must be an integer.
         *
         * @syscap SystemCapability.MultimodalInput.Input.InputSimulator
         * @stagemodelonly
         * @since 26.0.0
         */
        displayId: number;
        /**
         * X coordinate of the touch point relative to the left edge of the display, in pixels. The value must be an
         * integer.
         *
         * @syscap SystemCapability.MultimodalInput.Input.InputSimulator
         * @stagemodelonly
         * @since 26.0.0
         */
        displayX: number;
        /**
         * Y coordinate of the touch point relative to the top edge of the display, in pixels. The value must be an integer.
         *
         * @syscap SystemCapability.MultimodalInput.Input.InputSimulator
         * @stagemodelonly
         * @since 26.0.0
         */
        displayY: number;
    }
    /**
     * Provides the capability of simulating touch operations. The simulated touch operation sequence must meet the
     * following requirements:
     *
     * 1. All touch points must share the same **displayId**.
     * 2. Each touch point must begin with a **touchDown()** call, followed by zero or more **touchMove()** calls, and end
     * with an **touchUp()** call.
     *
     * @syscap SystemCapability.MultimodalInput.Input.InputSimulator
     * @stagemodelonly
     * @since 26.0.0
     */
    interface TouchController {
        /**
         * Presses down a touch point. This API uses a promise to return the result.
         *
         * @permission ohos.permission.CONTROL_DEVICE
         * @param { TouchPoint } touch - Information about the touch point that is in contact with the display.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 201 - Permission verification failed.
         *     The application does not have the permission required to call the API.
         * @throws { BusinessError } 4300001 - Invalid input event sequence. Possible causes:
         *     <br>1. The touch point is touching the display;
         *     <br>2. The touch point ID is not within the valid range [0,9].
         * @throws { BusinessError } 4300002 - The display does not exist.
         * @throws { BusinessError } 3800001 - Input service exception.
         * @syscap SystemCapability.MultimodalInput.Input.InputSimulator
         * @stagemodelonly
         * @since 26.0.0
         */
        touchDown(touch: TouchPoint): Promise<void>;
        /**
         * Moves a touch point. This API uses a promise to return the result.
         *
         * @permission ohos.permission.CONTROL_DEVICE
         * @param { TouchPoint } touch - Information about the touch point to be moved.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 201 - Permission verification failed.
         *     The application does not have the permission required to call the API.
         * @throws { BusinessError } 4300001 - Invalid input event sequence. Possible causes:
         *     <br>1. The touch point is not touching the display;
         *     <br>2. The touch point ID is not within the valid range [0,9].
         * @throws { BusinessError } 3800001 - Input service exception.
         * @syscap SystemCapability.MultimodalInput.Input.InputSimulator
         * @stagemodelonly
         * @since 26.0.0
         */
        touchMove(touch: TouchPoint): Promise<void>;
        /**
         * Releases a touch point. This API uses a promise to return the result.
         *
         * @permission ohos.permission.CONTROL_DEVICE
         * @param { TouchPoint } touch - Information about the touch point to be released.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 201 - Permission verification failed.
         *     The application does not have the permission required to call the API.
         * @throws { BusinessError } 4300001 - Invalid input event sequence. Possible causes:
         *     <br>1. The touch point is not touching the display;
         *     <br>2. The touch point ID is not within the valid range [0,9].
         * @throws { BusinessError } 3800001 - Input service exception.
         * @syscap SystemCapability.MultimodalInput.Input.InputSimulator
         * @stagemodelonly
         * @since 26.0.0
         */
        touchUp(touch: TouchPoint): Promise<void>;
    }
    /**
     * Creates a touch controller for simulating touch operations. This API uses a promise to return the result.
     *
     * @permission ohos.permission.CONTROL_DEVICE
     * @returns { Promise<TouchController> } Promise used to return the touch controller instance.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 3800001 - Input service exception.
     * @syscap SystemCapability.MultimodalInput.Input.InputSimulator
     * @stagemodelonly
     * @since 26.0.0
     */
    function createTouchController(): Promise<TouchController>;
}
export default inputEventClient;

```
