# @ohos.resourceschedule.backgroundTaskManager.d.ts

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
import { AsyncCallback, Callback } from './@ohos.base';
import { WantAgent } from '@ohos.wantAgent';
import Context from './application/BaseContext';
import type notificationManager from './@ohos.notificationManager';
/**
 * The **backgroundTaskManager** module provides APIs to request background tasks. You can use the APIs to request
 * transient tasks, continuous tasks, or efficiency resources to prevent the application process from being terminated
 * or suspended when your application is switched to the background. For details, see
 * [Continuous Task](docroot://task-management/continuous-task.md) and
 * [Transient Task](docroot://task-management/transient-task.md).
 *
 * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
 * @atomicservice [since 12]
 * @since 9
 */
declare namespace backgroundTaskManager {
    /**
     * Specifies details of the continuous task being requested or updated. It is typically used as input for the
     * [startBackgroundRunning()]{@link backgroundTaskManager.startBackgroundRunning(context: Context, request: ContinuousTaskRequest)}
     * and
     * [updateBackgroundRunning()]{@link backgroundTaskManager.updateBackgroundRunning(context: Context, request: ContinuousTaskRequest)}
     * APIs. Note that:
     *
     * 1. When requesting a continuous task via
     * [startBackgroundRunning()]{@link backgroundTaskManager.startBackgroundRunning(context: Context, request: ContinuousTaskRequest)},
     * notifications will be combined if the main type and subtype of the continuous task
     * to be requested are the same as those of the existing continuous task in the current application,
     * and the **combinedTaskNotification** value is **true** for both tasks.
     * Otherwise, notifications will not be combined.
     * 2. Notifications will not be combined if the continuous task has no notification.
     * For details about whether notifications are sent for the continuous task,
     * see [BackgroundTaskMode]{@link backgroundTaskManager.BackgroundTaskMode}.
     * 3. Notifications cannot be combined if the continuous task includes data transmission.
     * 4. Notifications that have been combined cannot be canceled.
     * If notifications have been combined, they cannot be updated to uncombined.
     * 5. After notifications are combined, tapping the notification will redirect to the UIAbility
     * corresponding to the first requested continuous task.
     * If the update API is called,
     * the redirection will target the UIAbility corresponding to the last updated continuous task.
     * 6. When the [updateBackgroundRunning()]{@link backgroundTaskManager.updateBackgroundRunning(context: Context, request: ContinuousTaskRequest)}
     * API is called to update a continuous task, the input **continuousTaskId** must exist. Otherwise, the update fails.
     * 7. Continuous tasks of the [MODE_SPECIAL_SCENARIO_PROCESSING]{@link backgroundTaskManager.BackgroundTaskMode} type
     * are supported since API version 22. This task type must be used independently and notifications cannot be combined.
     * Specifically, when you request or update a continuous task,
     * it must be of the **MODE_SPECIAL_SCENARIO_PROCESSING** type.
     * Otherwise, an error is returned.
     *
     * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
     * @atomicservice [since 26.0.0]
     * @since 21
     */
    export class ContinuousTaskRequest {
        /**
         * Main type of a continuous task.
         *
         * Note: The main type must match the subtype.
         *
         * @returns { BackgroundTaskMode[] } the background modes
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @atomicservice [since 26.0.0]
         * @since 21
         */
        get backgroundTaskModes(): BackgroundTaskMode[];
        /**
         * Main type of a continuous task.
         *
         * Note: The main type must match the subtype.
         *
         * @param { BackgroundTaskMode[] } value
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @atomicservice [since 26.0.0]
         * @since 21
         */
        set backgroundTaskModes(value: BackgroundTaskMode[]);
        /**
         * Subtype of a continuous task.
         *
         * Note: The main type must match the subtype.
         *
         * @returns { BackgroundTaskSubmode[] } the background submodes
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @atomicservice [since 26.0.0]
         * @since 21
         */
        get backgroundTaskSubmodes(): BackgroundTaskSubmode[];
        /**
         * Subtype of a continuous task.
         *
         * Note: The main type must match the subtype.
         *
         * @param { BackgroundTaskSubmode[] } value
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @atomicservice [since 26.0.0]
         * @since 21
         */
        set backgroundTaskSubmodes(value: BackgroundTaskSubmode[]);
        /**
         * Notification parameters, which are used to specify the target page that is redirected to when a continuous task
         * notification is clicked.
         *
         * @returns { WantAgent } the wantAgent
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @stagemodelonly
         * @atomicservice [since 26.0.0]
         * @since 21
         */
        get wantAgent(): WantAgent;
        /**
         * Notification parameters, which are used to specify the target page that is redirected to when a continuous task
         * notification is clicked.
         *
         * @param { WantAgent } value
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @atomicservice [since 26.0.0]
         * @since 21
         */
        set wantAgent(value: WantAgent);
        /**
         * Whether to combine notifications. The value **true** means to combine notifications, and the value **false** (
         * default) means the opposite.
         *
         * Note: This property does not take effect in
         * [updateBackgroundRunning]{@link backgroundTaskManager.updateBackgroundRunning(context: Context, request: ContinuousTaskRequest)}
         * API. If notifications need to be combined for an existing task, request the task again and set the value to
         * **true**.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @atomicservice [since 26.0.0]
         * @since 21
         */
        combinedTaskNotification?: boolean;
        /**
         * Continuous task ID. The default value is **-1**.
         *
         * Note: If **combinedTaskNotification** is set to true, this property is mandatory and the corresponding ID must
         * exist.
         *
         * Additionally, this property is mandatory (with the corresponding ID required) when used as an input parameter for
         * the
         * [updateBackgroundRunning]{@link backgroundTaskManager.updateBackgroundRunning(context: Context, request: ContinuousTaskRequest)}
         * API.
         *
         * You can call the
         * [getAllContinuousTasks]{@link backgroundTaskManager.getAllContinuousTasks(context: Context, includeSuspended: boolean)}
         * API to view information about all continuous tasks.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @atomicservice [since 26.0.0]
         * @since 21
         */
        continuousTaskId?: number;
        /**
         * Checks whether **BackgroundTaskMode** specified in
         * [ContinuousTaskRequest]{@link backgroundTaskManager.ContinuousTaskRequest} is supported. For details, see
         * [BackgroundTaskMode]{@link backgroundTaskManager.BackgroundTaskMode}.
         *
         * @permission ohos.permission.KEEP_BACKGROUND_RUNNING
         * @returns { boolean } Whether **BackgroundTaskMode** is supported. The value **true** means it is supported, and
         *     the value **false** means the opposite.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 9800005 - Continuous task verification failed.
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @atomicservice [since 26.0.0]
         * @since 21
         */
        isModeSupported(): boolean;
        /**
         * Requests user authorization to run tasks continuously in the background. This API uses an asynchronous callback
         * to return the result. If the API call is successful, a banner notification with a sound is sent. This API is
         * applicable only to continuous tasks of the
         * [MODE_SPECIAL_SCENARIO_PROCESSING]{@link backgroundTaskManager.BackgroundTaskMode} type.
         *
         * @permission ohos.permission.KEEP_BACKGROUND_RUNNING
         * @param { Context } context - Application context.
         *     <br>For details about the application context of the FA model,
         *     see [Context]{@link ./app/context}.<br>For details about the application context of the stage model, see
         *     [Context]{@link ./application/Context:Context}.<br> Note: Continuous tasks can be requested only by the
         *     UIAbility in the stage model and the ServiceAbility in the FA model.
         * @param { Callback<UserAuthResult> } callback - Callback used to return the user authorization result.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 9800004 - System service operation failed.
         * @throws { BusinessError } 9800005 - Continuous task verification failed.
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @stagemodelonly
         * @since 22
         */
        requestAuthFromUser(context: Context, callback: Callback<UserAuthResult>): void;
        /**
         * Requesting MODE_SPECIAL_SCENARIO_PROCESSING authorization from users,
         *     a dialog box will be displayed.
         *
         * @permission ohos.permission.KEEP_BACKGROUND_RUNNING
         * @param { Context } context - App running context.
         * @param { Callback<UserAuthResult> } callback - The callback of the function.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 9800004 - System service operation failed.
         * @throws { BusinessError } 9800005 - Continuous task verification failed.
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @stagemodelonly
         * @since 26.0.0
         */
        requestAuthFromUserByDialog(context: Context, callback: Callback<UserAuthResult>): void;
        /**
         * Checks whether the user has authorized tasks to run continuously in the background. This API uses a promise to
         * return the result.
         * An exception will be thrown if unauthorized.
         *
         * @permission ohos.permission.KEEP_BACKGROUND_RUNNING
         * @param { Context } context - Application context.
         *     <br>For details about the application context of the FA model,
         *     see [Context]{@link ./app/context}.<br>For details about the application context of the stage model, see
         *     [Context]{@link ./application/Context:Context}.<br> Note: Continuous tasks can be requested only by the
         *     UIAbility in the stage model and the ServiceAbility in the FA model.
         * @returns { Promise<UserAuthResult> } Promise used to return the user authorization result.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 9800004 - System service operation failed.
         * @throws { BusinessError } 9800005 - Continuous task verification failed.
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @stagemodelonly
         * @since 22
         */
        checkSpecialScenarioAuth(context: Context): Promise<UserAuthResult>;
        /**
         * Check whether the application can request MODE_SPECIAL_SCENARIO_PROCESSING.
         * No exception will be thrown whether authorized or not.
         *
         * @permission ohos.permission.KEEP_BACKGROUND_RUNNING
         * @param { Context } context - App running context.
         * @returns { Promise<UserAuthResult> } The promise returns the result of user authorization.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 9800004 - System service operation failed.
         * @throws { BusinessError } 9800005 - Continuous task verification failed.
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @stagemodelonly
         * @since 26.0.0
         */
        checkSpecialScenarioAuthResult(context: Context): Promise<UserAuthResult>;
    }
    /**
     * Defines the information about the transient task.
     *
     * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask
     * @since 9
     */
    interface DelaySuspendInfo {
        /**
         * Request ID of the transient task.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask
         * @since 9
         */
        requestId: number;
        /**
         * Actual duration of the transient task requested by the application, in milliseconds.
         * <br>Unit:ms
         *
         * Note: The maximum duration of a transient task is 3 minutes in normal cases. In the case of a low battery (
         * [BatteryCapacityLevel]{@link @ohos.batteryInfo:batteryInfo.BatteryCapacityLevel} set to **LEVEL_LOW**), the
         * maximum duration is decreased to 1 minute.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask
         * @since 9
         */
        actualDelayTime: number;
    }
    /**
     * Describes all transient task information.
     *
     * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask
     * @since 20
     */
    interface TransientTaskInfo {
        /**
         * Remaining quota of the application on the current day, in ms.
         * <br>Unit:ms
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask
         * @since 20
         */
        remainingQuota: number;
        /**
         * All information about the requested transient task.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask
         * @since 20
         */
        transientTasks: DelaySuspendInfo[];
    }
    /**
     * Describes the information about a continuous-task notification.
     *
     * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
     * @atomicservice
     * @since 12
     */
    interface ContinuousTaskNotification {
        /**
         * Slot type of a continuous-task notification.
         *
         * Note: After a continuous task is successfully requested or updated, no prompt tone is played.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @atomicservice
         * @since 12
         */
        slotType: notificationManager.SlotType;
        /**
         * Content type of a continuous-task notification.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @atomicservice
         * @since 12
         */
        contentType: notificationManager.ContentType;
        /**
         * ID of the continuous-task notification.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @atomicservice
         * @since 12
         */
        notificationId: number;
        /**
         * ID of a continuous task.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @atomicservice [since 26.0.0]
         * @since 15
         */
        continuousTaskId?: number;
    }
    /**
     * Describes the information about the cancellation of a continuous task.
     *
     * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
     * @since 15
     */
    interface ContinuousTaskCancelInfo {
        /**
         * Reason for canceling the continuous task.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 15
         */
        reason: ContinuousTaskCancelReason;
        /**
         * ID of the continuous task canceled.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 15
         */
        id: number;
        /**
         * Detailed reason for canceling the continuous task.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @stagemodelonly
         * @since 26.0.0
         */
        detailedReason?: ContinuousTaskDetailedCancelReason;
    }
    /**
     * Describes the activation information of a continuous task.
     *
     * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
     * @since 20
     */
    interface ContinuousTaskActiveInfo {
        /**
         * ID of the activated continuous task.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 20
         */
        id: number;
    }
    /**
     * Describes the continuous task information.
     *
     * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
     * @since 20
     */
    interface ContinuousTaskInfo {
        /**
         * UIAbility name.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 20
         */
        abilityName: string;
        /**
         * Application UID.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 20
         */
        uid: number;
        /**
         * Application PID.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 20
         */
        pid: number;
        /**
         * Whether to request a continuous task in WebView mode, that is, whether to request a continuous task through the
         * system proxy application. The value **true** indicates that the Webview mode is used, and the value **false**
         * indicates that the Webview mode is not used.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 20
         */
        isFromWebView: boolean;
        /**
         * [Type of a continuous task]{@link backgroundTaskManager.BackgroundMode}.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 20
         */
        backgroundModes: string[];
        /**
         * [Subtype of a continuous task]{@link backgroundTaskManager.BackgroundSubMode}.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 20
         */
        backgroundSubModes: string[];
        /**
         * Notification ID.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 20
         */
        notificationId: number;
        /**
         * Continuous task ID.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 20
         */
        continuousTaskId: number;
        /**
         * UIAbility ID.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 20
         */
        abilityId: number;
        /**
         * Bundle name configured in [WantAgent]{@link @ohos.app.ability.wantAgent}. **WantAgent** is a notification
         * parameter used to specify the target page when a continuous task notification is tapped.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 20
         */
        wantAgentBundleName: string;
        /**
         * Ability name configured in [WantAgent]{@link @ohos.app.ability.wantAgent}. **WantAgent** is a notification
         * parameter used to specify the target page when a continuous task notification is tapped.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 20
         */
        wantAgentAbilityName: string;
        /**
         * Whether the requested continuous task is suspended. The value **true** indicates that the task is suspended, and
         * the value **false** indicates that the task is activated.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 20
         */
        suspendState: boolean;
        /**
         * Application bundle name.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 23
         */
        bundleName?: string;
        /**
         * Index of an application clone.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 23
         */
        appIndex?: number;
    }
    /**
     * Describes the information about a suspended continuous task.
     *
     * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
     * @since 20
     */
    interface ContinuousTaskSuspendInfo {
        /**
         * ID of the suspended continuous task.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 20
         */
        continuousTaskId: number;
        /**
         * Continuous task state. The value **false** indicates that the task is activated, and the value **true** indicates
         * that the task is suspended.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 20
         */
        suspendState: boolean;
        /**
         * Reason why the continuous task is suspended.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 20
         */
        suspendReason: ContinuousTaskSuspendReason;
        /**
         * Describes the information about a suspended continuous task.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @stagemodelonly
         * @since 26.0.0
         */
        suspendMessage?: SuspendMessage;
    }
    /**
     * Describes the reason why a continuous task is suspended.
     *
     * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
     * @stagemodelonly
     * @since 26.0.0
     */
    interface SuspendMessage {
        /**
         * Suspension message.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @stagemodelonly
         * @since 26.0.0
         */
        message: string;
        /**
         * Reason why the continuous task is suspended.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @stagemodelonly
         * @since 26.0.0
         */
        reason: ContinuousTaskSuspendReason;
    }
    /**
     * Cancels a transient task.
     *
     * @param { number } requestId - Request ID of the transient task. It is obtained by calling the
     *     [requestSuspendDelay]{@link backgroundTaskManager.requestSuspendDelay} API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameters types; 3. Parameter verification failed.
     * @throws { BusinessError } 9800001 - Memory operation failed.
     * @throws { BusinessError } 9800002 - Failed to write data into parcel. Possible reasons: 1. Invalid parameters;
     *     <br> 2. Failed to apply for memory.
     * @throws { BusinessError } 9800003 - Internal transaction failed.
     * @throws { BusinessError } 9800004 - System service operation failed.
     * @throws { BusinessError } 9900001 - Caller information verification failed for a transient task.
     * @throws { BusinessError } 9900002 - Transient task verification failed.
     * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask
     * @since 9
     */
    function cancelSuspendDelay(requestId: number): void;
    /**
     * Obtains the remaining time of a transient task. This API uses an asynchronous callback to return the result.
     *
     * @param { number } requestId - Request ID of the transient task. It is obtained by calling the
     *     [requestSuspendDelay]{@link backgroundTaskManager.requestSuspendDelay} API.
     * @param { AsyncCallback<number> } callback - Callback used to return the remaining time of the transient task, in
     *     milliseconds.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameters types; 3. Parameter verification failed.
     * @throws { BusinessError } 9800001 - Memory operation failed.
     * @throws { BusinessError } 9800002 - Failed to write data into parcel. Possible reasons: 1. Invalid parameters;
     *     <br> 2. Failed to apply for memory.
     * @throws { BusinessError } 9800003 - Internal transaction failed.
     * @throws { BusinessError } 9800004 - System service operation failed.
     * @throws { BusinessError } 9900001 - Caller information verification failed for a transient task.
     * @throws { BusinessError } 9900002 - Transient task verification failed.
     * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask
     * @since 9
     */
    function getRemainingDelayTime(requestId: number, callback: AsyncCallback<number>): void;
    /**
     * Obtains the remaining time of a transient task. This API uses a promise to return the result.
     *
     * @param { number } requestId - Request ID of the transient task. It is obtained by calling the
     *     [requestSuspendDelay]{@link backgroundTaskManager.requestSuspendDelay} API.
     * @returns { Promise<number> } Promise that returns the remaining time of the transient task, in milliseconds.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameters types; 3. Parameter verification failed.
     * @throws { BusinessError } 9800001 - Memory operation failed.
     * @throws { BusinessError } 9800002 - Failed to write data into parcel. Possible reasons: 1. Invalid parameters;
     *     <br> 2. Failed to apply for memory.
     * @throws { BusinessError } 9800003 - Internal transaction failed.
     * @throws { BusinessError } 9800004 - System service operation failed.
     * @throws { BusinessError } 9900001 - Caller information verification failed for a transient task.
     * @throws { BusinessError } 9900002 - Transient task verification failed.
     * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask
     * @since 9
     */
    function getRemainingDelayTime(requestId: number): Promise<number>;
    /**
     * Requests a transient task.
     *
     * > **NOTE**
     * >
     * > For details about the constraints on requesting and using a transient task, see
     * > [Transient Task (ArkTS)](docroot://task-management/transient-task.md#constraints).
     *
     * @param { string } reason - Reason for requesting the transient task.
     * @param { Callback<void> } callback - Callback used to notify the application that the transient task is about to
     *     time out. Generally, the callback is invoked 6 seconds before the timeout.
     * @returns { DelaySuspendInfo } Information about the transient task.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameters types.
     * @throws { BusinessError } 9800001 - Memory operation failed.
     * @throws { BusinessError } 9800002 - Failed to write data into parcel. Possible reasons: 1. Invalid parameters;
     *     <br> 2. Failed to apply for memory.
     * @throws { BusinessError } 9800003 - Internal transaction failed.
     * @throws { BusinessError } 9800004 - System service operation failed.
     * @throws { BusinessError } 9900001 - Caller information verification failed for a transient task.
     * @throws { BusinessError } 9900002 - Transient task verification failed.
     * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask
     * @since 9
     */
    function requestSuspendDelay(reason: string, callback: Callback<void>): DelaySuspendInfo;
    /**
     * Obtains all transient task information, including the remaining quota of the current day. This API uses a promise
     * to return the result.
     *
     * @returns { Promise<TransientTaskInfo> } Promise that returns all transient task information.
     * @throws { BusinessError } 9900001 - Caller information verification failed for a transient task.
     * @throws { BusinessError } 9900003 - Failed to write data into parcel. Possible reasons: 1. Invalid parameters;
     *     <br> 2. Failed to apply for memory.
     * @throws { BusinessError } 9900004 - System service operation failed.
     * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.TransientTask
     * @since 20
     */
    function getTransientTaskInfo(): Promise<TransientTaskInfo>;
    /**
     * Requests a continuous task of a specific type. This API uses an asynchronous callback to return the result. After a
     * continuous task is successfully requested, there will be a notification message without prompt tone. A UIAbility (
     * ServiceAbility in the FA model) can request only one continuous task at a time through this API. You can request
     * multiple continuous tasks by calling
     * [startBackgroundRunning]{@link backgroundTaskManager.startBackgroundRunning(context: Context, request: ContinuousTaskRequest)}
     * added in API version 21.
     *
     * @permission ohos.permission.KEEP_BACKGROUND_RUNNING
     * @param { Context } context - Application context.
     *     <br>For details about the application context of the FA model, see
     *     [Context]{@link ./app/context}.<br>For details about the application context of the stage model, see
     *     [Context]{@link ./application/Context:Context}.<br> Note: Continuous tasks can be requested only by the
     *     UIAbility in the stage model and the ServiceAbility in the FA model.
     * @param { BackgroundMode } bgMode - Type of the continuous task.
     * @param { WantAgent } wantAgent - Notification parameters, which are used to specify the target page that is
     *     redirected to when a continuous task notification is clicked.
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the continuous task is requested,
     *     **err** is **undefined**. Otherwise, **err** is an error object.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 202 - Not System App.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameters types; 3. Parameter verification failed.
     * @throws { BusinessError } 9800001 - Memory operation failed.
     * @throws { BusinessError } 9800002 - Failed to write data into parcel. Possible reasons: 1. Invalid parameters;
     *     <br> 2. Failed to apply for memory.
     * @throws { BusinessError } 9800003 - Internal transaction failed.
     * @throws { BusinessError } 9800004 - System service operation failed.
     * @throws { BusinessError } 9800005 - Continuous task verification failed.
     * @throws { BusinessError } 9800006 - Notification verification failed for a continuous task.
     * @throws { BusinessError } 9800007 - Continuous task storage failed.
     * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
     * @atomicservice [since 12]
     * @since 9
     */
    function startBackgroundRunning(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent, callback: AsyncCallback<void>): void;
    /**
     * Requests a continuous task of a specific type. This API uses a promise to return the result. After a continuous
     * task is successfully requested, there will be a notification message without prompt tone. A UIAbility (
     * ServiceAbility in the FA model) can request only one continuous task at a time through this API. You can request
     * multiple continuous tasks by calling
     * [startBackgroundRunning]{@link backgroundTaskManager.startBackgroundRunning(context: Context, request: ContinuousTaskRequest)}
     * added in API version 21.
     *
     * @permission ohos.permission.KEEP_BACKGROUND_RUNNING
     * @param { Context } context - Application context.
     *     <br>For details about the application context of the FA model, see
     *     [Context]{@link ./app/context}.<br>For details about the application context of the stage model, see
     *     [Context]{@link ./application/Context:Context}.<br> Note: Continuous tasks can be requested only by the
     *     UIAbility in the stage model and the ServiceAbility in the FA model.
     * @param { BackgroundMode } bgMode - Type of the continuous task.
     * @param { WantAgent } wantAgent - Notification parameters, which are used to specify the target page that is
     *     redirected to when a continuous task notification is clicked.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 202 - Not System App.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameters types; 3. Parameter verification failed.
     * @throws { BusinessError } 9800001 - Memory operation failed.
     * @throws { BusinessError } 9800002 - Failed to write data into parcel. Possible reasons: 1. Invalid parameters;
     *     <br> 2. Failed to apply for memory.
     * @throws { BusinessError } 9800003 - Internal transaction failed.
     * @throws { BusinessError } 9800004 - System service operation failed.
     * @throws { BusinessError } 9800005 - Continuous task verification failed.
     * @throws { BusinessError } 9800006 - Notification verification failed for a continuous task.
     * @throws { BusinessError } 9800007 - Continuous task storage failed.
     * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
     * @atomicservice [since 12]
     * @since 9
     */
    function startBackgroundRunning(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent): Promise<void>;
    /**
     * Requests continuous tasks of multiple types. This API uses a promise to return the result. After a continuous task
     * is successfully requested, there will be a notification message without prompt tone. A UIAbility (ServiceAbility in
     * the FA model) can request only one continuous task at a time through this API. You can request multiple continuous
     * tasks by calling
     * [startBackgroundRunning]{@link backgroundTaskManager.startBackgroundRunning(context: Context, request: ContinuousTaskRequest)}
     * added in API version 21.
     *
     * @permission ohos.permission.KEEP_BACKGROUND_RUNNING
     * @param { Context } context - Application context.
     *     <br>For details about the application context of the FA model, see
     *     [Context]{@link ./app/context}.<br>For details about the application context of the stage model, see
     *     [Context]{@link ./application/Context:Context}.<br> Note: Continuous tasks can be requested only by the
     *     UIAbility in the stage model and the ServiceAbility in the FA model.
     * @param { string[] } bgModes - Types of continuous tasks.
     *     <br>For details about the available options, see
     *     [Item](docroot://task-management/continuous-task.md#use-cases).<br> Note: One or more types can be passed.
     * @param { WantAgent } wantAgent - Notification parameters, which are used to specify the target page that is
     *     redirected to when a continuous task notification is clicked.
     * @returns { Promise<ContinuousTaskNotification> } Promise that returns an object of the
     *     [ContinuousTaskNotification]{@link backgroundTaskManager.ContinuousTaskNotification} type.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameters types; 3. Parameter verification failed.
     * @throws { BusinessError } 9800001 - Memory operation failed.
     * @throws { BusinessError } 9800002 - Failed to write data into parcel. Possible reasons: 1. Invalid parameters;
     *     <br> 2. Failed to apply for memory.
     * @throws { BusinessError } 9800003 - Internal transaction failed.
     * @throws { BusinessError } 9800004 - System service operation failed.
     * @throws { BusinessError } 9800005 - Continuous task verification failed.
     * @throws { BusinessError } 9800006 - Notification verification failed for a continuous task.
     * @throws { BusinessError } 9800007 - Continuous task storage failed.
     * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
     * @atomicservice
     * @since 12
     */
    function startBackgroundRunning(context: Context, bgModes: string[], wantAgent: WantAgent): Promise<ContinuousTaskNotification>;
    /**
     * Requests a continuous task. This API allows a UIAbility (ServiceAbility in the FA model) to request multiple
     * continuous tasks and uses a promise to return the result. When using this API to request a continuous task, its
     * notification can be combined with that of an existing continuous task. For details, see
     * [ContinuousTaskRequest]{@link backgroundTaskManager.ContinuousTaskRequest}.
     *
     * A maximum of 10 continuous tasks can be created simultaneously. Upon successful creation of a continuous task, a
     * notification will be sent without a prompt tone.
     *
     * If a continuous task requested via this API includes multiple task types (including data transmission tasks), two
     * notifications will appear in the notification panel: one for the data transmission task and the other for the
     * remaining tasks. Removing either notification will cancel the continuous task and remove the other notification.
     * The continuous task notification ID returned by the API is the ID of the data transmission type, which is used to
     * update the data transmission progress.
     *
     * @permission ohos.permission.KEEP_BACKGROUND_RUNNING
     * @param { Context } context - Application context.
     *     <br>For details about the application context of the FA model, see
     *     [Context]{@link ./app/context}.<br>For details about the application context of the stage model, see
     *     [Context]{@link ./application/Context:Context}.<br> Note: Continuous tasks can be requested only by the
     *     UIAbility in the stage model and the ServiceAbility in the FA model.
     * @param { ContinuousTaskRequest } request - Request information of a continuous task, including the main type and
     *     subtype.
     * @returns { Promise<ContinuousTaskNotification> } Promise used to return the continuous task notification
     *     information, including the continuous task ID.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 9800001 - Memory operation failed.
     * @throws { BusinessError } 9800004 - System service operation failed.
     * @throws { BusinessError } 9800005 - Continuous task verification failed.
     * @throws { BusinessError } 9800006 - Notification verification failed for a continuous task.
     * @throws { BusinessError } 9800007 - Continuous task storage failed.
     * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
     * @atomicservice [since 26.0.0]
     * @since 21
     */
    function startBackgroundRunning(context: Context, request: ContinuousTaskRequest): Promise<ContinuousTaskNotification>;
    /**
     * Updates continuous tasks of multiple types. This API uses a promise to return the result. After a continuous task
     * is successfully updated, there will be a notification message without prompt tone.
     *
     * Before updating a continuous task, you can call
     * [getAllContinuousTasks]{@link backgroundTaskManager.getAllContinuousTasks(context: Context)} to retrieve
     * information about all existing continuous tasks. If there are no continuous tasks, the update will fail.
     *
     * This API can only be used to update continuous tasks that were requested via the following APIs:
     *
     * [startBackgroundRunning(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent, callback: AsyncCallback&lt;void&gt;): void]{@link backgroundTaskManager.startBackgroundRunning(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent, callback: AsyncCallback<void>)}
     *
     * [startBackgroundRunning(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent): Promise&lt;void&gt;]{@link backgroundTaskManager.startBackgroundRunning(context: Context, bgMode: BackgroundMode, wantAgent: WantAgent)}
     *
     * [startBackgroundRunning(context: Context, bgModes: string[], wantAgent: WantAgent): Promise&lt;ContinuousTaskNotification&gt;]{@link backgroundTaskManager.startBackgroundRunning(context: Context, bgModes: string[], wantAgent: WantAgent)}
     *
     * @permission ohos.permission.KEEP_BACKGROUND_RUNNING
     * @param { Context } context - Application context.
     *     <br>For details about the application context of the FA model, see
     *     [Context]{@link ./app/context}.<br>For details about the application context of the stage model, see
     *     [Context]{@link ./application/Context:Context}.<br> Note: Continuous tasks can be requested only by the
     *     UIAbility in the stage model and the ServiceAbility in the FA model.
     * @param { string[] } bgModes - Types of continuous tasks after the update.
     *     <br>For details about the available options,
     *     see [Item](docroot://task-management/continuous-task.md#use-cases).<br> Note: One or more types can be passed.
     * @returns { Promise<ContinuousTaskNotification> } Promise that returns an object of the
     *     [ContinuousTaskNotification]{@link backgroundTaskManager.ContinuousTaskNotification} type.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameters types; 3. Parameter verification failed.
     * @throws { BusinessError } 9800001 - Memory operation failed.
     * @throws { BusinessError } 9800002 - Failed to write data into parcel. Possible reasons: 1. Invalid parameters;
     *     <br> 2. Failed to apply for memory.
     * @throws { BusinessError } 9800003 - Internal transaction failed.
     * @throws { BusinessError } 9800004 - System service operation failed.
     * @throws { BusinessError } 9800005 - Continuous task verification failed.
     * @throws { BusinessError } 9800006 - Notification verification failed for a continuous task.
     * @throws { BusinessError } 9800007 - Continuous task storage failed.
     * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
     * @atomicservice
     * @since 12
     */
    function updateBackgroundRunning(context: Context, bgModes: string[]): Promise<ContinuousTaskNotification>;
    /**
     * Updates a continuous task. This API uses a promise to return the result. After a continuous task is successfully
     * updated, there will be a notification message without prompt tone.
     *
     * The following restrictions apply when updating a continuous task:
     *
     * 1. This API can only update continuous tasks requested via
     * [startBackgroundRunning(context: Context, request: ContinuousTaskRequest): Promise&lt;ContinuousTaskNotification&gt;]{@link backgroundTaskManager.startBackgroundRunning(context: Context, request: ContinuousTaskRequest)}.
     * 2. If the main type and subtype of the background tasks are the same,
     * only the wants information (such as **abilityName**) in **ContinuousTaskRequest.wantAgent** can be updated.
     * If the types are different, the update fails.
     * 3. If the continuous task to be updated or the specified update type contains the data transmission type,
     * a failure message is returned.
     *
     * @permission ohos.permission.KEEP_BACKGROUND_RUNNING
     * @param { Context } context - Application context.
     *     <br>For details about the application context of the FA model, see
     *     [Context]{@link ./app/context}.<br>For details about the application context of the stage model, see
     *     [Context]{@link ./application/Context:Context}.<br> Note: Continuous tasks can be requested only by the
     *     UIAbility in the stage model and the ServiceAbility in the FA model.
     * @param { ContinuousTaskRequest } request - Continuous task request information, including the ID of the continuous
     *     task to be updated.
     * @returns { Promise<ContinuousTaskNotification> } Promise used to return the updated continuous task notification
     *     information, including the continuous task ID.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 9800001 - Memory operation failed.
     * @throws { BusinessError } 9800004 - System service operation failed.
     * @throws { BusinessError } 9800005 - Continuous task verification failed.
     * @throws { BusinessError } 9800006 - Notification verification failed for a continuous task.
     * @throws { BusinessError } 9800007 - Continuous task storage failed.
     * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
     * @atomicservice [since 26.0.0]
     * @since 21
     */
    function updateBackgroundRunning(context: Context, request: ContinuousTaskRequest): Promise<ContinuousTaskNotification>;
    /**
     * Cancels all continuous tasks in the current UIAbility (ServiceAbility in the FA model). This API uses an
     * asynchronous callback to return the result. You can also call the
     * [stopBackgroundRunning]{@link backgroundTaskManager.stopBackgroundRunning(context: Context, continuousTaskId: number)}
     * API to cancel a continuous task with the specified ID.
     *
     * @param { Context } context - Application context.
     *     <br>For details about the application context of the FA model, see
     *     [Context]{@link ./app/context}.<br>For details about the application context of the stage model, see
     *     [Context]{@link ./application/Context:Context}.<br> Note: Continuous tasks can be requested only by the
     *     UIAbility in the stage model and the ServiceAbility in the FA model.
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the continuous task is canceled,
     *     **err** is **undefined**. Otherwise, **err** is an error object.
     * @throws { BusinessError } 201 - Permission denied. [since 9 - 18]
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     * @throws { BusinessError } 9800001 - Memory operation failed.
     * @throws { BusinessError } 9800002 - Failed to write data into parcel. Possible reasons: 1. Invalid parameters;
     *     <br> 2. Failed to apply for memory.
     * @throws { BusinessError } 9800003 - Internal transaction failed.
     * @throws { BusinessError } 9800004 - System service operation failed.
     * @throws { BusinessError } 9800005 - Continuous task verification failed.
     * @throws { BusinessError } 9800006 - Notification verification failed for a continuous task.
     * @throws { BusinessError } 9800007 - Continuous task storage failed.
     * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
     * @atomicservice [since 12]
     * @since 9
     */
    function stopBackgroundRunning(context: Context, callback: AsyncCallback<void>): void;
    /**
     * Cancels all continuous tasks in the current UIAbility (ServiceAbility in the FA model). This API uses a promise to
     * return the result. You can also call the
     * [stopBackgroundRunning]{@link backgroundTaskManager.stopBackgroundRunning(context: Context, continuousTaskId: number)}
     * API to cancel a continuous task with the specified ID.
     *
     * @param { Context } context - Application context.
     *     <br>For details about the application context of the FA model, see
     *     [Context]{@link ./app/context}.<br>For details about the application context of the stage model, see
     *     [Context]{@link ./application/Context:Context}.<br> Note: Continuous tasks can be requested only by the
     *     UIAbility in the stage model and the ServiceAbility in the FA model.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 201 - Permission denied. [since 9 - 18]
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     * @throws { BusinessError } 9800001 - Memory operation failed.
     * @throws { BusinessError } 9800002 - Failed to write data into parcel. Possible reasons: 1. Invalid parameters;
     *     <br> 2. Failed to apply for memory.
     * @throws { BusinessError } 9800003 - Internal transaction failed.
     * @throws { BusinessError } 9800004 - System service operation failed.
     * @throws { BusinessError } 9800005 - Continuous task verification failed.
     * @throws { BusinessError } 9800006 - Notification verification failed for a continuous task.
     * @throws { BusinessError } 9800007 - Continuous task storage failed.
     * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
     * @atomicservice [since 12]
     * @since 9
     */
    function stopBackgroundRunning(context: Context): Promise<void>;
    /**
     * Cancels a continuous task with the specified ID. This API uses a promise to return the result. You can also call
     * the
     * [stopBackgroundRunning]{@link backgroundTaskManager.stopBackgroundRunning(context: Context, callback: AsyncCallback<void>)}
     * API to cancel all continuous tasks in the current UIAbility.
     *
     * @param { Context } context - Application context.
     *     <br>For details about the application context of the FA model, see
     *     [Context]{@link ./app/context}.<br>For details about the application context of the stage model, see
     *     [Context]{@link ./application/Context:Context}.<br> Note: Continuous tasks can be requested only by the
     *     UIAbility in the stage model and the ServiceAbility in the FA model.
     * @param { number } continuousTaskId - Continuous task ID.
     *     <br>The value should be an integer.
     *     <br>Note: You can obtain the ID of the current continuous task
     *     through the return value of the
     *     [startBackgroundRunning]{@link backgroundTaskManager.startBackgroundRunning(context: Context, request: ContinuousTaskRequest)}
     *     API, or obtain information about all continuous tasks through the
     *     [getAllContinuousTasks]{@link backgroundTaskManager.getAllContinuousTasks(context: Context, includeSuspended: boolean)}
     *     API.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 9800001 - Memory operation failed.
     * @throws { BusinessError } 9800004 - System service operation failed.
     * @throws { BusinessError } 9800005 - Continuous task verification failed.
     * @throws { BusinessError } 9800006 - Notification verification failed for a continuous task.
     * @throws { BusinessError } 9800007 - Continuous task storage failed.
     * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
     * @atomicservice [since 26.0.0]
     * @since 21
     */
    function stopBackgroundRunning(context: Context, continuousTaskId: number): Promise<void>;
    /**
     * Obtains all continuous task information, including the task ID and type. This API uses a promise to return the
     * result.
     *
     * @permission ohos.permission.KEEP_BACKGROUND_RUNNING
     * @param { Context } context - Application context.
     *     <br>For details about the application context of the FA model, see
     *     [Context]{@link ./app/context}.<br>For details about the application context of the stage model, see
     *     [Context]{@link ./application/Context:Context}.<br> Note: Continuous tasks can be requested only by the
     *     UIAbility in the stage model and the ServiceAbility in the FA model.
     * @returns { Promise<ContinuousTaskInfo[]> } Promise that returns all continuous task information.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 9800002 - Failed to write data into parcel. Possible reasons: 1. Invalid parameters;
     *     <br> 2. Failed to apply for memory.
     * @throws { BusinessError } 9800004 - System service operation failed.
     * @throws { BusinessError } 9800005 - Continuous task verification failed.
     * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
     * @since 20
     */
    function getAllContinuousTasks(context: Context): Promise<ContinuousTaskInfo[]>;
    /**
     * Obtains all continuous task information, including the task ID and type. It supports specifying whether to include
     * suspended tasks and uses a promise to return the result.
     *
     * @permission ohos.permission.KEEP_BACKGROUND_RUNNING
     * @param { Context } context - Application context.
     *     <br>For details about the application context of the FA model, see
     *     [Context]{@link ./app/context}.<br>For details about the application context of the stage model, see
     *     [Context]{@link ./application/Context:Context}.<br> Note: Continuous tasks can be requested only by the
     *     UIAbility in the stage model and the ServiceAbility in the FA model.
     * @param { boolean } includeSuspended - Whether to obtain the information about the suspended continuous task. The
     *     value **true** means to obtain the information, and the value **false** means the opposite.
     * @returns { Promise<ContinuousTaskInfo[]> } Promise that returns all continuous task information.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 9800002 - Failed to write data into parcel. Possible reasons: 1. Invalid parameters;
     *     2. Failed to apply for memory.
     * @throws { BusinessError } 9800004 - System service operation failed.
     * @throws { BusinessError } 9800005 - Continuous task verification failed.
     * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
     * @since 20
     */
    function getAllContinuousTasks(context: Context, includeSuspended: boolean): Promise<ContinuousTaskInfo[]>;
    /**
     * Subscribes to continuous task cancellation events. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.KEEP_BACKGROUND_RUNNING
     * @param { 'continuousTaskCancel' } type - Event type. The value is fixed at **'continuousTaskCancel'**, indicating
     *     that a continuous task is canceled.
     * @param { Callback<ContinuousTaskCancelInfo> } callback - Callback used to return information such as the reason for
     *     canceling a continuous task.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible cause: 1. Callback parameter error;
     *     <br> 2. Register a exist callback type; 3. Parameter verification failed.
     * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
     * @since 15
     */
    function on(type: 'continuousTaskCancel', callback: Callback<ContinuousTaskCancelInfo>): void;
    /**
      * Unsubscribes from continuous task cancellation events. This API uses an asynchronous callback to return the
      * result.
      *
      * @permission ohos.permission.KEEP_BACKGROUND_RUNNING
      * @param { 'continuousTaskCancel' } type - Cancels a continuous task. The value is fixed at
      *     **'continuousTaskCancel'**.
      * @param { Callback<ContinuousTaskCancelInfo> } callback - Callback for which listening is cancelled. If this
      *     parameter is left unspecified, all registered callbacks are cancelled.
      * @throws { BusinessError } 201 - Permission denied.
      * @throws { BusinessError } 401 - Parameter error. Possible cause: 1. Callback parameter error;
      *     <br> 2. Unregister type has not register; 3. Parameter verification failed.
      * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
      * @since 15
      */
    function off(type: 'continuousTaskCancel', callback?: Callback<ContinuousTaskCancelInfo>): void;
    /**
     * Registers a listener for continuous task suspension. This API uses an asynchronous callback to return the result.
     * After the callback is registered, if the system detects for the first time that the application does not execute
     * the corresponding service, the system does not directly cancel the continuous task. Instead, it will mark the task
     * as suspended. If the detection failures persist, the system will cancel the continuous task.
     *
     * When a continuous task is suspended, the application will be suspended when switched to the background and
     * automatically activated when brought back to the foreground.
     *
     * @permission ohos.permission.KEEP_BACKGROUND_RUNNING
     * @param { 'continuousTaskSuspend' } type - Event type. The value is fixed at **'continuousTaskSuspend'**, indicating
     *     that the continuous task is suspended.
     * @param { Callback<ContinuousTaskSuspendInfo> } callback - Callback used to return information such as the reason
     *     for suspending a continuous task.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 9800005 - Continuous task verification failed.
     * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
     * @since 20
     */
    function on(type: 'continuousTaskSuspend', callback: Callback<ContinuousTaskSuspendInfo>): void;
    /**
     * Unregisters from the listener for continuous task suspension. This API uses an asynchronous callback to return the
     * result.
     *
     * @permission ohos.permission.KEEP_BACKGROUND_RUNNING
     * @param { 'continuousTaskSuspend' } type - Event type. The value is fixed at **'continuousTaskSuspend'**, indicating
     *     that the continuous task is suspended.
     * @param { Callback<ContinuousTaskSuspendInfo> } [callback] - Callback used to unregister from the listener for
     *     continuous task suspension. If this parameter is not passed, all listeners are unsubscribed from.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 9800005 - Continuous task verification failed.
     * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
     * @since 20
     */
    function off(type: 'continuousTaskSuspend', callback?: Callback<ContinuousTaskSuspendInfo>): void;
    /**
     * Registers a listener for continuous task activation. This API uses an asynchronous callback to return the result.
     * The application returns to the foreground to activate the suspended continuous task.
     *
     * @permission ohos.permission.KEEP_BACKGROUND_RUNNING
     * @param { 'continuousTaskActive' } type - Event type. The value is fixed at **'continuousTaskActive'**, indicating
     *     that the continuous task is activated.
     * @param { Callback<ContinuousTaskActiveInfo> } callback - Callback used to return the activation information about a
     *     continuous task.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 9800005 - Continuous task verification failed.
     * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
     * @since 20
     */
    function on(type: 'continuousTaskActive', callback: Callback<ContinuousTaskActiveInfo>): void;
    /**
     * Unregisters from the listener for continuous task activation. This API uses an asynchronous callback to return the
     * result.
     *
     * @permission ohos.permission.KEEP_BACKGROUND_RUNNING
     * @param { 'continuousTaskActive' } type - Event type. The value is fixed at **'continuousTaskActive'**, indicating
     *     that the continuous task is activated.
     * @param { Callback<ContinuousTaskActiveInfo> } [callback] - Callback used to unregister from the listener for
     *     continuous task activation. If this parameter is not passed, all listeners are unsubscribed from.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 9800005 - Continuous task verification failed.
     * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
     * @since 20
     */
    function off(type: 'continuousTaskActive', callback?: Callback<ContinuousTaskActiveInfo>): void;
    /**
     * Defines the type of a continuous task.
     *
     * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
     * @atomicservice [since 12]
     * @since 9
     */
    export enum BackgroundMode {
        /**
         * Data transfer.
         *
         * Use scenario: upload and download in non-hosting mode, for example, uploading or downloading data in the
         * background of a browser.
         *
         * Note: During data transfer, the application needs to update the progress. If the progress is not updated for more
         * than 10 minutes, the continuous task of the **DATA_TRANSFER** type will be canceled.
         *
         * The notification type of the progress update must be live view. For details, see the example in
         * [startBackgroundRunning()]{@link backgroundTaskManager.startBackgroundRunning(context: Context, bgModes: string[], wantAgent: WantAgent)}
         * .
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 9
         */
        DATA_TRANSFER = 1,
        /**
         * Audio and video playback.
         *
         * Use scenario: audio/video playback in the background and audio/video casting.
         *
         * Note: Since API version 20, if an application requests or updates a continuous task of the **AUDIO_PLAYBACK**
         * type without connecting to AVSession, a notification will appear in the notification panel once the task is
         * successfully requested or updated.
         *
         * Once AVSession is connected, notifications will be sent by AVSession instead of the background task module.
         *
         * For API version 19 and earlier versions, the background task module does not display notifications in the
         * notification panel.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @atomicservice [since 12]
         * @since 9
         */
        AUDIO_PLAYBACK = 2,
        /**
         * Audio recording.
         *
         * Use scenario: recording and screen capture in the background.<!--Del-->
         *
         * Note: No notification is displayed if a system application requests or updates a continuous task.<!--DelEnd-->
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 9
         */
        AUDIO_RECORDING = 3,
        /**
         * Positioning and navigation.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @atomicservice [since 26.0.0]
         * @since 9
         */
        LOCATION = 4,
        /**
         * Bluetooth-related services.
         *
         * Use scenario: An application moves to the background while transferring files via Bluetooth.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 9
         */
        BLUETOOTH_INTERACTION = 5,
        /**
         * Multi-device connection.
         *
         * Use scenario: distributed service connection and casting.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @atomicservice [since 12]
         * @since 9
         */
        MULTI_DEVICE_CONNECTION = 6,
        /**
         * Audio and video calls.
         *
         * Use scenario: Chat applications (with audio and video services) transition into the background during audio and
         * video calls.<!--Del-->
         *
         * Note: No notification is displayed if a system application requests or updates a continuous task.<!--DelEnd-->
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 13
         */
        VOIP = 8,
        /**
         * Computing tasks.
         *
         * Use scenario: antivirus software.
         *
         * **NOTE**: Starting from API version 21, this capability is available for PCs/2-in-1 devices, and non-PCs/2-in-1
         * devices that have obtained the ACL permission
         * [ohos.permission.KEEP_BACKGROUND_RUNNING_SYSTEM](docroot://security/AccessToken/restricted-permissions.md#ohospermissionkeep_background_running_system)
         * . In API version 20 and earlier versions, this task type is limited to PCs/2-in-1 devices only.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 9
         */
        TASK_KEEPING = 9
    }
    /**
     * Main type of a continuous task. It is usually used together with the subtype
     * [BackgroundTaskSubmode]{@link backgroundTaskManager.BackgroundTaskSubmode}. For details, see the mapping table. The
     * two types are newly added in API version 21 for
     * [requesting]{@link backgroundTaskManager.startBackgroundRunning(context: Context, request: ContinuousTaskRequest)}
     * and
     * [updating]{@link backgroundTaskManager.updateBackgroundRunning(context: Context, request: ContinuousTaskRequest)}
     * continuous tasks.
     *
     * When the main type of the continuous task is **MODE_SPECIAL_SCENARIO_PROCESSING**, or that of a non-PC/2-in-1
     * device is **MODE_TASK_KEEPING**, you need to request the ACL permission
     * [ohos.permission.KEEP_BACKGROUND_RUNNING_SYSTEM](docroot://security/AccessToken/restricted-permissions.md#ohospermissionkeep_background_running_system)
     * before calling APIs related to continuous tasks. In other scenarios, this permission is not required.
     *
     * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
     * @atomicservice [since 26.0.0]
     * @since 21
     */
    export enum BackgroundTaskMode {
        /**
         * Data transfer.
         *
         * Use scenario: upload and download in non-hosting mode, for example, uploading or downloading data in the
         * background of a browser.
         *
         * **NOTE**
         *
         * 1. During data transfer, the application needs to update the progress.
         * If the progress is not updated for more than 10 minutes,
         * the continuous task of the **DATA_TRANSFER** type will be canceled.
         * 2. The notification type of the progress update must be live view. For details, see the example in
         * [startBackgroundRunning()]{@link backgroundTaskManager.startBackgroundRunning(context: Context, bgModes: string[], wantAgent: WantAgent)}.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 21
         */
        MODE_DATA_TRANSFER = 1,
        /**
         * Audio and video playback.
         *
         * Use scenario: audio/video playback in the background and audio/video casting.
         *
         * Note: If a continuous task of the **MODE_AUDIO_PLAYBACK** type is requested or updated without connecting to
         * AVSession, a notification will appear in the notification panel once the task is successfully requested or
         * updated. Once AVSession is connected, notifications will be sent by AVSession instead of the background task
         * module.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @atomicservice [since 26.0.0]
         * @since 21
         */
        MODE_AUDIO_PLAYBACK = 2,
        /**
         * Audio recording.
         *
         * Use scenario: recording and screen capture in the background.<!--Del-->
         *
         * Note: No notification is displayed if a system application requests or updates a continuous task.<!--DelEnd-->
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 21
         */
        MODE_AUDIO_RECORDING = 3,
        /**
         * Positioning and navigation.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @atomicservice [since 26.0.0]
         * @since 21
         */
        MODE_LOCATION = 4,
        /**
         * Bluetooth-related services.
         *
         * Use scenario: An application moves to the background while transferring files via Bluetooth.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 21
         */
        MODE_BLUETOOTH_INTERACTION = 5,
        /**
         * Multi-device connection.
         *
         * Use scenario: distributed service connection and casting.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @atomicservice [since 26.0.0]
         * @since 21
         */
        MODE_MULTI_DEVICE_CONNECTION = 6,
        /**
         * Audio and video calls.
         *
         * Use scenario: Chat applications (with audio and video services) transition into the background during audio and
         * video calls. <!--Del-->
         *
         * Note: No notification is displayed if a system application requests or updates a continuous task.<!--DelEnd-->
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 21
         */
        MODE_VOIP = 8,
        /**
         * Computing tasks.
         *
         * Use scenario: antivirus software.
         *
         * **NOTE**: This capability is available only to PCs/2-in-1 devices, or non-PCs/2-in-1 devices that have obtained
         * the ACL permission
         * [ohos.permission.KEEP_BACKGROUND_RUNNING_SYSTEM](docroot://security/AccessToken/restricted-permissions.md#ohospermissionkeep_background_running_system)
         * .
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 21
         */
        MODE_TASK_KEEPING = 9,
        /**
         * Multimedia services.
         *
         * Use scenarios: audio/video playback, recording, and audio/video calls. The scenario must match that of the
         * subtype. You can select this task type or the corresponding main type for preceding scenarios. For example, you
         * can request a continuous task of the **MODE_AUDIO_PLAYBACK** or **MODE_AV_PLAYBACK_AND_RECORD** type for audio/
         * video playback.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @atomicservice [since 26.0.0]
         * @since 22
         */
        MODE_AV_PLAYBACK_AND_RECORD = 12,
        /**
         * Special scenarios (available only for smartphones, tablets, PCs/2-in-1 devices).
         *
         * Use scenarios: An application exports media files in the background or uses a third-party component to cast
         * content in the background. The scenario must match that of the subtype.
         *
         * **NOTE**
         *
         * 1. If an application needs to run in the background for a long time,
         * it can request user authorization through the
         * [requestAuthFromUser]{@link backgroundTaskManager.ContinuousTaskRequest.requestAuthFromUser} API
         * and check the authorization result via
         * [checkSpecialScenarioAuth]{@link backgroundTaskManager.ContinuousTaskRequest.checkSpecialScenarioAuth}.
         * 2. Since API version 24, this capability is available only to applications that have obtainedthe ACL permission
         * [ohos.permission.KEEP_BACKGROUND_RUNNING_SPECIAL_SCENARIO](docroot://security/AccessToken/restricted-permissions.md#ohospermissionkeep_background_running_special_scenario).
         * For API version 23 and earlier,
         * this capability is available only to applications that have obtained the ACL permission
         * [ohos.permission.KEEP_BACKGROUND_RUNNING_SYSTEM](docroot://security/AccessToken/restricted-permissions.md#ohospermissionkeep_background_running_system).
         * Applications that have obtained this permission are not affected for API version 24 and later.
         * 3. This task type must be used independently and notifications cannot be combined.
         * Specifically, when you request or update a continuous task,
         * it must be of the **MODE_SPECIAL_SCENARIO_PROCESSING** type. Otherwise, an error is returned.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 22
         */
        MODE_SPECIAL_SCENARIO_PROCESSING = 13,
        /**
         * NearLink device.
         *
         * Use scenario: An application transitions into the background during the process of file transfer using NearLink.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @stagemodelonly
         * @since 26.0.0
         */
        MODE_NEARLINK = 14
    }
    /**
     * Defines the subtype of a continuous task. It is usually used together with the main type
     * [BackgroundTaskMode]{@link backgroundTaskManager.BackgroundTaskMode}. For details, see the mapping table. The two
     * types are newly added in API version 21 for requesting and updating continuous tasks.
     *
     * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
     * @atomicservice [since 26.0.0]
     * @since 21
     */
    export enum BackgroundTaskSubmode {
        /**
         * **CAR_KEY** type. It is of the normal text notification type.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 21
         */
        SUBMODE_CAR_KEY_NORMAL_NOTIFICATION = 1,
        /**
         * Normal text notification.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @atomicservice [since 26.0.0]
         * @since 21
         */
        SUBMODE_NORMAL_NOTIFICATION = 2,
        /**
         * Live view notification.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 21
         */
        SUBMODE_LIVE_VIEW_NOTIFICATION = 3,
        /**
         * Audio and video playback. It is of the normal text notification type.
         * You can access [AVSession](docroot://media/avsession/avsession-overview.md) as needed.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @atomicservice [since 26.0.0]
         * @since 22
         */
        SUBMODE_AUDIO_PLAYBACK_NORMAL_NOTIFICATION = 4,
        /**
         * Audio and video playback scenario where [AVSession](docroot://media/avsession/avsession-overview.md) is accessed.
         * It is of the normal text notification type.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @atomicservice [since 26.0.0]
         * @since 22
         */
        SUBMODE_AVSESSION_AUDIO_PLAYBACK = 5,
        /**
         * Recording. It is of the normal text notification type.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 22
         */
        SUBMODE_AUDIO_RECORD_NORMAL_NOTIFICATION = 6,
        /**
         * Recording. It is of the normal text notification type.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 22
         */
        SUBMODE_SCREEN_RECORD_NORMAL_NOTIFICATION = 7,
        /**
         * Call. It is of the normal text notification type.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 22
         */
        SUBMODE_VOICE_CHAT_NORMAL_NOTIFICATION = 8,
        /**
         * Media processing. For example, an application exports media files in the background. It is of the normal text
         * notification type.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 22
         */
        SUBMODE_MEDIA_PROCESS_NORMAL_NOTIFICATION = 9,
        /**
         * Video casting. For example, an application uses a third-party casting component to cast a video in the
         * background, and the notification type is common text notification.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 22
         */
        SUBMODE_VIDEO_BROADCAST_NORMAL_NOTIFICATION = 10,
        /**
         * Exercise. For example, an application has an indoor running scenario in the background, and the notification type
         * is common text notification.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @stagemodelonly
         * @since 23
         */
        SUBMODE_WORK_OUT_NORMAL_NOTIFICATION = 11
    }
    /**
     * Describes the reason for canceling a continuous task.
     *
     * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
     * @since 15
     */
    export enum ContinuousTaskCancelReason {
        /**
         * The task is canceled by the user.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 15
         */
        USER_CANCEL = 1,
        /**
         * The task is canceled by the system.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 15
         */
        SYSTEM_CANCEL = 2,
        /**
         * User removal notification. This value is reserved.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 15
         */
        USER_CANCEL_REMOVE_NOTIFICATION = 3,
        /**
         * A continuous task of the DATA_TRANSFER type is requested, but the data transmission rate is low. This value is
         * reserved.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 15
         */
        SYSTEM_CANCEL_DATA_TRANSFER_LOW_SPEED = 4,
        /**
         * A continuous task of the AUDIO_PLAYBACK type is requested, but the
         * [AVSession](docroot://media/avsession/avsession-overview.md) is not accessed. This value is reserved.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 15
         */
        SYSTEM_CANCEL_AUDIO_PLAYBACK_NOT_USE_AVSESSION = 5,
        /**
         * A continuous task of the AUDIO_PLAYBACK type is requested, but the audio and video are not played. This value is
         * reserved.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 15
         */
        SYSTEM_CANCEL_AUDIO_PLAYBACK_NOT_RUNNING = 6,
        /**
         * A continuous task of the AUDIO_RECORDING type is requested, but audio recording is not in progress. This value is
         * reserved.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 15
         */
        SYSTEM_CANCEL_AUDIO_RECORDING_NOT_RUNNING = 7,
        /**
         * A continuous task of the **LOCATION** type is requested, but the location service is not in use. This value is
         * reserved.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 15
         */
        SYSTEM_CANCEL_NOT_USE_LOCATION = 8,
        /**
         * A continuous task of the BLUETOOTH_INTERACTION type is requested, but Bluetooth-related services are not used.
         * This value is reserved.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 15
         */
        SYSTEM_CANCEL_NOT_USE_BLUETOOTH = 9,
        /**
         * A continuous task of the MULTI_DEVICE_CONNECTION type is requested, but multi-device connection is not used. This
         * value is reserved.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 15
         */
        SYSTEM_CANCEL_NOT_USE_MULTI_DEVICE = 10,
        /**
         * A continuous task of an invalid type is used. For example, a continuous task of the **AUDIO_PLAYBACK** type is
         * requested, but the audio playback and location services are in use. This value is reserved.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 15
         */
        SYSTEM_CANCEL_USE_ILLEGALLY = 11
    }
    /**
     * Describes the detailed reason for canceling a continuous task.
     *
     * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
     * @stagemodelonly
     * @since 26.0.0
     */
    export enum ContinuousTaskDetailedCancelReason {
        /**
         * User removal notification.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @stagemodelonly
         * @since 26.0.0
         */
        USER_CANCEL_REMOVE_NOTIFICATION = 3,
        /**
         * A continuous task of the **DATA_TRANSFER** type is requested, but the data transmission rate is low.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @stagemodelonly
         * @since 26.0.0
         */
        SYSTEM_CANCEL_DATA_TRANSFER_LOW_SPEED = 4,
        /**
         * A continuous task of the **AUDIO_PLAYBACK** type is requested, but the audio and video are not played.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @stagemodelonly
         * @since 26.0.0
         */
        SYSTEM_CANCEL_AUDIO_PLAYBACK_NOT_RUNNING = 6,
        /**
         * A continuous task of the **AUDIO_RECORDING** type is requested, but audio recording is not in progress.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @stagemodelonly
         * @since 26.0.0
         */
        SYSTEM_CANCEL_AUDIO_RECORDING_NOT_RUNNING = 7,
        /**
         * A continuous task of the **LOCATION** type is requested, but the location service is not in use.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @stagemodelonly
         * @since 26.0.0
         */
        SYSTEM_CANCEL_NOT_USE_LOCATION = 8,
        /**
         * A continuous task of the **BLUETOOTH_INTERACTION** type is requested, but Bluetooth is not in use.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @stagemodelonly
         * @since 26.0.0
         */
        SYSTEM_CANCEL_NOT_USE_BLUETOOTH = 9,
        /**
         * A continuous task of the **MULTI_DEVICE_CONNECTION** type is requested, but the multi-device connection service
         * is not in use.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @stagemodelonly
         * @since 26.0.0
         */
        SYSTEM_CANCEL_NOT_USE_MULTI_DEVICE = 10,
        /**
         * A continuous task of an invalid type is used. For example, a continuous task of the **AUDIO_PLAYBACK** type is
         * requested, but the audio playback and location services are in use.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @stagemodelonly
         * @since 26.0.0
         */
        SYSTEM_CANCEL_USE_ILLEGALLY = 11,
        /**
         * A continuous task of the **DATA_TRANSFER** type is requested, but the progress is not updated for a long time (
         * the first update takes more than 10 minutes).
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @stagemodelonly
         * @since 26.0.0
         */
        SYSTEM_CANCEL_DATA_TRANSFER_NOT_UPDATE = 12,
        /**
         * A continuous task of the **VOIP** type is requested, but no audio stream or recording stream is in progress.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @stagemodelonly
         * @since 26.0.0
         */
        SYSTEM_CANCEL_VOIP_NOT_RUNNING = 13,
        /**
         * A continuous task of the special scenario type is requested, but the user is not authorized.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @stagemodelonly
         * @since 26.0.0
         */
        SYSTEM_CANCEL_USER_UNAUTHORIZED = 14
    }
    /**
     * Defines the subtype of a continuous task.
     *
     * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
     * @since 16
     */
    export enum BackgroundSubMode {
        /**
         * Car key.
         *
         * **NOTE**
         *
         * 1. The car key subtype takes effect only when a continuous task of the BLUETOOTH_INTERACTION type is requested.
         * 2. Continuous tasks of this type cannot be updated through the [updateBackgroundRunning]{@link backgroundTaskManager.updateBackgroundRunning(context: Context, bgModes: string[])} API.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 16
         */
        CAR_KEY = 1
    }
    /**
     * Defines the type of a continuous task.
     *
     * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
     * @since 16
     */
    export enum BackgroundModeType {
        /**
         * Subtype.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 16
         */
        SUB_MODE = 'subMode'
    }
    /**
     * Describes the reason why a continuous task is suspended.
     *
     * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
     * @since 20
     */
    export enum ContinuousTaskSuspendReason {
        /**
         * A continuous task of the **DATA_TRANSFER** type is requested, but the data transmission rate is low.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 20
         */
        SYSTEM_SUSPEND_DATA_TRANSFER_LOW_SPEED = 4,
        /**
         * A continuous task of the **AUDIO_PLAYBACK** type is requested, but
         * [AVSession](docroot://media/avsession/avsession-overview.md) is not accessed.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 20
         */
        SYSTEM_SUSPEND_AUDIO_PLAYBACK_NOT_USE_AVSESSION = 5,
        /**
         * A continuous task of the **AUDIO_PLAYBACK** type is requested, but audio playback is not in progress.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 20
         */
        SYSTEM_SUSPEND_AUDIO_PLAYBACK_NOT_RUNNING = 6,
        /**
         * A continuous task of the **AUDIO_RECORDING** type is requested, but audio recording is not in progress.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 20
         */
        SYSTEM_SUSPEND_AUDIO_RECORDING_NOT_RUNNING = 7,
        /**
         * A continuous task of the **LOCATION** type is requested, but the location service is not in use.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 20
         */
        SYSTEM_SUSPEND_LOCATION_NOT_USED = 8,
        /**
         * A continuous task of the **BLUETOOTH_INTERACTION** type is requested, but Bluetooth is not in use.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 20
         */
        SYSTEM_SUSPEND_BLUETOOTH_NOT_USED = 9,
        /**
         * A continuous task of the **MULTI_DEVICE_CONNECTION** type is requested, but the multi-device connection service
         * is not in use.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 20
         */
        SYSTEM_SUSPEND_MULTI_DEVICE_NOT_USED = 10,
        /**
         * A continuous task of an invalid type is used. For example, a continuous task of the **AUDIO_PLAYBACK** type is
         * requested, but the audio playback and location services are in use. This value is reserved.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 20
         */
        SYSTEM_SUSPEND_USED_ILLEGALLY = 11,
        /**
         * A continuous task is suspended due to high system load. This value is reserved.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 20
         */
        SYSTEM_SUSPEND_SYSTEM_LOAD_WARNING = 12,
        /**
         * A continuous task of the **VOIP** type is requested, but no audio stream or recording stream is in progress.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @stagemodelonly
         * @since 26.0.0
         */
        SYSTEM_SUSPEND_VOIP_NOT_USED = 13,
        /**
         * A continuous task of the **BLUETOOTH_INTERACTION** type is requested, but there is no Bluetooth data flow for a
         * period of time.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @stagemodelonly
         * @since 26.0.0
         */
        SYSTEM_SUSPEND_BLUETOOTH_DATA_NOT_EXIST = 14,
        /**
         * A continuous task of the **LOCATION** type is requested, but the device is absolutely still for a period of time.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @stagemodelonly
         * @since 26.0.0
         */
        SYSTEM_SUSPEND_POSITION_NOT_MOVED = 15,
        /**
         * A continuous task of the **AUDIO_PLAYBACK** type is requested, but the device is muted for a period of time.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @stagemodelonly
         * @since 26.0.0
         */
        SYSTEM_SUSPEND_AUDIO_PLAYBACK_MUTE = 16,
        /**
         * No nearlink connection for a period of time when request nearlink mode.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @stagemodelonly
         * @since 26.0.0
         */
        SYSTEM_SUSPEND_NEARLINK_NOT_USED = 17,
        /**
         * No nearlink data for a period of time when request nearlink mode.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @stagemodelonly
         * @since 26.0.0
         */
        SYSTEM_SUSPEND_NEARLINK_DATA_NOT_EXIST = 18,
        /**
         * A continuous task of the special scenario type is requested, but the user is not authorized.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @stagemodelonly
         * @since 26.0.0
         */
        SYSTEM_SUSPEND_USER_UNAUTHORIZED = 19
    }
    /**
     * Represents the user authorization result.
     *
     * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
     * @since 22
     */
    export enum UserAuthResult {
        /**
         * The authorization is not supported. For example, if the main type of the requested continuous task is not
         * **MODE_SPECIAL_SCENARIO_PROCESSING**, continuous task running in the background is not supported.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 22
         */
        NOT_SUPPORTED = 0,
        /**
         * No user operation.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 22
         */
        NOT_DETERMINED = 1,
        /**
         * The authorization is denied.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 22
         */
        DENIED = 2,
        /**
         * The authorization is granted this time.
         *
         * Note: The authorization record will be cleared when the application exits.
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 22
         */
        GRANTED_ONCE = 3,
        /**
         * The authorization is granted always.
         *
         * **NOTE**
         *
         * When the following common events are received, the related authorization records will be cleared:
         *
         * [COMMON_EVENT_PACKAGE_ADDED](docroot://reference/apis-basic-services-kit/common_event/commonEventManager-definitions.md#common_event_package_added)
         * ,
         * [COMMON_EVENT_PACKAGE_REMOVED](docroot://reference/apis-basic-services-kit/common_event/commonEventManager-definitions.md#common_event_package_removed)
         * ,
         * [COMMON_EVENT_BUNDLE_REMOVED](docroot://reference/apis-basic-services-kit/common_event/commonEventManager-definitions.md#common_event_bundle_removed)
         * ,
         * [COMMON_EVENT_PACKAGE_FULLY_REMOVED](docroot://reference/apis-basic-services-kit/common_event/commonEventManager-definitions.md#common_event_package_fully_removed)
         * ,
         * [COMMON_EVENT_PACKAGE_CHANGED](docroot://reference/apis-basic-services-kit/common_event/commonEventManager-definitions.md#common_event_package_changed)
         * .
         *
         * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
         * @since 22
         */
        GRANTED_ALWAYS = 4
    }
}
export default backgroundTaskManager;

```
