# @system.sensor.d.ts

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
 * The **Sensor** module provides APIs for querying the sensor list, subscribing to or unsubscribing from sensor data,
 * and executing control commands.
 *
 * The sensors are classified into the following categories based on their functions: motion, environment, orientation,
 * light, body, and other categories (such as Hall effect sensors). Each category includes different sensor types. A
 * sensor type may be a single hardware sensor or a composite of multiple hardware sensors.
 *
 * > **NOTE**
 * >
 * > - Module maintenance policy:
 * > >     - For lite wearables, this module is constantly maintained and available.
 * > >     - For other device types, this module is no longer maintained since API version 8, and You are advised to use
 * > the new [@ohos.sensor]{@link @ohos.sensor:sensor} module.
 * > - The initial APIs of this module are supported since API version 3.
 * > Newly added APIs will be marked with a superscript to indicate their earliest API version.
 * > - This module requires hardware support and can only be debugged on real devices.
 *
 * @file
 * @kit SensorServiceKit
 */
/**
 * Defines the callback invoked when the acceleration sensor data changes.
 *
 * @permission ohos.permission.ACCELEROMETER
 * @syscap SystemCapability.Sensors.Sensor.Lite
 * @famodelonly
 * @since 3
 * @deprecated since 8
 * @reserved ["liteWearable"]
 * @useinstead ohos.sensor/sensor#AccelerometerResponse
 */
export interface AccelerometerResponse {
    /**
     * Acceleration on the x-axis.
     *
     * @permission ohos.permission.ACCELEROMETER
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead ohos.sensor/sensor#AccelerometerResponse.x
     */
    x: number;
    /**
     * Acceleration on the y-axis.
     *
     * @permission ohos.permission.ACCELEROMETER
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead ohos.sensor/sensor#AccelerometerResponse.y
     */
    y: number;
    /**
     * Acceleration on the z-axis.
     *
     * @permission ohos.permission.ACCELEROMETER
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead ohos.sensor/sensor#AccelerometerResponse.z
     */
    z: number;
}
/**
 * Defines the type of data to return for a subscription to data changes of the acceleration sensor.
 *
 * @permission ohos.permission.ACCELEROMETER
 * @syscap SystemCapability.Sensors.Sensor.Lite
 * @famodelonly
 * @since 3
 * @deprecated since 8
 * @reserved ["liteWearable"]
 * @useinstead ohos.sensor/sensor.SensorId#ACCELEROMETER
 */
export interface subscribeAccelerometerOptions {
    /**
     * Execution frequency of the callback for returning the acceleration sensor data.
     *
     * The default value is **normal**. The options are as follows:
     *
     * - **game**: called at an interval of 20 ms, which is applicable to gaming scenarios.
     * - **ui**: called at an interval of 60 ms, which is applicable to UI updating scenarios.
     * - **normal**: called at an interval of 200 ms, which is applicable to power-saving scenarios.
     *
     * @permission ohos.permission.ACCELEROMETER
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead ohos.sensor/sensor#Options.interval
     */
    interval: string;
    /**
     * Callback invoked when the acceleration sensor data changes.
     *
     * @permission ohos.permission.ACCELEROMETER
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead ohos.sensor/sensor#on
     */
    success: (data: AccelerometerResponse) => void;
    /**
     * Callback invoked when an API call fails.
     *
     * @permission ohos.permission.ACCELEROMETER
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead ohos.sensor/sensor#on
     */
    fail?: (data: string, code: number) => void;
}
/**
 * Defines a **CompassResponse** object.
 *
 * @syscap SystemCapability.Sensors.Sensor.Lite
 * @famodelonly
 * @since 3
 * @deprecated since 8
 * @reserved ["liteWearable"]
 * @useinstead ohos.sensor/sensor#OrientationResponse
 */
export interface CompassResponse {
    /**
     * Direction of the device, in degrees.
     *
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead ohos.sensor/sensor#OrientationResponse.alpha
     */
    direction: number;
}
/**
 * Defines the type of data to return for a subscription to data changes of the compass sensor.
 *
 * @syscap SystemCapability.Sensors.Sensor.Lite
 * @famodelonly
 * @since 3
 * @deprecated since 8
 * @reserved ["liteWearable"]
 * @useinstead ohos.sensor/sensor.SensorId#ORIENTATION
 */
