# @ohos.app.agent.AgentExtensionAbility.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2026 Huawei Device Co., Ltd.
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
import AgentExtensionContext from './application/AgentExtensionContext';
import { AgentHostProxy } from './application/AgentHostProxy';
import ExtensionAbility from './@ohos.app.ability.ExtensionAbility';
import Want from './@ohos.app.ability.Want';
/**
 * The class of agent extension ability. This class cannot be used in Harmony Archive(HAR).
 *
 * @extends ExtensionAbility
 * @syscap SystemCapability.Ability.AgentRuntime.Core
 * @stagemodelonly
 * @atomicservice
 * @since 24
 */
declare class AgentExtensionAbility extends ExtensionAbility {
    /**
     * Context of the AgentExtensionAbility.
     *
     * @type { AgentExtensionContext }
     * @syscap SystemCapability.Ability.AgentRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 24
     */
    context: AgentExtensionContext;
    /**
    * Called back when an agent extension is started for initialization.
    *
    * @param { Want } want - Want information, including the ability name and bundle name.
    * @syscap SystemCapability.Ability.AgentRuntime.Core
    * @stagemodelonly
    * @atomicservice
    * @since 24
    */
    onCreate(want: Want): void;
    /**
     * Called back when an agent extension is connected to an ability.
     *
     * @param { Want } want - Indicates connection information about the AgentExtensionAbility.
     * @param { AgentHostProxy } proxy - Indicates the agent service host proxy.
     * @syscap SystemCapability.Ability.AgentRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 24
     */
    onConnect(want: Want, proxy: AgentHostProxy): void;
    /**
     * Called back when data is sent.
     *
     * @param { AgentHostProxy } proxy - Indicates the agent service host proxy.
     * @param { string } data - Indicates the received data.
     * @syscap SystemCapability.Ability.AgentRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 24
     */
    onData(proxy: AgentHostProxy, data: string): void;
    /**
     * Called back when authentication is sent.
     *
     * @param { AgentHostProxy } proxy - Indicates the agent service host proxy.
     * @param { string } handshakeData - Indicates the received handshake data.
     * @syscap SystemCapability.Ability.AgentRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 24
     */
    onAuth(proxy: AgentHostProxy, handshakeData: string): void;
    /**
     * Called back when ability connected to an agent service extension is disconnected.
     *
     * @param { Want } want - Indicates disconnection information about the agent service extension.
     * @param { AgentHostProxy } proxy - Indicates the agent service host proxy.
     * @syscap SystemCapability.Ability.AgentRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 24
     */
    onDisconnect(want: Want, proxy: AgentHostProxy): void;
    /**
     * Called back before an agent service extension is destroyed.
     *
     * @syscap SystemCapability.Ability.AgentRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 24
     */
    onDestroy(): void;
}
export default AgentExtensionAbility;

```
