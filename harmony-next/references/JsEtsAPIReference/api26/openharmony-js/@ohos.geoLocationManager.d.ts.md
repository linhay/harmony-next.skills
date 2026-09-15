# @ohos.geoLocationManager.d.ts

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
import { AsyncCallback, Callback } from './@ohos.base';
import { WantAgent } from './@ohos.wantAgent';
import { NotificationRequest } from './notification/notificationRequest';
/**
 * Provides interfaces for acquiring location information, managing location switches,
 * geocoding, reverse geocoding, country code, fencing and other functions.
 *
 * @syscap SystemCapability.Location.Location.Core [since 11]
 * @crossplatform [since 22]
 * @atomicservice [since 11]
 * @since 9
 */
declare namespace geoLocationManager {
    /**
     * Subscribe location changed.
     * You are advised to use the {@link onLocationChange} instead.
     *
     * @permission ohos.permission.APPROXIMATELY_LOCATION
     * @param { 'locationChange' } type - Indicates the location service event to be subscribed to.
     * @param { LocationRequest } request - Indicates the location request parameters. [since 9 - 11]
     * @param { LocationRequest | ContinuousLocationRequest } request - Indicates the location request
     *     parameters. [since 12]
     * @param { Callback<Location> } callback - Indicates the callback for reporting the location result.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters
     *     are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call
     *     ${geoLocationManager.on('locationChange')} due to limited device capabilities.
     * @throws { BusinessError } 3301000 - The location service is unavailable.
     * @throws { BusinessError } 3301100 - The location switch is off.
     * @throws { BusinessError } 3301200 - Failed to obtain the geographical location. [since 9 - 17]
     * @syscap SystemCapability.Location.Location.Core
     * @crossplatform [since 22]
     * @atomicservice [since 11]
     * @since 9
     */
    function on(type: 'locationChange', request: LocationRequest | ContinuousLocationRequest, callback: Callback<Location>): void;
    /**
     * Subscribe location changed.
     *
     * @permission ohos.permission.APPROXIMATELY_LOCATION
     * @param { LocationRequest | ContinuousLocationRequest } request - Indicates the location request
     *     parameters.
     * @param { Callback<Location> } callback - Indicates the callback for reporting the location result.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types;
     *     3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported.
     *     Failed to call ${geoLocationManager.onLocationChange} due to limited device capabilities.
     * @throws { BusinessError } 3301000 - The location service is unavailable.
     * @throws { BusinessError } 3301100 - The location switch is off.
     * @syscap SystemCapability.Location.Location.Core
     * @since 26.0.0
     */
    function onLocationChange(request: LocationRequest | ContinuousLocationRequest, callback: Callback<Location>): void;
    /**
     * Unsubscribe location changed.
     * You are advised to use the {@link offLocationChange} instead.
     *
     * @permission ohos.permission.APPROXIMATELY_LOCATION [since 9 - 24]
     * @param { 'locationChange' } type - Indicates the location service event to be subscribed to.
     * @param { Callback<Location> } [callback] - Indicates the callback for reporting the location result.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the
     *     permission required to call the API. Introduced in API 9 and will not be threw above
     *     API 24. [since 9 - 24]
     * @throws { BusinessError } 801 - Capability not supported. Failed to call
     *     ${geoLocationManager.off('locationChange')} due to limited device capabilities.
     * @throws { BusinessError } 3301000 - The location service is unavailable.
     * @throws { BusinessError } 3301100 - The location switch is off.
     *     Introduced in API 9 and will not be threw above API 17. [since 9 - 17]
     * @throws { BusinessError } 3301200 - Failed to obtain the geographical location.
     *     Introduced in API 9 and will not be threw above API 17. [since 9 - 17]
     * @syscap SystemCapability.Location.Location.Core
     * @crossplatform [since 22]
     * @atomicservice [since 11]
     * @since 9
     */
    function off(type: 'locationChange', callback?: Callback<Location>): void;
    /**
     * Unsubscribe location changed.
     *
     * @param { Callback<Location> } [callback] - Indicates the callback for reporting the location result.
     * @throws { BusinessError } 801 - Capability not supported.
     *     Failed to call ${geoLocationManager.offLocationChange} due to limited device capabilities.
     * @throws { BusinessError } 3301000 - The location service is unavailable.
     * @syscap SystemCapability.Location.Location.Core
     * @since 26.0.0
     */
    function offLocationChange(callback?: Callback<Location>): void;
    /**
     * Subscribe continuous location error changed.
     *
     * @permission ohos.permission.APPROXIMATELY_LOCATION
     * @param { 'locationError' } type - Indicates the location service event to be subscribed to.
     * @param { Callback<LocationError> } callback - Indicates the callback for reporting the
     *     continuous location error.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not
     *     have the permission required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters
     *     are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call
     *     ${geoLocationManager.on('locationError')} due to limited device capabilities.
     * @throws { BusinessError } 3301000 - The location service is unavailable.
     * @syscap SystemCapability.Location.Location.Core
     * @crossplatform [since 22]
     * @atomicservice
     * @since 12
     */
    function on(type: 'locationError', callback: Callback<LocationError>): void;
    /**
     * Unsubscribe continuous location error changed.
     *
     * @permission ohos.permission.APPROXIMATELY_LOCATION
     * @param { 'locationError' } type - Indicates the location service event to be subscribed to.
     * @param { Callback<LocationError> } [callback] - Indicates the callback for reporting the continuous
     *     location error.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the
     *     permission required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are
     *     left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call
     *     ${geoLocationManager.off('locationError')} due to limited device capabilities.
     * @throws { BusinessError } 3301000 - The location service is unavailable.
     * @syscap SystemCapability.Location.Location.Core
     * @crossplatform [since 22]
     * @atomicservice
     * @since 12
     */
    function off(type: 'locationError', callback?: Callback<LocationError>): void;
    /**
     * Subscribe location switch changed.
     *
     * @param { 'locationEnabledChange' } type - Indicates the location service event to be subscribed to.
     * @param { Callback<boolean> } callback - Indicates the callback for reporting the location switch status.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left
     *     unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call
     *     ${geoLocationManager.on('locationEnabledChange')} due to limited device capabilities.
     * @throws { BusinessError } 3301000 - The location service is unavailable.
     * @syscap SystemCapability.Location.Location.Core
     * @crossplatform [since 22]
     * @since 9
     */
    function on(type: 'locationEnabledChange', callback: Callback<boolean>): void;
    /**
     * Unsubscribe location switch changed.
     *
     * @param { 'locationEnabledChange' } type - Indicates the location service event to be subscribed to.
     * @param { Callback<boolean> } [callback] - Indicates the callback for reporting the location switch status.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left
     *     unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call
     *     ${geoLocationManager.off('locationEnabledChange')} due to limited device capabilities.
     * @throws { BusinessError } 3301000 - The location service is unavailable.
     * @syscap SystemCapability.Location.Location.Core
     * @crossplatform [since 22]
     * @since 9
     */
    function off(type: 'locationEnabledChange', callback?: Callback<boolean>): void;
    /**
     * Subscribe to cache GNSS locations update messages.
     *
     * @permission ohos.permission.APPROXIMATELY_LOCATION
     * @param { 'cachedGnssLocationsChange' } type - Indicates the location service event to be subscribed to.
     * @param { CachedGnssLocationsRequest } request - Indicates the cached GNSS locations request parameters.
     * @param { Callback<Array<Location>> } callback - Indicates the callback for reporting the cached GNSS locations.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call
     *     ${geoLocationManager.on('cachedGnssLocationsChange')} due to limited device capabilities.
     * @throws { BusinessError } 3301000 - The location service is unavailable.
     * @throws { BusinessError } 3301100 - The location switch is off.
     * @throws { BusinessError } 3301200 - Failed to obtain the geographical location. [since 9 - 17]
     * @syscap SystemCapability.Location.Location.Gnss
     * @crossplatform [since 22]
     * @since 9
     */
    function on(type: 'cachedGnssLocationsChange', request: CachedGnssLocationsRequest, callback: Callback<Array<Location>>): void;
    /**
     * Unsubscribe to cache GNSS locations update messages.
     *
     * @permission ohos.permission.APPROXIMATELY_LOCATION
     * @param { 'cachedGnssLocationsChange' } type - Indicates the location service event to be subscribed to.
     * @param { Callback<Array<Location>> } [callback] - Indicates the callback for reporting the cached gnss locations.
     * @throws { BusinessError } 201 - Permission verification failed. The application
     *     does not have the permission required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory
     *     parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call
     *     ${geoLocationManager.off('cachedGnssLocationsChange')} due to limited device capabilities.
     * @throws { BusinessError } 3301000 - The location service is unavailable.
     * @throws { BusinessError } 3301100 - The location switch is off.
     * @throws { BusinessError } 3301200 - Failed to obtain the geographical location. [since 9 - 17]
     * @syscap SystemCapability.Location.Location.Gnss
     * @crossplatform [since 22]
     * @since 9
     */
    function off(type: 'cachedGnssLocationsChange', callback?: Callback<Array<Location>>): void;
    /**
     * Subscribe satellite status changed.
     *
     * @permission ohos.permission.APPROXIMATELY_LOCATION
     * @param { 'satelliteStatusChange' } type - Indicates the location service event to be subscribed to.
     * @param { Callback<SatelliteStatusInfo> } callback - Indicates the callback for reporting the satellite status.
     * @throws { BusinessError } 201 - Permission verification failed. The application
     *     does not have the permission required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory
     *     parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call
     *     ${geoLocationManager.on('satelliteStatusChange')} due to limited device capabilities.
     * @throws { BusinessError } 3301000 - The location service is unavailable.
     * @throws { BusinessError } 3301100 - The location switch is off.
     * @syscap SystemCapability.Location.Location.Gnss
     * @crossplatform [since 22]
     * @since 9
     */
    function on(type: 'satelliteStatusChange', callback: Callback<SatelliteStatusInfo>): void;
    /**
     * Unsubscribe satellite status changed.
     *
     * @permission ohos.permission.APPROXIMATELY_LOCATION
     * @param { 'satelliteStatusChange' } type - Indicates the location service event to be subscribed to.
     * @param { Callback<SatelliteStatusInfo> } [callback] - Indicates the callback for reporting the satellite status.
     * @throws { BusinessError } 201 - Permission verification failed. The application
     *     does not have the permission required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory
     *     parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call
     *     ${geoLocationManager.off('satelliteStatusChange')} due to limited device capabilities.
     * @throws { BusinessError } 3301000 - The location service is unavailable.
     * @throws { BusinessError } 3301100 - The location switch is off.
     * @syscap SystemCapability.Location.Location.Gnss
     * @crossplatform [since 22]
     * @since 9
     */
    function off(type: 'satelliteStatusChange', callback?: Callback<SatelliteStatusInfo>): void;
    /**
     * Subscribe nmea message changed.
     *
     * @permission ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION
     * @param { 'nmeaMessage' } type - Indicates the location service event to be subscribed to.
     * @param { Callback<string> } callback - Indicates the callback for reporting the nmea message.
     * @throws { BusinessError } 201 - Permission verification failed. The application
     *     does not have the permission required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory
     *     parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call
     *     ${geoLocationManager.on('nmeaMessage')} due to limited device capabilities.
     * @throws { BusinessError } 3301000 - The location service is unavailable.
     * @throws { BusinessError } 3301100 - The location switch is off.
     * @syscap SystemCapability.Location.Location.Gnss
     * @crossplatform [since 22]
     * @since 9
     */
    function on(type: 'nmeaMessage', callback: Callback<string>): void;
    /**
     * Unsubscribe nmea message changed.
     *
     * @permission ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION
     * @param { 'nmeaMessage' } type - Indicates the location service event to be subscribed to.
     * @param { Callback<string> } [callback] - Indicates the callback for reporting the nmea message.
     * @throws { BusinessError } 201 - Permission verification failed. The application
     *     does not have the permission required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory
     *     parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call
     *     ${geoLocationManager.off('nmeaMessage')} due to limited device capabilities.
     * @throws { BusinessError } 3301000 - The location service is unavailable.
     * @throws { BusinessError } 3301100 - The location switch is off.
     * @syscap SystemCapability.Location.Location.Gnss
     * @crossplatform [since 22]
     * @since 9
     */
    function off(type: 'nmeaMessage', callback?: Callback<string>): void;
    /**
     * Add a geofence and subscribe geofence status changed.
     *
     * @permission ohos.permission.APPROXIMATELY_LOCATION
     * @param { 'gnssFenceStatusChange' } type - Indicates the location service event to be subscribed to.
     * @param { GeofenceRequest } request - Indicates the Geofence configuration parameters.
     * @param { WantAgent } want - Indicates which ability to start when the geofence event is triggered.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call ${geoLocationManager.on('
     *     gnssFenceStatusChange')} due to limited device capabilities.
     * @throws { BusinessError } 3301000 - The location service is unavailable.
     * @throws { BusinessError } 3301100 - The location switch is off.
     * @throws { BusinessError } 3301600 - Failed to operate the geofence.
     * @syscap SystemCapability.Location.Location.Geofence
     * @since 9
     */
    function on(type: 'gnssFenceStatusChange', request: GeofenceRequest, want: WantAgent): void;
    /**
     * Remove a geofence and unsubscribe geofence status changed.
     *
     * @permission ohos.permission.APPROXIMATELY_LOCATION [since 9 - 24]
     * @param { 'gnssFenceStatusChange' } type - Indicates the location service event to be subscribed to.
     * @param { GeofenceRequest } request - Indicates the Geofence configuration parameters.
     * @param { WantAgent } want - Indicates which ability to start when the geofence event is triggered.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API. [since 9 - 24]
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call
     *     ${geoLocationManager.off('gnssFenceStatusChange')} due to limited device capabilities.
     * @throws { BusinessError } 3301000 - The location service is unavailable.
     * @throws { BusinessError } 3301100 - The location switch is off.
     * @throws { BusinessError } 3301600 - Failed to operate the geofence.
     * @syscap SystemCapability.Location.Location.Geofence
     * @since 9
     */
    function off(type: 'gnssFenceStatusChange', request: GeofenceRequest, want: WantAgent): void;
    /**
     * Registering the callback function for listening to country code changes.
     *
     * @param { 'countryCodeChange' } type - Indicates the location service event to be subscribed to.
     * @param { Callback<CountryCode> } callback - Indicates the callback for reporting country code changes.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory
     *     parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call
     *     ${geoLocationManager.on('countryCodeChange')} due to limited device capabilities.
     * @throws { BusinessError } 3301000 - The location service is unavailable.
     * @throws { BusinessError } 3301500 - Failed to query the area information.
     * @syscap SystemCapability.Location.Location.Core
     * @crossplatform [since 22]
     * @since 9
     */
    function on(type: 'countryCodeChange', callback: Callback<CountryCode>): void;
    /**
     * Unregistering the callback function for listening to country code changes.
     *
     * @param { 'countryCodeChange' } type - Indicates the location service event to be subscribed to.
     * @param { Callback<CountryCode> } [callback] - Indicates the callback for reporting country code changes.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory
     *     parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call
     *     ${geoLocationManager.off('countryCodeChange')} due to limited device capabilities.
     * @throws { BusinessError } 3301000 - The location service is unavailable.
     * @throws { BusinessError } 3301500 - Failed to query the area information.
     * @syscap SystemCapability.Location.Location.Core
     * @crossplatform [since 22]
     * @since 9
     */
    function off(type: 'countryCodeChange', callback?: Callback<CountryCode>): void;
    /**
     * Registers and listens to bluetooth scanning results for location services.
     *
     * @permission ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION
     * @param { 'bluetoothScanResultChange' } type - Indicates the location service event to be subscribed to.
     * @param { Callback<BluetoothScanResult> } callback - Indicates the callback for reporting Bluetooth scan info.
     * @throws { BusinessError } 201 - Permission verification failed. The application does
     *     not have the permission required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory
     *     parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call
     *     ${geoLocationManager.on('bluetoothScanResultChange')} due to limited device capabilities.
     * @throws { BusinessError } 3301000 - The location service is unavailable.
     * @throws { BusinessError } 3301100 - The location switch is off.
     * @syscap SystemCapability.Location.Location.Core
     * @crossplatform [since 22]
     * @since 16
     */
    function on(type: 'bluetoothScanResultChange', callback: Callback<BluetoothScanResult>): void;
    /**
     * Stop bluetooth scanning and unregister to listen to bluetooth scanning result changes.
     *
     * @permission ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION
     * @param { 'bluetoothScanResultChange' } type - Indicates the location service event to be subscribed to.
     * @param { Callback<BluetoothScanResult> } [callback] - Indicates the callback for reporting Bluetooth scan info.
     * @throws { BusinessError } 201 - Permission verification failed. The application
     *     does not have the permission required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory
     *     parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call
     *     ${geoLocationManager.off('bluetoothScanResultChange')} due to limited device capabilities.
     * @throws { BusinessError } 3301000 - The location service is unavailable.
     * @syscap SystemCapability.Location.Location.Core
     * @crossplatform [since 22]
     * @since 16
     */
    function off(type: 'bluetoothScanResultChange', callback?: Callback<BluetoothScanResult>): void;
    /**
     * Obtain current location.
     *
     * @permission ohos.permission.APPROXIMATELY_LOCATION
     * @param { CurrentLocationRequest } request - Indicates the location request parameters. [since 9 - 11]
     * @param { CurrentLocationRequest | SingleLocationRequest } request - Indicates the location request
     *     parameters. [since 12]
     * @param { AsyncCallback<Location> } callback - Indicates the callback for reporting the location result.
     * @throws { BusinessError } 201 - Permission verification failed. The application
     *     does not have the permission required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory
     *     parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call
     *     ${geoLocationManager.getCurrentLocation} due to limited device capabilities.
     * @throws { BusinessError } 3301000 - The location service is unavailable.
     * @throws { BusinessError } 3301100 - The location switch is off.
     * @throws { BusinessError } 3301200 - Failed to obtain the geographical location.
     * @syscap SystemCapability.Location.Location.Core
     * @crossplatform [since 22]
     * @atomicservice [since 11]
     * @since 9
     */
    function getCurrentLocation(request: CurrentLocationRequest | SingleLocationRequest, callback: AsyncCallback<Location>): void;
    /**
     * Obtain current location.
     *
     * @permission ohos.permission.APPROXIMATELY_LOCATION
     * @param { AsyncCallback<Location> } callback - Indicates the callback for reporting the location result.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the
     *     permission required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left
     *     unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call
     *     ${geoLocationManager.getCurrentLocation} due to limited device capabilities.
     * @throws { BusinessError } 3301000 - The location service is unavailable.
     * @throws { BusinessError } 3301100 - The location switch is off.
     * @throws { BusinessError } 3301200 - Failed to obtain the geographical location.
     * @syscap SystemCapability.Location.Location.Core
     * @crossplatform [since 22]
     * @atomicservice [since 11]
     * @since 9
     */
    function getCurrentLocation(callback: AsyncCallback<Location>): void;
    /**
     * Obtain current location.
     *
     * @permission ohos.permission.APPROXIMATELY_LOCATION
     * @param { CurrentLocationRequest } [request] - Indicates the location request parameters. [since 9 - 11]
     * @param { CurrentLocationRequest | SingleLocationRequest } [request] - Indicates the location request
     *     parameters. [since 12]
     * @returns { Promise<Location> } The promise returned by the function.
     * @throws { BusinessError } 201 - Permission verification failed. The application does
     *     not have the permission required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory
     *     parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call
     *     ${geoLocationManager.getCurrentLocation} due to limited device capabilities.
     * @throws { BusinessError } 3301000 - The location service is unavailable.
     * @throws { BusinessError } 3301100 - The location switch is off.
     * @throws { BusinessError } 3301200 - Failed to obtain the geographical location.
     * @syscap SystemCapability.Location.Location.Core
     * @crossplatform [since 22]
     * @atomicservice [since 11]
     * @since 9
     */
    function getCurrentLocation(request?: CurrentLocationRequest | SingleLocationRequest): Promise<Location>;
    /**
     * Obtain last known location.
     *
     * @permission ohos.permission.APPROXIMATELY_LOCATION
     * @returns { Location } The last known location information.
     * @throws { BusinessError } 201 - Permission verification failed. The application
     *     does not have the permission required to call the API.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call
     *     ${geoLocationManager.getLastLocation} due to limited device capabilities.
     * @throws { BusinessError } 3301000 - The location service is unavailable.
     * @throws { BusinessError } 3301100 - The location switch is off.
     * @throws { BusinessError } 3301200 - Failed to obtain the geographical location.
     * @syscap SystemCapability.Location.Location.Core
     * @crossplatform [since 22]
     * @atomicservice [since 11]
     * @since 9
     */
    function getLastLocation(): Location;
    /**
     * Obtain current location switch status.
     *
     * @returns { boolean } Returns {@code true} if the location switch on, returns {@code false} otherwise.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call
     *     ${geoLocationManager.isLocationEnabled} due to limited device capabilities.
     * @throws { BusinessError } 3301000 - The location service is unavailable.
     * @syscap SystemCapability.Location.Location.Core
     * @crossplatform [since 22]
     * @atomicservice [since 11]
     * @since 9
     */
    function isLocationEnabled(): boolean;
    /**
     * Obtain address info from location.
     *
     * @param { ReverseGeoCodeRequest } request - Indicates the reverse geocode query parameters.
     * @param { AsyncCallback<Array<GeoAddress>> } callback - Indicates the callback for reporting the address info.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory
     *     parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call
     *     ${geoLocationManager.getAddressesFromLocation} due to limited device capabilities.
     * @throws { BusinessError } 3301000 - The location service is unavailable.
     * @throws { BusinessError } 3301300 - Reverse geocoding query failed.
     * @syscap SystemCapability.Location.Location.Geocoder
     * @crossplatform [since 22]
     * @since 9
     */
    function getAddressesFromLocation(request: ReverseGeoCodeRequest, callback: AsyncCallback<Array<GeoAddress>>): void;
    /**
     * Obtain address info from location.
     *
     * @param { ReverseGeoCodeRequest } request - Indicates the reverse geocode query parameters.
     * @returns { Promise<Array<GeoAddress>> } The promise returned by the function.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory
     *     parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call
     *     ${geoLocationManager.getAddressesFromLocation} due to limited device capabilities.
     * @throws { BusinessError } 3301000 - The location service is unavailable.
     * @throws { BusinessError } 3301300 - Reverse geocoding query failed.
     * @syscap SystemCapability.Location.Location.Geocoder
     * @crossplatform [since 22]
     * @since 9
     */
    function getAddressesFromLocation(request: ReverseGeoCodeRequest): Promise<Array<GeoAddress>>;
    /**
     * Obtain latitude and longitude info from location address.
     *
     * @param { GeoCodeRequest } request - Indicates the geocode query parameters.
     * @param { AsyncCallback<Array<GeoAddress>> } callback - Indicates the callback for reporting the
     *     latitude and longitude result.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are
     *     left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call
     *     ${geoLocationManager.getAddressesFromLocationName} due to limited device capabilities.
     * @throws { BusinessError } 3301000 - The location service is unavailable.
     * @throws { BusinessError } 3301400 - Geocoding query failed.
     * @syscap SystemCapability.Location.Location.Geocoder
     * @crossplatform [since 22]
     * @since 9
     */
    function getAddressesFromLocationName(request: GeoCodeRequest, callback: AsyncCallback<Array<GeoAddress>>): void;
    /**
     * Obtain latitude and longitude info from location address.
     *
     * @param { GeoCodeRequest } request - Indicates the geocode query parameters.
     * @returns { Promise<Array<GeoAddress>> } The promise returned by the function.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory
     *     parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call
     *     ${geoLocationManager.getAddressesFromLocationName} due to limited device capabilities.
     * @throws { BusinessError } 3301000 - The location service is unavailable.
     * @throws { BusinessError } 3301400 - Geocoding query failed.
     * @syscap SystemCapability.Location.Location.Geocoder
     * @crossplatform [since 22]
     * @since 9
     */
    function getAddressesFromLocationName(request: GeoCodeRequest): Promise<Array<GeoAddress>>;
    /**
     * Obtain geocoding service status.
     *
     * @returns { boolean } Returns {@code true} if geocoding service is available,
     *     returns {@code false} otherwise.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call
     *     ${geoLocationManager.isGeocoderAvailable} due to limited device capabilities.
     * @throws { BusinessError } 3301000 - The location service is unavailable.
     * @syscap SystemCapability.Location.Location.Geocoder
     * @crossplatform [since 22]
     * @since 9
     */
    function isGeocoderAvailable(): boolean;
    /**
     * Obtain the number of cached GNSS locations reported at a time.
     *
     * @permission ohos.permission.APPROXIMATELY_LOCATION
     * @param { AsyncCallback<number> } callback - Indicates the callback for reporting the cached GNSS locations size.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call
     *     ${geoLocationManager.getCachedGnssLocationsSize} due to limited device capabilities.
     * @throws { BusinessError } 3301000 - The location service is unavailable.
     * @throws { BusinessError } 3301100 - The location switch is off.
     * @syscap SystemCapability.Location.Location.Gnss
     * @crossplatform [since 22]
     * @since 9
     */
    function getCachedGnssLocationsSize(callback: AsyncCallback<number>): void;
    /**
     * Obtain the number of cached GNSS locations.
     *
     * @permission ohos.permission.APPROXIMATELY_LOCATION
     * @returns { Promise<number> } The promise returned by the function.
     * @throws { BusinessError } 201 - Permission verification failed. The application
     *     does not have the permission required to call the API.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call
     *     ${geoLocationManager.getCachedGnssLocationsSize} due to limited device capabilities.
     * @throws { BusinessError } 3301000 - The location service is unavailable.
     * @throws { BusinessError } 3301100 - The location switch is off.
     * @syscap SystemCapability.Location.Location.Gnss
     * @crossplatform [since 22]
     * @since 9
     */
    function getCachedGnssLocationsSize(): Promise<number>;
    /**
     * All prepared GNSS locations are returned to the application through the callback function,
     * and the bottom-layer buffer is cleared.
     *
     * @permission ohos.permission.APPROXIMATELY_LOCATION
     * @param { AsyncCallback<void> } callback - Indicates the callback for reporting the error message.
     *     If the function fails to execute, the error message will be carried in the first parameter
     *     err of AsyncCallback,
     *     If the function executes successfully, execute the callback function only, no data will be returned.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call
     *     ${geoLocationManager.flushCachedGnssLocations} due to limited device capabilities.
     * @throws { BusinessError } 3301000 - The location service is unavailable.
     * @throws { BusinessError } 3301100 - The location switch is off.
     * @throws { BusinessError } 3301200 - Failed to obtain the geographical location.
     * @syscap SystemCapability.Location.Location.Gnss
     * @crossplatform [since 22]
     * @since 9
     */
    function flushCachedGnssLocations(callback: AsyncCallback<void>): void;
    /**
     * All prepared GNSS locations are returned to the application,
     * and the bottom-layer buffer is cleared.
     *
     * @permission ohos.permission.APPROXIMATELY_LOCATION
     * @returns { Promise<void> } The promise returned by the function.
     * @throws { BusinessError } 201 - Permission verification failed. The application
     *     does not have the permission required to call the API.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call
     *     ${geoLocationManager.flushCachedGnssLocations} due to limited device capabilities.
     * @throws { BusinessError } 3301000 - The location service is unavailable.
     * @throws { BusinessError } 3301100 - The location switch is off.
     * @throws { BusinessError } 3301200 - Failed to obtain the geographical location.
     * @syscap SystemCapability.Location.Location.Gnss
     * @crossplatform [since 22]
     * @since 9
     */
    function flushCachedGnssLocations(): Promise<void>;
    /**
     * Send extended commands to location subsystem.
     *
     * @param { LocationCommand } command - Indicates the extended command message body.
     * @param { AsyncCallback<void> } callback - Indicates the callback for reporting the error message.
     *     If the function fails to execute, the error message will be carried in the first parameter err of
     *     AsyncCallback,
     *     If the function executes successfully, execute the callback function only, no data will be returned.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory
     *     parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call
     *     ${geoLocationManager.sendCommand} due to limited device capabilities.
     * @throws { BusinessError } 3301000 - The location service is unavailable.
     * @syscap SystemCapability.Location.Location.Core
     * @since 9
     */
    function sendCommand(command: LocationCommand, callback: AsyncCallback<void>): void;
    /**
     * Send extended commands to location subsystem.
     *
     * @param { LocationCommand } command - Indicates the extended command message body.
     * @returns { Promise<void> } The promise returned by the function.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory
     *     parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call
     *     ${geoLocationManager.sendCommand} due to limited device capabilities.
     * @throws { BusinessError } 3301000 - The location service is unavailable.
     * @syscap SystemCapability.Location.Location.Core
     * @since 9
     */
    function sendCommand(command: LocationCommand): Promise<void>;
    /**
     * Obtain the current country code.
     *
     * @param { AsyncCallback<CountryCode> } callback - Indicates the callback for reporting the country code.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1. Mandatory parameters are left unspecified; 2. Incorrect parameter types;
     *     3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call
     *     ${geoLocationManager.getCountryCode} due to limited device capabilities.
     * @throws { BusinessError } 3301000 - The location service is unavailable.
     * @throws { BusinessError } 3301500 - Failed to query the area information.
     * @syscap SystemCapability.Location.Location.Core
     * @crossplatform [since 22]
     * @since 9
     */
    function getCountryCode(callback: AsyncCallback<CountryCode>): void;
    /**
     * Obtain the current country code.
     *
     * @returns { Promise<CountryCode> } The promise returned by the function.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call
     *     ${geoLocationManager.getCountryCode} due to limited device capabilities.
     * @throws { BusinessError } 3301000 - The location service is unavailable.
     * @throws { BusinessError } 3301500 - Failed to query the area information.
     * @syscap SystemCapability.Location.Location.Core
     * @crossplatform [since 22]
     * @since 9
     */
    function getCountryCode(): Promise<CountryCode>;
    /**
     * Add a geofence.
     *
     * @permission ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION
     * @param { GnssGeofenceRequest } fenceRequest - Indicates the Geofence configuration parameters.
     * @returns { Promise<number> } The promise returned by the function, for reporting the ID of geofence.
     * @throws { BusinessError } 201 - Permission verification failed. The application
     *     does not have the permission required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory
     *     parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call
     *     ${geoLocationManager.addGnssGeofence} due to limited device capabilities.
     * @throws { BusinessError } 3301000 - The location service is unavailable.
     * @throws { BusinessError } 3301100 - The location switch is off.
     * @throws { BusinessError } 3301601 - The number of geofences exceeds the maximum.
     * @syscap SystemCapability.Location.Location.Geofence
     * @crossplatform [since 22]
     * @since 12
     */
    function addGnssGeofence(fenceRequest: GnssGeofenceRequest): Promise<number>;
    /**
     * Remove a geofence.
     *
     * @permission ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION [since 12 - 24]
     * @param { number } geofenceId - Indicates the ID of geofence.
     * @returns { Promise<void> } The promise returned by the function.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not
     *     have the permission required to call the API. [since 12 - 24]
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters
     *     are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call
     *     ${geoLocationManager.removeGnssGeofence} due to limited device capabilities.
     * @throws { BusinessError } 3301000 - The location service is unavailable.
     * @throws { BusinessError } 3301602 - Failed to delete a geofence due to an incorrect ID.
     * @syscap SystemCapability.Location.Location.Geofence
     * @crossplatform [since 22]
     * @since 12
     */
    function removeGnssGeofence(geofenceId: number): Promise<void>;
    /**
     * Get all active fences.
     *
     * @permission ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION
     * @returns { Promise<Map<number, Geofence>> } The promise returned by the function.
     *     The key of the map represents the fence ID. The value of the map represents
     *     the detailed information of the fence.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not
     *     have the permission required to call the API.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call
     *     ${geoLocationManager.getActiveGeoFences} due to limited device capabilities.
     * @syscap SystemCapability.Location.Location.Geofence
     * @since 23
     */
    function getActiveGeoFences(): Promise<Map<number, Geofence>>;
    /**
     * Obtains the coordinate system types supported by geofence.
     *
     * @returns { Array<CoordinateSystemType> } Return the coordinate system types supported by geofence.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call
     *     ${geoLocationManager.getGeofenceSupportedCoordTypes} due to limited device capabilities.
     * @throws { BusinessError } 3301000 - The location service is unavailable.
     * @syscap SystemCapability.Location.Location.Geofence
     * @crossplatform [since 22]
     * @since 12
     */
    function getGeofenceSupportedCoordTypes(): Array<CoordinateSystemType>;
    /**
       * Obtains the BSSID of the connected Wi-Fi hotspot.
       *
       * @permission ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION
       * @returns {string} Returns the BSSID of the connected Wi-Fi hotspot.
       * @throws { BusinessError } 201 - Permission verification failed. The application
       *     does not have the permission required to call the API.
       * @throws { BusinessError } 801 - Capability not supported. Failed to call
       *     ${geoLocationManager.getCurrentWifiBssidForLocating()} due to limited device capabilities.
       * @throws { BusinessError } 3301000 - The location service is unavailable.
       * @throws { BusinessError } 3301100 - The location switch is off.
       * @throws { BusinessError } 3301900 - Failed to obtain the BSSID of the Wi-Fi hotspot.
       *     The Wi-Fi network is not connected.
       * @syscap SystemCapability.Location.Location.Core
       * @crossplatform
       * @since 14
       */
    function getCurrentWifiBssidForLocating(): string;
    /**
     * Obtains the distance between two locations.
     *
     * @param { Location } location1 - Indicates first location.
     * @param { Location } location2 - Indicates second location.
     * @returns { number } Returns the distance between two locations.
     * @syscap SystemCapability.Location.Location.Core
     * @crossplatform [since 22]
     * @atomicservice
     * @since 20
     */
    function getDistanceBetweenLocations(location1: Location, location2: Location): number;
    /**
     * Check whether the POI service is supported.
     *
     * @returns { boolean } Returns {@code true} if POI service is available, returns {@code false} otherwise.
     * @syscap SystemCapability.Location.Location.Core
     * @atomicservice
     * @since 20
     */
    function isPoiServiceSupported(): boolean;
    /**
     * Obtaining POI Information.
     *
     * @permission ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION
     * @returns { Promise<PoiInfo> } The promise returned by the function, for reporting POI info.
     * @throws { BusinessError } 201 - Permission verification failed. The application
     *     does not have the permission required to call the API.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call
     *     ${geoLocationManager.getPoiInfo} due to limited device capabilities.
     * @throws { BusinessError } 3301000 - The location service is unavailable.
     * @throws { BusinessError } 3301100 - The location switch is off.
     * @syscap SystemCapability.Location.Location.Core
     * @atomicservice
     * @since 20
     */
    function getPoiInfo(): Promise<PoiInfo>;
    /**
     * Add a beacon fence.
     *
     * @permission ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION
     * @param { BeaconFenceRequest } fenceRequest - Indicates the details of the beacon fence.
     * @returns { Promise<number> } The promise returned by the function, for reporting the ID of beacon fence.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the
     *     permission required to call the API.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call ${geoLocationManager.addBeaconFence}
     *     due to limited device capabilities.
     * @throws { BusinessError } 3501100 - Failed to add a beacon fence because the location switch is off.
     * @throws { BusinessError } 3501101 - Failed to add a beacon fence because the bluetooth switch is off.
     * @throws { BusinessError } 3501601 - The number of beacon fences exceeds the maximum.
     * @throws { BusinessError } 3501603 - Duplicate beacon fence information.
     * @syscap SystemCapability.Location.Location.Geofence
     * @atomicservice
     * @since 20
     */
    function addBeaconFence(fenceRequest: BeaconFenceRequest): Promise<number>;
    /**
     * Remove a beacon fence.
     *
     * @permission ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION [since 20 - 24]
     * @param { BeaconFence } [beaconFence] - Indicates the details of the beacon fence.
     * @returns { Promise<void> } The promise returned by the function.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API. [since 20 - 24]
     * @throws { BusinessError } 801 - Capability not supported. Failed to call ${geoLocationManager.removeBeaconFence}
     *     due to limited device capabilities.
     * @throws { BusinessError } 3501602 - Failed to delete the fence due to incorrect beacon fence information.
     * @syscap SystemCapability.Location.Location.Geofence
     * @atomicservice
     * @since 20
     */
    function removeBeaconFence(beaconFence?: BeaconFence): Promise<void>;
    /**
     * Check whether the BeaconFence service is supported.
     *
     * @returns { boolean } Returns {@code true} if BeaconFence service is available, returns {@code false} otherwise.
     * @syscap SystemCapability.Location.Location.Geofence
     * @atomicservice
     * @since 20
     */
    function isBeaconFenceSupported(): boolean;
    /**
     * Check whether the WLAN scan results match the WLAN BSSID list.
     *
     * @permission ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION
     * @param { Array<string> } wlanBssidArray - Indicates the list of WLAN BSSIDs that need to be matched.
     * @param { number } rssiThreshold - Indicates the WLAN RSSI threshold, only matching WLAN BSSID with
     *     RSSI greater than this threshold.
     * @param { boolean } needStartScan - Indicate whether a WLAN scan needs to be initiated.
     * @returns { Promise<boolean> } The promise returned by the function.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call
     *     ${geoLocationManager.isWlanBssidMatched} due to limited device capabilities.
     * @throws { BusinessError } 3301100 - The location switch is off.
     * @throws { BusinessError } 3301800 - Failed to start WiFi scanning.
     * @syscap SystemCapability.Location.Location.Core
     * @atomicservice
     * @since 21
     */
    function isWlanBssidMatched(wlanBssidArray: Array<string>, rssiThreshold: number, needStartScan: boolean): Promise<boolean>;
    /**
     * Check whether the GNSS service is supported.
     *
     * @returns { boolean } Returns {@code true} if GNSS service is available, returns {@code false} otherwise.
     * @throws { BusinessError } 3301000 - The location service is unavailable.
     * @syscap SystemCapability.Location.Location.Core
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    function isGnssServiceSupported(): boolean;
    /**
     * Check whether the GNSS fence service is supported.
     *
     * @returns { boolean } Returns {@code true} if GNSS fence service is available, returns {@code false} otherwise.
     * @throws { BusinessError } 3301000 - The location service is unavailable.
     * @syscap SystemCapability.Location.Location.Core
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    function isGnssFenceServiceSupported(): boolean;
    /**
     * Check whether the cached GNSS service is supported.
     *
     * @returns { boolean } Returns {@code true} if cached GNSS service is available, returns {@code false} otherwise.
     * @throws { BusinessError } 3301000 - The location service is unavailable.
     * @syscap SystemCapability.Location.Location.Core
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    function isCachedGnssServiceSupported(): boolean;
    /**
     * Check whether the WLAN scan results match the WLAN BSSID list,
     * return information about the WLAN device that is successfully matched.
     *
     * @permission ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION
     * @param { Array<string> } wlanBssidArray - Indicates the list of WLAN BSSIDs that need to be matched.
     * @param { number } rssiThreshold - Indicates the WLAN RSSI threshold, only matches WLAN BSSIDs with
     *     RSSI greater than this threshold.
     * @param { boolean } needStartScan - Indicates whether a WLAN scan needs to be initiated.
     * @returns { Promise<Array<MatchingWlanInfo>> } The promise returned by the function.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call
     *     ${geoLocationManager.findMatchingWlan} due to limited device capabilities.
     * @throws { BusinessError } 3301100 - The location switch is off.
     * @throws { BusinessError } 3301800 - Failed to start WLAN scanning.
     * @syscap SystemCapability.Location.Location.Core
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    function findMatchingWlan(wlanBssidArray: Array<string>, rssiThreshold: number, needStartScan: boolean): Promise<Array<MatchingWlanInfo>>;
    /**
     * Obtains the information about the district where the current device is located.
     *
     * @permission ohos.permission.APPROXIMATELY_LOCATION
     * @param { DistrictRequestParams } [params] - Indicates request parameters for obtaining the district information.
     * @returns { Promise<DistrictInfo> } Promise used to return ${DistrictInfo}.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call
     *     ${geoLocationManager.getCurrentDistrict} due to limited device capabilities.
     * @throws { BusinessError } 3301000 - The location service is unavailable.
     * @throws { BusinessError } 3301100 - The location switch is off.
     * @throws { BusinessError } 3301500 - Failed to query the area information because the reverse geocoding server
     *     returns an error.
     * @syscap SystemCapability.Location.Location.Geocoder
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    function getCurrentDistrict(params?: DistrictRequestParams): Promise<DistrictInfo>;
    /**
     * Starts Bluetooth scanning and matches the device ID list in the input parameter
     * with the Bluetooth scanning result. If the matching is successful, the Bluetooth
     * device information is returned through the callback.
     *
     * @permission ohos.permission.APPROXIMATELY_LOCATION
     * @param { BluetoothSearchRequestParams } request - Indicates the configuration parameters
     *     for the Bluetooth search function.
     * @param { Callback<BluetoothScanResult> } callback - Callback used to return ${BluetoothScanResult}.
     * @throws { BusinessError } 201 - Permission verification failed. The application does
     *     not have the permission required to call the API.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call
     *     ${geoLocationManager.startBluetoothSearch} due to limited device capabilities.
     * @throws { BusinessError } 3301000 - The location service is unavailable.
     * @throws { BusinessError } 3301800 - Failed to start Bluetooth scanning.
     * @syscap SystemCapability.Location.Location.Core
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    function startBluetoothSearch(request: BluetoothSearchRequestParams, callback: Callback<BluetoothScanResult>): void;
    /**
     * Stop Bluetooth scanning and searching.
     *
     * @param { Callback<BluetoothScanResult> } [callback] - Callback used to return ${BluetoothScanResult}.
     *     It should be the same as the callback passed to ${geoLocationManager.startBluetoothSearch}.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call
     *     ${geoLocationManager.stopBluetoothSearch} due to limited device capabilities.
     * @throws { BusinessError } 3301000 - The location service is unavailable.
     * @syscap SystemCapability.Location.Location.Core
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    function stopBluetoothSearch(callback?: Callback<BluetoothScanResult>): void;
    /**
     * Obtain post-processing trajectory information under specific sport mode. Only
     * [SKIING]{@link geoLocationManager.SportsType.SKIING} is supported currently.
     *
     * Before calling this API, you need to call
     * [on('locationChange')]{@link geoLocationManager.on('locationChange')} and set the input parameter
     * [sportsType]{@link geoLocationManager.ContinuousLocationRequest.sportsType} to the specific sport mode to start
     * tracking.
     *
     * Returns data within 24 hours since tracking started; Subsequent calls return only new records.
     *
     * @permission ohos.permission.LOCATION
     * @param { SportsType } sportsType - Indicate the type of sports.
     * @returns { Promise<Array<Location>> } Promise used to return `Array<Location>`.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 801 - Capability not supported. Failed to call
     *     ${geoLocationManager.getPostProcessingTrack} due to limited device capabilities.
     * @throws { BusinessError } 3301000 - The location service is unavailable.
     * @throws { BusinessError } 3301100 - The location switch is off.
     * @throws { BusinessError } 3301200 - Failed to obtain the post processing track because sports type is not
     *     supported.
     * @syscap SystemCapability.Location.Location.Gnss
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    function getPostProcessingTrack(sportsType: SportsType): Promise<Array<Location>>;
    /**
     * Indicates request parameters for Bluetooth search function.
     *
     * @syscap SystemCapability.Location.Location.Core
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    export interface BluetoothSearchRequestParams {
        /**
         * Indicates the list of Bluetooth device ID that need to be search.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        deviceIdArray: Array<string>;
        /**
         * Indicates the Bluetooth RSSI threshold,
         * only search Bluetooth BSSID with RSSI greater than this threshold.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        rssiThreshold?: number;
    }
    /**
     * Indicates request parameters for obtaining the district information.
     *
     * @syscap SystemCapability.Location.Location.Geocoder
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    interface DistrictInfo {
        /**
         * Indicates language used for the location description.
         * zh indicates Chinese, and en indicates English.
         *
         * @syscap SystemCapability.Location.Location.Geocoder
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        locale?: string;
        /**
         * Indicates country code.
         *
         * @syscap SystemCapability.Location.Location.Geocoder
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        countryCode?: string;
        /**
         * Indicates country name.
         *
         * @syscap SystemCapability.Location.Location.Geocoder
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        countryName?: string;
        /**
         * Indicates administrative region name.
         *
         * @syscap SystemCapability.Location.Location.Geocoder
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        administrativeArea?: string;
        /**
         * Indicates sub-administrative region name.
         *
         * @syscap SystemCapability.Location.Location.Geocoder
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        subAdministrativeArea?: string;
        /**
         * Indicates locality information.
         *
         * @syscap SystemCapability.Location.Location.Geocoder
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        locality?: string;
        /**
         * Indicates sub-locality information.
         *
         * @syscap SystemCapability.Location.Location.Geocoder
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        subLocality?: string;
    }
    /**
     * Indicates request parameters for obtaining the district information.
     *
     * @syscap SystemCapability.Location.Location.Geocoder
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    export interface DistrictRequestParams {
        /**
         * Indicates the language area information.
         * ISO 639 alpha-2 or alpha-3 language code.
         * Example: "zh" (Chinese), "en" (English).
         * The default value is obtained from the language settings of the device (settings/system/Language & region
         * /Language).
         *
         * @syscap SystemCapability.Location.Location.Geocoder
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        locale?: string;
        /**
         * Indicates the timeout period.
         * The default value is 5000 ms.
         * The value range is all integers.
         *
         * @syscap SystemCapability.Location.Location.Geocoder
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        timeoutMs?: number;
    }
    /**
     * Satellite status information.
     *
     * @syscap SystemCapability.Location.Location.Gnss
     * @crossplatform [since 22]
     * @since 9
     */
    export interface SatelliteStatusInfo {
        /**
         * Number of satellites.
         *
         * @syscap SystemCapability.Location.Location.Gnss
         * @crossplatform [since 22]
         * @since 9
         */
        satellitesNumber: number;
        /**
         * Satellite ID array.
         *
         * @syscap SystemCapability.Location.Location.Gnss
         * @crossplatform [since 22]
         * @since 9
         */
        satelliteIds: Array<number>;
        /**
         * Carrier to noise density array.
         *
         * @syscap SystemCapability.Location.Location.Gnss
         * @crossplatform [since 22]
         * @since 9
         */
        carrierToNoiseDensitys: Array<number>;
        /**
         * Satellite altitude array.
         *
         * @syscap SystemCapability.Location.Location.Gnss
         * @crossplatform [since 22]
         * @since 9
         */
        altitudes: Array<number>;
        /**
         * Satellite azimuth array.
         *
         * @syscap SystemCapability.Location.Location.Gnss
         * @crossplatform [since 22]
         * @since 9
         */
        azimuths: Array<number>;
        /**
         * Satellite carrier frequency array.
         *
         * @syscap SystemCapability.Location.Location.Gnss
         * @crossplatform [since 22]
         * @since 9
         */
        carrierFrequencies: Array<number>;
        /**
         * Satellite constellation type array.
         *
         * @syscap SystemCapability.Location.Location.Gnss
         * @crossplatform [since 22]
         * @since 12
         */
        satelliteConstellation?: Array<SatelliteConstellationCategory>;
        /**
         * Satellite additional information array.
         *
         * @syscap SystemCapability.Location.Location.Gnss
         * @crossplatform [since 22]
         * @since 12
         */
        satelliteAdditionalInfo?: Array<number>;
    }
    /**
     * Parameters for requesting to report cache location information.
     *
     * @syscap SystemCapability.Location.Location.Gnss
     * @crossplatform [since 22]
     * @since 9
     */
    export interface CachedGnssLocationsRequest {
        /**
         * GNSS cache location report period.
         *
         * @syscap SystemCapability.Location.Location.Gnss
         * @crossplatform [since 22]
         * @since 9
         */
        reportingPeriodSec: number;
        /**
         * Indicates whether to wake up the listener when the GNSS cache location queue is full.
         *
         * @syscap SystemCapability.Location.Location.Gnss
         * @crossplatform [since 22]
         * @since 9
         */
        wakeUpCacheQueueFull: boolean;
    }
    /**
     * Configuring parameters in GNSS geofence requests.
     *
     * @syscap SystemCapability.Location.Location.Geofence
     * @crossplatform [since 22]
     * @since 12
     */
    export interface GnssGeofenceRequest {
        /**
         * Circular fence information.
         *
         * @syscap SystemCapability.Location.Location.Geofence
         * @crossplatform [since 22]
         * @since 12
         */
        geofence: Geofence;
        /**
         * Indicates geofence transition status monitored.
         *
         * @syscap SystemCapability.Location.Location.Geofence
         * @crossplatform [since 22]
         * @since 12
         */
        monitorTransitionEvents: Array<GeofenceTransitionEvent>;
        /**
         * Indicates the geofence notifications to publish.
         *
         * @syscap SystemCapability.Location.Location.Geofence
         * @crossplatform [since 22]
         * @since 12
         */
        notifications?: Array<NotificationRequest>;
        /**
         * Indicates the callback for reporting the geofence transition status.
         *
         * @syscap SystemCapability.Location.Location.Geofence
         * @crossplatform [since 22]
         * @since 12
         */
        geofenceTransitionCallback: AsyncCallback<GeofenceTransition>;
        /**
         * Indicates time for which a device is dwelling in the geofence, in milliseconds.
         * If the device dwelling time reaches the value specified by this parameter,
         * a GEOFENCE_TRANSITION_EVENT_DWELL event is reported.
         * The value should be an integer.
         *
         * @syscap SystemCapability.Location.Location.Geofence
         * @since 23
         */
        loiterTimeMs?: number;
        /**
         * Indicates the name of FenceExtensionAbility.
         *
         * @syscap SystemCapability.Location.Location.Geofence
         * @since 23
         */
        fenceExtensionAbilityName?: string;
    }
    /**
     * Configuring parameters in geo fence requests.
     *
     * @syscap SystemCapability.Location.Location.Geofence
     * @since 9
     */
    export interface GeofenceRequest {
        /**
         * Indicate the user scenario.
         *
         * @syscap SystemCapability.Location.Location.Geofence
         * @since 9
         */
        scenario: LocationRequestScenario;
        /**
         * Circular fence information.
         *
         * @syscap SystemCapability.Location.Location.Geofence
         * @since 9
         */
        geofence: Geofence;
    }
    /**
     * Circular fence information.
     *
     * @syscap SystemCapability.Location.Location.Geofence
     * @crossplatform [since 22]
     * @since 9
     */
    export interface Geofence {
        /**
         * Latitude of the center point of the circular fence.
         *
         * @syscap SystemCapability.Location.Location.Geofence
         * @crossplatform [since 22]
         * @since 9
         */
        latitude: number;
        /**
         * Longitude of the center point of the circular fence.
         *
         * @syscap SystemCapability.Location.Location.Geofence
         * @crossplatform [since 22]
         * @since 9
         */
        longitude: number;
        /**
         * Coordinate system type.
         *
         * @syscap SystemCapability.Location.Location.Geofence
         * @crossplatform [since 22]
         * @since 12
         */
        coordinateSystemType?: CoordinateSystemType;
        /**
         * Radius of the circular fence.
         *
         * @syscap SystemCapability.Location.Location.Geofence
         * @crossplatform [since 22]
         * @since 9
         */
        radius: number;
        /**
         * Expiration of the circular fence.
         *
         * @syscap SystemCapability.Location.Location.Geofence
         * @crossplatform [since 22]
         * @since 9
         */
        expiration: number;
    }
    /**
     * Configuring parameters in reverse geocode requests.
     *
     * @syscap SystemCapability.Location.Location.Geocoder
     * @crossplatform [since 22]
     * @since 9
     */
    export interface ReverseGeoCodeRequest {
        /**
         * Indicates the language area information.
         *
         * @syscap SystemCapability.Location.Location.Geocoder
         * @crossplatform [since 22]
         * @since 9
         */
        locale?: string;
        /**
         * Indicates the country information.
         *
         * @syscap SystemCapability.Location.Location.Geocoder
         * @crossplatform [since 22]
         * @since 12
         */
        country?: string;
        /**
         * Latitude for reverse geocoding query.
         *
         * @syscap SystemCapability.Location.Location.Geocoder
         * @crossplatform [since 22]
         * @since 9
         */
        latitude: number;
        /**
         * Longitude for reverse geocoding query.
         *
         * @syscap SystemCapability.Location.Location.Geocoder
         * @crossplatform [since 22]
         * @since 9
         */
        longitude: number;
        /**
         * Indicates the maximum number of addresses returned by reverse geocoding query.
         *
         * @syscap SystemCapability.Location.Location.Geocoder
         * @crossplatform [since 22]
         * @since 9
         */
        maxItems?: number;
    }
    /**
     * Configuring parameters in geocode requests.
     *
     * @syscap SystemCapability.Location.Location.Geocoder
     * @crossplatform [since 22]
     * @since 9
     */
    export interface GeoCodeRequest {
        /**
         * Indicates the language area information.
         *
         * @syscap SystemCapability.Location.Location.Geocoder
         * @crossplatform [since 22]
         * @since 9
         */
        locale?: string;
        /**
         * Indicates the country information.
         *
         * @syscap SystemCapability.Location.Location.Geocoder
         * @crossplatform [since 22]
         * @since 12
         */
        country?: string;
        /**
         * Address information.
         *
         * @syscap SystemCapability.Location.Location.Geocoder
         * @crossplatform [since 22]
         * @since 9
         */
        description: string;
        /**
         * Indicates the maximum number of geocode query results.
         *
         * @syscap SystemCapability.Location.Location.Geocoder
         * @crossplatform [since 22]
         * @since 9
         */
        maxItems?: number;
        /**
         * Indicates the minimum latitude for geocoding query results.
         *
         * @syscap SystemCapability.Location.Location.Geocoder
         * @crossplatform [since 22]
         * @since 9
         */
        minLatitude?: number;
        /**
         * Indicates the minimum longitude for geocoding query results.
         *
         * @syscap SystemCapability.Location.Location.Geocoder
         * @crossplatform [since 22]
         * @since 9
         */
        minLongitude?: number;
        /**
         * Indicates the maximum latitude for geocoding query results.
         *
         * @syscap SystemCapability.Location.Location.Geocoder
         * @crossplatform [since 22]
         * @since 9
         */
        maxLatitude?: number;
        /**
         * Indicates the maximum longitude for geocoding query results.
         *
         * @syscap SystemCapability.Location.Location.Geocoder
         * @crossplatform [since 22]
         * @since 9
         */
        maxLongitude?: number;
    }
    /**
     * Data struct describes geographic locations.
     *
     * @syscap SystemCapability.Location.Location.Geocoder
     * @crossplatform [since 22]
     * @since 9
     */
    export interface GeoAddress {
        /**
         * Indicates latitude information.
         * A positive value indicates north latitude,
         * and a negative value indicates south latitude.
         *
         * @syscap SystemCapability.Location.Location.Geocoder
         * @crossplatform [since 22]
         * @since 9
         */
        latitude?: number;
        /**
         * Indicates longitude information.
         * A positive value indicates east longitude ,
         * and a negative value indicates west longitude.
         *
         * @syscap SystemCapability.Location.Location.Geocoder
         * @crossplatform [since 22]
         * @since 9
         */
        longitude?: number;
        /**
         * Indicates language used for the location description.
         * zh indicates Chinese, and en indicates English.
         *
         * @syscap SystemCapability.Location.Location.Geocoder
         * @crossplatform [since 22]
         * @since 9
         */
        locale?: string;
        /**
         * Indicates detailed address information.
         *
         * @syscap SystemCapability.Location.Location.Geocoder
         * @crossplatform [since 22]
         * @since 9
         */
        placeName?: string;
        /**
         * Indicates country code.
         *
         * @syscap SystemCapability.Location.Location.Geocoder
         * @crossplatform [since 22]
         * @since 9
         */
        countryCode?: string;
        /**
         * Indicates country name.
         *
         * @syscap SystemCapability.Location.Location.Geocoder
         * @crossplatform [since 22]
         * @since 9
         */
        countryName?: string;
        /**
         * Indicates administrative region name.
         *
         * @syscap SystemCapability.Location.Location.Geocoder
         * @crossplatform [since 22]
         * @since 9
         */
        administrativeArea?: string;
        /**
         * Indicates sub-administrative region name.
         *
         * @syscap SystemCapability.Location.Location.Geocoder
         * @crossplatform [since 22]
         * @since 9
         */
        subAdministrativeArea?: string;
        /**
         * Indicates locality information.
         *
         * @syscap SystemCapability.Location.Location.Geocoder
         * @crossplatform [since 22]
         * @since 9
         */
        locality?: string;
        /**
         * Indicates sub-locality information.
         *
         * @syscap SystemCapability.Location.Location.Geocoder
         * @crossplatform [since 22]
         * @since 9
         */
        subLocality?: string;
        /**
         * Indicates road name.
         *
         * @syscap SystemCapability.Location.Location.Geocoder
         * @crossplatform [since 22]
         * @since 9
         */
        roadName?: string;
        /**
         * Indicates auxiliary road information.
         *
         * @syscap SystemCapability.Location.Location.Geocoder
         * @crossplatform [since 22]
         * @since 9
         */
        subRoadName?: string;
        /**
         * Indicates house information.
         *
         * @syscap SystemCapability.Location.Location.Geocoder
         * @crossplatform [since 22]
         * @since 9
         */
        premises?: string;
        /**
         * Indicates postal code.
         *
         * @syscap SystemCapability.Location.Location.Geocoder
         * @crossplatform [since 22]
         * @since 9
         */
        postalCode?: string;
        /**
         * Indicates phone number.
         *
         * @syscap SystemCapability.Location.Location.Geocoder
         * @crossplatform [since 22]
         * @since 9
         */
        phoneNumber?: string;
        /**
         * Indicates website URL.
         *
         * @syscap SystemCapability.Location.Location.Geocoder
         * @crossplatform [since 22]
         * @since 9
         */
        addressUrl?: string;
        /**
         * Indicates additional information.
         *
         * @syscap SystemCapability.Location.Location.Geocoder
         * @crossplatform [since 22]
         * @since 9
         */
        descriptions?: Array<string>;
        /**
         * Indicates the amount of additional descriptive information.
         *
         * @syscap SystemCapability.Location.Location.Geocoder
         * @crossplatform [since 22]
         * @since 9
         */
        descriptionsSize?: number;
    }
    /**
     * Configuring parameters in location requests.
     *
     * @syscap SystemCapability.Location.Location.Core
     * @crossplatform [since 22]
     * @atomicservice [since 11]
     * @since 9
     */
    export interface LocationRequest {
        /**
         * Priority of the location request.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice [since 11]
         * @since 9
         */
        priority?: LocationRequestPriority;
        /**
         * User scenario of the location request.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice [since 11]
         * @since 9
         */
        scenario?: LocationRequestScenario;
        /**
         * Location report interval.
         *
         * @type { ?number } [since 9 - 10]
         * @type { ?number } [since 11]
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice [since 11]
         * @since 9
         */
        timeInterval?: number;
        /**
         * Location report distance interval.
         *
         * @type { ?number } [since 9 - 10]
         * @type { ?number } [since 11]
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice [since 11]
         * @since 9
         */
        distanceInterval?: number;
        /**
         * Accuracy requirements for reporting locations.
         *
         * @type { ?number } [since 9 - 10]
         * @type { ?number } [since 11]
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice [since 11]
         * @since 9
         */
        maxAccuracy?: number;
    }
    /**
     * Configuring parameters in current location requests.
     *
     * @syscap SystemCapability.Location.Location.Core
     * @crossplatform [since 22]
     * @atomicservice [since 11]
     * @since 9
     */
    export interface CurrentLocationRequest {
        /**
         * Priority of the location request.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice [since 11]
         * @since 9
         */
        priority?: LocationRequestPriority;
        /**
         * User scenario of the location request.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice [since 11]
         * @since 9
         */
        scenario?: LocationRequestScenario;
        /**
         * Accuracy requirements for reporting locations.
         *
         * @type { ?number } [since 9 - 10]
         * @type { ?number } [since 11]
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice [since 11]
         * @since 9
         */
        maxAccuracy?: number;
        /**
         * Timeout interval of a single location request.
         *
         * @type { ?number } [since 9 - 10]
         * @type { ?number } [since 11]
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice [since 11]
         * @since 9
         */
        timeoutMs?: number;
    }
    /**
     * Geofence transition status.
     *
     * @syscap SystemCapability.Location.Location.Geofence
     * @crossplatform [since 22]
     * @since 12
     */
    export interface GeofenceTransition {
        /**
         * ID of the geofence.
         *
         * @syscap SystemCapability.Location.Location.Geofence
         * @crossplatform [since 22]
         * @since 12
         */
        geofenceId: number;
        /**
         * Indicates the geofence transition status.
         *
         * @syscap SystemCapability.Location.Location.Geofence
         * @crossplatform [since 22]
         * @since 12
         */
        transitionEvent: GeofenceTransitionEvent;
        /**
         * Indicate the beaconFence which transitionEvent occurs.
         *
         * @syscap SystemCapability.Location.Location.Geofence
         * @crossplatform [since 22]
         * @since 20
         */
        beaconFence?: BeaconFence;
    }
    /**
     * Configuring parameters in continuous location requests.
     *
     * @syscap SystemCapability.Location.Location.Core
     * @crossplatform [since 22]
     * @atomicservice
     * @since 12
     */
    export interface ContinuousLocationRequest {
        /**
         * Location report interval, in seconds.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice
         * @since 12
         */
        interval: number;
        /**
         * Location scenario. You can select a user activity scenario or power consumption scenario.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice
         * @since 12
         */
        locationScenario: UserActivityScenario | PowerConsumptionScenario;
        /**
         * Indicates the type of sports.
         * This parameter is valid only when locationScenario is set to UserActivityScenario.SPORT.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @atomicservice
         * @since 26.0.0
         */
        sportsType?: SportsType;
        /**
         * Indicates whether to obtain POI information near the current location.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice
         * @since 19
         */
        needPoi?: boolean;
    }
    /**
     * Configuring parameters in single location requests.
     *
     * @syscap SystemCapability.Location.Location.Core
     * @crossplatform [since 22]
     * @atomicservice
     * @since 12
     */
    export interface SingleLocationRequest {
        /**
         * Priority of the location request.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice
         * @since 12
         */
        locatingPriority: LocatingPriority;
        /**
         * Timeout of a single location request, in milliseconds.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice
         * @since 12
         */
        locatingTimeoutMs: number;
        /**
         * Indicates whether to obtain POI information near the current location.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice
         * @since 19
         */
        needPoi?: boolean;
    }
    /**
     * Provides information about geographic locations.
     *
     * @syscap SystemCapability.Location.Location.Core
     * @crossplatform [since 22]
     * @atomicservice [since 11]
     * @since 9
     */
    export interface Location {
        /**
         * Indicates latitude information.
         * A positive value indicates north latitude,
         * and a negative value indicates south latitude.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice [since 11]
         * @since 9
         */
        latitude: number;
        /**
         * Indicates Longitude information.
         * A positive value indicates east longitude ,
         * and a negative value indicates west longitude.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice [since 11]
         * @since 9
         */
        longitude: number;
        /**
         * Indicates location altitude, in meters.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice [since 11]
         * @since 9
         */
        altitude: number;
        /**
         * Indicates location accuracy, in meters.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice [since 11]
         * @since 9
         */
        accuracy: number;
        /**
         * Indicates speed, in m/s.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice [since 11]
         * @since 9
         */
        speed: number;
        /**
         * Indicates location timestamp in the UTC format.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice [since 11]
         * @since 9
         */
        timeStamp: number;
        /**
         * Indicates direction information.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice [since 11]
         * @since 9
         */
        direction: number;
        /**
         * Indicates location timestamp since boot.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice [since 11]
         * @since 9
         */
        timeSinceBoot: number;
        /**
         * Indicates additional information.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice [since 11]
         * @since 9
         */
        additions?: Array<string>;
        /**
         * Indicates additional information map.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice
         * @since 12
         */
        additionsMap?: Map<string, string>;
        /**
         * Indicates the amount of additional descriptive information.
         *
         * @type { ?number } [since 9 - 10]
         * @type { ?number } [since 11]
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice [since 11]
         * @since 9
         */
        additionSize?: number;
        /**
         * Indicates whether the location is mocked.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @atomicservice
         * @since 26.0.0
         */
        isFromMock?: boolean;
        /**
         * Indicates vertical position accuracy in meters.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice
         * @since 12
         */
        altitudeAccuracy?: number;
        /**
         * Indicates speed accuracy in meter per seconds.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice
         * @since 12
         */
        speedAccuracy?: number;
        /**
         * Indicates direction accuracy in degrees.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice
         * @since 12
         */
        directionAccuracy?: number;
        /**
         * Time uncertainty Of timeSinceBoot in nanosecond.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice
         * @since 12
         */
        uncertaintyOfTimeSinceBoot?: number;
        /**
         * Indicates the source of the location.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice
         * @since 12
         */
        sourceType?: LocationSourceType;
        /**
         * Indicates the poi information.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice
         * @since 19
         */
        poi?: PoiInfo;
    }
    /**
     * Describes the contents of the bluetooth scan results.
     *
     * @syscap SystemCapability.Location.Location.Core
     * @crossplatform [since 22]
     * @since 16
     */
    export interface BluetoothScanResult {
        /**
         * Address of the scanned device
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @since 16
         */
        deviceId: string;
        /**
         * RSSI of the scanned device
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @since 16
         */
        rssi: number;
        /**
         * The raw data of broadcast packet
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @since 16
         */
        data?: ArrayBuffer;
        /**
         * The local name of the scanned device
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @since 16
         */
        deviceName: string;
        /**
         * Connectable of the scanned device
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @since 16
         */
        connectable: boolean;
    }
    /**
     * Describes the information about a single POI.
     *
     * @syscap SystemCapability.Location.Location.Core
     * @atomicservice
     * @since 19
     */
    export interface Poi {
        /**
         * Indicates the ID of a POI.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @atomicservice
         * @since 19
         */
        id: string;
        /**
         * Indicates the confidence of POI information.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @atomicservice
         * @since 19
         */
        confidence: number;
        /**
         * Indicates the name of the POI.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @atomicservice
         * @since 19
         */
        name: string;
        /**
         * Indicates the latitude of POI.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @atomicservice
         * @since 19
         */
        latitude: number;
        /**
         * Indicates the longitude of POI.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @atomicservice
         * @since 19
         */
        longitude: number;
        /**
         * Indicates administrative region name.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @atomicservice
         * @since 19
         */
        administrativeArea: string;
        /**
         * Indicates sub-administrative region name.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @atomicservice
         * @since 19
         */
        subAdministrativeArea: string;
        /**
         * Indicates locality information.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @atomicservice
         * @since 19
         */
        locality: string;
        /**
         * Indicates sub-locality information.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @atomicservice
         * @since 19
         */
        subLocality: string;
        /**
         * Indicates the detailed address of the POI.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @atomicservice
         * @since 19
         */
        address: string;
        /**
         * Additional information about the POI.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        additionalInfo?: string;
    }
    /**
     * Describes the POI information struct.
     *
     * @syscap SystemCapability.Location.Location.Core
     * @atomicservice
     * @since 19
     */
    export interface PoiInfo {
        /**
         * Indicates POI information list.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @atomicservice
         * @since 19
         */
        poiArray: Array<Poi>;
        /**
         * Indicates the timestamp when the POI information is obtained.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @atomicservice
         * @since 19
         */
        timestamp: number;
    }
    /**
     * Beacon equipment manufacturer data.
     *
     * @syscap SystemCapability.Location.Location.Geofence
     * @atomicservice
     * @since 20
     */
    export interface BeaconManufactureData {
        /**
         * Manufacture id.
         *
         * @syscap SystemCapability.Location.Location.Geofence
         * @atomicservice
         * @since 20
         */
        manufactureId: number;
        /**
         * Manufacture data.
         *
         * @syscap SystemCapability.Location.Location.Geofence
         * @atomicservice
         * @since 20
         */
        manufactureData: ArrayBuffer;
        /**
         * Manufacture data mask.
         *
         * @syscap SystemCapability.Location.Location.Geofence
         * @atomicservice
         * @since 20
         */
        manufactureDataMask: ArrayBuffer;
    }
    /**
     * Beacon fence details.
     *
     * @syscap SystemCapability.Location.Location.Geofence
     * @atomicservice
     * @since 20
     */
    export interface BeaconFence {
        /**
         * Identifier of the beacon fence.
         *
         * @syscap SystemCapability.Location.Location.Geofence
         * @atomicservice
         * @since 20
         */
        identifier: string;
        /**
         * Beacon fence information type.
         *
         * @syscap SystemCapability.Location.Location.Geofence
         * @atomicservice
         * @since 20
         */
        beaconFenceInfoType: BeaconFenceInfoType;
        /**
         * Beacon equipment manufacture data.
         *
         * @syscap SystemCapability.Location.Location.Geofence
         * @atomicservice
         * @since 20
         */
        manufactureData?: BeaconManufactureData;
    }
    /**
     * Configuring parameters in BeaconFence request.
     *
     * @syscap SystemCapability.Location.Location.Geofence
     * @atomicservice
     * @since 20
     */
    export interface BeaconFenceRequest {
        /**
         * Beacon fence information.
         *
         * @syscap SystemCapability.Location.Location.Geofence
         * @atomicservice
         * @since 20
         */
        beacon: BeaconFence;
        /**
         * Indicates the callback for reporting the BeaconFence transition status.
         *
         * @syscap SystemCapability.Location.Location.Geofence
         * @atomicservice
         * @since 20
         */
        transitionCallback?: Callback<GeofenceTransition>;
        /**
         * Indicates the name of FenceExtensionAbility.
         *
         * @syscap SystemCapability.Location.Location.Geofence
         * @atomicservice
         * @since 20
         */
        fenceExtensionAbilityName?: string;
    }
    /**
     * Matching WLAN information structure.
     *
     * @syscap SystemCapability.Location.Location.Core
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    export interface MatchingWlanInfo {
        /**
         * Indicates the index of the matched WLAN in the wlanBssidArray.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        index: number;
        /**
         * WLAN SSID.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        ssid: string;
    }
    /**
     * Enum for the source of the location.
     *
     * @syscap SystemCapability.Location.Location.Core
     * @crossplatform [since 22]
     * @atomicservice
     * @since 12
     */
    export enum LocationSourceType {
        /**
         * The location is obtained from the GNSS.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice
         * @since 12
         */
        GNSS = 1,
        /**
         * The location comes from the network positioning technology.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice
         * @since 12
         */
        NETWORK = 2,
        /**
         * The location comes from the indoor positioning technology.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice
         * @since 12
         */
        INDOOR = 3,
        /**
         * The location comes from the GNSS RTK technology.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice
         * @since 12
         */
        RTK = 4
    }
    /**
     * Enum for coordinate system type.
     *
     * @syscap SystemCapability.Location.Location.Geofence
     * @crossplatform [since 22]
     * @since 12
     */
    export enum CoordinateSystemType {
        /**
         * WGS84 coordinates system.
         *
         * @syscap SystemCapability.Location.Location.Geofence
         * @crossplatform [since 22]
         * @since 12
         */
        WGS84 = 1,
        /**
         * GCJ-02 coordinates system.
         *
         * @syscap SystemCapability.Location.Location.Geofence
         * @crossplatform [since 22]
         * @since 12
         */
        GCJ02 = 2
    }
    /**
     * Enum for location error code.
     *
     * @syscap SystemCapability.Location.Location.Core
     * @crossplatform [since 22]
     * @atomicservice
     * @since 12
     */
    export enum LocationError {
        /**
         * Default cause for location failure.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice
         * @since 12
         */
        LOCATING_FAILED_DEFAULT = -1,
        /**
         * Locating failed because the location permission fails to be verified.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice
         * @since 12
         */
        LOCATING_FAILED_LOCATION_PERMISSION_DENIED = -2,
        /**
         * Locating failed because the app is in the background and the background location permission verification failed.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice
         * @since 12
         */
        LOCATING_FAILED_BACKGROUND_PERMISSION_DENIED = -3,
        /**
         * Locating failed because the location switch is turned off.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice
         * @since 12
         */
        LOCATING_FAILED_LOCATION_SWITCH_OFF = -4,
        /**
         * Locating failed because internet access failure.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice
         * @since 12
         */
        LOCATING_FAILED_INTERNET_ACCESS_FAILURE = -5
    }
    /**
     * Enum for geofence transition status.
     *
     * @syscap SystemCapability.Location.Location.Geofence
     * @crossplatform [since 22]
     * @since 12
     */
    export enum GeofenceTransitionEvent {
        /**
         * The device is within the geofence.
         *
         * @syscap SystemCapability.Location.Location.Geofence
         * @crossplatform [since 22]
         * @since 12
         */
        GEOFENCE_TRANSITION_EVENT_ENTER = 1,
        /**
         * The device is out of the geofence.
         *
         * @syscap SystemCapability.Location.Location.Geofence
         * @crossplatform [since 22]
         * @since 12
         */
        GEOFENCE_TRANSITION_EVENT_EXIT = 2,
        /**
         * The device is in the geographical fence for a period of time.
         *
         * @syscap SystemCapability.Location.Location.Geofence
         * @crossplatform [since 22]
         * @since 12
         */
        GEOFENCE_TRANSITION_EVENT_DWELL = 4
    }
    /**
     * Enum for satellite constellation category.
     *
     * @syscap SystemCapability.Location.Location.Gnss
     * @crossplatform [since 22]
     * @since 12
     */
    export enum SatelliteConstellationCategory {
        /**
         * Invalid value.
         *
         * @syscap SystemCapability.Location.Location.Gnss
         * @crossplatform [since 22]
         * @since 12
         */
        CONSTELLATION_CATEGORY_UNKNOWN = 0,
        /**
         * GPS.
         *
         * @syscap SystemCapability.Location.Location.Gnss
         * @crossplatform [since 22]
         * @since 12
         */
        CONSTELLATION_CATEGORY_GPS = 1,
        /**
         * SBAS.
         *
         * @syscap SystemCapability.Location.Location.Gnss
         * @crossplatform [since 22]
         * @since 12
         */
        CONSTELLATION_CATEGORY_SBAS = 2,
        /**
         * GLONASS.
         *
         * @syscap SystemCapability.Location.Location.Gnss
         * @crossplatform [since 22]
         * @since 12
         */
        CONSTELLATION_CATEGORY_GLONASS = 3,
        /**
         * QZSS.
         *
         * @syscap SystemCapability.Location.Location.Gnss
         * @crossplatform [since 22]
         * @since 12
         */
        CONSTELLATION_CATEGORY_QZSS = 4,
        /**
         * BEIDOU.
         *
         * @syscap SystemCapability.Location.Location.Gnss
         * @crossplatform [since 22]
         * @since 12
         */
        CONSTELLATION_CATEGORY_BEIDOU = 5,
        /**
         * GALILEO.
         *
         * @syscap SystemCapability.Location.Location.Gnss
         * @crossplatform [since 22]
         * @since 12
         */
        CONSTELLATION_CATEGORY_GALILEO = 6,
        /**
         * IRNSS.
         *
         * @syscap SystemCapability.Location.Location.Gnss
         * @crossplatform [since 22]
         * @since 12
         */
        CONSTELLATION_CATEGORY_IRNSS = 7
    }
    /**
     * Enum for satellite additional information.
     *
     * @syscap SystemCapability.Location.Location.Gnss
     * @crossplatform [since 22]
     * @since 12
     */
    export enum SatelliteAdditionalInfo {
        /**
         * Default value.
         *
         * @syscap SystemCapability.Location.Location.Gnss
         * @crossplatform [since 22]
         * @since 12
         */
        SATELLITES_ADDITIONAL_INFO_NULL = 0,
        /**
         * Ephemeris data exist.
         *
         * @syscap SystemCapability.Location.Location.Gnss
         * @crossplatform [since 22]
         * @since 12
         */
        SATELLITES_ADDITIONAL_INFO_EPHEMERIS_DATA_EXIST = 1,
        /**
         * Almanac data exist.
         *
         * @syscap SystemCapability.Location.Location.Gnss
         * @crossplatform [since 22]
         * @since 12
         */
        SATELLITES_ADDITIONAL_INFO_ALMANAC_DATA_EXIST = 2,
        /**
         * This satellite is being used in location fix.
         *
         * @syscap SystemCapability.Location.Location.Gnss
         * @crossplatform [since 22]
         * @since 12
         */
        SATELLITES_ADDITIONAL_INFO_USED_IN_FIX = 4,
        /**
         * Carrier frequency exist.
         *
         * @syscap SystemCapability.Location.Location.Gnss
         * @crossplatform [since 22]
         * @since 12
         */
        SATELLITES_ADDITIONAL_INFO_CARRIER_FREQUENCY_EXIST = 8
    }
    /**
     * Enum for user activity scenario.
     *
     * @syscap SystemCapability.Location.Location.Core
     * @crossplatform [since 22]
     * @atomicservice
     * @since 12
     */
    export enum UserActivityScenario {
        /**
         * Navigation scenario. High positioning precision and real-time performance are required.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice
         * @since 12
         */
        NAVIGATION = 0x401,
        /**
         * Sport scenario. High positioning precision is required.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice
         * @since 12
         */
        SPORT = 0x402,
        /**
         * Transport scenario. High positioning precision and real-time performance are required.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice
         * @since 12
         */
        TRANSPORT = 0x403,
        /**
         * Daily life scenarios. Low requirements on positioning precision.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice
         * @since 12
         */
        DAILY_LIFE_SERVICE = 0x404
    }
    /**
     * Enum for locating priority.
     *
     * @syscap SystemCapability.Location.Location.Core
     * @crossplatform [since 22]
     * @atomicservice
     * @since 12
     */
    export enum LocatingPriority {
        /**
         * Preferentially ensure the highest locating accuracy.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice
         * @since 12
         */
        PRIORITY_ACCURACY = 0x501,
        /**
         * Preferentially ensure the fastest locating speed.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice
         * @since 12
         */
        PRIORITY_LOCATING_SPEED = 0x502
    }
    /**
     * Enum for location priority.
     *
     * @syscap SystemCapability.Location.Location.Core
     * @crossplatform [since 22]
     * @atomicservice [since 11]
     * @since 9
     */
    export enum LocationRequestPriority {
        /**
         * Default priority.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice [since 11]
         * @since 9
         */
        UNSET = 0x200,
        /**
         * Preferentially ensure the locating accuracy.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice [since 11]
         * @since 9
         */
        ACCURACY,
        /**
         * Preferentially ensure low power consumption for locating.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice [since 11]
         * @since 9
         */
        LOW_POWER,
        /**
         * Preferentially ensure that the first location is time-consuming.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice [since 11]
         * @since 9
         */
        FIRST_FIX
    }
    /**
     * Enum for location scenario.
     *
     * @syscap SystemCapability.Location.Location.Core
     * @crossplatform [since 22]
     * @atomicservice [since 11]
     * @since 9
     */
    export enum LocationRequestScenario {
        /**
         * Default scenario.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice [since 11]
         * @since 9
         */
        UNSET = 0x300,
        /**
         * Navigation scenario. High positioning precision and real-time performance are required.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice [since 11]
         * @since 9
         */
        NAVIGATION,
        /**
         * Trajectory tracking scenario. High positioning precision is required.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice [since 11]
         * @since 9
         */
        TRAJECTORY_TRACKING,
        /**
         * Car hailing scenario. High positioning precision and real-time performance are required.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice [since 11]
         * @since 9
         */
        CAR_HAILING,
        /**
         * Daily life scenarios. Low requirements on positioning precision and real-time performance.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice [since 11]
         * @since 9
         */
        DAILY_LIFE_SERVICE,
        /**
         * Power saving scenarios.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice [since 11]
         * @since 9
         */
        NO_POWER
    }
    /**
     * Enum for power consumption scenario.
     *
     * @syscap SystemCapability.Location.Location.Core
     * @crossplatform [since 22]
     * @atomicservice
     * @since 12
     */
    export enum PowerConsumptionScenario {
        /**
         * High power consumption mode.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice
         * @since 12
         */
        HIGH_POWER_CONSUMPTION = 0x601,
        /**
         * Low power consumption mode.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice
         * @since 12
         */
        LOW_POWER_CONSUMPTION = 0x602,
        /**
         * Power saving scenarios.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice
         * @since 12
         */
        NO_POWER_CONSUMPTION = 0x603
    }
    /**
     * Enum for sports type
     *
     * @syscap SystemCapability.Location.Location.Core
     * @crossplatform [since 22]
     * @atomicservice
     * @since 18
     */
    export enum SportsType {
        /**
         * Indicates running.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice
         * @since 18
         */
        RUNNING = 1,
        /**
         * Indicates walking.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice
         * @since 18
         */
        WALKING = 2,
        /**
         * Indicates cycling.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @atomicservice
         * @since 18
         */
        CYCLING = 3,
        /**
         * Indicates Skiing.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @stagemodelonly
         * @crossplatform
         * @atomicservice
         * @since 26.0.0
         */
        SKIING = 4
    }
    /**
     * Location subsystem command structure.
     *
     * @syscap SystemCapability.Location.Location.Core
     * @since 9
     */
    export interface LocationCommand {
        /**
         * Information about the scenario where the command is sent.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @since 9
         */
        scenario: LocationRequestScenario;
        /**
         * Sent command content.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @since 9
         */
        command: string;
    }
    /**
     * Country code structure.
     *
     * @syscap SystemCapability.Location.Location.Core
     * @crossplatform [since 22]
     * @since 9
     */
    export interface CountryCode {
        /**
         * Country code character string.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @since 9
         */
        country: string;
        /**
         * Country code source.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @since 9
         */
        type: CountryCodeType;
    }
    /**
     * Indicates a location point, including the longitude and latitude.
     *
     * @syscap SystemCapability.Location.Location.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    export interface Point {
        /**
         * Indicates latitude.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        latitude: number;
        /**
         * Indicates longitude.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        longitude: number;
    }
    /**
     * Enum for country code type.
     *
     * @syscap SystemCapability.Location.Location.Core
     * @crossplatform [since 22]
     * @since 9
     */
    export enum CountryCodeType {
        /**
         * Country code obtained from the locale setting.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @since 9
         */
        COUNTRY_CODE_FROM_LOCALE = 1,
        /**
         * Country code obtained from the SIM information.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @since 9
         */
        COUNTRY_CODE_FROM_SIM = 2,
        /**
         * Query the country code information from the reverse geocoding result.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @since 9
         */
        COUNTRY_CODE_FROM_LOCATION = 3,
        /**
         * Obtain the country code from the cell registration information.
         *
         * @syscap SystemCapability.Location.Location.Core
         * @crossplatform [since 22]
         * @since 9
         */
        COUNTRY_CODE_FROM_NETWORK = 4
    }
    /**
     * Enum for the beacon fence information type.
     *
     * @syscap SystemCapability.Location.Location.Geofence
     * @atomicservice
     * @since 20
     */
    export enum BeaconFenceInfoType {
        /**
         * Identifies a beacon device using beacon device manufacture data.
         *
         * @syscap SystemCapability.Location.Location.Geofence
         * @atomicservice
         * @since 20
         */
        BEACON_MANUFACTURE_DATA = 1
    }
}
export default geoLocationManager;

```
