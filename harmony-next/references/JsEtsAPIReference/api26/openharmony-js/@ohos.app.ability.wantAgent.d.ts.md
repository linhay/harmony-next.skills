# @ohos.app.ability.wantAgent.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022-2023 Huawei Device Co., Ltd.
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
/**
 * The WantAgent module encapsulates a [Want]{@link ./@ohos.app.ability.Want:Want} object, enabling an application to
 * trigger a WantAgent object to perform specified operations (such as starting an ability or publishing a common event)
 * at a future time.
 *
 * The module provides the APIs for creating a WantAgent object, obtaining the bundle name and UID of the application to
 * which a WantAgent object belongs, proactively triggering a WantAgent object, and checking whether two WantAgent
 * objects are the same. A typical use scenario of WantAgent is notification processing. For example, when a user
 * touches a notification, the [trigger]{@link wantAgent.trigger} API of WantAgent is triggered and the target
 * application is started. For details, see
 * [Notification](docroot://notification/notification-with-wantagent.md).
 *
 * @file
 * @kit AbilityKit
 */
import { AsyncCallback } from './@ohos.base';
import Want from './@ohos.app.ability.Want';
import { WantAgentInfo as _WantAgentInfo } from './wantAgent/wantAgentInfo';
import { TriggerInfo as _TriggerInfo } from './wantAgent/triggerInfo';
/**
 * The WantAgent module encapsulates a [Want]{@link ./@ohos.app.ability.Want:Want} object, enabling an application to
 * trigger a WantAgent object to perform specified operations (such as starting an ability or publishing a common event)
 * at a future time.
 *
 * The module provides the APIs for creating a WantAgent object, obtaining the bundle name and UID of the application to
 * which a WantAgent object belongs, proactively triggering a WantAgent object, and checking whether two WantAgent
 * objects are the same. A typical use scenario of WantAgent is notification processing. For example, when a user
 * touches a notification, the [trigger]{@link trigger} API of WantAgent is triggered and the target application is
 * started. For details, see [Notification](docroot://notification/notification-with-wantagent.md).
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @atomicservice [since 12]
 * @since 9
 */
