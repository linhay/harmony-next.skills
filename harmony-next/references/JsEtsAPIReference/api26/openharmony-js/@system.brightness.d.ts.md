# @system.brightness.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022-2023 Huawei Device Co., Ltd.
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
 * @kit BasicServicesKit
 */
/**
 * The **brightness** module provides APIs for querying and adjusting the screen brightness and mode.
 *
 * > **NOTE**
 * >
 * > - Module maintenance policy:
 * >
 * >    - For lite wearables, this module is constantly maintained and available.
 * >
 * >    - For other device types, this module is no longer maintained since API version 7.<!--Del--> You are advised
 * > to use APIs of [@ohos.brightness]{@link @ohos.brightness:brightness}. <!--DelEnd-->The substitute APIs are
 * > available only for system applications.
 *
 */
/**
 * Defines a response that returns the screen brightness.
 *
 * @syscap SystemCapability.PowerManager.DisplayPowerManager.Lite
 * @FaAndStageModel
 * @since 3
 * @deprecated since 7
 * @reserved ["liteWearable"]
 */
export interface BrightnessResponse {
    /**
     * Screen brightness. The value ranges from **1** to **255**.
     *
     * @syscap SystemCapability.PowerManager.DisplayPowerManager.Lite
     * @FaAndStageModel
     * @since 3
     * @deprecated since 7
     * @reserved ["liteWearable"]
     */
    value: number;
}
/**
 * Options for obtaining the screen brightness.
 *
 * @syscap SystemCapability.PowerManager.DisplayPowerManager.Lite
 * @FaAndStageModel
 * @since 3
 * @deprecated since 7
 * @reserved ["liteWearable"]
 */
export interface GetBrightnessOptions {
    /**
     * Called when an API call is successful. **data** is a return value of the
     * [BrightnessResponse]{@link BrightnessResponse} type.
     *
     * @syscap SystemCapability.PowerManager.DisplayPowerManager.Lite
     * @FaAndStageModel
     * @since 3
     * @deprecated since 7
     * @reserved ["liteWearable"]
     */
    success?: (data: BrightnessResponse) => void;
    /**
     * Called when an API call has failed. **data** indicates the error information, and **code** indicates the error
     * code.
     *
     * @syscap SystemCapability.PowerManager.DisplayPowerManager.Lite
     * @FaAndStageModel
     * @since 3
     * @deprecated since 7
     * @reserved ["liteWearable"]
     */
    fail?: (data: string, code: number) => void;
    /**
     * Called when an API call is complete.
     *
     * @syscap SystemCapability.PowerManager.DisplayPowerManager.Lite
     * @FaAndStageModel
     * @since 3
     * @deprecated since 7
     * @reserved ["liteWearable"]
     */
    complete?: () => void;
}
/**
 * Options for setting the screen brightness.
 *
 * @syscap SystemCapability.PowerManager.DisplayPowerManager.Lite
 * @FaAndStageModel
 * @since 3
 * @deprecated since 7
 * @reserved ["liteWearable"]
 */
export interface SetBrightnessOptions {
    /**
     * Screen brightness. The value is an integer ranging from **1** to **255**.
     *
     * - If the value is less than or equal to **0**, value **1** will be used.
     * - If the value is greater than **255**, value **255** will be used.
     * - If the value contains decimals, the integral part of the value will be used. For example, if value **8.1** is set
     * , value **8** will be used.
     *
     * @syscap SystemCapability.PowerManager.DisplayPowerManager.Lite
     * @FaAndStageModel
     * @since 3
     * @deprecated since 7
     * @reserved ["liteWearable"]
     */
    value: number;
    /**
     * Called when an API call is successful.
     *
     * @syscap SystemCapability.PowerManager.DisplayPowerManager.Lite
     * @FaAndStageModel
     * @since 3
     * @deprecated since 7
     * @reserved ["liteWearable"]
     */
    success?: () => void;
    /**
     * Called when an API call has failed. **data** indicates the error information, and **code** indicates the error
     * code.
     *
     * @syscap SystemCapability.PowerManager.DisplayPowerManager.Lite
     * @FaAndStageModel
     * @since 3
     * @deprecated since 7
     * @reserved ["liteWearable"]
     */
    fail?: (data: string, code: number) => void;
    /**
     * Called when an API call is complete.
     *
     * @syscap SystemCapability.PowerManager.DisplayPowerManager.Lite
     * @FaAndStageModel
     * @since 3
     * @deprecated since 7
     * @reserved ["liteWearable"]
     */
    complete?: () => void;
}
/**
 *Defines a response that returns the screen brightness mode.
 *
 * @syscap SystemCapability.PowerManager.DisplayPowerManager.Lite
 * @FaAndStageModel
 * @since 3
 * @deprecated since 7
 * @reserved ["liteWearable"]
 */
