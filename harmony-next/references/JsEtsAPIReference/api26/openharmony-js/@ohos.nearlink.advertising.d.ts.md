# @ohos.nearlink.advertising.d.ts

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
 * @kit ConnectivityKit
 */
import type { Callback } from '@ohos.base';
/**
 * Provides methods related to advertising. Nearby devices can scan and discover this device.
 *
 * @syscap SystemCapability.Communication.NearLink.Base
 * @stagemodelonly
 * @since 26.0.0
 */
declare namespace advertising {
    /**
     * Starts advertising.
     *
     * @permission ohos.permission.ACCESS_NEARLINK
     * @param { AdvertisingParams } advertisingParams - Indicates the param for advertising.
     * @returns { Promise<number> } Returns the promise object advertise handle.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 801 - Capability not supported because the chip does not support it.
     * @throws { BusinessError } 36100003 - NearLink disabled.
     * @throws { BusinessError } 36100040 - Integer out of range.
     * @throws { BusinessError } 36100043 - Invalid UUID.
     * @throws { BusinessError } 36100099 - Operation failed.
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    function startAdvertising(advertisingParams: AdvertisingParams): Promise<number>;
    /**
     * Stops advertising with advertising ID.
     *
     * @permission ohos.permission.ACCESS_NEARLINK
     * @param { number } advertisingId - Indicates the ID for this advertising
     *     <br>The value must be an integer greater than or equal to 0, The value is the current advertising ID.
     * @returns { Promise<void> } Returns the promise object.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 801 - Capability not supported because the chip does not support it.
     * @throws { BusinessError } 36100003 - NearLink disabled.
     * @throws { BusinessError } 36100040 - Invalid advertising ID.
     * @throws { BusinessError } 36100099 - Operation failed.
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    function stopAdvertising(advertisingId: number): Promise<void>;
    /**
     * Subscribes to the advertising state change event.
     *
     * This event is accessible only to applications that granted the ohos.permission.NEARLINK_ACCESS permission.
     *
     * @param { Callback<AdvertisingStateChangeInfo> } callback - Callback used to listen for the advertising state.
     * @throws { BusinessError } 801 - Capability not supported because the chip does not support it.
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    function onAdvertisingStateChange(callback: Callback<AdvertisingStateChangeInfo>): void;
    /**
     * Unsubscribes from the advertising state change event.
     *
     * @param { Callback<AdvertisingStateChangeInfo> } [callback] - Callback used to listen for the advertising state.
     * @throws { BusinessError } 801 - Capability not supported because the chip does not support it.
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    function offAdvertisingStateChange(callback?: Callback<AdvertisingStateChangeInfo>): void;
    /**
     * Describes the advertising parameters.
     *
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    interface AdvertisingParams {
        /**
         * Indicates the advertising settings.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        advertisingSettings: AdvertisingSettings;
        /**
         * Indicates the advertising data.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        advertisingData: AdvertisingData;
    }
    /**
     * Describes the settings for advertising.
     *
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    interface AdvertisingSettings {
        /**
         * Indicates the advertising interval.
         * The minimum number of slots is 160, and the corresponding time is 20 ms (160 * 0.125 ms = 20 ms).
         * The maximum number of slots is 16777215, and the corresponding time is 2097151.875 ms.
         * Unit: Slots, The value must be an integer within [160,16777215], each slot is 125 microseconds.
         * Default value: 5000.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        interval?: number;
        /**
         * Indicates the advertising power mode.
         * Default value: ADV_TX_POWER_LOW.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        power?: TxPowerMode;
        /**
         * Indicates whether the advertising is connectable.
         * Default value: true.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        isConnectable?: boolean;
    }
    /**
     * Describes the advertising data.
     *
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    interface AdvertisingData {
        /**
         * The specified service UUIDs.
         * The length of each UUID must be 36, The value consists of 36 hexadecimal digits and hyphens (-),
         * for example, FFFFFFFF-1234-5678-ABCD-000000001234, indicating a 128-bit identifier.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        serviceUuids?: string[];
        /**
         * The specified manufacturer data.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        manufacturerData?: ManufacturerData[];
        /**
         * The specified service data.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        serviceData?: ServiceData[];
        /**
         * Indicates whether the device name will be included.
         * Default value: false.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        includeDeviceName?: boolean;
    }
    /**
     * Describes the manufacturer data.
     *
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    interface ManufacturerData {
        /**
         * Indicates the manufacturer ID.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        manufacturerId: number;
        /**
         * Indicates the manufacturer data.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        manufacturerData: ArrayBuffer;
    }
    /**
     * Describes the service data.
     *
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    interface ServiceData {
        /**
         * Indicates the service UUID.
         * The length must be 36, The value consists of 36 hexadecimal digits and hyphens (-),
         * for example, FFFFFFFF-1234-5678-ABCD-000000001234, indicating a 128-bit identifier.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        serviceUuid: string;
        /**
         * Indicates the service data.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        serviceData: ArrayBuffer;
    }
    /**
     * The enum of advertising mode.
     *
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    enum TxPowerMode {
        /**
         * Low power mode.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        ADV_TX_POWER_LOW = 1,
        /**
         * Medium power mode.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        ADV_TX_POWER_MEDIUM = 2,
        /**
         * High power mode.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        ADV_TX_POWER_HIGH = 3
    }
    /**
     * Advertising state change information.
     *
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    interface AdvertisingStateChangeInfo {
        /**
         * Indicates the advertising ID.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        advertisingId: number;
        /**
         * Indicates the advertising state.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        state: AdvertisingState;
    }
    /**
     * The enum of advertising state.
     *
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    enum AdvertisingState {
        /**
         * Indicates that advertising has started.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        STARTED = 1,
        /**
         * Indicates that advertising has stopped.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        STOPPED = 2
    }
}
export default advertising;

```
