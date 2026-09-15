# @ohos.test.PerfTest.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2025 Huawei Device Co., Ltd.
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
 * PerfTest provides white-box performance testing capabilities.
 * It can test performance data of specified code segments or scenarios, automatically execute test code segments,
 * and collect performance data such as time consumption, CPU, memory, latency, and frame rate.
 *
 * > **NOTE**
 * > - The initial APIs of this module are supported since API version 20.
 *     Newly added APIs will be marked with a superscript to indicate their earliest API version.
 * > - The APIs of this module can be used only in <!--RP1-->[JsUnit](../../application-test/unittest-guidelines.md)<!--RP1End-->.
 * > - The APIs of this module do not support concurrent calls.
 * > - The APIs of this module are applicable to phones, tablets, PCs/2-in-1 devices, smart TVs, and head units.
 *
 * @file
 * @kit TestKit
 *
 */
import { Callback } from './@ohos.base';
/**
 * Represents performance metrics that can be collected by the framework.
 *
 * > **NOTE**
 * >
 * > 1. The preceding metrics collect performance data for a specified application process, not for the system.
 * > 2. Description of collecting the CPU data (**CPU_LOAD** / **CPU_USAGE**) and memory (**MEMORY_RSS** / **MEMORY_PSS**):
 * > - During the test, the CPU and memory data of the specified application process is collected before and after the
 * >   code segment execution. Therefore, ensure that the application process to be tested exists during the test.
 * > 3. Description of collecting the application startup latency data (**APP_START_RESPONSE_TIME** / **APP_START_COMPLETE_TIME**):
 * > - Application startup latency data is affected by system log reporting. The start time is when the tap event is reported,
 * >   the end time of the response latency is when the first frame is displayed on the screen after the tap,
 * >   and the end time of the completion latency is when the first frame is displayed on the screen after the application is started.
 * >   The latency is different from what users perceive.
 * > - Application startup latency data can be collected in the following scenarios: tapping an application icon on the home screen,
 * >   tapping an application icon on the dock bar, and tapping an application icon in the application center.
 * > - During a test, only the first startup latency of the specified application is collected.
 * > 4. Description of collecting the page switching latency data (**PAGE_SWITCH_COMPLETE_TIME**):
 * > - The page switching latency calculation is affected by the system log reporting. The start time is when the tap event is reported,
 * >   and the end time is when the first frame is displayed on the screen after the page switching,
 * >   which is different from what users perceive.
 * > - Page switching latency data can be collected in the **Router** and **Navigation** components.
 * > - During a test, only the first page switching latency in the specified application is collected.
 * > 5. Description of collecting the list scrolling frame rate (**LIST_SWIPE_FPS**):
 * > - **LIST_SWIPE_FPS**: The number of frames rendered and updated on the screen per second when the list is scrolled.
 * > - Supported scenarios: list scrolling of the **List**, **Grid**, **Scroll**, and **WaterFlow** components in the ArkUI subsystem.
 * > - During a test, only the first list scrolling frame rate in the specified application is collected.
 *
 * @enum { number }
 * @syscap SystemCapability.Test.PerfTest
 * @atomicservice
 * @since 20
 * @test
 */
