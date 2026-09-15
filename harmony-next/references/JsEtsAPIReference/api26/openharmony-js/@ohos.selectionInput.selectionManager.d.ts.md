# @ohos.selectionInput.selectionManager.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2025 Huawei Device Co., Ltd.
 * Licensed under the Apache License, Version 2.0 (the "License"),
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
 * @file Word Selection Management
 * @kit BasicServicesKit
 */
import type { Callback } from './@ohos.base';
import type Context from './application/Context';
import type { PanelInfo } from './@ohos.selectionInput.SelectionPanel';
/**
 * This module provides word selection management capabilities, including creating, displaying, moving, hiding, and
 * destroying panels, listening for word selection events using a mouse or touchpad, and retrieving the selected text.
 * The typical usage process is as follows:
 * 1. Call [on('selectionCompleted')]{@link selectionManager.on} to subscribe to the selection completion event.
 * 2. In the callback, call [getSelectionContent]{@link selectionManager.getSelectionContent} to obtain the selected text.
 * 3. Call [createPanel]{@link selectionManager.createPanel} to create a word selection panel.
 * 4. Call [setUiContent]{@link selectionManager.Panel.setUiContent} to load the page content.
 * 5. Call [moveToGlobalDisplay]{@link selectionManager.Panel.moveToGlobalDisplay} to move the panel to the specified position.
 * 6. Call [show]{@link selectionManager.Panel.show} to display the panel.
 * 7. Call [destroyPanel]{@link selectionManager.destroyPanel} to destroy the panel.
 * 8. Call [off('selectionCompleted')]{@link selectionManager.off} to unsubscribe from the selection completion event.
 *
 * > **NOTE**
 * >
 * > - This module is supported only on PCs/2-in-1 devices. You can use
 * > **canIUse('SystemCapability.SelectionInput.Selection')** to check whether the current device supports this
 * > function.
 * > - APIs of this module can be called only by apps that integrate the extension ability for word selection. For
 * > details about how to implement the extension ability for word selection, see
 * > [SelectionExtensionAbility]{@link @ohos.selectionInput.SelectionExtensionAbility}.
 *
 * @syscap SystemCapability.SelectionInput.Selection
 * @stagemodelonly
 * @since 24
 */
