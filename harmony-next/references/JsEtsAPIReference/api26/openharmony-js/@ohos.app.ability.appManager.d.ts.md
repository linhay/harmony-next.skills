# @ohos.app.ability.appManager.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022-2024 Huawei Device Co., Ltd.
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
import { ProcessInformation as _ProcessInformation } from './application/ProcessInformation';
import * as _ApplicationStateObserver from './application/ApplicationStateObserver';
import * as _AbilityStateData from './application/AbilityStateData';
import * as _AppStateData from './application/AppStateData';
import type * as _ProcessData from './application/ProcessData';
/**
 * The appManager module implements application management. You can use the APIs of this module to query whether the
 * application is undergoing a stability test, whether the application is running on a RAM constrained device, the
 * memory size of the application, and information about the running process.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @atomicservice [since 11]
 * @since 9
 */
declare namespace appManager {
    /**
     * Enumerates the processes states.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @atomicservice [since 11]
     * @since 10
     */
    export enum ProcessState {
        /**
         * The process is created.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @atomicservice [since 11]
         * @since 10
         */
        STATE_CREATE,
        /**
         * The process is running in the foreground.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @atomicservice [since 11]
         * @since 10
         */
        STATE_FOREGROUND,
        /**
         * At least one window in the process has focus.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @atomicservice [since 11]
         * @since 10
         */
        STATE_ACTIVE,
        /**
         * The process is running in the background.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @atomicservice [since 11]
         * @since 10
         */
        STATE_BACKGROUND,
        /**
         * The process is destroyed.
         *
         * @syscap SystemCapability.Ability.AbilityRuntime.Core
         * @atomicservice [since 11]
         * @since 10
         */
        STATE_DESTROY
    }
    /**
     * Registers an observer to listen for lifecycle changes of all applications.
     *
     * @permission ohos.permission.RUNNING_STATE_OBSERVER
     * @param { 'applicationState' } type - Type of the API to call. It is fixed at **'applicationState'**.
     * @param { ApplicationStateObserver } observer - Application state observer, which is used to listen for applications
     *     lifecycle changes.
     * @returns { number } ID of the observer registered. You can pass this ID to
     *     [off('applicationState')]{@link appManager.off(type: 'applicationState', observerId: number)} to unregister the
     *     observer.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 16000050 - Internal error.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @since 14
     */
    function on(type: 'applicationState', observer: ApplicationStateObserver): number;
    /**
     * Registers an observer to listen for lifecycle changes of the specified application.
     *
     * @permission ohos.permission.RUNNING_STATE_OBSERVER
     * @param { 'applicationState' } type - Type of the API to call. It is fixed at **'applicationState'**.
     * @param { ApplicationStateObserver } observer - Application state observer, which is used to listen for application
     *     lifecycle changes.
     * @param { Array<string> } bundleNameList - **bundleName** array of the application. A maximum of 128 bundle names can be
     *     passed.
     * @returns { number } ID of the observer registered. You can pass this ID to
     *     [off('applicationState')]{@link appManager.off(type: 'applicationState', observerId: number)} to unregister the
     *     observer.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 16000050 - Internal error.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @since 14
     */
    function on(type: 'applicationState', observer: ApplicationStateObserver, bundleNameList: Array<string>): number;
    /**
     * Unregisters the observer used to listen for application state changes. This API uses an asynchronous callback to
     * return the result.
     *
     * @permission ohos.permission.RUNNING_STATE_OBSERVER
     * @param { 'applicationState' } type - Type of the API to call. It is fixed at **'applicationState'**.
     * @param { number } observerId - ID of the observer registered, which is the listener ID returned by
     *     [on('applicationState')]{@link appManager.on(type: 'applicationState', observer: ApplicationStateObserver)}.
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the application state observer is
     *     deregistered, **err** is undefined; otherwise, **error** is an error object.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 16000050 - Internal error.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @since 15
     */
    function off(type: 'applicationState', observerId: number, callback: AsyncCallback<void>): void;
    /**
     * Unregisters the observer used to listen for application state changes. This API uses a promise to return the
     * result.
     *
     * @permission ohos.permission.RUNNING_STATE_OBSERVER
     * @param { 'applicationState' } type - Type of the API to call. It is fixed at **'applicationState'**.
     * @param { number } observerId - ID of the observer registered, which is the listener ID returned by
     *     [on('applicationState')]{@link appManager.on(type: 'applicationState', observer: ApplicationStateObserver)}.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 16000050 - Internal error.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @since 14
     */
    function off(type: 'applicationState', observerId: number): Promise<void>;
    /**
     * Checks whether the system is undergoing a stability test. This API uses an asynchronous callback to return the
     * result.
     *
     * > **NOTE**
     * >
     * > A stability test scenario refers to a specific testing environment designed to verify application reliability
     * > under complex, extreme, or long-term operating conditions.
     *
     * @param { AsyncCallback<boolean> } callback - Callback used to return the result. If the API call is successful, **err**
     *     is **undefined** and **data** is the check result for whether the system is undergoing a stability test. Otherwise,
     *     **err** is an error object. You can perform error handling or other custom processing.<br>**true** is returned if
     *     the system is undergoing a stability test; **false** is returned otherwise.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 16000050 - Internal error.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @atomicservice [since 11]
     * @since 9
     */
    function isRunningInStabilityTest(callback: AsyncCallback<boolean>): void;
    /**
     * Checks whether the system is undergoing a stability test. This API uses a promise to return the result.
     *
     * > **NOTE**
     * >
     * > A stability test scenario refers to a specific testing environment designed to verify application reliability
     * > under complex, extreme, or long-term operating conditions.
     *
     * @returns { Promise<boolean> } Promise used to return the API call result and the result **true** or **false**. You can
     *     perform error handling or custom processing in this callback.
     *
     *     **true** is returned if the system is undergoing a stability test; **false** is returned otherwise.
     * @throws { BusinessError } 16000050 - Internal error.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @atomicservice [since 11]
     * @since 9
     */
    function isRunningInStabilityTest(): Promise<boolean>;
    /**
     * Kills a process by bundle name. This API uses a promise to return the result.
     *
     * @permission ohos.permission.KILL_APP_PROCESSES or ohos.permission.CLEAN_BACKGROUND_PROCESSES
     * @param { string } bundleName - Bundle name.
     * @param { boolean } clearPageStack - Whether to clear the page stack. **true** to clear, **false** otherwise.
     * @param { number } [appIndex] - ID of an application clone. The default value is **0**. If the value is **0**, all processes
     *     of the main application are terminated. If the value is greater than 0, all processes of the specified application
     *     clone are terminated.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - If the input parameter is not valid parameter.
     * @throws { BusinessError } 16000050 - Internal error.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @since 14
     */
    function killProcessesByBundleName(bundleName: string, clearPageStack: boolean, appIndex?: number): Promise<void>;
    /**
     * Checks whether the current device is a RAM-constrained device (a device with severely limited memory resources).
     * This API uses a promise to return the result.
     *
     * @returns { Promise<boolean> } Promise used to return the API call result and the result indicating whether the device is
     *     RAM-constrained. You can perform error handling or custom processing in this callback.
     *     **true** is returned if the device is RAM-constrained; **false** is returned otherwise.
     * @throws { BusinessError } 16000050 - Internal error.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @atomicservice [since 11]
     * @since 9
     */
    function isRamConstrainedDevice(): Promise<boolean>;
    /**
     * Checks whether the current device is a RAM-constrained device (a device with severely limited memory resources).
     * This API uses an asynchronous callback to return the result.
     *
     * @param { AsyncCallback<boolean> } callback - Callback used to return the result. If the API call is successful, **err**
     *     is **undefined** and **data** is the check result for whether the device is RAM-constrained. Otherwise, **err** is
     *     an error object. You can perform error handling or other custom processing.<br>**true** is returned if the device is
     *     RAM-constrained; **false** is returned otherwise.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 16000050 - Internal error.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @atomicservice [since 11]
     * @since 9
     */
    function isRamConstrainedDevice(callback: AsyncCallback<boolean>): void;
    /**
     * Obtains the maximum memory (RAM allocation) available to the current application. This API uses a promise to return
     *  the result.
     *
     * @returns { Promise<number> } Promise used to return the maximum memory (RAM allocation) size, in MB. You can perform error
     *     processing or other custom processing based on the size.
     * @throws { BusinessError } 16000050 - Internal error.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @atomicservice [since 11]
     * @since 9
     */
    function getAppMemorySize(): Promise<number>;
    /**
     * Obtains the maximum memory (RAM allocation) available to the current application. This API uses an asynchronous
     * callback to return the result.
     *
     * @param { AsyncCallback<number> } callback - Callback used to return the result. If the API call is successful, **err** is
     *     **undefined** and **data** is the maximum memory (RAM allocation) available to the current application. Otherwise,
     *     **err** is an error object. You can perform error handling or other custom processing based on the return value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 16000050 - Internal error.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @atomicservice [since 11]
     * @since 9
     */
    function getAppMemorySize(callback: AsyncCallback<number>): void;
    /**
     * Obtains information about the running processes of the current application. This API uses a promise to return the
     * result.
     *
     * > **NOTE**
     * >
     * > - In versions earlier than API version 11, this API requires the ohos.permission.GET_RUNNING_INFO permission,
     * > which is available only for system applications.
     * >
     * > - Starting from API version 11, this API is used only to obtain the process information of the caller. No
     * > permission is required.
     *
     * @permission ohos.permission.GET_RUNNING_INFO [since 9 - 10]
     * @returns { Promise<Array<ProcessInformation>> } Promise used to return the API call result and the process running
     *     information. You can perform error handling or custom processing in this callback.
     * @throws { BusinessError } 16000050 - Internal error.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @atomicservice [since 11]
     * @since 9
     */
    function getRunningProcessInformation(): Promise<Array<ProcessInformation>>;
    /**
     * Obtains information about the running processes of the current application. This API uses an asynchronous callback
     * to return the result.
     *
     * > **NOTE**
     * >
     * > - In versions earlier than API version 11, this API requires the ohos.permission.GET_RUNNING_INFO permission,
     * > which is available only for system applications.
     * >
     * > - Starting from API version 11, this API is used only to obtain the process information of the caller. No
     * > permission is required.
     *
     * @permission ohos.permission.GET_RUNNING_INFO [since 9 - 10]
     * @param { AsyncCallback<Array<ProcessInformation>> } callback - Callback used to return the result. If the API call is
     *     successful, **err** is **undefined** and **data** is the information about the running processes. Otherwise, **err**
     *     is an error object. You can perform error handling or other custom processing.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 16000050 - Internal error.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @atomicservice [since 11]
     * @since 9
     */
    function getRunningProcessInformation(callback: AsyncCallback<Array<ProcessInformation>>): void;
    /**
     * Checks whether the application with the specified bundle name and application clone index is running across all
     * users. This API uses a promise to return the result.
     *
     * > **NOTE**
     * >
     * > If the application is not installed for the current user, error code 16000073 is returned. If the application is
     * > installed for the current user, the system checks whether the application is running across all users.
     *
     * @permission ohos.permission.GET_RUNNING_INFO
     * @param { string } bundleName - Bundle name.
     * @param { number } [appCloneIndex] - Index of an application clone. The value ranges from 0 to 1000. The value **0** means
     *     the main application, and a value greater than 0 means a specific application clone.
     * @returns { Promise<boolean> } Promise used to return the result. **true** is returned if at least one user is running
     *     the specified application. **false** is returned if none of the users are running the application.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 16000050 - Internal error.
     * @throws { BusinessError } 16000073 - The app clone index is invalid.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @since 14
     */
    function isAppRunning(bundleName: string, appCloneIndex?: number): Promise<boolean>;
    /**
     * Defines the ability state data.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @since 14
     */
    export type AbilityStateData = _AbilityStateData.default;
    /**
     * Defines the application state data.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @since 14
     */
    export type AppStateData = _AppStateData.default;
    /**
     * Defines the observer used to listen for application state changes.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @since 14
     */
    export type ApplicationStateObserver = _ApplicationStateObserver.default;
    /**
     * Defines the process information.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @atomicservice [since 11]
     * @since 9
     */
    export type ProcessInformation = _ProcessInformation;
    /**
     * Defines the process data.
     *
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @since 14
     */
    export type ProcessData = _ProcessData.default;
}
export default appManager;

```
