# @ohos.bundle.overlay.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2023 Huawei Device Co., Ltd.
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
import * as _OverlayModuleInfo from './bundleManager/OverlayModuleInfo';
/**
 * The module provides APIs for querying the
 * [OverlayModuleInfo]{@link ./bundleManager/OverlayModuleInfo:OverlayModuleInfo} of an application with the overlay
 * feature, and disabling and enabling the feature.
 *
 * An application with the overlay feature contains an overlay resource package. For details about this package, see
 * [Overlay Mechanism](docroot://quick-start/resource-categories-and-access.md#overlay-mechanism).
 *
 * > **NOTE**
 * >
 * > The APIs provided by this module apply only to the stage model and
 * > [static overlay](docroot://quick-start/resource-categories-and-access.md#using-overlay-in-static-mode) mode.
 *
 * @syscap SystemCapability.BundleManager.BundleFramework.Overlay
 * @since 10
 */
declare namespace overlay {
    /**
     * Enables or disables a module with the overlay feature in the current application. This API uses an asynchronous
     * callback to return the result.
     *
     * @param { string } moduleName - Name of the module with the overlay feature.
     * @param { boolean } isEnabled - Whether to enable the module with the overlay feature. **true** to enable, **false**
     *     otherwise.
     * @param { AsyncCallback<void> } callback - [Callback]{@link @ohos.base:AsyncCallback} used to return the result. If
     *     the operation is successful, **err** is **null**; otherwise, **err** is an error object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types.
     * @throws { BusinessError } 17700002 - The specified module name is not found.
     * @throws { BusinessError } 17700033 - The specified module is not an overlay module.
     * @syscap SystemCapability.BundleManager.BundleFramework.Overlay
     * @since 10
     */
    function setOverlayEnabled(moduleName: string, isEnabled: boolean, callback: AsyncCallback<void>): void;
    /**
     * Enables or disables a module with the overlay feature in the current application. This API uses a promise to return
     * the result.
     *
     * @param { string } moduleName - Name of the module with the overlay feature.
     * @param { boolean } isEnabled - Whether to enable the module with the overlay feature. **true** to enable, **false**
     *     otherwise.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types.
     * @throws { BusinessError } 17700002 - The specified module name is not found.
     * @throws { BusinessError } 17700033 - The specified module is not an overlay module.
     * @syscap SystemCapability.BundleManager.BundleFramework.Overlay
     * @since 10
     */
    function setOverlayEnabled(moduleName: string, isEnabled: boolean): Promise<void>;
    /**
     * Obtains the OverlayModuleInfo about a module with the overlay feature in the current application. This API uses an
     * asynchronous callback to return the result.
     *
     * @param { string } moduleName - Name of the module with the overlay feature.
     * @param { AsyncCallback<OverlayModuleInfo> } callback - [Callback]{@link @ohos.base:AsyncCallback} used to return
     *     the result, which is an [OverlayModuleInfo]{@link ./bundleManager/OverlayModuleInfo:OverlayModuleInfo} object.
     *     If the operation is successful, **err** is **null**; otherwise, **err** is an error object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types.
     * @throws { BusinessError } 17700002 - The specified module name is not found.
     * @throws { BusinessError } 17700032 - The specified bundle does not contain any overlay module.
     * @throws { BusinessError } 17700033 - The specified module is not an overlay module.
     * @syscap SystemCapability.BundleManager.BundleFramework.Overlay
     * @since 10
     */
    function getOverlayModuleInfo(moduleName: string, callback: AsyncCallback<OverlayModuleInfo>): void;
    /**
     * Obtains the OverlayModuleInfo about a module with the overlay feature in the current application. This API uses a
     * promise to return the result.
     *
     * @param { string } moduleName - Name of the module with the overlay feature.
     * @returns { Promise<OverlayModuleInfo> } Promise used to return the result, which is an
     *     [OverlayModuleInfo]{@link ./bundleManager/OverlayModuleInfo:OverlayModuleInfo} object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types.
     * @throws { BusinessError } 17700002 - The specified module name is not found.
     * @throws { BusinessError } 17700032 - The specified bundle does not contain any overlay module.
     * @throws { BusinessError } 17700033 - The specified module is not an overlay module.
     * @syscap SystemCapability.BundleManager.BundleFramework.Overlay
     * @since 10
     */
    function getOverlayModuleInfo(moduleName: string): Promise<OverlayModuleInfo>;
    /**
     * Obtains the OverlayModuleInfo associated with the specified target module. Modules with the overlay feature
     * generally provide an overlay resource file for other modules (target module) on the device. This API uses an
     * asynchronous callback to return the result.
     *
     * @param { string } targetModuleName - Name of the target module specified by modules with the overlay feature.
     * @param { AsyncCallback<Array<OverlayModuleInfo>> } callback - [Callback]{@link @ohos.base:AsyncCallback} used to
     *     return the result, which is an [OverlayModuleInfo]{@link ./bundleManager/OverlayModuleInfo:OverlayModuleInfo}
     *     object. If the operation is successful, **err** is **null**; otherwise, **err** is an error object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types.
     * @throws { BusinessError } 17700002 - The specified module name is not found.
     * @throws { BusinessError } 17700034 - The specified module is an overlay module.
     * @syscap SystemCapability.BundleManager.BundleFramework.Overlay
     * @since 10
     */
    function getTargetOverlayModuleInfos(targetModuleName: string, callback: AsyncCallback<Array<OverlayModuleInfo>>): void;
    /**
     * Obtains the OverlayModuleInfo associated with the specified target module. Modules with the overlay feature
     * generally provide an overlay resource file for other modules (target module) on the device. This API uses a promise
     * to return the result.
     *
     * @param { string } targetModuleName - Name of the target module specified by modules with the overlay feature.
     * @returns { Promise<Array<OverlayModuleInfo>> } Promise used to return the result, which is an array of
     *     [OverlayModuleInfo]{@link ./bundleManager/OverlayModuleInfo:OverlayModuleInfo} objects.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types.
     * @throws { BusinessError } 17700002 - The specified module name is not found.
     * @throws { BusinessError } 17700034 - The specified module is an overlay module.
     * @syscap SystemCapability.BundleManager.BundleFramework.Overlay
     * @since 10
     */
    function getTargetOverlayModuleInfos(targetModuleName: string): Promise<Array<OverlayModuleInfo>>;
    /**
     * Defines the information about a module with the overlay feature.
     *
     * @syscap SystemCapability.BundleManager.BundleFramework.Overlay
     * @since 10
     */
    export type OverlayModuleInfo = _OverlayModuleInfo.OverlayModuleInfo;
}
export default overlay;

```