export interface SubscribeCompassOptions {
    /**
     * Callback invoked when the compass sensor data changes.
     *
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead ohos.sensor/sensor#on
     */
    success: (data: CompassResponse) => void;
    /**
     * Callback invoked when an API call fails.
     *
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead ohos.sensor/sensor#on
     */
    fail?: (data: string, code: number) => void;
}
/**
 * Callback invoked when the proximity sensor data changes.
 *
 * @syscap SystemCapability.Sensors.Sensor.Lite
 * @famodelonly
 * @since 3
 * @deprecated since 8
 * @reserved ["liteWearable"]
 * @useinstead ohos.sensor/sensor#ProximityResponse
 */
export interface ProximityResponse {
    /**
     * Distance between a visible object and the device screen.
     *
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead ohos.sensor/sensor#ProximityResponse.distance
     */
    distance: number;
}
/**
 * Defines the type of data to return for a subscription to data changes of the proximity sensor.
 *
 * @syscap SystemCapability.Sensors.Sensor.Lite
 * @famodelonly
 * @since 3
 * @deprecated since 8
 * @reserved ["liteWearable"]
 * @useinstead ohos.sensor/sensor.SensorId#PROXIMITY
 */
export interface SubscribeProximityOptions {
    /**
     * Defines a **ProximityResponse** object.
     *
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead ohos.sensor/sensor#on
     */
    success: (data: ProximityResponse) => void;
    /**
     * Callback invoked when an API call fails.
     *
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead ohos.sensor/sensor#on
     */
    fail?: (data: string, code: number) => void;
}
/**
 * Defines a **LightResponse** object.
 *
 * @syscap SystemCapability.Sensors.Sensor.Lite
 * @famodelonly
 * @since 3
 * @deprecated since 8
 * @reserved ["liteWearable"]
 * @useinstead ohos.sensor/sensor#LightResponse
 */
export interface LightResponse {
    /**
     * Light intensity, in lux.
     *
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead ohos.sensor/sensor#LightResponse.intensity
     */
    intensity: number;
}
/**
 * Defines the type of data to return for a subscription to data changes of the ambient light sensor.
 *
 * @syscap SystemCapability.Sensors.Sensor.Lite
 * @famodelonly
 * @since 3
 * @deprecated since 8
 * @reserved ["liteWearable"]
 * @useinstead ohos.sensor/sensor.SensorId#AMBIENT_LIGHT
 */
export interface SubscribeLightOptions {
    /**
     * Callback invoked when the ambient light sensor data changes.
     *
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead ohos.sensor/sensor#on
     */
    success: (data: LightResponse) => void;
    /**
     * Callback invoked when an API call fails.
     *
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead ohos.sensor/sensor#on
     */
    fail?: (data: string, code: number) => void;
}
/**
 * Callback invoked when the step counter sensor data changes.
 *
 * @permission ohos.permission.ACTIVITY_MOTION
 * @syscap SystemCapability.Sensors.Sensor.Lite
 * @famodelonly
 * @since 3
 * @deprecated since 8
 * @reserved ["liteWearable"]
 * @useinstead ohos.sensor/sensor#PedometerResponse
 */
export interface StepCounterResponse {
    /**
     * Number of counted steps after the sensor is restarted.
     *
     * @permission ohos.permission.ACTIVITY_MOTION
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead ohos.sensor/sensor#PedometerResponse.steps
     */
    steps: number;
}
/**
 * Defines the type of data to return for a subscription to data changes of the step counter sensor.
 *
 * @permission ohos.permission.ACTIVITY_MOTION
 * @syscap SystemCapability.Sensors.Sensor.Lite
 * @famodelonly
 * @since 3
 * @deprecated since 8
 * @reserved ["liteWearable"]
 * @useinstead ohos.sensor/SensorId#PEDOMETER
 */
