# @ohos.hiviewdfx.hiRetrieval.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2026 Huawei Device Co., Ltd.
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
 * Provide interfaces and functions for HiRetrieval feature.
 *
 * @syscap SystemCapability.HiviewDFX.HiRetrieval
 * @FaAndStageModel
 * @atomicservice
 * @since 26.0.0
 */
declare namespace hiRetrieval {
    /**
     * HiRetrieval functionality config.
     *
     * @syscap SystemCapability.HiviewDFX.HiRetrieval
     * @FaAndStageModel
     * @atomicservice
     * @since 26.0.0
     */
    interface HiRetrievalConfig {
        /**
         * Custom user type set by developers. No restrictions on format or character types,
         * maximum length is 128 characters and excess characters will be truncated.
         *
         * @syscap SystemCapability.HiviewDFX.HiRetrieval
         * @FaAndStageModel
         * @atomicservice
         * @since 26.0.0
         */
        userType: string;
        /**
         * Custom device type set by developers. No restrictions on format or character types,
         * maximum length is 128 characters and excess characters will be truncated.
         *
         * @syscap SystemCapability.HiviewDFX.HiRetrieval
         * @FaAndStageModel
         * @atomicservice
         * @since 26.0.0
         */
        deviceType: string;
        /**
         * Custom device model set by developers. No restrictions on format or character types,
         * maximum length is 128 characters and excess characters will be truncated.
         *
         * @syscap SystemCapability.HiviewDFX.HiRetrieval
         * @FaAndStageModel
         * @atomicservice
         * @since 26.0.0
         */
        deviceModel: string;
    }
    /**
     * Init the HiRetrieval functionality.
     *
     * @throws { BusinessError } 36000002 - Multi-instance applications not supported error.
     *                                      Possibly caused by invoking this function in a multi-instance application.
     * @syscap SystemCapability.HiviewDFX.HiRetrieval
     * @FaAndStageModel
     * @atomicservice
     * @since 26.0.0
     */
    function init(): void;
    /**
     * Participate the HiRetrieval project with given HiRetrievalConfig.
     *
     * @param { HiRetrievalConfig } config - The config set by the developers.
     * @throws { BusinessError } 36000001 - Initialization error.
     *                                      Possibly caused by invoking this function before invoking init function.
     * @syscap SystemCapability.HiviewDFX.HiRetrieval
     * @FaAndStageModel
     * @atomicservice
     * @since 26.0.0
     */
    function participate(config: HiRetrievalConfig): void;
    /**
     * Quit the HiRetrieval project. This operation clears the current HiRetrieval config.
     * Invoking init function again is required after invoking quit function.
     *
     * @throws { BusinessError } 36000001 - Initialization error.
     *                                      Possibly caused by invoking this function before invoking init function.
     * @syscap SystemCapability.HiviewDFX.HiRetrieval
     * @FaAndStageModel
     * @atomicservice
     * @since 26.0.0
     */
    function quit(): void;
    /**
     * Query if the app is participating the HiRetrieval project.
     *
     * @returns { boolean } Returns true if this app is participating HiRetrieval project, false otherwise.
     * @syscap SystemCapability.HiviewDFX.HiRetrieval
     * @FaAndStageModel
     * @atomicservice
     * @since 26.0.0
     */
    function isParticipant(): boolean;
    /**
     * Query the UNIX timestamp of the last participating time.
     *
     * @returns { number } Returns the timestamp of the last participating time in milliseconds,
     *                   if never participated return 0.
     * @syscap SystemCapability.HiviewDFX.HiRetrieval
     * @FaAndStageModel
     * @atomicservice
     * @since 26.0.0
     */
    function getLastParticipationTimestamp(): number;
    /**
     * Trigger the HiRetrieval functionality, make it start working.
     *
     * @throws { BusinessError } 36000001 - Initialization error.
     *                                      Possibly caused by invoking this function before invoking init function.
     * @syscap SystemCapability.HiviewDFX.HiRetrieval
     * @FaAndStageModel
     * @atomicservice
     * @since 26.0.0
     */
    function run(): void;
    /**
     * Query the current HiRetrieval config.
     *
     * @returns { HiRetrievalConfig } Returns the current HiRetrieval config, an empty HiRetrievalConfig will be returned
     *     if the result of invoking isParticipant function is false.
     * @syscap SystemCapability.HiviewDFX.HiRetrieval
     * @FaAndStageModel
     * @atomicservice
     * @since 26.0.0
     */
    function getCurrentConfig(): HiRetrievalConfig;
}
export default hiRetrieval;

```
