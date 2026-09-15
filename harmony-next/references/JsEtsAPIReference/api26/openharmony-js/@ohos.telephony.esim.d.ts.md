# @ohos.telephony.esim.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2024-2024 Huawei Device Co., Ltd.
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
 * @kit TelephonyKit
 */
/**
 * This indicates that the eSIM card performs the profile management operation synchronously.
 * Includes methods defined by GSMA Spec (SGP.22) and customized methods.
 *
 * @namespace eSIM
 * @syscap SystemCapability.Telephony.CoreService.Esim
 * @since 18
 */
declare namespace eSIM {
    /**
     * Whether embedded subscriptions are currently supported.
     *
     * @param { number } slotId - Indicates the card slot index number.
     * @returns { boolean } Returns {@code true} if the eSIM capability is supported; returns {@code false} otherwise.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     *     3. Parameter verification failed.
     * @throws { BusinessError } 3120001 - Service connection failed.
     * @throws { BusinessError } 3120002 - System internal error.
     * @syscap SystemCapability.Telephony.CoreService.Esim
     * @since 18
     */
    function isSupported(slotId: number): boolean;
    /**
     * Starts a page through an ability, on which users can touch the button to download a profile.
     *
     * @permission ohos.permission.SET_TELEPHONY_ESIM_STATE_OPEN
     * @param { DownloadableProfile } profile - Bound profile package data returned by the SM-DP+ server.
     * @returns { Promise<boolean> } Returns {@code true} if the profile is added successfully;
     * returns {@code false} otherwise.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types.
     *     3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 3120001 - Service connection failed.
     * @throws { BusinessError } 3120002 - System internal error.
     * @syscap SystemCapability.Telephony.CoreService.Esim
     * @since 18
     */
    function addProfile(profile: DownloadableProfile): Promise<boolean>;
    /**
     * Establishes a single UICC access rule pursuant to the GlobalPlatform Secure Element Access Control specification.
     *
     * @interface AccessRule
     * @syscap SystemCapability.Telephony.CoreService.Esim
     * @since 20
     */
    export interface AccessRule {
        /**
         * Certificate hash hexadecimal string.
         *
         * @type { string }
         * @syscap SystemCapability.Telephony.CoreService.Esim
         * @since 20
         */
        certificateHashHexStr: string;
        /**
         * The name of package.
         *
         * @type { string }
         * @syscap SystemCapability.Telephony.CoreService.Esim
         * @since 20
         */
        packageName: string;
        /**
         * The type of access.
         *
         * @type { number }
         * @syscap SystemCapability.Telephony.CoreService.Esim
         * @since 20
         */
        accessType: number;
    }
    /**
     * Information about a profile which is downloadable to an eUICC using.
     *
     * @interface DownloadableProfile
     * @syscap SystemCapability.Telephony.CoreService.Esim
     * @since 18
     */
    export interface DownloadableProfile {
        /**
         * Activation code.
         *
         * @type { string }
         * @syscap SystemCapability.Telephony.CoreService.Esim
         * @since 18
         */
        activationCode: string;
        /**
         * Confirmation code.
         *
         * @type { ?string }
         * @syscap SystemCapability.Telephony.CoreService.Esim
         * @since 18
         */
        confirmationCode?: string;
        /**
         * Carrier name.
         *
         * @type { ?string }
         * @syscap SystemCapability.Telephony.CoreService.Esim
         * @since 18
         */
        carrierName?: string;
        /**
         * Gets the accessRules.
         *
         * @type { ?Array<AccessRule> }
         * @syscap SystemCapability.Telephony.CoreService.Esim
         * @since 18
         */
        accessRules?: Array<AccessRule>;
    }
}
export default eSIM;

```
