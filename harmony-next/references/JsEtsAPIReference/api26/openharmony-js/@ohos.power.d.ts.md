# @ohos.power.d.ts

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
 * @kit BasicServicesKit
 */
import { AsyncCallback } from './@ohos.base';
/**
 * The **power** module provides APIs for rebooting and shutting down the system, as well as querying the screen status.
 * You can use these APIs to obtain the device activity status, power mode, and screen on/off status.
 *
 * @syscap SystemCapability.PowerManager.PowerManager.Core
 * @since 7
 */
declare namespace power {
    /**
     * Restarts the system.
     *
     * @permission ohos.permission.REBOOT
     * @param { string } reason - Indicates the restart reason. For example, "updater" indicates entering the updater mode
     *     after the restart. If the parameter is not specified, the system enters the normal mode after the restart.
     * @syscap SystemCapability.PowerManager.PowerManager.Core
     * @since 7
     * @deprecated since 9
     * @useinstead power.reboot
     */
    function rebootDevice(reason: string): void;
    /**
     * Checks the screen status of the current device. This API uses an asynchronous callback to return the result.
     *
     * @param { AsyncCallback<boolean> } callback - Callback used to return the result. If the operation is successful,
     *     **err** is **undefined** and **data** is the screen status obtained, where the value **true** indicates on and
     *     the value **false** indicates off. Otherwise, **err** is an error object.
     * @syscap SystemCapability.PowerManager.PowerManager.Core
     * @since 7
     * @deprecated since 9
     * @useinstead power.isActive
     */
    function isScreenOn(callback: AsyncCallback<boolean>): void;
    /**
     * Checks the screen status of the current device. This API uses a promise to return the result.
     *
     * @returns { Promise<boolean> } Returns true if the screen is on; returns false otherwise.
     * @syscap SystemCapability.PowerManager.PowerManager.Core
     * @since 7
     * @deprecated since 9
     * @useinstead power.isActive
     */
    function isScreenOn(): Promise<boolean>;
    /**
     * Checks whether the current device is active.
     *
     * - A device with a screen is active when the screen is on and inactive when the screen is off.
     * - A device without a screen is active when it exits the sleep mode and inactive when it enters the sleep mode.
     *
     * @returns { boolean } Return value **true** if the device is active; returns **false** otherwise.
     * @syscap SystemCapability.PowerManager.PowerManager.Core
     * @since 9
     */
    function isActive(): boolean;
    /**
     * Obtains the power mode of this device.
     *
     * @returns { DevicePowerMode } Power mode.
     * @syscap SystemCapability.PowerManager.PowerManager.Core
     * @since 9
     */
    function getPowerMode(): DevicePowerMode;
    /**
     * Checks whether the device is in standby mode.
     *
     * @returns { boolean } The value **true** indicates that the device is in standby mode, and the value **false**
     *     indicates the opposite.
     * @throws { BusinessError } 4900101 - Failed to connect to the service.
     * @syscap SystemCapability.PowerManager.PowerManager.Core
     * @since 10
     */
    function isStandby(): boolean;
    /**
     * Enumerates power modes.
     *
     * @syscap SystemCapability.PowerManager.PowerManager.Core
     * @since 9
     */
    export enum DevicePowerMode {
        /**
         * Standard mode. It is the default value.
         *
         * @syscap SystemCapability.PowerManager.PowerManager.Core
         * @since 9
         */
        MODE_NORMAL = 600,
        /**
         * Power saving mode.
         *
         * @syscap SystemCapability.PowerManager.PowerManager.Core
         * @since 9
         */
        MODE_POWER_SAVE,
        /**
         * Performance mode.
         *
         * @syscap SystemCapability.PowerManager.PowerManager.Core
         * @since 9
         */
        MODE_PERFORMANCE,
        /**
         * Ultra power saving mode.
         *
         * @syscap SystemCapability.PowerManager.PowerManager.Core
         * @since 9
         */
        MODE_EXTREME_POWER_SAVE,
        /**
         * Custom power saving mode.
         *
         * @syscap SystemCapability.PowerManager.PowerManager.Core
         * @since 20
         */
        MODE_CUSTOM_POWER_SAVE = 650
    }
    /**
     * Enumerates the power key filtering strategies.
     *
     * @syscap SystemCapability.PowerManager.PowerManager.Core
     * @since 21
     */
    export enum PowerKeyFilteringStrategy {
        /**
         * Disable the filtering of power key long-press event. This is the default value.
         *
         * @syscap SystemCapability.PowerManager.PowerManager.Core
         * @since 21
         */
        DISABLE_LONG_PRESS_FILTERING = 0,
        /**
         * Filters the current power key long-press event once. Subsequent long-press events are not filtered by default.
         *
         * @syscap SystemCapability.PowerManager.PowerManager.Core
         * @since 21
         */
        LONG_PRESS_FILTERING_ONCE = 1
    }
}
export default power;

```