export interface BrightnessModeResponse {
    /**
     * The value **0** indicates the manual adjustment mode, and the value **1** indicates the automatic adjustment mode.
     *
     * @syscap SystemCapability.PowerManager.DisplayPowerManager.Lite
     * @FaAndStageModel
     * @since 3
     * @deprecated since 7
     * @reserved ["liteWearable"]
     */
    mode: number;
}
/**
 * Options for obtaining the screen brightness mode.
 *
 * @syscap SystemCapability.PowerManager.DisplayPowerManager.Lite
 * @FaAndStageModel
 * @since 3
 * @deprecated since 7
 * @reserved ["liteWearable"]
 */
export interface GetBrightnessModeOptions {
    /**
     * Called when an API call is successful. **data** is a return value of the
     * [BrightnessModeResponse]{@link BrightnessModeResponse} type.
     *
     * @syscap SystemCapability.PowerManager.DisplayPowerManager.Lite
     * @FaAndStageModel
     * @since 3
     * @deprecated since 7
     * @reserved ["liteWearable"]
     */
    success?: (data: BrightnessModeResponse) => void;
    /**
     * Called when an API call has failed. **data** indicates the error information, and **code** indicates the error
     * code.
     *
     * @syscap SystemCapability.PowerManager.DisplayPowerManager.Lite
     * @FaAndStageModel
     * @since 3
     * @deprecated since 7
     * @reserved ["liteWearable"]
     */
    fail?: (data: string, code: number) => void;
    /**
     * Called when an API call is complete.
     *
     * @syscap SystemCapability.PowerManager.DisplayPowerManager.Lite
     * @FaAndStageModel
     * @since 3
     * @deprecated since 7
     * @reserved ["liteWearable"]
     */
    complete?: () => void;
}
/**
 * Options for setting the screen brightness mode.
 *
 * @syscap SystemCapability.PowerManager.DisplayPowerManager.Lite
 * @FaAndStageModel
 * @since 3
 * @deprecated since 7
 * @reserved ["liteWearable"]
 */
export interface SetBrightnessModeOptions {
    /**
     * The value **0** indicates the manual adjustment mode, and the value **1** indicates the automatic adjustment mode.
     *
     * @syscap SystemCapability.PowerManager.DisplayPowerManager.Lite
     * @FaAndStageModel
     * @since 3
     * @deprecated since 7
     * @reserved ["liteWearable"]
     */
    mode: number;
    /**
     * Called when an API call is successful.
     *
     * @syscap SystemCapability.PowerManager.DisplayPowerManager.Lite
     * @FaAndStageModel
     * @since 3
     * @deprecated since 7
     * @reserved ["liteWearable"]
     */
    success?: () => void;
    /**
     * Called when an API call has failed. **data** indicates the error information, and **code** indicates the error
     * code.
     *
     * @syscap SystemCapability.PowerManager.DisplayPowerManager.Lite
     * @FaAndStageModel
     * @since 3
     * @deprecated since 7
     * @reserved ["liteWearable"]
     */
    fail?: (data: string, code: number) => void;
    /**
     * Called when an API call is complete.
     *
     * @syscap SystemCapability.PowerManager.DisplayPowerManager.Lite
     * @FaAndStageModel
     * @since 3
     * @deprecated since 7
     * @reserved ["liteWearable"]
     */
    complete?: () => void;
}
/**
 * Options for setting the screen to be steady on.
 *
 * @syscap SystemCapability.PowerManager.DisplayPowerManager.Lite
 * @FaAndStageModel
 * @since 3
 * @deprecated since 7
 * @reserved ["liteWearable"]
 */
