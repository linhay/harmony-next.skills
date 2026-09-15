# @ohos.nearlink.scan.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
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
import nearlinkConstant from '@ohos.nearlink.constant';
/**
 * Provides methods for scanning and discovering nearby devices.
 *
 * @syscap SystemCapability.Communication.NearLink.Base
 * @stagemodelonly
 * @since 26.0.0
 */
declare namespace scan {
    /**
     * Starts scanning for specified NearLink devices with filters.
     * It is allowed to set filter parameter to {@code null} if you do not want to use filter.
     *
     * @permission ohos.permission.ACCESS_NEARLINK
     * @param { ScanFilters[] | null } filters - The list of filters and this parameter is mandatory.
     *     If you do not want to use filter, set this parameter to {@code null}.
     *     If you want to use filter, at least one filter should be set.
     * @param { ScanOptions } [options] - The parameters for scanning, and the low power mode is used by default.
     * @returns { Promise<void> } The promise object is returned.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 801 - Capability not supported because the chip does not support it.
     * @throws { BusinessError } 36100003 - NearLink disabled.
     * @throws { BusinessError } 36100040 - Integer out of range.
     * @throws { BusinessError } 36100041 - Invalid address.
     * @throws { BusinessError } 36100042 - Empty array.
     * @throws { BusinessError } 36100099 - Operation failed.
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    function startScan(filters: ScanFilters[] | null, options?: ScanOptions): Promise<void>;
    /**
     * Stops scanning.
     *
     * @permission ohos.permission.ACCESS_NEARLINK
     * @returns { Promise<void> }
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 801 - Capability not supported because the chip does not support it.
     * @throws { BusinessError } 36100003 - NearLink disabled.
     * @throws { BusinessError } 36100099 - Operation failed.
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    function stopScan(): Promise<void>;
    /**
     * Subscribes to NearLink scan results.
     *
     * This event is accessible only to applications that granted the ohos.permission.NEARLINK_ACCESS permission.
     * If the application is granted the ohos.permission.GET_NEARLINK_PEER_MAC permission,
     * the callback returns the real device address; otherwise, a random device address is returned.
     *
     * @param { Callback<ScanResults[]> } callback - Callback used to listen for the scan result event.
     * @throws { BusinessError } 801 - Capability not supported because the chip does not support it.
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    function onDeviceFound(callback: Callback<ScanResults[]>): void;
    /**
     * Unsubscribes from NearLink scan results.
     *
     * @param { Callback<ScanResults[]> } [callback] - Callback used to listen for the scan result event.
     * @throws { BusinessError } 801 - Capability not supported because the chip does not support it.
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    function offDeviceFound(callback?: Callback<ScanResults[]>): void;
    /**
     * Describes the contents of the scan results.
     *
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    interface ScanResults {
        /**
         * Address of the remote device.
         * The length is 17, and the value consists of hexadecimal digits and colons (:), for example, 11:22:33:AA:BB:FF.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        address: string;
        /**
         * RSSI of the remote device.
         * Unit: dBm. The value is an integer within [-128,127], and the value 127 indicates an invalid RSSI.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        rssi: number;
        /**
         * The raw data.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        data: ArrayBuffer;
        /**
         * Device name of the remote device.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        deviceName: string;
        /**
         * Indicates whether the remote device is connectable.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        isConnectable: boolean;
        /**
         * Indicates the device class.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        deviceClass?: nearlinkConstant.DeviceClass;
    }
    /**
     * Describes the scan filters.
     *
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    interface ScanFilters {
        /**
         * Indicates the device address.
         * The length must be 17, The value consists of hexadecimal digits and colons (:), for example, 11:22:33:AA:BB:FF.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        address?: string;
        /**
         * Indicates the device name.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        deviceName?: string;
        /**
         * Indicates the manufacturer ID.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        manufacturerId?: number;
        /**
         * Indicates the manufacturer data.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        manufacturerData?: ArrayBuffer;
        /**
         * Indicates the manufacturer data mask.
         * If a manufacturer data mask is set in the scan filter, its length must match the manufacturer data length.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        manufacturerDataMask?: ArrayBuffer;
        /**
         * Indicates the RSSI.
         * Unit: dBm, The value must be an integer within [-128,127].
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        rssi?: number;
    }
    /**
     * Describes the parameters for scan.
     *
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    interface ScanOptions {
        /**
         * Indicates the scan mode.
         * If the "scanMode" is not set, the default value is "SCAN_MODE_LOW_POWER".
         * Default value: SCAN_MODE_LOW_POWER.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        scanMode?: ScanMode;
        /**
         * Indicates the scan duration.
         * If the "duration" is not set, the scanning is performed all the time.
         * Unit: Seconds, The value must be an integer within [10,60].
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        duration?: number;
    }
    /**
     * The enum of scan mode.
     *
     * @syscap SystemCapability.Communication.NearLink.Base
     * @stagemodelonly
     * @since 26.0.0
     */
    enum ScanMode {
        /**
         * Low-power mode with a lower scan frequency (default).
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        SCAN_MODE_LOW_POWER = 0,
        /**
         * Medium-power mode with a medium scan frequency.
         *
         * @syscap SystemCapability.Communication.NearLink.Base
         * @stagemodelonly
         * @since 26.0.0
         */
        SCAN_MODE_BALANCED = 1
    }
}
export default scan;

```
