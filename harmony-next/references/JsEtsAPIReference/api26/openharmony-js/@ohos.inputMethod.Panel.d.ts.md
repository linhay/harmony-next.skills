# @ohos.inputMethod.Panel.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2023 Huawei Device Co., Ltd.
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
 * The **inputMethod.Panel** module provides APIs for managing the attributes of the input method panel.
 *
 * @file
 * @kit IMEKit
 */
/**
 * Defines the attributes of the input method panel.
 *
 * @syscap SystemCapability.MiscServices.InputMethodFramework
 * @since 11
 */
export interface PanelInfo {
    /**
     * Type of the input method panel.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 11
     */
    type: PanelType;
    /**
     * State type of the input method panel.
     *
     * - The default value is **FLAG_FIXED**.
     * - Currently, this parameter is used to describe the state type of the soft keyboard.
     *
     * @default FLG_FIXED
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 11
     */
    flag?: PanelFlag;
}
/**
 * Enumerates the state types of the input method panel.
 *
 * > **NOTE**
 * >
 * > Currently, only the **SOFT_KEYBOARD** panel is supported.
 *
 * @syscap SystemCapability.MiscServices.InputMethodFramework
 * @since 11
 */
export enum PanelFlag {
    /**
     * Fixed state type.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 11
     */
    FLAG_FIXED = 0,
    /**
     * Floating state type.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 11
     */
    FLAG_FLOATING,
    /**
     * Candidate state type.
     *
     * - When in the candidate state type, the input method panel is a window displaying candidates based on user input.
     * - The input method service does not proactively control the visibility of the candidate panel. You need to control
     * the visibility on your own.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 11
     */
    FLAG_CANDIDATE
}
/**
 * Enumerates the types of the input method panel.
 *
 * @syscap SystemCapability.MiscServices.InputMethodFramework
 * @since 11
 */
export enum PanelType {
    /**
     * Soft keyboard.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 11
     */
    SOFT_KEYBOARD = 0,
    /**
     * Status bar.
     *
     * @syscap SystemCapability.MiscServices.InputMethodFramework
     * @since 11
     */
    STATUS_BAR
}

```
