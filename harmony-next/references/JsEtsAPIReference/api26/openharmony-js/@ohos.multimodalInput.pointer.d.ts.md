# @ohos.multimodalInput.pointer.d.ts

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
 * @file Mouse Pointer
 * @kit InputKit
 */
import type { AsyncCallback } from './@ohos.base';
import type image from './@ohos.multimedia.image';
/**
 * The **pointer** module provides APIs related to pointer attribute management, such as querying and setting pointer
 * attributes.
 *
 * @syscap SystemCapability.MultimodalInput.Input.Pointer
 * @atomicservice [since 12]
 * @since 9
 */
declare namespace pointer {
    /**
     * Mouse pointer style types.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Pointer
     * @atomicservice [since 12]
     * @since 9
     */
    enum PointerStyle {
        /**
         * Default
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 9
         */
        DEFAULT = 0,
        /**
         * East arrow
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 9
         */
        EAST = 1,
        /**
         * West arrow
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 9
         */
        WEST = 2,
        /**
         * South arrow
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 9
         */
        SOUTH = 3,
        /**
         * North arrow
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 9
         */
        NORTH = 4,
        /**
         * West-east arrow
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 9
         */
        WEST_EAST = 5,
        /**
         * North-south arrow
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 9
         */
        NORTH_SOUTH = 6,
        /**
         * North-east arrow
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 9
         */
        NORTH_EAST = 7,
        /**
         * North-west arrow
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 9
         */
        NORTH_WEST = 8,
        /**
         * South-east arrow
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 9
         */
        SOUTH_EAST = 9,
        /**
         * South-west arrow
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 9
         */
        SOUTH_WEST = 10,
        /**
         * North-east and south-west adjustment
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 9
         */
        NORTH_EAST_SOUTH_WEST = 11,
        /**
         * North-west and south-east adjustment
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 9
         */
        NORTH_WEST_SOUTH_EAST = 12,
        /**
         * Cross (accurate selection)
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 9
         */
        CROSS = 13,
        /**
         * Copy
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 9
         */
        CURSOR_COPY = 14,
        /**
         * Forbid
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 9
         */
        CURSOR_FORBID = 15,
        /**
         * Color picker
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 9
         */
        COLOR_SUCKER = 16,
        /**
         * Grabbing hand
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 9
         */
        HAND_GRABBING = 17,
        /**
         * Opening hand
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 9
         */
        HAND_OPEN = 18,
        /**
         * Hand-shaped pointer
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 9
         */
        HAND_POINTING = 19,
        /**
         * Help
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 9
         */
        HELP = 20,
        /**
         * Move
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 9
         */
        MOVE = 21,
        /**
         * Left and right resizing
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 9
         */
        RESIZE_LEFT_RIGHT = 22,
        /**
         * Up and down resizing
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 9
         */
        RESIZE_UP_DOWN = 23,
        /**
         * Screenshot crosshair
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 9
         */
        SCREENSHOT_CHOOSE = 24,
        /**
         * Screenshot
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 9
         */
        SCREENSHOT_CURSOR = 25,
        /**
         * Text selection
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 9
         */
        TEXT_CURSOR = 26,
        /**
         * Zoom in
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 9
         */
        ZOOM_IN = 27,
        /**
         * Zoom out
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 9
         */
        ZOOM_OUT = 28,
        /**
         * Scrolling east
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 9
         */
        MIDDLE_BTN_EAST = 29,
        /**
         * Scrolling west
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 9
         */
        MIDDLE_BTN_WEST = 30,
        /**
         * Scrolling south
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 9
         */
        MIDDLE_BTN_SOUTH = 31,
        /**
         * Scrolling north
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 9
         */
        MIDDLE_BTN_NORTH = 32,
        /**
         * Scrolling north-south
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 9
         */
        MIDDLE_BTN_NORTH_SOUTH = 33,
        /**
         * Scrolling north-east
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 9
         */
        MIDDLE_BTN_NORTH_EAST = 34,
        /**
         * Scrolling north-west
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 9
         */
        MIDDLE_BTN_NORTH_WEST = 35,
        /**
         * Scrolling south-east
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 9
         */
        MIDDLE_BTN_SOUTH_EAST = 36,
        /**
         * Scrolling south-west
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 9
         */
        MIDDLE_BTN_SOUTH_WEST = 37,
        /**
         * Moving as a cone in four directions
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 9
         */
        MIDDLE_BTN_NORTH_SOUTH_WEST_EAST = 38,
        /**
         * Horizontal text selection
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 10
         */
        HORIZONTAL_TEXT_CURSOR = 39,
        /**
         * Cross
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 10
         */
        CURSOR_CROSS = 40,
        /**
         * Circle
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 10
         */
        CURSOR_CIRCLE = 41,
        /**
         * Animation loading
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @atomicservice [since 12]
         * @since 10
         */
        LOADING = 42,
        /**
         * Animation running in the background
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @atomicservice [since 12]
         * @since 10
         */
        RUNNING = 43,
        /**
         * Scrolling east-west
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 18
         */
        MIDDLE_BTN_EAST_WEST = 44,
        /**
         * Running in the background (extension 1)
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 22
         */
        RUNNING_LEFT = 45,
        /**
         * Running in the background (extension 2)
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 22
         */
        RUNNING_RIGHT = 46,
        /**
         * Custom circular pointer
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 22
         */
        AECH_DEVELOPER_DEFINED_ICON = 47,
        /**
         * Screen recording
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 20
         */
        SCREENRECORDER_CURSOR = 48,
        /**
         * Floating This pointer can be used only when the stylus enters the air mouse mode and cannot be directly set.
         *
         * In air mouse mode, you can rotate the stylus in the air to control the movement of the virtual pointer on the
         * screen and press the button on the stylus to turn pages up or down. This mode is used for PPT presentation and
         * air gesture control.
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 22
         */
        LASER_CURSOR = 49,
        /**
         * Click This pointer can be used only when the stylus enters the air mouse mode and cannot be directly set.
         *
         * In air mouse mode, you can rotate the stylus in the air to control the movement of the virtual pointer on the
         * screen and press the button on the stylus to turn pages up or down. This mode is used for PPT presentation and
         * air gesture control.
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 22
         */
        LASER_CURSOR_DOT = 50,
        /**
         * Laser pointer This pointer can be used only when the stylus enters the air mouse mode and cannot be directly set.
         *
         * In air mouse mode, you can rotate the stylus in the air to control the movement of the virtual pointer on the
         * screen and press the button on the stylus to turn pages up or down. This mode is used for PPT presentation and
         * air gesture control.
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 22
         */
        LASER_CURSOR_DOT_RED = 51,
        /**
         * Custom pointer. You can use [setCustomCursor]{@link pointer.setCustomCursor} to set a custom pointer. The custom
         * pointer cannot be directly set using [setPointerStyle]{@link pointer.setPointerStyle}.
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 22
         */
        DEVELOPER_DEFINED_ICON = -100
    }
    /**
     * Type of the primary mouse button.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Pointer
     * @since 10
     */
    enum PrimaryButton {
        /**
         * Left button.
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 10
         */
        LEFT = 0,
        /**
         * Right button.
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 10
         */
        RIGHT = 1
    }
    /**
     * Enumerates shortcut menu triggering modes.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Pointer
     * @since 10
     */
    enum RightClickType {
        /**
         * Tapping the right-button area of the touchpad.
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 10
         */
        TOUCHPAD_RIGHT_BUTTON = 1,
        /**
         * Tapping the left-button area of the touchpad.
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 10
         */
        TOUCHPAD_LEFT_BUTTON = 2,
        /**
         * Tapping or pressing the touchpad with two fingers.
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 10
         */
        TOUCHPAD_TWO_FINGER_TAP = 3,
        /**
         * Tapping or pressing the touchpad with two fingers, or tapping the right-button area of the touchpad.
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 20
         */
        TOUCHPAD_TWO_FINGER_TAP_OR_RIGHT_BUTTON = 4,
        /**
         * Tapping or pressing the touchpad with two fingers, or tapping the left-button area of the touchpad.
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 20
         */
        TOUCHPAD_TWO_FINGER_TAP_OR_LEFT_BUTTON = 5
    }
    /**
     * Defines custom cursor resources.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Pointer
     * @since 15
     */
    interface CustomCursor {
        /**
         * Pixel map. The minimum size is subject to the minimum limit of the image. The maximum size is 256 x 256 px.
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 15
         */
        pixelMap: image.PixelMap;
        /**
         * Horizontal coordinate of the custom pointer focus, in px. This coordinate is limited by the custom pointer size.
         * The minimum value is 0, and the maximum value is the maximum width of the resource image. The default value is
         * **0** when this parameter is omitted.
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 15
         */
        focusX?: number;
        /**
         * Vertical coordinate of the custom pointer focus, in px. This coordinate is limited by the custom pointer size.
         * The minimum value is 0, and the maximum value is the maximum width of the resource image. The default value is
         * **0** when this parameter is omitted.
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 15
         */
        focusY?: number;
    }
    /**
     * Defines custom cursor configuration.
     *
     * @syscap SystemCapability.MultimodalInput.Input.Pointer
     * @since 15
     */
    interface CursorConfig {
        /**
         * Whether to adjust the cursor size based on system settings. The value **true** means to adjust the cursor size
         * based on system settings, and the value **false** means to use the custom cursor size. The adjustment range is
         * [size of the cursor image, 256 x 256].
         *
         * @syscap SystemCapability.MultimodalInput.Input.Pointer
         * @since 15
         */
        followSystem: boolean;
    }
    /**
     * Sets the mouse pointer style type for a specified window. This API can set only the mouse pointer style type of
     * windows within the current application process. For details about how to set the mouse pointer style type of the
     * host window through the **UIExtensionAbility** process, see
     * [setCursor]{@link @ohos.arkui.UIContext:CursorController.setCursor}. This API uses an asynchronous callback to
     * return the result.
     *
     * @param { number } windowId - Window ID. The value is an integer greater than or equal to 0.
     *     <br>If the window ID is valid and the corresponding window exists, the mouse pointer style of the window can be
     *     set properly.
     *     <br>If the window ID is valid but the window does not exist, the mouse pointer style can also be set properly.
     *     <br>The result can be obtained through [getPointerStyle]{@link pointer.getPointerStyle}.
     * @param { PointerStyle } pointerStyle - Pointer style. Do not pass **DEVELOPER_DEFINED_ICON**.
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
     *     **err** is **undefined**. Otherwise, **err** is an error object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.MultimodalInput.Input.Pointer
     * @since 9
     */
    function setPointerStyle(windowId: number, pointerStyle: PointerStyle, callback: AsyncCallback<void>): void;
    /**
     * Sets the mouse pointer style type for a specified window. This API can set only the mouse pointer style type of
     * windows within the current application process. For details about how to set the mouse pointer style type of the
     * host window through the **UIExtensionAbility** process, see
     * [setCursor]{@link @ohos.arkui.UIContext:CursorController.setCursor}. This uses a promise to return the result.
     *
     * @param { number } windowId - Window ID. The value is an integer greater than or equal to 0.
     *     <br>If the window ID is valid and the corresponding window exists, the mouse pointer style of the window can be
     *     set properly.
     *     <br>If the window ID is valid but the window does not exist, the mouse pointer style can also be set properly.
     *     <br>The result can be obtained through [getPointerStyle]{@link pointer.getPointerStyle}.
     * @param { PointerStyle } pointerStyle - Pointer style.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.MultimodalInput.Input.Pointer
     * @since 9
     */
    function setPointerStyle(windowId: number, pointerStyle: PointerStyle): Promise<void>;
    /**
     * Sets the mouse pointer style type for a specified window and returns the result synchronously. This API can set
     * only the mouse pointer style type of windows within the current application process. For details about how to set
     * the mouse pointer style type of the host window through the **UIExtensionAbility** process, see
     * [setCursor]{@link @ohos.arkui.UIContext:CursorController.setCursor}.
     *
     * @param { number } windowId - Window ID. The value is an integer greater than or equal to 0.
     *     <br>If the window ID is valid and the corresponding window exists, the mouse pointer style of the window can be
     *     set properly.
     *     <br>If the window ID is valid but the window does not exist, the mouse pointer style can also be set properly.
     *     <br>The result can be obtained through [getPointerStyleSync]{@link pointer.getPointerStyleSync}.
     * @param { PointerStyle } pointerStyle - Pointer style.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.MultimodalInput.Input.Pointer
     * @since 10
     */
    function setPointerStyleSync(windowId: number, pointerStyle: PointerStyle): void;
    /**
     * Obtains the mouse pointer style type of a specified window. This API can obtain only the mouse pointer style type
     * of windows within the current application process. This API uses an asynchronous callback to return the result.
     *
     * @param { number } windowId - Window ID. The value is an integer greater than or equal to **-1**. The value **-1**
     *     indicates the global window.
     *     <br>If the window ID is valid and the corresponding window exists, the mouse pointer style of the window is
     *     returned.
     *     <br>If the window ID is valid but the window does not exist, the global mouse pointer style is returned by
     *     default.
     *     <br>If the mouse pointer style is set for a non-existent window through
     *     [setPointerStyle]{@link pointer.setPointerStyle}, this API can obtain the mouse pointer style properly.
     * @param { AsyncCallback<PointerStyle> } callback - Callback used to return the result. If the operation is
     *     successful, **err** is **undefined**, and **data** is the mouse pointer style type. Otherwise, **err** is an
     *     error object. In specific scenarios (obtaining the style on a window with a custom pointer style),
     *     **DEVELOPER_DEFINED_ICON** is returned.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.MultimodalInput.Input.Pointer
     * @since 9
     */
    function getPointerStyle(windowId: number, callback: AsyncCallback<PointerStyle>): void;
    /**
     * Obtains the mouse pointer style type. This API can obtain only the mouse pointer style type of windows within the
     * current application process. This API uses a promise to return the result.
     *
     * @param { number } windowId - Window ID. The value is an integer greater than or equal to **-1**. The value **-1**
     *     indicates the global window.
     *     <br>If the window ID is valid and the corresponding window exists, the mouse pointer style of the window is
     *     returned.
     *     <br>If the window ID is valid but the window does not exist, the global mouse pointer style is returned by
     *     default.
     *     <br>If the mouse pointer style is set for a non-existent window through
     *     [setPointerStyle]{@link pointer.setPointerStyle}, this API can obtain the mouse pointer style properly.
     * @returns { Promise<PointerStyle> } Promise object, which is used to return the mouse pointer style.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.MultimodalInput.Input.Pointer
     * @since 9
     */
    function getPointerStyle(windowId: number): Promise<PointerStyle>;
    /**
     * Queries the mouse pointer style type of a specified window, such as east arrow, west arrow, south arrow, and north
     * arrow. This API can obtain only the mouse pointer style type of windows within the current application process.
     *
     * @param { number } windowId - Window ID. The value is an integer greater than or equal to **-1**. The value **-1**
     *     indicates the global window.
     *     <br>If the window ID is valid and the corresponding window exists, the mouse pointer style of the window is
     *     returned.
     *     <br>If the window ID is valid but the window does not exist, the global mouse pointer style is returned by
     *     default.
     *     <br>If the mouse pointer style is set for a non-existent window through
     *     [setPointerStyleSync]{@link pointer.setPointerStyleSync}, this API can obtain the mouse pointer style properly.
     * @returns { PointerStyle } Mouse pointer style.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.MultimodalInput.Input.Pointer
     * @since 10
     */
    function getPointerStyleSync(windowId: number): PointerStyle;
    /**
     * Sets whether the mouse pointer is visible in the current window. This API uses an asynchronous callback to return
     * the result.
     *
     * @param { boolean } visible - Whether the mouse pointer is visible in the current window. The value **true**
     *     indicates that the mouse pointer is visible, and the value **false** indicates the opposite.
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
     *     **err** is **undefined**. Otherwise, **err** is an error object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported; [since 18]
     * @syscap SystemCapability.MultimodalInput.Input.Pointer
     * @since 9
     */
    function setPointerVisible(visible: boolean, callback: AsyncCallback<void>): void;
    /**
     * Sets whether the mouse pointer is visible in the current window. This API uses a promise to return the result.
     *
     * @param { boolean } visible - Whether the mouse pointer is visible in the current window. The value **true**
     *     indicates that the mouse pointer is visible, and the value **false** indicates the opposite.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported; [since 18]
     * @syscap SystemCapability.MultimodalInput.Input.Pointer
     * @since 9
     */
    function setPointerVisible(visible: boolean): Promise<void>;
    /**
     * Sets whether the mouse pointer is visible in the current window. This API returns the result synchronously.
     *
     * @param { boolean } visible - Whether the mouse pointer is visible in the current window. The value **true**
     *     indicates that the mouse pointer is visible, and the value **false** indicates the opposite.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.MultimodalInput.Input.Pointer
     * @since 10
     */
    function setPointerVisibleSync(visible: boolean): void;
    /**
     * Obtains the visible status of the mouse pointer. This API uses an asynchronous callback to return the result.
     *
     * @param { AsyncCallback<boolean> } callback - Callback used to return the result. If the operation is successful,
     *     **err** is **undefined**, and **data** is the visible status of the mouse pointer (**true** if visible and
     *     **false** if invisible). Otherwise, **err** is an error object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.MultimodalInput.Input.Pointer
     * @since 9
     */
    function isPointerVisible(callback: AsyncCallback<boolean>): void;
    /**
     * Obtains the visible status of the mouse pointer. This API uses a promise to return the result.
     *
     * @returns { Promise<boolean> } Promise used to return the result. **true** is returned if the mouse pointer is
     *     visible; **false** is returned if the mouse pointer is hidden.
     * @syscap SystemCapability.MultimodalInput.Input.Pointer
     * @since 9
     */
    function isPointerVisible(): Promise<boolean>;
    /**
     * Checks whether the mouse pointer is visible in the current window. This API returns the result synchronously.
     *
     * @returns { boolean } Visible status of the mouse pointer. The value **true** indicates that the mouse pointer is
     *     visible, and the value **false** indicates the opposite.
     * @syscap SystemCapability.MultimodalInput.Input.Pointer
     * @since 10
     */
    function isPointerVisibleSync(): boolean;
    /**
     * Sets a custom pointer style for a specified window. This API can set only the custom pointer style of windows
     * within the current application process. For details about how to set the custom pointer style of the host window
     * through the **UIExtensionAbility** process, see
     * [setCustomCursor]{@link @ohos.arkui.UIContext:CursorController.setCustomCursor}. This API uses a promise to return
     * the result.
     *
     * @param { number } windowId - Window ID.
     * @param { image.PixelMap } pixelMap - Custom cursor resource.
     * @param { number } focusX - Custom cursor focus X, in px. The value must be greater than or equal to 0. The default
     *     value is **0**.
     * @param { number } focusY - Custom cursor focus Y, in px. The value must be greater than or equal to 0. The default
     *     value is **0**.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.MultimodalInput.Input.Pointer
     * @since 11
     */
    function setCustomCursor(windowId: number, pixelMap: image.PixelMap, focusX?: number, focusY?: number): Promise<void>;
    /**
     * Sets a custom pointer style for a specified window synchronously. This API can set only the custom pointer style of
     * windows within the current application process. For details about how to set the custom pointer style of the host
     * window through the **UIExtensionAbility** process, see
     * [setCustomCursor]{@link @ohos.arkui.UIContext:CursorController.setCustomCursor}.
     *
     * @param { number } windowId - Window ID. The value must be an integer greater than 0.
     * @param { image.PixelMap } pixelMap - Custom cursor resource.
     * @param { number } focusX - Custom pointer focus X, in px. The value must be greater than or equal to 0. The default
     *     value is **0**.
     * @param { number } focusY - Custom pointer focus Y, in px. The value must be greater than or equal to 0. The default
     *     value is **0**.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.MultimodalInput.Input.Pointer
     * @since 11
     */
    function setCustomCursorSync(windowId: number, pixelMap: image.PixelMap, focusX?: number, focusY?: number): void;
    /**
     * Sets a custom pointer style for a specified window. This API can set only the custom pointer style of windows
     * within the current application process. For details about how to set the custom pointer style of the host window
     * through the **UIExtensionAbility** process, see
     * [setCustomCursor]{@link @ohos.arkui.UIContext:CursorController.setCustomCursor}. This API uses a promise to return
     * the result.
     *
     * The cursor may be switched back to the system style in the following cases: application window layout change, hot
     * zone switching, page redirection, moving of the cursor out of the window and then back to the window, or moving of
     * the cursor in different areas of the window. In this case, you need to reset the cursor style.
     *
     * @param { number } windowId - Window ID.
     * @param { CustomCursor } cursor - Custom cursor resource.
     * @param { CursorConfig } config - Custom cursor configuration, which specifies whether to adjust the cursor size
     *     based on system settings. If **followSystem** in **CursorConfig** is set to **true**, the supported adjustment
     *     range is [size of the cursor image, 256 x 256].
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Abnormal windowId parameter passed in;
     *     <br>2. Abnormal pixelMap parameter passed in; 3. Abnormal focusX parameter passed in;
     *     <br>4. Abnormal focusY parameter passed in.
     * @throws { BusinessError } 26500001 - Invalid windowId. Possible causes: The window id does not belong to the
     *     current process.
     * @syscap SystemCapability.MultimodalInput.Input.Pointer
     * @since 15
     */
    function setCustomCursor(windowId: number, cursor: CustomCursor, config: CursorConfig): Promise<void>;
}
export default pointer;

```
