# @ohos.resourceschedule.workScheduler.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022-2026 Huawei Device Co., Ltd.
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
 * @kit BackgroundTasksKit
 */
import { AsyncCallback } from './@ohos.base';
/**
 * The **workScheduler** module provides the APIs for registering, canceling, and querying deferred tasks. You can use
 * the APIs to register tasks that do not have high requirements on real-time performance as deferred tasks. The system
 * schedules and executes the deferred tasks at an appropriate time, subject to the storage space, power consumption,
 * and more. For details, see [Deferred Task Scheduling](docroot://task-management/work-scheduler.md).
 *
 * @syscap SystemCapability.ResourceSchedule.WorkScheduler
 * @stagemodelonly
 * @since 9
 */
declare namespace workScheduler {
    /**
     * Represents the deferred task information, which is used to set the trigger condition.
     *
     * @syscap SystemCapability.ResourceSchedule.WorkScheduler
     * @stagemodelonly
     * @since 9
     */
    export interface WorkInfo {
        /**
         * ID of the deferred task.
         *
         * @syscap SystemCapability.ResourceSchedule.WorkScheduler
         * @stagemodelonly
         * @since 9
         */
        workId: number;
        /**
         * Bundle name of the application where the deferred task is located.
         *
         * @syscap SystemCapability.ResourceSchedule.WorkScheduler
         * @stagemodelonly
         * @since 9
         */
        bundleName: string;
        /**
         * Ability name in the bundle.
         *
         * @syscap SystemCapability.ResourceSchedule.WorkScheduler
         * @stagemodelonly
         * @since 9
         */
        abilityName: string;
        /**
         * Whether the registered deferred task can be saved in the system. The default value is **false**.
         *
         * - **true**: The task can be saved. That is, the task can be restored after the system restarts.
         * - **false**: The task cannot be saved.
         *
         * @syscap SystemCapability.ResourceSchedule.WorkScheduler
         * @stagemodelonly
         * @since 9
         */
        isPersisted?: boolean;
        /**
         * Network type.
         *
         * @syscap SystemCapability.ResourceSchedule.WorkScheduler
         * @stagemodelonly
         * @since 9
         */
        networkType?: NetworkType;
        /**
         * Whether the device needs to enter the charging state. The default value is **false**.
         *
         * - **true**: The device needs to enter the charging state to trigger deferred task scheduling.
         * - **false**: The device does not need to enter the charging state to trigger deferred task scheduling.
         *
         * @syscap SystemCapability.ResourceSchedule.WorkScheduler
         * @stagemodelonly
         * @since 9
         */
        isCharging?: boolean;
        /**
         * Charging type.
         *
         * @syscap SystemCapability.ResourceSchedule.WorkScheduler
         * @stagemodelonly
         * @since 9
         */
        chargerType?: ChargingType;
        /**
         * Battery level.
         *
         * Value range: [0, 100]
         *
         * @syscap SystemCapability.ResourceSchedule.WorkScheduler
         * @stagemodelonly
         * @since 9
         */
        batteryLevel?: number;
        /**
         * Battery status.
         *
         * @syscap SystemCapability.ResourceSchedule.WorkScheduler
         * @stagemodelonly
         * @since 9
         */
        batteryStatus?: BatteryStatus;
        /**
         * Storage status.
         *
         * @syscap SystemCapability.ResourceSchedule.WorkScheduler
         * @stagemodelonly
         * @since 9
         */
        storageRequest?: StorageRequest;
        /**
         * Repeat interval, in milliseconds.
         *
         * @syscap SystemCapability.ResourceSchedule.WorkScheduler
         * @stagemodelonly
         * @since 9
         */
        repeatCycleTime?: number;
        /**
         * Whether the task is repeated. The default value is **false**.
         *
         * - **true**: The task is repeated.
         * - **false**: The task is not repeated.
         *
         * @syscap SystemCapability.ResourceSchedule.WorkScheduler
         * @stagemodelonly
         * @since 9
         */
        isRepeat?: boolean;
        /**
         * Number of repeat times.
         *
         * @syscap SystemCapability.ResourceSchedule.WorkScheduler
         * @stagemodelonly
         * @since 9
         */
        repeatCount?: number;
        /**
         * Whether the device needs to enter the idle state to trigger deferred task scheduling. The default value is
         * **false**.
         *
         * - **true**: The device needs to enter the idle state to trigger deferred task scheduling.
         * - **false**: The device does not need to enter the idle state to trigger deferred task scheduling.
         *
         * @syscap SystemCapability.ResourceSchedule.WorkScheduler
         * @stagemodelonly
         * @since 9
         */
        isDeepIdle?: boolean;
        /**
         * Idle wait time, in milliseconds.
         *
         * @syscap SystemCapability.ResourceSchedule.WorkScheduler
         * @stagemodelonly
         * @since 9
         */
        idleWaitTime?: number;
        /**
         * Carried parameters.
         *
         * @syscap SystemCapability.ResourceSchedule.WorkScheduler
         * @stagemodelonly
         * @since 9
         */
        parameters?: Record<string, number | string | boolean>;
        /**
         * Interval between the initial execution time and the request time for a task, in milliseconds. The default value
         * is **0**, and the value must be greater than or equal to 0.
         * The value range is all integers.
         *
         * @syscap SystemCapability.ResourceSchedule.WorkScheduler
         * @stagemodelonly
         * @since 22
         */
        earliestStartTime?: number;
    }
    /**
     * Requests a deferred task. Upon successful request, the deferred task is added to the execution queue and will be
     * executed by the system once the trigger conditions are met.
     *
     * @param { WorkInfo } work - The info of work.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameters types; 3. Parameter verification failed.
     * @throws { BusinessError } 9700001 - Memory operation failed.
     * @throws { BusinessError } 9700002 - Failed to write data into parcel. Possible reasons: 1. Invalid parameters;
     *     2. Failed to apply for memory.
     * @throws { BusinessError } 9700003 - System service operation failed.
     * @throws { BusinessError } 9700004 - Check on workInfo failed.
     * @throws { BusinessError } 9700005 - Calling startWork failed.
     * @syscap SystemCapability.ResourceSchedule.WorkScheduler
     * @stagemodelonly
     * @since 9
     */
    function startWork(work: WorkInfo): void;
    /**
     * Stops a deferred task.
     *
     * @param { WorkInfo } work - Deferred task to stop.
     * @param { boolean } needCancel - Whether to clear the task while stopping it.<br>The value **true** means to clear
     *     the task while stopping it, and **false** means to stop the task only. The default value is **false**.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameters types; 3. Parameter verification failed.
     * @throws { BusinessError } 9700001 - Memory operation failed.
     * @throws { BusinessError } 9700002 - Failed to write data into parcel. Possible reasons: 1. Invalid parameters;
     *     2. Failed to apply for memory.
     * @throws { BusinessError } 9700003 - System service operation failed.
     * @throws { BusinessError } 9700004 - Check on workInfo failed.
     * @syscap SystemCapability.ResourceSchedule.WorkScheduler
     * @stagemodelonly
     * @since 9
     */
    function stopWork(work: WorkInfo, needCancel?: boolean): void;
    /**
     * Obtains the information a deferred task. This API uses an asynchronous callback to return the result.
     *
     * @param { number } workId - ID of the deferred task.
     * @param { AsyncCallback<WorkInfo> } callback - Callback used to return the result. If **workId** is valid, the task
     *     information obtained from WorkSchedulerService is returned. Otherwise, an exception is thrown.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: Parameter verification failed.
     * @throws { BusinessError } 9700001 - Memory operation failed.
     * @throws { BusinessError } 9700002 - Failed to write data into parcel. Possible reasons: 1. Invalid parameters;
     *     2. Failed to apply for memory.
     * @throws { BusinessError } 9700003 - System service operation failed.
     * @throws { BusinessError } 9700004 - Check on workInfo failed.
     * @syscap SystemCapability.ResourceSchedule.WorkScheduler
     * @stagemodelonly
     * @since 9
     */
    function getWorkStatus(workId: number, callback: AsyncCallback<WorkInfo>): void;
    /**
     * Obtains the information a deferred task. This API uses a promise to return the result.
     *
     * @param { number } workId - ID of the deferred task.
     * @returns { Promise<WorkInfo> } Promise used to return the result. If **workId** is valid, the task information
     *     obtained from WorkSchedulerService is returned. Otherwise, an exception is thrown.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: Parameter verification failed.
     * @throws { BusinessError } 9700001 - Memory operation failed.
     * @throws { BusinessError } 9700002 - Failed to write data into parcel. Possible reasons: 1. Invalid parameters;
     *     2. Failed to apply for memory.
     * @throws { BusinessError } 9700003 - System service operation failed.
     * @throws { BusinessError } 9700004 - Check on workInfo failed.
     * @syscap SystemCapability.ResourceSchedule.WorkScheduler
     * @stagemodelonly
     * @since 9
     */
    function getWorkStatus(workId: number): Promise<WorkInfo>;
    /**
     * Obtains all the deferred tasks. This API uses an asynchronous callback to return the result.
     *
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If all the deferred tasks are
     *     obtained, **err** is **undefined**. Otherwise, **err** is an error object.
     * @returns { Array<WorkInfo> } List of deferred tasks. If deferred tasks have been added to the execution queue, the
     *     list of all deferred tasks in the current application is returned. Otherwise, an empty list is returned.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameters types.
     * @throws { BusinessError } 9700001 - Memory operation failed.
     * @throws { BusinessError } 9700002 - Failed to write data into parcel. Possible reasons: 1. Invalid parameters;
     *     2. Failed to apply for memory.
     * @throws { BusinessError } 9700003 - System service operation failed.
     * @syscap SystemCapability.ResourceSchedule.WorkScheduler
     * @stagemodelonly
     * @since 9
     * @deprecated since 10
     * @useinstead workScheduler.obtainAllWorks(callback: AsyncCallback<Array<WorkInfo>>)
     */
    function obtainAllWorks(callback: AsyncCallback<void>): Array<WorkInfo>;
    /**
     * Obtains all the deferred tasks. This API uses an asynchronous callback to return the result.
     *
     * @param { AsyncCallback<Array<WorkInfo>> } callback - Callback used to return the list of all deferred tasks in the
     *     current application. If the list fails to be obtained, an exception is thrown.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameters types.
     * @throws { BusinessError } 9700001 - Memory operation failed.
     * @throws { BusinessError } 9700002 - Failed to write data into parcel. Possible reasons: 1. Invalid parameters;
     *     2. Failed to apply for memory.
     * @throws { BusinessError } 9700003 - System service operation failed.
     * @syscap SystemCapability.ResourceSchedule.WorkScheduler
     * @stagemodelonly
     * @since 10
     */
    function obtainAllWorks(callback: AsyncCallback<Array<WorkInfo>>): void;
    /**
     * Obtains all the deferred tasks. This API uses a promise to return the result.
     *
     * @returns { Promise<Array<WorkInfo>> } Promise used to return all the deferred tasks.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameters types.
     * @throws { BusinessError } 9700001 - Memory operation failed.
     * @throws { BusinessError } 9700002 - Failed to write data into parcel. Possible reasons: 1. Invalid parameters;
     *     2. Failed to apply for memory.
     * @throws { BusinessError } 9700003 - System service operation failed.
     * @syscap SystemCapability.ResourceSchedule.WorkScheduler
     * @stagemodelonly
     * @since 9
     */
    function obtainAllWorks(): Promise<Array<WorkInfo>>;
    /**
     * Stops and clears all the deferred tasks.
     *
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameters types.
     * @throws { BusinessError } 9700001 - Memory operation failed.
     * @throws { BusinessError } 9700002 - Failed to write data into parcel. Possible reasons: 1. Invalid parameters;
     *     2. Failed to apply for memory.
     * @throws { BusinessError } 9700003 - System service operation failed.
     * @syscap SystemCapability.ResourceSchedule.WorkScheduler
     * @stagemodelonly
     * @since 9
     */
    function stopAndClearWorks(): void;
    /**
     * Checks whether the last execution of a task timed out. This API uses an asynchronous callback to return the result.
     *
     * @param { number } workId - ID of the deferred task.
     * @param { AsyncCallback<void> } callback - Callback used to return the result.
     * @returns { boolean } Whether the last execution of a deferred task timed out. If **workId** is valid, it returns
     *     whether the last execution of the task obtained from WorkSchedulerService timed out; otherwise, an exception is
     *     thrown. **true** indicates that the last execution of the deferred task corresponding to the **workId** timed
     *     out, while **false** indicates the opposite.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: Parameter verification failed.
     * @throws { BusinessError } 9700001 - Memory operation failed.
     * @throws { BusinessError } 9700002 - Failed to write data into parcel. Possible reasons: 1. Invalid parameters;
     *     2. Failed to apply for memory.
     * @throws { BusinessError } 9700003 - System service operation failed.
     * @throws { BusinessError } 9700004 - Check on workInfo failed.
     * @syscap SystemCapability.ResourceSchedule.WorkScheduler
     * @stagemodelonly
     * @since 9
     * @deprecated since 10
     * @useinstead workScheduler.isLastWorkTimeOut(workId: int, callback: AsyncCallback<boolean>)
     */
    function isLastWorkTimeOut(workId: number, callback: AsyncCallback<void>): boolean;
    /**
     * Checks whether the last execution of a task timed out. This API uses an asynchronous callback to return the result.
     *
     * @param { number } workId - ID of the deferred task.
     * @param { AsyncCallback<boolean> } callback - Callback used to return the result.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: Parameter verification failed.
     * @throws { BusinessError } 9700001 - Memory operation failed.
     * @throws { BusinessError } 9700002 - Failed to write data into parcel. Possible reasons: 1. Invalid parameters;
     *     2. Failed to apply for memory.
     * @throws { BusinessError } 9700003 - System service operation failed.
     * @throws { BusinessError } 9700004 - Check on workInfo failed.
     * @syscap SystemCapability.ResourceSchedule.WorkScheduler
     * @stagemodelonly
     * @since 10
     */
    function isLastWorkTimeOut(workId: number, callback: AsyncCallback<boolean>): void;
    /**
     * Checks whether the last execution of a task timed out. This API uses a promise to return the result.
     *
     * @param { number } workId - ID of the deferred task.
     * @returns { Promise<boolean> } Promise used to return the result. The value **true** means that the last execution
     *     of the specified task times out, and **false** means the opposite.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: Parameter verification failed.
     * @throws { BusinessError } 9700001 - Memory operation failed.
     * @throws { BusinessError } 9700002 - Failed to write data into parcel. Possible reasons: 1. Invalid parameters;
     *     2. Failed to apply for memory.
     * @throws { BusinessError } 9700003 - System service operation failed.
     * @throws { BusinessError } 9700004 - Check on workInfo failed.
     * @syscap SystemCapability.ResourceSchedule.WorkScheduler
     * @stagemodelonly
     * @since 9
     */
    function isLastWorkTimeOut(workId: number): Promise<boolean>;
    /**
     * Enumerates the network types that trigger deferred task callback.
     *
     * @syscap SystemCapability.ResourceSchedule.WorkScheduler
     * @stagemodelonly
     * @since 9
     * @name NetworkType
     */
    export enum NetworkType {
        /**
         * Any network type.
         *
         * @syscap SystemCapability.ResourceSchedule.WorkScheduler
         * @stagemodelonly
         * @since 9
         */
        NETWORK_TYPE_ANY = 0,
        /**
         * Mobile network.
         *
         * @syscap SystemCapability.ResourceSchedule.WorkScheduler
         * @stagemodelonly
         * @since 9
         */
        NETWORK_TYPE_MOBILE = 1,
        /**
         * Wi-Fi network.
         *
         * @syscap SystemCapability.ResourceSchedule.WorkScheduler
         * @stagemodelonly
         * @since 9
         */
        NETWORK_TYPE_WIFI = 2,
        /**
         * Bluetooth network.
         *
         * @syscap SystemCapability.ResourceSchedule.WorkScheduler
         * @stagemodelonly
         * @since 9
         */
        NETWORK_TYPE_BLUETOOTH = 3,
        /**
         * Wi-Fi P2P network.
         *
         * @syscap SystemCapability.ResourceSchedule.WorkScheduler
         * @stagemodelonly
         * @since 9
         */
        NETWORK_TYPE_WIFI_P2P = 4,
        /**
         * Ethernet.
         *
         * @syscap SystemCapability.ResourceSchedule.WorkScheduler
         * @stagemodelonly
         * @since 9
         */
        NETWORK_TYPE_ETHERNET = 5
    }
    /**
     * Enumerates the charging types that trigger deferred task callback.
     *
     * @syscap SystemCapability.ResourceSchedule.WorkScheduler
     * @stagemodelonly
     * @since 9
     * @name ChargingType
     */
    export enum ChargingType {
        /**
         * Any charging type.
         *
         * @syscap SystemCapability.ResourceSchedule.WorkScheduler
         * @stagemodelonly
         * @since 9
         */
        CHARGING_PLUGGED_ANY = 0,
        /**
         * DC charging.
         *
         * @syscap SystemCapability.ResourceSchedule.WorkScheduler
         * @stagemodelonly
         * @since 9
         */
        CHARGING_PLUGGED_AC = 1,
        /**
         * USB charging.
         *
         * @syscap SystemCapability.ResourceSchedule.WorkScheduler
         * @stagemodelonly
         * @since 9
         */
        CHARGING_PLUGGED_USB = 2,
        /**
         * Wireless charging.
         *
         * @syscap SystemCapability.ResourceSchedule.WorkScheduler
         * @stagemodelonly
         * @since 9
         */
        CHARGING_PLUGGED_WIRELESS = 3
    }
    /**
     * Enumerates the battery status that triggers the deferred task callback.
     *
     * @syscap SystemCapability.ResourceSchedule.WorkScheduler
     * @stagemodelonly
     * @since 9
     * @name BatteryStatus
     */
    export enum BatteryStatus {
        /**
         * A low battery alert is displayed.
         *
         * @syscap SystemCapability.ResourceSchedule.WorkScheduler
         * @stagemodelonly
         * @since 9
         */
        BATTERY_STATUS_LOW = 0,
        /**
         * The battery level is restored from low to normal.
         *
         * @syscap SystemCapability.ResourceSchedule.WorkScheduler
         * @stagemodelonly
         * @since 9
         */
        BATTERY_STATUS_OKAY = 1,
        /**
         * The battery level is restored from low to normal, or a low battery alert is displayed.
         *
         * @syscap SystemCapability.ResourceSchedule.WorkScheduler
         * @stagemodelonly
         * @since 9
         */
        BATTERY_STATUS_LOW_OR_OKAY = 2
    }
    /**
     * Enumerates the storage status that triggers the deferred task callback.
     *
     * @syscap SystemCapability.ResourceSchedule.WorkScheduler
     * @stagemodelonly
     * @since 9
     * @name StorageRequest
     */
    export enum StorageRequest {
        /**
         * The storage space is insufficient.
         *
         * @syscap SystemCapability.ResourceSchedule.WorkScheduler
         * @stagemodelonly
         * @since 9
         */
        STORAGE_LEVEL_LOW = 0,
        /**
         * The storage space is restored from insufficient to normal.
         *
         * @syscap SystemCapability.ResourceSchedule.WorkScheduler
         * @stagemodelonly
         * @since 9
         */
        STORAGE_LEVEL_OKAY = 1,
        /**
         * The storage space is insufficient, or the storage space is restored from insufficient to normal.
         *
         * @syscap SystemCapability.ResourceSchedule.WorkScheduler
         * @stagemodelonly
         * @since 9
         */
        STORAGE_LEVEL_LOW_OR_OKAY = 2
    }
}
export default workScheduler;

```
