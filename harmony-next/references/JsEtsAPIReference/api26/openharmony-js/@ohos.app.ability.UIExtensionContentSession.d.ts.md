# @ohos.app.ability.UIExtensionContentSession.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2023 Huawei Device Co., Ltd.
 * Licensed under the Apache License, Version 2.0 (the "License"),
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
 * UIExtensionContentSession is the UI operation class for the
 * [UIExtensionAbility]{@link ./@ohos.app.ability.UIExtensionAbility:UIExtensionAbility}. It provides control over page
 * loading and allows configuration of the window privacy mode of the host application (application that starts the
 * UIExtensionAbility). When the host application starts a specific UIExtensionAbility, the system creates a
 * UIExtensionContentSession object and passes it back via the
 * [onSessionCreate]{@link ./@ohos.app.ability.UIExtensionAbility:UIExtensionAbility.onSessionCreate} callback. Each
 * UIExtensionAbility corresponds to one UIExtensionContentSession object, and these objects operate independently
 * without interfering with each other.
 *
 * @file
 * @kit AbilityKit
 */
import type { AbilityResult } from './ability/abilityResult';
import type { AsyncCallback } from './@ohos.base';
import type uiExtension from './@ohos.arkui.uiExtension';
import type AbilityStartCallback from './application/AbilityStartCallback';
/**
 * UIExtensionContentSession is the UI operation class for the UIExtensionAbility. It provides control over page loading
 *  and allows configuration of the window privacy mode of the host application.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @stagemodelonly
 * @since 10
 */
