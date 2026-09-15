# @ohos.bluetooth.pan.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (C) 2023 Huawei Device Co., Ltd.
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
 * @kit ConnectivityKit
 */
import type baseProfile from './@ohos.bluetooth.baseProfile';
/**
 * Provides methods to accessing bluetooth PAN(Personal Area Networking Profile)-related capabilities.
 *
 * @syscap SystemCapability.Communication.Bluetooth.Core
 * @stagemodelonly
 * @since 10
 */
declare namespace pan {
    /**
     * Base interface of profile.
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 10
     */
    type BaseProfile = baseProfile.BaseProfile;
    /**
     * create the instance of pan profile.
     *
     * @returns { PanProfile } Returns the instance of pan profile.
     * @throws { BusinessError } 401 - Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 10
     */
    function createPanProfile(): PanProfile;
    /**
     * Manager pan host profile.
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 10
     */
    interface PanProfile extends BaseProfile {
        /**
         * Obtains the tethering enable or disable.
         *
         * @permission ohos.permission.ACCESS_BLUETOOTH
         * @returns { boolean } Returns the value {@code true} is tethering is on, returns {@code false} otherwise.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 801 - Capability not supported.
         *     Only can be called on phone, tablet, and 2in1 devices.
         *     Failed to call the API when the short-range chip is not inserted on 2in1 device.
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        isTetheringOn(): boolean;
        /**
         * Determine whether the local device supports PAN.
         *
         * @returns { boolean } Returns true if the local device supports PAN; returns false otherwise.
         * @throws { BusinessError } 2900099 - Operation failed.
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        isPanSupported(): boolean;
    }
}
export default pan;

```
