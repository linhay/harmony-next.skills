# @system.battery.d.ts

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
 * The **battery** module allows you to query the charging status and remaining power of a device.
 *
 * > **NOTE**
 * >
 * > - Module maintenance policy:
 * >
 * >    - For lite wearables, this module is constantly maintained and available.
 * >
 * >    - For other device types, this module is no longer maintained since API version 6. You are advised to use
 * > [@ohos.batteryInfo]{@link @ohos.batteryInfo:batteryInfo} instead.
 *
 */
/**
 * Defines a response that returns the charging status and remaining power of the device.
 *
 * @syscap SystemCapability.PowerManager.BatteryManager.Lite
 * @FaAndStageModel
 * @since 3
 * @deprecated since 6
 * @reserved ["liteWearable"]
 */
export interface BatteryResponse {
    /**
     * Whether the battery is being charged. The value **true** indicates that the battery is being charged; **false**
     * indicates the opposite. The default value is **false**.
     *
     * Note: This API is no longer maintained since API version 6 except for lite wearables. You are advised to use
     * [batteryInfo.chargingStatus](docroot://reference/apis-basic-services-kit/js-apis-battery-info.md#constants)
     * instead.
     *
     * @syscap SystemCapability.PowerManager.BatteryManager.Lite
     * @FaAndStageModel
     * @since 3
     * @deprecated since 6
     * @reserved ["liteWearable"]
     * @useinstead @ohos.batteryInfo:batteryInfo.chargingStatus
     */
    charging: boolean;
    /**
     * Current battery level in percent, which ranges from **0.00** to **1.00**.
     *
     * Note: This API is no longer maintained since API version 6 except for lite wearables. You are advised to use
     * [batteryInfo.batterySOC](docroot://reference/apis-basic-services-kit/js-apis-battery-info.md#constants) instead.
     *
     * @syscap SystemCapability.PowerManager.BatteryManager.Lite
     * @FaAndStageModel
     * @since 3
     * @deprecated since 6
     * @reserved ["liteWearable"]
     * @useinstead @ohos.batteryInfo:batteryInfo.batterySOC
     */
    level: number;
}
/**
 * Object that contains the API calling result.
 *
 * @syscap SystemCapability.PowerManager.BatteryManager.Lite
 * @FaAndStageModel
 * @since 3
 * @deprecated since 6
 * @reserved ["liteWearable"]
 */
export interface GetStatusOptions {
    /**
     * Called when an API call is successful. **data** is a return value of the
     *     {@link BatteryResponse} type.
     *
     * @syscap SystemCapability.PowerManager.BatteryManager.Lite
     * @FaAndStageModel
     * @since 3
     * @deprecated since 6
     * @reserved ["liteWearable"]
     */
    success?: (data: BatteryResponse) => void;
    /**
     * Called when an API call has failed. **data** indicates the error information, and **code** indicates the error
     *     code.
     *
     * @syscap SystemCapability.PowerManager.BatteryManager.Lite
     * @FaAndStageModel
     * @since 3
     * @deprecated since 6
     * @reserved ["liteWearable"]
     */
    fail?: (data: string, code: number) => void;
    /**
     * Called when an API call is complete.
     *
     * @syscap SystemCapability.PowerManager.BatteryManager.Lite
     * @FaAndStageModel
     * @since 3
     * @deprecated since 6
     * @reserved ["liteWearable"]
     */
    complete?: () => void;
}
/**
 * The module allows you to query the charging status and remaining power of a device.
 *
 * @syscap SystemCapability.PowerManager.BatteryManager.Lite
 * @FaAndStageModel
 * @since 3
 * @deprecated since 6
 * @reserved ["liteWearable"]
 */
export default class Battery {
    /**
     * Obtains the current charging state and battery level.
     *
     * @param { GetStatusOptions } options Object that contains the API calling result. This parameter is optional and
     *     is left blank by default.
     * @syscap SystemCapability.PowerManager.BatteryManager.Lite
     * @FaAndStageModel
     * @since 3
     * @deprecated since 6
     * @reserved ["liteWearable"]
     */
    static getStatus(options?: GetStatusOptions): void;
}

```
