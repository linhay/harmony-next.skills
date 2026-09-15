# @ohos.hiviewdfx.jsLeakWatcher.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2024 Huawei Device Co., Ltd.
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
 * This module provides the capability of monitoring whether JS objects are leaked.
 *
 * @syscap SystemCapability.HiviewDFX.HiChecker
 * @since 12
 */
declare namespace jsLeakWatcher {
    /**
     * Enables the detection for JS object leaks. This function is disabled by default.
     *
     * @param { boolean } isEnable - Whether to enable **jsLeakWatcher**. **true**: yes; **false**: no.
     * @syscap SystemCapability.HiviewDFX.HiChecker
     * @since 12
     */
    function enable(isEnable: boolean): void;
    /**
     * Registers the object to be checked.
     *
     * @param { object } obj - Name of the object to be checked.<br>Note: You can pass objects of any type.
     * @param { string } msg - Custom object information.
     * @syscap SystemCapability.HiviewDFX.HiChecker
     * @since 12
     */
    function watch(obj: object, msg: string): void;
    /**
     * Obtains the list of objects that are leaked and registered using **jsLeakWatcher.watch()**. Objects that are not
     * reclaimed after GC is triggered are marked as leaked.
     *
     * @returns { string } List of leaked objects that are not reclaimed after GC is triggered.
     *     <br>Note: If this API is successful, a list of leaked objects in JSON format is returned.
     *     Otherwise, an empty string is returned.
     * @syscap SystemCapability.HiviewDFX.HiChecker
     * @since 12
     */
    function check(): string;
    /**
     * Dumps the list of leaked objects and VM memory snapshot.
     *
     * @param { string } filePath - Path for storing exported information files.
     * @returns { Array<string> } Export result. The file name extension is **.jsleaklist** for the list of leaked objects
     *     and **.heapsnapshot** for the VM memory snapshot.
     *     <br>Note: If the dump is successful, the path of the leaked object list file and the VM memory snapshot path are
     *     returned. Otherwise, an empty array is returned.
     * @syscap SystemCapability.HiviewDFX.HiChecker
     * @since 12
     */
    function dump(filePath: string): Array<string>;
    /**
     * Enables the detection for JS object leaks. This function is disabled by default.
     *
     * This API can detect the JS object memory leak, which is simpler than the method that needs to call the **enable**,
     * **watch**, **check**, and **dump** functions.
     *
     * If a memory leak occurs, the leaked file is returned through the callback.
     *
     * @param { boolean } isEnabled - Whether to enable the detection for JS object memory leaks. **true**: yes; **false**
     *     : no.
     * @param { Array<string> } configs - Configuration item. Each element in the array indicates a specific object type
     *     to monitor.<br>Options: **XComponent**, **NodeContainer**, **Window**, **CustomComponent**, and **Ability**.<br
     *     >Note: An empty array indicates that all the preceding objects are monitored.
     * @param { Callback<Array<string>> } callback - Callback used to receive the memory-leaked object returned by the
     *     **jsLeakWatcher.enableLeakWatcher** API.<br>You need to input an array object in the callback. Index **0** is
     *     the name of the leak list file, whose extension is **.jsleaklist**. Index **1** is the name of the VM memory
     *     snapshot file, whose extension is **.rawheap**.
     * @throws { BusinessError } 10801001 - The parameter isEnabled is invalid.
     * @throws { BusinessError } 10801002 - The parameter config is invalid.
     * @throws { BusinessError } 10801003 - The parameter callback is invalid.
     *     Input parameter error. Possible causes:
     *     1.Mandatory parameters are left unspecified;
     *     2.Incorrect parameter types;
     *     3.Parameter verification failed.
     * @syscap SystemCapability.HiviewDFX.HiChecker
     * @since 20
     */
    function enableLeakWatcher(isEnabled: boolean, configs: Array<string>, callback: Callback<Array<string>>): void;
    /**
     * Enumerates the types of component objects to be monitored.
     *
     * @syscap SystemCapability.HiviewDFX.HiChecker
     * @FaAndStageModel
     * @since 24
     */
    export declare enum MonitorObjectType {
        /**
         * All component types are monitored.
         *
         * @syscap SystemCapability.HiviewDFX.HiChecker
         * @FaAndStageModel
         * @since 24
         */
        ALL = -1,
        /**
         * Custom component types are monitored.
         *
         * @syscap SystemCapability.HiviewDFX.HiChecker
         * @FaAndStageModel
         * @since 24
         */
        CUSTOM_COMPONENT = 1 << 0,
        /**
         * The **Window** component type is monitored.
         *
         * @syscap SystemCapability.HiviewDFX.HiChecker
         * @FaAndStageModel
         * @since 24
         */
        WINDOW = 1 << 1,
        /**
         * The **NodeContainer** component type is monitored.
         *
         * @syscap SystemCapability.HiviewDFX.HiChecker
         * @FaAndStageModel
         * @since 24
         */
        NODE_CONTAINER = 1 << 2,
        /**
         * The **XComponent** component type is monitored.
         *
         * @syscap SystemCapability.HiviewDFX.HiChecker
         * @FaAndStageModel
         * @since 24
         */
        X_COMPONENT = 1 << 3,
        /**
         * The **Ability** component type is monitored.
         *
         * @syscap SystemCapability.HiviewDFX.HiChecker
         * @FaAndStageModel
         * @since 24
         */
        ABILITY = 1 << 4
    }
    /**
     * Defines the **LeakWatcherConfig** object, which contains multiple configurable properties for memory leak
     * monitoring.
     *
     * @syscap SystemCapability.HiviewDFX.HiChecker
     * @FaAndStageModel
     * @since 24
     */
    interface LeakWatcherConfig {
        /**
         * Type of the monitored object.
         *
         * By default, all component types are monitored.
         *
         * @syscap SystemCapability.HiviewDFX.HiChecker
         * @FaAndStageModel
         * @since 24
         */
        monitorObjectTypes: MonitorObjectType;
        /**
         * List of IDs of monitored objects.
         *
         * This parameter applies only to custom components and does not affect the monitoring of other component types.
         *
         * For example, if the object class name ID set in the trustlist is the same as that in the custom ID list, the
         * custom ID list takes effect.
         *
         * The default value is an empty array.
         *
         * @syscap SystemCapability.HiviewDFX.HiChecker
         * @FaAndStageModel
         * @since 24
         */
        objectUniqueIDs?: Array<number>;
        /**
         * Interval between each round of leak detection, in milliseconds.
         *
         * The default value is 30 seconds.
         *
         * @syscap SystemCapability.HiviewDFX.HiChecker
         * @FaAndStageModel
         * @since 24
         */
        checkInterval?: number;
        /**
         * Threshold for the number of leaked objects in a foreground application. Dump is triggered when this threshold is
         * reached.
         *
         * During the GC/Dump phase, dump is triggered when the value is greater than or equal to 5.
         *
         * The default threshold is **5**.
         *
         * @syscap SystemCapability.HiviewDFX.HiChecker
         * @FaAndStageModel
         * @since 24
         */
        fgLeakCountThreshold?: number;
        /**
         * Threshold for the number of leak objects in a background application. Dump is triggered when this threshold is
         * reached.
         *
         * During the GC/Dump phase, dump is triggered when the value is greater than or equal to 1.
         *
         * The default threshold is **1**.
         *
         * @syscap SystemCapability.HiviewDFX.HiChecker
         * @FaAndStageModel
         * @since 24
         */
        bgLeakCountThreshold?: number;
        /**
         * Maximum number of dump files that can be saved. To prevent the disk space from being used up, the .rawheap and
         * .jsleaklist files with the minimum timestamp are deleted when the number of dump files exceeds the maximum.
         *
         * By default, 10 .rawheap files and 10 .jsleaklist files are saved.
         *
         * @syscap SystemCapability.HiviewDFX.HiChecker
         * @FaAndStageModel
         * @since 24
         */
        maxStoredHeapDumps?: number;
        /**
         * Delay interval for executing dump. This parameter ensures that GC can be scheduled and executed before dump. The
         * delay interval is less than or equal to the leak detection interval, in milliseconds.
         *
         * If the configured delay exceeds the leak detection interval, the delay defaults to that of the leak detection
         * interval.
         *
         * If no new leaked object exists, dump will not be triggered.
         *
         * By default, the dump is performed 5 seconds after the GC ends.
         *
         * @syscap SystemCapability.HiviewDFX.HiChecker
         * @FaAndStageModel
         * @since 24
         */
        dumpHeapWaitTimeMs?: number;
        /**
         * Class name of the object to be excluded from monitoring.
         *
         * This parameter applies only to custom components and does not affect the filtering of other component types.
         *
         * If obfuscation occurs, filtering cannot be performed. This parameter takes effect only in the development state.
         *
         * Configuration item conflict priority: ID list > trustlist.
         *
         * The default value is an empty array.
         *
         * @syscap SystemCapability.HiviewDFX.HiChecker
         * @FaAndStageModel
         * @since 24
         */
        exclusionList?: Array<string>;
    }
    /**
     * Enables the ArkTS object leak detection.
     *
     * This API can detect memory leaks of ArkTS objects with a single call, which is simpler than the previous method
     * that requires four functions (**enable**, **watch**, **check**, and **dump**). You can use the **configs**
     * parameter to customize the properties of monitoring items, greatly improving the leak detection performance.
     *
     * @param { boolean } isEnabled - Whether to enable the detection for ArkTS object memory leaks.<br>**true**: yes;<br>
     *     **false**: no.
     * @param { LeakWatcherConfig } configs - LeakWatcherConfig object, which contains multiple configurable properties
     *     for memory leak monitoring.<br>Note: If the parameter type in the object is set to null or a false value, the
     *     default value is used.
     * @param { Callback<Array<string>> } callback - Callback used to receive the memory-leaked object returned by the
     *     **jsLeakWatcher.enableLeakWatcher** API.<br>You need to input an array object in the callback. Index **0** is
     *     the name of the leak list file, whose extension is **.jsleaklist**. Index **1** is the name of the VM memory
     *     snapshot file, whose extension is **.rawheap**.
     * @throws { BusinessError } 10801001 - The parameter isEnabled is invalid.
     * @throws { BusinessError } 10801002 - The parameter config is invalid.
     * @throws { BusinessError } 10801003 - The parameter callback is invalid.
     *     Input parameter error. Possible causes:
     *     1.Mandatory parameters are left unspecified;
     *     2.Incorrect parameter types;
     *     3.Parameter verification failed.
     * @syscap SystemCapability.HiviewDFX.HiChecker
     * @FaAndStageModel
     * @since 24
     */
    function enableLeakWatcher(isEnabled: boolean, configs: LeakWatcherConfig, callback: Callback<Array<string>>): void;
}
export default jsLeakWatcher;

```
