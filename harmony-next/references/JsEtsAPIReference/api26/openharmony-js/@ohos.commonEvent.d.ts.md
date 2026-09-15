# @ohos.commonEvent.d.ts

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
 * @kit API10LessDeprecatedModules
 */
import { AsyncCallback } from './@ohos.base';
import { CommonEventData } from './commonEvent/commonEventData';
import { CommonEventSubscriber } from './commonEvent/commonEventSubscriber';
import { CommonEventSubscribeInfo } from './commonEvent/commonEventSubscribeInfo';
import { CommonEventPublishData } from './commonEvent/commonEventPublishData';
/**
 * The **CommonEvent** module provides capabilities to publish, subscribe to, and unsubscribe from common events, as
 * well as obtain and modify the common event result code and result data.
 *
 * @syscap SystemCapability.Notification.CommonEvent
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.commonEventManager:commonEventManager
 */
declare namespace commonEvent {
    /**
     * Publishes a common event with given properties. This API uses an asynchronous callback to return the result.
     *
     * @param { string } event - Name of the common event to publish.
     * @param { AsyncCallback<void> } callback - Callback used to return the result of publishing a common event.
     * @syscap SystemCapability.Notification.CommonEvent
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.commonEventManager:commonEventManager.publish(event: string, callback: AsyncCallback<void>)
     */
    function publish(event: string, callback: AsyncCallback<void>): void;
    /**
     * Publishes a common event with given properties. This API uses an asynchronous callback to return the result.
     *
     * @param { string } event - Name of the common event to publish.
     * @param { CommonEventPublishData } options - Properties of the common event to publish.
     * @param { AsyncCallback<void> } callback - Callback used to return the result of publishing a common event.
     * @syscap SystemCapability.Notification.CommonEvent
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.commonEventManager:commonEventManager.publish(event: string, options: CommonEventPublishData, callback: AsyncCallback<void>)
     */
    function publish(event: string, options: CommonEventPublishData, callback: AsyncCallback<void>): void;
    /**
     * Creates a subscriber. This API uses an asynchronous callback to return the result.
     *
     * @param { CommonEventSubscribeInfo } subscribeInfo - Subscriber information.
     * @param { AsyncCallback<CommonEventSubscriber> } callback - Callback used to return the result.
     * @syscap SystemCapability.Notification.CommonEvent
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.commonEventManager:commonEventManager.createSubscriber( subscribeInfo: CommonEventSubscribeInfo, callback: AsyncCallback<CommonEventSubscriber> )
     */
    function createSubscriber(subscribeInfo: CommonEventSubscribeInfo, callback: AsyncCallback<CommonEventSubscriber>): void;
    /**
     * Creates a subscriber. This API uses a promise to return the result.
     *
     * @param { CommonEventSubscribeInfo } subscribeInfo - Subscriber information.
     * @returns { Promise<CommonEventSubscriber> } Promise used to return the subscriber object.
     * @syscap SystemCapability.Notification.CommonEvent
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.commonEventManager:commonEventManager.createSubscriber(subscribeInfo: CommonEventSubscribeInfo)
     */
    function createSubscriber(subscribeInfo: CommonEventSubscribeInfo): Promise<CommonEventSubscriber>;
    /**
     * Subscribes to common events. This API uses an asynchronous callback to return the result.
     *
     * @param { CommonEventSubscriber } subscriber - Subscriber object.
     * @param { AsyncCallback<CommonEventData> } callback - Callback to be invoked when a common event is subscribed to.
     * @syscap SystemCapability.Notification.CommonEvent
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.commonEventManager:commonEventManager.subscribe
     */
    function subscribe(subscriber: CommonEventSubscriber, callback: AsyncCallback<CommonEventData>): void;
    /**
     * Unsubscribes from common events. This API uses an asynchronous callback to return the result.
     *
     * @param { CommonEventSubscriber } subscriber - Subscriber object.
     * @param { AsyncCallback<void> } [callback] - Callback used to return the result.
     * @syscap SystemCapability.Notification.CommonEvent
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.commonEventManager:commonEventManager.unsubscribe
     */
    function unsubscribe(subscriber: CommonEventSubscriber, callback?: AsyncCallback<void>): void;
    /**
     * A system common event is an event that is published by a system service or system application and requires specific
     * permissions to subscribe to. To publish or subscribe to this type of event, you must follow the event-specific
     * definitions.
     *
     * @syscap SystemCapability.Notification.CommonEvent
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.commonEventManager:commonEventManager.Support
     */
    export enum Support {
        /**
         * Indicates that the boot is complete and the system is loaded.
         *
         * To subscribe to this common event, your application must have the ohos.permission.RECEIVER_STARTUP_COMPLETED
         * permission. (This permission is available only for system applications.)
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_BOOT_COMPLETED
         */
        COMMON_EVENT_BOOT_COMPLETED = 'usual.event.BOOT_COMPLETED',
        /**
         * (reserved, not supported yet) Indicates that the guidance is complete and the system is loaded, but the screen is
         * still locked.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_LOCKED_BOOT_COMPLETED
         */
        COMMON_EVENT_LOCKED_BOOT_COMPLETED = 'usual.event.LOCKED_BOOT_COMPLETED',
        /**
         * Indicates that the device is being shut down and will continue until it is finally shut down.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_SHUTDOWN
         */
        COMMON_EVENT_SHUTDOWN = 'usual.event.SHUTDOWN',
        /**
         * Indicates that the battery charging status, battery level, and other information has changed.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_BATTERY_CHANGED
         */
        COMMON_EVENT_BATTERY_CHANGED = 'usual.event.BATTERY_CHANGED',
        /**
         * Indicates that the battery level is low.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_BATTERY_LOW
         */
        COMMON_EVENT_BATTERY_LOW = 'usual.event.BATTERY_LOW',
        /**
         * Indicates that the battery level is normal.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_BATTERY_OKAY
         */
        COMMON_EVENT_BATTERY_OKAY = 'usual.event.BATTERY_OKAY',
        /**
         * Indicates that the device is connected to an external power supply.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_POWER_CONNECTED
         */
        COMMON_EVENT_POWER_CONNECTED = 'usual.event.POWER_CONNECTED',
        /**
         * Indicates that the device is disconnected from the external power supply.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_POWER_DISCONNECTED
         */
        COMMON_EVENT_POWER_DISCONNECTED = 'usual.event.POWER_DISCONNECTED',
        /**
         * Indicates that the device screen is off and the device is in sleep mode.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_SCREEN_OFF
         */
        COMMON_EVENT_SCREEN_OFF = 'usual.event.SCREEN_OFF',
        /**
         * Indicates that the device screen is on and the device is in interactive state.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_SCREEN_ON
         */
        COMMON_EVENT_SCREEN_ON = 'usual.event.SCREEN_ON',
        /**
         * Indicates that the device thermal level has changed.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_THERMAL_LEVEL_CHANGED
         */
        COMMON_EVENT_THERMAL_LEVEL_CHANGED = 'usual.event.THERMAL_LEVEL_CHANGED',
        /**
         * (reserved, not supported yet) Indicates that the user unlocks the device.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_USER_PRESENT
         */
        COMMON_EVENT_USER_PRESENT = 'usual.event.USER_PRESENT',
        /**
         * Indicates that the system time has changed as time ticks by.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_TIME_TICK
         */
        COMMON_EVENT_TIME_TICK = 'usual.event.TIME_TICK',
        /**
         * Indicates that the system time is set.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_TIME_CHANGED
         */
        COMMON_EVENT_TIME_CHANGED = 'usual.event.TIME_CHANGED',
        /**
         * (reserved, not supported yet) Indicates that the system date has been changed.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_DATE_CHANGED
         */
        COMMON_EVENT_DATE_CHANGED = 'usual.event.DATE_CHANGED',
        /**
         * Indicates that the system time zone is changed.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_TIMEZONE_CHANGED
         */
        COMMON_EVENT_TIMEZONE_CHANGED = 'usual.event.TIMEZONE_CHANGED',
        /**
         * (reserved, not supported yet) Indicates that the user closes a temporary system dialog box.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_CLOSE_SYSTEM_DIALOGS
         */
        COMMON_EVENT_CLOSE_SYSTEM_DIALOGS = 'usual.event.CLOSE_SYSTEM_DIALOGS',
        /**
         * Indicates that a new application package has been installed on the device.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_PACKAGE_ADDED
         */
        COMMON_EVENT_PACKAGE_ADDED = 'usual.event.PACKAGE_ADDED',
        /**
         * (reserved, not supported yet) Indicates that a later version of an installed application package has replaced the
         * previous one on the device.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_PACKAGE_REPLACED
         */
        COMMON_EVENT_PACKAGE_REPLACED = 'usual.event.PACKAGE_REPLACED',
        /**
         * (reserved, not supported yet) Indicates that the new version of the application package has replaced the previous
         * version.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_MY_PACKAGE_REPLACED
         */
        COMMON_EVENT_MY_PACKAGE_REPLACED = 'usual.event.MY_PACKAGE_REPLACED',
        /**
         * Indicates that an installed application has been uninstalled from the device with the application data retained.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_PACKAGE_REMOVED
         */
        COMMON_EVENT_PACKAGE_REMOVED = 'usual.event.PACKAGE_REMOVED',
        /**
         * (reserved, not supported yet) Indicates that an installed bundle has been uninstalled from the device with the
         * application data retained.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_BUNDLE_REMOVED
         */
        COMMON_EVENT_BUNDLE_REMOVED = 'usual.event.BUNDLE_REMOVED',
        /**
         * (reserved, not supported yet) Indicates that an installed application, including both the application data and
         * code, has been completely uninstalled from the device.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_PACKAGE_FULLY_REMOVED
         */
        COMMON_EVENT_PACKAGE_FULLY_REMOVED = 'usual.event.PACKAGE_FULLY_REMOVED',
        /**
         * Indicates that an application package has been changed (for example, an ability in the package has been enabled
         * or disabled).
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_PACKAGE_CHANGED
         */
        COMMON_EVENT_PACKAGE_CHANGED = 'usual.event.PACKAGE_CHANGED',
        /**
         * Indicates that the user closed all processes of the application and restarted the application.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_PACKAGE_RESTARTED
         */
        COMMON_EVENT_PACKAGE_RESTARTED = 'usual.event.PACKAGE_RESTARTED',
        /**
         * Indicates that the user cleared the application package data.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_PACKAGE_DATA_CLEARED
         */
        COMMON_EVENT_PACKAGE_DATA_CLEARED = 'usual.event.PACKAGE_DATA_CLEARED',
        /**
         * (reserved, not supported yet) Indicates that application packages have been suspended.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_PACKAGES_SUSPENDED
         */
        COMMON_EVENT_PACKAGES_SUSPENDED = 'usual.event.PACKAGES_SUSPENDED',
        /**
         * (reserved, not supported yet) Indicates that the application HAP package is not suspended (resumed from the
         * suspended state).
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_PACKAGES_UNSUSPENDED
         */
        COMMON_EVENT_PACKAGES_UNSUSPENDED = 'usual.event.PACKAGES_UNSUSPENDED',
        /**
         * Indicates that the application HAP package is suspended.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_MY_PACKAGE_SUSPENDED
         */
        COMMON_EVENT_MY_PACKAGE_SUSPENDED = 'usual.event.MY_PACKAGE_SUSPENDED',
        /**
         * Indicates that the application package is not suspended.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_MY_PACKAGE_UNSUSPENDED
         */
        COMMON_EVENT_MY_PACKAGE_UNSUSPENDED = 'usual.event.MY_PACKAGE_UNSUSPENDED',
        /**
         * (reserved, not supported yet) Indicates that a user ID has been removed from the system.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_UID_REMOVED
         */
        COMMON_EVENT_UID_REMOVED = 'usual.event.UID_REMOVED',
        /**
         * (reserved, not supported yet) Indicates that an installed application is started for the first time.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_PACKAGE_FIRST_LAUNCH
         */
        COMMON_EVENT_PACKAGE_FIRST_LAUNCH = 'usual.event.PACKAGE_FIRST_LAUNCH',
        /**
         * (reserved, not supported yet) Indicates that an application requires system verification.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_PACKAGE_NEEDS_VERIFICATION
         */
        COMMON_EVENT_PACKAGE_NEEDS_VERIFICATION = 'usual.event.PACKAGE_NEEDS_VERIFICATION',
        /**
         * (reserved, not supported yet) Indicates that an application has been verified by the system.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_PACKAGE_VERIFIED
         */
        COMMON_EVENT_PACKAGE_VERIFIED = 'usual.event.PACKAGE_VERIFIED',
        /**
         * (reserved, not supported yet) Indicates that applications installed on the external storage are available for the
         * system.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_EXTERNAL_APPLICATIONS_AVAILABLE
         */
        COMMON_EVENT_EXTERNAL_APPLICATIONS_AVAILABLE = 'usual.event.EXTERNAL_APPLICATIONS_AVAILABLE',
        /**
         * (reserved, not supported yet) Indicates that applications installed on the external storage are not available for
         * the system.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_EXTERNAL_APPLICATIONS_UNAVAILABLE
         */
        COMMON_EVENT_EXTERNAL_APPLICATIONS_UNAVAILABLE = 'usual.event.EXTERNAL_APPLICATIONS_UNAVAILABLE',
        /**
         * (reserved, not supported yet) Indicates that the device state (for example, orientation and locale) has changed.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_CONFIGURATION_CHANGED
         */
        COMMON_EVENT_CONFIGURATION_CHANGED = 'usual.event.CONFIGURATION_CHANGED',
        /**
         * (reserved, not supported yet) Indicates that the device locale has changed.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_LOCALE_CHANGED
         */
        COMMON_EVENT_LOCALE_CHANGED = 'usual.event.LOCALE_CHANGED',
        /**
         * (reserved, not supported yet) Indicates that the device storage is insufficient.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_MANAGE_PACKAGE_STORAGE
         */
        COMMON_EVENT_MANAGE_PACKAGE_STORAGE = 'usual.event.MANAGE_PACKAGE_STORAGE',
        /**
         * (reserved, not supported yet) Indicates that the system is in driving mode.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_DRIVE_MODE
         */
        COMMON_EVENT_DRIVE_MODE = 'common.event.DRIVE_MODE',
        /**
         * (reserved, not supported yet) Indicates that the system is in home mode.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_HOME_MODE
         */
        COMMON_EVENT_HOME_MODE = 'common.event.HOME_MODE',
        /**
         * (reserved, not supported yet) Indicates that the system is in office mode.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_OFFICE_MODE
         */
        COMMON_EVENT_OFFICE_MODE = 'common.event.OFFICE_MODE',
        /**
         * (reserved, not supported yet) Indicates that the user has been started.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_USER_STARTED
         */
        COMMON_EVENT_USER_STARTED = 'usual.event.USER_STARTED',
        /**
         * (reserved, not supported yet) Indicates that the user has been brought to the background.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_USER_BACKGROUND
         */
        COMMON_EVENT_USER_BACKGROUND = 'usual.event.USER_BACKGROUND',
        /**
         * (reserved, not supported yet) Indicates that the user has been brought to the foreground.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_USER_FOREGROUND
         */
        COMMON_EVENT_USER_FOREGROUND = 'usual.event.USER_FOREGROUND',
        /**
         * Indicates that user switching is in progress.
         *
         * To subscribe to this common event, your application must have the ohos.permission.MANAGE_LOCAL_ACCOUNTS
         * permission. (This permission is available only for system applications.)
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_USER_SWITCHED
         */
        COMMON_EVENT_USER_SWITCHED = 'usual.event.USER_SWITCHED',
        /**
         * (reserved, not supported yet) Indicates that user starting is in progress.
         * To subscribe to this common event, your application must have the ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS
         * permission. (This permission is available only for system applications.)
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_USER_STARTING
         */
        COMMON_EVENT_USER_STARTING = 'usual.event.USER_STARTING',
        /**
         * (reserved, not supported yet) Indicates that the credential encryption storage of the current user has been
         * unlocked upon restart.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_USER_UNLOCKED
         */
        COMMON_EVENT_USER_UNLOCKED = 'usual.event.USER_UNLOCKED',
        /**
         * (reserved, not supported yet) Indicates the user to be stopped.
         *
         * To subscribe to this common event, your application must have the ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS
         * permission. (This permission is available only for system applications.)
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_USER_STOPPING
         */
        COMMON_EVENT_USER_STOPPING = 'usual.event.USER_STOPPING',
        /**
         * (reserved, not supported yet) Indicates that the user has been stopped.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_USER_STOPPED
         */
        COMMON_EVENT_USER_STOPPED = 'usual.event.USER_STOPPED',
        /**
         * HW id login successfully.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_DISTRIBUTED_ACCOUNT_LOGIN
         */
        COMMON_EVENT_HWID_LOGIN = 'common.event.HWID_LOGIN',
        /**
         * HW id logout successfully.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_DISTRIBUTED_ACCOUNT_LOGOUT
         */
        COMMON_EVENT_HWID_LOGOUT = 'common.event.HWID_LOGOUT',
        /**
         * HW id is invalid.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_DISTRIBUTED_ACCOUNT_TOKEN_INVALID
         */
        COMMON_EVENT_HWID_TOKEN_INVALID = 'common.event.HWID_TOKEN_INVALID',
        /**
         * HW id logs off.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_DISTRIBUTED_ACCOUNT_LOGOFF
         */
        COMMON_EVENT_HWID_LOGOFF = 'common.event.HWID_LOGOFF',
        /**
         * Indicates a change in the Wi-Fi state (enabled or disabled).
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_WIFI_POWER_STATE
         */
        COMMON_EVENT_WIFI_POWER_STATE = 'usual.event.wifi.POWER_STATE',
        /**
         * Indicates that the Wi-Fi access point has been scanned and proved available.
         *
         * To subscribe to this common event, your application must have the ohos.permission.LOCATION permission.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_WIFI_SCAN_FINISHED
         */
        COMMON_EVENT_WIFI_SCAN_FINISHED = 'usual.event.wifi.SCAN_FINISHED',
        /**
         * Indicates that the Wi-Fi signal strength (RSSI) has changed.
         *
         * To subscribe to this common event, your application must have the ohos.permission.GET_WIFI_INFO permission.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_WIFI_RSSI_VALUE
         */
        COMMON_EVENT_WIFI_RSSI_VALUE = 'usual.event.wifi.RSSI_VALUE',
        /**
         * Indicates that the Wi-Fi connection state has changed.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_WIFI_CONN_STATE
         */
        COMMON_EVENT_WIFI_CONN_STATE = 'usual.event.wifi.CONN_STATE',
        /**
         * Indicates a change in the Wi-Fi hotspot state (enabled or disabled).
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_WIFI_HOTSPOT_STATE
         */
        COMMON_EVENT_WIFI_HOTSPOT_STATE = 'usual.event.wifi.HOTSPOT_STATE',
        /**
         * Indicates that a client has joined the Wi-Fi hotspot of the current device.
         *
         * To subscribe to this common event, your application must have the ohos.permission.GET_WIFI_INFO permission.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_WIFI_AP_STA_JOIN
         */
        COMMON_EVENT_WIFI_AP_STA_JOIN = 'usual.event.wifi.WIFI_HS_STA_JOIN',
        /**
         * Indicates that the client is disconnected from the Wi-Fi hotspot of the current device.
         *
         * To subscribe to this common event, your application must have the ohos.permission.GET_WIFI_INFO permission.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_WIFI_AP_STA_LEAVE
         */
        COMMON_EVENT_WIFI_AP_STA_LEAVE = 'usual.event.wifi.WIFI_HS_STA_LEAVE',
        /**
         * (not supported yet) Indicates that the state of MPLINK (an enhanced Wi-Fi feature) has changed.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_WIFI_MPLINK_STATE_CHANGE
         */
        COMMON_EVENT_WIFI_MPLINK_STATE_CHANGE = 'usual.event.wifi.mplink.STATE_CHANGE',
        /**
         * Indicates that the Wi-Fi P2P connection state has changed.
         *
         * To subscribe to this common event, your application must have the ohos.permission.GET_WIFI_INFO and
         * ohos.permission.LOCATION permissions.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_WIFI_P2P_CONN_STATE
         */
        COMMON_EVENT_WIFI_P2P_CONN_STATE = 'usual.event.wifi.p2p.CONN_STATE_CHANGE',
        /**
         * Indicates a change in the Wi-Fi P2P state (enabled or disabled).
         *
         * To subscribe to this common event, your application must have the ohos.permission.GET_WIFI_INFO permission.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_WIFI_P2P_STATE_CHANGED
         */
        COMMON_EVENT_WIFI_P2P_STATE_CHANGED = 'usual.event.wifi.p2p.STATE_CHANGE',
        /**
         * Indicates that the state of the Wi-Fi P2P peer device has changed.
         *
         * To subscribe to this common event, your application must have the ohos.permission.GET_WIFI_INFO permission.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_WIFI_P2P_PEERS_STATE_CHANGED
         */
        COMMON_EVENT_WIFI_P2P_PEERS_STATE_CHANGED = 'usual.event.wifi.p2p.DEVICES_CHANGE',
        /**
         * Indicates that the Wi-Fi P2P discovery state has changed.
         *
         * To subscribe to this common event, your application must have the ohos.permission.GET_WIFI_INFO permission.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_WIFI_P2P_PEERS_DISCOVERY_STATE_CHANGED
         */
        COMMON_EVENT_WIFI_P2P_PEERS_DISCOVERY_STATE_CHANGED = 'usual.event.wifi.p2p.PEER_DISCOVERY_STATE_CHANGE',
        /**
         * Indicates that the state of the Wi-Fi P2P local device has changed.
         *
         * To subscribe to this common event, your application must have the ohos.permission.GET_WIFI_INFO permission.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_WIFI_P2P_CURRENT_DEVICE_STATE_CHANGED
         */
        COMMON_EVENT_WIFI_P2P_CURRENT_DEVICE_STATE_CHANGED = 'usual.event.wifi.p2p.CURRENT_DEVICE_CHANGE',
        /**
         * Indicates that the Wi-Fi P2P group information has changed.
         *
         * To subscribe to this common event, your application must have the ohos.permission.GET_WIFI_INFO permission.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_WIFI_P2P_GROUP_STATE_CHANGED
         */
        COMMON_EVENT_WIFI_P2P_GROUP_STATE_CHANGED = 'usual.event.wifi.p2p.GROUP_STATE_CHANGED',
        /**
         * (reserved, not supported yet) Indicates the connection state of Bluetooth handsfree communication.
         *
         * To subscribe to this common event, your application must have the ohos.permission.USE_BLUETOOTH permission.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_BLUETOOTH_HANDSFREE_AG_CONNECT_STATE_UPDATE
         */
        COMMON_EVENT_BLUETOOTH_HANDSFREE_AG_CONNECT_STATE_UPDATE = 'usual.event.bluetooth.handsfree.ag.CONNECT_STATE_UPDATE',
        /**
         * (reserved, not supported yet) Indicates that the device connected to the Bluetooth handsfree function is active.
         *
         * To subscribe to this common event, your application must have the ohos.permission.USE_BLUETOOTH permission.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_BLUETOOTH_HANDSFREE_AG_CURRENT_DEVICE_UPDATE
         */
        COMMON_EVENT_BLUETOOTH_HANDSFREE_AG_CURRENT_DEVICE_UPDATE = 'usual.event.bluetooth.handsfree.ag.CURRENT_DEVICE_UPDATE',
        /**
         * (reserved, not supported yet) Indicates that the connection state of Bluetooth A2DP has changed.
         *
         * To subscribe to this common event, your application must have the ohos.permission.USE_BLUETOOTH permission.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_BLUETOOTH_HANDSFREE_AG_AUDIO_STATE_UPDATE
         */
        COMMON_EVENT_BLUETOOTH_HANDSFREE_AG_AUDIO_STATE_UPDATE = 'usual.event.bluetooth.handsfree.ag.AUDIO_STATE_UPDATE',
        /**
         * (reserved, not supported yet) Indicates the connection state of Bluetooth A2DP.
         *
         * To subscribe to this common event, your application must have the ohos.permission.USE_BLUETOOTH permission.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_BLUETOOTH_A2DPSOURCE_CONNECT_STATE_UPDATE
         */
        COMMON_EVENT_BLUETOOTH_A2DPSOURCE_CONNECT_STATE_UPDATE = 'usual.event.bluetooth.a2dpsource.CONNECT_STATE_UPDATE',
        /**
         * (reserved, not supported yet) Indicates that the device connected using Bluetooth A2DP is active.
         *
         * To subscribe to this common event, your application must have the ohos.permission.USE_BLUETOOTH permission.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_BLUETOOTH_A2DPSOURCE_CURRENT_DEVICE_UPDATE
         */
        COMMON_EVENT_BLUETOOTH_A2DPSOURCE_CURRENT_DEVICE_UPDATE = 'usual.event.bluetooth.a2dpsource.CURRENT_DEVICE_UPDATE',
        /**
         * (reserved, not supported yet) Indicates that the playing state of Bluetooth A2DP has changed.
         *
         * To subscribe to this common event, your application must have the ohos.permission.USE_BLUETOOTH permission.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_BLUETOOTH_A2DPSOURCE_PLAYING_STATE_UPDATE
         */
        COMMON_EVENT_BLUETOOTH_A2DPSOURCE_PLAYING_STATE_UPDATE = 'usual.event.bluetooth.a2dpsource.PLAYING_STATE_UPDATE',
        /**
         * (reserved, not supported yet) Indicates that the AVRCP connection state of Bluetooth A2DP has changed.
         *
         * To subscribe to this common event, your application must have the ohos.permission.USE_BLUETOOTH permission.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_BLUETOOTH_A2DPSOURCE_AVRCP_CONNECT_STATE_UPDATE
         */
        COMMON_EVENT_BLUETOOTH_A2DPSOURCE_AVRCP_CONNECT_STATE_UPDATE = 'usual.event.bluetooth.a2dpsource.AVRCP_CONNECT_STATE_UPDATE',
        /**
         * (reserved, not supported yet) Indicates that the audio codec state of Bluetooth A2DP has changed.
         *
         * To subscribe to this common event, your application must have the ohos.permission.USE_BLUETOOTH permission.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_BLUETOOTH_A2DPSOURCE_CODEC_VALUE_UPDATE
         */
        COMMON_EVENT_BLUETOOTH_A2DPSOURCE_CODEC_VALUE_UPDATE = 'usual.event.bluetooth.a2dpsource.CODEC_VALUE_UPDATE',
        /**
         * (reserved, not supported yet) Indicates that a remote Bluetooth device is discovered.
         *
         * To subscribe to this common event, your application must have the ohos.permission.LOCATION and
         * ohos.permission.USE_BLUETOOTH permissions.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_BLUETOOTH_REMOTEDEVICE_DISCOVERED
         */
        COMMON_EVENT_BLUETOOTH_REMOTEDEVICE_DISCOVERED = 'usual.event.bluetooth.remotedevice.DISCOVERED',
        /**
         * (reserved, not supported yet) Indicates that the Bluetooth class of a remote Bluetooth device has changed.
         *
         * To subscribe to this common event, your application must have the ohos.permission.USE_BLUETOOTH permission.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_BLUETOOTH_REMOTEDEVICE_CLASS_VALUE_UPDATE
         */
        COMMON_EVENT_BLUETOOTH_REMOTEDEVICE_CLASS_VALUE_UPDATE = 'usual.event.bluetooth.remotedevice.CLASS_VALUE_UPDATE',
        /**
         * (reserved, not supported yet) Indicates that a low-level (ACL) connection has been established with the remote
         * Bluetooth device.
         *
         * To subscribe to this common event, your application must have the ohos.permission.USE_BLUETOOTH permission.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_BLUETOOTH_REMOTEDEVICE_ACL_CONNECTED
         */
        COMMON_EVENT_BLUETOOTH_REMOTEDEVICE_ACL_CONNECTED = 'usual.event.bluetooth.remotedevice.ACL_CONNECTED',
        /**
         * (reserved, not supported yet) Indicates that the low-level (ACL) connection has been disconnected from the remote
         * Bluetooth device.
         *
         * To subscribe to this common event, your application must have the ohos.permission.USE_BLUETOOTH permission.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_BLUETOOTH_REMOTEDEVICE_ACL_DISCONNECTED
         */
        COMMON_EVENT_BLUETOOTH_REMOTEDEVICE_ACL_DISCONNECTED = 'usual.event.bluetooth.remotedevice.ACL_DISCONNECTED',
        /**
         * (reserved, not supported yet) Indicates that the friendly name of a remote Bluetooth device is retrieved for the
         * first time or has changed since the last retrieval.
         *
         * To subscribe to this common event, your application must have the ohos.permission.USE_BLUETOOTH permission.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_BLUETOOTH_REMOTEDEVICE_NAME_UPDATE
         */
        COMMON_EVENT_BLUETOOTH_REMOTEDEVICE_NAME_UPDATE = 'usual.event.bluetooth.remotedevice.NAME_UPDATE',
        /**
         * (reserved, not supported yet) Indicates the connection state with a remote Bluetooth device is changed.
         *
         * To subscribe to this common event, your application must have the ohos.permission.USE_BLUETOOTH permission.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_BLUETOOTH_REMOTEDEVICE_PAIR_STATE
         */
        COMMON_EVENT_BLUETOOTH_REMOTEDEVICE_PAIR_STATE = 'usual.event.bluetooth.remotedevice.PAIR_STATE',
        /**
         * (reserved, not supported yet) Indicates that the battery level of a remote Bluetooth device is retrieved for the
         * first time or has changed since the last retrieval.
         *
         * To subscribe to this common event, your application must have the ohos.permission.USE_BLUETOOTH permission.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_BLUETOOTH_REMOTEDEVICE_BATTERY_VALUE_UPDATE
         */
        COMMON_EVENT_BLUETOOTH_REMOTEDEVICE_BATTERY_VALUE_UPDATE = 'usual.event.bluetooth.remotedevice.BATTERY_VALUE_UPDATE',
        /**
         * (reserved, not supported yet) Indicates the SDP state of a remote Bluetooth device.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_BLUETOOTH_REMOTEDEVICE_SDP_RESULT
         */
        COMMON_EVENT_BLUETOOTH_REMOTEDEVICE_SDP_RESULT = 'usual.event.bluetooth.remotedevice.SDP_RESULT',
        /**
         * (reserved, not supported yet) Indicates the UUID connection state with a remote Bluetooth device.
         *
         * To subscribe to this common event, your application must have the ohos.permission.DISCOVER_BLUETOOTH permission.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_BLUETOOTH_REMOTEDEVICE_UUID_VALUE
         */
        COMMON_EVENT_BLUETOOTH_REMOTEDEVICE_UUID_VALUE = 'usual.event.bluetooth.remotedevice.UUID_VALUE',
        /**
         * (reserved, not supported yet) Indicates the pairing request from a remote Bluetooth device.
         *
         * To subscribe to this common event, your application must have the ohos.permission.DISCOVER_BLUETOOTH permission.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_BLUETOOTH_REMOTEDEVICE_PAIRING_REQ
         */
        COMMON_EVENT_BLUETOOTH_REMOTEDEVICE_PAIRING_REQ = 'usual.event.bluetooth.remotedevice.PAIRING_REQ',
        /**
         * (reserved, not supported yet) Indicates that Bluetooth pairing has been canceled.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_BLUETOOTH_REMOTEDEVICE_PAIRING_CANCEL
         */
        COMMON_EVENT_BLUETOOTH_REMOTEDEVICE_PAIRING_CANCEL = 'usual.event.bluetooth.remotedevice.PAIRING_CANCEL',
        /**
         * (reserved, not supported yet) Indicates the connection request from a remote Bluetooth device.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_BLUETOOTH_REMOTEDEVICE_CONNECT_REQ
         */
        COMMON_EVENT_BLUETOOTH_REMOTEDEVICE_CONNECT_REQ = 'usual.event.bluetooth.remotedevice.CONNECT_REQ',
        /**
         * (reserved, not supported yet) Indicates the response to the connection request from a remote Bluetooth device.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_BLUETOOTH_REMOTEDEVICE_CONNECT_REPLY
         */
        COMMON_EVENT_BLUETOOTH_REMOTEDEVICE_CONNECT_REPLY = 'usual.event.bluetooth.remotedevice.CONNECT_REPLY',
        /**
         * (reserved, not supported yet) Indicates that the connection to a remote Bluetooth device has been canceled.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_BLUETOOTH_REMOTEDEVICE_CONNECT_CANCEL
         */
        COMMON_EVENT_BLUETOOTH_REMOTEDEVICE_CONNECT_CANCEL = 'usual.event.bluetooth.remotedevice.CONNECT_CANCEL',
        /**
         * (reserved, not supported yet) Indicates that the connection state with a Bluetooth handsfree has changed.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_BLUETOOTH_HANDSFREEUNIT_CONNECT_STATE_UPDATE
         */
        COMMON_EVENT_BLUETOOTH_HANDSFREEUNIT_CONNECT_STATE_UPDATE = 'usual.event.bluetooth.handsfreeunit.CONNECT_STATE_UPDATE',
        /**
         * (reserved, not supported yet) Indicates that the audio state of a Bluetooth handsfree has changed.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_BLUETOOTH_HANDSFREEUNIT_AUDIO_STATE_UPDATE
         */
        COMMON_EVENT_BLUETOOTH_HANDSFREEUNIT_AUDIO_STATE_UPDATE = 'usual.event.bluetooth.handsfreeunit.AUDIO_STATE_UPDATE',
        /**
         * (reserved, not supported yet) Indicates that the audio gateway state of a Bluetooth handsfree has changed.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_BLUETOOTH_HANDSFREEUNIT_AG_COMMON_EVENT
         */
        COMMON_EVENT_BLUETOOTH_HANDSFREEUNIT_AG_COMMON_EVENT = 'usual.event.bluetooth.handsfreeunit.AG_COMMON_EVENT',
        /**
         * (reserved, not supported yet) Indicates that the calling state of a Bluetooth handsfree has changed.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_BLUETOOTH_HANDSFREEUNIT_AG_CALL_STATE_UPDATE
         */
        COMMON_EVENT_BLUETOOTH_HANDSFREEUNIT_AG_CALL_STATE_UPDATE = 'usual.event.bluetooth.handsfreeunit.AG_CALL_STATE_UPDATE',
        /**
         * (reserved, not supported yet) Indicates a change in the Bluetooth adapter state (enabled or disabled).
         *
         * To subscribe to this common event, your application must have the ohos.permission.USE_BLUETOOTH permission.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_BLUETOOTH_HOST_STATE_UPDATE
         */
        COMMON_EVENT_BLUETOOTH_HOST_STATE_UPDATE = 'usual.event.bluetooth.host.STATE_UPDATE',
        /**
         * (reserved, not supported yet) Indicates that Bluetooth is discoverable.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_BLUETOOTH_HOST_REQ_DISCOVERABLE
         */
        COMMON_EVENT_BLUETOOTH_HOST_REQ_DISCOVERABLE = 'usual.event.bluetooth.host.REQ_DISCOVERABLE',
        /**
         * (reserved, not supported yet) Indicates that Bluetooth is enabled.
         *
         * To subscribe to this common event, your application must have the ohos.permission.USE_BLUETOOTH permission.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_BLUETOOTH_HOST_REQ_ENABLE
         */
        COMMON_EVENT_BLUETOOTH_HOST_REQ_ENABLE = 'usual.event.bluetooth.host.REQ_ENABLE',
        /**
         * (reserved, not supported yet) Indicates that Bluetooth is disabled.
         *
         * To subscribe to this common event, your application must have the ohos.permission.USE_BLUETOOTH permission.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_BLUETOOTH_HOST_REQ_DISABLE
         */
        COMMON_EVENT_BLUETOOTH_HOST_REQ_DISABLE = 'usual.event.bluetooth.host.REQ_DISABLE',
        /**
         * (reserved, not supported yet) Indicates that the Bluetooth scan mode of the device is changed.
         *
         * To subscribe to this common event, your application must have the ohos.permission.USE_BLUETOOTH permission.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_BLUETOOTH_HOST_SCAN_MODE_UPDATE
         */
        COMMON_EVENT_BLUETOOTH_HOST_SCAN_MODE_UPDATE = 'usual.event.bluetooth.host.SCAN_MODE_UPDATE',
        /**
         * (reserved, not supported yet) Indicates that Bluetooth discovery is started on the device.
         *
         * To subscribe to this common event, your application must have the ohos.permission.USE_BLUETOOTH permission.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_BLUETOOTH_HOST_DISCOVERY_STARTED
         */
        COMMON_EVENT_BLUETOOTH_HOST_DISCOVERY_STARTED = 'usual.event.bluetooth.host.DISCOVERY_STARTED',
        /**
         * (reserved, not supported yet) Indicates that Bluetooth discovery is finished on the device.
         *
         * To subscribe to this common event, your application must have the ohos.permission.USE_BLUETOOTH permission.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_BLUETOOTH_HOST_DISCOVERY_FINISHED
         */
        COMMON_EVENT_BLUETOOTH_HOST_DISCOVERY_FINISHED = 'usual.event.bluetooth.host.DISCOVERY_FINISHED',
        /**
         * (reserved, not supported yet) Indicates that the name of the device Bluetooth adapter has changed.
         *
         * To subscribe to this common event, your application must have the ohos.permission.USE_BLUETOOTH permission.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_BLUETOOTH_HOST_NAME_UPDATE
         */
        COMMON_EVENT_BLUETOOTH_HOST_NAME_UPDATE = 'usual.event.bluetooth.host.NAME_UPDATE',
        /**
         * (reserved, not supported yet) Indicates that the connection state of Bluetooth A2DP Sink has changed.
         *
         * To subscribe to this common event, your application must have the ohos.permission.USE_BLUETOOTH permission.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_BLUETOOTH_A2DPSINK_CONNECT_STATE_UPDATE
         */
        COMMON_EVENT_BLUETOOTH_A2DPSINK_CONNECT_STATE_UPDATE = 'usual.event.bluetooth.a2dpsink.CONNECT_STATE_UPDATE',
        /**
         * (reserved, not supported yet) Indicates that the playing state of Bluetooth A2DP Sink has changed.
         *
         * To subscribe to this common event, your application must have the ohos.permission.USE_BLUETOOTH permission.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_BLUETOOTH_A2DPSINK_PLAYING_STATE_UPDATE
         */
        COMMON_EVENT_BLUETOOTH_A2DPSINK_PLAYING_STATE_UPDATE = 'usual.event.bluetooth.a2dpsink.PLAYING_STATE_UPDATE',
        /**
         * (reserved, not supported yet) Indicates that the audio state of Bluetooth A2DP Sink has changed.
         *
         * To subscribe to this common event, your application must have the ohos.permission.USE_BLUETOOTH permission.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_BLUETOOTH_A2DPSINK_AUDIO_STATE_UPDATE
         */
        COMMON_EVENT_BLUETOOTH_A2DPSINK_AUDIO_STATE_UPDATE = 'usual.event.bluetooth.a2dpsink.AUDIO_STATE_UPDATE',
        /**
         * (reserved, not supported yet) Indicates that the state of the device NFC adapter has changed.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_NFC_ACTION_ADAPTER_STATE_CHANGED
         */
        COMMON_EVENT_NFC_ACTION_ADAPTER_STATE_CHANGED = 'usual.event.nfc.action.ADAPTER_STATE_CHANGED',
        /**
         * (reserved, not supported yet) Indicates that the NFC RF field is detected to be in the enabled state.
         *
         * To subscribe to this common event, your application must have the ohos.permission.MANAGE_SECURE_SETTINGS
         * permission. (This permission is available only for system applications.)
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_NFC_ACTION_RF_FIELD_ON_DETECTED
         */
        COMMON_EVENT_NFC_ACTION_RF_FIELD_ON_DETECTED = 'usual.event.nfc.action.RF_FIELD_ON_DETECTED',
        /**
         * (reserved, not supported yet) Indicates that the NFC RF field is detected to be in the disabled state.
         *
         * To subscribe to this common event, your application must have the ohos.permission.MANAGE_SECURE_SETTINGS
         * permission. (This permission is available only for system applications.)
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_NFC_ACTION_RF_FIELD_OFF_DETECTED
         */
        COMMON_EVENT_NFC_ACTION_RF_FIELD_OFF_DETECTED = 'usual.event.nfc.action.RF_FIELD_OFF_DETECTED',
        /**
         * Indicates that the system stops charging the battery.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_DISCHARGING
         */
        COMMON_EVENT_DISCHARGING = 'usual.event.DISCHARGING',
        /**
         * Indicates that the system starts charging the battery.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_CHARGING
         */
        COMMON_EVENT_CHARGING = 'usual.event.CHARGING',
        /**
         * (reserved, not supported yet) Indicates that the system idle mode has changed.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_DEVICE_IDLE_MODE_CHANGED
         */
        COMMON_EVENT_DEVICE_IDLE_MODE_CHANGED = 'usual.event.DEVICE_IDLE_MODE_CHANGED',
        /**
         * Indicates that the system power-saving mode has changed.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_POWER_SAVE_MODE_CHANGED
         */
        COMMON_EVENT_POWER_SAVE_MODE_CHANGED = 'usual.event.POWER_SAVE_MODE_CHANGED',
        /**
         * Indicates that a user has been added to the system.
         *
         * To subscribe to this common event, your application must have the ohos.permission.MANAGE_LOCAL_ACCOUNTS
         * permission. (This permission is available only for system applications.)
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_USER_ADDED
         */
        COMMON_EVENT_USER_ADDED = 'usual.event.USER_ADDED',
        /**
         * Indicates that a user has been removed from the system.
         *
         * To subscribe to this common event, your application must have the ohos.permission.MANAGE_LOCAL_ACCOUNTS
         * permission. (This permission is available only for system applications.)
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_USER_REMOVED
         */
        COMMON_EVENT_USER_REMOVED = 'usual.event.USER_REMOVED',
        /**
         * (reserved, not supported yet) Indicates that an ability has been added.
         *
         * To subscribe to this common event, your application must have the ohos.permission.LISTEN_BUNDLE_CHANGE permission.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_ABILITY_ADDED
         */
        COMMON_EVENT_ABILITY_ADDED = 'common.event.ABILITY_ADDED',
        /**
         * (reserved, not supported yet) Indicates that an ability has been removed.
         *
         * To subscribe to this common event, your application must have the ohos.permission.LISTEN_BUNDLE_CHANGE permission.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_ABILITY_REMOVED
         */
        COMMON_EVENT_ABILITY_REMOVED = 'common.event.ABILITY_REMOVED',
        /**
         * (reserved, not supported yet) Indicates that an ability has been updated.
         *
         * To subscribe to this common event, your application must have the ohos.permission.LISTEN_BUNDLE_CHANGE permission.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_ABILITY_UPDATED
         */
        COMMON_EVENT_ABILITY_UPDATED = 'common.event.ABILITY_UPDATED',
        /**
         * (reserved, not supported yet) Indicates that the location mode of the system has changed.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_LOCATION_MODE_STATE_CHANGED
         */
        COMMON_EVENT_LOCATION_MODE_STATE_CHANGED = 'usual.event.location.MODE_STATE_CHANGED',
        /**
         * (reserved, not supported yet) Indicates that the in-vehicle infotainment (IVI) system of the vehicle is sleeping.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_IVI_SLEEP
         */
        COMMON_EVENT_IVI_SLEEP = 'common.event.IVI_SLEEP',
        /**
         * (reserved, not supported yet) Indicates that the IVI system of the vehicle is in sleep mode and notifies the
         * application to stop playing.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_IVI_PAUSE
         */
        COMMON_EVENT_IVI_PAUSE = 'common.event.IVI_PAUSE',
        /**
         * (reserved, not supported yet) Indicates that a third-party application in the IVI system of a vehicle is
         * suspended.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_IVI_STANDBY
         */
        COMMON_EVENT_IVI_STANDBY = 'common.event.IVI_STANDBY',
        /**
         * (reserved, not supported yet) Indicates that the third-party application in the IVI system of the vehicle saves
         * the last mode.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_IVI_LASTMODE_SAVE
         */
        COMMON_EVENT_IVI_LASTMODE_SAVE = 'common.event.IVI_LASTMODE_SAVE',
        /**
         * (reserved, not supported yet) Indicates that the voltage of the vehicle's power system is abnormal.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_IVI_VOLTAGE_ABNORMAL
         */
        COMMON_EVENT_IVI_VOLTAGE_ABNORMAL = 'common.event.IVI_VOLTAGE_ABNORMAL',
        /**
         * (reserved, not supported yet) Indicates that the temperature of the IVI system of the vehicle is too high.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_IVI_HIGH_TEMPERATURE
         */
        COMMON_EVENT_IVI_HIGH_TEMPERATURE = 'common.event.IVI_HIGH_TEMPERATURE',
        /**
         * (reserved, not supported yet) Indicates that the temperature of the IVI system of the vehicle is extremely high.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_IVI_EXTREME_TEMPERATURE
         */
        COMMON_EVENT_IVI_EXTREME_TEMPERATURE = 'common.event.IVI_EXTREME_TEMPERATURE',
        /**
         * (reserved, not supported yet) Indicates that the IVI system of the vehicle has an extreme temperature.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_IVI_TEMPERATURE_ABNORMAL
         */
        COMMON_EVENT_IVI_TEMPERATURE_ABNORMAL = 'common.event.IVI_TEMPERATURE_ABNORMAL',
        /**
         * (reserved, not supported yet) Indicates that the voltage of the vehicle's power system is restored to normal.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_IVI_VOLTAGE_RECOVERY
         */
        COMMON_EVENT_IVI_VOLTAGE_RECOVERY = 'common.event.IVI_VOLTAGE_RECOVERY',
        /**
         * (reserved, not supported yet) Indicates that the temperature of the IVI system is restored to normal.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_IVI_TEMPERATURE_RECOVERY
         */
        COMMON_EVENT_IVI_TEMPERATURE_RECOVERY = 'common.event.IVI_TEMPERATURE_RECOVERY',
        /**
         * (reserved, not supported yet) Indicates that the battery service of the vehicle-mounted system is active.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_IVI_ACTIVE
         */
        COMMON_EVENT_IVI_ACTIVE = 'common.event.IVI_ACTIVE',
        /**
         * Indicates that a USB device has been attached to the device functioning as a USB host.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_USB_DEVICE_ATTACHED
         */
        COMMON_EVENT_USB_DEVICE_ATTACHED = 'usual.event.hardware.usb.action.USB_DEVICE_ATTACHED',
        /**
         * Indicates that a USB device has been detached from the device functioning as a USB host.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_USB_DEVICE_DETACHED
         */
        COMMON_EVENT_USB_DEVICE_DETACHED = 'usual.event.hardware.usb.action.USB_DEVICE_DETACHED',
        /**
         * (reserved, not supported yet) Indicates that a USB accessory was attached.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_USB_ACCESSORY_ATTACHED
         */
        COMMON_EVENT_USB_ACCESSORY_ATTACHED = 'usual.event.hardware.usb.action.USB_ACCESSORY_ATTACHED',
        /**
         * (reserved, not supported yet) Indicates that the USB attachment is uninstalled.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_USB_ACCESSORY_DETACHED
         */
        COMMON_EVENT_USB_ACCESSORY_DETACHED = 'usual.event.hardware.usb.action.USB_ACCESSORY_DETACHED',
        /**
         * (reserved, not supported yet) Indicates that an external storage device was removed.
         *
         * To subscribe to this common event, your application must have the ohos.permission.STORAGE_MANAGER
         * permission. (This permission is available only for system applications.)
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_DISK_REMOVED
         */
        COMMON_EVENT_DISK_REMOVED = 'usual.event.data.DISK_REMOVED',
        /**
         * (reserved, not supported yet) Indicates that an external storage device was unmounted.
         *
         * To subscribe to this common event, your application must have the ohos.permission.STORAGE_MANAGER
         * permission. (This permission is available only for system applications.)
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_DISK_UNMOUNTED
         */
        COMMON_EVENT_DISK_UNMOUNTED = 'usual.event.data.DISK_UNMOUNTED',
        /**
         * (reserved, not supported yet) Indicates that an external storage device was mounted.
         *
         * To subscribe to this common event, your application must have the ohos.permission.STORAGE_MANAGER
         * permission. (This permission is available only for system applications.)
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_DISK_MOUNTED
         */
        COMMON_EVENT_DISK_MOUNTED = 'usual.event.data.DISK_MOUNTED',
        /**
         * (reserved, not supported yet) Indicates that an external storage device was removed without being unmounted.
         *
         * To subscribe to this common event, your application must have the ohos.permission.STORAGE_MANAGER
         * permission. (This permission is available only for system applications.)
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_DISK_BAD_REMOVAL
         */
        COMMON_EVENT_DISK_BAD_REMOVAL = 'usual.event.data.DISK_BAD_REMOVAL',
        /**
         * (reserved, not supported yet) Indicates that the external storage device cannot be mounted when a card is
         * inserted.
         *
         * To subscribe to this common event, your application must have the ohos.permission.STORAGE_MANAGER
         * permission. (This permission is available only for system applications.)
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_DISK_UNMOUNTABLE
         */
        COMMON_EVENT_DISK_UNMOUNTABLE = 'usual.event.data.DISK_UNMOUNTABLE',
        /**
         * (reserved, not supported yet) Indicates that the external storage medium has been ejected (interactive operation
         * at the system software layer, not directly ejected physically).
         *
         * To subscribe to this common event, your application must have the ohos.permission.STORAGE_MANAGER
         * permission. (This permission is available only for system applications.)
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_DISK_EJECT
         */
        COMMON_EVENT_DISK_EJECT = 'usual.event.data.DISK_EJECT',
        /**
         * (reserved, not supported yet) Indicates that the account visibility changed.
         *
         * To subscribe to this common event, your application must have the ohos.permission.GET_APP_ACCOUNTS
         * permission. (This permission is available only for system applications.)
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_VISIBLE_ACCOUNTS_UPDATED
         */
        COMMON_EVENT_VISIBLE_ACCOUNTS_UPDATED = 'usual.event.data.VISIBLE_ACCOUNTS_UPDATED',
        /**
         * (reserved, not supported yet) Indicates that an account was deleted.
         *
         * To subscribe to this common event, your application must have the ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS
         * permission. (This permission is available only for system applications.)
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_ACCOUNT_DELETED
         */
        COMMON_EVENT_ACCOUNT_DELETED = 'usual.event.data.ACCOUNT_DELETED',
        /**
         * (reserved, not supported yet) Indicates that the foundation is ready.
         *
         * To subscribe to this common event, your application must have the ohos.permission.RECEIVER_STARTUP_COMPLETED
         * permission. (This permission is available only for system applications.)
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_FOUNDATION_READY
         */
        COMMON_EVENT_FOUNDATION_READY = 'common.event.FOUNDATION_READY',
        /**
         * Indicates that the airplane mode of the device has changed.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_AIRPLANE_MODE_CHANGED
         */
        COMMON_EVENT_AIRPLANE_MODE_CHANGED = 'usual.event.AIRPLANE_MODE',
        /**
         * Indicates that the screen has been split.
         *
         * @syscap SystemCapability.Notification.CommonEvent
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.commonEventManager:commonEventManager.Support#COMMON_EVENT_SPLIT_SCREEN
         */
        COMMON_EVENT_SPLIT_SCREEN = 'common.event.SPLIT_SCREEN'
    }
}
export default commonEvent;

```
