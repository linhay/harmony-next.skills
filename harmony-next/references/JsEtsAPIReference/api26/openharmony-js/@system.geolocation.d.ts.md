# @system.geolocation.d.ts

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
 * @kit LocationKit
 */
/**
 * @syscap SystemCapability.Location.Location.Lite
 * @famodelonly
 * @since 3
 * @deprecated since 9
 * @reserved ["liteWearable"]
 * @useinstead ohos.geoLocationManager/geoLocationManager.Location
 */
export interface GeolocationResponse {
    /**
     * Longitude.
     * @syscap SystemCapability.Location.Location.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 9
     * @reserved ["liteWearable"]
     * @useinstead ohos.geoLocationManager/geoLocationManager.Location#longitude
     */
    longitude: number;
    /**
     * Latitude.
     * @syscap SystemCapability.Location.Location.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 9
     * @reserved ["liteWearable"]
     * @useinstead ohos.geoLocationManager/geoLocationManager.Location#latitude
     */
    latitude: number;
    /**
     * Altitude.
     * @syscap SystemCapability.Location.Location.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 9
     * @reserved ["liteWearable"]
     * @useinstead ohos.geoLocationManager/geoLocationManager.Location#altitude
     */
    altitude: number;
    /**
     * Location accuracy.
     * @syscap SystemCapability.Location.Location.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 9
     * @reserved ["liteWearable"]
     * @useinstead ohos.geoLocationManager/geoLocationManager.Location#accuracy
     */
    accuracy: number;
    /**
     * Time when the location is obtained.
     * @syscap SystemCapability.Location.Location.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 9
     * @reserved ["liteWearable"]
     * @useinstead ohos.geoLocationManager/geoLocationManager.Location#timeStamp
     */
    time: number;
}
/**
 * @permission ohos.permission.LOCATION
 * @syscap SystemCapability.Location.Location.Lite
 * @famodelonly
 * @since 3
 * @deprecated since 9
 * @reserved ["liteWearable"]
 * @useinstead ohos.geoLocationManager/geoLocationManager.CurrentLocationRequest
 */
export interface GetLocationOption {
    /**
     * Timeout duration, in milliseconds.
     * For the rich device, the default value is 30000.
     * For the lite wearable device, the default value is 180000.
     * The timeout duration is necessary in case no result is returned if the request to obtain the geographic location is rejected for the lack of the required permission, weak positioning signal, or incorrect location settings. After the timeout duration expires, the fail function will be called.
     * The value is a 32-digit positive integer.
     * If the value set is less than or equal to 0, the default value will be used.
     * @syscap SystemCapability.Location.Location.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 9
     * @reserved ["liteWearable"]
     * @useinstead ohos.geoLocationManager/geoLocationManager.CurrentLocationRequest#timeoutMs
     */
    timeout?: number;
    /**
     * Coordinate system type. Available types can be obtained using getSupportedCoordTypes.
     * The default type is wgs84.
     * @syscap SystemCapability.Location.Location.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 9
     * @reserved ["liteWearable"]
     */
    coordType?: string;
    /**
     * Called when the geographic location is obtained.
     * @syscap SystemCapability.Location.Location.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 9
     * @reserved ["liteWearable"]
     * @useinstead ohos.geoLocationManager/geoLocationManager.getCurrentLocation#callback
     */
    success?: (data: GeolocationResponse) => void;
    /**
     * Called when the location types fail to be obtained
     * @syscap SystemCapability.Location.Location.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 9
     * @reserved ["liteWearable"]
     * @useinstead ohos.geoLocationManager/geoLocationManager.getCurrentLocation#callback
     */
    fail?: (data: string, code: number) => void;
    /**
     * Called when the execution is completed.
     * @syscap SystemCapability.Location.Location.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 9
     * @reserved ["liteWearable"]
     * @useinstead ohos.geoLocationManager/geoLocationManager.getCurrentLocation#callback
     */
    complete?: () => void;
}
/**
 * @syscap SystemCapability.Location.Location.Lite
 * @famodelonly
 * @since 3
 * @deprecated since 9
 * @reserved ["liteWearable"]
 */
