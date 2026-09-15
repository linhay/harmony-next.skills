# @ohos.sensor.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2021-2025 Huawei Device Co., Ltd.
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
 * @kit SensorServiceKit
 */
import { AsyncCallback, Callback } from './@ohos.base';
/**
 * The **Sensor** module provides APIs for obtaining the sensor list and subscribing to sensor data. It also provides
 * some common sensor algorithms.
 *
 * @syscap SystemCapability.Sensors.Sensor
 * @atomicservice [since 11]
 * @since 8
 */
declare namespace sensor {
    /**
     * Enumerates the sensor types.
     *
     * @syscap SystemCapability.Sensors.Sensor
     * @atomicservice [since 11]
     * @since 9
     */
    enum SensorId {
        /**
         * Acceleration sensor.
         *
         * This API can be used in atomic services since API version 11.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @atomicservice [since 11]
         * @since 9
         */
        ACCELEROMETER = 1,
        /**
         * Gyroscope sensor.
         *
         * This API can be used in atomic services since API version 11.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @atomicservice [since 11]
         * @since 9
         */
        GYROSCOPE = 2,
        /**
         * Ambient light sensor.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 9
         */
        AMBIENT_LIGHT = 5,
        /**
         * Magnetic field sensor.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 9
         */
        MAGNETIC_FIELD = 6,
        /**
         * Barometer sensor.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 9
         */
        BAROMETER = 8,
        /**
         * Hall effect sensor.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 9
         */
        HALL = 10,
        /**
         * Proximity sensor.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 9
         */
        PROXIMITY = 12,
        /**
         * Humidity sensor.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 9
         */
        HUMIDITY = 13,
        /**
         * Orientation sensor.
         *
         * This API can be used in atomic services since API version 11.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @atomicservice [since 11]
         * @since 9
         */
        ORIENTATION = 256,
        /**
         * Gravity sensor.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 9
         */
        GRAVITY = 257,
        /**
         * Linear acceleration sensor.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 9
         */
        LINEAR_ACCELEROMETER = 258,
        /**
         * Rotation vector sensor.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 9
         */
        ROTATION_VECTOR = 259,
        /**
         * Ambient temperature sensor.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 9
         */
        AMBIENT_TEMPERATURE = 260,
        /**
         * Uncalibrated magnetic field sensor.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 9
         */
        MAGNETIC_FIELD_UNCALIBRATED = 261,
        /**
         * Uncalibrated gyroscope sensor.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 9
         */
        GYROSCOPE_UNCALIBRATED = 263,
        /**
         * Significant motion sensor.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 9
         */
        SIGNIFICANT_MOTION = 264,
        /**
         * Pedometer detection sensor.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 9
         */
        PEDOMETER_DETECTION = 265,
        /**
         * Pedometer sensor.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 9
         */
        PEDOMETER = 266,
        /**
         * Heart rate sensor.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 9
         */
        HEART_RATE = 278,
        /**
         * Wear detection sensor.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 9
         */
        WEAR_DETECTION = 280,
        /**
         * Uncalibrated acceleration sensor.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 9
         */
        ACCELEROMETER_UNCALIBRATED = 281,
        /**
         * Fused pressure sensor.
         *
         * This sensor is available only on smart watches.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 22
         */
        FUSION_PRESSURE = 283
    }
    /**
     * Subscribes to data of the acceleration sensor.
     *
     * @permission ohos.permission.ACCELEROMETER
     * @param { SensorId.ACCELEROMETER } type - Sensor type. The value is fixed at **SensorId.ACCELEROMETER**.
     * @param { Callback<AccelerometerResponse> } callback - Callback used to report the sensor data, which is an
     *     **AccelerometerResponse** object.
     * @param { Options } [options] - List of optional parameters. This parameter is used to set the data reporting
     *     frequency. The default value is 200,000,000 ns.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @atomicservice [since 11]
     * @since 9
     */
    function on(type: SensorId.ACCELEROMETER, callback: Callback<AccelerometerResponse>, options?: Options): void;
    /**
     * Subscribes to data of the uncalibrated acceleration sensor.
     *
     * @permission ohos.permission.ACCELEROMETER
     * @param { SensorId.ACCELEROMETER_UNCALIBRATED } type - Sensor type. The value is fixed at
     *     **SensorId.ACCELEROMETER_UNCALIBRATED**.
     * @param { Callback<AccelerometerUncalibratedResponse> } callback - Callback used to report the sensor data, which is
     *     an **AccelerometerUncalibratedResponse** object.
     * @param { Options } [options] - List of optional parameters. This parameter is used to set the data reporting
     *     frequency. The default value is 200,000,000 ns.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function on(type: SensorId.ACCELEROMETER_UNCALIBRATED, callback: Callback<AccelerometerUncalibratedResponse>, options?: Options): void;
    /**
     * Subscribes to data of the ambient light sensor.
     *
     * @param { SensorId.AMBIENT_LIGHT } type - Sensor type. The value is fixed at **SensorId.AMBIENT_LIGHT**.
     * @param { Callback<LightResponse> } callback - Callback used to report the sensor data, which is a **LightResponse**
     *     object.
     * @param { Options } [options] - List of optional parameters. This parameter is used to set the data reporting
     *     frequency. The default value is 200,000,000 ns.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function on(type: SensorId.AMBIENT_LIGHT, callback: Callback<LightResponse>, options?: Options): void;
    /**
     * Subscribes to data of the ambient temperature sensor.
     *
     * @param { SensorId.AMBIENT_TEMPERATURE } type - Sensor type. The value is fixed at **SensorId.AMBIENT_TEMPERATURE**.
     * @param { Callback<AmbientTemperatureResponse> } callback - Callback used to report the sensor data, which is an
     *     **AmbientTemperatureResponse** object.
     * @param { Options } [options] - List of optional parameters. This parameter is used to set the data reporting
     *     frequency. The default value is 200,000,000 ns.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function on(type: SensorId.AMBIENT_TEMPERATURE, callback: Callback<AmbientTemperatureResponse>, options?: Options): void;
    /**
     * Subscribes to data of the barometer sensor.
     *
     * @param { SensorId.BAROMETER } type - Sensor type. The value is fixed at **SensorId.BAROMETER**.
     * @param { Callback<BarometerResponse> } callback - Callback used to report the sensor data, which is a
     *     **BarometerResponse** object.
     * @param { Options } [options] - List of optional parameters. This parameter is used to set the data reporting
     *     frequency. The default value is 200,000,000 ns.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function on(type: SensorId.BAROMETER, callback: Callback<BarometerResponse>, options?: Options): void;
    /**
     * Subscribes to data of the gravity sensor.
     *
     * @param { SensorId.GRAVITY } type - Sensor type. The value is fixed at **SensorId.GRAVITY**.
     * @param { Callback<GravityResponse> } callback - Callback used to report the sensor data, which is a
     *     **GravityResponse** object.
     * @param { Options } [options] - List of optional parameters. This parameter is used to set the data reporting
     *     frequency. The default value is 200,000,000 ns.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function on(type: SensorId.GRAVITY, callback: Callback<GravityResponse>, options?: Options): void;
    /**
     * Subscribes to data of the gyroscope sensor.
     *
     * @permission ohos.permission.GYROSCOPE
     * @param { SensorId.GYROSCOPE } type - Sensor type. The value is fixed at **SensorId.GYROSCOPE**.
     * @param { Callback<GyroscopeResponse> } callback - Callback used to report the sensor data, which is a
     *     **GyroscopeResponse** object.
     * @param { Options } [options] - List of optional parameters. This parameter is used to set the data reporting
     *     frequency. The default value is 200,000,000 ns.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @atomicservice [since 11]
     * @since 9
     */
    function on(type: SensorId.GYROSCOPE, callback: Callback<GyroscopeResponse>, options?: Options): void;
    /**
     * Subscribes to data of the uncalibrated gyroscope sensor.
     *
     * @permission ohos.permission.GYROSCOPE
     * @param { SensorId.GYROSCOPE_UNCALIBRATED } type - Sensor type. The value is fixed at
     *     **SensorId.GYROSCOPE_UNCALIBRATED**.
     * @param { Callback<GyroscopeUncalibratedResponse> } callback - Callback used to report the sensor data, which is a
     *     **GyroscopeUncalibratedResponse** object.
     * @param { Options } [options] - List of optional parameters. This parameter is used to set the data reporting
     *     frequency. The default value is 200,000,000 ns.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function on(type: SensorId.GYROSCOPE_UNCALIBRATED, callback: Callback<GyroscopeUncalibratedResponse>, options?: Options): void;
    /**
     * Subscribes to data of the Hall effect sensor.
     *
     * @param { SensorId.HALL } type - Sensor type. The value is fixed at **SensorId.HALL**.
     * @param { Callback<HallResponse> } callback - Callback used to report the sensor data, which is a **HallResponse**
     *     object.
     * @param { Options } [options] - List of optional parameters. The default value is 200,000,000 ns. This parameter is
     *     used to set the data reporting frequency when Hall effect events are frequently triggered.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function on(type: SensorId.HALL, callback: Callback<HallResponse>, options?: Options): void;
    /**
     * Subscribes to data of the heart rate sensor.
     *
     * @permission ohos.permission.READ_HEALTH_DATA
     * @param { SensorId.HEART_RATE } type - Sensor type. The value is fixed at **SensorId.HEART_RATE**.
     * @param { Callback<HeartRateResponse> } callback - Callback used to report the sensor data, which is a
     *     **HeartRateResponse** object.
     * @param { Options } [options] - List of optional parameters. This parameter is used to set the data reporting
     *     frequency. The default value is 200,000,000 ns.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function on(type: SensorId.HEART_RATE, callback: Callback<HeartRateResponse>, options?: Options): void;
    /**
     * Subscribes to data of the humidity sensor.
     *
     * @param { SensorId.HUMIDITY } type - Sensor type. The value is fixed at **SensorId.HUMIDITY**.
     * @param { Callback<HumidityResponse> } callback - Callback used to report the sensor data, which is a
     *     **HumidityResponse** object.
     * @param { Options } [options] - List of optional parameters. This parameter is used to set the data reporting
     *     frequency. The default value is 200,000,000 ns.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function on(type: SensorId.HUMIDITY, callback: Callback<HumidityResponse>, options?: Options): void;
    /**
     * Subscribes to data of the linear acceleration sensor.
     *
     * @permission ohos.permission.ACCELEROMETER
     * @param { SensorId.LINEAR_ACCELEROMETER } type - Sensor type. The value is fixed at
     *     **SensorId.LINEAR_ACCELEROMETER**.
     * @param { Callback<LinearAccelerometerResponse> } callback - Callback used to report the sensor data, which is a
     *     **LinearAccelerometerResponse** object.
     * @param { Options } [options] - List of optional parameters. This parameter is used to set the data reporting
     *     frequency. The default value is 200,000,000 ns.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function on(type: SensorId.LINEAR_ACCELEROMETER, callback: Callback<LinearAccelerometerResponse>, options?: Options): void;
    /**
     * Subscribes to data of the magnetic field sensor.
     *
     * @param { SensorId.MAGNETIC_FIELD } type - Sensor type. The value is fixed at **SensorId.MAGNETIC_FIELD**.
     * @param { Callback<MagneticFieldResponse> } callback - Callback used to report the sensor data, which is a
     *     **MagneticFieldResponse** object.
     * @param { Options } [options] - List of optional parameters. This parameter is used to set the data reporting
     *     frequency. The default value is 200,000,000 ns.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function on(type: SensorId.MAGNETIC_FIELD, callback: Callback<MagneticFieldResponse>, options?: Options): void;
    /**
     * Subscribes to data of the uncalibrated magnetic field sensor.
     *
     * @param { SensorId.MAGNETIC_FIELD_UNCALIBRATED } type - Sensor type. The value is fixed at
     *     **SensorId.MAGNETIC_FIELD_UNCALIBRATED**.
     * @param { Callback<MagneticFieldUncalibratedResponse> } callback - Callback used to report the sensor data, which is
     *     a **MagneticFieldUncalibratedResponse** object.
     * @param { Options } [options] - List of optional parameters. This parameter is used to set the data reporting
     *     frequency. The default value is 200,000,000 ns.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function on(type: SensorId.MAGNETIC_FIELD_UNCALIBRATED, callback: Callback<MagneticFieldUncalibratedResponse>, options?: Options): void;
    /**
     * Subscribes to data of the orientation sensor.
     *
     * > **NOTE**
     * >
     * > Applications or services invoking this API can prompt users to use figure-8 calibration to improve the accuracy
     * > of the direction sensor. The sensor has a theoretical error of ��5 degrees, but the specific precision may vary
     * > depending on different driver implementations and algorithmic designs.
     *
     * @param { SensorId.ORIENTATION } type - Sensor type. The value is fixed at **SensorId.ORIENTATION**.
     * @param { Callback<OrientationResponse> } callback - Callback used to report the sensor data, which is a
     *     **OrientationResponse** object.
     * @param { Options } [options] - List of optional parameters. This parameter is used to set the data reporting
     *     frequency. The default value is 200,000,000 ns.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @atomicservice [since 11]
     * @since 9
     */
    function on(type: SensorId.ORIENTATION, callback: Callback<OrientationResponse>, options?: Options): void;
    /**
     * Subscribes to data of the pedometer sensor. The step counter sensor's data reporting is subject to some delay, and
     * the delay is determined by specific product implementations.
     *
     * @permission ohos.permission.ACTIVITY_MOTION
     * @param { SensorId.PEDOMETER } type - Sensor type. The value is fixed at **SensorId.PEDOMETER**.
     * @param { Callback<PedometerResponse> } callback - Callback used to report the sensor data, which is a
     *     **PedometerResponse** object.
     * @param { Options } [options] - List of optional parameters. This parameter is used to set the data reporting
     *     frequency. The default value is 200,000,000 ns.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function on(type: SensorId.PEDOMETER, callback: Callback<PedometerResponse>, options?: Options): void;
    /**
     * Subscribes to data of the pedometer detection sensor.
     *
     * @permission ohos.permission.ACTIVITY_MOTION
     * @param { SensorId.PEDOMETER_DETECTION } type - Sensor type. The value is fixed at **SensorId.PEDOMETER_DETECTION**.
     * @param { Callback<PedometerDetectionResponse> } callback - Callback used to report the sensor data, which is a
     *     **PedometerDetectionResponse** object.
     * @param { Options } [options] - List of optional parameters. This parameter is used to set the data reporting
     *     frequency. The default value is 200,000,000 ns.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function on(type: SensorId.PEDOMETER_DETECTION, callback: Callback<PedometerDetectionResponse>, options?: Options): void;
    /**
     * Subscribes to data of the proximity sensor.
     *
     * @param { SensorId.PROXIMITY } type - Sensor type. The value is fixed at **SensorId.PROXIMITY**.
     * @param { Callback<ProximityResponse> } callback - Callback used to report the sensor data, which is a
     *     **ProximityResponse** object.
     * @param { Options } [options] - List of optional parameters. The default value is 200,000,000 ns. This parameter is
     *     used to set the data reporting frequency when proximity sensor events are frequently triggered.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function on(type: SensorId.PROXIMITY, callback: Callback<ProximityResponse>, options?: Options): void;
    /**
     * Subscribes to data of the rotation vector sensor.
     *
     * @param { SensorId.ROTATION_VECTOR } type - Sensor type. The value is fixed at **SensorId.ROTATION_VECTOR**.
     * @param { Callback<RotationVectorResponse> } callback - Callback used to report the sensor data, which is a
     *     **RotationVectorResponse** object.
     * @param { Options } [options] - List of optional parameters. This parameter is used to set the data reporting
     *     frequency. The default value is 200,000,000 ns.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function on(type: SensorId.ROTATION_VECTOR, callback: Callback<RotationVectorResponse>, options?: Options): void;
    /**
     * Subscribes to the significant motion sensor data.
     *
     * @param { SensorId.SIGNIFICANT_MOTION } type - Sensor type. The value is fixed at **SensorId.SIGNIFICANT_MOTION**.
     * @param { Callback<SignificantMotionResponse> } callback - Callback used to report the sensor data, which is a
     *     **SignificantMotionResponse** object.
     * @param { Options } [options] - List of optional parameters. This parameter is used to set the data reporting
     *     frequency. The default value is 200,000,000 ns.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function on(type: SensorId.SIGNIFICANT_MOTION, callback: Callback<SignificantMotionResponse>, options?: Options): void;
    /**
     * Subscribes to data of the wear detection sensor.
     *
     * @param { SensorId.WEAR_DETECTION } type - Sensor type. The value is fixed at **SensorId.WEAR_DETECTION**.
     * @param { Callback<WearDetectionResponse> } callback - Callback used to report the sensor data, which is a
     *     **WearDetectionResponse** object.
     * @param { Options } [options] - List of optional parameters. This parameter is used to set the data reporting
     *     frequency. The default value is 200,000,000 ns.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function on(type: SensorId.WEAR_DETECTION, callback: Callback<WearDetectionResponse>, options?: Options): void;
    /**
     * Subscribes to the fused pressure sensor data.
     *
     * @param { SensorId.FUSION_PRESSURE } type - Sensor type. The value is fixed at SensorId.FUSION_PRESSURE.
     * @param { Callback<FusionPressureResponse> } callback - Callback used to report the sensor data, which is a
     *     **FusionPressureResponse** object.
     * @param { Options } [options] - List of optional parameters. This parameter is used to set the data reporting
     *     frequency. The default value is 200,000,000 ns.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 22
     */
    function on(type: SensorId.FUSION_PRESSURE, callback: Callback<FusionPressureResponse>, options?: Options): void;
    /**
     * Obtains data of the acceleration sensor once.
     *
     * @permission ohos.permission.ACCELEROMETER
     * @param { SensorId.ACCELEROMETER } type - Sensor type. The value is fixed at **SensorId.ACCELEROMETER**.
     * @param { Callback<AccelerometerResponse> } callback - Callback used to report the sensor data, which is an
     *     **AccelerometerResponse** object.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function once(type: SensorId.ACCELEROMETER, callback: Callback<AccelerometerResponse>): void;
    /**
     * Obtains data of the uncalibrated acceleration sensor once.
     *
     * @permission ohos.permission.ACCELEROMETER
     * @param { SensorId.ACCELEROMETER_UNCALIBRATED } type - Sensor type. The value is fixed at
     *     **SensorId.ACCELEROMETER_UNCALIBRATED**.
     * @param { Callback<AccelerometerUncalibratedResponse> } callback - Callback used to report the sensor data, which is
     *     an **AccelerometerUncalibratedResponse** object.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function once(type: SensorId.ACCELEROMETER_UNCALIBRATED, callback: Callback<AccelerometerUncalibratedResponse>): void;
    /**
     * Obtains data of the ambient light sensor once.
     *
     * @param { SensorId.AMBIENT_LIGHT } type - Sensor type. The value is fixed at **SensorId.AMBIENT_LIGHT**.
     * @param { Callback<LightResponse> } callback - Callback used to report the sensor data, which is a **LightResponse**
     *     object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function once(type: SensorId.AMBIENT_LIGHT, callback: Callback<LightResponse>): void;
    /**
     * Obtains data of the temperature sensor once.
     *
     * @param { SensorId.AMBIENT_TEMPERATURE } type - Sensor type. The value is fixed at **SensorId.AMBIENT_TEMPERATURE**.
     * @param { Callback<AmbientTemperatureResponse> } callback - Callback used to report the sensor data, which is an
     *     **AmbientTemperatureResponse** object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function once(type: SensorId.AMBIENT_TEMPERATURE, callback: Callback<AmbientTemperatureResponse>): void;
    /**
     * Obtains data of the barometer sensor once.
     *
     * @param { SensorId.BAROMETER } type - Sensor type. The value is fixed at **SensorId.BAROMETER**.
     * @param { Callback<BarometerResponse> } callback - Callback used to report the sensor data, which is a
     *     **BarometerResponse** object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function once(type: SensorId.BAROMETER, callback: Callback<BarometerResponse>): void;
    /**
     * Obtains data of the gravity sensor once.
     *
     * @param { SensorId.GRAVITY } type - Sensor type. The value is fixed at **SensorId.GRAVITY**.
     * @param { Callback<GravityResponse> } callback - Callback used to report the sensor data, which is a
     *     **GravityResponse** object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function once(type: SensorId.GRAVITY, callback: Callback<GravityResponse>): void;
    /**
     * Obtains data of the gyroscope sensor once.
     *
     * @permission ohos.permission.GYROSCOPE
     * @param { SensorId.GYROSCOPE } type - Sensor type. The value is fixed at **SensorId.GYROSCOPE**.
     * @param { Callback<GyroscopeResponse> } callback - Callback used to report the sensor data, which is a
     *     **GyroscopeResponse** object.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function once(type: SensorId.GYROSCOPE, callback: Callback<GyroscopeResponse>): void;
    /**
     * Obtains data of the uncalibrated gyroscope sensor once.
     *
     * @permission ohos.permission.GYROSCOPE
     * @param { SensorId.GYROSCOPE_UNCALIBRATED } type - Sensor type. The value is fixed at
     *     **SensorId.GYROSCOPE_UNCALIBRATED**.
     * @param { Callback<GyroscopeUncalibratedResponse> } callback - Callback used to report the sensor data, which is a
     *     **GyroscopeUncalibratedResponse** object.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function once(type: SensorId.GYROSCOPE_UNCALIBRATED, callback: Callback<GyroscopeUncalibratedResponse>): void;
    /**
     * Obtains data of the Hall effect sensor once.
     *
     * @param { SensorId.HALL } type - Sensor type. The value is fixed at **SensorId.HALL**.
     * @param { Callback<HallResponse> } callback - Callback used to report the sensor data, which is a **HallResponse**
     *     object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function once(type: SensorId.HALL, callback: Callback<HallResponse>): void;
    /**
     * Obtains data of the heart rate sensor once.
     *
     * @permission ohos.permission.READ_HEALTH_DATA
     * @param { SensorId.HEART_RATE } type - Sensor type. The value is fixed at **SensorId.HEART_RATE**.
     * @param { Callback<HeartRateResponse> } callback - Callback used to report the sensor data, which is a
     *     **HeartRateResponse** object.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function once(type: SensorId.HEART_RATE, callback: Callback<HeartRateResponse>): void;
    /**
     * Obtains data of the humidity sensor once.
     *
     * @param { SensorId.HUMIDITY } type - Sensor type. The value is fixed at **SensorId.HUMIDITY**.
     * @param { Callback<HumidityResponse> } callback - Callback used to report the sensor data, which is a
     *     **HumidityResponse** object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function once(type: SensorId.HUMIDITY, callback: Callback<HumidityResponse>): void;
    /**
     * Obtains data of the linear acceleration sensor once.
     *
     * @permission ohos.permission.ACCELEROMETER
     * @param { SensorId.LINEAR_ACCELEROMETER } type - Sensor type. The value is fixed at
     *     **SensorId.LINEAR_ACCELEROMETER**.
     * @param { Callback<LinearAccelerometerResponse> } callback - Callback used to report the sensor data, which is a
     *     **LinearAccelerometerResponse** object.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function once(type: SensorId.LINEAR_ACCELEROMETER, callback: Callback<LinearAccelerometerResponse>): void;
    /**
     * Obtains data of the magnetic field sensor once.
     *
     * @param { SensorId.MAGNETIC_FIELD } type - Sensor type. The value is fixed at **SensorId.MAGNETIC_FIELD**.
     * @param { Callback<MagneticFieldResponse> } callback - Callback used to report the sensor data, which is a
     *     **MagneticFieldResponse** object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function once(type: SensorId.MAGNETIC_FIELD, callback: Callback<MagneticFieldResponse>): void;
    /**
     * Obtains data of the uncalibrated magnetic field sensor once.
     *
     * @param { SensorId.MAGNETIC_FIELD_UNCALIBRATED } type - Sensor type. The value is fixed at
     *     **SensorId.MAGNETIC_FIELD_UNCALIBRATED**.
     * @param { Callback<MagneticFieldUncalibratedResponse> } callback - Callback used to report the sensor data, which is
     *     a **MagneticFieldUncalibratedResponse** object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function once(type: SensorId.MAGNETIC_FIELD_UNCALIBRATED, callback: Callback<MagneticFieldUncalibratedResponse>): void;
    /**
     * Obtains data of the orientation sensor once.
     *
     * @param { SensorId.ORIENTATION } type - Sensor type. The value is fixed at **SensorId.ORIENTATION**.
     * @param { Callback<OrientationResponse> } callback - Callback used to report the sensor data, which is a
     *     **OrientationResponse** object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function once(type: SensorId.ORIENTATION, callback: Callback<OrientationResponse>): void;
    /**
     * Obtains data of the pedometer sensor once. The step counter sensor's data reporting is subject to some delay, and
     * the delay is determined by specific product implementations.
     *
     * @permission ohos.permission.ACTIVITY_MOTION
     * @param { SensorId.PEDOMETER } type - Sensor type. The value is fixed at **SensorId.PEDOMETER**.
     * @param { Callback<PedometerResponse> } callback - Callback used to report the sensor data, which is a
     *     **PedometerResponse** object.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function once(type: SensorId.PEDOMETER, callback: Callback<PedometerResponse>): void;
    /**
     * Obtains data of the pedometer sensor once.
     *
     * @permission ohos.permission.ACTIVITY_MOTION
     * @param { SensorId.PEDOMETER_DETECTION } type - Sensor type. The value is fixed at **SensorId.PEDOMETER_DETECTION**.
     * @param { Callback<PedometerDetectionResponse> } callback - Callback used to report the sensor data, which is a
     *     **PedometerDetectionResponse** object.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function once(type: SensorId.PEDOMETER_DETECTION, callback: Callback<PedometerDetectionResponse>): void;
    /**
     * Obtains data of the proximity sensor once.
     *
     * @param { SensorId.PROXIMITY } type - Sensor type. The value is fixed at **SensorId.PROXIMITY**.
     * @param { Callback<ProximityResponse> } callback - Callback used to report the sensor data, which is a
     *     **ProximityResponse** object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function once(type: SensorId.PROXIMITY, callback: Callback<ProximityResponse>): void;
    /**
     * Obtains data of the rotation vector sensor once.
     *
     * @param { SensorId.ROTATION_VECTOR } type - Sensor type. The value is fixed at **SensorId.ROTATION_VECTOR**.
     * @param { Callback<RotationVectorResponse> } callback - Callback used to report the sensor data, which is a
     *     **RotationVectorResponse** object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function once(type: SensorId.ROTATION_VECTOR, callback: Callback<RotationVectorResponse>): void;
    /**
     * Obtains the significant motion sensor data once.
     *
     * @param { SensorId.SIGNIFICANT_MOTION } type - Sensor type. The value is fixed at **SensorId.SIGNIFICANT_MOTION**.
     * @param { Callback<SignificantMotionResponse> } callback - Callback used to report the sensor data, which is a
     *     **SignificantMotionResponse** object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function once(type: SensorId.SIGNIFICANT_MOTION, callback: Callback<SignificantMotionResponse>): void;
    /**
     * Obtains data of the wear detection sensor once.
     *
     * @param { SensorId.WEAR_DETECTION } type - Sensor type. The value is fixed at **SensorId.WEAR_DETECTION**.
     * @param { Callback<WearDetectionResponse> } callback - Callback used to report the sensor data, which is a
     *     **WearDetectionResponse** object.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function once(type: SensorId.WEAR_DETECTION, callback: Callback<WearDetectionResponse>): void;
    /**
     * Unsubscribes from data of the acceleration sensor.
     *
     * @permission ohos.permission.ACCELEROMETER
     * @param { SensorId.ACCELEROMETER } type - Sensor type. The value is fixed at **SensorId.ACCELEROMETER**.
     * @param { Callback<AccelerometerResponse> } callback - Callback used for unsubscription. If this parameter is not
     *     specified, all callbacks of the specified sensor type are unsubscribed from.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Sensors.Sensor
     * @atomicservice [since 11]
     * @since 9
     */
    function off(type: SensorId.ACCELEROMETER, callback?: Callback<AccelerometerResponse>): void;
    /**
     * Unsubscribes from data of the acceleration sensor.
     *
     * @permission ohos.permission.ACCELEROMETER
     * @param { SensorId.ACCELEROMETER } type - Sensor type. The value is fixed at **SensorId.ACCELEROMETER**.
     * @param { SensorInfoParam } [sensorInfoParam] - Sensor parameters, including **deviceId** and **sensorIndex**.
     * @param { Callback<AccelerometerResponse> } [callback] - Callback used for unsubscription. If this parameter is not
     *     specified, all callbacks of the specified sensor type are unsubscribed from.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @atomicservice
     * @since 19
     */
    function off(type: SensorId.ACCELEROMETER, sensorInfoParam?: SensorInfoParam, callback?: Callback<AccelerometerResponse>): void;
    /**
     * Unsubscribes from data of the uncalibrated acceleration sensor.
     *
     * @permission ohos.permission.ACCELEROMETER
     * @param { SensorId.ACCELEROMETER_UNCALIBRATED } type - Sensor type. The value is fixed at
     *     **SensorId.ACCELEROMETER_UNCALIBRATED**.
     * @param { Callback<AccelerometerUncalibratedResponse> } callback - Callback used for unsubscription. If this
     *     parameter is not specified, all callbacks of the specified sensor type are unsubscribed from.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function off(type: SensorId.ACCELEROMETER_UNCALIBRATED, callback?: Callback<AccelerometerUncalibratedResponse>): void;
    /**
     * Unsubscribes from data of the uncalibrated acceleration sensor.
     *
     * @permission ohos.permission.ACCELEROMETER
     * @param { SensorId.ACCELEROMETER_UNCALIBRATED } type - Sensor type. The value is fixed at
     *     **SensorId.ACCELEROMETER_UNCALIBRATED**.
     * @param { SensorInfoParam } [sensorInfoParam] - Sensor parameters, including **deviceId** and **sensorIndex**.
     * @param { Callback<AccelerometerUncalibratedResponse> } [callback] - Callback used for unsubscription. If this
     *     parameter is not specified, all callbacks of the specified sensor type are unsubscribed from.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 19
     */
    function off(type: SensorId.ACCELEROMETER_UNCALIBRATED, sensorInfoParam?: SensorInfoParam, callback?: Callback<AccelerometerUncalibratedResponse>): void;
    /**
     * Unsubscribes from data of the ambient light sensor.
     *
     * @param { SensorId.AMBIENT_LIGHT } type - Sensor type. The value is fixed at **SensorId.AMBIENT_LIGHT**.
     * @param { Callback<LightResponse> } callback - Callback used for unsubscription. If this parameter is not specified,
     *     all callbacks of the specified sensor type are unsubscribed from.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function off(type: SensorId.AMBIENT_LIGHT, callback?: Callback<LightResponse>): void;
    /**
     * Unsubscribes from data of the ambient light sensor.
     *
     * @param { SensorId.AMBIENT_LIGHT } type - Sensor type. The value is fixed at **SensorId.AMBIENT_LIGHT**.
     * @param { SensorInfoParam } [sensorInfoParam] - Sensor parameters, including **deviceId** and **sensorIndex**.
     * @param { Callback<LightResponse> } [callback] - Callback used for unsubscription. If this parameter is not
     *     specified, all callbacks of the specified sensor type are unsubscribed from.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 19
     */
    function off(type: SensorId.AMBIENT_LIGHT, sensorInfoParam?: SensorInfoParam, callback?: Callback<LightResponse>): void;
    /**
     * Unsubscribes from data of the ambient temperature sensor.
     *
     * @param { SensorId.AMBIENT_TEMPERATURE } type - Sensor type. The value is fixed at **SensorId.AMBIENT_TEMPERATURE**.
     * @param { Callback<AmbientTemperatureResponse> } callback - Callback used for unsubscription. If this parameter is
     *     not specified, all callbacks of the specified sensor type are unsubscribed from.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function off(type: SensorId.AMBIENT_TEMPERATURE, callback?: Callback<AmbientTemperatureResponse>): void;
    /**
     * Unsubscribes from data of the ambient temperature sensor.
     *
     * @param { SensorId.AMBIENT_TEMPERATURE } type - Sensor type. The value is fixed at **SensorId.AMBIENT_TEMPERATURE**.
     * @param { SensorInfoParam } [sensorInfoParam] - Sensor parameters, including **deviceId** and **sensorIndex**.
     * @param { Callback<AmbientTemperatureResponse> } [callback] - Callback used for unsubscription. If this parameter is
     *     not specified, all callbacks of the specified sensor type are unsubscribed from.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 19
     */
    function off(type: SensorId.AMBIENT_TEMPERATURE, sensorInfoParam?: SensorInfoParam, callback?: Callback<AmbientTemperatureResponse>): void;
    /**
     * Unsubscribes from data of the barometer sensor.
     *
     * @param { SensorId.BAROMETER } type - Sensor type. The value is fixed at **SensorId.BAROMETER**.
     * @param { Callback<BarometerResponse> } callback - Callback used for unsubscription. If this parameter is not
     *     specified, all callbacks of the specified sensor type are unsubscribed from.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function off(type: SensorId.BAROMETER, callback?: Callback<BarometerResponse>): void;
    /**
     * Unsubscribes from data of the barometer sensor.
     *
     * @param { SensorId.BAROMETER } type - Sensor type. The value is fixed at **SensorId.BAROMETER**.
     * @param { SensorInfoParam } [sensorInfoParam] - Sensor parameters, including **deviceId** and **sensorIndex**.
     * @param { Callback<BarometerResponse> } [callback] - Callback used for unsubscription. If this parameter is not
     *     specified, all callbacks of the specified sensor type are unsubscribed from.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 19
     */
    function off(type: SensorId.BAROMETER, sensorInfoParam?: SensorInfoParam, callback?: Callback<BarometerResponse>): void;
    /**
     * Unsubscribes from data of the gravity sensor.
     *
     * @param { SensorId.GRAVITY } type - Sensor type. The value is fixed at **SensorId.GRAVITY**.
     * @param { Callback<GravityResponse> } callback - Callback used for unsubscription. If this parameter is not
     *     specified, all callbacks of the specified sensor type are unsubscribed from.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function off(type: SensorId.GRAVITY, callback?: Callback<GravityResponse>): void;
    /**
     * Unsubscribes from data of the gravity sensor.
     *
     * @param { SensorId.GRAVITY } type - Sensor type. The value is fixed at **SensorId.GRAVITY**.
     * @param { SensorInfoParam } [sensorInfoParam] - Sensor parameters, including **deviceId** and **sensorIndex**.
     * @param { Callback<GravityResponse> } [callback] - Callback used for unsubscription. If this parameter is not
     *     specified, all callbacks of the specified sensor type are unsubscribed from.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 19
     */
    function off(type: SensorId.GRAVITY, sensorInfoParam?: SensorInfoParam, callback?: Callback<GravityResponse>): void;
    /**
     * Unsubscribes from data of the gyroscope sensor.
     *
     * @permission ohos.permission.GYROSCOPE
     * @param { SensorId.GYROSCOPE } type - Sensor type. The value is fixed at **SensorId.GYROSCOPE**.
     * @param { Callback<GyroscopeResponse> } callback - Callback used for unsubscription. If this parameter is not
     *     specified, all callbacks of the specified sensor type are unsubscribed from.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Sensors.Sensor
     * @atomicservice [since 11]
     * @since 9
     */
    function off(type: SensorId.GYROSCOPE, callback?: Callback<GyroscopeResponse>): void;
    /**
     * Unsubscribes from data of the gyroscope sensor.
     *
     * @permission ohos.permission.GYROSCOPE
     * @param { SensorId.GYROSCOPE } type - Sensor type. The value is fixed at **SensorId.GYROSCOPE**.
     * @param { SensorInfoParam } [sensorInfoParam] - Sensor parameters, including **deviceId** and **sensorIndex**.
     * @param { Callback<GyroscopeResponse> } [callback] - Callback used for unsubscription. If this parameter is not
     *     specified, all callbacks of the specified sensor type are unsubscribed from.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @atomicservice
     * @since 19
     */
    function off(type: SensorId.GYROSCOPE, sensorInfoParam?: SensorInfoParam, callback?: Callback<GyroscopeResponse>): void;
    /**
     * Unsubscribes from data of the uncalibrated gyroscope sensor.
     *
     * @permission ohos.permission.GYROSCOPE
     * @param { SensorId.GYROSCOPE_UNCALIBRATED } type - Sensor type. The value is fixed at
     *     **SensorId.GYROSCOPE_UNCALIBRATED**.
     * @param { Callback<GyroscopeUncalibratedResponse> } callback - Callback used for unsubscription. If this parameter
     *     is not specified, all callbacks of the specified sensor type are unsubscribed from.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function off(type: SensorId.GYROSCOPE_UNCALIBRATED, callback?: Callback<GyroscopeUncalibratedResponse>): void;
    /**
     * Unsubscribes from data of the uncalibrated gyroscope sensor.
     *
     * @permission ohos.permission.GYROSCOPE
     * @param { SensorId.GYROSCOPE_UNCALIBRATED } type - Sensor type. The value is fixed at
     *     **SensorId.GYROSCOPE_UNCALIBRATED**.
     * @param { SensorInfoParam } [sensorInfoParam] - Sensor parameters, including **deviceId** and **sensorIndex**.
     * @param { Callback<GyroscopeUncalibratedResponse> } [callback] - Callback used for unsubscription. If this parameter
     *     is not specified, all callbacks of the specified sensor type are unsubscribed from.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 19
     */
    function off(type: SensorId.GYROSCOPE_UNCALIBRATED, sensorInfoParam?: SensorInfoParam, callback?: Callback<GyroscopeUncalibratedResponse>): void;
    /**
     * Unsubscribes from data of the Hall effect sensor.
     *
     * @param { SensorId.HALL } type - Sensor type. The value is fixed at **SensorId.HALL**.
     * @param { Callback<HallResponse> } callback - Callback used for unsubscription. If this parameter is not specified,
     *     all callbacks of the specified sensor type are unsubscribed from.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function off(type: SensorId.HALL, callback?: Callback<HallResponse>): void;
    /**
     * Unsubscribes from data of the Hall effect sensor.
     *
     * @param { SensorId.HALL } type - Sensor type. The value is fixed at **SensorId.HALL**.
     * @param { SensorInfoParam } [sensorInfoParam] - Sensor parameters, including **deviceId** and **sensorIndex**.
     * @param { Callback<HallResponse> } [callback] - Callback used for unsubscription. If this parameter is not specified
     *     , all callbacks of the specified sensor type are unsubscribed from.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 19
     */
    function off(type: SensorId.HALL, sensorInfoParam?: SensorInfoParam, callback?: Callback<HallResponse>): void;
    /**
     * Unsubscribes from data of the heart rate sensor.
     *
     * @permission ohos.permission.READ_HEALTH_DATA
     * @param { SensorId.HEART_RATE } type - Sensor type. The value is fixed at **SensorId.HEART_RATE**.
     * @param { Callback<HeartRateResponse> } callback - Callback used for unsubscription. If this parameter is not
     *     specified, all callbacks of the specified sensor type are unsubscribed from.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function off(type: SensorId.HEART_RATE, callback?: Callback<HeartRateResponse>): void;
    /**
     * Unsubscribes from data of the heart rate sensor.
     *
     * @permission ohos.permission.READ_HEALTH_DATA
     * @param { SensorId.HEART_RATE } type - Sensor type. The value is fixed at **SensorId.HEART_RATE**.
     * @param { SensorInfoParam } [sensorInfoParam] - Sensor parameters, including **deviceId** and **sensorIndex**.
     * @param { Callback<HeartRateResponse> } [callback] - Callback used for unsubscription. If this parameter is not
     *     specified, all callbacks of the specified sensor type are unsubscribed from.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 19
     */
    function off(type: SensorId.HEART_RATE, sensorInfoParam?: SensorInfoParam, callback?: Callback<HeartRateResponse>): void;
    /**
     * Unsubscribes from data of the humidity sensor.
     *
     * @param { SensorId.HUMIDITY } type - Sensor type. The value is fixed at **SensorId.HUMIDITY**.
     * @param { Callback<HumidityResponse> } callback - Callback used for unsubscription. If this parameter is not
     *     specified, all callbacks of the specified sensor type are unsubscribed from.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function off(type: SensorId.HUMIDITY, callback?: Callback<HumidityResponse>): void;
    /**
     * Unsubscribes from data of the humidity sensor.
     *
     * @param { SensorId.HUMIDITY } type - Sensor type. The value is fixed at **SensorId.HUMIDITY**.
     * @param { SensorInfoParam } [sensorInfoParam] - Sensor parameters, including **deviceId** and **sensorIndex**.
     * @param { Callback<HumidityResponse> } [callback] - Callback used for unsubscription. If this parameter is not
     *     specified, all callbacks of the specified sensor type are unsubscribed from.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 19
     */
    function off(type: SensorId.HUMIDITY, sensorInfoParam?: SensorInfoParam, callback?: Callback<HumidityResponse>): void;
    /**
     * Unsubscribes from data of the linear acceleration sensor.
     *
     * @permission ohos.permission.ACCELEROMETER
     * @param { SensorId.LINEAR_ACCELEROMETER } type - Sensor type. The value is fixed at
     *     **SensorId.LINEAR_ACCELERATION**.
     * @param { Callback<LinearAccelerometerResponse> } callback - Callback used for unsubscription. If this parameter is
     *     not specified, all callbacks of the specified sensor type are unsubscribed from.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function off(type: SensorId.LINEAR_ACCELEROMETER, callback?: Callback<LinearAccelerometerResponse>): void;
    /**
     * Unsubscribes from data of the linear acceleration sensor.
     *
     * @permission ohos.permission.ACCELEROMETER
     * @param { SensorId.LINEAR_ACCELEROMETER } type - Sensor type. The value is fixed at
     *     **SensorId.LINEAR_ACCELERATION**.
     * @param { SensorInfoParam } [sensorInfoParam] - Sensor parameters, including **deviceId** and **sensorIndex**.
     * @param { Callback<LinearAccelerometerResponse> } [callback] - Callback used for unsubscription. If this parameter
     *     is not specified, all callbacks of the specified sensor type are unsubscribed from.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 19
     */
    function off(type: SensorId.LINEAR_ACCELEROMETER, sensorInfoParam?: SensorInfoParam, callback?: Callback<LinearAccelerometerResponse>): void;
    /**
     * Unsubscribes from data of the magnetic field sensor.
     *
     * @param { SensorId.MAGNETIC_FIELD } type - Sensor type. The value is fixed at **SensorId.MAGNETIC_FIELD**.
     * @param { Callback<MagneticFieldResponse> } callback - Callback used for unsubscription. If this parameter is not
     *     specified, all callbacks of the specified sensor type are unsubscribed from.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function off(type: SensorId.MAGNETIC_FIELD, callback?: Callback<MagneticFieldResponse>): void;
    /**
     * Unsubscribes from data of the magnetic field sensor.
     *
     * @param { SensorId.MAGNETIC_FIELD } type - Sensor type. The value is fixed at **SensorId.MAGNETIC_FIELD**.
     * @param { SensorInfoParam } [sensorInfoParam] - Sensor parameters, including **deviceId** and **sensorIndex**.
     * @param { Callback<MagneticFieldResponse> } [callback] - Callback used for unsubscription. If this parameter is not
     *     specified, all callbacks of the specified sensor type are unsubscribed from.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 19
     */
    function off(type: SensorId.MAGNETIC_FIELD, sensorInfoParam?: SensorInfoParam, callback?: Callback<MagneticFieldResponse>): void;
    /**
     * Unsubscribes from data of the uncalibrated magnetic field sensor.
     *
     * @param { SensorId.MAGNETIC_FIELD_UNCALIBRATED } type - Sensor type. The value is fixed at
     *     **SensorId.MAGNETIC_FIELD_UNCALIBRATED**.
     * @param { Callback<MagneticFieldUncalibratedResponse> } callback - Callback used for unsubscription. If this
     *     parameter is not specified, all callbacks of the specified sensor type are unsubscribed from.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function off(type: SensorId.MAGNETIC_FIELD_UNCALIBRATED, callback?: Callback<MagneticFieldUncalibratedResponse>): void;
    /**
     * Unsubscribes from data of the uncalibrated magnetic field sensor.
     *
     * @param { SensorId.MAGNETIC_FIELD_UNCALIBRATED } type - Sensor type. The value is fixed at
     *     **SensorId.MAGNETIC_FIELD_UNCALIBRATED**.
     * @param { SensorInfoParam } [sensorInfoParam] - Sensor parameters, including **deviceId** and **sensorIndex**.
     * @param { Callback<MagneticFieldUncalibratedResponse> } [callback] - Callback used for unsubscription. If this
     *     parameter is not specified, all callbacks of the specified sensor type are unsubscribed from.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 19
     */
    function off(type: SensorId.MAGNETIC_FIELD_UNCALIBRATED, sensorInfoParam?: SensorInfoParam, callback?: Callback<MagneticFieldUncalibratedResponse>): void;
    /**
     * Unsubscribes from data of the orientation sensor.
     *
     * @param { SensorId.ORIENTATION } type - Sensor type. The value is fixed at **SensorId.ORIENTATION**.
     * @param { Callback<OrientationResponse> } callback - Callback used for unsubscription. If this parameter is not
     *     specified, all callbacks of the specified sensor type are unsubscribed from.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Sensors.Sensor
     * @atomicservice [since 11]
     * @since 9
     */
    function off(type: SensorId.ORIENTATION, callback?: Callback<OrientationResponse>): void;
    /**
     * Unsubscribes from data of the orientation sensor.
     *
     * @param { SensorId.ORIENTATION } type - Sensor type. The value is fixed at **SensorId.ORIENTATION**.
     * @param { SensorInfoParam } [sensorInfoParam] - Sensor parameters, including **deviceId** and **sensorIndex**.
     * @param { Callback<OrientationResponse> } [callback] - Callback used for unsubscription. If this parameter is not
     *     specified, all callbacks of the specified sensor type are unsubscribed from.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @atomicservice
     * @since 19
     */
    function off(type: SensorId.ORIENTATION, sensorInfoParam?: SensorInfoParam, callback?: Callback<OrientationResponse>): void;
    /**
     * Unsubscribes from data of the pedometer sensor.
     *
     * @permission ohos.permission.ACTIVITY_MOTION
     * @param { SensorId.PEDOMETER } type - Sensor type. The value is fixed at **SensorId.PEDOMETER**.
     * @param { Callback<PedometerResponse> } callback - Callback used for unsubscription. If this parameter is not
     *     specified, all callbacks of the specified sensor type are unsubscribed from.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function off(type: SensorId.PEDOMETER, callback?: Callback<PedometerResponse>): void;
    /**
     * Unsubscribes from data of the pedometer sensor.
     *
     * @permission ohos.permission.ACTIVITY_MOTION
     * @param { SensorId.PEDOMETER } type - Sensor type. The value is fixed at **SensorId.PEDOMETER**.
     * @param { SensorInfoParam } [sensorInfoParam] - Sensor parameters, including **deviceId** and **sensorIndex**.
     * @param { Callback<PedometerResponse> } [callback] - Callback used for unsubscription. If this parameter is not
     *     specified, all callbacks of the specified sensor type are unsubscribed from.
     * @throws { BusinessError } 201 - Permission denied
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 19
     */
    function off(type: SensorId.PEDOMETER, sensorInfoParam?: SensorInfoParam, callback?: Callback<PedometerResponse>): void;
    /**
     * Unsubscribes from data of the pedometer detection sensor.
     *
     * @permission ohos.permission.ACTIVITY_MOTION
     * @param { SensorId.PEDOMETER_DETECTION } type - Sensor type. The value is fixed at **SensorId.PEDOMETER_DETECTION**.
     * @param { Callback<PedometerDetectionResponse> } callback - Callback used for unsubscription. If this parameter is
     *     not specified, all callbacks of the specified sensor type are unsubscribed from.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function off(type: SensorId.PEDOMETER_DETECTION, callback?: Callback<PedometerDetectionResponse>): void;
    /**
     * Unsubscribes from data of the pedometer detection sensor.
     *
     * @permission ohos.permission.ACTIVITY_MOTION
     * @param { SensorId.PEDOMETER_DETECTION } type - Sensor type. The value is fixed at **SensorId.PEDOMETER_DETECTION**.
     * @param { SensorInfoParam } [sensorInfoParam] - Sensor parameters, including **deviceId** and **sensorIndex**.
     * @param { Callback<PedometerDetectionResponse> } [callback] - Callback used for unsubscription. If this parameter is
     *     not specified, all callbacks of the specified sensor type are unsubscribed from.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 19
     */
    function off(type: SensorId.PEDOMETER_DETECTION, sensorInfoParam?: SensorInfoParam, callback?: Callback<PedometerDetectionResponse>): void;
    /**
     * Unsubscribes from data of the proximity sensor.
     *
     * @param { SensorId.PROXIMITY } type - Sensor type. The value is fixed at **SensorId.PROXIMITY**.
     * @param { Callback<ProximityResponse> } callback - Callback used for unsubscription. If this parameter is not
     *     specified, all callbacks of the specified sensor type are unsubscribed from.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function off(type: SensorId.PROXIMITY, callback?: Callback<ProximityResponse>): void;
    /**
     * Unsubscribes from data of the proximity sensor.
     *
     * @param { SensorId.PROXIMITY } type - Sensor type. The value is fixed at **SensorId.PROXIMITY**.
     * @param { SensorInfoParam } [sensorInfoParam] - Sensor parameters, including **deviceId** and **sensorIndex**.
     * @param { Callback<ProximityResponse> } [callback] - Callback used for unsubscription. If this parameter is not
     *     specified, all callbacks of the specified sensor type are unsubscribed from.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 19
     */
    function off(type: SensorId.PROXIMITY, sensorInfoParam?: SensorInfoParam, callback?: Callback<ProximityResponse>): void;
    /**
     * Unsubscribes from data of the rotation vector sensor.
     *
     * @param { SensorId.ROTATION_VECTOR } type - Sensor type. The value is fixed at **SensorId.ROTATION_VECTOR**.
     * @param { Callback<RotationVectorResponse> } callback - Callback used for unsubscription. If this parameter is not
     *     specified, all callbacks of the specified sensor type are unsubscribed from.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function off(type: SensorId.ROTATION_VECTOR, callback?: Callback<RotationVectorResponse>): void;
    /**
     * Unsubscribes from data of the rotation vector sensor.
     *
     * @param { SensorId.ROTATION_VECTOR } type - Sensor type. The value is fixed at **SensorId.ROTATION_VECTOR**.
     * @param { SensorInfoParam } [sensorInfoParam] - Sensor parameters, including **deviceId** and **sensorIndex**.
     * @param { Callback<RotationVectorResponse> } [callback] - Callback used for unsubscription. If this parameter is not
     *     specified, all callbacks of the specified sensor type are unsubscribed from.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 19
     */
    function off(type: SensorId.ROTATION_VECTOR, sensorInfoParam?: SensorInfoParam, callback?: Callback<RotationVectorResponse>): void;
    /**
     * Unsubscribes from valid motion sensor data.
     *
     * @param { SensorId.SIGNIFICANT_MOTION } type - Sensor type. The value is fixed at **SensorId.SIGNIFICANT_MOTION**.
     * @param { Callback<SignificantMotionResponse> } callback - Callback used for unsubscription. If this parameter is
     *     not specified, all callbacks of the specified sensor type are unsubscribed from.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function off(type: SensorId.SIGNIFICANT_MOTION, callback?: Callback<SignificantMotionResponse>): void;
    /**
     * Unsubscribes from valid motion sensor data.
     *
     * @param { SensorId.SIGNIFICANT_MOTION } type - Sensor type. The value is fixed at **SensorId.SIGNIFICANT_MOTION**.
     * @param { SensorInfoParam } [sensorInfoParam] - Sensor parameters, including **deviceId** and **sensorIndex**.
     * @param { Callback<SignificantMotionResponse> } [callback] - Callback used for unsubscription. If this parameter is
     *     not specified, all callbacks of the specified sensor type are unsubscribed from.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 19
     */
    function off(type: SensorId.SIGNIFICANT_MOTION, sensorInfoParam?: SensorInfoParam, callback?: Callback<SignificantMotionResponse>): void;
    /**
     * Unsubscribes from data of the wear detection sensor.
     *
     * @param { SensorId.WEAR_DETECTION } type - Sensor type. The value is fixed at **SensorId.WEAR_DETECTION**.
     * @param { Callback<WearDetectionResponse> } callback - Callback used for unsubscription. If this parameter is not
     *     specified, all callbacks of the specified sensor type are unsubscribed from.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function off(type: SensorId.WEAR_DETECTION, callback?: Callback<WearDetectionResponse>): void;
    /**
     * Unsubscribes from the fused pressure sensor data.
     *
     * @param { SensorId.FUSION_PRESSURE } type - Sensor type. The value is fixed at SensorId.FUSION_PRESSURE.
     * @param { SensorInfoParam } [sensorInfoParam] - Sensor parameters, including **deviceId** and **sensorIndex**.
     * @param { Callback<FusionPressureResponse> } callback - Callback used for unsubscription. If this parameter is not
     *     specified, all callbacks of the specified sensor type are unsubscribed from.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 22
     */
    function off(type: SensorId.FUSION_PRESSURE, sensorInfoParam?: SensorInfoParam, callback?: Callback<FusionPressureResponse>): void;
    /**
     * Unsubscribes from data of the wear detection sensor.
     *
     * @param { SensorId.WEAR_DETECTION } type - Sensor type. The value is fixed at **SensorId.WEAR_DETECTION**.
     * @param { SensorInfoParam } [sensorInfoParam] - Sensor parameters, including **deviceId** and **sensorIndex**.
     * @param { Callback<WearDetectionResponse> } [callback] - Callback used for unsubscription. If this parameter is not
     *     specified, all callbacks of the specified sensor type are unsubscribed from.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 19
     */
    function off(type: SensorId.WEAR_DETECTION, sensorInfoParam?: SensorInfoParam, callback?: Callback<WearDetectionResponse>): void;
    /**
     * Subscribes to data changes of the acceleration sensor. If this API is called multiple times for the same
     * application, the last call takes effect.
     *
     * @permission ohos.permission.ACCELEROMETER
     * @param { SensorType.SENSOR_TYPE_ID_ACCELEROMETER } type - Type of the sensor to subscribe to, which is
     *     **SENSOR_TYPE_ID_ACCELEROMETER**.
     * @param { Callback<AccelerometerResponse> } callback - Callback used to return the acceleration sensor data. The
     *     reported data type in the callback is **AccelerometerResponse**.
     * @param { Options } options - List of optional parameters. This parameter is used to set the data reporting
     *     frequency. The default value is 200,000,000 ns.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.on(type: SensorId.ACCELEROMETER, callback: Callback<AccelerometerResponse>, options?: Options)
     */
    function on(type: SensorType.SENSOR_TYPE_ID_ACCELEROMETER, callback: Callback<AccelerometerResponse>, options?: Options): void;
    /**
     * Subscribes to data changes of the uncalibrated acceleration sensor. If this API is called multiple times for the
     * same application, the last call takes effect.
     *
     * @permission ohos.permission.ACCELEROMETER
     * @param { SensorType.SENSOR_TYPE_ID_ACCELEROMETER_UNCALIBRATED } type - Type of the sensor to subscribe to, which is
     *     **SENSOR_TYPE_ID_ACCELEROMETER_UNCALIBRATED**.
     * @param { Callback<AccelerometerUncalibratedResponse> } callback - Callback used to return the uncalibrated
     *     acceleration sensor data. The reported data type in the callback is **AccelerometerUncalibratedResponse**.
     * @param { Options } options - List of optional parameters. This parameter is used to set the data reporting
     *     frequency. The default value is 200,000,000 ns.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.on(type: SensorId.ACCELEROMETER_UNCALIBRATED, callback: Callback<AccelerometerUncalibratedResponse>, options?: Options)
     */
    function on(type: SensorType.SENSOR_TYPE_ID_ACCELEROMETER_UNCALIBRATED, callback: Callback<AccelerometerUncalibratedResponse>, options?: Options): void;
    /**
     * Subscribes to data changes of the ambient light sensor. If this API is called multiple times for the same
     * application, the last call takes effect.
     *
     * @param { SensorType.SENSOR_TYPE_ID_AMBIENT_LIGHT } type - Type of the sensor to subscribe to, which is
     *     **SENSOR_TYPE_ID_AMBIENT_LIGHT**.
     * @param { Callback<LightResponse> } callback - Callback used to return the ambient light sensor data. The reported
     *     data type in the callback is **LightResponse**.
     * @param { Options } options - List of optional parameters. This parameter is used to set the data reporting
     *     frequency. The default value is 200,000,000 ns.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.on(type: SensorId.AMBIENT_LIGHT, callback: Callback<LightResponse>, options?: Options)
     */
    function on(type: SensorType.SENSOR_TYPE_ID_AMBIENT_LIGHT, callback: Callback<LightResponse>, options?: Options): void;
    /**
     * Subscribes to data changes of the ambient temperature sensor. If this API is called multiple times for the same
     * application, the last call takes effect.
     *
     * @param { SensorType.SENSOR_TYPE_ID_AMBIENT_TEMPERATURE } type - Type of the sensor to subscribe to, which is
     *     **SENSOR_TYPE_ID_AMBIENT_TEMPERATURE**.
     * @param { Callback<AmbientTemperatureResponse> } callback - Callback used to return the ambient temperature sensor
     *     data. The reported data type in the callback is **AmbientTemperatureResponse**.
     * @param { Options } options - List of optional parameters. This parameter is used to set the data reporting
     *     frequency. The default value is 200,000,000 ns.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.on(type: SensorId.AMBIENT_TEMPERATURE, callback: Callback<AmbientTemperatureResponse>, options?: Options)
     */
    function on(type: SensorType.SENSOR_TYPE_ID_AMBIENT_TEMPERATURE, callback: Callback<AmbientTemperatureResponse>, options?: Options): void;
    /**
     * Subscribes to data changes of the barometer sensor. If this API is called multiple times for the same application,
     * the last call takes effect.
     *
     * @param { SensorType.SENSOR_TYPE_ID_BAROMETER } type - Type of the sensor to subscribe to, which is
     *     **SENSOR_TYPE_ID_BAROMETER**.
     * @param { Callback<BarometerResponse> } callback - Callback used to return the barometer sensor data. The reported
     *     data type in the callback is **BarometerResponse**.
     * @param { Options } options - List of optional parameters. This parameter is used to set the data reporting
     *     frequency. The default value is 200,000,000 ns.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.on(type: SensorId.BAROMETER, callback: Callback<BarometerResponse>, options?: Options)
     */
    function on(type: SensorType.SENSOR_TYPE_ID_BAROMETER, callback: Callback<BarometerResponse>, options?: Options): void;
    /**
     * Subscribes to data changes of the gravity sensor. If this API is called multiple times for the same application,
     * the last call takes effect.
     *
     * @param { SensorType.SENSOR_TYPE_ID_GRAVITY } type - Type of the sensor to subscribe to, which is
     *     **SENSOR_TYPE_ID_GRAVITY**.
     * @param { Callback<GravityResponse> } callback - Callback used to return the gravity sensor data. The reported data
     *     type in the callback is **GravityResponse**.
     * @param { Options } options - List of optional parameters. This parameter is used to set the data reporting
     *     frequency. The default value is 200,000,000 ns.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.on(type: SensorId.GRAVITY, callback: Callback<GravityResponse>, options?: Options)
     */
    function on(type: SensorType.SENSOR_TYPE_ID_GRAVITY, callback: Callback<GravityResponse>, options?: Options): void;
    /**
     * Subscribes to data changes of the gyroscope sensor. If this API is called multiple times for the same application,
     * the last call takes effect.
     *
     * @permission ohos.permission.GYROSCOPE
     * @param { SensorType.SENSOR_TYPE_ID_GYROSCOPE } type - Type of the sensor to subscribe to, which is
     *     **SENSOR_TYPE_ID_GYROSCOPE**.
     * @param { Callback<GyroscopeResponse> } callback - Callback used to return the gyroscope sensor data. The reported
     *     data type in the callback is **GyroscopeResponse**.
     * @param { Options } options - List of optional parameters. This parameter is used to set the data reporting
     *     frequency. The default value is 200,000,000 ns.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.on(type: SensorId.GYROSCOPE, callback: Callback<GyroscopeResponse>, options?: Options)
     */
    function on(type: SensorType.SENSOR_TYPE_ID_GYROSCOPE, callback: Callback<GyroscopeResponse>, options?: Options): void;
    /**
     * Subscribes to data changes of the uncalibrated gyroscope sensor. If this API is called multiple times for the same
     * application, the last call takes effect.
     *
     * @permission ohos.permission.GYROSCOPE
     * @param { SensorType.SENSOR_TYPE_ID_GYROSCOPE_UNCALIBRATED } type - Type of the sensor to subscribe to, which is
     *     **SENSOR_TYPE_ID_GYROSCOPE_UNCALIBRATED**.
     * @param { Callback<GyroscopeUncalibratedResponse> } callback - Callback used to return the uncalibrated gyroscope
     *     sensor data. The reported data type in the callback is **GyroscopeUncalibratedResponse**.
     * @param { Options } options - List of optional parameters. This parameter is used to set the data reporting
     *     frequency. The default value is 200,000,000 ns.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.on(type: SensorId.GYROSCOPE_UNCALIBRATED, callback: Callback<GyroscopeUncalibratedResponse>, options?: Options)
     */
    function on(type: SensorType.SENSOR_TYPE_ID_GYROSCOPE_UNCALIBRATED, callback: Callback<GyroscopeUncalibratedResponse>, options?: Options): void;
    /**
     * Subscribes to data changes of the Hall effect sensor. If this API is called multiple times for the same application
     * , the last call takes effect.
     *
     * @param { SensorType.SENSOR_TYPE_ID_HALL } type - Type of the sensor to subscribe to, which is
     *     **SENSOR_TYPE_ID_HALL**.
     * @param { Callback<HallResponse> } callback - Callback used to return the Hall effect sensor data. The reported data
     *     type in the callback is **HallResponse**.
     * @param { Options } options - List of optional parameters. The default value is 200,000,000 ns. This parameter is
     *     used to set the data reporting frequency when Hall effect events are frequently triggered.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.on(type: SensorId.HALL, callback: Callback<HallResponse>, options?: Options)
     */
    function on(type: SensorType.SENSOR_TYPE_ID_HALL, callback: Callback<HallResponse>, options?: Options): void;
    /**
     * Subscribes to data changes of the heart rate sensor. If this API is called multiple times for the same application,
     * the last call takes effect.
     *
     * @permission ohos.permission.HEALTH_DATA
     * @param { SensorType.SENSOR_TYPE_ID_HEART_RATE } type - Type of the sensor to subscribe to, which is
     *     **SENSOR_TYPE_ID_HEART_RATE**.
     * @param { Callback<HeartRateResponse> } callback - Callback used to return the heart rate sensor data. The reported
     *     data type in the callback is **HeartRateResponse**.
     * @param { Options } options - List of optional parameters. This parameter is used to set the data reporting
     *     frequency. The default value is 200,000,000 ns.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.on(type: SensorId.HEART_RATE, callback: Callback<HeartRateResponse>, options?: Options)
     */
    function on(type: SensorType.SENSOR_TYPE_ID_HEART_RATE, callback: Callback<HeartRateResponse>, options?: Options): void;
    /**
     * Subscribes to data changes of the humidity sensor. If this API is called multiple times for the same application,
     * the last call takes effect.
     *
     * @param { SensorType.SENSOR_TYPE_ID_HUMIDITY } type - Type of the sensor to subscribe to, which is
     *     **SENSOR_TYPE_ID_HUMIDITY**.
     * @param { Callback<HumidityResponse> } callback - Callback used to return the humidity sensor data. The reported
     *     data type in the callback is **HumidityResponse**.
     * @param { Options } options - List of optional parameters. This parameter is used to set the data reporting
     *     frequency. The default value is 200,000,000 ns.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.on(type: SensorId.HUMIDITY, callback: Callback<HumidityResponse>, options?: Options)
     */
    function on(type: SensorType.SENSOR_TYPE_ID_HUMIDITY, callback: Callback<HumidityResponse>, options?: Options): void;
    /**
     * Subscribes to data changes of the linear acceleration sensor. If this API is called multiple times for the same
     * application, the last call takes effect.
     *
     * @permission ohos.permission.ACCELEROMETER
     * @param { SensorType.SENSOR_TYPE_ID_LINEAR_ACCELERATION } type - Type of the sensor to subscribe to, which is
     *     **SENSOR_TYPE_ID_LINEAR_ACCELERATION**.
     * @param { Callback<LinearAccelerometerResponse> } callback - Callback used to return the linear acceleration sensor
     *     data. The reported data type in the callback is **LinearAccelerometerResponse**.
     * @param { Options } options - List of optional parameters. This parameter is used to set the data reporting
     *     frequency. The default value is 200,000,000 ns.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.on(type: SensorId.LINEAR_ACCELEROMETER, callback: Callback<LinearAccelerometerResponse>, options?: Options)
     */
    function on(type: SensorType.SENSOR_TYPE_ID_LINEAR_ACCELERATION, callback: Callback<LinearAccelerometerResponse>, options?: Options): void;
    /**
     * Subscribes to data changes of the magnetic field sensor. If this API is called multiple times for the same
     * application, the last call takes effect.
     *
     * @param { SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD } type - Type of the sensor to subscribe to, which is
     *     **SENSOR_TYPE_ID_MAGNETIC_FIELD**.
     * @param { Callback<MagneticFieldResponse> } callback - Callback used to return the magnetic field sensor data. The
     *     reported data type in the callback is **MagneticFieldResponse**.
     * @param { Options } options - List of optional parameters. This parameter is used to set the data reporting
     *     frequency. The default value is 200,000,000 ns.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.on(type: SensorId.MAGNETIC_FIELD, callback: Callback<MagneticFieldResponse>, options?: Options)
     */
    function on(type: SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD, callback: Callback<MagneticFieldResponse>, options?: Options): void;
    /**
     * Subscribes to data changes of the uncalibrated magnetic field sensor. If this API is called multiple times for the
     * same application, the last call takes effect.
     *
     * @param { SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD_UNCALIBRATED } type - Type of the sensor to subscribe to, which
     *     is **SENSOR_TYPE_ID_MAGNETIC_FIELD_UNCALIBRATED**.
     * @param { Callback<MagneticFieldUncalibratedResponse> } callback - Callback used to return the uncalibrated magnetic
     *     field sensor data. The reported data type in the callback is **MagneticFieldUncalibratedResponse**.
     * @param { Options } options - List of optional parameters. This parameter is used to set the data reporting
     *     frequency. The default value is 200,000,000 ns.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.on(type: SensorId.MAGNETIC_FIELD_UNCALIBRATED, callback: Callback<MagneticFieldUncalibratedResponse>, options?: Options)
     */
    function on(type: SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD_UNCALIBRATED, callback: Callback<MagneticFieldUncalibratedResponse>, options?: Options): void;
    /**
     * Subscribes to data changes of the orientation sensor. If this API is called multiple times for the same application
     * , the last call takes effect.
     *
     * @param { SensorType.SENSOR_TYPE_ID_ORIENTATION } type - Type of the sensor to subscribe to, which is
     *     **SENSOR_TYPE_ID_ORIENTATION**.
     * @param { Callback<OrientationResponse> } callback - Callback used to return the orientation sensor data. The
     *     reported data type in the callback is **OrientationResponse**.
     * @param { Options } options - List of optional parameters. This parameter is used to set the data reporting
     *     frequency. The default value is 200,000,000 ns.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.on(type: SensorId.ORIENTATION, callback: Callback<OrientationResponse>, options?: Options)
     */
    function on(type: SensorType.SENSOR_TYPE_ID_ORIENTATION, callback: Callback<OrientationResponse>, options?: Options): void;
    /**
     * Subscribes to data changes of the pedometer sensor. If this API is called multiple times for the same application,
     * the last call takes effect.
     *
     * @permission ohos.permission.ACTIVITY_MOTION
     * @param { SensorType.SENSOR_TYPE_ID_PEDOMETER } type - Type of the sensor to subscribe to, which is
     *     **SENSOR_TYPE_ID_PEDOMETER**.
     * @param { Callback<PedometerResponse> } callback - Callback used to return the pedometer sensor data. The reported
     *     data type in the callback is **PedometerResponse**.
     * @param { Options } options - List of optional parameters. This parameter is used to set the data reporting
     *     frequency. The default value is 200,000,000 ns.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.on(type: SensorId.PEDOMETER, callback: Callback<PedometerResponse>, options?: Options)
     */
    function on(type: SensorType.SENSOR_TYPE_ID_PEDOMETER, callback: Callback<PedometerResponse>, options?: Options): void;
    /**
     * Subscribes to data changes of the pedometer detection sensor. If this API is called multiple times for the same
     * application, the last call takes effect.
     *
     * @permission ohos.permission.ACTIVITY_MOTION
     * @param { SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION } type - Type of the sensor to subscribe to, which is
     *     **SENSOR_TYPE_ID_PEDOMETER_DETECTION**.
     * @param { Callback<PedometerDetectionResponse> } callback - Callback used to return the pedometer detection sensor
     *     data. The reported data type in the callback is **PedometerDetectionResponse**.
     * @param { Options } options - List of optional parameters. This parameter is used to set the data reporting
     *     frequency. The default value is 200,000,000 ns.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.on(type: SensorId.PEDOMETER_DETECTION, callback: Callback<PedometerDetectionResponse>, options?: Options)
     */
    function on(type: SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION, callback: Callback<PedometerDetectionResponse>, options?: Options): void;
    /**
     * Subscribes to data changes of the proximity sensor. If this API is called multiple times for the same application,
     * the last call takes effect.
     *
     * @param { SensorType.SENSOR_TYPE_ID_PROXIMITY } type - Type of the sensor to subscribe to, which is
     *     **SENSOR_TYPE_ID_PROXIMITY**.
     * @param { Callback<ProximityResponse> } callback - Callback used to return the proximity sensor data. The reported
     *     data type in the callback is **ProximityResponse**.
     * @param { Options } options - List of optional parameters. The default value is 200,000,000 ns. This parameter is
     *     used to set the data reporting frequency when proximity sensor events are frequently triggered.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.on(type: SensorId.PROXIMITY, callback: Callback<ProximityResponse>, options?: Options)
     */
    function on(type: SensorType.SENSOR_TYPE_ID_PROXIMITY, callback: Callback<ProximityResponse>, options?: Options): void;
    /**
     * Subscribes to data changes of the rotation vector sensor. If this API is called multiple times for the same
     * application, the last call takes effect.
     *
     * @param { SensorType.SENSOR_TYPE_ID_ROTATION_VECTOR } type - Type of the sensor to subscribe to, which is
     *     **SENSOR_TYPE_ID_ROTATION_VECTOR**.
     * @param { Callback<RotationVectorResponse> } callback - Callback used to return the rotation vector sensor data. The
     *     reported data type in the callback is **RotationVectorResponse**.
     * @param { Options } options - List of optional parameters. This parameter is used to set the data reporting
     *     frequency. The default value is 200,000,000 ns.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.on(type: SensorId.ROTATION_VECTOR, callback: Callback<RotationVectorResponse>, options?: Options)
     */
    function on(type: SensorType.SENSOR_TYPE_ID_ROTATION_VECTOR, callback: Callback<RotationVectorResponse>, options?: Options): void;
    /**
     * Subscribes to data changes of the significant motion sensor. If this API is called multiple times for the same
     * application, the last call takes effect.
     *
     * @param { SensorType.SENSOR_TYPE_ID_SIGNIFICANT_MOTION } type - Type of the sensor to subscribe to, which is
     *     **SENSOR_TYPE_ID_SIGNIFICANT_MOTION**.
     * @param { Callback<SignificantMotionResponse> } callback - Callback used to return the significant motion sensor
     *     data. The reported data type in the callback is **SignificantMotionResponse**.
     * @param { Options } options - List of optional parameters. This parameter is used to set the data reporting
     *     frequency. The default value is 200,000,000 ns.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.on(type: SensorId.SIGNIFICANT_MOTION, callback: Callback<SignificantMotionResponse>, options?: Options)
     */
    function on(type: SensorType.SENSOR_TYPE_ID_SIGNIFICANT_MOTION, callback: Callback<SignificantMotionResponse>, options?: Options): void;
    /**
     * Subscribes to data changes of the wear detection sensor. If this API is called multiple times for the same
     * application, the last call takes effect.
     *
     * @param { SensorType.SENSOR_TYPE_ID_WEAR_DETECTION } type - Type of the sensor to subscribe to, which is
     *     **SENSOR_TYPE_ID_WEAR_DETECTION**.
     * @param { Callback<WearDetectionResponse> } callback - Callback used to return the wear detection sensor data. The
     *     reported data type in the callback is **WearDetectionResponse**.
     * @param { Options } options - List of optional parameters. This parameter is used to set the data reporting
     *     frequency. The default value is 200,000,000 ns.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.on(type: SensorId.WEAR_DETECTION, callback: Callback<WearDetectionResponse>, options?: Options)
     */
    function on(type: SensorType.SENSOR_TYPE_ID_WEAR_DETECTION, callback: Callback<WearDetectionResponse>, options?: Options): void;
    /**
     * Subscribes to only one data change of the acceleration sensor.
     *
     * @permission ohos.permission.ACCELEROMETER
     * @param { SensorType.SENSOR_TYPE_ID_ACCELEROMETER } type - Type of the sensor to subscribe to, which is
     *     **SENSOR_TYPE_ID_ACCELEROMETER**.
     * @param { Callback<AccelerometerResponse> } callback - One-shot callback used to return the acceleration sensor
     *     data. The reported data type in the callback is **AccelerometerResponse**.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.once(type: SensorId.ACCELEROMETER, callback: Callback<AccelerometerResponse>)
     */
    function once(type: SensorType.SENSOR_TYPE_ID_ACCELEROMETER, callback: Callback<AccelerometerResponse>): void;
    /**
     * Subscribes to only one data change of the uncalibrated acceleration sensor.
     *
     * @permission ohos.permission.ACCELEROMETER
     * @param { SensorType.SENSOR_TYPE_ID_ACCELEROMETER_UNCALIBRATED } type - Type of the sensor to subscribe to, which is
     *     **SENSOR_TYPE_ID_ACCELEROMETER_UNCALIBRATED**.
     * @param { Callback<AccelerometerUncalibratedResponse> } callback - One-shot callback used to return the uncalibrated
     *     acceleration sensor data. The reported data type in the callback is **AccelerometerUncalibratedResponse**.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.once(type: SensorId.ACCELEROMETER_UNCALIBRATED, callback: Callback<AccelerometerUncalibratedResponse>)
     */
    function once(type: SensorType.SENSOR_TYPE_ID_ACCELEROMETER_UNCALIBRATED, callback: Callback<AccelerometerUncalibratedResponse>): void;
    /**
     * Subscribes to only one data change of the ambient light sensor.
     *
     * @param { SensorType.SENSOR_TYPE_ID_AMBIENT_LIGHT } type - Type of the sensor to subscribe to, which is
     *     **SENSOR_TYPE_ID_AMBIENT_LIGHT**.
     * @param { Callback<LightResponse> } callback - One-shot callback used to return the ambient light sensor data. The
     *     reported data type in the callback is **LightResponse**.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.once(type: SensorId.AMBIENT_LIGHT, callback: Callback<LightResponse>)
     */
    function once(type: SensorType.SENSOR_TYPE_ID_AMBIENT_LIGHT, callback: Callback<LightResponse>): void;
    /**
     * Subscribes to only one data change of the ambient temperature sensor.
     *
     * @param { SensorType.SENSOR_TYPE_ID_AMBIENT_TEMPERATURE } type - Type of the sensor to subscribe to, which is
     *     **SENSOR_TYPE_ID_AMBIENT_TEMPERATURE**.
     * @param { Callback<AmbientTemperatureResponse> } callback - One-shot callback used to return the ambient temperature
     *     sensor data. The reported data type in the callback is **AmbientTemperatureResponse**.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.once(type: SensorId.AMBIENT_TEMPERATURE, callback: Callback<AmbientTemperatureResponse>)
     */
    function once(type: SensorType.SENSOR_TYPE_ID_AMBIENT_TEMPERATURE, callback: Callback<AmbientTemperatureResponse>): void;
    /**
     * Subscribes to only one data change of the barometer sensor.
     *
     * @param { SensorType.SENSOR_TYPE_ID_BAROMETER } type - Type of the sensor to subscribe to, which is
     *     **SENSOR_TYPE_ID_BAROMETER**.
     * @param { Callback<BarometerResponse> } callback - One-shot callback used to return the barometer sensor data. The
     *     reported data type in the callback is **BarometerResponse**.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.once(type: SensorId.BAROMETER, callback: Callback<BarometerResponse>)
     */
    function once(type: SensorType.SENSOR_TYPE_ID_BAROMETER, callback: Callback<BarometerResponse>): void;
    /**
     * Subscribes to only one data change of the gravity sensor.
     *
     * @param { SensorType.SENSOR_TYPE_ID_GRAVITY } type - Type of the sensor to subscribe to, which is
     *     **SENSOR_TYPE_ID_GRAVITY**.
     * @param { Callback<GravityResponse> } callback - One-shot callback used to return the gravity sensor data. The
     *     reported data type in the callback is **GravityResponse**.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.once(type: SensorId.GRAVITY, callback: Callback<GravityResponse>)
     */
    function once(type: SensorType.SENSOR_TYPE_ID_GRAVITY, callback: Callback<GravityResponse>): void;
    /**
     * Subscribes to only one data change of the gyroscope sensor.
     *
     * @permission ohos.permission.GYROSCOPE
     * @param { SensorType.SENSOR_TYPE_ID_GYROSCOPE } type - Type of the sensor to subscribe to, which is
     *     **SENSOR_TYPE_ID_GYROSCOPE**.
     * @param { Callback<GyroscopeResponse> } callback - One-shot callback used to return the gyroscope sensor data. The
     *     reported data type in the callback is **GyroscopeResponse**.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.once(type: SensorId.GYROSCOPE, callback: Callback<GyroscopeResponse>)
     */
    function once(type: SensorType.SENSOR_TYPE_ID_GYROSCOPE, callback: Callback<GyroscopeResponse>): void;
    /**
     * Subscribes to only one data change of the uncalibrated gyroscope sensor.
     *
     * @permission ohos.permission.GYROSCOPE
     * @param { SensorType.SENSOR_TYPE_ID_GYROSCOPE_UNCALIBRATED } type - Type of the sensor to subscribe to, which is
     *     **SENSOR_TYPE_ID_GYROSCOPE_UNCALIBRATED**.
     * @param { Callback<GyroscopeUncalibratedResponse> } callback - One-shot callback used to return the uncalibrated
     *     gyroscope sensor data. The reported data type in the callback is **GyroscopeUncalibratedResponse**.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.once(type: SensorId.GYROSCOPE_UNCALIBRATED, callback: Callback<GyroscopeUncalibratedResponse>)
     */
    function once(type: SensorType.SENSOR_TYPE_ID_GYROSCOPE_UNCALIBRATED, callback: Callback<GyroscopeUncalibratedResponse>): void;
    /**
     * Subscribes to only one data change of the Hall effect sensor.
     *
     * @param { SensorType.SENSOR_TYPE_ID_HALL } type - Type of the sensor to subscribe to, which is
     *     **SENSOR_TYPE_ID_HALL**.
     * @param { Callback<HallResponse> } callback - One-shot callback used to return the Hall effect sensor data. The
     *     reported data type in the callback is **HallResponse**.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.once(type: SensorId.HALL, callback: Callback<HallResponse>)
     */
    function once(type: SensorType.SENSOR_TYPE_ID_HALL, callback: Callback<HallResponse>): void;
    /**
     * Subscribes to only one data change of the heart rate sensor.
     *
     * @permission ohos.permission.HEART_RATE
     * @param { SensorType.SENSOR_TYPE_ID_HEART_RATE } type - Type of the sensor to subscribe to, which is
     *     **SENSOR_TYPE_ID_HEART_RATE**.
     * @param { Callback<HeartRateResponse> } callback - One-shot callback used to return the heart rate sensor data. The
     *     reported data type in the callback is **HeartRateResponse**.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.once(type: SensorId.HEART_RATE, callback: Callback<HeartRateResponse>)
     */
    function once(type: SensorType.SENSOR_TYPE_ID_HEART_RATE, callback: Callback<HeartRateResponse>): void;
    /**
     * Subscribes to only one data change of the humidity sensor.
     *
     * @param { SensorType.SENSOR_TYPE_ID_HUMIDITY } type - Type of the sensor to subscribe to, which is
     *     **SENSOR_TYPE_ID_HUMIDITY**.
     * @param { Callback<HumidityResponse> } callback - One-shot callback used to return the humidity sensor data. The
     *     reported data type in the callback is **HumidityResponse**.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.once(type: SensorId.HUMIDITY, callback: Callback<HumidityResponse>)
     */
    function once(type: SensorType.SENSOR_TYPE_ID_HUMIDITY, callback: Callback<HumidityResponse>): void;
    /**
     * Subscribes to only one data change of the linear acceleration sensor.
     *
     * @permission ohos.permission.ACCELEROMETER
     * @param { SensorType.SENSOR_TYPE_ID_LINEAR_ACCELERATION } type - Type of the sensor to subscribe to, which is
     *     **SENSOR_TYPE_ID_LINEAR_ACCELERATION**.
     * @param { Callback<LinearAccelerometerResponse> } callback - One-shot callback used to return the linear
     *     acceleration sensor data. The reported data type in the callback is **LinearAccelerometerResponse**.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.once(type: SensorId.LINEAR_ACCELEROMETER, callback: Callback<LinearAccelerometerResponse>)
     */
    function once(type: SensorType.SENSOR_TYPE_ID_LINEAR_ACCELERATION, callback: Callback<LinearAccelerometerResponse>): void;
    /**
     * Subscribes to only one data change of the magnetic field sensor.
     *
     * @param { SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD } type - Type of the sensor to subscribe to, which is
     *     **SENSOR_TYPE_ID_MAGNETIC_FIELD**.
     * @param { Callback<MagneticFieldResponse> } callback - One-shot callback used to return the magnetic field sensor
     *     data. The reported data type in the callback is **MagneticFieldResponse**.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.once(type: SensorId.MAGNETIC_FIELD, callback: Callback<MagneticFieldResponse>)
     */
    function once(type: SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD, callback: Callback<MagneticFieldResponse>): void;
    /**
     * Subscribes to only one data change of the uncalibrated magnetic field sensor.
     *
     * @param { SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD_UNCALIBRATED } type - Type of the sensor to subscribe to, which
     *     is **SENSOR_TYPE_ID_MAGNETIC_FIELD_UNCALIBRATED**.
     * @param { Callback<MagneticFieldUncalibratedResponse> } callback - One-shot callback used to return the uncalibrated
     *     magnetic field sensor data. The reported data type in the callback is **MagneticFieldUncalibratedResponse**.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.once(type: SensorId.MAGNETIC_FIELD_UNCALIBRATED, callback: Callback<MagneticFieldUncalibratedResponse>)
     */
    function once(type: SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD_UNCALIBRATED, callback: Callback<MagneticFieldUncalibratedResponse>): void;
    /**
     * Subscribes to only one data change of the orientation sensor.
     *
     * @param { SensorType.SENSOR_TYPE_ID_ORIENTATION } type - Type of the sensor to subscribe to, which is
     *     **SENSOR_TYPE_ID_ORIENTATION**.
     * @param { Callback<OrientationResponse> } callback - One-shot callback used to return the orientation sensor data.
     *     The reported data type in the callback is **OrientationResponse**.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.once(type: SensorId.ORIENTATION, callback: Callback<OrientationResponse>)
     */
    function once(type: SensorType.SENSOR_TYPE_ID_ORIENTATION, callback: Callback<OrientationResponse>): void;
    /**
     * Subscribes to only one data change of the pedometer sensor.
     *
     * @permission ohos.permission.ACTIVITY_MOTION
     * @param { SensorType.SENSOR_TYPE_ID_PEDOMETER } type - Type of the sensor to subscribe to, which is
     *     **SENSOR_TYPE_ID_PEDOMETER**.
     * @param { Callback<PedometerResponse> } callback - One-shot callback used to return the pedometer sensor data. The
     *     reported data type in the callback is **PedometerResponse**.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.once(type: SensorId.PEDOMETER, callback: Callback<PedometerResponse>)
     */
    function once(type: SensorType.SENSOR_TYPE_ID_PEDOMETER, callback: Callback<PedometerResponse>): void;
    /**
     * Subscribes to only one data change of the pedometer detection sensor.
     *
     * @permission ohos.permission.ACTIVITY_MOTION
     * @param { SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION } type - Type of the sensor to subscribe to, which is
     *     **SENSOR_TYPE_ID_PEDOMETER_DETECTION**.
     * @param { Callback<PedometerDetectionResponse> } callback - One-shot callback used to return the pedometer detection
     *     sensor data. The reported data type in the callback is **PedometerDetectionResponse**.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.once(type: SensorId.PEDOMETER_DETECTION, callback: Callback<PedometerDetectionResponse>)
     */
    function once(type: SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION, callback: Callback<PedometerDetectionResponse>): void;
    /**
     * Subscribes to only one data change of the proximity sensor.
     *
     * @param { SensorType.SENSOR_TYPE_ID_PROXIMITY } type - Type of the sensor to subscribe to, which is
     *     **SENSOR_TYPE_ID_PROXIMITY**.
     * @param { Callback<ProximityResponse> } callback - One-shot callback used to return the proximity sensor data. The
     *     reported data type in the callback is **ProximityResponse**.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.once(type: SensorId.PROXIMITY, callback: Callback<ProximityResponse>)
     */
    function once(type: SensorType.SENSOR_TYPE_ID_PROXIMITY, callback: Callback<ProximityResponse>): void;
    /**
     * Subscribes to only one data change of the rotation vector sensor.
     *
     * @param { SensorType.SENSOR_TYPE_ID_ROTATION_VECTOR } type - Type of the sensor to subscribe to, which is
     *     **SENSOR_TYPE_ID_ROTATION_VECTOR**.
     * @param { Callback<RotationVectorResponse> } callback - One-shot callback used to return the rotation vector sensor
     *     data. The reported data type in the callback is **RotationVectorResponse**.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.once(type: SensorId.ROTATION_VECTOR, callback: Callback<RotationVectorResponse>)
     */
    function once(type: SensorType.SENSOR_TYPE_ID_ROTATION_VECTOR, callback: Callback<RotationVectorResponse>): void;
    /**
     * Subscribes to only one data change of the significant motion sensor.
     *
     * @param { SensorType.SENSOR_TYPE_ID_SIGNIFICANT_MOTION } type - Type of the sensor to subscribe to, which is
     *     **SENSOR_TYPE_ID_SIGNIFICANT_MOTION**.
     * @param { Callback<SignificantMotionResponse> } callback - One-shot callback used to return the significant motion
     *     sensor data. The reported data type in the callback is **SignificantMotionResponse**.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.once(type: SensorId.SIGNIFICANT_MOTION, callback: Callback<SignificantMotionResponse>)
     */
    function once(type: SensorType.SENSOR_TYPE_ID_SIGNIFICANT_MOTION, callback: Callback<SignificantMotionResponse>): void;
    /**
     * Subscribes to only one data change of the wear detection sensor.
     *
     * @param { SensorType.SENSOR_TYPE_ID_WEAR_DETECTION } type - Type of the sensor to subscribe to, which is
     *     **SENSOR_TYPE_ID_WEAR_DETECTION**.
     * @param { Callback<WearDetectionResponse> } callback - One-shot callback used to return the wear detection sensor
     *     data. The reported data type in the callback is **WearDetectionResponse**.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.once(type: SensorId.WEAR_DETECTION, callback: Callback<WearDetectionResponse>)
     */
    function once(type: SensorType.SENSOR_TYPE_ID_WEAR_DETECTION, callback: Callback<WearDetectionResponse>): void;
    /**
     * Unsubscribes from sensor data changes.
     *
     * @permission ohos.permission.ACCELEROMETER
     * @param { SensorType.SENSOR_TYPE_ID_ACCELEROMETER } type - Type of the sensor to unsubscribe from, which is
     *     **SENSOR_TYPE_ID_ACCELEROMETER**.
     * @param { Callback<AccelerometerResponse> } callback - Callback used for unsubscription. If this parameter is not
     *     specified, all callbacks of the specified sensor type are unsubscribed from.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.off(type: SensorId.ACCELEROMETER, callback?: Callback<AccelerometerResponse>)
     */
    function off(type: SensorType.SENSOR_TYPE_ID_ACCELEROMETER, callback?: Callback<AccelerometerResponse>): void;
    /**
     * Unsubscribes from sensor data changes.
     *
     * @permission ohos.permission.ACCELEROMETER
     * @param { SensorType.SENSOR_TYPE_ID_ACCELEROMETER_UNCALIBRATED } type - Type of the sensor to unsubscribe from,
     *     which is **SENSOR_TYPE_ID_ACCELEROMETER_UNCALIBRATED**.
     * @param { Callback<AccelerometerUncalibratedResponse> } callback - Callback used for unsubscription. If this
     *     parameter is not specified, all callbacks of the specified sensor type are unsubscribed from.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.off(type: SensorId.ACCELEROMETER_UNCALIBRATED, callback?: Callback<AccelerometerUncalibratedResponse>)
     */
    function off(type: SensorType.SENSOR_TYPE_ID_ACCELEROMETER_UNCALIBRATED, callback?: Callback<AccelerometerUncalibratedResponse>): void;
    /**
     * Unsubscribes from sensor data changes.
     *
     * @param { SensorType.SENSOR_TYPE_ID_AMBIENT_LIGHT } type - Type of the sensor to unsubscribe from, which is
     *     **SENSOR_TYPE_ID_AMBIENT_LIGHT**.
     * @param { Callback<LightResponse> } callback - Callback used for unsubscription. If this parameter is not specified,
     *     all callbacks of the specified sensor type are unsubscribed from.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.off(type: SensorId.AMBIENT_LIGHT, callback?: Callback<LightResponse>)
     */
    function off(type: SensorType.SENSOR_TYPE_ID_AMBIENT_LIGHT, callback?: Callback<LightResponse>): void;
    /**
     * Unsubscribes from sensor data changes.
     *
     * @param { SensorType.SENSOR_TYPE_ID_AMBIENT_TEMPERATURE } type - Type of the sensor to unsubscribe from, which is
     *     **SENSOR_TYPE_ID_AMBIENT_TEMPERATURE**.
     * @param { Callback<AmbientTemperatureResponse> } callback - Callback used for unsubscription. If this parameter is
     *     not specified, all callbacks of the specified sensor type are unsubscribed from.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.off(type: SensorId.AMBIENT_TEMPERATURE, callback?: Callback<AmbientTemperatureResponse>)
     */
    function off(type: SensorType.SENSOR_TYPE_ID_AMBIENT_TEMPERATURE, callback?: Callback<AmbientTemperatureResponse>): void;
    /**
     * Unsubscribes from sensor data changes.
     *
     * @param { SensorType.SENSOR_TYPE_ID_BAROMETER } type - Type of the sensor to unsubscribe from, which is
     *     **SENSOR_TYPE_ID_BAROMETER**.
     * @param { Callback<BarometerResponse> } callback - Callback used for unsubscription. If this parameter is not
     *     specified, all callbacks of the specified sensor type are unsubscribed from.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.off(type: SensorId.BAROMETER, callback?: Callback<BarometerResponse>)
     */
    function off(type: SensorType.SENSOR_TYPE_ID_BAROMETER, callback?: Callback<BarometerResponse>): void;
    /**
     * Unsubscribes from sensor data changes.
     *
     * @param { SensorType.SENSOR_TYPE_ID_GRAVITY } type - Type of the sensor to unsubscribe from, which is
     *     **SENSOR_TYPE_ID_GRAVITY**.
     * @param { Callback<GravityResponse> } callback - Callback used for unsubscription. If this parameter is not
     *     specified, all callbacks of the specified sensor type are unsubscribed from.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.off(type: SensorId.GRAVITY, callback?: Callback<GravityResponse>)
     */
    function off(type: SensorType.SENSOR_TYPE_ID_GRAVITY, callback?: Callback<GravityResponse>): void;
    /**
     * Unsubscribes from sensor data changes.
     *
     * @permission ohos.permission.GYROSCOPE
     * @param { SensorType.SENSOR_TYPE_ID_GYROSCOPE } type - Type of the sensor to unsubscribe from, which is
     *     **SENSOR_TYPE_ID_GYROSCOPE**.
     * @param { Callback<GyroscopeResponse> } callback - Callback used for unsubscription. If this parameter is not
     *     specified, all callbacks of the specified sensor type are unsubscribed from.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.off(type: SensorId.GYROSCOPE, callback?: Callback<GyroscopeResponse>)
     */
    function off(type: SensorType.SENSOR_TYPE_ID_GYROSCOPE, callback?: Callback<GyroscopeResponse>): void;
    /**
     * Unsubscribes from sensor data changes.
     *
     * @permission ohos.permission.GYROSCOPE
     * @param { SensorType.SENSOR_TYPE_ID_GYROSCOPE_UNCALIBRATED } type - Type of the sensor to unsubscribe from, which is
     *     **SENSOR_TYPE_ID_GYROSCOPE_UNCALIBRATED**.
     * @param { Callback<GyroscopeUncalibratedResponse> } callback - Callback used for unsubscription. If this parameter
     *     is not specified, all callbacks of the specified sensor type are unsubscribed from.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.off(type: SensorId.GYROSCOPE_UNCALIBRATED, callback?: Callback<GyroscopeUncalibratedResponse>)
     */
    function off(type: SensorType.SENSOR_TYPE_ID_GYROSCOPE_UNCALIBRATED, callback?: Callback<GyroscopeUncalibratedResponse>): void;
    /**
     * Unsubscribes from sensor data changes.
     *
     * @param { SensorType.SENSOR_TYPE_ID_HALL } type - Type of the sensor to unsubscribe from, which is
     *     **SENSOR_TYPE_ID_HALL**.
     * @param { Callback<HallResponse> } callback - Callback used for unsubscription. If this parameter is not specified,
     *     all callbacks of the specified sensor type are unsubscribed from.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.off(type: SensorId.HALL, callback?: Callback<HallResponse>)
     */
    function off(type: SensorType.SENSOR_TYPE_ID_HALL, callback?: Callback<HallResponse>): void;
    /**
     * Unsubscribes from sensor data changes.
     *
     * @permission ohos.permission.HEALTH_DATA
     * @param { SensorType.SENSOR_TYPE_ID_HEART_RATE } type - Type of the sensor to unsubscribe from, which is
     *     **SENSOR_TYPE_ID_HEART_RATE**.
     * @param { Callback<HeartRateResponse> } callback - Callback used for unsubscription. If this parameter is not
     *     specified, all callbacks of the specified sensor type are unsubscribed from.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.off(type: SensorId.HEART_RATE, callback?: Callback<HeartRateResponse>)
     */
    function off(type: SensorType.SENSOR_TYPE_ID_HEART_RATE, callback?: Callback<HeartRateResponse>): void;
    /**
     * Unsubscribes from sensor data changes.
     *
     * @param { SensorType.SENSOR_TYPE_ID_HUMIDITY } type - Type of the sensor to unsubscribe from, which is
     *     **SENSOR_TYPE_ID_HUMIDITY**.
     * @param { Callback<HumidityResponse> } callback - Callback used for unsubscription. If this parameter is not
     *     specified, all callbacks of the specified sensor type are unsubscribed from.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.off(type: SensorId.HUMIDITY, callback?: Callback<HumidityResponse>)
     */
    function off(type: SensorType.SENSOR_TYPE_ID_HUMIDITY, callback?: Callback<HumidityResponse>): void;
    /**
     * Unsubscribes from sensor data changes.
     *
     * @permission ohos.permission.ACCELEROMETER
     * @param { SensorType.SENSOR_TYPE_ID_LINEAR_ACCELERATION } type - Type of the sensor to unsubscribe from, which is
     *     **SENSOR_TYPE_ID_LINEAR_ACCELERATION**.
     * @param { Callback<LinearAccelerometerResponse> } callback - Callback used for unsubscription. If this parameter is
     *     not specified, all callbacks of the specified sensor type are unsubscribed from.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.off(type: SensorId.LINEAR_ACCELEROMETER, callback?: Callback<LinearAccelerometerResponse>)
     */
    function off(type: SensorType.SENSOR_TYPE_ID_LINEAR_ACCELERATION, callback?: Callback<LinearAccelerometerResponse>): void;
    /**
     * Unsubscribes from sensor data changes.
     *
     * @param { SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD } type - Type of the sensor to unsubscribe from, which is
     *     **SENSOR_TYPE_ID_MAGNETIC_FIELD**.
     * @param { Callback<MagneticFieldResponse> } callback - Callback used for unsubscription. If this parameter is not
     *     specified, all callbacks of the specified sensor type are unsubscribed from.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.off(type: SensorId.MAGNETIC_FIELD, callback?: Callback<MagneticFieldResponse>)
     */
    function off(type: SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD, callback?: Callback<MagneticFieldResponse>): void;
    /**
     * Unsubscribes from sensor data changes.
     *
     * @param { SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD_UNCALIBRATED } type - Type of the sensor to unsubscribe from,
     *     which is **SENSOR_TYPE_ID_MAGNETIC_FIELD_UNCALIBRATED**.
     * @param { Callback<MagneticFieldUncalibratedResponse> } callback - Callback used for unsubscription. If this
     *     parameter is not specified, all callbacks of the specified sensor type are unsubscribed from.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.off(type: SensorId.MAGNETIC_FIELD_UNCALIBRATED, callback?: Callback<MagneticFieldUncalibratedResponse>)
     */
    function off(type: SensorType.SENSOR_TYPE_ID_MAGNETIC_FIELD_UNCALIBRATED, callback?: Callback<MagneticFieldUncalibratedResponse>): void;
    /**
     * Unsubscribes from sensor data changes.
     *
     * @param { SensorType.SENSOR_TYPE_ID_ORIENTATION } type - Type of the sensor to unsubscribe from, which is
     *     **SENSOR_TYPE_ID_ORIENTATION**.
     * @param { Callback<OrientationResponse> } callback - Callback used for unsubscription. If this parameter is not
     *     specified, all callbacks of the specified sensor type are unsubscribed from.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.off(type: SensorId.ORIENTATION, callback?: Callback<OrientationResponse>)
     */
    function off(type: SensorType.SENSOR_TYPE_ID_ORIENTATION, callback?: Callback<OrientationResponse>): void;
    /**
     * Unsubscribes from sensor data changes.
     *
     * @permission ohos.permission.ACTIVITY_MOTION
     * @param { SensorType.SENSOR_TYPE_ID_PEDOMETER } type - Type of the sensor to unsubscribe from, which is
     *     **SENSOR_TYPE_ID_PEDOMETER**.
     * @param { Callback<PedometerResponse> } callback - Callback used for unsubscription. If this parameter is not
     *     specified, all callbacks of the specified sensor type are unsubscribed from.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.off(type: SensorId.PEDOMETER, callback?: Callback<PedometerResponse>)
     */
    function off(type: SensorType.SENSOR_TYPE_ID_PEDOMETER, callback?: Callback<PedometerResponse>): void;
    /**
     * Unsubscribes from sensor data changes.
     *
     * @permission ohos.permission.ACTIVITY_MOTION
     * @param { SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION } type - Type of the sensor to unsubscribe from, which is
     *     **SENSOR_TYPE_ID_PEDOMETER_DETECTION**.
     * @param { Callback<PedometerDetectionResponse> } callback - Callback used for unsubscription. If this parameter is
     *     not specified, all callbacks of the specified sensor type are unsubscribed from.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.off(type: SensorId.PEDOMETER_DETECTION, callback?: Callback<PedometerDetectionResponse>)
     */
    function off(type: SensorType.SENSOR_TYPE_ID_PEDOMETER_DETECTION, callback?: Callback<PedometerDetectionResponse>): void;
    /**
     * Unsubscribes from sensor data changes.
     *
     * @param { SensorType.SENSOR_TYPE_ID_PROXIMITY } type - Type of the sensor to unsubscribe from, which is
     *     **SENSOR_TYPE_ID_PROXIMITY**.
     * @param { Callback<ProximityResponse> } callback - Callback used for unsubscription. If this parameter is not
     *     specified, all callbacks of the specified sensor type are unsubscribed from.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.off(type: SensorId.PROXIMITY, callback?: Callback<ProximityResponse>)
     */
    function off(type: SensorType.SENSOR_TYPE_ID_PROXIMITY, callback?: Callback<ProximityResponse>): void;
    /**
     * Unsubscribes from sensor data changes.
     *
     * @param { SensorType.SENSOR_TYPE_ID_ROTATION_VECTOR } type - Type of the sensor to unsubscribe from, which is
     *     **SENSOR_TYPE_ID_ROTATION_VECTOR**.
     * @param { Callback<RotationVectorResponse> } callback - Callback used for unsubscription. If this parameter is not
     *     specified, all callbacks of the specified sensor type are unsubscribed from.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.off(type: SensorId.ROTATION_VECTOR, callback?: Callback<RotationVectorResponse>)
     */
    function off(type: SensorType.SENSOR_TYPE_ID_ROTATION_VECTOR, callback?: Callback<RotationVectorResponse>): void;
    /**
     * Unsubscribes from valid motion sensor data.
     *
     * @param { SensorType.SENSOR_TYPE_ID_SIGNIFICANT_MOTION } type - Type of the sensor to unsubscribe from, which is
     *     **SENSOR_TYPE_ID_SIGNIFICANT_MOTION**.
     * @param { Callback<SignificantMotionResponse> } callback - Callback used for unsubscription. If this parameter is
     *     not specified, all callbacks of the specified sensor type are unsubscribed from.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.off(type: SensorId.SIGNIFICANT_MOTION, callback?: Callback<SignificantMotionResponse>)
     */
    function off(type: SensorType.SENSOR_TYPE_ID_SIGNIFICANT_MOTION, callback?: Callback<SignificantMotionResponse>): void;
    /**
     * Unsubscribes from sensor data changes.
     *
     * @param { SensorType.SENSOR_TYPE_ID_WEAR_DETECTION } type - Type of the sensor to unsubscribe from, which is
     *     **SENSOR_TYPE_ID_WEAR_DETECTION**.
     * @param { Callback<WearDetectionResponse> } callback - Callback used for unsubscription. If this parameter is not
     *     specified, all callbacks of the specified sensor type are unsubscribed from.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.off(type: SensorId.WEAR_DETECTION, callback?: Callback<WearDetectionResponse>)
     */
    function off(type: SensorType.SENSOR_TYPE_ID_WEAR_DETECTION, callback?: Callback<WearDetectionResponse>): void;
    /**
     * Describes the sensor information.
     *
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    interface Sensor {
        /**
         * Sensor name.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 9
         */
        sensorName: string;
        /**
         * Vendor of the sensor.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 9
         */
        vendorName: string;
        /**
         * Firmware version of the sensor.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 9
         */
        firmwareVersion: string;
        /**
         * Hardware version of the sensor.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 9
         */
        hardwareVersion: string;
        /**
         * Sensor type ID.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 9
         */
        sensorId: number;
        /**
         * Maximum measurement range of the sensor.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 9
         */
        maxRange: number;
        /**
         * Minimum sampling period.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 9
         */
        minSamplePeriod: number;
        /**
         * Maximum sampling period.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 9
         */
        maxSamplePeriod: number;
        /**
         * Precision of the sensor.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 9
         */
        precision: number;
        /**
         * Estimated sensor power, in mA.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 9
         */
        power: number;
        /**
         * Sensor index.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 19
         */
        sensorIndex?: number;
        /**
         * Device ID.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 19
         */
        deviceId?: number;
        /**
         * Device name.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 19
         */
        deviceName?: string;
        /**
         * Whether the sensor is a local sensor. The value **true** indicates a local sensor, and the value **false**
         * indicates the opposite.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 19
         */
        isLocalSensor?: boolean;
        /**
         * Whether the sensor is a mock sensor. The value **true** indicates a mock sensor, and the value **false**
         * indicates the opposite.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 23
         */
        isMockSensor?: boolean;
    }
    /**
     * Obtains information about the sensor of a specific type. This API uses an asynchronous callback to return the
     * result.
     *
     * @param { SensorId } type - Sensor type.
     * @param { AsyncCallback<Sensor> } callback - Callback used to return the sensor information.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @throws { BusinessError } 14500102 - The sensor is not supported by the device. [since 12]
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function getSingleSensor(type: SensorId, callback: AsyncCallback<Sensor>): void;
    /**
     * Obtains information about the sensor of a specific type. This API uses a promise to return the result.
     *
     * @param { SensorId } type - Sensor type.
     * @returns { Promise<Sensor> } Promise used to return the sensor information.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @throws { BusinessError } 14500102 - The sensor is not supported by the device. [since 12]
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function getSingleSensor(type: SensorId): Promise<Sensor>;
    /**
     * Obtains information about the sensor of a specific type. This API returns the result synchronously.
     *
     * @param { SensorId } type - Sensor type.
     * @returns { Sensor } Sensor information.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @throws { BusinessError } 14500102 - The sensor is not supported by the device.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 12
     */
    function getSingleSensorSync(type: SensorId): Sensor;
    /**
     * Obtains information about the sensor of a specific type.
     *
     * @param { SensorId } type - Sensor type.
     * @param { number } [deviceId] - Device ID. The default value is **-1**, indicating the local device. You can use
     *     [getSensorList]{@link sensor.getSensorList(callback: AsyncCallback<Array<Sensor>>)} or
     *     [sensorStatusChange]{@link sensor.on(type: 'sensorStatusChange', callback: Callback<SensorStatusEvent>)} to
     *     obtain the device ID.
     * @returns { Array<Sensor> } Sensor attribute list.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 19
     */
    function getSingleSensorByDeviceSync(type: SensorId, deviceId?: number): Array<Sensor>;
    /**
     * Obtains information about all sensors on the device. This API uses an asynchronous callback to return the result.
     *
     * @param { AsyncCallback<Array<Sensor>> } callback - Callback used to return the sensor list.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function getSensorList(callback: AsyncCallback<Array<Sensor>>): void;
    /**
     * Obtains information about all sensors on the device. This API uses a promise to return the result.
     *
     * @returns { Promise<Array<Sensor>> } Promise used to return the sensor list.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function getSensorList(): Promise<Array<Sensor>>;
    /**
     * Obtains information about all sensors on the device. This API returns the result synchronously.
     *
     * @returns { Array<Sensor> } List of sensor attributes.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 12
     */
    function getSensorListSync(): Array<Sensor>;
    /**
     * Obtains the information about all sensors on the device.
     *
     * @param { number } [deviceId] - Device ID. The default value is **-1**, indicating the local device. You can use
     *     [getSensorList]{@link sensor.getSensorList(callback: AsyncCallback<Array<Sensor>>)} or
     *     [sensorStatusChange]{@link sensor.on(type: 'sensorStatusChange', callback: Callback<SensorStatusEvent>)} to
     *     obtain the device ID.
     * @returns { Array<Sensor> } Sensor attribute list.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 19
     */
    function getSensorListByDeviceSync(deviceId?: number): Array<Sensor>;
    /**
     * Describes a geomagnetic response object.
     *
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     */
    interface GeomagneticResponse {
        /**
         * North component of the geomagnetic field, in nT.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        x: number;
        /**
         * East component of the geomagnetic field, in nT.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        y: number;
        /**
         * Vertical component of the geomagnetic field, in nT.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        z: number;
        /**
         * Magnetic dip, also called magnetic inclination, which is the angle measured from the horizontal plane to the
         * magnetic field vector, in degrees.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        geomagneticDip: number;
        /**
         * Magnetic declination, which is the angle between true north (geographic north) and the magnetic north (the
         * horizontal component of the field), in degrees.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        deflectionAngle: number;
        /**
         * Horizontal intensity of the magnetic field vector field, in nT.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        levelIntensity: number;
        /**
         * Total intensity of the magnetic field vector, in nT.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        totalIntensity: number;
    }
    /**
     * Describes the geographical location.
     *
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     */
    interface LocationOptions {
        /**
         * Latitude, in degrees.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        latitude: number;
        /**
         * Longitude, in degrees.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        longitude: number;
        /**
         * Altitude, in m.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        altitude: number;
    }
    /**
     * Obtains the geomagnetic field of a geographic location. This API uses an asynchronous callback to return the
     * result.
     *
     * @param { LocationOptions } locationOptions - Geographic location.
     * @param { number } timeMillis - Time for obtaining the magnetic declination, in milliseconds.
     * @param { AsyncCallback<GeomagneticResponse> } callback - Callback used to return the geomagnetic field.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.getGeomagneticInfo(locationOptions: LocationOptions, timeMillis: long, callback: AsyncCallback<GeomagneticResponse>)
     */
    function getGeomagneticField(locationOptions: LocationOptions, timeMillis: number, callback: AsyncCallback<GeomagneticResponse>): void;
    /**
     * Obtains the geomagnetic field of a geographic location. This API uses a promise to return the result.
     *
     * @param { LocationOptions } locationOptions - Geographic location.
     * @param { number } timeMillis - Time for obtaining the magnetic declination, in milliseconds.
     * @returns { Promise<GeomagneticResponse> } Promise used to return the geomagnetic field.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.getGeomagneticInfo(locationOptions: LocationOptions, timeMillis: long)
     */
    function getGeomagneticField(locationOptions: LocationOptions, timeMillis: number): Promise<GeomagneticResponse>;
    /**
     * Obtains the geomagnetic field of a geographic location at a certain time. This API uses an asynchronous callback to
     * return the result.
     *
     * @param { LocationOptions } locationOptions - Geographic location, including the longitude, latitude, and altitude.
     * @param { number } timeMillis - Time when the magnetic declination is obtained. The value is a Unix timestamp, in ms.
     * @param { AsyncCallback<GeomagneticResponse> } callback - Callback used to return the geomagnetic field.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function getGeomagneticInfo(locationOptions: LocationOptions, timeMillis: number, callback: AsyncCallback<GeomagneticResponse>): void;
    /**
     * Obtains the geomagnetic field of a geographic location at a certain time. This API uses a promise to return the
     * result.
     *
     * @param { LocationOptions } locationOptions - Geographic location, including the longitude, latitude, and altitude.
     * @param { number } timeMillis - Time when the magnetic declination is obtained. The value is a Unix timestamp, in ms.
     * @returns { Promise<GeomagneticResponse> } Promise used to return the geomagnetic field.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function getGeomagneticInfo(locationOptions: LocationOptions, timeMillis: number): Promise<GeomagneticResponse>;
    /**
     * Obtains the altitude at which the device is located based on the sea-level atmospheric pressure and the current
     * atmospheric pressure. This API uses an asynchronous callback to return the result.
     *
     * @param { number } seaPressure - Sea-level atmospheric pressure, in hPa.
     * @param { number } currentPressure - Atmospheric pressure at the altitude where the device is located, in hPa.
     * @param { AsyncCallback<number> } callback - Callback used to return the altitude, in meters.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.getDeviceAltitude(seaPressure: double, currentPressure: double, callback: AsyncCallback<double>)
     */
    function getAltitude(seaPressure: number, currentPressure: number, callback: AsyncCallback<number>): void;
    /**
     * Obtains the altitude at which the device is located based on the sea-level atmospheric pressure and the current
     * atmospheric pressure. This API uses a promise to return the result.
     *
     * @param { number } seaPressure - Sea-level atmospheric pressure, in hPa.
     * @param { number } currentPressure - Atmospheric pressure at the altitude where the device is located, in hPa.
     * @returns { Promise<number> } Promise used to return the altitude, in meters.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.getDeviceAltitude(seaPressure: double, currentPressure: double)
     */
    function getAltitude(seaPressure: number, currentPressure: number): Promise<number>;
    /**
     * Obtains the altitude based on the atmospheric pressure. This API uses an asynchronous callback to return the
     * result.
     *
     * @param { number } seaPressure - Sea-level atmospheric pressure, in hPa.
     * @param { number } currentPressure - Specified atmospheric pressure, in hPa.
     * @param { AsyncCallback<number> } callback - Callback used to return the altitude, in meters.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function getDeviceAltitude(seaPressure: number, currentPressure: number, callback: AsyncCallback<number>): void;
    /**
     * Obtains the altitude based on the atmospheric pressure. This API uses a promise to return the result.
     *
     * @param { number } seaPressure - Sea-level atmospheric pressure, in hPa.
     * @param { number } currentPressure - Specified atmospheric pressure, in hPa.
     * @returns { Promise<number> } Promise used to return the altitude, in meters.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function getDeviceAltitude(seaPressure: number, currentPressure: number): Promise<number>;
    /**
     * Obtains the magnetic dip based on the inclination matrix. This API uses an asynchronous callback to return the
     * result.
     *
     * @param { Array<number> } inclinationMatrix - Inclination matrix.
     * @param { AsyncCallback<number> } callback - Callback used to return the magnetic dip, in radians.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.getInclination(inclinationMatrix: Array<double>, callback: AsyncCallback<double>)
     */
    function getGeomagneticDip(inclinationMatrix: Array<number>, callback: AsyncCallback<number>): void;
    /**
     * Obtains the magnetic dip based on the inclination matrix. This API uses a promise to return the result.
     *
     * @param { Array<number> } inclinationMatrix - Inclination matrix.
     * @returns { Promise<number> } Promise used to return the magnetic dip, in radians.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.getInclination(inclinationMatrix: Array<double>)
     */
    function getGeomagneticDip(inclinationMatrix: Array<number>): Promise<number>;
    /**
     * Obtains the magnetic dip based on the inclination matrix. This API uses an asynchronous callback to return the
     * result.
     *
     * @param { Array<number> } inclinationMatrix - Inclination matrix.
     * @param { AsyncCallback<number> } callback - Callback used to return the magnetic dip, in radians.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function getInclination(inclinationMatrix: Array<number>, callback: AsyncCallback<number>): void;
    /**
     * Obtains the magnetic dip based on the inclination matrix. This API uses a promise to return the result.
     *
     * @param { Array<number> } inclinationMatrix - Inclination matrix.
     * @returns { Promise<number> } Promise used to return the magnetic dip, in radians.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function getInclination(inclinationMatrix: Array<number>): Promise<number>;
    /**
     * Obtains the angle change between two rotation matrices. This API uses an asynchronous callback to return the
     * result.
     *
     * @param { Array<number> } currentRotationMatrix - Current rotation matrix.
     * @param { Array<number> } preRotationMatrix - The other rotation matrix.
     * @param { AsyncCallback<Array<number>> } callback - Callback used to return the angle change around the z, x, and y
     *     axes, in degrees.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.getAngleVariation(currentRotationMatrix: Array<double>, preRotationMatrix: Array<double>, callback: AsyncCallback<Array<double>>)
     */
    function getAngleModify(currentRotationMatrix: Array<number>, preRotationMatrix: Array<number>, callback: AsyncCallback<Array<number>>): void;
    /**
     * Obtains the angle change between two rotation matrices. This API uses a promise to return the result.
     *
     * @param { Array<number> } currentRotationMatrix - Current rotation matrix.
     * @param { Array<number> } preRotationMatrix - The other rotation matrix.
     * @returns { Promise<Array<number>> } Promise used to return the angle change around the z, x, and y axes, in
     *     degrees.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.getAngleVariation(currentRotationMatrix: Array<double>, preRotationMatrix: Array<double>)
     */
    function getAngleModify(currentRotationMatrix: Array<number>, preRotationMatrix: Array<number>): Promise<Array<number>>;
    /**
     * Obtains the angle change between two rotation matrices. This API uses an asynchronous callback to return the
     * result.
     *
     * @param { Array<number> } currentRotationMatrix - Current rotation matrix.
     * @param { Array<number> } preRotationMatrix - The other rotation matrix.
     * @param { AsyncCallback<Array<number>> } callback - Callback used to return the angle change around the z, x, and y
     *     axes, in degrees.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function getAngleVariation(currentRotationMatrix: Array<number>, preRotationMatrix: Array<number>, callback: AsyncCallback<Array<number>>): void;
    /**
     * Obtains the angle change between two rotation matrices. This API uses a promise to return the result.
     *
     * @param { Array<number> } currentRotationMatrix - Current rotation matrix.
     * @param { Array<number> } preRotationMatrix - The other rotation matrix.
     * @returns { Promise<Array<number>> } Promise used to return the angle change around the z, x, and y axes, in
     *     degrees.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function getAngleVariation(currentRotationMatrix: Array<number>, preRotationMatrix: Array<number>): Promise<Array<number>>;
    /**
     * Converts a rotation vector into a rotation matrix. This API uses an asynchronous callback to return the result.
     *
     * @param { Array<number> } rotationVector - Rotation vector to convert.
     * @param { AsyncCallback<Array<number>> } callback - Callback used to return the rotation matrix.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.getRotationMatrix(rotationVector: Array<double>, callback: AsyncCallback<Array<double>>)
     */
    function createRotationMatrix(rotationVector: Array<number>, callback: AsyncCallback<Array<number>>): void;
    /**
     * Converts a rotation vector into a rotation matrix. This API uses a promise to return the result.
     *
     * @param { Array<number> } rotationVector - Rotation vector to convert.
     * @returns { Promise<Array<number>> } Promise used to return the rotation matrix.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.getRotationMatrix(rotationVector: Array<double>)
     */
    function createRotationMatrix(rotationVector: Array<number>): Promise<Array<number>>;
    /**
     * Obtains the rotation matrix from a rotation vector. This API uses an asynchronous callback to return the result.
     *
     * @param { Array<number> } rotationVector - Rotation vector.
     * @param { AsyncCallback<Array<number>> } callback - Callback used to return the rotation matrix.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function getRotationMatrix(rotationVector: Array<number>, callback: AsyncCallback<Array<number>>): void;
    /**
     * Obtains the rotation matrix from a rotation vector. This API uses a promise to return the result.
     *
     * @param { Array<number> } rotationVector - Rotation vector.
     * @returns { Promise<Array<number>> } Promise used to return the rotation matrix.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function getRotationMatrix(rotationVector: Array<number>): Promise<Array<number>>;
    /**
     * Describes the coordinate options.
     *
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     */
    interface CoordinatesOptions {
        /**
         * X coordinate direction.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        x: number;
        /**
         * Y coordinate direction.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        y: number;
    }
    /**
     * Rotates a rotation vector so that it can represent the coordinate system in different ways. This API uses an
     * asynchronous callback to return the result.
     *
     * @param { Array<number> } inRotationVector - Rotation vector.
     * @param { CoordinatesOptions } coordinates - Direction of the coordinate system.
     * @param { AsyncCallback<Array<number>> } callback - Callback used to return the rotation vector after being rotated.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.transformRotationMatrix(inRotationVector: Array<double>, coordinates: CoordinatesOptions, callback: AsyncCallback<Array<double>>)
     */
    function transformCoordinateSystem(inRotationVector: Array<number>, coordinates: CoordinatesOptions, callback: AsyncCallback<Array<number>>): void;
    /**
     * Rotates a rotation vector so that it can represent the coordinate system in different ways. This API uses a promise
     * to return the result.
     *
     * @param { Array<number> } inRotationVector - Rotation vector.
     * @param { CoordinatesOptions } coordinates - Direction of the coordinate system.
     * @returns { Promise<Array<number>> } Promise used to return the rotation vector after being rotated.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.transformRotationMatrix(inRotationVector: Array<double>, coordinates: CoordinatesOptions)
     */
    function transformCoordinateSystem(inRotationVector: Array<number>, coordinates: CoordinatesOptions): Promise<Array<number>>;
    /**
     * Transforms a rotation vector based on the coordinate system. This API uses an asynchronous callback to return the
     * result.
     *
     * @param { Array<number> } inRotationVector - Rotation vector.
     * @param { CoordinatesOptions } coordinates - Rotation vector to transform.
     * @param { AsyncCallback<Array<number>> } callback - Callback used to return the rotation vector after being
     *     transformed.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function transformRotationMatrix(inRotationVector: Array<number>, coordinates: CoordinatesOptions, callback: AsyncCallback<Array<number>>): void;
    /**
     * Transforms a rotation vector based on the coordinate system. This API uses a promise to return the result.
     *
     * @param { Array<number> } inRotationVector - Rotation vector.
     * @param { CoordinatesOptions } coordinates - Rotation vector to transform.
     * @returns { Promise<Array<number>> } Promise used to return the rotation vector after being transformed.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function transformRotationMatrix(inRotationVector: Array<number>, coordinates: CoordinatesOptions): Promise<Array<number>>;
    /**
     * Converts a rotation vector into a quaternion. This API uses an asynchronous callback to return the result.
     *
     * @param { Array<number> } rotationVector - Rotation vector to convert.
     * @param { AsyncCallback<Array<number>> } callback - Callback used to return the quaternion.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.getQuaternion(rotationVector: Array<double>, callback: AsyncCallback<Array<double>>)
     */
    function createQuaternion(rotationVector: Array<number>, callback: AsyncCallback<Array<number>>): void;
    /**
     * Converts a rotation vector into a quaternion. This API uses a promise to return the result.
     *
     * @param { Array<number> } rotationVector - Rotation vector to convert.
     * @returns { Promise<Array<number>> } Promise used to return the quaternion.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.getQuaternion(rotationVector: Array<double>)
     */
    function createQuaternion(rotationVector: Array<number>): Promise<Array<number>>;
    /**
     * Obtains the quaternion from a rotation vector. This API uses an asynchronous callback to return the result.
     *
     * @param { Array<number> } rotationVector - Rotation vector.
     * @param { AsyncCallback<Array<number>> } callback - Callback used to return the quaternion.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function getQuaternion(rotationVector: Array<number>, callback: AsyncCallback<Array<number>>): void;
    /**
     * Obtains the quaternion from a rotation vector. This API uses a promise to return the result.
     *
     * @param { Array<number> } rotationVector - Rotation vector.
     * @returns { Promise<Array<number>> } Promise used to return the quaternion.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function getQuaternion(rotationVector: Array<number>): Promise<Array<number>>;
    /**
     * Obtains the device direction based on the rotation matrix. This API uses an asynchronous callback to return the
     * result.
     *
     * @param { Array<number> } rotationMatrix - Rotation matrix.
     * @param { AsyncCallback<Array<number>> } callback - Callback used to return the rotation angle around the z, x, and
     *     y axes, in degrees.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.getOrientation(rotationMatrix: Array<double>, callback: AsyncCallback<Array<double>>)
     */
    function getDirection(rotationMatrix: Array<number>, callback: AsyncCallback<Array<number>>): void;
    /**
     * Obtains the device direction based on the rotation matrix. This API uses a promise to return the result.
     *
     * @param { Array<number> } rotationMatrix - Rotation matrix.
     * @returns { Promise<Array<number>> } Promise used to return the rotation angle around the z, x, and y axes, in
     *     degrees.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.getOrientation(rotationMatrix: Array<double>)
     */
    function getDirection(rotationMatrix: Array<number>): Promise<Array<number>>;
    /**
     * Obtains the device direction based on the rotation matrix. This API uses an asynchronous callback to return the
     * result.
     *
     * @param { Array<number> } rotationMatrix - Rotation matrix.
     * @param { AsyncCallback<Array<number>> } callback - Callback used to return the rotation angle around the z, x, and
     *     y axes, in degrees.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function getOrientation(rotationMatrix: Array<number>, callback: AsyncCallback<Array<number>>): void;
    /**
     * Obtains the device direction based on the rotation matrix. This API uses a promise to return the result.
     *
     * @param { Array<number> } rotationMatrix - Rotation matrix.
     * @returns { Promise<Array<number>> } Promise used to return the rotation angle around the z, x, and y axes, in
     *     degrees.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function getOrientation(rotationMatrix: Array<number>): Promise<Array<number>>;
    /**
     * Describes the response for setting the rotation matrix.
     *
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     */
    interface RotationMatrixResponse {
        /**
         * Rotation matrix.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        rotation: Array<number>;
        /**
         * Inclination matrix.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        inclination: Array<number>;
    }
    /**
     * Obtains the rotation matrix based on a gravity vector and geomagnetic vector. This API uses an asynchronous
     * callback to return the result.
     *
     * @param { Array<number> } gravity - Gravity vector.
     * @param { Array<number> } geomagnetic - Geomagnetic vector.
     * @param { AsyncCallback<RotationMatrixResponse> } callback - Callback used to return the rotation matrix.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.getRotationMatrix(gravity: Array<double>, geomagnetic: Array<double>, callback: AsyncCallback<RotationMatrixResponse>)
     */
    function createRotationMatrix(gravity: Array<number>, geomagnetic: Array<number>, callback: AsyncCallback<RotationMatrixResponse>): void;
    /**
     * Obtains the rotation matrix based on a gravity vector and geomagnetic vector. This API uses a promise to return the
     * result.
     *
     * @param { Array<number> } gravity - Gravity vector.
     * @param { Array<number> } geomagnetic - Geomagnetic vector.
     * @returns { Promise<RotationMatrixResponse> } Promise used to return the rotation matrix.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.getRotationMatrix(gravity: Array<double>, geomagnetic: Array<double>)
     */
    function createRotationMatrix(gravity: Array<number>, geomagnetic: Array<number>): Promise<RotationMatrixResponse>;
    /**
     * Obtains the rotation matrix based on a gravity vector and geomagnetic vector. This API uses an asynchronous
     * callback to return the result.
     *
     * @param { Array<number> } gravity - Gravity vector.
     * @param { Array<number> } geomagnetic - Geomagnetic vector.
     * @param { AsyncCallback<RotationMatrixResponse> } callback - Callback used to return the rotation matrix.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function getRotationMatrix(gravity: Array<number>, geomagnetic: Array<number>, callback: AsyncCallback<RotationMatrixResponse>): void;
    /**
     * Obtains the rotation matrix based on a gravity vector and geomagnetic vector. This API uses a promise to return the
     * result.
     *
     * @param { Array<number> } gravity - Gravity vector.
     * @param { Array<number> } geomagnetic - Geomagnetic vector.
     * @returns { Promise<RotationMatrixResponse> } Promise used to return the rotation matrix.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br> 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 9
     */
    function getRotationMatrix(gravity: Array<number>, geomagnetic: Array<number>): Promise<RotationMatrixResponse>;
    /**
     * Describes the sensor data reporting frequency.
     *
     * @syscap SystemCapability.Sensors.Sensor
     * @atomicservice [since 11]
     * @since 8
     */
    interface Options {
        /**
         * Frequency at which a sensor reports data. The default value is 200,000,000 ns. The maximum and minimum values of
         * this parameter are determined by the reporting frequency supported by the hardware. If the configured frequency
         * is greater than the maximum value, the maximum value is used for data reporting. If the configured frequency is
         * less than the minimum value, the minimum value is used for data reporting.
         *
         * @type { ?number } [since 8 - 10]
         * @type { ?(number | SensorFrequency) } [since 11]
         * @syscap SystemCapability.Sensors.Sensor
         * @atomicservice [since 11]
         * @since 8
         */
        interval?: number | SensorFrequency;
        /**
         * Sensor parameters, including **deviceId** and **sensorIndex**.
         *
         * This API can be used in atomic services since API version 19.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @atomicservice
         * @since 19
         */
        sensorInfoParam?: SensorInfoParam;
    }
    /**
     * Defines the reporting frequency mode of the sensor.
     *
     * @syscap SystemCapability.Sensors.Sensor
     * @unionmember { 'game' } Game mode, which specifies a sensor data reporting frequency of 20,000,000 ns. This
     *     parameter takes effect only when the frequency is within the frequency range supported by the hardware.
     * @unionmember { 'ui' } UI mode, which specifies a sensor data reporting frequency of 60,000,000 ns. This parameter
     *     takes effect only when the frequency is within the frequency range supported by the hardware.
     * @unionmember { 'normal' } Normal mode, which specifies a sensor data reporting frequency of 200,000,000 ns. This
     *     parameter takes effect only when the frequency is within the frequency range supported by the hardware.
     * @atomicservice
     * @since 11
     */
    type SensorFrequency = 'game' | 'ui' | 'normal';
    /**
     * Enumerates the sensor types.
     *
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     * @deprecated since 9
     * @useinstead sensor.SensorId
     */
    enum SensorType {
        /**
         * Acceleration sensor.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         * @deprecated since 9
         * @useinstead sensor.SensorId#ACCELEROMETER
         */
        SENSOR_TYPE_ID_ACCELEROMETER = 1,
        /**
         * Gyroscope sensor.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         * @deprecated since 9
         * @useinstead sensor.SensorId#GYROSCOPE
         */
        SENSOR_TYPE_ID_GYROSCOPE = 2,
        /**
         * Ambient light sensor.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         * @deprecated since 9
         * @useinstead sensor.SensorId#AMBIENT_LIGHT
         */
        SENSOR_TYPE_ID_AMBIENT_LIGHT = 5,
        /**
         * Magnetic field sensor.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         * @deprecated since 9
         * @useinstead sensor.SensorId#MAGNETIC_FIELD
         */
        SENSOR_TYPE_ID_MAGNETIC_FIELD = 6,
        /**
         * Barometer sensor.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         * @deprecated since 9
         * @useinstead sensor.SensorId#BAROMETER
         */
        SENSOR_TYPE_ID_BAROMETER = 8,
        /**
         * Hall effect sensor.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         * @deprecated since 9
         * @useinstead sensor.SensorId#HALL
         */
        SENSOR_TYPE_ID_HALL = 10,
        /**
         * Proximity sensor.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         * @deprecated since 9
         * @useinstead sensor.SensorId#PROXIMITY
         */
        SENSOR_TYPE_ID_PROXIMITY = 12,
        /**
         * Humidity sensor.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         * @deprecated since 9
         * @useinstead sensor.SensorId#HUMIDITY
         */
        SENSOR_TYPE_ID_HUMIDITY = 13,
        /**
         * Orientation sensor.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         * @deprecated since 9
         * @useinstead sensor.SensorId#ORIENTATION
         */
        SENSOR_TYPE_ID_ORIENTATION = 256,
        /**
         * Gravity sensor.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         * @deprecated since 9
         * @useinstead sensor.SensorId#GRAVITY
         */
        SENSOR_TYPE_ID_GRAVITY = 257,
        /**
         * Linear acceleration sensor.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         * @deprecated since 9
         * @useinstead sensor.SensorId#LINEAR_ACCELEROMETER
         */
        SENSOR_TYPE_ID_LINEAR_ACCELERATION = 258,
        /**
         * Rotation vector sensor.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         * @deprecated since 9
         * @useinstead sensor.SensorId#ROTATION_VECTOR
         */
        SENSOR_TYPE_ID_ROTATION_VECTOR = 259,
        /**
         * Ambient temperature sensor.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         * @deprecated since 9
         * @useinstead sensor.SensorId#AMBIENT_TEMPERATURE
         */
        SENSOR_TYPE_ID_AMBIENT_TEMPERATURE = 260,
        /**
         * Uncalibrated magnetic field sensor.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         * @deprecated since 9
         * @useinstead sensor.SensorId#MAGNETIC_FIELD_UNCALIBRATED
         */
        SENSOR_TYPE_ID_MAGNETIC_FIELD_UNCALIBRATED = 261,
        /**
         * Uncalibrated gyroscope sensor.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         * @deprecated since 9
         * @useinstead sensor.SensorId#GYROSCOPE_UNCALIBRATED
         */
        SENSOR_TYPE_ID_GYROSCOPE_UNCALIBRATED = 263,
        /**
         * Significant motion sensor.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         * @deprecated since 9
         * @useinstead sensor.SensorId#SIGNIFICANT_MOTION
         */
        SENSOR_TYPE_ID_SIGNIFICANT_MOTION = 264,
        /**
         * Pedometer detection sensor.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         * @deprecated since 9
         * @useinstead sensor.SensorId#PEDOMETER_DETECTION
         */
        SENSOR_TYPE_ID_PEDOMETER_DETECTION = 265,
        /**
         * Pedometer sensor.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         * @deprecated since 9
         * @useinstead sensor.SensorId#PEDOMETER
         */
        SENSOR_TYPE_ID_PEDOMETER = 266,
        /**
         * Heart rate sensor.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         * @deprecated since 9
         * @useinstead sensor.SensorId#HEART_RATE
         */
        SENSOR_TYPE_ID_HEART_RATE = 278,
        /**
         * Wear detection sensor.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         * @deprecated since 9
         * @useinstead sensor.SensorId#WEAR_DETECTION
         */
        SENSOR_TYPE_ID_WEAR_DETECTION = 280,
        /**
         * Uncalibrated acceleration sensor.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         * @deprecated since 9
         * @useinstead sensor.SensorId#ACCELEROMETER_UNCALIBRATED
         */
        SENSOR_TYPE_ID_ACCELEROMETER_UNCALIBRATED = 281
    }
    /**
     * Enumerates the accuracy levels of sensor data.
     *
     * @syscap SystemCapability.Sensors.Sensor
     * @atomicservice
     * @since 11
     */
    enum SensorAccuracy {
        /**
         * The sensor data is unreliable.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @atomicservice
         * @since 11
         */
        ACCURACY_UNRELIABLE = 0,
        /**
         * The sensor data is at a low accuracy level.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @atomicservice
         * @since 11
         */
        ACCURACY_LOW = 1,
        /**
         * The sensor data is at a medium accuracy level.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @atomicservice
         * @since 11
         */
        ACCURACY_MEDIUM = 2,
        /**
         * The sensor data is at a high accuracy level.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @atomicservice
         * @since 11
         */
        ACCURACY_HIGH = 3
    }
    /**
     * Describes the timestamp of the sensor data.
     *
     * @syscap SystemCapability.Sensors.Sensor
     * @atomicservice [since 11]
     * @since 8
     */
    interface Response {
        /**
         * Timestamp when the sensor reports data. Time from device startup to data reporting, in nanoseconds.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @atomicservice [since 11]
         * @since 8
         */
        timestamp: number;
        /**
         * Accuracy of the sensor data.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @atomicservice
         * @since 11
         */
        accuracy: SensorAccuracy;
    }
    /**
     * Describes the acceleration sensor data. It extends from [Response]{@link sensor.Response}.
     *
     * @syscap SystemCapability.Sensors.Sensor
     * @atomicservice [since 11]
     * @since 8
     */
    interface AccelerometerResponse extends Response {
        /**
         * Acceleration along the x-axis of the device, in m/s?. The value is equal to the reported physical quantity.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @atomicservice [since 11]
         * @since 8
         */
        x: number;
        /**
         * Acceleration along the y-axis of the device, in m/s?. The value is equal to the reported physical quantity.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @atomicservice [since 11]
         * @since 8
         */
        y: number;
        /**
         * Acceleration along the z-axis of the device, in m/s?. The value is equal to the reported physical quantity.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @atomicservice [since 11]
         * @since 8
         */
        z: number;
    }
    /**
     * Describes the linear acceleration sensor data. It extends from [Response]{@link sensor.Response}.
     *
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     */
    interface LinearAccelerometerResponse extends Response {
        /**
         * Linear acceleration along the x-axis of the device, in m/s?.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        x: number;
        /**
         * Linear acceleration along the y-axis of the device, in m/s?.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        y: number;
        /**
         * Linear acceleration along the z-axis of the device, in m/s?.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        z: number;
    }
    /**
     * Describes the uncalibrated acceleration sensor data. It extends from [Response]{@link sensor.Response}.
     *
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     */
    interface AccelerometerUncalibratedResponse extends Response {
        /**
         * Uncalibrated acceleration along the x-axis of the device, in m/s?.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        x: number;
        /**
         * Uncalibrated acceleration along the y-axis of the device, in m/s?.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        y: number;
        /**
         * Uncalibrated acceleration along the z-axis of the device, in m/s?.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        z: number;
        /**
         * Uncalibrated acceleration bias along the x-axis of the device, in m/s?.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        biasX: number;
        /**
         * Uncalibrated acceleration bias along the y-axis of the device, in m/s?.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        biasY: number;
        /**
         * Uncalibrated acceleration bias along the z-axis of the device, in m/s?.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        biasZ: number;
    }
    /**
     * Describes the gravity sensor data. It extends from [Response]{@link sensor.Response}.
     *
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     */
    interface GravityResponse extends Response {
        /**
         * Gravitational acceleration along the x-axis of the device, in m/s?.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        x: number;
        /**
         * Gravitational acceleration along the y-axis of the device, in m/s?.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        y: number;
        /**
         * Gravitational acceleration along the z-axis of the device, in m/s?.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        z: number;
    }
    /**
     * Describes the orientation sensor data. It extends from [Response]{@link sensor.Response}.
     *
     * @syscap SystemCapability.Sensors.Sensor
     * @atomicservice [since 11]
     * @since 8
     */
    interface OrientationResponse extends Response {
        /**
         * Rotation angle of the device around the z-axis, in degrees. The value ranges from 0 to 360.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @atomicservice [since 11]
         * @since 8
         */
        alpha: number;
        /**
         * Rotation angle of the device around the x-axis, in degrees. The value ranges from 0 to ��180.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @atomicservice [since 11]
         * @since 8
         */
        beta: number;
        /**
         * Rotation angle of the device around the y-axis, in degrees. The value ranges from 0 to ��90.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @atomicservice [since 11]
         * @since 8
         */
        gamma: number;
    }
    /**
     * Describes the rotation vector sensor data. It extends from [Response]{@link sensor.Response}.
     *
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     */
    interface RotationVectorResponse extends Response {
        /**
         * X-component of the rotation vector.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        x: number;
        /**
         * Y-component of the rotation vector.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        y: number;
        /**
         * Z-component of the rotation vector.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        z: number;
        /**
         * Scalar, which describes the rotation status of the device relative to a reference direction, in radians
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        w: number;
    }
    /**
     * Describes the gyroscope sensor data. It extends from [Response]{@link sensor.Response}.
     *
     * @syscap SystemCapability.Sensors.Sensor
     * @atomicservice [since 11]
     * @since 8
     */
    interface GyroscopeResponse extends Response {
        /**
         * Angular velocity of rotation around the x-axis of the device, in rad/s. The value is equal to the reported
         * physical quantity.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @atomicservice [since 11]
         * @since 8
         */
        x: number;
        /**
         * Angular velocity of rotation around the y-axis of the device, in rad/s. The value is equal to the reported
         * physical quantity.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @atomicservice [since 11]
         * @since 8
         */
        y: number;
        /**
         * Angular velocity of rotation around the z-axis of the device, in rad/s. The value is equal to the reported
         * physical quantity.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @atomicservice [since 11]
         * @since 8
         */
        z: number;
    }
    /**
     * Describes the uncalibrated gyroscope sensor data. It extends from [Response]{@link sensor.Response}.
     *
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     */
    interface GyroscopeUncalibratedResponse extends Response {
        /**
         * Uncalibrated angular velocity of rotation around the x-axis of the device, in rad/s.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        x: number;
        /**
         * Uncalibrated angular velocity of rotation around the y-axis of the device, in rad/s.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        y: number;
        /**
         * Uncalibrated angular velocity of rotation around the z-axis of the device, in rad/s.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        z: number;
        /**
         * Uncalibrated angular velocity bias of rotation around the x-axis of the device, in rad/s.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        biasX: number;
        /**
         * Uncalibrated angular velocity bias of rotation around the y-axis of the device, in rad/s.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        biasY: number;
        /**
         * Uncalibrated angular velocity bias of rotation around the z-axis of the device, in rad/s.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        biasZ: number;
    }
    /**
     * Describes the significant motion sensor data. It extends from [Response]{@link sensor.Response}.
     *
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     */
    interface SignificantMotionResponse extends Response {
        /**
         * Intensity of a motion. This parameter specifies whether a device has a significant motion on three physical axes
         * (X, Y, and Z). The value **1** is reported when the device has a significant motion.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        scalar: number;
    }
    /**
     * Describes the proximity sensor data. It extends from [Response]{@link sensor.Response}.
     *
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     */
    interface ProximityResponse extends Response {
        /**
         * Proximity between the visible object and the device monitor. The value **0** means the two are close to each
         * other, and a value greater than 0 means that they are far away from each other.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        distance: number;
    }
    /**
     * Describes the ambient light sensor data. It extends from [Response]{@link sensor.Response}.
     *
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     */
    interface LightResponse extends Response {
        /**
         * Illumination, in lux.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        intensity: number;
        /**
         * Color temperature, in Kelvin. This parameter is optional. If this parameter is not supported, a fixed value (
         * customized by the sensor) is returned. If this parameter is supported, a normal value is returned.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 12
         */
        colorTemperature?: number;
        /**
         * Infrared luminance, in cd/m?. This parameter is optional. If this parameter is not supported, a fixed value (
         * customized by the sensor) is returned. If this parameter is supported, a normal value is returned.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 12
         */
        infraredLuminance?: number;
    }
    /**
     * Describes the Hall effect sensor data. It extends from [Response]{@link sensor.Response}.
     *
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     */
    interface HallResponse extends Response {
        /**
         * Hall effect sensor status. This parameter specifies whether a magnetic field exists around a device. The value
         * **0** means that a magnetic field does not exist, and a value greater than **0** means the opposite.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        status: number;
    }
    /**
     * Describes the magnetic field sensor data. It extends from [Response]{@link sensor.Response}.
     *
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     */
    interface MagneticFieldResponse extends Response {
        /**
         * Magnetic field strength on the x-axis, in ��T.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        x: number;
        /**
         * Magnetic field strength on the y-axis, in ��T.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        y: number;
        /**
         * Magnetic field strength on the z-axis, in ��T.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        z: number;
    }
    /**
     * Describes the uncalibrated magnetic field sensor data. It extends from [Response]{@link sensor.Response}.
     *
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     */
    interface MagneticFieldUncalibratedResponse extends Response {
        /**
         * Uncalibrated magnetic field strength on the x-axis, in ��T.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        x: number;
        /**
         * Uncalibrated magnetic field strength on the y-axis, in ��T.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        y: number;
        /**
         * Uncalibrated magnetic field strength on the z-axis, in ��T.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        z: number;
        /**
         * Bias of the uncalibrated magnetic field strength on the x-axis, in ��T.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        biasX: number;
        /**
         * Bias of the uncalibrated magnetic field strength on the y-axis, in ��T.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        biasY: number;
        /**
         * Bias of the uncalibrated magnetic field strength on the z-axis, in ��T.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        biasZ: number;
    }
    /**
     * Describes the pedometer sensor data. It extends from [Response]{@link sensor.Response}.
     *
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     */
    interface PedometerResponse extends Response {
        /**
         * Number of steps a user has walked.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        steps: number;
    }
    /**
     * Describes the humidity sensor data. It extends from [Response]{@link sensor.Response}.
     *
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     */
    interface HumidityResponse extends Response {
        /**
         * Ambient relative humidity, in a percentage (%).
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        humidity: number;
    }
    /**
     * Describes the pedometer detection sensor data. It extends from [Response]{@link sensor.Response}.
     *
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     */
    interface PedometerDetectionResponse extends Response {
        /**
         * Pedometer detection. This parameter specifies whether a user takes a step. The value **0** means that the user
         * does not take a step, and **1** means that the user takes a step.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        scalar: number;
    }
    /**
     * Describes the ambient temperature sensor data. It extends from [Response]{@link sensor.Response}.
     *
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     */
    interface AmbientTemperatureResponse extends Response {
        /**
         * Ambient temperature, in degree Celsius.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        temperature: number;
    }
    /**
     * Describes the barometer sensor data. It extends from [Response]{@link sensor.Response}.
     *
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     */
    interface BarometerResponse extends Response {
        /**
         * Atmospheric pressure, in units of hPa.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        pressure: number;
    }
    /**
     * Describes the heart rate sensor data. It extends from [Response]{@link sensor.Response}.
     *
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     */
    interface HeartRateResponse extends Response {
        /**
         * Heart rate, in beats per minute (bpm).
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        heartRate: number;
    }
    /**
     * Describes the wear detection sensor data. It extends from [Response]{@link sensor.Response}.
     *
     * @syscap SystemCapability.Sensors.Sensor
     * @since 8
     */
    interface WearDetectionResponse extends Response {
        /**
         * Whether the device is being worn. The value **1** means that the device is being worn, and **0** means the
         * opposite.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 8
         */
        value: number;
    }
    /**
     * Describes the fusion pressure sensor data. It extends from [Response]{@link sensor.Response}.
     *
     * @syscap SystemCapability.Sensors.Sensor
     * @since 22
     */
    interface FusionPressureResponse extends Response {
        /**
         * Pressure percentage on the fused pressure sensor, in percentage (%)
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 22
         */
        fusionPressure: number;
    }
    /**
     * Enables listening for sensor status changes. This API asynchronously returns the result through a callback.
     *
     * @param { 'sensorStatusChange' } type - Event type. The value **sensorStatusChange** indicates the sensor status
     *     change event.
     * @param { Callback<SensorStatusEvent> } callback - Callback used to return the sensor status change event.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 19
     */
    function on(type: 'sensorStatusChange', callback: Callback<SensorStatusEvent>): void;
    /**
     * Disables listening for sensor status changes.
     *
     * @param { 'sensorStatusChange' } type - Event type. The value **sensorStatusChange** indicates the sensor status
     *     change event.
     * @param { Callback<SensorStatusEvent> } [callback] - Callback passed to **sensor.on**. If this parameter is left
     *     unspecified, listening will be disabled for all callbacks.
     * @throws { BusinessError } 14500101 - Service exception. Possible causes: 1. Sensor hdf service exception;
     *     <br> 2. Sensor service ipc exception;3. Sensor data channel exception.
     * @syscap SystemCapability.Sensors.Sensor
     * @since 19
     */
    function off(type: 'sensorStatusChange', callback?: Callback<SensorStatusEvent>): void;
    /**
     * Defines a device status change event.
     *
     * @syscap SystemCapability.Sensors.Sensor
     * @since 19
     */
    interface SensorStatusEvent {
        /**
         * Timestamp when an event occurs, in ms.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 19
         */
        timestamp: number;
        /**
         * Sensor ID.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 19
         */
        sensorId: number;
        /**
         * Sensor index.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 19
         */
        sensorIndex: number;
        /**
         * Sensor status. The value **true** indicates that the sensor is online, and the value **false** indicates the
         * opposite.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 19
         */
        isSensorOnline: boolean;
        /**
         * Device ID.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 19
         */
        deviceId: number;
        /**
         * Device name.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @since 19
         */
        deviceName: string;
    }
    /**
     * Defines sensor parameters, including **deviceId** and **sensorIndex**.
     *
     * @syscap SystemCapability.Sensors.Sensor
     * @atomicservice
     * @since 19
     */
    interface SensorInfoParam {
        /**
         * Device ID. The default value is -1, indicating the local device. You can use
         * [getSensorList]{@link sensor.getSensorList(callback: AsyncCallback<Array<Sensor>>)} or
         * [sensorStatusChange]{@link sensor.on(type: 'sensorStatusChange', callback: Callback<SensorStatusEvent>)} to
         * obtain the device ID.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @atomicservice
         * @since 19
         */
        deviceId?: number;
        /**
         * Sensor index. The default value is **0**, indicating the default sensor on the device. You can use
         * [getSensorList]{@link sensor.getSensorList(callback: AsyncCallback<Array<Sensor>>)} or
         * [sensorStatusChange]{@link sensor.on(type: 'sensorStatusChange', callback: Callback<SensorStatusEvent>)} to
         * obtain the sensor index.
         *
         * @syscap SystemCapability.Sensors.Sensor
         * @atomicservice
         * @since 19
         */
        sensorIndex?: number;
    }
}
export default sensor;

```
