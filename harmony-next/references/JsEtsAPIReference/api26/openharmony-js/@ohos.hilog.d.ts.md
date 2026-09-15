# @ohos.hilog.d.ts

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
 * @kit PerformanceAnalysisKit
 */
/**
 * # Parameter Format
 *
 * Parameters in the log are printed in the following format:
 *
 * %{[private flag]}specifier
 *
 * |  Private Flag| Description|
 * | ------------ | ---- |
 * |      Unspecified     | The default value is **private**, indicating that parameters in plaintext are not printed.|
 * |  private     | Prints private parameters.|
 * |  public      | Prints parameters in plaintext.|
 *
 * | Specifier| Description| Example|
 * | ------------ | ---- | ---- |
 * |      d/i      | Prints logs of the **number** and **bigint** types.| 123 |
 * |   s     | Prints logs of the **string undefined bool** and **null** types.| "123" |
 * | o/O | Prints logs of the **object**, **undefined**, and **null** types.<br>This specifier is supported since API
 * version 20.| { 'name': "Jack", 'age': 22 } |
 *
 */
/**
 * The HiLog subsystem allows your applications or services to output logs based on the specified type, level, and
 * format string. Such logs help you learn the running status of applications and better debug programs.
 *
 * @syscap SystemCapability.HiviewDFX.HiLog
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 7
 */
