# @ohos.multimodalAwareness.motion.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2025 Huawei Device Co., Ltd.
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
import type { Callback } from "./@ohos.base";
/**
 * The **motion** module provides the user motion awareness capabilities, including user gestures and actions.
 *
 * @syscap SystemCapability.MultimodalAwareness.Motion
 * @since 15
 */
declare namespace motion {
    /**
     * Defines the status of the operating hand.
     *
     * @syscap SystemCapability.MultimodalAwareness.Motion
     * @since 15
     */
    export enum OperatingHandStatus {
        /**
         * Unknown status.
         *
         * @syscap SystemCapability.MultimodalAwareness.Motion
         * @since 15
         */
        UNKNOWN_STATUS = 0,
        /**
         * Left hand in use.
         *
         * @syscap SystemCapability.MultimodalAwareness.Motion
         * @since 15
         */
        LEFT_HAND_OPERATED = 1,
        /**
         * Right hand in use.
         *
         * @syscap SystemCapability.MultimodalAwareness.Motion
         * @since 15
         */
        RIGHT_HAND_OPERATED = 2
    }
    /**
     * Represents the holding hand status. The holding hand status is returned if listening for holding hand status
     * changes is enabled.
     *
     * @syscap SystemCapability.MultimodalAwareness.Motion
     * @since 20
     */
    export enum HoldingHandStatus {
        /**
         * No holding.
         *
         * @syscap SystemCapability.MultimodalAwareness.Motion
         * @since 20
         */
        NOT_HELD = 0,
        /**
         * Holding with the left hand.
         *
         * @syscap SystemCapability.MultimodalAwareness.Motion
         * @since 20
         */
        LEFT_HAND_HELD = 1,
        /**
         * Holding with the right hand.
         *
         * @syscap SystemCapability.MultimodalAwareness.Motion
         * @since 20
         */
        RIGHT_HAND_HELD = 2,
        /**
         * Holding with both hands.
         *
         * @syscap SystemCapability.MultimodalAwareness.Motion
         * @since 20
         */
        BOTH_HANDS_HELD = 3,
        /**
         * Unknown status.
         *
         * @syscap SystemCapability.MultimodalAwareness.Motion
         * @since 20
         */
        UNKNOWN_STATUS = 16
    }
    /**
     * Subscribes to operating hand change events.
     *
     * If the device does not support this function, error code 801 is returned.
     *
     * @permission ohos.permission.ACTIVITY_MOTION [since 15 - 19]
     * @permission ohos.permission.ACTIVITY_MOTION or ohos.permission.DETECT_GESTURE [since 20]
     * @param { 'operatingHandChanged' } type - Event type. This parameter has a fixed value of **operatingHandChanged**.
     * @param { Callback<OperatingHandStatus> } callback - Callback used to return the result.
     * @throws { BusinessError } 201 - Permission denied. An attempt was made to subscribe operatingHandChanged
     *     <br> event forbidden by permission: ohos.permission.ACTIVITY_MOTION or ohos.permission.DETECT_GESTURE.
     * @throws { BusinessError } 401 - Parameter error. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported. Function can not work correctly due to limited
     *     <br> device capabilities.
     * @throws { BusinessError } 31500001 - Service exception. Possible causes: 1. A system error, such as null pointer,
     *     container-related exception;
     *     <br> 2. N-API invocation exception, invalid N-API status.
     * @throws { BusinessError } 31500002 - Subscription failed. Possible causes: 1. Callback registration failure;
     *     <br> 2. Failed to bind native object to js wrapper; 3. N-API invocation exception, invalid N-API status; 4. IPC
     *     request exception.
     * @syscap SystemCapability.MultimodalAwareness.Motion
     * @since 15
     */
    function on(type: 'operatingHandChanged', callback: Callback<OperatingHandStatus>): void;
    /**
     * Unsubscribes from operating hand change events.
     *
     * @permission ohos.permission.ACTIVITY_MOTION [since 15 - 19]
     * @permission ohos.permission.ACTIVITY_MOTION or ohos.permission.DETECT_GESTURE [since 20]
     * @param { 'operatingHandChanged' } type - Event type. This parameter has a fixed value of **operatingHandChanged**.
     * @param { Callback<OperatingHandStatus> } [callback] - Callback used to return the result.
     * @throws { BusinessError } 201 - Permission denied. An attempt was made to unsubscribe operatingHandChanged
     *     <br> event forbidden by permission: ohos.permission.ACTIVITY_MOTION or ohos.permission.DETECT_GESTURE.
     * @throws { BusinessError } 401 - Parameter error. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported. Function can not work correctly due to limited
     *     <br> device capabilities.
     * @throws { BusinessError } 31500001 - Service exception. Possible causes: 1. A system error, such as null pointer,
     *     container-related exception;
     *     <br> 2. N-API invocation exception, invalid N-API status.
     * @throws { BusinessError } 31500003 - Unsubscription failed. Possible causes: 1. Callback failure;
     *     <br> 2. N-API invocation exception, invalid N-API status; 3. IPC request exception.
     * @syscap SystemCapability.MultimodalAwareness.Motion
     * @since 15
     */
    function off(type: 'operatingHandChanged', callback?: Callback<OperatingHandStatus>): void;
    /**
     * Obtains the latest operating hand status.
     *
     * @permission ohos.permission.ACTIVITY_MOTION [since 15 - 19]
     * @permission ohos.permission.ACTIVITY_MOTION or ohos.permission.DETECT_GESTURE [since 20]
     * @returns { OperatingHandStatus } Status of the operating hand.
     * @throws { BusinessError } 201 - Permission denied. An attempt was made to get the recent operating hand
     *     <br> status forbidden by permission: ohos.permission.ACTIVITY_MOTION or ohos.permission.DETECT_GESTURE.
     * @throws { BusinessError } 801 - Capability not supported. Function can not work correctly due to limited
     *     <br> device capabilities.
     * @throws { BusinessError } 31500001 - Service exception. Possible causes: 1. A system error, such as null pointer,
     *     container-related exception;
     *     <br> 2. N-API invocation exception, invalid N-API status.
     * @syscap SystemCapability.MultimodalAwareness.Motion
     * @since 15
     */
    function getRecentOperatingHandStatus(): OperatingHandStatus;
    /**
     * Enables listening for holding hand status changes.
     *
     * @permission ohos.permission.DETECT_GESTURE
     * @param { 'holdingHandChanged' } type - Event type. The value **holdingHandChanged** indicates the holding hand
     *     status change event.
     * @param { Callback<HoldingHandStatus> } callback - Callback used to return the holding hand status.
     * @throws { BusinessError } 201 - Permission denied. An attempt was made to subscribe holdingHandChanged
     *     <br> event forbidden by permission: ohos.permission.DETECT_GESTURE.
     * @throws { BusinessError } 801 - Capability not supported. Function can not work correctly due to limited
     *     <br> device capabilities.
     * @throws { BusinessError } 31500001 - Service exception. Possible causes: 1. A system error, such as null pointer,
     *     container-related exception;
     *     <br> 2. N-API invocation exception, invalid N-API status.
     * @throws { BusinessError } 31500002 - Subscription failed. Possible causes: 1. Callback registration failure;
     *     <br> 2. Failed to bind native object to js wrapper; 3. N-API invocation exception, invalid N-API status; 4. IPC
     *     request exception.
     * @syscap SystemCapability.MultimodalAwareness.Motion
     * @since 20
     */
    function on(type: 'holdingHandChanged', callback: Callback<HoldingHandStatus>): void;
    /**
     * Disables listening for holding hand status changes.
     *
     * @permission ohos.permission.DETECT_GESTURE
     * @param { 'holdingHandChanged' } type - Event type. The value **holdingHandChanged** indicates the holding hand
     *     status change event.
     * @param { Callback<HoldingHandStatus> } [callback] - Callback to unregister. If this parameter is not passed, all
     *     callbacks for the holding hand status change event will be unregistered.
     * @throws { BusinessError } 201 - Permission denied. An attempt was made to unsubscribe holdingHandChanged
     *     <br> event forbidden by permission: ohos.permission.DETECT_GESTURE.
     * @throws { BusinessError } 801 - Capability not supported. Function can not work correctly due to limited
     *     <br> device capabilities.
     * @throws { BusinessError } 31500001 - Service exception. Possible causes: 1. A system error, such as null pointer,
     *     container-related exception;
     *     <br> 2. N-API invocation exception, invalid N-API status.
     * @throws { BusinessError } 31500003 - Unsubscription failed. Possible causes: 1. Callback failure;
     *     <br> 2. N-API invocation exception, invalid N-API status; 3. IPC request exception.
     * @syscap SystemCapability.MultimodalAwareness.Motion
     * @since 20
     */
    function off(type: 'holdingHandChanged', callback?: Callback<HoldingHandStatus>): void;
}
export default motion;

```
