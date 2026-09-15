# @hms.health.store.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) Huawei Technologies Co., Ltd. 2026-2026. All rights reserved.
 */
/**
 * @file Defines the capabilities of HealthServiceKit.
 * @kit HealthServiceKit
 */
import { Callback } from '@ohos.base';
/**
 * This module provides the health storage function.
 *
 * @syscap SystemCapability.Health.HealthStore.Lite
 * @famodelonly
 * @since 6.1.1(24)
 */
declare namespace healthStore {
    /**
     * Data types of health data.
     *
     * @syscap SystemCapability.Health.HealthStore.Lite
     * @famodelonly
     * @since 6.1.1(24)
     */
    interface DataType {
        /**
         * Unique ID of a data type.
         *
         * @readonly
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        readonly id: number;
        /**
         * Unique ID of a data type.
         *
         * @readonly
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        readonly name?: string;
    }
    /**
     * Subdata type.
     *
     * @syscap SystemCapability.Health.HealthStore.Lite
     * @famodelonly
     * @since 6.1.1(24)
     */
    type SubDataType = DataType;
    /**
     * Step cadence.
     *
     * @syscap SystemCapability.Health.HealthStore.Lite
     * @famodelonly
     * @since 6.1.1(24)
     */
    type PaceValueType = Record<string, number>;
    /**
     * Field value type.
     *
     * @syscap SystemCapability.Health.HealthStore.Lite
     * @famodelonly
     * @since 6.1.1(24)
     */
    type HealthValueType = number | string | boolean | undefined;
    /**
     * Exercise sequence summary data.
     * It defines the statistics of a data type in a certain period of time during an exercise.
     *
     * @syscap SystemCapability.Health.HealthStore.Lite
     * @famodelonly
     * @since 6.1.1(24)
     */
    interface ExerciseSummary extends Record<string, HealthValueType | PaceValueType> {
    }
    /**
     * Defines the model for instantaneous sample data during exercise.
     * It uses one or more fields to describe the data.
     *
     * @syscap SystemCapability.Health.HealthStore.Lite
     * @famodelonly
     * @since 6.1.1(24)
     */
    interface SequencePoint extends Record<string, HealthValueType> {
        /**
         * Unix timestamp.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        startTime: number;
        /**
         * Detailed data point field.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        [P: string]: HealthValueType;
    }
    /**
     * Basic information about health data.
     *
     * @syscap SystemCapability.Health.HealthStore.Lite
     * @famodelonly
     * @since 6.1.1(24)
     */
    interface SampleDataBase {
        /**
         * Data type.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        dataType: DataType;
        /**
         * Data source ID.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        dataSourceId: string;
        /**
         * Local date of data.
         * It is in MM/DD/YYYY format.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        localDate: string;
        /**
         * Unix timestamp.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        startTime: number;
        /**
         * Unix timestamp.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        endTime: number;
        /**
         * Time zone where the data is located.
         * Example: `+0800`
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        timeZone: string;
        /**
         * Time when the data is created or modified.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        modifiedTime: number;
    }
    /**
     * Exercise sequence.
     * It consists of exercise sequence data over a specific period.
     * It contains sequence summary data and detailed sequence points.
     *
     * @syscap SystemCapability.Health.HealthStore.Lite
     * @famodelonly
     * @since 6.1.1(24)
     */
    interface ExerciseSequence<K extends Record<string, ExerciseSummary> = Record<string, ExerciseSummary>, DK extends Record<string, SequencePoint[]> = Record<string, SequencePoint[]>> extends SampleDataBase {
        /**
         * Workout type.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        exerciseType: SubDataType;
        /**
         * Activity duration of the exercise sequence data, in milliseconds since the Unix epoch.
         * The start and end times identify the full duration of the exercise.
         * However, the active duration may be shorter.
         * If no value is assigned, the duration is calculated based on the start and end times by default.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        duration?: number;
        /**
         * Summary data.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        summaries: Pick<K, keyof K>;
        /**
         * Details.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        details?: Pick<DK, keyof DK>;
    }
    /**
     * Data source options, which are used in query and deletion operations.
     *
     * @syscap SystemCapability.Health.HealthStore.Lite
     * @famodelonly
     * @since 6.1.1(24)
     */
    interface DataSourceOptions {
        /**
         * Unique data source ID for data source association.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        dataSourceId?: string;
        /**
         * Unique device ID for device association.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        deviceUniqueId?: string;
        /**
         * App package name.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        appBundleName?: string;
        /**
         * App ID.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        appId?: string;
    }
    /**
     * Basic API for requests.
     *
     * @syscap SystemCapability.Health.HealthStore.Lite
     * @famodelonly
     * @since 6.1.1(24)
     */
    interface DataRequest {
        /**
         * Local start date of data.
         * It should be formatted as MM/DD/YYYY using Intl.DateTimeFormat with the "en-US" locale.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        startLocalDate: string;
        /**
         * Local end date of data.
         * It should be formatted as MM/DD/YYYY using Intl.DateTimeFormat with the "en-US" locale.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        endLocalDate: string;
        /**
         * Request start time, in milliseconds since the Unix epoch.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        startTime: number;
        /**
         * Request end time, in milliseconds since the Unix epoch.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        endTime: number;
        /**
         * Data sources for a request.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        dataSourceOptions?: DataSourceOptions;
    }
    /**
     * Result sorting order.
     *
     * @syscap SystemCapability.Health.HealthStore.Lite
     * @famodelonly
     * @since 6.1.1(24)
     */
    enum SortOrder {
        /**
         * Sorts data in ascending order.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        ASC = 0,
        /**
         * Sorts data in descending order.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        DESC = 1
    }
    /**
     * Basic API for reading data requests.
     *
     * @syscap SystemCapability.Health.HealthStore.Lite
     * @famodelonly
     * @since 6.1.1(24)
     */
    interface DataReadRequest<DK extends Record<string, HealthValueType> = Record<string, HealthValueType>> extends DataRequest {
        /**
         * Number of records to read.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        count?: number;
        /**
         * Offset relative to the current position.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        offset?: number;
        /**
         * Sorting order. It can be omitted for ascending order.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        sortOrder?: SortOrder;
    }
    /**
     * Reading options for exercise sequence and health sequence details.
     * Any combination of the options is valid, but withDetails will override withPartialDetails.
     *
     * @syscap SystemCapability.Health.HealthStore.Lite
     * @famodelonly
     * @since 6.1.1(24)
     */
    interface SequenceReadOptions<DK extends Record<string, SequencePoint[]> = Record<string, SequencePoint[]>> {
        /**
         * Indicates to read details.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        withDetails?: boolean;
        /**
         * Indicates to read partial details.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        withPartialDetails?: (keyof DK)[];
    }
    /**
     * Base class for authorization request types.
     *
     * @syscap SystemCapability.Health.HealthStore.Lite
     * @famodelonly
     * @since 6.1.1(24)
     */
    interface AuthorizationBase {
        /**
         * Data types that require read permission.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        readDataTypes: DataType[];
        /**
         * Data types that require write permission.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        writeDataTypes: DataType[];
    }
    /**
     * Authorization response.
     *
     * @syscap SystemCapability.Health.HealthStore.Lite
     * @famodelonly
     * @since 6.1.1(24)
     */
    interface AuthorizationResponse extends AuthorizationBase {
        /**
         * Other permissions required.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        scopes?: string[];
    }
    /**
     * Authorization request parameters.
     *
     * @syscap SystemCapability.Health.HealthStore.Lite
     * @famodelonly
     * @since 6.1.1(24)
     */
    interface AuthorizationRequest extends AuthorizationBase {
        /**
         * Other permissions required.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        scopes?: string[];
    }
    /**
     * Executes a sequence read request.
     *
     * @syscap SystemCapability.Health.HealthStore.Lite
     * @famodelonly
     * @since 6.1.1(24)
     */
    interface ExerciseSequenceReadRequest<DK extends Record<string, SequencePoint[]> = Record<string, SequencePoint[]>> extends Omit<DataReadRequest, 'startLocalDate' | 'endLocalDate'> {
        /**
         * Subdata types.
         * If the value is null, the subdata types are not restricted.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        exerciseType: SubDataType | SubDataType[] | null;
        /**
         * Reading options for the exercise sequence.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        readOptions?: SequenceReadOptions<DK>;
    }
    /**
     * Requests authorization and displays the authorization screen.
     *
     * @param { AuthorizationRequest } request  - 1. Start the authorization screen for app authorization.
     *     2. The API is called by a third-party service.
     *     3. After user authorization is obtained, subsequent associated APIs can be called.
     * @returns { AuthorizationResponse } Returns the authorization result.
     * @syscap SystemCapability.Health.HealthStore.Lite
     * @famodelonly
     * @since 6.1.1(24)
     */
    function requestAuthorizations(request: AuthorizationRequest): AuthorizationResponse;
    /**
     * Obtains the local authorization result.
     *
     * @param { AuthorizationRequest } request  - Authorization query request.
     * @returns { AuthorizationResponse } Return query authorizations response.
     * @syscap SystemCapability.Health.HealthStore.Lite
     * @famodelonly
     * @since 6.1.1(24)
     */
    function getAuthorizations(request: AuthorizationRequest): AuthorizationResponse;
    /**
     * Reads exercise sequence data from the health data storage.
     * You must have the read permission on the data type in parameters.
     *
     * @param { ExerciseSequenceReadRequest } request  - Data read request.
     * @param { Callback<T[]> } callback  - Callback that returns the health data array.
     * @throws { BusinessError } 201  - Permission verification failed. Please ensure that the app has
     *     applied for the Health Service Kit, selected the product type, enabled the corresponding data
     *     read and write permissions, and the user has completed authorization.
     * @throws { BusinessError } 1002700001  - Internal system error.
     * @throws { BusinessError } 1002700002  - Database processing error.
     * @throws { BusinessError } 1002701001  - Network error. The network is unavailable.
     * @throws { BusinessError } 1002702001  - Account error. The user is not signed in with a HUAWEI ID.
     * @throws { BusinessError } 1002702002  - Account error. Failed to obtain the HUAWEI ID information.
     * @throws { BusinessError } 1002703001  - User privacy agreement not accepted.
     * @syscap SystemCapability.Health.HealthStore.Lite
     * @famodelonly
     * @since 6.1.1(24)
     */
    function readData<T extends ExerciseSequence>(request: ExerciseSequenceReadRequest, callback: Callback<T[]>): void;
    /**
     * Saves the exercise sequence data to the health data storage.
     * You must have the write permission on the data type in parameters.
     *
     * @param { ExerciseSequence } exerciseSequence  - Health data to save.
     * @throws { BusinessError } 201  - Permission verification failed. Please ensure that the app has
     *     applied for the Health Service Kit, selected the product type, enabled the corresponding data
     *     read and write permissions, and the user has completed authorization.
     * @throws { BusinessError } 1002700001  - Internal system error.
     * @throws { BusinessError } 1002700002  - Database processing error.
     * @throws { BusinessError } 1009104003  - Illegal command. Called when workout is not started.
     * @throws { BusinessError } 1002701001  - Network error. The network is unavailable.
     * @throws { BusinessError } 1002702001  - Account error. The user is not signed in with a HUAWEI ID.
     * @throws { BusinessError } 1002702002  - Account error. Failed to obtain the HUAWEI ID information.
     * @throws { BusinessError } 1002703001  - User privacy agreement not accepted.
     * @syscap SystemCapability.Health.HealthStore.Lite
     * @famodelonly
     * @since 6.1.1(24)
     */
    function saveData(exerciseSequence: ExerciseSequence): void;
    /**
     * Defines all data type constants.
     *
     * @syscap SystemCapability.Health.HealthStore.Lite
     * @famodelonly
     * @since 6.1.1(24)
     */
    namespace healthDataTypes {
        /**
         * Workout record data type.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        const WORKOUT_SUMMARY: healthStore.DataType;
        /**
         * Workout record details authorization type.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        const WORKOUT_DETAIL: healthStore.DataType;
        /**
         * Exercise record data type.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        const WORKOUT: healthStore.DataType;
        /**
         * Workout real-time data types.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        const WORKOUT_REALTIME: healthStore.DataType;
        /**
         * Data type (Badminton).
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        const BADMINTON: healthStore.SubDataType;
        /**
         * Exercise type constant for an exercise sequence.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        const TENNIS: healthStore.SubDataType;
        /**
         * Exercise type constant for an exercise sequence, indicating stair climbing.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        const STAIR_CLIMBING: healthStore.SubDataType;
        /**
         * Exercise type constant for an exercise sequence.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        const SOCCER: healthStore.SubDataType;
        /**
         * Exercise type constant for an exercise sequence.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        const PICKLEBALL: healthStore.SubDataType;
        /**
         * Exercise type constant for an exercise sequence, indicating strength training.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        const STRENGTH_TRAINING: healthStore.SubDataType;
    }
    /**
     * Define data model field structures used in the health store.
     *
     * @syscap SystemCapability.Health.HealthStore.Lite
     * @famodelonly
     * @since 6.1.1(24)
     */
    namespace healthFields {
        /**
         * API for defining SequencePoint struct for the workout heart rate.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        interface ExerciseHeartRate extends healthStore.SequencePoint {
            /**
             * Workout heart rate, in bpm. The value must be in the range of (0, 255).
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            bpm: number;
        }
        /**
         * API for defining the sequence point structure.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        interface Altitude extends healthStore.SequencePoint {
            /**
             * Altitude measured in meters.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            altitude: number;
        }
        /**
         * API for defining SequencePoint struct for the speed.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        interface Speed extends healthStore.SequencePoint {
            /**
             * Speed measured in m/s. The value must be in the range of [0, ∞).
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            speed: number;
        }
        /**
         * Define the type for strengthTraining groupSummary structure.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        type GroupSummary = {
            /**
             * Training weight.
             * The maximum length is 10.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            trainingWeight: number[];
            /**
             * Number of action groups.
             * The maximum length is 10.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            groupCount: number[];
            /**
             * Single group duration, in seconds.
             * The maximum length is 10.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            groupTime: number[];
        };
        /**
         * Define the type for strengthTraining actionSummary structure.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        type ActionSummary = {
            /**
             * Action name.
             * The maximum length is 50.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            actionName: string;
            /**
             * Interval rest duration between groups, in seconds.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            groupRestingTime: number;
            /**
             * Number of groups, Maximum value is 10.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            actionTimes?: number;
            /**
             * Training capacity.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            trainingVolume?: number;
            /**
             * Train weight unit, must be kg or lbs.
             * Default value: 'kg'.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            weightUnit?: 'kg' | 'lbs';
            /**
             * Group summary information for each exercise group.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            groups: GroupSummary[];
        };
        /**
         * Define the type for badminton exerciseSummary structure.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        type BadmintonSummary = {
            /**
             * Start time of the data, Unix epoch in millisecond.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            startTime: number;
            /**
             * Total time of the data, the unit is second.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            totalTime: number;
            /**
             * Total duration of the target motion data, the unit is second.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            targetDuration?: number;
            /**
             * Average heart rate throughout the workout, the unit is times per minute.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            avgHeartRate?: number;
            /**
             * Max heart rate throughout the workout, the unit is times per minute.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            maxHeartRate?: number;
            /**
             * Heart rate zone type (0: maximum heart rate zone, 1: reserve heart rate zone).
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            mHeartrateZoneType?: number;
            /**
             * Restore the initial heart rate value.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            startHeartRate?: number;
            /**
             * Heart rate at the end of the recovery heart rate measurement, in beats per minute.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            endHeartRate?: number;
            /**
             * Peak exercise load level.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            loadPeakLevel?: number;
            /**
             * Aerobic training stress value, value must be [0.0, 5.0].
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            aerobicTrainingStress?: number;
            /**
             * Anaerobic training stress value, value must be [0.0, 5.0].
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            anaerobicTrainingStress?: number;
            /**
             * Estimated recovery time, in hours.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            recoveryTime?: number;
            /**
             * Total number of calories for exerciseSequence in calories, value must be (0, ∞).
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            totalCalories: number;
            /**
             * Calories actively burned through exercise, excluding basal metabolism, in calories, value must be (0, ∞).
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            activeCalorie: number;
            /**
             * Average hitting speed, in kilometers per hour, value must be [0,500].
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            avgShotSpeed?: number;
            /**
             * Maximum hitting speed, in kilometers per hour, value must be [0,500].
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            maxShotSpeed?: number;
            /**
             * Total number of shots hit, value must be [0,20000].
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            shots?: number;
            /**
             * Maximum number of consecutive exchanges rounds, value must be [0,10000].
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            maxContinuousRally?: number;
            /**
             * Number of forehand shots, value must be [0,10000].
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            forehandStroke?: number;
            /**
             * Number of backhand strokes, value must be [0,10000].
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            backhandStroke?: number;
            /**
             * Number of times at bat, value must be [0,10000].
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            overhandStroke?: number;
            /**
             * Number of downshots hit, value must be [0,10000].
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            underhandStroke?: number;
            /**
             * Smash Count, value must be [0,10000].
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            smash?: number;
            /**
             * Number of high clears, value must be [0,10000].
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            highClear?: number;
        };
        /**
         * Fields about badminton details.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        type BadmintonDetail = {
            /**
             * SequencePoint array of exercise heart rate for walking exerciseSequence.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            exerciseHeartRate?: ExerciseHeartRate[];
        };
        /**
         * Define the type for soccer exerciseSummary structure.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        type SoccerSummary = {
            /**
             * Start time of the data, Unix epoch in millisecond.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            startTime: number;
            /**
             * Total time of the data, the unit is second.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            totalTime: number;
            /**
             * Total duration of the target motion data, the unit is second.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            targetDuration?: number;
            /**
             * Average heart rate throughout the workout, the unit is times per minute.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            avgHeartRate?: number;
            /**
             * Max heart rate throughout the workout, the unit is times per minute.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            maxHeartRate?: number;
            /**
             * Heart rate zone type (0: maximum heart rate zone, 1: reserve heart rate zone).
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            mHeartrateZoneType?: number;
            /**
             * Restore the initial heart rate value.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            startHeartRate?: number;
            /**
             * Heart rate at the end of the recovery heart rate measurement, in beats per minute.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            endHeartRate?: number;
            /**
             * Peak exercise load level.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            loadPeakLevel?: number;
            /**
             * Aerobic training stress value, value must be [0.0, 5.0].
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            aerobicTrainingStress?: number;
            /**
             * Anaerobic training stress value, value must be [0.0, 5.0].
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            anaerobicTrainingStress?: number;
            /**
             * Estimated recovery time, in hours.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            recoveryTime?: number;
            /**
             * Total number of calories for exerciseSequence in calories, value must be (0, ∞).
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            totalCalories: number;
            /**
             * Calories actively burned through exercise, excluding basal metabolism, in calories, value must be (0, ∞).
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            activeCalorie: number;
            /**
             * Goals scored, value must be [0,10000].
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            goalsTimes?: number;
            /**
             * Assists made, value must be [0,10000].
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            assistsTimes?: number;
        };
        /**
         * Fields about soccer details.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        type SoccerDetail = {
            /**
             * Real-time heart rate data array during the exercise process, in beats per minute.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            exerciseHeartRate?: ExerciseHeartRate[];
        };
        /**
         * Define the type for strengthTraining exerciseSummary structure.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        type StrengthTrainingSummary = {
            /**
             * Start time of the data, Unix epoch in millisecond.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            startTime: number;
            /**
             * Total time of the data, the unit is second.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            totalTime: number;
            /**
             * Total duration of the target motion data, the unit is second.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            targetDuration?: number;
            /**
             * Average heart rate throughout the workout, the unit is times per minute.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            avgHeartRate?: number;
            /**
             * Max heart rate throughout the workout, the unit is times per minute.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            maxHeartRate?: number;
            /**
             * Heart rate zone type (0: maximum heart rate zone, 1: reserve heart rate zone).
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            mHeartrateZoneType?: number;
            /**
             * Restore the initial heart rate value.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            startHeartRate?: number;
            /**
             * Heart rate at the end of the recovery heart rate measurement, in beats per minute.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            endHeartRate?: number;
            /**
             * Peak exercise load level.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            loadPeakLevel?: number;
            /**
             * Aerobic training stress value, value must be [0.0, 5.0].
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            aerobicTrainingStress?: number;
            /**
             * Anaerobic training stress value, value must be [0.0, 5.0].
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            anaerobicTrainingStress?: number;
            /**
             * Estimated recovery time, in hours.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            recoveryTime?: number;
            /**
             * Total number of calories for exerciseSequence in calories, value must be (0, ∞).
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            totalCalories: number;
            /**
             * Calories actively burned through exercise, excluding basal metabolism, in calories, value must be (0, ∞).
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            activeCalorie: number;
            /**
             * Number of actions.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            actionCount?: number;
            /**
             * Total training capacity, in kilograms.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            totalTrainingVolume?: number;
            /**
             * Total number of groups.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            actionGroups?: number;
            /**
             * Subjective fatigue grade.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            rpe?: number;
            /**
             * List of strength training actions, recording detailed information of exercises performed
             *     during the workout.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            actions?: healthFields.ActionSummary[];
        };
        /**
         * Fields about strength training details.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        type StrengthTrainingDetail = {
            /**
             * Real-time heart rate data array during the exercise process, in beats per minute.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            heartRate?: ExerciseHeartRate[];
        };
        /**
         * Fields about tennis statistics.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        type TennisSummary = {
            /**
             * Start time of the data, Unix epoch in millisecond.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            startTime: number;
            /**
             * Total time of the data, the unit is second.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            totalTime: number;
            /**
             * Total duration of the target motion data, the unit is second.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            targetDuration?: number;
            /**
             * Average heart rate throughout the workout, the unit is times per minute.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            avgHeartRate?: number;
            /**
             * Max heart rate throughout the workout, the unit is times per minute.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            maxHeartRate?: number;
            /**
             * Heart rate zone type (0: maximum heart rate zone, 1: reserve heart rate zone).
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            mHeartrateZoneType?: number;
            /**
             * Restore the initial heart rate value.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            startHeartRate?: number;
            /**
             * Heart rate at the end of the recovery heart rate measurement, in beats per minute.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            endHeartRate?: number;
            /**
             * Peak exercise load level.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            loadPeakLevel?: number;
            /**
             * Aerobic training stress value, value must be [0.0, 5.0].
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            aerobicTrainingStress?: number;
            /**
             * Anaerobic training stress value, value must be [0.0, 5.0].
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            anaerobicTrainingStress?: number;
            /**
             * Estimated recovery time, in hours.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            recoveryTime?: number;
            /**
             * Total number of calories for exerciseSequence in calories, value must be (0, ∞).
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            totalCalories: number;
            /**
             * Calories actively burned through exercise, excluding basal metabolism, in calories, value must be (0, ∞).
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            activeCalorie: number;
            /**
             * Total number of forehand shots made.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            forehand?: number;
            /**
             * Total number of backhand shots made.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            backhand?: number;
            /**
             * Total number of swings (including all forehand serves, forehand shots, and backhand shots).
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            swingTimes: number;
            /**
             * Longest consecutive hit streak.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            maxContinuousRally: number;
        };
        /**
         * Fields about tennis details.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        type TennisDetail = {
            /**
             * SequencePoint array of exercise heart rate for walking exerciseSequence.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            exerciseHeartRate?: ExerciseHeartRate[];
        };
        /**
         * Fields about stairClimb statistics.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        type StairClimbSummary = {
            /**
             * Start time of the data, Unix epoch in millisecond.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            startTime: number;
            /**
             * Total time of the data, the unit is second.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            totalTime: number;
            /**
             * Total duration of the target motion data, the unit is second.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            targetDuration?: number;
            /**
             * Average heart rate throughout the workout, the unit is times per minute.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            avgHeartRate?: number;
            /**
             * Max heart rate throughout the workout, the unit is times per minute.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            maxHeartRate?: number;
            /**
             * Heart rate zone type (0: maximum heart rate zone, 1: reserve heart rate zone).
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            mHeartrateZoneType?: number;
            /**
             * Restore the initial heart rate value.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            startHeartRate?: number;
            /**
             * Heart rate at the end of the recovery heart rate measurement, in beats per minute.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            endHeartRate?: number;
            /**
             * Peak exercise load level.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            loadPeakLevel?: number;
            /**
             * Aerobic training stress value, value must be [0.0, 5.0].
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            aerobicTrainingStress?: number;
            /**
             * Anaerobic training stress value, value must be [0.0, 5.0].
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            anaerobicTrainingStress?: number;
            /**
             * Estimated recovery time, in hours.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            recoveryTime?: number;
            /**
             * Total number of calories for exerciseSequence in calories, value must be (0, ∞).
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            totalCalories: number;
            /**
             * Calories actively burned through exercise, excluding basal metabolism, in calories, value must be (0, ∞).
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            activeCalorie: number;
            /**
             * Total steps.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            totalSteps: number;
            /**
             * Cumulative climb for altitude gain.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            elevationGain: number;
            /**
             * Number of floors climbed, value range [0,4999].
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            floors?: number;
            /**
             * Average number of floors per minute, value range [0.0, 99.9).
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            avgFloorSpeed?: number;
        };
        /**
         * Fields about stairClimb details.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        type StairClimbDetail = {
            /**
             * SequencePoint array of exercise heart rate for walking exerciseSequence.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            exerciseHeartRate?: ExerciseHeartRate[];
        };
        /**
         * Fields about pickleBall summary.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        type PickleBallSummary = {
            /**
             * Start time of the data, Unix epoch in millisecond.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            startTime: number;
            /**
             * Total time of the data, the unit is second.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            totalTime: number;
            /**
             * Total duration of the target motion data, the unit is second.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            targetDuration?: number;
            /**
             * Average heart rate throughout the workout, the unit is times per minute.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            avgHeartRate?: number;
            /**
             * Max heart rate throughout the workout, the unit is times per minute.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            maxHeartRate?: number;
            /**
             * Heart rate zone type (0: maximum heart rate zone, 1: reserve heart rate zone).
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            mHeartrateZoneType?: number;
            /**
             * Restore the initial heart rate value.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            startHeartRate?: number;
            /**
             * Heart rate at the end of the recovery heart rate measurement, in beats per minute.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            endHeartRate?: number;
            /**
             * Peak exercise load level.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            loadPeakLevel?: number;
            /**
             * Aerobic training stress value, value must be [0.0, 5.0].
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            aerobicTrainingStress?: number;
            /**
             * Anaerobic training stress value, value must be [0.0, 5.0].
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            anaerobicTrainingStress?: number;
            /**
             * Estimated recovery time, in hours.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            recoveryTime?: number;
            /**
             * Total number of calories for exerciseSequence in calories, value must be (0, ∞).
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            totalCalories: number;
            /**
             * Calories actively burned through exercise, excluding basal metabolism, in calories, value must be (0, ∞).
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            activeCalorie: number;
            /**
             * Total number of forehand shots made.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            forehand?: number;
            /**
             * Total number of backhand shots made.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            backhand?: number;
            /**
             * Number of swings with the racket.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            swingTimes?: number;
            /**
             * Maximum Burst Shots Count.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            maxContinuousRally?: number;
        };
        /**
         * Fields about pickleBall details.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        type PickleBallDetail = {
            /**
             * Real-time heart rate data array during the exercise process, in beats per minute.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            exerciseHeartRate?: ExerciseHeartRate[];
        };
    }
    /**
     * Namespace for ExerciseRealtime related functionality.
     *
     * @syscap SystemCapability.Health.HealthStore.Lite
     * @famodelonly
     * @since 6.1.1(24)
     */
    namespace exerciseRealtimeHelper {
        /**
         * Constant for the real-time activity time during exercise.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        const REALTIME_KEY_ACTIVE_TIME: string;
        /**
         * Constant for real-time aerobic training stress during exercise.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        const REALTIME_KEY_AEROBIC_TRAINING_STRESS: string;
        /**
         * Constant for real-time anaerobic training stress during exercise.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        const REALTIME_KEY_ANAEROBIC_TRAINING_STRESS: string;
        /**
         * Constant for real-time heart rate during exercise.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        const REALTIME_KEY_HEART_RATE: string;
        /**
         * Constant for the exercise duration.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        const REALTIME_KEY_DURATION: string;
        /**
         * Constant for real-time total calories during exercise.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        const REALTIME_KEY_TOTAL_CALORIES: string;
        /**
         * Constant for real-time active calorie during exercise.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        const REALTIME_KEY_ACTIVE_CALORIE: string;
        /**
         * Constant for the real-time average shooting speed during exercise.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        const REALTIME_KEY_AVG_SHOT_SPEED: string;
        /**
         * Constant for real-time shot count during exercise.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        const REALTIME_KEY_SHOTS: string;
        /**
         * Constant, indicating real-time maximum continuous rally during exercise.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        const REALTIME_KEY_MAX_CONTINUOUS_RALLY: string;
        /**
         * Constant, indicating real-time forehand stroke during exercise.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        const REALTIME_KEY_FOREHAND_STROKE: string;
        /**
         * Constant, indicating real-time backhand stroke during exercise.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        const REALTIME_KEY_BACKHAND_STROKE: string;
        /**
         * Constant for real-time smash during exercise.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        const REALTIME_KEY_SMASH: string;
        /**
         * Constant for real-time high clear during exercise.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        const REALTIME_KEY_HIGH_CLEAR: string;
        /**
         * Constant for the real-time maximum shooting speed during exercise.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        const REALTIME_KEY_MAX_SHOT_SPEED: string;
        /**
         * Constant for real-time overhand stroke during exercise.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        const REALTIME_KEY_OVERHAND_STROKE: string;
        /**
         * Constant for real-time underhand stroke during exercise.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        const REALTIME_KEY_UNDERHAND_STROKE: string;
        /**
         * Constant for real-time floors during exercise.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        const REALTIME_KEY_FLOORS: string;
        /**
         * Constant for real-time average floor speed during exercise.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        const REALTIME_KEY_AVG_FLOOR_SPEED: string;
        /**
         * Constant for real-time forehand during exercise.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        const REALTIME_KEY_FOREHAND: string;
        /**
         * Constant for real-time backhand during exercise.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        const REALTIME_KEY_BACKHAND: string;
        /**
         * Constant for real-time swing times during exercise.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        const REALTIME_KEY_SWING_TIMES: string;
        /**
         * Constant for real-time goal during exercise.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        const REALTIME_KEY_GOALS_TIMES: string;
        /**
         * Constant for real-time assist count during exercise.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        const REALTIME_KEY_ASSISTS_TIMES: string;
        /**
         * Constant for real-time total steps during exercise.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        const REALTIME_KEY_TOTAL_STEPS: string;
    }
    /**
     * Namespace for executing sequence-related functions.
     *
     * @syscap SystemCapability.Health.HealthStore.Lite
     * @famodelonly
     * @since 6.1.1(24)
     */
    namespace exerciseSequenceHelper {
        /**
         * Exercise sequence data type.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        const DATA_TYPE: healthStore.DataType;
        /**
         * Namespace for badminton-related functions.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        namespace badminton {
            /**
             * Workout type indicating badminton.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            const EXERCISE_TYPE: healthStore.SubDataType;
            /**
             * Fields of BadmintonSummary.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            type SummaryFields = healthFields.BadmintonSummary;
            /**
             * Fields of BadmintonDetail.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            type DetailFields = healthFields.BadmintonDetail;
        }
        /**
         * Namespace for tennis-related functions.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        namespace tennis {
            /**
             * Workout type indicating tennis.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            const EXERCISE_TYPE: healthStore.SubDataType;
            /**
             * Tennis court for a tennis match.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            type SummaryFields = healthFields.TennisSummary;
            /**
             * Tennis fields.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            type DetailFields = healthFields.TennisDetail;
        }
        /**
         * Namespace of the stair climbing-related functions.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        namespace stairClimb {
            /**
             * Workout type indicating stair climbing.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            const EXERCISE_TYPE: healthStore.SubDataType;
            /**
             * The fields for StairClimbSummary.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            type SummaryFields = healthFields.StairClimbSummary;
            /**
             * Fields of StairClimbDetail.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            type DetailFields = healthFields.StairClimbDetail;
        }
        /**
         * Namespace for soccer-related functions.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        namespace soccer {
            /**
             * Workout type indicating soccer.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            const EXERCISE_TYPE: healthStore.SubDataType;
            /**
             * Fields of SoccerSummary.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            type SummaryFields = healthFields.SoccerSummary;
            /**
             * Fields of SoccerDetail.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            type DetailFields = healthFields.SoccerDetail;
        }
        /**
         * Namespace of pickleball-related functions.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        namespace pickleBall {
            /**
             * Workout type indicating pickleball.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            const EXERCISE_TYPE: healthStore.SubDataType;
            /**
             * Fields of PickleBallSummary.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            type SummaryFields = healthFields.PickleBallSummary;
            /**
             * Fields of PickleBallDetail.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            type DetailFields = healthFields.PickleBallDetail;
        }
        /**
         * Namespace of strength training-related functions.
         *
         * @syscap SystemCapability.Health.HealthStore.Lite
         * @famodelonly
         * @since 6.1.1(24)
         */
        namespace strengthTraining {
            /**
             * Workout type indicating strength training.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            const EXERCISE_TYPE: healthStore.SubDataType;
            /**
             * Strength training summary fields.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            type SummaryFields = healthFields.StrengthTrainingSummary;
            /**
             * Fields of the strength training details.
             *
             * @syscap SystemCapability.Health.HealthStore.Lite
             * @famodelonly
             * @since 6.1.1(24)
             */
            type DetailFields = healthFields.StrengthTrainingDetail;
        }
    }
}
export default healthStore;

```