declare class UIExtensionContentSession {
    /**
     * Loads a page for the [UIExtensionAbility]{@link ./@ohos.app.ability.UIExtensionAbility:UIExtensionAbility}, with
     * state properties passed to the page through [LocalStorage](docroot://ui/state-management/arkts-localstorage.md).
     * This API is used to load a page in the
     * [onSessionCreate]{@link ./@ohos.app.ability.UIExtensionAbility:UIExtensionAbility.onSessionCreate} lifecycle of the
     * UIExtensionAbility.
     *
     * @param { string } path - Path of the page to load. The path is configured using the
     *     [pages](docroot://quick-start/module-configuration-file.md#pages) tag in the
     *     [module.json5](docroot://quick-start/module-configuration-file.md) file.
     * @param { LocalStorage } [storage] - A page-level UI state storage unit, which is used to pass state properties to the
     *     page.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 16000050 - Internal error.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 10
     */
    loadContent(path: string, storage?: LocalStorage): void;
    /**
     * Loads a [named route](docroot://ui/arkts-routing.md#named-route) page for a
     * [UIExtensionAbility]{@link ./@ohos.app.ability.UIExtensionAbility:UIExtensionAbility}, with state properties passed
     * to the page through [LocalStorage](docroot://ui/state-management/arkts-localstorage.md). This API is used to load a
     *  named route page in the
     * [onSessionCreate]{@link ./@ohos.app.ability.UIExtensionAbility:UIExtensionAbility.onSessionCreate} lifecycle of the
     * UIExtensionAbility.
     *
     * @param { string } name - Name of the named route page.
     * @param { LocalStorage } [storage] - A page-level UI state storage unit, which is used to pass state properties to the
     *     page.
     * @throws { BusinessError } 16000050 - Internal error.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 18
     */
    loadContentByName(name: string, storage?: LocalStorage): void;
    /**
     * Destroys this UIExtensionAbility and closes the corresponding window of the host application. This API uses an
     * asynchronous callback to return the result.
     *
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful, **err** is
     *     **undefined**. Otherwise, **err** is an error object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 10
     */
    terminateSelf(callback: AsyncCallback<void>): void;
    /**
     * Destroys this UIExtensionAbility and closes the corresponding window of the host application. This API uses a
     * promise to return the result.
     *
     * @returns { Promise<void> } Promise that returns no value.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 10
     */
    terminateSelf(): Promise<void>;
    /**
     * Destroys this UIExtensionAbility, closes the corresponding window of the host application, and returns the result
     * to the host application. This API uses an asynchronous callback to return the result.
     *
     * @param { AbilityResult } parameter - Information returned to the host application.
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful, **err** is
     *     **undefined**. Otherwise, **err** is an error object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 10
     */
    terminateSelfWithResult(parameter: AbilityResult, callback: AsyncCallback<void>): void;
    /**
     * Destroys this UIExtensionAbility, closes the corresponding window of the host application, and returns the result
     * to the host application. This API uses a promise to return the result.
     *
     * @param { AbilityResult } parameter - Information returned to the host application.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 10
     */
    terminateSelfWithResult(parameter: AbilityResult): Promise<void>;
    /**
     * Enables or disables the window privacy mode of the host application. A window in privacy mode cannot be captured or
     *  recorded. This API uses a promise to return the result.
     *
     * @permission ohos.permission.PRIVACY_WINDOW
     * @param { boolean } isPrivacyMode - Whether to enable the privacy mode. **true** to enable, **false** otherwise.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 201 - The application does not have permission to call the interface.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 10
     */
    setWindowPrivacyMode(isPrivacyMode: boolean): Promise<void>;
    /**
     * Enables or disables the window privacy mode of the host application. A window in privacy mode cannot be captured or
     *  recorded. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.PRIVACY_WINDOW
     * @param { boolean } isPrivacyMode - Whether to enable the privacy mode. **true** to enable, **false** otherwise.
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the setting is successful, **err** is
     *     **undefined**. Otherwise, **err** is an error object.
     * @throws { BusinessError } 201 - The application does not have permission to call the interface.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 10
     */
    setWindowPrivacyMode(isPrivacyMode: boolean, callback: AsyncCallback<void>): void;
    /**
     * Implicitly starts a given type of UIExtensionAbility. This API uses an asynchronous callback to return the result.
     * It can be called only by applications running in the foreground.
     * If the target ability is visible, you can start the target ability; If the target ability is invisible,
     * you need to apply for permission:ohos.permission.START_INVISIBLE_ABILITY to start target invisible ability.
     *
     * @param { string } type - Type of the UIExtensionAbility. For details, see
     *     [Starting an Application of the Specified Type](docroot://application-models/start-intent-panel.md#matching-rules).
     * @param { Record<string, Object> } wantParam - Parameters passed for starting the UIExtensionAbility.
     * @param { AbilityStartCallback } abilityStartCallback - Execution result of starting the UIExtensionAbility.
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful, **err** is
     *     **undefined**. Otherwise, **err** is an error object.
     * @throws { BusinessError } 201 - The application does not have permission to call the interface. [since 11 - 11]
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types.
     * @throws { BusinessError } 16000001 - The specified ability does not exist. [since 11 - 11]
     * @throws { BusinessError } 16000002 - Incorrect ability type. [since 11 - 11]
     * @throws { BusinessError } 16000004 - Cannot start an invisible component. [since 11 - 11]
     * @throws { BusinessError } 16000050 - Internal error.
     * @throws { BusinessError } 16200001 - The caller has been released. [since 11 - 11]
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 11
     */
    startAbilityByType(type: string, wantParam: Record<string, Object>, abilityStartCallback: AbilityStartCallback, callback: AsyncCallback<void>): void;
    /**
     * Implicitly starts a given type of UIExtensionAbility. This API uses a promise to return the result. It can be
     * called only by applications running in the foreground.
     *
     * @param { string } type - Type of the UIExtensionAbility. For details, see
     *     [Starting an Application of the Specified Type](docroot://application-models/start-intent-panel.md#matching-rules).
     * @param { Record<string, Object> } wantParam - Parameters passed for starting the UIExtensionAbility.
     * @param { AbilityStartCallback } abilityStartCallback - Execution result of starting the UIExtensionAbility.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 201 - The application does not have permission to call the interface. [since 11 - 11]
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types.
     * @throws { BusinessError } 16000001 - The specified ability does not exist. [since 11 - 11]
     * @throws { BusinessError } 16000002 - Incorrect ability type. [since 11 - 11]
     * @throws { BusinessError } 16000004 - Cannot start an invisible component. [since 11 - 11]
     * @throws { BusinessError } 16000050 - Internal error.
     * @throws { BusinessError } 16200001 - The caller has been released. [since 11 - 11]
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 11
     */
    startAbilityByType(type: string, wantParam: Record<string, Object>, abilityStartCallback: AbilityStartCallback): Promise<void>;
    /**
     * Obtains the window proxy of this UIExtensionAbility.
     *
     * @returns { uiExtension.WindowProxy } Window proxy of the host application.
     * @throws { BusinessError } 16000050 - Internal error.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 12
     */
    getUIExtensionWindowProxy(): uiExtension.WindowProxy;
}
export default UIExtensionContentSession;

```