export interface SetKeepScreenOnOptions {
    /**
     * The value **true** means to keep the screen steady on, and the value **false** indicates the opposite.
     *
     * @syscap SystemCapability.PowerManager.DisplayPowerManager.Lite
     * @FaAndStageModel
     * @since 3
     * @deprecated since 7
     * @reserved ["liteWearable"]
     */
    keepScreenOn: boolean;
    /**
     * Called when an API call is successful.
     *
     * @syscap SystemCapability.PowerManager.DisplayPowerManager.Lite
     * @FaAndStageModel
     * @since 3
     * @deprecated since 7
     * @reserved ["liteWearable"]
     */
    success?: () => void;
    /**
     * Called when an API call has failed. **data** indicates the error information, and **code** indicates the error
     * code.
     *
     * @syscap SystemCapability.PowerManager.DisplayPowerManager.Lite
     * @FaAndStageModel
     * @since 3
     * @deprecated since 7
     * @reserved ["liteWearable"]
     */
    fail?: (data: string, code: number) => void;
    /**
     * Called when an API call is complete.
     *
     * @syscap SystemCapability.PowerManager.DisplayPowerManager.Lite
     * @FaAndStageModel
     * @since 3
     * @deprecated since 7
     * @reserved ["liteWearable"]
     */
    complete?: () => void;
}
/**
 * The module provides APIs for querying and adjusting the screen brightness and mode.
 *
 * @syscap SystemCapability.PowerManager.DisplayPowerManager.Lite
 * @FaAndStageModel
 * @since 3
 * @deprecated since 7
 * @reserved ["liteWearable"]
 */
export default class Brightness {
    /**
     * Obtains the current screen brightness.
     *
     * @param { GetBrightnessOptions } options Options for obtaining the screen brightness. This parameter is
     *     optional and is left blank by default.
     * @syscap SystemCapability.PowerManager.DisplayPowerManager.Lite
     * @FaAndStageModel
     * @since 3
     * @deprecated since 7
     * @reserved ["liteWearable"]
     */
    static getValue(options?: GetBrightnessOptions): void;
    /**
     * Sets the screen brightness.
     *
     * @param { SetBrightnessOptions } options Options for setting the screen brightness. This parameter is
     *     optional and is left blank by default.
     * @syscap SystemCapability.PowerManager.DisplayPowerManager.Lite
     * @FaAndStageModel
     * @since 3
     * @deprecated since 7
     * @reserved ["liteWearable"]
     * @useinstead @ohos.brightness:brightness.setValue
     */
    static setValue(options?: SetBrightnessOptions): void;
    /**
     * Obtains the screen brightness adjustment mode.
     *
     * @param { GetBrightnessModeOptions } options Options for obtaining the screen brightness mode. This parameter is
     *     optional and is left blank by default.
     * @syscap SystemCapability.PowerManager.DisplayPowerManager.Lite
     * @FaAndStageModel
     * @since 3
     * @deprecated since 7
     * @reserved ["liteWearable"]
     */
    static getMode(options?: GetBrightnessModeOptions): void;
    /**
     * Sets the screen brightness adjustment mode.
     *
     * @param { SetBrightnessModeOptions } options Options for setting the screen brightness mode. This parameter is
     *     optional and is left blank by default.
     * @syscap SystemCapability.PowerManager.DisplayPowerManager.Lite
     * @FaAndStageModel
     * @since 3
     * @deprecated since 7
     * @reserved ["liteWearable"]
     */
    static setMode(options?: SetBrightnessModeOptions): void;
    /**
     * Sets whether to always keep the screen on. Call this API in **onShow()**.
     *
     * **NOTE**
     *
     * - This API is no longer maintained since API version 7 except for lite wearables. You are advised to use
     * [window.setWindowKeepScreenOn()](docroot://reference/apis-arkui/arkts-apis-window-Window.md#setwindowkeepscreenon9)
     * instead.
     *
     * - On Lite Wearables, this API can only prevent the system from turning off the screen due to inactivity
     * timeout (automatic). It cannot prevent screen-off caused by user actions (such as covering the screen) or
     * the end of the keep-screen-on period.
     *
     * @param { SetKeepScreenOnOptions } options Options for setting the screen to be steady on. This parameter is
     *     optional and is left blank by default.
     * @syscap SystemCapability.PowerManager.DisplayPowerManager.Lite
     * @FaAndStageModel
     * @since 3
     * @deprecated since 7
     * @reserved ["liteWearable"]
     * @useinstead @ohos.window:Window.setWindowKeepScreenOn
     */
    static setKeepScreenOn(options?: SetKeepScreenOnOptions): void;
}

```
