# @ohos.app.ability.EnvironmentCallback.d.ts

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
 * The EnvironmentCallback module provides capabilities to listen for system environment changes.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @crossplatform [since 26.0.0]
 * @atomicservice [since 11]
 * @since 9
 */
export default class EnvironmentCallback {
    /**
     * Called when the system configuration changes, after
     * [a listener has been registered for such events]{@link ./application/ApplicationContext:ApplicationContext#on(type: 'environment', callback: EnvironmentCallback)}
     * .
     *
     * @param { Configuration } config - Configuration object after the change.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @crossplatform [since 26.0.0]
     * @atomicservice [since 11]
     * @since 9
     */
    onConfigurationUpdated(config: Configuration): void;
    /**
     * Called when the system memory level changes, after
     * [a listener has been registered for such events]{@link ./application/ApplicationContext:ApplicationContext#on(type: 'environment', callback: EnvironmentCallback)}
     * .
     *
     * @param { AbilityConstant.MemoryLevel } level - Memory level, indicating the available memory of the entire device.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @crossplatform [since 26.0.0]
     * @atomicservice [since 11]
     * @since 9
     */
    onMemoryLevel(level: AbilityConstant.MemoryLevel): void;
}

```