declare enum PerfMetric {
    /**
     * Execution duration of a code segment, in milliseconds.
     *
     * @syscap SystemCapability.Test.PerfTest
     * @atomicservice
     * @since 20
     * @test
     */
    DURATION = 0,
    /**
     * CPU load of the application process, in percentage.
     *
     * @syscap SystemCapability.Test.PerfTest
     * @atomicservice
     * @since 20
     * @test
     */
    CPU_LOAD = 1,
    /**
     * CPU usage of the application process, in percentage.
     *
     * @syscap SystemCapability.Test.PerfTest
     * @atomicservice
     * @since 20
     * @test
     */
    CPU_USAGE = 2,
    /**
     * Physical memory (including the shared library) occupied by the application process when a code segment is executed, in KB.
     *
     * @syscap SystemCapability.Test.PerfTest
     * @atomicservice
     * @since 20
     * @test
     */
    MEMORY_RSS = 3,
    /**
     * Physical memory (excluding the shared library) occupied by the application process when a code segment is executed, in KB.
     *
     * @syscap SystemCapability.Test.PerfTest
     * @atomicservice
     * @since 20
     * @test
     */
    MEMORY_PSS = 4,
    /**
     * Response latency of application startup, in milliseconds.
     *
     * Marks:
     * 1) Delay calculation is restricted by system dotting reporting. The start time is the time when the click event is reported,
     * and the end time of the response delay is the time when the system responds to the first frame after the click.
     * It is different from the end-to-end user-perceived delay.
     * 2) Application start delay can be collected in the following scenarios: clicking the application icon on the desktop;
     * clicking the application on the Multi-Task Center; clicking the application icon on the Dock;
     * clicking the application icon on the application center.
     * 3) This metric does not support the test of current application.
     * 4) During the test, only the data of the first startup of the specified application can be collected.
     *
     * @syscap SystemCapability.Test.PerfTest
     * @atomicservice
     * @since 20
     * @test
     */
    APP_START_RESPONSE_TIME = 5,
    /**
     * Completion latency of application startup, in milliseconds.
     *
     * Marks:
     * 1) Delay calculation is restricted by system dotting reporting. The start time is the time when the click event is reported,
     * and the end time of the completion delay is the time when the first frame is displayed after the application is started.
     * It is different from the end-to-end user-perceived delay.
     * 2) Application start delay can be collected in the following scenarios: clicking the application icon on the desktop;
     * clicking the application on the Multi-Task Center; clicking the application icon on the Dock;
     * clicking the application icon on the application center.
     * 3) This metric does not support the test of current application.
     * 4) During the test, only the data of the first start of specified application can be collected.
     *
     * @syscap SystemCapability.Test.PerfTest
     * @atomicservice
     * @since 20
     * @test
     */
    APP_START_COMPLETE_TIME = 6,
    /**
     * Completion latency of page switching in an application, in milliseconds.
     *
     * Marks:
     * 1) Delay calculation is restricted by system dotting and reporting. The start time is the time when the click event is reported,
     * and the end time of the completion delay is the time when the first frame is displayed after page is switched.
     * It is different from the end-to-end user-perceived delay.
     * 2) Page switching delay can be collected in the page switchover scenario of the Router or Navigation component.
     * 3) During the test, only the data of the first page switching in specified application can be collected.
     *
     * @syscap SystemCapability.Test.PerfTest
     * @atomicservice
     * @since 20
     * @test
     */
    PAGE_SWITCH_COMPLETE_TIME = 7,
    /**
     * List scrolling frame rate in an application, in frames per second (fps).
     *
     * Mark:
     * 1) List sliding frame rate: refers to the frequency at which the screen can be refreshed when the list is sliding.
     * Only the sliding frame rate of the List, grid, scroll, and waterflow scroll components of ArkUI subsystems can be collected.
     * 2) During the test, only the data of the first sliding of the component in specified application can be collected.
     *
     * @syscap SystemCapability.Test.PerfTest
     * @atomicservice
     * @since 20
     * @test
     */
    LIST_SWIPE_FPS = 8
}
/**
 * Represents the performance test strategy.
 *
 * > **NOTE**
 * >
 * > The input parameter type of the **actionCode** and **resetCode** attributes is the **Callback\<boolean>**.
 *   You need to call this callback in the code segment to notify the framework that the code segment execution is complete.
 *   Otherwise, the code segment execution times out.
 * > The callback parameter is of the **Boolean** type.
 *   The value **true** indicates that the code segment execution meets the expectation, and false indicates the opposite.
 *
 * @syscap SystemCapability.Test.PerfTest
 * @atomicservice
 * @since 20
 * @test
 */
declare interface PerfTestStrategy {
    /**
     * List of performance metrics to be collected.
     *
     * @syscap SystemCapability.Test.PerfTest
     * @atomicservice
     * @since 20
     * @test
     */
    metrics: Array<PerfMetric>;
    /**
     * Code segment for performance testing.
     * The input parameter type of actionCode is {@link Callback<boolean>}. As actionCode can be defined as asynchronous function,
     * developers need to invoke this callback function when the execution of actionCode is complete,
     * to help PerfTest identify the time when the execution of the actionCode is complete.
     * For example, the input parameter callback function of actionCode is defined as "(finish: Callback<boolean>)".
     * When actionCode is executed completely, "finish(true)" should be invoked, the value true indicates actionCode is successfully executed.
     * When an exception occurs, "finish(false)" should be invoked, the value false indicates actionCode is unsuccessfully executed.
     *
     * @syscap SystemCapability.Test.PerfTest
     * @atomicservice
     * @since 20
     * @test
     */
    actionCode: Callback<Callback<boolean>>;
    /**
     * Code segment for resetting the environment after the {@link actionCode}. is complete. The default value is empty.
     * Data collection is not performed during this execution.
     * The input parameter type of resetCode is {@link Callback<boolean>}. As resetCode can be defined as asynchronous function,
     * developers need to invoke this callback function when the execution of resetCode is complete,
     * to help PerfTest identify the time when the execution of the resetCode is complete.
     * For example, the input parameter callback function of resetCode is defined as "(finish: Callback<boolean>)".
     * When resetCode is executed completely, "finish(true)" should be invoked, the value true indicates resetCode is successfully executed.
     * When an exception occurs, "finish(false)" should be invoked, the value false indicates resetCode is unsuccessfully executed.
     *
     * @syscap SystemCapability.Test.PerfTest
     * @atomicservice
     * @since 20
     * @test
     */
    resetCode?: Callback<Callback<boolean>>;
    /**
     * Bundle name of the application to test.
     * The default value is "". The framework tests the performance data of the current application.
     *
     * @syscap SystemCapability.Test.PerfTest
     * @atomicservice
     * @since 20
     * @test
     */
    bundleName?: string;
    /**
     * Number of test iterations. The default value is 5.
     *
     * @syscap SystemCapability.Test.PerfTest
     * @atomicservice
     * @since 20
     * @test
     */
    iterations?: number;
    /**
     * Timeout interval for executing a code segment ({@link actionCode} or {@link resetCode}) at a time.
     * The default value is 10,000 ms.
     *
     * @syscap SystemCapability.Test.PerfTest
     * @atomicservice
     * @since 20
     * @test
     */
    timeout?: number;
}
/**
 * Represents the measurement result data corresponding to the performance metric.
 *
 * @syscap SystemCapability.Test.PerfTest
 * @atomicservice
 * @since 20
 * @test
 */