export interface SubscribeStepCounterOptions {
    /**
     * Defines a **StepCounterResponse** object.
     *
     * @permission ohos.permission.ACTIVITY_MOTION
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead ohos.sensor/sensor#on
     */
    success: (data: StepCounterResponse) => void;
    /**
     * Callback invoked when an API call fails.
     *
     * @permission ohos.permission.ACTIVITY_MOTION
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead ohos.sensor/sensor#on
     */
    fail?: (data: string, code: number) => void;
}
/**
 * Defines a **BarometerResponse** object.
 *
 * @syscap SystemCapability.Sensors.Sensor.Lite
 * @famodelonly
 * @since 3
 * @deprecated since 8
 * @reserved ["liteWearable"]
 * @useinstead ohos.sensor/sensor#BarometerResponse
 */
export interface BarometerResponse {
    /**
     * Pressure, in pascal.
     *
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead ohos.sensor/sensor#BarometerResponse.pressure
     */
    pressure: number;
}
/**
 * Defines the type of data to return for a subscription to data changes of the barometer sensor.
 *
 * @syscap SystemCapability.Sensors.Sensor.Lite
 * @famodelonly
 * @since 3
 * @deprecated since 8
 * @reserved ["liteWearable"]
 * @useinstead ohos.sensor/sensor.SensorId#BAROMETER
 */
export interface SubscribeBarometerOptions {
    /**
     * Callback invoked when the barometer sensor data changes.
     *
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead ohos.sensor/sensor#on
     */
    success: (data: BarometerResponse) => void;
    /**
     * Callback invoked when an API call fails.
     *
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead ohos.sensor/sensor#on
     */
    fail?: (data: string, code: number) => void;
}
/**
 * Defines a **HeartRateResponse** object.
 *
 * @permission ohos.permission.READ_HEALTH_DATA
 * @syscap SystemCapability.Sensors.Sensor.Lite
 * @famodelonly
 * @since 3
 * @deprecated since 8
 * @reserved ["liteWearable"]
 * @useinstead ohos.sensor/sensor#HeartRateResponse
 */
export interface HeartRateResponse {
    /**
     * Heart rate.
     *
     * @permission ohos.permission.READ_HEALTH_DATA
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead ohos.sensor/sensor#HeartRateResponse.heartRate
     */
    heartRate: number;
}
/**
 * Defines the type of data to return for a subscription to data changes of the heart rate sensor.
 *
 * @permission ohos.permission.READ_HEALTH_DATA
 * @syscap SystemCapability.Sensors.Sensor.Lite
 * @famodelonly
 * @since 3
 * @deprecated since 8
 * @reserved ["liteWearable"]
 * @useinstead ohos.sensor/sensor.SensorId#HEART_RATE
 */
export interface SubscribeHeartRateOptions {
    /**
     * Callback invoked when the heart rate sensor data changes. This callback is invoked every five seconds.
     *
     * @permission ohos.permission.READ_HEALTH_DATA
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead ohos.sensor/sensor#on
     */
    success: (data: HeartRateResponse) => void;
    /**
     * Callback invoked when an API call fails.
     *
     * @permission ohos.permission.READ_HEALTH_DATA
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead ohos.sensor/sensor#on
     */
    fail?: (data: string, code: number) => void;
}
/**
 * Specifies whether the device that houses the sensor is worn.
 *
 * @syscap SystemCapability.Sensors.Sensor.Lite
 * @famodelonly
 * @since 3
 * @deprecated since 8
 * @reserved ["liteWearable"]
 * @useinstead ohos.sensor/sensor#WearDetectionResponse
 */
export interface OnBodyStateResponse {
    /**
     * Boolean value indicating whether the device is worn. The value **true** indicates that the device is worn, and the
     * value **false** indicates the opposite.
     *
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead ohos.sensor/sensor#WearDetectionResponse.value
     */
    value: boolean;
}
/**
 * Defines the callback invoked upon change in the wearing state of the device that houses the sensor.
 *
 * @syscap SystemCapability.Sensors.Sensor.Lite
 * @famodelonly
 * @since 3
 * @deprecated since 8
 * @reserved ["liteWearable"]
 * @useinstead ohos.sensor/sensor.SensorId#WEAR_DETECTION
 */
