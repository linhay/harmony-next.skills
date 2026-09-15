# @ohos.web.WebNativeMessagingExtensionContext.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2025 Huawei Device Co., Ltd.
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
 * @kit ArkWeb
 */
import ExtensionContext from './application/ExtensionContext';
import Want from './@ohos.app.ability.Want';
import StartOptions from './@ohos.app.ability.StartOptions';
import { AbilityResult } from './ability/abilityResult';
/**
 * WebNativeMessagingExtensionContext is the context of web native message extension and is inherited from
 * ExtensionContext. It provides the capability of exchanging messages with WebNativeMessagingExtension.
 * The APIs of this module can be used only in the stage model.
 *
 * @extends ExtensionContext
 * @syscap SystemCapability.Web.Webview.Core
 * @stagemodelonly
 * @since 21
 */
export default class WebNativeMessagingExtensionContext extends ExtensionContext {
    /**
     * Starts an ability using a promise.
     *
     * @param { Want } want - Information about the ability to start.
     * @param { StartOptions } [options] - Startup options.
     * @returns { Promise<void> } Promise that returns by the function.
     * @throws { BusinessError } 201 - The application does not have permission to call the interface.
     * @throws { BusinessError } 16000001 - The specified ability does not exist.
     * @throws { BusinessError } 16000002 - Incorrect ability type.
     * @throws { BusinessError } 16000004 - Cannot start an invisible component.
     * @throws { BusinessError } 16000005 - The specified process does not have the permission.
     * @throws { BusinessError } 16000008 - The crowdtesting application expires.
     * @throws { BusinessError } 16000009 - An ability cannot be started or stopped in Wukong mode.
     * @throws { BusinessError } 16000010 - The call with the continuation and prepare continuation flag is forbidden.
     * @throws { BusinessError } 16000011 - The context does not exist.
     * @throws { BusinessError } 16000012 - The application is controlled.
     * @throws { BusinessError } 16000013 - The application is controlled by EDM.
     * @throws { BusinessError } 16000019 - No matching ability is found.
     * @throws { BusinessError } 16000050 - Internal error. Possible causes: 1. Failed to connect to the system service;
     *     2. The system service failed to communicate with dependency module.
     * @throws { BusinessError } 16000055 - Installation-free timed out.
     * @throws { BusinessError } 16000071 - App clone is not supported.
     * @throws { BusinessError } 16000072 - App clone or multi-instance is not supported.
     * @throws { BusinessError } 16000073 - The app clone index is invalid.
     * @throws { BusinessError } 16000076 - The app instance key is invalid.
     * @throws { BusinessError } 16000077 - The number of app instances reaches the limit.
     * @throws { BusinessError } 16000078 - The multi-instance is not supported.
     * @throws { BusinessError } 16000079 - The APP_INSTANCE_KEY cannot be specified.
     * @throws { BusinessError } 16000080 - Creating a new instance is not supported.
     * @syscap SystemCapability.Web.Webview.Core
     * @stagemodelonly
     * @since 21
     */
    startAbility(want: Want, options?: StartOptions): Promise<void>;
    /**
     * Starts an ability and returns the execution result when the ability is destroyed.
     *
     * @param { Want } want - Indicates the ability to start.
     * @param { StartOptions } [options] - Indicates the start options.
     * @returns { Promise<AbilityResult> } Returns the result of startAbility.
     * @throws { BusinessError } 201 - The application does not have permission to call the interface.
     * @throws { BusinessError } 16000001 - The specified ability does not exist.
     * @throws { BusinessError } 16000002 - Incorrect ability type.
     * @throws { BusinessError } 16000004 - Cannot start an invisible component.
     * @throws { BusinessError } 16000005 - The specified process does not have the permission.
     * @throws { BusinessError } 16000008 - The crowdtesting application expires.
     * @throws { BusinessError } 16000009 - An ability cannot be started or stopped in Wukong mode.
     * @throws { BusinessError } 16000010 - The call with the continuation and prepare continuation flag is forbidden.
     * @throws { BusinessError } 16000011 - The context does not exist.
     * @throws { BusinessError } 16000012 - The application is controlled by the AppGallery and cannot be started.
     * @throws { BusinessError } 16000013 - The application is controlled by Enterprise Device Manager and
     *     cannot be started.
     * @throws { BusinessError } 16000019 - No matching ability is found.
     * @throws { BusinessError } 16000050 - Internal error. Possible causes: 1. Failed to connect to the system service;
     *     2. The system service failed to communicate with dependency module.
     * @throws { BusinessError } 16000055 - Installation-free timed out.
     * @throws { BusinessError } 16000071 - The application does not support appClone mode in multiAppMode.
     * @throws { BusinessError } 16000072 - The application does not support appClone and multi-instance mode in
     *     multiAppMode.
     * @throws { BusinessError } 16000073 - The app clone index is invalid.
     * @throws { BusinessError } 16000076 - The app instance key is invalid.
     * @throws { BusinessError } 16000077 - The number of app instances reaches the limit.
     * @throws { BusinessError } 16000078 - The application does not support multiple instances.
     * @throws { BusinessError } 16000079 - The APP_INSTANCE_KEY cannot be specified.
     * @throws { BusinessError } 16000080 - Instances cannot be created for other applications during
     *     inter-application startup.
     * @syscap SystemCapability.Web.Webview.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    startAbilityForResult(want: Want, options?: StartOptions): Promise<AbilityResult>;
    /**
     * Destroys the current native web message extension.
     *
     * @returns { Promise<void> } Promise that returns by the function.
     * @throws { BusinessError } 16000009 - An ability cannot be started or stopped in Wukong mode.
     * @throws { BusinessError } 16000011 - The context does not exist.
     * @throws { BusinessError } 16000050 - Internal error. Possible causes: 1. Failed to connect to the system service;
     *     2. The system service failed to communicate with dependency module.
     * @syscap SystemCapability.Web.Webview.Core
     * @stagemodelonly
     * @since 21
     */
    terminateSelf(): Promise<void>;
    /**
     * Stops a native connection. This API uses a promise to return the result.
     *
     * @param { number } connectionId - ID of the connection to stop
     *     <br>The value range is all integers.
     * @returns { Promise<void> } Promise that returns by the function.
     * @throws { BusinessError } 201 - The application does not have permission to call the interface.
     * @throws { BusinessError } 16000011 - The context does not exist.
     * @throws { BusinessError } 16000050 - Internal error. Possible causes: 1. Failed to connect to the system service;
     *     2. The system service failed to communicate with dependency module.
     * @syscap SystemCapability.Web.Webview.Core
     * @stagemodelonly
     * @since 21
     */
    stopNativeConnection(connectionId: number): Promise<void>;
}

```
