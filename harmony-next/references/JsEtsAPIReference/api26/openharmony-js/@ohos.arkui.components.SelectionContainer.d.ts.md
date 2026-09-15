# @ohos.arkui.components.SelectionContainer.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2026 Huawei Device Co., Ltd.
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
/**
 * Defines text join style for SelectionContainer.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 26.0.0
 */
export declare enum SelectionContainerTextJoinStyle {
    /**
     * Join text with line break (`\n`) between text nodes.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    NEWLINE = 0,
    /**
     * Join text directly without separator between text nodes.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    DIRECT = 1
}
/**
 * Defines selection menu options for SelectionContainer.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 26.0.0
 */
export interface SelectionContainerMenuOptions {
    /**
     * Called when the selection menu appears.
     * The callback parameter is the selected text concatenated in the visual order of Text components.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    onAppear?: Callback<string>;
    /**
     * Called when the selection menu disappears.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    onDisappear?: Callback<void>;
    /**
     * Called when the selection menu is displayed.
     * The callback parameter is the selected text concatenated in the visual order of Text components.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    onMenuShow?: Callback<string>;
    /**
     * Called when the selection menu is hidden.
     * The callback parameter is the selected text concatenated in the visual order of Text components.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    onMenuHide?: Callback<string>;
}
/**
 * Invoke upon clicking an item, capable of intercepting the default system menu execution behavior.
 *
 * @param { TextMenuItem } menuItem - current clicked menu item.
 * @param { string } value - selected text content.
 * @returns { boolean } Return true if the event is consumed; false otherwise.
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 26.0.0
 */
export type OnMenuItemClickWithTextCallback = (menuItem: TextMenuItem, value: string) => boolean;
/**
 * Defines custom edit menu options for SelectionContainer.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 26.0.0
 */
export interface SelectionContainerEditMenuOptions {
    /**
     * Passes the default menu, invokes before every display to generate a menu for triggering click events.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    onCreateMenu?: OnCreateMenuCallback;
    /**
     * Invoked upon clicking an item, capable of intercepting the default system menu execution behavior.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    onMenuItemClick?: OnMenuItemClickWithTextCallback;
    /**
     * Callback before displaying the menu when the selection text changes.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    onPrepareMenu?: OnPrepareMenuCallback;
}
/**
 * Describes the initialization options of the SelectionContainer component.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 26.0.0
 */
export interface SelectionContainerOptions {
    /**
     * SelectionContainer controller.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    controller: SelectionContainerController;
}
/**
 * Defines the controller of the SelectionContainer component.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 26.0.0
 */
export declare class SelectionContainerController {
    /**
     * Closes the custom or default selection menu of the SelectionContainer.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    closeSelectionMenu(): void;
    /**
     * Clears the current text selection of the SelectionContainer,
     * and closes the selection menu if it is currently shown.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    clearTextSelection(): void;
}
/**
 * Provides a SelectionContainer component interface.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 26.0.0
 */
export interface SelectionContainerInterface {
    /**
     * Defines the constructor of SelectionContainer.
     *
     * @param { SelectionContainerOptions } [value] - Initialization options of the component.
     * @returns { SelectionContainerAttribute }
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    (value?: SelectionContainerOptions): SelectionContainerAttribute;
}
/**
 * Defines the attributes of SelectionContainer.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 26.0.0
 */
export declare class SelectionContainerAttribute extends CommonMethod<SelectionContainerAttribute> {
    /**
     * Set whether to allow copy and where data can be copied.
     *
     * @param { Optional<CopyOptions> } value - copy option for selected text. Default value is CopyOptions.InApp.
     * @returns { SelectionContainerAttribute } returns the instance of the SelectionContainerAttribute.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    copyOption(value: Optional<CopyOptions>): SelectionContainerAttribute;
    /**
     * Set the caret color for selected text.
     *
     * @param { Optional<ResourceColor> } color - caret color.
     * @returns { SelectionContainerAttribute } returns the instance of the SelectionContainerAttribute.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    caretColor(color: Optional<ResourceColor>): SelectionContainerAttribute;
    /**
     * Set selected text background color.
     *
     * @param { Optional<ResourceColor> } color - selected text background color.
     * @returns { SelectionContainerAttribute } returns the instance of the SelectionContainerAttribute.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    selectedBackgroundColor(color: Optional<ResourceColor>): SelectionContainerAttribute;
    /**
     * Enable or disable haptic feedback.
     *
     * @param { Optional<boolean> } isEnabled - whether to enable haptic feedback. Default value is true.
     * @returns { SelectionContainerAttribute } returns the instance of the SelectionContainerAttribute.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    enableHapticFeedback(isEnabled: Optional<boolean>): SelectionContainerAttribute;
    /**
     * Set text join style for aggregated text in SelectionContainer.
     *
     * <p><strong>NOTE</strong>:
     * <br>This setting affects the string value used in callbacks such as onWillCopy and onCopy.
     * <br>It also affects built-in text menu item logic that depends on string concatenation, such as copy.
     * <br>The default style is SelectionContainerTextJoinStyle.NEWLINE.
     * </p>
     *
     * @param { Optional<SelectionContainerTextJoinStyle> } style - text join style for aggregated text.
     * @returns { SelectionContainerAttribute } returns the instance of the SelectionContainerAttribute.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    textJoinStyle(style: Optional<SelectionContainerTextJoinStyle>): SelectionContainerAttribute;
    /**
     * Bind to the selection menu.
     *
     * <p><strong>NOTE</strong>:
     * <br>The duration required for a long-press gesture is 600 ms for bindSelectionMenu and 800 ms for bindContextMenu.
     * <br>When both bindSelectionMenu and bindContextMenu are set and both are configured to be triggered by a
     *     long-press gesture, bindSelectionMenu is triggered first.
     * <br>If the custom menu is too long, embed a Scroll component to prevent the keyboard from being blocked.
     * </p>
     *
     * @param { Optional<TextSpanType> } spanType - Indicates the type of selection menu. Default value is
     *     TextSpanType.TEXT.
     * @param { Optional<CustomBuilder> } content - Indicates the content of selection menu.
     * @param { Optional<TextResponseType> } responseType - Indicates response type of selection menu. Default value is
     *     TextResponseType.LONG_PRESS.
     * @param { Optional<SelectionContainerMenuOptions> } [options] - Indicates the options of selection menu.
     * @returns { SelectionContainerAttribute } returns the instance of the SelectionContainerAttribute.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    bindSelectionMenu(spanType: Optional<TextSpanType>, content: Optional<CustomBuilder>, responseType: Optional<TextResponseType>, options?: Optional<SelectionContainerMenuOptions>): SelectionContainerAttribute;
    /**
     * Set the custom text menu.
     * Sets the extended options of the custom context menu on selection,
     * including the text content, icon, and callback.
     *
     * @param { Optional<SelectionContainerEditMenuOptions> } editMenu - Customize text menu options.
     * @returns { SelectionContainerAttribute } returns the instance of the SelectionContainerAttribute.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    editMenuOptions(editMenu: Optional<SelectionContainerEditMenuOptions>): SelectionContainerAttribute;
    /**
     * Called when text selection changes in SelectionContainer.
     *
     * @param { Optional<Callback<Array<string>>> } callback - callback of selection change event.
     *     The order of items in the first callback parameter array is consistent with the visual order of Text
     *     components.
     * @returns { SelectionContainerAttribute } returns the instance of the SelectionContainerAttribute.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    onTextSelectionChange(callback: Optional<Callback<Array<string>>>): SelectionContainerAttribute;
    /**
     * Called before using the Clipboard copy menu.
     * Currently, only text can be copied.
     *
     * @param { Optional<Callback<string, boolean>> } callback - callback used to check whether copy is allowed.
     *     The first callback parameter (string) is the selected text concatenated in the visual order of Text components.
     * @returns { SelectionContainerAttribute } returns the instance of the SelectionContainerAttribute.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    onWillCopy(callback: Optional<Callback<string, boolean>>): SelectionContainerAttribute;
    /**
     * Called when selected text is copied.
     * Currently, only text can be copied.
     *
     * @param { Optional<Callback<string>> } callback - callback of copy event.
     *     The callback parameter (string) is the selected text concatenated in the visual order of Text components.
     * @returns { SelectionContainerAttribute } returns the instance of the SelectionContainerAttribute.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    onCopy(callback: Optional<Callback<string>>): SelectionContainerAttribute;
}
/**
 * Defines SelectionContainer component.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @uicomponent
 * @since 26.0.0
 */
export declare const SelectionContainer: SelectionContainerInterface;
/**
 * Defines SelectionContainer component instance.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 26.0.0
 */
export declare const SelectionContainerInstance: SelectionContainerAttribute;

```
