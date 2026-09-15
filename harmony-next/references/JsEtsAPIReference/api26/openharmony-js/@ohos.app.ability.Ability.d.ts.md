# @ohos.app.ability.Ability.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022-2023 Huawei Device Co., Ltd.
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
import AbilityConstant from './@ohos.app.ability.AbilityConstant';
import { Configuration } from './@ohos.app.ability.Configuration';
/**
 * The Ability class is the fundamental unit for application lifecycle scheduling. It is the base class of
 * [UIAbility]{@link @ohos.app.ability.UIAbility} and
 * [ExtensionAbility]{@link @ohos.app.ability.ExtensionAbility:ExtensionAbility}, and provides callbacks for system
 * configuration updates and memory level updates. However, you cannot inherit directly from this base class. You should
 *  opt for either [UIAbility]{@link @ohos.app.ability.UIAbility} or
 * [ExtensionAbility]{@link @ohos.app.ability.ExtensionAbility:ExtensionAbility} based on your service needs. For
 * details, see [Introduction to Ability Kit](docroot://application-models/abilitykit-overview.md).
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
 * @stagemodelonly
 * @crossplatform [since 26.0.0]
 * @atomicservice [since 11]
 * @since 9
 */
declare class Ability {
    /**
     * Called when a system environment variable changes. You can override this callback to respond to changes in the
     * system environment variables. For example, when the system language changes, the application can perform customized
     *  processing in the callback.
     *
     * > **NOTE**
     * >
     * > There are certain restrictions when this callback is actually triggered. For example, if you set the application
     * > language by calling [setLanguage]{@link ./application/ApplicationContext:ApplicationContext.setLanguage}, the
     * > system does not trigger the **onConfigurationUpdate** callback even if the system language changes. For details,
     * > see [When to Use](docroot://application-models/subscribe-system-environment-variable-changes.md#when-to-use).
     *
     * @param { Configuration } newConfig - New configuration.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @crossplatform [since 26.0.0]
     * @atomicservice [since 11]
     * @since 9
     */
    onConfigurationUpdate(newConfig: Configuration): void;
    /**
     * Called when the available memory of the entire device changes to a specified level. You can override this callback
     * to respond to changes in the memory level, for example, releasing cached data.
     *
     * > **NOTE**
     * >
     * > Releasing UI components in the **onMemoryLevel** callback may block the main thread tasks of the current process.
     * >  Therefore, you are advised not to release UI components in this callback.
     *
     * @param { AbilityConstant.MemoryLevel } level - Level of the available memory.<br>**NOTE**<br>The trigger conditions may
     *     differ across various devices. For example, on a standard device with 12 GB of memory:<br>- When the available
     *     memory of the entire device drops to 1700 MB to 1800 MB, the **onMemoryLevel** callback of the MEMORY_LEVEL_MODERATE
     *     type is triggered, indicating that the available memory is moderate.<br>- When the available memory of the entire
     *     device drops to 1600 MB to 1700 MB, the **onMemoryLevel** callback of the MEMORY_LEVEL_LOW type is triggered,
     *     indicating that the available memory is low.<br>- When the available memory of the entire device drops below 1600 MB
     *     , the **onMemoryLevel** callback of the MEMORY_LEVEL_CRITICAL type is triggered, indicating that the available
     *     memory is critically low.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @crossplatform [since 26.0.0]
     * @atomicservice [since 11]
     * @since 9
     */
    onMemoryLevel(level: AbilityConstant.MemoryLevel): void;
}
export default Ability;

```
