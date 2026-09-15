# @ohos.reminderAgent.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2021-2026 Huawei Device Co., Ltd.
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
import notification from './@ohos.notification';
import { NotificationSlot } from './notification/notificationSlot';
/**
 * The **reminderAgent** module provides APIs for publishing scheduled reminders through the reminder agent.
 *
 * You can use the APIs to create scheduled reminders for countdown timers, calendar events, and alarm clocks. When the
 * created reminders are published, the timing and pop-up notification functions of your application will be taken over
 * by the reminder agent in the background when your application is frozen or exits.
 *
 * @syscap SystemCapability.Notification.ReminderAgent
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.reminderAgentManager:reminderAgentManager
 */
declare namespace reminderAgent {
    /**
     * Publishes a reminder through the reminder agent. This API uses an asynchronous callback to return the result. It
     * can be called only when notification is enabled for the application through
     * [Notification.requestEnableNotification]{@link @ohos.notification:notification.requestEnableNotification(callback: AsyncCallback<void>)}
     *
     * @permission ohos.permission.PUBLISH_AGENT_REMINDER
     * @param { ReminderRequest } reminderReq - Reminder to be published.
     * @param { AsyncCallback<number> } callback - Callback used to return the published reminder's ID.
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 7
     * @deprecated since 9
     * @useinstead reminderAgentManager.publishReminder
     */
    function publishReminder(reminderReq: ReminderRequest, callback: AsyncCallback<number>): void;
    /**
     * Publishes a reminder through the reminder agent. This API uses a promise to return the result. It can be called
     * only when notification is enabled for the application through
     * [Notification.requestEnableNotification]{@link @ohos.notification:notification.requestEnableNotification(callback: AsyncCallback<void>)}
     *
     * @permission ohos.permission.PUBLISH_AGENT_REMINDER
     * @param { ReminderRequest } reminderReq Indicates the reminder instance to publish.
     * @returns { Promise<number> } reminder id.
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 7
     * @deprecated since 9
     * @useinstead reminderAgentManager.publishReminder
     */
    function publishReminder(reminderReq: ReminderRequest): Promise<number>;
    /**
     * Cancels the reminder with the specified ID. This API uses an asynchronous callback to return the cancellation
     * result.
     *
     * @param { number } reminderId - ID of the reminder.
     * @param { AsyncCallback<void> } callback - Callback used to return the result.
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 7
     * @deprecated since 9
     * @useinstead reminderAgentManager.cancelReminder
     */
    function cancelReminder(reminderId: number, callback: AsyncCallback<void>): void;
    /**
     * Cancels the reminder with the specified ID. This API uses a promise to return the cancellation result.
     *
     * @param { number } reminderId - ID of the reminder.
     * @returns { Promise<void> } Promise used to return the result.
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 7
     * @deprecated since 9
     * @useinstead reminderAgentManager.cancelReminder
     */
    function cancelReminder(reminderId: number): Promise<void>;
    /**
     * Obtains all valid (not yet expired) reminders set by the current application. This API uses an asynchronous
     * callback to return the result.
     *
     * @param { AsyncCallback<Array<ReminderRequest>> } callback - Callback used to return an array of all valid reminders
     *     set by the current application.
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 7
     * @deprecated since 9
     * @useinstead reminderAgentManager.getValidReminders
     */
    function getValidReminders(callback: AsyncCallback<Array<ReminderRequest>>): void;
    /**
     * Obtains all valid (not yet expired) reminders set by the current application. This API uses a promise to return the
     * reminders.
     *
     * @returns { Promise<Array<ReminderRequest>> } Promise used to return an array of all valid reminders set by the
     *     current application.
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 7
     * @deprecated since 9
     * @useinstead reminderAgentManager.getValidReminders
     */
    function getValidReminders(): Promise<Array<ReminderRequest>>;
    /**
     * Cancels all reminders set by the current application. This API uses an asynchronous callback to return the
     * cancellation result.
     *
     * @param { AsyncCallback<void> } callback - Callback used to return the result.
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 7
     * @deprecated since 9
     * @useinstead reminderAgentManager.cancelAllReminders
     */
    function cancelAllReminders(callback: AsyncCallback<void>): void;
    /**
     * Cancels all reminders set by the current application. This API uses a promise to return the cancellation result.
     *
     * @returns { Promise<void> } Promise used to return the result.
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 7
     * @deprecated since 9
     * @useinstead reminderAgentManager.cancelAllReminders
     */
    function cancelAllReminders(): Promise<void>;
    /**
     * Adds a notification slot. This API uses an asynchronous callback to return the result.
     *
     * @param { NotificationSlot } slot - Notification slot, whose type can be set.
     * @param { AsyncCallback<void> } callback - Callback used to return the result.
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 7
     * @deprecated since 9
     * @useinstead reminderAgentManager.addNotificationSlot
     */
    function addNotificationSlot(slot: NotificationSlot, callback: AsyncCallback<void>): void;
    /**
     * Adds a notification slot. This API uses a promise to return the result.
     *
     * @param { NotificationSlot } slot - Notification slot, whose type can be set.
     * @returns { Promise<void> } Promise used to return the result.
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 7
     * @deprecated since 9
     * @useinstead reminderAgentManager.addNotificationSlot
     */
    function addNotificationSlot(slot: NotificationSlot): Promise<void>;
    /**
     * Removes a notification slot of a specified type. This API uses an asynchronous callback to return the result.
     *
     * @param { notification.SlotType } slotType - Type of the reminder notification slot to remove.
     * @param { AsyncCallback<void> } callback - Callback used to return the result.
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 7
     * @deprecated since 9
     * @useinstead reminderAgentManager.removeNotificationSlot
     */
    function removeNotificationSlot(slotType: notification.SlotType, callback: AsyncCallback<void>): void;
    /**
     * Removes a notification slot of a specified type. This API uses a promise to return the result.
     *
     * @param { notification.SlotType } slotType - Type of the reminder notification slot to remove.
     * @returns { Promise<void> } Promise used to return the result.
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 7
     * @deprecated since 9
     * @useinstead reminderAgentManager.removeNotificationSlot
     */
    function removeNotificationSlot(slotType: notification.SlotType): Promise<void>;
    /**
     * Enumerates the button types.
     *
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.reminderAgentManager:reminderAgentManager.ActionButtonType
     */
    export enum ActionButtonType {
        /**
         * Button for closing the reminder.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 7
         * @deprecated since 9
         * @useinstead reminderAgentManager.ActionButtonType.ACTION_BUTTON_TYPE_CLOSE
         */
        ACTION_BUTTON_TYPE_CLOSE = 0,
        /**
         * Button for snoozing the reminder.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 7
         * @deprecated since 9
         * @useinstead reminderAgentManager.ActionButtonType.ACTION_BUTTON_TYPE_SNOOZE
         */
        ACTION_BUTTON_TYPE_SNOOZE = 1
    }
    /**
     * Enumerates reminder types.
     *
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.reminderAgentManager:reminderAgentManager.ReminderType
     */
    export enum ReminderType {
        /**
         * Countdown reminder.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 7
         * @deprecated since 9
         * @useinstead reminderAgentManager.ReminderType.REMINDER_TYPE_TIMER
         */
        REMINDER_TYPE_TIMER = 0,
        /**
         * Calendar reminder.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 7
         * @deprecated since 9
         * @useinstead reminderAgentManager.ReminderType.REMINDER_TYPE_CALENDAR
         */
        REMINDER_TYPE_CALENDAR = 1,
        /**
         * Alarm reminder.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 7
         * @deprecated since 9
         * @useinstead reminderAgentManager.ReminderType.REMINDER_TYPE_ALARM
         */
        REMINDER_TYPE_ALARM = 2
    }
    /**
     * Defines a button displayed in the reminder notification.
     *
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.reminderAgentManager:reminderAgentManager.ActionButton
     */
    interface ActionButton {
        /**
         * Text on the button.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 7
         * @deprecated since 9
         * @useinstead reminderAgentManager.ActionButton.title
         */
        title: string;
        /**
         * Button type.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 7
         * @deprecated since 9
         * @useinstead reminderAgentManager.ActionButton.type
         */
        type: ActionButtonType;
    }
    /**
     * Sets the package and ability that are redirected to when the reminder notification is clicked.
     *
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.reminderAgentManager:reminderAgentManager.WantAgent
     */
    interface WantAgent {
        /**
         * Name of the HAP that is redirected to when the reminder notification is clicked.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 7
         * @deprecated since 9
         * @useinstead reminderAgentManager.WantAgent.pkgName
         */
        pkgName: string;
        /**
         * Name of the ability that is redirected to when the reminder notification is clicked.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 7
         * @deprecated since 9
         * @useinstead reminderAgentManager.WantAgent.abilityName
         */
        abilityName: string;
    }
    /**
     * Provides the information about the target package and ability to start automatically when the reminder is displayed
     * in full-screen mode. This API is reserved.
     *
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.reminderAgentManager:reminderAgentManager.MaxScreenWantAgent
     */
    interface MaxScreenWantAgent {
        /**
         * Name of the HAP that is automatically started when the reminder arrives and the device is not in use.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 7
         * @deprecated since 9
         * @useinstead reminderAgentManager.MaxScreenWantAgent.pkgName
         */
        pkgName: string;
        /**
         * Name of the ability that is automatically started when the reminder arrives and the device is not in use.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 7
         * @deprecated since 9
         * @useinstead reminderAgentManager.MaxScreenWantAgent.abilityName
         */
        abilityName: string;
    }
    /**
     * Defines the reminder to publish.
     *
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.reminderAgentManager:reminderAgentManager.ReminderRequest
     */
    interface ReminderRequest {
        /**
         * Type of the reminder.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 7
         * @deprecated since 9
         * @useinstead reminderAgentManager.ReminderRequest.reminderType
         */
        reminderType: ReminderType;
        /**
         * Button displayed in the reminder notification. (The parameter is optional. Up to two buttons are supported.)
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 7
         * @deprecated since 9
         * @useinstead reminderAgentManager.ReminderRequest.actionButton
         */
        actionButton?: [
            ActionButton?,
            ActionButton?
        ];
        /**
         * Information about the ability that is redirected to when the notification is clicked.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 7
         * @deprecated since 9
         * @useinstead reminderAgentManager.ReminderRequest.wantAgent
         */
        wantAgent?: WantAgent;
        /**
         * Information about the ability that is automatically started when the reminder arrives. If the device is in use, a
         * notification will be displayed.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 7
         * @deprecated since 9
         * @useinstead reminderAgentManager.ReminderRequest.maxScreenWantAgent
         */
        maxScreenWantAgent?: MaxScreenWantAgent;
        /**
         * Ringing duration, in seconds. The default value is **1**.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 7
         * @deprecated since 9
         * @useinstead reminderAgentManager.ReminderRequest.ringDuration
         */
        ringDuration?: number;
        /**
         * Number of reminder snooze times. The default value is **0**.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 7
         * @deprecated since 9
         * @useinstead reminderAgentManager.ReminderRequest.snoozeTimes
         */
        snoozeTimes?: number;
        /**
         * Reminder snooze interval, in seconds. The default value is **0**.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 7
         * @deprecated since 9
         * @useinstead reminderAgentManager.ReminderRequest.timeInterval
         */
        timeInterval?: number;
        /**
         * Reminder title.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 7
         * @deprecated since 9
         * @useinstead reminderAgentManager.ReminderRequest.title
         */
        title?: string;
        /**
         * Reminder content.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 7
         * @deprecated since 9
         * @useinstead reminderAgentManager.ReminderRequest.content
         */
        content?: string;
        /**
         * Content to be displayed after the reminder expires.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 7
         * @deprecated since 9
         * @useinstead reminderAgentManager.ReminderRequest.expiredContent
         */
        expiredContent?: string;
        /**
         * Content to be displayed when the reminder is snoozing.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 7
         * @deprecated since 9
         * @useinstead reminderAgentManager.ReminderRequest.snoozeContent
         */
        snoozeContent?: string;
        /**
         * Notification ID used by the reminder. If there are reminders with the same notification ID, the later one will
         * overwrite the earlier one.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 7
         * @deprecated since 9
         * @useinstead reminderAgentManager.ReminderRequest.notificationId
         */
        notificationId?: number;
        /**
         * Type of the slot used by the reminder.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 7
         * @deprecated since 9
         * @useinstead reminderAgentManager.ReminderRequest.slotType
         */
        slotType?: notification.SlotType;
    }
    /**
     * Defines a reminder for a calendar event.
     *
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.reminderAgentManager:reminderAgentManager.ReminderRequestCalendar
     */
    interface ReminderRequestCalendar extends ReminderRequest {
        /**
         * Reminder time.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 7
         * @deprecated since 9
         * @useinstead reminderAgentManager.ReminderRequestCalendar.dateTime
         */
        dateTime: LocalDateTime;
        /**
         * Month in which the reminder repeats.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 7
         * @deprecated since 9
         * @useinstead reminderAgentManager.ReminderRequestCalendar.repeatMonths
         */
        repeatMonths?: Array<number>;
        /**
         * Date on which the reminder repeats.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 7
         * @deprecated since 9
         * @useinstead reminderAgentManager.ReminderRequestCalendar.repeatDays
         */
        repeatDays?: Array<number>;
    }
    /**
     * Defines a reminder for an alarm.
     *
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.reminderAgentManager:reminderAgentManager.ReminderRequestAlarm
     */
    interface ReminderRequestAlarm extends ReminderRequest {
        /**
         * Hour portion of the reminder time.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 7
         * @deprecated since 9
         * @useinstead reminderAgentManager.ReminderRequestAlarm.hour
         */
        hour: number;
        /**
         * Minute portion of the reminder time.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 7
         * @deprecated since 9
         * @useinstead reminderAgentManager.ReminderRequestAlarm.minute
         */
        minute: number;
        /**
         * Days of a week when the reminder repeats. The value ranges from 1 to 7, corresponding to the data from Monday to
         * Sunday.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 7
         * @deprecated since 9
         * @useinstead reminderAgentManager.ReminderRequestAlarm.daysOfWeek
         */
        daysOfWeek?: Array<number>;
    }
    /**
     * Defines a reminder for a scheduled timer.
     *
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.reminderAgentManager:reminderAgentManager.ReminderRequestTimer
     */
    interface ReminderRequestTimer extends ReminderRequest {
        /**
         * Number of seconds in the countdown timer.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 7
         * @deprecated since 9
         * @useinstead reminderAgentManager.ReminderRequestTimer.triggerTimeInSeconds
         */
        triggerTimeInSeconds: number;
    }
    /**
     * Sets the time information for a calendar reminder.
     *
     * @syscap SystemCapability.Notification.ReminderAgent
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.reminderAgentManager:reminderAgentManager.LocalDateTime
     */
    interface LocalDateTime {
        /**
         * Year.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 7
         * @deprecated since 9
         * @useinstead reminderAgentManager.LocalDateTime.year
         */
        year: number;
        /**
         * Month.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 7
         * @deprecated since 9
         * @useinstead reminderAgentManager.LocalDateTime.month
         */
        month: number;
        /**
         * Date.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 7
         * @deprecated since 9
         * @useinstead reminderAgentManager.LocalDateTime.day
         */
        day: number;
        /**
         * Hour.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 7
         * @deprecated since 9
         * @useinstead reminderAgentManager.LocalDateTime.hour
         */
        hour: number;
        /**
         * Minute.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 7
         * @deprecated since 9
         * @useinstead reminderAgentManager.LocalDateTime.minute
         */
        minute: number;
        /**
         * Second.
         *
         * @syscap SystemCapability.Notification.ReminderAgent
         * @since 7
         * @deprecated since 9
         * @useinstead reminderAgentManager.LocalDateTime.second
         */
        second?: number;
    }
}
export default reminderAgent;

```
