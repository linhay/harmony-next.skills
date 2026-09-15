# @ohos.app.agent.agentConstant.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2026 Huawei Device Co., Ltd.
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
/**
 * This module provides constants for agent.
 *
 * @syscap SystemCapability.Ability.AgentRuntime.Core
 * @stagemodelonly
 * @atomicservice
 * @since 26.0.0
 */
declare namespace agentConstant {
    /**
     * The type of an AgentCard.
     *
     * @syscap SystemCapability.Ability.AgentRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    export enum AgentCardType {
        /**
        * Application-type agent card.
         *
         * @syscap SystemCapability.Ability.AgentRuntime.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        APP = 0,
        /**
         * Atomic service-type agent card.
         *
         * @syscap SystemCapability.Ability.AgentRuntime.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        ATOMIC_SERVICE = 1
    }
}
export default agentConstant;

```
