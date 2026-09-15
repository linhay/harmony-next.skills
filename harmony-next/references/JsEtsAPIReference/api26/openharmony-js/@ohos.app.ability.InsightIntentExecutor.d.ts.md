# @ohos.app.ability.InsightIntentExecutor.d.ts

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
 * @file
 * @kit AbilityKit
 */
import type window from './@ohos.window';
import type insightIntent from './@ohos.app.ability.insightIntent';
import type InsightIntentContext from './@ohos.app.ability.InsightIntentContext';
import type UIExtensionContentSession from './@ohos.app.ability.UIExtensionContentSession';
/**
 * The module provides the base class for intent execution. You can use this module to interface with the
 * [InsightIntent framework](docroot://application-models/insight-intent-overview.md) on the device side and implement
 * intent service logic through [configuration files](docroot://application-models/insight-intent-config-development.md)
 * .
 * In addition to developing intents via configuration files, intents can also be developed using decorators. For API
 * version 20 and later, you are advised to
 * [develop intents using decorators](docroot://application-models/insight-intent-decorator-development.md).
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @stagemodelonly
 * @atomicservice
 * @since 11
 */
declare class InsightIntentExecutor {
    /**
     * Context for intent execution.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 11
     */
    context: InsightIntentContext;
    /**
     * Called during the UIAbility lifecycle when the [UIAbility]{@link @ohos.app.ability.UIAbility} that the intent
     * execution depends on is started in the foreground. Both synchronous calls and asynchronous calls using Promise are
     * supported.
     *
     * - If the UIAbility is cold started, the UIAbility lifecycle callbacks are triggered in the following sequence
     * during intent execution: [onCreate]{@link @ohos.app.ability.UIAbility:UIAbility#onCreate},
     * [onWindowStageCreate]{@link @ohos.app.ability.UIAbility:UIAbility#onWindowStageCreate},
     * onExecuteInUIAbilityForegroundMode, and [onForeground]{@link @ohos.app.ability.UIAbility:UIAbility#onForeground}.
     * - If the UIAbility is hot started in the background, the UIAbility lifecycle callbacks are triggered in the
     * following sequence during intent execution: [onNewWant]{@link @ohos.app.ability.UIAbility:UIAbility#onNewWant},
     * onExecuteInUIAbilityForegroundMode, and [onForeground]{@link @ohos.app.ability.UIAbility:UIAbility#onForeground}.
     * - If the UIAbility is hot started in the foreground, the UIAbility lifecycle callbacks are triggered in the
     * following sequence during intent execution: onExecuteInUIAbilityForegroundMode.
     *
     * @param { string } name - Intent name.
     * @param { Record<string, Object> } param - Intent parameter, which is the data passed from the system entry point to the
     *     application for this intent execution.
     * @param { window.WindowStage } pageLoader - WindowStage instance, which is the same as the WindowStage instance in the
     *     [onWindowStageCreate]{@link @ohos.app.ability.UIAbility:UIAbility#onWindowStageCreate} API and can be used to load
     *     the page for intent execution.
     * @returns { insightIntent.ExecuteResult | Promise<insightIntent.ExecuteResult> } Intent execution result or a Promise
     *     object containing the intent execution result, representing the data returned to the system entry point from this
     *     intent execution.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @atomicservice
     * @since 11
     */
    onExecuteInUIAbilityForegroundMode(name: string, param: Record<string, Object>, pageLoader: window.WindowStage): insightIntent.ExecuteResult | Promise<insightIntent.ExecuteResult>;
    /**
     * Called during the UIAbility lifecycle when the [UIAbility]{@link @ohos.app.ability.UIAbility} that the intent
     * execution depends on is started in the background. Both synchronous calls and asynchronous calls using Promise are
     * supported.
     *
     * - If the UIAbility is cold started, the UIAbility lifecycle callbacks are triggered in the following sequence
     * during intent execution: [onCreate]{@link @ohos.app.ability.UIAbility:UIAbility#onCreate},
     * onExecuteInUIAbilityBackgroundMode, and [onBackground]{@link @ohos.app.ability.UIAbility:UIAbility#onBackground}.
     * - If the UIAbility is hot started, the UIAbility lifecycle callbacks are triggered in the following sequence during
     *  intent execution: onExecuteInUIAbilityBackgroundMode.
     *
     * @param { string } name - Intent name.
     * @param { Record<string, Object> } param - Intent parameter, which is the data passed from the system entry point to the
     *     application for this intent execution.
     * @returns { insightIntent.ExecuteResult | Promise<insightIntent.ExecuteResult> } Intent execution result or a Promise
     *     object containing the intent execution result, representing the data returned to the system entry point from this
     *     intent execution.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @atomicservice
     * @since 11
     */
    onExecuteInUIAbilityBackgroundMode(name: string, param: Record<string, Object>): insightIntent.ExecuteResult | Promise<insightIntent.ExecuteResult>;
    /**
     * Called during the UIExtensionAbility lifecycle when the
     * [UIExtensionAbility]{@link @ohos.app.ability.UIExtensionAbility:UIExtensionAbility} that the intent execution
     * depends on is started. Both synchronous calls and asynchronous calls using Promise are supported.
     *
     * - The UIExtensionAbility lifecycle callbacks are triggered in the following sequence during intent execution:
     * [onCreate]{@link @ohos.app.ability.UIExtensionAbility:UIExtensionAbility#onCreate},
     * [onSessionCreate]{@link @ohos.app.ability.UIExtensionAbility:UIExtensionAbility#onSessionCreate},
     * onExecuteInUIExtensionAbility, and
     * [onForeground]{@link @ohos.app.ability.UIExtensionAbility:UIExtensionAbility#onForeground}.
     *
     * @param { string } name - Intent name.
     * @param { Record<string, Object> } param - Intent parameter, which is the data passed from the system entry point to the
     *     application for this intent execution.
     * @param { UIExtensionContentSession } pageLoader - UIExtensionContentSession instance, which is the same as the
     *     UIExtensionContentSession instance in the
     *     [onSessionCreate]{@link @ohos.app.ability.UIExtensionAbility:UIExtensionAbility#onSessionCreate} API and can be used
     *     to load the page for intent execution.
     * @returns { insightIntent.ExecuteResult | Promise<insightIntent.ExecuteResult> } Intent execution result or a Promise
     *     object containing the intent execution result, representing the data returned to the system entry point from this
     *     intent execution.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 11
     */
    onExecuteInUIExtensionAbility(name: string, param: Record<string, Object>, pageLoader: UIExtensionContentSession): insightIntent.ExecuteResult | Promise<insightIntent.ExecuteResult>;
    /**
     * Called during the ServiceExtensionAbility lifecycle when the ServiceExtensionAbility that the intent execution
     * depends on is started. Both synchronous calls and asynchronous calls using Promise are supported.
     *
     * - The ServiceExtensionAbility lifecycle callbacks are triggered in the following sequence during intent execution:
     * **onCreate**, **onRequest**, and **onExecuteInServiceExtensionAbility**.
     *
     * @param { string } name - Intent name.
     * @param { Record<string, Object> } param - Intent parameter, which is the data passed from the system entry point to the
     *     application for this intent execution.
     * @returns { insightIntent.ExecuteResult | Promise<insightIntent.ExecuteResult> } Intent execution result or a Promise
     *     object containing the intent execution result, representing the data returned to the system entry point from this
     *     intent execution.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 11
     */
    onExecuteInServiceExtensionAbility(name: string, param: Record<string, Object>): insightIntent.ExecuteResult | Promise<insightIntent.ExecuteResult>;
}
export default InsightIntentExecutor;

```
