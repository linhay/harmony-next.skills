# @ohos.multimodalAwareness.deviceStatus.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2025 Huawei Device Co., Ltd.
 * Licensed under the Apache License, Version 2.0 (the "License"),
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
import type { Callback } from "./@ohos.base";
/**
 * The **deviceStatus** module provides the device status awareness functionality.
 *
 * @syscap SystemCapability.MultimodalAwareness.DeviceStatus
 * @since 18
 */
declare namespace deviceStatus {
    /**
     * Defines the steady standing state (that is, stand mode).
     *
     * A device enters stand mode when it is stationary, and its screen is at an angle between 45 and 135 degrees relative
     * to the horizontal plane. For foldable smartphones, the device must be in a folded state or fully unfolded state.
     *
     * @syscap SystemCapability.MultimodalAwareness.DeviceStatus
     * @since 18
     */
    export enum SteadyStandingStatus {
        /**
         * Exit of the stand mode.
         *
         * @syscap SystemCapability.MultimodalAwareness.DeviceStatus
         * @since 18
         */
        STATUS_EXIT = 0,
        /**
         * Entry to the stand mode.
         *
         * @syscap SystemCapability.MultimodalAwareness.DeviceStatus
         * @since 18
         */
        STATUS_ENTER = 1
    }
    /**
     * Subscribes to steady standing state events.
     *
     * @param { 'steadyStandingDetect' } type - Event type. This field has a fixed value of **steadyStandingDetect**.
     * @param { Callback<SteadyStandingStatus> } callback - Callback used to return the steady standing state of the
     *     device.
     * @throws { BusinessError } 801 - Capability not supported. Function can not work correctly due to limited
     * <br> device capabilities.
     * @throws { BusinessError } 32500001 - Service exception.
     * @throws { BusinessError } 32500002 - Subscription failed.
     * @syscap SystemCapability.MultimodalAwareness.DeviceStatus
     * @since 18
     */
    function on(type: 'steadyStandingDetect', callback: Callback<SteadyStandingStatus>): void;
    /**
     * Unsubscribes from steady standing state events.
     *
     * @param { 'steadyStandingDetect' } type - Event type. This field has a fixed value of **steadyStandingDetect**.
     * @param { Callback<SteadyStandingStatus> } [callback] - Callback used to return the steady standing state of the
     *     device.
     * @throws { BusinessError } 801 - Capability not supported. Function can not work correctly due to limited
     * <br> device capabilities.
     * @throws { BusinessError } 32500001 - Service exception.
     * @throws { BusinessError } 32500003 - Unsubscription failed.
     * @syscap SystemCapability.MultimodalAwareness.DeviceStatus
     * @since 18
     */
    function off(type: 'steadyStandingDetect', callback?: Callback<SteadyStandingStatus>): void;
}
export default deviceStatus;

```
