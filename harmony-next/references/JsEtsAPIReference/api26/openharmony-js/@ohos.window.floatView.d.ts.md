# @ohos.window.floatView.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2026 Huawei Device Co., Ltd.
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
import type { Callback } from './@ohos.base';
import type floatingBall from './@ohos.window.floatingBall';
import window from './@ohos.window';
/**
 * A float view is a small window that floats on a desktop or an application screen, providing flexible window
 * management capabilities.
 *
 * This module provides capabilities about the float view, including determining whether a device supports a float view,
 * and creating a float view controller to start, update, or stop a float view.
 *
 * **Application scenarios**:
 *
 * A float view is applicable to scenarios where application content needs to be continuously displayed in an
 * independent small window or shortcut operations need to be provided. Examples:
 *
 * - Application for stock market tracking: When browsing other applications, users can use a float view to view real-
 * time stock market changes without frequently switching between applications.
 * - Live streaming application on a mobile phone: During live streaming, hosts can use a float view to display a custom
 * interaction panel or control UI, facilitating real-time operations and interactions.
 *
 * **Linkage with the floating ball**:
 *
 * This module can be used together with [@ohos.window.floatingBall]{@link @ohos.window.floatingBall:floatingBall}.
 * After the float view controller is bound to the floating ball controller using the
 * [floatView.bind]{@link floatView.bind} API, users can tap the floating ball to expand it as a float view, and click
 * the minimize button in the upper left corner of the float view to collapse it back as a floating ball. This allows
 * for seamless switching between the two window forms.
 *
 * **Comparison between the global floating window and float view**:
 *
 * - Similarities: Both the global floating window and float view are special types of application auxiliary windows
 * that can remain displayed on the foreground even after the application's main window and corresponding ability
 * transition to the background. They can be used to continue displaying the UI after the application transitions to the
 * background.
 * - Differences:
 *  - The global floating window is managed and its UI is drawn by developers, without a unified UI or animation effect.
 *  - The float view is managed by the system and its UI is drawn in a unified manner, offering a more sophisticated and
 * refined animation effect.
 *  - The float view can be bound to the [floating ball]{@link @ohos.window.floatingBall:floatingBall} for joint use,
 * enabling more complex scenarios.
 *
 * **Start version**: 26.0.0
 *
 * > **NOTE**
 * >
 * > - Use [canIUse()](docroot://reference/common/js-apis-syscap.md#caniuse) to check whether the device supports the
 * > system capability SystemCapability.Window.SessionManager and the corresponding APIs.
 * >
 * > - The APIs of this module can be used only in the stage model.
 *
 * @syscap SystemCapability.Window.SessionManager
 * @stagemodelonly
 * @since 26.0.0
 */
