# @ohos.notificationManager.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022-2024 Huawei Device Co., Ltd.
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
 * @file
 * @kit NotificationKit
 */
import { BundleOption as _BundleOption } from './notification/NotificationCommonDef';
import { NotificationActionButton as _NotificationActionButton } from './notification/notificationActionButton';
import { NotificationBasicContent as _NotificationBasicContent } from './notification/notificationContent';
import { NotificationContent as _NotificationContent } from './notification/notificationContent';
import { NotificationLongTextContent as _NotificationLongTextContent } from './notification/notificationContent';
import { NotificationMultiLineContent as _NotificationMultiLineContent } from './notification/notificationContent';
import { NotificationPictureContent as _NotificationPictureContent } from './notification/notificationContent';
import { NotificationSystemLiveViewContent as _NotificationSystemLiveViewContent } from './notification/notificationContent';
import { NotificationCapsule as _NotificationCapsule } from './notification/notificationContent';
import { NotificationButton as _NotificationButton } from './notification/notificationContent';
import { NotificationTime as _NotificationTime } from './notification/notificationContent';
import { NotificationProgress as _NotificationProgress } from './notification/notificationContent';
import { NotificationRequest as _NotificationRequest } from './notification/notificationRequest';
import { DistributedOptions as _DistributedOptions } from './notification/notificationRequest';
import { NotificationSlot as _NotificationSlot } from './notification/notificationSlot';
import { NotificationTemplate as _NotificationTemplate } from './notification/notificationTemplate';
import { NotificationUserInput as _NotificationUserInput } from './notification/notificationUserInput';
import { NotificationParameters as _NotificationParameters } from './notification/notificationRequest';
import { AsyncCallback } from './@ohos.base';
import type UIAbilityContext from './application/UIAbilityContext';
/**
 * This module provides notification management capabilities, allowing applications to manage the complete lifecycle
 * of notifications. This includes operations such as publishing, updating, and canceling notifications, creating and
 * querying notification slots, querying and requesting authorization status for notification capabilities, setting
 * application badges, and querying stored notifications in the notification center.
 *
 * **APIs used in combination**:
 *
 * The APIs of this module follow the following workflow of notifications: Authorization → Publishing → Cancellation →
 * Channel Management. The APIs are designed to be used in combination with one another.
 *
 * 1. **Authorization query and request process**: Before publishing a notification, first query the authorization
 * status of the notification capability through **isNotificationEnabled**. If the notification capability is not
 * authorized, guide the user to enable the notification permission through **requestEnableNotification**.
 *
 * 2. **Notification publish and update process**: Publish a notification via the **publish** method, with the
 * notification content specified through **NotificationRequest**. If a newly published notification has the same ID
 * and tag as an existing one, the existing notification will be automatically updated. If the ID or tag differs, a
 * new notification will be created instead.
 *
 * 3. **Notification cancellation process**: Cancel a notification with a specified ID through **cancel**, cancel all
 * notifications of this application through **cancelAll**, and cancel notifications under a specified group through
 * **cancelGroup**.
 *
 * 4. **Notification slot management process**: Create a notification slot through **addSlot**, query notification slot
 * configurations through **getSlot** / **getSlots**, and delete notification slots through
 * **removeSlot** / **removeAllSlots**. It is recommended to create the corresponding type of notification slot before
 * publishing a notification. In addition to using **addSlot** to create a notification slot, you can also carry the
 * **notificationSlotType** field in the NotificationRequest when publishing a notification. If a slot of the
 * corresponding type does not exist, it will be automatically created.
 *
 * 5. **Badge management process**: Set the badge number through **setBadgeNumber**, or when publishing a notification
 * through the **publish** API, carry the number of badges to be incremented in the **badgeNumber** field of
 * NotificationRequest.
 *
 * 6. **Stored notification query process**: Obtain the number of stored notifications for this application in the
 * notification center through **getActiveNotificationCount**, and obtain the details of stored notifications for this
 * application in the notification center through **getActiveNotifications**.
 *
 * @syscap SystemCapability.Notification.Notification
 * @crossplatform [since 12]
 * @atomicservice [since 12]
 * @since 9
 */
