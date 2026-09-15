# @ohos.net.networkSecurity.d.ts

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
 * @file Network Security
 * @kit NetworkKit
 */
/**
 * The **networkSecurity** module provides the network security verification capability. Specifically, it provides APIs
 * for applications to verify the certificates in use.
 *
 * @syscap SystemCapability.Communication.NetStack
 * @since 11
 */
declare namespace networkSecurity {
    /**
     * Enumerates certificate types.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @since 11
     */
    export enum CertType {
        /**
         * PEM certificate
         *
         * @syscap SystemCapability.Communication.NetStack
         * @since 11
         */
        CERT_TYPE_PEM = 0,
        /**
         * DER certificate.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @since 11
         */
        CERT_TYPE_DER = 1
    }
    /**
     * Defines the certificate data.
     *
     * @syscap SystemCapability.Communication.NetStack
     * @since 11
     */
    export interface CertBlob {
        /**
         * Certificate type.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @since 11
         */
        type: CertType;
        /**
         * Certificate data.
         *
         * @syscap SystemCapability.Communication.NetStack
         * @since 11
         */
        data: string | ArrayBuffer;
    }
    /**
     * Verifies the certificate passed by the application using the preset CA certificate and the CA certificate installed
     * by the user in the certificate management. This API uses a promise to return the result.
     *
     * @param { CertBlob } cert - Certificate to be verified.
     * @param { CertBlob } [caCert] - Custom CA certificate.
     * @returns { Promise<number> } Promise used to return the result. The value **0** indicates that the certificate
     *     verification is successful, and a non-0 value indicates that the verification has failed.
     * @throws { BusinessError } 401 - Parameter error.
     * @throws { BusinessError } 2305001 - Unspecified error.
     * @throws { BusinessError } 2305002 - Unable to get issuer certificate.
     * @throws { BusinessError } 2305003 - Unable to get certificate revocation list (CRL).
     * @throws { BusinessError } 2305004 - Unable to decrypt certificate signature.
     * @throws { BusinessError } 2305005 - Unable to decrypt CRL signature.
     * @throws { BusinessError } 2305006 - Unable to decode issuer public key.
     * @throws { BusinessError } 2305007 - Certificate signature failure.
     * @throws { BusinessError } 2305008 - CRL signature failure.
     * @throws { BusinessError } 2305009 - Certificate is not yet valid.
     * @throws { BusinessError } 2305010 - Certificate has expired.
     * @throws { BusinessError } 2305011 - CRL is not yet valid.
     * @throws { BusinessError } 2305012 - CRL has expired.
     * @throws { BusinessError } 2305023 - Certificate has been revoked.
     * @throws { BusinessError } 2305024 - Invalid certificate authority (CA).
     * @throws { BusinessError } 2305027 - Certificate is untrusted.
     * @throws { BusinessError } 2305018 - Self-signed certificate. [since 12]
     * @throws { BusinessError } 2305069 - Invalid certificate verification context. [since 12]
     * @syscap SystemCapability.Communication.NetStack
     * @since 11
     */
    export function certVerification(cert: CertBlob, caCert?: CertBlob): Promise<number>;
    /**
     * Verifies the certificate passed by the application using the preset CA certificate and the CA certificate installed
     * by the user in the certificate management. This API returns the result synchronously.
     *
     * @param { CertBlob } cert - Certificate to be verified.
     * @param { CertBlob } [caCert] - Custom CA certificate.
     * @returns { number } Certificate verification result. The value **0** indicates that the certificate verification is
     *     successful, and a non-0 value indicates that the verification has failed.
     * @throws { BusinessError } 401 - Parameter error.
     * @throws { BusinessError } 2305001 - Unspecified error.
     * @throws { BusinessError } 2305002 - Unable to get issuer certificate.
     * @throws { BusinessError } 2305003 - Unable to get certificate revocation list (CRL).
     * @throws { BusinessError } 2305004 - Unable to decrypt certificate signature.
     * @throws { BusinessError } 2305005 - Unable to decrypt CRL signature.
     * @throws { BusinessError } 2305006 - Unable to decode issuer public key.
     * @throws { BusinessError } 2305007 - Certificate signature failure.
     * @throws { BusinessError } 2305008 - CRL signature failure.
     * @throws { BusinessError } 2305009 - Certificate is not yet valid.
     * @throws { BusinessError } 2305010 - Certificate has expired.
     * @throws { BusinessError } 2305011 - CRL is not yet valid.
     * @throws { BusinessError } 2305012 - CRL has expired.
     * @throws { BusinessError } 2305023 - Certificate has been revoked.
     * @throws { BusinessError } 2305024 - Invalid certificate authority (CA).
     * @throws { BusinessError } 2305027 - Certificate is untrusted.
     * @throws { BusinessError } 2305018 - Self-signed certificate. [since 12]
     * @throws { BusinessError } 2305069 - Invalid certificate verification context. [since 12]
     * @syscap SystemCapability.Communication.NetStack
     * @since 11
     */
    export function certVerificationSync(cert: CertBlob, caCert?: CertBlob): number;
    /**
     * Verifies the server certificate chain and returns a sorted chain.
     *
     * @param { CertBlob[] } cert - Certificate chain to be verified.
     * @param { CertBlob } [caCert] - Incoming custom CA cert.
     * @param { string } [hostname] - Hostname to be verified.
     * @returns { Promise<CertBlob[]> } Returns a promise that resolves to the sorted certificate chain
     *     (ordered from leaf to root) if verification succeeds.
     * @throws { BusinessError } 2305001 - Unspecified error.
     * @throws { BusinessError } 2305002 - Unable to get issuer certificate.
     * @throws { BusinessError } 2305004 - Unable to decrypt certificate signature.
     * @throws { BusinessError } 2305006 - Unable to decode issuer public key.
     * @throws { BusinessError } 2305007 - Certificate signature failure.
     * @throws { BusinessError } 2305009 - Certificate is not yet valid.
     * @throws { BusinessError } 2305010 - Certificate has expired.
     * @throws { BusinessError } 2305018 - Self-signed certificate.
     * @throws { BusinessError } 2305024 - Invalid certificate authority (CA).
     * @throws { BusinessError } 2305027 - Certificate is untrusted.
     * @throws { BusinessError } 2305062 - Invalid hostname.
     * @throws { BusinessError } 2305069 - Invalid certificate verification context.
     * @syscap SystemCapability.Communication.NetStack
     * @stagemodelonly
     * @since 26.0.0
     */
    export function verifyCertChain(cert: CertBlob[], caCert?: CertBlob, hostname?: string): Promise<CertBlob[]>;
    /**
     * Checks whether plaintext HTTP access is allowed from the preset **network_config.json** file of the application. By
     * default, plaintext HTTP access is allowed.
     *
     * @permission ohos.permission.INTERNET
     * @returns { boolean } Boolean value indicating whether plaintext HTTP is allowed. The value **true** indicates that
     *     plaintext HTTP is allowed, and the value **false** indicates the opposite. The default value is **true**.
     * @throws { BusinessError } 201 - Permission denied.
     * @syscap SystemCapability.Communication.NetStack
     * @since 18
     */
    export function isCleartextPermitted(): boolean;
    /**
     * Checks whether host name–based plaintext HTTP access is allowed from the preset **network_config.json** file of the
     * application. By default, plaintext HTTP access is allowed.
     *
     * @permission ohos.permission.INTERNET
     * @param { string } hostName - Host name.
     * @returns { boolean } Boolean value indicating whether host name–based plaintext HTTP is allowed. The value **true**
     *     indicates that plaintext HTTP is allowed, and the value **false** indicates the opposite. The default value is
     *     **true**.
     * @throws { BusinessError } 201 - Permission denied.
     * @syscap SystemCapability.Communication.NetStack
     * @since 18
     */
    export function isCleartextPermittedByHostName(hostName: string): boolean;
}
export default networkSecurity;

```
