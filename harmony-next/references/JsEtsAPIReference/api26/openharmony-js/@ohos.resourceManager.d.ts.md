# @ohos.resourceManager.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2021-2024 Huawei Device Co., Ltd.
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
 * @kit LocalizationKit
 */
import { RawFileDescriptor as _RawFileDescriptor } from './global/rawFileDescriptor';
import { Resource as _Resource } from './global/resource';
import { AsyncCallback as _AsyncCallback } from './@ohos.base';
import { DrawableDescriptor } from './@ohos.arkui.drawableDescriptor';
/**
 * This module provides the capabilities to access application resources and system resources. It allows applications
 * to obtain the best-matching application or system resources based on the current
 * [configuration]{@link resourceManager.Configuration}, supporting internationalization resource matching and multi-
 * device adaptation. For details about the matching rules, see
 * [Matching Resources](docroot://quick-start/resource-categories-and-access.md#matching-resources).
 *
 * The configuration includes language, script, country/region, orientation, color mode, Mobile Country Code (MCC),
 * Mobile Network Code (MNC), device type, and screen density.
 *
 * **Use scenarios**
 * - Application internationalization: Automatically obtains matching string resources based on the user's language and
 * region.
 * - Multi-device adaptation: Obtains appropriate media resources based on device type and screen density.
 * - Dynamic resource configuration: Obtains resources corresponding to the current device state, such as orientation
 * and color mode.
 *
 * **How to Use**
 * - In the FA model, you need to import the module and then call
 * [getResourceManager]{@link resourceManager.getResourceManager} to obtain a **ResourceManager** object.
 * - Since API version 9, in the stage model, the stage model allows you to obtain the **resourceManager** object
 * through context without importing any module. For details about the context, see
 * [application context](docroot://application-models/application-context-stage.md).
 *
 *   ```ts
 *   import { UIAbility } from '@kit.AbilityKit';
 *   import { window } from '@kit.ArkUI';
 *
 *   export default class EntryAbility extends UIAbility {
 *     onWindowStageCreate(windowStage: window.WindowStage) {
 *       let context = this.context;
 *       let resourceManager = context.resourceManager;
 *     }
 *   }
 *   ```
 *
 * @syscap SystemCapability.Global.ResourceManager
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 6
 */
