# @ohos.hiTraceChain.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2021 Huawei Device Co., Ltd.
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
 * @file Distributed Tracing
 * @kit PerformanceAnalysisKit
 */
/**
 * The **hiTraceChain** module implements call chain trace throughout a service process. It provides functions such as
 * starting and stopping call chain trace and configuring trace points.
 *
 * @syscap SystemCapability.HiviewDFX.HiTrace
 * @since 8
 */
declare namespace hiTraceChain {
    /**
     * Enumerates trace flag types.
     *
     * @syscap SystemCapability.HiviewDFX.HiTrace
     * @since 8
     */
    enum HiTraceFlag {
        /**
         * Default flag.
         *
         * @syscap SystemCapability.HiviewDFX.HiTrace
         * @since 8
         */
        DEFAULT = 0,
        /**
         * Asynchronous call flag.
         *
         * When this flag is set, both synchronous and asynchronous calls are traced. By default, only synchronous calls are
         * traced.
         *
         * @syscap SystemCapability.HiviewDFX.HiTrace
         * @since 8
         */
        INCLUDE_ASYNC = 1,
        /**
         * No span flag.
         *
         * When this flag is set, no span information is created. By default, span information is created.
         *
         * @syscap SystemCapability.HiviewDFX.HiTrace
         * @since 8
         */
        DONOT_CREATE_SPAN = 1 << 1,
        /**
         * Trace point flag.
         *
         * When this flag is set in the debugging scenario, the HiLog logs of the trace point are printed upon calling the
         * **[tracepoint()]{@link hiTraceChain.tracepoint}** API. By default, the HiLog logs are not printed.
         *
         * @syscap SystemCapability.HiviewDFX.HiTrace
         * @since 8
         */
        TP_INFO = 1 << 2,
        /**
         * No begin and end flag.
         *
         * When this flag is set in the debugging scenario, the HiLog logs about the begin and end of tracing are printed
         * when the [begin()]{@link hiTraceChain.begin} and [end()]{@link hiTraceChain.end} APIs are called. By default, the
         * HiLog logs about the begin and end of tracing are not printed.
         *
         * @syscap SystemCapability.HiviewDFX.HiTrace
         * @since 8
         */
        NO_BE_INFO = 1 << 3,
        /**
         * Log association flag.
         *
         * When this flag is set, the **HiTraceId** information is not added to the HiLog logs. By default, the
         * **HiTraceId** information is added to the HiLog logs.
         *
         * @syscap SystemCapability.HiviewDFX.HiTrace
         * @since 8
         */
        DISABLE_LOG = 1 << 4,
        /**
         * Failure trigger flag. This is a reserved flag.
         *
         * @syscap SystemCapability.HiviewDFX.HiTrace
         * @since 8
         */
        FAILURE_TRIGGER = 1 << 5,
        /**
         * Device-to-device trace point flag. It is a subset of **TP_INFO** and is used in debugging scenarios.
         *
         * When the **TP_INFO** flag is set, the **D2D_TP_INFO** flag does not take effect.
         *
         * When **TP_INFO** is not set and **D2D_TP_INFO** is set, the HiLog logs of the trace point are printed only when
         * the mode parameter is set to **DEVICE** upon calling [tracepoint()]{@link hiTraceChain.tracepoint}.
         *
         * @syscap SystemCapability.HiviewDFX.HiTrace
         * @since 8
         */
        D2D_TP_INFO = 1 << 6
    }
    /**
     * Enumerates trace point types.
     *
     * @syscap SystemCapability.HiviewDFX.HiTrace
     * @since 8
     */
    enum HiTraceTracepointType {
        /**
         * CS trace point.
         *
         * @syscap SystemCapability.HiviewDFX.HiTrace
         * @since 8
         */
        CS = 0,
        /**
         * CR trace point.
         *
         * @syscap SystemCapability.HiviewDFX.HiTrace
         * @since 8
         */
        CR = 1,
        /**
         * SS trace point.
         *
         * @syscap SystemCapability.HiviewDFX.HiTrace
         * @since 8
         */
        SS = 2,
        /**
         * SR trace point.
         *
         * @syscap SystemCapability.HiviewDFX.HiTrace
         * @since 8
         */
        SR = 3,
        /**
         * General type, which identifies the trace points except the CS, CR, SS, and SR trace points.
         *
         * @syscap SystemCapability.HiviewDFX.HiTrace
         * @since 8
         */
        GENERAL = 4
    }
    /**
     * Enumerates communication modes.
     *
     * @syscap SystemCapability.HiviewDFX.HiTrace
     * @since 8
     */
    enum HiTraceCommunicationMode {
        /**
         * Default communication.
         *
         * @syscap SystemCapability.HiviewDFX.HiTrace
         * @since 8
         */
        DEFAULT = 0,
        /**
         * Inter-thread communication.
         *
         * @syscap SystemCapability.HiviewDFX.HiTrace
         * @since 8
         */
        THREAD = 1,
        /**
         * Inter-process communication.
         *
         * @syscap SystemCapability.HiviewDFX.HiTrace
         * @since 8
         */
        PROCESS = 2,
        /**
         * Inter-device communication.
         *
         * @syscap SystemCapability.HiviewDFX.HiTrace
         * @since 8
         */
        DEVICE = 3
    }
    /**
     * Defines a **HiTraceId** object.
     *
     * @syscap SystemCapability.HiviewDFX.HiTrace
     * @since 8
     */
    interface HiTraceId {
        /**
         * Call chain ID.
         *
         * @syscap SystemCapability.HiviewDFX.HiTrace
         * @since 8
         */
        chainId: bigint;
        /**
         * Span ID. The default value is **0**.
         *
         * @syscap SystemCapability.HiviewDFX.HiTrace
         * @since 8
         */
        spanId?: number;
        /**
         * Parent span ID. The default value is **0**.
         *
         * @syscap SystemCapability.HiviewDFX.HiTrace
         * @since 8
         */
        parentSpanId?: number;
        /**
         * Trace flag. The default value is **0**.
         *
         * @syscap SystemCapability.HiviewDFX.HiTrace
         * @since 8
         */
        flags?: number;
    }
    /**
     * Starts call chain trace. This API returns the result synchronously.
     *
     * If the current thread's TLS does not contain a valid HiTrace ID, this function generates one, stores it in TLS, and
     * returns it.
     *
     * If the current thread's TLS already contains a valid HiTrace ID, this function does not start tracing and returns
     * an invalid HiTrace ID with all property values being 0.
     *
     * @param { string } name - Traced service name.<br>It is recommended that the length of this parameter be less than
     *     or equal to 63 bytes. The excess part will be truncated.
     * @param { number } flags - Trace flag combination. For details, see [HiTraceFlag]{@link hiTraceChain.HiTraceFlag}. The
     *     default value is **0**.
     * @returns { HiTraceId } **HiTraceId** instance.
     * @syscap SystemCapability.HiviewDFX.HiTrace
     * @since 8
     */
    function begin(name: string, flags?: number): HiTraceId;
    /**
     * Stops call chain trace. This API works in synchronous manner.
     *
     * If the given HiTrace ID is valid and is the same as the HiTrace ID in the current thread's TLS, the tracing is
     * stopped and the HiTrace ID in the current thread's TLS is set to invalid.
     *
     * If the given HiTrace ID is invalid or is not the same as the HiTrace ID in the current thread's TLS, the tracing
     * fails to be stopped, and a tracing stop failure log is printed.
     *
     * @param { HiTraceId } id - **HiTraceId** instance.
     * @syscap SystemCapability.HiviewDFX.HiTrace
     * @since 8
     */
    function end(id: HiTraceId): void;
    /**
     * Obtains the trace ID. This API returns the result synchronously.
     *
     * Obtains the HiTrace ID in the TLS of the current thread.
     *
     * @returns { HiTraceId } **HiTraceId** instance.
     * @syscap SystemCapability.HiviewDFX.HiTrace
     * @since 8
     */
    function getId(): HiTraceId;
    /**
     * Sets a trace ID. This API returns the result synchronously.
     *
     * Sets the given HiTrace ID to the TLS of the current thread. If the given HiTrace ID is invalid, no operation is
     * performed.
     *
     * @param { HiTraceId } id - **HiTraceId** instance.
     * @syscap SystemCapability.HiviewDFX.HiTrace
     * @since 8
     */
    function setId(id: HiTraceId): void;
    /**
     * Clears the trace ID. This API returns the result synchronously.
     *
     * Clears the HiTrace ID in the current thread's TLS.
     *
     * @syscap SystemCapability.HiviewDFX.HiTrace
     * @since 8
     */
    function clearId(): void;
    /**
     * Creates a trace span. This API works in synchronous manner.
     *
     * Specifically, create a **HiTraceId**, use the **chainId** and **spanId** in the TLS of the current thread to
     * initialize the **chainId** and **parentSpanId** of the **HiTraceId**, generate a new **spanId** for the
     * **HiTraceId**, and return the **HiTraceId**.
     *
     * @returns { HiTraceId } **HiTraceId** instance.
     * @syscap SystemCapability.HiviewDFX.HiTrace
     * @since 8
     */
    function createSpan(): HiTraceId;
    /**
     * Adds a trace point for the [@ohos.hiTraceMeter (Performance Tracing)]{@link @ohos.hiTraceMeter:hiTraceMeter}
     * logging, which is synchronous.
     *
     * When type is set to **CS** and **SR**, the HiTraceMeter tracing starts. When type is set to **CR** and **SS**, the
     * HiTraceMeter tracing ends. When type is set to **GENERAL**, the HiTraceMeter tracing does not start.
     *
     * The trace points for **CS** and **CR** types must be used as a pair; likewise, trace points for **SR** and **SS**
     * types must also be used together. Otherwise, the start and end trace points of HiTraceMeter cannot match each
     * other.
     *
     * @param { HiTraceCommunicationMode } mode - Communication mode for the trace point.
     * @param { HiTraceTracepointType } type - Trace point type.
     * @param { HiTraceId } id - **HiTraceId** instance for trace point triggering.
     * @param { string } msg - Trace description information passed by the HiTraceMeter logging. The default value is "".
     * @syscap SystemCapability.HiviewDFX.HiTrace
     * @since 8
     */
    function tracepoint(mode: HiTraceCommunicationMode, type: HiTraceTracepointType, id: HiTraceId, msg?: string): void;
    /**
     * Checks whether a **HiTraceId** instance is valid. This API returns the result synchronously.
     *
     * @param { HiTraceId } id - **HiTraceId** instance.
     * @returns { boolean } The value **true** indicates that **HiTraceId** is valid, and **false** indicates the
     *     opposite.
     * @syscap SystemCapability.HiviewDFX.HiTrace
     * @since 8
     */
    function isValid(id: HiTraceId): boolean;
    /**
     * Checks whether the trace flag is enabled for **HiTraceId**. This API returns the result synchronously.
     *
     * @param { HiTraceId } id - **HiTraceId** instance to be checked.
     * @param { HiTraceFlag } flag - Specified trace flag.
     * @returns { boolean } The value **true** indicates that the flag for **HiTraceId** is enabled, and **false**
     *     indicates the opposite.
     * @syscap SystemCapability.HiviewDFX.HiTrace
     * @since 8
     */
    function isFlagEnabled(id: HiTraceId, flag: HiTraceFlag): boolean;
    /**
     * Enables the trace flag specified in HiTraceId. This API returns the result synchronously.
     *
     * @param { HiTraceId } id - **HiTraceId** instance for which the trace flag is enabled.
     * @param { HiTraceFlag } flag - Specified trace flag.
     * @syscap SystemCapability.HiviewDFX.HiTrace
     * @since 8
     */
    function enableFlag(id: HiTraceId, flag: HiTraceFlag): void;
}
export default hiTraceChain;

```
