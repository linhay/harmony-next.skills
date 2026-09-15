# @system.device.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2020 Huawei Device Co., Ltd.
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
 *
 * @syscap SystemCapability.Startup.SystemInfo.Lite
 * @FaAndStageModel
 * @since 3
 * @deprecated since 6
 * @reserved ["liteWearable"]
 */
export interface DeviceResponse {
    /**
     * Brand.
     *
     * @syscap SystemCapability.Startup.SystemInfo.Lite
     * @FaAndStageModel
     * @since 3
     * @deprecated since 6
     * @reserved ["liteWearable"]
     */
    brand: string;
    /**
     * Manufacturer.
     *
     * @syscap SystemCapability.Startup.SystemInfo.Lite
     * @FaAndStageModel
     * @since 3
     * @deprecated since 6
     * @reserved ["liteWearable"]
     */
    manufacturer: string;
    /**
     * Model.
     *
     * @syscap SystemCapability.Startup.SystemInfo.Lite
     * @FaAndStageModel
     * @since 3
     * @deprecated since 6
     * @reserved ["liteWearable"]
     */
    model: string;
    /**
     * Product number.
     *
     * @syscap SystemCapability.Startup.SystemInfo.Lite
     * @FaAndStageModel
     * @since 3
     * @deprecated since 6
     * @reserved ["liteWearable"]
     */
    product: string;
    /**
     * System language.
     *
     * @syscap SystemCapability.Startup.SystemInfo.Lite
     * @FaAndStageModel
     * @since 4
     * @deprecated since 6
     * @reserved ["liteWearable"]
     */
    language: string;
    /**
     * System region.
     *
     * @syscap SystemCapability.Startup.SystemInfo.Lite
     * @FaAndStageModel
     * @since 4
     * @deprecated since 6
     * @reserved ["liteWearable"]
     */
    region: string;
    /**
     * Window width, unit px.
     *
     * @syscap SystemCapability.Startup.SystemInfo.Lite
     * @FaAndStageModel
     * @since 3
     * @deprecated since 6
     * @reserved ["liteWearable"]
     */
    windowWidth: number;
    /**
     * Window Height, unit px.
     *
     * @syscap SystemCapability.Startup.SystemInfo.Lite
     * @FaAndStageModel
     * @since 3
     * @deprecated since 6
     * @reserved ["liteWearable"]
     */
    windowHeight: number;
    /**
     * Screen density, unit dpi.
     *
     * @syscap SystemCapability.Startup.SystemInfo.Lite
     * @FaAndStageModel
     * @since 4
     * @deprecated since 6
     * @reserved ["liteWearable"]
     */
    screenDensity: number;
    /**
     * Screen shape. The options are as follows:
     * rect: Rectangle screen.
     * circle: Circle screen.
     *
     * @syscap SystemCapability.Startup.SystemInfo.Lite
     * @FaAndStageModel
     * @since 4
     * @deprecated since 6
     * @reserved ["liteWearable"]
     */
    screenShape: 'rect' | 'circle';
    /**
     * API version.
     *
     * @syscap SystemCapability.Startup.SystemInfo.Lite
     * @FaAndStageModel
     * @since 4
     * @deprecated since 6
     * @reserved ["liteWearable"]
     */
    apiVersion: number;
    /**
     * Minor API version of the system software.
     * From API 26 and later versions, the system API version format is
     * sdkApiVersion.sdkMinorApiVersion.sdkPatchApiVersion.
     * Example: 26.0.0
     * Value range: (-∞,+∞).
     *
     * @syscap SystemCapability.Startup.SystemInfo.Lite
     * @famodelonly
     * @since 26.0.0
     * @deprecated since 26.0.0
     * @reserved ["liteWearable"]
     */
    sdkMinorApiVersion?: number;
    /**
     * Minor API version of the system software.
     * From API 26 and later versions, the system API version format is
     * sdkApiVersion.sdkMinorApiVersion.sdkPatchApiVersion.
     * Example: 26.0.0
     * Value range: (-∞,+∞).
     *
     * @syscap SystemCapability.Startup.SystemInfo.Lite
     * @famodelonly
     * @since 26.0.0
     * @deprecated since 26.0.0
     * @reserved ["liteWearable"]
     */
    sdkPatchApiVersion?: number;
    /**
     * Device type. The options are as follows:
     * phone: smartphone
     * tablet: tablet
     * tv: smart TV
     * wearable: wearable
     * liteWearable: lite wearable
     * ar: AR
     * vr: virtual reality
     * earphones: headset
     * pc: personal computer
     * speaker: speaker
     * smartVision: smart visual device
     * linkIoT: connection module
     *
     * @syscap SystemCapability.Startup.SystemInfo.Lite
     * @FaAndStageModel
     * @since 4
     * @deprecated since 6
     * @reserved ["liteWearable"]
     */
    deviceType: string;
}
/**
 *
 * @syscap SystemCapability.Startup.SystemInfo.Lite
 * @FaAndStageModel
 * @since 3
 * @deprecated since 6
 * @reserved ["liteWearable"]
 */
export interface GetDeviceOptions {
    /**
     * Called when the device information is obtained.
     *
     * @syscap SystemCapability.Startup.SystemInfo.Lite
     * @FaAndStageModel
     * @since 3
     * @deprecated since 6
     * @reserved ["liteWearable"]
     */
    success?: (data: DeviceResponse) => void;
    /**
     * Called when the device information fails to be obtained.
     *
     * @syscap SystemCapability.Startup.SystemInfo.Lite
     * @FaAndStageModel
     * @since 3
     * @deprecated since 6
     * @reserved ["liteWearable"]
     */
    fail?: (data: any, code: number) => void;
    /**
     * Called when the execution is completed.
     *
     * @syscap SystemCapability.Startup.SystemInfo.Lite
     * @FaAndStageModel
     * @since 3
     * @deprecated since 6
     * @reserved ["liteWearable"]
     */
    complete?: () => void;
}
/**
 * getInfo interface
 *
 * @syscap SystemCapability.Startup.SystemInfo.Lite
 * @FaAndStageModel
 * @since 3
 * @deprecated since 6
 * @reserved ["liteWearable"]
 */
export default class Device {
    /**
     * Obtains the device information.
     *
     * @param { GetDeviceOptions } options - Options
     * @syscap SystemCapability.Startup.SystemInfo.Lite
     * @FaAndStageModel
     * @since 3
     * @deprecated since 6
     * @reserved ["liteWearable"]
     */
    static getInfo(options?: GetDeviceOptions): void;
}

```
