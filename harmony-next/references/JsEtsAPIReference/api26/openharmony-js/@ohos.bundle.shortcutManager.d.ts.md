# @ohos.bundle.shortcutManager.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2024 Huawei Device Co., Ltd.
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
 * @kit AbilityKit
 */
import { ShortcutInfo as _ShortcutInfo, ShortcutWant as _ShortcutWant, ParameterItem as _ParameterItem } from './bundleManager/ShortcutInfo';
/**

* This module provides the application's management capabilities for shortcuts, including setting whether a shortcut
 * is displayed. Through shortcuts, users can quickly launch specific features of an app from the home screen,
 * improving the app's ease of use and user retention. Typical usage scenarios include: providing users with quick
 * access to frequently used features, dynamically adjusting the display of shortcuts based on user habits, etc.
 *
 * @syscap SystemCapability.BundleManager.BundleFramework.Launcher
 * @since 20
 */
declare namespace shortcutManager {
    /**
     * Obtains all the shortcut information defined in the
     * [configuration](docroot://quick-start/module-configuration-file.md#shortcuts) file of the current application. This
     * API uses a promise to return the result.
     *
     * @returns { Promise<Array<ShortcutInfo>> } Promise that returns all the shortcut information defined in the
     *     configuration file.
     * @syscap SystemCapability.BundleManager.BundleFramework.Launcher
     * @since 20
     */
    function getAllShortcutInfoForSelf(): Promise<Array<ShortcutInfo>>;
    /**
     * Sets whether to display the specified shortcut for the current application. This API uses a promise to return the
     * result.
     *
     * @param { string } id - Shortcut ID, which is the value of the **shortcutId** field under the **shortcuts** tag in
     *     the [module.json5](docroot://quick-start/module-configuration-file.md) file. The value is a string of up to 63
     *     bytes.
     * @param { boolean } visible - Whether to display the shortcut. **true** to display, **false** otherwise.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 17700070 - The specified shortcut id is not exist.
     * @syscap SystemCapability.BundleManager.BundleFramework.Launcher
     * @since 20
     */
    function setShortcutVisibleForSelf(id: string, visible: boolean): Promise<void>;
    /**
     * Checks whether the current device supports shortcuts.
     *
     * @returns { boolean } Indicates whether the current device supports shortcuts.
     *     The return value true indicates that the current device supports shortcuts;
     *     the return value false indicates that the current device does not support shortcuts.
     * @syscap SystemCapability.BundleManager.BundleFramework.Launcher
     * @stagemodelonly
     * @since 26.0.0
     */
    function isShortcutSupported(): boolean;
    /**
     * Defines the shortcut information defined in the
     * [module.json5](docroot://quick-start/module-configuration-file.md#shortcuts) file of the application.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework.Launcher
     * @since 20
     */
    export type ShortcutInfo = _ShortcutInfo;
    /**
     * Defines the target [wants](docroot://quick-start/module-configuration-file.md#wants) defined in the shortcut
     * configuration.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework.Launcher
     * @since 20
     */
    export type ShortcutWant = _ShortcutWant;
    /**
     * Defines the custom data in the shortcut configuration.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework.Launcher
     * @since 20
     */
    export type ParameterItem = _ParameterItem;
}
export default shortcutManager;

```