declare namespace hilog {
    /**
     * Prints DEBUG logs.
     *
     * DEBUG logs are not recorded in official versions by default. They are available in debug versions or in official
     * versions with the debug function enabled.
     *
     * @param { number } domain - Service domain of logs. The value ranges from **0x0** to **0xFFFF**. If the value
     *     exceeds the range, logs cannot be printed.<br>You can define the value as required.
     * @param { string } tag - Log tag in the string format. You are advised to use this parameter to identify a
     *     particular service behavior or the class holding the ongoing method. A tag can contain a maximum of 31 bytes.
     *     If a tag exceeds this limit, it will be truncated. Chinese characters are not recommended because garbled
     *     characters or alignment problems may occur.
     * @param { string } format - Format string used to output logs in a specified format. It can contain several elements
     *     , where the parameter type and privacy identifier are mandatory.<br>Parameters labeled **{public}** are public
     *     data and are displayed in plaintext; parameters labeled **{private}** (default value) are private data and are
     *     filtered by **<private>**.
     * @param { any[] } args - Variable-length parameter list corresponding to the format string. The number and type of
     *     parameters must map to the identifier in the format string.
     * @syscap SystemCapability.HiviewDFX.HiLog
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 7
     */
    function debug(domain: number, tag: string, format: string, ...args: any[]): void;
    /**
     * Prints INFO logs.
     *
     * @param { number } domain - Service domain of logs. The value ranges from **0x0** to **0xFFFF**. If the value
     *     exceeds the range, logs cannot be printed.<br>You can define the value as required.
     * @param { string } tag - Log tag in the string format. You are advised to use this parameter to identify a
     *     particular service behavior or the class holding the ongoing method. A tag can contain a maximum of 31 bytes.
     *     If a tag exceeds this limit, it will be truncated. Chinese characters are not recommended because garbled
     *     characters or alignment problems may occur.
     * @param { string } format - Format string used to output logs in a specified format. It can contain several elements
     *     , where the parameter type and privacy identifier are mandatory.<br>Parameters labeled **{public}** are public
     *     data and are displayed in plaintext; parameters labeled **{private}** (default value) are private data and are
     *     filtered by **<private>**.
     * @param { any[] } args - Variable-length parameter list corresponding to the format string. The number and type of
     *     parameters must map to the identifier in the format string.
     * @syscap SystemCapability.HiviewDFX.HiLog
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 7
     */
    function info(domain: number, tag: string, format: string, ...args: any[]): void;
    /**
     * Prints WARN logs.
     *
     * @param { number } domain - Service domain of logs. The value ranges from **0x0** to **0xFFFF**. If the value
     *     exceeds the range, logs cannot be printed.<br>You can define the value as required.
     * @param { string } tag - Log tag in the string format. You are advised to use this parameter to identify a
     *     particular service behavior or the class holding the ongoing method. A tag can contain a maximum of 31 bytes.
     *     If a tag exceeds this limit, it will be truncated. Chinese characters are not recommended because garbled
     *     characters or alignment problems may occur.
     * @param { string } format - Format string used to output logs in a specified format. It can contain several elements
     *     , where the parameter type and privacy identifier are mandatory.<br>Parameters labeled **{public}** are public
     *     data and are displayed in plaintext; parameters labeled **{private}** (default value) are private data and are
     *     filtered by **<private>**.
     * @param { any[] } args - Variable-length parameter list corresponding to the format string. The number and type of
     *     parameters must map to the identifier in the format string.
     * @syscap SystemCapability.HiviewDFX.HiLog
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 7
     */
    function warn(domain: number, tag: string, format: string, ...args: any[]): void;
    /**
     * Prints ERROR logs.
     *
     * @param { number } domain - Service domain of logs. The value ranges from **0x0** to **0xFFFF**. If the value
     *     exceeds the range, logs cannot be printed.<br>You can define the value as required.
     * @param { string } tag - Log tag in the string format. You are advised to use this parameter to identify a
     *     particular service behavior or the class holding the ongoing method. A tag can contain a maximum of 31 bytes.
     *     If a tag exceeds this limit, it will be truncated. Chinese characters are not recommended because garbled
     *     characters or alignment problems may occur.
     * @param { string } format - Format string used to output logs in a specified format. It can contain several elements
     *     , where the parameter type and privacy identifier are mandatory.<br>Parameters labeled **{public}** are public
     *     data and are displayed in plaintext; parameters labeled **{private}** (default value) are private data and are
     *     filtered by **<private>**.
     * @param { any[] } args - Variable-length parameter list corresponding to the format string. The number and type of
     *     parameters must map to the identifier in the format string.
     * @syscap SystemCapability.HiviewDFX.HiLog
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 7
     */
    function error(domain: number, tag: string, format: string, ...args: any[]): void;
    /**
     * Prints FATAL logs.
     *
     * @param { number } domain - Service domain of logs. The value ranges from **0x0** to **0xFFFF**. If the value
     *     exceeds the range, logs cannot be printed.<br>You can define the value as required.
     * @param { string } tag - Log tag in the string format. You are advised to use this parameter to identify a
     *     particular service behavior or the class holding the ongoing method. A tag can contain a maximum of 31 bytes.
     *     If a tag exceeds this limit, it will be truncated. Chinese characters are not recommended because garbled
     *     characters or alignment problems may occur.
     * @param { string } format - Format string used to output logs in a specified format. It can contain several elements
     *     , where the parameter type and privacy identifier are mandatory.<br>Parameters labeled **{public}** are public
     *     data and are displayed in plaintext; parameters labeled **{private}** (default value) are private data and are
     *     filtered by **<private>**.
     * @param { any[] } args - Variable-length parameter list corresponding to the format string. The number and type of
     *     parameters must map to the identifier in the format string.
     * @syscap SystemCapability.HiviewDFX.HiLog
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 7
     */
    function fatal(domain: number, tag: string, format: string, ...args: any[]): void;
    /**
     * Checks whether logs are printable based on the specified service domain, log tag, and log level.
     *
     * @param { number } domain - Service domain of logs. The value ranges from **0x0** to **0xFFFF**. If the value exceeds
     *     the range, logs cannot be printed.<br>You can define the value as required.
     * @param { string } tag - Log tag in the string format. You are advised to use this parameter to identify a
     *     particular service behavior or the class holding the ongoing method. A tag can contain a maximum of 31 bytes.
     *     If a tag exceeds this limit, it will be truncated. Chinese characters are not recommended because garbled
     *     characters or alignment problems may occur.
     * @param { LogLevel } level - Log level.
     * @returns { boolean } Returns **true** logs are printable based on the specified service domain, log tag, and log
     *     level; returns **false** otherwise.
     * @syscap SystemCapability.HiviewDFX.HiLog
     * @atomicservice [since 11]
     * @since 7
     */
    function isLoggable(domain: number, tag: string, level: LogLevel): boolean;
    /**
     * Sets the minimum log level.
     *
     * > **NOTE**
     * >
     * > If the set log level is lower than the
     * > [global log level](docroot://dfx/hilog.md#displaying-and-setting-log-levels), the setting does not take effect.
     * >
     * > This function does not take effect for debug applications.
     *
     * @param { LogLevel } level - Log level.
     * @syscap SystemCapability.HiviewDFX.HiLog
     * @atomicservice
     * @since 15
     */
    function setMinLogLevel(level: LogLevel): void;
    /**
     * Sets the minimum log level of the current application process.
     *
     * You can configure different preference strategies using the **prefer** parameter. The **PREFER_CLOSE_LOG** strategy
     * has the same effect as the **setMinLogLevel()** function.
     *
     * > **NOTE**
     * >
     * > This function does not take effect for debug applications.
     *
     * @param { LogLevel } level - Log level.
     * @param { PreferStrategy } prefer - Preference strategy.
     * @syscap SystemCapability.HiviewDFX.HiLog
     * @atomicservice
     * @since 21
     */
    function setLogLevel(level: LogLevel, prefer: PreferStrategy): void;
    /**
     * Sets the output type of hilog.
     *
     * @param { OutputType } type - output type of hilog.
     * @returns { OutputType } previous output type of hilog.
     * @syscap SystemCapability.HiviewDFX.HiLog
     * @FaAndStageModel
     * @atomicservice
     * @since 26.0.0
     */
    function setOutputType(type: OutputType): OutputType;
    /**
     * Sets the output type for hilog for the domainID list.
     *
     * @param { OutputType } type - output type for hilog.
     * @param { Array<number> } domainIDs - domainID list, if isExclude is true, the output type for the domainID
     *     list is set to DEFAULT, and the output type for the remaining domainIDs is set to the currently
     *     specified output type; if isExclude is false, the output type for the domainID list is set to the
     *     currently specified output type, and the output type for the remaining domainIDs is set to DEFAULT
     * @param { boolean } isExclude - determine whether the domainIDs take effect for the currently specified output type.
     * @returns { OutputType } previous value of output type.
     * @syscap SystemCapability.HiviewDFX.HiLog
     * @FaAndStageModel
     * @atomicservice
     * @since 26.0.0
     */
    function setOutputTypeByDomainID(type: OutputType, domainIDs: Array<number>, isExclude: boolean): OutputType;
    /**
     * Returns the current output type of hilog.
     *
     * @returns { OutputType } current output type for hilog.
     * @syscap SystemCapability.HiviewDFX.HiLog
     * @FaAndStageModel
     * @atomicservice
     * @since 26.0.0
     */
    function getOutputType(): OutputType;
    /**
     * Returns the directory path of hilog logs in the sandbox.
     *     If the output type of hilog is DEFAULT, an empty string is returned.
     *
     * @returns { string } the directory path of hilog logs in the sandbox.
     * @syscap SystemCapability.HiviewDFX.HiLog
     * @FaAndStageModel
     * @atomicservice
     * @since 26.0.0
     */
    function getOutputDir(): string;
    /**
     * Delete all hilog logs in the sandbox.
     *
     * @syscap SystemCapability.HiviewDFX.HiLog
     * @FaAndStageModel
     * @atomicservice
     * @since 26.0.0
     */
    function clean(): void;
    /**
     * Flush hilog logs in the sandbox.
     *
     * @syscap SystemCapability.HiviewDFX.HiLog
     * @FaAndStageModel
     * @atomicservice
     * @since 26.0.0
     */
    function flush(): void;
    /**
     * Returns the list of hilog log file paths in the sandbox for the specified recent time period.
     *
     * @param { number } latestSeconds - the specified time period from a given number of seconds in the past to the present.
     * @returns { Array<string> } list of hilog log file paths in the sandbox for the specified rencent time period,
     *                            with newer files appearing first in the list.
     * @syscap SystemCapability.HiviewDFX.HiLog
     * @FaAndStageModel
     * @atomicservice
     * @since 26.0.0
     */
    function getLogFile(latestSeconds: number): Array<string>;
    /**
     * Enumerates the log levels.
     *
     * @syscap SystemCapability.HiviewDFX.HiLog
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 7
     */
    enum LogLevel {
        /**
         * Log level used to record more detailed process information than INFO logs to help developers analyze service
         * processes and locate faults.
         *
         * @syscap SystemCapability.HiviewDFX.HiLog
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        DEBUG = 3,
        /**
         * Log level used to record key service process nodes and exceptions that occur during service running,
         *
         * for example, no network signal or login failure.
         *
         * These logs should be recorded by the dominant module in the service to avoid repeated logging conducted by
         * multiple invoked modules or low-level functions.
         *
         * @syscap SystemCapability.HiviewDFX.HiLog
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        INFO = 4,
        /**
         * Log level used to record severe, unexpected faults that have little impact on users and can be rectified by the
         * programs themselves or through simple operations.
         *
         * @syscap SystemCapability.HiviewDFX.HiLog
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        WARN = 5,
        /**
         * Log level used to record program or functional errors that affect the normal running or use of the functionality
         * and can be fixed at a high cost, for example, by resetting data.
         *
         * @syscap SystemCapability.HiviewDFX.HiLog
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        ERROR = 6,
        /**
         * Log level used to record program or functionality crashes that cannot be rectified.
         *
         * @syscap SystemCapability.HiviewDFX.HiLog
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        FATAL = 7
    }
    /**
     * Enumerates the preference strategies.
     *
     * @syscap SystemCapability.HiviewDFX.HiLog
     * @crossplatform
     * @atomicservice
     * @since 21
     */
    enum PreferStrategy {
        /**
         * The setting is cleared. The system-controlled minimum log level takes effect.
         *
         * @syscap SystemCapability.HiviewDFX.HiLog
         * @crossplatform
         * @atomicservice
         * @since 21
         */
        UNSET_LOGLEVEL = 0,
        /**
         * The larger value of the new log level and the system-controlled minimum log level takes effect.
         *
         * @syscap SystemCapability.HiviewDFX.HiLog
         * @crossplatform
         * @atomicservice
         * @since 21
         */
        PREFER_CLOSE_LOG = 1,
        /**
         * The smaller value of the new log level and the system-controlled minimum log level takes effect.
         *
         * @syscap SystemCapability.HiviewDFX.HiLog
         * @crossplatform
         * @atomicservice
         * @since 21
         */
        PREFER_OPEN_LOG = 2
    }
    /**
     * Enumerates output type of hilog.
     *
     * @enum { number }
     * @syscap SystemCapability.HiviewDFX.HiLog
     * @FaAndStageModel
     * @crossplatform
     * @atomicservice
     * @since 26.0.0
     */
    enum OutputType {
        /**
         * DEFAULT Default output type, equivalent to CONSOLE_ONLY.
         *
         * @syscap SystemCapability.HiviewDFX.HiLog
         * @FaAndStageModel
         * @crossplatform
         * @atomicservice
         * @since 26.0.0
         */
        DEFAULT = 0,
        /**
         * CONSOLE_ONLY Hilog is output to the console only, equivalent to DEFAULT.
         *
         * @syscap SystemCapability.HiviewDFX.HiLog
         * @FaAndStageModel
         * @crossplatform
         * @atomicservice
         * @since 26.0.0
         */
        CONSOLE_ONLY = 0,
        /**
         * PRIVATE_SANDBOX_ONLY Hilog is output to files in its own private sandbox.
         *
         * @syscap SystemCapability.HiviewDFX.HiLog
         * @FaAndStageModel
         * @crossplatform
         * @atomicservice
         * @since 26.0.0
         */
        PRIVATE_SANDBOX_ONLY = 1,
        /**
         * SHARE_SANDBOX_ONLY Hilog is output to files in its own sandbox, accessible to itself and the hiview service.
         *
         * @syscap SystemCapability.HiviewDFX.HiLog
         * @FaAndStageModel
         * @crossplatform
         * @atomicservice
         * @since 26.0.0
         */
        SHARE_SANDBOX_ONLY = 2,
        /**
         * PRIVATE_SANDBOX_WITH_CONSOLE Enable both CONSOLE_ONLY and PRIVATE_SANDBOX_ONLY at the same time.
         *
         * @syscap SystemCapability.HiviewDFX.HiLog
         * @FaAndStageModel
         * @crossplatform
         * @atomicservice
         * @since 26.0.0
         */
        PRIVATE_SANDBOX_WITH_CONSOLE = 3,
        /**
         * SHARE_SANDBOX_WITH_CONSOLE Enable both CONSOLE_ONLY and SHARE_SANGBOX_ONLY at the same time.
         *
         * @syscap SystemCapability.HiviewDFX.HiLog
         * @FaAndStageModel
         * @crossplatform
         * @atomicservice
         * @since 26.0.0
         */
        SHARE_SANDBOX_WITH_CONSOLE = 4
    }
}
export default hilog;

```
