# @ohos.ability.screenLockFileManager.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (C) 2024-2026 Huawei Device Co., Ltd.
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
 * @file Sensitive Data Access Management Under Lock Screen
 * @kit AbilityKit
 */
/**
 * This module provides the capability to protect app sensitive data under the lock screen, supporting requesting and
 * releasing access permissions for sensitive data under the lock screen, as well as querying the status of sensitive
 * data keys. When the reference count of a sensitive data key reaches zero and the screen has been locked for a
 * duration reaching the system-configured lock duration threshold, the key is destroyed, and operations on that data
 * become impossible. These keys can be restored only after the screen is unlocked. By calling the
 * [acquireAccess]{@link screenLockFileManager.acquireAccess} API of this module, you can prevent the key from being
 * destroyed after the screen has been locked for a duration reaching the system-configured lock duration threshold.
 *
 * > **NOTE**
 * >
 * > - To enable the sensitive data protection function under the lock screen for an app, you need to configure the
 * > ohos.permission.PROTECT_SCREEN_LOCK_DATA permission in
 * > [requestPermissions](docroot://security/AccessToken/declare-permissions.md#declaring-permissions-in-the-configuration-file).
 *
 * @syscap SystemCapability.Security.ScreenLockFileManager
 * @since 12
 */
declare namespace screenLockFileManager {
    /**
     * Enumerates the types of sensitive data that can be accessed under the lock screen.
     *
     * @syscap SystemCapability.Security.ScreenLockFileManager
     * @since 12
     */
    export enum DataType {
        /**
         * Media data type.
         *
         * @syscap SystemCapability.Security.ScreenLockFileManager
         * @since 12
         */
        MEDIA_DATA = 0x00000001,
        /**
         * All sensitive data types.
         *
         * @syscap SystemCapability.Security.ScreenLockFileManager
         * @since 12
         */
        ALL_DATA = 0xffffffff
    }
    /**
     * Enumerates the statuses for requesting access permissions for sensitive data under the lock screen.
     *
     * @syscap SystemCapability.Security.ScreenLockFileManager
     * @since 12
     */
    export enum AccessStatus {
        /**
         * The request for access permission for sensitive data under lock screen is denied.
         *
         * @syscap SystemCapability.Security.ScreenLockFileManager
         * @since 12
         */
        ACCESS_DENIED = -1,
        /**
         * The request for access permission for sensitive data under lock screen is granted.
         *
         * @syscap SystemCapability.Security.ScreenLockFileManager
         * @since 12
         */
        ACCESS_GRANTED = 0
    }
    /**
     * Enumerates the statuses for releasing access permissions for sensitive data under the lock screen.
     *
     * @syscap SystemCapability.Security.ScreenLockFileManager
     * @since 12
     */
    export enum ReleaseStatus {
        /**
         * Release of access permission for sensitive data under lock screen is denied.
         *
         * @syscap SystemCapability.Security.ScreenLockFileManager
         * @since 12
         */
        RELEASE_DENIED = -1,
        /**
         * Release of access permission for sensitive data under lock screen is granted.
         *
         * @syscap SystemCapability.Security.ScreenLockFileManager
         * @since 12
         */
        RELEASE_GRANTED = 0
    }
    /**
     * Enumerates the statuses of sensitive data keys under the lock screen.
     *
     * @syscap SystemCapability.Security.ScreenLockFileManager
     * @since 18
     */
    export enum KeyStatus {
        /**
         * The key does not exist. This status indicates that the app has not enabled the sensitive data protection function
         * under lock screen, or the protection function is unavailable on the current device.
         *
         * @syscap SystemCapability.Security.ScreenLockFileManager
         * @since 18
         */
        KEY_NOT_EXIST = -2,
        /**
         * The key has been released. This status indicates that sensitive data under lock screen cannot be operated.
         *
         * @syscap SystemCapability.Security.ScreenLockFileManager
         * @since 18
         */
        KEY_RELEASED = -1,
        /**
         * The key exists. This status indicates that sensitive data under lock screen can be operated normally.
         *
         * @syscap SystemCapability.Security.ScreenLockFileManager
         * @since 18
         */
        KEY_EXIST = 0
    }
    /**
     * Requests the access permission for the caller app's sensitive data under the lock screen in synchronous mode. After
     * the request is successful, the reference count of the sensitive data key increases, preventing the key from being
     * destroyed after the screen has been locked for a duration reaching the system-configured lock duration threshold.
     * This method must be used in pair with [releaseAccess]{@link screenLockFileManager.releaseAccess}.
     *
     * Before calling this API, ensure that the app has enabled the sensitive data protection function under the lock
     * screen, and that the key status queried through the
     * [queryAppKeyState]{@link screenLockFileManager.queryAppKeyState} API is KEY_EXIST.
     *
     * @returns { AccessStatus } Application status for access permission for sensitive data under lock screen.
     * @throws { BusinessError } 801 - The specified SystemCapability name was not found.
     * @throws { BusinessError } 29300002 - The system ability works abnormally.
     * @throws { BusinessError } 29300003 - The application is not enabled the data protection under lock screen.
     * @throws { BusinessError } 29300004 - File access is denied.
     * @syscap SystemCapability.Security.ScreenLockFileManager
     * @since 12
     */
    function acquireAccess(): AccessStatus;
    /**
     * Releases the access permission for the caller app's sensitive data under the lock screen in synchronous mode. After
     * the release is successful, the reference count of the sensitive data key decreases. When the count reaches zero,
     * the key can be destroyed after the screen has been locked for a duration reaching the system-configured lock
     * duration threshold.
     *
     * Before calling this API, ensure that the app has enabled the sensitive data protection function under the lock
     * screen, and that the [acquireAccess]{@link screenLockFileManager.acquireAccess} API has been called to request the
     * permission successfully first.
     *
     * @returns { ReleaseStatus } Release status of the access permission for sensitive data under lock screen.
     * @throws { BusinessError } 801 - The specified SystemCapability name was not found.
     * @throws { BusinessError } 29300002 - The system ability works abnormally.
     * @throws { BusinessError } 29300003 - The application is not enabled the data protection under lock screen.
     * @throws { BusinessError } 29300005 - File access was not acquired.
     * @syscap SystemCapability.Security.ScreenLockFileManager
     * @since 12
     */
    function releaseAccess(): ReleaseStatus;
    /**
     * Queries the status of the caller app's sensitive data key under the lock screen in synchronous mode.
     *
     * @returns { KeyStatus } Status of the key for sensitive data under lock screen.
     * @throws { BusinessError } 801 - The specified SystemCapability name was not found.
     * @throws { BusinessError } 29300002 - The system ability works abnormally.
     * @syscap SystemCapability.Security.ScreenLockFileManager
     * @since 18
     */
    function queryAppKeyState(): KeyStatus;
}
export default screenLockFileManager;

```