declare namespace wantAgent {
    /**
     * Obtains the bundle name of a WantAgent object.
     * This API uses an asynchronous callback to return the result.
     *
     * @param { WantAgent } agent - Target WantAgent object.
     * @param { AsyncCallback<string> } callback - Callback used to return the bundle name.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 16000007 - Service busy. There are concurrent tasks. Try again later.
     * @throws { BusinessError } 16000151 - Invalid wantAgent object.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @atomicservice [since 12]
     * @since 9
     */
    function getBundleName(agent: WantAgent, callback: AsyncCallback<string>): void;
    /**
     * Obtains the bundle name of a WantAgent object.
     * This API uses a promise to return the result.
     *
     * @param { WantAgent } agent - Target WantAgent object.
     * @returns { Promise<string> } Promise used to return the bundle name.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 16000007 - Service busy. There are concurrent tasks. Try again later.
     * @throws { BusinessError } 16000151 - Invalid wantAgent object.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @atomicservice [since 12]
     * @since 9
     */
    function getBundleName(agent: WantAgent): Promise<string>;
    /**
     * Obtains the user ID of a WantAgent object.
     * This API uses an asynchronous callback to return the result.
     *
     * @param { WantAgent } agent - Target WantAgent object.
     * @param { AsyncCallback<number> } callback - Callback used to return the user ID.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 16000007 - Service busy. There are concurrent tasks. Try again later.
     * @throws { BusinessError } 16000151 - Invalid wantAgent object.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @atomicservice [since 12]
     * @since 9
     */
    function getUid(agent: WantAgent, callback: AsyncCallback<number>): void;
    /**
     * Obtains the user ID of a WantAgent object.
     * This API uses a promise to return the result.
     *
     * @param { WantAgent } agent - Target WantAgent object.
     * @returns { Promise<number> } Promise used to return the user ID.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 16000007 - Service busy. There are concurrent tasks. Try again later.
     * @throws { BusinessError } 16000151 - Invalid wantAgent object.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @atomicservice [since 12]
     * @since 9
     */
    function getUid(agent: WantAgent): Promise<number>;
    /**
     * Cancels a WantAgent object.
     * This API uses an asynchronous callback to return the result.
     *
     * @param { WantAgent } agent - Target WantAgent object.
     * @param { AsyncCallback<void> } callback - Callback used to return the result.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 16000007 - Service busy. There are concurrent tasks. Try again later.
     * @throws { BusinessError } 16000151 - Invalid wantAgent object.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @atomicservice [since 12]
     * @since 9
     */
    function cancel(agent: WantAgent, callback: AsyncCallback<void>): void;
    /**
     * Cancels a WantAgent object.
     * This API uses a promise to return the result.
     *
     * @param { WantAgent } agent - Target WantAgent object.
     * @returns { Promise<void> } Promise used to return the result.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 16000007 - Service busy. There are concurrent tasks. Try again later.
     * @throws { BusinessError } 16000151 - Invalid wantAgent object.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @atomicservice [since 12]
     * @since 9
     */
    function cancel(agent: WantAgent): Promise<void>;
    /**
     * Proactively triggers a WantAgent object.
     * This API uses an asynchronous callback to return the result.
     *
     * @param { WantAgent } agent - Target WantAgent object.
     * @param { TriggerInfo } triggerInfo - {@link TriggerInfo} object.
     * @param { AsyncCallback<CompleteData> } [callback] - Callback used to return the result.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @atomicservice [since 12]
     * @since 9
     */
    function trigger(agent: WantAgent, triggerInfo: TriggerInfo, callback?: AsyncCallback<CompleteData>): void;
    /**
     * Checks whether two WantAgent objects are equal, so as to determine whether the same operation is from the
     * same application.
     * This API uses an asynchronous callback to return the result.
     *
     * @param { WantAgent } agent - The first WantAgent object.
     * @param { WantAgent } otherAgent - The second WantAgent object.
     * @param { AsyncCallback<boolean> } callback - Callback used to return the result. The value <code>true</code> means
     *     that the two WantAgent objects are equal, and <code>false</code> means the opposite.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @atomicservice [since 12]
     * @since 9
     */
    function equal(agent: WantAgent, otherAgent: WantAgent, callback: AsyncCallback<boolean>): void;
    /**
     * Checks whether two WantAgent objects are equal, so as to determine whether the same operation is from the
     * same application.
     * This API uses a promise to return the result.
     *
     * @param { WantAgent } agent - The first WantAgent object.
     * @param { WantAgent } otherAgent - The second WantAgent object.
     * @returns { Promise<boolean> } Promise used to return the result. The value <code>true</code> means that the two
     *     WantAgent objects are equal, and <code>false</code> means the opposite.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @atomicservice [since 12]
     * @since 9
     */
    function equal(agent: WantAgent, otherAgent: WantAgent): Promise<boolean>;
    /**
     * Obtains a WantAgent object.
     * This API uses an asynchronous callback to return the result.
     * If the creation fails, a null WantAgent object is returned.
     *
     * <p>**NOTE**:
     * <br>Third-party applications can set only their own abilities.
     * </p>
     *
     * @param { WantAgentInfo } info - Information about the WantAgent object to obtain.
     * @param { AsyncCallback<WantAgent> } callback - Callback used to return the WantAgent object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 16000007 - Service busy. There are concurrent tasks. Try again later.
     * @throws { BusinessError } 16000151 - Invalid wantAgent object.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @atomicservice [since 12]
     * @since 9
     */
    function getWantAgent(info: WantAgentInfo, callback: AsyncCallback<WantAgent>): void;
    /**
     * Obtains a WantAgent object.
     * This API uses a promise to return the result.
     * If the creation fails, a null WantAgent object is returned.
     *
     * <p>**NOTE**:
     * <br>Third-party applications can set only their own abilities.
     * </p>
     *
     * @param { WantAgentInfo } info - Information about the WantAgent object to obtain.
     * @returns { Promise<WantAgent> } Promise used to return the WantAgent object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 16000007 - Service busy. There are concurrent tasks. Try again later.
     * @throws { BusinessError } 16000151 - Invalid wantAgent object.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @atomicservice [since 12]
     * @since 9
     */
    function getWantAgent(info: WantAgentInfo): Promise<WantAgent>;
    /**
     * Obtains the operation type of a WantAgent object.
     * This API uses an asynchronous callback to return the result.
     *
     * @param { WantAgent } agent - Target WantAgent object.
     * @param { AsyncCallback<number> } callback - Callback used to return the operation type.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 16000007 - Service busy. There are concurrent tasks. Try again later.
     * @throws { BusinessError } 16000015 - Service timeout.
     * @throws { BusinessError } 16000151 - Invalid wantAgent object.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @atomicservice [since 12]
     * @since 9
     */
    function getOperationType(agent: WantAgent, callback: AsyncCallback<number>): void;
    /**
     * Obtains the operation type of a WantAgent object.
     * This API uses a promise to return the result.
     *
     * @param { WantAgent } agent - Indicates the WantAgent.
     * @returns { Promise<number> } Returns the OperationType of the WantAgent.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 16000007 - Service busy. There are concurrent tasks. Try again later.
     * @throws { BusinessError } 16000015 - Service timeout.
     * @throws { BusinessError } 16000151 - Invalid wantAgent object.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @atomicservice [since 12]
     * @since 9
     */
    function getOperationType(agent: WantAgent): Promise<number>;
    /**
     * Enumerates the flags used by the WantAgent objects.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @atomicservice [since 12]
     * @since 9
     */
    export enum WantAgentFlags {
        /**
         * The WantAgent object can be used only once.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @atomicservice [since 12]
         * @since 9
         */
        ONE_TIME_FLAG = 0,
        /**
         * The WantAgent object does not exist and hence it is not created. In this case, <code>null</code> is returned.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @atomicservice [since 12]
         * @since 9
         */
        NO_BUILD_FLAG,
        /**
         * The existing WantAgent object should be canceled before a new object is generated.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @atomicservice [since 12]
         * @since 9
         */
        CANCEL_PRESENT_FLAG,
        /**
         * Extra information of the existing WantAgent object is replaced with that of the new object.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @atomicservice [since 12]
         * @since 9
         */
        UPDATE_PRESENT_FLAG,
        /**
         * The WantAgent object is immutable.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @atomicservice [since 12]
         * @since 9
         */
        CONSTANT_FLAG,
        /**
         * The element property in the current Want can be replaced by the element property in the Want passed in
         * WantAgent.trigger().This processing is not supported yet.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @atomicservice [since 12]
         * @since 9
         */
        REPLACE_ELEMENT,
        /**
         * The action property in the current Want can be replaced by the action property in the Want passed in
         * WantAgent.trigger().This processing is not supported yet.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @atomicservice [since 12]
         * @since 9
         */
        REPLACE_ACTION,
        /**
         * The uri property in the current Want can be replaced by the uri property in the Want passed in
         * WantAgent.trigger().This processing is not supported yet.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @atomicservice [since 12]
         * @since 9
         */
        REPLACE_URI,
        /**
         * The <code>entities</code> property in the current Want can be replaced by the <code>entities</code> property in
         * the Want passed in WantAgent.trigger().This processing is not supported yet.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @atomicservice [since 12]
         * @since 9
         */
        REPLACE_ENTITIES,
        /**
         * The <code>bundleName</code> property in the current Want can be replaced by the <code>bundleName</code> property
         * in the Want passed in WantAgent.trigger().This processing is not supported yet.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @atomicservice [since 12]
         * @since 9
         */
        REPLACE_BUNDLE
    }
    /**
     * Enumerates the operation types of the WantAgent objects.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @atomicservice [since 12]
     * @since 9
     */
    export enum OperationType {
        /**
         * Unknown operation type.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @atomicservice [since 12]
         * @since 9
         */
        UNKNOWN_TYPE = 0,
        /**
         * Starts an ability with a UI.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @atomicservice [since 12]
         * @since 9
         */
        START_ABILITY,
        /**
         * Starts multiple abilities with a UI.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @atomicservice [since 12]
         * @since 9
         */
        START_ABILITIES,
        /**
         * Starts an ability without a UI (valid only in the FA model).
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @atomicservice [since 12]
         * @since 9
         */
        START_SERVICE,
        /**
         * Sends a common event.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @atomicservice [since 12]
         * @since 9
         */
        SEND_COMMON_EVENT
    }
    /**
     * Describes the data returned by the operation of proactive triggering a WantAgent object.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @atomicservice [since 12]
     * @since 9
     */
    export interface CompleteData {
        /**
         * WantAgent object that is triggered.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @atomicservice [since 12]
         * @since 9
         */
        info: WantAgent;
        /**
         * Existing Want that is triggered.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @atomicservice [since 12]
         * @since 9
         */
        want: Want;
        /**
         * Request code that triggers the WantAgent object.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @atomicservice [since 12]
         * @since 9
         */
        finalCode: number;
        /**
         * Final data collected by the common event.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @atomicservice [since 12]
         * @since 9
         */
        finalData: string;
        /**
         * Extra information.
         *
         * @type { ?object } [since 9 - 10]
         * @type { ?Record<string, Object> } [since 11]
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @atomicservice [since 12]
         * @since 9
         */
        extraInfo?: Record<string, Object>;
    }
    /**
     * Defines the TriggerInfo object.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @atomicservice [since 12]
     * @since 9
     */
    export type TriggerInfo = _TriggerInfo;
    /**
     * Defines the WantAgentInfo object.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @atomicservice [since 12]
     * @since 9
     */
    export type WantAgentInfo = _WantAgentInfo;
}
/**
 * Target WantAgent object.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @since 9
 */
export type WantAgent = object;
export default wantAgent;

```
