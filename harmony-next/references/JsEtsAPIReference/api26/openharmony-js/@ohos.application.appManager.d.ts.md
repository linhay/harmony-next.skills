# @ohos.application.appManager.d.ts

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
 * @kit API10LessDeprecatedModules
 */
import { AsyncCallback } from './@ohos.base';
import { ProcessRunningInfo } from './application/ProcessRunningInfo';
/**
 * The appManager module provides APIs for application management. For example, you can query whether the system is
 * undergoing a stability test, determine whether the device is RAM-constrained, obtain the maximum memory available to
 * the current application, and retrieve information about running processes.
 *
 * @syscap SystemCapability.Ability.AbilityRuntime.Core
 * @since 8
 * @deprecated since 9
 * @useinstead ohos.app.ability.appManager/appManager
 */
declare namespace appManager {
    /**
     * Checks whether the system is undergoing a stability test. This API uses an asynchronous callback to return the
     * result.
     *
     * > **NOTE**
     * >
     * > A stability test scenario refers to a specific testing environment designed to verify application reliability
     * > under complex, extreme, or long-term operating conditions.
     *
     * @param { AsyncCallback<boolean> } callback - Callback used to return the API call result and the result indicating
     *     whether the system is undergoing a stability test. You can perform error handling or custom processing in this
     *     callback. **true** if the system is undergoing a stability test, **false** otherwise.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.app.ability.appManager/appManager#isRunningInStabilityTest
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
     * @returns { Promise<boolean> } Promise used to return the API call result and the result indicating whether the system is
     *     undergoing a stability test. You can perform error handling or custom processing in this callback. **true** if the
     *     system is undergoing a stability test, **false** otherwise.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.app.ability.appManager/appManager#isRunningInStabilityTest
     */
    function isRunningInStabilityTest(): Promise<boolean>;
    /**
     * Obtains information about the running processes. This API uses a promise to return the result.
     *
     * > This API is deprecated since API version 9. You are advised to use
     * > [appManager.getRunningProcessInformation]{@link @ohos.app.ability.appManager:appManager.getRunningProcessInformation()}
     * >  instead.
     *
     * @permission ohos.permission.GET_RUNNING_INFO
     * @returns { Promise<Array<ProcessRunningInfo>> } Promise used to return the information about the running processes.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.app.ability.appManager/appManager#getRunningProcessInformation
     */
    function getProcessRunningInfos(): Promise<Array<ProcessRunningInfo>>;
    /**
     * Obtains information about the running processes. This API uses an asynchronous callback to return the result.
     *
     * > This API is deprecated since API version 9. You are advised to use
     * > [appManager.getRunningProcessInformation]{@link @ohos.app.ability.appManager:appManager.getRunningProcessInformation()}
     * >  instead.
     *
     * @permission ohos.permission.GET_RUNNING_INFO
     * @param { AsyncCallback<Array<ProcessRunningInfo>> } callback - Callback used to return the information about the running
     *     processes.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @since 8
     * @deprecated since 9
     * @useinstead ohos.app.ability.appManager/appManager#getRunningProcessInformation
     */
    function getProcessRunningInfos(callback: AsyncCallback<Array<ProcessRunningInfo>>): void;
    /**
     * Checks whether the current device is a RAM-constrained device (a device with severely limited memory resources).
     * This API uses a promise to return the result.
     *
     * @returns { Promise<boolean> } Promise used to return the API call result and the result indicating whether the device is
     *     RAM-constrained. You can perform error handling or custom processing in this callback. **true** if the device is RAM
     *     -constrained, **false** otherwise.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.app.ability.appManager/appManager#isRamConstrainedDevice
     */
    function isRamConstrainedDevice(): Promise<boolean>;
    /**
     * Checks whether the current device is a RAM-constrained device (a device with severely limited memory resources).
     * This API uses an asynchronous callback to return the result.
     *
     * @param { AsyncCallback<boolean> } callback - Callback used to return the API call result and the result indicating
     *     whether the device is RAM-constrained. You can perform error handling or custom processing in this callback.
     *     **true** if the device is RAM-constrained, **false** otherwise.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.app.ability.appManager/appManager#isRamConstrainedDevice
     */
    function isRamConstrainedDevice(callback: AsyncCallback<boolean>): void;
    /**
     * Obtains the maximum memory (RAM allocation) available to the current application. This API uses a promise to return
     *  the result.
     *
     * @returns { Promise<number> } Promise used to return the maximum memory (RAM allocation) size, in MB. You can perform
     *     error processing or other custom processing based on the size.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.app.ability.appManager/appManager#getAppMemorySize
     */
    function getAppMemorySize(): Promise<number>;
    /**
     * Obtains the maximum memory (RAM allocation) available to the current application. This API uses an asynchronous
     * callback to return the result.
     *
     * @param { AsyncCallback<number> } callback - Callback used to return the maximum memory (RAM allocation) size, in MB. You
     *     can perform error processing or other custom processing based on the size.
     * @syscap SystemCapability.Ability.AbilityRuntime.Core
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.app.ability.appManager/appManager#getAppMemorySize
     */
    function getAppMemorySize(callback: AsyncCallback<number>): void;
}
export default appManager;

```
