# @ohos.app.ability.InsightIntentEntryExecutor.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2025 Huawei Device Co., Ltd.
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
import window from './@ohos.window';
import insightIntent from './@ohos.app.ability.insightIntent';
import InsightIntentContext from './@ohos.app.ability.InsightIntentContext';
import UIExtensionContentSession from './@ohos.app.ability.UIExtensionContentSession';
/**
 * The class of insight intent entry executor.
 *
 * @class InsightIntentEntryExecutor<T>
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @stagemodelonly
 * @atomicservice
 * @since 20
 */
declare class InsightIntentEntryExecutor<T> {
    /**
     * The insight intent execute mode.
     *
     * @type { insightIntent.ExecuteMode }
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    executeMode: insightIntent.ExecuteMode;
    /**
     * The insight intent context.
     *
     * @type { InsightIntentContext }
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    context: InsightIntentContext;
    /**
     * The window stage.
     *
     * @type { ?window.WindowStage }
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    windowStage?: window.WindowStage;
    /**
     * The UIExtension content session.
     *
     * @type { ?UIExtensionContentSession }
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    uiExtensionSession?: UIExtensionContentSession;
    /**
     * Called when insight intent execute.
     *
     * @returns { Promise<insightIntent.IntentResult<T>> } The result of insight intent execution, support promise.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    onExecute(): Promise<insightIntent.IntentResult<T>>;
}
export default InsightIntentEntryExecutor;

```
