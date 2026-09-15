# @ohos.app.ability.InsightIntentContext.d.ts

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
import type { AsyncCallback } from './@ohos.base';
import type insightIntent from './@ohos.app.ability.insightIntent';
import type Want from './@ohos.app.ability.Want';
/**
 * The module provides the context for intent execution. It is used as a property in both the
 * [intent execution base class]{@link @ohos.app.ability.InsightIntentExecutor:InsightIntentExecutor} and
 * [base class decorated with @InsightIntentEntry]{@link @ohos.app.ability.InsightIntentEntryExecutor:InsightIntentEntryExecutor}
 * , offering essential capabilities for intent implementation, for example, starting
 * [UIAbility components]{@link @ohos.app.ability.UIAbility} within the same application.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @stagemodelonly
 * @atomicservice
 * @since 11
 */
declare class InsightIntentContext {
    /**
     * Unique ID of an intent instance. Its execution result can be returned through
     * [insightIntentProvider.sendExecuteResult]
     * {@link @ohos.app.ability.insightIntentProvider:insightIntentProvider.sendExecuteResult} and
     * [insightIntentProvider.sendIntentResult]
     * {@link @ohos.app.ability.insightIntentProvider:insightIntentProvider.sendIntentResult}.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 23
     */
    instanceId: number;
    /**
     * Starts a UIAbility. This API can only be used to start UIAbility components within the same application. This API
     * uses an asynchronous callback to return the result.
     *
     * @param { Want } want - Want information for starting the UIAbility.
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
     *     **err** is **undefined**. Otherwise, **err** is an error object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 16000001 - The specified ability does not exist.
     * @throws { BusinessError } 16000004 - Cannot start an invisible component.
     * @throws { BusinessError } 16000005 - The specified process does not have the permission.
     * @throws { BusinessError } 16000006 - Cross-user operations are not allowed.
     * @throws { BusinessError } 16000008 - The crowdtesting application expires.
     * @throws { BusinessError } 16000009 - An ability cannot be started or stopped in Wukong mode.
     * @throws { BusinessError } 16000011 - The context does not exist.
     * @throws { BusinessError } 16000012 - The application is controlled.
     * @throws { BusinessError } 16000013 - The application is controlled by EDM.
     * @throws { BusinessError } 16000050 - Internal error.
     * @throws { BusinessError } 16000053 - The ability is not on the top of the UI.
     * @throws { BusinessError } 16000055 - Installation-free timed out.
     * @throws { BusinessError } 16000061 - Operation not supported.
     * @throws { BusinessError } 16200001 - The caller has been released.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 11
     */
    startAbility(want: Want, callback: AsyncCallback<void>): void;
    /**
     * Starts a UIAbility. This API can only be used to start UIAbility components within the same application. This API
     * uses a promise to return the result.
     *
     * @param { Want } want - Want information for starting the UIAbility.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 16000001 - The specified ability does not exist.
     * @throws { BusinessError } 16000004 - Cannot start an invisible component.
     * @throws { BusinessError } 16000005 - The specified process does not have the permission.
     * @throws { BusinessError } 16000006 - Cross-user operations are not allowed.
     * @throws { BusinessError } 16000008 - The crowdtesting application expires.
     * @throws { BusinessError } 16000009 - An ability cannot be started or stopped in Wukong mode.
     * @throws { BusinessError } 16000011 - The context does not exist.
     * @throws { BusinessError } 16000012 - The application is controlled.
     * @throws { BusinessError } 16000013 - The application is controlled by EDM.
     * @throws { BusinessError } 16000050 - Internal error.
     * @throws { BusinessError } 16000053 - The ability is not on the top of the UI.
     * @throws { BusinessError } 16000055 - Installation-free timed out.
     * @throws { BusinessError } 16000061 - Operation not supported.
     * @throws { BusinessError } 16200001 - The caller has been released.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 11
     */
    startAbility(want: Want): Promise<void>;
    /**
     * Sets the return mode of the intent execution result. This API is applicable to intents with the execution mode set
     * to [UI_ABILITY_FOREGROUND]{@link @ohos.app.ability.insightIntent:insightIntent.ExecuteMode}.
     *
     * @param { insightIntent.ReturnMode } returnMode - Return mode of the intent execution result.
     * @throws { BusinessError } 16000011 - The context does not exist. Possible causes: 1.The context is
     *     not insightIntentContext; 2.The context is not for UIAbility foreground insight intent execute mode.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 23
     */
    setReturnModeForUIAbilityForeground(returnMode: insightIntent.ReturnMode): void;
    /**
     * Sets the return mode of the intent execution result. This API is applicable to intents with the execution mode set
     * to [UI_EXTENSION_ABILITY]{@link @ohos.app.ability.insightIntent:insightIntent.ExecuteMode}.
     *
     * @param { insightIntent.ReturnMode } returnMode - Return mode of the intent execution result.
     * @throws { BusinessError } 16000011 - The context does not exist. Possible causes: 1.The context is not
     *     insightIntentContext; 2.The context is not for UIExtensionAbility insight intent execute mode.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 23
     */
    setReturnModeForUIExtensionAbility(returnMode: insightIntent.ReturnMode): void;
}
export default InsightIntentContext;

```