export interface SubscribeOnBodyStateOptions {
    /**
     * Callback invoked when the wearing state of the device that houses the sensor is successfully obtained.
     *
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead ohos.sensor/sensor#on
     */
    success: (data: OnBodyStateResponse) => void;
    /**
     * Callback invoked when an API call fails.
     *
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead ohos.sensor/sensor#on
     */
    fail?: (data: string, code: number) => void;
}
/**
 * Defines the callback invoked upon change in the wearing state of the device that houses the sensor.
 *
 * @syscap SystemCapability.Sensors.Sensor.Lite
 * @famodelonly
 * @since 3
 * @deprecated since 8
 * @reserved ["liteWearable"]
 * @useinstead ohos.sensor/sensor.SensorId#WEAR_DETECTION
 */
export interface GetOnBodyStateOptions {
    /**
     * Callback upon a successful API call.
     *
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead ohos.sensor/sensor#once
     */
    success: (data: OnBodyStateResponse) => void;
    /**
     * Callback invoked when an API call fails.
     *
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead ohos.sensor/sensor#once
     */
    fail?: (data: string, code: number) => void;
    /**
     * Callback invoked when the API call is complete.
     *
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead ohos.sensor/sensor#once
     */
    complete?: () => void;
}
/**
 * Defines a **DeviceOrientationResponse** object.
 *
 * @syscap SystemCapability.Sensors.Sensor.Lite
 * @famodelonly
 * @since 6
 * @deprecated since 8
 * @reserved ["liteWearable"]
 * @useinstead ohos.sensor/sensor#OrientationResponse
 */
export interface DeviceOrientationResponse {
    /**
     * Rotation angle around the Z axis when the X/Y axis of the device coincides with the X/Y axis of the earth.
     *
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 6
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead ohos.sensor/sensor#OrientationResponse.alpha
     */
    alpha: number;
    /**
     * Rotation angle around the X axis when the Y/Z axis of the device coincides with the Y/Z axis of the earth.
     *
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 6
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead ohos.sensor/sensor#OrientationResponse.beta
     */
    beta: number;
    /**
     * Rotation angle around the Y axis when the X/Z axis of the device coincides with the X/Z axis of the earth.
     *
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 6
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead ohos.sensor/sensor#OrientationResponse.gamma
     */
    gamma: number;
}
/**
 * Defines the type of data to return for a subscription to data changes of the device orientation sensor.
 *
 * @syscap SystemCapability.Sensors.Sensor.Lite
 * @famodelonly
 * @since 6
 * @deprecated since 8
 * @reserved ["liteWearable"]
 * @useinstead ohos.sensor/sensor.SensorId#ORIENTATION
 */
export interface SubscribeDeviceOrientationOptions {
    /**
     * Interval at which the callback is invoked to return the device orientation sensor data.
     *
     * The default value is **normal**. The options are as follows:
     *
     * - **game**: called at an interval of 20 ms, which is applicable to gaming scenarios.
     * - **ui**: called at an interval of 60 ms, which is applicable to UI updating scenarios.
     * - **normal**: called at an interval of 200 ms, which is applicable to power-saving scenarios.
     *
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 6
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead ohos.sensor/sensor#Options.interval
     */
    interval: string;
    /**
     * Callback invoked when the device orientation sensor data changes.
     *
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 6
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead ohos.sensor/sensor#on
     */
    success: (data: DeviceOrientationResponse) => void;
    /**
     * Callback invoked when an API call fails.
     *
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 6
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead ohos.sensor/sensor#on
     */
    fail?: (data: string, code: number) => void;
}
/**
 * Defines a **GyroscopeResponse** object.
 *
 * @permission ohos.permission.GYROSCOPE
 * @syscap SystemCapability.Sensors.Sensor.Lite
 * @famodelonly
 * @since 6
 * @deprecated since 8
 * @reserved ["liteWearable"]
 * @useinstead ohos.sensor/sensor#GyroscopeResponse
 */
export interface GyroscopeResponse {
    /**
     * Rotation angular velocity of the X axis.
     *
     * @permission ohos.permission.GYROSCOPE
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 6
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead ohos.sensor/sensor#GyroscopeResponse.x
     */
    x: number;
    /**
     * Rotation angular velocity of the Y axis.
     *
     * @permission ohos.permission.GYROSCOPE
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 6
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead ohos.sensor/sensor#GyroscopeResponse.y
     */
    y: number;
    /**
     * Rotation angular velocity of the Z axis.
     *
     * @permission ohos.permission.GYROSCOPE
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 6
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead ohos.sensor/sensor#GyroscopeResponse.z
     */
    z: number;
}
/**
 * Defines the type of data to return for a subscription to data changes of the gyroscope sensor.
 *
 * @permission ohos.permission.GYROSCOPE
 * @syscap SystemCapability.Sensors.Sensor.Lite
 * @famodelonly
 * @since 6
 * @deprecated since 8
 * @reserved ["liteWearable"]
 * @useinstead ohos.sensor/sensor.SensorId#GYROSCOPE
 */
