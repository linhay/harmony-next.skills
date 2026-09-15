# @ohos.batteryInfo.d.ts

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
/**
 * The **batteryInfo** module provides APIs for querying the charger type, battery health status, and battery charging
 * status.
 *
 * @syscap SystemCapability.PowerManager.BatteryManager.Core
 * @atomicservice [since 12]
 * @since 6
 */
declare namespace batteryInfo {
    /**
     * Battery state of charge (SoC) of the device, in unit of percentage, which ranges from 0 to 100.
     *
     * @syscap SystemCapability.PowerManager.BatteryManager.Core
     * @atomicservice [since 12]
     * @since 6
     */
    const batterySOC: number;
    /**
     * Battery charging state of the current device.
     *
     * @syscap SystemCapability.PowerManager.BatteryManager.Core
     * @atomicservice [since 12]
     * @since 6
     */
    const chargingStatus: BatteryChargeState;
    /**
     * Battery health status of the device.
     *
     * @syscap SystemCapability.PowerManager.BatteryManager.Core
     * @since 6
     */
    const healthStatus: BatteryHealthState;
    /**
     * Charger type of the device.
     *
     * @syscap SystemCapability.PowerManager.BatteryManager.Core
     * @since 6
     */
    const pluggedType: BatteryPluggedType;
    /**
     * Battery voltage of the device, in unit of microvolt.
     *
     * @syscap SystemCapability.PowerManager.BatteryManager.Core
     * @since 6
     */
    const voltage: number;
    /**
     * Battery technology of the device.
     *
     * @syscap SystemCapability.PowerManager.BatteryManager.Core
     * @since 6
     */
    const technology: string;
    /**
     * Battery temperature of the device, in unit of 0.1°C.
     *
     * @syscap SystemCapability.PowerManager.BatteryManager.Core
     * @since 6
     */
    const batteryTemperature: number;
    /**
     * Whether the battery is supported or present. The value **true** means that the battery is supported or present;
     * **false** means the opposite.
     *
     * Default value: **false**.
     *
     * @syscap SystemCapability.PowerManager.BatteryManager.Core
     * @since 7
     */
    const isBatteryPresent: boolean;
    /**
     * Battery level of the device.
     *
     * @syscap SystemCapability.PowerManager.BatteryManager.Core
     * @since 9
     */
    const batteryCapacityLevel: BatteryCapacityLevel;
    /**
     * Battery current of the device, in unit of mA.
     *
     * @syscap SystemCapability.PowerManager.BatteryManager.Core
     * @since 12
     */
    const nowCurrent: number;
    /**
     * Enumerates charger types.
     *
     * @syscap SystemCapability.PowerManager.BatteryManager.Core
     * @since 6
     */
    export enum BatteryPluggedType {
        /**
         * Unknown charger type.
         *
         * @syscap SystemCapability.PowerManager.BatteryManager.Core
         * @since 6
         */
        NONE,
        /**
         * AC charger.
         *
         * @syscap SystemCapability.PowerManager.BatteryManager.Core
         * @since 6
         */
        AC,
        /**
         * USB charger.
         *
         * @syscap SystemCapability.PowerManager.BatteryManager.Core
         * @since 6
         */
        USB,
        /**
         * Wireless charger.
         *
         * @syscap SystemCapability.PowerManager.BatteryManager.Core
         * @since 6
         */
        WIRELESS
    }
    /**
     * Enumerates charging states.
     *
     * @syscap SystemCapability.PowerManager.BatteryManager.Core
     * @atomicservice [since 12]
     * @since 6
     */
    export enum BatteryChargeState {
        /**
         * Unknown state.
         *
         * @syscap SystemCapability.PowerManager.BatteryManager.Core
         * @atomicservice [since 12]
         * @since 6
         */
        NONE,
        /**
         * The battery is being charged.
         *
         * @syscap SystemCapability.PowerManager.BatteryManager.Core
         * @atomicservice [since 12]
         * @since 6
         */
        ENABLE,
        /**
         * The battery is not being charged.
         *
         * @syscap SystemCapability.PowerManager.BatteryManager.Core
         * @atomicservice [since 12]
         * @since 6
         */
        DISABLE,
        /**
         * The battery is fully charged.
         *
         * @syscap SystemCapability.PowerManager.BatteryManager.Core
         * @atomicservice [since 12]
         * @since 6
         */
        FULL
    }
    /**
     * Enumerates battery health states.
     *
     * @syscap SystemCapability.PowerManager.BatteryManager.Core
     * @since 6
     */
    export enum BatteryHealthState {
        /**
         * Unknown state.
         *
         * @syscap SystemCapability.PowerManager.BatteryManager.Core
         * @since 6
         */
        UNKNOWN,
        /**
         * The battery is in the healthy state.
         *
         * @syscap SystemCapability.PowerManager.BatteryManager.Core
         * @since 6
         */
        GOOD,
        /**
         * The battery is overheated.
         *
         * @syscap SystemCapability.PowerManager.BatteryManager.Core
         * @since 6
         */
        OVERHEAT,
        /**
         * The battery voltage is over high.
         *
         * @syscap SystemCapability.PowerManager.BatteryManager.Core
         * @since 6
         */
        OVERVOLTAGE,
        /**
         * The battery temperature is low.
         *
         * @syscap SystemCapability.PowerManager.BatteryManager.Core
         * @since 6
         */
        COLD,
        /**
         * The battery is dead.
         *
         * @syscap SystemCapability.PowerManager.BatteryManager.Core
         * @since 6
         */
        DEAD
    }
    /**
     * Enumerates battery levels.
     *
     * @syscap SystemCapability.PowerManager.BatteryManager.Core
     * @since 9
     */
    export enum BatteryCapacityLevel {
        /**
         * Unknown battery level.
         *
         * @syscap SystemCapability.PowerManager.BatteryManager.Core
         * @since 23
         */
        LEVEL_NONE,
        /**
         * Full battery level.
         *
         * @syscap SystemCapability.PowerManager.BatteryManager.Core
         * @since 9
         */
        LEVEL_FULL,
        /**
         * High battery level.
         *
         * @syscap SystemCapability.PowerManager.BatteryManager.Core
         * @since 9
         */
        LEVEL_HIGH,
        /**
         * Normal battery level.
         *
         * @syscap SystemCapability.PowerManager.BatteryManager.Core
         * @since 9
         */
        LEVEL_NORMAL,
        /**
         * Low battery level.
         *
         * @syscap SystemCapability.PowerManager.BatteryManager.Core
         * @since 9
         */
        LEVEL_LOW,
        /**
         * Alarm battery level.
         *
         * @syscap SystemCapability.PowerManager.BatteryManager.Core
         * @since 9
         */
        LEVEL_WARNING,
        /**
         * Ultra-low battery level.
         *
         * @syscap SystemCapability.PowerManager.BatteryManager.Core
         * @since 9
         */
        LEVEL_CRITICAL,
        /**
         * Power-down battery level.
         *
         * @syscap SystemCapability.PowerManager.BatteryManager.Core
         * @since 9
         */
        LEVEL_SHUTDOWN
    }
    /**
     * Enumerates keys for querying the additional information about the **COMMON_EVENT_BATTERY_CHANGED** event.
     *
     * @syscap SystemCapability.PowerManager.BatteryManager.Core
     * @since 9
     */
    export enum CommonEventBatteryChangedKey {
        /**
         * Remaining battery level in percentage.
         *
         * @syscap SystemCapability.PowerManager.BatteryManager.Core
         * @since 9
         */
        EXTRA_SOC = 'soc',
        /**
         * Battery charging status of the device.
         *
         * @syscap SystemCapability.PowerManager.BatteryManager.Core
         * @since 9
         */
        EXTRA_CHARGE_STATE = 'chargeState',
        /**
         * Battery health status of the device.
         *
         * @syscap SystemCapability.PowerManager.BatteryManager.Core
         * @since 9
         */
        EXTRA_HEALTH_STATE = 'healthState',
        /**
         * Type of the charger connected to the device.
         *
         * @syscap SystemCapability.PowerManager.BatteryManager.Core
         * @since 9
         */
        EXTRA_PLUGGED_TYPE = 'pluggedType',
        /**
         * Battery voltage of the device.
         *
         * @syscap SystemCapability.PowerManager.BatteryManager.Core
         * @since 9
         */
        EXTRA_VOLTAGE = 'voltage',
        /**
         * Battery technology of the device.
         *
         * @syscap SystemCapability.PowerManager.BatteryManager.Core
         * @since 9
         */
        EXTRA_TECHNOLOGY = 'technology',
        /**
         * Battery temperature of the device.
         *
         * @syscap SystemCapability.PowerManager.BatteryManager.Core
         * @since 9
         */
        EXTRA_TEMPERATURE = 'temperature',
        /**
         * Whether the battery is supported by the device or installed.
         *
         * @syscap SystemCapability.PowerManager.BatteryManager.Core
         * @since 9
         */
        EXTRA_PRESENT = 'present',
        /**
         * Battery level of the device.
         *
         * @syscap SystemCapability.PowerManager.BatteryManager.Core
         * @since 9
         */
        EXTRA_CAPACITY_LEVEL = 'capacityLevel'
    }
}
export default batteryInfo;

```
