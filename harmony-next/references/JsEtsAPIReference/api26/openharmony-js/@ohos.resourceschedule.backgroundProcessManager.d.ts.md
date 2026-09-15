# @ohos.resourceschedule.backgroundProcessManager.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2025 Huawei Device Co., Ltd.
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
 * @file Background Child Process Management
 * @kit BackgroundTasksKit
 */
/**
 * The **backgroundProcessManager** module provides APIs for background child process management. You can use these APIs
 * to suppress and unsuppress child processes to prevent child processes from occupying too many system resources and
 * causing system stuttering. The APIs take effect only for the child processes created through
 * [OH_Ability_StartNativeChildProcess](docroot://reference/apis-ability-kit/capi-native-child-process-h.md#oh_ability_startnativechildprocess)
 * .
 *
 * @syscap SystemCapability.Resourceschedule.BackgroundProcessManager
 * @since 17
 */
declare namespace backgroundProcessManager {
    /**
     * Specifies the child process priority.
     *
     * @syscap SystemCapability.Resourceschedule.BackgroundProcessManager
     * @since 17
     */
    export enum ProcessPriority {
        /**
         * Compared with **PROCESS_INACTIVE**, **PROCESS_LOWER** has a more significant suppression effect and obtains
         * fewer CPU resources. You are advised to set this priority when executing background child processes that
         * cannot be perceived by users, such as background image-text pages.
         *
         * @syscap SystemCapability.Resourceschedule.BackgroundProcessManager
         * @since 17
         */
        PROCESS_BACKGROUND = 1,
        /**
         * You are advised to set this priority when executing background child processes that can be perceived by users
         * , such as audio playback and navigation.
         *
         * @syscap SystemCapability.Resourceschedule.BackgroundProcessManager
         * @since 17
         */
        PROCESS_INACTIVE = 2
    }
    /**
     * Specifies the power saving mode.
     *
     * @syscap SystemCapability.Resourceschedule.BackgroundProcessManager
     * @since 20
     */
    export enum PowerSaveMode {
        /**
         * Efficiency mode. Applications set to this mode will not enter the power saving mode, where fewer CPU
         * resources are available.
         *
         * @syscap SystemCapability.Resourceschedule.BackgroundProcessManager
         * @since 20
         */
        EFFICIENCY_MODE = 1,
        /**
         * Default mode. Applications set to this mode may follow the system to enter the power saving mode.
         *
         * @syscap SystemCapability.Resourceschedule.BackgroundProcessManager
         * @since 20
         */
        DEFAULT_MODE = 2
    }
    /**
     * Sets the child process priority. After a child process is suppressed, the CPU resources that can be obtained will
     * be limited. If the scheduling policy of the main process changes, for example, from the background to the
     * foreground, the child process changes with the main process. To suppress the child process, call this API again.
     *
     * @param { number } pid - ID of the child process to be suppressed, which is the **pid** parameter after the child
     *     process is created through the
     *     [OH_Ability_StartNativeChildProcess](docroot://reference/apis-ability-kit/capi-native-child-process-h.md#oh_ability_startnativechildprocess)
     *     API.
     * @param { ProcessPriority } priority - Suppression priority.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: priority is out of range.
     * @syscap SystemCapability.Resourceschedule.BackgroundProcessManager
     * @since 17
     */
    function setProcessPriority(pid: number, priority: ProcessPriority): Promise<void>;
    /**
     * Unsuppresses the child process. In this case, the child process follows the scheduling policy of the main
     * process. If the scheduling policy of the main process changes, for example, from the background to the foreground
     * , the child process changes with the main process. The effect is the same as calling **resetProcessPriority**.
     *
     * @param { number } pid - ID of the child process, which is the **pid** parameter of the
     *     [OH_Ability_StartNativeChildProcess](docroot://reference/apis-ability-kit/capi-native-child-process-h.md#oh_ability_startnativechildprocess)
     *     API.
     * @returns { Promise<void> } Promise that returns no value.
     * @syscap SystemCapability.Resourceschedule.BackgroundProcessManager
     * @since 17
     */
    function resetProcessPriority(pid: number): Promise<void>;
    /**
     * Sets the power saving mode for a process. This API uses a promise to return the result.
     *
     * You can set to enter the power saving mode when:
     *
     * - The application is not focused, and there are no audio operations or UI updates.
     * - The application cannot obtain the power lock through the system framework.
     * - The application needs to perform time-consuming computing tasks, such as compression, decompression, and
     * compilation, which are significantly restricted by CPU resources. (In this case, the power saving mode will be
     * enabled forcibly.)
     *
     * @permission ohos.permission.BACKGROUND_MANAGER_POWER_SAVE_MODE
     * @param { number } pid - Process ID.
     * @param { PowerSaveMode } powerSaveMode - Power saving mode.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 31800002 - Parameter error. Possible causes:
     *     <br>  1. Mandatory parameters are left unspecified;
     *     <br>  2. Incorrect parameter types; 3. PowerSaveMode status is out of range.
     * @throws { BusinessError } 31800003 - Setup error, This setting is overridden by settings in Task Manager
     * @throws { BusinessError } 31800004 - The setting failed due to system scheduling reasons.
     * @throws { BusinessError } 801 - Capability not supported.
     * @syscap SystemCapability.Resourceschedule.BackgroundProcessManager
     * @since 20
     */
    function setPowerSaveMode(pid: number, powerSaveMode: PowerSaveMode): Promise<void>;
    /**
     * Queries whether the process is in power saving mode. This API uses a promise to return the result.
     *
     * @permission ohos.permission.BACKGROUND_MANAGER_POWER_SAVE_MODE
     * @param { number } pid - Process ID.
     * @returns { Promise<boolean> } Promise used to return the query result. The value **true** means that the process
     *     is in power saving mode; the value **false** means the opposite.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 31800002 - Parameter error. Possible causes:
     *     <br> 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types;
     * @throws { BusinessError } 801 - Capability not supported.
     * @syscap SystemCapability.Resourceschedule.BackgroundProcessManager
     * @since 20
     */
    function isPowerSaveMode(pid: number): Promise<boolean>;
    /**
     * Obtains the power saving mode of a process. This API uses a promise to return the result.
     *
     * @permission ohos.permission.BACKGROUND_MANAGER_POWER_SAVE_MODE
     * @param { number } pid - Process ID.<br>Value range: any integer greater than 0.
     * @returns { Promise<PowerSaveMode> } Promise that returns the power saving mode of a process.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 31800002 - Parameter error. Possible causes:
     *     1. Mandatory parameters are left unspecified; 2. Incorrect parameter types;
     * @throws { BusinessError } 801 - Capability not supported.
     * @syscap SystemCapability.Resourceschedule.BackgroundProcessManager
     * @since 23
     */
    function getPowerSaveMode(pid: number): Promise<PowerSaveMode>;
}
export default backgroundProcessManager;

```
