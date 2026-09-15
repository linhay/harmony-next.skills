# @ohos.promptAction.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2021-2023 Huawei Device Co., Ltd.
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
 * Enumerates the display level modes of the dialog box.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 15
 */
export enum LevelMode {
    /**
     * The dialog box is displayed at the root node level of the application window and remains visible during navigation.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 15
     */
    OVERLAY = 0,
    /**
     * The dialog box is a child of the page's route/navigation and is hidden when the page is hidden.
     * <br>**NOTE**
     * <br>1. Currently, the dialog box can only be mounted to a **Page** or
     * [NavDestination](./arkui-ts/ts-basic-components-navdestination.md) node, with **Page** nodes taking precedence.
     * The dialog box is displayed only on top of these two page types.
     * <br>2. In this mode, new pages can be displayed over the dialog box. When users return to the previous page,
     * the dialog box remains visible and its content is preserved.
     * <br>3. In this mode, you must ensure that the target page node, such as the **Page** node, has been attached to
     * the tree before bringing up the dialog box; otherwise, the dialog box will not be able to be attached to the
     * corresponding page node.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 15
     */
    EMBEDDED = 1
}
/**
 * Enumerates the display area modes of the dialog box overlay within a page.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 15
 */
export enum ImmersiveMode {
    /**
     * The dialog box overlay follows the layout constraints of its parent node.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 15
     */
    DEFAULT = 0,
    /**
     * The dialog box overlay can extend to cover the status bar and navigation bar for a more immersive look.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 15
     */
    EXTEND = 1
}
/**
 * Defines the display order of a dialog box.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 18
 */
