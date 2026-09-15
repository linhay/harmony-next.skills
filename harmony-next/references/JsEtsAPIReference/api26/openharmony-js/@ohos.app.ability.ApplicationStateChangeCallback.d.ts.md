# @ohos.app.ability.ApplicationStateChangeCallback.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2023-2025 Huawei Device Co., Ltd.
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
/**
 * The module is used to listen for state changes of the current application process. For ease of description, the term
 * "application process" will be referred to as "process" in the following sections.
 * You can call
 * [ApplicationContext.on('applicationStateChange')]{@link ./application/ApplicationContext:ApplicationContext.on(type: 'applicationStateChange', callback: ApplicationStateChangeCallback)}
 *  and pass in a custom ApplicationStateChangeCallback to listen for foreground/background state changes of the current
 *  process. This allows you to perform certain actions based on the process state changes, for example, tracking the
 * duration of the process in the foreground and background, or clearing memory caches when the process moves to the
 * background.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
 * @stagemodelonly
 * @crossplatform [since 18]
 * @atomicservice [since 11]
 * @since 10
 */
export default class ApplicationStateChangeCallback {
    /**
     * Called when the current process switches from the background to the foreground. When this callback is triggered,
     * it does not mean that the process is already fully in the foreground state, but rather that it is about to enter
     * the foreground state. At this point, operations that depend on the foreground state (such as launching another
     * UIAbility) cannot be performed.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @crossplatform [since 18]
     * @atomicservice [since 11]
     * @since 10
     */
    onApplicationForeground(): void;
    /**
     * Called when the current process switches from the foreground to the background. When this callback is triggered,
     * the process is fully in the background state, and you can perform operations suitable for the background state
     * (for example, clearing memory caches).
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @crossplatform [since 18]
     * @atomicservice [since 11]
     * @since 10
     */
    onApplicationBackground(): void;
}

```
