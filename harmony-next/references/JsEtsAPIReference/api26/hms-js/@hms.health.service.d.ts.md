# @hms.health.service.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) Huawei Technologies Co., Ltd. 2026-2026. All rights reserved.
 */
/**
 * @file Defines the capabilities of HealthServiceKit.
 * @kit HealthServiceKit
 */
import type healthStore from './@hms.health.store';
import { Callback } from '@ohos.base';
/**
 * Mini Health Service Kit API for lite wearables.
 *
 * @syscap SystemCapability.Health.HealthService.Lite
 * @famodelonly
 * @since 6.1.1(24)
 */
declare namespace healthService {
    /**
     * Real-time sampling data structure, which is usually used for sensor data.
     *
     * @syscap SystemCapability.Health.HealthService.Lite
     * @famodelonly
     * @since 6.1.1(24)
     */
    interface SampleReal<K extends Record<string, healthStore.HealthValueType> = Record<string, healthStore.HealthValueType>> {
        /**
         * Data type.
         *
         * @syscap SystemCapability.Health.HealthService.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        dataType: healthStore.DataType;
        /**
         * Unix timestamp.
         *
         * @syscap SystemCapability.Health.HealthService.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        time: number;
        /**
         * Data fields.
         *
         * @syscap SystemCapability.Health.HealthService.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        fields: Pick<K, keyof K>;
        /**
         * Device ID.
         *
         * @syscap SystemCapability.Health.HealthService.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        deviceUniqueId?: string;
    }
    /**
     * Namespace for daily activity data and api.
     *
     * @syscap SystemCapability.Health.HealthService.Lite
     * @famodelonly
     * @since 6.1.1(24)
     */
    namespace workout {
        /**
         * Mini Health Service Kit API for lite wearables.
         *
         * @syscap SystemCapability.Health.HealthService.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        type ConfigType = number | string | boolean;
        /**
         * Mini Health Service Kit API for lite wearables.
         *
         * @syscap SystemCapability.Health.HealthService.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        interface WorkoutConfig {
            /**
             * Workout linkage type, for example, course link and activity link.
             *
             * @syscap SystemCapability.Health.HealthService.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            linkageType: LinkageType;
            /**
             * Sport-type workout.
             *
             * @syscap SystemCapability.Health.HealthService.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            sportType: number;
            /**
             * Workout goal.
             *
             * @syscap SystemCapability.Health.HealthService.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            activityGoals?: Goal[];
            /**
             * Extended workout configuration.
             *
             * @syscap SystemCapability.Health.HealthService.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            extensionConfig?: Record<string, ConfigType>;
        }
        /**
         * Workout goal.
         *
         * @syscap SystemCapability.Health.HealthService.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        interface Goal {
            /**
             * Target type.
             *
             * @syscap SystemCapability.Health.HealthService.Lite
             * @famodelonly
             * @since 6.1.1(24)
             * @see { TargetType }
             */
            type: number;
            /**
             * Target value.
             *
             * @syscap SystemCapability.Health.HealthService.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            value: number;
        }
        /**
         * Algorithm dynamic library loading
         *
         * @param { string } path - Algorithm dynamic library path.
         * @throws { BusinessError } 201  - Permission verification failed. Please ensure that the app has
         *     applied for the Health Service Kit, selected the product type, enabled the corresponding data
         *     read and write permissions, and the user has completed authorization.
         * @throws { BusinessError } 1009104001 - Sport service busy. Workout is already started by other application.
         * @throws { BusinessError } 1009104003 - Illegal command. Called when workout is not started.
         * @throws { BusinessError } 1009104004 - Permission verification error.
         *     Application has no permission, such as Motion Permission.
         * @throws { BusinessError } 1009104005 - Failed to load the dynamic library.
         * @throws { BusinessError } 1009104999 - System internal error.
         * @syscap SystemCapability.Health.HealthService.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        function load(path: string): void;
        /**
         * Algorithm dynamic library loading (asynchronous version)
         *
         * @param { string } path - Algorithm dynamic library path.
         * @param { Callback<DynamicLibResult> } callback - Callback function to receive result code.
         * @throws { BusinessError } 201 - Permission verification failed. Please ensure that the app has
         *     applied for the Health Service Kit, selected the product type, enabled the corresponding data
         *     read and write permissions, and the user has completed authorization.
         * @throws { BusinessError } 1009104001 - Sport service busy. Workout is already started by other application.
         * @throws { BusinessError } 1009104003 - Illegal command. Called when workout is not started.
         * @throws { BusinessError } 1009104004 - Permission verification error.
         *     Application has no permission, such as Motion Permission.
         * @throws { BusinessError } 1009104005 - Failed to load the dynamic library.
         * @throws { BusinessError } 1009104999 - System internal error.
         * @syscap SystemCapability.Health.HealthService.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        function load(path: string, callback: Callback<DynamicLibResult>): void;
        /**
         * Algorithm dynamic library unloading
         *
         * @param { string } path - Algorithm dynamic library path.
         * @throws { BusinessError } 201  - Permission verification failed. Please ensure that the app has
         *     applied for the Health Service Kit, selected the product type, enabled the corresponding data
         *     read and write permissions, and the user has completed authorization.
         * @throws { BusinessError } 1009104001 - Sport service busy. Workout is already started by other application.
         * @throws { BusinessError } 1009104003 - Illegal command. Called when workout is not started.
         * @throws { BusinessError } 1009104004 - Permission verification error.
         *     Application has no permission, such as Motion Permission.
         * @throws { BusinessError } 1009104006 - Failed to unload the dynamic library.
         * @throws { BusinessError } 1009104999 - System internal error.
         * @syscap SystemCapability.Health.HealthService.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        function unload(path: string): void;
        /**
         * Unloads the algorithm dynamic library (asynchronously).
         *
         * @param { string } path  - Path of the algorithm dynamic library.
         * @param { Callback<DynamicLibResult> } callback  - Callback function for receiving the return code.
         * @throws { BusinessError } 201 - Permission verification failed. Please ensure that the app has
         *     applied for the Health Service Kit, selected the product type, enabled the corresponding data
         *     read and write permissions, and the user has completed authorization.
         * @throws { BusinessError } 1009104001 - Sport service busy. Workout is already started by other application.
         * @throws { BusinessError } 1009104003 - Illegal command. Called when workout is not started.
         * @throws { BusinessError } 1009104004 - Permission verification error.
         *     Application has no permission, such as Motion Permission.
         * @throws { BusinessError } 1009104006 - Failed to unload the dynamic library.
         * @throws { BusinessError } 1009104999 - System internal error.
         * @syscap SystemCapability.Health.HealthService.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        function unload(path: string, callback: Callback<DynamicLibResult>): void;
        /**
         * Workout configuration.
         *
         * @param { WorkoutConfig } workoutConfig  - Workout configuration information.
         * @throws { BusinessError } 201  - Permission verification failed. Please ensure that the app has
         *     applied for the Health Service Kit, selected the product type, enabled the corresponding data
         *     read and write permissions, and the user has completed authorization.
         * @throws { BusinessError } 1009104003 - Illegal command. Called when workout not in stoped or idle state.
         * @throws { BusinessError } 1009104999 - System internal error.
         * @syscap SystemCapability.Health.HealthService.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        function config(workoutConfig: WorkoutConfig): void;
        /**
         * Start a activity.
         *
         * @returns { StartResult } Result of function call, contains the return code and reason.
         * @throws { BusinessError } 201  - Permission verification failed. Please ensure that the app has
         *     applied for the Health Service Kit, selected the product type, enabled the corresponding data
         *     read and write permissions, and the user has completed authorization.
         * @throws { BusinessError } 1009104001 - Sport service busy. Workout is already started by other application.
         * @throws { BusinessError } 1009104002 - Unsupported sport type.
         * @throws { BusinessError } 1009104003 - Illegal command. Called when workout in sporting, paused or stopped state.
         * @throws { BusinessError } 1009104004 - Permission verification error.
         *      Application has no permission, such as Motion Permission.
         * @throws { BusinessError } 1009104999 - System internal error.
         * @syscap SystemCapability.Health.HealthService.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        function start(): StartResult;
        /**
         * Pause a activity.
         *
         * @throws { BusinessError } 201  - Permission verification failed. Please ensure that the app has
         *     applied for the Health Service Kit, selected the product type, enabled the corresponding data
         *     read and write permissions, and the user has completed authorization.
         * @throws { BusinessError } 1009104001 - Sport service busy. Workout is already started by other application.
         * @throws { BusinessError } 1009104003 - Illegal command. Called when workout in ready, paused or stoped state.
         * @throws { BusinessError } 1009104999 - System internal error.
         * @syscap SystemCapability.Health.HealthService.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        function pause(): void;
        /**
         * Resume a activity.
         *
         * @throws { BusinessError } 201  - Permission verification failed. Please ensure that the app has
         *     applied for the Health Service Kit, selected the product type, enabled the corresponding data
         *     read and write permissions, and the user has completed authorization.
         * @throws { BusinessError } 1009104001 - Sport service busy. Workout is already started by other application.
         * @throws { BusinessError } 1009104003 - Illegal command. Called when workout in ready, sporting or stopped state.
         * @throws { BusinessError } 1009104999 - System internal error.
         * @syscap SystemCapability.Health.HealthService.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        function resume(): void;
        /**
         * Stops a workout.
         *
         * @throws { BusinessError } 201  - Permission verification failed. Please ensure that the app has
         *     applied for the Health Service Kit, selected the product type, enabled the corresponding data
         *     read and write permissions, and the user has completed authorization.
         * @throws { BusinessError } 1009104003 - Illegal command. Called when workout is not started.
         * @throws { BusinessError } 1009104999 - System internal error.
         * @syscap SystemCapability.Health.HealthService.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        function stop(): void;
        /**
         * Subscribe all types of data.
         *
         * @param { undefined } dataType - DataType is undefined means every type data that can be obtained.
         * @param { Callback<SampleReal[]> } listener - Callback for data subscription.
         * @throws { BusinessError } 201 - Permission verification failed. Please ensure that the app has
         *     applied for the Health Service Kit, selected the product type, enabled the corresponding data
         *     read and write permissions, and the user has completed authorization.
         * @throws { BusinessError } 1009104001 - Sport service busy. Workout is already started by other application.
         * @throws { BusinessError } 1009104003 - Illegal command. Called when workout is not started.
         * @throws { BusinessError } 1009104999 - System internal error.
         * @syscap SystemCapability.Health.HealthService.Lite
         * @famodelonly
         * @since 6.1.1(24)
         * @deprecated since 26.0.0
         * @useinstead onData(listener: Callback)
         */
        function onData(dataType: undefined, listener: Callback<SampleReal[]>): void;
        /**
         * Unsubscribe subscription of all types of data.
         *
         * @param { undefined } dataType - DataType is undefined means every type data that can be obtained.
         * @param { Callback<SampleReal[]> } [listener] - Callback for data subscription.
         * @throws { BusinessError } 201 - Permission verification failed. Please ensure that the app has
         *     applied for the Health Service Kit, selected the product type, enabled the corresponding data
         *     read and write permissions, and the user has completed authorization.
         * @throws { BusinessError } 1009104001 - Sport service busy. Workout is already started by other application.
         * @throws { BusinessError } 1009104999 - System internal error.
         * @syscap SystemCapability.Health.HealthService.Lite
         * @famodelonly
         * @since 6.1.1(24)
         * @deprecated since 26.0.0
         * @useinstead offData(listener?: Callback)
         */
        function offData(dataType: undefined, listener?: Callback<SampleReal[]>): void;
        /**
         * Send data to linkages.
         *
         * @param { SampleReal[] } sampleReal - Realtime data.
         * @throws { BusinessError } 201  - Permission verification failed. Please ensure that the app has
         *     applied for the Health Service Kit, selected the product type, enabled the corresponding data
         *     read and write permissions, and the user has completed authorization.
         * @throws { BusinessError } 1009104001 - Sport service busy. Workout is already started by other application.
         * @throws { BusinessError } 1009104999 - System internal error.
         * @syscap SystemCapability.Health.HealthService.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        function sendData(sampleReal: SampleReal[]): void;
        /**
         * Result code of starting workout.
         *
         * @syscap SystemCapability.Health.HealthService.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        enum StartCode {
            /**
             * Startup success.
             *
             * @syscap SystemCapability.Health.HealthService.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            SUCCESS = 0,
            /**
             * Workout has started.
             *
             * @syscap SystemCapability.Health.HealthService.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            WORKOUT_WORKING = 1,
            /**
             * No connected devices.
             *
             * @syscap SystemCapability.Health.HealthService.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            NO_SUPPORTED_DEVICE = 2,
            /**
             * Device busy.
             *
             * @syscap SystemCapability.Health.HealthService.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            DEVICE_BUSY = 3
        }
        /**
         * Result code of algorithm dynamic library.
         *
         * @syscap SystemCapability.Health.HealthService.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        enum DynamicLibErrorCode {
            /**
             * Load/unload success.
             *
             * @syscap SystemCapability.Health.HealthService.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            OPERATION_SUCCESS = 0,
            /**
             * Algorithm dynamic library file not found.
             *
             * @syscap SystemCapability.Health.HealthService.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            FILE_NOT_FOUND = 1,
            /**
             * Service busy.
             *
             * @syscap SystemCapability.Health.HealthService.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            SERVICE_BUSY = 2,
            /**
             * Algorithm dynamic library load/unload fail.
             *
             * @syscap SystemCapability.Health.HealthService.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            OPERATION_FAILED = 3,
            /**
             * system internal error.
             *
             * @syscap SystemCapability.Health.HealthService.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            SYSTEM_INTERNAL_ERROR = 4
        }
        /**
         * Algorithm dynamic library operation result
         *
         * @syscap SystemCapability.Health.HealthService.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        interface DynamicLibResult {
            /**
             * Operation code
             *
             * @syscap SystemCapability.Health.HealthService.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            operationCode: DynamicLibErrorCode;
        }
        /**
         * Workout start result.
         *
         * @syscap SystemCapability.Health.HealthService.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        interface StartResult {
            /**
             * Start code.
             *
             * @syscap SystemCapability.Health.HealthService.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            startCode: StartCode;
            /**
             * Status of connected devices.
             *
             * @syscap SystemCapability.Health.HealthService.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            deviceState: DeviceState[];
        }
        /**
         * Status of a connected device.
         *
         * @syscap SystemCapability.Health.HealthService.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        interface DeviceState {
            /**
             * Device ID.
             *
             * @syscap SystemCapability.Health.HealthService.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            deviceId: string;
            /**
             * Device name.
             *
             * @syscap SystemCapability.Health.HealthService.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            deviceName?: string;
            /**
             * Device status.
             *
             * @syscap SystemCapability.Health.HealthService.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            state: number;
        }
        /**
         * Workout linkage type.
         *
         * @syscap SystemCapability.Health.HealthService.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        enum LinkageType {
            /**
             * Fitness course.
             *
             * @syscap SystemCapability.Health.HealthService.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            COURSE_LINK = 0,
            /**
             * Activity such as running, walking, or cycling.
             *
             * @syscap SystemCapability.Health.HealthService.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            ACTIVITY_LINK = 1
        }
        /**
         * Linkage type.
         *
         * @syscap SystemCapability.Health.HealthService.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        enum TargetType {
            /**
             * No goal.
             *
             * @syscap SystemCapability.Health.HealthService.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            NONE = 0,
            /**
             * Distance.
             *
             * @syscap SystemCapability.Health.HealthService.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            DISTANCE = 1,
            /**
             * Calories.
             *
             * @syscap SystemCapability.Health.HealthService.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            CALORIE = 2,
            /**
             * Time.
             *
             * @syscap SystemCapability.Health.HealthService.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            TIME = 3,
            /**
             * Number of rope jumps.
             *
             * @syscap SystemCapability.Health.HealthService.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            SKIPPING_TIMES = 4
        }
        /**
         * Subscribes to all types of data.
         *
         * @param { Callback<SampleReal[]> } listener  - Data subscription callback.
         * @throws { BusinessError } 201  - Permission verification failed. For the app, ensure that you have
         *     requested Health Service Kit, selected the product type, and enabled required data
         *     read and write permissions, and that the user has granted authorization.
         * @throws { BusinessError } 1009104001  – Sports service busy. Workout has already been started by another
         *     app.
         * @throws { BusinessError } 1009104003  - Invalid command. The API is called when workout is not started.
         * @throws { BusinessError } 1009104999  - Internal system error.
         * @syscap SystemCapability.Health.HealthService.Lite
         * @famodelonly
         * @since 26.0.0
         */
        function onData(listener: Callback<SampleReal[]>): void;
        /**
         * Cancel subscriptions for all data types.
         *
         * @param { Callback<SampleReal[]> } [listener]  - Data subscription callback.
         * @throws { BusinessError } 201  - Permission verification failed. For the app, ensure that you have
         *     requested Health Service Kit, selected the product type, and enabled required data
         *     read and write permissions, and that the user has granted authorization.
         * @throws { BusinessError } 1009104001  – Sports service busy. Workout has already been started by
         *     another app.
         * @throws { BusinessError } 1009104999  - Internal system error.
         * @syscap SystemCapability.Health.HealthService.Lite
         * @famodelonly
         * @since 26.0.0
         */
        function offData(listener?: Callback<SampleReal[]>): void;
    }
}
export default healthService;

```