export interface SubscribeGyroscopeOptions {
    /**
     * Interval at which the callback is invoked to return the gyroscope sensor data.
     *
     * The default value is **normal**. The options are as follows:
     *
     * - **game**: called at an interval of 20 ms, which is applicable to gaming scenarios.
     * - **ui**: called at an interval of 60 ms, which is applicable to UI updating scenarios.
     * - **normal**: called at an interval of 200 ms, which is applicable to power-saving scenarios.
     *
     * @permission ohos.permission.GYROSCOPE
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 6
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead ohos.sensor/sensor#Options.interval
     */
    interval: string;
    /**
     * Callback invoked when the gyroscope sensor data changes.
     *
     * @permission ohos.permission.GYROSCOPE
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 6
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead ohos.sensor/sensor#on
     */
    success: (data: GyroscopeResponse) => void;
    /**
     * Callback invoked when an API call fails.
     *
     * @permission ohos.permission.GYROSCOPE
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 6
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead ohos.sensor/sensor#on
     */
    fail?: (data: string, code: number) => void;
}
/**
 *
 * @syscap SystemCapability.Sensors.Sensor.Lite
 * @famodelonly
 * @since 6
 * @deprecated since 8
 * @reserved ["liteWearable"]
 * @useinstead ohos.sensor/sensor
 */
