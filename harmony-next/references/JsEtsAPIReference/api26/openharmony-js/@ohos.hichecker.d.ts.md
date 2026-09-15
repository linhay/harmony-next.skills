# @ohos.hichecker.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022 Huawei Device Co., Ltd.
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
 * The HiChecker module allows you to check issues that may be easily ignored during development of applications (
 * including system-built and third-party applications). Such issues include calling of time-consuming functions by key
 * application threads, event distribution and execution timeout in application processes, and ability resource leakage
 * in application processes. The issues are recorded in logs or lead to process crashes explicitly so that you can find
 * and rectify them.
 *
 * @syscap SystemCapability.HiviewDFX.HiChecker
 * @since 8
 */
declare namespace hichecker {
    /**
     * Alarm rule, which is programmed to print a log when an alarm is generated.
     *
     * @constant
     * @syscap SystemCapability.HiviewDFX.HiChecker
     * @since 8
     */
    const RULE_CAUTION_PRINT_LOG = 9223372036854775808n;
    /**
     * Alarm rule, which is programmed to force the application to exit when an alarm is generated.
     *
     * @constant
     * @syscap SystemCapability.HiviewDFX.HiChecker
     * @since 8
     */
    const RULE_CAUTION_TRIGGER_CRASH = 4611686018427387904n;
    /**
     * Caution rule, which is programmed to detect whether any time-consuming function is invoked.
     *
     * @constant
     * @syscap SystemCapability.HiviewDFX.HiChecker
     * @since 8
     */
    const RULE_THREAD_CHECK_SLOW_PROCESS = 1n;
    /**
     * Caution rule, which is programmed to detect whether ability leakage has occurred.
     *
     * @constant
     * @syscap SystemCapability.HiviewDFX.HiChecker
     * @since 8
     */
    const RULE_CHECK_ABILITY_CONNECTION_LEAK = 8589934592n;
    /**
     * Caution rule, which is programmed to detect the ArkUI performance.
     *
     * @constant
     * @syscap SystemCapability.HiviewDFX.HiChecker
     * @since 11
     */
    const RULE_CHECK_ARKUI_PERFORMANCE = 17179869184n;
    /**
     * The thread rule check network usage.
     *
     * @syscap SystemCapability.HiviewDFX.HiChecker
     * @FaAndStageModel
     * @since 26.0.0
     */
    const RULE_THREAD_CHECK_NETWORK_USAGE = 2n;
    /**
     * Adds one or more rules. HiChecker detects unexpected operations or gives feedback based on the added rules.
     *
     * @param { bigint } rule - Rule to be added.
     * @syscap SystemCapability.HiviewDFX.HiChecker
     * @since 8
     * @deprecated since 9
     * @useinstead hichecker.addCheckRule
     */
    function addRule(rule: bigint): void;
    /**
     * Removes one or more rules. The removed rules will become ineffective.
     *
     * @param { bigint } rule - Rule to be removed.
     * @syscap SystemCapability.HiviewDFX.HiChecker
     * @since 8
     * @deprecated since 9
     * @useinstead hichecker.removeCheckRule
     */
    function removeRule(rule: bigint): void;
    /**
     * Obtains a collection of thread, process, and alarm rules that have been added.
     *
     * @returns { bigint } Collection of added rules.
     * @syscap SystemCapability.HiviewDFX.HiChecker
     * @since 8
     */
    function getRule(): bigint;
    /**
     * Checks whether the specified rule exists in the collection of added rules. If the rule is of the thread level, this
     * operation is performed only on the current thread.
     *
     * @param { bigint } rule - Rule to be checked.
     * @returns { boolean } Check result. If the rule exists in the collection of added rules, **true** is returned;
     *     otherwise, **false** is returned.
     * @syscap SystemCapability.HiviewDFX.HiChecker
     * @since 8
     * @deprecated since 9
     * @useinstead hichecker.containsCheckRule
     */
    function contains(rule: bigint): boolean;
    /**
     * Adds one or more check rules. HiChecker detects unexpected operations or gives feedback based on the added rules.
     * You can use **grep HiChecker** to check for the application running information in the hilog.
     *
     * @param { bigint } rule - Rule to be added.
     * @throws { BusinessError } 401 - the parameter check failed, only one bigint type parameter is needed
     * @syscap SystemCapability.HiviewDFX.HiChecker
     * @since 9
     */
    function addCheckRule(rule: bigint): void;
    /**
     * Removes one or more rules. The removed rules will become ineffective.
     *
     * @param { bigint } rule - Rule to be removed.
     * @throws { BusinessError } 401 - the parameter check failed, only one bigint type parameter is needed
     * @syscap SystemCapability.HiviewDFX.HiChecker
     * @since 9
     */
    function removeCheckRule(rule: bigint): void;
    /**
     * Checks whether the specified rule exists in the collection of added rules. If the rule is of the thread level, this
     * operation is performed only on the current thread.
     *
     * @param { bigint } rule - Rule to be checked.
     * @returns { boolean } Check result. If the rule exists in the collection of added rules, **true** is returned;
     *     otherwise, **false** is returned.
     * @throws { BusinessError } 401 - the parameter check failed, only one bigint type parameter is needed
     * @syscap SystemCapability.HiviewDFX.HiChecker
     * @since 9
     */
    function containsCheckRule(rule: bigint): boolean;
}
export default hichecker;

```
