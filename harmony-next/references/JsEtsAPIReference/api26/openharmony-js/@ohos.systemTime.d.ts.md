# @ohos.systemTime.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (C) 2021 Huawei Device Co., Ltd.
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
 * @file System Time and Time Zone
 * @kit BasicServicesKit
 */
import { AsyncCallback } from './@ohos.base';
/**
 * # Supported System Time Zones
 *
 * The following table lists the supported system time zones and the respective offset (unit: h) between each time zone
 * and time zone 0.
 *
 * | Time Zone                          | Offset        |
 * | ------------------------------ | --------------------- |
 * | Antarctica/McMurdo             | 12                    |
 * | America/Argentina/Buenos_Aires | -3                    |
 * | Australia/Sydney               | 10                    |
 * | America/Noronha                | -2                    |
 * | America/St_Johns               | -3                    |
 * | Africa/Kinshasa                | 1                     |
 * | America/Santiago               | -3                    |
 * | Asia/Shanghai                  | 8                     |
 * | Asia/Nicosia                   | 3                     |
 * | Europe/Berlin                  | 2                     |
 * | America/Guayaquil              | -5                    |
 * | Europe/Madrid                  | 2                     |
 * | Pacific/Pohnpei                | 11                    |
 * | America/Godthab                | -2                    |
 * | Asia/Jakarta                   | 7                     |
 * | Pacific/Tarawa                 | 12                    |
 * | Asia/Almaty                    | 6                     |
 * | Pacific/Majuro                 | 12                    |
 * | Asia/Ulaanbaatar               | 8                     |
 * | America/Mexico_City            | -5                    |
 * | Asia/Kuala_Lumpur              | 8                     |
 * | Pacific/Auckland               | 12                    |
 * | Pacific/Tahiti                 | -10                   |
 * | Pacific/Port_Moresby           | 10                    |
 * | Asia/Gaza                      | 3                     |
 * | Europe/Lisbon                  | 1                     |
 * | Europe/Moscow                  | 3                     |
 * | Europe/Kiev                    | 3                     |
 * | Pacific/Wake                   | 12                    |
 * | America/New_York               | -4                    |
 * | Asia/Tashkent                  | 5                     |
 */
/**
 * The **systemTime** module provides system time and time zone features. You can use the APIs of this module to set and
 * obtain the system time and time zone.
 *
 * @syscap SystemCapability.MiscServices.Time
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.systemDateTime:systemDateTime
 */
