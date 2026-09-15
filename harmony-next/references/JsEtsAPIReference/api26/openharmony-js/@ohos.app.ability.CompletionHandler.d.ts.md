# @ohos.app.ability.CompletionHandler.d.ts

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
 * **CompletionHandler** is an optional parameter of [StartOptions]{@link @ohos.app.ability.StartOptions:StartOptions}
 * and [OpenLinkOptions]{@link @ohos.app.ability.OpenLinkOptions:OpenLinkOptions}. It is used to process the result of
 * an application launch request.
 *
 * @file
 * @kit AbilityKit
 */
import { ElementName } from './bundleManager/ElementName';
/**
 * CompletionHandler provides two callback functions,
 * [onRequestSuccess]{@link CompletionHandler.onRequestSuccess(elementName: ElementName, message: string)} and
 * [onRequestFailure]{@link CompletionHandler.onRequestFailure(elementName: ElementName, message: string)}, to handle
 * the results of successful and failed application launch requests, respectively.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @stagemodelonly
 * @atomicservice
 * @since 20
 */
declare class CompletionHandler {
    /**
     * Called when the application is successfully launched.
     *
     * @param { ElementName } elementName - **ElementName** information used to identify the target application. Typically,
     *     **ElementName** includes only **abilityName** and **bundleName**. The presence of **moduleName** and **deviceId**
     *     depends on whether the caller provides them. **shortName** and **uri** are empty.
     * @param { string } message - Message displayed when the application is successfully launched. This message is in JSON
     *     format, as follows:
     *
     *     {
     *
     *     ?"errMsg": "Succeeded."
     *
     *     }
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    onRequestSuccess(elementName: ElementName, message: string): void;
    /**
     * Called when the application fails to be launched.
     *
     * @param { ElementName } elementName - **ElementName** information used to identify the target application.
     *
     *     - Typically, **ElementName** includes only **abilityName** and **bundleName**. The presence of **moduleName** and
     *     **deviceId** depends on whether the caller provides them. **shortName** and **uri** are empty.
     *
     *     - **ElementName** information cannot be obtained if the implicit startup fails.
     * @param { string } message - Message displayed when the application fails to be launched. This message is in JSON format,
     *     as follows:
     *
     *     {
     *
     *     ?"errMsg": "xxx"
     *
     *     }
     *
     *     The value of *xxx* is described as follows:
     *
     *     Failed to call <api-name>: An error occurs when calling the API. <api-name> is the specific API name, for example,
     *     **startAbility**.
     *
     *     User refused redirection: The user has closed the application redirection dialog box.
     *
     *     User closed the implicit startup picker: The user has closed the dialog box for selecting an application for
     *     implicit startup.
     *
     *     User closed the app clone picker: The user has closed the dialog box for selecting a cloned application.
     *
     *     Free installation failed: The free installation fails.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    onRequestFailure(elementName: ElementName, message: string): void;
}
export default CompletionHandler;

```