export interface GetLocationTypeResponse {
    /**
     * @syscap SystemCapability.Location.Location.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 9
     * @reserved ["liteWearable"]
     */
    types: Array<string>;
}
/**
 * @syscap SystemCapability.Location.Location.Lite
 * @famodelonly
 * @since 3
 * @deprecated since 9
 * @reserved ["liteWearable"]
 */
export interface GetLocationTypeOption {
    /**
     * Called when the location types are obtained.
     * @syscap SystemCapability.Location.Location.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 9
     * @reserved ["liteWearable"]
     */
    success?: (data: GetLocationTypeResponse) => void;
    /**
     * Called when the location types fail to be obtained.
     * @syscap SystemCapability.Location.Location.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 9
     * @reserved ["liteWearable"]
     */
    fail?: (data: string, code: number) => void;
    /**
     * Called when the execution is completed.
     * @syscap SystemCapability.Location.Location.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 9
     * @reserved ["liteWearable"]
     */
    complete?: () => void;
}
/**
 * @permission ohos.permission.LOCATION
 * @syscap SystemCapability.Location.Location.Lite
 * @famodelonly
 * @since 3
 * @deprecated since 9
 * @reserved ["liteWearable"]
 * @useinstead ohos.geoLocationManager/geoLocationManager.LocationRequest
 */
export interface SubscribeLocationOption {
    /**
     * Coordinate system type. Available types can be obtained using getSupportedCoordTypes.
     * The default type is wgs84.
     * @syscap SystemCapability.Location.Location.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 9
     * @reserved ["liteWearable"]
     */
    coordType?: string;
    /**
     * Called whenever the geographical location changes.
     * @syscap SystemCapability.Location.Location.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 9
     * @reserved ["liteWearable"]
     */
    success: (data: GeolocationResponse) => void;
    /**
     * Called when the listening fails.
     * @syscap SystemCapability.Location.Location.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 9
     * @reserved ["liteWearable"]
     */
    fail?: (data: string, code: number) => void;
}
/**
 * @syscap SystemCapability.Location.Location.Lite
 * @famodelonly
 * @since 3
 * @deprecated since 9
 * @reserved ["liteWearable"]
 * @useinstead ohos.geoLocationManager/geoLocationManager
 */
export default class Geolocation {
    /**
     * Obtains the geographic location.
     * @permission ohos.permission.LOCATION
     * @param options Options.
     * @syscap SystemCapability.Location.Location.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 9
     * @reserved ["liteWearable"]
     * @useinstead ohos.geoLocationManager/geoLocationManager.getCurrentLocation
     */
    static getLocation(options?: GetLocationOption): void;
    /**
     * Obtains the location types supported by the system.
     * @param options Options.
     * @syscap SystemCapability.Location.Location.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 9
     * @reserved ["liteWearable"]
     */
    static getLocationType(options?: GetLocationTypeOption): void;
    /**
     * Listens to the geographical location. If this method is called multiple times, the last call takes effect.
     * @permission ohos.permission.LOCATION
     * @param options Options.
     * @syscap SystemCapability.Location.Location.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 9
     * @reserved ["liteWearable"]
     * @useinstead ohos.geoLocationManager/geoLocationManager.on#event:locationChange
     */
    static subscribe(options: SubscribeLocationOption): void;
    /**
     * Cancels listening to the geographical location.
     * @permission ohos.permission.LOCATION
     * @syscap SystemCapability.Location.Location.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 9
     * @reserved ["liteWearable"]
     * @useinstead ohos.geoLocationManager/geoLocationManager.off#event:locationChange
     */
    static unsubscribe(): void;
    /**
     * Obtains the supported coordinate system types.
     * @returns A string array of the supported coordinate system types, for example, ['wgs84'].
     * @syscap SystemCapability.Location.Location.Lite
     * @famodelonly
     * @since 3
     * @deprecated since 9
     * @reserved ["liteWearable"]
     */
    static getSupportedCoordTypes(): Array<string>;
}

```
