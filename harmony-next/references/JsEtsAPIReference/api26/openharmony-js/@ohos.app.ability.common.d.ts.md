# @ohos.app.ability.common.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022-2026 Huawei Device Co., Ltd.
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
import * as _UIAbilityContext from './application/UIAbilityContext';
import type * as _UIExtensionContext from './application/UIExtensionContext';
import * as _AbilityStageContext from './application/AbilityStageContext';
import * as _ApplicationContext from './application/ApplicationContext';
import * as _BaseContext from './application/BaseContext';
import * as _Context from './application/Context';
import * as _ExtensionContext from './application/ExtensionContext';
import * as _FormExtensionContext from './application/FormExtensionContext';
import * as _FormEditExtensionContext from './application/FormEditExtensionContext';
import * as _LiveFormExtensionContext from './application/LiveFormExtensionContext';
import * as _EventHub from './application/EventHub';
import type * as _VpnExtensionContext from './application/VpnExtensionContext';
import type * as _EmbeddableUIAbilityContext from './application/EmbeddableUIAbilityContext';
import type * as _PhotoEditorExtensionContext from './application/PhotoEditorExtensionContext';
import * as _UIServiceProxy from './application/UIServiceProxy';
import * as _UIServiceExtensionConnectCallback from './application/UIServiceExtensionConnectCallback';
import { AbilityResult as _AbilityResult } from './ability/abilityResult';
import type _AbilityStartCallback from './application/AbilityStartCallback';
import { ConnectOptions as _ConnectOptions } from './ability/connectOptions';
import { PacMap as _PacMap } from './ability/dataAbilityHelper';
import { AgentCard as _AgentCard, AgentProvider as _AgentProvider, AgentCapabilities as _AgentCapabilities, AgentSkill as _AgentSkill, AgentAppInfo as _AgentAppInfo } from './application/AgentCard';
import { AgentHostProxy as _AgentHostProxy } from './application/AgentHostProxy';
import _AgentExtensionContext from './application/AgentExtensionContext';
/**
 * You can use this module to reference the ability public module class.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @stagemodelonly
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare namespace common {
    /**
     * Defines the context environment for the [UIAbility]{@link @ohos.app.ability.UIAbility}. It inherits from Context.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    export type UIAbilityContext = _UIAbilityContext.default;
    /**
     * Defines the context environment for the [AbilityStage]{@link @ohos.app.ability.AbilityStage:AbilityStage}. It
     * inherits from Context.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    export type AbilityStageContext = _AbilityStageContext.default;
    /**
     * Defines the application context. It inherits from Context.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    export type ApplicationContext = _ApplicationContext.default;
    /**
     * Defines the parent class of all context types.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    export type BaseContext = _BaseContext.default;
    /**
     * Defines the context base class for the
     * [stage model](docroot://application-models/ability-terminology.md#stage-model).
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    export type Context = _Context.default;
    /**
     * Defines the context environment for the
     * [ExtensionAbility]{@link @ohos.app.ability.ExtensionAbility:ExtensionAbility}. It inherits from Context.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice [since 11]
     * @since 9
     */
    export type ExtensionContext = _ExtensionContext.default;
    /**
     * The context of form extension. It allows access to
     * formExtension-specific resources.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 9
     */
    /**
     * The context of form extension. It allows access to
     * formExtension-specific resources.
     *
     * @typedef { _FormExtensionContext.default }
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 11
     */
    export type FormExtensionContext = _FormExtensionContext.default;
    /**
     * The context of form edit extension. It allows access to
     * formEditExtension-specific resources.
     *
     * @typedef { _FormEditExtensionContext.default }
     * @syscap SystemCapability.Ability.Form
     * @stagemodelonly
     * @atomicservice
     * @since 22
     */
    export type FormEditExtensionContext = _FormEditExtensionContext.default;
    /**
     * The context of live form extension. It allows access to
     * liveFormExtension-specific resources.
     *
     * @typedef { _LiveFormExtensionContext.default }
     * @syscap SystemCapability.Ability.Form
     * @stagemodelonly
     * @atomicservice
     * @since 22
     */
    export type LiveFormExtensionContext = _LiveFormExtensionContext.default;
    /**
     * Defines EventHub, which is an event communication mechanism based on the publish-subscribe pattern.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @crossplatform [since 12]
     * @atomicservice [since 11]
     * @since 9
     */
    export type EventHub = _EventHub.default;
    /**
     * Defines the container of basic data types.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @atomicservice [since 11]
     * @since 9
     */
    export type PacMap = _PacMap;
    /**
     * Defines the result code and data returned when a started ability is terminated.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice [since 11]
     * @since 9
     */
    export type AbilityResult = _AbilityResult;
    /**
     * Defines the connection options. It is used as an input parameter for connection to a background service, to receive
     *  the connection status with the background service.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 9
     */
    export type ConnectOptions = _ConnectOptions;
    /**
     * Defines the context environment for the
     * [UIExtensionAbility]{@link @ohos.app.ability.UIExtensionAbility:UIExtensionAbility}. It inherits from Context.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 10
     */
    export type UIExtensionContext = _UIExtensionContext.default;
    /**
     * Defines the callback invoked to return the UIExtensionAbility startup result. It is usually used as an input
     * parameter in
     * [UIAbilityContext.startAbilityByType]{@link ./application/UIAbilityContext:UIAbilityContext.startAbilityByType(type: string, wantParam: Record<string, Object>, abilityStartCallback: AbilityStartCallback, callback: AsyncCallback<void>)}
     *  or
     * [UIExtensionContext.startAbilityByType]{@link @ohos.app.ability.UIExtensionContentSession:UIExtensionContentSession.startAbilityByType(type: string, wantParam: Record<string, Object>, abilityStartCallback: AbilityStartCallback, callback: AsyncCallback<void>)}
     * .
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 11
     */
    export type AbilityStartCallback = _AbilityStartCallback;
    /**
     * The context of vpn extension. It allows access to
     * vpnExtension-specific resources.
     * The class of auto startup info.
     *
     * @typedef { _VpnExtensionContext.default }
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 11
     */
    export type VpnExtensionContext = _VpnExtensionContext.default;
    /**
     * Defines the context environment for the
     * [EmbeddableUIAbility]{@link @ohos.app.ability.EmbeddableUIAbility:EmbeddableUIAbility}. It inherits from Context.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 12
     */
    export type EmbeddableUIAbilityContext = _EmbeddableUIAbilityContext.default;
    /**
     * The context of an photo editor extension ability.
     *
     * @typedef { _PhotoEditorExtensionContext.default }
     * @syscap SystemCapability.Ability.AppExtension.PhotoEditorExtension
     * @stagemodelonly
     * @since 12
     */
    export type PhotoEditorExtensionContext = _PhotoEditorExtensionContext.default;
    /**
     * Defines the capability for data communication with the UIServiceExtensionAbility. UIServiceExtensionAbility is a
     * special type of ExtensionAbility provided by the system and is used to provide extended capabilities related to
     * floating windows.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 14
     */
    export type UIServiceProxy = _UIServiceProxy.default;
    /**
     * Defines the connection callback. It is used as an input parameter for connection to a UIServiceExtensionAbility, to
     *  provide the callback for the connection.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 14
     */
    export type UIServiceExtensionConnectCallback = _UIServiceExtensionConnectCallback.default;
    /**
     * Defines the context environment for the
     * [AppServiceExtensionAbility](docroot://reference/apis-ability-kit/js-apis-app-ability-appServiceExtensionAbility.md)
     * . It inherits from Context.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @stagemodelonly
     * @since 20
     */
    export type AppServiceExtensionContext = _AppServiceExtensionContext.default;
    /**
     * The AgentCard information describes the basic information and capabilities provided by an Agent.
     *
     * @syscap SystemCapability.Ability.AgentRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 24
     */
    export type AgentCard = _AgentCard;
    /**
     * The Provider in an AgentCard refers to the organization or platform that issues and
     * manages the agent's credentials.
     *
     * @syscap SystemCapability.Ability.AgentRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 24
     */
    export type AgentProvider = _AgentProvider;
    /**
     * Capabilities in an AgentCard represent the specific skills, services, and functions that
     * an agent can perform or provide within the system.
     *
     * @syscap SystemCapability.Ability.AgentRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 24
     */
    export type AgentCapabilities = _AgentCapabilities;
    /**
     * Skills in an AgentCard represent the specific abilities, expertise, and proficiencies that an
     * agent possesses for performing tasks or solving problems.
     *
     * @syscap SystemCapability.Ability.AgentRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 24
     */
    export type AgentSkill = _AgentSkill;
    /**
     * Application-related information for the agent.
     *
     * @syscap SystemCapability.Ability.AgentRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 24
     */
    export type AgentAppInfo = _AgentAppInfo;
    /**
     * The AgentHostProxy is a proxy object for the client connected to the Agent, through which it
     * can communicate with the Agent's connection counterpart.
     *
     * @syscap SystemCapability.Ability.AgentRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 24
     */
    export type AgentHostProxy = _AgentHostProxy;
    /**
     * The context of the agent service ability.
     *
     * @typedef { _AgentExtensionContext }
     * @syscap SystemCapability.Ability.AgentRuntime.Core
     * @stagemodelonly
     * @atomicservice
     * @since 24
     */
    export type AgentExtensionContext = _AgentExtensionContext;
}
export default common;

```
