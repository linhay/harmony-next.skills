# @ohos.app.ability.UIAbility.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022-2025 Huawei Device Co., Ltd.
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
 * UIAbility is an application component that has the UI. It inherits from
 * [Ability]{@link ./@ohos.app.ability.Ability:Ability} and provides
 * [lifecycle](docroot://reference/apis-ability-kit/js-apis-app-ability-uiAbility.md#uiability-lifecycle-states)
 * callbacks such as component creation, destruction, and foreground/background switching. It also provides the
 * [background communication capability](docroot://reference/apis-ability-kit/js-apis-app-ability-uiAbility.md#background-communication-capability)
 * .
 *
 * > **NOTE**
 * >
 * > For details about the inheritance relationship of each ability, see
 * > [Inheritance Relationship](docroot://reference/apis-ability-kit/js-apis-app-ability-ability.md#ability-inheritance-relationship)
 * > .
 *
 * @file
 * @kit AbilityKit
 */
/**
 * # UIAbility Lifecycle States
 *
 * **Figure 1** UIAbility lifecycle states
 *
 * ![Ability lifecycle](docroot://application-models/figures/Ability-Life-Cycle.png)
 *
 * - **Create**: A UIAbility instance has been created. The system triggers the [onCreate]{@link UIAbility.onCreate}
 * callback in this state, where you can perform initialization operations.
 * - **Foreground**: The UIAbility has been brought to the foreground. The system triggers the
 * [onForeground]{@link UIAbility.onForeground} callback in this state, where you can request resources required by the
 * application.
 * - **Background**: The UIAbility has been moved to the background. The system triggers the
 * [onBackground]{@link UIAbility.onBackground} callback in this state, where you can release some application
 * resources.
 * - **Destroy**: The UIAbility instance is about to be destroyed. The system triggers the
 * [onDestroy]{@link UIAbility.onDestroy} callback in this state, where you can save data.
 */
/**
 * # Background Communication Capability
 *
 * **Call** invocations can be used for background communication with the target UIAbility. The following figure shows
 * the Call invocation.
 *
 * **Figure 2** Diagram of Call invocation
 *
 * ![call](docroot://application-models/figures/call.png)
 *
 * - The Caller UIAbility uses
 * [startAbilityByCall()]{@link ./application/UIAbilityContext:UIAbilityContext.startAbilityByCall} to obtain a
 * [Caller]{@link Caller} object and then uses the [call]{@link Caller} API of the Caller object to send data to the
 * Callee UIAbility.
 * - The Callee UIAbility holds a [Callee]{@link Callee} object and uses the [on]{@link UIAbility.onCreate} API of the
 * Callee object to register a callback function for receiving data sent by the Caller object.
 */
import Ability from './@ohos.app.ability.Ability';
import AbilityConstant from './@ohos.app.ability.AbilityConstant';
import Want from './@ohos.app.ability.Want';
import window from './@ohos.window';
import UIAbilityContext from './application/UIAbilityContext';
import rpc from './@ohos.rpc';
/**
 * Defines the callback that is invoked when the stub on the target UIAbility is disconnected.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
 * @stagemodelonly
 * @since 9
 */
export interface OnReleaseCallback {
    /**
     * Defines the callback of OnRelease.
     *
     * @param { string } msg - Message used for disconnection.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @since 9
     */
    (msg: string): void;
}
/**
 * Defines the callback that is invoked when the remote UIAbility state changes in the collaboration scenario.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
 * @stagemodelonly
 * @since 10
 */
export interface OnRemoteStateChangeCallback {
    /**
     * Defines the callback of OnRemoteStateChange.
     *
     * @param { string } msg - Message used for disconnection.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @since 10
     */
    (msg: string): void;
}
/**
 * Defines the callback of the registration message notification of the UIAbility.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
 * @stagemodelonly
 * @since 9
 */
export interface CalleeCallback {
    /**
     * Defines the callback of Callee.
     *
     * @param { rpc.MessageSequence } indata - Data to be transferred.
     * @returns { rpc.Parcelable } Returned data object.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @since 9
     */
    (indata: rpc.MessageSequence): rpc.Parcelable;
}
/**
 * A Caller UIAbility can use the
 * [startAbilityByCall]{@link ./application/UIAbilityContext:UIAbilityContext.startAbilityByCall} API to start the
 * target Callee UIAbility. After the target UIAbility is started successfully, a Caller object is returned to the
 * caller for communication.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
 * @stagemodelonly
 * @since 9
 */
export interface Caller {
    /**
     * Used by a Caller UIAbility to send serialized data, as agreed upon by both parties, to the Callee UIAbility. This
     * API uses a promise to return the result.
     *
     * @param { string } method - Method name agreed upon by the Caller UIAbility and Callee UIAbility, used by the Callee
     *     UIAbility to identify the type of message.
     * @param { rpc.Parcelable } data - Message content sent from the Caller UIAbility to the Callee UIAbility, which is
     *     in serialized form.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 16200001 - The caller has been released.
     * @throws { BusinessError } 16200002 - The callee does not exist.
     * @throws { BusinessError } 16000050 - Internal error.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @since 9
     */
    call(method: string, data: rpc.Parcelable): Promise<void>;
    /**
     * Used by a Caller UIAbility to send serialized data to a Callee UIAbility and return the result after the Callee
     * UIAbility processes the message. This API uses a promise to return the result.
     *
     * @param { string } method - Method name agreed upon by the Caller UIAbility and Callee UIAbility, used by the Callee
     *     UIAbility to identify the type of message.
     * @param { rpc.Parcelable } data - Message content sent from the Caller UIAbility to the Callee UIAbility, which is
     *     in serialized form.
     * @returns { Promise<rpc.MessageSequence> } Promise used to return the response data from the Callee UIAbility.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 16200001 - The caller has been released.
     * @throws { BusinessError } 16200002 - The callee does not exist.
     * @throws { BusinessError } 16000050 - Internal error.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @since 9
     */
    callWithResult(method: string, data: rpc.Parcelable): Promise<rpc.MessageSequence>;
    /**
     * Used by a Caller UIAbility to proactively release the connection with the Callee UIAbility. After this API is
     * called, the Caller UIAbility can no longer use **call** or **callWithResult** to send messages to the Callee
     * UIAbility.
     *
     * @throws { BusinessError } 16200001 - The caller has been released.
     * @throws { BusinessError } 16200002 - The callee does not exist.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @since 9
     */
    release(): void;
    /**
     * Used by the Caller UIAbility to register a listener for disconnection notifications from the Callee UIAbility.
     *
     * @param { OnReleaseCallback } callback - Callback used to return the result.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 16200001 - The caller has been released.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @since 9
     */
    onRelease(callback: OnReleaseCallback): void;
    /**
     * Called when the remote UIAbility state changes in the collaboration scenario. This API uses an asynchronous
     * callback to return the result.
     *
     * @param { OnRemoteStateChangeCallback } callback - Callback used to return the result.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types.
     * @throws { BusinessError } 16200001 - The caller has been released.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @since 10
     */
    onRemoteStateChange(callback: OnRemoteStateChangeCallback): void;
    /**
     * Used by the Caller UIAbility to register a listener for disconnection notifications from the Callee UIAbility.
     *
     * @param { 'release' } type - Event type. The value is fixed at **'release'**.
     * @param { OnReleaseCallback } callback - Callback used to return the result.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 16200001 - The caller has been released.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @since 9
     */
    on(type: 'release', callback: OnReleaseCallback): void;
    /**
     * Unregisters the listener for disconnection notifications from the Callee UIAbility. This is the reverse operation
     * of [on('release')]{@link Caller.on}. It is currently not supported.
     *
     * @param { 'release' } type - Event type. The value is fixed at **'release'**.
     * @param { OnReleaseCallback } callback - Callback used to return the result.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @since 9
     */
    off(type: 'release', callback: OnReleaseCallback): void;
    /**
     * Unregisters the listener for disconnection notifications from the Callee UIAbility. This is the reverse operation
     * of [Caller.on('release')]{@link Caller.on}. It is currently not supported.
     *
     * @param { 'release' } type - Event type. The value is fixed at **'release'**.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @since 9
     */
    off(type: 'release'): void;
}
/**
 * Background communication object created by the system for the UIAbility, known as the Callee UIAbility (Callee),
 * which is capable of receiving data sent from the Caller object.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
 * @stagemodelonly
 * @since 9
 */
export interface Callee {
    /**
     * Registers a caller notification callback, which is invoked when the target UIAbility registers a function.
     *
     * @param { string } method - Method name agreed upon by the Caller UIAbility and Callee UIAbility, used by the Callee
     *     UIAbility to identify the type of message.
     * @param { CalleeCallback } callback - JS notification synchronization callback of the
     *     [rpc.MessageSequence]{@link ./@ohos.rpc:rpc.MessageSequence} type. The callback must return at least one empty
     *     [rpc.Parcelable]{@link ./@ohos.rpc:rpc.Parcelable} object. Otherwise, the function execution fails.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 16200004 - The method has been registered.
     * @throws { BusinessError } 16000050 - Internal error.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @since 9
     */
    on(method: string, callback: CalleeCallback): void;
    /**
     * Unregisters a caller notification callback, which is invoked when the target UIAbility registers a function.
     *
     * @param { string } method - Registered notification message string.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 16200005 - The method has not been registered.
     * @throws { BusinessError } 16000050 - Internal error.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @since 9
     */
    off(method: string): void;
}
/**
 * Application component that has the UI. It provides lifecycle callbacks such as component creation, destruction, and
 * foreground/background switching, and supports background communication.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
 * @stagemodelonly
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare class UIAbility extends Ability {
    /**
     * Context of the UIAbility.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    context: UIAbilityContext;
    /**
     * Want in the request used to
     * [cold start](docroot://application-models/uiability-intra-device-interaction.md#cold-starting-uiability) the
     * UIAbility. The value is the Want received in [onCreate]{@link UIAbility.onCreate}.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @atomicservice [since 11]
     * @since 9
     */
    launchWant: Want;
    /**
     * Want in the most recent request to launch the UIAbility.
     *
     * - On the first launch of a UIAbility, it is the Want parameter received in [onCreate]{@link UIAbility.onCreate}.
     * - On subsequent launches, it is the most recent Want received in [onNewWant]{@link UIAbility.onNewWant}.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @atomicservice [since 11]
     * @since 9
     */
    lastRequestWant: Want;
    /**
     * Background communication object created by the system for the UIAbility, known as the Callee UIAbility (Callee),
     * which is capable of receiving data sent from the Caller object.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @since 9
     */
    callee: Callee;
    /**
     * Custom UIAbility ID. This parameter is available only when the UIAbility launch mode is set to
     * [specified](docroot://application-models/uiability-launch-type.md#specified).
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @since 23
     */
    specifiedId?: string;
    /**
     * Called when a UIAbility instance is created. You can execute initialization logic (such as defining variables and
     * loading resources) in this callback. This callback is invoked during a
     * [cold start](docroot://application-models/uiability-intra-device-interaction.md#cold-starting-uiability) of the
     * UIAbility.
     *
     * This API returns the result synchronously and does not support asynchronous callback.
     *
     * @param { Want } want - Data passed by the caller when launching the UIAbility.
     * @param { AbilityConstant.LaunchParam } launchParam - Parameters for application launch, including the reason for
     *     application launch and the reason for the last application exit.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void;
    /**
     * Called when a [WindowStage]{@link ./@ohos.window} instance is created. You can load a page through the WindowStage
     * instance in this callback.
     *
     * @param { window.WindowStage } windowStage - WindowStage instance.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    onWindowStageCreate(windowStage: window.WindowStage): void;
    /**
     * Called when the WindowStage instance is about to be destroyed. You can cancel the listening of WindowStage events
     * in this lifecycle.
     *
     * @param { window.WindowStage } windowStage - WindowStage instance.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @atomicservice
     * @since 12
     */
    onWindowStageWillDestroy(windowStage: window.WindowStage): void;
    /**
     * Called when the WindowStage instance has been destroyed. It informs applications that the WindowStage instance is
     * no longer available for use.
     *
     * The callback is invoked only when the UIAbility exits gracefully. It is not invoked in cases of abnormal exits (for
     * example, process termination due to low memory conditions).
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    onWindowStageDestroy(): void;
    /**
     * Called when the page stack is restored for the target UIAbility during cross-device migration.
     *
     * > **NOTE**
     * >
     * > When an application is launched as a result of a migration, the **onWindowStageRestore()** lifecycle callback
     * > function, rather than **onWindowStageCreate()**, is triggered following [onCreate()]{@link UIAbility.onCreate} or
     * > [onNewWant()]{@link UIAbility.onNewWant}. This sequence occurs for both
     * > [cold start](docroot://application-models/uiability-intra-device-interaction.md#cold-starting-uiability) and
     * > [hot start](docroot://application-models/uiability-intra-device-interaction.md#hot-starting-uiability).
     *
     * @param { window.WindowStage } windowStage - WindowStage instance.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @atomicservice [since 11]
     * @since 9
     */
    onWindowStageRestore(windowStage: window.WindowStage): void;
    /**
     * Called when the UIAbility is destroyed (for example, when the UIAbility is terminated using the
     * [terminateSelf]{@link ./application/UIAbilityContext:UIAbilityContext.terminateSelf(callback: AsyncCallback<void>)}
     * API). You can clear resources and save data during this lifecycle.
     *
     * This API returns the result synchronously or uses a promise to return the result.
     *
     * > **NOTE**
     * >
     * > - Once the **onDestroy** lifecycle callback completes, the application may exit. This can interrupt any pending
     * > asynchronous operations (such as asynchronously writing data to a database), preventing them from finishing
     * > successfully. In this case, you are advised to use a promise to return the result.
     * >
     * > - The callback is invoked only when the UIAbility exits gracefully. It is not invoked in cases of abnormal exits
     * > (for example, process termination due to low memory conditions).
     *
     * @returns { void | Promise<void> } No return value or a Promise object that returns no result.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    onDestroy(): void | Promise<void>;
    /**
     * Called when the application is initially launched into the foreground or transitions from the background to the
     * foreground. You can request necessary system resources, for example, requesting location services when the
     * application transitions to the foreground, within this callback.
     *
     * This API returns the result synchronously and does not support asynchronous callback.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    onForeground(): void;
    /**
     * Called just before the application transitions to the foreground. It is called before
     * [onForeground]{@link UIAbility.onForeground}. It can be used to capture the moment when the application starts to
     * transition to the foreground. When paired with [onDidForeground]{@link UIAbility.onDidForeground}, it can also
     * measure the duration from the application's initial foreground entry to its full transition into the foreground
     * state.
     *
     * This API returns the result synchronously and does not support asynchronous callback.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    onWillForeground(): void;
    /**
     * Called after the application has transitioned to the foreground. It is called after
     * [onForeground]{@link UIAbility.onForeground}. It can be used to capture the moment when the application fully
     * transitions to the foreground. When paired with [onWillForeground]{@link UIAbility.onWillForeground}, it can also
     * measure the duration from the application's initial foreground entry to its full transition into the foreground
     * state.
     *
     * This API returns the result synchronously and does not support asynchronous callback.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    onDidForeground(): void;
    /**
     * Called when the application transitions from the foreground to the background. You can release resources when the
     * UI is no longer visible, for example, stopping location services, within this callback.
     *
     * This API returns the result synchronously and does not support asynchronous callback.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    onBackground(): void;
    /**
     * Called just when the application transitions to the background. It is called before
     * [onBackground]{@link UIAbility.onBackground}. It can be used to log various types of data, such as faults,
     * statistics, security information, and user behavior that occur during application running.
     *
     * This API returns the result synchronously and does not support asynchronous callback.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    onWillBackground(): void;
    /**
     * Called after the application has transitioned to the background. It is called after
     * [onBackground]{@link UIAbility.onBackground}. It can be used to release resources after the application has entered
     * the background, for example, stopping audio playback.
     *
     * This API returns the result synchronously and does not support asynchronous callback.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    onDidBackground(): void;
    /**
     * Called when a UIAbility is to be migrated across devices. You can save service data to be migrated.
     *
     * > **NOTE**
     * >
     * > For versions prior to API version 18, only synchronous calls are supported. Starting from API version 18,
     * > asynchronous calls are also supported.
     *
     * @param { object } wantParam - Data to be migrated. [since 9 - 10]
     * @param { Record<string, Object> } wantParam - Data to be migrated. [since 11]
     * @returns { AbilityConstant.OnContinueResult } Return the result of onContinue. [since 9 - 11]
     * @returns { AbilityConstant.OnContinueResult | Promise<AbilityConstant.OnContinueResult> } Whether the migration is
     *     accepted. The options are as follows:
     *     <br>- **AGREE**: The migration is allowed.
     *     <br>- **REJECT**: The migration is rejected, for example, when an application is abnormal in **onContinue()**.
     *     <br>- **MISMATCH**: The application versions of the source and target devices do not match. The application on the
     *     source device can obtain the version of the target application from **onContinue**. If the ability continuation
     *     cannot be performed due to version mismatch, this result is returned.
     *     <br> This callback comes in pairs with **onWindowStageRestore**. In ability continuation scenarios, the source
     *     UIAbility triggers **onContinue** to save custom data, and the target UIAbility triggers
     *     **onWindowStageRestore** to restore the custom data. [since 12]
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @atomicservice [since 11]
     * @since 9
     */
    onContinue(wantParam: Record<string, Object>): AbilityConstant.OnContinueResult | Promise<AbilityConstant.OnContinueResult>;
    /**
     * Called when a started UIAbility instance is brought up again. If there are specific scenarios where you do not want
     * this lifecycle callback to be triggered, you can use
     * [setOnNewWantSkipScenarios]{@link ./application/UIAbilityContext:UIAbilityContext.setOnNewWantSkipScenarios} to set
     * those [scenarios]{@link ./@ohos.app.ability.contextConstant:contextConstant.Scenarios}.
     *
     * This API returns the result synchronously and does not support asynchronous callback.
     *
     * @param { Want } want - Data passed by the caller when re-launching the UIAbility.
     * @param { AbilityConstant.LaunchParam } launchParam - UIAbility launch parameters, including the launch reason.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void;
    /**
     * Called when UIAbility data is dumped by running the dump command during application debugging. You can return non-
     * sensitive information to be dumped by the UIAbility in this callback.
     *
     * @param { Array<string> } params - Parameters for the dump command.
     * @returns { Array<string> } Information returned by the dump operation.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @atomicservice [since 11]
     * @since 9
     */
    onDump(params: Array<string>): Array<string>;
    /**
     * This API must be used with [appRecovery]{@link ./@ohos.app.ability.appRecovery:appRecovery}. When the application has
     * enabled the fault recovery feature (with the **saveOccasion** parameter in
     * [enableAppRecovery]{@link ./@ohos.app.ability.appRecovery:appRecovery.enableAppRecovery} set to **SAVE_WHEN_ERROR**),
     * this callback is invoked to save the UIAbility data in the case of an application fault.
     *
     * > **NOTE**
     * >
     * > Starting from API version 20, this callback is not executed when
     * > [onSaveStateAsync]{@link UIAbility.onSaveStateAsync(stateType: AbilityConstant.StateType, wantParam: Record<string, Object>)}
     * > is implemented.
     *
     * @param { AbilityConstant.StateType } reason - Reason for triggering the application to save its state. Currently,
     *     only **APP_RECOVERY** (fault recovery scenario) is supported.
     * @param { object } wantParam - Custom application state data, which is stored in **Want.parameters** in
     *     [onCreate]{@link UIAbility.onCreate} when the application restarts. [since 9 - 10]
     * @param { Record<string, Object> } wantParam - Custom application state data, which is stored in **Want.parameters**
     *     in [onCreate]{@link UIAbility.onCreate} when the application restarts. [since 11]
     * @returns { AbilityConstant.OnSaveResult } An object indicating the data-saving policy (for example, all denied, all
     *     allowed, or only allowed in fault recovery scenarios).
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @atomicservice [since 11]
     * @since 9
     */
    onSaveState(reason: AbilityConstant.StateType, wantParam: Record<string, Object>): AbilityConstant.OnSaveResult;
    /**
     * This API must be used with [appRecovery]{@link ./@ohos.app.ability.appRecovery:appRecovery}. When the application has
     * enabled the fault recovery feature (with the **saveOccasion** parameter in
     * [enableAppRecovery]{@link ./@ohos.app.ability.appRecovery:appRecovery.enableAppRecovery} set to **SAVE_WHEN_ERROR**),
     * this callback is invoked to save the UIAbility data in the case of an application fault. This API uses a promise to
     * return the result.
     *
     * @param { AbilityConstant.StateType } stateType - Reason for triggering the application to save its state. Currently
     *     , only **APP_RECOVERY** (fault recovery scenario) is supported.
     * @param { Record<string, Object> } wantParam - Custom application state data, which is stored in **Want.parameters**
     *     in [onCreate]{@link UIAbility.onCreate} when the application restarts.
     * @returns { Promise<AbilityConstant.OnSaveResult> } Promise used to return the result. An object indicating the data
     *     -saving policy (for example, all denied, all allowed, or only allowed in fault recovery scenarios).
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @atomicservice
     * @since 20
     */
    onSaveStateAsync(stateType: AbilityConstant.StateType, wantParam: Record<string, Object>): Promise<AbilityConstant.OnSaveResult>;
    /**
     * Called when an atomic service is shared across devices. You can set the title, abstract, and URL of the atomic
     * service to be shared in this callback.
     *
     * @param { object } wantParam - Data to share. [since 10 - 10]
     * @param { Record<string, Object> } wantParam - Data to share. [since 11]
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @atomicservice [since 11]
     * @since 10
     */
    onShare(wantParam: Record<string, Object>): void;
    /**
     * Triggered by the system just before the UIAbility is about to close (for example, when the user clicks the close
     * button in the top-right corner of the application window or exits from the dock or system tray), allowing for
     * additional operations to be performed before the UIAbility is officially shut down. You can return **true** to
     * block the current closure attempt and then manually call
     * [terminateSelf]{@link ./application/UIAbilityContext:UIAbilityContext#terminateSelf(callback: AsyncCallback<void>)}
     * at an appropriate time to close it. For example, you might ask the user to confirm whether they want to close the
     * UIAbility and then proceed with the closure manually.
     * This API executes the callback normally only on 2-in-1 devices and tablets. It does not execute the callback on
     * other devices.
     *
     * > **NOTE**
     * >
     * > - Starting from API version 15, this callback is not executed when
     * > [UIAbility.onPrepareToTerminateAsync]{@link UIAbility.onPrepareToTerminateAsync} is implemented. When
     * > [AbilityStage.onPrepareTerminationAsync]{@link ./@ohos.app.ability.AbilityStage:AbilityStage.onPrepareTerminationAsync}
     * > or [AbilityStage.onPrepareTermination]{@link ./@ohos.app.ability.AbilityStage:AbilityStage.onPrepareTermination} is
     * > implemented, this callback is not executed if the user right-clicks the dock bar or system tray to close the
     * > UIAbility.
     * >
     * > - Additionally, if the application or a third-party framework registers a listener for
     * > [window.WindowStage.on('windowStageClose')](docroot://reference/apis-arkui/arkts-apis-window-WindowStage.md#onwindowstageclose14)
     * > , this callback function is not executed.
     *
     * @permission ohos.permission.PREPARE_APP_TERMINATE
     * @returns { boolean } Whether to terminate the UIAbility.
     *     <br>The value <code>true</code> means that the termination process is canceled.
     *     <br>The value <code>false</code> means to continue terminating the UIAbility.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @atomicservice [since 11]
     * @since 10
     */
    onPrepareToTerminate(): boolean;
    /**
     * Triggered by the system just before the UIAbility is close (for example, when the user clicks the close button in
     * the top-right corner of the application window or exits from the dock or system tray), allowing for additional
     * operations to be performed before the UIAbility is officially shut down.
     *
     * You can return **true** to block the current closure attempt and then manually call
     * [terminateSelf]{@link ./application/UIAbilityContext:UIAbilityContext.terminateSelf(callback: AsyncCallback<void>)}
     * at an appropriate time to close it. For example, you might ask the user to confirm whether they want to close the
     * UIAbility and then proceed with the closure manually.
     * Starting from API version 15, this API executes the callback normally only on 2-in-1 devices. It does not execute
     * the callback on other devices.
     * Starting from API version 19, this API executes the callback normally only on 2-in-1 devices and tablets. It does
     * not execute the callback on other devices.
     *
     * > **NOTE**
     * >
     * > - When
     * > [AbilityStage.onPrepareTerminationAsync]{@link ./@ohos.app.ability.AbilityStage:AbilityStage.onPrepareTerminationAsync}
     * > or [AbilityStage.onPrepareTermination]{@link ./@ohos.app.ability.AbilityStage:AbilityStage.onPrepareTermination} is
     * > implemented, this callback is not executed if the user right-clicks the dock bar or system tray to close the
     * > UIAbility.
     * >
     * > - Additionally, if the application or a third-party framework registers a listener for
     * > [window.WindowStage.on('windowStageClose')](docroot://reference/apis-arkui/arkts-apis-window-WindowStage.md#onwindowstageclose14)
     * > , this callback function is not executed.
     * >
     * > - If an asynchronous callback crashes, it will be handled as a timeout. If the UIAbility does not respond within
     * > 10 seconds, it will be terminated forcibly.
     *
     * @permission ohos.permission.PREPARE_APP_TERMINATE
     * @returns { Promise<boolean> } Promise used to return the result.
     *     <br>The value <code>true</code> means that the termination process is canceled.
     *     <br>The value <code>false</code> means to continue terminating the UIAbility.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @atomicservice
     * @since 15
     */
    onPrepareToTerminateAsync(): Promise<boolean>;
    /**
     * Called when an operation of going back to the previous page is triggered on this UIAbility. The return value
     * determines whether to destroy the UIAbility instance.
     *
     * - When the target SDK version is earlier than 12, the default return value is **false**, indicating that the
     * UIAbility will be destroyed.
     * - When the target SDK version is 12 or later, the default return value is **true**, indicating that the UIAbility
     * will be moved to the background and will not be destroyed.
     *
     * @returns { boolean } The value <code>true</code> means that the UIAbility instance will be moved to the background
     *     and will not be destroyed, and <code>false</code> means that the UIAbility instance will be destroyed.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @atomicservice [since 11]
     * @since 10
     */
    onBackPressed(): boolean;
    /**
     * Callback invoked to return the collaboration result in multi-device collaboration scenarios.
     *
     * > **NOTE**
     * >
     * > - This callback does not support ability launch in
     * > [specified mode](docroot://application-models/uiability-launch-type.md#specified).
     * >
     * > - When you use methods such as
     * > [startAbility]{@link ./application/UIAbilityContext:UIAbilityContext.startAbility(want: Want, callback: AsyncCallback<void>)}
     * > to start an application, you must include **FLAG_ABILITY_ON_COLLABORATE** in
     * > [Flags]{@link ./@ohos.app.ability.wantConstant:wantConstant.Flags} in the Want object.
     * >
     * > - During a
     * > [cold start](docroot://application-models/uiability-intra-device-interaction.md#cold-starting-uiability), this
     * > callback must be invoked before [onForeground]{@link UIAbility.onForeground} or after
     * > [onBackground]{@link UIAbility.onBackground}. During a
     * > [hot start](docroot://application-models/uiability-intra-device-interaction.md#hot-starting-uiability), this
     * > callback must be invoked before [onNewWant]{@link UIAbility.onNewWant}.
     *
     * @param { Record<string, Object> } wantParam - Want parameter, which supports only the key
     *     **"ohos.extra.param.key.supportCollaborateIndex"**. The key can be used to obtain the data passed by the caller
     *     and perform corresponding processing.
     * @returns { AbilityConstant.CollaborateResult } Whether the coordinator accepts the collaboration result.
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @since 18
     */
    onCollaborate(wantParam: Record<string, Object>): AbilityConstant.CollaborateResult;
    /**
     * Indicates whether the UIAbility has been destroyed. The default value is **false**.
     *
     * After the [onDestroy]{@link UIAbility.onDestroy} callback is executed, this property is set to **true**.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.AbilityCore
     * @stagemodelonly
     * @since 26.0.0
     */
    isDestroyed: boolean;
}
export default UIAbility;

```