declare namespace systemTime {
    /**
     * Sets the system time. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.SET_TIME
     * @param { number } time - Timestamp to set, in milliseconds.
     * @param { AsyncCallback<void> } callback - Callback used to return the result.
     * @throws { BusinessError } -1 - Parameter check failed, permission denied, or system error.
     * @syscap SystemCapability.MiscServices.Time
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.systemDateTime:systemDateTime.setTime
     */
    function setTime(time: number, callback: AsyncCallback<void>): void;
    /**
     * Sets the system time. This API uses a promise to return the result.
     *
     * @permission ohos.permission.SET_TIME
     * @param { number } time - Timestamp to set, in milliseconds.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } -1 - Parameter check failed, permission denied, or system error.
     * @syscap SystemCapability.MiscServices.Time
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.systemDateTime:systemDateTime.setTime
     */
    function setTime(time: number): Promise<void>;
    /**
     * Obtains the time elapsed since the Unix epoch. This API uses an asynchronous callback to return the result.
     *
     * @param { boolean } isNano - Whether the time to return is in nanoseconds.<br>- **true**: The result is in
     *     nanoseconds.<br>- **false**: The result is in milliseconds.
     * @param { AsyncCallback<number> } callback - Callback used to return the time elapsed since the Unix epoch.
     * @throws { BusinessError } -1 - Parameter check failed, permission denied, or system error.
     * @syscap SystemCapability.MiscServices.Time
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.systemDateTime:systemDateTime.getTime
     */
    function getCurrentTime(isNano: boolean, callback: AsyncCallback<number>): void;
    /**
     * Obtains the time elapsed since the Unix epoch. This API uses an asynchronous callback to return the result.
     *
     * @param { AsyncCallback<number> } callback - Callback used to return the time elapsed since the Unix epoch, in
     *     milliseconds.
     * @throws { BusinessError } -1 - Parameter check failed, permission denied, or system error.
     * @syscap SystemCapability.MiscServices.Time
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.systemDateTime:systemDateTime.getTime
     */
    function getCurrentTime(callback: AsyncCallback<number>): void;
    /**
     * Obtains the time elapsed since the Unix epoch. This API uses a promise to return the result.
     *
     * @param { boolean } isNano - Whether the time to return is in nanoseconds. The default value is **false**.<br>The
     *     default value is false.<br>- **true**: The result is in nanoseconds.<br>- **false**: The result is in
     *     milliseconds.
     * @returns { Promise<number> } Promise used to return the time elapsed since the Unix epoch.
     * @throws { BusinessError } -1 - Parameter check failed, permission denied, or system error.
     * @syscap SystemCapability.MiscServices.Time
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.systemDateTime:systemDateTime.getTime
     */
    function getCurrentTime(isNano?: boolean): Promise<number>;
    /**
     * Obtains the time elapsed since system startup, excluding the deep sleep time. This API uses an asynchronous
     * callback to return the result.
     *
     * @param { boolean } isNano - Whether the time to return is in nanoseconds.<br>- **true**: The result is in
     *     nanoseconds.<br>- **false**: The result is in milliseconds.
     * @param { AsyncCallback<number> } callback - Callback used to return the result.
     * @throws { BusinessError } -1 - Parameter check failed, permission denied, or system error.
     * @syscap SystemCapability.MiscServices.Time
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.systemDateTime:systemDateTime.getUptime
     */
    function getRealActiveTime(isNano: boolean, callback: AsyncCallback<number>): void;
    /**
     * Obtains the time elapsed since system startup, excluding the deep sleep time. This API uses an asynchronous
     * callback to return the result.
     *
     * @param { AsyncCallback<number> } callback - Callback used to return the result.
     * @throws { BusinessError } -1 - Parameter check failed, permission denied, or system error.
     * @syscap SystemCapability.MiscServices.Time
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.systemDateTime:systemDateTime.getUptime
     */
    function getRealActiveTime(callback: AsyncCallback<number>): void;
    /**
     * Obtains the time elapsed since system startup, excluding the deep sleep time. This API uses a promise to return the
     * result.
     *
     * @param { boolean } isNano - Whether the time to return is in nanoseconds. The default value is **false**.<br>-
     *     **true**: The result is in nanoseconds.<br>- **false**: The result is in milliseconds.
     * @returns { Promise<number> } Promise used to return the time elapsed since system startup, excluding the deep sleep
     *     time.
     * @throws { BusinessError } -1 - Parameter check failed, permission denied, or system error.
     * @syscap SystemCapability.MiscServices.Time
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.systemDateTime:systemDateTime.getUptime
     */
    function getRealActiveTime(isNano?: boolean): Promise<number>;
    /**
     * Obtains the time elapsed since system startup, including the deep sleep time. This API uses an asynchronous
     * callback to return the result.
     *
     * @param { boolean } isNano - Whether the time to return is in nanoseconds.<br>- **true**: The result is in
     *     nanoseconds.<br>- **false**: The result is in milliseconds.
     * @param { AsyncCallback<number> } callback - Callback used to return the result.
     * @throws { BusinessError } -1 - Parameter check failed, permission denied, or system error.
     * @syscap SystemCapability.MiscServices.Time
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.systemDateTime:systemDateTime.getUptime
     */
    function getRealTime(isNano: boolean, callback: AsyncCallback<number>): void;
    /**
     * Obtains the time elapsed since system startup, including the deep sleep time. This API uses an asynchronous
     * callback to return the result.
     *
     * @param { AsyncCallback<number> } callback - Callback used to return the result.
     * @throws { BusinessError } -1 - Parameter check failed, permission denied, or system error.
     * @syscap SystemCapability.MiscServices.Time
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.systemDateTime:systemDateTime.getUptime
     */
    function getRealTime(callback: AsyncCallback<number>): void;
    /**
     * Obtains the time elapsed since system startup, including the deep sleep time. This API uses a promise to return the
     * result.
     *
     * @param { boolean } isNano - Whether the time to return is in nanoseconds. The default value is **false**.<br>The
     *     default value is false.<br>- **true**: The result is in nanoseconds.<br>- **false**: The result is in
     *     milliseconds.
     * @returns { Promise<number> } Promise used to return the time elapsed since system startup, including the deep sleep
     *     time.
     * @throws { BusinessError } -1 - Parameter check failed, permission denied, or system error.
     * @syscap SystemCapability.MiscServices.Time
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.systemDateTime:systemDateTime.getUptime
     */
    function getRealTime(isNano?: boolean): Promise<number>;
    /**
     * Sets the system date. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.SET_TIME
     * @param { Date } date - Target date to set.
     * @param { AsyncCallback<void> } callback - Callback used to return the result.
     * @throws { BusinessError } -1 - Parameter check failed, permission denied, or system error.
     * @syscap SystemCapability.MiscServices.Time
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.systemDateTime:systemDateTime.setDate
     */
    function setDate(date: Date, callback: AsyncCallback<void>): void;
    /**
     * Sets the system date. This API uses a promise to return the result.
     *
     * @permission ohos.permission.SET_TIME
     * @param { Date } date - Target date to set.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } -1 - Parameter check failed, permission denied, or system error.
     * @syscap SystemCapability.MiscServices.Time
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.systemDateTime:systemDateTime.setDate
     */
    function setDate(date: Date): Promise<void>;
    /**
     * Obtains the current system date. This API uses an asynchronous callback to return the result.
     *
     * @param { AsyncCallback<Date> } callback - Callback used to return the current system date.
     * @throws { BusinessError } -1 - Parameter check failed, permission denied, or system error.
     * @syscap SystemCapability.MiscServices.Time
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.systemDateTime:systemDateTime.setDate
     */
    function getDate(callback: AsyncCallback<Date>): void;
    /**
     * Obtains the current system date. This API uses a promise to return the result.
     *
     * @returns { Promise<Date> } Promise used to return the current system date.
     * @throws { BusinessError } -1 - Parameter check failed, permission denied, or system error.
     * @syscap SystemCapability.MiscServices.Time
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.systemDateTime:systemDateTime.getDate
     */
    function getDate(): Promise<Date>;
    /**
     * Sets the system time zone. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.SET_TIME_ZONE
     * @param { string } timezone - System time zone to set. For details, see
     *     [Supported System Time Zones](docroot://reference/apis-basic-services-kit/js-apis-system-time.md#supported-system-time-zones)
     *     .
     * @param { AsyncCallback<void> } callback - Callback used to return the result.
     * @throws { BusinessError } -1 - Parameter check failed, permission denied, or system error.
     * @syscap SystemCapability.MiscServices.Time
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.systemDateTime:systemDateTime.setTimezone
     */
    function setTimezone(timezone: string, callback: AsyncCallback<void>): void;
    /**
     * Sets the system time zone. This API uses a promise to return the result.
     *
     * @permission ohos.permission.SET_TIME_ZONE
     * @param { string } timezone - System time zone to set. For details, see
     *     [Supported System Time Zones](docroot://reference/apis-basic-services-kit/js-apis-system-time.md#supported-system-time-zones)
     *     .
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } -1 - Parameter check failed, permission denied, or system error.
     * @syscap SystemCapability.MiscServices.Time
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.systemDateTime:systemDateTime.setTimezone
     */
    function setTimezone(timezone: string): Promise<void>;
    /**
     * Obtains the system time zone. This API uses an asynchronous callback to return the result.
     *
     * @param { AsyncCallback<string> } callback - Callback used to return the system time zone. For details, see
     *     [Supported System Time Zones](docroot://reference/apis-basic-services-kit/js-apis-system-time.md#supported-system-time-zones)
     *     .
     * @throws { BusinessError } -1 - Parameter check failed, permission denied, or system error.
     * @syscap SystemCapability.MiscServices.Time
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.systemDateTime:systemDateTime.getTimezone(callback: AsyncCallback<string>)
     */
    function getTimezone(callback: AsyncCallback<string>): void;
    /**
     * Obtains the system time zone. This API uses a promise to return the result.
     *
     * @returns { Promise<string> } Promise used to return the system time zone. For details, see
     *     [Supported System Time Zones](docroot://reference/apis-basic-services-kit/js-apis-system-time.md#supported-system-time-zones)
     *     .
     * @throws { BusinessError } -1 - Parameter check failed, permission denied, or system error.
     * @syscap SystemCapability.MiscServices.Time
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.systemDateTime:systemDateTime.getTimezone()
     */
    function getTimezone(): Promise<string>;
}
export default systemTime;

```
