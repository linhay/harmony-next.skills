# @ohos.bundle.defaultAppManager.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022-2024 Huawei Device Co., Ltd.
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
import { AsyncCallback } from './@ohos.base';
/**
 * The module provides APIs to query whether the current application is the default application of a specific type.
 *
 * @syscap SystemCapability.BundleManager.BundleFramework.DefaultApp
 * @since 9
 */
declare namespace defaultAppManager {
    /**
     * Enumerates the default application types.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework.DefaultApp
     * @since 9
     */
    export enum ApplicationType {
        /**
         * Default browser.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.DefaultApp
         * @since 9
         */
        BROWSER = "Web Browser",
        /**
         * Default image viewer.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.DefaultApp
         * @since 9
         */
        IMAGE = "Image Gallery",
        /**
         * Default audio player.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.DefaultApp
         * @since 9
         */
        AUDIO = "Audio Player",
        /**
         * Default video player.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.DefaultApp
         * @since 9
         */
        VIDEO = "Video Player",
        /**
         * Default PDF reader.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.DefaultApp
         * @since 9
         */
        PDF = "PDF Viewer",
        /**
         * Default Word viewer.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.DefaultApp
         * @since 9
         */
        WORD = "Word Viewer",
        /**
         * Default Excel viewer.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.DefaultApp
         * @since 9
         */
        EXCEL = "Excel Viewer",
        /**
         * Default PowerPoint viewer.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.DefaultApp
         * @since 9
         */
        PPT = "PPT Viewer",
        /**
         * Default email.
         *
         * @syscap SystemCapability.BundleManager.BundleFramework.DefaultApp
         * @since 12
         */
        EMAIL = 'Email'
    }
    /**
     * Checks whether this application is the default application of a system-defined application type or a
     * [uniform data type]{@link @ohos.data.uniformTypeDescriptor:uniformTypeDescriptor}. This API uses an asynchronous
     * callback to return the result.
     *
     * @param { string } type - Type of the target application. It must be set to a value defined by
     *     [ApplicationType]{@link defaultAppManager.ApplicationType} or
     *     [UniformDataType]{@link @ohos.data.uniformTypeDescriptor:uniformTypeDescriptor}.
     * @param { AsyncCallback<boolean> } callback - [Callback]{@link @ohos.base:AsyncCallback} used to return the result.
     *     If the operation is successful, **err** is **null** and **data** is a Boolean value (**true** if the
     *     application is the default application, **false** otherwise). If the operation fails, **err** is an error
     *     object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types.
     * @throws { BusinessError } 801 - Capability not supported.
     * @syscap SystemCapability.BundleManager.BundleFramework.DefaultApp
     * @since 9
     */
    function isDefaultApplication(type: string, callback: AsyncCallback<boolean>): void;
    /**
     * Checks whether this application is the default application of a system-defined application type or a
     * [uniform data type]{@link @ohos.data.uniformTypeDescriptor:uniformTypeDescriptor}. This API uses a promise to
     * return the result.
     *
     * @param { string } type - Type of the target application. It must be set to a value defined by
     *     [ApplicationType]{@link defaultAppManager.ApplicationType} or
     *     [UniformDataType]{@link @ohos.data.uniformTypeDescriptor:uniformTypeDescriptor}.
     * @returns { Promise<boolean> } Promise used to return the result, indicating whether the application is the default
     *     application. **true** if the application is the default application, **false** otherwise.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types.
     * @throws { BusinessError } 801 - Capability not supported.
     * @syscap SystemCapability.BundleManager.BundleFramework.DefaultApp
     * @since 9
     */
    function isDefaultApplication(type: string): Promise<boolean>;
    /**
     * Checks whether this application is the default application of a system-defined application type or a
     * [uniform data type]{@link @ohos.data.uniformTypeDescriptor:uniformTypeDescriptor}. This API returns the result
     * synchronously.
     *
     * @param { string } type - Type of the target application. It must be set to a value defined by
     *     [ApplicationType]{@link defaultAppManager.ApplicationType} or
     *     [UniformDataType]{@link @ohos.data.uniformTypeDescriptor:uniformTypeDescriptor}.
     * @returns { boolean } Returns **true** if the application is the default application; returns **false** otherwise.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types.
     * @throws { BusinessError } 801 - Capability not supported.
     * @syscap SystemCapability.BundleManager.BundleFramework.DefaultApp
     * @since 10
     */
    function isDefaultApplicationSync(type: string): boolean;
}
export default defaultAppManager;

```
