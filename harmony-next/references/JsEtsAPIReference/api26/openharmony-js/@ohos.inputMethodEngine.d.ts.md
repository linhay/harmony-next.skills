# @ohos.inputMethodEngine.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2021-2024 Huawei Device Co., Ltd.
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
 * @kit IMEKit
 */
import type { AsyncCallback, Callback } from './@ohos.base';
import type { KeyEvent as InputKeyEvent } from './@ohos.multimodalInput.keyEvent';
import InputMethodSubtype from './@ohos.InputMethodSubtype';
import BaseContext from './application/BaseContext';
import window from './@ohos.window';
import { InputMethodExtraConfig } from './@ohos.inputMethod.ExtraConfig';
/**
 * The **inputMethodEngine** module is oriented to input method applications (including system and third-party input
 * method applications). With the APIs of this module, input method applications are able to create soft keyboard
 * windows, insert or delete characters, select text, and listen for physical keyboard events.
 *
 * @syscap SystemCapability.MiscServices.InputMethodFramework
 * @since 8
 */
declare namespace inputMethodEngine {
    /**
     * No function is specified for the key.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 8
     */
    const ENTER_KEY_TYPE_UNSPECIFIED: number;
    /**
     * Key that executes a command or navigates to a specific location.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 8
     */
    const ENTER_KEY_TYPE_GO: number;
    /**
     * Key that initiates a search operation.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 8
     */
    const ENTER_KEY_TYPE_SEARCH: number;
    /**
     * Key that sends the text to its target.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 8
     */
    const ENTER_KEY_TYPE_SEND: number;
    /**
     * Key that moves the focus to the next item in a sequence.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 8
     */
    const ENTER_KEY_TYPE_NEXT: number;
    /**
     * Key that indicates that a task or input is complete.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 8
     */
    const ENTER_KEY_TYPE_DONE: number;
    /**
     * Key that moves the focus to the previous item in a sequence.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 8
     */
    const ENTER_KEY_TYPE_PREVIOUS: number;
    /**
     * Key that inserts a new line.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 12
     */
    const ENTER_KEY_TYPE_NEWLINE: number;
    /**
     * Any type of edit box.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 8
     */
    const PATTERN_NULL: number;
    /**
     * Text edit box.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 8
     */
    const PATTERN_TEXT: number;
    /**
     * Number edit box.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 8
     */
    const PATTERN_NUMBER: number;
    /**
     * Phone number edit box.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 8
     */
    const PATTERN_PHONE: number;
    /**
     * Date edit box.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 8
     */
    const PATTERN_DATETIME: number;
    /**
     * Email edit box.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 8
     */
    const PATTERN_EMAIL: number;
    /**
     * URI edit box.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 8
     */
    const PATTERN_URI: number;
    /**
     * Password edit box.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 8
     */
    const PATTERN_PASSWORD: number;
    /**
     * Screen lock password edit box.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 11
     */
    const PATTERN_PASSWORD_SCREEN_LOCK: number;
    /**
     * Numeric password edit box.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 11
     */
    const PATTERN_PASSWORD_NUMBER: number;
    /**
     * User name edit box. The value is fixed at 10.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @stagemodelonly
     * @since 20
     */
    const PATTERN_USER_NAME: number;
    /**
     * New password edit box. The value is fixed at 11.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @stagemodelonly
     * @since 20
     */
    const PATTERN_NEW_PASSWORD: number;
    /**
     * Edit box for numbers with decimal points. The value is fixed at 12.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @stagemodelonly
     * @since 20
     */
    const PATTERN_NUMBER_DECIMAL: number;
    /**
     * Verification code edit box. The value is fixed at 13.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @stagemodelonly
     * @since 20
     */
    const PATTERN_ONE_TIME_CODE: number;
    /**
     * The edit box is being selected.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 8
     */
    const FLAG_SELECTING: number;
    /**
     * The edit box allows only single-line input.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 8
     */
    const FLAG_SINGLE_LINE: number;
    /**
     * The edit box is displayed in half-screen mode.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 8
     */
    const DISPLAY_MODE_PART: number;
    /**
     * The edit box is displayed in full screen.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 8
     */
    const DISPLAY_MODE_FULL: number;
    /**
     * ASCII values are allowed.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 8
     */
    const OPTION_ASCII: number;
    /**
     * No input attribute is specified.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 8
     */
    const OPTION_NONE: number;
    /**
     * Characters are allowed.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 8
     */
    const OPTION_AUTO_CAP_CHARACTERS: number;
    /**
     * Sentences are allowed.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 8
     */
    const OPTION_AUTO_CAP_SENTENCES: number;
    /**
     * Words are allowed.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 8
     */
    const OPTION_AUTO_WORDS: number;
    /**
     * Multiple lines are allowed.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 8
     */
    const OPTION_MULTI_LINE: number;
    /**
     * Half-screen style.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 8
     */
    const OPTION_NO_FULLSCREEN: number;
    /**
     * The caret moves upward.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 9
     */
    const CURSOR_UP: number;
    /**
     * The caret moves downward.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 9
     */
    const CURSOR_DOWN: number;
    /**
     * The caret moves leftward.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 9
     */
    const CURSOR_LEFT: number;
    /**
     * The caret moves rightward.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 9
     */
    const CURSOR_RIGHT: number;
    /**
     * The input method is displayed in a floating window.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 9
     */
    const WINDOW_TYPE_INPUT_METHOD_FLOAT: number;
    /**
     * Obtains an [InputMethodAbility]{@link inputMethodEngine.InputMethodAbility} instance for the input method. This API
     * can be called only by an input method.
     *
     * The input method can use the obtained instance to subscribe to a soft keyboard display/hide request event, create/
     * destroy an input method panel, and the like.
     *
     * @returns { InputMethodAbility } **InputMethodAbility** instance.
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 9
     */
    function getInputMethodAbility(): InputMethodAbility;
    /**
     * Obtains an [InputMethodEngine]{@link inputMethodEngine.InputMethodEngine} instance for the input method.
     *
     * The input method can use the obtained instance to subscribe to a soft keyboard display/hide request event.
     *
     * @returns { InputMethodEngine } **InputMethodAbility** instance.
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 8
     * @deprecated since 9
     * @useinstead inputMethodEngine.getInputMethodAbility()
     */
    function getInputMethodEngine(): InputMethodEngine;
    /**
     * Obtains a [KeyboardDelegate]{@link inputMethodEngine.KeyboardDelegate} instance for the input method.
     *
     * The input method can use the obtained instance to subscribe to a physical keyboard event, text selection change
     * event, and more.
     *
     * @returns { KeyboardDelegate } **KeyboardDelegate** instance.
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 9
     */
    function getKeyboardDelegate(): KeyboardDelegate;
    /**
     * Obtains a [KeyboardDelegate]{@link inputMethodEngine.KeyboardDelegate} instance for the input method. The input
     * method can use the obtained instance to subscribe to a physical keyboard event, text selection change event, and
     * more.
     *
     * @returns { KeyboardDelegate } **KeyboardDelegate** instance.
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 8
     * @deprecated since 9
     * @useinstead inputMethodEngine.getKeyboardDelegate()
     */
    function createKeyboardDelegate(): KeyboardDelegate;
    /**
     * Defines the private data type, which varies depending on its function.
     *
     * @unionmember { int } Number.
     * @unionmember { string } String.
     * @unionmember { boolean } Boolean.
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 12
     */
    type CommandDataType = number | string | boolean;
    /**
     * Callback triggered when the size of the input method panel changes.
     *
     * @param { window.Size } size - Panel size.
     * @param { KeyboardArea } keyboardArea - Size of the keyboard area.
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 15
     */
    export type SizeChangeCallback = (size: window.Size, keyboardArea?: KeyboardArea) => void;
    /**
     * In the following API examples, you must first use
     * [getKeyboardDelegate]{@link inputMethodEngine.getKeyboardDelegate()} to obtain a **KeyboardDelegate** instance, and
     * then call the APIs using the obtained instance.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 8
     */
    interface KeyboardController {
        /**
         * Hides the keyboard. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         */
        hide(callback: AsyncCallback<void>): void;
        /**
         * Hides the keyboard. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         */
        hide(): Promise<void>;
        /**
         * Hides the keyboard. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**. Otherwise, **err** is an error object.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 8
         * @deprecated since 9
         * @useinstead inputMethodEngine.KeyboardController.hide(callback: AsyncCallback<void>)
         */
        hideKeyboard(callback: AsyncCallback<void>): void;
        /**
         * Hides the keyboard. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 8
         * @deprecated since 9
         * @useinstead inputMethodEngine.KeyboardController.hide()
         */
        hideKeyboard(): Promise<void>;
        /**
         * Exits this input type. This API can be called only by the preconfigured default input method. This API uses an
         * asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 12800008 - input method manager service error. Possible cause:
         *     a system error, such as null pointer, IPC exception.
         * @throws { BusinessError } 12800010 - not the preconfigured default input method.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 11
         */
        exitCurrentInputType(callback: AsyncCallback<void>): void;
        /**
         * Exits this input type. This API can be called only by the preconfigured default input method. This API uses a
         * promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 12800008 - input method manager service error. Possible cause:
         *     a system error, such as null pointer, IPC exception.
         * @throws { BusinessError } 12800010 - not the preconfigured default input method.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 11
         */
        exitCurrentInputType(): Promise<void>;
    }
    /**
     * In the following API examples, you must first use
     * [getInputMethodEngine]{@link inputMethodEngine.getInputMethodEngine} to obtain an **InputMethodEngine** instance,
     * and then call the APIs using the obtained instance.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 8
     * @deprecated since 23
     * @useinstead inputMethodEngine.InputMethodAbility
     */
    interface InputMethodEngine {
        /**
         * Enables listening for the input method binding event. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { 'inputStart' } type - Event type, which is **'inputStart'**.
         * @param { function } callback - Callback used to return the **KeyboardController** and **TextInputClient**
         *     instances.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 8
         * @deprecated since 23
         * @useinstead inputMethodEngine.InputMethodAbility.on(type: 'inputStart', callback: (kbController: KeyboardController, inputClient: InputClient) => void)
         */
        on(type: 'inputStart', callback: (kbController: KeyboardController, textInputClient: TextInputClient) => void): void;
        /**
         * Disables listening for the input method binding event.
         *
         * @param { 'inputStart' } type - Event type, which is **'inputStart'**.
         * @param { function } callback - Callback to unregister. If this parameter is not specified, this API unregisters
         *     all callbacks for the specified type.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 8
         * @deprecated since 23
         * @useinstead inputMethodEngine.InputMethodAbility.off(type: 'inputStart', callback?: (kbController: KeyboardController, inputClient: InputClient) => void)
         */
        off(type: 'inputStart', callback?: (kbController: KeyboardController, textInputClient: TextInputClient) => void): void;
        /**
         * Enables listening for a keyboard visibility event. This API uses an asynchronous callback to return the result.
         *
         * @param { 'keyboardShow' | 'keyboardHide' } type - Event type.
         *     <br>- The value **'keyboardShow'** indicates the keyboard display event.
         *     <br>- The value **'keyboardHide'** indicates the keyboard hiding event.
         * @param { function } callback - Callback used to return the result.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 8
         * @deprecated since 23
         * @useinstead inputMethodEngine.InputMethodAbility.on(type: 'keyboardShow' | 'keyboardHide', callback: () => void)
         */
        on(type: 'keyboardShow' | 'keyboardHide', callback: () => void): void;
        /**
         * Disables listening for a keyboard visibility event. This API uses an asynchronous callback to return the result.
         *
         * @param { 'keyboardShow' | 'keyboardHide' } type - Event type.
         *     <br>- The value **'keyboardShow'** indicates the keyboard display event.
         *     <br>- The value **'keyboardHide'** indicates the keyboard hiding event.
         * @param { function } [callback] - Callback to unregister. If this parameter is not specified, this API unregisters
         *     all callbacks for the specified type.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 8
         * @deprecated since 23
         * @useinstead inputMethodEngine.InputMethodAbility.off(type: 'keyboardShow' | 'keyboardHide', callback?: () => void)
         */
        off(type: 'keyboardShow' | 'keyboardHide', callback?: () => void): void;
    }
    /**
     * In the following API examples, you must first use
     * [getInputMethodAbility]{@link inputMethodEngine.getInputMethodAbility()} to obtain an **InputMethodAbility**
     * instance, and then call the APIs using the obtained instance.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 9
     */
    interface InputMethodAbility {
        /**
         * Enables listening for the input method binding event. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { 'inputStart' } type - Event type, which is **'inputStart'**.
         * @param { function } callback - Callback used to return instances related to input method operations.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         */
        on(type: 'inputStart', callback: (kbController: KeyboardController, inputClient: InputClient) => void): void;
        /**
         * Disables listening for the input method binding event. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { 'inputStart' } type - Event type, which is **'inputStart'**.
         * @param { function } [callback] - Callback to unregister. If this parameter is not specified, this API unregisters
         *     all callbacks for the specified type.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         */
        off(type: 'inputStart', callback?: (kbController: KeyboardController, inputClient: InputClient) => void): void;
        /**
         * Enables listening for the input method unbinding event. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { 'inputStop' } type - Event type, which is **'inputStop'**.
         * @param { function } callback - Callback used to return the result.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         */
        on(type: 'inputStop', callback: () => void): void;
        /**
         * Disables listening for the input method stop event. This API uses an asynchronous callback to return the result.
         *
         * @param { 'inputStop' } type - Event type, which is **'inputStop'**.
         * @param { function } callback - Callback to unregister. If this parameter is not specified, this API unregisters
         *     all callbacks for the specified type.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         */
        off(type: 'inputStop', callback: () => void): void;
        /**
         * Enables listening for the window invocation setting event. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { 'setCallingWindow' } type - Event type, which is **'setCallingWindow'**.
         * @param { function } callback - Callback used to return the window ID of the caller.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         */
        on(type: 'setCallingWindow', callback: (wid: number) => void): void;
        /**
         * Disables listening for the window invocation setting event. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { 'setCallingWindow' } type - Event type, which is **'setCallingWindow'**.
         * @param { function } callback - Callback to unregister. If this parameter is not specified, this API unregisters
         *     all callbacks for the specified type.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         */
        off(type: 'setCallingWindow', callback: (wid: number) => void): void;
        /**
         * Enables listening for a keyboard visibility event. This API uses an asynchronous callback to return the result.
         *
         * @param { 'keyboardShow' | 'keyboardHide' } type - Event type.
         *     <br>- The value **'keyboardShow'** indicates the keyboard display event.
         *     <br>- The value **'keyboardHide'** indicates the keyboard hiding event.
         * @param { function } callback - Callback used to return the result.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         */
        on(type: 'keyboardShow' | 'keyboardHide', callback: () => void): void;
        /**
         * Disables listening for a keyboard visibility event. This API uses an asynchronous callback to return the result.
         *
         * @param { 'keyboardShow' | 'keyboardHide' } type - Event type.
         *     <br>- The value **'keyboardShow'** indicates the keyboard display event.
         *     <br>- The value **'keyboardHide'** indicates the keyboard hiding event.
         * @param { function } [callback] - Callback used to return the result.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         */
        off(type: 'keyboardShow' | 'keyboardHide', callback?: () => void): void;
        /**
         * Enables listening for the input method subtype setting event. This API uses an asynchronous callback to return
         * the result.
         *
         * @param { 'setSubtype' } type - Event type, which is **'setSubtype'**.
         * @param { function } callback - Callback used to return the input method subtype.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         */
        on(type: 'setSubtype', callback: (inputMethodSubtype: InputMethodSubtype) => void): void;
        /**
         * Disables listening for the input method subtype setting event. This API uses an asynchronous callback to return
         * the result.
         *
         * @param { 'setSubtype' } type - Event type, which is **'setSubtype'**.
         * @param { function } [callback] - Callback to unregister. If this parameter is not specified, this API unregisters
         *     all callbacks for the specified type.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         */
        off(type: 'setSubtype', callback?: (inputMethodSubtype: InputMethodSubtype) => void): void;
        /**
         * Enables listening for the security mode changes of the input method. This API uses an asynchronous callback to
         * return the result.
         *
         * @param { 'securityModeChange' } type - Event type, which is **'securityModeChange'**.
         * @param { Callback<SecurityMode> } callback - Callback used to return the current security mode.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 11
         */
        on(type: 'securityModeChange', callback: Callback<SecurityMode>): void;
        /**
         * Disables listening for the security mode changes of the input method. This API uses an asynchronous callback to
         * return the result.
         *
         * @param { 'securityModeChange' } type - Event type, which is **'securityModeChange'**.
         * @param { Callback<SecurityMode> } [callback] - Callback to unregister. If this parameter is not specified, this
         *     API unregisters all callbacks for the specified type.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 11
         */
        off(type: 'securityModeChange', callback?: Callback<SecurityMode>): void;
        /**
         * Enables listening for the private data event of the input method. This API uses an asynchronous callback to
         * return the result.
         *
         * @param { 'privateCommand' } type - Event type, which is **'privateCommand'**.
         * @param { Callback<Record<string, CommandDataType>> } callback - Callback used to return the private data sent to
         *     the input method application.
         * @throws { BusinessError } 12800010 - not the preconfigured default input method.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 12
         */
        on(type: 'privateCommand', callback: Callback<Record<string, CommandDataType>>): void;
        /**
         * Disables listening for the private data event of the input method. This API uses an asynchronous callback to
         * return the result.
         *
         * @param { 'privateCommand' } type - Event type, which is **'privateCommand'**.
         * @param { Callback<Record<string, CommandDataType>> } [callback] - Callback to unregister. If this parameter is
         *     not specified, this API unregisters all callbacks for the specified type.
         * @throws { BusinessError } 12800010 - not the preconfigured default input method.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 12
         */
        off(type: 'privateCommand', callback?: Callback<Record<string, CommandDataType>>): void;
        /**
         * Enables listening for changes of the screen ID of the window associated with the edit box. This API uses an
         * asynchronous callback to return the result.
         *
         * @param { 'callingDisplayDidChange' } type - Event type, which is **'callingDisplayDidChange'**.
         * @param { Callback<number> } callback - Callback used to return the screen ID of the window corresponding to the
         *     edit box.
         * @throws { BusinessError } 801 - capability not supported.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 18
         */
        on(type: 'callingDisplayDidChange', callback: Callback<number>): void;
        /**
         * Disables listening for changes of the screen ID of the window associated with the edit box. This API uses an
         * asynchronous callback to return the result.
         *
         * @param { 'callingDisplayDidChange' } type - Event type, which is **'callingDisplayDidChange'**.
         * @param { Callback<number> } [callback] - Callback to unregister. If this parameter is not specified, this API
         *     unregisters all callbacks for the specified type.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 18
         */
        off(type: 'callingDisplayDidChange', callback?: Callback<number>): void;
        /**
         * Subscribes to the event of discarding candidate words and sends the event to the input method. This API uses an
         * asynchronous callback to return the result.
         *
         * @param { 'discardTypingText' } type - Event type, which is **'discardTypingText'**.
         *     <br> - **'discardTypingText'**
         *     : indicates subscribing to the event of discarding candidate words and sending the event to the input method.
         * @param { Callback<void> } callback - Callback used to return the result. If the operation is successful, **err**
         *     is **undefined**. Otherwise, **err** is an error object.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 20
         */
        on(type: 'discardTypingText', callback: Callback<void>): void;
        /**
         * Unsubscribes from the event of discarding candidate words and sends the event to the input method. This API uses
         * an asynchronous callback to return the result.
         *
         * @param { 'discardTypingText' } type - Event type, which is **'discardTypingText'**.
         *     <br> - **'discardTypingText'**: indicates unsubscribing from the event of discarding candidate words and
         *     sending the event to the input method.
         * @param { Callback<void> } [callback] - Callback to unregister. If this parameter is not specified, this API
         *     unregisters all callbacks for the specified type.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 20
         */
        off(type: 'discardTypingText', callback?: Callback<void>): void;
        /**
         * Obtains the current security mode of the input method.
         *
         * @returns { SecurityMode } Security mode.
         * @throws { BusinessError } 12800004 - not an input method application.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 11
         */
        getSecurityMode(): SecurityMode;
        /**
         * Creates an input method panel. This API can be called only by the input method application in the
         * [InputMethodExtensionAbility]{@link @ohos.InputMethodExtensionAbility:InputMethodExtensionAbility} class. This
         * API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > Only one [SOFT_KEYBOARD]{@link inputMethodEngine.PanelType} panel and one
         * > [STATUS_BAR]{@link inputMethodEngine.PanelType} panel can be created for a single input method.
         *
         * > The input method panel does not support subwindows. For example, subwindows cannot be created using APIs such
         * > as
         * > [window.createWindow]{@link window.createWindow}
         * > , [bindContextMenu]{@link CommonMethod<T>.bindContextMenu},
         * > and [CustomDialog]{@link ./@internal/component/ets/custom_dialog_controller}. You are advised to adopt
         * > alternative solutions to sub-windows, such as using a [dialog box]{@link @ohos.arkui.advanced.Dialog} or
         * > [bindMenu]{@link CommonMethod<T>.bindMenu}, or set
         * > **showInSubwindow** to **false**.
         *
         * @param { BaseContext } ctx - Current context of the input method.
         * @param { PanelInfo } info - Information about the input method panel.
         * @param { AsyncCallback<Panel> } callback - Callback used to return the result. If the operation is successful,
         *     the created input method panel is returned.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @throws { BusinessError } 12800004 - not an input method application.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        createPanel(ctx: BaseContext, info: PanelInfo, callback: AsyncCallback<Panel>): void;
        /**
         * Creates an input method panel. This API can be called only by the input method application in the
         * [InputMethodExtensionAbility]{@link @ohos.InputMethodExtensionAbility:InputMethodExtensionAbility} class. This
         * API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > Only one [SOFT_KEYBOARD]{@link inputMethodEngine.PanelType} panel and one
         * > [STATUS_BAR]{@link inputMethodEngine.PanelType} panel can be created for a single input method.
         *
         * > The input method panel does not support subwindows. For example, subwindows cannot be created using APIs such
         * > as
         * > [window.createWindow](docroot://windowmanager/application-window-fa.md#setting-the-child-window-of-an-application)
         * > , [bindContextMenu]{@link CommonMethod<T>.bindContextMenu},
         * > and [CustomDialog]{@link ./@internal/component/ets/custom_dialog_controller}. You are advised to adopt
         * > alternative solutions to sub-windows, such as using a [dialog box]{@link @ohos.arkui.advanced.Dialog} or
         * > [bindMenu]{@link CommonMethod<T>.bindMenu}, or set
         * > **showInSubwindow** to **false**.
         *
         * @param { BaseContext } ctx - Current context of the input method.
         * @param { PanelInfo } info - Information about the input method panel.
         * @returns { Promise<Panel> } the promise returned by the function.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @throws { BusinessError } 12800004 - not an input method application.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        createPanel(ctx: BaseContext, info: PanelInfo): Promise<Panel>;
        /**
         * Destroys the specified input method panel. This API uses an asynchronous callback to return the result.
         *
         * @param { Panel } panel - Input method panel to destroy.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        destroyPanel(panel: Panel, callback: AsyncCallback<void>): void;
        /**
         * Destroys the specified input method panel. This API uses a promise to return the result.
         *
         * @param { Panel } panel - Input method panel to destroy.
         * @returns { Promise<void> } the promise returned by the function.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        destroyPanel(panel: Panel): Promise<void>;
    }
    /**
     * In the following API examples, you must first use
     * [on('inputStart')]{@link inputMethodEngine.InputMethodEngine.on(type: 'inputStart',
     * callback: (kbController: KeyboardController, textInputClient: TextInputClient) => void): void;}
     * to obtain a **TextInputClient**
     * instance, and then call the APIs using the obtained instance.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 8
     * @deprecated since 9
     * @useinstead inputMethodEngine.InputClient
     */
    interface TextInputClient {
        /**
         * Sends the function key. This API uses an asynchronous callback to return the result.
         *
         * @param { number } action - Action of the function key.
         *     <br>- **0**: invalid key.
         *     <br>- **1**: confirm key (Enter key).
         * @param { AsyncCallback<boolean> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **data** is **true**. Otherwise, **err** is an error object.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 8
         * @deprecated since 9
         * @useinstead inputMethodEngine.InputClient.sendKeyFunction(action: int, callback: AsyncCallback<boolean>)
         */
        sendKeyFunction(action: number, callback: AsyncCallback<boolean>): void;
        /**
         * Sends the function key. This API uses a promise to return the result.
         *
         * @param { number } action - Action of the function key.
         *     <br>**0**: invalid key.
         *     <br>**1**: confirm key (Enter key).
         * @returns { Promise<boolean> } Promise used to return the result. The value **true** means that the setting is
         *     successful, and **false** means the opposite.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 8
         * @deprecated since 9
         * @useinstead inputMethodEngine.InputClient.sendKeyFunction(action: int): Promise<boolean>
         */
        sendKeyFunction(action: number): Promise<boolean>;
        /**
         * Deletes the fixed-length text before the cursor. This API uses an asynchronous callback to return the result.
         *
         * @param { number } length - Text length, which cannot be less than 0.
         * @param { AsyncCallback<boolean> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **data** is **true**. Otherwise, **err** is an error object.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 8
         * @deprecated since 9
         * @useinstead inputMethodEngine.InputClient.deleteForward(length: int, callback: AsyncCallback<boolean>)
         */
        deleteForward(length: number, callback: AsyncCallback<boolean>): void;
        /**
         * Deletes the fixed-length text before the cursor. This API uses a promise to return the result.
         *
         * @param { number } length - Text length, which cannot be less than 0.
         * @returns { Promise<boolean> } Promise used to return the result. The value **true** means that the deletion is
         *     successful, and **false** means the opposite.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 8
         * @deprecated since 9
         * @useinstead inputMethodEngine.InputClient.deleteForward(length: int): Promise<boolean>
         */
        deleteForward(length: number): Promise<boolean>;
        /**
         * Deletes the fixed-length text after the cursor. This API uses an asynchronous callback to return the result.
         *
         * @param { number } length - Text length, which cannot be less than 0.
         * @param { AsyncCallback<boolean> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **data** is **true**. Otherwise, **err** is an error object.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 8
         * @deprecated since 9
         * @useinstead inputMethodEngine.InputClient.deleteBackward(length: int, callback: AsyncCallback<boolean>)
         */
        deleteBackward(length: number, callback: AsyncCallback<boolean>): void;
        /**
         * Deletes the fixed-length text after the cursor. This API uses a promise to return the result.
         *
         * @param { number } length - Text length, which cannot be less than 0.
         * @returns { Promise<boolean> } Promise used to return the result. The value **true** means that the deletion is
         *     successful, and **false** means the opposite.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 8
         * @deprecated since 9
         * @useinstead inputMethodEngine.InputClient.deleteBackward(length: int): Promise<boolean>
         */
        deleteBackward(length: number): Promise<boolean>;
        /**
         * Inserts text. This API uses an asynchronous callback to return the result.
         *
         * @param { string } text - Text to insert.
         * @param { AsyncCallback<boolean> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **data** is **true**. Otherwise, **err** is an error object.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 8
         * @deprecated since 9
         * @useinstead inputMethodEngine.InputClient.insertText(text: string, callback: AsyncCallback<boolean>)
         */
        insertText(text: string, callback: AsyncCallback<boolean>): void;
        /**
         * Inserts text. This API uses a promise to return the result.
         *
         * @param { string } text - Text to insert.
         * @returns { Promise<boolean> } Promise used to return the result. The value **true** means that the insertion is
         *     successful, and **false** means the opposite.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 8
         * @deprecated since 9
         * @useinstead inputMethodEngine.InputClient.insertText(text: string): Promise<boolean>
         */
        insertText(text: string): Promise<boolean>;
        /**
         * Obtains the specific-length text before the cursor. This API uses an asynchronous callback to return the result.
         *
         * @param { number } length - Text length, which cannot be less than 0.
         * @param { AsyncCallback<string> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **data** is the obtained text. Otherwise, **err** is an error object.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 8
         * @deprecated since 9
         * @useinstead inputMethodEngine.InputClient.getForward(length: int, callback: AsyncCallback<string>)
         */
        getForward(length: number, callback: AsyncCallback<string>): void;
        /**
         * Obtains the specific-length text before the cursor. This API uses a promise to return the result.
         *
         * @param { number } length - Text length, which cannot be less than 0.
         * @returns { Promise<string> } Promise used to return the specific-length text before the cursor.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 8
         * @deprecated since 9
         * @useinstead inputMethodEngine.InputClient.getForward(length: int): Promise<string>
         */
        getForward(length: number): Promise<string>;
        /**
         * Obtains the specific-length text after the cursor. This API uses an asynchronous callback to return the result.
         *
         * @param { number } length - Text length, which cannot be less than 0.
         * @param { AsyncCallback<string> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **data** is the obtained text. Otherwise, **err** is an error object.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 8
         * @deprecated since 9
         * @useinstead inputMethodEngine.InputClient.getBackward(length: int, callback: AsyncCallback<string>)
         */
        getBackward(length: number, callback: AsyncCallback<string>): void;
        /**
         * Obtains the specific-length text after the cursor. This API uses a promise to return the result.
         *
         * @param { number } length - Text length, which cannot be less than 0.
         * @returns { Promise<string> } Promise used to return the specific-length text after the cursor.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 8
         * @deprecated since 9
         * @useinstead inputMethodEngine.InputClient.getBackward(length: int, callback: AsyncCallback<string>)
         */
        getBackward(length: number): Promise<string>;
        /**
         * Obtains the attribute of the edit box. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<EditorAttribute> } callback - Callback used to return the result. If the operation is
         *     successful, **err** is **undefined** and **data** is the attribute of the edit box. Otherwise, **err** is an
         *     error object.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 8
         * @deprecated since 9
         * @useinstead inputMethodEngine.InputClient.getEditorAttribute(callback: AsyncCallback<EditorAttribute>)
         */
        getEditorAttribute(callback: AsyncCallback<EditorAttribute>): void;
        /**
         * Obtains the attribute of the edit box. This API uses a promise to return the result.
         *
         * @returns { Promise<EditorAttribute> } Promise used to return the attribute of the edit box.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 8
         * @deprecated since 9
         * @useinstead inputMethodEngine.InputClient.getEditorAttribute(callback: AsyncCallback<EditorAttribute>)
         */
        getEditorAttribute(): Promise<EditorAttribute>;
    }
    /**
     * You must first use [on('inputStart')]{@link inputMethodEngine.InputMethodAbility. on(type: 'inputStart', callback:
     * (kbController: KeyboardController, inputClient: InputClient) => void): void;} to obtain a
     * **InputClient** instance, and then use this instance to call the following APIs.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 9
     */
    interface InputClient {
        /**
         * Sends the function key. This API uses an asynchronous callback to return the result.
         *
         * @param { number } action - Action of the function key.
         *     <br>- **0**: invalid key.
         *     <br>- **1**: confirm key (Enter key).
         * @param { AsyncCallback<boolean> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **data** is **true**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         */
        sendKeyFunction(action: number, callback: AsyncCallback<boolean>): void;
        /**
         * Sends the function key. This API uses a promise to return the result.
         *
         * @param { number } action - Action of the function key.
         *     <br>**0**: invalid key.
         *     <br>**1**: confirm key (Enter key).
         * @returns { Promise<boolean> } Promise used to return the result. The value **true** means that the operation is
         *     successful, and **false** means the opposite.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         */
        sendKeyFunction(action: number): Promise<boolean>;
        /**
         * Deletes the fixed-length text before the cursor. This API uses an asynchronous callback to return the result.
         *
         * @param { number } length - Text length, which cannot be less than 0.
         * @param { AsyncCallback<boolean> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **data** is **true**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @throws { BusinessError } 12800002 - input method engine error. Possible causes:
         *     1.input method panel not created. 2.the input method application does not subscribe to related events.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         */
        deleteForward(length: number, callback: AsyncCallback<boolean>): void;
        /**
         * Deletes the fixed-length text before the cursor. This API uses a promise to return the result.
         *
         * @param { number } length - Text length, which cannot be less than 0.
         * @returns { Promise<boolean> } Promise used to return the result. The value **true** means that the deletion is
         *     successful, and **false** means the opposite.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @throws { BusinessError } 12800002 - input method engine error. Possible causes:
         *     1.input method panel not created. 2.the input method application does not subscribe to related events.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         */
        deleteForward(length: number): Promise<boolean>;
        /**
         * Deletes the fixed-length text before the cursor.
         *
         * @param { number } length - Text length, which cannot be less than 0.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
         * @throws { BusinessError } 12800002 - input method engine error. Possible causes:
         *     1.input method panel not created. 2.the input method application does not subscribe to related events.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        deleteForwardSync(length: number): void;
        /**
         * Deletes the fixed-length text after the cursor. This API uses an asynchronous callback to return the result.
         *
         * @param { number } length - Text length, which cannot be less than 0.
         * @param { AsyncCallback<boolean> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **data** is **true**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @throws { BusinessError } 12800002 - input method engine error. Possible causes:
         *     1.input method panel not created. 2.the input method application does not subscribe to related events.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         */
        deleteBackward(length: number, callback: AsyncCallback<boolean>): void;
        /**
         * Deletes the fixed-length text after the cursor. This API uses a promise to return the result.
         *
         * @param { number } length - Text length, which cannot be less than 0.
         * @returns { Promise<boolean> } Promise used to return the result. The value **true** means that the deletion is
         *     successful, and **false** means the opposite.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @throws { BusinessError } 12800002 - input method engine error. Possible causes:
         *     1.input method panel not created. 2.the input method application does not subscribe to related events.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         */
        deleteBackward(length: number): Promise<boolean>;
        /**
         * Deletes the fixed-length text after the cursor.
         *
         * @param { number } length - Text length, which cannot be less than 0.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
         * @throws { BusinessError } 12800002 - input method engine error. Possible causes:
         *     1.input method panel not created. 2.the input method application does not subscribe to related events.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        deleteBackwardSync(length: number): void;
        /**
         * Inserts text. This API uses an asynchronous callback to return the result.
         *
         * @param { string } text - Text to insert.
         * @param { AsyncCallback<boolean> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **data** is **true**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @throws { BusinessError } 12800002 - input method engine error. Possible causes:
         *     1.input method panel not created. 2.the input method application does not subscribe to related events.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         */
        insertText(text: string, callback: AsyncCallback<boolean>): void;
        /**
         * Inserts text. This API uses a promise to return the result.
         *
         * @param { string } text - Text to insert.
         * @returns { Promise<boolean> } Promise used to return the result. The value **true** means that the insertion is
         *     successful, and **false** means the opposite.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @throws { BusinessError } 12800002 - input method engine error. Possible causes:
         *     1.input method panel not created. 2.the input method application does not subscribe to related events.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         */
        insertText(text: string): Promise<boolean>;
        /**
         * Inserts text.
         *
         * @param { string } text - Text to insert.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @throws { BusinessError } 12800002 - input method engine error. Possible causes:
         *     1.input method panel not created. 2.the input method application does not subscribe to related events.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        insertTextSync(text: string): void;
        /**
         * Obtains the specific-length text before the cursor. This API uses an asynchronous callback to return the result.
         *
         * @param { number } length - Text length, which cannot be less than 0.
         * @param { AsyncCallback<string> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **data** is the obtained text. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @throws { BusinessError } 12800006 - input method controller error. Possible cause:
         *     create InputMethodController object failed.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         */
        getForward(length: number, callback: AsyncCallback<string>): void;
        /**
         * Obtains the specific-length text before the cursor. This API uses a promise to return the result.
         *
         * @param { number } length - Text length, which cannot be less than 0.
         * @returns { Promise<string> } Promise used to return the specific-length text before the cursor.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @throws { BusinessError } 12800006 - input method controller error. Possible cause:
         *     create InputMethodController object failed.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         */
        getForward(length: number): Promise<string>;
        /**
         * Obtains the specific-length text before the cursor.
         *
         * @param { number } length - Text length, which cannot be less than 0.
         * @returns { string } Specific-length text before the cursor.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @throws { BusinessError } 12800006 - input method controller error. Possible cause:
         *     create InputMethodController object failed.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        getForwardSync(length: number): string;
        /**
         * Obtains the specific-length text after the cursor. This API uses an asynchronous callback to return the result.
         *
         * @param { number } length - Text length, which cannot be less than 0.
         * @param { AsyncCallback<string> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **data** is the obtained text. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @throws { BusinessError } 12800006 - input method controller error. Possible cause:
         *     create InputMethodController object failed.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         */
        getBackward(length: number, callback: AsyncCallback<string>): void;
        /**
         * Obtains the specific-length text after the cursor. This API uses a promise to return the result.
         *
         * @param { number } length - Text length, which cannot be less than 0.
         * @returns { Promise<string> } Promise used to return the specific-length text after the cursor.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @throws { BusinessError } 12800006 - input method controller error. Possible cause:
         *     create InputMethodController object failed.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         */
        getBackward(length: number): Promise<string>;
        /**
         * Obtains the specific-length text after the cursor.
         *
         * @param { number } length - Text length, which cannot be less than 0.
         * @returns { string } Specific-length text after the cursor.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @throws { BusinessError } 12800006 - input method controller error. Possible cause:
         *     create InputMethodController object failed.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        getBackwardSync(length: number): string;
        /**
         * Obtains the attribute of the edit box. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<EditorAttribute> } callback - Callback used to return the result. If the operation is
         *     successful, **err** is **undefined** and **data** is the attribute of the edit box. Otherwise, **err** is an
         *     error object.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         */
        getEditorAttribute(callback: AsyncCallback<EditorAttribute>): void;
        /**
         * Obtains the attribute of the edit box. This API uses a promise to return the result.
         *
         * @returns { Promise<EditorAttribute> } Promise used to return the attribute of the edit box.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         */
        getEditorAttribute(): Promise<EditorAttribute>;
        /**
         * Obtains the attribute of the edit box.
         *
         * @returns { EditorAttribute } Attribute information.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        getEditorAttributeSync(): EditorAttribute;
        /**
         * Moves the cursor. This API uses an asynchronous callback to return the result.
         *
         * @param { number } direction - Direction in which the cursor moves.
         *     <br>- **1**: upward.
         *     <br>- **2**: downward.
         *     <br>- **3**: leftward.
         *     <br>- **4**: rightward. which cannot be less than 0.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         */
        moveCursor(direction: number, callback: AsyncCallback<void>): void;
        /**
         * Moves the cursor. This API uses a promise to return the result.
         *
         * @param { number } direction - Direction in which the cursor moves.
         *     <br>- **1**: upward.
         *     <br>- **2**: downward.
         *     <br>- **3**: leftward.
         *     <br>- **4**: rightward. which cannot be less than 0.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         */
        moveCursor(direction: number): Promise<void>;
        /**
         * Moves the cursor.
         *
         * @param { number } direction - Direction in which the cursor moves.
         *     <br>- **1**: upward.
         *     <br>- **2**: downward.
         *     <br>- **3**: leftward.
         *     <br>- **4**: rightward. which cannot be less than 0.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        moveCursorSync(direction: number): void;
        /**
         * Selects text based on the specified range. This API uses an asynchronous callback to return the result.
         *
         * @param { Range } range - Range of the selected text.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the selection event is sent,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        selectByRange(range: Range, callback: AsyncCallback<void>): void;
        /**
         * Selects text based on the specified range. This API uses a promise to return the result.
         *
         * @param { Range } range - Range of the selected text.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        selectByRange(range: Range): Promise<void>;
        /**
         * Selects text based on the specified range.
         *
         * @param { Range } range - Range of the selected text.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        selectByRangeSync(range: Range): void;
        /**
         * Selects text based on the cursor movement direction. This API uses an asynchronous callback to return the result.
         *
         * @param { Movement } movement - Direction in which the cursor moves when the text is selected.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the selection event is sent,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        selectByMovement(movement: Movement, callback: AsyncCallback<void>): void;
        /**
         * Selects text based on the cursor movement direction. This API uses a promise to return the result.
         *
         * @param { Movement } movement - Direction in which the cursor moves when the text is selected.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        selectByMovement(movement: Movement): Promise<void>;
        /**
         * Selects text based on the cursor movement direction.
         *
         * @param { Movement } movement - Direction in which the cursor moves when the text is selected.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        selectByMovementSync(movement: Movement): void;
        /**
         * Obtains the index of the text where the cursor is located. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { AsyncCallback<number> } callback - Callback used to return the result. If the text index is obtained,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @throws { BusinessError } 12800006 - input method controller error. Possible cause:
         *     create InputMethodController object failed.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        getTextIndexAtCursor(callback: AsyncCallback<number>): void;
        /**
         * Obtains the index of the text where the cursor is located. This API uses a promise to return the result.
         *
         * @returns { Promise<number> } Promise used to return the result.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @throws { BusinessError } 12800006 - input method controller error. Possible cause:
         *     create InputMethodController object failed.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        getTextIndexAtCursor(): Promise<number>;
        /**
         * Obtains the index of the text where the cursor is located.
         *
         * @returns { number } Index of the text where the cursor is located.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @throws { BusinessError } 12800006 - input method controller error. Possible cause:
         *     create InputMethodController object failed.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        getTextIndexAtCursorSync(): number;
        /**
         * Sends an extended edit action. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > The input method applications call this API to send extended edit actions to the edit box. The edit box listens
         * > for the corresponding event using
         * > [on('handleExtendAction')]{@link @ohos.inputMethod:inputMethod.InputMethodController.on(type: 'handleExtendAction',
         *  callback: (action: ExtendAction) => void): void} for further processing.
         * >
         * > When the edit box responds to the **PASTE** command of [ExtendAction]{@link inputMethodEngine.ExtendAction},
         * > the edit box application needs to apply for the
         * > [ohos.permission.READ_PASTEBOARD](docroot://security/AccessToken/restricted-permissions.md#ohospermissionread_pasteboard)
         * > permission.
         *
         * @param { ExtendAction } action - Extended edit action to send.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @throws { BusinessError } 12800006 - input method controller error. Possible cause:
         *     create InputMethodController object failed.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        sendExtendAction(action: ExtendAction, callback: AsyncCallback<void>): void;
        /**
         * Sends an extended edit action. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > The input method applications call this API to send extended edit actions to the edit box. The edit box listens
         * > for the corresponding event using
         * > [on('handleExtendAction')]{@link @ohos.inputMethod:inputMethod.InputMethodController.on(type: 'handleExtendAction',
         *  callback: (action: ExtendAction) => void): void;} for
         * > further processing.
         * >
         * > When the edit box responds to the **PASTE** command of [ExtendAction]{@link inputMethodEngine.ExtendAction},
         * > the edit box application needs to apply for the
         * > [ohos.permission.READ_PASTEBOARD](docroot://security/AccessToken/restricted-permissions.md#ohospermissionread_pasteboard)
         * > permission.
         *
         * @param { ExtendAction } action - Extended edit action to send.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @throws { BusinessError } 12800006 - input method controller error. Possible cause:
         *     create InputMethodController object failed.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        sendExtendAction(action: ExtendAction): Promise<void>;
        /**
         * Sends private data to the system component that needs to communicate with the input method application. This API
         * uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > - The private data channel allows communication between the system preset input method application and specific
         * > system components (such as a text box or a home screen application). It is usually used to implement custom
         * > input on a specific device.
         * >
         * > - The total size of the private data is 32 KB, and the maximum number of private data records is 5.
         *
         * @param { Record<string, CommandDataType> } commandData - Private data to send.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @throws { BusinessError } 12800010 - not the preconfigured default input method.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 12
         */
        sendPrivateCommand(commandData: Record<string, CommandDataType>): Promise<void>;
        /**
         * Obtains information about the application window, in which the input box that starts an input method is located.
         * This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API applies only to the input method applications that use [Panel]{@link inputMethodEngine.Panel} as the
         * > soft keyboard window.
         *
         * @returns { Promise<WindowInfo> } Promise used to return the information obtained.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @throws { BusinessError } 12800012 - the input method panel does not exist.
         * @throws { BusinessError } 12800013 - window manager service error.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 12
         */
        getCallingWindowInfo(): Promise<WindowInfo>;
        /**
         * Sets the preview text. This API uses a promise to return the result.
         *
         * @param { string } text - Preview text to set.
         * @param { Range } range - Range of the preview text.
         *     <br>- If the value is { start: -1, end: -1 }, **text**
         *     replaces the entire text in the current preview area by default.
         *     <br>- If **start** is equal to **end**,
         *     **text** is inserted into the cursor position specified by **start**.
         *     <br>- If **start** is not equal to **end**, **text** replaces the text of the specified range.
         *     <br>- If the values of **start** and **end** are negative values, a parameter error is returned.
         *     <br>- If there is preview text in the text box, the value of
         *     **range** cannot exceed the range of the preview text. Otherwise, a parameter error is returned.
         *     <br>- If there is no preview text in the text box, the value of **range** cannot exceed the text range of
         *     the text box. Otherwise, a parameter error is returned.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @throws { BusinessError } 12800011 - text preview not supported.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 12
         */
        setPreviewText(text: string, range: Range): Promise<void>;
        /**
         * Sets the preview text.
         *
         * @param { string } text - Preview text to set.
         * @param { Range } range - Range of the preview text.
         *     <br>- If the value is { start: -1, end: -1 }, **text**
         *     replaces the entire text in the current preview area by default.
         *     <br>- If **start** is equal to **end**,
         *     **text** is inserted into the cursor position specified by **start**.
         *     <br>- If **start** is not equal to
         *     **end**, **text** replaces the text of the specified range.
         *     <br>- If the values of **start** and **end** are negative values, a parameter error is returned.
         *     <br>- If there is preview text in the text box, the value of
         *     **range** cannot exceed the range of the preview text. Otherwise, a parameter error is returned.
         *     <br>- If there is no preview text in the text box, the value of **range** cannot exceed the text range of
         *     the text box. Otherwise, a parameter error is returned.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @throws { BusinessError } 12800011 - text preview not supported.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 12
         */
        setPreviewTextSync(text: string, range: Range): void;
        /**
         * Finishes the text preview. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > If there is preview text in the current text box, calling this API will display the preview text on the screen.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @throws { BusinessError } 12800011 - text preview not supported.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 12
         */
        finishTextPreview(): Promise<void>;
        /**
         * Finishes the text preview.
         *
         * > **NOTE**
         * >
         * > If there is preview text in the current text box, calling this API will display the preview text on the screen.
         *
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @throws { BusinessError } 12800011 - text preview not supported.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 12
         */
        finishTextPreviewSync(): void;
        /**
         * Sends the custom communication to the edit box application attached to the input method application. This API
         * uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API can be called only when the edit box is attached to the input method and enter the edit mode, and the
         * > input method application is in full experience mode.
         * >
         * > The maximum length of **msgId** is 256 B, and the maximum length of **msgParam** is 128 KB.
         *
         * @param { string } msgId - Identifier of the custom data to be sent to the edit box application attached to the
         *     input method application.
         * @param { ?ArrayBuffer } [msgParam] - Message body of the custom data to be sent to the edit box application
         *     attached to the input method application.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1. Incorrect parameter types. 2. Incorrect parameter length.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @throws { BusinessError } 12800009 - input method client detached.
         * @throws { BusinessError } 12800014 - the input method is in basic mode.
         * @throws { BusinessError } 12800015 - the other side does not accept the request.
         * @throws { BusinessError } 12800016 - input method client is not editable.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 15
         */
        sendMessage(msgId: string, msgParam?: ArrayBuffer): Promise<void>;
        /**
         * Registers or unregisters MessageHandler.
         *
         * > **NOTE**
         * >
         * > The [MessageHandler]{@link inputMethodEngine.MessageHandler} object is globally unique. After multiple
         * > registrations, only the last registered object is valid and retained, and the
         * > [onTerminated]{@link inputMethodEngine.MessageHandler.onTerminated()} callback of the penultimate registered
         * > object is triggered.
         * >
         * > If no parameter is set, unregister [MessageHandler]{@link inputMethodEngine.MessageHandler}. Its
         * > [onTerminated]{@link inputMethodEngine.MessageHandler.onTerminated()} callback will be triggered.
         *
         * @param { ?MessageHandler } [msgHandler] - This object receives custom communication data from the edit box
         *     application attached to the input method application through
         *     [onMessage]{@link inputMethodEngine.MessageHandler.onMessage(msgId: string, msgParam?: ArrayBuffer)} and
         *     receives a message for terminating the subscription to this object through
         *     [onTerminated]{@link inputMethodEngine.MessageHandler.onTerminated()}.
         *     <br>If no parameter is set, unregister
         *     [MessageHandler]{@link inputMethodEngine.MessageHandler}. Its
         *     [onTerminated]{@link inputMethodEngine.MessageHandler.onTerminated()} callback will be triggered.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Incorrect parameter types.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 15
         */
        recvMessage(msgHandler?: MessageHandler): void;
        /**
         * Obtains the additional options for binding an input method.
         *
         * @returns { AttachOptions } Additional options for binding an input method.
         * @throws { BusinessError } 801 - Capability not supported. [since 19 - 19]
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 19
         */
        getAttachOptions(): AttachOptions;
        /**
         * Subscribes to the event indicating that the additional options for binding an input method are changed. This API
         * uses an asynchronous callback to return the result.
         *
         * @param { 'attachOptionsDidChange' } type - Additional option change event when the input method is bound. The
         *     value is fixed to **'attachOptionsDidChange'**.
         * @param { Callback<AttachOptions> } callback - Callback used to return the additional options for binding an input
         *     method.
         * @throws { BusinessError } 801 - Capability not supported. [since 19 - 19]
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 19
         */
        on(type: 'attachOptionsDidChange', callback: Callback<AttachOptions>): void;
        /**
         * Unsubscribes from the event indicating that additional options for binding an input method are changed. This API
         * uses an asynchronous callback to return the result.
         *
         * @param { 'attachOptionsDidChange' } type - Additional option change event when the input method is bound. The
         *     value is fixed to **'attachOptionsDidChange'**.
         * @param { Callback<AttachOptions> } [callback] - Callback to unregister. If this parameter is not specified, this
         *     API unregisters all callbacks for the specified type by default.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 19
         */
        off(type: 'attachOptionsDidChange', callback?: Callback<AttachOptions>): void;
    }
    /**
     * In the following API examples, you must first use
     * [getKeyboardDelegate]{@link inputMethodEngine.getKeyboardDelegate()} to obtain a **KeyboardDelegate** instance, and
     * then call the APIs using the obtained instance.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 8
     */
    interface KeyboardDelegate {
        /**
         * Enables listening for a physical keyboard event. This API uses an asynchronous callback to return the result.
         *
         * @param { 'keyDown' | 'keyUp' } type - Event type.
         *     <br>- The value **'keyDown'** indicates the keydown event.
         *     <br>- The value **'keyUp'** indicates the keyup event.
         * @param { function } callback - Callback used to return the key information. If the event is consumed by the event
         *     subscriber, **true** is returned. Otherwise, **false** is returned.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 8
         */
        on(type: 'keyDown' | 'keyUp', callback: (event: KeyEvent) => boolean): void;
        /**
         * Disables listening for a physical keyboard event. This API uses an asynchronous callback to return the result.
         *
         * @param { 'keyDown' | 'keyUp' } type - Event type.
         *     <br>- The value **'keyDown'** indicates the keydown event.
         *     <br>- The value **'keyUp'** indicates the keyup event.
         * @param { function } [callback] - Callback to unregister. If this parameter is not specified, this API unregisters
         *     all callbacks for the specified type.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 8
         */
        off(type: 'keyDown' | 'keyUp', callback?: (event: KeyEvent) => boolean): void;
        /**
         * Enables listening for a keyboard event. This API uses an asynchronous callback to return the result.
         *
         * @param { 'keyEvent' } type - Event type, which is **'keyEvent'**.
         * @param { function } callback - Callback used to return the result. The input parameter is the key event
         *     information and the return value is of the Boolean type.
         *     <br>- Input parameter: [InputKeyEvent]{@link @ohos.multimodalInput.keyEvent:KeyEvent}.
         *     <br>- If the event is consumed by the event
         *     subscriber, **true** is returned. Otherwise, **false** is returned.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        on(type: 'keyEvent', callback: (event: InputKeyEvent) => boolean): void;
        /**
         * Disables listening for a keyboard event. This API uses an asynchronous callback to return the result.
         *
         * @param { 'keyEvent' } type - Event type, which is **'keyEvent'**.
         * @param { function } [callback] - Callback to unregister. If this parameter is not specified, this API unregisters
         *     all callbacks for the specified type.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        off(type: 'keyEvent', callback?: (event: InputKeyEvent) => boolean): void;
        /**
         * Enables listening for the cursor change event. This API uses an asynchronous callback to return the result.
         *
         * @param { 'cursorContextChange' } type - Event type, which is **'cursorContextChange'**.
         * @param { function } callback - Callback used to return the cursor information.
         *     <br>- **x**: x coordinate of the top of the cursor.
         *     <br>- **y**: y coordinate of the bottom of the cursor.
         *     <br>- **height**: height of the cursor.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 8
         */
        on(type: 'cursorContextChange', callback: (x: number, y: number, height: number) => void): void;
        /**
         * Disables listening for cursor context changes. This API uses an asynchronous callback to return the result.
         *
         * @param { 'cursorContextChange' } type - Event type, which is **'cursorContextChange'**.
         * @param { function } [callback] - Callback to unregister. If this parameter is not specified, this API unregisters
         *     all callbacks for the specified type.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 8
         */
        off(type: 'cursorContextChange', callback?: (x: number, y: number, height: number) => void): void;
        /**
         * Enables listening for the text selection change event. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { 'selectionChange' } type - Event type, which is **'selectionChange'**.
         * @param { function } callback - Callback used to return the text selection information.
         *     <br>- **oldBegin**: start of the selected text before the change.
         *     <br>- **oldEnd**: end of the selected text before the change.
         *     <br>- **newBegin**: start of the selected text after the change.
         *     <br>- **newEnd**: end of the selected text after the change.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 8
         */
        on(type: 'selectionChange', callback: (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => void): void;
        /**
         * Disables listening for the text selection change event. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { 'selectionChange' } type - Event type, which is **'selectionChange'**.
         * @param { function } [callback] - Callback to unregister. If this parameter is not specified, this API unregisters
         *     all callbacks for the specified type.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 8
         */
        off(type: 'selectionChange', callback?: (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => void): void;
        /**
         * Enables listening for the text change event. This API uses an asynchronous callback to return the result.
         *
         * @param { 'textChange' } type - Event type, which is **'textChange'**.
         * @param { function } callback - Callback used to return the text content.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 8
         */
        on(type: 'textChange', callback: (text: string) => void): void;
        /**
         * Disables listening for the text change event. This API uses an asynchronous callback to return the result.
         *
         * @param { 'textChange' } type - Event type, which is **'textChange'**.
         * @param { function } [callback] - Callback to unregister. If this parameter is not specified, this API unregisters
         *     all callbacks for the specified type.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 8
         */
        off(type: 'textChange', callback?: (text: string) => void): void;
        /**
         * Enables listening for the edit box attribute change event. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { 'editorAttributeChanged' } type - Event type, which is **'editorAttributeChanged'**.
         * @param { function } callback - Callback used to return the changed edit box attribute.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        on(type: 'editorAttributeChanged', callback: (attr: EditorAttribute) => void): void;
        /**
         * Disables listening for the edit box attribute change event. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { 'editorAttributeChanged' } type - Event type, which is **'editorAttributeChanged'**.
         * @param { function } [callback] - Callback used for unsubscription. If this parameter is not specified, this API
         *     unregisters all callbacks for the specified type by default.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        off(type: 'editorAttributeChanged', callback?: (attr: EditorAttribute) => void): void;
    }
    /**
     * Enumerates the immersive modes of the input method.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 15
     */
    export enum ImmersiveMode {
        /**
         * Default immersive mode, the panel is not in immersive mode.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 15
         */
        NONE_IMMERSIVE = 0,
        /**
         * Immersive mode of the input method.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 15
         */
        IMMERSIVE,
        /**
         * Light immersive mode.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 15
         */
        LIGHT_IMMERSIVE,
        /**
         * Dark immersive mode.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 15
         */
        DARK_IMMERSIVE
    }
    /**
     * Enumerates the gradient modes of the input method.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 20
     */
    export enum GradientMode {
        /**
         * Disable gradient mode.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 20
         */
        NONE = 0,
        /**
         * Linear gradient mode.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 20
         */
        LINEAR_GRADIENT = 1
    }
    /**
     * Describes the immersive effect.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 20
     */
    interface ImmersiveEffect {
        /**
         * Gradient height, which cannot exceed 15% of the screen height.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 20
         */
        gradientHeight: number;
        /**
         * Gradient mode. If this attribute is not specified or is set to an invalid value, the gradient mode is not used by
         * default.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 20
         */
        gradientMode: GradientMode;
    }
    /**
     * Enumerates the reasons for requesting keyboard input.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 19
     */
    export enum RequestKeyboardReason {
        /**
         * The request keyboard reason is NONE.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 19
         */
        NONE = 0,
        /**
         * The request keyboard reason is MOUSE.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 19
         */
        MOUSE = 1,
        /**
         * The request keyboard reason is TOUCH.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 19
         */
        TOUCH = 2,
        /**
         * The request keyboard reason is OTHER.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 19
         */
        OTHER = 20
    }
    /**
     * In the following API examples, you must first use
     * [createPanel]{@link inputMethodEngine.InputMethodAbility.createPanel(ctx: BaseContext, info: PanelInfo, callback: AsyncCallback<Panel>)}
     * to obtain a **Panel** instance, and then call the APIs using the obtained instance.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 10
     */
    interface Panel {
        /**
         * Loads content from a page to this input method panel. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { string } path - Path of the page from which the content will be loaded.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        setUiContent(path: string, callback: AsyncCallback<void>): void;
        /**
         * Loads content from a page to this input method panel. This API uses a promise to return the result.
         *
         * @param { string } path - Path of the page from which the content will be loaded.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        setUiContent(path: string): Promise<void>;
        /**
         * Loads content from a page linked to LocalStorage to this input method panel. This API uses an asynchronous
         * callback to return the result.
         *
         * @param { string } path - Path of the page linked to LocalStorage.
         * @param { LocalStorage } storage - Storage unit that provides storage for mutable and immutable state variables in
         *     the application.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        setUiContent(path: string, storage: LocalStorage, callback: AsyncCallback<void>): void;
        /**
         * Loads content from a page linked to LocalStorage to this panel. This API uses a promise to return the result.
         *
         * @param { string } path - Path of the page from which the content will be loaded.
         * @param { LocalStorage } storage - Storage unit that provides storage for mutable and immutable state variables in
         *     the application.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        setUiContent(path: string, storage: LocalStorage): Promise<void>;
        /**
         * Resizes this input method panel. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > The panel width cannot exceed the screen width, and the panel height cannot be 0.7 times higher than the screen
         * > height.
         * >
         * > When the **PanelFlag** of a smartphone is **FLG_FLOATING** and the panel width is between 0 and 288 vp, the
         * > function buttons at the bottom of the panel will dynamically adjust their size according to the panel width. To
         * > ensure the optimal user experience, it is recommended that the panel width be no less than 90 vp.
         *
         * @param { number } width - Target width of the panel, in px. The value is an integer greater than or equal to 0, and
         *     cannot be greater than the screen width.
         * @param { number } height - Target height of the panel, in px. The value is an integer greater than or equal to 0,
         *     and cannot be greater than 0.7 times the screen height.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        resize(width: number, height: number, callback: AsyncCallback<void>): void;
        /**
         * Resizes this input method panel. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > The panel width cannot exceed the screen width, and the panel height cannot be 0.7 times higher than the screen
         * > height.
         * >
         * > When the **PanelFlag** of a smartphone is **FLG_FLOATING** and the panel width is between 0 and 288 vp, the
         * > function buttons at the bottom of the panel will dynamically adjust their size according to the panel width. To
         * > ensure the optimal user experience, it is recommended that the panel width be no less than 90 vp.
         *
         * @param { number } width - Target width of the panel, in px. The value is an integer greater than or equal to 0, and
         *     cannot be greater than the screen width.
         * @param { number } height - Target height of the panel, in px. The value is an integer greater than or equal to 0,
         *     and cannot be greater than 0.7 times the screen height.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        resize(width: number, height: number): Promise<void>;
        /**
         * Moves this input method panel to the specified position. This API uses an asynchronous callback to return the
         * result. This API does not work on panels in the [FLG_FIXED]{@link inputMethodEngine.PanelFlag} state.
         *
         * @param { number } x - Distance to move along the horizontal axis, in px. A positive value indicates moving
         *     rightwards. The value must be an integer.
         * @param { number } y - Distance to move along the vertical axis, in px. A positive value indicates moving downwards.
         *     The value must be an integer.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        moveTo(x: number, y: number, callback: AsyncCallback<void>): void;
        /**
         * Moves this input method panel to the specified position. This API uses a promise to return the result. This API
         * does not work on panels in the [FLG_FIXED]{@link inputMethodEngine.PanelFlag} state.
         *
         * @param { number } x - Distance to move along the horizontal axis, in px. A positive value indicates moving
         *     rightwards. The value must be an integer.
         * @param { number } y - Distance to move along the vertical axis, in px. A positive value indicates moving downwards.
         *     The value must be an integer.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        moveTo(x: number, y: number): Promise<void>;
        /**
         * Sends a command to start moving the window. The window can be moved only when the mouse is clicked.
         *
         * @throws { BusinessError } 12800002 - input method engine error. Possible causes:
         *     1.input method panel not created. 2.the input method application does not subscribe to related events.
         * @throws { BusinessError } 12800013 - window manager service error.
         * @throws { BusinessError } 12800017 - invalid panel type or panel flag.
         * @throws { BusinessError } 801 - capability not supported. [since 18]
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 15
         */
        startMoving(): void;
        /**
         * Obtains the window ID. This API uses a promise to return the result.
         *
         * @returns { Promise<number> } Promise used to return the result. It returns **displayId** of the window.
         * @throws { BusinessError } 12800002 - input method engine error. Possible causes:
         *     1.input method panel not created. 2.the input method application does not subscribe to related events.
         * @throws { BusinessError } 12800013 - window manager service error.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 15
         */
        getDisplayId(): Promise<number>;
        /**
         * Shows this input method panel. This API uses an asynchronous callback to return the result. It can be called when
         * the input method is bound to the edit box.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**. Otherwise, **err** is an error object.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        show(callback: AsyncCallback<void>): void;
        /**
         * Shows this input method panel. This API uses a promise to return the result. It can be called when the input
         * method is bound to the edit box.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        show(): Promise<void>;
        /**
         * Hides this panel. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**. Otherwise, **err** is an error object.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        hide(callback: AsyncCallback<void>): void;
        /**
         * Hides this panel. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        hide(): Promise<void>;
        /**
         * Enables listening for the show event of this panel. This API uses an asynchronous callback to return the result.
         *
         * @param { 'show' } type - Event type, which is **'show'**.
         * @param { function } callback - Callback used to return the result.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        on(type: 'show', callback: () => void): void;
        /**
         * Disables listening for the show event of this panel. This API uses an asynchronous callback to return the result.
         *
         * @param { 'show' } type - Event type, which is **'show'**.
         * @param { function } [callback] - Callback to unregister. If this parameter is not specified, this API unregisters
         *     all callbacks for the specified type.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        off(type: 'show', callback?: () => void): void;
        /**
         * Enables listening for the hide event of this panel. This API uses an asynchronous callback to return the result.
         *
         * @param { 'hide' } type - Event type, which is **'hide'**.
         * @param { function } callback - Callback used to return the result.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        on(type: 'hide', callback: () => void): void;
        /**
         * Disables listening for the hide event of this panel. This API uses an asynchronous callback to return the result.
         *
         * @param { 'hide' } type - Event type, which is **'hide'**.
         * @param { function } [callback] - Callback to unregister. If this parameter is not specified, this API unregisters
         *     all callbacks for the specified type.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        off(type: 'hide', callback?: () => void): void;
        /**
         * Changes the state type ([PanelFlag]{@link inputMethodEngine.PanelFlag}) of this input method panel. This API only
         * works for [SOFT_KEYBOARD]{@link inputMethodEngine.PanelType} panels.
         *
         * @param { PanelFlag } flag - Type of the state of the target panel.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        changeFlag(flag: PanelFlag): void;
        /**
         * Sets the input method panel to privacy mode. In privacy mode, screenshot and screen recording are blocked.
         *
         * @permission ohos.permission.PRIVACY_WINDOW
         * @param { boolean } isPrivacyMode - Whether to set the input method panel to privacy mode.
         *     <br>- **true**: privacy mode.
         *     <br>- **false**: non-privacy mode.
         * @throws { BusinessError } 201 - permissions check fails.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 11
         */
        setPrivacyMode(isPrivacyMode: boolean): void;
        /**
         * Adjusts the panel rectangle. After the API is called, the adjust request is submitted to the input method
         * framework, but the execution is not complete.
         *
         * > **NOTE**
         * >
         * > This API applies only to the panels of the **SOFT_KEYBOARD** type in the **FLG_FIXED** or **FLG_FLOATING**
         * > state.
         * >
         * > This API returns the result synchronously. The return only indicates that the system receives the setting
         * > request, not that the setting is complete.
         * >
         * > When the **PanelFlag** of a smartphone is **FLG_FLOATING** and the panel width is between 0 and 288 vp, the
         * > function buttons at the bottom of the panel will dynamically adjust their size according to the panel width. To
         * > ensure the optimal user experience, it is recommended that the panel width be no less than 90 vp.
         *
         * @param { PanelFlag } flag - Type of the state of the target panel. It can be **FLG_FIXED** or **FLG_FLOATING**.
         * @param { PanelRect } rect - Landscape rectangle and portrait rectangle of the target panel. For the panel of the
         *     fixed state, the height cannot exceed 70% of the screen height, and the width cannot exceed the screen width.
         *     For the panel of the floating state, the height cannot exceed the screen height, and the width cannot exceed
         *     the screen width.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
         * @throws { BusinessError } 12800013 - window manager service error.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 12
         */
        adjustPanelRect(flag: PanelFlag, rect: PanelRect): void;
        /**
         * Adjusts the panel rectangle, and customizes the avoid area and touch area.
         *
         * > **NOTE**
         * >
         * > This API applies only to the panels of the **SOFT_KEYBOARD** type in the **FLG_FIXED** or **FLG_FLOATING**
         * > state. This API is compatible with
         * > [adjustPanelRect]{@link inputMethodEngine.Panel.adjustPanelRect(flag: PanelFlag, rect: PanelRect)}. If the
         * > input parameter **rect** contains only the **landscapeRect** and **portraitRect** attributes,
         * > [adjustPanelRect]{@link inputMethodEngine.Panel.adjustPanelRect(flag: PanelFlag, rect: PanelRect)} is called by
         * > default.
         * >
         * > This API returns the result synchronously. The return only indicates that the system receives the setting
         * > request, not that the setting is complete.
         * >
         * > When the **PanelFlag** of a smartphone is **FLG_FLOATING** and the panel width is between 0 and 288 vp, the
         * > function buttons at the bottom of the panel will dynamically adjust their size according to the panel width. To
         * > ensure the optimal user experience, it is recommended that the panel width be no less than 90 vp.
         *
         * @param { PanelFlag } flag - Type of the state of the target panel. It can be **FLG_FIXED** or **FLG_FLOATING**.
         * @param { EnhancedPanelRect } rect - The target panel rectangle, avoid area, and touch area.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
         * @throws { BusinessError } 12800013 - window manager service error.
         * @throws { BusinessError } 12800017 - invalid panel type or panel flag.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 15
         */
        adjustPanelRect(flag: PanelFlag, rect: EnhancedPanelRect): void;
        /**
         * Update the panel rectangle. This API uses a promise to return the result.
         * > **NOTE**
         * >
         * > This API applies only to the panels of the **SOFT_KEYBOARD** type in the **FLG_FIXED** or **FLG_FLOATING**
         * > state.
         * >
         * > When the **PanelFlag** of a smartphone is **FLG_FLOATING** and the panel width is between 0 and 288 vp, the
         * > function buttons at the bottom of the panel will dynamically update their size according to the panel width. To
         * > ensure the optimal user experience, it is recommended that the panel width be no less than 90 vp.
         *
         * @param { PanelFlag } flag - Type of the state of the target panel. It can be **FLG_FIXED** or **FLG_FLOATING**.
         * @param { PanelRect } rect - Landscape rectangle and portrait rectangle of the target panel. For the panel of the
         * fixed state, the height cannot exceed 70% of the screen height, and the width cannot exceed the screen width.
         * For the panel of the floating state, the height cannot exceed the screen height, and the width cannot exceed
         * the screen width.
         * @returns { Promise<void>> } Promise that returns no value.
         * @throws { BusinessError } 12800013 - window manager service error.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @stagemodelonly
         * @since 26.0.0
         */
        updatePanelRect(flag: PanelFlag, rect: PanelRect): Promise<void>;
        /**
         * Update the panel rectangle, and customizes the avoid area and touch area. This API
         * uses a promise to return the result.
         * > **NOTE**
         * >
         * > This API applies only to the panels of the **SOFT_KEYBOARD** type in the **FLG_FIXED** or **FLG_FLOATING**
         * > state. This API is compatible with
         * > [updatePanelRect]{@link inputMethodEngine.Panel.updatePanelRect(flag: PanelFlag, rect: PanelRect)}.
         * > If the input parameter **rect** contains only the **landscapeRect** and **portraitRect** attributes,
         * > [updatePanelRect]{@link inputMethodEngine.Panel.updatePanelRect(flag: PanelFlag, rect: PanelRect)}
         * > is called by default.
         * >
         * > When the **PanelFlag** of a smartphone is **FLG_FLOATING** and the panel width is between 0 and 288 vp, the
         * > function buttons at the bottom of the panel will dynamically update their size according to the panel width. To
         * > ensure the optimal user experience, it is recommended that the panel width be no less than 90 vp.
         *
         * @param { PanelFlag } flag - Type of the state of the target panel. It can be **FLG_FIXED** or **FLG_FLOATING**.
         * @param { EnhancedPanelRect } rect - The target panel rectangle, avoid area, and touch area.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 12800013 - window manager service error.
         * @throws { BusinessError } 12800017 - invalid panel type or panel flag.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @stagemodelonly
         * @since 26.0.0
         */
        updatePanelRect(flag: PanelFlag, rect: EnhancedPanelRect): Promise<void>;
        /**
         * Update the panel rectangle.
         * > **NOTE**
         * >
         * > This API applies only to the panels of the **SOFT_KEYBOARD** type in the **FLG_FIXED** or **FLG_FLOATING**
         * > state.
         * >
         * > When the **PanelFlag** of a smartphone is **FLG_FLOATING** and the panel width is between 0 and 288 vp, the
         * > function buttons at the bottom of the panel will dynamically update their size according to the panel width. To
         * > ensure the optimal user experience, it is recommended that the panel width be no less than 90 vp.
         *
         * @param { PanelFlag } flag - Type of the state of the target panel. It can be **FLG_FIXED** or **FLG_FLOATING**.
         * @param { PanelRect } rect - Landscape rectangle and portrait rectangle of the target panel. For the panel of the
         *     fixed state, the height cannot exceed 70% of the screen height, and the width cannot exceed the screen width.
         *     For the panel of the floating state, the height cannot exceed the screen height, and the width cannot exceed
         *     the screen width.
         * @throws { BusinessError } 12800013 - window manager service error.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @stagemodelonly
         * @since 26.0.0
         */
        updatePanelRectSync(flag: PanelFlag, rect: PanelRect): void;
        /**
         * Update the panel rectangle, and customizes the avoid area and touch area.
         * > **NOTE**
         * >
         * > This API applies only to the panels of the **SOFT_KEYBOARD** type in the **FLG_FIXED** or **FLG_FLOATING**
         * > state. This API is compatible with
         * > [updatePanelRectSync]{@link inputMethodEngine.Panel.updatePanelRectSync(flag: PanelFlag, rect: PanelRect)}.
         * > If the input parameter **rect** contains only the **landscapeRect** and **portraitRect** attributes,
         * > [updatePanelRectSync]{@link inputMethodEngine.Panel.updatePanelRectSync(flag: PanelFlag, rect: PanelRect)}
         * > is called by default.
         * >
         * > When the **PanelFlag** of a smartphone is **FLG_FLOATING** and the panel width is between 0 and 288 vp, the
         * > function buttons at the bottom of the panel will dynamically update their size according to the panel width. To
         * > ensure the optimal user experience, it is recommended that the panel width be no less than 90 vp.
         *
         * @param { PanelFlag } flag - Type of the state of the target panel. It can be **FLG_FIXED** or **FLG_FLOATING**.
         * @param { EnhancedPanelRect } rect - The target panel rectangle, avoid area, and touch area.
         * @throws { BusinessError } 12800013 - window manager service error.
         * @throws { BusinessError } 12800017 - invalid panel type or panel flag.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @stagemodelonly
         * @since 26.0.0
         */
        updatePanelRectSync(flag: PanelFlag, rect: EnhancedPanelRect): void;
        /**
         * Updates the hot zone on the input method panel in the current state.
         *
         * > **NOTE**
         * >
         * > This API applies only to the panels of the **SOFT_KEYBOARD** type in the **FLG_FIXED** or **FLG_FLOATING**
         * > state.
         * >
         * > This API returns the result synchronously. The return only indicates that the system has received the request
         * > for updating the hot zone, not that the hot zone has been updated.
         *
         * @param { Array<window.Rect> } inputRegion - Region for receiving input events.
         *     <br>- The array size is limited to [1, 4].
         *     <br>- The input hot zone is relative to the left vertex of the input method panel window.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
         * @throws { BusinessError } 12800013 - window manager service error.
         * @throws { BusinessError } 12800017 - invalid panel type or panel flag.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 15
         */
        updateRegion(inputRegion: Array<window.Rect>): void;
        /**
         * Enables listening for the panel size change. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > This API applies only to the panels of the **SOFT_KEYBOARD** type in the **FLG_FIXED** or **FLG_FLOATING**
         * > state. When you call **adjustPanelRect** to adjust the panel size, the system calculates the final value based
         * > on certain rules (for example, whether the panel size exceeds the screen). This callback can be used to obtain
         * > the actual panel size to refresh the panel layout.
         * >
         * > -  This API is supported from API version 12 to 14. The callback function of this API contains only mandatory
         * > parameters of the [window.Size]{@link window.Size} type.
         * >
         * > -  Since API version 15, after the
         * > [adjustPanelRect]{@link inputMethodEngine.Panel.adjustPanelRect(flag: PanelFlag, rect: EnhancedPanelRect)} API
         * > is called, an optional parameter of the [KeyboardArea]{@link inputMethodEngine.KeyboardArea} type is added to
         * > the callback function of this API.
         *
         * @param { 'sizeChange' } type - Event type, which is **'sizeChange'**.
         * @param { Callback<window.Size> } callback - Callback used to return the size of the soft keyboard panel,
         *     including the width and height. [since 12 - 14]
         * @param { SizeChangeCallback } callback - Callback used to return the size of the soft keyboard panel, including
         *     the width and height. [since 15]
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 12
         */
        on(type: 'sizeChange', callback: SizeChangeCallback): void;
        /**
         * Disables listening for the panel size change. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > This API applies only to the panels of the **SOFT_KEYBOARD** type in the **FLG_FIXED** or **FLG_FLOATING**
         * > state. When you call **adjustPanelRect** to adjust the panel size, the system calculates the final value based
         * > on certain rules (for example, whether the panel size exceeds the screen). This callback can be used to obtain
         * > the actual panel size to refresh the panel layout.
         * >
         * > -  This API is supported from API version 12 to 14. The callback function of this API contains only mandatory
         * > parameters of the [window.Size]{@link window.Size} type.
         * >
         * > -  Since API version 15, after the
         * > [adjustPanelRect]{@link inputMethodEngine.Panel.adjustPanelRect(flag: PanelFlag, rect: EnhancedPanelRect)} API
         * > is called, an optional parameter of the [KeyboardArea]{@link inputMethodEngine.KeyboardArea} type is added to
         * > the callback function of this API.
         *
         * @param { 'sizeChange' } type - Event type, which is **'sizeChange'**.
         * @param { ?Callback<window.Size> } [callback] - Callback used to return the size of the soft keyboard panel,
         *     including the width and height. [since 12 - 14]
         * @param { ?SizeChangeCallback } [callback] - Callback used to return the size of the soft keyboard panel,
         *     including the width and height. [since 15]
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 12
         */
        off(type: 'sizeChange', callback?: SizeChangeCallback): void;
        /**
         * Sets the immersive mode of the input method application. You can only set the immersion mode to
         * **NONE_IMMERSIVE**, **LIGHT_IMMERSIVE**, or **DARK_IMMERSIVE**. **IMMERSIVE** cannot be set.
         *
         * @param { ImmersiveMode } mode - Immersive mode.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Incorrect parameter types; 2.Parameter verification failed.
         * @throws { BusinessError } 12800002 - input method engine error. Possible causes:
         *     1.input method panel not created. 2.the input method application does not subscribe to related events.
         * @throws { BusinessError } 12800013 - window manager service error.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 15
         */
        setImmersiveMode(mode: ImmersiveMode): void;
        /**
         * Obtains the immersive mode of the input method application.
         *
         * @returns { ImmersiveMode } Immersive mode.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 15
         */
        getImmersiveMode(): ImmersiveMode;
        /**
         * Sets the immersive effect of the input method application.
         *
         * - Gradient mode and fluid light mode can be used only when the
         * [immersive mode]{@link inputMethodEngine.Panel.setImmersiveMode} is enabled.
         * - The fluid light mode can be used only when the gradient mode is enabled.
         * - If the gradient mode is disabled, the gradient height must be 0 px.
         * - Only system applications can set the fluid light mode.
         * - The current API can be called only after any of the following APIs is called:
         *  - [adjustPanelRect]{@link inputMethodEngine.Panel.adjustPanelRect(flag: PanelFlag, rect: PanelRect)} (available
         * since API version 12)
         *  - [adjustPanelRect]{@link inputMethodEngine.Panel.adjustPanelRect(flag: PanelFlag, rect: EnhancedPanelRect)} (
         * available since API version 15)
         *  - [resize]{@link inputMethodEngine.Panel.resize(width: number, height: number, callback: AsyncCallback<void>)} (
         * available since API version 10)
         *
         * @param { ImmersiveEffect } effect - Immersive effect.
         * @throws { BusinessError } 801 - capability not supported.
         * @throws { BusinessError } 12800002 - input method engine error. Possible causes:
         *     1. input method panel not created. 2. the input method application does not subscribe to related events.
         * @throws { BusinessError } 12800013 - window manager service error.
         * @throws { BusinessError } 12800020 - invalid immersive effect.
         *     1. The gradient mode and the fluid light mode can only be used when the immersive mode is enabled.
         *     2. The fluid light mode can only be used when the gradient mode is enabled.
         *     3. When the gradient mode is not enabled, the gradient height can only be 0.
         * @throws { BusinessError } 12800021 - this operation is allowed only after adjustPanelRect or resize is called.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 20
         */
        setImmersiveEffect(effect: ImmersiveEffect): void;
        /**
         * Sets to keep the screen always on. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > - When the keyboard is displayed, the screen stays on. When the keyboard is hidden, the screen turns off.
         * >
         * > - You need to use this API properly. Set the attribute to **true** in necessary scenarios (for example, voice
         * > input) and reset this attribute to **false** after exiting necessary scenarios. In other scenarios, do not use
         * > this API.
         *
         * @param { boolean } isKeepScreenOn - Whether to keep the screen always on. The value **true** means that the
         *     screen is always on; the value **false** means the opposite.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 12800013 - window manager service error.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 20
         */
        setKeepScreenOn(isKeepScreenOn: boolean): Promise<void>;
        /**
         * Obtains the offset area of the soft keyboard relative to the system panel under the current state of the
         * specified screen (for example, folded or unfolded) and the current state of the input method keyboard (for
         * example, floating or fixed). This API uses a promise to return the result.
         *
         * @param { number } displayId - Display ID of the screen where the input method keyboard is located. It can be
         *     obtained by calling [getDisplayId]{@link inputMethodEngine.Panel.getDisplayId}.
         * @returns { Promise<SystemPanelInsets> } Promise used to return the offset area between the input method keyboard
         *     and the system panel.
         * @throws { BusinessError } 12800013 - window manager service error.
         * @throws { BusinessError } 12800017 - invalid panel type or panel flag. Possible causes:
         *     1. Current panel's type is not SOFT_KEYBOARD.  2. Panel's flag is not FLG_FIXED or FLG_FLOATING.
         * @throws { BusinessError } 12800022 - invalid displayId.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 21
         */
        getSystemPanelCurrentInsets(displayId: number): Promise<SystemPanelInsets>;
        /**
         * Sets the color of the function buttons and their background color on the current panel. This API uses a promise
         * to return the result.
         *
         * @param { string | undefined } fillColor - Color of the function buttons. The value can be [#01000000, #FFFFFFFF]
         *     or [#000000, #FFFFFF]. The value of the fully transparent alpha channel (**#00xxxxxx**) is not supported.
         * @param { string | undefined } backgroundColor - Background color of the function buttons. The value can be
         *     [#01000000, #FFFFFFFF] or [#000000, #FFFFFF]. The value of the fully transparent alpha channel (#00xxxxxx) is
         *     not supported.
         * @returns { Promise<void> } Promise that returns no result.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 22
         */
        setSystemPanelButtonColor(fillColor: string | undefined, backgroundColor: string | undefined): Promise<void>;
    }
    /**
     * Defines the offset area between the input method soft keyboard and the system panel.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 21
     */
    interface SystemPanelInsets {
        /**
         * Distance between the left border of the keyboard area and the left border of the system panel area, in px. The
         * value is an integer.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 21
         */
        readonly left: number;
        /**
         * Distance between the right border of the keyboard area and the right border of the system panel area, in px. The
         * value is an integer.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 21
         */
        readonly right: number;
        /**
         * Distance between the bottom border of the keyboard area and the bottom border of the system panel area, in px.
         * The value is an integer.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 21
         */
        readonly bottom: number;
    }
    /**
     * In the following API examples, you must first use
     * [getKeyboardDelegate]{@link inputMethodEngine.getKeyboardDelegate()} to obtain a **KeyboardDelegate** instance, and
     * then call the APIs using the obtained instance.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 8
     */
    interface EditorAttribute {
        /**
         * Text attribute of the edit box. For details, see
         * [edit box definitions in constants](docroot://reference/apis-ime-kit/js-apis-inputmethodengine.md#Constants).
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 8
         */
        readonly inputPattern: number;
        /**
         * Function attributes of the edit box. For details, see
         * [function key definitions in constants](docroot://reference/apis-ime-kit/js-apis-inputmethodengine.md#Constants).
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 8
         */
        readonly enterKeyType: number;
        /**
         * Whether text preview is supported.
         *
         * - **true**: Supported.
         * - **false**: Unsupported.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 12
         */
        isTextPreviewSupported: boolean;
        /**
         * Name of the application package to which the edit box belongs. The value may be **""**. Handle this scenario when
         * using the attribute.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 14
         */
        readonly bundleName?: string;
        /**
         * Immersive mode of the input method.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 15
         */
        readonly immersiveMode?: ImmersiveMode;
        /**
         * ID of the window where the edit box is located.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 18
         */
        readonly windowId?: number;
        /**
         * Screen ID of the window corresponding to the edit box. If window ID is not set, the screen ID of the focused
         * window is used.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 18
         */
        readonly displayId?: number;
        /**
         * Placeholder information set for the edit box.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 20
         */
        readonly placeholder?: string;
        /**
         * Ability name set for the edit box.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 20
         */
        readonly abilityName?: string;
        /**
         * Whether to capitalize the first letter in the edit box. If it is not set or is set to an invalid value, the first
         * letter is not capitalized by default.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 20
         */
        readonly capitalizeMode?: CapitalizeMode;
        /**
         * Gradient mode. If this attribute is not specified or is set to an invalid value, the gradient mode is not used by
         * default.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 20
         */
        readonly gradientMode?: GradientMode;
        /**
         * Extra information about the input method.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 22
         */
        readonly extraConfig?: InputMethodExtraConfig;
        /**
         * Whether the editor supports consuming key events.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @stagemodelonly
         * @since 26.0.0
         */
        readonly consumeKeyEvents?: boolean;
    }
    /**
     * In the following API examples, you must first use
     * [getKeyboardDelegate]{@link inputMethodEngine.getKeyboardDelegate()} to obtain a **KeyboardDelegate** instance, and
     * then call the APIs using the obtained instance.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 8
     */
    interface KeyEvent {
        /**
         * Key value. For details, see [KeyCode]{@link @ohos.multimodalInput.keyCode:KeyCode}.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 8
         */
        readonly keyCode: number;
        /**
         * Key event type.
         *
         * - **2**: keydown event.
         * - **3**: keyup event.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 8
         */
        readonly keyAction: number;
    }
    /**
     * Enumerates the state types of the input method panel.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 10
     */
    export enum PanelFlag {
        /**
         * Fixed style.
         *
         * <p>It's provided for the panel with type of SOFT_KEYBOARD.
         * When the flag is set, the soft keyboard is fixed at the bottom of the screen.</p>
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        FLG_FIXED = 0,
        /**
         * Floating style.
         *
         * <p>It's provided for the panel with type of SOFT_KEYBOARD.
         * When the flag is set, the soft keyboard is floating.</p>
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        FLG_FLOATING,
        /**
         * Candidate style.
         *
         * <p>It's provided for the panel with type of SOFT_KEYBOARD.
         * When the flag is set, the soft keyboard is a candidate window which will show the possible characters when user types a input code.
         * Panel with candidate style will not be automatically shown or hidden by input method service.
         * Input method application developers are supposed to control the panel status on their own.</p>
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 15
         */
        FLAG_CANDIDATE
    }
    /**
     * Enumerates the types of the input method panel.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 10
     */
    export enum PanelType {
        /**
         * Panel for displaying a virtual software keyboard.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        SOFT_KEYBOARD = 0,
        /**
         * Panel for displaying status bar.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        STATUS_BAR
    }
    /**
     * Describes the attributes of the input method panel.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 10
     */
    export interface PanelInfo {
        /**
         * Type of the panel.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        type: PanelType;
        /**
         * State type of the panel.
         *
         * @default FLG_FIXED
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        flag?: PanelFlag;
    }
    /**
     * Enumerates the directions of cursor movement of the input method.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 10
     */
    export enum Direction {
        /**
         * Upward.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        CURSOR_UP = 1,
        /**
         * Downward.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        CURSOR_DOWN,
        /**
         * Leftward.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        CURSOR_LEFT,
        /**
         * Rightward.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        CURSOR_RIGHT
    }
    /**
     * Describes the security mode.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 11
     */
    export enum SecurityMode {
        /**
         * Basic access mode, where network access is restricted.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 11
         */
        BASIC = 0,
        /**
         * Full access mode, where network access is not restricted.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 11
         */
        FULL
    }
    /**
     * Describes the range of the selected text.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 10
     */
    export interface Range {
        /**
         * Index of the first selected character in the text box.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        start: number;
        /**
         * Index of the last selected character in the text box.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        end: number;
    }
    /**
     * Describes the direction in which the cursor moves when the text is selected.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 10
     */
    export interface Movement {
        /**
         * Direction in which the cursor moves when the text is selected.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        direction: Direction;
    }
    /**
     * Describes the type of the extended edit action on the text box.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 10
     */
    export enum ExtendAction {
        /**
         * Select all.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        SELECT_ALL = 0,
        /**
         * Cut.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        CUT = 3,
        /**
         * Copy.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        COPY = 4,
        /**
         * Paste.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        PASTE = 5
    }
    /**
     * Represents window information.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 12
     */
    export interface WindowInfo {
        /**
         * Rectangular area of the window.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 12
         */
        rect: window.Rect;
        /**
         * Window status type.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 12
         */
        status: window.WindowStatusType;
    }
    /**
     * Represents the size of the input method panel.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 12
     */
    export interface PanelRect {
        /**
         * Size of the input method panel window in landscape mode.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 12
         */
        landscapeRect: window.Rect;
        /**
         * Size of the input method panel window in portrait mode.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 12
         */
        portraitRect: window.Rect;
    }
    /**
     * Represents a custom communication object.
     *
     * > **NOTE**
     * >
     * > You can register this object to receive custom communication data sent by the edit box application attached to
     * > the input method application. When the custom communication data is received, the
     * > [onMessage]{@link inputMethodEngine.MessageHandler.onMessage(msgId: string, msgParam?: ArrayBuffer)} callback in
     * > this object is triggered.
     * >
     * > This object is globally unique. After multiple registrations, only the last registered object is valid and
     * > retained, and the [onTerminated]{@link inputMethodEngine.MessageHandler.onTerminated()} callback of the
     * > penultimate registered object is triggered.
     * >
     * > If this object is unregistered, its [onTerminated]{@link inputMethodEngine.MessageHandler.onTerminated()}
     * > callback will be triggered.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 15
     */
    interface MessageHandler {
        /**
         * Receives the custom data callback sent by the edit box application attached to the input method application.
         *
         * > **NOTE**
         * >
         * > This callback is triggered when the registered [MessageHandler]{@link inputMethodEngine.MessageHandler}
         * > receives custom communication data sent by the edit box application attached to the input method application.
         * >
         * > The **msgId** parameter is mandatory, and the **msgParam** parameter is optional. If only the custom **msgId**
         * > data is received, confirm it with the data sender.
         *
         * @param { string } msgId - Identifier of the received custom communication data.
         * @param { ArrayBuffer } [msgParam] - Message body of the received custom communication data.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 15
         */
        onMessage(msgId: string, msgParam?: ArrayBuffer): void;
        /**
         * Listens for MessageHandler termination.
         *
         * > **NOTE**
         * >
         * > When an application registers a new [MessageHandler]{@link inputMethodEngine.MessageHandler} object, the
         * > [onTerminated]{@link inputMethodEngine.MessageHandler.onTerminated()} callback of the penultimate registered
         * > [MessageHandler]{@link inputMethodEngine.MessageHandler} object is triggered.
         * >
         * > When an application unregisters a new [MessageHandler]{@link inputMethodEngine.MessageHandler} object, the
         * > [onTerminated]{@link inputMethodEngine.MessageHandler.onTerminated()} callback of the registered
         * > [MessageHandler]{@link inputMethodEngine.MessageHandler} object is triggered.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 15
         */
        onTerminated(): void;
    }
    /**
     * Indicates the size of the enhanced input method panel, including the custom avoid area and touch area.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 15
     */
    export interface EnhancedPanelRect {
        /**
         * Size of the input method panel window in landscape mode.
         *
         * - This attribute is mandatory when **fullScreenMode** is not set or is set to **false**.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 15
         */
        landscapeRect?: window.Rect;
        /**
         * Size of the input method panel window in portrait mode.
         *
         * - This attribute is mandatory when **fullScreenMode** is not set or is set to **false**.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 15
         */
        portraitRect?: window.Rect;
        /**
         * Distance between the avoid line and the top of the panel in landscape mode, in px. The default value is **0**.
         *
         * - Other system components in the application avoid the input method panel area below the avoid line.
         * - When the panel is fixed, the distance between the avoid line and the bottom of the screen cannot exceed 70% of
         * the screen height.
         *
         * @default 0
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 15
         */
        landscapeAvoidY?: number;
        /**
         * Region where the panel receives input events in landscape mode.
         *
         * - The array size is limited to [1, 4]. The default value is the panel size in landscape mode.
         * - The input hot zone is relative to the left vertex of the input method panel window.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 15
         */
        landscapeInputRegion?: Array<window.Rect>;
        /**
         * Distance between the avoid line and the top of the panel in portrait mode, in px. The default value is **0**.
         *
         * - Other system components in the application avoid the input method panel area below the avoid line.
         * - When the panel is fixed, the distance between the avoid line and the bottom of the screen cannot exceed 70% of
         * the screen height.
         *
         * @default 0
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 15
         */
        portraitAvoidY?: number;
        /**
         * Region where the panel receives input events in portrait mode.
         *
         * - The array size is limited to [1, 4]. The default value is the panel size in portrait mode.
         * - The input hot zone is relative to the left vertex of the input method panel window.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 15
         */
        portraitInputRegion?: Array<window.Rect>;
        /**
         * Indicates whether to enable the full-screen mode. The default value is **false**.
         *
         * - If the value is **true**, **landscapeRect** and **portraitRect** are optional.
         * - If the value is **false**, **landscapeRect** and **portraitRect** are mandatory.
         *
         * @default false
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 15
         */
        fullScreenMode?: boolean;
    }
    /**
     * Represents the keyboard area on the panel.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 15
     */
    export interface KeyboardArea {
        /**
         * Distance between the upper boundary of the keyboard area and the upper boundary of the panel area, in pixels. The
         * value is an integer.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 15
         */
        top: number;
        /**
         * Distance between the lower boundary of the keyboard area and the lower boundary of the panel area, in pixels. The
         * value is an integer.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 15
         */
        bottom: number;
        /**
         * Distance between the left boundary of the keyboard area and the left boundary of the panel area, in pixels. The
         * value is an integer.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 15
         */
        left: number;
        /**
         * Distance between the right border of the keyboard area and the right border of the panel area, in pixels. The
         * value is an integer.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 15
         */
        right: number;
    }
    /**
     * Defines additional options for binding an input method.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 19
     */
    export interface AttachOptions {
        /**
         * Reason for requesting the keyboard. This attribute is set by the edit box application. If this attribute is not
         * set or is set to an invalid value, the keyboard will not be triggered by default.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 19
         */
        requestKeyboardReason?: RequestKeyboardReason;
        /**
         * Whether to enable the simple keyboard. This attribute is set by the edit box application. The value **true**
         * means that the simple keyboard is enabled, and the value **false** means the opposite.
         *
         * If this attribute is not set or is set to an invalid value, the simple keyboard is disabled by default.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 20
         */
        isSimpleKeyboardEnabled?: boolean;
    }
    /**
     * Enumerates the modes of capitalizing the first letter of a text.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 20
     */
    export enum CapitalizeMode {
        /**
         * Capitalize nothing.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 20
         */
        NONE = 0,
        /**
         * Capitalize the first letter of each sentence.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 20
         */
        SENTENCES,
        /**
         * Capitalize the first letter of each word.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 20
         */
        WORDS,
        /**
         * Capitalize each letter.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 20
         */
        CHARACTERS
    }
}
export default inputMethodEngine;

```
