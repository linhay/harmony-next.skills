# @ohos.inputMethod.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2021-2025 Huawei Device Co., Ltd.
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
import type { Callback, AsyncCallback } from './@ohos.base';
import InputMethodSubtype from './@ohos.InputMethodSubtype';
import { UIContext } from './@ohos.arkui.UIContext';
import type { ElementName } from './bundleManager/ElementName';
/**
 * The **inputMethod** module is oriented to common foreground applications (system applications such as Notes,
 * Messaging, and Settings). It provides input method control and management capabilities, including displaying or
 * hiding the soft keyboard, switching between input methods, and obtaining the list of all input methods.
 *
 * @syscap SystemCapability.MiscServices.InputMethodFramework
 * @since 6
 */
declare namespace inputMethod {
    /**
     * Keyboard max number. Max value is 128.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 8
     */
    const MAX_TYPE_NUM: number;
    /**
     * Input method setting
     *
     * @returns { InputMethodSetting } the object of InputMethodSetting
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 8
     * @deprecated since 9
     * @useinstead inputMethod#getSetting
     */
    function getInputMethodSetting(): InputMethodSetting;
    /**
     * Input method controller
     *
     * @returns { InputMethodController } the object of InputMethodController.
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 6
     * @deprecated since 9
     * @useinstead inputMethod#getController
     */
    function getInputMethodController(): InputMethodController;
    /**
     * Input method setting
     *
     * @returns { InputMethodSetting } the object of InputMethodSetting.
     * @throws { BusinessError } 12800007 - input method setter error. Possible cause:
     *     create InputMethodSetting object failed.
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 9
     */
    function getSetting(): InputMethodSetting;
    /**
     * Input method controller
     *
     * @returns { InputMethodController } the object of InputMethodController.
     * @throws { BusinessError } 12800006 - input method controller error. Possible cause:
     *     create InputMethodController object failed.
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 9
     */
    function getController(): InputMethodController;
    /**
     * Get default input method
     *
     * @returns { InputMethodProperty } property of the default input method.
     * @throws { BusinessError } 12800008 - input method manager service error. Possible cause:
     *     a system error, such as null pointer, IPC exception.
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 11
     */
    function getDefaultInputMethod(): InputMethodProperty;
    /**
     * Get system input method config ability
     *
     * @returns { ElementName } the information of system input method config ability.
     * @throws { BusinessError } 12800008 - input method manager service error. Possible cause:
     *     a system error, such as null pointer, IPC exception.
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 11
     */
    function getSystemInputMethodConfigAbility(): ElementName;
    /**
     * Switch input method. The caller must be the current inputmethod.
     *
     * @permission ohos.permission.CONNECT_IME_ABILITY [since 9 - 10]
     * @param { InputMethodProperty } target - indicates the target input method.
     * @param { AsyncCallback<boolean> } callback - the callback of switchInputMethod.
     * @throws { BusinessError } 201 - permissions check fails. [since 9 - 10]
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
     * @throws { BusinessError } 12800005 - configuration persistence error.
     * @throws { BusinessError } 12800008 - input method manager service error. Possible cause:
     *     a system error, such as null pointer, IPC exception.
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 9
     */
    function switchInputMethod(target: InputMethodProperty, callback: AsyncCallback<boolean>): void;
    /**
     * Switch input method. The caller must be the current inputmethod.
     *
     * @permission ohos.permission.CONNECT_IME_ABILITY [since 9 - 10]
     * @param { InputMethodProperty } target - indicates the target input method.
     * @returns { Promise<boolean> } the promise returned by the function.
     * @throws { BusinessError } 201 - permissions check fails. [since 9 - 10]
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
     * @throws { BusinessError } 12800005 - configuration persistence error.
     * @throws { BusinessError } 12800008 - input method manager service error. Possible cause:
     *     a system error, such as null pointer, IPC exception.
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 9
     */
    function switchInputMethod(target: InputMethodProperty): Promise<boolean>;
    /**
     * Get current input method
     *
     * @returns { InputMethodProperty } the property of current inputmethod.
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 9
     */
    function getCurrentInputMethod(): InputMethodProperty;
    /**
     * Switch current input method subtype. The caller must be the current inputmethod.
     *
     * @permission ohos.permission.CONNECT_IME_ABILITY [since 9 - 10]
     * @param { InputMethodSubtype } target - indicates the target input method subtype.
     * @param { AsyncCallback<boolean> } callback - the callback of switchCurrentInputMethodSubtype.
     * @throws { BusinessError } 201 - permissions check fails. [since 9 - 10]
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
     * @throws { BusinessError } 12800005 - configuration persistence error.
     * @throws { BusinessError } 12800008 - input method manager service error. Possible cause:
     *     a system error, such as null pointer, IPC exception.
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 9
     */
    function switchCurrentInputMethodSubtype(target: InputMethodSubtype, callback: AsyncCallback<boolean>): void;
    /**
     * Switch current input method subtype. The caller must be the current inputmethod.
     *
     * @permission ohos.permission.CONNECT_IME_ABILITY [since 9 - 10]
     * @param { InputMethodSubtype } target - indicates the target input method subtype.
     * @returns { Promise<boolean> } the promise returned by the function.
     * @throws { BusinessError } 201 - permissions check fails. [since 9 - 10]
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
     * @throws { BusinessError } 12800005 - configuration persistence error.
     * @throws { BusinessError } 12800008 - input method manager service error. Possible cause:
     *     a system error, such as null pointer, IPC exception.
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 9
     */
    function switchCurrentInputMethodSubtype(target: InputMethodSubtype): Promise<boolean>;
    /**
     * Get the current input method subtype
     *
     * @returns { InputMethodSubtype } the subtype of the current input method.
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 9
     */
    function getCurrentInputMethodSubtype(): InputMethodSubtype;
    /**
     * Switch input method and subtype. The caller must be the current inputmethod.
     *
     * @permission ohos.permission.CONNECT_IME_ABILITY [since 9 - 10]
     * @param { InputMethodProperty } inputMethodProperty - indicates the target input method.
     * @param { InputMethodSubtype } inputMethodSubtype - indicates the target input method subtype.
     * @param { AsyncCallback<boolean> } callback - the callback of switchCurrentInputMethodAndSubtype.
     * @throws { BusinessError } 201 - permissions check fails. [since 9 - 10]
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
     * @throws { BusinessError } 12800005 - configuration persistence error.
     * @throws { BusinessError } 12800008 - input method manager service error. Possible cause:
     *     a system error, such as null pointer, IPC exception.
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 9
     */
    function switchCurrentInputMethodAndSubtype(inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype, callback: AsyncCallback<boolean>): void;
    /**
     * Switch input method and subtype. The caller must be the current inputmethod.
     *
     * @permission ohos.permission.CONNECT_IME_ABILITY [since 9 - 10]
     * @param { InputMethodProperty } inputMethodProperty - indicates the target input method.
     * @param { InputMethodSubtype } inputMethodSubtype - indicates the target input method subtype.
     * @returns { Promise<boolean> } the promise returned by the function.
     * @throws { BusinessError } 201 - permissions check fails. [since 9 - 10]
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
     * @throws { BusinessError } 12800005 - configuration persistence error.
     * @throws { BusinessError } 12800008 - input method manager service error. Possible cause:
     *     a system error, such as null pointer, IPC exception.
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 9
     */
    function switchCurrentInputMethodAndSubtype(inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype): Promise<boolean>;
    /**
     * Set simple keyboard mode.
     *
     * @param { boolean } enable - indicates enable simple keyboard or not.
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 20
     */
    function setSimpleKeyboardEnabled(enable: boolean): void;
    /**
     * Subscribe the attachment failure event.
     *
     * @param { Callback<AttachFailureReason> } callback - the callback is invoked only when the attachment
     *     triggered by the registrant's process fails.
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 22
     */
    function onAttachmentDidFail(callback: Callback<AttachFailureReason>): void;
    /**
     * Unsubscribe the attachment failure event.
     *
     * @param { Callback<AttachFailureReason> } [callback] - the callback is invoked only when the attachment
     *     triggered by the registrant's process fails. When subscriber unsubscribes all callback, this parameter
     *     can be left blank.
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 22
     */
    function offAttachmentDidFail(callback?: Callback<AttachFailureReason>): void;
    /**
     * In the following API examples, you must first use [getSetting]{@link @ohos.inputMethod:inputMethod.getSetting} to
     * obtain an **InputMethodSetting** instance, and then call the APIs using the obtained instance.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 8
     */
    interface InputMethodSetting {
        /**
         * Subscribe input method or subtype change.
         *
         * @param { 'imeChange' } type - Indicates the event type.
         * @param { function } callback - the callback of 'imeChange'
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         */
        on(type: 'imeChange', callback: (inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype) => void): void;
        /**
         * Unsubscribe input method or subtype change.
         *
         * @param { 'imeChange' } type - Indicates the event type.
         * @param { function } [callback] - the callback of 'imeChange',
         *     when subscriber unsubscribes all callback functions of event 'imeChange', this parameter can be left blank.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         */
        off(type: 'imeChange', callback?: (inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype) => void): void;
        /**
         * List subtype of the specified input method.
         *
         * @param { InputMethodProperty } inputMethodProperty - the property of the specified inputmethod.
         * @param { AsyncCallback<Array<InputMethodSubtype>> } callback - the callback of listInputMethodSubtype.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
         * @throws { BusinessError } 12800001 - bundle manager error.
         * @throws { BusinessError } 12800008 - input method manager service error. Possible cause:
         *     a system error, such as null pointer, IPC exception.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         */
        listInputMethodSubtype(inputMethodProperty: InputMethodProperty, callback: AsyncCallback<Array<InputMethodSubtype>>): void;
        /**
         * List subtype of the specified input method.
         *
         * @param { InputMethodProperty } inputMethodProperty - Indicates the specified input method.
         * @returns { Promise<Array<InputMethodSubtype>> } the promise returned by the function.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
         * @throws { BusinessError } 12800001 - bundle manager error.
         * @throws { BusinessError } 12800008 - input method manager service error. Possible cause:
         *     a system error, such as null pointer, IPC exception.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         */
        listInputMethodSubtype(inputMethodProperty: InputMethodProperty): Promise<Array<InputMethodSubtype>>;
        /**
         * List subtype of current input method
         *
         * @param { AsyncCallback<Array<InputMethodSubtype>> } callback - the callback of listCurrentInputMethodSubtype.
         * @throws { BusinessError } 12800001 - bundle manager error.
         * @throws { BusinessError } 12800008 - input method manager service error. Possible cause:
         *     a system error, such as null pointer, IPC exception.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         */
        listCurrentInputMethodSubtype(callback: AsyncCallback<Array<InputMethodSubtype>>): void;
        /**
         * List subtype of current input method
         *
         * @returns { Promise<Array<InputMethodSubtype>> } the promise returned by the function.
         * @throws { BusinessError } 12800001 - bundle manager error.
         * @throws { BusinessError } 12800008 - input method manager service error. Possible cause:
         *     a system error, such as null pointer, IPC exception.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         */
        listCurrentInputMethodSubtype(): Promise<Array<InputMethodSubtype>>;
        /**
         * List input methods
         *
         * @param { boolean } enable -
         *     If true, collect enabled input methods.
         *     If false, collect disabled input methods.
         * @param { AsyncCallback<Array<InputMethodProperty>> } callback - the callback of getInputMethods.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @throws { BusinessError } 12800001 - bundle manager error.
         * @throws { BusinessError } 12800008 - input method manager service error. Possible cause:
         *     a system error, such as null pointer, IPC exception.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         */
        getInputMethods(enable: boolean, callback: AsyncCallback<Array<InputMethodProperty>>): void;
        /**
         * List input methods
         *
         * @param { boolean } enable -
         *     If true, collect enabled input methods.
         *     If false, collect disabled input methods.
         * @returns { Promise<Array<InputMethodProperty>> } the promise returned by the function.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @throws { BusinessError } 12800001 - bundle manager error.
         * @throws { BusinessError } 12800008 - input method manager service error. Possible cause:
         *     a system error, such as null pointer, IPC exception.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         */
        getInputMethods(enable: boolean): Promise<Array<InputMethodProperty>>;
        /**
         * List enabled or disabled input methods sync
         *
         * @param { boolean } enable -
         *     If true, collect enabled input methods.
         *     If false, collect disabled input methods.
         * @returns { Array<InputMethodProperty> } the list of inputmethod.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @throws { BusinessError } 12800001 - bundle manager error.
         * @throws { BusinessError } 12800008 - input method manager service error. Possible cause:
         *     a system error, such as null pointer, IPC exception.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 11
         */
        getInputMethodsSync(enable: boolean): Array<InputMethodProperty>;
        /**
         * List all input methods
         *
         * @param { AsyncCallback<Array<InputMethodProperty>> } callback - the callback of getInputMethods.
         * @throws { BusinessError } 12800001 - bundle manager error.
         * @throws { BusinessError } 12800008 - input method manager service error. Possible cause:
         *     a system error, such as null pointer, IPC exception.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 11
         */
        getAllInputMethods(callback: AsyncCallback<Array<InputMethodProperty>>): void;
        /**
         * List all input methods
         *
         * @returns { Promise<Array<InputMethodProperty>> } the promise returned by the function.
         * @throws { BusinessError } 12800001 - bundle manager error.
         * @throws { BusinessError } 12800008 - input method manager service error. Possible cause:
         *     a system error, such as null pointer, IPC exception.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 11
         */
        getAllInputMethods(): Promise<Array<InputMethodProperty>>;
        /**
         * List all input methods sync
         *
         * @returns { Array<InputMethodProperty> } the list of all inputmethod.
         * @throws { BusinessError } 12800001 - bundle manager error.
         * @throws { BusinessError } 12800008 - input method manager service error. Possible cause:
         *     a system error, such as null pointer, IPC exception.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 11
         */
        getAllInputMethodsSync(): Array<InputMethodProperty>;
        /**
         *
         * @param { AsyncCallback<Array<InputMethodProperty>> } callback - the callback of listInputMethod.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 8
         * @deprecated since 9
         * @useinstead inputMethod.InputMethodSetting#getInputMethods
         */
        listInputMethod(callback: AsyncCallback<Array<InputMethodProperty>>): void;
        /**
         *
         * @returns { Promise<Array<InputMethodProperty>> } the promise returned by the function.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 8
         * @deprecated since 9
         * @useinstead inputMethod.InputMethodSetting#getInputMethods
         */
        listInputMethod(): Promise<Array<InputMethodProperty>>;
        /**
         * Show input method setting extension dialog
         *
         * @param { AsyncCallback<boolean> } callback - the callback of showOptionalInputMethods.
         * @throws { BusinessError } 12800008 - input method manager service error. Possible cause:
         *     a system error, such as null pointer, IPC exception.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         * @deprecated since 18
         * @useinstead ohos.inputMethodList/InputMethodListDialog
         */
        showOptionalInputMethods(callback: AsyncCallback<boolean>): void;
        /**
         * Show input method setting extension dialog
         *
         * @returns { Promise<boolean> } the promise returned by the function.
         * @throws { BusinessError } 12800008 - input method manager service error. Possible cause:
         *     a system error, such as null pointer, IPC exception.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         * @deprecated since 18
         * @useinstead ohos.inputMethodList/InputMethodListDialog
         */
        showOptionalInputMethods(): Promise<boolean>;
        /**
         *
         * @param { AsyncCallback<void> } callback - the callback of displayOptionalInputMethod.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.inputMethodList/InputMethodListDialog
         */
        displayOptionalInputMethod(callback: AsyncCallback<void>): void;
        /**
         *
         * @returns { Promise<void> } the promise returned by the function.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.inputMethodList/InputMethodListDialog
         */
        displayOptionalInputMethod(): Promise<void>;
        /**
         * The input method application calls this interface to obtain its own enabled state.
         *
         * @returns { Promise<EnabledState> } the promise returned by the function.
         * @throws { BusinessError } 12800004 - not an input method application.
         * @throws { BusinessError } 12800008 - input method manager service error. Possible cause:
         *     a system error, such as null pointer, IPC exception.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 15
         */
        getInputMethodState(): Promise<EnabledState>;
    }
    /**
     * A control class that encapsulates APIs for input method management, which can only be invoked after an
     * **InputMethodController** instance is obtained via
     * [getController]{@link @ohos.inputMethod:inputMethod.getController}.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 6
     */
    interface InputMethodController {
        /**
         * Attach application to the input method service.
         *
         * @param { boolean } showKeyboard - show the keyboard or not when attach the input method.
         * @param { TextConfig } textConfig - indicates the config of the textInput.
         * @param { AsyncCallback<void> } callback - the callback of attach.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @throws { BusinessError } 12800008 - input method manager service error. Possible cause:
         *     a system error, such as null pointer, IPC exception.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        attach(showKeyboard: boolean, textConfig: TextConfig, callback: AsyncCallback<void>): void;
        /**
         * Attach application to the input method service.
         *
         * @param { boolean } showKeyboard - show the keyboard or not when attach the input method.
         * @param { TextConfig } textConfig - indicates the config of the textInput.
         * @returns { Promise<void> } the promise returned by the function.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @throws { BusinessError } 12800008 - input method manager service error. Possible cause:
         *     a system error, such as null pointer, IPC exception.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        attach(showKeyboard: boolean, textConfig: TextConfig): Promise<void>;
        /**
         * Attach application to the input method service.
         *
         * @param { boolean } showKeyboard - show the keyboard or not when attach the input method.
         * @param { TextConfig } textConfig - indicates the config of the textInput.
         * @param { RequestKeyboardReason } requestKeyboardReason - requestKeyboardReason of show the keyboard .
         * @returns { Promise<void> } the promise returned by the function.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @throws { BusinessError } 12800008 - input method manager service error. Possible cause:
         *     a system error, such as null pointer, IPC exception.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 15
         */
        attach(showKeyboard: boolean, textConfig: TextConfig, requestKeyboardReason: RequestKeyboardReason): Promise<void>;
        /**
         * Attach application to the input method service with UI context.
         *
         * @param { UIContext } uiContext - indicates the ui context where the attachment will be performed.
         * @param { TextConfig } textConfig - indicates the config of the textInput.
         * @param { AttachOptions } [attachOptions] - indicates the attach options.
         * @returns { Promise<void> } the promise returned by the function.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @throws { BusinessError } 12800008 - input method manager service error. Possible cause:
         *     a system error, such as null pointer, IPC exception.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @stagemodelonly
         * @since 23
         */
        attachWithUIContext(uiContext: UIContext, textConfig: TextConfig, attachOptions?: AttachOptions): Promise<void>;
        /**
         * Discard the typing text
         *
         * @returns { Promise<void> } the promise returned by the function.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @throws { BusinessError } 12800009 - input method client detached.
         * @throws { BusinessError } 12800015 - the other side does not accept the request.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 20
         */
        discardTypingText(): Promise<void>;
        /**
         * Show the text input and start typing.
         *
         * @param { AsyncCallback<void> } callback - the callback of showTextInput.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @throws { BusinessError } 12800008 - input method manager service error. Possible cause:
         *     a system error, such as null pointer, IPC exception.
         * @throws { BusinessError } 12800009 - input method client detached.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        showTextInput(callback: AsyncCallback<void>): void;
        /**
         * Show the text input and start typing.
         *
         * @returns { Promise<void> } the promise returned by the function.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @throws { BusinessError } 12800008 - input method manager service error. Possible cause:
         *     a system error, such as null pointer, IPC exception.
         * @throws { BusinessError } 12800009 - input method client detached.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        showTextInput(): Promise<void>;
        /**
         * Show the text input and start typing.
         *
         * @param { RequestKeyboardReason } requestKeyboardReason - requestKeyboardReason of show the keyboard .
         * @returns { Promise<void> } the promise returned by the function.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @throws { BusinessError } 12800008 - input method manager service error. Possible cause:
         *     a system error, such as null pointer, IPC exception.
         * @throws { BusinessError } 12800009 - input method client detached.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 15
         */
        showTextInput(requestKeyboardReason: RequestKeyboardReason): Promise<void>;
        /**
         * Hide the text input and stop typing.
         *
         * @param { AsyncCallback<void> } callback - the callback of hideTextInput.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @throws { BusinessError } 12800008 - input method manager service error. Possible cause:
         *     a system error, such as null pointer, IPC exception.
         * @throws { BusinessError } 12800009 - input method client detached.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        hideTextInput(callback: AsyncCallback<void>): void;
        /**
         * Hide the text input and stop typing.
         *
         * @returns { Promise<void> } the promise returned by the function.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @throws { BusinessError } 12800008 - input method manager service error. Possible cause:
         *     a system error, such as null pointer, IPC exception.
         * @throws { BusinessError } 12800009 - input method client detached.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        hideTextInput(): Promise<void>;
        /**
         * Detach the applications from the input method manager service.
         *
         * @param { AsyncCallback<void> } callback - the callback of detach.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @throws { BusinessError } 12800008 - input method manager service error. Possible cause:
         *     a system error, such as null pointer, IPC exception.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        detach(callback: AsyncCallback<void>): void;
        /**
         * Detach the applications from the input method manager service.
         *
         * @returns { Promise<void> } the promise returned by the function.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @throws { BusinessError } 12800008 - input method manager service error. Possible cause:
         *     a system error, such as null pointer, IPC exception.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        detach(): Promise<void>;
        /**
         * Inform the system of the window ID of the application currently bound to the input method.
         * After the correct setting, the window where the client is located can avoid the input method window.
         *
         * @param { number } windowId - the window ID of the application currently bound to the input method.
         * @param { AsyncCallback<void> } callback - the callback of setCallingWindow.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @throws { BusinessError } 12800008 - input method manager service error. Possible cause:
         *     a system error, such as null pointer, IPC exception.
         * @throws { BusinessError } 12800009 - input method client detached.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        setCallingWindow(windowId: number, callback: AsyncCallback<void>): void;
        /**
         * Inform the system of the window ID of the application currently bound to the input method.
         * After the correct setting, the window where the client is located can avoid the input method window.
         *
         * @param { number } windowId - the window ID of the application currently bound to the input method.
         * @returns { Promise<void> } the promise returned by the function.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @throws { BusinessError } 12800008 - input method manager service error. Possible cause:
         *     a system error, such as null pointer, IPC exception.
         * @throws { BusinessError } 12800009 - input method client detached.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        setCallingWindow(windowId: number): Promise<void>;
        /**
         * Update Cursor and notify the input method that the current application cursor has changed.
         *
         * @param { CursorInfo } cursorInfo - the CursorInfo object.
         * @param { AsyncCallback<void> } callback - the callback of updateCursor.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @throws { BusinessError } 12800008 - input method manager service error. Possible cause:
         *     a system error, such as null pointer, IPC exception.
         * @throws { BusinessError } 12800009 - input method client detached.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        updateCursor(cursorInfo: CursorInfo, callback: AsyncCallback<void>): void;
        /**
         * Update Cursor and notify the input method that the current application cursor has changed.
         *
         * @param { CursorInfo } cursorInfo - the CursorInfo object.
         * @returns { Promise<void> } the promise returned by the function.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @throws { BusinessError } 12800008 - input method manager service error. Possible cause:
         *     a system error, such as null pointer, IPC exception.
         * @throws { BusinessError } 12800009 - input method client detached.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        updateCursor(cursorInfo: CursorInfo): Promise<void>;
        /**
         * Notify the input method the selected text and the selection range of the current application text has changed.
         *
         * @param { string } text - the whole input text.
         * @param { number } start - start position of selected text.
         * @param { number } end - end position of selected text.
         * @param { AsyncCallback<void> } callback - the callback of changeSelection.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @throws { BusinessError } 12800008 - input method manager service error. Possible cause:
         *     a system error, such as null pointer, IPC exception.
         * @throws { BusinessError } 12800009 - input method client detached.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        changeSelection(text: string, start: number, end: number, callback: AsyncCallback<void>): void;
        /**
         * Notify the input method the selected text and the selection range of the current application text has changed.
         *
         * @param { string } text - the selected text.
         * @param { number } start - start position of selected text.
         * @param { number } end - end position of selected text.
         * @returns { Promise<void> } the promise returned by the function.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @throws { BusinessError } 12800008 - input method manager service error. Possible cause:
         *     a system error, such as null pointer, IPC exception.
         * @throws { BusinessError } 12800009 - input method client detached.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        changeSelection(text: string, start: number, end: number): Promise<void>;
        /**
         * Update InputAttribute information of input text.
         *
         * @param { InputAttribute } attribute - the InputAttribute object.
         * @param { AsyncCallback<void> } callback - the callback of updateAttribute.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @throws { BusinessError } 12800008 - input method manager service error. Possible cause:
         *     a system error, such as null pointer, IPC exception.
         * @throws { BusinessError } 12800009 - input method client detached.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        updateAttribute(attribute: InputAttribute, callback: AsyncCallback<void>): void;
        /**
         * Update InputAttribute information of input text.
         *
         * @param { InputAttribute } attribute - the InputAttribute object.
         * @returns { Promise<void> } the promise returned by the function.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @throws { BusinessError } 12800008 - input method manager service error. Possible cause:
         *     a system error, such as null pointer, IPC exception.
         * @throws { BusinessError } 12800009 - input method client detached.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        updateAttribute(attribute: InputAttribute): Promise<void>;
        /**
         * Stop input session
         *
         * @param { AsyncCallback<boolean> } callback - the callback of stopInputSession.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @throws { BusinessError } 12800008 - input method manager service error. Possible cause:
         *     a system error, such as null pointer, IPC exception.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         */
        stopInputSession(callback: AsyncCallback<boolean>): void;
        /**
         * Stop input session
         *
         * @returns { Promise<boolean> } the promise returned by the function.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @throws { BusinessError } 12800008 - input method manager service error. Possible cause:
         *     a system error, such as null pointer, IPC exception.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         */
        stopInputSession(): Promise<boolean>;
        /**
         * Stop input
         *
         * @param { AsyncCallback<boolean> } callback - the callback of stopInput.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 6
         * @deprecated since 9
         * @useinstead inputMethod.InputMethodController#stopInputSession
         */
        stopInput(callback: AsyncCallback<boolean>): void;
        /**
         * Stop input
         *
         * @returns { Promise<boolean> } the promise returned by the function.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 6
         * @deprecated since 9
         * @useinstead inputMethod.InputMethodController#stopInputSession
         */
        stopInput(): Promise<boolean>;
        /**
         * Show soft keyboard.
         * This API can be called only by system applications.
         *
         * @permission ohos.permission.CONNECT_IME_ABILITY
         * @param { AsyncCallback<void> } callback - the callback of showSoftKeyboard.
         * @throws { BusinessError } 201 - permissions check fails.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @throws { BusinessError } 12800008 - input method manager service error. Possible cause:
         *     a system error, such as null pointer, IPC exception.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         */
        showSoftKeyboard(callback: AsyncCallback<void>): void;
        /**
         * Show soft keyboard.
         * This API can be called only by system applications.
         *
         * @permission ohos.permission.CONNECT_IME_ABILITY
         * @returns { Promise<void> } the promise returned by the function.
         * @throws { BusinessError } 201 - permissions check fails.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @throws { BusinessError } 12800008 - input method manager service error. Possible cause:
         *     a system error, such as null pointer, IPC exception.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         */
        showSoftKeyboard(): Promise<void>;
        /**
         * Hide soft keyboard.
         * This API can be called only by system applications.
         *
         * @permission ohos.permission.CONNECT_IME_ABILITY
         * @param { AsyncCallback<void> } callback - the callback of hideSoftKeyboard.
         * @throws { BusinessError } 201 - permissions check fails.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @throws { BusinessError } 12800008 - input method manager service error. Possible cause:
         *     a system error, such as null pointer, IPC exception.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         */
        hideSoftKeyboard(callback: AsyncCallback<void>): void;
        /**
         * Hide soft keyboard.
         * This API can be called only by system applications.
         *
         * @permission ohos.permission.CONNECT_IME_ABILITY
         * @returns { Promise<void> } the promise returned by the function.
         * @throws { BusinessError } 201 - permissions check fails.
         * @throws { BusinessError } 12800003 - input method client error. Possible causes:
         *     1.the edit box is not focused. 2.no edit box is bound to current input method application.
         *     3.ipc failed due to the large amount of data transferred or other reasons.
         * @throws { BusinessError } 12800008 - input method manager service error. Possible cause:
         *     a system error, such as null pointer, IPC exception.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         */
        hideSoftKeyboard(): Promise<void>;
        /**
         * Send message to input method.
         *
         * @param { string } msgId - the identifier of the message. Max size is 256B.
         * @param { ?ArrayBuffer } [msgParam] - the param of the custom message. Max size is 128KB.
         * @returns { Promise<void> } the promise returned by the function.
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
         * Start receiving message from input method.
         *
         * @param { ?MessageHandler } [msgHandler] - optional, the handler of the custom message.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Incorrect parameter types.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 15
         */
        recvMessage(msgHandler?: MessageHandler): void;
        /**
         * Register a callback and when IME sends select event with range of selection,
         * the callback will be invoked.
         *
         * @param { 'selectByRange' } type - event type, fixed as 'selectByRange'.
         * @param { Callback<Range> } callback - processes selectByRange command. The range of selection is provided for
         *     this callback, and subscribers are expected to select corresponding text in callback according to
         *     the range.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        on(type: 'selectByRange', callback: Callback<Range>): void;
        /**
         * Unregister the callback of selectedByRange.
         *
         * @param { 'selectByRange' } type - event type, fixed as 'selectByRange'.
         * @param { Callback<Range> } [callback] - the callback of 'selectByRange',
         *     when subscriber unsubscribes all callback functions of event 'selectByRange', this parameter can be left
         *     blank.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        off(type: 'selectByRange', callback?: Callback<Range>): void;
        /**
         * Register a callback and when IME sends select event witch movement of cursor,
         * the callback will be invoked.
         *
         * @param { 'selectByMovement' } type - event type, fixed as 'selectByMovement'.
         * @param { Callback<Movement> } callback - processes selectByMovement command. The movement of cursor is provided
         *     for this callback, and subscribers are expected to select corresponding text in callback according to
         *     the movement.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        on(type: 'selectByMovement', callback: Callback<Movement>): void;
        /**
         * Unregister the callback of selectedByMovement.
         *
         * @param { 'selectByMovement' } type - event type, fixed as 'selectByMovement'.
         * @param { Callback<Movement> } [callback] - the callback of 'selectByMovement',
         *     when subscriber unsubscribes all callback functions of event 'selectByMovement', this parameter can be left
         *     blank.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        off(type: 'selectByMovement', callback?: Callback<Movement>): void;
        /**
         * Register a callback and when IME sends insert text event, the callback will be invoked.
         *
         * @param { 'insertText' } type - event type, fixed as 'insertText'.
         * @param { function } callback - processes insertText command. The text of insert is provided for this callback.
         *     Subscribers are expected to process the inserted text and update changes in editor by changeSelection and
         *     updateCursor as needed.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
         * @throws { BusinessError } 12800009 - input method client detached.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        on(type: 'insertText', callback: (text: string) => void): void;
        /**
         * Unregister the callback of insertText.
         *
         * @param { 'insertText' } type - event type, fixed as 'insertText'.
         * @param { function } [callback] - the callback of 'insertText',
         *     when subscriber unsubscribes all callback functions of event 'insertText', this parameter can be left blank.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        off(type: 'insertText', callback?: (text: string) => void): void;
        /**
         * Register a callback and when IME sends delete left event with length,
         * the callback will be invoked.
         *
         * @param { 'deleteLeft' } type - event type, fixed as 'deleteLeft'.
         * @param { function } callback - processes deleteLeft command. The length of
         *     delete is provided for this callback. Subscribers are expected to delete specified length of text
         *     to the left of the cursor and update changes in editor by changeSelection and updateCursor as needed.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
         * @throws { BusinessError } 12800009 - input method client detached.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        on(type: 'deleteLeft', callback: (length: number) => void): void;
        /**
         * Unregister the callback of deleteLeft.
         *
         * @param { 'deleteLeft' } type - event type, fixed as 'deleteLeft'.
         * @param { function } [callback] - the callback of 'deleteLeft',
         *     when subscriber unsubscribes all callback functions of event 'deleteLeft', this parameter can be left blank.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        off(type: 'deleteLeft', callback?: (length: number) => void): void;
        /**
         * Register a callback and when IME sends delete right event with length,
         * the callback will be invoked.
         *
         * @param { 'deleteRight' } type - event type, fixed as 'deleteRight'.
         * @param { function } callback - processes deleteRight command. The length of
         *     delete is provided for this callback. Subscribers are expected to delete specified length of text
         *     to the right of the cursor and update changes in editor by changeSelection and updateCursor as needed.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
         * @throws { BusinessError } 12800009 - input method client detached.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        on(type: 'deleteRight', callback: (length: number) => void): void;
        /**
         * Unregister the callback of deleteRight.
         *
         * @param { 'deleteRight' } type - event type, fixed as 'deleteRight'.
         * @param { function } [callback] - the callback of 'deleteRight',
         *     when subscriber unsubscribes all callback functions of event 'deleteRight', this parameter can be left blank.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        off(type: 'deleteRight', callback?: (length: number) => void): void;
        /**
         * Register a callback and when IME sends keyboard status, the callback will be invoked.
         *
         * @param { 'sendKeyboardStatus' } type - event type, fixed as 'sendKeyboardStatus'.
         * @param { function } callback - processes sendKeyboardStatus command.
         *     The keyboardStatus is provided for this callback.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
         * @throws { BusinessError } 12800009 - input method client detached.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        on(type: 'sendKeyboardStatus', callback: (keyboardStatus: KeyboardStatus) => void): void;
        /**
         * Unregister the callback of sendKeyboardStatus.
         *
         * @param { 'sendKeyboardStatus' } type - event type, fixed as 'sendKeyboardStatus'.
         * @param { function } [callback] - the callback of 'sendKeyboardStatus',
         *     when subscriber unsubscribes all callback functions of event 'sendKeyboardStatus', this parameter can be left
         *     blank.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        off(type: 'sendKeyboardStatus', callback?: (keyboardStatus: KeyboardStatus) => void): void;
        /**
         * Register a callback and when IME sends functionKey, the callback will be invoked.
         *
         * @param { 'sendFunctionKey' } type - event type, fixed as 'sendFunctionKey'.
         * @param { function } callback - processes sendFunctionKey command.
         *     The functionKey is provided for this callback.Subscribers are expected to complete the
         *     corresponding task based on the value of functionKey.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
         * @throws { BusinessError } 12800009 - input method client detached.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        on(type: 'sendFunctionKey', callback: (functionKey: FunctionKey) => void): void;
        /**
         * Unregister the callback of sendFunctionKey.
         *
         * @param { 'sendFunctionKey' } type - event type, fixed as 'sendFunctionKey'.
         * @param { function } [callback] - the callback of 'sendFunctionKey',
         *     when subscriber unsubscribes all callback functions of event 'sendFunctionKey', this parameter can be left
         *     blank.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        off(type: 'sendFunctionKey', callback?: (functionKey: FunctionKey) => void): void;
        /**
         * Register a callback and when IME sends move cursor, the callback will be invoked.
         *
         * @param { 'moveCursor' } type - event type, fixed as 'moveCursor'.
         * @param { function } callback - processes moveCursor command. The direction of
         *     cursor is provided for this callback. Subscribers are expected to move the cursor and update changes
         *     in editor by changeSelection and updateCursor.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
         * @throws { BusinessError } 12800009 - input method client detached.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        on(type: 'moveCursor', callback: (direction: Direction) => void): void;
        /**
         * Unregister the callback of moveCursor.
         *
         * @param { 'moveCursor' } type - event type, fixed as 'moveCursor'.
         * @param { function } [callback] - the callback of 'moveCursor',
         *     when subscriber unsubscribes all callback functions of event 'moveCursor', this parameter can be left blank.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        off(type: 'moveCursor', callback?: (direction: Direction) => void): void;
        /**
         * Register a callback and when IME sends extend action code, the callback will be invoked.
         *
         * @param { 'handleExtendAction' } type - event type, fixed as 'handleExtendAction'.
         * @param { function } callback - processes handleExtendAction command. The action code
         *     is provided for this callback.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
         * @throws { BusinessError } 12800009 - input method client detached.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        on(type: 'handleExtendAction', callback: (action: ExtendAction) => void): void;
        /**
         * Unregister the callback of handleExtendAction.
         *
         * @param { 'handleExtendAction' } type - event type, fixed as 'handleExtendAction'.
         * @param { function } [callback] - the callback of 'handleExtendAction',
         *     when subscriber unsubscribes all callback functions of event 'handleExtendAction', this parameter can be left
         *     blank.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        off(type: 'handleExtendAction', callback?: (action: ExtendAction) => void): void;
        /**
         * Register a callback and when input method ability gets left text of cursor, the callback will be invoked.
         *
         * @param { 'getLeftTextOfCursor' } type - event type, fixed as 'getLeftTextOfCursor'.
         * @param { function } callback - processes getLeftTextOfCursor command. The callback
         *     must be a synchronization method and will block the input method application.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
         * @throws { BusinessError } 12800009 - input method client detached.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        on(type: 'getLeftTextOfCursor', callback: (length: number) => string): void;
        /**
         * Unregister the callback of getLeftTextOfCursor event.
         *
         * @param { 'getLeftTextOfCursor' } type - event type, fixed as 'getLeftTextOfCursor'.
         * @param { function } [callback] - the callback of 'getLeftTextOfCursor',
         *     when subscriber unsubscribes all callback functions of event 'getLeftTextOfCursor', this parameter can be
         *     left blank.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        off(type: 'getLeftTextOfCursor', callback?: (length: number) => string): void;
        /**
         * Register a callback and when input method ability gets right text of cursor, the callback will be invoked.
         *
         * @param { 'getRightTextOfCursor' } type - event type, fixed as 'getRightTextOfCursor'.
         * @param { function } callback - processes getRightTextOfCursor command. The callback
         *     must be a synchronization method and will block the input method application.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
         * @throws { BusinessError } 12800009 - input method client detached.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        on(type: 'getRightTextOfCursor', callback: (length: number) => string): void;
        /**
         * Unregister the callback of getRightTextOfCursor event.
         *
         * @param { 'getRightTextOfCursor' } type - event type, fixed as 'getRightTextOfCursor'.
         * @param { function } [callback] - the callback of 'getRightTextOfCursor',
         *     when subscriber unsubscribes all callback functions of event 'getRightTextOfCursor', this parameter can be
         *     left blank.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        off(type: 'getRightTextOfCursor', callback?: (length: number) => string): void;
        /**
         * Register a callback and when input method ability gets the text index at cursor, the callback will be invoked.
         *
         * @param { 'getTextIndexAtCursor' } type - event type, fixed as 'getTextIndexAtCursor'.
         * @param { function } callback - processes getTextIndexAtCursor command. The callback
         *     must be a synchronization method, and should return the text index at the cursor.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.
         * @throws { BusinessError } 12800009 - input method client detached.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        on(type: 'getTextIndexAtCursor', callback: () => number): void;
        /**
         * Unregister the callback of getTextIndexAtCursor.
         *
         * @param { 'getTextIndexAtCursor' } type - event type, fixed as 'getTextIndexAtCursor'.
         * @param { function } [callback] - the callback of 'getTextIndexAtCursor',
         *     when subscriber unsubscribes all callback functions of event 'getTextIndexAtCursor', this parameter can be
         *     left blank.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        off(type: 'getTextIndexAtCursor', callback?: () => number): void;
        /**
         * <p>Subscribe 'setPreviewText' event.</p>
         * <p>To support the preview text feature, developers should subscribe to this event before calling attach.</p>
         *
         * @param { 'setPreviewText' } type - the type of subscribe event.
         * @param { SetPreviewTextCallback } callback - the callback of on('setPreviewText').
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 17
         */
        on(type: 'setPreviewText', callback: SetPreviewTextCallback): void;
        /**
         * Unsubscribe 'setPreviewText' event.
         *
         * @param { 'setPreviewText' } type - the type of unsubscribe event.
         * @param { SetPreviewTextCallback } [callback] - optional, the callback of off('setPreviewText').
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 17
         */
        off(type: 'setPreviewText', callback?: SetPreviewTextCallback): void;
        /**
         * <p>Subscribe 'finishTextPreview' event.</p>
         * <p>To support the preview text feature, developers should subscribe to this event before calling attach.</p>
         *
         * @param { 'finishTextPreview' } type - the type of subscribe event.
         * @param { Callback<void> } callback - the callback of on('finishTextPreview').
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 17
         */
        on(type: 'finishTextPreview', callback: Callback<void>): void;
        /**
         * Unsubscribe 'finishTextPreview' event.
         *
         * @param { 'finishTextPreview' } type - the type of unsubscribe event.
         * @param { Callback<void> } [callback] - optional, the callback of off('finishTextPreview').
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 17
         */
        off(type: 'finishTextPreview', callback?: Callback<void>): void;
    }
    /**
     * input method property
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 8
     */
    interface InputMethodProperty {
        /**
         * The name of input method
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 8
         * @deprecated since 9
         * @useinstead inputMethod.InputMethodProperty#name
         */
        readonly packageName: string;
        /**
         * The id of input method
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 8
         * @deprecated since 9
         * @useinstead inputMethod.InputMethodProperty#id
         */
        readonly methodId: string;
        /**
         * The name of input method
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         */
        readonly name: string;
        /**
         * The id of input method
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         */
        readonly id: string;
        /**
         * The label of input method
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         */
        readonly label?: string;
        /**
         * The label id of input method
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        readonly labelId?: number;
        /**
         * The icon of input method
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         */
        readonly icon?: string;
        /**
         * The icon id of input method
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         */
        readonly iconId?: number;
        /**
         * The enabledState of input method
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 20
         */
        readonly enabledState?: EnabledState;
        /**
         * The extra info of input method
         *
         * @type { object } [since 9 - 9]
         * @type { ?object } [since 10]
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 9
         */
        extra?: object;
    }
    /**
     * Enumerates the moving direction of cursor
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 10
     */
    export enum Direction {
        /**
         * Cursor moves up
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        CURSOR_UP = 1,
        /**
         * Cursor moves down
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        CURSOR_DOWN,
        /**
         * Cursor moves left
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        CURSOR_LEFT,
        /**
         * Cursor moves right
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        CURSOR_RIGHT
    }
    /**
     * Range of selected text.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 10
     */
    export interface Range {
        /**
         * Indicates the index of the first character of the selected text.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        start: number;
        /**
         * Indicates the index of the last character of the selected text.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        end: number;
    }
    /**
     * Movement of cursor.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 10
     */
    export interface Movement {
        /**
         * Indicates the direction of cursor movement
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        direction: Direction;
    }
    /**
     * Enumerates the text input type.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 10
     */
    export enum TextInputType {
        /**
         * The text input type is NONE.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        NONE = -1,
        /**
         * The text input type is TEXT.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        TEXT = 0,
        /**
         * The text input type is MULTILINE.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        MULTILINE,
        /**
         * The text input type is NUMBER.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        NUMBER,
        /**
         * The text input type is PHONE.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        PHONE,
        /**
         * The text input type is DATETIME.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        DATETIME,
        /**
         * The text input type is EMAIL_ADDRESS.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        EMAIL_ADDRESS,
        /**
         * The text input type is URL.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        URL,
        /**
         * The text input type is VISIBLE_PASSWORD.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        VISIBLE_PASSWORD,
        /**
         * The text input type is NUMBER_PASSWORD.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 11
         */
        NUMBER_PASSWORD,
        /**
         * The text input type is SCREEN_LOCK_PASSWORD.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 20
         */
        SCREEN_LOCK_PASSWORD,
        /**
         * The text input type is USER_NAME.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 20
         */
        USER_NAME,
        /**
         * The text input type is NEW_PASSWORD.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 20
         */
        NEW_PASSWORD,
        /**
         * The text input type is NUMBER_DECIMAL.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 20
         */
        NUMBER_DECIMAL,
        /**
         * The text input type is ONE_TIME_CODE.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 20
         */
        ONE_TIME_CODE
    }
    /**
     * Enumerates the enter key type.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 10
     */
    export enum EnterKeyType {
        /**
         * The enter key type is UNSPECIFIED.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        UNSPECIFIED = 0,
        /**
         * The enter key type is NONE.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        NONE,
        /**
         * The enter key type is GO.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        GO,
        /**
         * The enter key type is SEARCH.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        SEARCH,
        /**
         * The enter key type is SEND.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        SEND,
        /**
         * The enter key type is NEXT.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        NEXT,
        /**
         * The enter key type is DONE.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        DONE,
        /**
         * The enter key type is PREVIOUS.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        PREVIOUS,
        /**
         * The enter key type is NEWLINE.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 12
         */
        NEWLINE
    }
    /**
     * Enumerates the keyboard status.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 10
     */
    export enum KeyboardStatus {
        /**
         * The keyboard status is none.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        NONE = 0,
        /**
         * The keyboard status is hide.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        HIDE = 1,
        /**
         * The keyboard status is show.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        SHOW = 2
    }
    /**
     * Attribute of Input.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 10
     */
    export interface InputAttribute {
        /**
         * Indicates the text input type of the input method.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        textInputType: TextInputType;
        /**
         * Indicates the enter key type of the input method.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        enterKeyType: EnterKeyType;
        /**
         * Placeholder text in the edit box.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 20
         */
        placeholder?: string;
        /**
         * The name of the ability where the edit box is located.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 20
         */
        abilityName?: string;
        /**
         * Whether the editor supports consuming key events.
         *
         * @default false
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @stagemodelonly
         * @since 26.0.0
         */
        consumeKeyEvents?: boolean;
    }
    /**
     * FunctionKey of Input.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 10
     */
    export interface FunctionKey {
        /**
         * Indicates the enter key type of the input method.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        enterKeyType: EnterKeyType;
    }
    /**
     * Information of Cursor.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 10
     */
    export interface CursorInfo {
        /**
         * Indicates the left point of the cursor info and must be absolute coordinate of the physical screen, unit is px.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        left: number;
        /**
         * Indicates the top point of the cursor info and must be absolute coordinate of the physical screen, unit is px.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        top: number;
        /**
         * Indicates the width point of the cursor info, unit is px.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        width: number;
        /**
         * Indicates the height point of the cursor info, unit is px.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        height: number;
        /**
         * Indicates the ID of the display where the cursor locates.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @stagemodelonly
         * @since 26.0.0
         */
        displayId?: number;
    }
    /**
     * Config of editor.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 10
     */
    export interface TextConfig {
        /**
         * Attribute of Input.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        inputAttribute: InputAttribute;
        /**
         * Cursor information.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        cursorInfo?: CursorInfo;
        /**
         * Selection information.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        selection?: Range;
        /**
         * The window ID of the application currently bound to the input method.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        windowId?: number;
        /**
         * Indicates that this is a new edit box.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 20
         */
        newEditBox?: boolean;
        /**
         * Indicates the capitalize mode of the edit box.
         *
         * @default CapitalizeMode.NONE
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 20
         */
        capitalizeMode?: CapitalizeMode;
    }
    /**
     * Enumerates the extend action.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 10
     */
    export enum ExtendAction {
        /**
         * Select all text.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        SELECT_ALL = 0,
        /**
         * Cut selecting text.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        CUT = 3,
        /**
         * Copy selecting text.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        COPY = 4,
        /**
         * Paste from paste board.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        PASTE = 5
    }
    /**
     * Information of input window.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 10
     */
    export interface InputWindowInfo {
        /**
         * Indicates name of the input window.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        name: string;
        /**
         * Indicates the abscissa of the upper-left vertex of input window, unit is px.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        left: number;
        /**
         * Indicates the ordinate of the upper-left vertex of input window, unit is px.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        top: number;
        /**
         * Indicates the width of the input window, unit is px.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        width: number;
        /**
         * Indicates the height of the input window, unit is px.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 10
         */
        height: number;
        /**
         * Indicates the id of the display where the input window is shown.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @stagemodelonly
         * @since 23
         */
        displayId?: number;
    }
    /**
     * <p>Custom message handler.</p>
     * <p>Implement this interface to respond to custom messages.</p>
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 15
     */
    interface MessageHandler {
        /**
         * This method is called when a custom message is received.
         *
         * @param { string } msgId - the identifier of the message.
         * @param { ArrayBuffer } [msgParam] - the parameter of the custom message.
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 15
         */
        onMessage(msgId: string, msgParam?: ArrayBuffer): void;
        /**
         * This method is called when a new message handler is set.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 15
         */
        onTerminated(): void;
    }
    /**
     * Enumerates the enabled state.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 15
     */
    export enum EnabledState {
        /**
         * Disabled state.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 15
         */
        DISABLED = 0,
        /**
         * Enabled state with basic mode.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 15
         */
        BASIC_MODE,
        /**
         * Enabled state with full experience mode.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 15
         */
        FULL_EXPERIENCE_MODE
    }
    /**
     * requestKeyboardReason of input click
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 15
     */
    export enum RequestKeyboardReason {
        /**
         * The request keyboard reason is NONE.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 15
         */
        NONE = 0,
        /**
         * The request keyboard reason is MOUSE.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 15
         */
        MOUSE = 1,
        /**
         * The request keyboard reason is TOUCH.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 15
         */
        TOUCH = 2,
        /**
         * The request keyboard reason is OTHER.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 15
         */
        OTHER = 20
    }
    /**
     * The callback of 'setPreviewText' event.
     *
     * @param { string } text - text to be previewed.
     * @param { Range } range - the range of the text to be replaced by the preview text.
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 17
     */
    export type SetPreviewTextCallback = (text: string, range: Range) => void;
    /**
      * Enumerates the capitalization mode.
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
    /**
     * Enumerates the specific reasons for attachment failure
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 22
     */
    export enum AttachFailureReason {
        /**
         * The attachment failure reason is CALLER_NOT_FOCUSED.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 22
         */
        CALLER_NOT_FOCUSED = 0,
        /**
         * The attachment failure reason is IME_ABNORMAL.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 22
         */
        IME_ABNORMAL,
        /**
         * The attachment failure reason is SERVICE_ABNORMAL.
         *
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @since 22
         */
        SERVICE_ABNORMAL
    }
    /**
     * Attach options.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @stagemodelonly
     * @since 23
     */
    export interface AttachOptions {
        /**
         * Whether to show the keyboard when attaching.
         *
         * @default true
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @stagemodelonly
         * @since 23
         */
        showKeyboard?: boolean;
        /**
         * The reason for request keyboard.
         *
         * @default RequestKeyboardReason.NONE
         * @syscap SystemCapability.MiscServices.InputMethodFramework
         * @stagemodelonly
         * @since 23
         */
        requestKeyboardReason?: RequestKeyboardReason;
    }
}
export default inputMethod;

```
