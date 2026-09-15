# @ohos.reminderAgentManager.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022-2026 Huawei Device Co., Ltd.
 * Licensed under the Apache License, Version 2.0 (the "License"),
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
/**
 * @file Agent-powered Reminder
 * @kit BackgroundTasksKit
 */
import { AsyncCallback } from './@ohos.base';
import notification from './@ohos.notificationManager';
import { NotificationSlot } from './notification/notificationSlot';
import type { Callback } from './@ohos.base';
/**
 * The **reminderAgentManager** module provides APIs related to agent-powered reminders. When your application is frozen
 * or exits, the application's scheduled notification capability will be taken over by a system service running in the
 * background. You can use the APIs to create scheduled reminders for countdown timers, calendar events, and alarm
 * clocks. For details, see [Agent-powered Reminder](docroot://task-management/agent-powered-reminder.md).
 *
 * @syscap SystemCapability.Notification.ReminderAgent
 * @since 9
 */
declare namespace reminderAgentManager {
    /**
     * Publishes a reminder. This API uses an asynchronous callback to return the result.
     *
     * > **NOTE**
     * >
     * > This API can be called only after the
     * > [notificationManager.requestEnableNotification]{@link @ohos.notificationManager:notificationManager.requestEnableNotification(context: UIAbilityContext, callback: AsyncCallback<void>)}
     * > permission is obtained.
     * >
     *
     * @permission ohos.permission.PUBLISH_AGENT_REMINDER
     * @param { ReminderRequest } reminderReq - Request used for publishing the reminder.
     * @param { AsyncCallback<number> } callback - Callback used to return the result.
     *     After the agent-powered reminder is
     *     published, **err** is **undefined**, and **data** is the ID of the published reminder. Otherwise, **err** is an
     *     error object.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - If the input parameter is not valid parameter.
     * @throws { BusinessError } 1700001 - Notification is not enabled.
     * @throws { BusinessError } 1700002 - The number of reminders exceeds the limit.
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 9
     */
    function publishReminder(reminderReq: ReminderRequest, callback: AsyncCallback<number>): void;
    /**
     * Publishes a reminder. This API uses a promise to return the result.
     *
     * > **NOTE**
     * >
     * > This API can be called only after the
     * > [notificationManager.requestEnableNotification]{@link @ohos.notificationManager:notificationManager.requestEnableNotification(context: UIAbilityContext, callback: AsyncCallback<void>)}
     * > permission is obtained.
     * >
     *
     * @permission ohos.permission.PUBLISH_AGENT_REMINDER
     * @param { ReminderRequest } reminderReq - Request used for publishing the reminder.
     * @returns { Promise<number> } Promise used to return the published reminder ID.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - If the input parameter is not valid parameter.
     * @throws { BusinessError } 1700001 - Notification is not enabled.
     * @throws { BusinessError } 1700002 - The number of reminders exceeds the limit.
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 9
     */
    function publishReminder(reminderReq: ReminderRequest): Promise<number>;
    /**
     * Cancels a reminder published. This API uses an asynchronous callback to return the result.
     *
     * @param { number } reminderId - ID of the agent-powered reminder to be canceled.
     *     The reminder ID is returned when the
     *     [publishReminder]{@link reminderAgentManager.publishReminder(reminderReq: ReminderRequest, callback: AsyncCallback<number>)}
     *     API is called.
     * @param { AsyncCallback<void> } callback - Callback used to return the result.
     *     If all the reminders are canceled,
     *     **err** is **undefined**. Otherwise, **err** is an error object.
     * @throws { BusinessError } 401 - If the input parameter is not valid parameter.
     * @throws { BusinessError } 1700003 - The reminder does not exist.
     * @throws { BusinessError } 1700004 - The bundle name does not exist.
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 9
     */
    function cancelReminder(reminderId: number, callback: AsyncCallback<void>): void;
    /**
     * Cancels a reminder published. This API uses a promise to return the result.
     *
     * @param { number } reminderId - ID of the agent-powered reminder to be canceled.
     *     The reminder ID is returned when the
     *     [publishReminder]{@link reminderAgentManager.publishReminder(reminderReq: ReminderRequest, callback: AsyncCallback<number>)}
     *     API is called.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 401 - If the input parameter is not valid parameter.
     * @throws { BusinessError } 1700003 - The reminder does not exist.
     * @throws { BusinessError } 1700004 - The bundle name does not exist.
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 9
     */
    function cancelReminder(reminderId: number): Promise<void>;
    /**
     * Cancels the notification card displayed in the notification center with the agent reminder data retained. For
     * example, for a daily repeating reminder, calling this API removes the card from the notification center, but the
     * reminder will be triggered again the next day according to its schedule.
     *
     * @param { number } reminderId - ID of the agent-powered reminder to be canceled.
     *     The reminder ID is returned when the
     *     [publishReminder]{@link reminderAgentManager.publishReminder(reminderReq: ReminderRequest, callback: AsyncCallback<number>)}
     *     API is called
     *     <br>The value range is all integers.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 1700003 - The reminder does not exist.
     * @throws { BusinessError } 1700007 - If the input parameter is not valid parameter.
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 23
     */
    function cancelReminderOnDisplay(reminderId: number): Promise<void>;
    /**
     * Obtains all [valid (not yet expired) reminders](docroot://task-management/agent-powered-reminder.md#constraints)
     * set by the current application. This API uses an asynchronous callback to return the result.
     *
     * @param { AsyncCallback<Array<ReminderRequest>> } callback - Callback used to return the result.
     *     If the agent-powered reminder is queried, **err** is **undefined**, and **data** contains all valid (not yet
     *     expired) reminders set by the current application. Otherwise, **err** is an error object.
     * @throws { BusinessError } 401 - If the input parameter is not valid parameter.
     * @throws { BusinessError } 1700004 - The bundle name does not exist.
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 9
     */
    function getValidReminders(callback: AsyncCallback<Array<ReminderRequest>>): void;
    /**
     * Obtains all [valid (not yet expired) reminders](docroot://task-management/agent-powered-reminder.md#constraints)
     * set by the current application. This API uses a promise to return the result.
     *
     * @returns { Promise<Array<ReminderRequest>> } Promise used to return all the valid reminders.
     * @throws { BusinessError } 401 - If the input parameter is not valid parameter.
     * @throws { BusinessError } 1700004 - The bundle name does not exist.
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 9
     */
    function getValidReminders(): Promise<Array<ReminderRequest>>;
    /**
     * Cancels all reminders set by the current application. This API uses an asynchronous callback to return the result.
     *
     * @param { AsyncCallback<void> } callback - Callback used to return the result.
     *     If all the reminders are canceled,
     *     **err** is **undefined**. Otherwise, **err** is an error object.
     * @throws { BusinessError } 401 - If the input parameter is not valid parameter.
     * @throws { BusinessError } 1700004 - The bundle name does not exist.
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 9
     */
    function cancelAllReminders(callback: AsyncCallback<void>): void;
    /**
     * Cancels all reminders set by the current application. This API uses a promise to return the result.
     *
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 401 - If the input parameter is not valid parameter.
     * @throws { BusinessError } 1700004 - The bundle name does not exist.
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 9
     */
    function cancelAllReminders(): Promise<void>;
    /**
     * Updates the agent-powered reminder with the specified ID. This API uses a promise to return the result. Only
     * [valid (not yet expired) reminders](docroot://task-management/agent-powered-reminder.md#constraints) that are not
     * displayed in the notification panel can be updated.
     *
     * @permission ohos.permission.PUBLISH_AGENT_REMINDER
     * @param { number } reminderId - ID of the agent-powered reminder to be updated.
     *     The reminder ID is returned when the
     *     [publishReminder]{@link reminderAgentManager.publishReminder(reminderReq: ReminderRequest, callback: AsyncCallback<number>)}
     *     API is called.
     * @param { ReminderRequest } reminderReq - Request instance used to set detailed information such as the reminder
     *     type and ringing duration.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 1700003 - The reminder does not exist.
     * @throws { BusinessError } 1700007 - If the input parameter is not valid parameter.
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 20
     */
    function updateReminder(reminderId: number, reminderReq: ReminderRequest): Promise<void>;
    /**
     * Adds a notification slot. This API uses an asynchronous callback to return the result.
     *
     * @param { NotificationSlot } slot - Notification slot instance. Only the **notificationType** property can be set.
     * @param { AsyncCallback<void> } callback - Callback used to return the result.
     *     If the notification slot is added,
     *     **err** is **undefined**. Otherwise, **err** is an error object.
     * @throws { BusinessError } 401 - If the input parameter is not valid parameter.
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 9
     */
    function addNotificationSlot(slot: NotificationSlot, callback: AsyncCallback<void>): void;
    /**
     * Adds a notification slot. This API uses a promise to return the result.
     *
     * @param { NotificationSlot } slot - Notification slot instance. Only the **notificationType** property can be set.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 401 - If the input parameter is not valid parameter.
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 9
     */
    function addNotificationSlot(slot: NotificationSlot): Promise<void>;
    /**
     * Removes a specified notification slot. This API uses an asynchronous callback to return the result.
     *
     * @param { notification.SlotType } slotType - Type of the notification slot.
     * @param { AsyncCallback<void> } callback - Callback used to return the result.
     *     If the notification slot is removed,
     *     **err** is **undefined**. Otherwise, **err** is an error object.
     * @throws { BusinessError } 401 - If the input parameter is not valid parameter.
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 9
     */
    function removeNotificationSlot(slotType: notification.SlotType, callback: AsyncCallback<void>): void;
    /**
     * Removes a specified notification slot. This API uses a promise to return the result.
     *
     * @param { notification.SlotType } slotType - Type of the notification slot.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 401 - If the input parameter is not valid parameter.
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 9
     */
    function removeNotificationSlot(slotType: notification.SlotType): Promise<void>;
    /**
     * Adds a non-reminder date for a recurring calendar reminder with a specific ID. For example, configure a daily
     * reminder to skip notifications on Tuesdays. This API uses a promise to return the result.
     *
     * @param { number } reminderId - ID of the agent-powered reminder to be added.
     *     The reminder ID is returned when the
     *     [publishReminder]{@link reminderAgentManager.publishReminder(reminderReq: ReminderRequest, callback: AsyncCallback<number>)}
     *     API is called.
     * @param { Date } date - Non-reminder date.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 201 - Permission denied
     * @throws { BusinessError } 401 - If the input parameter is not valid parameter.
     * @throws { BusinessError } 1700003 - The reminder does not exist.
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 12
     */
    function addExcludeDate(reminderId: number, date: Date): Promise<void>;
    /**
     * Deletes all non-reminder dates for a recurring calendar reminder with a specific ID. This API uses a promise to
     * return the result.
     *
     * @param { number } reminderId - ID of the agent-powered reminder to be removed.
     *     The reminder ID is returned when the
     *     [publishReminder]{@link reminderAgentManager.publishReminder(reminderReq: ReminderRequest, callback: AsyncCallback<number>)}
     *     API is called.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 201 - Permission denied
     * @throws { BusinessError } 1700003 - The reminder does not exist.
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 12
     */
    function deleteExcludeDates(reminderId: number): Promise<void>;
    /**
     * Obtains all non-reminder dates for a recurring calendar reminder with a specific ID. This API uses a promise to
     * return the result.
     *
     * @param { number } reminderId - ID of the agent-powered reminder to be queried.
     *     The reminder ID is returned when the
     *     [publishReminder]{@link reminderAgentManager.publishReminder(reminderReq: ReminderRequest, callback: AsyncCallback<number>)}
     *     API is called.
     * @returns { Promise<Array<Date>> } Promise used to return all the non-reminder dates.
     * @throws { BusinessError } 201 - Permission denied
     * @throws { BusinessError } 1700003 - The reminder does not exist.
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 12
     */
    function getExcludeDates(reminderId: number): Promise<Array<Date>>;
    /**
     * Obtains all [valid (not yet expired) reminders](docroot://task-management/agent-powered-reminder.md#constraints)
     * set by the current application. This API uses a promise to return the result. To call this API, you need to request
     * the ohos.permission.PUBLISH_AGENT_REMINDER permission.
     *
     * @returns { Promise<Array<ReminderInfo>> } Promise used to return all the valid reminders.
     * @throws { BusinessError } 201 - Permission denied.
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 12
     */
    function getAllValidReminders(): Promise<Array<ReminderInfo>>;
    /**
     * Subscribes to agent-powered reminder state changes. This API uses a promise to return the result.
     *
     * @permission ohos.permission.PUBLISH_AGENT_REMINDER
     * @param { Callback<Array<ReminderState>> } callback - Callback used to return the agent-powered reminder state.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 1700007 - If the input parameter is not valid parameter.
     * @syscap SystemCapability.Notification.ReminderAgent
     * @stagemodelonly
     * @since 23
     */
    function subscribeReminderState(callback: Callback<Array<ReminderState>>): Promise<void>;
    /**
     * Unsubscribes from agent-powered reminder state changes. This API uses a promise to return the result.
     *
     * @param { Callback<Array<ReminderState>> } [callback] - Callback used to return the result. If the **callback**
     *     parameter is not passed, all subscriptions are canceled.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 1700007 - If the input parameter is not valid parameter.
     * @syscap SystemCapability.Notification.ReminderAgent
     * @stagemodelonly
     * @since 23
     */
    function unsubscribeReminderState(callback?: Callback<Array<ReminderState>>): Promise<void>;
    /**
     * Enumerates the types of buttons displayed for a reminder.
     *
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 9
     */
    export enum ActionButtonType {
        /**
         * Button for closing the reminder.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 9
         */
        ACTION_BUTTON_TYPE_CLOSE = 0,
        /**
         * Button for snoozing the reminder, with the frequency and timing configured via **snoozeTimes** and
         * **timeInterval** in the [ReminderRequest]{@link reminderAgentManager.ReminderRequest} struct.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 9
         */
        ACTION_BUTTON_TYPE_SNOOZE = 1
    }
    /**
     * Enumerates the reminder types.
     *
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 9
     */
    export enum ReminderType {
        /**
         * Countdown reminder.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 9
         */
        REMINDER_TYPE_TIMER = 0,
        /**
         * Calendar reminder.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 9
         */
        REMINDER_TYPE_CALENDAR = 1,
        /**
         * Alarm reminder.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 9
         */
        REMINDER_TYPE_ALARM = 2
    }
    /**
     * Enumerates the audio playback channels for the custom prompt tone.
     *
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 20
     */
    export enum RingChannel {
        /**
         * Alarm channel.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 20
         */
        RING_CHANNEL_ALARM = 0,
        /**
         * Media channel.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 20
         */
        RING_CHANNEL_MEDIA = 1,
        /**
         * Notification slot.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 23
         */
        RING_CHANNEL_NOTIFICATION = 2
    }
    /**
     * Enumerates the time zone types. When the time zone is changed, the reminder time is recalculated based
     * on the new time zone.
     *
     * @syscap SystemCapability.Notification.ReminderAgent
     * @stagemodelonly
     * @since 26.0.0
     */
    export enum TimeZoneType {
        /**
         * Default value. When the time zone is changed, the reminder time is calculated in the same way as that
         * for the time zone type of **FIXED_TIME_ZONE**. When the time is changed, the reminder time is calculated
         * in the same way as that for the time zone type of **SYSTEM_TIME_ZONE**. You are advised to set the time
         * zone type to **FIXED_TIME_ZONE** or **SYSTEM_TIME_ZONE** based on the service scenario.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @stagemodelonly
         * @since 26.0.0
         */
        DEFAULT = 0,
        /**
         * Fixed time zone, which is used in scenarios such as ticket booking and meetings. For example, if the reminder
         * time is set to 08:00 (GMT+8), the reminder will be triggered at 08:00 (GMT+8) no matter whether the device time
         * zone is changed. If the device time zone is changed to GMT+4, the reminder will be triggered at 04:00. The
         * reminder time is not affected by the change of the system time.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @stagemodelonly
         * @since 26.0.0
         */
        FIXED_TIME_ZONE = 1,
        /**
         * System time zone, which is used in scenarios such as setting the alarm clock, fixed time for exercise, and sleep time.
         * For example, if the reminder time is set to 08:00 (GMT+8), and the time zone is changed to GMT+4, the reminder will
         * still be triggered at 08:00. The reminder time is not affected by the change of the system time.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @stagemodelonly
         * @since 26.0.0
         */
        SYSTEM_TIME_ZONE = 2
    }
    /**
     * Describes the button displayed for a reminder.
     *
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 9
     */
    interface ActionButton {
        /**
         * Text on the button.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 9
         */
        title: string;
        /**
         * Resource ID of the title. This parameter is used to read the title information after the system language is
         * switched.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 11
         */
        titleResource?: string;
        /**
         * Button type.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 9
         */
        type: ActionButtonType;
    }
    /**
     * Defines the information about the redirected-to ability.
     *
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 9
     */
    interface WantAgent {
        /**
         * Name of the target package.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 9
         */
        pkgName: string;
        /**
         * Name of the target ability.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 9
         */
        abilityName: string;
        /**
         * URI of the target ability.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 12
         */
        uri?: string;
        /**
         * Parameters to be transferred to the target.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 12
         */
        parameters?: Record<string, Object>;
    }
    /**
     * Describes the information about the ability that is started automatically and displayed in full-screen mode when a
     * reminder is displayed in the notification center. This API is reserved.
     *
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 9
     */
    interface MaxScreenWantAgent {
        /**
         * Name of the target package. (If the device is in use, only a notification banner is displayed.)
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 9
         */
        pkgName: string;
        /**
         * Name of the target ability. (If the device is in use, only a notification banner is displayed.)
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 9
         */
        abilityName: string;
    }
    /**
     * Notification request proxy.
     *
     * @syscap SystemCapability.Notification.ReminderAgent
     * @stagemodelonly
     * @since 26.0.0
     */
    interface NotificationRequestProxy {
        /**
         * Unique ID carried in a notification sent by an application, which is used for notification deduplication.
         * This parameter is left empty by default. For details, see
         * [NotificationRequest.appMessageId]{@link ./notification/notificationRequest:NotificationRequest}.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @stagemodelonly
         * @since 26.0.0
         */
        appMessageId?: string;
        /**
         * Whether to send a notification alert only once when a notification is published or updated. The default value is
         * **false**. For details, see
         * [NotificationRequest.isAlertOnce]{@link ./notification/notificationRequest:NotificationRequest}.
         *
         * - **true**: An alert is sent only when the notification is published for the first time. For subsequent update,
         * the alert mode is changed to [LEVEL_LOW]{@link @ohos.notificationManager:notificationManager.SlotLevel}.
         * - **false**: The alert is sent in the configured alert mode.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @stagemodelonly
         * @since 26.0.0
         */
        isAlertOnce?: boolean;
    }
    /**
     * Defines the request for publishing a reminder.
     *
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 9
     */
    interface ReminderRequest {
        /**
         * Type of the reminder.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 9
         */
        reminderType: ReminderType;
        /**
         * Buttons displayed for the reminder notification.
         *
         * For third-party applications, a maximum of two buttons are supported.
         *
         * For system applications, a maximum of three buttons are supported in API version 10 and later versions, and a
         * maximum of two buttons are supported in versions earlier than API version 10.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 9
         */
        actionButton?: [
            ActionButton?,
            ActionButton?,
            ActionButton?
        ];
        /**
         * Information about the ability that is redirected to when the reminder is clicked.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 9
         */
        wantAgent?: WantAgent;
        /**
         * Information about the ability that is started automatically and displayed in full-screen mode when the reminder
         * arrives. If the device is in use, only a notification banner is displayed.
         *
         * This API is reserved.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 9
         */
        maxScreenWantAgent?: MaxScreenWantAgent;
        /**
         * Ringing duration.
         *
         * The value ranges from 0 to1800, in seconds. The default value is **1**.
         *
         * If the value is **0**, the system notification tone is used.
         *
         * If the value is greater than 0 and [ReminderRequest.customRingUri]{@link reminderAgentManager.ReminderRequest} is
         * set, the reminder rings on the specified channel
         * [ReminderRequest.ringChannel]{@link reminderAgentManager.ReminderRequest}. Otherwise, the custom notification
         * tone of the agent-powered reminder is used.
         *
         * The device vibrates when the reminder rings. Since API version 26.0.0, long vibration is supported, and the
         * vibration duration is the same as the ring duration. In versions earlier than API 26.0.0, the device vibrates
         * once quickly when the reminder rings.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 9
         */
        ringDuration?: number;
        /**
         * Audio channel of the custom prompt tone. The default channel is the alarm channel.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 20
         */
        ringChannel?: RingChannel;
        /**
         * Number of reminder snooze times. The default value is **0**. (It is not applicable to countdown reminders.)
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 9
         */
        snoozeTimes?: number;
        /**
         * Reminder snooze interval,
         *
         * in seconds. The minimum value is 30s. (It is not applicable to countdown reminders.)
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 9
         */
        timeInterval?: number;
        /**
         * Reminder title.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 9
         */
        title?: string;
        /**
         * Resource ID of the reminder title, which can be obtained through $r(*resource-name*).id.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 18
         */
        titleResourceId?: number;
        /**
         * Reminder content.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 9
         */
        content?: string;
        /**
         * Resource ID of the reminder content, which can be obtained through $r(*resource-name*).id.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 18
         */
        contentResourceId?: number;
        /**
         * Content to be displayed after the reminder expires.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 9
         */
        expiredContent?: string;
        /**
         * Resource ID of the content to be displayed after the reminder expires, which can be obtained through $r(*resource
         * -name*).id.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 18
         */
        expiredContentResourceId?: number;
        /**
         * Content to be displayed when the reminder is snoozing. (It is not applicable to countdown reminders.)
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 9
         */
        snoozeContent?: string;
        /**
         * Resource ID of the content to be displayed when the reminder is snoozing, which can be obtained through $r(
         * *resource-name*).id.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 18
         */
        snoozeContentResourceId?: number;
        /**
         * Notification ID used by the reminder. You must pass in a notification ID. If there are reminders with the same
         * notification ID, the later one will overwrite the earlier one. The default value is **0**.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 9
         */
        notificationId?: number;
        /**
         * Group ID used for the reminder. If "Don't ask again" or similar information is selected for the reminder, other
         * reminders with the same group ID are also canceled.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 11
         */
        groupId?: string;
        /**
         * Type of the slot used by the reminder.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 9
         */
        slotType?: notification.SlotType;
        /**
         * Whether the reminder is automatically cleared. The default value is **true**. For details, see
         * [NotificationRequest.tapDismissed]{@link ./notification/notificationRequest:NotificationRequest.tapDismissed}
         *
         * - **true** (default): The reminder is automatically cleared after the notification or button is tapped.
         * - **false**: The reminder is retained after the notification or button is tapped.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 10
         */
        tapDismissed?: boolean;
        /**
         * Time when the notification is automatically cleared.
         *
         * The data format is timestamp, in milliseconds. For details, please refer to
         * [NotificationRequest.autoDeletedTime]{@link ./notification/notificationRequest:NotificationRequest.autoDeletedTime}
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 10
         */
        autoDeletedTime?: number;
        /**
         * Type of the slot used by the snoozed reminder. (It is not applicable to countdown reminders.)
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 11
         */
        snoozeSlotType?: notification.SlotType;
        /**
         * URI of the custom prompt tone. The prompt tone file must be stored in the **resources/rawfile** directory and
         * supports formats such as M4A, AAC, MP3, OGG, WAV, FLAC, and AMR.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 11
         */
        customRingUri?: string;
        /**
         * Time zone type. The default value is **TimeZoneType.DEFAULT**.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @stagemodelonly
         * @since 26.0.0
         */
        fixedTimeZone?: TimeZoneType;
        /**
         * Notification request message. This parameter is left empty by default.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @stagemodelonly
         * @since 26.0.0
         */
        notificationRequestProxy?: NotificationRequestProxy;
    }
    /**
     * ReminderRequestCalendar extends ReminderRequest
     *
     * Defines a reminder for a calendar event.
     *
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 9
     */
    interface ReminderRequestCalendar extends ReminderRequest {
        /**
         * Reminder time.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 9
         */
        dateTime: LocalDateTime;
        /**
         * Month in which the reminder repeats. The value range is [1, 12]. This parameter is left empty by default. This
         * parameter must be used together with **repeatDays**.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 9
         */
        repeatMonths?: Array<number>;
        /**
         * Day in which the reminder repeats. The value range is [1, 31]. This parameter is left empty by default. This
         * parameter must be used together with **repeatMonths**.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 9
         */
        repeatDays?: Array<number>;
        /**
         * Days of a week when the reminder repeats. The value ranges from 1 to 7, corresponding to the data from Monday to
         * Sunday. This parameter is left empty by default.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 11
         */
        daysOfWeek?: Array<number>;
        /**
         * End time of the reminder.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 12
         */
        endDateTime?: LocalDateTime;
    }
    /**
     * ReminderRequestAlarm extends ReminderRequest
     *
     * Defines a reminder for an alarm.
     *
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 9
     */
    interface ReminderRequestAlarm extends ReminderRequest {
        /**
         * Hour portion of the reminder time. The value range is [0, 23].
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 9
         */
        hour: number;
        /**
         * Minute portion of the reminder time. The value range is [0, 59].
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 9
         */
        minute: number;
        /**
         * Days of a week when the reminder repeats. The value ranges from 1 to 7, corresponding to the data from Monday to
         * Sunday. This parameter is left empty by default.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 9
         */
        daysOfWeek?: Array<number>;
    }
    /**
     * ReminderRequestTimer extends ReminderRequest
     *
     * Defines a reminder for a scheduled timer.
     *
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 9
     */
    interface ReminderRequestTimer extends ReminderRequest {
        /**
         * Number of seconds in the countdown timer.
         *
         * Unit: s
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 9
         */
        triggerTimeInSeconds: number;
        /**
         * Repeat interval. There is no default value. If no value is set, there is no repeat interval. This parameter
         * must be used together with **repeatCount**.
         *
         * The value range is [86400, +∞), in seconds. If the value is out of range, error code 401 is returned.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @stagemodelonly
         * @since 26.0.0
         */
        repeatInterval?: number;
        /**
         * Number of repetitions. The default value is **0**, indicating infinite repetitions. This parameter must be used
         * together with **repeatInterval**.
         *
         * The value range is [0, +∞). If the value is out of range, error code 401 is returned.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @stagemodelonly
         * @since 26.0.0
         */
        repeatCount?: number;
    }
    /**
     * Defines the reminder information.
     *
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 12
     */
    interface ReminderInfo {
        /**
         * Reminder ID.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 12
         */
        reminderId: number;
        /**
         * Request used for publishing the reminder.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 12
         */
        reminderReq: ReminderRequest;
    }
    /**
     * Defines the time information for a calendar reminder.
     *
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 9
     */
    interface LocalDateTime {
        /**
         * Year.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 9
         */
        year: number;
        /**
         * Month. The value ranges from 1 to 12.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 9
         */
        month: number;
        /**
         * Day. The value ranges from 1 to 31.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 9
         */
        day: number;
        /**
         * Hour. The value ranges from 0 to 23.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 9
         */
        hour: number;
        /**
         * Minute. The value ranges from 0 to 59.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 9
         */
        minute: number;
        /**
         * Second. The value ranges from 0 to 59.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 9
         */
        second?: number;
    }
    /**
     * Defines the agent-powered reminder state information, for which notifications are triggered in the following
     * scenarios:
     *
     * 1. When a user taps a button on an agent-powered reminder notification,
     * a notification specifying the tapped button type is sent to the application if it is running.
     * If the application is not running, the notification will not be received.
     * 2. Since the above scenario cannot guarantee that the application receives the notification,
     * all callbacks associated with user-tapped button types under the application are returned to the application
     * when it registers a new callback function. State information is retained for a maximum of 30 days.
     * Cached state information is cleared when the application registers a new callback function or has not registered
     * any callback function for more than 30 days.
     *
     * @syscap SystemCapability.Notification.ReminderAgent
     * @stagemodelonly
     * @since 23
     */
    interface ReminderState {
        /**
         * Reminder ID.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @stagemodelonly
         * @since 23
         */
        reminderId: number;
        /**
         * Button type.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @stagemodelonly
         * @since 23
         */
        buttonType: ActionButtonType;
        /**
         * Whether a message is sent repeatedly.
         *
         * - **false**: The message is sent for the first time. Applicable scenarios: The application is running when the
         * user taps a button on the agent-powered reminder notification; the application is not running when the user taps
         * the button, and the application registers a new callback function afterward.
         * - **true**: The message is sent repeatedly. Applicable scenario: The application is running and registers a new
         * callback function after the user taps a button on the agent-powered reminder notification.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @stagemodelonly
         * @since 23
         */
        isMessageResent: boolean;
    }
}
export default reminderAgentManager;

```
