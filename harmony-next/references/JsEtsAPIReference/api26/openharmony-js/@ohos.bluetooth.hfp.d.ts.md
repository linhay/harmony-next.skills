# @ohos.bluetooth.hfp.d.ts

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
 * Provides methods to accessing bluetooth call-related capabilities.
 *
 * @syscap SystemCapability.Communication.Bluetooth.Core
 * @since 10
 */
declare namespace hfp {
    /**
     * Base interface of profile.
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @since 10
     */
    type BaseProfile = baseProfile.BaseProfile;
    /**
     * create the instance of hfp profile.
     *
     * @returns { HandsFreeAudioGatewayProfile } Returns the instance of profile.
     * @throws { BusinessError } 401 - Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @since 10
     */
    function createHfpAgProfile(): HandsFreeAudioGatewayProfile;
    /**
     * create the instance of HF(Hands-Free Unit) for HFP(Hands-Free Profile).
     *
     * @returns { HandsFreeHfProfile } Returns the instance of profile.
     * @throws { BusinessError } 801 - Capability not supported.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    function createHfpHfProfile(): HandsFreeHfProfile;
    /**
     * Manager hfp source profile.
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @since 10
     */
    interface HandsFreeAudioGatewayProfile extends BaseProfile {
    }
    /**
     * Manage hfp sink profile.
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    interface HandsFreeHfProfile extends BaseProfile {
    }
}
export default hfp;

```
