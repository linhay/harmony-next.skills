# @ohos.runningLock.d.ts

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
 * The **runningLock** module provides APIs for creating, querying, holding, and releasing running locks. A running lock
 * enables the proximity sensor to turn on or off the screen, or prevents the device from entering sleep mode when the
 * screen is off. For details about the running lock types, see [RunningLockType]{@link runningLock.RunningLockType}.
 *
 * @syscap SystemCapability.PowerManager.PowerManager.Core
 * @since 7
 */
declare namespace runningLock {
    /**
     * Defines a **RunningLock** object.
     *
     * @syscap SystemCapability.PowerManager.PowerManager.Core
     * @since 7
     */
    class RunningLock {
        /**
         * Locks and holds a **RunningLock** object.
         *
         * @permission ohos.permission.RUNNING_LOCK
         * @param { number } timeout - Duration for locking and holding the **RunningLock** object, in ms.
         * @syscap SystemCapability.PowerManager.PowerManager.Core
         * @since 7
         * @deprecated since 9
         * @useinstead runningLock.RunningLock.hold
         */
        lock(timeout: number): void;
        /**
         * Holds a running lock.
         *
         * @permission ohos.permission.RUNNING_LOCK
         * @param { number } timeout - Duration for locking and holding the **RunningLock** object, in ms.<br>The value must be
         *     a number:<br>**-1**: The lock is permanently held and needs to be released automatically.<br>**0**: The lock
         *     is released 3 seconds after the timer expires by default.<br>> 0: The lock is released based on the input
         *     value after the timer expires.
         * @throws { BusinessError } 201 - If the permission is denied.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Incorrect parameter types;
         * @syscap SystemCapability.PowerManager.PowerManager.Core
         * @since 9
         */
        hold(timeout: number): void;
        /**
         * Checks whether this running lock is used.
         *
         * @returns { boolean } Returns true if the lock is held or in use; returns false if the lock has been released.
         * @syscap SystemCapability.PowerManager.PowerManager.Core
         * @since 7
         * @deprecated since 9
         * @useinstead runningLock.RunningLock.isHolding
         */
        isUsed(): boolean;
        /**
         * Checks whether this running lock is being held.
         *
         * @returns { boolean } The value **true** indicates that the **RunningLock** object is held; and the value
         *     **false** indicates that the **RunningLock** object is released.
         * @syscap SystemCapability.PowerManager.PowerManager.Core
         * @since 9
         */
        isHolding(): boolean;
        /**
         * Releases this running lock.
         *
         * @permission ohos.permission.RUNNING_LOCK
         * @syscap SystemCapability.PowerManager.PowerManager.Core
         * @since 7
         * @deprecated since 9
         * @useinstead runningLock.RunningLock.unhold
         */
        unlock(): void;
        /**
         * Releases this running lock.
         *
         * @permission ohos.permission.RUNNING_LOCK
         * @throws { BusinessError } 201 - If the permission is denied.
         * @syscap SystemCapability.PowerManager.PowerManager.Core
         * @since 9
         */
        unhold(): void;
    }
    /**
     * Enumerates the types of **RunningLock** objects.
     *
     * @syscap SystemCapability.PowerManager.PowerManager.Core
     * @since 7
     */
    export enum RunningLockType {
        /**
         * A lock that prevents the system from entering sleep mode when the screen is off.
         *
         * **NOTE**
         *
         * This parameter is supported since API version 7 and deprecated since API version 10.
         *
         * @syscap SystemCapability.PowerManager.PowerManager.Core
         * @since 7
         * @deprecated since 10
         */
        BACKGROUND = 1,
        /**
         * A lock that enables the proximity sensor and turns on or off the screen based on the distance between the sensor
         * and the obstacle.
         *
         * @syscap SystemCapability.PowerManager.PowerManager.Core
         * @since 7
         */
        PROXIMITY_SCREEN_CONTROL = 2,
        /**
         * A background lock that prevents the system from automatically entering sleep mode when the user is inactive for a
         * period of time. Note: This lock cannot prevent the system from entering the forced sleep state in scenarios such
         * as closing the PC lid. The user must listen for the
         * [COMMON_EVENT_ENTER_FORCE_SLEEP](docroot://reference/apis-basic-services-kit/common_event/commonEventManager-definitions.md#common_event_enter_force_sleep12)
         * event and release this lock after receiving the event. The behavior of this lock varies with devices. For details
         * about how to use this type of lock, see
         * [Preventing the Idle System from Entering Sleep Mode](docroot://basic-services/powermgr/runningLock/runningLock-dev.md).
         *
         * @syscap SystemCapability.PowerManager.PowerManager.Core
         * @since 23
         */
        BACKGROUND_USER_IDLE = 129
    }
    /**
     * Checks whether a specified type of {@link RunningLock} is supported. This API uses an asynchronous callback to
     * return the result.
     *
     * @param { RunningLockType } type - Type of the running lock.
     * @param { AsyncCallback<boolean> } callback - Callback used to return the result. If the operation is successful,
     *     **err** is **undefined** and **data** is the query result obtained, where the value **true** indicates that the
     *     specified type of the running lock is supported and **false** indicates the opposite. Otherwise, **err** is an
     *     error object.
     * @syscap SystemCapability.PowerManager.PowerManager.Core
     * @since 7
     * @deprecated since 9
     * @useinstead runningLock.isSupported
     */
    function isRunningLockTypeSupported(type: RunningLockType, callback: AsyncCallback<boolean>): void;
    /**
     * Checks whether a specified type of {@link RunningLock} is supported. This API uses a promise to return the
     * result.
     *
     * @param { RunningLockType } type - Type of the running lock.
     * @returns { Promise<boolean> } Promise used to return the result. The value **true** indicates that the specified
     *     type of the running lock is supported, and the value **false** indicates the opposite.
     * @syscap SystemCapability.PowerManager.PowerManager.Core
     * @since 7
     * @deprecated since 9
     * @useinstead runningLock.isSupported
     */
    function isRunningLockTypeSupported(type: RunningLockType): Promise<boolean>;
    /**
     * Checks whether a specified type of {@link RunningLock} is supported.
     *
     * @param { RunningLockType } type - Type of the running lock. The value must be an enum.
     * @returns { boolean } The value **true** indicates that the specified type of the running lock is supported, and the
     *     value **false** indicates the opposite.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Incorrect parameter types;
     *     2. Parameter verification failed.
     * @syscap SystemCapability.PowerManager.PowerManager.Core
     * @since 9
     */
    function isSupported(type: RunningLockType): boolean;
    /**
     * Creates a {@link RunningLock} object. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.RUNNING_LOCK
     * @param { string } name - Indicates the {@link RunningLock} name. A recommended name consists of the package or
     *     class name and a suffix.
     * @param { RunningLockType } type - Indicates the {@link RunningLockType}.
     * @param { AsyncCallback<RunningLock> } callback - Callback used to return the result. If the operation is
     *     successful, **err** is **undefined** and data is the created **RunningLock** object. Otherwise, **err** is an
     *     error object. **AsyncCallback** has encapsulated an API of the **RunningLock** class.
     * @syscap SystemCapability.PowerManager.PowerManager.Core
     * @since 7
     * @deprecated since 9
     * @useinstead runningLock.create
     */
    function createRunningLock(name: string, type: RunningLockType, callback: AsyncCallback<RunningLock>): void;
    /**
     * Creates a {@link RunningLock} object. This API uses a promise to return the result.
     *
     * @permission ohos.permission.RUNNING_LOCK
     * @param { string } name - Indicates the {@link RunningLock} name. A recommended name consists of the package or
     *     class name and a suffix.
     * @param { RunningLockType } type - Indicates the {@link RunningLockType}.
     * @returns { Promise<RunningLock> } Promise used to return the {@link RunningLock} object.
     * @syscap SystemCapability.PowerManager.PowerManager.Core
     * @since 7
     * @deprecated since 9
     * @useinstead runningLock.create
     */
    function createRunningLock(name: string, type: RunningLockType): Promise<RunningLock>;
    /**
     * Creates a {@link RunningLock} object. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.RUNNING_LOCK
     * @param { string } name - Name of the **RunningLock** object. The value must be a string.
     * @param { RunningLockType } type - Type of the **RunningLock** object. The value must be an enum.
     * @param { AsyncCallback<RunningLock> } callback - Callback used to return the result. If the operation is
     *     successful, **err** is **undefined** and data is the created **RunningLock** object. Otherwise, **err** is an
     *     error object. **AsyncCallback** has encapsulated an API of the **RunningLock** class.
     * @throws { BusinessError } 201 - If the permission is denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Parameter verification failed.
     * @syscap SystemCapability.PowerManager.PowerManager.Core
     * @since 9
     */
    function create(name: string, type: RunningLockType, callback: AsyncCallback<RunningLock>): void;
    /**
     * Creates a {@link RunningLock} object. This API uses a promise to return the result.
     *
     * @permission ohos.permission.RUNNING_LOCK
     * @param { string } name - Name of the **RunningLock** object. The value must be a string.
     * @param { RunningLockType } type - Type of the **RunningLock** object. The value must be an enum.
     * @returns { Promise<RunningLock> } Promise used to return the {@link RunningLock} object.
     * @throws { BusinessError } 201 - If the permission is denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Parameter verification failed.
     * @syscap SystemCapability.PowerManager.PowerManager.Core
     * @since 9
     */
    function create(name: string, type: RunningLockType): Promise<RunningLock>;
}
export default runningLock;

```
