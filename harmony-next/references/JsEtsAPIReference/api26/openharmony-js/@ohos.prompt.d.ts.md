# @ohos.prompt.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2021 Huawei Device Co., Ltd.
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
 * @kit ArkUI
 */
import { AsyncCallback } from './@ohos.base';
/**
 * @namespace prompt
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @FaAndStageModel
 * @since 8
 * @deprecated since 9
 * @useinstead ohos.promptAction/promptAction
 */
declare namespace prompt {
    /**
     * Defines the options of ShowToast.
     *
     * @interface ShowToastOptions
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @FaAndStageModel
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.promptAction/promptAction.ShowToastOptions
     */
    interface ShowToastOptions {
        /**
         * Text to display.
         *
         * @type { string }
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @FaAndStageModel
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.promptAction/promptAction.ShowToastOptions#message
         */
        message: string;
        /**
         * Duration of toast dialog box. The default value is 1500.
         * The recommended value ranges from 1500 ms to 10000ms.
         * NOTE: A value less than 1500 is automatically changed to 1500. The maximum value is 10000 ms.
         *
         * @type { ?number }
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @FaAndStageModel
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.promptAction/promptAction.ShowToastOptions#duration
         */
        duration?: number;
        /**
         * The distance between toast dialog box and the bottom of screen.
         *
         * @type { ?(string | number) }
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @FaAndStageModel
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.promptAction/promptAction.ShowToastOptions#bottom
         */
        bottom?: string | number;
    }
    /**
     * Defines the prompt info of button.
     *
     * @interface Button
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @FaAndStageModel
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.promptAction/promptAction.Button
     */
    interface Button {
        /**
         * Defines the button info.
         *
         * @type { string }
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @FaAndStageModel
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.promptAction/promptAction.Button#text
         */
        text: string;
        /**
         * Defines the color of button.
         *
         * @type { string }
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @FaAndStageModel
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.promptAction/promptAction.Button#color
         */
        color: string;
    }
    /**
     * Defines the response of ShowDialog.
     *
     * @interface ShowDialogSuccessResponse
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.promptAction/promptAction.ShowDialogSuccessResponse
     */
    interface ShowDialogSuccessResponse {
        /**
         * Defines the index of data.
         *
         * @type { number }
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @FaAndStageModel
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.promptAction/promptAction.ShowDialogSuccessResponse#index
         */
        index: number;
    }
    /**
     * Defines the option of show dialog.
     *
     * @interface ShowDialogOptions
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @FaAndStageModel
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.promptAction/promptAction.ShowDialogOptions
     */
    interface ShowDialogOptions {
        /**
         * Title of the text to display.
         *
         * @type { ?string }
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @FaAndStageModel
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.promptAction/promptAction.ShowDialogOptions#title
         */
        title?: string;
        /**
         * Text body.
         *
         * @type { ?string }
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @FaAndStageModel
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.promptAction/promptAction.ShowDialogOptions#message
         */
        message?: string;
        /**
         * Array of buttons in the dialog box.
         * The array structure is {text:'button', color: '#666666'}.
         * One to three buttons are supported. The first button is of the positiveButton type, the second is of the negativeButton type, and the third is of the neutralButton type.
         *
         * @type { ?[Button, Button?, Button?] }
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @FaAndStageModel
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.promptAction/promptAction.ShowDialogOptions#buttons
         */
        buttons?: [
            Button,
            Button?,
            Button?
        ];
    }
    /**
     * Defines the response of ShowActionMenu.
     *
     * @interface ActionMenuSuccessResponse
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.promptAction/promptAction.ActionMenuSuccessResponse
     */
    interface ActionMenuSuccessResponse {
        /**
         * Defines the index of data.
         *
         * @type { number }
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @FaAndStageModel
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.promptAction/promptAction.ActionMenuSuccessResponse#index
         */
        index: number;
    }
    /**
     * Defines the option of ShowActionMenu.
     *
     * @interface ActionMenuOptions
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @FaAndStageModel
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.promptAction/promptAction.ActionMenuOptions
     */
    interface ActionMenuOptions {
        /**
         * Title of the text to display.
         *
         * @type { ?string }
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @FaAndStageModel
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.promptAction/promptAction.ActionMenuOptions#title
         */
        title?: string;
        /**
         * Array of buttons in the dialog box.
         * The array structure is {text:'button', color: '#666666'}.
         * One to six buttons are supported.
         *
         * @type { [Button, Button?, Button?, Button?, Button?, Button?] }
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @FaAndStageModel
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.promptAction/promptAction.ActionMenuOptions#buttons
         */
        buttons: [
            Button,
            Button?,
            Button?,
            Button?,
            Button?,
            Button?
        ];
    }
    /**
     * Displays the notification text.
     *
     * @param { ShowToastOptions } options - Options.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @FaAndStageModel
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.arkui.UIContext.PromptAction#showToast
     */
    function showToast(options: ShowToastOptions): void;
    /**
     * Displays the dialog box.
     *
     * @param { ShowDialogOptions } options - Options.
     * @param { AsyncCallback<ShowDialogSuccessResponse> } callback
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @FaAndStageModel
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.arkui.UIContext.PromptAction#showDialog
     */
    function showDialog(options: ShowDialogOptions, callback: AsyncCallback<ShowDialogSuccessResponse>): void;
    /**
     * Displays the dialog box.
     *
     * @param { ShowDialogOptions } options - Options.
     * @returns { Promise<ShowDialogSuccessResponse> }
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @FaAndStageModel
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.arkui.UIContext.PromptAction#showDialog
     */
    function showDialog(options: ShowDialogOptions): Promise<ShowDialogSuccessResponse>;
    /**
     * Displays the menu.
     *
     * @param { ActionMenuOptions } options - Options.
     * @param { AsyncCallback<ActionMenuSuccessResponse> } callback
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @FaAndStageModel
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.arkui.UIContext.PromptAction#showActionMenu
     */
    function showActionMenu(options: ActionMenuOptions, callback: AsyncCallback<ActionMenuSuccessResponse>): void;
    /**
     * Displays the menu.
     *
     * @param { ActionMenuOptions } options - Options.
     * @returns { Promise<ActionMenuSuccessResponse> }
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @FaAndStageModel
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.arkui.UIContext.PromptAction#showActionMenu
     */
    function showActionMenu(options: ActionMenuOptions): Promise<ActionMenuSuccessResponse>;
}
export default prompt;

```
