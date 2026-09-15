# @ohos.notification.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2021-2023 Huawei Device Co., Ltd.
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
import { AsyncCallback } from './@ohos.base';
import { NotificationRequest } from './notification/notificationRequest';
import { NotificationSlot } from './notification/notificationSlot';
/**
 * The **Notification** module provides notification management capabilities, covering notifications, notification slots
 * , notification subscription, notification enabled status, and notification badge status.
 *
 * @syscap SystemCapability.Notification.Notification
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.notificationManager:notificationManager
 */
declare namespace notification {
    /**
     * Publishes a notification. This API uses an asynchronous callback to return the result.
     *
     * @param { NotificationRequest } request - Content and related configuration of the notification to publish.
     * @param { AsyncCallback<void> } callback - Callback used to return the result.
     * @syscap SystemCapability.Notification.Notification
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.notificationManager/notificationManager#publish
     */
    function publish(request: NotificationRequest, callback: AsyncCallback<void>): void;
    /**
     * Publishes a notification. This API uses a promise to return the result.
     *
     * @param { NotificationRequest } request - Content and related configuration of the notification to publish.
     * @returns { Promise<void> } Promise that returns no value.
     * @syscap SystemCapability.Notification.Notification
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.notificationManager/notificationManager#publish
     */
    function publish(request: NotificationRequest): Promise<void>;
    /**
     * Cancels a notification with the specified ID. This API uses an asynchronous callback to return the result.
     *
     * @param { number } id - Notification ID.
     * @param { AsyncCallback<void> } callback - Callback used to return the result.
     * @syscap SystemCapability.Notification.Notification
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.notificationManager/notificationManager#cancel
     */
    function cancel(id: number, callback: AsyncCallback<void>): void;
    /**
     * Cancels a notification with the specified ID and label. This API uses an asynchronous callback to return the
     * result.
     *
     * @param { number } id - Notification ID.
     * @param { string } label - Notification label.
     * @param { AsyncCallback<void> } callback - Callback used to return the result.
     * @syscap SystemCapability.Notification.Notification
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.notificationManager/notificationManager#cancel
     */
    function cancel(id: number, label: string, callback: AsyncCallback<void>): void;
    /**
     * Cancels a notification with the specified ID and optional label. This API uses a promise to return the result.
     *
     * @param { number } id - Notification ID.
     * @param { string } [label] - Notification label. This parameter is left empty by default.
     * @returns { Promise<void> } Promise that returns no value.
     * @syscap SystemCapability.Notification.Notification
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.notificationManager/notificationManager#cancel
     */
    function cancel(id: number, label?: string): Promise<void>;
    /**
     * Cancels all notifications. This API uses an asynchronous callback to return the result.
     *
     * @param { AsyncCallback<void> } callback - Callback used to return the result.
     * @syscap SystemCapability.Notification.Notification
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.notificationManager/notificationManager#cancelAll
     */
    function cancelAll(callback: AsyncCallback<void>): void;
    /**
     * Cancels all notifications. This API uses a promise to return the result.
     *
     * @returns { Promise<void> } Promise that returns no value.
     * @syscap SystemCapability.Notification.Notification
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.notificationManager/notificationManager#cancelAll
     */
    function cancelAll(): Promise<void>;
    /**
     * Adds a notification slot of a specified type. This API uses an asynchronous callback to return the result.
     *
     * @param { SlotType } type - Type of the notification slot to add.
     * @param { AsyncCallback<void> } callback - Callback used to return the result.
     * @syscap SystemCapability.Notification.Notification
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.notificationManager/notificationManager#addSlot
     */
    function addSlot(type: SlotType, callback: AsyncCallback<void>): void;
    /**
     * Adds a notification slot of a specified type. This API uses a promise to return the result.
     *
     * @param { SlotType } type - Type of the notification slot to add.
     * @returns { Promise<void> } Promise that returns no value.
     * @syscap SystemCapability.Notification.Notification
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.notificationManager/notificationManager#addSlot
     */
    function addSlot(type: SlotType): Promise<void>;
    /**
     * Obtains a notification slot of a specified type. This API uses an asynchronous callback to return the result.
     *
     * @param { SlotType } slotType - Type of the notification slot, which can be used for social communication, service
     *     information, content consultation, and other purposes.
     * @param { AsyncCallback<NotificationSlot> } callback - Callback used to return the result.
     * @syscap SystemCapability.Notification.Notification
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.notificationManager/notificationManager#getSlot
     */
    function getSlot(slotType: SlotType, callback: AsyncCallback<NotificationSlot>): void;
    /**
     * Obtains a notification slot of a specified type. This API uses a promise to return the result.
     *
     * @param { SlotType } slotType - Type of the notification slot, which can be used for social communication, service
     *     information, content consultation, and other purposes.
     * @returns { Promise<NotificationSlot> } Promise used to return the result.
     * @syscap SystemCapability.Notification.Notification
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.notificationManager/notificationManager#getSlot
     */
    function getSlot(slotType: SlotType): Promise<NotificationSlot>;
    /**
     * Obtains all notification slots. This API uses an asynchronous callback to return the result.
     *
     * @param { AsyncCallback<Array<NotificationSlot>> } callback - Callback used to return the result.
     * @syscap SystemCapability.Notification.Notification
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.notificationManager/notificationManager#getSlots
     */
    function getSlots(callback: AsyncCallback<Array<NotificationSlot>>): void;
    /**
     * Obtains all notification slots of this application. This API uses a promise to return the result.
     *
     * @returns { Promise<Array<NotificationSlot>> } Promise used to return the result.
     * @syscap SystemCapability.Notification.Notification
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.notificationManager/notificationManager#getSlots
     */
    function getSlots(): Promise<Array<NotificationSlot>>;
    /**
     * Removes a notification slot of a specified type. This API uses an asynchronous callback to return the result.
     *
     * @param { SlotType } slotType - Type of the notification slot, which can be used for social communication, service
     *     information, content consultation, and other purposes.
     * @param { AsyncCallback<void> } callback - Callback used to return the result.
     * @syscap SystemCapability.Notification.Notification
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.notificationManager/notificationManager#removeSlot
     */
    function removeSlot(slotType: SlotType, callback: AsyncCallback<void>): void;
    /**
     * Removes a notification slot of a specified type. This API uses a promise to return the result.
     *
     * @param { SlotType } slotType - Type of the notification slot, which can be used for social communication, service
     *     information, content consultation, and other purposes.
     * @returns { Promise<void> } Promise that returns no value.
     * @syscap SystemCapability.Notification.Notification
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.notificationManager/notificationManager#removeSlot
     */
    function removeSlot(slotType: SlotType): Promise<void>;
    /**
     * Removes all notification slots. This API uses an asynchronous callback to return the result.
     *
     * @param { AsyncCallback<void> } callback - Callback used to return the result.
     * @syscap SystemCapability.Notification.Notification
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.notificationManager/notificationManager#removeAllSlots
     */
    function removeAllSlots(callback: AsyncCallback<void>): void;
    /**
     * Removes all notification slots. This API uses a promise to return the result.
     *
     * @returns { Promise<void> } Promise that returns no value.
     * @syscap SystemCapability.Notification.Notification
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.notificationManager/notificationManager#removeAllSlots
     */
    function removeAllSlots(): Promise<void>;
    /**
     * Enumerates the notification slot types.
     *
     * @syscap SystemCapability.Notification.Notification
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.notificationManager/notificationManager#SlotType
     */
    export enum SlotType {
        /**
         * Unknown type.
         *
         * @syscap SystemCapability.Notification.Notification
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.notificationManager/notificationManager.SlotType#UNKNOWN_TYPE
         */
        UNKNOWN_TYPE = 0,
        /**
         * Notification slot for social communication.
         *
         * @syscap SystemCapability.Notification.Notification
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.notificationManager/notificationManager.SlotType#SOCIAL_COMMUNICATION
         */
        SOCIAL_COMMUNICATION = 1,
        /**
         * Notification slot for service information.
         *
         * @syscap SystemCapability.Notification.Notification
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.notificationManager/notificationManager.SlotType#SERVICE_INFORMATION
         */
        SERVICE_INFORMATION = 2,
        /**
         * Notification slot for content consultation.
         *
         * @syscap SystemCapability.Notification.Notification
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.notificationManager/notificationManager.SlotType#CONTENT_INFORMATION
         */
        CONTENT_INFORMATION = 3,
        /**
         * Notification slot for other purposes.
         *
         * @syscap SystemCapability.Notification.Notification
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.notificationManager/notificationManager.SlotType#OTHER_TYPES
         */
        OTHER_TYPES = 0xFFFF
    }
    /**
     * Enumerates the notification content types.
     *
     * @syscap SystemCapability.Notification.Notification
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.notificationManager/notificationManager.SlotType#ContentType
     */
    export enum ContentType {
        /**
         * Normal text notification.
         *
         * @syscap SystemCapability.Notification.Notification
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.notificationManager/notificationManager.ContentType#NOTIFICATION_CONTENT_BASIC_TEXT
         */
        NOTIFICATION_CONTENT_BASIC_TEXT,
        /**
         * Long text notification.
         *
         * @syscap SystemCapability.Notification.Notification
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.notificationManager/notificationManager.ContentType#NOTIFICATION_CONTENT_LONG_TEXT
         */
        NOTIFICATION_CONTENT_LONG_TEXT,
        /**
         * Picture-attached notification.
         *
         * @syscap SystemCapability.Notification.Notification
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.notificationManager/notificationManager.ContentType#NOTIFICATION_CONTENT_PICTURE
         */
        NOTIFICATION_CONTENT_PICTURE,
        /**
         * Conversation notification.
         *
         * @syscap SystemCapability.Notification.Notification
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.notificationManager/notificationManager.ContentType#NOTIFICATION_CONTENT_CONVERSATION
         */
        NOTIFICATION_CONTENT_CONVERSATION,
        /**
         * Multi-line text notification.
         *
         * @syscap SystemCapability.Notification.Notification
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.notificationManager/notificationManager.ContentType#NOTIFICATION_CONTENT_MULTILINE
         */
        NOTIFICATION_CONTENT_MULTILINE
    }
    /**
     * Enumerates the notification level.
     *
     * @syscap SystemCapability.Notification.Notification
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.notificationManager/notificationManager#SlotLevel
     */
    export enum SlotLevel {
        /**
         * The notification function is disabled.
         *
         * @syscap SystemCapability.Notification.Notification
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.notificationManager/notificationManager.SlotLevel#LEVEL_NONE
         */
        LEVEL_NONE = 0,
        /**
         * The notification function is enabled, but the notification icon is not displayed in the status bar, with no
         * banner or alert tone.
         *
         * @syscap SystemCapability.Notification.Notification
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.notificationManager/notificationManager.SlotLevel#LEVEL_MIN
         */
        LEVEL_MIN = 1,
        /**
         * The notification function is enabled, and the notification icon is displayed in the status bar, with no banner or
         * alert tone.
         *
         * @syscap SystemCapability.Notification.Notification
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.notificationManager/notificationManager.SlotLevel#LEVEL_LOW
         */
        LEVEL_LOW = 2,
        /**
         * The notification feature is enabled, and the notification icon is displayed in the status bar, with an alert tone
         * but no banner.
         *
         * @syscap SystemCapability.Notification.Notification
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.notificationManager/notificationManager.SlotLevel#LEVEL_DEFAULT
         */
        LEVEL_DEFAULT = 3,
        /**
         * The notification feature is enabled, and the notification icon is displayed in the status bar, with an alert tone
         * and banner.
         *
         * @syscap SystemCapability.Notification.Notification
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.notificationManager/notificationManager.SlotLevel#LEVEL_HIGH
         */
        LEVEL_HIGH = 4
    }
    /**
     * Obtains the number of active notifications of this application. This API uses an asynchronous callback to return
     * the result.
     *
     * @param { AsyncCallback<number> } callback - Callback used to return the result.
     * @syscap SystemCapability.Notification.Notification
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.notificationManager/notificationManager#getActiveNotificationCount
     */
    function getActiveNotificationCount(callback: AsyncCallback<number>): void;
    /**
     * Obtains the number of active notifications of this application. This API uses a promise to return the result.
     *
     * @returns { Promise<number> } Promise used to return the result.
     * @syscap SystemCapability.Notification.Notification
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.notificationManager/notificationManager#getActiveNotificationCount
     */
    function getActiveNotificationCount(): Promise<number>;
    /**
     * Obtains active notifications of this application. This API uses an asynchronous callback to return the result.
     *
     * @param { AsyncCallback<Array<NotificationRequest>> } callback - Callback used to return the result.
     * @syscap SystemCapability.Notification.Notification
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.notificationManager/notificationManager#getActiveNotifications
     */
    function getActiveNotifications(callback: AsyncCallback<Array<NotificationRequest>>): void;
    /**
     * Obtains active notifications of this application. This API uses a promise to return the result.
     *
     * @returns { Promise<Array<NotificationRequest>> } Promise used to return the result.
     * @syscap SystemCapability.Notification.Notification
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.notificationManager/notificationManager#getActiveNotifications
     */
    function getActiveNotifications(): Promise<Array<NotificationRequest>>;
    /**
     * Cancels notifications under a notification group of this application. This API uses an asynchronous callback to
     * return the result.
     *
     * @param { string } groupName - Name of the notification group, which is specified through
     *     [NotificationRequest]{@link notification.requestEnableNotification(callback: AsyncCallback<void>)} when the
     *     notification is published.
     * @param { AsyncCallback<void> } callback - Callback used to return the result.
     * @syscap SystemCapability.Notification.Notification
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.notificationManager/notificationManager#cancelGroup
     */
    function cancelGroup(groupName: string, callback: AsyncCallback<void>): void;
    /**
     * Cancels notifications under a notification group of this application. This API uses a promise to return the result.
     *
     * @param { string } groupName - Name of the notification group.
     * @returns { Promise<void> } Promise that returns no value.
     * @syscap SystemCapability.Notification.Notification
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.notificationManager/notificationManager#cancelGroup
     */
    function cancelGroup(groupName: string): Promise<void>;
    /**
     * Checks whether a specified template is supported before using
     * [NotificationTemplate](@link ./notification/notificationTemplate:NotificationTemplate) to publish a notification.
     * This API uses an asynchronous callback to return the result.
     *
     * @param { string } templateName - Template name. Currently, only **downloadTemplate** is supported.
     * @param { AsyncCallback<boolean> } callback - Callback used to return the result.
     * @syscap SystemCapability.Notification.Notification
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.notificationManager/notificationManager#isSupportTemplate
     */
    function isSupportTemplate(templateName: string, callback: AsyncCallback<boolean>): void;
    /**
     * Checks whether a specified template is supported before using
     * [NotificationTemplate](@link ./notification/notificationTemplate:NotificationTemplate) to publish a notification.
     * This API uses a promise to return the result.
     *
     * @param { string } templateName - Template name. Currently, only **downloadTemplate** is supported.
     * @returns { Promise<boolean> } Promise used to return the result.
     * @syscap SystemCapability.Notification.Notification
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.notificationManager/notificationManager#isSupportTemplate
     */
    function isSupportTemplate(templateName: string): Promise<boolean>;
    /**
     * Requests notification to be enabled for this application. This API uses an asynchronous callback to return the
     * result.
     *
     * @param { AsyncCallback<void> } callback - Callback used to return the result.
     * @syscap SystemCapability.Notification.Notification
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.notificationManager/notificationManager#requestEnableNotification
     */
    function requestEnableNotification(callback: AsyncCallback<void>): void;
    /**
     * Requests notification to be enabled for this application. This API uses a promise to return the result.
     *
     * @returns { Promise<void> } Promise that returns no value.
     * @syscap SystemCapability.Notification.Notification
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.notificationManager/notificationManager#requestEnableNotification
     */
    function requestEnableNotification(): Promise<void>;
    /**
     * Checks whether this device supports distributed notifications. This API uses an asynchronous callback to return the
     * result.
     *
     * @param { AsyncCallback<boolean> } callback - Callback used to return the result.
     * @syscap SystemCapability.Notification.Notification
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.notificationManager/notificationManager#isDistributedEnabled
     */
    function isDistributedEnabled(callback: AsyncCallback<boolean>): void;
    /**
     * Checks whether this device supports distributed notifications. This API uses a promise to return the result.
     *
     * @returns { Promise<boolean> } Promise used to return the result.
     * @syscap SystemCapability.Notification.Notification
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.notificationManager/notificationManager#isDistributedEnabled
     */
    function isDistributedEnabled(): Promise<boolean>;
    /**
     * Describes the **BundleOption** information, that is, the bundle information of an application.
     *
     * @syscap SystemCapability.Notification.Notification
     * @since 7
     * @deprecated since 9
     * @useinstead .ohos.notificationManager/notificationManager#BundleOption
     */
    export interface BundleOption {
        /**
         * Bundle information of the application.
         *
         * @syscap SystemCapability.Notification.Notification
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.notificationManager/notificationManager#BundleOption
         */
        bundle: string;
        /**
         * User ID. The default value is 0.
         *
         * @syscap SystemCapability.Notification.Notification
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.notificationManager/notificationManager#BundleOption
         */
        uid?: number;
    }
    /**
     * Notification key.
     *
     * @syscap SystemCapability.Notification.Notification
     * @since 7
     * @deprecated since 9
     */
    export interface NotificationKey {
        /**
         * Notification ID.
         *
         * @syscap SystemCapability.Notification.Notification
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.notificationManager/notificationManager#NotificationKey
         */
        id: number;
        /**
         * Notification label.
         *
         * @syscap SystemCapability.Notification.Notification
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.notificationManager/notificationManager#NotificationKey
         */
        label?: string;
    }
}
export default notification;

```
