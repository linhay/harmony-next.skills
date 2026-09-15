# @ohos.multimodalInput.inputConsumer.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (C) 2021-2025 Huawei Device Co., Ltd.
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
 * @file Global Shortcut Keys
 * @kit InputKit
 */
import { Callback } from './@ohos.base';
import { KeyEvent } from './@ohos.multimodalInput.keyEvent';
/**
 * The **inputConsumer** module implements listening for combination key events as well as listening and interception
 * for volume key events.
 *
 * > **NOTE**
 * >
 * > - Global shortcut keys are combination keys defined by the system or application. System shortcut keys are defined
 * > by the system, and application shortcut keys are defined by applications.
 *
 * @syscap SystemCapability.MultimodalInput.Input.InputConsumer
 * @since 14
 */
declare namespace inputConsumer {
    /**
     * Defines shortcut key options.
     *
     * @syscap SystemCapability.MultimodalInput.Input.InputConsumer
     * @since 14
     */
    interface HotkeyOptions {
        /**
         * Modifier key set (including Ctrl, Shift, and Alt). One to four modifier keys are supported. There is no
         * requirement on the sequence of modifier keys.
         *
         * For example, in **Ctrl+Shift+Esc**, **Ctrl** and **Shift** are modifier keys.
         *
         * @syscap SystemCapability.MultimodalInput.Input.InputConsumer
         * @since 14
         */
        preKeys: Array<number>;
        /**
         * Modified key, which can be any key except the modifier keys and Meta key. For details about the keys, see
         * [@ohos.multimodalInput.keyCode (Keycode)]{@link @ohos.multimodalInput.keyCode:KeyCode}.
         *
         * For example, in **Ctrl+Shift+Esc**, **Esc** is the modifier key.
         *
         * @syscap SystemCapability.MultimodalInput.Input.InputConsumer
         * @since 14
         */
        finalKey: number;
        /**
         * Whether to report repeated key events. The value **true** means to report repeated key events, and the value
         * **false** means the opposite. The default value is **true**.
         *
         * @syscap SystemCapability.MultimodalInput.Input.InputConsumer
         * @since 14
         */
        isRepeat?: boolean;
    }
    /**
     * Sets the key event consumption configuration.
     *
     * @syscap SystemCapability.MultimodalInput.Input.InputConsumer
     * @since 16
     */
    interface KeyPressedConfig {
        /**
         * Key value.
         *
         * **Note:** Since API version 26.0.0, the
         * [KEYCODE_FINGERPRINT_SLIDE_UP]{@link @ohos.multimodalInput.keyCode:KeyCode} and
         * [KEYCODE_FINGERPRINT_SLIDE_DOWN]{@link @ohos.multimodalInput.keyCode:KeyCode} keys are supported. The keys are
         * not universal device keys. Before using them, check whether the current device supports the reporting of related
         * key events. For details, see
         * [Preferential Response of System Function Keys](docroot://device/input/keypressed-guidelines.md).
         *
         * Since API version 21, the [KEYCODE_MEDIA_PLAY_PAUSE]{@link @ohos.multimodalInput.keyCode:KeyCode},
         * [KEYCODE_MEDIA_NEXT]{@link @ohos.multimodalInput.keyCode:KeyCode}, and
         * [KEYCODE_MEDIA_PREVIOUS]{@link @ohos.multimodalInput.keyCode:KeyCode} keys are supported.
         *
         * In API version 20 or earlier versions, only the [KEYCODE_VOLUME_UP]{@link @ohos.multimodalInput.keyCode:KeyCode}
         * and [KEYCODE_VOLUME_DOWN]{@link @ohos.multimodalInput.keyCode:KeyCode} keys are supported.
         *
         * @type { number } [since 16 - 24]
         * @syscap SystemCapability.MultimodalInput.Input.InputConsumer
         * @since 16
         */
        key: number;
        /**
         * Subscription type.
         *
         * **Note**: Since API version 21, the value of this parameter can be **1** or **2**. The value **1** indicates
         * subscription to only key press events, and the value **2** indicates subscription to both key press and release
         * events.
         *
         * In API version 20 or earlier versions, the value of this parameter can only be set to **1**, indicating
         * subscription to only key press events.
         *
         * @syscap SystemCapability.MultimodalInput.Input.InputConsumer
         * @since 16
         */
        action: number;
        /**
         * Whether to report repeated key events. The value **true** means to report repeated key events, and the value
         * **false** means the opposite. The default value is **true**.
         *
         * @syscap SystemCapability.MultimodalInput.Input.InputConsumer
         * @since 16
         */
        isRepeat: boolean;
    }
    /**
     * Obtains all system shortcut keys. This API uses a promise to return the result.
     *
     * @returns { Promise<Array<HotkeyOptions>> } Promise used to return the list of all system shortcut keys.
     * @throws { BusinessError } 801 - Capability not supported.
     * @syscap SystemCapability.MultimodalInput.Input.InputConsumer
     * @since 14
     */
    function getAllSystemHotkeys(): Promise<Array<HotkeyOptions>>;
    /**
     * Subscribes to application shortcut key change events. This API obtains combination key input events that meet the
     * specified conditions, and uses an asynchronous callback to return the result.
     *
     * @param { 'hotkeyChange' } type - Event type. This parameter has a fixed value of **hotkeyChange**.
     * @param { HotkeyOptions } hotkeyOptions - Shortcut key options.
     * @param { Callback<HotkeyOptions> } callback - Callback used to return the combination key input events that meet
     *     the conditions.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 4200002 - The hotkey has been used by the system.
     * @throws { BusinessError } 4200003 - The hotkey has been subscribed to by another.
     * @syscap SystemCapability.MultimodalInput.Input.InputConsumer
     * @since 14
     */
    function on(type: 'hotkeyChange', hotkeyOptions: HotkeyOptions, callback: Callback<HotkeyOptions>): void;
    /**
     * Unsubscribes from application shortcut key change events. This API uses an asynchronous callback to return the
     * result.
     *
     * @param { 'hotkeyChange' } type - Event type. This parameter has a fixed value of **hotkeyChange**.
     * @param { HotkeyOptions } hotkeyOptions - Shortcut key options.
     * @param { Callback<HotkeyOptions> } callback - Callback to unregister. If this parameter is left unspecified,
     *     listening will be disabled for all callbacks registered for the specified shortcut key options.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported.
     * @syscap SystemCapability.MultimodalInput.Input.InputConsumer
     * @since 14
     */
    function off(type: 'hotkeyChange', hotkeyOptions: HotkeyOptions, callback?: Callback<HotkeyOptions>): void;
    /**
     * Subscribes to key press events. If the current application is in the foreground focus window, a callback is
     * triggered when the specified key is pressed. This API uses an asynchronous callback to return the result.
     *
     * If the API call is successful, the system's default response to the key event will be intercepted; that is, system-
     * level actions, such as volume adjustment, will no longer be triggered. To restore the system response, call
     * [off]{@link inputConsumer.off(type: 'keyPressed', callback?: Callback<KeyEvent>)} to disable listening for the key
     * event.
     *
     * @param { 'keyPressed' } type - Event type. This parameter has a fixed value of **keyPressed**.
     * @param { KeyPressedConfig } options - Sets the key event consumption configuration.
     * @param { Callback<KeyEvent> } callback - Callback used to return key press events. Ensure that different callbacks
     *     are used for different key events. Otherwise, the subscription does not take effect.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported.
     * @syscap SystemCapability.MultimodalInput.Input.InputConsumer
     * @since 16
     */
    function on(type: 'keyPressed', options: KeyPressedConfig, callback: Callback<KeyEvent>): void;
    /**
     * Unsubscribes from key press events. This API uses an asynchronous callback to return the result. If the API call is
     * successful, the system's default response to the key event will be resumed; that is, system-level actions, such as
     * volume adjustment, will be triggered normally.
     *
     * @param { 'keyPressed' } type - Event type. This parameter has a fixed value of **keyPressed**.
     * @param { Callback<KeyEvent> } callback - Callback to unregister. If this parameter is not specified, listening will
     *     be disabled for all registered callbacks.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported.
     * @syscap SystemCapability.MultimodalInput.Input.InputConsumer
     * @since 16
     */
    function off(type: 'keyPressed', callback?: Callback<KeyEvent>): void;
}
export default inputConsumer;

```
