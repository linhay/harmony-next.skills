# @ohos.net.eap.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2025 Huawei Device Co., Ltd.
 * Licensed under the Apache License, Version 2.0 (the "License"),
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
 * @file Extensible Authentication
 * @kit NetworkKit
 */
import { Callback } from "./@ohos.base";
/**
 * The **eap** module provides the extensible authentication mechanism to enable third-party clients to access custom 80
 * 2.1X (a port-based network access control protocol) authentication, such as Extensible Authentication Protocol (EAP)
 * authentication.
 *
 * @syscap SystemCapability.Communication.NetManager.Eap
 * @since 20
 */
declare namespace eap {
    /**
     * Registers a custom handler of Extensible Authentication Protocol (EAP) packets for extensible authentication. This
     * API returns the result asynchronously through a callback.
     *
     * The system will encapsulate the eligible EAP packets into the callback function for enterprise applications to
     * retrieve.
     *
     * @permission ohos.permission.MANAGE_ENTERPRISE_WIFI_CONNECTION
     * @param { number } netType - Network type. The value can be **1** or **2**.
     *     <br>The value **1** indicates WLAN, and the value **2** indicates Ethernet.
     * @param { number } eapCode - EAP code. The value can be any of the following:
     *     <br>code=1 Request, code=2 Response, code=3 Success, code=4 Failure.
     * @param { number } eapType - EAP method. The value range is [0, 255].
     *     <br>Common values include the following: eapType=1 Identity, eapType=2 Notification, eapType=3 NAK, eapType=4
     *     MD5-Challenge, eapType=5 OTP (One-Time Password), eapType=6 GTC (Generic Token Card), eapType=13 EAP-TLS,
     *     eapType=21 EAP-TTLS, eapType=25 EAP-PEAP, eapType=254 Expanded Types, and eapType=255 Experimental use.
     * @param { Callback<EapData> } callback - Callback function, which returns the packet of the specified eapCode+
     *     eapType.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 33200006 - Invalid net type
     * @throws { BusinessError } 33200007 - Invalid eap code
     * @throws { BusinessError } 33200008 - Invalid eap type
     * @throws { BusinessError } 33200009 - netmanager stop
     * @throws { BusinessError } 33200099 - internal error
     * @syscap SystemCapability.Communication.NetManager.Eap
     * @since 20
     */
    function regCustomEapHandler(netType: number, eapCode: number, eapType: number, callback: Callback<EapData>): void;
    /**
     * Unregisters the custom handler of EAP packets for extensible authentication. This API returns the result
     * asynchronously through a callback.
     *
     * @permission ohos.permission.MANAGE_ENTERPRISE_WIFI_CONNECTION
     * @param { number } netType - Network type. The value can be **1** or **2**.
     *     <br>The value **1** indicates WLAN, and the value **2** indicates Ethernet.
     * @param { number } eapCode - EAP code. The value can be any of the following:
     *     <br>code=1 Request, code=2 Response, code=3 Success, code=4 Failure.
     * @param { number } eapType - EAP method. The value range is [0, 255].
     *     <br>Common values include the following: eapType=1 Identity, eapType=2 Notification, eapType=3 NAK, eapType=4
     *     MD5-Challenge, eapType=5 OTP (One-Time Password), eapType=6 GTC (Generic Token Card), eapType=13 EAP-TLS,
     *     eapType=21 EAP-TTLS, eapType=25 EAP-PEAP, eapType=254 Expanded Types, and eapType=255 Experimental use.
     * @param { Callback<EapData> } callback - Callback function, which returns the packet of the specified eapCode+
     *     eapType.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 33200006 - Invalid net type
     * @throws { BusinessError } 33200007 - Invalid eap code
     * @throws { BusinessError } 33200008 - Invalid eap type
     * @throws { BusinessError } 33200009 - netmanager stop
     * @throws { BusinessError } 33200099 - internal error
     * @syscap SystemCapability.Communication.NetManager.Eap
     * @since 20
     */
    function unregCustomEapHandler(netType: number, eapCode: number, eapType: number, callback: Callback<EapData>): void;
    /**
     * Notifies the system of the extensible authentication result.
     *
     * > **NOTE**
     * >
     * > - If this callback is used to process received EAP data packets, the customized portion added by the server must
     * > be removed from the EAP data transmitted to the system.
     * >
     * > - If this callback is used to process sent EAP data packets, the EAP data transmitted to the system is the EAP
     * > data with the customized portion added by the server.
     *
     * @permission ohos.permission.MANAGE_ENTERPRISE_WIFI_CONNECTION
     * @param { CustomResult } result - Extensible authentication result.
     * @param { EapData } data - EAP data.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 33200004 - Invalid result
     * @throws { BusinessError } 33200005 - Invalid size of eap data
     * @throws { BusinessError } 33200009 - netmanager stop
     * @throws { BusinessError } 33200099 - internal error
     * @syscap SystemCapability.Communication.NetManager.Eap
     * @since 20
     */
    function replyCustomEapData(result: CustomResult, data: EapData): void;
    /**
     * Starts EAP authentication on an Ethernet NIC.
     *
     * @permission ohos.permission.MANAGE_ENTERPRISE_WIFI_CONNECTION
     * @param { number } netId - ID of the Ethernet NIC. If the default value **-1** is specified, the system automatically
     *     matches the Ethernet NIC to initiate EAP authentication.
     * @param { EthEapProfile } profile - EAP profile.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 33200001 - Invalid netId
     * @throws { BusinessError } 33200003 - Invalid profile
     * @throws { BusinessError } 33200009 - netmanager stop
     * @throws { BusinessError } 33200010 - invalid eth state
     * @throws { BusinessError } 33200099 - internal error
     * @syscap SystemCapability.Communication.NetManager.Eap
     * @since 20
     */
    function startEthEap(netId: number, profile: EthEapProfile): void;
    /**
     * Revokes the EAP-authenticated state of an Ethernet NIC.
     *
     * @permission ohos.permission.MANAGE_ENTERPRISE_WIFI_CONNECTION
     * @param { number } netId - ID of the Ethernet NIC. If the default value **-1** is specified, the system automatically
     *     matches the Ethernet NIC to initiate EAP authentication.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 33200001 - Invalid netId
     * @throws { BusinessError } 33200002 - Log off fail
     * @throws { BusinessError } 33200009 - netmanager stop
     * @throws { BusinessError } 33200010 - invalid eth state
     * @throws { BusinessError } 33200099 - internal error
     * @syscap SystemCapability.Communication.NetManager.Eap
     * @since 20
     */
    function logOffEthEap(netId: number): void;
    /**
     * Defines the EAP data.
     *
     * ​
     *
     * @syscap SystemCapability.Communication.NetManager.Eap
     * @since 20
     */
    interface EapData {
        /**
         * Pseudo random number used to associate the EAP data before and after processing.
         *
         * @syscap SystemCapability.Communication.NetManager.Eap
         * @since 20
         */
        msgId: number;
        /**
         * Raw EAP data starting from the EAP header, which is not encrypted.
         *
         * @syscap SystemCapability.Communication.NetManager.Eap
         * @since 20
         */
        eapBuffer: Uint8Array;
        /**
         * Data length.
         *
         * @syscap SystemCapability.Communication.NetManager.Eap
         * @since 20
         */
        bufferLen: number;
    }
    /**
     * Enumerates the EAP authentication results.
     *
     * ​
     *
     * @syscap SystemCapability.Communication.NetManager.Eap
     * @since 20
     */
    enum CustomResult {
        /**
         * The authentication process ends with a failed result.
         *
         * @syscap SystemCapability.Communication.NetManager.Eap
         * @since 20
         */
        RESULT_FAIL = 0,
        /**
         * The authentication is successful, and the process proceeds to the next step.
         *
         * @syscap SystemCapability.Communication.NetManager.Eap
         * @since 20
         */
        RESULT_NEXT = 1,
        /**
         * The authentication process ends with a successful result.
         *
         * @syscap SystemCapability.Communication.NetManager.Eap
         * @since 20
         */
        RESULT_FINISH = 2
    }
    /**
     * Enumerates the EAP authentication methods.
     *
     * @syscap SystemCapability.Communication.NetManager.Eap
     * @since 20
     */
    enum EapMethod {
        /**
         * Not specified.
         *
         * @syscap SystemCapability.Communication.NetManager.Eap
         * @since 20
         */
        EAP_NONE = 0,
        /**
         * PEAP.
         *
         * @syscap SystemCapability.Communication.NetManager.Eap
         * @since 20
         */
        EAP_PEAP = 1,
        /**
         * TLS.
         *
         * @syscap SystemCapability.Communication.NetManager.Eap
         * @since 20
         */
        EAP_TLS = 2,
        /**
         * TTLS.
         *
         * @syscap SystemCapability.Communication.NetManager.Eap
         * @since 20
         */
        EAP_TTLS = 3,
        /**
         * Password.
         *
         * @syscap SystemCapability.Communication.NetManager.Eap
         * @since 20
         */
        EAP_PWD = 4,
        /**
         * SIM.
         *
         * @syscap SystemCapability.Communication.NetManager.Eap
         * @since 20
         */
        EAP_SIM = 5,
        /**
         * AKA.
         *
         * @syscap SystemCapability.Communication.NetManager.Eap
         * @since 20
         */
        EAP_AKA = 6,
        /**
         * AKA Prime.
         *
         * @syscap SystemCapability.Communication.NetManager.Eap
         * @since 20
         */
        EAP_AKA_PRIME = 7,
        /**
         * UNAUTH TLS.
         *
         * @syscap SystemCapability.Communication.NetManager.Eap
         * @since 20
         */
        EAP_UNAUTH_TLS = 8
    }
    /**
     * Enumerates the Phase 2 authentication methods.
     *
     * @syscap SystemCapability.Communication.NetManager.Eap
     * @since 20
     */
    enum Phase2Method {
        /**
         * Not specified.
         *
         * @syscap SystemCapability.Communication.NetManager.Eap
         * @since 20
         */
        PHASE2_NONE = 0,
        /**
         * PAP.
         *
         * @syscap SystemCapability.Communication.NetManager.Eap
         * @since 20
         */
        PHASE2_PAP = 1,
        /**
         * MS-CHAP.
         *
         * @syscap SystemCapability.Communication.NetManager.Eap
         * @since 20
         */
        PHASE2_MSCHAP = 2,
        /**
         * MS-CHAPv2.
         *
         * @syscap SystemCapability.Communication.NetManager.Eap
         * @since 20
         */
        PHASE2_MSCHAPV2 = 3,
        /**
         * GTC.
         *
         * @syscap SystemCapability.Communication.NetManager.Eap
         * @since 20
         */
        PHASE2_GTC = 4,
        /**
         * SIM.
         *
         * @syscap SystemCapability.Communication.NetManager.Eap
         * @since 20
         */
        PHASE2_SIM = 5,
        /**
         * AKA.
         *
         * @syscap SystemCapability.Communication.NetManager.Eap
         * @since 20
         */
        PHASE2_AKA = 6,
        /**
         * AKA Prime.
         *
         * @syscap SystemCapability.Communication.NetManager.Eap
         * @since 20
         */
        PHASE2_AKA_PRIME = 7
    }
    /**
     * Represents the EAP profile information.
     *
     * @syscap SystemCapability.Communication.NetManager.Eap
     * @since 20
     */
    interface EthEapProfile {
        /**
         * EAP authentication method.
         *
         * @syscap SystemCapability.Communication.NetManager.Eap
         * @since 20
         */
        eapMethod: EapMethod;
        /**
         * Phase 2 authentication method.
         *
         * @syscap SystemCapability.Communication.NetManager.Eap
         * @since 20
         */
        phase2Method: Phase2Method;
        /**
         * Identity information.
         *
         * @syscap SystemCapability.Communication.NetManager.Eap
         * @since 20
         */
        identity: string;
        /**
         * Anonymous identity.
         *
         * @syscap SystemCapability.Communication.NetManager.Eap
         * @since 20
         */
        anonymousIdentity: string;
        /**
         * Password.
         *
         * @syscap SystemCapability.Communication.NetManager.Eap
         * @since 20
         */
        password: string;
        /**
         * CA certificate alias.
         *
         * @syscap SystemCapability.Communication.NetManager.Eap
         * @since 20
         */
        caCertAliases: string;
        /**
         * CA certificate path.
         *
         * @syscap SystemCapability.Communication.NetManager.Eap
         * @since 20
         */
        caPath: string;
        /**
         * Client certificate alias.
         *
         * @syscap SystemCapability.Communication.NetManager.Eap
         * @since 20
         */
        clientCertAliases: string;
        /**
         * CA certificate content.
         *
         * @syscap SystemCapability.Communication.NetManager.Eap
         * @since 20
         */
        certEntry: Uint8Array;
        /**
         * CA certificate password.
         *
         * @syscap SystemCapability.Communication.NetManager.Eap
         * @since 20
         */
        certPassword: string;
        /**
         * A string to match the alternate subject.
         *
         * @syscap SystemCapability.Communication.NetManager.Eap
         * @since 20
         */
        altSubjectMatch: string;
        /**
         * A string to match the domain suffix.
         *
         * @syscap SystemCapability.Communication.NetManager.Eap
         * @since 20
         */
        domainSuffixMatch: string;
        /**
         * Realm for the passpoint credential.
         *
         * @syscap SystemCapability.Communication.NetManager.Eap
         * @since 20
         */
        realm: string;
        /**
         * Public land mobile network (PLMN) of the passpoint credential provider.
         *
         * @syscap SystemCapability.Communication.NetManager.Eap
         * @since 20
         */
        plmn: string;
        /**
         * Sub-ID of the SIM card.
         *
         * @syscap SystemCapability.Communication.NetManager.Eap
         * @since 20
         */
        eapSubId: number;
    }
}
export default eap;

```