declare namespace resourceManager {
    /**
     * Enumerates the screen directions.
     *
     * @syscap SystemCapability.Global.ResourceManager
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 6
     */
    export enum Direction {
        /**
         * Portrait
         *
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        DIRECTION_VERTICAL = 0,
        /**
         * Landscape
         *
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        DIRECTION_HORIZONTAL = 1
    }
    /**
     * Enumerates the device types.
     *
     * <!--RP1-->
     *
     * <!--RP1End-->
     *
     * @syscap SystemCapability.Global.ResourceManager
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 6
     */
    export enum DeviceType {
        /**
         * Phone
         *
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        DEVICE_TYPE_PHONE = 0x00,
        /**
         * Tablet
         *
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 6
         */
        DEVICE_TYPE_TABLET = 0x01,
        /**
         * Head unit
         *
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 6
         */
        DEVICE_TYPE_CAR = 0x02,
        /**
         * Indicates a PC.
         *
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 6
         */
        DEVICE_TYPE_PC = 0x03,
        /**
         * Smart TV
         *
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 6
         */
        DEVICE_TYPE_TV = 0x04,
        /**
         * Wearable
         *
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 6
         */
        DEVICE_TYPE_WEARABLE = 0x06,
        /**
         * PC/2-in-1 device
         *
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform
         * @atomicservice
         * @since 11
         */
        DEVICE_TYPE_2IN1 = 0x07
    }
    /**
     * Enumerates the screen density types.
     *
     * @syscap SystemCapability.Global.ResourceManager
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 6
     */
    export enum ScreenDensity {
        /**
         * Small-scale DPI.
         *
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        SCREEN_SDPI = 120,
        /**
         * Medium-scale DPI.
         *
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        SCREEN_MDPI = 160,
        /**
         * Large-scale DPI.
         *
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        SCREEN_LDPI = 240,
        /**
         * Extra-large-scale DPI.
         *
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        SCREEN_XLDPI = 320,
        /**
         * Extra-extra-large-scale DPI.
         *
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        SCREEN_XXLDPI = 480,
        /**
         * Extra-extra-extra-large-scale DPI.
         *
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        SCREEN_XXXLDPI = 640
    }
    /**
     * Defines the color mode of the current device.
     *
     * @syscap SystemCapability.Global.ResourceManager
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    export enum ColorMode {
        /**
         * Dark mode.
         *
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        DARK = 0,
        /**
         * Light mode.
         *
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        LIGHT = 1
    }
    /**
     * Defines the device configuration.
     *
     * @syscap SystemCapability.Global.ResourceManager
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 6
     */
    export class Configuration {
        /**
         * Screen orientation modes.
         *
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        direction: Direction;
        /**
         * Language locale.
         *
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        locale: string;
        /**
         * Device type.
         *
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        deviceType: DeviceType;
        /**
         * Screen density
         *
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        screenDensity: ScreenDensity;
        /**
         * Color mode.
         *
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        colorMode: ColorMode;
        /**
         * Mobile country code (MCC).
         *
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        mcc: number;
        /**
         * Mobile network code (MNC).
         *
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        mnc: number;
    }
    /**
     * Defines the device capability.
     *
     * @syscap SystemCapability.Global.ResourceManager
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 6
     */
    export class DeviceCapability {
        /**
         * Screen density of the device.
         *
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        screenDensity: ScreenDensity;
        /**
         * Device type.
         *
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        deviceType: DeviceType;
    }
    /**
     * Asynchronous callback interface.
     *
     * @syscap SystemCapability.Global.ResourceManager
     * @since 6
     * @deprecated since 9
     * @useinstead @ohos.base:AsyncCallback
     */
    export interface AsyncCallback<T> {
        /**
         * Defines an asynchronous callback that carries an error parameter and asynchronous return value.
         *
         * @param { Error } err - Error message returned when the API fails to be called.
         * @param { T } data - Callback invoked when the API is called.
         * @syscap SystemCapability.Global.ResourceManager
         * @since 6
         * @deprecated since 9
         * @useinstead @ohos.base:AsyncCallback
         */
        (err: Error, data: T): void;
    }
    /**
     * Obtains the **ResourceManager** object of the current application. This API uses an asynchronous callback to
     * return the result.
     *
     * @param { AsyncCallback<ResourceManager> } callback - Callback used to return the **ResourceManager** object.
     * @syscap SystemCapability.Global.ResourceManager
     * @FAModelOnly
     * @since 6
     */
    export function getResourceManager(callback: AsyncCallback<ResourceManager>): void;
    /**
     * Obtains the **ResourceManager** object of the specified application. This API uses an asynchronous callback to
     * return the result.
     *
     * @param { string } bundleName - Bundle name of the application.
     * @param { AsyncCallback<ResourceManager> } callback - Callback used to return the **ResourceManager** object.
     * @syscap SystemCapability.Global.ResourceManager
     * @FAModelOnly
     * @since 6
     */
    export function getResourceManager(bundleName: string, callback: AsyncCallback<ResourceManager>): void;
    /**
     * Obtains the **ResourceManager** object of the current application. This API uses a promise to return the result.
     *
     * @returns { Promise<ResourceManager> } Promise used to return the **ResourceManager** object.
     * @syscap SystemCapability.Global.ResourceManager
     * @FAModelOnly
     * @since 6
     */
    export function getResourceManager(): Promise<ResourceManager>;
    /**
     * Obtains the **ResourceManager** object of the specified application. This API uses a promise to return the result.
     *
     * @param { string } bundleName - Bundle name of the application.
     * @returns { Promise<ResourceManager> } Promise used to return the **ResourceManager** object.
     * @syscap SystemCapability.Global.ResourceManager
     * @FAModelOnly
     * @since 6
     */
    export function getResourceManager(bundleName: string): Promise<ResourceManager>;
    /**
     * Obtains a system resource management object for accessing preset system resources.
     *
     * > **NOTE**
     * >
     * > The **Configuration** parameter in the **ResourceManager** object obtained via this API uses the default value.
     * > The default value is
     * > **{"locale": "", "direction": -1, "deviceType": -1, "screenDensity": 0, "colorMode": 1, "mcc": 0, "mnc": 0}**.
     *
     * @returns { ResourceManager } The system **ResourceManager** object.
     * @throws { BusinessError } 9001009 - Failed to access the system resource.
     *     which is not mapped to application sandbox, This error code will be thrown.
     * @syscap SystemCapability.Global.ResourceManager
     * @crossplatform [since 11]
     * @atomicservice [since 11]
     * @since 10
     * @deprecated since 20
     * @useinstead resourceManager.getSysResourceManager
     */
    export function getSystemResourceManager(): ResourceManager;
    /**
     * Obtains a system resource management object for accessing preset system resources.
     *
     * @returns { ResourceManager } The system **ResourceManager** object.
     * @throws { BusinessError } 9001009 - Failed to access the system resource.
     *     which is not mapped to application sandbox, This error code will be thrown.
     * @syscap SystemCapability.Global.ResourceManager
     * @crossplatform
     * @atomicservice
     * @since 20
     */
    export function getSysResourceManager(): ResourceManager;
    /**
     * Provides the capability of accessing application resources and system resources. The accessible resources include
     * the resources in the HAP/HSP module corresponding to the current context and all system resources.
     *
     * > **NOTE**
     * >
     * > - The methods involved in **ResourceManager** are applicable only to the TypeScript-based declarative
     * > development paradigm.
     * >
     * > - Resource files are defined in the **resources** directory of the project. You can obtain resource values such
     * > as strings, string arrays, and colors based on the specified **resName**, **resId**, or **Resource** object.
     * > **resName** indicates the resource name, **resId** indicates the resource ID, which can be obtained through
     * > `$r(*resource-address*).id`, for example, `$r('app.string.test').id`.
     * >
     * > - No matter whether resources are in the same HAP or different HAPs or HSPs, you are advised to use the API with
     * > **resName** or **resId** specified. Using the **Resource** object will take a longer time. If the resources are
     * > in different HAPs or HSPs, you first need to use
     * > [createModuleContext]{@link @ohos.app.ability.application:application.createModuleContext} to create the context
     * > of the corresponding module and then call the API with **resName** or **resId** specified. For more information,
     * > see [Accessing Resources](docroot://quick-start/resource-categories-and-access.md#accessing-resources).
     * >
     * > - In API version 22 and earlier versions, an exception is thrown due to an invalid ID when the intermediate-code
     * > HAR or bytecode HAR accesses resources through resource ID-related APIs. From API version 23, the intermediate-
     * > code HAR or bytecode HAR can properly access resources through resource ID-related APIs. For details, see
     * > [Accessing Resources](docroot://quick-start/resource-categories-and-access.md#accessing-resources).
     *
     * @syscap SystemCapability.Global.ResourceManager
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 6
     */
    export interface ResourceManager {
        /**
         * Obtains the string corresponding to the specified resource ID. This API uses an asynchronous callback to return
         * the result.
         *
         * @param { number } resId - Resource ID.
         * @param { AsyncCallback<string> } callback - Callback used to return the obtained string.
         * @syscap SystemCapability.Global.ResourceManager
         * @since 6
         * @deprecated since 9
         * @useinstead resourceManager.ResourceManager.getStringValue(resId: long, callback: _AsyncCallback<string>)
         */
        getString(resId: number, callback: AsyncCallback<string>): void;
        /**
         * Obtains the string corresponding to the specified resource ID. This API uses a promise to return the result.
         *
         * @param { number } resId - Resource ID.
         * @returns { Promise<string> } Promise used to return the obtained string.
         * @syscap SystemCapability.Global.ResourceManager
         * @since 6
         * @deprecated since 9
         * @useinstead resourceManager.ResourceManager.getStringValue(resId: long)
         */
        getString(resId: number): Promise<string>;
        /**
         * Obtains the string corresponding to the specified resource object. This API uses an asynchronous callback to
         * return the result.
         *
         * @param { Resource } resource - Resource object.
         * @param { _AsyncCallback<string> } callback - Callback used to return the obtained string.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @syscap SystemCapability.Global.ResourceManager
         * @stagemodelonly
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         * @deprecated since 20
         * @useinstead resourceManager.ResourceManager.getStringValue(resId: long, callback: _AsyncCallback<string>)
         */
        getStringValue(resource: Resource, callback: _AsyncCallback<string>): void;
        /**
         * Obtains the string corresponding to the specified resource object. This API uses a promise to return the result.
         *
         * @param { Resource } resource - Resource object.
         * @returns { Promise<string> } Promise used to return the obtained string.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @syscap SystemCapability.Global.ResourceManager
         * @stagemodelonly
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         * @deprecated since 20
         * @useinstead resourceManager.ResourceManager.getStringValue(resId: long)
         */
        getStringValue(resource: Resource): Promise<string>;
        /**
         * Obtains the string array corresponding to the specified resource ID. This API uses an asynchronous callback to
         * return the result.
         *
         * @param { number } resId - Resource ID.
         * @param { AsyncCallback<Array<string>> } callback - Callback used to return the obtained string array.
         * @syscap SystemCapability.Global.ResourceManager
         * @since 6
         * @deprecated since 9
         * @useinstead resourceManager.ResourceManager.getStringArrayValue(resId: long, callback: _AsyncCallback<Array<string>>)
         */
        getStringArray(resId: number, callback: AsyncCallback<Array<string>>): void;
        /**
         * Obtains the string array corresponding to the specified resource ID. This API uses a promise to return the
         * result.
         *
         * @param { number } resId - Resource ID.
         * @returns { Promise<Array<string>> } Promise used to return the obtained string array.
         * @syscap SystemCapability.Global.ResourceManager
         * @since 6
         * @deprecated since 9
         * @useinstead resourceManager.ResourceManager.getStringArrayValue(resId: long)
         */
        getStringArray(resId: number): Promise<Array<string>>;
        /**
         * Obtains the string array corresponding to the specified resource object. This API uses an asynchronous callback
         * to return the result.
         *
         * @param { Resource } resource - Resource object.
         * @param { _AsyncCallback<Array<string>> } callback - Callback used to return the obtained string array.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @syscap SystemCapability.Global.ResourceManager
         * @stagemodelonly
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         * @deprecated since 20
         * @useinstead resourceManager.ResourceManager.getStringArrayValue(resId: long, callback: _AsyncCallback<Array<string>>)
         */
        getStringArrayValue(resource: Resource, callback: _AsyncCallback<Array<string>>): void;
        /**
         * Obtains the string array corresponding to the specified resource object. This API uses a promise to return the
         * result.
         *
         * @param { Resource } resource - Resource object.
         * @returns { Promise<Array<string>> } Promise used to return the obtained string array.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @syscap SystemCapability.Global.ResourceManager
         * @stagemodelonly
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         * @deprecated since 20
         * @useinstead resourceManager.ResourceManager.getStringArrayValue(resId: long)
         */
        getStringArrayValue(resource: Resource): Promise<Array<string>>;
        /**
         * Obtains the content of the media file corresponding to the specified resource ID. This API uses an asynchronous
         * callback to return the result.
         *
         * @param { number } resId - Resource ID.
         * @param { AsyncCallback<Uint8Array> } callback - Callback used to return the media file content.
         * @syscap SystemCapability.Global.ResourceManager
         * @since 6
         * @deprecated since 9
         * @useinstead resourceManager.ResourceManager.getMediaContent(resId: long, callback: _AsyncCallback<Uint8Array>)
         */
        getMedia(resId: number, callback: AsyncCallback<Uint8Array>): void;
        /**
         * Obtains the content of the media file corresponding to the specified resource ID. This API uses a promise to
         * return the result.
         *
         * @param { number } resId - Resource ID.
         * @returns { Promise<Uint8Array> } Promise used to return the media file content.
         * @syscap SystemCapability.Global.ResourceManager
         * @since 6
         * @deprecated since 9
         * @useinstead resourceManager.ResourceManager.getMediaContent(resId: long)
         */
        getMedia(resId: number): Promise<Uint8Array>;
        /**
         * Obtains the content of the media file corresponding to the specified resource object. This API uses an
         * asynchronous callback to return the result.
         *
         * @param { Resource } resource - Resource object.
         * @param { _AsyncCallback<Uint8Array> } callback - Callback used to return the media file content.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @syscap SystemCapability.Global.ResourceManager
         * @stagemodelonly
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         * @deprecated since 20
         * @useinstead resourceManager.ResourceManager.getMediaContent(resId: long, callback: _AsyncCallback<Uint8Array>)
         */
        getMediaContent(resource: Resource, callback: _AsyncCallback<Uint8Array>): void;
        /**
         * Obtains the media file content for the specified screen density based on the specified resource object. This API
         * uses an asynchronous callback to return the result.
         *
         * @param { Resource } resource - Resource object.
         * @param { number } density - Screen density. The value **0** indicates the default screen density. For details
         *     about the values, see [ScreenDensity]{@link resourceManager.ScreenDensity}.
         * @param { _AsyncCallback<Uint8Array> } callback - Callback used to return the media file content.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Incorrect parameter types; 2
         *     .Parameter verification failed.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @syscap SystemCapability.Global.ResourceManager
         * @stagemodelonly
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 10
         * @deprecated since 20
         * @useinstead resourceManager.ResourceManager.getMediaContent(resId: long, density: int, callback: _AsyncCallback<Uint8Array>)
         */
        getMediaContent(resource: Resource, density: number, callback: _AsyncCallback<Uint8Array>): void;
        /**
         * Obtains the content of the media file corresponding to the specified resource object. This API uses a promise to
         * return the result.
         *
         * @param { Resource } resource - Resource object.
         * @returns { Promise<Uint8Array> } Promise used to return the media file content.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @syscap SystemCapability.Global.ResourceManager
         * @stagemodelonly
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         * @deprecated since 20
         * @useinstead resourceManager.ResourceManager.getMediaContent(resId: long)
         */
        getMediaContent(resource: Resource): Promise<Uint8Array>;
        /**
         * Obtains the media file content for the specified screen density based on the specified resource object. This API
         * uses a promise to return the result.
         *
         * @param { Resource } resource - Resource object.
         * @param { number } density - Screen density. The value **0** indicates the default screen density. For details
         *     about the values, see [ScreenDensity]{@link resourceManager.ScreenDensity}.
         * @returns { Promise<Uint8Array> } Promise used to return the media file content.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Incorrect parameter types; 2
         *     .Parameter verification failed.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @syscap SystemCapability.Global.ResourceManager
         * @stagemodelonly
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 10
         * @deprecated since 20
         * @useinstead resourceManager.ResourceManager.getMediaContent(resId: long, density: int)
         */
        getMediaContent(resource: Resource, density: number): Promise<Uint8Array>;
        /**
         * Obtains the Base64 encoding of the image resource corresponding to the specified resource ID. This API uses an
         * asynchronous callback to return the result.
         *
         * @param { number } resId - Resource ID.
         * @param { AsyncCallback<string> } callback - Callback used to return the Base64 encoding of the image.
         * @syscap SystemCapability.Global.ResourceManager
         * @since 6
         * @deprecated since 9
         * @useinstead resourceManager.ResourceManager.getMediaContentBase64(resId: long, callback: _AsyncCallback<string>)
         */
        getMediaBase64(resId: number, callback: AsyncCallback<string>): void;
        /**
         * Obtains the Base64 encoding of the image resource corresponding to the specified resource ID. This API uses a
         * promise to return the result.
         *
         * @param { number } resId - Resource ID.
         * @returns { Promise<string> } Promise used to return the Base64 encoding of the image.
         * @syscap SystemCapability.Global.ResourceManager
         * @since 6
         * @deprecated since 9
         * @useinstead resourceManager.ResourceManager.getMediaContentBase64(resId: long)
         */
        getMediaBase64(resId: number): Promise<string>;
        /**
         * Obtains the Base64 encoding of the image resource corresponding to the specified resource object. This API uses
         * an asynchronous callback to return the result.
         *
         * @param { Resource } resource - Resource object.
         * @param { _AsyncCallback<string> } callback - Callback used to return the Base64 encoding of the image.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @syscap SystemCapability.Global.ResourceManager
         * @stagemodelonly
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         * @deprecated since 20
         * @useinstead resourceManager.ResourceManager.getMediaContentBase64(resId: long, callback: _AsyncCallback<string>)
         */
        getMediaContentBase64(resource: Resource, callback: _AsyncCallback<string>): void;
        /**
         * Obtains the Base64 encoding of the image resource corresponding to the specified resource object and the
         * specified screen density. This API uses an asynchronous callback to return the result.
         *
         * @param { Resource } resource - Resource object.
         * @param { number } density - Screen density. The value **0** indicates the default screen density. For details
         *     about the values, see [ScreenDensity]{@link resourceManager.ScreenDensity}.
         * @param { _AsyncCallback<string> } callback - Callback used to return the Base64 encoding of the image.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Incorrect parameter types; 2
         *     .Parameter verification failed.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @syscap SystemCapability.Global.ResourceManager
         * @stagemodelonly
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 10
         * @deprecated since 20
         * @useinstead resourceManager.ResourceManager.getMediaContentBase64(resId: long, density: int, callback: _AsyncCallback<string>)
         */
        getMediaContentBase64(resource: Resource, density: number, callback: _AsyncCallback<string>): void;
        /**
         * Obtains the Base64 encoding of the image resource corresponding to the specified resource object. This API uses
         * a promise to return the result.
         *
         * @param { Resource } resource - Resource object.
         * @returns { Promise<string> } Promise used to return the Base64 encoding of the image.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @syscap SystemCapability.Global.ResourceManager
         * @stagemodelonly
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         * @deprecated since 20
         * @useinstead resourceManager.ResourceManager.getMediaContentBase64(resId: long)
         */
        getMediaContentBase64(resource: Resource): Promise<string>;
        /**
         * Obtains the Base64 encoding of the image resource corresponding to the specified resource object and the
         * specified screen density. This API uses a promise to return the result.
         *
         * @param { Resource } resource - Resource object.
         * @param { number } density - Screen density. The value **0** indicates the default screen density. For details
         *     about the values, see [ScreenDensity]{@link resourceManager.ScreenDensity}.
         * @returns { Promise<string> } Promise used to return the Base64 encoding of the image.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Incorrect parameter types; 2
         *     .Parameter verification failed.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @syscap SystemCapability.Global.ResourceManager
         * @stagemodelonly
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 10
         * @deprecated since 20
         * @useinstead resourceManager.ResourceManager.getMediaContentBase64(resId: long, density: int)
         */
        getMediaContentBase64(resource: Resource, density: number): Promise<string>;
        /**
         * Obtains the device capabilities of a device. This API uses an asynchronous callback to return the result.
         *
         * @param { _AsyncCallback<DeviceCapability> } callback - Callback used to return the device capability.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        getDeviceCapability(callback: _AsyncCallback<DeviceCapability>): void;
        /**
         * Obtains the device capabilities of a device. This API uses a promise to return the result.
         *
         * @returns { Promise<DeviceCapability> } Promise used to return the device capability.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        getDeviceCapability(): Promise<DeviceCapability>;
        /**
         * Obtains the configuration of a device. This API uses an asynchronous callback to return the result.
         *
         * @param { _AsyncCallback<Configuration> } callback - Callback used to return the device configuration.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        getConfiguration(callback: _AsyncCallback<Configuration>): void;
        /**
         * Obtains the configuration of a device. This API uses a promise to return the result.
         *
         * @returns { Promise<Configuration> } Promise used to return the device configuration.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 6
         */
        getConfiguration(): Promise<Configuration>;
        /**
         * Obtains the plural string based on the specified resource ID and the specified resource quantity. This API uses
         * an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > Strings distinguish between singular and plural forms in all languages except Chinese. For details, see
         * > [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).
         *
         * @param { number } resId - Resource ID.
         * @param { number } num - Quantity value, used to obtain the corresponding string representation based on the
         *     current language's
         *     [plural rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).
         * @param { AsyncCallback<string> } callback - Callback used to return the obtained singular/plural string.
         * @syscap SystemCapability.Global.ResourceManager
         * @since 6
         * @deprecated since 9
         * @useinstead resourceManager.ResourceManager.getPluralStringValue(resId: number, num: number, callback: _AsyncCallback<string>)
         */
        getPluralString(resId: number, num: number, callback: AsyncCallback<string>): void;
        /**
         * Obtains the plural string based on the specified resource ID and the specified resource quantity. This API uses
         * a promise to return the result.
         *
         * > **NOTE**
         * >
         * > Strings distinguish between singular and plural forms in all languages except Chinese. For details, see
         * > [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).
         *
         * @param { number } resId - Resource ID.
         * @param { number } num - Quantity value, used to obtain the corresponding string representation based on the
         *     current language's
         *     [plural rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).
         * @returns { Promise<string> } Promise used to return the obtained singular/plural string.
         * @syscap SystemCapability.Global.ResourceManager
         * @since 6
         * @deprecated since 9
         * @useinstead resourceManager.ResourceManager.getPluralStringValue(resId: number, num: number)
         */
        getPluralString(resId: number, num: number): Promise<string>;
        /**
         * Obtains the plural string based on the specified resource information and the specified resource quantity. This
         * API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > Strings distinguish between singular and plural forms in all languages except Chinese. For details, see
         * > [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).
         *
         * @param { Resource } resource - Resource object.
         * @param { number } num - Quantity value, used to obtain the corresponding string representation based on the
         *     current language's
         *     [plural rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).
         * @param { _AsyncCallback<string> } callback - Callback used to return the obtained singular/plural string.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @syscap SystemCapability.Global.ResourceManager
         * @stagemodelonly
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         * @deprecated since 18
         * @useinstead resourceManager.ResourceManager.getIntPluralStringValueSync(resId: number, num: number,...args: Array<string | number>)
         */
        getPluralStringValue(resource: Resource, num: number, callback: _AsyncCallback<string>): void;
        /**
         * Obtains the plural string based on the specified resource information and the specified resource quantity. This
         * API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > Strings distinguish between singular and plural forms in all languages except Chinese. For details, see
         * > [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).
         *
         * @param { Resource } resource - Resource object.
         * @param { number } num - Quantity value, used to obtain the corresponding string representation based on the
         *     current language's
         *     [plural rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).
         * @returns { Promise<string> } Promise used to return the obtained singular/plural string.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @syscap SystemCapability.Global.ResourceManager
         * @stagemodelonly
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         * @deprecated since 18
         * @useinstead resourceManager.ResourceManager.getIntPluralStringValueSync(resId: number, num: number,...args: Array<string | number>)
         */
        getPluralStringValue(resource: Resource, num: number): Promise<string>;
        /**
         * Obtain the content of a rawfile in the **resources/rawfile** directory. This API uses an asynchronous callback
         * to return the result.
         *
         * @param { string } path - rawfile path relative to the **resources/rawfile** directory, such as **test.txt** or
         *     **subdir/test.txt**. The path must not start with a slash (/).
         * @param { AsyncCallback<Uint8Array> } callback - Callback used to return the rawfile content.
         * @syscap SystemCapability.Global.ResourceManager
         * @since 8
         * @deprecated since 9
         * @useinstead resourceManager.ResourceManager.getRawFileContent(path: string, callback: _AsyncCallback<Uint8Array>)
         */
        getRawFile(path: string, callback: AsyncCallback<Uint8Array>): void;
        /**
         * Obtain the content of a rawfile in the **resources/rawfile** directory. This API uses a promise to return the
         * result.
         *
         * @param { string } path - rawfile path relative to the **resources/rawfile** directory, such as **test.txt** or
         *     **subdir/test.txt**. The path must not start with a slash (/).
         * @returns { Promise<Uint8Array> } Promise used to return the rawfile content.
         * @syscap SystemCapability.Global.ResourceManager
         * @since 8
         * @deprecated since 9
         * @useinstead resourceManager.ResourceManager.getRawFileContent(path: string)
         */
        getRawFile(path: string): Promise<Uint8Array>;
        /**
         * Obtains the file descriptor (fd) of a specific rawfile in the **resources/rawfile** directory. This API uses an
         * asynchronous callback to return the result.
         *
         * @param { string } path - rawfile path relative to the **resources/rawfile** directory, such as **test.txt** or
         *     **subdir/test.txt**. The path must not start with a slash (/).
         * @param { AsyncCallback<RawFileDescriptor> } callback - Callback used to return the obtained fd.
         * @syscap SystemCapability.Global.ResourceManager
         * @since 8
         * @deprecated since 9
         * @useinstead resourceManager.ResourceManager.getRawFd(path: string, callback: _AsyncCallback<RawFileDescriptor>)
         */
        getRawFileDescriptor(path: string, callback: AsyncCallback<RawFileDescriptor>): void;
        /**
         * Obtains the file descriptor (fd) of a specific rawfile in the **resources/rawfile** directory. This API uses a
         * promise to return the result.
         *
         * @param { string } path - rawfile path relative to the **resources/rawfile** directory, such as **test.txt** or
         *     **subdir/test.txt**. The path must not start with a slash (/).
         * @returns { Promise<RawFileDescriptor> } Promise used to return the obtained fd.
         * @syscap SystemCapability.Global.ResourceManager
         * @since 8
         * @deprecated since 9
         * @useinstead resourceManager.ResourceManager.getRawFd(path: string)
         */
        getRawFileDescriptor(path: string): Promise<RawFileDescriptor>;
        /**
         * Closes the file descriptor (fd) of a specific rawfile in the **resources/rawfile** directory. This API uses an
         * asynchronous callback to return the result.
         *
         * @param { string } path - rawfile path relative to the **resources/rawfile** directory, such as **test.txt** or
         *     **subdir/test.txt**. The path must not start with a slash (/).
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**. Otherwise, **err** is an error object.
         * @syscap SystemCapability.Global.ResourceManager
         * @since 8
         * @deprecated since 9
         * @useinstead resourceManager.ResourceManager.closeRawFd(path: string, callback: _AsyncCallback<void>)
         */
        closeRawFileDescriptor(path: string, callback: AsyncCallback<void>): void;
        /**
         * Closes the file descriptor (fd) of a specific rawfile in the **resources/rawfile** directory. This API uses a
         * promise to return the result.
         *
         * @param { string } path - rawfile path relative to the **resources/rawfile** directory, such as **test.txt** or
         *     **subdir/test.txt**. The path must not start with a slash (/).
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Global.ResourceManager
         * @since 8
         * @deprecated since 9
         * @useinstead resourceManager.ResourceManager.closeRawFd(path: string)
         */
        closeRawFileDescriptor(path: string): Promise<void>;
        /**
         * Obtains the string corresponding to the specified resource name. This API uses an asynchronous callback to
         * return the result.
         *
         * @param { string } resName - Resource name.
         * @param { _AsyncCallback<string> } callback - Callback used to return the obtained string.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001003 - Invalid resource name.
         * @throws { BusinessError } 9001004 - No matching resource is found based on the resource name.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        getStringByName(resName: string, callback: _AsyncCallback<string>): void;
        /**
         * Obtains the string corresponding to the specified resource name. This API uses a promise to return the result.
         *
         * @param { string } resName - Resource name.
         * @returns { Promise<string> } Promise used to return the obtained string.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001003 - Invalid resource name.
         * @throws { BusinessError } 9001004 - No matching resource is found based on the resource name.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        getStringByName(resName: string): Promise<string>;
        /**
         * Obtains the string array corresponding to the specified resource name. This API uses an asynchronous callback to
         * return the result.
         *
         * @param { string } resName - Resource name.
         * @param { _AsyncCallback<Array<string>> } callback - Callback used to return the obtained string array.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001003 - Invalid resource name.
         * @throws { BusinessError } 9001004 - No matching resource is found based on the resource name.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        getStringArrayByName(resName: string, callback: _AsyncCallback<Array<string>>): void;
        /**
         * Obtains the string array corresponding to the specified resource name. This API uses a promise to return the
         * result.
         *
         * @param { string } resName - Resource name.
         * @returns { Promise<Array<string>> } Promise used to return the obtained string array.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001003 - Invalid resource name.
         * @throws { BusinessError } 9001004 - No matching resource is found based on the resource name.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        getStringArrayByName(resName: string): Promise<Array<string>>;
        /**
         * Obtains the content of the media file corresponding to the specified resource name. This API uses an
         * asynchronous callback to return the result.
         *
         * @param { string } resName - Resource name.
         * @param { _AsyncCallback<Uint8Array> } callback - Callback used to return the media file content.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001003 - Invalid resource name.
         * @throws { BusinessError } 9001004 - No matching resource is found based on the resource name.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        getMediaByName(resName: string, callback: _AsyncCallback<Uint8Array>): void;
        /**
         * Obtains the media file content for the specified screen density based on the specified resource name. This API
         * uses an asynchronous callback to return the result.
         *
         * @param { string } resName - Resource name.
         * @param { number } density - Screen density. The value **0** indicates the default screen density. For details about
         *     the values, see [ScreenDensity]{@link resourceManager.ScreenDensity}.
         * @param { _AsyncCallback<Uint8Array> } callback - Callback used to return the media file content.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Incorrect parameter types;
         *     2.Parameter verification failed.
         * @throws { BusinessError } 9001003 - Invalid resource name.
         * @throws { BusinessError } 9001004 - No matching resource is found based on the resource name.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 10
         */
        getMediaByName(resName: string, density: number, callback: _AsyncCallback<Uint8Array>): void;
        /**
         * Obtains the content of the media file corresponding to the specified resource name. This API uses a promise to
         * return the result.
         *
         * @param { string } resName - Resource name.
         * @returns { Promise<Uint8Array> } Promise used to return the media file content.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001003 - Invalid resource name.
         * @throws { BusinessError } 9001004 - No matching resource is found based on the resource name.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        getMediaByName(resName: string): Promise<Uint8Array>;
        /**
         * Obtains the media file content for the specified screen density based on the specified resource name. This API
         * uses a promise to return the result.
         *
         * @param { string } resName - Resource name.
         * @param { number } density - Screen density. The value **0** indicates the default screen density. For details about
         *     the values, see [ScreenDensity]{@link resourceManager.ScreenDensity}.
         * @returns { Promise<Uint8Array> } Promise used to return the media file content.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Incorrect parameter types;
         *     2.Parameter verification failed.
         * @throws { BusinessError } 9001003 - Invalid resource name.
         * @throws { BusinessError } 9001004 - No matching resource is found based on the resource name.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 10
         */
        getMediaByName(resName: string, density: number): Promise<Uint8Array>;
        /**
         * Obtains the Base64 encoding of the image resource corresponding to the specified resource name. This API uses an
         * asynchronous callback to return the result.
         *
         * @param { string } resName - Resource name.
         * @param { _AsyncCallback<string> } callback - Callback used to return the Base64 encoding of the image.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001003 - Invalid resource name.
         * @throws { BusinessError } 9001004 - No matching resource is found based on the resource name.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        getMediaBase64ByName(resName: string, callback: _AsyncCallback<string>): void;
        /**
         * Obtains the Base64 encoding of the image resource for the specified screen density corresponding to the
         * specified resource name. This API uses an asynchronous callback to return the result.
         *
         * @param { string } resName - Resource name.
         * @param { number } density - Screen density. The value **0** indicates the default screen density. For details about
         *     the values, see [ScreenDensity]{@link resourceManager.ScreenDensity}.
         * @param { _AsyncCallback<string> } callback - Callback used to return the Base64 encoding of the image.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Incorrect parameter types;
         *     2.Parameter verification failed.
         * @throws { BusinessError } 9001003 - Invalid resource name.
         * @throws { BusinessError } 9001004 - No matching resource is found based on the resource name.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 10
         */
        getMediaBase64ByName(resName: string, density: number, callback: _AsyncCallback<string>): void;
        /**
         * Obtains the Base64 encoding of the image resource corresponding to the specified resource name. This API uses a
         * promise to return the result.
         *
         * @param { string } resName - Resource name.
         * @returns { Promise<string> } Promise used to return the Base64 encoding of the image.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001003 - Invalid resource name.
         * @throws { BusinessError } 9001004 - No matching resource is found based on the resource name.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        getMediaBase64ByName(resName: string): Promise<string>;
        /**
         * Obtains the Base64 encoding of the image resource for the specified screen density corresponding to the
         * specified resource name. This API uses a promise to return the result.
         *
         * @param { string } resName - Resource name.
         * @param { number } density - Screen density. The value **0** indicates the default screen density. For details about
         *     the values, see [ScreenDensity]{@link resourceManager.ScreenDensity}.
         * @returns { Promise<string> } Promise used to return the Base64 encoding of the image.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Incorrect parameter types;
         *     2.Parameter verification failed.
         * @throws { BusinessError } 9001003 - Invalid resource name.
         * @throws { BusinessError } 9001004 - No matching resource is found based on the resource name.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 10
         */
        getMediaBase64ByName(resName: string, density: number): Promise<string>;
        /**
         * Obtains the plural string based on the specified resource name and the specified resource quantity. This API
         * uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > Strings distinguish between singular and plural forms in all languages except Chinese. For details, see
         * > [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).
         *
         * @param { string } resName - Resource name.
         * @param { number } num - Quantity value, used to obtain the corresponding string representation based on the
         *     current language's
         *     [plural rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).
         * @param { _AsyncCallback<string> } callback - Callback used to return the obtained singular/plural string.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001003 - Invalid resource name.
         * @throws { BusinessError } 9001004 - No matching resource is found based on the resource name.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         * @deprecated since 18
         * @useinstead resourceManager.ResourceManager.getIntPluralStringByNameSync(resName: string, num: number, ...args: Array<string | number>)
         */
        getPluralStringByName(resName: string, num: number, callback: _AsyncCallback<string>): void;
        /**
         * Obtains the plural string based on the specified resource name and the specified resource quantity. This API
         * uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > Strings distinguish between singular and plural forms in all languages except Chinese. For details, see
         * > [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).
         *
         * @param { string } resName - Resource name.
         * @param { number } num - Quantity value, used to obtain the corresponding string representation based on the
         *     current language's
         *     [plural rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).
         * @returns { Promise<string> } Promise used to return the result, which is the singular/plural string corresponding
         *     to the specified resource name.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001003 - Invalid resource name.
         * @throws { BusinessError } 9001004 - No matching resource is found based on the resource name.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         * @deprecated since 18
         * @useinstead resourceManager.ResourceManager.getIntPluralStringByNameSync(resName: string, num: number, ...args: Array<string | number>)
         */
        getPluralStringByName(resName: string, num: number): Promise<string>;
        /**
         * Obtains the string corresponding to the specified resource ID. This API returns the result synchronously.
         *
         * @param { number } resId - Resource ID.
         * @returns { string } String corresponding to the specified resource ID.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        getStringSync(resId: number): string;
        /**
         * Obtains the string corresponding to the specified resource ID, and replaces the format placeholders in the
         * string in sequence using the **args** parameter. This API returns the result synchronously.
         *
         * @param { number } resId - Resource ID.
         * @param { Array<string | number> } args - Parameters for the formatted string resource. Supported parameter types
         *     include `%d`, `%f`, `%s`, `%%`, `%number$d`, `%number$f`, and `%number$s`.
         *     <br>**NOTE**
         *     <br>- `%%` is escaped as `%`. For example, `%%d` is formatted as `%d`.
         *     <br>- In `%number$d`, `number` indicates the parameter index, starting from `1`. For example, `%1$d` uses
         *     `args[0]` for formatting, `%2$d` uses `args[1]`, and so on.
         * @returns { string } Formatted string corresponding to the specified resource ID.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @throws { BusinessError } 9001007 - Failed to format the resource obtained based on the resource ID.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform
         * @atomicservice [since 11]
         * @since 10
         */
        getStringSync(resId: number, ...args: Array<string | number>): string;
        /**
         * Obtains a string based on the specified resource object. This API returns the result synchronously.
         *
         * @param { Resource } resource - Resource object.
         * @returns { string } String corresponding to the specified resource object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @syscap SystemCapability.Global.ResourceManager
         * @stagemodelonly
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         * @deprecated since 20
         * @useinstead resourceManager.ResourceManager.getStringSync(resId: long)
         */
        getStringSync(resource: Resource): string;
        /**
         * Obtains the string corresponding to the specified resource object, and replaces the format placeholders in the
         * string in sequence using the **args** parameter. This API returns the result synchronously.
         *
         * @param { Resource } resource - Resource object.
         * @param { Array<string | number> } args - Parameters for the formatted string resource. Supported parameter types
         *     include `%d`, `%f`, `%s`, `%%`, `%number$d`, `%number$f`, and `%number$s`.
         *     <br>**NOTE**
         *     <br>- `%%` is escaped as `%`. For example, `%%d` is formatted as `%d`.
         *     <br>- In `%number$d`, `number` indicates the parameter index, starting from `1`. For example, `%1$d` uses
         *     `args[0]` for formatting, `%2$d` uses `args[1]`, and so on.
         * @returns { string } Formatted string corresponding to the specified resource object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @throws { BusinessError } 9001007 - Failed to format the resource obtained based on the resource ID.
         * @syscap SystemCapability.Global.ResourceManager
         * @stagemodelonly
         * @crossplatform
         * @atomicservice [since 11]
         * @since 10
         * @deprecated since 20
         * @useinstead resourceManager.ResourceManager.getStringSync(resId: number, ...args: Array<string | number>)
         */
        getStringSync(resource: Resource, ...args: Array<string | number>): string;
        /**
         * Obtains the string corresponding to the specified resource name. This API returns the result synchronously.
         *
         * @param { string } resName - Resource name.
         * @returns { string } String corresponding to the specified resource name.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001003 - Invalid resource name.
         * @throws { BusinessError } 9001004 - No matching resource is found based on the resource name.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        getStringByNameSync(resName: string): string;
        /**
         * Obtains the string corresponding to the specified resource name, and replaces the format placeholders in the
         * string in sequence using the **args** parameter. This API returns the result synchronously.
         *
         * @param { string } resName - Resource name.
         * @param { Array<string | number> } args - Parameters for the formatted string resource. Supported parameter types
         *     include `%d`, `%f`, `%s`, `%%`, `%number$d`, `%number$f`, and `%number$s`.
         *     <br>**NOTE**
         *     <br>- `%%` is escaped as `%`. For example, `%%d` is formatted as `%d`.
         *     <br>- In `%number$d`, `number` indicates the parameter index, starting from `1`. For example, `%1$d` uses
         *     `args[0]` for formatting, `%2$d` uses `args[1]`, and so on.
         * @returns { string } Formatted string corresponding to the specified resource name.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001003 - Invalid resource name.
         * @throws { BusinessError } 9001004 - No matching resource is found based on the resource name.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @throws { BusinessError } 9001008 - Failed to format the resource obtained based on the resource name.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform
         * @atomicservice [since 11]
         * @since 10
         */
        getStringByNameSync(resName: string, ...args: Array<string | number>): string;
        /**
         * Obtains a Boolean value based on the specified resource ID. This API returns the result synchronously.
         *
         * @param { number } resId - Resource ID.
         * @returns { boolean } Boolean value.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        getBoolean(resId: number): boolean;
        /**
         * Obtains a Boolean value based on the specified resource object. This API returns the result synchronously.
         *
         * @param { Resource } resource - Resource object.
         * @returns { boolean } Boolean value.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @syscap SystemCapability.Global.ResourceManager
         * @stagemodelonly
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         * @deprecated since 20
         * @useinstead resourceManager.ResourceManager.getBoolean(resId: long)
         */
        getBoolean(resource: Resource): boolean;
        /**
         * Obtains a Boolean value based on the specified resource name. This API returns the result synchronously.
         *
         * @param { string } resName - Resource name.
         * @returns { boolean } Boolean value.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001003 - Invalid resource name.
         * @throws { BusinessError } 9001004 - No matching resource is found based on the resource name.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        getBooleanByName(resName: string): boolean;
        /**
         * Obtains an integer or float number based on the specified resource ID. This API returns the result synchronously.
         *
         * @param { number } resId - Resource ID.
         * @returns { number } Integer or float value corresponding to the specified resource ID.
         *     <br>For resources of the integer type, the original value defined in the resource file is returned.
         *     <br>For resources of the float type, the original value defined in the resource file is returned if no unit
         *     is specified. If the unit is vp or fp, the converted pixel (px) value is returned. The conversion formula is:
         *     Pixel value = Original value × `densityPixels`.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        getNumber(resId: number): number;
        /**
         * Obtains an integer or float number based on the specified resource object. This API returns the result
         * synchronously.
         *
         * @param { Resource } resource - Resource object.
         * @returns { number } Integer or float number.
         *     <br>For resources of the integer type, the original value defined in the resource file is returned.
         *     <br>For resources of the float type, the original value defined in the resource file is returned if no unit
         *     is specified. If the unit is vp or fp, the converted pixel (px) value is returned. The conversion formula is:
         *     Pixel value = Original value × `densityPixels`.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @syscap SystemCapability.Global.ResourceManager
         * @stagemodelonly
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         * @deprecated since 20
         * @useinstead resourceManager.ResourceManager.getNumber(resId: number)
         */
        getNumber(resource: Resource): number;
        /**
         * Obtains an integer or float number based on the specified resource name. This API returns the result
         * synchronously.
         *
         * @param { string } resName - Resource name.
         * @returns { number } Integer or float value corresponding to the specified resource name.
         *     <br>For resources of the integer type, the original value defined in the resource file is returned.
         *     <br>For resources of the float type, the original value defined in the resource file is returned if no unit
         *     is specified. If the unit is vp or fp, the converted pixel (px) value is returned. The conversion formula is:
         *     Pixel value = Original value × `densityPixels`.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001003 - Invalid resource name.
         * @throws { BusinessError } 9001004 - No matching resource is found based on the resource name.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        getNumberByName(resName: string): number;
        /**
         * Releases an **resourceManager **object. This API is not supported currently. Calling this API does not have any
         * effect.
         *
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         * @deprecated since 12
         */
        release();
        /**
         * Obtains the string corresponding to the specified resource ID. This API uses an asynchronous callback to return
         * the result.
         *
         * @param { number } resId - Resource ID.
         * @param { _AsyncCallback<string> } callback - Callback used to return the obtained string.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        getStringValue(resId: number, callback: _AsyncCallback<string>): void;
        /**
         * Obtains the string corresponding to the specified resource ID. This API uses a promise to return the result.
         *
         * @param { number } resId - Resource ID.
         * @returns { Promise<string> } Promise used to return the obtained string.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        getStringValue(resId: number): Promise<string>;
        /**
         * Obtains the string array corresponding to the specified resource ID. This API uses an asynchronous callback to
         * return the result.
         *
         * @param { number } resId - Resource ID.
         * @param { _AsyncCallback<Array<string>> } callback - Callback used to return the obtained string array.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        getStringArrayValue(resId: number, callback: _AsyncCallback<Array<string>>): void;
        /**
         * Obtains the string array corresponding to the specified resource ID. This API uses a promise to return the
         * result.
         *
         * @param { number } resId - Resource ID.
         * @returns { Promise<Array<string>> } Promise used to return the obtained string array.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        getStringArrayValue(resId: number): Promise<Array<string>>;
        /**
         * Obtains the plural string based on the specified resource ID and the specified resource quantity. This API uses
         * an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > Strings distinguish between singular and plural forms in all languages except Chinese. For details, see
         * > [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).
         *
         * @param { number } resId - Resource ID.
         * @param { number } num - Quantity value, used to obtain the corresponding string representation based on the
         *     current language's
         *     [plural rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).
         * @param { _AsyncCallback<string> } callback - Callback used to return the obtained singular/plural string.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         * @deprecated since 18
         * @useinstead resourceManager.ResourceManager.getIntPluralStringValueSync(resId: number, num: number,...args: Array<string | number>)
         */
        getPluralStringValue(resId: number, num: number, callback: _AsyncCallback<string>): void;
        /**
         * Obtains the plural string based on the specified resource ID and the specified resource quantity. This API uses
         * a promise to return the result.
         *
         * > **NOTE**
         * >
         * > Strings distinguish between singular and plural forms in all languages except Chinese. For details, see
         * > [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).
         *
         * @param { number } resId - Resource ID.
         * @param { number } num - Quantity value, used to obtain the corresponding string representation based on the
         *     current language's
         *     [plural rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).
         * @returns { Promise<string> } Promise used to return the obtained singular/plural string.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         * @deprecated since 18
         * @useinstead resourceManager.ResourceManager.getIntPluralStringValueSync(resId: number, num: number,...args: Array<string | number>)
         */
        getPluralStringValue(resId: number, num: number): Promise<string>;
        /**
         * Obtains the [plural](docroot://internationalization/l10n-singular-plural.md) string corresponding to the
         * specified resource ID, and replaces the format placeholders in the string in sequence using the **args**
         * parameters. This API returns the result synchronously.
         *
         * > **NOTE**
         * >
         * > - Strings distinguish between singular and plural forms in all languages except Chinese. For details, see
         * > [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).
         * >
         * > - In languages such as English and German, singular/plural numbers are classified into cardinal numbers (for
         * > example, 1, 2, 3) and ordinal numbers (for example, 1st, 2nd, 3rd). This API applies only to cardinal numbers.
         *
         * @param { number } resId - Resource ID.
         * @param { number } num - Integer number used to obtain the corresponding string representation based on the
         *     current language's
         *     [plural rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).
         * @param { Array<string | number> } args - Parameters for the formatted string resource. Supported parameter types
         *     include `%d`, `%f`, `%s`, `%%`, `%number$d`, `%number$f`, and `%number$s`.
         *     <br>**NOTE**
         *     <br>- `%%` is escaped as `%`. For example, `%%d` is formatted as `%d`.
         *     <br>- In `%number$d`, `number` indicates the parameter index, starting from `1`. For example, `%1$d` uses
         *     `args[0]` for formatting, `%2$d` uses `args[1]`, and so on.
         * @returns { string } Formatted string corresponding to the specified resource ID.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @throws { BusinessError } 9001007 - Failed to format the resource obtained based on the resource ID.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        getIntPluralStringValueSync(resId: number, num: number, ...args: Array<string | number>): string;
        /**
         * Obtains the [plural](docroot://internationalization/l10n-singular-plural.md) string corresponding to the
         * specified resource object, and replaces the format placeholders in the string in sequence using the **args**
         * parameters. This API returns the result synchronously.
         *
         * > **NOTE**
         * >
         * > - Strings distinguish between singular and plural forms in all languages except Chinese. For details, see
         * > [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).
         *
         * @param { Resource } resource - Resource object.
         * @param { number } num - Integer number used to obtain the corresponding string representation based on the
         *     current language's
         *     [plural rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).
         * @param { Array<string | number> } args - Parameters for the formatted string resource. Supported parameter types
         *     include `%d`, `%f`, `%s`, `%%`, `%number$d`, `%number$f`, and `%number$s`.
         *     <br>**NOTE**
         *     <br>- `%%` is escaped as `%`. For example, `%%d` is formatted as `%d`.
         *     <br>- In `%number$d`, `number` indicates the parameter index, starting from `1`. For example, `%1$d` uses
         *     `args[0]` for formatting, `%2$d` uses `args[1]`, and so on.
         * @returns { string } Formatted string corresponding to the specified resource object.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @throws { BusinessError } 9001007 - Failed to format the resource obtained based on the resource ID.
         * @syscap SystemCapability.Global.ResourceManager
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 18
         * @deprecated since 20
         * @useinstead resourceManager.ResourceManager.getIntPluralStringValueSync(resId: number, num: number,...args: Array<string | number>)
         */
        getIntPluralStringValueSync(resource: Resource, num: number, ...args: Array<string | number>): string;
        /**
         * Obtains the [plural](docroot://internationalization/l10n-singular-plural.md) string corresponding to the
         * specified resource name, and replaces the format placeholders in the string in sequence using the **args**
         * parameters. This API returns the result synchronously.
         *
         * > **NOTE**
         * >
         * > - Strings distinguish between singular and plural forms in all languages except Chinese. For details, see
         * > [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).
         * >
         * > - In languages such as English and German, singular/plural numbers are classified into cardinal numbers (for
         * > example, 1, 2, 3) and ordinal numbers (for example, 1st, 2nd, 3rd). This API applies only to cardinal numbers.
         *
         * @param { string } resName - Resource name.
         * @param { number } num - Integer number used to obtain the corresponding string representation based on the
         *     current language's
         *     [plural rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).
         * @param { Array<string | number> } args - Parameters for the formatted string resource. Supported parameter types
         *     include `%d`, `%f`, `%s`, `%%`, `%number$d`, `%number$f`, and `%number$s`.
         *     <br>**NOTE**
         *     <br>- `%%` is escaped as `%`. For example, `%%d` is formatted as `%d`.
         *     <br>- In `%number$d`, `number` indicates the parameter index, starting from `1`. For example, `%1$d` uses
         *     `args[0]` for formatting, `%2$d` uses `args[1]`, and so on.
         * @returns { string } Formatted string corresponding to the specified resource name.
         * @throws { BusinessError } 9001003 - Invalid resource name.
         * @throws { BusinessError } 9001004 - No matching resource is found based on the resource name.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @throws { BusinessError } 9001008 - Failed to format the resource obtained based on the resource name.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        getIntPluralStringByNameSync(resName: string, num: number, ...args: Array<string | number>): string;
        /**
         * Obtains the [plural](docroot://internationalization/l10n-singular-plural.md) string corresponding to the
         * specified resource ID, and replaces the format placeholders in the string in sequence using the **args**
         * parameters. This API returns the result synchronously.
         *
         * > **NOTE**
         * >
         * > - Strings distinguish between singular and plural forms in all languages except Chinese. For details, see
         * > [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).
         * >
         * > - In languages such as English and German, singular/plural numbers are classified into cardinal numbers (for
         * > example, 1, 2, 3) and ordinal numbers (for example, 1st, 2nd, 3rd). This API applies only to cardinal numbers.
         *
         * @param { number } resId - Resource ID.
         * @param { number } num - Quantity value (a floating point number), used to obtain the corresponding string
         *     representation based on the current language's
         *     [plural rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).
         * @param { Array<string | number> } args - Parameters for the formatted string resource. Supported parameter types
         *     include `%d`, `%f`, `%s`, `%%`, `%number$d`, `%number$f`, and `%number$s`.
         *     <br>**NOTE**
         *     <br>- `%%` is escaped as `%`. For example, `%%d` is formatted as `%d`.
         *     <br>- In `%number$d`, `number` indicates the parameter index, starting from `1`. For example, `%1$d` uses
         *     `args[0]` for formatting, `%2$d` uses `args[1]`, and so on.
         * @returns { string } Formatted string corresponding to the specified resource ID.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @throws { BusinessError } 9001007 - Failed to format the resource obtained based on the resource ID.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        getDoublePluralStringValueSync(resId: number, num: number, ...args: Array<string | number>): string;
        /**
         * Obtains the [plural](docroot://internationalization/l10n-singular-plural.md) string corresponding to the
         * specified resource object, and replaces the format placeholders in the string in sequence using the **args**
         * parameters. This API returns the result synchronously.
         *
         * > **NOTE**
         * >
         * > - Strings distinguish between singular and plural forms in all languages except Chinese. For details, see
         * > [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).
         *
         * @param { Resource } resource - Resource object.
         * @param { number } num - Quantity value (a floating point number), used to obtain the corresponding string
         *     representation based on the current language's
         *     [plural rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).
         * @param { Array<string | number> } args - Parameters for the formatted string resource. Supported parameter types
         *     include `%d`, `%f`, `%s`, `%%`, `%number$d`, `%number$f`, and `%number$s`.
         *     <br>**NOTE**
         *     <br>- `%%` is escaped as `%`. For example, `%%d` is formatted as `%d`.
         *     <br>- In `%number$d`, `number` indicates the parameter index, starting from `1`. For example, `%1$d` uses
         *     `args[0]` for formatting, `%2$d` uses `args[1]`, and so on.
         * @returns { string } Formatted string corresponding to the specified resource object.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @throws { BusinessError } 9001007 - Failed to format the resource obtained based on the resource ID.
         * @syscap SystemCapability.Global.ResourceManager
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 18
         * @deprecated since 20
         * @useinstead resourceManager.ResourceManager.getDoublePluralStringValueSync(resId: number, num: number, ...args: Array<string | number>)
         */
        getDoublePluralStringValueSync(resource: Resource, num: number, ...args: Array<string | number>): string;
        /**
         * Obtains the [plural](docroot://internationalization/l10n-singular-plural.md) string corresponding to the
         * specified resource name, and replaces the format placeholders in the string in sequence using the **args**
         * parameters. This API returns the result synchronously.
         *
         * > **NOTE**
         * >
         * > - Strings distinguish between singular and plural forms in all languages except Chinese. For details, see
         * > [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).
         * >
         * > - In languages such as English and German, singular/plural numbers are classified into cardinal numbers (for
         * > example, 1, 2, 3) and ordinal numbers (for example, 1st, 2nd, 3rd). This API applies only to cardinal numbers.
         *
         * @param { string } resName - Resource name.
         * @param { number } num - Quantity value (a floating point number), used to obtain the corresponding string
         *     representation based on the current language's
         *     [plural rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).
         * @param { Array<string | number> } args - Parameters for the formatted string resource. Supported parameter types
         *     include `%d`, `%f`, `%s`, `%%`, `%number$d`, `%number$f`, and `%number$s`.
         *     <br>**NOTE**
         *     <br>- `%%` is escaped as `%`. For example, `%%d` is formatted as `%d`.
         *     <br>- In `%number$d`, `number` indicates the parameter index, starting from `1`. For example, `%1$d` uses
         *     `args[0]` for formatting, `%2$d` uses `args[1]`, and so on.
         * @returns { string } Formatted string corresponding to the specified resource name.
         * @throws { BusinessError } 9001003 - Invalid resource name.
         * @throws { BusinessError } 9001004 - No matching resource is found based on the resource name.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @throws { BusinessError } 9001008 - Failed to format the resource obtained based on the resource name.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        getDoublePluralStringByNameSync(resName: string, num: number, ...args: Array<string | number>): string;
        /**
         * Obtains the content of the media file corresponding to the specified resource ID. This API uses an asynchronous
         * callback to return the result.
         *
         * @param { number } resId - Resource ID.
         * @param { _AsyncCallback<Uint8Array> } callback - Callback used to return the media file content.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        getMediaContent(resId: number, callback: _AsyncCallback<Uint8Array>): void;
        /**
         * Obtains the media file content for the specified screen density based on the specified resource ID. This API
         * uses an asynchronous callback to return the result.
         *
         * @param { number } resId - Resource ID.
         * @param { number } density - Screen density. The value **0** indicates the default screen density. For details about
         *     the values, see [ScreenDensity]{@link resourceManager.ScreenDensity}.
         * @param { _AsyncCallback<Uint8Array> } callback - Callback used to return the media file content.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Incorrect parameter types;
         *     2.Parameter verification failed.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 10
         */
        getMediaContent(resId: number, density: number, callback: _AsyncCallback<Uint8Array>): void;
        /**
         * Obtains the content of the media file corresponding to the specified resource ID. This API uses a promise to
         * return the result.
         *
         * @param { number } resId - Resource ID.
         * @returns { Promise<Uint8Array> } Promise used to return the media file content.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        getMediaContent(resId: number): Promise<Uint8Array>;
        /**
         * Obtains the media file content for the specified screen density based on the specified resource ID. This API
         * uses a promise to return the result.
         *
         * @param { number } resId - Resource ID.
         * @param { number } density - Screen density. The value **0** indicates the default screen density. For details about
         *     the values, see [ScreenDensity]{@link resourceManager.ScreenDensity}.
         * @returns { Promise<Uint8Array> } Promise used to return the media file content.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Incorrect parameter types;
         *     2.Parameter verification failed.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 10
         */
        getMediaContent(resId: number, density: number): Promise<Uint8Array>;
        /**
         * Obtains the Base64 encoding of the image resource corresponding to the specified resource ID. This API uses an
         * asynchronous callback to return the result.
         *
         * @param { number } resId - Resource ID.
         * @param { _AsyncCallback<string> } callback - Callback used to return the Base64 encoding of the image.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        getMediaContentBase64(resId: number, callback: _AsyncCallback<string>): void;
        /**
         * Obtains the Base64 encoding of the image resource corresponding to the specified resource ID and the specified
         * screen density. This API uses an asynchronous callback to return the result.
         *
         * @param { number } resId - Resource ID.
         * @param { number } density - Screen density. The value **0** indicates the default screen density. For details about
         *     the values, see [ScreenDensity]{@link resourceManager.ScreenDensity}.
         * @param { _AsyncCallback<string> } callback - Callback used to return the Base64 encoding of the image.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Incorrect parameter types;
         *     2.Parameter verification failed.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 10
         */
        getMediaContentBase64(resId: number, density: number, callback: _AsyncCallback<string>): void;
        /**
         * Obtains the Base64 encoding of the image resource corresponding to the specified resource ID. This API uses a
         * promise to return the result.
         *
         * @param { number } resId - Resource ID.
         * @returns { Promise<string> } Promise used to return the Base64 encoding of the image.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        getMediaContentBase64(resId: number): Promise<string>;
        /**
         * Obtains the Base64 encoding of the image resource corresponding to the specified resource ID and the specified
         * screen density. This API uses a promise to return the result.
         *
         * @param { number } resId - Resource ID.
         * @param { number } density - Screen density. The value **0** indicates the default screen density. For details about
         *     the values, see [ScreenDensity]{@link resourceManager.ScreenDensity}.
         * @returns { Promise<string> } Promise used to return the Base64 encoding of the image.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Incorrect parameter types;
         *     2.Parameter verification failed.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 10
         */
        getMediaContentBase64(resId: number, density: number): Promise<string>;
        /**
         * Obtain the content of a rawfile in the **resources/rawfile** directory. This API uses an asynchronous callback
         * to return the result.
         *
         * @param { string } path - rawfile path relative to the **resources/rawfile** directory, such as **test.txt** or
         *     **subdir/test.txt**. The path must not start with a slash (/).
         * @param { _AsyncCallback<Uint8Array> } callback - Callback used to return the content of the rawfile.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001005 - Invalid relative path.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        getRawFileContent(path: string, callback: _AsyncCallback<Uint8Array>): void;
        /**
         * Obtain the content of a rawfile in the **resources/rawfile** directory. This API uses a promise to return the
         * result.
         *
         * @param { string } path - rawfile path relative to the **resources/rawfile** directory, such as **test.txt** or
         *     **subdir/test.txt**. The path must not start with a slash (/).
         * @returns { Promise<Uint8Array> } Promise used to return the content of the rawfile.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001005 - Invalid relative path.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        getRawFileContent(path: string): Promise<Uint8Array>;
        /**
         * Obtains the file descriptor (fd) of the HAP where a specific rawfile in the **resources/rawfile** directory is
         * located. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > To prevent resource leakage, call [closeRawFdSync]{@link resourceManager.ResourceManager.closeRawFdSync} or
         * > [closeRawFd]{@link resourceManager.ResourceManager.closeRawFd(path: string, callback: _AsyncCallback<void>)}
         * > to close the fd after use.
         *
         * @param { string } path - rawfile path relative to the **resources/rawfile** directory, such as **test.txt** or
         *     **subdir/test.txt**. The path must not start with a slash (/).
         * @param { _AsyncCallback<RawFileDescriptor> } callback - Callback used to return the fd of the HAP.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001005 - Invalid relative path.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        getRawFd(path: string, callback: _AsyncCallback<RawFileDescriptor>): void;
        /**
         * Obtains the file descriptor (fd) of the HAP where a specific rawfile in the **resources/rawfile** directory is
         * located. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > To prevent resource leakage, call [closeRawFdSync]{@link resourceManager.ResourceManager.closeRawFdSync} or
         * > [closeRawFd]{@link resourceManager.ResourceManager.closeRawFd(path: string, callback: _AsyncCallback<void>)}
         * > to close the fd after use.
         *
         * @param { string } path - rawfile path relative to the **resources/rawfile** directory, such as **test.txt** or
         *     **subdir/test.txt**. The path must not start with a slash (/).
         * @returns { Promise<RawFileDescriptor> } Promise used to return the fd of the HAP.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001005 - Invalid relative path.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        getRawFd(path: string): Promise<RawFileDescriptor>;
        /**
         * Closes the file descriptor (fd) of the HAP where a specific rawfile in the **resources/rawfile** directory is
         * located. This API uses an asynchronous callback to return the result.
         *
         * @param { string } path - rawfile path relative to the **resources/rawfile** directory, such as **test.txt** or
         *     **subdir/test.txt**. The path must not start with a slash (/).
         * @param { _AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001005 - Invalid relative path.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        closeRawFd(path: string, callback: _AsyncCallback<void>): void;
        /**
         * Closes the file descriptor (fd) of the HAP where a specific rawfile in the **resources/rawfile** directory is
         * located. This API uses a promise to return the result.
         *
         * @param { string } path - rawfile path relative to the **resources/rawfile** directory, such as **test.txt** or
         *     **subdir/test.txt**. The path must not start with a slash (/).
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001005 - Invalid relative path.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        closeRawFd(path: string): Promise<void>;
        /**
         * Obtains the **DrawableDescriptor** object for icon display corresponding to the specified resource ID. This API
         * returns the result synchronously.
         *
         * @param { number } resId - Resource ID.
         * @param { number } density - Screen density. The default value or value **0** indicates the default screen density.
         *     For details about the values, see [ScreenDensity]{@link resourceManager.ScreenDensity}.
         * @param { number } type - Icon type. The default value is **0**.
         *     <br>**0**: Icon resource of the application.
         *     <br>**1**: Layered icon resource of the application in the theme resource package.
         * @returns { DrawableDescriptor } **DrawableDescriptor** object corresponding to the specified resource ID.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Incorrect parameter types;
         *     2.Parameter verification failed.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        getDrawableDescriptor(resId: number, density?: number, type?: number): DrawableDescriptor;
        /**
         * Obtains the **DrawableDescriptor** object for icon display corresponding to the specified resource name. This
         * API returns the result synchronously.
         *
         * @param { string } resName - Resource name.
         * @param { number } density - Screen density. The default value or value **0** indicates the default screen density.
         *     For details about the values, see [ScreenDensity]{@link resourceManager.ScreenDensity}.
         * @param { number } type - Icon type. The default value is **0**.
         *     <br>**0**: Icon resource of the application.
         *     <br>**1**: Layered icon resource of the application in the theme resource package.
         * @returns { DrawableDescriptor } **DrawableDescriptor** object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Incorrect parameter types;
         *     2.Parameter verification failed.
         * @throws { BusinessError } 9001003 - Invalid resource name.
         * @throws { BusinessError } 9001004 - No matching resource is found based on the resource name.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        getDrawableDescriptorByName(resName: string, density?: number, type?: number): DrawableDescriptor;
        /**
         * Obtains a **DrawableDescriptor** object for icon display based on the specified resource object. This API
         * returns the result synchronously.
         *
         * @param { Resource } resource - Resource object.
         * @param { number } density - Screen density. The default value or value **0** indicates the default screen
         *     density. For details about the values, see [ScreenDensity]{@link resourceManager.ScreenDensity}.
         * @param { number } type - Icon type. The default value is **0**.
         *     <br>**0**: Icon resource of the application.
         *     <br>**1**: Layered icon resource of the application in the theme resource package.
         * @returns { DrawableDescriptor } **DrawableDescriptor** object corresponding to the specified resource ID.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Incorrect parameter types; 2
         *     .Parameter verification failed.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @syscap SystemCapability.Global.ResourceManager
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         * @deprecated since 20
         * @useinstead resourceManager.ResourceManager.getDrawableDescriptor(resId: long, density?: int, type?: int)
         */
        getDrawableDescriptor(resource: Resource, density?: number, type?: number): DrawableDescriptor;
        /**
         * Obtains the list of directories and files in the specified subdirectory under **resources/rawfile**. This API
         * uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > If there is no folder or file in the directory, an exception is thrown. If there are folders and files in the
         * > directory, the list of the folders and files is returned.
         *
         * @param { string } path - rawfile subdirectory path relative to the **resources/rawfile** directory, such as
         *     **subdir**. The path must not start with a slash (/).
         *     <br>An empty string **""** indicates that the list of directories and files in the **rawfile** root
         *     directory is obtained.
         * @param { _AsyncCallback<Array<string>> } callback - Callback used to return the list of directories and files in
         *     a rawfile subdirectory.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001005 - Invalid relative path.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 10
         */
        getRawFileList(path: string, callback: _AsyncCallback<Array<string>>): void;
        /**
         * Obtains the list of directories and files in the specified subdirectory under **resources/rawfile**. This API
         * uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > If there is no folder or file in the directory, an exception is thrown. If there are folders and files in the
         * > directory, the list of the folders and files is returned.
         *
         * @param { string } path - rawfile subdirectory path relative to the **resources/rawfile** directory, such as
         *     **subdir**. The path must not start with a slash (/).
         *     <br>An empty string **""** indicates that the list of directories and files in the **rawfile** root
         *     directory is obtained.
         * @returns { Promise<Array<string>> } Promise used to return the list of directories and files in a rawfile
         *     subdirectory.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001005 - Invalid relative path.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 10
         */
        getRawFileList(path: string): Promise<Array<string>>;
        /**
         * Obtains the color value corresponding to the specified resource ID. This API uses an asynchronous callback to
         * return the result.
         *
         * @param { number } resId - Resource ID.
         * @param { _AsyncCallback<number> } callback - Callback used to return the color value (decimal).
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 10
         */
        getColor(resId: number, callback: _AsyncCallback<number>): void;
        /**
         * Obtains the color value corresponding to the specified resource ID. This API uses a promise to return the result.
         *
         * @param { number } resId - Resource ID.
         * @returns { Promise<number> } Promise used to return the color value (decimal).
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 10
         */
        getColor(resId: number): Promise<number>;
        /**
         * Obtains the color value corresponding to the specified resource object. This API uses an asynchronous callback
         * to return the result.
         *
         * @param { Resource } resource - Resource object.
         * @param { _AsyncCallback<number> } callback - Callback used to return the color value (decimal).
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @syscap SystemCapability.Global.ResourceManager
         * @stagemodelonly
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 10
         * @deprecated since 20
         * @useinstead resourceManager.ResourceManager.getColor(resId: long, callback: _AsyncCallback<long>)
         */
        getColor(resource: Resource, callback: _AsyncCallback<number>): void;
        /**
         * Obtains the color value corresponding to the specified resource object. This API uses a promise to return the
         * result.
         *
         * @param { Resource } resource - Resource object.
         * @returns { Promise<number> } Promise used to return the color value (decimal).
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @syscap SystemCapability.Global.ResourceManager
         * @stagemodelonly
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 10
         * @deprecated since 20
         * @useinstead resourceManager.ResourceManager.getColor(resId: long)
         */
        getColor(resource: Resource): Promise<number>;
        /**
         * Obtains the color value corresponding to the specified resource name. This API uses an asynchronous callback to
         * return the result.
         *
         * @param { string } resName - Resource name.
         * @param { _AsyncCallback<number> } callback - Callback used to return the color value (decimal).
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001003 - Invalid resource name.
         * @throws { BusinessError } 9001004 - No matching resource is found based on the resource name.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 10
         */
        getColorByName(resName: string, callback: _AsyncCallback<number>): void;
        /**
         * Obtains the color value corresponding to the specified resource name. This API uses a promise to return the
         * result.
         *
         * @param { string } resName - Resource name.
         * @returns { Promise<number> } Promise used to return the color value (decimal).
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001003 - Invalid resource name.
         * @throws { BusinessError } 9001004 - No matching resource is found based on the resource name.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 10
         */
        getColorByName(resName: string): Promise<number>;
        /**
         * Obtains a color value based on the specified resource ID. This API returns the result synchronously.
         *
         * @param { number } resId - Resource ID.
         * @returns { number } Color value (decimal) corresponding to the specified resource ID.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 10
         */
        getColorSync(resId: number): number;
        /**
         * Obtains a color value based on the specified resource object. This API returns the result synchronously.
         *
         * @param { Resource } resource - Resource object.
         * @returns { number } Color value (decimal) corresponding to the specified resource object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @syscap SystemCapability.Global.ResourceManager
         * @stagemodelonly
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 10
         * @deprecated since 20
         * @useinstead resourceManager.ResourceManager.getColorSync(resId: long)
         */
        getColorSync(resource: Resource): number;
        /**
         * Obtains a color value based on the specified resource name. This API returns the result synchronously.
         *
         * @param { string } resName - Resource name.
         * @returns { number } Color value (decimal) corresponding to the specified resource name.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001003 - Invalid resource name.
         * @throws { BusinessError } 9001004 - No matching resource is found based on the resource name.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 10
         */
        getColorByNameSync(resName: string): number;
        /**
         * Loads the specified overlay resource during application runtime to implement theme switching or resource
         * overriding.
         *
         * > **NOTE**
         * >
         * > Resource overwriting is not supported for the **rawfile** and **resfile** directories.
         *
         * @param { string } path - Absolute path of the HSP or HAP resource package to be loaded.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001010 - Invalid overlay path.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 10
         */
        addResource(path: string): void;
        /**
         * Removes the specified overlay resource during application runtime and restores the original resource before the
         * override.
         *
         * > **NOTE**
         * >
         * > Resource overwriting is not supported for the **rawfile** and **resfile** directories.
         *
         * @param { string } path - Absolute path of the HSP or HAP resource package to be removed.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001010 - Invalid overlay path.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 10
         */
        removeResource(path: string): void;
        /**
         * Obtains the file descriptor (fd) of the HAP where the rawfile file in the resources/rawfile directory is located.
         * This API is called in synchronous mode.
         *
         * > **NOTE**
         * >
         * > To prevent resource leakage, call [closeRawFdSync]{@link resourceManager.ResourceManager.closeRawFdSync} or
         * > [closeRawFd]{@link resourceManager.ResourceManager.closeRawFd(path: string, callback: _AsyncCallback<void>)}
         * > to close the fd after use.
         *
         * @param { string } path - rawfile path relative to the **resources/rawfile** directory, such as **test.txt** or
         *     **subdir/test.txt**. The path must not start with a slash (/).
         * @returns { RawFileDescriptor } fd of the HAP where the rawfile is located.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001005 - Invalid relative path.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 10
         */
        getRawFdSync(path: string): RawFileDescriptor;
        /**
         * Closes the file descriptor (fd) of the HAP where the **rawfile** file in the **resources/rawfile** directory is
         * located. This API returns the result synchronously.
         *
         * @param { string } path - rawfile path relative to the **resources/rawfile** directory, such as **test.txt** or
         *     **subdir/test.txt**. The path must not start with a slash (/).
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001005 - Invalid relative path.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 10
         */
        closeRawFdSync(path: string): void;
        /**
         * Obtains the list of directories and files in the specified subdirectory under **resources/rawfile**. This API
         * returns the result synchronously.
         *
         * > **NOTE**
         * >
         * > If there is no folder or file in the directory, an exception is thrown. If there are folders and files in the
         * > directory, the list of the folders and files is returned.
         *
         * @param { string } path - rawfile subdirectory path relative to the **resources/rawfile** directory, such as
         *     **subdir**. The path must not start with a slash (/).
         *     <br>An empty string **""** indicates that the list of directories and files in the **rawfile** root
         *     directory is obtained.
         * @returns { Array<string> } List of folders and files in the **rawfile** directory.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001005 - Invalid relative path.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 10
         */
        getRawFileListSync(path: string): Array<string>;
        /**
         * Obtains the content of a rawfile in the **resources/rawfile** directory. This API returns the result
         * synchronously.
         *
         * @param { string } path - rawfile path relative to the **resources/rawfile** directory, such as **test.txt** or
         *     **subdir/test.txt**. The path must not start with a slash (/).
         * @returns { Uint8Array } Content of the rawfile.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001005 - Invalid relative path.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 10
         */
        getRawFileContentSync(path: string): Uint8Array;
        /**
         * Obtains the media file content for the default or specified screen density based on the specified resource ID.
         * This API returns the result synchronously.
         *
         * @param { number } resId - Resource ID.
         * @param { number } density - Screen density. The default value or value **0** indicates the default screen density.
         *     For details about the values, see [ScreenDensity]{@link resourceManager.ScreenDensity}.
         * @returns { Uint8Array } Content of the media file corresponding to the specified resource ID.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Incorrect parameter types;
         *     2.Parameter verification failed.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 10
         */
        getMediaContentSync(resId: number, density?: number): Uint8Array;
        /**
         * Obtains the media file content for the default or specified screen density based on the specified resource
         * object. This API returns the result synchronously.
         *
         * @param { Resource } resource - Resource object.
         * @param { number } density - Screen density. The default value or value **0** indicates the default screen
         *     density. For details about the values, see [ScreenDensity]{@link resourceManager.ScreenDensity}.
         * @returns { Uint8Array } Content of the media file corresponding to the specified resource object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Incorrect parameter types; 2
         *     .Parameter verification failed.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @syscap SystemCapability.Global.ResourceManager
         * @stagemodelonly
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 10
         * @deprecated since 20
         * @useinstead resourceManager.ResourceManager.getMediaContentSync(resId: long, density?: int)
         */
        getMediaContentSync(resource: Resource, density?: number): Uint8Array;
        /**
         * Obtains an image's Base64 encoding for the default or specified screen density based on the specified resource
         * ID. This API returns the result synchronously.
         *
         * @param { number } resId - Resource ID.
         * @param { number } density - Screen density. The default value or value **0** indicates the default screen density.
         *     For details about the values, see [ScreenDensity]{@link resourceManager.ScreenDensity}.
         * @returns { string } Base64 encoding of the image corresponding to the specified resource ID.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Incorrect parameter types;
         *     2.Parameter verification failed.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 10
         */
        getMediaContentBase64Sync(resId: number, density?: number): string;
        /**
         * Obtains an image's Base64 encoding for the default or specified screen density based on the specified resource
         * object. This API returns the result synchronously.
         *
         * @param { Resource } resource - Resource object.
         * @param { number } density - Screen density. The default value or value **0** indicates the default screen
         *     density. For details about the values, see [ScreenDensity]{@link resourceManager.ScreenDensity}.
         * @returns { string } Base64 encoding of the image corresponding to the specified resource object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1.Incorrect parameter types; 2
         *     .Parameter verification failed.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @syscap SystemCapability.Global.ResourceManager
         * @stagemodelonly
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 10
         * @deprecated since 20
         * @useinstead resourceManager.ResourceManager.getMediaContentBase64Sync(resId: long, density?: int)
         */
        getMediaContentBase64Sync(resource: Resource, density?: number): string;
        /**
         * Obtains singular/plural strings based on the specified resource ID and quantity. This API returns the result
         * synchronously.
         *
         * > **NOTE**
         * >
         * > Strings distinguish between singular and plural forms in all languages except Chinese. For details, see
         * > [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).
         *
         * @param { number } resId - Resource ID.
         * @param { number } num - Quantity value, used to obtain the corresponding string representation based on the
         *     current language's
         *     [plural rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).
         * @returns { string } Singular/plural string corresponding to the specified quantity and resource ID.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 10
         * @deprecated since 18
         * @useinstead resourceManager.ResourceManager.getIntPluralStringValueSync(resId: number, num: number,...args: Array<string | number>)
         */
        getPluralStringValueSync(resId: number, num: number): string;
        /**
         * Obtains singular/plural strings based on the specified quantity and resource object. This API returns the result
         * synchronously.
         *
         * > **NOTE**
         * >
         * > Strings distinguish between singular and plural forms in all languages except Chinese. For details, see
         * > [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).
         *
         * @param { Resource } resource - Resource object.
         * @param { number } num - Quantity value, used to obtain the corresponding string representation based on the
         *     current language's
         *     [plural rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).
         * @returns { string } Singular/plural string corresponding to the specified quantity and resource object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @syscap SystemCapability.Global.ResourceManager
         * @stagemodelonly
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 10
         * @deprecated since 18
         * @useinstead resourceManager.ResourceManager.getIntPluralStringValueSync(resId: number, num: number,...args: Array<string | number>)
         */
        getPluralStringValueSync(resource: Resource, num: number): string;
        /**
         * Obtains the string array corresponding to the specified resource ID. This API returns the result synchronously.
         *
         * @param { number } resId - Resource ID.
         * @returns { Array<string> } String array corresponding to the specified resource ID.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 10
         */
        getStringArrayValueSync(resId: number): Array<string>;
        /**
         * Obtains a string array based on the specified resource object. This API returns the result synchronously.
         *
         * @param { Resource } resource - Resource object.
         * @returns { Array<string> } String array corresponding to the specified resource object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @syscap SystemCapability.Global.ResourceManager
         * @stagemodelonly
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 10
         * @deprecated since 20
         * @useinstead resourceManager.ResourceManager.getStringArrayValueSync(resId: long)
         */
        getStringArrayValueSync(resource: Resource): Array<string>;
        /**
         * Obtains singular/plural strings based on the specified quantity and resource name. This API returns the result
         * synchronously.
         *
         * > **NOTE**
         * >
         * > Strings distinguish between singular and plural forms in all languages except Chinese. For details, see
         * > [Language Plural Rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).
         *
         * @param { string } resName - Resource name.
         * @param { number } num - Quantity value, used to obtain the corresponding string representation based on the
         *     current language's
         *     [plural rules](https://www.unicode.org/cldr/charts/45/supplemental/language_plural_rules.html).
         * @returns { string } Singular/plural string corresponding to the specified quantity and resource name.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001003 - Invalid resource name.
         * @throws { BusinessError } 9001004 - No matching resource is found based on the resource name.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 10
         * @deprecated since 18
         * @useinstead resourceManager.ResourceManager.getIntPluralStringByNameSync(resName: string, num: number, ...args: Array<string | number>)
         */
        getPluralStringByNameSync(resName: string, num: number): string;
        /**
         * Obtains the media file content for the default or specified screen density based on the specified resource name.
         * This API returns the result synchronously.
         *
         * @param { string } resName - Resource name.
         * @param { number } density - Screen density. The default value or value **0** indicates the default screen density.
         *     For details about the values, see [ScreenDensity]{@link resourceManager.ScreenDensity}.
         * @returns { Uint8Array } Promise used to return the result, which is the content of the media file corresponding
         *     to the specified resource name.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Incorrect parameter types;
         *     2.Parameter verification failed.
         * @throws { BusinessError } 9001003 - Invalid resource name.
         * @throws { BusinessError } 9001004 - No matching resource is found based on the resource name.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 10
         */
        getMediaByNameSync(resName: string, density?: number): Uint8Array;
        /**
         * Obtains an image's Base64 encoding for the default or specified screen density based on the specified resource
         * name. This API returns the result synchronously.
         *
         * @param { string } resName - Resource name.
         * @param { number } density - Screen density. The default value or value **0** indicates the default screen density.
         *     For details about the values, see [ScreenDensity]{@link resourceManager.ScreenDensity}.
         * @returns { string } Base64 encoding of the image corresponding to the specified resource name.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Incorrect parameter types;
         *     2.Parameter verification failed.
         * @throws { BusinessError } 9001003 - Invalid resource name.
         * @throws { BusinessError } 9001004 - No matching resource is found based on the resource name.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 10
         */
        getMediaBase64ByNameSync(resName: string, density?: number): string;
        /**
         * Obtains the string array corresponding to the specified resource name. This API returns the result synchronously.
         *
         * @param { string } resName - Resource name.
         * @returns { Array<string> } String array corresponding to the specified resource name.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001003 - Invalid resource name.
         * @throws { BusinessError } 9001004 - No matching resource is found based on the resource name.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 10
         */
        getStringArrayByNameSync(resName: string): Array<string>;
        /**
         * Obtains the device configuration. This API returns the result synchronously.
         *
         * @returns { Configuration } Device configuration.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 10
         */
        getConfigurationSync(): Configuration;
        /**
         * Obtains the device capability. This API returns the result synchronously.
         *
         * @returns { DeviceCapability } Device capability.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 10
         */
        getDeviceCapabilitySync(): DeviceCapability;
        /**
         * Obtains the language list of an application.
         *
         * @param { boolean } [includeSystem] - Whether system resources are included. The default value is **false**.
         *     <br> - **false**: Only application resources are included.
         *     <br> - **true**: Both system and application resources are included.
         *     <br>If the value of **includeSystem** is invalid, the language list of system resources will be returned.
         * @returns { Array<string> } Language list. The strings in the list are comprised of the language, script (optional
         *     ), and region (optional), which are connected by a hyphen (-).
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform
         * @atomicservice
         * @since 11
         */
        getLocales(includeSystem?: boolean): Array<string>;
        /**
         * Obtains the Unicode of a [symbol](https://developer.huawei.com/consumer/en/design/harmonyos-symbol) based on the
         * specified resource ID. This API returns the result synchronously.
         *
         * @param { number } resId - Resource ID.
         * @returns { number } Unicode code (decimal) of the symbol.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform
         * @atomicservice
         * @since 11
         */
        getSymbol(resId: number): number;
        /**
         * Obtains the Unicode of a [symbol](https://developer.huawei.com/consumer/en/design/harmonyos-symbol) based on the
         * specified resource object. This API returns the result synchronously.
         *
         * @param { Resource } resource - Resource object.
         * @returns { number } Unicode code (decimal) of the symbol.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @throws { BusinessError } 9001002 - No matching resource is found based on the resource ID.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @syscap SystemCapability.Global.ResourceManager
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 11
         * @deprecated since 20
         * @useinstead resourceManager.ResourceManager.getSymbol(resId: long)
         */
        getSymbol(resource: Resource): number;
        /**
         * Obtains the Unicode of a [symbol](https://developer.huawei.com/consumer/en/design/harmonyos-symbol) based on the
         * specified resource name. This API returns the result synchronously.
         *
         * @param { string } resName - Resource name.
         * @returns { number } Unicode code (decimal) of the symbol.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001003 - Invalid resource name.
         * @throws { BusinessError } 9001004 - No matching resource is found based on the resource name.
         * @throws { BusinessError } 9001006 - The resource is referenced cyclically.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform
         * @atomicservice
         * @since 11
         */
        getSymbolByName(resName: string): number;
        /**
         * Checks whether a path is a subdirectory in the **rawfile** directory. This API returns the result synchronously.
         *
         * @param { string } path - rawfile or subdirectory path relative to the **resources/rawfile** directory, such as
         *     **test.txt** or **subdir**. The path must not start with a slash (/).
         * @returns { boolean } Whether the path is a subdirectory in the **rawfile** directory.
         *     <br> - **true**: The path is a subdirectory in the **rawfile** directory.
         *     <br> - **false**: The path is not a subdirectory in the **rawfile** directory.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @throws { BusinessError } 9001005 - Invalid relative path.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        isRawDir(path: string): boolean;
        /**
         * Obtains a **ResourceManager** object for loading differentiated resources. This API returns the result
         * synchronously.
         *
         * The resource configuration (including the language, color mode, resolution, and orientation) obtained by a
         * common **ResourceManager** object is determined by the system. With this API, an application can obtain
         * resources of the specified configuration (that is, differentiated resources), for example, dark color resources
         * in light color mode.
         *
         * @param { Configuration } [configuration] - Resource configuration.
         *     <br>After obtaining the configuration of differentiated resources through
         *     [getOverrideConfiguration]{@link resourceManager.ResourceManager.getOverrideConfiguration}, modify the
         *     configuration items as required, and then pass these items as input parameters to the API.
         *     <br>If no configuration is specified, the current system configuration is used.
         * @returns { ResourceManager } **ResourceManager** object for loading differentiated resources.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        getOverrideResourceManager(configuration?: Configuration): ResourceManager;
        /**
         * Obtains the configuration of differentiated resources. This API returns the result synchronously.
         *
         * For both the common resource management object and the differentiated resource management object obtained
         * through the [getOverrideResourceManager]{@link resourceManager.ResourceManager.getOverrideResourceManager} API,
         * this API returns the same configuration information.
         *
         * @returns { Configuration } Configuration of differentiated resources.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        getOverrideConfiguration(): Configuration;
        /**
         * Updates the configuration of a differentiated resource management object.
         *
         * This API updates the configuration of the differentiated resource management object, regardless of whether it is
         * called on the common resource management object or on the differentiated one obtained via
         * [getOverrideResourceManager]{@link resourceManager.ResourceManager.getOverrideResourceManager}.
         *
         * @param { Configuration } configuration - Configuration of differentiated resources. After obtaining the
         *     configuration of differentiated resources through
         *     [getOverrideConfiguration]{@link resourceManager.ResourceManager.getOverrideConfiguration}, modify the
         *     configuration items as required, and then pass these items as input parameters to the API.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: Incorrect parameter types.
         * @syscap SystemCapability.Global.ResourceManager
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        updateOverrideConfiguration(configuration: Configuration): void;
        /**
         * Obtains the resource name corresponding to the specified resource ID.
         *
         * @param { number } resId - Resource ID.
         * @returns { string } Resource name corresponding to the resource ID.
         * @throws { BusinessError } 9001001 - Invalid resource ID.
         * @syscap SystemCapability.Global.ResourceManager
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        getResourceName(resId: number): string;
    }
    /**
     * Describes the file descriptor information of the HAP where the rawfile is located.
     *
     * @syscap SystemCapability.Global.ResourceManager
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    export type RawFileDescriptor = _RawFileDescriptor;
    /**
     * Describes the resource information, including the application package name, application module name, resource ID,
     * resource type, and formatting parameters.
     *
     * @syscap SystemCapability.Global.ResourceManager
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    export type Resource = _Resource;
}
export default resourceManager;

```