declare namespace notificationManager {
    /**
     * Publishes a notification. This API uses an asynchronous callback to return the result.
     *
     * After a notification is published, it will be displayed as a notification widget in the device's
     * notification center, status bar, etc. If the ID and tag of the newly published notification are the
     * same as those of an already published notification, the new notification will replace the original
     * one, achieving a notification update effect.
     *
     * @param { NotificationRequest } request - Content and related configuration of the notification to publish.
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
     *     **err** is **undefined**; otherwise, **err** is an error object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 1600001 - Internal error.
     * @throws { BusinessError } 1600002 - Marshalling or unmarshalling error.
     * @throws { BusinessError } 1600003 - Failed to connect to the service.
     * @throws { BusinessError } 1600004 - Notification disabled.
     * @throws { BusinessError } 1600005 - Notification slot disabled.
     * @throws { BusinessError } 1600007 - The notification does not exist. [since 11]
     * @throws { BusinessError } 1600009 - The notification sending frequency reaches the upper limit.
     * @throws { BusinessError } 1600012 - No memory space.
     * @throws { BusinessError } 1600014 - No permission. [since 11]
     * @throws { BusinessError } 1600015 - The current notification status does not support duplicate
     *     configurations. [since 11]
     * @throws { BusinessError } 1600016 - The notification version for this update is too low. [since 11]
     * @throws { BusinessError } 1600020 - The application is not allowed to send notifications due to permission
     *     settings. [since 12]
     * @throws { BusinessError } 1600029 - The system failed to find the ExtensionAbility instance for the
     *     custom Live View widget template. [since 26.0.0]
     * @throws { BusinessError } 2300007 - Network unreachable. [since 11]
     * @syscap SystemCapability.Notification.Notification
     * @crossplatform [since 12]
     * @since 9
     */
    function publish(request: NotificationRequest, callback: AsyncCallback<void>): void;
    /**
     * Publishes a notification. This API uses a promise to return the result.
     *
     * After a notification is published, it will be displayed as a notification card in the device's notification
     * center, status bar, and other locations. If the ID and tag of the newly published notification are the same
     * as those of an already published notification, the new notification will replace the original one, achieving
     * a notification update effect.
     *
     * @param { NotificationRequest } request - Content and related configuration of the notification to publish.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 1600001 - Internal error.
     * @throws { BusinessError } 1600002 - Marshalling or unmarshalling error.
     * @throws { BusinessError } 1600003 - Failed to connect to the service.
     * @throws { BusinessError } 1600004 - Notification disabled.
     * @throws { BusinessError } 1600005 - Notification slot disabled.
     * @throws { BusinessError } 1600007 - The notification does not exist. [since 11]
     * @throws { BusinessError } 1600009 - The notification sending frequency reaches the upper limit.
     * @throws { BusinessError } 1600012 - No memory space.
     * @throws { BusinessError } 1600014 - No permission. [since 11]
     * @throws { BusinessError } 1600015 - The current notification status does not support duplicate
     *     configurations. [since 11]
     * @throws { BusinessError } 1600016 - The notification version for this update is too low. [since 11]
     * @throws { BusinessError } 1600020 - The application is not allowed to send notifications due to permission
     *     settings. [since 12]
     * @throws { BusinessError } 1600029 - The system failed to find the ExtensionAbility instance for the
     *     custom Live View widget template. [since 26.0.0]
     * @throws { BusinessError } 2300007 - Network unreachable. [since 11]
     * @syscap SystemCapability.Notification.Notification
     * @crossplatform [since 12]
     * @since 9
     */
    function publish(request: NotificationRequest): Promise<void>;
    /**
     * Cancels a notification with the specified ID. This API uses an asynchronous callback to return the result.
     *
     * After cancellation, the corresponding notification will be removed from the notification center, status
     * bar, etc., and will no longer be visible to the user.
     *
     * Compared with notificationManager.cancel(id, label, callback), which includes the label parameter,
     * this API does not pass in a label and will cancel the notification matching the specified ID.
     * When a notification is published with a non-empty label, the
     * `notificationManager.cancel(id, label, callback)` API must be used to cancel it.
     *
     * @param { number } id - Notification ID, used to identify the target notification. This value is
     *     specified by the **id** field of NotificationRequest when a notification is published.
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
     *     **err** is **undefined**; otherwise, **err** is an error object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 1600001 - Internal error.
     * @throws { BusinessError } 1600002 - Marshalling or unmarshalling error.
     * @throws { BusinessError } 1600003 - Failed to connect to the service.
     * @throws { BusinessError } 1600007 - The notification does not exist.
     * @syscap SystemCapability.Notification.Notification
     * @crossplatform [since 12]
     * @since 9
     */
    function cancel(id: number, callback: AsyncCallback<void>): void;
    /**
     * Cancels a published notification based on the notification ID and label. This API uses an asynchronous callback to
     * return the result.
     *
     * After cancellation, the corresponding notification will be removed from the notification center, status
     * bar, and other locations, and will no longer be visible to the user. This is suitable for scenarios
     * where a specific notification with a particular tag needs to be precisely canceled.
     *
     * Compared with notificationManager.cancel(id, callback), which requires only the notification ID, this
     * API additionally has the **label** parameter, allowing precise cancellation of notifications with the
     * same ID but different labels.
     *
     * @param { number } id - Notification ID, used to identify the target notification. This value is
     *     specified by the **id** field of NotificationRequest when a notification is published.
     * @param { string } label - Notification label. This value is specified by the **label** field of
     *     NotificationRequest during the notification publishment. If the **label** field is empty, the
     *     published notification that matches the specified notification ID and has an empty label is
     *     canceled. If the **label** field is not empty, the published notification that matches both the
     *     specified notification ID and label is canceled.
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
     *     **err** is **undefined**; otherwise, **err** is an error object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 1600001 - Internal error.
     * @throws { BusinessError } 1600002 - Marshalling or unmarshalling error.
     * @throws { BusinessError } 1600003 - Failed to connect to the service.
     * @throws { BusinessError } 1600007 - The notification does not exist.
     * @syscap SystemCapability.Notification.Notification
     * @since 9
     */
    function cancel(id: number, label: string, callback: AsyncCallback<void>): void;
    /**
     * Cancels a published notification based on the notification ID and label. This API uses a promise to
     * return the result.
     *
     * After cancellation, the corresponding notification will be removed from the notification center, status
     * bar, and other locations, and will no longer be visible to the user.
     *
     * @param { number } id - Notification ID, used to identify the target notification. This value is
     *     specified by the id field of NotificationRequest when publishing a notification.
     * @param { string } [label] - Notification label. The default value is empty. This value is specified
     *     by the **label** field of NotificationRequest during the notification publishment. If the
     *     **label** field is empty, the published notification that matches the specified notification ID
     *     and has an empty label is canceled. If the **label** field is not empty, the published
     *     notification that matches both the specified notification ID and label is canceled.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 1600001 - Internal error.
     * @throws { BusinessError } 1600002 - Marshalling or unmarshalling error.
     * @throws { BusinessError } 1600003 - Failed to connect to the service.
     * @throws { BusinessError } 1600007 - The notification does not exist.
     * @syscap SystemCapability.Notification.Notification
     * @since 9
     */
    function cancel(id: number, label?: string): Promise<void>;
    /**
     * Cancels all notifications of this application. This API uses an asynchronous callback to return the result.
     *
     * After cancellation, all notifications of the current application will be removed from the notification
     * center, status bar, and other locations, and will no longer be visible to the user. This is
     * suitable for scenarios such as application exit or when the user manually clears all notifications.
     *
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
     *     **err** is **undefined**; otherwise, **err** is an error object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 1600001 - Internal error.
     * @throws { BusinessError } 1600002 - Marshalling or unmarshalling error.
     * @throws { BusinessError } 1600003 - Failed to connect to the service.
     * @syscap SystemCapability.Notification.Notification
     * @crossplatform [since 12]
     * @since 9
     */
    function cancelAll(callback: AsyncCallback<void>): void;
    /**
     * Cancels all notifications of this application. This API uses a promise to return the result.
     *
     * After cancellation, all notifications of the current application will be removed from the notification
     * center, status bar, and other locations, and will no longer be visible to the user. This is
     * suitable for scenarios such as application exit or when the user manually clears all notifications.
     *
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 1600001 - Internal error.
     * @throws { BusinessError } 1600002 - Marshalling or unmarshalling error.
     * @throws { BusinessError } 1600003 - Failed to connect to the service.
     * @syscap SystemCapability.Notification.Notification
     * @crossplatform [since 12]
     * @since 9
     */
    function cancelAll(): Promise<void>;
    /**
     * Adds a notification slot of a specified type. This API uses an asynchronous callback to return the result.
     *
     * The notification slot NotificationSlot defines the reminder type (such as alert sound, vibration, and
     * banner) and level of a notification. Before publishing a notification, the application needs to
     * create a corresponding type of notification slot first, or the system will automatically create a
     * corresponding type of notification slot when the notification is published. Only one notification
     * slot of the same type can be created.
     *
     * @param { SlotType } type - Notification slot type to create. Different slot types correspond to
     *     different default SlotLevel values, which affect the notification alert method. For example,
     *     **SOCIAL_COMMUNICATION** corresponds to **LEVEL_HIGH** (status bar icon + banner + sound), and
     *     **CONTENT_INFORMATION** corresponds to **LEVEL_MIN** (no status bar icon + no banner + no sound).
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
     *     **err** is **undefined**; otherwise, **err** is an error object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 1600001 - Internal error.
     * @throws { BusinessError } 1600002 - Marshalling or unmarshalling error.
     * @throws { BusinessError } 1600003 - Failed to connect to the service.
     * @throws { BusinessError } 1600012 - No memory space.
     * @syscap SystemCapability.Notification.Notification
     * @since 9
     */
    function addSlot(type: SlotType, callback: AsyncCallback<void>): void;
    /**
     * Adds a notification slot of a specified type. This API uses a promise to return the result.
     *
     * The notification slot NotificationSlot defines the reminder type (such as alert sound, vibration, and
     * banner) and level of a notification. Before publishing a notification, the application needs to
     * create a corresponding type of notification slot first, or the system will automatically create a
     * corresponding type of notification slot when the notification is published. Only one notification
     * slot of the same type can be created.
     *
     * @param { SlotType } type - Notification slot type to create. Different slot types correspond to
     *     different default SlotLevel values, which affect the notification alert method. For example,
     *     **SOCIAL_COMMUNICATION** corresponds to **LEVEL_HIGH** (status bar icon + banner + sound), and
     *     **CONTENT_INFORMATION** corresponds to **LEVEL_MIN** (no status bar icon + no banner + no sound).
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 1600001 - Internal error.
     * @throws { BusinessError } 1600002 - Marshalling or unmarshalling error.
     * @throws { BusinessError } 1600003 - Failed to connect to the service.
     * @throws { BusinessError } 1600012 - No memory space.
     * @syscap SystemCapability.Notification.Notification
     * @since 9
     */
    function addSlot(type: SlotType): Promise<void>;
    /**
     * Obtains a notification slot of a specified type. This API uses an asynchronous callback to return the result.
     *
     * This API is used to query the detailed configuration information of a created notification slot,
     * including settings such as reminder method, level, and lock screen display. A corresponding type
     * of notification slot must be created first through addSlot, otherwise the obtained result will be
     * empty.
     *
     * @param { SlotType } slotType - Notification slot type, such as social communication, service reminder,
     *     and content consultation.
     * @param { AsyncCallback<NotificationSlot> } callback - Callback used to return the result. If the
     *     notification slot is obtained successfully, **err** is **undefined** and **data** is the obtained
     *     **NotificationSlot**; otherwise, **err** is an error object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 1600001 - Internal error.
     * @throws { BusinessError } 1600002 - Marshalling or unmarshalling error.
     * @throws { BusinessError } 1600003 - Failed to connect to the service.
     * @syscap SystemCapability.Notification.Notification
     * @since 9
     */
    function getSlot(slotType: SlotType, callback: AsyncCallback<NotificationSlot>): void;
    /**
     * Obtains a notification slot of a specified type. This API uses a promise to return the result.
     *
     * This API is used to query the detailed configuration information of a created notification slot,
     * including settings such as reminder method, level, and lock screen display. A corresponding type
     * of notification slot must be created first through addSlot, otherwise the obtained result will be
     * empty.
     *
     * @param { SlotType } slotType - Notification slot type, such as social communication, service reminder,
     *     and content consultation.
     * @returns { Promise<NotificationSlot> } Promise used to return the result.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 1600001 - Internal error.
     * @throws { BusinessError } 1600002 - Marshalling or unmarshalling error.
     * @throws { BusinessError } 1600003 - Failed to connect to the service.
     * @syscap SystemCapability.Notification.Notification
     * @since 9
     */
    function getSlot(slotType: SlotType): Promise<NotificationSlot>;
    /**
     * Obtains all notification slots of this application. This API uses an asynchronous callback to return the result.
     *
     * This API is used to batch query the configuration information of all notification slots created by the
     * current application, including settings such as the type, reminder method, and level of each slot.
     * This is suitable for scenarios where all slot configurations need to be viewed. The corresponding
     * notification slots must be created through addSlot first; otherwise, the obtained result will be empty.
     *
     * @param { AsyncCallback<Array<NotificationSlot>> } callback - Callback used to return the result. If
     *     the notification slots are obtained successfully, **err** is **undefined** and **data** is the
     *     obtained **NotificationSlot** array. Otherwise, **err** is an error object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 1600001 - Internal error.
     * @throws { BusinessError } 1600002 - Marshalling or unmarshalling error.
     * @throws { BusinessError } 1600003 - Failed to connect to the service.
     * @syscap SystemCapability.Notification.Notification
     * @since 9
     */
    function getSlots(callback: AsyncCallback<Array<NotificationSlot>>): void;
    /**
     * Obtains all notification slots of this application. This API uses a promise to return the result.
     *
     * This API is used to batch query the configuration information of all notification slots created by the
     * current application, including settings such as the type, reminder method, and level of each slot.
     * This is suitable for scenarios where all slot configurations need to be viewed. The corresponding
     * notification slots must be created through addSlot first; otherwise, the obtained result will be empty.
     *
     * @returns { Promise<Array<NotificationSlot>> } Promise used to return the result.
     * @throws { BusinessError } 1600001 - Internal error.
     * @throws { BusinessError } 1600002 - Marshalling or unmarshalling error.
     * @throws { BusinessError } 1600003 - Failed to connect to the service.
     * @syscap SystemCapability.Notification.Notification
     * @since 9
     */
    function getSlots(): Promise<Array<NotificationSlot>>;
    /**
     * Removes a notification slot of a specified type for this application. This API uses an asynchronous
     * callback to return the result.
     *
     * After deletion, the corresponding type of notification slot and its configuration will be permanently
     * removed. When a notification of this type is published subsequently, the system will automatically
     * create a default slot. Notifications already published through this slot are not affected and can
     * still be viewed in the notification center. This is suitable for scenarios where a slot needs to be
     * deleted and then recreated for reconfiguration.
     *
     * @param { SlotType } slotType - Notification slot type, such as social communication, service reminder,
     *     and content consultation. The created slot type must be passed in; otherwise, the deletion
     *     operation is invalid.
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
     *     **err** is **undefined**; otherwise, **err** is an error object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 1600001 - Internal error.
     * @throws { BusinessError } 1600002 - Marshalling or unmarshalling error.
     * @throws { BusinessError } 1600003 - Failed to connect to the service.
     * @syscap SystemCapability.Notification.Notification
     * @since 9
     */
    function removeSlot(slotType: SlotType, callback: AsyncCallback<void>): void;
    /**
     * Removes a notification slot of a specified type for this application. This API uses a promise to return the result.
     *
     * After deletion, the corresponding notification slot and its configuration will be permanently removed.
     * When a notification of this type is published subsequently, the system will automatically create a
     * default slot. Notifications already published through this slot are not affected and can still be
     * viewed in the notification center. This is suitable for scenarios where a slot needs to be deleted
     * and then recreated for reconfiguration.
     *
     * @param { SlotType } slotType - Notification slot type, such as social communication, service reminder,
     *     and content consultation. The created slot type must be passed in; otherwise, the deletion
     *     operation is invalid.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 1600001 - Internal error.
     * @throws { BusinessError } 1600002 - Marshalling or unmarshalling error.
     * @throws { BusinessError } 1600003 - Failed to connect to the service.
     * @syscap SystemCapability.Notification.Notification
     * @since 9
     */
    function removeSlot(slotType: SlotType): Promise<void>;
    /**
     * Removes all notification slots for this application. This API uses an asynchronous callback to return the result.
     *
     * After deletion, all notification slots and their configurations of the current application will be
     * permanently removed. When notifications are published subsequently, the system will automatically
     * create slots of the corresponding types. Notifications already published through these slots are
     * not affected and can still be viewed in the notification center. This is suitable for scenarios
     * where all slot configurations need to be cleared at once.
     *
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
     *     **err** is **undefined**; otherwise, **err** is an error object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 1600001 - Internal error.
     * @throws { BusinessError } 1600002 - Marshalling or unmarshalling error.
     * @throws { BusinessError } 1600003 - Failed to connect to the service.
     * @syscap SystemCapability.Notification.Notification
     * @since 9
     */
    function removeAllSlots(callback: AsyncCallback<void>): void;
    /**
     * Removes all notification slots for this application. This API uses a promise to return the result.
     *
     * After deletion, all notification slots and their configurations of the current application will be
     * permanently removed. When notifications are published subsequently, the system will automatically
     * create slots of the corresponding types. Notifications already published through these slots are
     * not affected and can still be viewed in the notification center. This is suitable for scenarios
     * where all slot configurations need to be cleared at once.
     *
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 1600001 - Internal error.
     * @throws { BusinessError } 1600002 - Marshalling or unmarshalling error.
     * @throws { BusinessError } 1600003 - Failed to connect to the service.
     * @syscap SystemCapability.Notification.Notification
     * @since 9
     */
    function removeAllSlots(): Promise<void>;
    /**
     * Queries the notification authorization status of the current application. This API uses an asynchronous
     * callback to return the result.
     *
     * This API is used to check whether the current application is allowed to send notifications before
     * publishing, preventing publish failures when notification authorization is disabled.
     *
     * @param { AsyncCallback<boolean> } callback - Callback used to return the result. The value **true** means that the
     *     notification can be published; **false** means the opposite. If this API call fails, an error object is
     *     returned.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 1600001 - Internal error.
     * @throws { BusinessError } 1600002 - Marshalling or unmarshalling error.
     * @throws { BusinessError } 1600003 - Failed to connect to the service.
     * @throws { BusinessError } 1600008 - The user does not exist.
     * @throws { BusinessError } 17700001 - The specified bundle name was not found.
     * @syscap SystemCapability.Notification.Notification
     * @crossplatform [since 12]
     * @since 11
     */
    function isNotificationEnabled(callback: AsyncCallback<boolean>): void;
    /**
     * Queries the notification authorization status of the current application. This API uses a promise to
     * return the result.
     *
     * This API is used to check whether the current application is allowed to send notifications before
     * publishing, preventing publish failures when notification authorization is disabled.
     *
     * @returns { Promise<boolean> } Promise used to return the result. The value **true** means that the notification is
     *     enabled, and **false** means the opposite.
     * @throws { BusinessError } 1600001 - Internal error.
     * @throws { BusinessError } 1600002 - Marshalling or unmarshalling error.
     * @throws { BusinessError } 1600003 - Failed to connect to the service.
     * @throws { BusinessError } 1600008 - The user does not exist.
     * @throws { BusinessError } 17700001 - The specified bundle name was not found.
     * @syscap SystemCapability.Notification.Notification
     * @crossplatform [since 12]
     * @since 11
     */
    function isNotificationEnabled(): Promise<boolean>;
    /**
     * Synchronously queries the notification authorization status of the current application.
     *
     * This API is used to quickly check whether the current application is allowed to send notifications
     * before publishing. It is synchronous and returns the result immediately after being called,
     * suitable for scenarios where the enabled status needs to be obtained in a synchronous code flow.
     *
     * @returns { boolean } Result of the notification enabling status. The value **true** means that the notification is
     *     enabled, and **false** means the opposite.
     * @throws { BusinessError } 1600001 - Internal error.
     * @throws { BusinessError } 1600002 - Marshalling or unmarshalling error.
     * @throws { BusinessError } 1600003 - Failed to connect to the service.
     * @syscap SystemCapability.Notification.Notification
     * @since 12
     */
    function isNotificationEnabledSync(): boolean;
    /**
     * Obtains the number of active notifications of this application. This API uses an asynchronous callback to return
     * the result.
     *
     * This API is used to query the number of active notifications published by the current application in the
     * notification center. This is suitable for scenarios where an unread notification count prompt needs to be
     * displayed.
     *
     * @param { AsyncCallback<number> } callback - Callback used to return the result. If the operation is successful,
     *     **err** is **undefined** and data is the obtained number of active notifications; otherwise, **err** is an
     *     error object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 1600001 - Internal error.
     * @throws { BusinessError } 1600002 - Marshalling or unmarshalling error.
     * @throws { BusinessError } 1600003 - Failed to connect to the service.
     * @syscap SystemCapability.Notification.Notification
     * @since 9
     */
    function getActiveNotificationCount(callback: AsyncCallback<number>): void;
    /**
     * Obtains the number of active notifications of this application. This API uses a promise to return the result.
     *
     * This API is used to query the number of active notifications published by the current application in the
     * notification center. This is suitable for scenarios where an unread notification count prompt needs to be
     * displayed.
     *
     * @returns { Promise<number> } Promise used to return the result.
     * @throws { BusinessError } 1600001 - Internal error.
     * @throws { BusinessError } 1600002 - Marshalling or unmarshalling error.
     * @throws { BusinessError } 1600003 - Failed to connect to the service.
     * @syscap SystemCapability.Notification.Notification
     * @since 9
     */
    function getActiveNotificationCount(): Promise<number>;
    /**
     * Obtains the active notifications of this application. This API uses an asynchronous callback to return the result.
     *
     * This API is used to query the detailed information list of all stored notifications of the current application in
     * the notification center, including the ID, tag, content, and creation time of each notification.
     *
     * @param { AsyncCallback<Array<NotificationRequest>> } callback - Callback used to return the result. If the
     *     operation is successful, **err** is **undefined** and data is the obtained **NotificationRequest** array;
     *     otherwise, **err** is an error object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 1600001 - Internal error.
     * @throws { BusinessError } 1600002 - Marshalling or unmarshalling error.
     * @throws { BusinessError } 1600003 - Failed to connect to the service.
     * @syscap SystemCapability.Notification.Notification
     * @since 9
     */
    function getActiveNotifications(callback: AsyncCallback<Array<NotificationRequest>>): void;
    /**
     * Obtains the active notifications of this application. This API uses a promise to return the result.
     *
     * This API is used to query the detailed information list of all stored notifications of the current application in
     * the notification center, including the ID, tag, content, and creation time of each notification.
     *
     * @returns { Promise<Array<NotificationRequest>> } Promise used to return the result.
     * @throws { BusinessError } 1600001 - Internal error.
     * @throws { BusinessError } 1600002 - Marshalling or unmarshalling error.
     * @throws { BusinessError } 1600003 - Failed to connect to the service.
     * @syscap SystemCapability.Notification.Notification
     * @since 9
     */
    function getActiveNotifications(): Promise<Array<NotificationRequest>>;
    /**
     * Obtains some information about the **wantAgent** field in
     * [NotificationRequest]{@link ./notification/notificationRequest:NotificationRequest}. This API uses a promise to
     * return the result.
     *
     * @param { number } id - Notification ID, used to identify the target notification. This value is specified by the
     *     **id** field of NotificationRequest when a notification is published.
     * @param { string } [label] - Notification label. This parameter is left empty by default.
     * @returns { Promise<NotificationParameters> } Promise used to return some information about **wantAgent**.
     * @throws { BusinessError } 1600001 - Internal error.
     * @throws { BusinessError } 1600002 - Marshalling or unmarshalling error.
     * @throws { BusinessError } 1600003 - Failed to connect to the service.
     * @throws { BusinessError } 1600007 - The notification does not exist.
     * @syscap SystemCapability.Notification.Notification
     * @stagemodelonly
     * @since 24
     */
    function getNotificationParameters(id: number, label?: string): Promise<NotificationParameters>;
    /**
     * Cancels notifications under a notification group of this application. This API uses an asynchronous callback to
     * return the result.
     *
     * The notification group **groupName** is the group identifier specified through the **groupName** field of
     * NotificationRequest when a notification is published. After cancellation, all notifications under this group
     * will be removed from the notification center. This is suitable for scenarios where notifications need to be
     * canceled in batches by service group.
     *
     * @param { string } groupName - Name of the notification group, which is specified through
     *     [NotificationRequest]{@link ./notification/notificationRequest:NotificationRequest} when the notification is
     *     published.
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
     *     **err** is **undefined**; otherwise, **err** is an error object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 1600001 - Internal error.
     * @throws { BusinessError } 1600002 - Marshalling or unmarshalling error.
     * @throws { BusinessError } 1600003 - Failed to connect to the service.
     * @syscap SystemCapability.Notification.Notification
     * @since 9
     */
    function cancelGroup(groupName: string, callback: AsyncCallback<void>): void;
    /**
     * Cancels notifications under a notification group of this application. This API uses a promise to return the result.
     *
     * The notification group **groupName** is the group identifier specified through the **groupName** field of
     * NotificationRequest when a notification is published. After cancellation, all notifications under this group
     * will be removed from the notification center. This is suitable for scenarios where notifications need to be
     * canceled in batches by service group.
     *
     * @param { string } groupName - Name of the notification group, which is specified through
     *     [NotificationRequest]{@link ./notification/notificationRequest:NotificationRequest} when the notification is
     *     published.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 1600001 - Internal error.
     * @throws { BusinessError } 1600002 - Marshalling or unmarshalling error.
     * @throws { BusinessError } 1600003 - Failed to connect to the service.
     * @syscap SystemCapability.Notification.Notification
     * @since 9
     */
    function cancelGroup(groupName: string): Promise<void>;
    /**
     * Checks whether a specified template is supported before using
     * [NotificationTemplate]{@link ./notification/notificationTemplate:NotificationTemplate} to publish a notification.
     * This API uses an asynchronous callback to return the result.
     *
     * @param { string } templateName - Template name. Currently, only **downloadTemplate** is supported.
     * @param { AsyncCallback<boolean> } callback - Callback used to return the result. The value **true** indicates that
     *     the template is supported, and **false** indicates the opposite. If this API call fails, an error object is
     *     returned.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 1600001 - Internal error.
     * @throws { BusinessError } 1600002 - Marshalling or unmarshalling error.
     * @throws { BusinessError } 1600003 - Failed to connect to the service.
     * @syscap SystemCapability.Notification.Notification
     * @since 9
     */
    function isSupportTemplate(templateName: string, callback: AsyncCallback<boolean>): void;
    /**
     * Checks whether a specified template is supported before using
     * [NotificationTemplate]{@link ./notification/notificationTemplate:NotificationTemplate} to publish a notification.
     * This API uses a promise to return the result.
     *
     * @param { string } templateName - Template name. Currently, only **downloadTemplate** is supported.
     * @returns { Promise<boolean> } Promise used to return the result. The value **true** means that the specified
     *     template is supported, and **false** means the opposite.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 1600001 - Internal error.
     * @throws { BusinessError } 1600002 - Marshalling or unmarshalling error.
     * @throws { BusinessError } 1600003 - Failed to connect to the service.
     * @syscap SystemCapability.Notification.Notification
     * @since 9
     */
    function isSupportTemplate(templateName: string): Promise<boolean>;
    /**
     * Requests notification to be enabled for this application. This API uses an asynchronous callback to return the
     * result.
     *
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
     *     **err** is **undefined**; otherwise, **err** is an error object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 1600001 - Internal error.
     * @throws { BusinessError } 1600002 - Marshalling or unmarshalling error.
     * @throws { BusinessError } 1600003 - Failed to connect to the service.
     * @throws { BusinessError } 1600004 - Notification disabled. [since 11]
     * @throws { BusinessError } 1600013 - A notification dialog box is already displayed. [since 11]
     * @syscap SystemCapability.Notification.Notification
     * @crossplatform [since 12]
     * @since 9
     * @deprecated since 12
     * @useinstead requestEnableNotification
     */
    function requestEnableNotification(callback: AsyncCallback<void>): void;
    /**
     * Requests notification to be enabled for this application. You can call this API to display a dialog box prompting
     * the user to enable notification for your application before publishing a notification. This API uses an
     * asynchronous callback to return the result.
     *
     * > **NOTE**
     * >
     * > - This API can be called only after the application UI is loaded (that is,
     * > [loadContent]{@link @ohos.app.ability.UIExtensionContentSession:UIExtensionContentSession.loadContent} is
     * > successfully called).
     * >
     * > - When an application uses **requestEnableNotification()** to display a dialog box for notification authorization
     * > and the user rejects the authorization, the application cannot use this API to open the dialog box again. However
     * > , it can call [openNotificationSettingsWithResult]{@link notificationManager.openNotificationSettingsWithResult}
     * > to open the notification management dialog box.
     *
     * @param { UIAbilityContext } context - Ability context bound to the notification dialog box.
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
     *     **err** is **undefined**; otherwise, **err** is an error object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 1600001 - Internal error.
     * @throws { BusinessError } 1600002 - Marshalling or unmarshalling error.
     * @throws { BusinessError } 1600003 - Failed to connect to the service.
     * @throws { BusinessError } 1600004 - Notification disabled. [since 11]
     * @throws { BusinessError } 1600013 - A notification dialog box is already displayed. [since 11]
     * @syscap SystemCapability.Notification.Notification
     * @StageModelOnly
     * @crossplatform [since 12]
     * @since 10
     */
    function requestEnableNotification(context: UIAbilityContext, callback: AsyncCallback<void>): void;
    /**
     * Requests notification to be enabled for this application. This API uses a promise to return the result.
     *
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 1600001 - Internal error.
     * @throws { BusinessError } 1600002 - Marshalling or unmarshalling error.
     * @throws { BusinessError } 1600003 - Failed to connect to the service.
     * @throws { BusinessError } 1600004 - Notification disabled. [since 11]
     * @throws { BusinessError } 1600013 - A notification dialog box is already displayed. [since 11]
     * @syscap SystemCapability.Notification.Notification
     * @crossplatform [since 12]
     * @since 9
     * @deprecated since 12
     * @useinstead requestEnableNotification
     */
    function requestEnableNotification(): Promise<void>;
    /**
     * Requests notification to be enabled for this application. You can call this API to display a dialog box prompting
     * the user to enable notification for your application before publishing a notification. This API uses a promise to
     * return the result.
     *
     * > **NOTE**
     * >
     * > - This API can be called only after the application UI is loaded (that is,
     * > [loadContent]{@link @ohos.app.ability.UIExtensionContentSession:UIExtensionContentSession.loadContent} is
     * > successfully called).
     * >
     * > - When an application uses **requestEnableNotification()** to display a dialog box for notification authorization
     * > and the user rejects the authorization, the application cannot use this API to open the dialog box again. However
     * > , it can call [openNotificationSettingsWithResult]{@link notificationManager.openNotificationSettingsWithResult}
     * > to open the notification management dialog box.
     *
     * @param { UIAbilityContext } context - Ability context bound to the notification dialog box.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 1600001 - Internal error.
     * @throws { BusinessError } 1600002 - Marshalling or unmarshalling error.
     * @throws { BusinessError } 1600003 - Failed to connect to the service.
     * @throws { BusinessError } 1600004 - Notification disabled. [since 11]
     * @throws { BusinessError } 1600013 - A notification dialog box is already displayed. [since 11]
     * @syscap SystemCapability.Notification.Notification
     * @StageModelOnly
     * @crossplatform [since 12]
     * @since 10
     */
    function requestEnableNotification(context: UIAbilityContext): Promise<void>;
    /**
     * Checks whether the device supports cross-device notifications. This API uses an asynchronous callback to return the
     * result.
     *
     * @param { AsyncCallback<boolean> } callback - Callback used to return the result. The value **true** means that the
     *     cross-device notification is supported; **false** means the opposite. If this API call fails, an error object
     *     is returned.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported. [since 26.0.0]
     * @throws { BusinessError } 1600001 - Internal error.
     * @throws { BusinessError } 1600002 - Marshalling or unmarshalling error.
     * @throws { BusinessError } 1600003 - Failed to connect to the service.
     * @throws { BusinessError } 1600010 - Distributed operation failed.
     * @syscap SystemCapability.Notification.Notification
     * @since 9
     * @deprecated since 26.0.0
     */
    function isDistributedEnabled(callback: AsyncCallback<boolean>): void;
    /**
     * Checks whether the device supports cross-device notifications. This API uses a promise to return the result.
     *
     * @returns { Promise<boolean> } Promise used to return the result. The value **true** means that the cross-device
     *     notification is supported; **false** means the opposite.
     * @throws { BusinessError } 801 - Capability not supported. [since 26.0.0]
     * @throws { BusinessError } 1600001 - Internal error.
     * @throws { BusinessError } 1600002 - Marshalling or unmarshalling error.
     * @throws { BusinessError } 1600003 - Failed to connect to the service.
     * @throws { BusinessError } 1600010 - Distributed operation failed.
     * @syscap SystemCapability.Notification.Notification
     * @since 9
     * @deprecated since 26.0.0
     */
    function isDistributedEnabled(): Promise<boolean>;
    /**
     * Sets the notification badge number. This API uses an asynchronous callback to return the result.
     *
     * A badge is a numeric identifier displayed in the upper right corner of an application's desktop icon, used to
     * prompt the user about the number of unprocessed notifications. After setting, the desktop icon will display the
     * corresponding badge number. This is suitable for scenarios where the number of pending messages needs to be
     * prompted on the desktop icon, such as the number of unread messages and to-do items.
     *
     * This API can be properly called on devices other than wearables. If it is called on wearables, error code 801 is
     * returned.
     *
     * @param { number } badgeNumber - Notification badge number to set. If **badgeNumber** is set to a value less than or
     *     equal to **0**, badges are cleared; if the value is greater than **99**, **99+** is displayed on the badge.
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
     *     **err** is **undefined**; otherwise, **err** is an error object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported. [since 18]
     * @throws { BusinessError } 1600001 - Internal error.
     * @throws { BusinessError } 1600002 - Marshalling or unmarshalling error.
     * @throws { BusinessError } 1600003 - Failed to connect to the service.
     * @throws { BusinessError } 1600012 - No memory space.
     * @syscap SystemCapability.Notification.Notification
     * @crossplatform [since 12]
     * @since 10
     */
    function setBadgeNumber(badgeNumber: number, callback: AsyncCallback<void>): void;
    /**
     * Sets the notification badge number. This API uses a promise to return the result.
     *
     * A badge is a numeric identifier displayed in the upper right corner of an application's desktop icon, used to
     * prompt the user about the number of unprocessed notifications. After setting, the desktop icon will display the
     * corresponding badge number. This is suitable for scenarios where the number of pending messages needs to be
     * prompted on the desktop icon, such as the number of unread messages and to-do items.
     *
     * This API can be properly called on devices other than wearables. If it is called on wearables, error code 801 is
     * returned.
     *
     * @param { number } badgeNumber - Notification badge number to set. If **badgeNumber** is set to a value less than or
     *     equal to **0**, badges are cleared; if the value is greater than **99**, **99+** is displayed on the badge.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported. [since 18]
     * @throws { BusinessError } 1600001 - Internal error.
     * @throws { BusinessError } 1600002 - Marshalling or unmarshalling error.
     * @throws { BusinessError } 1600003 - Failed to connect to the service.
     * @throws { BusinessError } 1600012 - No memory space.
     * @syscap SystemCapability.Notification.Notification
     * @crossplatform [since 12]
     * @since 10
     */
    function setBadgeNumber(badgeNumber: number): Promise<void>;
    /**
     * Obtains the notification settings of the application, including the switch statuses for
     * lock screen notifications, banner notifications, desktop badges, vibration, and ringtone.
     * This API uses a promise to return the result.
     *
     * @returns { Promise<NotificationSetting> } Promise used to return the result.
     * @throws { BusinessError } 1600001 - Internal error.
     * @throws { BusinessError } 1600002 - Marshalling or unmarshalling error.
     * @throws { BusinessError } 1600003 - Failed to connect to the service.
     * @syscap SystemCapability.Notification.Notification
     * @since 20
     */
    function getNotificationSetting(): Promise<NotificationSetting>;
    /**
     * Opens the notification settings page of the application, which is displayed in semi-modal mode and can be used to
     * set the notification enabling and notification mode. This API uses a promise to return the result.
     *
     * This is suitable for scenarios where users need to manually modify notification settings, such as
     * a secondary request after a user denies authorization, or when the notification reminder method
     * (vibration, ringtone, etc.) needs to be modified. When the requestEnableNotification dialog
     * box is denied by the user, you can call this API to guide the user to the notification settings
     * page to manually enable it.
     *
     * @param { UIAbilityContext } context - Ability context bound to the notification settings page.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 801 - Capability not supported. [since 18]
     * @throws { BusinessError } 1600001 - Internal error.
     * @throws { BusinessError } 1600003 - Failed to connect to the service.
     * @throws { BusinessError } 1600018 - The notification settings window is already displayed.
     * @syscap SystemCapability.Notification.NotificationSettings
     * @stagemodelonly
     * @since 13
     */
    function openNotificationSettings(context: UIAbilityContext): Promise<void>;
    /**
     * Opens the notification settings page of the application, which is presented in a semi-modal window
     * and can be used to set notification switches, notification reminder methods, etc. This API uses
     * a promise to return the user-set status when the semi-modal window is closed.
     *
     * Unlike openNotificationSettings, this API returns a NotificationSetting object when the semi-modal
     * window is closed. You can determine whether the user has enabled the notification permission
     * based on the returned result, thereby deciding subsequent logic.
     *
     * @param { UIAbilityContext } context - Ability context bound to the notification settings page.
     * @returns { Promise<NotificationSetting> } Promise used to return the result.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 1600001 - Internal error.
     * @throws { BusinessError } 1600003 - Failed to connect to the service.
     * @throws { BusinessError } 1600018 - The notification settings window is already displayed.
     * @syscap SystemCapability.Notification.NotificationSettings
     * @stagemodelonly
     * @since 26.0.0
     */
    function openNotificationSettingsWithResult(context: UIAbilityContext): Promise<NotificationSetting>;
    /**
     * Obtains the badge number of this application. This API uses a promise to return the result.
     *
     * This API is used to query the badge number displayed on the current application's desktop icon.
     *
     * @returns { Promise<number> } Promise used to return the badge number. (The value is irrelevant to whether
     *     notifications and home-screen badges of this application are enabled.)
     * @throws { BusinessError } 1600001 - Internal error.
     * @throws { BusinessError } 1600002 - Marshalling or unmarshalling error.
     * @throws { BusinessError } 1600003 - Failed to connect to the service.
     * @syscap SystemCapability.Notification.Notification
     * @since 22
     */
    function getBadgeNumber(): Promise<number>;
    /**
     * Checks whether geofencing is enabled. This API uses a promise to return the result.
     *
     * @returns { Promise<boolean> } Promise used to return the result. The value **true** indicates that geofencing is
     *     enabled, and the value **false** indicates the opposite.
     * @throws { BusinessError } 1600001 - Internal error.
     * @throws { BusinessError } 1600002 - Marshalling or unmarshalling error.
     * @throws { BusinessError } 1600003 - Failed to connect to the service.
     * @throws { BusinessError } 1600012 - No memory space.
     * @syscap SystemCapability.Notification.Notification
     * @since 23
     */
    function isGeofenceEnabled(): Promise<boolean>;
    /**
     * Describes the setting status of the notification mode switch.
     *
     * @syscap SystemCapability.Notification.Notification
     * @since 20
     */
    export interface NotificationSetting {
        /**
         * Whether to enable vibration.
         *
         * - **true**: enable.
         * - **false**: disable.
         *
         * @syscap SystemCapability.Notification.Notification
         * @since 20
         */
        vibrationEnabled: boolean;
        /**
         * Whether to enable ringtone.
         *
         * - **true**: enable.
         * - **false**: disable.
         *
         * @syscap SystemCapability.Notification.Notification
         * @since 20
         */
        soundEnabled: boolean;
        /**
         * Whether to enable lock screen notification.
         *
         * - **true**: enable.
         * - **false**: disable.
         *
         * @syscap SystemCapability.Notification.Notification
         * @stagemodelonly
         * @since 26.0.0
         */
        lockScreenEnabled?: boolean;
        /**
         * Whether to enable banner notification.
         *
         * - **true**: enable.
         * - **false**: disable.
         *
         * @syscap SystemCapability.Notification.Notification
         * @stagemodelonly
         * @since 26.0.0
         */
        bannerEnabled?: boolean;
        /**
         * Whether to enable the display of notification badges.
         *
         * - **true**: enable.
         * - **false**: disable.
         *
         * @syscap SystemCapability.Notification.Notification
         * @stagemodelonly
         * @since 26.0.0
         */
        badgeNumberEnabled?: boolean;
        /**
         * Whether to enable the application notification.
         *
         * - **true**: enable.
         * - **false**: disable.
         *
         * @syscap SystemCapability.Notification.Notification
         * @stagemodelonly
         * @since 26.0.0
         */
        notificationEnabled?: boolean;
    }
    /**
     * Enumerates the notification slot types.
     *
     * Different types correspond to different [SlotLevel]{@link notificationManager.SlotLevel} values,
     * determining the reminder behavior of the notification.
     *
     * @syscap SystemCapability.Notification.Notification
     * @atomicservice [since 12]
     * @since 9
     */
    export enum SlotType {
        /**
         * Unknown type. This type corresponds to the
         * [SlotLevel]{@link notificationManager.SlotLevel} of **LEVEL_MIN**.
         *
         * @syscap SystemCapability.Notification.Notification
         * @atomicservice [since 12]
         * @since 9
         */
        UNKNOWN_TYPE = 0,
        /**
         * Social communication. This type corresponds to the
         * [SlotLevel]{@link notificationManager.SlotLevel} of **LEVEL_HIGH**.
         *
         * @syscap SystemCapability.Notification.Notification
         * @atomicservice [since 12]
         * @since 9
         */
        SOCIAL_COMMUNICATION = 1,
        /**
         * Service information. This type corresponds to the
         * [SlotLevel]{@link notificationManager.SlotLevel} of **LEVEL_HIGH**.
         *
         * @syscap SystemCapability.Notification.Notification
         * @atomicservice [since 12]
         * @since 9
         */
        SERVICE_INFORMATION = 2,
        /**
         * Content information. This type corresponds to the
         * [SlotLevel]{@link notificationManager.SlotLevel} of **LEVEL_MIN**.
         *
         * @syscap SystemCapability.Notification.Notification
         * @atomicservice [since 12]
         * @since 9
         */
        CONTENT_INFORMATION = 3,
        /**
         * Live view. A third-party application cannot directly create a notification of this type. Instead, after the
         * system proxy creates a notification, the third-party application can release the notification with the same
         * ID to update the specified content. This type corresponds to the
         * [SlotLevel]{@link notificationManager.SlotLevel} of **LEVEL_DEFAULT**.
         *
         * @syscap SystemCapability.Notification.Notification
         * @atomicservice [since 12]
         * @since 11
         */
        LIVE_VIEW = 4,
        /**
         * Customer service message. This type is used for messages between users and customer service
         * providers. The messages must be initiated by users. This type corresponds to the
         * [SlotLevel]{@link notificationManager.SlotLevel} of **LEVEL_DEFAULT**.
         *
         * @syscap SystemCapability.Notification.Notification
         * @atomicservice [since 12]
         * @since 11
         */
        CUSTOMER_SERVICE = 5,
        /**
         * Other types. This type corresponds to the
         * [SlotLevel]{@link notificationManager.SlotLevel} of **LEVEL_MIN**.
         *
         * @syscap SystemCapability.Notification.Notification
         * @atomicservice [since 12]
         * @since 9
         */
        OTHER_TYPES = 0xFFFF
    }
    /**
     * Enumerates the notification content types.
     *
     * @syscap SystemCapability.Notification.Notification
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 9
     */
    export enum ContentType {
        /**
         * Normal text notification.
         *
         * @syscap SystemCapability.Notification.Notification
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        NOTIFICATION_CONTENT_BASIC_TEXT,
        /**
         * Long text notification.
         *
         * @syscap SystemCapability.Notification.Notification
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        NOTIFICATION_CONTENT_LONG_TEXT,
        /**
         * Picture-attached notification.
         *
         * @syscap SystemCapability.Notification.Notification
         * @atomicservice [since 12]
         * @since 9
         */
        NOTIFICATION_CONTENT_PICTURE,
        /**
         * Conversation notification.
         *
         * @syscap SystemCapability.Notification.Notification
         * @atomicservice [since 12]
         * @since 9
         */
        NOTIFICATION_CONTENT_CONVERSATION,
        /**
         * Multi-line text notification.
         *
         * @syscap SystemCapability.Notification.Notification
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        NOTIFICATION_CONTENT_MULTILINE,
        /**
         * System live view notification. A third-party application cannot directly create a notification of this type. After the
         * system proxy creates a system live view, the third-party application publishes a notification with the same ID to
         * update the specified content.
         *
         * @syscap SystemCapability.Notification.Notification
         * @atomicservice [since 12]
         * @since 11
         */
        NOTIFICATION_CONTENT_SYSTEM_LIVE_VIEW,
        /**
         * Common live view notification. Available only to system applications.
         *
         * @syscap SystemCapability.Notification.Notification
         * @atomicservice [since 12]
         * @since 11
         */
        NOTIFICATION_CONTENT_LIVE_VIEW
    }
    /**
     * Enumerates the notification level.
     *
     * This API is used to define the notification reminder behavior level of NotificationSlot, affecting how the
     * notification is displayed in the status bar, whether to show banners and alert sounds, etc.
     *
     * @syscap SystemCapability.Notification.Notification
     * @since 9
     */
    export enum SlotLevel {
        /**
         * Notification is disabled.
         *
         * @syscap SystemCapability.Notification.Notification
         * @since 9
         */
        LEVEL_NONE = 0,
        /**
         * Notification is enabled, but the notification icon is not displayed in the status bar, with no alert tone and
         * banner.
         *
         * @syscap SystemCapability.Notification.Notification
         * @since 9
         */
        LEVEL_MIN = 1,
        /**
         * Notification is enabled, and the notification icon is displayed in the status bar, with no alert tone and banner.
         *
         * @syscap SystemCapability.Notification.Notification
         * @since 9
         */
        LEVEL_LOW = 2,
        /**
         * Notification is enabled, and the notification icon is displayed in the status bar, with an alert tone but no
         * banner.
         *
         * @syscap SystemCapability.Notification.Notification
         * @since 9
         */
        LEVEL_DEFAULT = 3,
        /**
         * Notification is enabled, and the notification icon is displayed in the status bar, with an alert tone and banner.
         *
         * @syscap SystemCapability.Notification.Notification
         * @since 9
         */
        LEVEL_HIGH = 4
    }
    /**
     * Describes the priority type of a notification.
     *
     * @syscap SystemCapability.Notification.Notification
     * @since 23
     */
    export enum PriorityNotificationType {
        /**
         * Default.
         *
         * @syscap SystemCapability.Notification.Notification
         * @since 23
         */
        OTHER = 'OTHER',
        /**
         * Primary contact.
         *
         * @syscap SystemCapability.Notification.Notification
         * @since 23
         */
        PRIMARY_CONTACT = 'PRIMARY_CONTACT',
        /**
         * Message that mentions me.
         *
         * @syscap SystemCapability.Notification.Notification
         * @since 23
         */
        AT_ME = 'AT_ME',
        /**
         * Urgent message.
         *
         * @syscap SystemCapability.Notification.Notification
         * @since 23
         */
        URGENT_MESSAGE = 'URGENT_MESSAGE',
        /**
         * Schedule reminder.
         *
         * @syscap SystemCapability.Notification.Notification
         * @since 23
         */
        SCHEDULE_REMINDER = 'SCHEDULE_REMINDER'
    }
    /**
     * Describes the bundle information of an application.
     *
     * @syscap SystemCapability.Notification.Notification
     * @since 9
     */
    export type BundleOption = _BundleOption;
    /**
     * Describes the operation button displayed in the notification.
     *
     * @syscap SystemCapability.Notification.Notification
     * @since 9
     */
    export type NotificationActionButton = _NotificationActionButton;
    /**
     * Describes the normal text notification.
     *
     * @syscap SystemCapability.Notification.Notification
     * @crossplatform [since 12]
     * @since 9
     */
    export type NotificationBasicContent = _NotificationBasicContent;
    /**
     * Describes the notification content.
     *
     * @syscap SystemCapability.Notification.Notification
     * @crossplatform [since 12]
     * @since 9
     */
    export type NotificationContent = _NotificationContent;
    /**
     * Describes the long text notification.
     *
     * @syscap SystemCapability.Notification.Notification
     * @crossplatform [since 12]
     * @since 9
     */
    export type NotificationLongTextContent = _NotificationLongTextContent;
    /**
     * Describes the multi-line text notification.
     *
     * @syscap SystemCapability.Notification.Notification
     * @crossplatform [since 12]
     * @since 9
     */
    export type NotificationMultiLineContent = _NotificationMultiLineContent;
    /**
     * Describes the picture-attached notification.
     *
     * @syscap SystemCapability.Notification.Notification
     * @since 9
     */
    export type NotificationPictureContent = _NotificationPictureContent;
    /**
     * Describes the system live view notification.
     *
     * @syscap SystemCapability.Notification.Notification
     * @since 11
     */
    export type NotificationSystemLiveViewContent = _NotificationSystemLiveViewContent;
    /**
     * Describes the notification request.
     *
     * @syscap SystemCapability.Notification.Notification
     * @crossplatform [since 12]
     * @since 9
     */
    export type NotificationRequest = _NotificationRequest;
    /**
     * Describes distributed notification options.
     *
     * @syscap SystemCapability.Notification.Notification
     * @since 9
     */
    export type DistributedOptions = _DistributedOptions;
    /**
     * Describes the notification slot.
     *
     * @syscap SystemCapability.Notification.Notification
     * @since 9
     */
    export type NotificationSlot = _NotificationSlot;
    /**
     * Describes the notification template.
     *
     * @syscap SystemCapability.Notification.Notification
     * @since 9
     */
    export type NotificationTemplate = _NotificationTemplate;
    /**
     * Describes the user input for the notification.
     *
     * @syscap SystemCapability.Notification.Notification
     * @since 9
     */
    export type NotificationUserInput = _NotificationUserInput;
    /**
     * Describes the notification capsule.
     *
     * @syscap SystemCapability.Notification.Notification
     * @since 11
     */
    export type NotificationCapsule = _NotificationCapsule;
    /**
     * Describes the notification button.
     *
     * @syscap SystemCapability.Notification.Notification
     * @since 11
     */
    export type NotificationButton = _NotificationButton;
    /**
     * Describes the notification timing information.
     *
     * @syscap SystemCapability.Notification.Notification
     * @since 11
     */
    export type NotificationTime = _NotificationTime;
    /**
     * Describes the notification progress.
     *
     * @syscap SystemCapability.Notification.Notification
     * @since 11
     */
    export type NotificationProgress = _NotificationProgress;
    /**
     * Describes partial information about the **wantAgent** in the notification request.
     *
     * @syscap SystemCapability.Notification.Notification
     * @stagemodelonly
     * @since 24
     */
    export type NotificationParameters = _NotificationParameters;
}
export default notificationManager;

```
