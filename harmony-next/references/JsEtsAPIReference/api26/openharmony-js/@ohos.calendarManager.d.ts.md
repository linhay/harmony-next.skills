# @ohos.calendarManager.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022-2023 Huawei Device Co., Ltd.
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
 * @kit CalendarKit
 */
import { AsyncCallback } from './@ohos.base';
import type Context from './application/Context';
/**
 * The calendarManager module provides APIs for calendar and event management,
 * including those for creating, deleting, modifying, and querying calendars and events.
 *
 * @syscap SystemCapability.Applications.CalendarData
 * @atomicservice [since 11]
 * @since 10
 */
declare namespace calendarManager {
    /**
     * Obtains a CalendarManager object based on the context.
     *
     * @param { Context } context - Application context. For details about the application context
     * of the stage model, see Context.
     * @returns { CalendarManager } CalendarManager object obtained.
     * @syscap SystemCapability.Applications.CalendarData
     * @StageModelOnly
     * @atomicservice [since 11]
     * @since 10
     */
    function getCalendarManager(context: Context): CalendarManager;
    /**
    * Before calling any of the following APIs to manage the calendar, you must use
    * [getCalendarManager()]{@link calendarManager.getCalendarManager} to obtain a **CalendarManager** object first.
    *
    * @syscap SystemCapability.Applications.CalendarData
    * @atomicservice [since 11]
    * @since 10
    */
    export interface CalendarManager {
        /**
         * Creates a Calendar object based on the calendar account information.
         * This API uses a promise to return the result.
         *
         * @permission ohos.permission.WRITE_CALENDAR or ohos.permission.WRITE_WHOLE_CALENDAR
         * @param { CalendarAccount } calendarAccount - Calendar account information.
         * @returns { Promise<Calendar> } Promise used to return the created Calendar object.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 23900004 - Internal program errors. Possible causes:
         *     <br>1. dataShare database execution error;
         *	   <br>2. null pointer error;
         *     <br>3. Data parsing error. [since 23]
         * @syscap SystemCapability.Applications.CalendarData
         * @since 10
         */
        createCalendar(calendarAccount: CalendarAccount): Promise<Calendar>;
        /**
         * Creates a Calendar object based on the calendar account information.
         * This API uses an asynchronous callback to return the result.
         *
         * @permission ohos.permission.WRITE_CALENDAR or ohos.permission.WRITE_WHOLE_CALENDAR
         * @param { CalendarAccount } calendarAccount - Calendar account information.
         * @param { AsyncCallback<Calendar> } callback - Callback used to return the created Calendar object.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 23900004 - Internal program errors. Possible causes:
         *     <br>1. dataShare database execution error;
         *	   <br>2. null pointer error;
         *     <br>3. Data parsing error. [since 23]
         * @syscap SystemCapability.Applications.CalendarData
         * @since 10
         */
        createCalendar(calendarAccount: CalendarAccount, callback: AsyncCallback<Calendar>): void;
        /**
         * Deletes a specified Calendar object. This API uses a promise to return the result.
         *
         * @permission ohos.permission.WRITE_CALENDAR or ohos.permission.WRITE_WHOLE_CALENDAR
         * @param { Calendar } calendar - Calendar object to delete. The default account cannot be deleted.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 23900004 - Internal program errors. Possible causes:
         *     <br>1. dataShare database execution error;
         *	   <br>2. null pointer error;
         *     <br>3. Data parsing error. [since 23]
         * @syscap SystemCapability.Applications.CalendarData
         * @since 10
         */
        deleteCalendar(calendar: Calendar): Promise<void>;
        /**
         * Deletes a specified Calendar object. This API uses an asynchronous callback to return the result.
         *
         * @permission ohos.permission.WRITE_CALENDAR or ohos.permission.WRITE_WHOLE_CALENDAR
         * @param { Calendar } calendar - Calendar object to delete. The default account cannot be deleted.
         * @param { AsyncCallback<void> } callback - Asynchronous callback that returns no value.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 23900004 - Internal program errors. Possible causes:
         *     <br>1. dataShare database execution error;
         *	   <br>2. null pointer error;
         *     <br>3. Data parsing error. [since 23]
         * @syscap SystemCapability.Applications.CalendarData
         * @since 10
         */
        deleteCalendar(calendar: Calendar, callback: AsyncCallback<void>): void;
        /**
         * Obtains the default or specified Calendar object. This API uses a promise to return the result.
         *
         * @permission ohos.permission.READ_CALENDAR or ohos.permission.READ_WHOLE_CALENDAR
         * @param { CalendarAccount } [calendarAccount] - Calendar account information, which is used to obtain
         * a specified Calendar object. If this parameter is not set, the default Calendar object is obtained.
         * @returns { Promise<Calendar> } the promise returned by the function.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 23900003 - The specified account was not found. [since 23]
         * @throws { BusinessError } 23900004 - Internal program errors. Possible causes:
         *     <br>1. dataShare database execution error;
         *	   <br>2. null pointer error;
         *     <br>3. Data parsing error. [since 23]
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        getCalendar(calendarAccount?: CalendarAccount): Promise<Calendar>;
        /**
         * Obtains a specified Calendar object. This API uses an asynchronous callback to return the result.
         *
         * @permission ohos.permission.READ_CALENDAR or ohos.permission.READ_WHOLE_CALENDAR
         * @param { CalendarAccount } calendarAccount - Calendar account information.
         * @param { AsyncCallback<Calendar> } callback - Callback used to return the obtained Calendar object.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 23900003 - The specified account was not found. [since 23]
         * @throws { BusinessError } 23900004 - Internal program errors. Possible causes:
         *     <br>1. dataShare database execution error;
         *	   <br>2. null pointer error;
         *     <br>3. Data parsing error. [since 23]
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        getCalendar(calendarAccount: CalendarAccount, callback: AsyncCallback<Calendar>): void;
        /**
         * Obtains the default Calendar object, which is created when the data storage runs for the first time.
         * This API uses an asynchronous callback to return the result.
         * You can call this API instead of createCalendar() to use the default calendar for a new event.
         *
         * @permission ohos.permission.READ_CALENDAR or ohos.permission.READ_WHOLE_CALENDAR
         * @param { AsyncCallback<Calendar> } callback - Callback used to return the obtained Calendar object.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 23900004 - Internal program errors. Possible causes:
         *     <br>1. dataShare database execution error;
         *	   <br>2. null pointer error;
         *     <br>3. Data parsing error. [since 23]
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        getCalendar(callback: AsyncCallback<Calendar>): void;
        /**
         * Obtains the created and default Calendar objects of the current application.
         * This API uses a promise to return the result.
         *
         * @permission ohos.permission.READ_CALENDAR or ohos.permission.READ_WHOLE_CALENDAR
         * @returns { Promise<Calendar[]> } Promise used to return an array of obtained Calendar objects.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 23900004 - Internal program errors. Possible causes:
         *     <br>1. dataShare database execution error;
         *	   <br>2. null pointer error;
         *     <br>3. Data parsing error. [since 23]
         * @syscap SystemCapability.Applications.CalendarData
         * @since 10
         */
        getAllCalendars(): Promise<Calendar[]>;
        /**
         * Obtains the created and default Calendar objects of the current application.
         * This API uses an asynchronous callback to return the result.
         *
         * @permission ohos.permission.READ_CALENDAR or ohos.permission.READ_WHOLE_CALENDAR
         * @param {AsyncCallback<Calendar[]>} callback - Callback used to return an array of the obtained Calendar objects.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 23900004 - Internal program errors. Possible causes:
         *     <br>1. dataShare database execution error;
         *	   <br>2. null pointer error;
         *     <br>3. Data parsing error. [since 23]
         * @syscap SystemCapability.Applications.CalendarData
         * @since 10
         */
        getAllCalendars(callback: AsyncCallback<Calendar[]>): void;
        /**
         * Edits an event on the event creation page, with no event ID specified in **Event**. The **instanceStartTime**, **instanceEndTime**,
         * **identifier**, **attendee**, **service**, **isLunar**, and **timeZone** attributes cannot be set. Important events cannot be added either.
         * This API uses a promise to return the result.
         *
         * Events created using this API can be obtained and modified by the system calendar.
         * Third-party applications can obtain and modify the events after they requested the **READ_WHOLE_CALENDAR**
         * permission and the **WRITE_WHOLE_CALENDAR** permission, respectively.
         *
         * @param { Event } event - **Event** object.
         * @returns { Promise<number> } Promise used to return the event ID. The event ID is the unique identifier of an
         *     event and is the auto-increment primary key of the database. If the event creation fails, no value is
         *     returned; if the value is less than **0**, the event creation is canceled; if the value is greater than **0**
         *     , the event creation is successful. The return value cannot be **0**
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice
         * @since 12
         */
        editEvent(event: Event): Promise<number>;
    }
    /**
     * In the following API examples, you need to use
     * [createCalendar()]{@link calendarManager.CalendarManager.createCalendar(calendarAccount: CalendarAccount,
     * callback: AsyncCallback<Calendar>)} or [getCalendar()]{@link calendarManager.CalendarManager.getCalendar
     * (callback: AsyncCallback<Calendar>)} to obtain
     *
     * a **Calendar** object before calling related APIs.
     *
     * @syscap SystemCapability.Applications.CalendarData
     * @atomicservice [since 11]
     * @since 10
     */
    export interface Calendar {
        /**
         * Calendar account ID, which is the unique identifier of a calendar account and is the auto-increment primary
         * key of the database. If the value is less than 0, the account creation fails;
         * if the value is greater than 0, the account creation succeeds.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        readonly id: number;
        /**
         * Adds an event, with no event ID, instanceStartTime, and instanceEndTime specified in Event.
         * This API uses a promise to return the result.
         *
         * @permission ohos.permission.WRITE_CALENDAR or ohos.permission.WRITE_WHOLE_CALENDAR [since 23]
         * @param { Event } event - Event object.
         * @returns { Promise<number> } Promise used to return the event ID. The ID is greater than 0.
         * @throws { BusinessError } 201 - Permission denied. [since 23]
         * @throws { BusinessError } 23900004 - Internal program errors. Possible causes:
         *     <br>1. dataShare database execution error;
         *	   <br>2. null pointer error;
         *     <br>3. Data parsing error. [since 23]
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        addEvent(event: Event): Promise<number>;
        /**
         * Adds an event, with no event ID, instanceStartTime, and instanceEndTime specified in Event.
         * This API uses an asynchronous callback to return the result.
         *
         * @permission ohos.permission.WRITE_CALENDAR or ohos.permission.WRITE_WHOLE_CALENDAR [since 23]
         * @param { Event } event - Event object.
         * @param { AsyncCallback<number> } callback - Callback used to return the event ID. The event ID is the unique
         * identifier of an event and is the auto-increment primary key of the database. If the value is less than 0,
         * the event creation fails; if the value is greater than 0, the event creation succeeds.
         * @throws { BusinessError } 201 - Permission denied. [since 23]
         * @throws { BusinessError } 23900004 - Internal program errors. Possible causes:
         *     <br>1. dataShare database execution error;
         *	   <br>2. null pointer error;
         *     <br>3. Data parsing error. [since 23]
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        addEvent(event: Event, callback: AsyncCallback<number>): void;
        /**
         * Adds events in batches, with no event ID, instanceStartTime, and instanceEndTime specified in Event.
         * This API uses a promise to return the result.
         *
         * @permission ohos.permission.WRITE_CALENDAR or ohos.permission.WRITE_WHOLE_CALENDAR [since 23]
         * @param { Event[] } events - Array of Event objects.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 201 - Permission denied. [since 23]
         * @throws { BusinessError } 23900004 - Internal program errors. Possible causes:
         *     <br>1. dataShare database execution error;
         *	   <br>2. null pointer error;
         *     <br>3. Data parsing error. [since 23]
         * @syscap SystemCapability.Applications.CalendarData
         * @since 10
         */
        addEvents(events: Event[]): Promise<void>;
        /**
         * Adds events in batches, with no event ID, instanceStartTime, and instanceEndTime specified in Event.
         * This API uses an asynchronous callback to return the result.
         *
         * @permission ohos.permission.WRITE_CALENDAR or ohos.permission.WRITE_WHOLE_CALENDAR [since 23]
         * @param { Event[] } events - Array of Event objects.
         * @param { AsyncCallback<void> } callback - Callback used to return the result.
         * @throws { BusinessError } 201 - Permission denied. [since 23]
         * @throws { BusinessError } 23900004 - Internal program errors. Possible causes:
         *     <br>1. dataShare database execution error;
         *	   <br>2. null pointer error;
         *     <br>3. Data parsing error. [since 23]
         * @syscap SystemCapability.Applications.CalendarData
         * @since 10
         */
        addEvents(events: Event[], callback: AsyncCallback<void>): void;
        /**
         * Deletes an event with the specified ID. This API uses a promise to return the result.
         *
         * @param { number } id - Event ID.
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Applications.CalendarData
         * @since 10
         */
        deleteEvent(id: number): Promise<void>;
        /**
         * Deletes an event with the specified ID. This API uses an asynchronous callback to return the result.
         *
         * @param { number } id - Event ID, which is the unique identifier of an event. If the input event ID is an integer,
         * the event is created.
         * @param {AsyncCallback<void>} callback - Callback used to return the result.
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 21]
         * @since 10
         */
        deleteEvent(id: number, callback: AsyncCallback<void>): void;
        /**
         * Deletes a batch of events with the specified IDs. This API uses a promise to return the result.
         *
         * @param { number[] } ids - Array of event IDs.
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Applications.CalendarData
         * @since 10
         */
        deleteEvents(ids: number[]): Promise<void>;
        /**
         * Deletes a batch of events with the specified IDs. This API uses an asynchronous callback to return the result.
         *
         * @param { number[] } ids - Array of event IDs.
         * @param {AsyncCallback<void>} callback - Callback used to return the result.
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 21]
         * @since 10
         */
        deleteEvents(ids: number[], callback: AsyncCallback<void>): void;
        /**
         * Updates an event. This API uses a promise to return the result.
         *
         * @param { Event } event - Event object.
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Applications.CalendarData
         * @since 10
         */
        updateEvent(event: Event): Promise<void>;
        /**
         * Updates an event. This API uses an asynchronous callback to return the result.
         *
         * @param { Event } event - Event object.
         * @param { AsyncCallback<void> } callback - The callback of updateEvent.
         * @syscap SystemCapability.Applications.CalendarData
         * @since 10
         */
        updateEvent(event: Event, callback: AsyncCallback<void>): void;
        /**
         * Obtains all events in a calendar that match the filter criteria. This API uses a promise to return the result.
         * If there is only one input parameter, the filter criteria, corresponding to the type EventFilter, must be set as the parameter.
         * If no input parameter is specified, all events under the specified calendar account can be queried.
         *
         * @permission ohos.permission.READ_CALENDAR or ohos.permission.READ_WHOLE_CALENDAR [since 23]
         * @param { EventFilter } [eventFilter] - Filter criteria.
         * @param { (keyof Event)[] } [eventKey] - Filter field. For versions earlier than API version 20, the default
         * fields to be obtained include id, type, title, startTime, endTime, isAllDay, description, timeZone, location,
         * service, attendee, and reminderTime if this parameter is left empty. Since API version 20, the default fields
         * to be obtained include id, type, title, startTime, endTime, isAllDay, description, timeZone, location, service,
         * attendee, reminderTime, and identifier if this parameter is left empty. The field is not returned if it is empty.
         * @returns { Promise<Event[]> } Promise used to return the result, which is an array of Event objects.
         * @throws { BusinessError } 201 - Permission denied. [since 23]
         * @throws { BusinessError } 23900004 - Internal program errors. Possible causes:
         *     <br>1. dataShare database execution error;
         *	   <br>2. null pointer error;
         *     <br>3. Data parsing error. [since 23]
         * @syscap SystemCapability.Applications.CalendarData
         * @since 10
         */
        getEvents(eventFilter?: EventFilter, eventKey?: (keyof Event)[]): Promise<Event[]>;
        /**
         * Obtains all events in a calendar that match the filter criteria. This API uses an asynchronous
         * callback to return the result.
         *
         * @permission ohos.permission.READ_CALENDAR or ohos.permission.READ_WHOLE_CALENDAR [since 23]
         * @param { EventFilter } eventFilter - Filter criteria.
         * @param { (keyof Event)[] } eventKey - Filter field.
         * @param { AsyncCallback<Event[]> } callback - Callback used to return an array of events.
         * @throws { BusinessError } 201 - Permission denied. [since 23]
         * @throws { BusinessError } 23900004 - Internal program errors. Possible causes:
         *     <br>1. dataShare database execution error;
         *	   <br>2. null pointer error;
         *     <br>3. Data parsing error. [since 23]
         * @syscap SystemCapability.Applications.CalendarData
         * @since 10
         */
        getEvents(eventFilter: EventFilter, eventKey: (keyof Event)[], callback: AsyncCallback<Event[]>): void;
        /**
         * Obtains all events in the current calendar. This API uses an asynchronous callback to return the result.
         *
         * For versions earlier than API version 20, the default fields to be obtained include id, type, title, startTime,
         * endTime, isAllDay, description, timeZone, location, service, attendee, and reminderTime. Since API version 20,
         * the default fields to be obtained include id, type, title, startTime, endTime, isAllDay, description, timeZone,
         * location, service, attendee, reminderTime, and identifier. The field is not returned if it is empty.
         *
         * @permission ohos.permission.READ_CALENDAR or ohos.permission.READ_WHOLE_CALENDAR [since 23]
         * @param { AsyncCallback<Event[]> } callback - Callback used to return an array of events.
         * @throws { BusinessError } 201 - Permission denied. [since 23]
         * @throws { BusinessError } 23900004 - Internal program errors. Possible causes:
         *     <br>1. dataShare database execution error;
         *	   <br>2. null pointer error;
         *     <br>3. Data parsing error. [since 23]
         * @syscap SystemCapability.Applications.CalendarData
         * @since 10
         */
        getEvents(callback: AsyncCallback<Event[]>): void;
        /**
         * Obtains the calendar configuration information.
         *
         * @returns { CalendarConfig } Calendar configuration information.
         * @syscap SystemCapability.Applications.CalendarData
         * @since 10
         */
        getConfig(): CalendarConfig;
        /**
         * Sets the calendar configuration information. This API uses a promise to return the result.
         *
         * @param { CalendarConfig } config - Calendar configuration information.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 23900001 – Parameter value error. [since 23]
         * @syscap SystemCapability.Applications.CalendarData
         * @since 10
         */
        setConfig(config: CalendarConfig): Promise<void>;
        /**
         * Sets the calendar configuration information. This API uses an asynchronous callback to return the result.
         *
         * @param { CalendarConfig } config - Calendar configuration information.
         * @param { AsyncCallback<void> } callback - Callback used to return the result.
         * @throws { BusinessError } 23900001 – Parameter value error. [since 23]
         * @syscap SystemCapability.Applications.CalendarData
         * @since 10
         */
        setConfig(config: CalendarConfig, callback: AsyncCallback<void>): void;
        /**
         * Obtains the calendar account information.
         *
         * @returns { CalendarAccount } Calendar account information.
         * @syscap SystemCapability.Applications.CalendarData
         * @since 10
         */
        getAccount(): CalendarAccount;
        /**
         * Queries the event instance with a specified event key in a calendar. This API uses a promise to return the result.
         *
         * @permission ohos.permission.READ_CALENDAR or ohos.permission.READ_WHOLE_CALENDAR [since 23]
         * @param { number } start - Start time of an event. The value is a 13-digit timestamp.
         * @param { number } end - End time of an event. The value is a 13-digit timestamp.
         * @param { number[] } [ids] - Array of event IDs to be queried, which can be empty or undefined.
         * @param { (keyof Event)[] } [eventKey] - Event key for querying events. If this parameter is left empty, the
         * default fields for filtering are id, title, startTime, endTime, instanceStartTime, instanceEndTime,
         * isAllDay, description, timeZone, location, and service. The field is not returned if it is empty.
         * @returns { Promise<Event[]> } Promise used to return the result, which is an array of Event objects.
         * @throws { BusinessError } 201 - Permission denied. [since 23]
         * @throws { BusinessError } 23900004 - Internal program errors. Possible causes:
         *     <br>1. dataShare database execution error;
         *	   <br>2. null pointer error;
         *     <br>3. Data parsing error. [since 23]
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice
         * @since 18
         */
        queryEventInstances(start: number, end: number, ids?: number[], eventKey?: (keyof Event)[]): Promise<Event[]>;
        /**
         * Opens the event edit page.
         * @param { number } id - The ID of the event to be edited.
         * @returns { Promise<void> } the promise returned by the function.
         * @throws { BusinessError } 23900001 - Parameter value error.
         * @throws { BusinessError } 23900005 - This event cannot be edited.
         * @syscap SystemCapability.Applications.CalendarData
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        openEventEditPage(id: number): Promise<void>;
    }
    /**
     * Describes the calendar account information.
     *
     * @syscap SystemCapability.Applications.CalendarData
     * @atomicservice [since 11]
     * @since 10
     */
    interface CalendarAccount {
        /**
         * Account name (defined by developers), with a maximum of 5,000 characters.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        readonly name: string;
        /**
         * Account type.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        type: CalendarType;
        /**
         * Account name displayed on the calendar application (defined by users). If this parameter is not specified, the
         * default value is an empty string with a maximum of 64 characters.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        displayName?: string;
    }
    /**
     * Describes the calendar configuration information.
     *
     * @syscap SystemCapability.Applications.CalendarData
     * @since 10
     */
    interface CalendarConfig {
        /**
         * Whether the calendar provides a reminder
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @since 10
         */
        enableReminder?: boolean;
        /**
         * Color of the calendar
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @since 10
         */
        color?: number | string;
    }
    /**
      * Describes an **Event** object, including the event title, start time, and end time.
      *
      * @syscap SystemCapability.Applications.CalendarData
      * @atomicservice [since 11]
      * @since 10
      */
    interface Event {
        /**
         * Event ID. When you call
         * [addEvent()]{@link calendarManager.Calendar.addEvent(event: Event, callback: AsyncCallback<number>)} or
         * [addEvents()]{@link calendarManager.Calendar.addEvents(events: Event[], callback: AsyncCallback<void>)} to create
         * an event, this parameter is not required. When you call
         * [deleteEvent()]{@link calendarManager.Calendar.deleteEvent(id: number, callback: AsyncCallback<void>)} or
         * [deleteEvents()]{@link calendarManager.Calendar.deleteEvents(ids: number[], callback: AsyncCallback<void>)} to
         * delete an event, this parameter is required and must be set to an array of integers. If this parameter is set to
         * an invalid value, an error will be reported.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        id?: number;
        /**
         * Event type.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        type: EventType;
        /**
         * Event title, with a maximum of 5,000 characters. If this parameter is not specified, the default value is an
         * empty string.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        title?: string;
        /**
         * Event location. If this parameter is not set, the default null value is used.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        location?: Location;
        /**
         * Start time of an event. The value is a 13-digit timestamp. For an all-day event, this field is converted to the
         * timestamp corresponding to 00:00 of the specified date.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        startTime: number;
        /**
         * End time of an event. The value is a 13-digit timestamp. For an all-day event, this field is converted to the
         * timestamp corresponding to 24:00 of the specified date.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        endTime: number;
        /**
         * Whether the event is an all-day event. The value **true** means that the event is an all-day event, and **false**
         * means the opposite. The default value is **false**.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        isAllDay?: boolean;
        /**
         * Attendees in a meeting. If this parameter is not set, the default null value is used.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        attendee?: Attendee[];
        /**
         * Time zone of the event, with a maximum of 5,000 characters. If this parameter is not specified or set to an
         * invalid value, the current time zone is used by default. If a different time zone is required, enter the
         * corresponding time zone. You can call
         * [systemDateTime.getTimezone()]{@link @ohos.systemDateTime:systemDateTime.getTimezone(callback: AsyncCallback<string>)}
         * to obtain the current system time zone.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        timeZone?: string;
        /**
         * Reminder time of the event, in minutes. For example, if the value is 5, the reminder occurs 5 minutes before the
         * event starts. If this parameter is not set, no reminder is set. A negative value indicates the delay time for
         * sending a notification. For an all-day event, this parameter specifies the time offset in minutes before 9 a.m.
         * on the event date. A negative value indicates the number of minutes after 9 a.m.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        reminderTime?: number[];
        /**
         * Recurrence rule of an event. The event is a recurring event if this parameter is set; otherwise, the event is a
         * non-recurring event.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        recurrenceRule?: RecurrenceRule;
        /**
         * Event description, with a maximum of 5,000 characters. If this parameter is not specified, the default value is
         * an empty string.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        description?: string;
        /**
         * <!--RP1-->Event service. If this parameter is not set, no one-click service is available. This function is not supported currently.<!--RP1End-->
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        service?: EventService;
        /**
         * Unique ID of an event, with a maximum of 5,000 characters. If this parameter is not specified, the default value is null.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice
         * @since 12
         */
        identifier?: string;
        /**
         * Whether it is a lunar calendar event. The value true means that the event is a lunar calendar event, and false means the opposite.
         * The default value is false.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice
         * @since 12
         */
        isLunar?: boolean;
        /**
         * Start time of an event. The value is a 13-digit timestamp. This parameter does not need to be set in
         * [addEvent()]{@link calendarManager.Calendar.addEvent(event: Event, callback: AsyncCallback<number>)}
         * or [addEvents()]{@link calendarManager.Calendar.addEvents(events: Event[], callback: AsyncCallback<void>)}.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice
         * @since 18
         */
        instanceStartTime?: number;
        /**
         * End time of an event. The value is a 13-digit timestamp. This parameter does not need to be set in
         * [addEvent()]{@link calendarManager.Calendar.addEvent(event: Event, callback: AsyncCallback<number>)}
         * or [addEvents()]{@link calendarManager.Calendar.addEvents(events: Event[], callback: AsyncCallback<void>)}.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice
         * @since 18
         */
        instanceEndTime?: number;
    }
    /**
     * Enumerates the account types.
     *
     * @syscap SystemCapability.Applications.CalendarData
     * @atomicservice [since 11]
     * @since 10
     */
    enum CalendarType {
        /**
         * Local account.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        LOCAL = 'local',
        /**
         * Email account.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        EMAIL = 'email',
        /**
         * Birthday account.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        BIRTHDAY = 'birthday',
        /**
         * CalDAV account.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        CALDAV = 'caldav',
        /**
         * Subscription account.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        SUBSCRIBED = 'subscribed'
    }
    /**
     * Describes the event location.
     *
     * @syscap SystemCapability.Applications.CalendarData
     * @atomicservice [since 11]
     * @since 10
     */
    interface Location {
        /**
         * Location, with a maximum of 5,000 characters. If this parameter is not specified, the default value is an empty string.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        location?: string;
        /**
         * Longitude of the location. The value range is [-180, 180]. The default value is **undefined**. If the value is
         * out of the range, the map cannot be displayed properly.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        longitude?: number;
        /**
         * Latitude of the location. The value range is [-90, 90]. The default value is **undefined**. If the value is out
         * of the range, the map cannot be displayed properly.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        latitude?: number;
    }
    /**
     * Implements an event filter.
     *
     * You can use [filterById()]{@link calendarManager.EventFilter.filterById},
     * [filterByTime()]{@link calendarManager.EventFilter.filterByTime},
     * [filterByTitle()]{@link calendarManager.EventFilter.filterByTitle} to
     * obtain an event filter, and then pass the filter in getEvents() for filtering.
     *
     * @syscap SystemCapability.Applications.CalendarData
     * @since 10
     */
    class EventFilter {
        /**
         * Defines a filter based on the event ID.
         *
         * @param {number[]} An array of event IDs, where each event ID must be an integer.
         * @returns { EventFilter } EventFilter object.
         * @syscap SystemCapability.Applications.CalendarData
         * @since 10
         */
        static filterById(ids: number[]): EventFilter;
        /**
         * Defines a filter based on the event time.
         *
         * @param { number } start - Start time. The value is a 13-digit timestamp.
         * @param { number } end - End time. The value is a 13-digit timestamp.
         * @returns { EventFilter } EventFilter object.
         * @syscap SystemCapability.Applications.CalendarData
         * @since 10
         */
        static filterByTime(start: number, end: number): EventFilter;
        /**
         * Filters events by event title. This API supports fuzzy match.
         *
         * @param { string } title - Event title, with a maximum of 5,000 characters.
         * @returns {EventFilter } EventFilter object.
         * @syscap SystemCapability.Applications.CalendarData
         * @since 10
         */
        static filterByTitle(title: string): EventFilter;
    }
    /**
     * Enumerates event types.
     *
     * @syscap SystemCapability.Applications.CalendarData
     * @atomicservice [since 11]
     * @since 10
     */
    enum EventType {
        /**
         * Normal event, such as conference or an alarm clock.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        NORMAL = 0,
        /**
         * Important event, such as wedding anniversary, are not recommended for third-party developers. Important events do
         * not support one-click service redirection and custom reminder time.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        IMPORTANT = 1
    }
    /**
     * Describes the recurrence rule of a recurring event.
     *
     * @syscap SystemCapability.Applications.CalendarData
     * @atomicservice [since 11]
     * @since 10
     */
    export interface RecurrenceRule {
        /**
         * Type of the event recurrence rule.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        recurrenceFrequency: RecurrenceFrequency;
        /**
         * End date of the recurrence period. The value is a 13-digit timestamp. If this parameter is not specified, the
         * event has no end date.
         *
         * If **expire**, **count**, and **interval** are set at the same time, the restriction that is reached first
         * prevails.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        expire?: number;
        /**
         * Number of times that an event recurs. The value is a non-negative integer. If the value is a floating point number,
         * it is rounded down. If this parameter is left empty, the default value is 0, indicating that the number of recurrence
         * times is not limited and the event will continuously recur. If the value is negative, the effect is the same as that of 0.
         * If count, interval, and expire are set at the same time, the restriction that is reached first prevails.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice
         * @since 12
         */
        count?: number;
        /**
         * Recurrence interval of a recurring event. The value is a non-negative integer. If the value is a floating point number, it is rounded down.
         * If this parameter is not specified, the default value is 0. If the value is 0, 1, or negative, the event recurs every day, week, month, or year.
         * If interval, count, and expire are set at the same time, the restriction that is reached first prevails.
         * This property is related to the recurrenceFrequency rule. The recurrence interval varies according to the
         * recurrence rule. For example, if the interval value is 2, the following situations occur:
         * Daily recurrence: The event recurs every two days. Weekly recurrence: The event recurs every two weeks.
         * Monthly recurrence: The event recurs every two months. Yearly recurrence: The event recurs every two years.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice
         * @since 12
         */
        interval?: number;
        /**
         * Excluded dates set for a duplicate calendar event, in timestamp format. The value must be exactly the same as the start time (hour, minute, and second) of the event.
         * Otherwise, the setting does not take effect. This parameter is not specified by default. If the value is 0 or a negative number, it is treated as an empty value.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice
         * @since 12
         */
        excludedDates?: number[];
        /**
         * Repeats by day of a week. If this parameter is not set, the default value is empty, indicating that there is no recurrence rule.
         * The value range is [1, 7], corresponding to Monday to Sunday. Other values are invalid and have the same effect as the empty value.
         * The relevant field arrays are in one-to-one mapping. For example, if the values of weeksOfMonth and daysOfWeek are [1, 2, 3],
         * the event recurs on Monday of the first week, Tuesday of the second week, and Wednesday of the third week of each month.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice
         * @since 12
         */
        daysOfWeek?: number[];
        /**
         * Repeats by day of a month. If this parameter is not set, the default value is empty, indicating that there is no
         * recurrence rule. The value range is [1, 31], corresponding to the first to the last days of each month.
         * Other values are invalid and have the same effect as the empty value. The value 29, 30, or 31 is invalid if the
         * corresponding date does not exist in the current month. The relevant field arrays are in one-to-one mapping.
         * For example, if the values of monthsOfYear and daysOfMonth are [1, 2, 3], the event recurs on January 1,
         * February 2, and March 3.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice
         * @since 12
         */
        daysOfMonth?: number[];
        /**
         * Repeats by day of a year. If this parameter is not set, the default value is empty, indicating that there is no
         * recurrence rule. The value range is [1, 366], corresponding to the first to the last days of each year. Other
         * values are invalid and have the same effect as the empty value. If this year only has 365 days, the value 366 is invalid.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice
         * @since 12
         */
        daysOfYear?: number[];
        /**
         * Repeats by week of a month. If this parameter is not set, the default value is empty, indicating that there is no recurrence rule.
         * The value range is [1, 5], corresponding to the first to the last weeks of each month. Other values are invalid and have the same effect as the empty value.
         * If this month only has four weeks, the value 5 is invalid.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice
         * @since 12
         */
        weeksOfMonth?: number[];
        /**
         * Repeats by week of a year. If this parameter is not set, the default value is empty, indicating that there is no recurrence rule. The value range is [1, 53],
         * corresponding to the first to the last weeks of each year. Other values are invalid and have the same effect as the empty value.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice
         * @since 12
         */
        weeksOfYear?: number[];
        /**
         * Repeats by month of a year. If this parameter is not set, the default value is empty, indicating that there is no recurrence rule. The value range is [1, 12],
         * corresponding to the first to the last months of each year. Other values are invalid and have the same effect as the empty value.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice
         * @since 12
         */
        monthsOfYear?: number[];
    }
    /**
     * Enumerates the types of the event recurrence rule.
     *
     * @syscap SystemCapability.Applications.CalendarData
     * @atomicservice [since 11]
     * @since 10
     */
    export enum RecurrenceFrequency {
        /**
         * Yearly.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        YEARLY = 0,
        /**
         * Monthly.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        MONTHLY = 1,
        /**
         * Weekly.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        WEEKLY = 2,
        /**
         * Daily.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        DAILY = 3
    }
    /**
     * Describes the attendees in a meeting.
     *
     * @syscap SystemCapability.Applications.CalendarData
     * @atomicservice [since 11]
     * @since 10
     */
    export interface Attendee {
        /**
         * Name of the attendee, with a maximum of 5,000 characters.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        name: string;
        /**
         * Email address of the attendee, with a maximum of 5,000 characters.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        email: string;
        /**
         * Role of the Attendee.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice
         * @since 12
         */
        role?: AttendeeRole;
        /**
         * Type of the attendee. If this parameter is not set, the default value is empty.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice
         * @since 18
         */
        type?: AttendeeType;
        /**
         * Status of the attendee. If this parameter is not set, the default value is empty.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice
         * @since 18
         */
        status?: AttendeeStatus;
    }
    /**
     * Enumerates the attendee role types in a conference event.
     *
     * @syscap SystemCapability.Applications.CalendarData
     * @atomicservice
     * @since 12
     */
    export enum AttendeeRole {
        /**
         * Conference organizer.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice
         * @since 12
         */
        ORGANIZER = 'organizer',
        /**
         * Conference participant.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice
         * @since 12
         */
        PARTICIPANT = 'participant'
    }
    /**
     * Enumerates the types of attendees invited to a conference event.
     *
     * @syscap SystemCapability.Applications.CalendarData
     * @atomicservice
     * @since 18
     */
    export enum AttendeeType {
        /**
         * Required attendee.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice
         * @since 18
         */
        REQUIRED = 1,
        /**
         * Optional attendee.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice
         * @since 18
         */
        OPTIONAL = 2,
        /**
         * Resources (such as TVs or projectors) used in a conference.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice
         * @since 18
         */
        RESOURCE = 3
    }
    /**
     * Enumerates the status types of an attendee.
     *
     * @syscap SystemCapability.Applications.CalendarData
     * @atomicservice
     * @since 18
     */
    export enum AttendeeStatus {
        /**
         * The attendee status is unknown.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice
         * @since 18
         */
        UNKNOWN = 0,
        /**
         * The attendee status is tentative.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice
         * @since 18
         */
        TENTATIVE = 1,
        /**
         * The attendee has accepted the conference invitation.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice
         * @since 18
         */
        ACCEPTED = 2,
        /**
         * The attendee has rejected the conference invitation.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice
         * @since 18
         */
        DECLINED = 3,
        /**
         * The attendee does not respond.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice
         * @since 18
         */
        UNRESPONSIVE = 4
    }
    /**
     * Describes the event service.
     *
     * @syscap SystemCapability.Applications.CalendarData
     * @atomicservice [since 11]
     * @since 10
     */
    export interface EventService {
        /**
         * Service type.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        type: ServiceType;
        /**
         * Service URI, in the DeepLink format. The URI can then redirect the user to the corresponding third-party
         * application page. The value is a string with a maximum of 5,000 characters.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        uri: string;
        /**
         * Description of the service, with a maximum of 5,000 characters. If this parameter is not specified, the default
         * value is an empty string.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        description?: string;
    }
    /**
     * Enumerates the event service types.
     *
     * @syscap SystemCapability.Applications.CalendarData
     * @atomicservice [since 11]
     * @since 10
     */
    export enum ServiceType {
        /**
         * Join a meeting.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        MEETING = 'Meeting',
        /**
         * Watch a video.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        WATCHING = 'Watching',
        /**
         * Make a payment.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        REPAYMENT = 'Repayment',
        /**
         * Watch live TV.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        LIVE = 'Live',
        /**
         * Go shopping.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        SHOPPING = 'Shopping',
        /**
         * View the trip.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        TRIP = 'Trip',
        /**
         * Join class.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        CLASS = 'Class',
        /**
         * Watch a sports event.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        SPORTS_EVENTS = 'SportsEvents',
        /**
         * Start exercising.
         *
         * @syscap SystemCapability.Applications.CalendarData
         * @atomicservice [since 11]
         * @since 10
         */
        SPORTS_EXERCISE = 'SportsExercise'
    }
}
export default calendarManager;

```
