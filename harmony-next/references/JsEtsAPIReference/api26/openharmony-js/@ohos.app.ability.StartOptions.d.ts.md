# @ohos.app.ability.StartOptions.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022-2024 Huawei Device Co., Ltd.
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
 * @kit AbilityKit
 */
import contextConstant from './@ohos.app.ability.contextConstant';
import image from './@ohos.multimedia.image';
import bundleManager from './@ohos.bundle.bundleManager';
import CompletionHandler from './@ohos.app.ability.CompletionHandler';
import window from './@ohos.window';
/**
 * StartOptions can be used as an input parameter for APIs used to launch a UIAbility (for example,
 * [startAbility()]{@link ./application/UIAbilityContext:UIAbilityContext#startAbility(want: Want, options: StartOptions, callback: AsyncCallback<void>)}
 * ). It specifies the options for starting the target UIAbility, including but not limited to the window mode and the
 * display where the target UIAbility is started.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @stagemodelonly
 * @atomicservice [since 11]
 * @since 9
 */
declare class StartOptions {
    /**
     * Window mode for the UIAbility upon startup. For details, see
     * [WindowMode]{@link ./@ohos.app.ability.AbilityConstant:AbilityConstant.WindowMode}.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 12
     */
    windowMode?: number;
    /**
     * The type of split ratio preference.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    splitRatio?: window.SplitRatioPreference;
    /**
     * Display ID, which is an integer greater than or equal to -1.
     *
     * - The value **-1** means the current screen.
     * - The value **0** means the primary screen.
     * - A positive integer means a specific screen with that ID.
     *
     * **NOTE**
     *
     * Starting from API version 14, the default value is **-1**, indicating the current screen.
     *
     * In versions earlier than API version 14, the default value is **0**, indicating the primary screen.
     *
     * @type { ?number } [since 9 - 10]
     * @type { ?number } [since 11]
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice [since 11]
     * @since 9
     */
    displayId?: number;
    /**
     * Whether animation effects are used for the UIAbility upon startup. **true** if used, **false** otherwise.
     *
     * **Constraints**:
     *
     * 1. This property takes effect only on 2-in-1 devices and tablets.
     * 2. The caller and target must be the same application.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 11
     */
    withAnimation?: boolean;
    /**
     * Distance the window moves along the x-axis, with the top-left vertex of the screen specified by **displayId** as
     * the starting point. The unit is px. A positive value means moving to the right, and a negative value means moving
     * to the left. The value is an integer. Non-integer values will be rounded down. When the top-left vertex of the
     * window exceeds the screen area of the specified **displayId**, the window is restricted to be visible only within
     * the screen range of the specified **displayId**. When configuring this field, you are advised to configure
     * **windowTop** at the same time.
     *
     * **Constraints**:
     *
     * This function takes effect only in the
     * [freeform window](docroot://windowmanager/window-terminology.md#freeform-window) state.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 11
     */
    windowLeft?: number;
    /**
     * Distance the window moves along the y-axis, with the top-left vertex of the screen specified by **displayId** as
     * the starting point. The unit is px. A positive value means moving downward, and a negative value means moving
     * upward. The value is an integer. Non-integer values will be rounded down. When the top of the window exceeds the
     * screen area of the specified **displayId**, the window is restricted to be visible only within the screen range of
     * the specified **displayId**. When configuring this field, you are advised to also configure **windowLeft**.
     *
     * **Constraints**:
     *
     * This function takes effect only in the
     * [freeform window](docroot://windowmanager/window-terminology.md#freeform-window) state.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 11
     */
    windowTop?: number;
    /**
     * Window width, in px.
     *
     * The value range is [**minWindowWidth**, **maxWindowWidth**], with the unit being vp. You can call
     * [vp2px]{@link @ohos.arkui.UIContext:UIContext.vp2px} to convert it to the corresponding px value.
     *
     * **Constraints**:
     *
     * This function takes effect only in the
     * [freeform window](docroot://windowmanager/window-terminology.md#freeform-window) state.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 11
     */
    windowWidth?: number;
    /**
     * Window height, in px.
     *
     * The value range is [**minWindowHeight**, **maxWindowHeight**], with the unit being vp. You can call
     * [vp2px]{@link @ohos.arkui.UIContext:UIContext.vp2px} to convert it to the corresponding px value.
     *
     * **Constraints**:
     *
     * This function takes effect only in the
     * [freeform window](docroot://windowmanager/window-terminology.md#freeform-window) state.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 11
     */
    windowHeight?: number;
    /**
     * Process mode of the UIAbility after it is started.
     *
     * **Constraints**:
     *
     * 1. This property takes effect only on 2-in-1 devices and tablets.
     * 2. This property takes effect only in
     * [UIAbilityContext.startAbility]{@link ./application/UIAbilityContext:UIAbilityContext#startAbility}.
     * 3. **processMode** and **startupVisibility** must be set in pair.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 12
     */
    processMode?: contextConstant.ProcessMode;
    /**
     * Visibility status of the UIAbility after it is started. If the target UIAbility is set to invisible, the window of
     * the target UIAbility is not displayed in the foreground, there is no icon in the dock, and the **onForeground**
     * lifecycle of the target UIAbility is not triggered.
     *
     * **Constraints**:
     *
     * 1. This property takes effect only on 2-in-1 devices and tablets.
     * 2. This property takes effect only in
     * [UIAbilityContext.startAbility]{@link ./application/UIAbilityContext:UIAbilityContext#startAbility}.
     * 3. **processMode** and **startupVisibility** must be set in pair.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 12
     */
    startupVisibility?: contextConstant.StartupVisibility;
    /**
     * Icon displayed on the starting window for the UIAbility of the current application upon startup. If this property
     * is not set, the value of **startWindowIcon** in the **module.json5** file is used by default.
     *
     * **Constraints**:
     *
     * - This property does not take effect for the UIAbility of another application.
     * - This property takes effect only on 2-in-1 devices and tablets.
     * - This property takes effect only in
     * [UIAbilityContext.startAbility]{@link ./application/UIAbilityContext:UIAbilityContext#startAbility}.
     * - The maximum size of an image used as the startup icon is 600 MB.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 14
     */
    startWindowIcon?: image.PixelMap;
    /**
     * Background color of the window for the UIAbility of the current application upon startup. The value is in ARGB
     * format, for example, **#E5FFFFFF**. If this property is not set, the value of **startWindowBackground** in the
     * **module.json5** file is used by default.
     *
     * **Constraints**:
     *
     * - This property does not take effect for the UIAbility of another application.
     * - This property takes effect only on 2-in-1 devices and tablets.
     * - This property takes effect only in
     * [UIAbilityContext.startAbility]{@link ./application/UIAbilityContext:UIAbilityContext#startAbility}.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 14
     */
    startWindowBackgroundColor?: string;
    /**
     * Window mode supported by the UIAbility when it is started. The supported window mode specifies whether to display
     * the maximize, minimize, or split-screen button. If this property is not set, the value of **supportWindowMode**
     * configured under [abilities](docroot://quick-start/module-configuration-file.md#abilities) in the
     * [module.json5](docroot://quick-start/module-configuration-file.md) file corresponding to the UIAbility is used by
     * default.
     *
     * - **FULL_SCREEN**: full-screen mode.
     * - **FLOATING**: floating window mode.
     * - **SPLIT**: split-screen mode. Generally, **FULL_SCREEN** or **FLOATING** must be used together. You are not
     * advised to configure only **SPLIT**. If only **SPLIT** is configured, the window on 2-in-1 devices is in floating
     * window mode by default and can transition to the split-screen mode, and the window on tablets is in full-screen
     * mode by default and can transition to the split-screen mode.
     *
     * When **FULL_SCREEN** and **SPLIT** are both configured for a
     * [freeform window](docroot://windowmanager/window-terminology.md#freeform-window), the window will be started in
     * floating window mode if the value of
     * [targetAPIVersion](docroot://quick-start/app-configuration-file.md#tags-in-the-configuration-file) is less than 15
     * , and in full-screen mode if the value is greater than or equal to 15.
     *
     * **Constraints**:
     *
     * <!--RP1-->This property takes effect only on 2-in-1 devices and tablets.<!--RP1End-->
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 14
     */
    supportWindowModes?: Array<bundleManager.SupportWindowMode>;
    /**
     * Maximum height of the window, in vp. You can call
     * [getWindowLimitsVP]{@link @ohos.window.d.ts:window.getWindowLimitsVP} to obtain the size limit of the current
     * window.
     *
     * **Constraints**:
     *
     * This function takes effect only in the
     * [freeform window](docroot://windowmanager/window-terminology.md#freeform-window) state.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 17
     */
    maxWindowHeight?: number;
    /**
     * Minimum width of the window, in vp. You can call
     * [getWindowLimitsVP]{@link @ohos.window.d.ts:window.getWindowLimitsVP} to obtain the size limit of the current
     * window.
     *
     * **Constraints**:
     *
     * This function takes effect only in the
     * [freeform window](docroot://windowmanager/window-terminology.md#freeform-window) state.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 17
     */
    minWindowWidth?: number;
    /**
     * Minimum height of the window, in vp. You can call
     * [getWindowLimitsVP]{@link @ohos.window.d.ts:window.getWindowLimitsVP} to obtain the size limit of the current
     * window.
     *
     * **Constraints**:
     *
     * This function takes effect only in the
     * [freeform window](docroot://windowmanager/window-terminology.md#freeform-window) state.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 17
     */
    minWindowHeight?: number;
    /**
     * Maximum width of the window, in vp. You can call
     * [getWindowLimitsVP]{@link @ohos.window.d.ts:window.getWindowLimitsVP} to obtain the size limit of the current
     * window.
     *
     * **Constraints**:
     *
     * This function takes effect only in the
     * [freeform window](docroot://windowmanager/window-terminology.md#freeform-window) state.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 17
     */
    maxWindowWidth?: number;
    /**
     * Operation class used to handle the result of an application launch request.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    completionHandler?: CompletionHandler;
    /**
     * Whether to hide the starting window for the UIAbility of the current application upon startup. The options include
     * **true** (yes) and **false** (no). For details about the starting window and its specifications, see
     * [StartWindow](docroot://quick-start/module-configuration-file.md#startwindow).
     *
     * **Constraints**:
     *
     * 1. This property takes effect only on tablets in free windows mode and 2-in-1 devices.
     * 2. This property applies only for an attempt to launch the UIAbility of the current application.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 20
     */
    hideStartWindow?: boolean;
    /**
     * Parameters for the window for the UIAbility upon startup.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 20
     */
    windowCreateParams?: window.WindowCreateParams;
}
export default StartOptions;

```
