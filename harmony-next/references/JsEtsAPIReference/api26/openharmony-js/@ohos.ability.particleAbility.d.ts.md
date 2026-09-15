# @ohos.ability.particleAbility.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2021-2023 Huawei Device Co., Ltd.
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
import { AsyncCallback } from './@ohos.base';
import { StartAbilityParameter } from './ability/startAbilityParameter';
import { DataAbilityHelper } from './ability/dataAbilityHelper';
import { NotificationRequest } from './notification/notificationRequest';
import { ConnectOptions } from './ability/connectOptions';
import Want from './@ohos.app.ability.Want';
/**
 * The particleAbility module provides APIs for operating a DataAbility and ServiceAbility. You can use the APIs to
 * start and terminate a ParticleAbility, obtain a dataAbilityHelper object, and connect to or disconnect from a
 * ServiceAbility.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
 * @famodelonly
 * @since 7
 */
declare namespace particleAbility {
    /**
     * Starts a ParticleAbility. This API uses an asynchronous callback to return the result.
     *
     * > **NOTE**
     * >
     * > For details about the startup rules for the components in the FA model, see
     * > [Component Startup Rules (FA Model)](docroot://application-models/component-startup-rules-fa.md).
     *
     * @param { StartAbilityParameter } parameter - Ability to start.
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the ParticleAbility is started, **err**
     *     is **undefined**; otherwise, **err** is an error object.
     * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
     * @famodelonly
     * @since 7
     */
    function startAbility(parameter: StartAbilityParameter, callback: AsyncCallback<void>): void;
    /**
     * Starts a ParticleAbility. This API uses a promise to return the result.
     *
     * > **NOTE**
     * >
     * > For details about the startup rules for the components in the FA model, see
     * > [Component Startup Rules (FA Model)](docroot://application-models/component-startup-rules-fa.md).
     *
     * @param { StartAbilityParameter } parameter - Ability to start.
     * @returns { Promise<void> } Promise used to return the result. Promise that returns no value.
     * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
     * @famodelonly
     * @since 7
     */
    function startAbility(parameter: StartAbilityParameter): Promise<void>;
    /**
     * Terminates this ParticleAbility. This API uses an asynchronous callback to return the result.
     *
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the ParticleAbility is terminated,
     *     **err** is **undefined**; otherwise, **err** is an error object.
     * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
     * @famodelonly
     * @since 7
     */
    function terminateSelf(callback: AsyncCallback<void>): void;
    /**
     * Terminates this ParticleAbility. This API uses a promise to return the result.
     *
     * @returns { Promise<void> } Promise used to return the result. Promise that returns no value.
     * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
     * @famodelonly
     * @since 7
     */
    function terminateSelf(): Promise<void>;
    /**
     * Obtains a dataAbilityHelper object.
     *
     * > **NOTE**
     * >
     * > For details about the startup rules for the components in the FA model, see
     * > [Component Startup Rules (FA Model)](docroot://application-models/component-startup-rules-fa.md).
     * > To access a DataAbility of another application, the target application must be configured with associated
     * > startup (**AssociateWakeUp** set to **true**).
     *
     * @param { string } uri - URI of the file to open.
     * @returns { DataAbilityHelper } A utility class used to help other abilities access a DataAbility.
     * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
     * @famodelonly
     * @since 7
     */
    function acquireDataAbilityHelper(uri: string): DataAbilityHelper;
    /**
     * Requests a continuous task from the system. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.KEEP_BACKGROUND_RUNNING
     * @param { number } id - Notification ID of the continuous task.
     * @param { NotificationRequest } request - Notification parameter, which is used to display information in the
     *     notification bar.
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the continuous task is requested,
     *     **err** is **undefined**. Otherwise, **err** is an error object.
     * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
     * @famodelonly
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.resourceschedule.backgroundTaskManager:backgroundTaskManager.startBackgroundRunning
     */
    function startBackgroundRunning(id: number, request: NotificationRequest, callback: AsyncCallback<void>): void;
    /**
     * Requests a continuous task from the system. This API uses a promise to return the result.
     *
     * @permission ohos.permission.KEEP_BACKGROUND_RUNNING
     * @param { number } id - Notification ID of the continuous task.
     * @param { NotificationRequest } request - Notification parameter, which is used to display information in the
     *     notification bar.
     * @returns { Promise<void> } Promise used to return the result. Promise that returns no value.
     * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
     * @famodelonly
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.resourceschedule.backgroundTaskManager:backgroundTaskManager.startBackgroundRunning
     */
    function startBackgroundRunning(id: number, request: NotificationRequest): Promise<void>;
    /**
     * Requests to cancel a continuous task from the system. This API uses an asynchronous callback to return the result.
     *
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the continuous task is canceled,
     *     **err** is **undefined**. Otherwise, **err** is an error object.
     * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
     * @famodelonly
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.resourceschedule.backgroundTaskManager:backgroundTaskManager.stopBackgroundRunning
     */
    function cancelBackgroundRunning(callback: AsyncCallback<void>): void;
    /**
     * Requests to cancel a continuous task from the system. This API uses a promise to return the result.
     *
     * @returns { Promise<void> } Promise used to return the result. Promise that returns no value.
     * @syscap SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask
     * @famodelonly
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.resourceschedule.backgroundTaskManager:backgroundTaskManager.stopBackgroundRunning
     */
    function cancelBackgroundRunning(): Promise<void>;
    /**
     * Connects this ability to a ServiceAbility.
     *
     * > **NOTE**
     * >
     * > For details about the startup rules for the components in the FA model, see
     * > [Component Startup Rules (FA Model)](docroot://application-models/component-startup-rules-fa.md).
     * > > To connect to a ServiceAbility of another application, the target application must be configured with
     * > associated startup (**AssociateWakeUp** set to **true**).
     *
     * @param { Want } request - ServiceAbility to connect.
     * @param { ConnectOptions } options - Connection options.
     * @returns { number } ID of the connected ServiceAbility. The ID starts from 0 and is incremented by 1 each time a
     *     connection is set up.
     * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
     * @famodelonly
     * @since 7
     */
    function connectAbility(request: Want, options: ConnectOptions): number;
    /**
     * Disconnects this ability from a specific ServiceAbility. This API uses an asynchronous callback to return the
     * result.
     *
     * @param { number } connection - ID of the ServiceAbility to disconnect.
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the disconnection is successful,
     *     **err** is **undefined**. Otherwise, **err** is an error object.
     * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
     * @famodelonly
     * @since 7
     */
    function disconnectAbility(connection: number, callback: AsyncCallback<void>): void;
    /**
     * Disconnects this ability from a specific ServiceAbility. This API uses a promise to return the result.
     *
     * @param { number } connection - ID of the ServiceAbility to disconnect.
     * @returns { Promise<void> } Promise used to return the result. Promise that returns no value.
     * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
     * @famodelonly
     * @since 7
     */
    function disconnectAbility(connection: number): Promise<void>;
    /**
     * Enumerates the error codes that may be returned when an ability is started.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
     * @famodelonly
     * @since 7
     */
    export enum ErrorCode {
        /**
         * Invalid parameter.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.FAModel
         * @famodelonly
         * @since 7
         */
        INVALID_PARAMETER = -1
    }
}
export default particleAbility;

```