declare interface PerfMeasureResult {
    /**
     * Performance metric to test.
     *
     * @syscap SystemCapability.Test.PerfTest
     * @atomicservice
     * @since 20
     * @test
     */
    readonly metric: PerfMetric;
    /**
     * Measurement data value of each round of the tested performance metric. If data collection fails, the value **-1** is returned.
     *
     * @syscap SystemCapability.Test.PerfTest
     * @atomicservice
     * @since 20
     * @test
     */
    readonly roundValues: Array<number>;
    /**
     * Maximum value of the measurement data of each round (the value **-1** is excluded).
     *
     * @syscap SystemCapability.Test.PerfTest
     * @atomicservice
     * @since 20
     * @test
     */
    readonly maximum: number;
    /**
     * Minimum value of the measurement data of each round (the value **-1** is excluded).
     *
     * @syscap SystemCapability.Test.PerfTest
     * @atomicservice
     * @since 20
     * @test
     */
    readonly minimum: number;
    /**
     * Average value of the measurement data of each round (the value **-1** is excluded).
     *
     * @syscap SystemCapability.Test.PerfTest
     * @atomicservice
     * @since 20
     * @test
     */
    readonly average: number;
}
/**
 * Represents the general entry of the white-box performance test framework.
 * It provides capabilities such as test task creation, test code segment execution, data collection, and measurement result obtaining.
 *
 * @syscap SystemCapability.Test.PerfTest
 * @atomicservice
 * @since 20
 * @test
 */
declare class PerfTest {
    /**
     * Creates a {@link PerfTest} object and returns the object created. This API is a static API.
     *
     * @param { PerfTestStrategy } strategy - Performance test strategy.
     * @returns { PerfTest }  {@link PerfTest} object created.
     * @throws { BusinessError } 32400001 - Initialization failed.
     * @throws { BusinessError } 32400002 - Internal error. Possible causes: 1. IPC connection failed. 2. The object does not exist.
     * @throws { BusinessError } 32400003 - Parameter verification failed.
     * @throws { BusinessError } 32400007 - The API does not support concurrent calls.
     * @static
     * @syscap SystemCapability.Test.PerfTest
     * @atomicservice
     * @since 20
     * @test
     */
    static create(strategy: PerfTestStrategy): PerfTest;
    /**
     * Runs a performance test, iteratively executes test code segments, and collects performance data.
     * This API uses a promise to return the result.
     *
     * @returns { Promise<void> }
     * @throws { BusinessError } 32400002 - Internal error. Possible causes: 1. IPC connection failed. 2. The object does not exist.
     * @throws { BusinessError } 32400004 - Failed to execute the callback. Possible causes: 1. An exception is thrown in the callback. 2. Callback execution timed out.
     * @throws { BusinessError } 32400005 - Failed to collect metric data.
     * @throws { BusinessError } 32400007 - The API does not support concurrent calls.
     *
     * @syscap SystemCapability.Test.PerfTest
     * @atomicservice
     * @since 20
     * @test
     */
    run(): Promise<void>;
    /**
     * Obtains the measurement data of a specified performance metric.
     *
     * @param { PerfMetric } metric - Performance metric.
     * @returns { PerfMeasureResult } - Measurement result data corresponding to the performance metric.
     * @throws { BusinessError } 32400002 - Internal error. Possible causes: 1. IPC connection failed. 2. The object does not exist.
     * @throws { BusinessError } 32400003 - Parameter verification failed.
     * @throws { BusinessError } 32400006 - Failed to obtain the measurement result.
     * @throws { BusinessError } 32400007 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.PerfTest
     * @atomicservice
     * @since 20
     * @test
     */
    getMeasureResult(metric: PerfMetric): PerfMeasureResult;
    /**
     * Destroys the {@link PerfTest} object.
     * @throws { BusinessError } 32400002 - Internal error. Possible causes: 1. IPC connection failed. 2. The object does not exist.
     * @throws { BusinessError } 32400007 - The API does not support concurrent calls.
     * @syscap SystemCapability.Test.PerfTest
     * @atomicservice
     * @since 20
     * @test
     */
    destroy(): void;
}
export { PerfMetric, PerfTestStrategy, PerfMeasureResult, PerfTest };

```
