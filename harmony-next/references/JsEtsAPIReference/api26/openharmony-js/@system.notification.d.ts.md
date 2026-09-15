# @system.notification.d.ts

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
/**
 *
 * @file
 * @kit NotificationKit
 */
/**
 *
 * @syscap SystemCapability.Notification.Notification
 * @since 3
 * @deprecated since 7
 */
export interface ActionResult {
    /**
     * Name of the application bundle to which the notification will be redirected after being clicked.
     *
     * @syscap SystemCapability.Notification.Notification
     * @since 3
     * @deprecated since 7
     */
    bundleName: string;
    /**
     * Name of the application ability to which the notification will be redirected after being clicked.
     *
     * @syscap SystemCapability.Notification.Notification
     * @since 3
     * @deprecated since 7
     */
    abilityName: string;
    /**
     * URI of the page to be redirected to.
     *
     * @syscap SystemCapability.Notification.Notification
     * @since 3
     * @deprecated since 7
     */
    uri: string;
}
/**
 *
 * @syscap SystemCapability.Notification.Notification
 * @since 3
 * @deprecated since 7
 */
export interface ShowNotificationOptions {
    /**
     * Notification title.
     *
     * @syscap SystemCapability.Notification.Notification
     * @since 3
     * @deprecated since 7
     */
    contentTitle?: string;
    /**
     * Notification content.
     *
     * @syscap SystemCapability.Notification.Notification
     * @since 3
     * @deprecated since 7
     */
    contentText?: string;
    /**
     * Action triggered when the notification is clicked.
     *
     * This API is deprecated since API version 7.
     *
     * @syscap SystemCapability.Notification.Notification
     * @since 3
     * @deprecated since 7
     */
    clickAction?: ActionResult;
}
/**
 * Manages notifications.
 *
 * @syscap SystemCapability.Notification.Notification
 * @since 3
 * @deprecated since 7
 * @useinstead ohos.notification/notification
 */
declare class Notification {
    /**
     * Displays the notification.
     *
     * @param { ShowNotificationOptions } [options] - Notification title.
     * @syscap SystemCapability.Notification.Notification
     * @since 3
     * @deprecated since 7
     * @useinstead ohos.notification/notification
     */
    static show(options?: ShowNotificationOptions): void;
}
export default Notification;

```