export class LevelOrder {
    /**
     * Creates a dialog box level with the specified order.
     *
     * @param { number } order - Display order of the dialog box. The value range is [-100000.0, +100000.0].
     *      Values outside this range are clamped to the nearest limit.
     * @returns { LevelOrder } Current instance.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    static clamp(order: number): LevelOrder;
    /**
     * Obtains the display order of this dialog box.
     *
     * @returns { number } Display order of the dialog box.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    getOrder(): number;
}
/**
 * This module provides API for creating and displaying toasts, dialog boxes, and action menus.
 *
 * > **NOTE**
 * >
 * > - This module cannot be used in the file declaration of the [UIAbility]{@link @ohos.app.ability.UIAbility}. In
 * > other words, the APIs of this module can be used only after a component instance is created; they cannot be called
 * > in the lifecycle of the UIAbility.
 * >
 * > - The functionality of this module depends on UI context. This means that the APIs of this module cannot be used
 * > where [the UI context is ambiguous](docroot://ui/arkts-global-interface.md#ambiguous-ui-context). For details, see
 * > [UIContext]{@link @ohos.arkui.UIContext}. It is recommended that you use the dialog box APIs provided by
 * > **UIContext**<!--Del-->, except for UI-less scenarios such as
 * > [ServiceExtensionAbility](docroot://application-models/serviceextensionability-sys.md)<!--DelEnd-->.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @FaAndStageModel
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare namespace promptAction {
    /**
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @FaAndStageModel
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    interface ShowToastOptions {
        /**
         * Text to display.
         * <br>**NOTE**
         * <br>The default font is **'Harmony Sans'**. Other fonts are not supported.<br>
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @FaAndStageModel
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        message: string | Resource;
        /**
         * Duration that the toast will remain on the screen.<br>Default value: 1500 ms.<br>
         * Value range: [1500, 10000].<br>
         * If a value less than 1500 ms is set, the default value is used. If the value greater than 10000 ms is set,
         * the upper limit 10000 ms is used.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @FaAndStageModel
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        duration?: number;
        /**
         * Distance from the bottom of the toast to the navigation bar. If the soft keyboard is raised and
         * the **bottom** value is too small, the toast will automatically avoid being blocked by the soft keyboard by
         * moving up 80 vp above it.<br>
         * Default value: **80vp**<br>
         * **NOTE**<br>
         * When there is no navigation bar at the bottom, **bottom** sets the distance from the bottom of the toast to
         * the bottom of the window.<br>If the **alignment** property is set, **bottom** will not take effect.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @FaAndStageModel
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        bottom?: string | number;
        /**
         * Display level mode of the toast.<br>
         * Default value: **ToastShowMode.DEFAULT**, which means to show the toast in the application.
         *
         * @default ToastShowMode.DEFAULT
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 11
         */
        showMode?: ToastShowMode;
        /**
         * Alignment mode.<br>
         * Default value: **undefined**. If **alignment** is not set and a navigation bar or soft keyboard is present,
         * the toast is automatically adjusted according to the position of the navigation bar or soft keyboard.
         * For details, see the description of **bottom**.<br>
         * **NOTE**<br>
         * The figure below shows the position of the toast in different alignment modes.<br>
         * ![en-us_image_0001](figures/toast_alignment.PNG)<br>
         * The text display of the toast is always left-aligned; other alignment modes are not supported.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        alignment?: Alignment;
        /**
         * Offset in the specified alignment mode.<br>
         * Default value: **{ dx: 0, dy: 0 }**, indicating no offset<br>
         * **NOTE**<br>
         * Only values in units of px are supported. Values in other units must be converted to units of px before being
         * passed in. For example, to set a value in vp, convert it to px first and then pass the converted value.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        offset?: Offset;
        /**
         * Background color of the toast.<br>
         * Default value: **Color.Transparent**.<br>
         * **NOTE**<br>
         * The background color will be visually combined with the blur effect when both properties are set.
         * If the resulting effect does not match your design requirements, you can disable the blur effect entirely
         * by explicitly setting the **backgroundBlurStyle** property to **BlurStyle.NONE**.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        backgroundColor?: ResourceColor;
        /**
         * Text color of the toast.<br>Default value: **Color.Black**.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        textColor?: ResourceColor;
        /**
         * Background blur style of the toast.<br>
         * Default value: **BlurStyle.COMPONENT_ULTRA_THICK**<br>
         * **NOTE**<br>
         * Setting this parameter to **BlurStyle.NONE** disables the background blur. When **backgroundBlurStyle** is set
         *  to a value other than **NONE**, do not set **backgroundColor**. If you do, the color display may not produce
         *  the expected visual effect.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        backgroundBlurStyle?: BlurStyle;
        /**
         * Shadow of the toast background.<br>
         * Default value: **ShadowStyle.OUTER_DEFAULT_MD**
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        shadow?: ShadowOptions | ShadowStyle;
        /**
         * Whether to respond when the device is in semi-folded mode. The value **true** means to respond when the device
         *  is in semi-folded mode.<br>
         * Default value: **false**, meaning not to respond when the device is in semi-folded mode.
         *
         * @default false
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 14
         */
        enableHoverMode?: boolean;
        /**
         * Display area of the toast in the hover state.<br>
         * Default value: **HoverModeAreaType.BOTTOM_SCREEN**, indicating that the toast is displayed in the lower half screen
         *
         * @default HoverModeAreaType.BOTTOM_SCREEN
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 14
         */
        hoverModeArea?: HoverModeAreaType;
        /**
         * Set system-styled materials for toast. Different materials have different effects, which can influence
         * backgroundColor, border, shadow, and other visual attributes of toast.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 26.0.0
         */
        systemMaterial?: SystemUiMaterial;
    }
    /**
     * Enumerates display modes for toasts. By default, the toast is displayed within the application and supports display in subwindows.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 11
     */
    export enum ToastShowMode {
        /**
         * The toast is displayed within the application.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 11
         */
        DEFAULT = 0,
        /**
         * The toast is displayed in a subwindow.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 11
         */
        TOP_MOST = 1
    }
    /**
     * Describes the menu item button in the action menu.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @FaAndStageModel
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    interface Button {
        /**
         * Button text.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @FaAndStageModel
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        text: string | Resource;
        /**
         * Text color of the button.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @FaAndStageModel
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        color: string | Resource;
        /**
         * Whether the button responds to the **Enter** key by default when the dialog box has focus and the **Tab** key
         *  is not pressed for sequential focus navigation. If there are multiple buttons, set this parameter to **true**
         * for only one button. Otherwise, no button will respond. Multiple dialog boxes can automatically gain focus and
         *  respond to user interactions in a sequential manner. **true**: The button responds to the **Enter** key by default.
         *  **false**: The button does not respond to the **Enter** key by default.<br>Default value: **false**.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        primary?: boolean;
    }
    /**
     * Describes the dialog box response result.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @FaAndStageModel
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    interface ShowDialogSuccessResponse {
        /**
         * Index of the selected button in the **buttons** array, starting from **0**.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @FaAndStageModel
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        index: number;
    }
    /**
     * Describes the options for showing the dialog box.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @FaAndStageModel
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    interface ShowDialogOptions {
        /**
         * Title of the dialog box.<br>Default value: **undefined**, which indicates that no title is not displayed by default.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @FaAndStageModel
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        title?: string | Resource;
        /**
         * Text body.<br>Default value: **undefined**, which indicates that no content is displayed by default.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @FaAndStageModel
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        message?: string | Resource;
        /**
         * Array of buttons in the dialog box.
         * The array structure is {text:'button',&nbsp;color:&nbsp;'\#666666'}. More than one button is supported.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @FaAndStageModel
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        buttons?: Array<Button>;
        /**
         * Mask area of the dialog box. Events within the mask area are blocked, while events outside the mask area are
         * transmitted.<br>
         * Default value: **{ x: 0, y: 0, width: '100%', height: '100%' }**<br>
         * **NOTE**<br>
         * **maskRect** does not take effect when **showInSubWindow** is set to **true**.<br>
         * If only some properties in [Rectangle](arkui-ts/ts-methods-alert-dialog-box.md#rectangle8) are set, the unset
         * properties default to 0.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice [since 11]
         * @since 10
         */
        maskRect?: Rectangle;
        /**
         * Alignment mode of the dialog box in the vertical direction.<br>
         * Default value: **DialogAlignment.Default**<br>
         * **NOTE**<br>
         * If **showInSubWindow** is set to **true** in **UIExtension**, the dialog box is aligned with the host window
         * based on **UIExtension**.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice [since 11]
         * @since 10
         */
        alignment?: DialogAlignment;
        /**
         * Offset of the dialog box relative to the alignment position.<br>
         * Default value: **{&nbsp;dx:&nbsp;0&nbsp;,&nbsp;dy:&nbsp;0&nbsp;}**
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice [since 11]
         * @since 10
         */
        offset?: Offset;
        /**
         * Whether to show the dialog box in a subwindow when the dialog box needs to be displayed outside the main window.
         * <br>**true**: The dialog box is shown in a subwindow.
         * <br>**false** (default): The dialog box is displayed within the application, not in a separate subwindow.
         * <br>Note: A dialog box whose **showInSubWindow** attribute is **true** cannot trigger the display of another
         * dialog box whose **showInSubWindow** attribute is also **true**.
         *
         * @default false
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        showInSubWindow?: boolean;
        /**
         * Whether the dialog box is a modal, which has a mask applied and does not allow for interaction with other
         * components around the dialog box.
         * <br>**true**: The dialog box is a modal.
         * <br>**false**: The dialog box is not a modal.
         * <br>Default value: **true**.
         *
         * @default true
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        isModal?: boolean;
        /**
         * Background color of the dialog box.
         * <br>Default value: **Color.Transparent**.
         * <br>**NOTE**
         * <br>The background color will be visually combined with the blur effect when both properties are set.
         * If the resulting effect does not match your design requirements, you can disable the blur effect entirely
         * by explicitly setting the **backgroundBlurStyle** property to **BlurStyle.NONE**.
         *
         * @default Color.Transparent
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        backgroundColor?: ResourceColor;
        /**
         * Background blur style of the dialog box.
         * <br>Default value: **BlurStyle.COMPONENT_ULTRA_THICK**
         * <br>**NOTE**
         * <br>Setting this parameter to **BlurStyle.NONE** disables the background blur.
         * When **backgroundBlurStyle** is set to a value other than **NONE**, do not set **backgroundColor**.
         * If you do, the color display may not produce the expected visual effect.
         *
         * @default BlurStyle.COMPONENT_ULTRA_THICK
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        backgroundBlurStyle?: BlurStyle;
        /**
         * Options for customizing the background blur style. For details about the default value, see **BackgroundBlurStyleOptions**.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 19
         */
        backgroundBlurStyleOptions?: BackgroundBlurStyleOptions;
        /**
         * Options for customizing the background effect. For details about the default value, see **BackgroundEffectOptions**.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 19
         */
        backgroundEffect?: BackgroundEffectOptions;
        /**
         * Shadow of the dialog box.
         * <br> Default value on 2-in-1 devices: **ShadowStyle.OUTER_FLOATING_MD** when the dialog box is focused
         * and **ShadowStyle.OUTER_FLOATING_SM** otherwise On other devices, the dialog box has no shadow by default.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        shadow?: ShadowOptions | ShadowStyle;
        /**
         * Whether to respond when the device is in semi-folded mode. The value **true** means to respond when the device
         *  is in semi-folded mode.
         * <br>Default value: **false**, meaning not to respond when the device is in semi-folded mode.
         * <br>**NOTE**
         * <br>For a PC or 2-in-1 device, the prompt is displayed on the upper half of the screen by default
         * when **enableHoverMode** is set to **true**. You can set **hoverModeArea** to display the prompt on the lower
         * half of the screen. For other devices, the prompt is displayed on the lower half of the screen by default
         * when **enableHoverMode** is set to **true**. You can set **hoverModeArea** to display the prompt on the upper
         * half of the screen.
         *
         * @default false
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 14
         */
        enableHoverMode?: boolean;
        /**
         * Default display area of the dialog box in semi-folded mode.
         * <br>Default value: **HoverModeAreaType.BOTTOM_SCREEN**
         *
         * @default HoverModeAreaType.BOTTOM_SCREEN
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 14
         */
        hoverModeArea?: HoverModeAreaType;
        /**
         * Callback invoked after the dialog box appears.
         * <br>**NOTE**
         * <br>1. The normal timing sequence is as follows: onWillAppear > onDidAppear > onWillDisappear > onDidDisappear.
         * <br>2. You can set the callback event for changing the dialog box display effect in **onDidAppear**.
         * The settings take effect next time the dialog box appears.
         * <br>3. When a dialog box is dismissed immediately after being shown, **onWillDisappear** may be triggered before **onDidAppear**.
         * <br>4. If the dialog box is dismissed before its appearance animation is finished, the animation will be
         * interrupted, and **onDidAppear** will not be invoked.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 19
         */
        onDidAppear?: Callback<void>;
        /**
         * Callback invoked after the dialog box disappears.
         * <br>**NOTE**
         * <br>1. The normal timing sequence is as follows: onWillAppear > onDidAppear > onWillDisappear > onDidDisappear.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 19
         */
        onDidDisappear?: Callback<void>;
        /**
         * Callback invoked before the dialog box appearance animation.
         * <br>**NOTE**
         * <br>1. The normal timing sequence is as follows: onWillAppear > onDidAppear > onWillDisappear > onDidDisappear.
         * <br>2. You can set the callback event for changing the dialog box display effect in **onWillAppear**.
         * The settings take effect next time the dialog box appears.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 19
         */
        onWillAppear?: Callback<void>;
        /**
         * Callback invoked before the dialog box disappearance animation.
         * <br>**NOTE**
         * <br>1. The normal timing sequence is as follows: onWillAppear > onDidAppear > onWillDisappear > onDidDisappear.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 19
         */
        onWillDisappear?: Callback<void>;
        /**
         * Display level of the dialog box.
         * <br>**NOTE**
         * <br>- Default value: **LevelMode.OVERLAY**
         * <br>- This parameter takes effect only when **showInSubWindow** is set to **false**.
         *
         * @default LevelMode.OVERLAY
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 15
         */
        levelMode?: LevelMode;
        /**
         * [Unique ID](js-apis-arkui-frameNode.md#getuniqueid12) of the node under the display level for the page-level dialog box.
         * <br>Value range: a number no less than 0<br>**NOTE**
         * <br>- This parameter takes effect only when **levelMode** is set to **LevelMode.EMBEDDED**.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 15
         */
        levelUniqueId?: number;
        /**
         * Overlay effect for the page-level dialog box.
         * <br>**NOTE**
         * <br>- Default value: **ImmersiveMode.DEFAULT**
         * <br>- This parameter takes effect only when **levelMode** is set to **LevelMode.EMBEDDED**.
         *
         * @default ImmersiveMode.DEFAULT
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 15
         */
        immersiveMode?: ImmersiveMode;
        /**
         * Display order of the dialog box.
         * <br>**NOTE**
         * <br>- Default value: **LevelOrder.clamp(0)**
         * <br>- Dynamic updating is not supported.
         *
         * @default The value returned by LevelOrder.clamp(0)
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        levelOrder?: LevelOrder;
        /**
         * System material of the dialog box. Different materials have different effects and can affect visual attributes
         *  such as the background color, border, and shadow of the dialog box.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 26.0.0
         */
        systemMaterial?: SystemUiMaterial;
    }
    /**
     * Enumerates states of the custom dialog box.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 20
     */
    enum CommonState {
        /**
         * State before the controller is bound to the dialog box.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        UNINITIALIZED = 0,
        /**
         * State after the controller is bound to the dialog box.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        INITIALIZED = 1,
        /**
         * State during the dialog box appearance animation.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        APPEARING = 2,
        /**
         * State after the dialog display appearance ends.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        APPEARED = 3,
        /**
         * State during the dialog box disappearance animation.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        DISAPPEARING = 4,
        /**
         * State after the dialog box disappearance animation ends.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        DISAPPEARED = 5
    }
    /**
     * Implements a common controller for managing components related to **promptAction**.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    class CommonController {
        /**
         * A constructor used to create a controller instance.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        constructor();
        /**
         * Closes the custom dialog box. If the dialog box is already closed, this API has no effect.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        close(): void;
        /**
         * Obtains the state of the custom dialog box.
         *
         * @returns { CommonState } State of the custom dialog box.
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        getState(): CommonState;
    }
    /**
     * Implements a custom dialog controller that inherits from [CommonController](#commoncontroller18).
     *
     * It can be used as a member variable of **UIContext** to display custom dialog boxes. For specific usage,
     * see the examples for [openCustomDialogWithController](arkts-apis-uicontext-promptaction.md#opencustomdialogwithcontroller18)
     * and [presentCustomDialog](arkts-apis-uicontext-promptaction.md#presentcustomdialog18).
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    class DialogController extends CommonController {
    }
    /**
     * Defines the options of the dialog box.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice [since 12]
     * @since 11
     */
    interface BaseDialogOptions {
        /**
         * Mask area.
         * <br>Default value: **{ x: 0, y: 0, width: '100%', height: '100%' }**
         * <br>**NOTE**
         * <br>**maskRect** does not take effect when **showInSubWindow** is set to **true**.
         * <br>If only some properties in [Rectangle](arkui-ts/ts-methods-alert-dialog-box.md#rectangle8) are set,
         * the unset properties default to 0.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        maskRect?: Rectangle;
        /**
         * Alignment mode of the dialog box in the vertical direction.
         * <br>Default value: **DialogAlignment.Default**
         * <br>**NOTE**
         * <br>If **showInSubWindow** is set to **true** in **UIExtension**, the dialog box is aligned with the host window based on **UIExtension**.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        alignment?: DialogAlignment;
        /**
         * Offset of the dialog box based on the **alignment** settings.
         * <br>Default value: **{&nbsp;dx:&nbsp;0&nbsp;,&nbsp;dy:&nbsp;0&nbsp;}**
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        offset?: Offset;
        /**
         * Whether to show the dialog box in a subwindow when the dialog box needs to be displayed outside the main window.
         * <br>**true**: The dialog box is shown in a subwindow.
         * <br>Default value: **false**, meaning the dialog box is displayed within the application, not in a separate subwindow
         *
         * @default false
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        showInSubWindow?: boolean;
        /**
         * Defines the dialog display mode when show in subwindow.
         *
         * @default DialogDisplayMode.SCREEN_BASED
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 26.0.0
         */
        displayModeInSubWindow?: DialogDisplayMode;
        /**
         * Whether the dialog box is a modal, which has a mask applied and does not allow for interaction with other
         * components around the dialog box.
         * <br>**true**: The dialog box is a modal.
         * <br>**false**: The dialog box is not a modal.
         * <br>Default value: **true**.
         *
         * @default true
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        isModal?: boolean;
        /**
         * Whether to dismiss the dialog box when the mask is touched. The value **true** means to dismiss the dialog
         * box when the mask is touched, and **false** means the opposite.<br>Default value: **true**.
         *
         * @default true
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        autoCancel?: boolean;
        /**
         * Transition effect for the appearance and disappearance of the dialog box.<br>**NOTE**
         * <br> 1. If this parameter is not set, the default effect is used.
         * <br> 2. Touching the Back button during the appearance animation pauses the appearance animation and starts
         *  the disappearance animation. The final effect is one obtained after the curves of the appearance and
         * disappearance animations are combined.
         * <br> 3. Touching the Back button during the exit animation does not affect the animation playback.
         * Touching the Back button again closes the application.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        transition?: TransitionEffect;
        /**
         * Transition effect for the dialog box content. By default, there is no transition effect.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 19
         */
        dialogTransition?: TransitionEffect;
        /**
         * Transition effect for the mask. By default, there is no transition effect.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 19
         */
        maskTransition?: TransitionEffect;
        /**
         * Mask color.
         * <br>Default value: **0x33000000**
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        maskColor?: ResourceColor;
        /**
         * Callback for interactive dismissal of the dialog box.
         * <br>**NOTE**
         * <br>1. If this callback is registered, the dialog box will not be dismissed immediately after the user touches
         * the mask or the Back button, presses the Esc key, or swipes left or right on the screen.
         * The **reason** parameter in the callback is used to determine whether the dialog box can be dismissed.
         * The reason returned by the component does not support the value **CLOSE_BUTTON**.
         * <br>2. In the **onWillDismiss** callback, another **onWillDismiss** callback is not allowed.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        onWillDismiss?: Callback<DismissDialogAction>;
        /**
         * Event callback after the dialog box appears.
         * <br>**NOTE**
         * <br>1. The normal timing sequence is as follows: onWillAppear > onDidAppear > (onDateAccept/onCancel/onDateChange)
         * > onWillDisappear > onDidDisappear.
         * <br>2. You can set the callback event for changing the dialog box display effect in **onDidAppear**.
         * The settings take effect next time the dialog box appears.
         * <br>3. If the user dismisses the dialog box immediately after it appears, **onWillDisappear** is invoked before **onDidAppear**.
         * <br>4. If the dialog box is dismissed before its appearance animation is finished, this callback is not invoked.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        onDidAppear?: () => void;
        /**
         * Event callback after the dialog box disappears.
         * <br>**NOTE**
         * <br>The normal timing sequence is as follows: onWillAppear > onDidAppear > (onDateAccept/onCancel/onDateChange)
         *  > onWillDisappear > onDidDisappear.
         * <br>This callback is not triggered if the dialog box disappearance animation is interrupted (for example, by page navigation).
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        onDidDisappear?: () => void;
        /**
         * Event callback when the dialog box is about to appear.
         * <br>**NOTE**
         * <br>1. The normal timing sequence is as follows: onWillAppear > onDidAppear > (onDateAccept/onCancel/onDateChange)
         *  > onWillDisappear > onDidDisappear.
         * <br>2. You can set the callback event for changing the dialog box display effect in **onWillAppear**.
         * The settings take effect next time the dialog box appears.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        onWillAppear?: () => void;
        /**
         * Event callback when the dialog box is about to disappear.
         * <br>**NOTE**
         * <br>1. The normal timing sequence is as follows: onWillAppear > onDidAppear > (onDateAccept/onCancel/onDateChange)
         *  > onWillDisappear > onDidDisappear.
         * <br>2. If the user dismisses the dialog box immediately after it appears, **onWillDisappear** is invoked before **onDidAppear**.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        onWillDisappear?: () => void;
        /**
         * How the dialog box avoids the soft keyboard when it is brought up.
         * <br>Default value: **KeyboardAvoidMode.DEFAULT**
         *
         * @default KeyboardAvoidMode.DEFAULT
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        keyboardAvoidMode?: KeyboardAvoidMode;
        /**
         * Whether to respond when the device is in semi-folded mode. The value **true** means to respond when the device
         * is in semi-folded mode.
         * <br>Default value: **false**, meaning not to respond when the device is in semi-folded mode.
         * <br>**NOTE**
         * <br>For a PC or 2-in-1 device, the prompt is displayed on the upper half of the screen by default
         * when **enableHoverMode** is set to **true**. You can set **hoverModeArea** to display the prompt on
         * the lower half of the screen. For other devices, the prompt is displayed on the lower half of the screen
         * by default when **enableHoverMode** is set to **true**. You can set **hoverModeArea** to display
         * the prompt on the upper half of the screen.
         *
         * @default false
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 14
         */
        enableHoverMode?: boolean;
        /**
         * Display area of the dialog box in the hover state.
         * <br>Default value: **HoverModeAreaType.BOTTOM_SCREEN**
         *
         * @default HoverModeAreaType.BOTTOM_SCREEN
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 14
         */
        hoverModeArea?: HoverModeAreaType;
        /**
         * Options for customizing the background blur style. For details about the default value, see **BackgroundBlurStyleOptions**.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 19
         */
        backgroundBlurStyleOptions?: BackgroundBlurStyleOptions;
        /**
         * Options for customizing the background effect. For details about the default value, see **BackgroundEffectOptions**.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 19
         */
        backgroundEffect?: BackgroundEffectOptions;
        /**
         * Distance between the dialog box and the keyboard after keyboard avoidance is applied.
         * <br>**NOTE**
         * <br>- Default value: **16vp**
         * <br>- Default unit: vp
         * <br>- This parameter takes effect only when **keyboardAvoidMode** is set to **DEFAULT**.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 15
         */
        keyboardAvoidDistance?: LengthMetrics;
        /**
         * Display level of the dialog box.
         * <br>**NOTE**
         * <br>- Default value: **LevelMode.OVERLAY**
         * <br>- This parameter takes effect only when **showInSubWindow** is set to **false**.
         *
         * @default LevelMode.OVERLAY
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 15
         */
        levelMode?: LevelMode;
        /**
         * [Unique ID](js-apis-arkui-frameNode.md#getuniqueid12) of the node under the display level for the page-level dialog box.
         * <br>Value range: a number no less than 0
         * <br>**NOTE**
         * <br>- This parameter takes effect only when **levelMode** is set to **LevelMode.EMBEDDED**.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 15
         */
        levelUniqueId?: number;
        /**
         * Overlay effect for the page-level dialog box.
         * <br>**NOTE**
         * <br>- Default value: **ImmersiveMode.DEFAULT**
         * <br>- This parameter takes effect only when **levelMode** is set to **LevelMode.EMBEDDED**.
         *
         * @default ImmersiveMode.DEFAULT
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 15
         */
        immersiveMode?: ImmersiveMode;
        /**
         * Display order of the dialog box.
         * <br>**NOTE**
         * <br>- Default value: **LevelOrder.clamp(0)**
         * <br>- Dynamic updating is not supported.
         *
         * @default The value returned by LevelOrder.clamp(0)
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        levelOrder?: LevelOrder;
        /**
         * Whether the dialog box can gain focus.
         * <br>**true**: The dialog box can gain focus.
         * <br>**false**: The dialog box cannot gain focus.
         * <br>Default value: **true**.
         * <br>**NOTE**
         * <br>Only dialog boxes that are displayed on top of the current window can gain focus.
         *
         * @default true
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 19
         */
        focusable?: boolean;
        /**
         * System material of the dialog box. Different materials have different effects and can affect visual attributes
         *  such as the background color, border, and shadow of the dialog box.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 26.0.0
         */
        systemMaterial?: SystemUiMaterial;
    }
    /**
     * Extends [BaseDialogOptions](#basedialogoptions11) to provide enhanced customization capabilities for the dialog box.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice [since 12]
     * @since 11
     */
    interface CustomDialogOptions extends BaseDialogOptions {
        /**
         * Custom content of the dialog box.
         * <br>**NOTE**
         * <br>The builder needs to be assigned an arrow function in the following format: () => { this.XXX() },
         * where XXX indicates the internal builder name.
         * <br>Global builders must be created inside the component and called within the internal builder.
         * <br>The width and height percentages of the builder's root node are relative to the size of the dialog box container.
         * <br>The width and height percentages of non-root nodes are relative to the size of their parent node.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        builder: CustomBuilder;
        /**
         * Background color of the dialog box.<br>Default value: **Color.Transparent**.
         * <br>**NOTE**
         * <br>When **backgroundColor** is set to a non-transparent color, **backgroundBlurStyle** must be set to **BlurStyle.NONE**;
         * otherwise, the color display may not meet the expected effect.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        backgroundColor?: ResourceColor;
        /**
         * Corner radius of the background.
         * <br>You can set separate radii for the four corners.
         * <br>Default value: **{ topLeft: '32vp', topRight: '32vp', bottomLeft: '32vp', bottomRight: '32vp' }**
         * <br> The radius of the rounded corners is subject to the component size. Its maximum value is half of the
         * component width or height. If the value is negative, the default value is used.
         * <br> When set to a percentage, the value defines the radius as a percentage of the parent dialog box's width or height.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        cornerRadius?: Dimension | BorderRadiuses;
        /**
         * Width of the dialog box.
         * <br>**NOTE**
         * <br>- Default maximum width of the dialog box: 400 vp
         * <br>- Percentage-based configuration: The reference width of the dialog box is adjusted based on the width
         * of the window where the dialog box is located.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        width?: Dimension;
        /**
         * Height of the dialog box.
         * <br>**NOTE**
         * <br>- Default maximum height of the dialog box: 0.9 x (Window height – Safe area)
         * <br>- When this parameter is set to a percentage, the reference height of the dialog box is the height of
         * the window where the dialog box is located minus the safe area. You can decrease or increase the height as needed.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        height?: Dimension;
        /**
         * Border width of the dialog box.
         * <br>You can set the width for all four sides or set separate widths for individual sides.
         * <br>Default value: **0**.
         * <br>Unit: vp.
         * <br> When set to a percentage, the value defines the border width as a percentage of the parent dialog box's width.
         * <br>If the left and right borders are greater than its width, or the top and bottom borders are greater than its height,
         * the dialog box may not display as expected.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        borderWidth?: Dimension | EdgeWidths;
        /**
         * Border color of the dialog box.
         * <br>Default value: **Color.Black**.
         * <br> **borderColor** must be used with **borderWidth** in pairs.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        borderColor?: ResourceColor | EdgeColors;
        /**
         * Border style of the dialog box.
         * <br>Default value: **BorderStyle.Solid**.
         * <br> **borderStyle** must be used with **borderWidth** in pairs.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        borderStyle?: BorderStyle | EdgeStyles;
        /**
         * Shadow of the dialog box.
         * <br>Default value on 2-in-1 devices: **ShadowStyle.OUTER_FLOATING_MD** when the dialog box is focused
         * and **ShadowStyle.OUTER_FLOATING_SM** otherwise On other devices, the dialog box has no shadow by default.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        shadow?: ShadowOptions | ShadowStyle;
        /**
         * Background blur style of the dialog box.
         * <br>Default value: **BlurStyle.COMPONENT_ULTRA_THICK**
         * <br>**NOTE**
         * <br>Setting this parameter to **BlurStyle.NONE** disables the background blur.
         * When **backgroundBlurStyle** is set to a value other than **NONE**, do not set **backgroundColor**.
         * If you do, the color display may not produce the expected visual effect.
         *
         * @default BlurStyle.COMPONENT_ULTRA_THICK
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        backgroundBlurStyle?: BlurStyle;
    }
    /**
     * Defines the allowed data types for specifying the background corner radius of a dialog box.
     *
     * @typedef { Dimension | BorderRadiuses } DialogOptionsCornerRadius
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    declare type DialogOptionsCornerRadius = Dimension | BorderRadiuses;
    /**
     * Defines the allowed data types for specifying the background border width of a dialog box.
     *
     * @typedef { Dimension | EdgeWidths } DialogOptionsBorderWidth
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    declare type DialogOptionsBorderWidth = Dimension | EdgeWidths;
    /**
     * Defines the allowed data types for specifying the background border color of a dialog box.
     *
     * @typedef { ResourceColor | EdgeColors } DialogOptionsBorderColor
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    declare type DialogOptionsBorderColor = ResourceColor | EdgeColors;
    /**
     * Defines the allowed data types for specifying the background border style of a dialog box.
     *
     * @typedef { BorderStyle | EdgeStyles } DialogOptionsBorderStyle
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    declare type DialogOptionsBorderStyle = BorderStyle | EdgeStyles;
    /**
     * Defines the allowed data types for specifying the background shadow of a dialog box.
     *
     * @typedef { ShadowOptions | ShadowStyle } DialogOptionsShadow
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    declare type DialogOptionsShadow = ShadowOptions | ShadowStyle;
    /**
     * Extends [BaseDialogOptions](#basedialogoptions11) to provide enhanced customization capabilities for the dialog box.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    interface DialogOptions extends BaseDialogOptions {
        /**
         * Background color of the dialog box.<br>Default value: **Color.Transparent**.
         * <br>**NOTE**
         * <br>The background color will be visually combined with the blur effect when both properties are set.
         * If the resulting effect does not match your design requirements, you can disable the blur effect entirely by
         * explicitly setting the **backgroundBlurStyle** property to **BlurStyle.NONE**.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        backgroundColor?: ResourceColor;
        /**
         * Background corner radius of the dialog box.<br>You can set separate radii for the four corners.
         * <br>Default value: **{ topLeft: '32vp', topRight: '32vp', bottomLeft: '32vp', bottomRight: '32vp' }**
         * <br> The radius of the rounded corners is subject to the component size. Its maximum value is half of the
         * component width or height. If the value is negative, the default value is used.
         * <br> When set to a percentage, the value defines the radius as a percentage of the parent dialog box's width or height.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        cornerRadius?: DialogOptionsCornerRadius;
        /**
         * Width of the dialog box.
         * <br>**NOTE**
         * <br>- Default maximum value: 400vp
         * <br>- Percentage-based configuration: The reference width of the dialog box is adjusted based on the width of
         * the window where the dialog box is located.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        width?: Dimension;
        /**
         * Height of the dialog box.
         * <br>**NOTE**
         * <br>- Default maximum value: 0.9 x (Window height – Safe area)
         * <br>- When this parameter is set to a percentage, the reference height of the dialog box is the height of
         * the window where the dialog box is located minus the safe area. You can decrease or increase the height as needed.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        height?: Dimension;
        /**
         * Border width of the dialog box.
         * <br>You can set the width for all four sides or set separate widths for individual sides.
         * <br>Default value: **0**.
         * <br>Unit: vp.
         * <br> When set to a percentage, the value defines the border width as a percentage of the parent dialog box's width.
         * <br>If the left and right borders are greater than its width, or the top and bottom borders are greater than
         * its height, the dialog box may not display as expected.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        borderWidth?: DialogOptionsBorderWidth;
        /**
         * Border color of the dialog box.
         * <br>Default value: **Color.Black**.
         * <br> **borderColor** must be used with **borderWidth** in pairs.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        borderColor?: DialogOptionsBorderColor;
        /**
         * Border style of the dialog box.
         * <br>Default value: **BorderStyle.Solid**.
         * <br> **borderStyle** must be used with **borderWidth** in pairs.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        borderStyle?: DialogOptionsBorderStyle;
        /**
         * Shadow of the dialog box.
         * <br>Default value on 2-in-1 devices: **ShadowStyle.OUTER_FLOATING_MD** when the dialog box is focused
         * and **ShadowStyle.OUTER_FLOATING_SM** otherwise On other devices, the dialog box has no shadow by default.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        shadow?: DialogOptionsShadow;
        /**
         * Background blur style of the dialog box.
         * <br>Default value: **BlurStyle.COMPONENT_ULTRA_THICK**
         * <br>**NOTE**
         * <br>Setting this parameter to **BlurStyle.NONE** disables the background blur. When **backgroundBlurStyle**
         * is set to a value other than **NONE**, do not set **backgroundColor**.
         * If you do, the color display may not produce the expected visual effect.
         *
         * @default BlurStyle.COMPONENT_ULTRA_THICK
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        backgroundBlurStyle?: BlurStyle;
    }
    /**
     * Describes the action menu response result.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @FaAndStageModel
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    interface ActionMenuSuccessResponse {
        /**
         * Index of the selected button in the **buttons** array, starting from **0**.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @FaAndStageModel
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        index: number;
    }
    /**
     * Describes the options for showing the action menu.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @FaAndStageModel
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    interface ActionMenuOptions {
        /**
         * Title of the dialog box.<br>Default value: **undefined**, which indicates that no title is not displayed by default.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @FaAndStageModel
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        title?: string | Resource;
        /**
         * Array of menu item buttons.
         * The array structure is **{text:'button', color: '\#666666'}**.
         * Up to six buttons are supported. If there are more than six buttons, only the first six buttons will be displayed.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @FaAndStageModel
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        buttons: [
            Button,
            Button?,
            Button?,
            Button?,
            Button?,
            Button?
        ];
        /**
         * Whether to show the menu in a subwindow when the menu needs to be displayed outside the main window.
         * <br>**true**: The menu is shown in a subwindow.
         * <br>Default value: **false**, indicating that the dialog box is not displayed in a subwindow.<br>**NOTE**
         * <br> - A menu whose **showInSubWindow** attribute is **true** cannot trigger the display of another menu
         * whose **showInSubWindow** attribute is also **true**.
         * <br> - If **showInSubWindow** is set to **true** in **UIExtension**, the menu is aligned with the host window
         * based on **UIExtension**.
         *
         * @default false
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        showInSubWindow?: boolean;
        /**
         * Whether the menu is a modal, which has a mask applied and does not allow for interaction with other components
         * around the menu. <br>**true**: The menu is a modal.
         * <br>**false**: The menu is not a modal.
         * <br>Default value: **true**.
         *
         * @default true
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        isModal?: boolean;
        /**
         * Display level mode of the menu.
         * <br>**NOTE**
         * <br>- Default value: **LevelMode.OVERLAY**
         * <br>- This parameter takes effect only when **showInSubWindow** is set to **false**.
         *
         * @default LevelMode.OVERLAY
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 15
         */
        levelMode?: LevelMode;
        /**
         * [Unique ID](js-apis-arkui-frameNode.md#getuniqueid12) of the node under the display level for the page-level menu.
         * <br>Value range: a number no less than 0
         * <br>**NOTE**
         * <br>- This parameter takes effect only when **levelMode** is set to **LevelMode.EMBEDDED**.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 15
         */
        levelUniqueId?: number;
        /**
         * Overlay effect for the page-level menu.
         * <br>**NOTE**
         * <br>- Default value: **ImmersiveMode.DEFAULT**
         * <br>- This parameter takes effect only when **levelMode** is set to **LevelMode.EMBEDDED**.
         *
         * @default ImmersiveMode.DEFAULT
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 15
         */
        immersiveMode?: ImmersiveMode;
        /**
         * Callback invoked after the menu appears.
         * <br>**NOTE**
         * <br>1. The normal timing sequence is as follows: onWillAppear > onDidAppear > onWillDisappear > onDidDisappear.
         * <br>2. When a menu is dismissed immediately after being shown, **onWillDisappear** may be triggered before **onDidAppear**.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        onDidAppear?: Callback<void>;
        /**
         * Callback invoked after the menu disappears.
         * <br>**NOTE**
         * <br>1. The normal timing sequence is as follows: onWillAppear > onDidAppear > onWillDisappear > onDidDisappear.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        onDidDisappear?: Callback<void>;
        /**
         * Callback invoked before the menu appearance animation.<br>**NOTE**
         * <br>1. The normal timing sequence is as follows: onWillAppear > onDidAppear > onWillDisappear > onDidDisappear.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        onWillAppear?: Callback<void>;
        /**
         * Callback invoked before the menu disappearance animation.
         * <br>**NOTE**
         * <br>1. The normal timing sequence is as follows: onWillAppear > onDidAppear > onWillDisappear > onDidDisappear.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        onWillDisappear?: Callback<void>;
        /**
         * System material of the dialog box. Different materials have different effects and can affect visual attributes
         *  such as the background color, border, and shadow of the dialog box.
         *
         * @syscap SystemCapability.ArkUI.ArkUI.Full
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 26.0.0
         */
        systemMaterial?: SystemUiMaterial;
    }
    /**
     * Creates and displays a toast.
     *
     * > **NOTE**
     * >
     * > - This API is supported since API version 9 and deprecated since API version 18. You are advised to use
     * [showToast](arkts-apis-uicontext-promptaction.md#showtoast) instead.
     * Before calling this API, you need to obtain the [PromptAction](arkts-apis-uicontext-promptaction.md) object
     * using the [getPromptAction](arkts-apis-uicontext-uicontext.md#getpromptaction) method in
     * [UIContext](arkts-apis-uicontext-uicontext.md). Directly using **showToast** can lead to the issue of
     * [ambiguous UI context](../../ui/arkts-global-interface.md#ambiguous-ui-context).
     * >
     * > - Since API version 10, you can use the [getPromptAction](arkts-apis-uicontext-uicontext.md#getpromptaction) API
     * in [UIContext](arkts-apis-uicontext-uicontext.md) to obtain the [PromptAction](arkts-apis-uicontext-promptaction.md)
     * object associated with the current UI context.
     * >
     * > - The toast has a fixed style and does not support content customization. For specific supported capabilities,
     * see [ShowToastOptions](#showtoastoptions).
     *
     * @param { ShowToastOptions } options - Toast configuration options.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br> 1. Mandatory parameters are left unspecified.
     *     <br> 2. Incorrect parameters types.
     *     <br> 3. Parameter verification failed.
     * @throws { BusinessError } 100001 - Internal error.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @FaAndStageModel
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @deprecated since 18
     * @useinstead ohos.arkui.UIContext.PromptAction#showToast
     */
    function showToast(options: ShowToastOptions): void;
    /**
     * Shows a toast. This API uses a promise to return the toast ID.
     *
     * > **NOTE**
     * >
     * > - Subwindows with **showMode** set to **TOP_MOST** or **SYSTEM_TOP_MOST** do not support **openToast** in input
     * > method type windows. For details, see the constraints in the input method framework
     * > [createPanel]{@link @ohos.inputMethodEngine:inputMethodEngine.InputMethodAbility.createPanel(ctx: BaseContext, info: PanelInfo)}
     * > .
     * >
     * > - Directly using **openToast** can lead to the issue of
     * > [ambiguous UI context](docroot://ui/arkts-global-interface.md#ambiguous-ui-context). To avoid this, obtain the
     * > **PromptAction** object using the **getPromptAction** API in **UIContext** and then call the
     * > [openToast]{@link @ohos.arkui.UIContext:PromptAction.openToast} API through this object.
     *
     * @param { ShowToastOptions } options - Toast configuration options.
     * @returns { Promise<number> } Promise that returns the toast ID for use with **closeToast**.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br> 1. Mandatory parameters are left unspecified.
     *     <br> 2. Incorrect parameters types.
     *     <br> 3. Parameter verification failed.
     * @throws { BusinessError } 100001 - Internal error.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    function openToast(options: ShowToastOptions): Promise<number>;
    /**
     * Closes the specified toast.
     *
     * > **NOTE**
     * >
     * > Directly using **closeToast** can lead to the issue of
     * > [ambiguous UI context](docroot://ui/arkts-global-interface.md#ambiguous-ui-context). To avoid this, obtain the
     * > **PromptAction** object using the **getPromptAction** API in **UIContext** and then call the
     * > [closeToast]{@link @ohos.arkui.UIContext:PromptAction.closeToast} API through this object.
     *
     * @param { number } toastId - Toast ID returned from **openToast**.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br> 1. Mandatory parameters are left unspecified.
     *     <br> 2. Incorrect parameters types.
     *     <br> 3. Parameter verification failed.
     * @throws { BusinessError } 100001 - Internal error.
     * @throws { BusinessError } 103401 - Cannot find the toast.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    function closeToast(toastId: number): void;
    /**
     * Creates and displays a dialog box. This API uses an asynchronous callback to return the result.
     *
     * > **NOTE**
     * >
     * > - This API is supported since API version 9 and deprecated since API version 18.
     * You are advised to use [showDialog](arkts-apis-uicontext-promptaction.md#showdialog) instead.
     * Before calling this API, you need to obtain the [PromptAction](arkts-apis-uicontext-promptaction.md) object
     * using the [getPromptAction](arkts-apis-uicontext-uicontext.md#getpromptaction) method
     * in [UIContext](arkts-apis-uicontext-uicontext.md). Directly using **showDialog** can lead to the issue
     * of [ambiguous UI context](../../ui/arkts-global-interface.md#ambiguous-ui-context).
     * >
     * > - Since API version 10, you can use the [getPromptAction](arkts-apis-uicontext-uicontext.md#getpromptaction) API
     * in [UIContext](arkts-apis-uicontext-uicontext.md) to obtain the [PromptAction](arkts-apis-uicontext-promptaction.md)
     * object associated with the current UI context.
     *
     * @param { ShowDialogOptions } options - Dialog box configuration options.
     * @param { AsyncCallback<ShowDialogSuccessResponse> } callback - Callback used to return the result.
     *      On success, **err** is **undefined** and **data** contains the dialog box response.
     *      On failure, **err** provides error details.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br> 1. Mandatory parameters are left unspecified.
     *     <br> 2. Incorrect parameters types.
     *     <br> 3. Parameter verification failed.
     * @throws { BusinessError } 100001 - Internal error.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @FaAndStageModel
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @deprecated since 18
     * @useinstead ohos.arkui.UIContext.PromptAction#showDialog
     */
    function showDialog(options: ShowDialogOptions, callback: AsyncCallback<ShowDialogSuccessResponse>): void;
    /**
     * Creates and displays a dialog box in the given settings. This API uses a promise to return the result.
     *
     * > **NOTE**
     * >
     * > - This API is supported since API version 9 and deprecated since API version 18.
     * You are advised to use [showDialog](arkts-apis-uicontext-promptaction.md#showdialog-1) instead.
     * Before calling this API, you need to obtain the [PromptAction](arkts-apis-uicontext-promptaction.md) object
     * using the [getPromptAction](arkts-apis-uicontext-uicontext.md#getpromptaction) method in [UIContext](arkts-apis-uicontext-uicontext.md).
     * Directly using **showDialog** can lead to the issue of [ambiguous UI context](../../ui/arkts-global-interface.md#ambiguous-ui-context).
     * >
     * > - Since API version 10, you can use the [getPromptAction](arkts-apis-uicontext-uicontext.md#getpromptaction) API
     * in [UIContext](arkts-apis-uicontext-uicontext.md) to obtain the [PromptAction](arkts-apis-uicontext-promptaction.md)
     * object associated with the current UI context.
     *
     * @param { ShowDialogOptions } options - Dialog box configuration options.
     * @returns { Promise<ShowDialogSuccessResponse> } Promise that returns the dialog box response.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br> 1. Mandatory parameters are left unspecified.
     *     <br> 2. Incorrect parameters types.
     *     <br> 3. Parameter verification failed.
     * @throws { BusinessError } 100001 - Internal error.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @FaAndStageModel
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @deprecated since 18
     * @useinstead ohos.arkui.UIContext.PromptAction#showDialog
     */
    function showDialog(options: ShowDialogOptions): Promise<ShowDialogSuccessResponse>;
    /**
     * Opens a custom dialog box. This API uses a promise to return the result.
     *
     * <!--Del-->This API cannot be used in **ServiceExtension**.<!--DelEnd-->
     *
     *
     * By default, the width of the dialog box in portrait mode is the width of the window where it is located minus the
     * left and right margins (40 vp for 2-in-1 devices and 16 vp for other devices), and the maximum width is 400 vp.
     *
     * > **NOTE**
     * >
     * > - This API is supported since API version 11 and deprecated since API version 18.
     * You are advised to use [openCustomDialog](arkts-apis-uicontext-promptaction.md#opencustomdialog12-1) instead.
     * Before calling this API, you need to obtain the [PromptAction](arkts-apis-uicontext-promptaction.md) object
     * using the [getPromptAction](arkts-apis-uicontext-uicontext.md#getpromptaction) method in [UIContext](arkts-apis-uicontext-uicontext.md).
     * Directly using **openCustomDialog** can lead to the issue of [ambiguous UI context](../../ui/arkts-global-interface.md#ambiguous-ui-context).
     * >
     * > - Since API version 12, you can use the [getPromptAction](arkts-apis-uicontext-uicontext.md#getpromptaction) API
     * in [UIContext](arkts-apis-uicontext-uicontext.md) to obtain the [PromptAction](arkts-apis-uicontext-promptaction.md)
     * object associated with the current UI context.
     *
     * @param { CustomDialogOptions } options - Content of the custom dialog box.
     *      <br>Note: If both [isModal](js-apis-promptAction.md#basedialogoptions11) and
     *      [showInSubWindow](js-apis-promptAction.md#basedialogoptions11) in **BaseDialogOptions** are set to **true**,
     *      only **showInSubWindow** takes effect. In this case, the non-modal dialog box is displayed
     *      without mask in the subwindow.
     * @returns { Promise<number> } ID of the custom dialog box, which can be used in **closeCustomDialog**.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br> 1. Mandatory parameters are left unspecified.
     *     <br> 2. Incorrect parameters types.
     *     <br> 3. Parameter verification failed.
     * @throws { BusinessError } 100001 - Internal error.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice [since 12]
     * @since 11
     * @deprecated since 18
     * @useinstead ohos.arkui.UIContext.PromptAction#openCustomDialog
     */
    function openCustomDialog(options: CustomDialogOptions): Promise<number>;
    /**
     * Closes the specified custom dialog box.
     *
     * > **NOTE**
     * >
     * > - This API is supported since API version 11 and deprecated since API version 18.
     * You are advised to use [closeCustomDialog](arkts-apis-uicontext-promptaction.md#closecustomdialog12-1) instead.
     * Before calling this API, you need to obtain the [PromptAction](arkts-apis-uicontext-promptaction.md) object
     * using the [getPromptAction](arkts-apis-uicontext-uicontext.md#getpromptaction) method in [UIContext](arkts-apis-uicontext-uicontext.md).
     * Directly using **closeCustomDialog** can lead to the issue of [ambiguous UI context](../../ui/arkts-global-interface.md#ambiguous-ui-context).
     * >
     * > - Since API version 12, you can use the [getPromptAction](arkts-apis-uicontext-uicontext.md#getpromptaction) API
     * in [UIContext](arkts-apis-uicontext-uicontext.md) to obtain the [PromptAction](arkts-apis-uicontext-promptaction.md)
     * object associated with the current UI context.
     *
     * @param { number } dialogId - ID of the custom dialog box to close. It is returned from **openCustomDialog**.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br> 1. Mandatory parameters are left unspecified.
     *     <br> 2. Incorrect parameters types.
     *     <br> 3. Parameter verification failed.
     * @throws { BusinessError } 100001 - Internal error.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice [since 12]
     * @since 11
     * @deprecated since 18
     * @useinstead ohos.arkui.UIContext.PromptAction#closeCustomDialog
     */
    function closeCustomDialog(dialogId: number): void;
    /**
     * Creates and displays an action menu. This API uses an asynchronous callback to return the result.
     *
     * > **NOTE**
     * >
     * > - This API is supported since API version 9 and deprecated since API version 18.
     * You are advised to use [showActionMenu](arkts-apis-uicontext-promptaction.md#showactionmenu11) instead.
     * Before calling this API, you need to obtain the [PromptAction](arkts-apis-uicontext-promptaction.md) object
     *  using the [getPromptAction](arkts-apis-uicontext-uicontext.md#getpromptaction) method in [UIContext](arkts-apis-uicontext-uicontext.md).
     * Directly using **showActionMenu** can lead to the issue of [ambiguous UI context](../../ui/arkts-global-interface.md#ambiguous-ui-context).
     * >
     * > - Since API version 11, you can use the [getPromptAction](arkts-apis-uicontext-uicontext.md#getpromptaction) API
     * in [UIContext](arkts-apis-uicontext-uicontext.md) to obtain the [PromptAction](arkts-apis-uicontext-promptaction.md) object
     *  associated with the current UI context.
     *
     * @param { ActionMenuOptions } options - Action menu options.
     * @param { AsyncCallback<ActionMenuSuccessResponse> } callback - Callback used to return the result.
     *      On success, **err** is **undefined** and **data** contains the action menu response.
     *      On failure, **err** provides error details.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br> 1. Mandatory parameters are left unspecified.
     *     <br> 2. Incorrect parameters types.
     *     <br> 3. Parameter verification failed.
     * @throws { BusinessError } 100001 - Internal error.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @FaAndStageModel
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @deprecated since 18
     * @useinstead ohos.arkui.UIContext.PromptAction#showActionMenu
     */
    function showActionMenu(options: ActionMenuOptions, callback: AsyncCallback<ActionMenuSuccessResponse>): void;
    /**
     * Creates and displays an action menu in the given settings. This API uses a promise to return the result.
     *
     * > **NOTE**
     * >
     * > - This API is supported since API version 9 and deprecated since API version 18.
     * You are advised to use [showActionMenu](arkts-apis-uicontext-promptaction.md#showactionmenu) instead.
     *  Before calling this API, you need to obtain the [PromptAction](arkts-apis-uicontext-promptaction.md) object
     * using the [getPromptAction](arkts-apis-uicontext-uicontext.md#getpromptaction) method in [UIContext](arkts-apis-uicontext-uicontext.md).
     * Directly using **showActionMenu** can lead to the issue of [ambiguous UI context](../../ui/arkts-global-interface.md#ambiguous-ui-context).
     * >
     * > - Since API version 10, you can use the [getPromptAction](arkts-apis-uicontext-uicontext.md#getpromptaction)
     * API in [UIContext](arkts-apis-uicontext-uicontext.md) to obtain the [PromptAction](arkts-apis-uicontext-promptaction.md)
     * object associated with the current UI context.
     *
     * @param { ActionMenuOptions } options - Promise that returns the action menu response.
     * @returns { Promise<ActionMenuSuccessResponse> } Promise that returns the action menu response.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br> 1. Mandatory parameters are left unspecified.
     *     <br> 2. Incorrect parameters types.
     *     <br> 3. Parameter verification failed.
     * @throws { BusinessError } 100001 - Internal error.
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @FaAndStageModel
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @deprecated since 18
     * @useinstead ohos.arkui.UIContext.PromptAction#showActionMenu
     */
    function showActionMenu(options: ActionMenuOptions): Promise<ActionMenuSuccessResponse>;
}
/**
 * Provides information about the action to dismiss the dialog box.
 *
 * @syscap SystemCapability.ArkUI.ArkUI.Full
 * @stagemodelonly
 * @crossplatform
 * @atomicservice
 * @since 12
 */
declare interface DismissDialogAction {
    /**
     * Callback for dismissing the dialog box. This API is called only when the dialog box needs to be exited.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    dismiss: Callback<void>;
    /**
     * Reason why the dialog box cannot be dismissed. You must specify whether to close the dialog box for each of the listed actions.
     *
     * @syscap SystemCapability.ArkUI.ArkUI.Full
     * @stagemodelonly
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    reason: DismissReason;
}
export default promptAction;

```
