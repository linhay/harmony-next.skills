# @ohos.bundle.launcherBundleManager.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022 Huawei Device Co., Ltd.
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
import { LauncherAbilityInfo as _LauncherAbilityInfo } from './bundleManager/LauncherAbilityInfo';
import { ShortcutInfo as _ShortcutInfo, ShortcutWant as _ShortcutWant, ParameterItem as _ParameterItem } from './bundleManager/ShortcutInfo';
/**
 * The module providers APIs for launcher applications (applications with icons on the home screen) to obtain the
 * [launcher ability information]{@link ./bundleManager/LauncherAbilityInfo:LauncherAbilityInfo}.
 *
 * @syscap SystemCapability.BundleManager.BundleFramework.Launcher
 * @since 9
 */
declare namespace launcherBundleManager {
    /**
     * Obtains the [launcher ability information]{@link ./bundleManager/LauncherAbilityInfo:LauncherAbilityInfo} based on
     * the given bundle name and user ID.
     *
     * @permission ohos.permission.GET_BUNDLE_INFO_PRIVILEGED
     * @param { string } bundleName - Bundle name.
     * @param { number } userId - User ID, which can be obtained by calling
     *     [getOsAccountLocalId]{@link @ohos.account.osAccount:osAccount.AccountManager.getOsAccountLocalId(callback: AsyncCallback<number>)}
     *     .
     * @returns { Array<LauncherAbilityInfo> } Array of the
     *     [LauncherAbilityInfo]{@link ./bundleManager/LauncherAbilityInfo:LauncherAbilityInfo} objects obtained.
     * @throws { BusinessError } 201 - Verify permission denied.
     * @throws { BusinessError } 801 - Capability not support.
     * @throws { BusinessError } 17700001 - The specified bundle name is not found.
     * @throws { BusinessError } 17700004 - The specified user ID is not found.
     * @syscap SystemCapability.BundleManager.BundleFramework.Launcher
     * @since 18
     */
    function getLauncherAbilityInfoSync(bundleName: string, userId: number): Array<LauncherAbilityInfo>;
    /**
     * Defines the information about the launcher ability.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework.Launcher
     * @since 18
     */
    export type LauncherAbilityInfo = _LauncherAbilityInfo;
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
export default launcherBundleManager;

```