export default class Sensor {
    /**
     * Subscribes to data changes of the acceleration sensor. If this API is called multiple times for the same
     * application, the last call takes effect.
     *
     * > **NOTE**
     * >
     * > Except for lite wearables, You are advised to use
     * > [ACCELEROMETER]{@link @ohos.sensor:sensor.on(type: SensorType.SENSOR_TYPE_ID_ACCELEROMETER, callback: Callback<AccelerometerResponse>, options?: Options)}
     * > instead. since API Version 8.
     *
     * @permission ohos.permission.ACCELEROMETER
     * @param { subscribeAccelerometerOptions } options - Type of data to return.
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead @ohos.sensor:sensor.on(type: SensorType.SENSOR_TYPE_ID_ACCELEROMETER, callback: Callback<AccelerometerResponse>, options?: Options)
     */
    static subscribeAccelerometer(options: subscribeAccelerometerOptions): void;
    /**
     * Unsubscribes from data changes of the acceleration sensor.
     *
     * > **NOTE**
     * >
     * > Except for lite wearables, You are advised to use
     * > [ACCELEROMETER]{@link @ohos.sensor:sensor.off(type: SensorType.SENSOR_TYPE_ID_ACCELEROMETER, callback?: Callback<AccelerometerResponse>)}
     * > instead. since API Version 8.
     *
     * @permission ohos.permission.ACCELEROMETER
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead @ohos.sensor:sensor.off(type: SensorType.SENSOR_TYPE_ID_ACCELEROMETER, callback?: Callback<AccelerometerResponse>)
     */
    static unsubscribeAccelerometer(): void;
    /**
     * Subscribes to data changes of the compass sensor. If this API is called multiple times for the same application,
     * the last call takes effect.
     *
     * > **NOTE**
     * >
     * > Except for lite wearables, You are advised to use
     * > [ORIENTATION]{@link @ohos.sensor:sensor.on(type: SensorType.SENSOR_TYPE_ID_ORIENTATION, callback: Callback<OrientationResponse>, options?: Options)}
     * > since API Version 8.
     *
     * @param { SubscribeCompassOptions } options - Type of data to return.
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead ohos.sensor/sensor.SensorId#ORIENTATION
     */
    static subscribeCompass(options: SubscribeCompassOptions): void;
    /**
     * Unsubscribes from data changes of the compass sensor.
     *
     * > **NOTE**
     * >
     * > Except for lite wearables, You are advised to use
     * > [ORIENTATION]{@link @ohos.sensor:sensor.off(type: SensorType.SENSOR_TYPE_ID_ORIENTATION, callback?: Callback<OrientationResponse>)}
     * > instead.
     *
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead @ohos.sensor:sensor.off(type: SensorType.SENSOR_TYPE_ID_ORIENTATION, callback?: Callback<OrientationResponse>)
     */
    static unsubscribeCompass(): void;
    /**
     * Subscribes to data changes of the proximity sensor. If this API is called multiple times for the same application,
     * the last call takes effect.
     *
     * > **NOTE**
     * >
     * > Except for lite wearables, You are advised to use
     * > [PROXIMITY]{@link @ohos.sensor:sensor.on(type: SensorType.SENSOR_TYPE_ID_PROXIMITY, callback: Callback<ProximityResponse>, options?: Options)}
     * >  instead. since API Version 8.
     *
     * @param { SubscribeProximityOptions } options - Type of data to return.
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead ohos.sensor/sensor.SensorId#PROXIMITY
     */
    static subscribeProximity(options: SubscribeProximityOptions): void;
    /**
     * Unsubscribes from data changes of the proximity sensor.
     *
     * > **NOTE**
     * >
     * > Except for lite wearables, You are advised to use
     * > [PROXIMITY]{@link @ohos.sensor:sensor.off(type: SensorType.SENSOR_TYPE_ID_PROXIMITY, callback?: Callback<ProximityResponse>)}
     * >  instead. since API Version 8.
     *
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead ohos.sensor/sensor.SensorId#PROXIMITY
     */
    static unsubscribeProximity(): void;
    /**
     * Subscribes to data changes of the ambient light sensor. If this API is called multiple times, the last call takes
     * effect.
     *
     * > **NOTE**
     * >
     * > Except for lite wearables, You are advised to use
     * > [AMBIENT_LIGHT]{@link @ohos.sensor:sensor.on(type: SensorType.SENSOR_TYPE_ID_AMBIENT_LIGHT, callback: Callback<LightResponse>, options?: Options)}
     * > since API Version 8.
     *
     * @param { SubscribeLightOptions } options - Type of data to return.
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead ohos.sensor/sensor.SensorId#AMBIENT_LIGHT
     */
    static subscribeLight(options: SubscribeLightOptions): void;
    /**
     * Unsubscribes from data changes of the ambient light sensor.
     *
     * > **NOTE**
     * >
     * > Except for lite wearables, You are advised to use
     * > [AMBIENT_LIGHT]{@link @ohos.sensor:sensor.off(type: SensorType.SENSOR_TYPE_ID_AMBIENT_LIGHT, callback?: Callback<LightResponse>)}
     * > instead. since API Version 8.
     *
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead @ohos.sensor:sensor.off(type: SensorType.SENSOR_TYPE_ID_AMBIENT_LIGHT, callback?: Callback<LightResponse>)
     */
    static unsubscribeLight(): void;
    /**
     * Subscribes to data changes of the step counter sensor. If this API is called multiple times for the same
     * application, the last call takes effect.
     *
     * > **NOTE**
     * >
     * > Except for lite wearables, You are advised to use
     * > [PEDOMETER]{@link @ohos.sensor:sensor.on(type: SensorType.SENSOR_TYPE_ID_PEDOMETER, callback: Callback<PedometerResponse>, options?: Options)}
     * > instead. since API Version 8.
     *
     * @permission ohos.permission.ACTIVITY_MOTION
     * @param { SubscribeStepCounterOptions } options - Type of data to return.
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead @ohos.sensor:sensor.on(type: SensorType.SENSOR_TYPE_ID_PEDOMETER, callback: Callback<PedometerResponse>, options?: Options)
     */
    static subscribeStepCounter(options: SubscribeStepCounterOptions): void;
    /**
     * Unsubscribes from data changes of the step counter sensor.
     *
     * > **NOTE**
     * >
     * > Except for lite wearables, You are advised to use
     * > [PEDOMETER]{@link @ohos.sensor:sensor.off(type: SensorType.SENSOR_TYPE_ID_PEDOMETER, callback?: Callback<PedometerResponse>)}
     * > instead. since API Version 8.
     *
     * @permission ohos.permission.ACTIVITY_MOTION
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead @ohos.sensor:sensor.off(type: SensorType.SENSOR_TYPE_ID_PEDOMETER, callback?: Callback<PedometerResponse>)
     */
    static unsubscribeStepCounter(): void;
    /**
     * Subscribes to data changes of the barometer sensor. If this API is called multiple times for the same application,
     * the last call takes effect.
     *
     * > **NOTE**
     * >
     * > Except for lite wearables, You are advised to use
     * > [BAROMETER]{@link @ohos.sensor:sensor.on(type: SensorType.SENSOR_TYPE_ID_BAROMETER, callback: Callback<BarometerResponse>, options?: Options)}
     * > instead. since API Version 8.
     *
     * @param { SubscribeBarometerOptions } options - Type of data to return.
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead @ohos.sensor:sensor.on(type: SensorType.SENSOR_TYPE_ID_BAROMETER, callback: Callback<BarometerResponse>, options?: Options)
     */
    static subscribeBarometer(options: SubscribeBarometerOptions): void;
    /**
     * Unsubscribes from data changes of the barometer sensor.
     *
     * > **NOTE**
     * >
     * > Except for lite wearables, You are advised to use
     * > [BAROMETER]{@link @ohos.sensor:sensor.off(type: SensorType.SENSOR_TYPE_ID_BAROMETER, callback?: Callback<BarometerResponse>)}
     * > instead. since API Version 8.
     *
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead @ohos.sensor:sensor.off(type: SensorType.SENSOR_TYPE_ID_BAROMETER, callback?: Callback<BarometerResponse>)
     */
    static unsubscribeBarometer(): void;
    /**
     * Subscribes to data changes of the heart rate sensor. If this API is called multiple times for the same application,
     * the last call takes effect.
     *
     * > **NOTE**
     * >
     * > Except for lite wearables, You are advised to use
     * > [HEART_RATE]{@link @ohos.sensor:sensor.on(type: SensorType.SENSOR_TYPE_ID_HEART_RATE, callback: Callback<HeartRateResponse>, options?: Options)}
     * > instead. since API Version 8.
     *
     * @permission ohos.permission.READ_HEALTH_DATA
     * @param { SubscribeHeartRateOptions } options - Type of data to return.
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead @ohos.sensor:sensor.on(type: SensorType.SENSOR_TYPE_ID_HEART_RATE, callback: Callback<HeartRateResponse>, options?: Options)
     */
    static subscribeHeartRate(options: SubscribeHeartRateOptions): void;
    /**
     * Unsubscribes from data changes of the heart rate sensor.
     *
     * > **NOTE**
     * >
     * > Except for lite wearables, You are advised to use
     * > [HEART_RATE]{@link @ohos.sensor:sensor.off(type: SensorType.SENSOR_TYPE_ID_HEART_RATE, callback?: Callback<HeartRateResponse>)}
     * > instead. since API Version 8.
     *
     * @permission ohos.permission.READ_HEALTH_DATA
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead @ohos.sensor:sensor.off(type: SensorType.SENSOR_TYPE_ID_HEART_RATE, callback?: Callback<HeartRateResponse>)
     */
    static unsubscribeHeartRate(): void;
    /**
     * Subscribes to wearing status changes of a wearable device. If this API is called multiple times for the same
     * application, the last call takes effect.
     *
     * > **NOTE**
     * >
     * > Except for lite wearables, You are advised to use
     * > [WEAR_DETECTION]{@link @ohos.sensor:sensor.on(type: SensorType.SENSOR_TYPE_ID_WEAR_DETECTION, callback: Callback<WearDetectionResponse>, options?: Options)}
     * > instead. since API Version 8.
     *
     * @param { SubscribeOnBodyStateOptions } options - Type of data to return.
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead @ohos.sensor:sensor.on(type: SensorType.SENSOR_TYPE_ID_WEAR_DETECTION, callback: Callback<WearDetectionResponse>, options?: Options)
     */
    static subscribeOnBodyState(options: SubscribeOnBodyStateOptions): void;
    /**
     * Unsubscribes from wearing status changes of a wearable device.
     *
     * > **NOTE**
     * >
     * > Except for lite wearables, You are advised to use
     * > [WEAR_DETECTION]{@link @ohos.sensor:sensor.off(type: SensorType.SENSOR_TYPE_ID_WEAR_DETECTION, callback?: Callback<WearDetectionResponse>)}
     * > instead. since API Version 8.
     *
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead @ohos.sensor:sensor.off(type: SensorType.SENSOR_TYPE_ID_WEAR_DETECTION, callback?: Callback<WearDetectionResponse>)
     */
    static unsubscribeOnBodyState(): void;
    /**
     * Obtains the wearing state of a wearable device.
     *
     * @param { GetOnBodyStateOptions } options - Callback invoked when obtaining the wearing state of the device that
     *     houses the sensor.
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead ohos.sensor/sensor.SensorId#WEAR_DETECTION
     */
    static getOnBodyState(options: GetOnBodyStateOptions): void;
    /**
     * Subscribes to data changes of the device orientation sensor.
     *
     * If this API is called multiple times for the same application, the last call takes effect. However, this API cannot
     * be called multiple times in one click event.
     *
     * > **NOTE**
     * >
     * > Except for lite wearables, You are advised to use
     * > [ORIENTATION]{@link @ohos.sensor:sensor.on(type: SensorType.SENSOR_TYPE_ID_ORIENTATION, callback: Callback<OrientationResponse>, options?: Options)}
     * > instead. since API Version 8.
     *
     * @param { SubscribeDeviceOrientationOptions } options - Type of data to return.
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 6
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead @ohos.sensor:sensor.on(type: SensorType.SENSOR_TYPE_ID_ORIENTATION, callback: Callback<OrientationResponse>, options?: Options)
     */
    static subscribeDeviceOrientation(options: SubscribeDeviceOrientationOptions): void;
    /**
     * Unsubscribes from data changes of the device orientation sensor.
     *
     * > **NOTE**
     * >
     * > Except for lite wearables, You are advised to use
     * > [ORIENTATION]{@link @ohos.sensor:sensor.off(type: SensorType.SENSOR_TYPE_ID_ORIENTATION, callback?: Callback<OrientationResponse>)}
     * > instead. since API Version 8.
     *
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 6
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead @ohos.sensor:sensor.off(type: SensorType.SENSOR_TYPE_ID_ORIENTATION, callback?: Callback<OrientationResponse>)
     */
    static unsubscribeDeviceOrientation(): void;
    /**
     * Subscribes to data changes of the gyroscope sensor.
     *
     * If this API is called multiple times for the same application, the last call takes effect. However, this API cannot
     * be called multiple times in one click event.
     *
     * > **NOTE**
     * >
     * > Except for lite wearables, You are advised to use
     * > [GYROSCOPE]{@link @ohos.sensor:sensor.on(type: SensorType.SENSOR_TYPE_ID_GYROSCOPE, callback: Callback<GyroscopeResponse>, options?: Options)}
     * > instead. since API Version 8.
     *
     * @permission ohos.permission.GYROSCOPE
     * @param { SubscribeGyroscopeOptions } options - Type of data to return.
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 6
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead @ohos.sensor:sensor.on(type: SensorType.SENSOR_TYPE_ID_GYROSCOPE, callback: Callback<GyroscopeResponse>, options?: Options)
     */
    static subscribeGyroscope(options: SubscribeGyroscopeOptions): void;
    /**
     * Unsubscribes from data changes of the gyroscope sensor.
     *
     * > **NOTE**
     * >
     * > Except for lite wearables, You are advised to use
     * > [GYROSCOPE]{@link @ohos.sensor:sensor.off(type: SensorType.SENSOR_TYPE_ID_GYROSCOPE, callback?: Callback<GyroscopeResponse>)}
     * > instead. since API Version 8.
     *
     * @permission ohos.permission.GYROSCOPE
     * @syscap SystemCapability.Sensors.Sensor.Lite
     * @famodelonly
     * @since 6
     * @deprecated since 8
     * @reserved ["liteWearable"]
     * @useinstead @ohos.sensor:sensor.off(type: SensorType.SENSOR_TYPE_ID_GYROSCOPE, callback?: Callback<GyroscopeResponse>)
     */
    static unsubscribeGyroscope(): void;
}

```