declare namespace selectionManager {
    /**
     * Subscribes to the word selection completion event. This API is used together with
     * [off('selectionCompleted')]{@link selectionManager.off(type: 'selectionCompleted', callback?: Callback<SelectionInfo>)}.
     *
     * [off('selectionCompleted')]{@link selectionManager.off(type: 'selectionCompleted', callback?: Callback<SelectionInfo>)}
     * is used to unsubscribe from the event.
     *
     * @param { 'selectionCompleted' } type - Event type, which is **'selectionCompleted'**.
     * @param { Callback<SelectionInfo> } callback - Callback used to return
     *     [SelectionInfo]{@link selectionManager.SelectionInfo}. This callback is triggered only when the user selects
     *     text using the mouse or touchpad (by double-clicking, triple-clicking, or sliding the left mouse button) and
     *     then presses **Ctrl**.
     * @throws { BusinessError } 33600003 - The application calling the API does not match the application
     *     selected in the system settings.
     * @syscap SystemCapability.SelectionInput.Selection
     * @since 24
     */
    function on(type: 'selectionCompleted', callback: Callback<SelectionInfo>): void;
    /**
     * Unsubscribes from the word selection completion event. This API is used together with
     * [on('selectionCompleted')]{@link selectionManager.on(type: 'selectionCompleted', callback: Callback<SelectionInfo>)}.
     *
     * @param { 'selectionCompleted' } type - Type of the event to unsubscribe from. The value is fixed to
     *     **'selectionCompleted'**.
     * @param { Callback<SelectionInfo> } [callback] - Callback to be unregistered, which the callback instance
     *     registered using **on**. If this parameter is not specified, this API unregisters all callbacks for the specified
     *     type.
     * @syscap SystemCapability.SelectionInput.Selection
     * @since 24
     */
    function off(type: 'selectionCompleted', callback?: Callback<SelectionInfo>): void;
    /**
     * Obtains the content of the selected text. This API uses a promise to return the result. This API must be called in
     * the
     * [on('selectionCompleted')]{@link selectionManager.on(type: 'selectionCompleted', callback: Callback<SelectionInfo>)}
     * callback and is valid only after the word selection completion event is triggered.
     *
     * @returns { Promise<string> } Promise used to return the content of the selected text.
     * @throws { BusinessError } 33600001 - Selection service invocation exception.
     * @throws { BusinessError } 33600004 - The interface is called too frequently.
     * @throws { BusinessError } 33600005 - The interface is called at the wrong time.
     * @throws { BusinessError } 33600006 - The current application is prohibited from accessing content.
     * @throws { BusinessError } 33600007 - The length of selected content is out of range.
     * @throws { BusinessError } 33600008 - Getting the selected content times out.
     * @syscap SystemCapability.SelectionInput.Selection
     * @since 24
     */
    function getSelectionContent(): Promise<string>;
    /**
     * Creates a word selection panel, which is used to display the service-related operation UI or text processing
     * result. After the panel is used, call [destroyPanel]{@link selectionManager.destroyPanel} to destroy the panel and
     * release resources. This API uses a promise to return the result.
     *
     * Only one [MENU_PANEL]{@link @ohos.selectionInput.SelectionPanel:PanelType} and one
     * [MAIN_PANEL]{@link @ohos.selectionInput.SelectionPanel:PanelType} can be created for one word selection
     * application.
     *
     * @param { Context } ctx - Context that the current word selection panel depends on, which is provided by
     *     **SelectionExtensionAbility**.
     * @param { PanelInfo } info - Configuration information of the word selection panel, which is used to specify the
     *     panel type, position, width, and height. Only one **MENU_PANEL** and one **MAIN_PANEL** can be created for one
     *     word selection app.
     * @returns { Promise<Panel> } Promise used to return the **Panel** object created, which can be used to set, display,
     *     hide, and move the panel, and subscribe to events.
     * @throws { BusinessError } 33600001 - Selection service exception.
     * @throws { BusinessError } 33600003 - The application calling the API does not match the application
     *     selected in the system settings.
     * @syscap SystemCapability.SelectionInput.Selection
     * @stagemodelonly
     * @since 24
     */
    function createPanel(ctx: Context, info: PanelInfo): Promise<Panel>;
    /**
     * Destroys the word selection panel. This API is used together with [createPanel]{@link selectionManager.createPanel}
     * to destroy the panel object created by **createPanel()**. This API uses a promise to return the result.
     *
     * @param { Panel } panel - Word selection panel to destroy.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 33600001 - Selection service exception.
     * @syscap SystemCapability.SelectionInput.Selection
     * @stagemodelonly
     * @since 24
     */
    function destroyPanel(panel: Panel): Promise<void>;
    /**
     * Defines the information of a word selection event.
     *
     * @syscap SystemCapability.SelectionInput.Selection
     * @stagemodelonly
     * @since 24
     */
    interface SelectionInfo {
        /**
         * Word selection types.
         *
         * @default MOUSE_MOVE
         * @syscap SystemCapability.SelectionInput.Selection
         * @stagemodelonly
         * @since 24
         */
        selectionType: SelectionType;
        /**
         * X-coordinate of the screen where the word selection starts, in px.
         *
         * @syscap SystemCapability.SelectionInput.Selection
         * @stagemodelonly
         * @since 24
         */
        startDisplayX: number;
        /**
         * Y-coordinate of the screen where the word selection starts, in px.
         *
         * @syscap SystemCapability.SelectionInput.Selection
         * @stagemodelonly
         * @since 24
         */
        startDisplayY: number;
        /**
         * X-coordinate of the screen where the word selection ends, in px.
         *
         * @syscap SystemCapability.SelectionInput.Selection
         * @stagemodelonly
         * @since 24
         */
        endDisplayX: number;
        /**
         * Y-coordinate of the screen where the word selection ends, in px.
         *
         * @syscap SystemCapability.SelectionInput.Selection
         * @stagemodelonly
         * @since 24
         */
        endDisplayY: number;
        /**
         * X-coordinate of the window where the word selection starts, in px.
         *
         * @syscap SystemCapability.SelectionInput.Selection
         * @stagemodelonly
         * @since 24
         */
        startWindowX: number;
        /**
         * Y-coordinate of the window where the word selection starts, in px.
         *
         * @syscap SystemCapability.SelectionInput.Selection
         * @stagemodelonly
         * @since 24
         */
        startWindowY: number;
        /**
         * X-coordinate of the window where the word selection ends, in px.
         *
         * @syscap SystemCapability.SelectionInput.Selection
         * @stagemodelonly
         * @since 24
         */
        endWindowX: number;
        /**
         * Y-coordinate of the window where the word selection ends, in px.
         *
         * @syscap SystemCapability.SelectionInput.Selection
         * @stagemodelonly
         * @since 24
         */
        endWindowY: number;
        /**
         * ID of the screen where the window with selected words is located.
         *
         * @syscap SystemCapability.SelectionInput.Selection
         * @stagemodelonly
         * @since 24
         */
        displayID: number;
        /**
         * ID of the window where words are selected.
         *
         * @syscap SystemCapability.SelectionInput.Selection
         * @stagemodelonly
         * @since 24
         */
        windowID: number;
        /**
         * Bundle name of the application where words are selected.
         *
         * @syscap SystemCapability.SelectionInput.Selection
         * @stagemodelonly
         * @since 24
         */
        bundleName: string;
    }
    /**
     * Describes a **Panel** object, which is created using [createPanel]{@link selectionManager.createPanel}. This method can
     * be used to set, display, hide, and move the panel, as well as subscribe to events. It is applicable to scenarios
     * where a custom operation UI needs to be displayed to users after word selection is complete.
     *
     * @syscap SystemCapability.SelectionInput.Selection
     * @stagemodelonly
     * @since 24
     */
    interface Panel {
        /**
         * Sets the UI content for the current word selection panel, for example, to display translation results, search
         * suggestions, or custom action buttons. This API can be called only after a **Panel** instance is obtained by
         * calling [createPanel]{@link selectionManager.createPanel}. This API uses a promise to return the result.
         *
         * @param { string } path - Path of the page content to be set. This path is configured in the
         *     **resources/base/profile/main_pages.json** file of the project in the stage model. The FA model is not
         *     supported.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 33600001 - Selection service exception.
         * @throws { BusinessError } 33600002 - This selection window has been destroyed.
         * @syscap SystemCapability.SelectionInput.Selection
         * @stagemodelonly
         * @since 24
         */
        setUiContent(path: string): Promise<void>;
        /**
         * Shows the word selection panel. This API is used together with [hide]{@link selectionManager.Panel.hide}. This
         * API can be called only after a **Panel** instance is obtained by calling
         * [createPanel]{@link selectionManager.createPanel}. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 33600001 - Selection service exception.
         * @throws { BusinessError } 33600002 - This selection window has been destroyed.
         * @syscap SystemCapability.SelectionInput.Selection
         * @stagemodelonly
         * @since 24
         */
        show(): Promise<void>;
        /**
         * Hides the word selection panel. This API is used together with [show]{@link selectionManager.Panel.show}. This
         * API can be called only after a **Panel** instance is obtained by calling
         * [createPanel]{@link selectionManager.createPanel}. This API uses a promise to return the result. If this API is
         * not called proactively, the panel is automatically hidden when it loses focus.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 33600001 - Selection service exception.
         * @throws { BusinessError } 33600002 - This selection window has been destroyed.
         * @syscap SystemCapability.SelectionInput.Selection
         * @since 24
         */
        hide(): Promise<void>;
        /**
         * Sets whether the word selection panel can be dragged along with the mouse, touchpad, or touchscreen. The panel
         * automatically stops moving after the pointer is released. This API can be called only after a **Panel** instance
         * is obtained by calling [createPanel]{@link selectionManager.createPanel}. This API uses a promise to return the
         * result. This API must be called in the **onTouch** callback, and the event type must be **TouchType.Down**.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 33600001 - Selection service exception.
         * @throws { BusinessError } 33600002 - This selection window has been destroyed.
         * @syscap SystemCapability.SelectionInput.Selection
         * @stagemodelonly
         * @since 24
         */
        startMoving(): Promise<void>;
        /**
         * Moves the word selection panel to the specified coordinates in the global coordinates system of the screen. The
         * panel can be moved to an extended screen. This API can be called only after a **Panel** instance is obtained by
         * calling [createPanel]{@link selectionManager.createPanel}. This API uses a promise to return the result.
         *
         * @param { number } x - X-coordinate of the target position in the global coordinate system of the screen, in px. The
         *     upper left corner of the main screen is the origin of the global coordinate system, and the positive
         *     direction of the X axis is rightward. The x-coordinate of an extended screen may be negative, depending on
         *     the screen layout.
         * @param { number } y - Y-coordinate of the target position in the global coordinate system of the screen, in px. The
         *     upper left corner of the main screen is the origin of the global coordinate system, and the positive
         *     direction of the Y axis is downward. The y-coordinate of an extended screen may be negative, depending on the
         *     screen layout.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 33600001 - Selection service exception.
         * @throws { BusinessError } 33600002 - This selection window has been destroyed.
         * @syscap SystemCapability.SelectionInput.Selection
         * @stagemodelonly
         * @since 24
         */
        moveToGlobalDisplay(x: number, y: number): Promise<void>;
        /**
         * Subscribes to the word selection panel destruction event. This API is used together with
         * [off('destroyed')]{@link selectionManager.Panel.off(type: 'destroyed', callback?: Callback<void>)}. This API can
         * be called only after a **Panel** instance is obtained by calling
         * [createPanel]{@link selectionManager.createPanel}.
         *
         * @param { 'destroyed' } type - Event type, which is **'destroyed'**.
         * @param { Callback<void> } callback - Callback used to return the result, which is triggered when
         *     [destroyPanel]{@link selectionManager.destroyPanel} is called to destroy the panel.
         * @syscap SystemCapability.SelectionInput.Selection
         * @since 24
         */
        on(type: 'destroyed', callback: Callback<void>): void;
        /**
         * Unsubscribes from the word selection panel destruction event. This API is used together with
         * [on('destroyed')]{@link selectionManager.Panel.on(type: 'destroyed', callback: Callback<void>)}. This API can be
         * called only after a **Panel** instance is obtained by calling [createPanel]{@link selectionManager.createPanel}.
         *
         * @param { 'destroyed' } type - Type of the event to unsubscribe from. The value is fixed to **'destroyed'**.
         * @param { Callback<void> } [callback] - Callback to be unregistered, which the callback instance registered
         *     using **on**. If this parameter is not specified, this API unregisters all callbacks for the specified type.
         * @syscap SystemCapability.SelectionInput.Selection
         * @since 24
         */
        off(type: 'destroyed', callback?: Callback<void>): void;
        /**
         * Subscribes to the word selection panel hiding event. This API is used together with
         * [off('hidden')]{@link selectionManager.Panel.off(type: 'hidden', callback?: Callback<void>)}. This event is
         * triggered when the panel is hidden by calling [hide]{@link selectionManager.Panel.hide} or automatically hidden
         * when it loses focus. This API can be called only after a **Panel** instance is obtained by calling
         * [createPanel]{@link selectionManager.createPanel}.
         *
         * @param { 'hidden' } type - Event type, which is **'hidden'**.
         * @param { Callback<void> } callback - Callback used to return the result, which is triggered when the panel is
         *     hidden. The panel can be hidden by calling [hide]{@link selectionManager.Panel.hide} or automatically hidden
         *     when it loses focus.
         * @syscap SystemCapability.SelectionInput.Selection
         * @since 24
         */
        on(type: 'hidden', callback: Callback<void>): void;
        /**
         * Unsubscribes from the word selection panel hiding event. This API is used together with
         * [on('hidden')]{@link selectionManager.Panel.on(type: 'hidden', callback: Callback<void>)}. This API can be called
         * only after a **Panel** instance is obtained by calling [createPanel]{@link selectionManager.createPanel}.
         *
         * @param { 'hidden' } type - Type of the event to unsubscribe from. The value is fixed to **'hidden'**.
         * @param { Callback<void> } [callback] - Callback to be unregistered, which the callback instance registered
         *     using **on**. If this parameter is not specified, this API unregisters all callbacks for the specified type.
         * @syscap SystemCapability.SelectionInput.Selection
         * @since 24
         */
        off(type: 'hidden', callback?: Callback<void>): void;
    }
    /**
     * Enumerates the word selection types.
     *
     * | Name        | Value| Description              |
     * | ------------ | -- | ------------------ |
     * | MOUSE_MOVE | 1 | Word selection by sliding the mouse or touchpad. |
     * | DOUBLE_CLICK   | 2 | Word selection by double-clicking the mouse or touchpad. |
     * | TRIPLE_CLICK   | 3 | Word selection by triple-clicking the mouse or touchpad. |
     *
     * @syscap SystemCapability.SelectionInput.Selection
     * @stagemodelonly
     * @since 24
     */
    enum SelectionType {
        /**
         * Word selection by sliding the mouse or touchpad.
         *
         * @syscap SystemCapability.SelectionInput.Selection
         * @stagemodelonly
         * @since 24
         */
        MOUSE_MOVE = 1,
        /**
         * Word selection by double-clicking the mouse or touchpad.
         *
         * @syscap SystemCapability.SelectionInput.Selection
         * @stagemodelonly
         * @since 24
         */
        DOUBLE_CLICK = 2,
        /**
         * Word selection by triple-clicking the mouse or touchpad.
         *
         * @syscap SystemCapability.SelectionInput.Selection
         * @stagemodelonly
         * @since 24
         */
        TRIPLE_CLICK = 3
    }
}
export default selectionManager;

```
