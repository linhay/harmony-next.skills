# @ohos.multimodalAwareness.userStatus.d.ts

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
import type { Callback } from './@ohos.base';
/**
 * The **UserStatus** module, designed for user state awareness, empowers the system to perceive specific conditions of
 * users, such as determining their age group or recognizing environmental sounds, among other functions.
 *
 * @syscap SystemCapability.MultimodalAwareness.UserStatus
 * @since 20
 */
declare namespace userStatus {
    /**
     * Defines the user age group detection result.
     *
     * @syscap SystemCapability.MultimodalAwareness.UserStatus
     * @since 20
     * @deprecated since 24
     */
    export interface UserClassification {
        /**
         * User age group, for example, child or adult.
         *
         * @syscap SystemCapability.MultimodalAwareness.UserStatus
         * @since 20
         * @deprecated since 24
         */
        ageGroup?: UserAgeGroup;
        /**
         * Confidence of the detection result. The value is a floating point number ranging from 0 to 1. A larger value
         * indicates a higher confidence.
         *
         * @syscap SystemCapability.MultimodalAwareness.UserStatus
         * @since 20
         * @deprecated since 24
         */
        confidence?: float;
    }
    /**
     * Enumerates the user age groups, for example, child or adult.
     *
     * @syscap SystemCapability.MultimodalAwareness.UserStatus
     * @since 20
     * @deprecated since 24
     */
    export enum UserAgeGroup {
        /**
         * Adult.
         *
         * @syscap SystemCapability.MultimodalAwareness.UserStatus
         * @since 20
         * @deprecated since 24
         */
        OTHERS = 0,
        /**
         * Child.
         *
         * @syscap SystemCapability.MultimodalAwareness.UserStatus
         * @since 20
         * @deprecated since 24
         */
        CHILD = 1
    }
    /**
     * Enables the age group detection function.
     *
     * When the function is enabled, the application can recommend content based on the age group detection result.
     *
     * > **NOTE**
     * >
     * > This API is supported only on some phones. Error code **801** is returned if it is called on unsupported phones.
     *
     * @param { 'userAgeGroupDetected' } type - Event type. The value **userAgeGroupDetected** indicates the event of
     *     enabling age group detection.
     * @param { Callback<UserClassification> } callback - Callback used to return the detection result.
     * @throws { BusinessError } 801 - Capability not supported. Function can not work correctly due to limited
     *     <br> device capabilities.
     * @throws { BusinessError } 33900001 - Service exception. Possible causes:
     *     <br>1. System error, such as a null pointer and container-related exception.
     *     <br>2. Node-API invocation exception, such as invalid Node-API status.
     * @throws { BusinessError } 33900002 - Subscription failed. Possible causes:
     *     <br>1. Callback registration failed.
     *     <br>2. Failed to bind the native object to the JS wrapper.
     *     <br>3. Node-API invocation exception, such as invalid Node-API status.
     *     <br>4. IPC request exception.
     * @syscap SystemCapability.MultimodalAwareness.UserStatus
     * @since 20
     * @deprecated since 24
     */
    function on(type: 'userAgeGroupDetected', callback: Callback<UserClassification>): void;
    /**
     * Disables the age group detection function.
     *
     * > **NOTE**
     * >
     * > This API is supported only on some phones. Error code **33900003** is returned if it is called on unsupported
     * > phones.
     *
     * @param { 'userAgeGroupDetected' } type - Event type. The value **userAgeGroupDetected** indicates the event of
     *     enabling age group detection.
     * @param { Callback<UserClassification> } [callback] - Callback used to return the detection result.
     * @throws { BusinessError } 801 - Capability not supported. Function can not work correctly due to limited
     *     <br> device capabilities.
     * @throws { BusinessError } 33900001 - Service exception. Possible causes:
     *     <br>1. System error, such as a null pointer and container-related exception.
     *     <br>2. Node-API invocation exception, such as invalid Node-API status.
     * @throws { BusinessError } 33900003 - Unsubscription failed. Possible causes:
     *     <br>1. Callback failure.
     *     <br>2. Node-API invocation exception, such as invalid Node-API status.
     *     <br>3. IPC request exception.
     * @syscap SystemCapability.MultimodalAwareness.UserStatus
     * @since 20
     * @deprecated since 24
     */
    function off(type: 'userAgeGroupDetected', callback?: Callback<UserClassification>): void;
}
export default userStatus;

```
