# @ohos.window.floatingBall.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2025 Huawei Device Co., Ltd.
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
import type BaseContext from './application/BaseContext';
import type image from './@ohos.multimedia.image';
import type Want from './@ohos.app.ability.Want';
import type { Callback } from './@ohos.base';
/**
 * This module provides essential functionalities for floating balls. It lets you check whether the device supports
 * floating balls and create a controller to start, update, or stop them. It is ideal for tasks like comparing prices,
 * searching for answers, or grabbing orders. The floating ball appears as a floating widget above other application,
 * quickly showing important information.
 *
 * > **NOTE**
 * >
 * > - For the system capability SystemCapability.Window.SessionManager, use
 * > [canIUse()]{@link canIUse} to check whether the device supports this system
 * > capability and the corresponding APIs.
 *
 * @syscap SystemCapability.Window.SessionManager
 * @since 20
 */
declare namespace floatingBall {
    /**
     * Checks whether the device supports floating balls.
     *
     * @returns { boolean } Check result for the support of floating balls. **true** if supported, **false** otherwise.
     * @syscap SystemCapability.Window.SessionManager
     * @since 20
     */
    function isFloatingBallEnabled(): boolean;
    /**
     * Creates a floating ball controller. This API uses a promise to return the result.
     *
     * @param { FloatingBallConfiguration } config - Parameters for creating the floating ball controller. This parameter
     *     cannot be empty, and **context** that is used to construct this parameter cannot be empty.
     * @returns { Promise<FloatingBallController> } Promise used to return the floating ball controller.
     * @throws { BusinessError } 801 - Capability not supported.
     *     Failed to call the API due to limited device capabilities.
     * @throws { BusinessError } 1300019 - Wrong parameters for operating the floating ball.
     * @throws { BusinessError } 1300023 - Floating ball internal error.
     * @syscap SystemCapability.Window.SessionManager
     * @since 20
     */
    function create(config: FloatingBallConfiguration): Promise<FloatingBallController>;
    /**
     * Describes the parameters for creating a floating ball controller.
     *
     * @syscap SystemCapability.Window.SessionManager
     * @since 20
     */
    interface FloatingBallConfiguration {
        /**
         * Context environment.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @since 20
         */
        context: BaseContext;
    }
    /**
     * Implements a floating ball controller instance, which is used to start, update, and stop floating balls, and
     * register callbacks.
     *
     * Before calling any of the following APIs, you must use [floatingBall.create()]{@link floatingBall.create} to create
     * a floating ball controller instance.
     *
     * @syscap SystemCapability.Window.SessionManager
     * @since 20
     */
    interface FloatingBallController {
        /**
         * Starts the floating ball. This API uses a promise to return the result.
         *
         * @permission ohos.permission.USE_FLOAT_BALL
         * @param { FloatingBallParams } params - Parameters for starting the floating ball.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 201 - Permission verification failed, usually returned by VerifyAccessToken.
         * @throws { BusinessError } 1300019 - Wrong parameters for operating the floating ball.
         * @throws { BusinessError } 1300020 - Failed to create the floating ball window.
         * @throws { BusinessError } 1300021 - Failed to start multiple floating ball windows.
         * @throws { BusinessError } 1300022 - Repeated floating ball operation.
         * @throws { BusinessError } 1300023 - Floating ball internal error.
         * @throws { BusinessError } 1300024 - The floating ball window state is abnormal.
         * @throws { BusinessError } 1300025 - The floating ball state does not support this operation.
         * @throws { BusinessError } 1300034 - This operation conflicts with other floating windows. Possible cause:
         *     App has already started float view. [since 26.0.0]
         * @syscap SystemCapability.Window.SessionManager
         * @since 20
         */
        startFloatingBall(params: FloatingBallParams): Promise<void>;
        /**
         * Updates the floating ball. This API uses a promise to return the result.
         *
         * @param { FloatingBallParams } params - Parameters for updating the floating ball.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 1300002 - This window state is abnormal.
         * @throws { BusinessError } 1300003 - This window manager service works abnormally.
         * @throws { BusinessError } 1300004 - Unauthorized operation.
         * @throws { BusinessError } 1300019 - Wrong parameters for operating the floating ball.
         * @throws { BusinessError } 1300023 - Floating ball internal error.
         * @throws { BusinessError } 1300024 - The floating ball window state is abnormal.
         * @throws { BusinessError } 1300025 - The floating ball state does not support this operation.
         * @throws { BusinessError } 1300027 - When updating the floating ball, the template type cannot be changed.
         * @throws { BusinessError } 1300028 - Updating static template-based floating balls is not supported.
         * @syscap SystemCapability.Window.SessionManager
         * @since 20
         */
        updateFloatingBall(params: FloatingBallParams): Promise<void>;
        /**
         * Stops the floating ball. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 1300022 - Repeated floating ball operation.
         * @throws { BusinessError } 1300023 - Floating ball internal error.
         * @throws { BusinessError } 1300024 - The floating ball window state is abnormal.
         * @syscap SystemCapability.Window.SessionManager
         * @since 20
         */
        stopFloatingBall(): Promise<void>;
        /**
         * Registers a listener for lifecycle state changes of the floating ball. To prevent memory leaks, remember to
         * unregister the listener when it is no longer needed.
         *
         * @param { 'stateChange' } type - Event type. The event **'stateChange'** is triggered when the floating ball
         *     lifecycle state changes.
         * @param { Callback<FloatingBallState> } callback - Callback used to return the floating ball lifecycle state.
         * @throws { BusinessError } 1300019 - Wrong parameters for operating the floating ball.
         * @throws { BusinessError } 1300022 - Repeated floating ball operation.
         * @throws { BusinessError } 1300023 - Floating ball internal error.
         * @throws { BusinessError } 1300024 - The floating ball window state is abnormal.
         * @syscap SystemCapability.Window.SessionManager
         * @since 20
         */
        on(type: 'stateChange', callback: Callback<FloatingBallState>): void;
        /**
         * Unregisters the listener for lifecycle state changes of the floating ball.
         *
         * @param { 'stateChange' } type - Event type. The event **'stateChange'** is triggered when the floating ball
         *     lifecycle state changes.
         * @param { Callback<FloatingBallState> } [callback] - Callback used to return the floating ball lifecycle state. If
         *     a value is passed in, the corresponding subscription is canceled. If no value is passed in, all subscriptions
         *     to the specified event are canceled.
         * @throws { BusinessError } 1300019 - Wrong parameters for operating the floating ball.
         * @throws { BusinessError } 1300023 - Floating ball internal error.
         * @throws { BusinessError } 1300024 - The floating ball window state is abnormal.
         * @syscap SystemCapability.Window.SessionManager
         * @since 20
         */
        off(type: 'stateChange', callback?: Callback<FloatingBallState>): void;
        /**
         * Registers a listener for click events of the floating ball. To prevent memory leaks, remember to unregister the
         * listener when it is no longer needed.
         *
         * @param { 'click' } type - Event type. The event **'click'** is triggered when the floating ball is tapped.
         * @param { Callback<void> } callback - Callback invoked when the floating ball is tapped. It does not return any
         *     parameter.
         * @throws { BusinessError } 1300019 - Wrong parameters for operating the floating ball.
         * @throws { BusinessError } 1300022 - Repeated floating ball operation.
         * @throws { BusinessError } 1300023 - Floating ball internal error.
         * @throws { BusinessError } 1300024 - The floating ball window state is abnormal.
         * @syscap SystemCapability.Window.SessionManager
         * @since 20
         */
        on(type: 'click', callback: Callback<void>): void;
        /**
         * Unregisters the listener for click events of the floating ball.
         *
         * @param { 'click' } type - Event type. The event **'click'** is triggered when the floating ball is tapped.
         * @param { Callback<void> } [callback] - Callback invoked when the floating ball is tapped. It does not return any
         *     parameter. If a value is passed in, the corresponding subscription is canceled. If no value is passed in, all
         *     subscriptions to the specified event are canceled.
         * @throws { BusinessError } 1300019 - Wrong parameters for operating the floating ball.
         * @throws { BusinessError } 1300023 - Floating ball internal error.
         * @throws { BusinessError } 1300024 - The floating ball window state is abnormal.
         * @syscap SystemCapability.Window.SessionManager
         * @since 20
         */
        off(type: 'click', callback?: Callback<void>): void;
        /**
         * Register floating ball destroy event listener.
         *
         * @param { Callback<string> } callback - Used to handle {'destroy'} command.
         * @throws { BusinessError } 1300019 - Wrong parameters for operating the floating ball. Possible cause:
         *     Callback is null or not callable.
         * @throws { BusinessError } 1300022 - Repeated floating ball operation.
         * @throws { BusinessError } 1300023 - Floating ball internal error. Possible cause:
         *     System error, such as a null pointer, insufficient memory.
         * @throws { BusinessError } 1300024 - The floating ball window state is abnormal. Possible cause:
         *     The floating ball controller has been destroyed.
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        onDestroy(callback: Callback<string>): void;
        /**
         * Unregister floating ball destroy event listener.
         *
         * @param { Callback<string> } [callback] - Indicates the callback function. If not provided,
         *     all callbacks for the given event type will be removed.
         * @throws { BusinessError } 1300019 - Wrong parameters for operating the floating ball. Possible cause:
         *     Callback is null or not callable.
         * @throws { BusinessError } 1300023 - Floating ball internal error. Possible cause:
         *     System error, such as a null pointer, insufficient memory.
         * @throws { BusinessError } 1300024 - The floating ball window state is abnormal. Possible cause:
         *     The floating ball controller has been destroyed.
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        offDestroy(callback?: Callback<string>): void;
        /**
         * Obtains the floating ball window information. This API uses a promise to return the result.
         *
         * @returns { Promise<FloatingBallWindowInfo> } Promise used to return the floating ball window information.
         * @throws { BusinessError } 1300002 - This window state is abnormal.
         * @throws { BusinessError } 1300003 - This window manager service works abnormally.
         * @throws { BusinessError } 1300004 - Unauthorized operation.
         * @throws { BusinessError } 1300023 - Floating ball internal error.
         * @throws { BusinessError } 1300024 - The floating ball window state is abnormal.
         * @throws { BusinessError } 1300025 - The floating ball state does not support this operation.
         * @syscap SystemCapability.Window.SessionManager
         * @since 20
         */
        getFloatingBallWindowInfo(): Promise<FloatingBallWindowInfo>;
        /**
         * Restores the main window of the application and loads the specified page. This API uses a promise to return the
         * result. This API can be called only after the floating ball is tapped. If the application has the
         * **ohos.permission.AUTO_RESTORE_MAIN_WINDOW** permission, this API can be called directly without tapping the
         * floating ball.
         *
         * @permission ohos.permission.USE_FLOAT_BALL
         * @param { Want } want - Want used for loading the specified page.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 201 - Permission verification failed, usually returned by VerifyAccessToken.
         * @throws { BusinessError } 1300002 - This window state is abnormal.
         * @throws { BusinessError } 1300003 - This window manager service works abnormally.
         * @throws { BusinessError } 1300004 - Unauthorized operation.
         * @throws { BusinessError } 1300019 - Wrong parameters for operating the floating ball.
         * @throws { BusinessError } 1300023 - Floating ball internal error.
         * @throws { BusinessError } 1300024 - The floating ball window state is abnormal.
         * @throws { BusinessError } 1300025 - The floating ball state does not support this operation.
         * @throws { BusinessError } 1300026 - Failed to restore the main window. Possible causes:
         *     1. Invalid parameter. The provided bundleName does not match the caller's application bundleName.
         *     2. The application lacks the ohos.permission.AUTO_RESTORE_MAIN_WINDOW permission,
         *        and no user interaction (click) on the floating ball has occurred.
         * @syscap SystemCapability.Window.SessionManager
         * @since 20
         */
        restoreMainWindow(want: Want): Promise<void>;
        /**
         * Sets whether the floating ball is visible in the application. This API uses a promise to return the result.
         *
         * - When the application is on the recent tasks screen (the
         * [lifecycle state](docroot://windowmanager/window-overview.md#lifecycle-states) is **PAUSED**), the floating ball
         * is invisible.
         * - By default (when this API is not called) or when this API is called with the value **true** passed in, the
         * floating ball is visible except on the recent tasks screen.
         * - When this API is called with the value **false** passed in, the floating ball is invisible when the application
         * is in the foreground (the [lifecycle state](docroot://windowmanager/window-overview.md#lifecycle-states) is
         * **SHOWN** or **RESUMED**) and is visible when the application is in the background (the
         * [lifecycle state](docroot://windowmanager/window-overview.md#lifecycle-states) is **HIDDEN**).
         *
         * @param { boolean } isVisible - **true** indicates that the floating ball is visible in the application, and
         *     **false** indicates the opposite.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 1300003 - This window manager service works abnormally.
         *     Possible cause: Internal IPC error.
         * @throws { BusinessError } 1300023 - Floating ball internal error. Possible cause:
         *     The floating ball controller is null.
         * @throws { BusinessError } 1300024 - The floating ball window state is abnormal. Possible causes:
         *     The floating ball window has not been created or has been destroyed.
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 24
         */
        setFloatingBallVisibilityInApp(isVisible: boolean): Promise<void>;
    }
    /**
     * Describes the parameters for starting and updating the floating ball.
     *
     * @syscap SystemCapability.Window.SessionManager
     * @since 20
     */
    interface FloatingBallParams {
        /**
         * Floating ball template.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @since 20
         */
        template: FloatingBallTemplate;
        /**
         * Title of the floating ball. It cannot be an empty string and cannot exceed 64 bytes.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @since 20
         */
        title: string;
        /**
         * Content of the floating ball. It cannot exceed 64 bytes. The default value is an empty string, and no content is
         * displayed on the floating ball.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @since 20
         */
        content?: string;
        /**
         * The color of the floating ball title, in hexadecimal format without opacity
         * (e.g., **'#008EF5'** or **'#FF008EF5'**).
         * Providing titleColor is not allowed if 'backgroundColor' is not provided.
         *
         * @default Set different default values according to the 'backgroundColor'.
         *     - If 'backgroundColor' is provided, when 'backgroundColor' is light color, default value is '#E5FFFFFF',
         *       otherwise is '#E5000000'.
         *     - If 'backgroundColor' is not provided, default value is $r('sys.color.font_primary').
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        titleColor?: string;
        /**
         * The color of the floating ball content, in hexadecimal format without opacity
         * (e.g., **'#008EF5'** or **'#FF008EF5'**).
         * Providing contentColor is not allowed if 'backgroundColor' is not provided.
         *
         * @default Set different default values according to the 'backgroundColor'.
         *     - If 'backgroundColor' is provided, when 'backgroundColor' is light color, default value is '#99FFFFFF',
         *       otherwise is '#99000000'
         *     - If 'backgroundColor' is not provided, default value is $r('sys.color.font_secondary')
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        contentColor?: string;
        /**
         * Background color of the floating ball, in hexadecimal format without opacity (for example, **'#008EF5'** or
         * **'#FF008EF5'**). If this parameter is not specified, the default background color of the system (light or dark
         * mode) is used.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @since 20
         */
        backgroundColor?: string;
        /**
         * Icon of the floating ball. The total number of bytes of the icon pixels cannot exceed 192 KB (which is obtained
         * through [getPixelBytesNumber]{@link @ohos.multimedia.image:image.PixelMap.getPixelBytesNumber}). The recommended
         * size is 128 px * 128 px. Actual display may vary based on the device capability and floating ball UI style.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @since 20
         */
        icon?: image.PixelMap;
        /**
         * Animation type used when the floating ball text is updated. The default value is
         * **FloatingBallTextUpdateAnimationType.ANIMATION_NONE**.
         *
         * @default FloatingBallTextUpdateAnimationType.ANIMATION_NONE
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        textUpdateAnimationType?: FloatingBallTextUpdateAnimationType;
    }
    /**
     * Enumerates the lifecycle states of the floating ball.
     *
     * @syscap SystemCapability.Window.SessionManager
     * @since 20
     */
    enum FloatingBallState {
        /**
         * The floating ball is started.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @since 20
         */
        STARTED = 1,
        /**
         * The floating ball is stopped.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @since 20
         */
        STOPPED = 2
    }
    /**
     * Enumerates the types of the floating ball template.
     *
     * @syscap SystemCapability.Window.SessionManager
     * @since 20
     */
    enum FloatingBallTemplate {
        /**
         * Static layout, which provides a title and an icon. When this template is used, the **title** and **icon**
         * parameters in **FloatingBallParams** must be passed.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @since 20
         */
        STATIC = 1,
        /**
         * Standard text layout, which provides a title and content. When this template is used, the **title** parameter in
         * **FloatingBallParams** must be passed.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @since 20
         */
        NORMAL = 2,
        /**
         * Emphasized text layout, which provides an icon, a title, and content. When this template is used, the **title**
         * parameter in **FloatingBallParams** must be passed.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @since 20
         */
        EMPHATIC = 3,
        /**
         * Plain text layout, which provides only a title. When this template is used, the **title** parameter in
         * **FloatingBallParams** must be passed.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @since 20
         */
        SIMPLE = 4
    }
    /**
     * Describes the floating ball window information.
     *
     * @syscap SystemCapability.Window.SessionManager
     * @since 20
     */
    interface FloatingBallWindowInfo {
        /**
         * ID of the floating ball window.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @since 20
         */
        readonly windowId: number;
    }
    /**
     * Enumerates the animation types used when the floating ball text is updated.
     *
     * @syscap SystemCapability.Window.SessionManager
     * @stagemodelonly
     * @since 26.0.0
     */
    enum FloatingBallTextUpdateAnimationType {
        /**
         * No animation.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        ANIMATION_NONE = 0,
        /**
         * Fade-in and fade-out animation.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        ANIMATION_OPACITY = 1
    }
}
export default floatingBall;

```
