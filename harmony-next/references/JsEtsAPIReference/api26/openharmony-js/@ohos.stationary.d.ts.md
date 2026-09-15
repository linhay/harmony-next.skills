# @ohos.stationary.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022 Huawei Device Co., Ltd.
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
 * @kit MultimodalAwarenessKit
 */
import type { Callback } from './@ohos.base';
/**
 * The **stationary** module provides APIs to report the device status, including absolute still and relative still.
 *
 * > **NOTE**
 * >
 * > This module does not support x86 emulators.
 *
 * @syscap SystemCapability.Msdp.DeviceStatus.Stationary
 * @since 9
 */
declare namespace stationary {
    /**
     * Defines the response interface to receive the device status.
     *
     * @syscap SystemCapability.Msdp.DeviceStatus.Stationary
     * @since 9
     */
    interface ActivityResponse {
        /**
         * New device status.
         *
         * @syscap SystemCapability.Msdp.DeviceStatus.Stationary
         * @since 9
         */
        state: ActivityState;
    }
    /**
     * Enumerates the device status types.
     *
     * @syscap SystemCapability.Msdp.DeviceStatus.Stationary
     * @unionmember { 'still' } Absolutely still.
     * @unionmember { 'relativeStill' } Relatively still.
     * @since 9
     */
    type ActivityType = 'still' | 'relativeStill';
    /**
     * Enumerates the device status events.
     *
     * @syscap SystemCapability.Msdp.DeviceStatus.Stationary
     * @since 9
     */
    enum ActivityEvent {
        /**
         * Enter event.
         *
         * @syscap SystemCapability.Msdp.DeviceStatus.Stationary
         * @since 9
         */
        ENTER = 1,
        /**
         * Exit event.
         *
         * @syscap SystemCapability.Msdp.DeviceStatus.Stationary
         * @since 9
         */
        EXIT = 2,
        /**
         * Enter and exit events.
         *
         * @syscap SystemCapability.Msdp.DeviceStatus.Stationary
         * @since 9
         */
        ENTER_EXIT = 3
    }
    /**
     * Enumerates the device statuses.
     *
     * @syscap SystemCapability.Msdp.DeviceStatus.Stationary
     * @since 9
     */
    enum ActivityState {
        /**
         * Enter state.
         *
         * @syscap SystemCapability.Msdp.DeviceStatus.Stationary
         * @since 9
         */
        ENTER = 1,
        /**
         * Exit state.
         *
         * @syscap SystemCapability.Msdp.DeviceStatus.Stationary
         * @since 9
         */
        EXIT = 2
    }
    /**
     * Subscribes to the device status.
     *
     * @param { ActivityType } activity - Device status type.
     * @param { ActivityEvent } event - Event type.
     * @param { number } reportLatencyNs - Report delay, in ns. The value ranges from **1000000000** to **3000000000**.
     * @param { Callback<ActivityResponse> } callback - Callback used to receive reported data.
     * @syscap SystemCapability.Msdp.DeviceStatus.Stationary
     * @since 9
     */
    function on(activity: ActivityType, event: ActivityEvent, reportLatencyNs: number, callback: Callback<ActivityResponse>): void;
    /**
     * Obtains the device status.
     *
     * @param { ActivityType } activity - Device status type.
     * @param { Callback<ActivityResponse> } callback - Callback used to receive reported data.
     * @syscap SystemCapability.Msdp.DeviceStatus.Stationary
     * @since 9
     */
    function once(activity: ActivityType, callback: Callback<ActivityResponse>): void;
    /**
     * Unsubscribes from the device status.
     *
     * @param { ActivityType } activity - Device status type.
     * @param { ActivityEvent } event - Event type.
     * @param { Callback<ActivityResponse> } [callback] - Callback used to receive reported data. If no value or
     *     **undefined** is passed, all callbacks associated with the specified event in the process will be unregistered.
     * @syscap SystemCapability.Msdp.DeviceStatus.Stationary
     * @since 9
     */
    function off(activity: ActivityType, event: ActivityEvent, callback?: Callback<ActivityResponse>): void;
}
export default stationary;

```
