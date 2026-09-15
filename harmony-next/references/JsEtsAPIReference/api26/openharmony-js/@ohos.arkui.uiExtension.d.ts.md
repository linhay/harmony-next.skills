# @ohos.arkui.uiExtension.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2024 Huawei Device Co., Ltd.
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
import { Callback } from './@ohos.base';
import window from './@ohos.window';
/**
 * The **uiExtension** module provides APIs for the
 * [EmbeddedUIExtensionAbility](docroot://application-models/embeddeduiextensionability.md) (or
 * [UIExtensionAbility]{@link @ohos.app.ability.UIExtensionAbility:UIExtensionAbility}) to obtain the host application
 * window information or the information about the corresponding
 * [EmbeddedComponent]{@link ./@internal/component/ets/embedded_component}<!--Del--> (or
 * [UIExtensionComponent]{@link ./@internal/component/ets/ui_extension_component})<!--DelEnd--> component.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @atomicservice
 * @since 12
 */
declare namespace uiExtension {
    /**
     * The proxy of the UIExtension window.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @atomicservice
     * @since 12
     */
    interface WindowProxy {
        /**
         * Obtains the area where this window cannot be displayed, for example, the system bar area, notch, gesture area,
         * and soft keyboard area.
         *
         * @param { window.AvoidAreaType } type - Type of the avoidance area.
         * @returns { window.AvoidArea } Avoidance area for the content of the host window.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1. Mandatory parameters are left unspecified.
         *     2. Incorrect parameters types.
         *     3. Parameter verification failed.
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @atomicservice
         * @since 12
         */
        getWindowAvoidArea(type: window.AvoidAreaType): window.AvoidArea;
        /**
         * Subscribes to events of system avoidance area changes.
         *
         * @param { 'avoidAreaChange' } type - Event type. The value is fixed at **'avoidAreaChange'**, indicating the event
         *     of changes to the area where the window cannot be displayed.
         * @param { Callback<AvoidAreaInfo> } callback - Callback function that receives the information about the current
         *     avoidance area.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1. Mandatory parameters are left unspecified.
         *     2. Incorrect parameters types.
         *     3. Parameter verification failed.
         * @throws { BusinessError } 1300002 - Abnormal state. Possible causes:
         *     1. The listening type is not supported.
         *     2. The listener has been registered.
         *     3. The UIExtension window proxy is abnormal.
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @atomicservice
         * @since 12
         */
        on(type: 'avoidAreaChange', callback: Callback<AvoidAreaInfo>): void;
        /**
         * Unsubscribes from events of system avoidance area changes.
         *
         * @param { 'avoidAreaChange' } type - Event type. The value is fixed at **'avoidAreaChange'**, indicating the event
         *     of changes to the area where the window cannot be displayed.
         * @param { Callback<AvoidAreaInfo> } callback - Callback used for unsubscription. If a value is passed in, the
         *     corresponding subscription is canceled. If no value is passed in, all subscriptions to the specified event
         *     are canceled.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1. Mandatory parameters are left unspecified.
         *     2. Incorrect parameters types.
         *     3. Parameter verification failed.
         * @throws { BusinessError } 1300002 - Abnormal state. Possible causes:
         *     1. The listening type is not supported.
         *     2. The listening type is not registered.
         *     3. The listener has not been registered.
         *     4. The UIExtension window proxy is abnormal.
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @atomicservice
         * @since 12
         */
        off(type: 'avoidAreaChange', callback?: Callback<AvoidAreaInfo>): void;
        /**
         * Subscribes to size change events of the component (**EmbeddedComponent** or **UIExtensionComponent**).
         *
         * @param { 'windowSizeChange' } type - Event type. The value is fixed at **'windowSizeChange'**, indicating the
         *     component (**EmbeddedComponent** or **UIExtensionComponent**) size change events.
         * @param { Callback<window.Size> } callback - Callback function that receives the current component size as the
         *     input parameter.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1. Mandatory parameters are left unspecified.
         *     2. Incorrect parameters types.
         *     3. Parameter verification failed.
         * @throws { BusinessError } 1300002 - Abnormal state. Possible causes:
         *     1. The listening type is not supported.
         *     2. The listener has been registered.
         *     3. The UIExtension window proxy is abnormal.
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @atomicservice
         * @since 12
         */
        on(type: 'windowSizeChange', callback: Callback<window.Size>): void;
        /**
         * Unsubscribes from size change events of the component (**EmbeddedComponent** or **UIExtensionComponent**).
         *
         * @param { 'windowSizeChange' } type - Event type. The value is fixed at **'windowSizeChange'**, indicating the
         *     component (**EmbeddedComponent** or **UIExtensionComponent**) size change events.
         * @param { Callback<window.Size> } [callback] - Callback used to return the size of the current component (
         *     **EmbeddedComponent** or **UIExtensionComponent**). If a value is passed in, the corresponding subscription
         *     is canceled. If no value is passed in, all subscriptions to the specified event are canceled.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1. Mandatory parameters are left unspecified.
         *     2. Incorrect parameters types.
         *     3. Parameter verification failed.
         * @throws { BusinessError } 1300002 - Abnormal state. Possible causes:
         *     1. The listening type is not supported.
         *     2. The listening type is not registered.
         *     3. The listener has not been registered.
         *     4. The UIExtension window proxy is abnormal.
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @atomicservice
         * @since 12
         */
        off(type: 'windowSizeChange', callback?: Callback<window.Size>): void;
        /**
         * Creates a subwindow for this window proxy. This API uses a promise to return the result.
         *
         * @param { string } name - Name of the subwindow.
         * @param { window.SubWindowOptions } subWindowOptions - Parameters used for creating the subwindow.
         * @returns { Promise<window.Window> } Promise used to return the subwindow created.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1. Mandatory parameters are left unspecified.
         *     2. Incorrect parameters types.
         *     3. Parameter verification failed.
         * @throws { BusinessError } 801 - Capability not supported. Failed to call the API due to limited device
         *     capabilities.
         * @throws { BusinessError } 1300002 - This window state is abnormal. Possible causes:
         *     1. The window is not created or destroyed.
         *     2. Internal task error.
         *     3. The subWindow has been created and cannot be created again.
         *     4. It is not allowed to create non-secure window when secure extension exists.
         * @throws { BusinessError } 1300035 - Creating a subwindow is not allowed in the current context. Possible cause:
         *     1. An AgentUIExtensionAbility cannot create a subwindow.
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @atomicservice
         * @since 12
         */
        createSubWindowWithOptions(name: string, subWindowOptions: window.SubWindowOptions): Promise<window.Window>;
        /**
         * Create subwindow.
         *
         * @param { string } name - Name of the subwindow.
         * @param { window.SubWindowOptions } subWindowConfig - Configuration parameters for creating the subwindow.
         * @param { boolean } followCreatorLifecycle - Whether the lifecycle of the subwindow follows creator of
         *     subwindow. If true, when the creator goes to background, the subwindow will also go to background, when the
         *     creator returns to foreground, the subwindow will also return to foreground. If false, the subwindow will
         *     not change when the creator goes to background or returns to foreground.
         * @returns { Promise<window.Window> } Promise used to return the subwindow.
         * @throws { BusinessError } 801 - Capability not supported.
         *     Failed to call the API due to limited device capabilities.
         * @throws { BusinessError } 1300002 - This window state is abnormal. Possible cause:
         *     1. The window is not created or destroyed.
         *     2. Internal task error.
         *     3. The subWindow has been created and cannot be created again.
         *     4. It is not allowed to create non-secure window when secure extension exists.
         * @throws { BusinessError } 1300035 - Creating a subwindow is not allowed in the current context. Possible cause:
         *     1. An AgentUIExtensionAbility cannot create a subwindow.
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @since 23
         */
        createSubWindowWithOptions(name: string, subWindowConfig: window.SubWindowOptions, followCreatorLifecycle: boolean): Promise<window.Window>;
        /**
         * Information about the component (**EmbeddedComponent** or **UIExtensionComponent**).
         *
         * Note: Due to architecture restrictions, avoid obtaining the value in
         * [onSessionCreate]{@link @ohos.app.ability.UIExtensionAbility:UIExtensionAbility.onSessionCreate}. Instead, when
         * possible, obtain the value after receiving the
         * [on('windowSizeChange')]{@link @ohos.arkui.uiExtension:uiExtension.WindowProxy.on(type: 'windowSizeChange', callback: Callback<window.Size>)}
         * callback.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @atomicservice
         * @since 14
         */
        properties: WindowProxyProperties;
        /**
         * Unsubscribes from position and size change events of the component (**EmbeddedComponent** or
         * **UIExtensionComponent**).
         *
         * @param { 'rectChange' } type - Event type. The value is fixed at **'rectChange'**, indicating the rectangle
         *     change event for the component (**EmbeddedComponent** or **UIExtensionComponent**).
         * @param { Callback<RectChangeOptions> } callback - Callback used to return the current rectangle change values and
         *     the reason for the change of the component (**EmbeddedComponent** or **UIExtensionComponent**). If a value is
         *     passed in, the corresponding subscription is canceled. If no value is passed in, all subscriptions to the
         *     specified event are canceled.
         * @throws { BusinessError } 401 - Parameter error. Possible cause:
         *     1. Mandatory parameters are left unspecified.
         *     2. Incorrect parameters types.
         *     3. Parameter verification failed.
         * @throws { BusinessError } 801 - Capability not supported. Failed to call the API due to limited device
         *     capabilities.
         * @throws { BusinessError } 1300002 - Abnormal state. Possible causes:
         *     1. The listening type is not supported.
         *     2. The listening type is not registered.
         *     3. The listener has not been registered.
         *     4. The UIExtension window proxy is abnormal.
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @atomicservice
         * @since 14
         */
        off(type: 'rectChange', callback?: Callback<RectChangeOptions>): void;
        /**
         * Sets the events that the component (**EmbeddedComponent** or **UIExtensionComponent**) will occupy, preventing
         * the host from responding to these events within the component's area.
         *
         * @param { number } eventFlags - Type of events to occupy. For details about the available values, see
         *     [EventFlag]{@link uiExtension.EventFlag}.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error. Possible cause:
         *     1. Mandatory parameters are left unspecified.
         *     2. Incorrect parameters types.
         * @throws { BusinessError } 1300002 - This window state is abnormal. Possible cause:
         *     1. The window is not created or destroyed.
         *     2. Internal task error.
         * @throws { BusinessError } 1300003 - This window manager service works abnormally.
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @atomicservice
         * @since 18
         */
        occupyEvents(eventFlags: number): Promise<void>;
        /**
         * Subscribes to position and size change events of the component (**EmbeddedComponent** or **UIExtensionComponent**
         * ).
         *
         * @param { 'rectChange' } type - Event type. The value is fixed at **'rectChange'**, indicating the rectangle
         *     change event for the component (**EmbeddedComponent** or **UIExtensionComponent**).
         * @param { "number" } reasons - Reason why the position and size of the component (**EmbeddedComponent** or
         *     **UIExtensionComponent**) change. For details about the values, see
         *     [RectChangeReason]{@link uiExtension.RectChangeReason}.
         * @param { Callback<RectChangeOptions> } callback - Callback used to return the current rectangle change values and
         *     the reason for the change of the component (**EmbeddedComponent** or **UIExtensionComponent**).
         * @throws { BusinessError } 401 - Parameter error. Possible cause:
         *     1. Mandatory parameters are left unspecified.
         *     2. Incorrect parameters types.
         *     3. Parameter verification failed.
         * @throws { BusinessError } 801 - Capability not supported. Failed to call the API due to limited device
         *     capabilities.
         * @throws { BusinessError } 1300002 - Abnormal state. Possible causes:
         *     1. The listening type is not supported.
         *     2. The listener has been registered.
         *     3. The UIExtension window proxy is abnormal.
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @atomicservice
         * @since 14
         */
        on(type: 'rectChange', reasons: number, callback: Callback<RectChangeOptions>): void;
    }
    /**
     * Represents the information about the avoidance area of the window.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @atomicservice
     * @since 12
     */
    interface AvoidAreaInfo {
        /**
         * Type of the avoidance area of the window.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @atomicservice
         * @since 12
         */
        type: window.AvoidAreaType;
        /**
         * Avoidance area for the content of the window.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @atomicservice
         * @since 12
         */
        area: window.AvoidArea;
    }
    /**
     * Provides information about a component.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @atomicservice
     * @since 14
     */
    interface WindowProxyProperties {
        /**
         * Position and size of the component (**EmbeddedComponent** or **UIExtensionComponent**).
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @atomicservice
         * @since 14
         */
        uiExtensionHostWindowProxyRect: window.Rect;
    }
    /**
     * Provides the values and reasons returned when the rectangle (position and size) of the component (
     * **EmbeddedComponent** or **UIExtensionComponent**) changes.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @atomicservice
     * @since 14
     */
    interface RectChangeOptions {
        /**
         * New values of the rectangle of the component after the change.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @atomicservice
         * @since 14
         */
        rect: window.Rect;
        /**
         * Reason for the rectangle change.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @atomicservice
         * @since 14
         */
        reason: RectChangeReason;
    }
    /**
     * Enumerates event types.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @atomicservice
     * @since 18
     */
    enum EventFlag {
        /**
         * Pan-left event.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @atomicservice
         * @since 18
         */
        EVENT_PAN_GESTURE_LEFT = 0x00000001,
        /**
         * Pan-right event.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @atomicservice
         * @since 18
         */
        EVENT_PAN_GESTURE_RIGHT = 0x00000002,
        /**
         * Long press event.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @atomicservice
         * @since 18
         */
        EVENT_LONG_PRESS = 0x00000200,
        /**
         * Pan-up event.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @atomicservice
         * @since 18
         */
        EVENT_PAN_GESTURE_UP = 0x00000004,
        /**
         * Click event.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @atomicservice
         * @since 18
         */
        EVENT_CLICK = 0x00000100,
        /**
         * No event.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @atomicservice
         * @since 18
         */
        EVENT_NONE = 0x00000000,
        /**
         * Pan-down event.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @atomicservice
         * @since 18
         */
        EVENT_PAN_GESTURE_DOWN = 0x00000008
    }
    /**
     * Enumerates the reasons for changes in the rectangle (position and size) of the component (**EmbeddedComponent** or
     * **UIExtensionComponent**).
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @atomicservice
     * @since 14
     */
    enum RectChangeReason {
        /**
         * The rectangle of the host window containing the component changes.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @atomicservice
         * @since 14
         */
        HOST_WINDOW_RECT_CHANGE = 0x0001
    }
}
export default uiExtension;

```
