# @system.package.d.ts

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
 * > **NOTE**
 * >
 * > - The APIs of this module have been deprecated since API version 9. You are advised to use
 * > [@ohos.bundle.bundleManager]{@link @ohos.bundle.bundleManager:bundleManager} instead.
 *
 * @file
 * @kit AbilityKit
 */
/**
 * > **NOTE**
 * >
 * > This API has been supported since API version 3 and deprecated since API version 9.
 *
 * Checks whether a bundle has been installed.
 *
 * @syscap SystemCapability.BundleManager.BundleFramework
 * @since 3
 * @deprecated since 9
 */
export interface CheckPackageHasInstalledResponse {
    /**
     * Check result for whether the bundle has been installed. **true** if installed, **false** otherwise.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework
     * @since 3
     * @deprecated since 9
     */
    result: boolean;
}
/**
 * > **NOTE**
 * >
 * > This API has been supported since API version 3 and deprecated since API version 9.
 *
 * Checks whether a bundle has been installed.
 *
 * @syscap SystemCapability.BundleManager.BundleFramework
 * @since 3
 * @deprecated since 9
 */
export interface CheckPackageHasInstalledOptions {
    /**
     * Bundle name.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework
     * @since 3
     * @deprecated since 9
     */
    bundleName: string;
    /**
     * Called when API call is successful.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework
     * @since 3
     * @deprecated since 9
     */
    success?: (data: CheckPackageHasInstalledResponse) => void;
    /**
     * Called when API call has failed.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework
     * @since 3
     * @deprecated since 9
     */
    fail?: (data: any, code: number) => void;
    /**
     * Called when API call is complete.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework
     * @since 3
     * @deprecated since 9
     */
    complete?: () => void;
}
/**
 * > **NOTE**
 * >
 * > This API has been supported since API version 3 and deprecated since API version 9.
 *
 * Checks whether a bundle has been installed.
 *
 * @syscap SystemCapability.BundleManager.BundleFramework
 * @since 3
 * @deprecated since 9
 */
export default class Package {
    /**
     * Checks whether an application exists, or whether a native application has been installed.
     *
     * @param { CheckPackageHasInstalledOptions } options Options
     * @syscap SystemCapability.BundleManager.BundleFramework
     * @since 3
     * @deprecated since 9
     * @useinstead ohos.bundle.bundleManager/bundleManager#canOpenLink
     */
    static hasInstalled(options: CheckPackageHasInstalledOptions): void;
}

```
