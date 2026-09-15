# @ohos.process.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2021-2022 Huawei Device Co., Ltd.
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
 * @kit ArkTS
 */
/**
 * The **process** module provides process management APIs, for example, APIs for obtaining process information.
 *
 * @syscap SystemCapability.Utils.Lang
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 7
 */
declare namespace process {
    /**
     * Provides APIs for throwing exceptions during the addition of a process.
     *
     * Construct a **ProcessManager** object.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     * @name ProcessManager
     */
    export class ProcessManager {
        /**
         * Checks whether a UID belongs to this application.
         *
         * @param { number } v - UID. which can be obtained by running **process.uid**.
         * @returns { boolean } Check result. The value **true** is returned if the UID belongs to the application;
         *     otherwise, **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        isAppUid(v: number): boolean;
        /**
         * Obtains the UID of a user from the user database of the system based on the specified user name.
         *
         * @param { string } v - User name.
         * @returns { number } UID of the user. If the user does not exist, **-1** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        getUidForName(v: string): number;
        /**
         * Obtains the thread priority based on the specified TID.
         *
         * @param { number } v - TID.
         * @returns { number } Priority of the thread. The priority depends on the operating system.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        getThreadPriority(v: number): number;
        /**
         * Obtains the system configuration.
         *
         * @param { number } name - System configuration parameter name.
         * @returns { number } System configuration obtained. If the configuration does not exist, **-1** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        getSystemConfig(name: number): number;
        /**
         * Obtains the value of an environment variable.
         *
         * > **NOTE**
         * >
         * > Obtains the value of an environment variable. If the environment variable does not exist, **undefined** is
         * > returned.
         *
         * @param { string } name - Environment variable name.
         * @returns { string } Value of the environment variable.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        getEnvironmentVar(name: string): string;
        /**
         * Terminates this process.
         *
         * Exercise caution when using this API. After this API is called, the application exits. If the input parameter
         * is not 0, data loss or exceptions may occur.
         *
         * @param { number } code - Exit code of the process.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        exit(code: number): void;
        /**
         * Sends a signal to the specified process to terminate it. Only the current process can be terminated.
         *
         * @param { number } signal - Signal to send. Value range: 1 <= signal <= 64.
         * @param { number } pid - PID of the process, to which the signal will be sent.
         * @returns { boolean } Signal sending result. The value **true** is returned if the signal is sent successfully;
         *     otherwise, **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        kill(signal: number, pid: number): boolean;
    }
    /**
     * User identifier (UID) of the process.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 7
     */
    const uid: number;
    /**
     * Process ID (PID) of the process.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 7
     */
    const pid: number;
    /**
     * Thread ID (TID) of the thread.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 8
     */
    const tid: number;
    /**
     * Checks whether this process is isolated.
     *
     * @returns { boolean } Check result. The value **true** is returned if the process is isolated; otherwise,
     *     **false** is returned.
     * @syscap SystemCapability.Utils.Lang
     * @atomicservice [since 11]
     * @since 8
     */
    function isIsolatedProcess(): boolean;
    /**
     * Checks whether a UID belongs to this application.
     *
     * @param { number } v - UID.
     * @returns { boolean } Check result. The value **true** is returned if the UID belongs to the application;
     *     otherwise, **false** is returned.
     * @syscap SystemCapability.Utils.Lang
     * @since 8
     * @deprecated since 9
     * @useinstead process.ProcessManager.isAppUid
     */
    function isAppUid(v: number): boolean;
    /**
     * Checks whether this process is running in a 64-bit environment.
     *
     * @returns { boolean } Check result. The value **true** is returned if the process is running in a 64-bit
     *     environment; otherwise, **false** is returned.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 8
     */
    function is64Bit(): boolean;
    /**
     * Obtains the UID of a user from the user database of the system based on the specified user name.
     *
     * @param { string } v - User name.
     * @returns { number } UID of the user.
     * @syscap SystemCapability.Utils.Lang
     * @since 8
     * @deprecated since 9
     * @useinstead process.ProcessManager.getUidForName
     */
    function getUidForName(v: string): number;
    /**
     * Obtains the thread priority based on the specified TID.
     *
     * @param { number } v - TID.
     * @returns { number } Priority of the thread. The priority depends on the operating system.
     * @syscap SystemCapability.Utils.Lang
     * @since 8
     * @deprecated since 9
     * @useinstead process.ProcessManager.getThreadPriority
     */
    function getThreadPriority(v: number): number;
    /**
     * Obtains the duration (excluding the system sleep time), in milliseconds, from the time the system starts to the
     * time the process starts.
     *
     * @returns { number } Duration obtained, in milliseconds.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 8
     */
    function getStartRealtime(): number;
    /**
     * Obtains the CPU time (in milliseconds) from the time the process starts to the current time.
     *
     * @returns { number } CPU time obtained, in milliseconds.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 8
     */
    function getPastCpuTime(): number;
    /**
     * Obtains the system configuration.
     *
     * @param { number } name - System configuration parameter name.
     * @returns { number } System configuration obtained.
     * @syscap SystemCapability.Utils.Lang
     * @since 8
     * @deprecated since 9
     * @useinstead process.ProcessManager.getSystemConfig
     */
    function getSystemConfig(name: number): number;
    /**
     * Obtains the value of an environment variable.
     *
     * @param { string } name - Environment variable name.
     * @returns { string } Value of the environment variable.
     * @syscap SystemCapability.Utils.Lang
     * @since 8
     * @deprecated since 9
     * @useinstead process.ProcessManager.getEnvironmentVar
     */
    function getEnvironmentVar(name: string): string;
    /**
     * Event to store.
     *
     * @param { Object } evt - Event. [since 12]
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 7
     */
    type EventListener = (evt: Object) => void;
    /**
     * Aborts a process and generates a core file. This method will cause a process to exit immediately. Exercise
     * caution when using this method.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 7
     */
    function abort(): void;
    /**
     * Terminates this process.
     *
     * Exercise caution when using this API. After this API is called, the application exits. If the input parameter is
     * not 0, data loss or exceptions may occur.
     *
     * @param { number } code - Exit code of the process.
     * @syscap SystemCapability.Utils.Lang
     * @since 7
     * @deprecated since 9
     * @useinstead process.ProcessManager.exit
     */
    function exit(code: number): void;
    /**
     * Obtains the running time of the current system, in seconds.
     *
     * @returns { number } Running time of the system, in seconds.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 7
     */
    function uptime(): number;
    /**
     * Sends a signal to a specified process to terminate it.
     *
     * @param { number } signal - Signal to send.
     * @param { number } pid - PID of the process, to which the signal will be sent.
     * @returns { boolean } If the signal is sent successfully, **true** is returned. Other, **false** is returned.
     * @syscap SystemCapability.Utils.Lang
     * @since 7
     * @deprecated since 9
     * @useinstead process.ProcessManager.kill
     */
    function kill(signal: number, pid: number): boolean;
}
export default process;

```
