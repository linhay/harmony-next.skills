# @ohos.application.NotificationSubscriberExtensionAbility.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2025 Huawei Device Co., Ltd.
 * Licensed under the Apache License, Version 2.0 (the "License"),
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
 * @kit NotificationKit
 */
import type NotificationSubscriberExtensionContext from './@ohos.application.NotificationSubscriberExtensionContext';
import { NotificationInfo } from './notification/NotificationInfo';
/**
 * NotificationSubscriberExtensionAbility is the base class for notification subscriber extension abilities, providing
 * notification subscription-related functionality. Third-party wearable apps (such as companion applications for
 * watches)implement callback logic by inheriting this class, receiving notification information when notifications
 * are published on the local device and forwarding them to the wearable device via Bluetooth, and receiving callbacks
 * for notification cancellation when local notifications are cancelled and forwarding them to the wearable device to
 * delete the corresponding notifications.
 *
 * Use this module when your wearable application needs to obtain local notifications and sync them to a paired wearable
 * device. This module is used together with the notificationExtensionSubscription module. This module is responsible
 * for receiving and processing notification data in callbacks, while the notificationExtensionSubscription module is
 * responsible for management operations such as authorization, subscription, and unsubscription.
 *
 * @syscap SystemCapability.Notification.Notification
 * @stagemodelonly
 * @since 22
 */
declare class NotificationSubscriberExtensionAbility {
    /**
     * Context for the NotificationSubscriberExtensionAbility.
     *
     * @syscap SystemCapability.Notification.Notification
     * @stagemodelonly
     * @since 22
     */
    context: NotificationSubscriberExtensionContext;
    /**
     * Called when the notification subscription extension is destroyed.
     *
     * @syscap SystemCapability.Notification.Notification
     * @stagemodelonly
     * @since 22
     */
    onDestroy(): void;
    /**
     * Called when a notification is received.
     *
     * @param { NotificationInfo } notificationInfo - Callback information about the notification received in the
     *     notification subscription extension capability.
     * @syscap SystemCapability.Notification.Notification
     * @stagemodelonly
     * @since 22
     */
    onReceiveMessage(notificationInfo: NotificationInfo): void;
    /**
     * Called when notifications are canceled.
     *
     * @param { Array<string> } hashCodes - List of hash codes of the notifications to cancel, obtained through
     *     {@link @ohos.application.NotificationSubscriberExtensionAbility:
     *     NotificationSubscriberExtensionAbility.onReceiveMessage}.
     * @syscap SystemCapability.Notification.Notification
     * @stagemodelonly
     * @since 22
     */
    onCancelMessages(hashCodes: Array<string>): void;
}
export default NotificationSubscriberExtensionAbility;

```
