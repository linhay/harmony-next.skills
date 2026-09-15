# @ohos.thermal.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2023 Huawei Device Co., Ltd.
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
 * @kit BasicServicesKit
 */
import { AsyncCallback, Callback } from './@ohos.base';
/**
 * The **thermal** module provides thermal level-related callback and query APIs to obtain the information required for
 * thermal control.
 *
 * @syscap SystemCapability.PowerManager.ThermalManager
 * @since 8
 */
declare namespace thermal {
    /**
     * Enumerates thermal levels.
     *
     * @syscap SystemCapability.PowerManager.ThermalManager
     * @since 8
     */
    export enum ThermalLevel {
        /**
         * The device is cool, and services are not restricted.
         *
         * @syscap SystemCapability.PowerManager.ThermalManager
         * @since 8
         */
        COOL = 0,
        /**
         * The device is in the normal temperature range but it is getting warm. You need to downgrade or reduce the load of
         * imperceptible services.
         *
         * @syscap SystemCapability.PowerManager.ThermalManager
         * @since 8
         */
        NORMAL = 1,
        /**
         * The device is warm. You need to stop or delay some imperceptible services.
         *
         * @syscap SystemCapability.PowerManager.ThermalManager
         * @since 8
         */
        WARM = 2,
        /**
         * The device is heating up. You need to stop all imperceptible services and downgrade or reduce the load of non-
         * critical services.
         *
         * @syscap SystemCapability.PowerManager.ThermalManager
         * @since 8
         */
        HOT = 3,
        /**
         * The device is overheated. You need to stop all imperceptible services and downgrade or reduce the load of major
         * foreground services.
         *
         * @syscap SystemCapability.PowerManager.ThermalManager
         * @since 8
         */
        OVERHEATED = 4,
        /**
         * The device is overheated and is about to enter the emergency state. You need to stop all imperceptible services
         * and downgrade major foreground services to the maximum extent.
         *
         * @syscap SystemCapability.PowerManager.ThermalManager
         * @since 8
         */
        WARNING = 5,
        /**
         * The device has entered the emergency state. You need to stop all services except those for fundamental use.
         *
         * @syscap SystemCapability.PowerManager.ThermalManager
         * @since 8
         */
        EMERGENCY = 6,
        /**
         * The device is about to enter the escape state. You need to stop all services and take necessary emergency
         * measures such as data backup.
         *
         * @syscap SystemCapability.PowerManager.ThermalManager
         * @since 11
         */
        ESCAPE = 7
    }
    /**
     * Subscribes to the thermal level changes. This API uses an asynchronous callback to return the result.
     *
     * @param { AsyncCallback<ThermalLevel> } callback - Callback used to return thermal level. This parameter is of the
     *     function type.
     * @syscap SystemCapability.PowerManager.ThermalManager
     * @since 8
     * @deprecated since 9
     * @useinstead thermal.registerThermalLevelCallback
     */
    function subscribeThermalLevel(callback: AsyncCallback<ThermalLevel>): void;
    /**
     * Registers a callback to be invoked when the thermal level changes. This API uses an asynchronous callback to return
     * the result.
     *
     * @param { Callback<ThermalLevel> } callback - Callback used to return thermal level. This parameter is of the
     *     function type.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Incorrect parameter types;
     * @syscap SystemCapability.PowerManager.ThermalManager
     * @since 9
     */
    function registerThermalLevelCallback(callback: Callback<ThermalLevel>): void;
    /**
     * Unsubscribes from the thermal level changes. This API uses an asynchronous callback to return the result.
     *
     * @param { AsyncCallback<void> } callback - Callback that returns no value. If this parameter is not set, all
     *     callbacks will be unregistered.
     * @syscap SystemCapability.PowerManager.ThermalManager
     * @since 8
     * @deprecated since 9
     * @useinstead thermal.unregisterThermalLevelCallback
     */
    function unsubscribeThermalLevel(callback?: AsyncCallback<void>): void;
    /**
     * Unregisters from the thermal level changes. This API uses an asynchronous callback to return the result.
     *
     * @param { Callback<void> } callback - (Optional) Callback that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Incorrect parameter types;
     * @syscap SystemCapability.PowerManager.ThermalManager
     * @since 9
     */
    function unregisterThermalLevelCallback(callback?: Callback<void>): void;
    /**
     * Obtains the current thermal level.
     *
     * @returns { ThermalLevel } Thermal level.
     * @syscap SystemCapability.PowerManager.ThermalManager
     * @since 8
     * @deprecated since 9
     * @useinstead thermal.getLevel
     */
    function getThermalLevel(): ThermalLevel;
    /**
     * Obtains the current thermal level.
     *
     * @returns { ThermalLevel } Thermal level.
     * @syscap SystemCapability.PowerManager.ThermalManager
     * @since 9
     */
    function getLevel(): ThermalLevel;
}
export default thermal;

```
