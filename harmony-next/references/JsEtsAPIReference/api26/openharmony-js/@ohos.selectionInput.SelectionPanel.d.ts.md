# @ohos.selectionInput.SelectionPanel.d.ts

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
 * The text selection panel is an operation panel that pops up after a user selects text. This module is applicable when
 * quick operations such as translation and search need to be provided for the selected text. This helps developers
 * quickly integrate the text selection capability and improve user interaction experience. The panel adopts a two-level
 * architecture design. The menu panel (**MENU_PANEL**) is the level-1 panel, which displays the function entries (such
 * as translation and search) provided by the current app. The main panel (**MAIN_PANEL**) is the level-2 panel, which
 * pops up after a user taps a function button on the menu panel and displays the specific function result. This module
 * provides the attributes and types of the word selection panel. You can use [PanelInfo]{@link PanelInfo} to set the
 * position and size of the panel and use [PanelType]{@link PanelType} to specify the panel type.
 * [createPanel]{@link @ohos.selectionInput.selectionManager:selectionManager.createPanel} and
 * [show]{@link @ohos.selectionInput.selectionManager:selectionManager.Panel.show} are used to create and display the
 * word selection panel.
 *
 * > **NOTE**
 * >
 * > - This module is supported only on PCs/2-in-1 devices. You can use **canIUse('
 * > SystemCapability.SelectionInput.Selection')** to check whether the current device supports this function.
 *
 * @file Word Selection Panel
 * @kit BasicServicesKit
 */
/**
 * Defines attributes of the word selection panel, including its type, position, and size. You can specify the panel
 * type (menu panel or main panel) using **panelType**, set the coordinates of the upper left corner of the panel using
 * **x** and **y**, and set the panel size using **width** and **height**. These attributes collectively define the
 * display form of the panel.
 *
 * @syscap SystemCapability.SelectionInput.Selection
 * @stagemodelonly
 * @since 24
 */
export interface PanelInfo {
    /**
     * Word selection panel types, which include two options. For details, see [PanelType]{@link PanelType}.
     *
     * @default MENU_PANEL
     * @syscap SystemCapability.SelectionInput.Selection
     * @stagemodelonly
     * @since 24
     */
    panelType: PanelType;
    /**
     * X-coordinate of the upper left corner of the word selection panel, in px. The upper left corner of the main screen
     * is the origin, and the positive direction of the X axis is rightward. The value range is
     * [0, +∞). If a negative value is passed, the panel cannot be created.
     *
     * @syscap SystemCapability.SelectionInput.Selection
     * @stagemodelonly
     * @since 24
     */
    x: number;
    /**
     * Y-coordinate of the upper left corner of the word selection panel, in px. The upper left corner of the main screen
     * is the origin, and the positive direction of the Y axis is downward. The value range is
     * [0, +∞). If a negative value is passed, the panel cannot be created.
     *
     * @syscap SystemCapability.SelectionInput.Selection
     * @stagemodelonly
     * @since 24
     */
    y: number;
    /**
     * Width of the word selection panel, in px. The value range is (0, +∞). If **0** or a negative value is passed, the
     * panel cannot be created.
     *
     * @syscap SystemCapability.SelectionInput.Selection
     * @stagemodelonly
     * @since 24
     */
    width: number;
    /**
     * Height of the word selection panel, in px. The value range is (0, +∞). If **0** or a negative value is passed, the
     * panel cannot be created.
     *
     * @syscap SystemCapability.SelectionInput.Selection
     * @stagemodelonly
     * @since 24
     */
    height: number;
}
/**
 * Enumerates the word selection panel types, which defines the two-level architecture of the panel: menu panel (level 1)
 * and main panel (level 2).
 *
 * @syscap SystemCapability.SelectionInput.Selection
 * @stagemodelonly
 * @since 24
 */
export enum PanelType {
    /**
     * Menu panel, which serves as the level-1 panel to display the functions that the current app can provide, such as
     * translation and search.
     *
     * @syscap SystemCapability.SelectionInput.Selection
     * @stagemodelonly
     * @since 24
     */
    MENU_PANEL = 1,
    /**
     * Main panel, which serves as the level-2 panel and is displayed when a user taps a function button on the menu
     * panel. It displays specific content such as translation or search results.
     *
     * @syscap SystemCapability.SelectionInput.Selection
     * @stagemodelonly
     * @since 24
     */
    MAIN_PANEL = 2
}

```
