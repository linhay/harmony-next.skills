# @ohos.app.appstartup.StartupConfigEntry.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2024 Huawei Device Co., Ltd.
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
 * @file
 * @kit AbilityKit
 */
import StartupConfig from './@ohos.app.appstartup.StartupConfig';
import Want from './@ohos.app.ability.Want';
/**
 * The module provides the capability to configure [AppStartup](docroot://application-models/app-startup.md).
 *
 * @syscap SystemCapability.Ability.AppStartup
 * @stagemodelonly
 * @since 12
 */
declare class StartupConfigEntry {
    /**
     * Called if the HAP of the AbilityStage has
     * [defined the AppStartup configuration file](docroot://application-models/app-startup.md#defining-startup-parameter-configuration)
     * . This callback is triggered before
     * [AbilityStage.onCreate]{@link @ohos.app.ability.AbilityStage:AbilityStage.onCreate}.
     *
     * You can set the AppStartup configuration within this callback. For details, see
     * [Setting Startup Parameters](docroot://application-models/app-startup.md#setting-startup-parameters).
     *
     * @returns { StartupConfig } AppStartup configuration.
     * @syscap SystemCapability.Ability.AppStartup
     * @stagemodelonly
     * @since 12
     */
    onConfig?(): StartupConfig;
    /**
     * Called if the HAP of the AbilityStage has
     * [defined the AppStartup configuration file](docroot://application-models/app-startup.md#defining-startup-parameter-configuration)
     * . This callback is triggered after [StartupConfigEntry.onConfig]{@link StartupConfigEntry#onConfig?()} but before
     * [AbilityStage.onCreate]{@link @ohos.app.ability.AbilityStage:AbilityStage.onCreate}.
     *
     * You can use this callback to return different custom matching rules based on parameters in the Want object passed
     * by the caller to start the UIAbility. . AppStartup matches these rules with the **customization** field in
     * **matchRules** of the startup task configuration. If a match is successful, the task is executed automatically. For
     * details about the matching rules, see
     * [Adding Task Matching Rules](docroot://application-models/app-startup.md#adding-task-matching-rules).
     *
     * This API is typically used in scenarios where tasks cannot be matched directly using URI, action, or intent name
     * rules. It allows for further refinement of matching rules.
     *
     * @param { Want } want - Want information about the target UIAbility.
     * @returns { string } Custom matching rule, which is used to determine whether to automatically execute the task.
     * @syscap SystemCapability.Ability.AppStartup
     * @stagemodelonly
     * @since 20
     */
    onRequestCustomMatchRule(want: Want): string;
}
export default StartupConfigEntry;

```