declare namespace floatView {
    /**
     * Checks whether the device supports the float view.
     *
     * | Type| Description|
     * |------------|------------|
     * | boolean  | Whether the device supports the float view. **true** to support; **false** otherwise.|
     *
     * @returns { boolean } true if the float view is enabled, otherwise false.
     * @syscap SystemCapability.Window.SessionManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function isFloatViewEnabled(): boolean;
    /**
     * Creates a float view controller. This API uses a promise to return the result.
     *
     * @param { FloatViewConfiguration } config - Parameter for creating a float view controller. This parameter and the
     *     context for constructing this parameter cannot be null or undefined. Otherwise, error code 401 is thrown. Error
     *     code 1300016 is thrown for other parameter exceptions.
     * @returns { Promise<FloatViewController> } Promise used to return the created float view controller.
     * @throws { BusinessError } 801 - Capability not supported. Possible cause: Call the API on unsupported device.
     * @throws { BusinessError } 1300002 - This window state is abnormal. Possible cause:
     *     1. This window context is abnormal.
     *     2. System error, such as a null pointer, insufficient memory or a JS engine exception.
     * @throws { BusinessError } 1300016 - Parameter error.
     *     Possible cause: Invalid template type.
     * @syscap SystemCapability.Window.SessionManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function create(config: FloatViewConfiguration): Promise<FloatViewController>;
    /**
     * Binds the float view and floating ball. You need to create the
     * [float view controller]{@link floatView.FloatViewController} and
     * [floating ball controller]{@link @ohos.window.floatingBall:floatingBall.FloatingBallController} first, and neither
     * of them has been started. This API uses a promise to return the result.
     *
     * > **NOTE**
     * >
     * > - After the binding is successful, calling [start()]{@link floatView.FloatViewController.start} or
     * > [startFloatingBall()]{@link @ohos.window.floatingBall:floatingBall.FloatingBallController.startFloatingBall} will
     * > create both a float view and the floating ball window, and trigger the status callback registered for the
     * > corresponding window. However, only one window is displayed at a time, and the display sequence depends on which
     * > controller's start API is called first.
     * >
     * > - After the binding is successful, users can switch between the float view and the floating ball window by
     * > clicking.
     * >
     * > - After the binding is successful, calling the stop API ([stop()]{@link floatView.FloatViewController.stop} or
     * > [stopFloatingBall()]{@link @ohos.window.floatingBall:floatingBall.FloatingBallController.stopFloatingBall}) of
     * > either controller will destroy both the float view and the floating ball window, and trigger the status callback
     * > registered for the corresponding window.
     *
     * @permission ohos.permission.USE_FLOAT_BALL and ohos.permission.FLOAT_VIEW
     * @param { FloatViewController } floatViewController - Float view controller.
     * @param { floatingBall.FloatingBallController } floatingBallController - Floating ball controller.
     * @param { floatingBall.FloatingBallParams } floatingBallParams - Floating ball parameters. The parameters set during
     *     binding will overwrite the parameters saved when the floating ball controller is started.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 201 - Permission verification failed. Possible cause:
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 801 - Capability not supported on this device. Possible cause:
     *     Call api on unsupported device.
     * @throws { BusinessError } 1300019 - Wrong parameters for operating the floating ball. Possible cause:
     *     Invalid floating ball params.
     * @throws { BusinessError } 1300025 - The floating ball state does not support this operation. Possible cause:
     *     1. The floating ball has started but not stopped yet.
     *     2. The floating ball controller has been bound.
     * @throws { BusinessError } 1300031 - The floatView state does not support this operation. Possible cause:
     *     1. The float view has started but not stopped yet.
     *     2. The float view controller has been bound.
     * @syscap SystemCapability.Window.SessionManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function bind(floatViewController: FloatViewController, floatingBallController: floatingBall.FloatingBallController, floatingBallParams: floatingBall.FloatingBallParams): Promise<void>;
    /**
     * Unbinds the float view and floating ball. The unbinding can be performed only after both the
     * [float view controller]{@link floatView.FloatViewController} and
     * [floating ball controller]{@link @ohos.window.floatingBall:floatingBall.FloatingBallController} are stopped. This
     * API uses a promise to return the result.
     *
     * @param { FloatViewController } floatViewController - Float view controller.
     * @param { floatingBall.FloatingBallController } floatingBallController - Floating ball controller.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 801 - Capability not supported on this device. Possible cause:
     *     Call api on unsupported device.
     * @throws { BusinessError } 1300025 - The floating ball state does not support this operation. Possible cause:
     *     1. The floating ball has started but not stopped yet.
     *     2. The floatingBallController has not been bound.
     * @throws { BusinessError } 1300031 - The floatView state does not support this operation. Possible cause:
     *     1. The float view has started but not stopped yet.
     *     2. The floatViewController has not been bound.
     *     3. The floatViewController and the floatingBallController are not bound together.
     * @syscap SystemCapability.Window.SessionManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function unbind(floatViewController: FloatViewController, floatingBallController: floatingBall.FloatingBallController): Promise<void>;
    /**
     * Obtains the limits of the float view based on the passed template type. The unit is px.
     *
     * @param { FloatViewTemplateType } templateType - Template type of the float view.
     * @returns { FloatViewLimits } Limits of the float view, including the maximum size, minimum size, and aspect ratio.
     * @throws { BusinessError } 801 - Capability not supported. Possible cause:
     *     Call the API on unsupported device.
     * @throws { BusinessError } 1300002 - This window state is abnormal. Possible cause:
     *     System error, such as a null pointer, insufficient memory or a JS engine exception.
     * @throws { BusinessError } 1300003 - This window manager service works abnormally. Possible cause:
     *     Internal IPC error.
     * @throws { BusinessError } 1300016 - Parameter error. Possible cause: Invalid template type.
     * @syscap SystemCapability.Window.SessionManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function getFloatViewLimits(templateType: FloatViewTemplateType): FloatViewLimits;
    /**
     * Provides parameter configuration required for creating a float view controller.
     *
     * @syscap SystemCapability.Window.SessionManager
     * @stagemodelonly
     * @since 26.0.0
     */
    interface FloatViewConfiguration {
        /**
         * Context environment.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        context: BaseContext;
        /**
         * Template type of the float view.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        templateType: FloatViewTemplateType;
        /**
         * This field controls whether user confirmation is required when the close button is clicked.
         * **true** if clicking the close button requires user confirmation, otherwise no confirmation is needed.
         * Default value: default value is false.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        isConfirmOnClose?: boolean;
    }
    /**
     * Provides parameter configuration required for switching the float view template and modifying the size of the
     * window.
     *
     * @syscap SystemCapability.Window.SessionManager
     * @stagemodelonly
     * @since 26.0.0
     */
    interface TemplateProperty {
        /**
         * Template type of the float view.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        templateType: FloatViewTemplateType;
        /**
         * Window size required for updating the template type.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        size: window.Size;
    }
    /**
     * Defines a float view controller instance, which is used to start and stop the float view and register callbacks.
     *
     * Before calling the following APIs, you must use [floatView.create()]{@link floatView.create} to create a float view
     * controller instance (that is, **floatViewController**).
     *
     * @syscap SystemCapability.Window.SessionManager
     * @stagemodelonly
     * @since 26.0.0
     */
    interface FloatViewController {
        /**
         * Loads the content of a page, with its path specified in the current project, for the float view, and transfers
         * the state attribute to the page through **LocalStorage**. This API uses a promise to return the result.
         *
         * @param { string } path - Path of the page content which needs to be loaded to the window. The path needs to be
         *     configured in the **main_pages.json** file of the project. The path cannot be a relative path and must be the
         *     same as the value of **src** in the **main_pages.json** file.
         * @param { LocalStorage } [storage] - Page-level UI state storage unit, which is used to transfer the state
         *     attribute for the page. By default, the value is empty.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 1300002 - This window state is abnormal. Possible cause:
         *     The float view controller object is null.
         * @throws { BusinessError } 1300016 - Parameter error. Possible causes: Invalid path.
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        setUIContext(path: string, storage?: LocalStorage): Promise<void>;
        /**
         * Sets the UI content of a [named route](docroot://ui/arkts-routing.md#named-route) page to this float view window.
         *
         * @param { string } name - Name of the named route page.
         * @param { LocalStorage } [storage] - The data object shared within the content instance loaded by the window.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 1300002 - This window state is abnormal. Possible cause:
         *     The float view controller object is null.
         * @throws { BusinessError } 1300016 - Parameter error. Possible causes: Invalid name.
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        setUIContextByName(name: string, storage?: LocalStorage): Promise<void>;
        /**
         * Sets the size of the float view. You are advised to call the
         * [getFloatViewLimits]{@link floatView.getFloatViewLimits} API to obtain the recommended width and height ranges
         * and aspect ratio range, and then call this API based on the recommended values. The actual window size change can
         * be listened to through the
         * [onRectChange]{@link floatView.FloatViewController.onRectChange(callback: Callback<FloatViewRectChangeInfo>)}
         * API. This API uses a promise to return the result.
         *
         * @param { window.Size } size - Window size. It is recommended that the size meet the limits returned by the
         *     [getFloatViewLimits]{@link floatView.getFloatViewLimits} API.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 1300002 - This window state is abnormal. Possible cause:
         *     The float view controller object is null.
         * @throws { BusinessError } 1300003 - This window manager service works abnormally. Possible cause:
         *     Internal IPC error.
         * @throws { BusinessError } 1300016 - Parameter error.
         *     Possible cause: The value of the size is less than or equal to 0.
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        setWindowSize(size: window.Size): Promise<void>;
        /**
         * Switches the template of the flow view and changes the window size. You are advised to call the
         * [getFloatViewLimits]{@link floatView.getFloatViewLimits} API to obtain the recommended width and height ranges
         * and aspect ratio range of the target template, and then call this API based on the recommended values. The actual
         * window size change can be listened to through the
         * [onRectChange]{@link floatView.FloatViewController.onRectChange(callback: Callback<FloatViewRectChangeInfo>)}
         * API. This API uses a promise to return the result.
         *
         * @param { TemplateProperty } templateProperty - Target flow view template and window size. It is recommended that
         *     the size meet the limits returned by the [getFloatViewLimits]{@link floatView.getFloatViewLimits} API.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 1300002 - This window state is abnormal. Possible cause:
         *     The float view controller object is null.
         * @throws { BusinessError } 1300003 - This window manager service works abnormally. Possible cause:
         *     Internal IPC error.
         * @throws { BusinessError } 1300016 - Parameter error. Possible cause:
         *     1. Invalid template type.
         *     2. The value of the size is less than or equal to 0.
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        switchTemplate(templateProperty: TemplateProperty): Promise<void>;
        /**
         * Starts the float view. The return value of this API does not indicate that the start process is complete. You
         * need to use the
         * [onStateChange]{@link floatView.FloatViewController.onStateChange(callback: Callback<FloatViewStateChangeInfo>)}
         * API to listen for the **STARTED** callback to determine whether the start is successful. You are advised to call
         * **start ()** after calling [setUIContext()]{@link floatView.FloatViewController.setUIContext}. This API uses a
         * promise to return the result.
         *
         * @permission ohos.permission.FLOAT_VIEW
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 201 - Permission verification failed. Possible cause:
         *     The application does not have the permission required to call the API.
         * @throws { BusinessError } 1300002 - This window state is abnormal. Possible cause:
         *     The float view controller object is null.
         * @throws { BusinessError } 1300003 - This window manager service works abnormally. Possible cause:
         *     Internal IPC error.
         * @throws { BusinessError } 1300030 - Repeated operations on the float view. Possible cause:
         *     The float view is starting or has already started.
         * @throws { BusinessError } 1300031 - The float view state does not support this operation. Possible cause:
         *     The float view is stopping.
         * @throws { BusinessError } 1300033 - Failed to start float view. Possible causes:
         *     1. Start multiple float views.
         *     2. The main window of context is not foreground.
         * @throws { BusinessError } 1300034 - This operation conflicts with other floating windows. Possible cause:
         *     App has already started floating ball or pip window.
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        start(): Promise<void>;
        /**
         * Stops the float view. The return value of this API does not indicate that the stop process is complete. You need
         * to use the
         * [onStateChange]{@link floatView.FloatViewController.onStateChange(callback: Callback<FloatViewStateChangeInfo>)}
         * API to listen for the **STOPPED** callback to determine whether the stop is successful. This API uses a promise
         * to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 1300002 - This window state is abnormal. Possible cause:
         *     The float view controller object is null.
         * @throws { BusinessError } 1300003 - This window manager service works abnormally. Possible cause:
         *     Internal IPC error.
         * @throws { BusinessError } 1300030 - Repeated operations on the float view. Possible cause:
         *     The float view is stopping or has already stopped.
         * @throws { BusinessError } 1300031 - This operation is not supported on the float view in the current state.
         *     Possible cause: The float view window is not started.
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        stop(): Promise<void>;
        /**
         * Sets whether the float view is visible when the application is running in the foreground. This API uses a promise
         * to return the result.
         *
         * After the float view is created and before this API is called, the float view is visible by default when the
         * application is running in the foreground.
         *
         * @param { boolean } isVisible - Whether the float view is visible when the application is running in the
         *     foreground. The value **true** indicates that the window is visible, and **false** indicates the opposite.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 1300002 - This window state is abnormal. Possible cause:
         *     The float view controller object is null.
         * @throws { BusinessError } 1300003 - This window manager service works abnormally. Possible cause:
         *     Internal IPC error.
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        setFloatViewVisibilityInApp(isVisible: boolean): Promise<void>;
        /**
         * Restores the main window of the float view to display in the foreground. If this API is called when the main
         * window is already in the foreground, the main window level will be raised. This API can be used only after the
         * float view is clicked. If the main window is in the **PAUSED** state or in the multitasking state, error code 130
         * 0032 will be returned if this API is called. This API uses a promise to return the result.
         *
         * @param { Record<string, Object> } [wantParameters] - Custom parameters passed to the main window when the main
         *     window of the float view is restored. The main window will receive the parameters when the
         *     [onNewWant]{@link @ohos.app.ability.AbilityLifecycleCallback:AbilityLifecycleCallback#onNewWant?(ability: UIAbility)}
         *     callback is triggered. The default value is empty, indicating that no custom parameters are passed to the
         *     main window.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 1300002 - This window state is abnormal. Possible cause:
         *     The float view controller object is null.
         * @throws { BusinessError } 1300003 - This window manager service works abnormally. Possible cause:
         *     Internal IPC error.
         * @throws { BusinessError } 1300031 - This operation is not supported on the float view in the current state.
         *     Possible cause: The float view window is not started when restoring.
         * @throws { BusinessError } 1300032 - Failed to restore the main window. Possible cause:
         *     1. User has never clicked the float view window before restore.
         *     2. The float view window is not in the foreground.
         *     3. The main window is in PAUSED lifecycle state.
         *     4. The main window is in background during recent.
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        restoreMainWindow(wantParameters?: Record<string, Object>): Promise<void>;
        /**
         * Obtains the properties of the float view.
         *
         * @returns { FloatViewProperties } Properties of the float view.
         * @throws { BusinessError } 1300002 - This window state is abnormal. Possible cause:
         *     The float view controller object is null.
         * @throws { BusinessError } 1300031 - This operation is not supported on the float view in the current state.
         *     Possible cause: The float view window has not started, has stopped, or is in an error state.
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        getWindowProperties(): FloatViewProperties;
        /**
         * Registers a callback for listening to float view state changes. To prevent memory leaks, remember to unregister
         * the callback when it is no longer needed.
         *
         * @param { Callback<FloatViewStateChangeInfo> } callback - Callback used to return the status change information of
         *     the current float view.
         * @throws { BusinessError } 1300002 - This window state is abnormal. Possible cause:
         *     The float view controller object is null.
         * @throws { BusinessError } 1300030 - Repeated operations on the float view. Possible cause:
         *     The callback has already registered.
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        onStateChange(callback: Callback<FloatViewStateChangeInfo>): void;
        /**
         * Unregisters the callback for listening to float view state changes.
         *
         * @param { Callback<FloatViewStateChangeInfo> } [callback] - Callback used to return the status change information
         *     of the current float view. If a value is passed in, the corresponding callback is unregistered. If no value
         *     is passed in, all callbacks associated with the status change event of the float view are unregistered.
         * @throws { BusinessError } 1300002 - This window state is abnormal. Possible cause:
         *     The float view controller object is null.
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        offStateChange(callback?: Callback<FloatViewStateChangeInfo>): void;
        /**
         * Registers a callback for listening to changes in the rectangular area (position and size) of the float view. To
         * prevent memory leaks, remember to unregister the callback when it is no longer needed.
         *
         * @param { Callback<FloatViewRectChangeInfo> } callback - Callback used to return the rectangle area change
         *     information of the current float view.
         * @throws { BusinessError } 1300002 - This window state is abnormal. Possible cause:
         *     The float view controller object is null.
         * @throws { BusinessError } 1300030 - Repeated operations on the float view. Possible cause:
         *     The callback has already registered.
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        onRectChange(callback: Callback<FloatViewRectChangeInfo>): void;
        /**
         * Unregisters the callback for listening to changes in the rectangular area of the float view.
         *
         * @param { Callback<FloatViewRectChangeInfo> } [callback] - Callback used to return the rectangle area change
         *     information of the current float view. If a value is passed in, the corresponding callback is unregistered.
         *     If no value is passed in, all callbacks associated with the rectangle area change event of the float view are
         *     unregistered.
         * @throws { BusinessError } 1300002 - This window state is abnormal. Possible cause:
         *     The float view controller object is null.
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        offRectChange(callback?: Callback<FloatViewRectChangeInfo>): void;
        /**
         * Registers a callback for listening to limit changes of the float view. When the limit changes, for example, when
         * the device is folded or unfolded, the callback is triggered. To prevent memory leaks, remember to unregister the
         * callback when it is no longer needed.
         *
         * @param { Callback<FloatViewLimits> } callback - Callback used to return the limit change information of the
         *     current float view.
         * @throws { BusinessError } 1300002 - This window state is abnormal. Possible cause:
         *     The float view controller object is null.
         * @throws { BusinessError } 1300030 - Repeated operations on the float view. Possible cause:
         *     The callback has already registered.
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        onLimitsChange(callback: Callback<FloatViewLimits>): void;
        /**
         * Unregisters the callback for listening to limit changes of the float view.
         *
         * @param { Callback<FloatViewLimits> } [callback] - Callback used to return the limit change information of the
         *     current float view. If a value is passed in, the corresponding callback is unregistered. If no value is
         *     passed in, all callbacks associated with the limit change event of the float view are unregistered.
         * @throws { BusinessError } 1300002 - This window state is abnormal. Possible cause:
         *     The float view controller object is null.
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        offLimitsChange(callback?: Callback<FloatViewLimits>): void;
    }
    /**
     * Provides the template type of the float view.
     *
     * @syscap SystemCapability.Window.SessionManager
     * @stagemodelonly
     * @since 26.0.0
     */
    enum FloatViewTemplateType {
        /**
         * Rectangle with rounded corners.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        ROUNDED_RECTANGLE = 0,
        /**
         * Horizontal bar rectangle.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        HORIZONTAL_BAR = 1
    }
    /**
     * Provides the properties of the float view.
     *
     * @syscap SystemCapability.Window.SessionManager
     * @stagemodelonly
     * @since 26.0.0
     */
    interface FloatViewProperties {
        /**
         * Template type of the float view.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        templateType: FloatViewTemplateType;
        /**
         * Float view ID.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        windowId: number;
        /**
         * ID of the display where the float view is located.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        displayId: number;
        /**
         * Rectangle area of the float view.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        windowRect: window.Rect;
        /**
         * Scale factor of the float view.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        windowScale: number;
        /**
         * Avoid area for the content of the float view.
         *
         * Note:
         *
         * On the page loaded by [setUIContext]{@link floatView.FloatViewController.setUIContext}, components in the avoid
         * area do not respond to gesture events. When adding components that require gesture response events, avoid the
         * area.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        avoidArea: window.AvoidArea;
        /**
         * Whether the float view is in the sidebar. **true**: in the sidebar; **false**: not in the sidebar.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        inSidebar: boolean;
    }
    /**
     * Provides the aspect ratio range of the float view. The aspect ratio is obtained by dividing the width of the
     * rectangular area of the window by its height.
     *
     * @syscap SystemCapability.Window.SessionManager
     * @stagemodelonly
     * @since 26.0.0
     */
    interface RatioLimit {
        /**
         * Minimum aspect ratio of the float view.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        minRatio: number;
        /**
         * Maximum aspect ratio of the float view.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        maxRatio: number;
    }
    /**
     * Provides the limits of the float view.
     *
     * @syscap SystemCapability.Window.SessionManager
     * @stagemodelonly
     * @since 26.0.0
     */
    interface FloatViewLimits {
        /**
         * Minimum size of the float view.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        minSize: window.Size;
        /**
         * Maximum size of the float view.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        maxSize: window.Size;
        /**
         * Aspect ratio range of the float view.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        ratioLimits: Array<RatioLimit>;
    }
    /**
     * Provides the state change information of the float view.
     *
     * @syscap SystemCapability.Window.SessionManager
     * @stagemodelonly
     * @since 26.0.0
     */
    interface FloatViewStateChangeInfo {
        /**
         * State of the float view.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        state: FloatViewState;
        /**
         * Reason why the float view stops. This parameter is valid only when **state** is set to
         * **FloatViewState.STOPPED**. In other states, this parameter is an empty string by default. The stop reasons and
         * their meanings are as follows:
         *
         * **"APP_STOP"**: The application proactively stops the float view.
         *
         * **"STOP_IN_SIDEBAR"**: The float view is closed in the sidebar.
         *
         * **"TITLE_BAR_STOP_CLICK"**: The float view is closed by clicking the close button on the title bar.
         *
         * **"DUMPSTER_STOP"**: The float view is dragged to the trash can.
         *
         * **"REPLACE_STOP"**: The float view is occupied by another float view.
         *
         * **"FLOATING_BALL_STOP"**: The float view stops when the bound floating ball stops.
         *
         * **"MAIN_WINDOW_DESTROY_STOP"**: The float view stops after the main window associated with the context is
         * destroyed.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        stopReason: string;
    }
    /**
     * Enumerates the states of the float view.
     *
     * @syscap SystemCapability.Window.SessionManager
     * @stagemodelonly
     * @since 26.0.0
     */
    enum FloatViewState {
        /**
         * The float view has been started and displayed.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        STARTED = 1,
        /**
         * The float view has been hidden. This event is triggered when the user swipes up to enter the multitasking screen
         * or when the [setFloatViewVisibilityInApp]{@link floatView.FloatViewController.setFloatViewVisibilityInApp} API is
         * called to hide the float view when the application is in the foreground and the application is in the foreground.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        HIDDEN = 2,
        /**
         * The float view has been stopped.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        STOPPED = 3,
        /**
         * The float view is in the sidebar.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        IN_SIDEBAR = 4,
        /**
         * The float view is switched to the floating ball.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        IN_FLOATING_BALL = 5,
        /**
         * An exception occurs in the float view.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        ERROR = 6
    }
    /**
     * Provides the rectangle area change information of the float view.
     *
     * @syscap SystemCapability.Window.SessionManager
     * @stagemodelonly
     * @since 26.0.0
     */
    interface FloatViewRectChangeInfo {
        /**
         * Rectangle area of the float view.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        windowRect: window.Rect;
        /**
         * Scale factor of the float view.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        windowScale: number;
        /**
         * Reason for the change of the rectangle area of the float view. The reasons and their meanings are as follows:
         *
         * **"POSITION_CHANGE"**: The position changes.
         *
         * **"SIZE_CHANGE"**: The size changes.
         *
         * **"RECT_CHANGE"**: Both the position and size change.
         *
         * @syscap SystemCapability.Window.SessionManager
         * @stagemodelonly
         * @since 26.0.0
         */
        reason: string;
    }
}
export default floatView;

```
