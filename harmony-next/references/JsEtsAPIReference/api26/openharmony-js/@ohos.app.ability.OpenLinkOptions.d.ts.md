# @ohos.app.ability.OpenLinkOptions.d.ts

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
import CompletionHandler from './@ohos.app.ability.CompletionHandler';
/**
 * **OpenLinkOptions** can be used as an input parameter of
 * [openLink()]{@link ./application/UIAbilityContext:UIAbilityContext.openLink} to indicate whether to enable only App
 * Linking and pass in optional parameters in the form of key-value pairs.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @stagemodelonly
 * @atomicservice
 * @since 12
 */
export default interface OpenLinkOptions {
    /**
     * Whether the UIAbility must be started using <!--RP1-->
     * [App Linking](docroot://application-models/app-linking-startup.md)<!--RP1End-->.
     *
     * - If this parameter is set to **true** and no UIAbility matches the URL in App Linking, the result is returned
     * directly.
     * - If this parameter is set to **false** and no UIAbility matches the URL in App Linking, App Linking falls back to
     * [Deep Linking](docroot://application-models/deep-linking-startup.md). The default value is **false**.
     *
     * When the aa command is used to implicitly start an ability, you can set **--pb appLinkingOnly true** or
     * **--pb appLinkingOnly false** to start the ability in App Linking mode.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 12
     */
    appLinkingOnly?: boolean;
    /**
     * List of parameters in Want.
     *
     * Note: For details about the usage rules, see **parameters** in [want]{@link @ohos.app.ability.Want:Want}.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 12
     */
    parameters?: Record<string, Object>;
    /**
     * Operation class used to handle the result of an application launch request.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 21
     */
    completionHandler?: CompletionHandler;
    /**
     * Whether to display a "No app available" dialog box when a suitable application is not found using
     * [Deep Linking](docroot://application-models/deep-linking-startup.md).
     *
     * - **true**: The "No app available" dialog box is not displayed.
     * - **false**: The "No app available" dialog box is displayed. The default value is **false**.
     *
     * Note: If **appLinkingOnly** is set to **true**, the Deep Linking process is not triggered, and this field does not
     * take effect.
     *
     * @default { false }
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 21
     */
    hideFailureTipDialog?: boolean;
}

```
