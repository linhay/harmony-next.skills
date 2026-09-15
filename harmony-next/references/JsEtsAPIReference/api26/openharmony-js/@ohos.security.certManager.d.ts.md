# @ohos.security.certManager.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2023-2024 Huawei Device Co., Ltd.
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
 * @kit DeviceCertificateKit
 */
import type { AsyncCallback } from './@ohos.base';
/**
 * The **certManager** module provides system-level certificate management capabilities to implement management and
 * secure use of certificates throughout their lifecycle (installation, storage, use, and destruction).
 *
 * It can be used to verify the HTTPS certificate chain of the application server , and log in to the website or
 * application server using two-way HTTPS.
 *
 * @syscap SystemCapability.Security.CertificateManager
 * @since 11
 */
declare namespace certificateManager {
    /**
     * Enumerates the error codes used in the certificate management APIs.
     *
     * @syscap SystemCapability.Security.CertificateManager
     * @since 11
     */
    export enum CMErrorCode {
        /**
         * The application does not have the permission to call the API.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        CM_ERROR_NO_PERMISSION = 201,
        /**
         * Invalid input parameter is found.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        CM_ERROR_INVALID_PARAMS = 401,
        /**
         * An internal error occurs when the interface is called.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        CM_ERROR_GENERIC = 17500001,
        /**
         * The certificate or credential does not exist.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        CM_ERROR_NO_FOUND = 17500002,
        /**
         * The certificate or credential is in invalid format.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        CM_ERROR_INCORRECT_FORMAT = 17500003,
        /**
         * The number of certificates or credentials has reached the limit.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 12
         */
        CM_ERROR_MAX_CERT_COUNT_REACHED = 17500004,
        /**
         * The application has not obtained user authorization.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 12
         */
        CM_ERROR_NO_AUTHORIZATION = 17500005,
        /**
         * The device enters the advanced security mode. In this mode, CA certificate installation is restricted.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 18
         */
        CM_ERROR_DEVICE_ENTER_ADVSECMODE = 17500007,
        /**
         * The device does not support the specified certificate storage path.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 20
         */
        CM_ERROR_STORE_PATH_NOT_SUPPORTED = 17500009,
        /**
         * The USB Key service fails to be accessed.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 22
         */
        CM_ERROR_ACCESS_UKEY_SERVICE_FAILED = 17500010,
        /**
         * The input parameter validation fails.
         *
         * For example, the parameter format is incorrect or the parameter range is invalid.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 22
         */
        CM_ERROR_PARAMETER_VALIDATION_FAILED = 17500011
    }
    /**
     * Represents detailed information about a certificate.
     *
     * @syscap SystemCapability.Security.CertificateManager
     * @since 11
     */
    export interface CertInfo {
        /**
         * Unique identifier of a certificate. The value contains up to 256 bytes.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        uri: string;
        /**
         * Alias of a certificate. The value contains up to 128 bytes.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        certAlias: string;
        /**
         * Certificate state. The value **true** indicates that the certificate is enabled, and **false** means the
         * opposite.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        state: boolean;
        /**
         * Name of the certificate issuer. The value contains up to 256 bytes.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        issuerName: string;
        /**
         * Name of the certificate subject. The value contains up to 1024 bytes.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        subjectName: string;
        /**
         * Serial number of a certificate. The value contains up to 64 bytes. The value is a hexadecimal string, for example
         * , **62C2CB4DE8405E96**.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        serial: string;
        /**
         * Start date of a certificate. The value contains up to 32 bytes.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        notBefore: string;
        /**
         * Expiry date of a certificate. The value contains up to 32 bytes.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        notAfter: string;
        /**
         * Fingerprint of a certificate. The value contains up to 128 bytes.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        fingerprintSha256: string;
        /**
         * Binary data of a certificate. The value contains up to 8196 bytes.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        cert: Uint8Array;
    }
    /**
     * Represents brief information about a certificate.
     *
     * @syscap SystemCapability.Security.CertificateManager
     * @since 11
     */
    export interface CertAbstract {
        /**
         * Unique identifier of a certificate. The value contains up to 256 bytes.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        uri: string;
        /**
         * Alias of a certificate. The value contains up to 128 bytes.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        certAlias: string;
        /**
         * Certificate state. The value **true** indicates that the certificate is enabled, and **false** means the
         * opposite.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        state: boolean;
        /**
         * Name of the certificate subject. The value contains up to 1024 bytes.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        subjectName: string;
    }
    /**
     * Represents detailed information about a credential.
     *
     * @syscap SystemCapability.Security.CertificateManager
     * @since 11
     */
    export interface Credential {
        /**
         * Type of a credential. The value contains up to 8 bytes.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        type: string;
        /**
         * Alias of a credential. The value contains up to 128 bytes.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        alias: string;
        /**
         * Unique identifier of a credential. The value contains up to 256 bytes.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        keyUri: string;
        /**
         * Number of certificates contained in the credential.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        certNum: number;
        /**
         * Number of keys contained in the credential.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        keyNum: number;
        /**
         * Binary data of a credential. The value contains up to 20480 bytes.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        credentialData: Uint8Array;
        /**
         * Credential usage. The default value is **CertificatePurpose.PURPOSE_DEFAULT**.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 22
         */
        certPurpose?: CertificatePurpose;
    }
    /**
     * Represents brief information about a credential.
     *
     * @syscap SystemCapability.Security.CertificateManager
     * @since 11
     */
    export interface CredentialAbstract {
        /**
         * Type of a credential. The value contains up to 8 bytes.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        type: string;
        /**
         * Alias of a credential. The value contains up to 128 bytes.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        alias: string;
        /**
         * Unique identifier of a credential. The value contains up to 256 bytes.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        keyUri: string;
    }
    /**
     * Represents the result returned.
     *
     * @syscap SystemCapability.Security.CertificateManager
     * @since 11
     */
    export interface CMResult {
        /**
         * Brief certificate information.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        certList?: Array<CertAbstract>;
        /**
         * Detailed certificate information.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        certInfo?: CertInfo;
        /**
         * Brief credential information.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        credentialList?: Array<CredentialAbstract>;
        /**
         * Detailed credential information.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        credential?: Credential;
        /**
         * List of authorized applications.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        appUidList?: Array<string>;
        /**
         * Unique identifier of a certificate or credential. The value contains up to 256 bytes.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        uri?: string;
        /**
         * Signature generated.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        outData?: Uint8Array;
        /**
         * Represents detailed information about a credential.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 22
         */
        credentialDetailList?: Array<Credential>;
        /**
         * Certificate URI list.
         * **Since**: 26.0.0
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @stagemodelonly
         * @since 26.0.0
         */
        uriList?: Array<string>;
    }
    /**
     * Enumerates the purposes of using the key.
     *
     * @syscap SystemCapability.Security.CertificateManager
     * @since 11
     */
    export enum CmKeyPurpose {
        /**
         * Signs data.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        CM_KEY_PURPOSE_SIGN = 4,
        /**
         * Verifies a signature.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        CM_KEY_PURPOSE_VERIFY = 8
    }
    /**
     * Enumerates the digest algorithms that can be used for signing and signature verification.
     *
     * @syscap SystemCapability.Security.CertificateManager
     * @since 11
     */
    export enum CmKeyDigest {
        /**
         * When this option is selected, it indicates that the application performs a digest calculation on the data to be
         * signed or verified.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        CM_DIGEST_NONE = 0,
        /**
         * MD5.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        CM_DIGEST_MD5 = 1,
        /**
         * SHA-1.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        CM_DIGEST_SHA1 = 2,
        /**
         * SHA-224.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        CM_DIGEST_SHA224 = 3,
        /**
         * SHA-256.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        CM_DIGEST_SHA256 = 4,
        /**
         * SHA-384.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        CM_DIGEST_SHA384 = 5,
        /**
         * SHA-512.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        CM_DIGEST_SHA512 = 6,
        /**
         * SM3.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 18
         */
        CM_DIGEST_SM3 = 7
    }
    /**
     * Enumerates the padding modes that can be used for signing and signature verification.
     *
     * @syscap SystemCapability.Security.CertificateManager
     * @since 11
     */
    export enum CmKeyPadding {
        /**
         * No padding.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        CM_PADDING_NONE = 0,
        /**
         * PSS.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        CM_PADDING_PSS = 1,
        /**
         * PKCS1-V1_5.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        CM_PADDING_PKCS1_V1_5 = 2
    }
    /**
     * Represents a set of parameters used for signing or signature verification, including the key usage purpose, padding
     * mode, and digest algorithm.
     *
     * @syscap SystemCapability.Security.CertificateManager
     * @since 11
     */
    export interface CMSignatureSpec {
        /**
         * Purpose of using the key.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        purpose: CmKeyPurpose;
        /**
         * Enumeration representing the padding mode.
         * Default value: CM_PADDING_PSS: indicates that the PSS filling mode is used.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        padding?: CmKeyPadding;
        /**
         * Digest algorithm.
         * Default value: CM_DIGEST_SHA256: indicates that the SHA256 digest algorithm is used.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        digest?: CmKeyDigest;
    }
    /**
     * Represents the handle to a signing or signature verification operation.
     *
     * @syscap SystemCapability.Security.CertificateManager
     * @since 11
     */
    export interface CMHandle {
        /**
         * Handle of the initialization for signing and signature verification. The value contains up to 8 bytes.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 11
         */
        handle: Uint8Array;
    }
    /**
     * Installs a private credential. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.ACCESS_CERT_MANAGER
     * @param { Uint8Array } keystore - Keystore file with a key pair and certificate. The value contains up to 20480
     *     bytes.
     * @param { string } keystorePwd - Password of the keystore file. The password cannot exceed 32 bytes.
     * @param { string } certAlias - Credential alias. Currently, the alias can contain only digits, letters, and
     *     underscores (_) and should not exceed 32 bytes.
     * @param { AsyncCallback<CMResult> } callback - Callback used to return the result. If the operation is successful,
     *     **err** is **null** and **data** is **uri** in the [CMResult]{@link certificateManager.CMResult} object.
     *     Otherwise, **err** is an error object.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17500001 - Internal error. Possible causes: 1. IPC communication failed;
     *     <br>2. Memory operation error; 3. File operation error. Please try again.
     * @throws { BusinessError } 17500003 - The keystore is in an invalid format or the keystore password is incorrect.
     * @throws { BusinessError } 17500004 - The number of certificates or credentials reaches the maximum allowed.
     *     [since 12]
     * @syscap SystemCapability.Security.CertificateManager
     * @since 11
     */
    function installPrivateCertificate(keystore: Uint8Array, keystorePwd: string, certAlias: string, callback: AsyncCallback<CMResult>): void;
    /**
     * Installs a private credential. This API uses a promise to return the result.
     *
     * @permission ohos.permission.ACCESS_CERT_MANAGER
     * @param { Uint8Array } keystore - Keystore file with a key pair and certificate. The value contains up to 20480
     *     bytes.
     * @param { string } keystorePwd - Password of the keystore file. The password cannot exceed 32 bytes.
     * @param { string } certAlias - Credential alias. Currently, the alias can contain only digits, letters, and
     *     underscores (_) and should not exceed 32 bytes.
     * @returns { Promise<CMResult> } Promise used to return the operation result, that is, **uri** in the
     *     [CMResult]{@link certificateManager.CMResult} object.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17500001 - Internal error. Possible causes: 1. IPC communication failed;
     *     <br>2. Memory operation error; 3. File operation error. Please try again.
     * @throws { BusinessError } 17500003 - The keystore is in an invalid format or the keystore password is incorrect.
     * @throws { BusinessError } 17500004 - The number of certificates or credentials reaches the maximum allowed.
     *     [since 12]
     * @syscap SystemCapability.Security.CertificateManager
     * @since 11
     */
    function installPrivateCertificate(keystore: Uint8Array, keystorePwd: string, certAlias: string): Promise<CMResult>;
    /**
     * Uninstalls a private credential. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.ACCESS_CERT_MANAGER
     * @param { string } keyUri - Unique identifier of the credential to be uninstalled. The value contains up to 256
     *     bytes.
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
     *     **err** is **null**. Otherwise, **err** is an error object.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17500001 - Internal error. Possible causes: 1. IPC communication failed;
     *     <br>2. Memory operation error; 3. File operation error. Please try again.
     * @throws { BusinessError } 17500002 - The certificate does not exist.
     * @syscap SystemCapability.Security.CertificateManager
     * @since 11
     */
    function uninstallPrivateCertificate(keyUri: string, callback: AsyncCallback<void>): void;
    /**
     * Uninstalls a private credential. This API uses a promise to return the result.
     *
     * @permission ohos.permission.ACCESS_CERT_MANAGER
     * @param { string } keyUri - Unique identifier of the credential to be uninstalled. The value contains up to 256
     *     bytes.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17500001 - Internal error. Possible causes: 1. IPC communication failed;
     *     <br>2. Memory operation error; 3. File operation error. Please try again.
     * @throws { BusinessError } 17500002 - The certificate does not exist.
     * @syscap SystemCapability.Security.CertificateManager
     * @since 11
     */
    function uninstallPrivateCertificate(keyUri: string): Promise<void>;
    /**
     * Obtains detailed information about a private credential. This API uses an asynchronous callback to return the
     * result.
     *
     * @permission ohos.permission.ACCESS_CERT_MANAGER
     * @param { string } keyUri - Unique identifier of the credential to be obtained. The value contains up to 256 bytes.
     * @param { AsyncCallback<CMResult> } callback - Callback used to return the result. If the operation is successful,
     *     **err** is **null** and **data** is **credential** in the [CMResult]{@link certificateManager.CMResult} object.
     *     Otherwise, **err** is an error object.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17500001 - Internal error. Possible causes: 1. IPC communication failed;
     *     <br>2. Memory operation error; 3. File operation error. Please try again.
     * @throws { BusinessError } 17500002 - The certificate does not exist. Possible causes:
     *     1. The certificate URI is incorrect;
     *     2. The certificate has been uninstalled. Please check the certificate URI.
     * @syscap SystemCapability.Security.CertificateManager
     * @since 11
     */
    function getPrivateCertificate(keyUri: string, callback: AsyncCallback<CMResult>): void;
    /**
     * Obtains detailed information about a private credential. This API uses a promise to return the result.
     *
     * @permission ohos.permission.ACCESS_CERT_MANAGER
     * @param { string } keyUri - Unique identifier of the credential to be obtained. The value contains up to 256 bytes.
     * @returns { Promise<CMResult> } Promise used to return the private credential details obtained, that is,
     *     **credential** in the [CMResult]{@link certificateManager.CMResult} object.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17500001 - Internal error. Possible causes: 1. IPC communication failed;
     *     <br>2. Memory operation error; 3. File operation error. Please try again.
     * @throws { BusinessError } 17500002 - The certificate does not exist.
     * @syscap SystemCapability.Security.CertificateManager
     * @since 11
     */
    function getPrivateCertificate(keyUri: string): Promise<CMResult>;
    /**
     * Indicates the initialization of signature and signature verification using credentials. This is the first step in
     * the signature verification process. Later, the update and finish interfaces need to be invoked in sequence to
     * complete the operations. Use Callback to return the result asynchronously.
     *
     * @permission ohos.permission.ACCESS_CERT_MANAGER
     * @param { string } authUri - Unique identifier of the credential to be used. The value contains up to 256 bytes.
     * @param { CMSignatureSpec } spec - Parameters for the signing or signature verification operation.
     * @param { AsyncCallback<CMHandle> } callback - Callback used to return the result. If the operation is successful,
     *     **err** is **null** and **data** is the obtained **CMHandle**. Otherwise, **err** is an error object.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17500001 - Internal error. Possible causes: 1. IPC communication failed;
     *     <br>2. Memory operation error; 3. File operation error. Please try again.
     * @throws { BusinessError } 17500002 - The certificate does not exist.
     * @throws { BusinessError } 17500005 - The application is not authorized by the user.
     *     Please call [openAuthorizeDialog]{@link certificateManagerDialog.openAuthorizeDialog}
     *     method to request user authorization for the certificate or credential. [since 12]
     * @syscap SystemCapability.Security.CertificateManager
     * @since 11
     */
    function init(authUri: string, spec: CMSignatureSpec, callback: AsyncCallback<CMHandle>): void;
    /**
     * Initializes the signing or signature verification operation using the specified credential. This API uses a promise
     * to return the result.
     *
     * @permission ohos.permission.ACCESS_CERT_MANAGER
     * @param { string } authUri - Unique identifier of the credential to be used. The value contains up to 256 bytes.
     * @param { CMSignatureSpec } spec - Parameters for the signing or signature verification operation.
     * @returns { Promise<CMHandle> } Promise used to return the operation result, that is, the **CMHandle** object.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17500001 - Internal error. Possible causes: 1. IPC communication failed;
     *     <br>2. Memory operation error; 3. File operation error. Please try again.
     * @throws { BusinessError } 17500002 - The certificate does not exist.
     * @throws { BusinessError } 17500005 - The application is not authorized by the user. [since 12]
     * @syscap SystemCapability.Security.CertificateManager
     * @since 11
     */
    function init(authUri: string, spec: CMSignatureSpec): Promise<CMHandle>;
    /**
     * Updates the data for the signing or signature verification operation.  It needs to be invoked after the init
     * operation to transfer the data to be signed and verified. This API uses an asynchronous callback to
     * return the result.
     *
     * @permission ohos.permission.ACCESS_CERT_MANAGER
     * @param { Uint8Array } handle - Handle of initialization which needs to be obtained by calling the init method.
     * @param { Uint8Array } data - Data to be signed or verified.
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
     *     **err** is **null**. Otherwise, **err** is an error object.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17500001 - Internal error. Possible causes: 1. IPC communication failed;
     *     <br>2. Memory operation error; 3. File operation error. Please try again.
     * @syscap SystemCapability.Security.CertificateManager
     * @since 11
     */
    function update(handle: Uint8Array, data: Uint8Array, callback: AsyncCallback<void>): void;
    /**
     * Updates the data for the signing or signature verification operation. This API uses a promise to return the result.
     *
     * @permission ohos.permission.ACCESS_CERT_MANAGER
     * @param { Uint8Array } handle - Handle of initialization, which needs to be obtained by calling the init method
     * @param { Uint8Array } data - Data to be signed or verified.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17500001 - Internal error. Possible causes: 1. IPC communication failed;
     *     <br>2. Memory operation error; 3. File operation error. Please try again.
     * @syscap SystemCapability.Security.CertificateManager
     * @since 11
     */
    function update(handle: Uint8Array, data: Uint8Array): Promise<void>;
    /**
     * Finishes the signing operation. This is the last step in the signature process. The init and update interfaces need
     *  to be invoked first. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.ACCESS_CERT_MANAGER
     * @param { Uint8Array } handle - Handle of initialization. You need to invoke the init method to obtain the handle.
     * @param { AsyncCallback<CMResult> } callback - Callback used to return the result. If the operation is successful,
     *     **err** is **null** and **data** is the signature, that is, **outData** of the
     *     [CMResult]{@link certificateManager.CMResult} object. Otherwise, **err** is an error object.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17500001 - Internal error. Possible causes: 1. IPC communication failed;
     *     <br>2. Memory operation error; 3. File operation error. Please try again.
     * @syscap SystemCapability.Security.CertificateManager
     * @since 11
     */
    function finish(handle: Uint8Array, callback: AsyncCallback<CMResult>): void;
    /**
     * Finishes the signature verification operation. This is the last step in the signature verification process. The
     * init and update interfaces need to be invoked first. This API uses an asynchronous callback to return the result.
     *
     * @permission ohos.permission.ACCESS_CERT_MANAGER
     * @param { Uint8Array } handle - Handle of initialization. You need to invoke the init method to obtain the handle.
     * @param { Uint8Array } signature - Data to sign or verify.
     * @param { AsyncCallback<CMResult> } callback - Callback used to return the result. If the operation is successful,
     *     **err** is **null**. Otherwise, **err** is an error object.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17500001 - Internal error. Possible causes: 1. IPC communication failed;
     *     <br>2. Memory operation error; 3. File operation error. Please try again.
     * @syscap SystemCapability.Security.CertificateManager
     * @since 11
     */
    function finish(handle: Uint8Array, signature: Uint8Array, callback: AsyncCallback<CMResult>): void;
    /**
     * Finishes the signing or signature verification operation. This API uses a promise to return the result.
     *
     * @permission ohos.permission.ACCESS_CERT_MANAGER
     * @param { Uint8Array } handle - Handle of initialization. You need to invoke the init method to obtain the handle.
     * @param { Uint8Array } signature - Signature data used for signature verification.  This parameter does not need to
     *     be specified for signature operation.
     * @returns { Promise<CMResult> } Promise used to return the signature of a signing operation, that is, **outData** in
     *     the [CMResult]{@link certificateManager.CMResult} object. For a signature verification operation, the promise
     *     returns no value.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17500001 - Internal error. Possible causes: 1. IPC communication failed;
     *     <br>2. Memory operation error; 3. File operation error. Please try again.
     * @syscap SystemCapability.Security.CertificateManager
     * @since 11
     */
    function finish(handle: Uint8Array, signature?: Uint8Array): Promise<CMResult>;
    /**
     * Aborts the signing or signature verification operation. This method is mutually exclusive with the finish method.
     * Only one method can be invoked in a signature verification process. This API uses an asynchronous callback to
     * return the result.
     *
     * @permission ohos.permission.ACCESS_CERT_MANAGER
     * @param { Uint8Array } handle - Handle of initialization. The value contains up to 8 bytes.
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
     *     **err** is **null**. Otherwise, **err** is an error object.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17500001 - Internal error. Possible causes: 1. IPC communication failed;
     *     <br>2. Memory operation error; 3. File operation error. Please try again.
     * @syscap SystemCapability.Security.CertificateManager
     * @since 11
     */
    function abort(handle: Uint8Array, callback: AsyncCallback<void>): void;
    /**
     * Aborts the signing or signature verification operation. This method is mutually exclusive with the finish method.
     * Only one method can be invoked in a signature verification process. This API uses a promise to return the result.
     *
     * @permission ohos.permission.ACCESS_CERT_MANAGER
     * @param { Uint8Array } handle - Handle of initialization. The value contains up to 8 bytes.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17500001 - Internal error. Possible causes: 1. IPC communication failed;
     *     <br>2. Memory operation error; 3. File operation error. Please try again.
     * @syscap SystemCapability.Security.CertificateManager
     * @since 11
     */
    function abort(handle: Uint8Array): Promise<void>;
    /**
     * Obtains detailed information about a public credential. This API uses a promise to return the result.
     *
     * @permission ohos.permission.ACCESS_CERT_MANAGER
     * @param { string } keyUri - Unique identifier of a user's public credential. The value contains up to 256 bytes.
     * @returns { Promise<CMResult> } Promise used to return the detailed information about the user's public credential
     *     obtained, that is, **credential** in the [CMResult]{@link certificateManager.CMResult} object.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17500001 - Internal error. Possible causes: 1. IPC communication failed;
     *     <br>2. Memory operation error; 3. File operation error. Please try again.
     * @throws { BusinessError } 17500002 - The certificate does not exist.
     * @throws { BusinessError } 17500005 - The application is not authorized by the user.
     * @syscap SystemCapability.Security.CertificateManager
     * @since 12
     */
    function getPublicCertificate(keyUri: string): Promise<CMResult>;
    /**
     * Checks whether this application is authorized by the specified user credential. This API uses a promise to return
     * the result.
     *
     * @permission ohos.permission.ACCESS_CERT_MANAGER
     * @param { string } keyUri - Unique identifier of the credential authorized by the user to the application. The value
     *     contains up to 256 bytes.
     * @returns { Promise<boolean> } Promise used to return whether the application is authorized. The value **true**
     *     means authorized; the value **false** means the opposite.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17500001 - Internal error. Possible causes: 1. IPC communication failed;
     *     <br>2. Memory operation error; 3. File operation error. Please try again.
     * @syscap SystemCapability.Security.CertificateManager
     * @since 12
     */
    function isAuthorizedApp(keyUri: string): Promise<boolean>;
    /**
     * Obtains all user trusted root CA certificates of the device. This API uses a promise to return the result.
     *
     * @permission ohos.permission.ACCESS_CERT_MANAGER
     * @returns { Promise<CMResult> } Promise used to return the operation result, that is, **certList** in the
     *     [CMResult]{@link certificateManager.CMResult} object.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 17500001 - Internal error. Possible causes: 1. IPC communication failed;
     *     <br>2. Memory operation error; 3. File operation error. Please try again.
     * @syscap SystemCapability.Security.CertificateManager
     * @since 12
     */
    function getAllUserTrustedCertificates(): Promise<CMResult>;
    /**
     * Obtains the detailed information about a user root CA certificate. This API uses a promise to return the result.
     *
     * @permission ohos.permission.ACCESS_CERT_MANAGER
     * @param { string } certUri - Unique identifier of a user's root CA certificate. The value contains up to 256 bytes.
     * @returns { Promise<CMResult> } Promise used to return the operation result, that is, **certInfo** in the
     *     [CMResult]{@link certificateManager.CMResult} object.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17500001 - Internal error. Possible causes: 1. IPC communication failed;
     *     <br>2. Memory operation error; 3. File operation error. Please try again.
     * @throws { BusinessError } 17500002 - The certificate does not exist.
     * @syscap SystemCapability.Security.CertificateManager
     * @since 12
     */
    function getUserTrustedCertificate(certUri: string): Promise<CMResult>;
    /**
     * Obtains the credentials for installing the application. This API uses a promise to return the result
     * asynchronously.
     *
     * @permission ohos.permission.ACCESS_CERT_MANAGER
     * @returns { Promise<CMResult> } Promise used to return credentials obtained, which is **credentialList** in
     *     [CMResult]{@link certificateManager.CMResult}.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 17500001 - Internal error. Possible causes: 1. IPC communication failed;
     *     <br>2. Memory operation error; 3. File operation error. Please try again.
     * @syscap SystemCapability.Security.CertificateManager
     * @since 13
     */
    function getPrivateCertificates(): Promise<CMResult>;
    /**
     * Obtains the certificate storage path.
     *
     * @param { CertStoreProperty } property - Storage information about the target certificate.
     * @returns { string } Certificate storage path.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left
     *     unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed. For example, CertStoreProperty.certType
     *     is set to CA_CERT_USER, but CertStoreProperty.certScope is not specified.
     * @throws { BusinessError } 17500001 - Internal error. Possible causes: 1. IPC communication failed;
     *     <br>2. Memory operation error; 3. File operation error. Please try again.
     * @throws { BusinessError } 17500009 - The device does not support the specified certificate storage path,
     *     For example, the device outside China does not support the certificate that uses SM algorithm. [since 20]
     * @syscap SystemCapability.Security.CertificateManager
     * @since 18
     */
    function getCertificateStorePath(property: CertStoreProperty): string;
    /**
     * Installs a user CA certificate.
     *
     * @permission ohos.permission.ACCESS_ENTERPRISE_USER_TRUSTED_CERT or ohos.permission.ACCESS_USER_TRUSTED_CERT
     * @param { Uint8Array } cert - CA certificate data. The value contains up to 8196 bytes.
     * @param { CertScope } certScope - Scope of the CA certificate.
     * @returns { CMResult } CA certificate installation result. The **uri** property in **CMResult** is returned if the
     *     certificate is installed successfully.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17500001 - Internal error. Possible causes: 1. IPC communication failed;
     *     <br>2. Memory operation error; 3. File operation error. Please try again.
     * @throws { BusinessError } 17500003 - Indicates that the certificate is in an invalid format.
     * @throws { BusinessError } 17500004 - Indicates that the number of certificates reaches the maximum allowed.
     * @throws { BusinessError } 17500007 - Indicates that the device enters advanced security mode. In this mode, the
     *     user CA certificate cannot be installed.
     * @syscap SystemCapability.Security.CertificateManager
     * @since 18
     */
    function installUserTrustedCertificateSync(cert: Uint8Array, certScope: CertScope): CMResult;
    /**
     * Enumerates the credential storage levels.
     *
     * @syscap SystemCapability.Security.CertificateManager
     * @since 18
     */
    export enum AuthStorageLevel {
        /**
         * The credential can be accessed after the device is started.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 18
         */
        EL1 = 1,
        /**
         * The credential can be accessed after the device is unlocked for the first time.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 18
         */
        EL2 = 2,
        /**
         * The credential can be accessed after the device is unlocked.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 18
         */
        EL4 = 4
    }
    /**
     * Represents the storage information about a certificate, including the certificate type and location.
     *
     * @syscap SystemCapability.Security.CertificateManager
     * @since 18
     */
    export interface CertStoreProperty {
        /**
         * Type of the certificate.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 18
         */
        certType: CertType;
        /**
         * Scope of the certificate. This parameter is mandatory when **certType** is **CA_CERT_USER**.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 18
         */
        certScope?: CertScope;
        /**
         * Certificate algorithm. This parameter is valid only when **certType** is set to **CA_CERT_SYSTEM**. The default
         * value is **INTERNATIONAL**.
         * Devices outside China do not support the SM algorithm.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 20
         */
        certAlg?: CertAlgorithm;
    }
    /**
     * Enumerates the certificate types.
     *
     * @syscap SystemCapability.Security.CertificateManager
     * @since 18
     */
    export enum CertType {
        /**
         * System CA certificate.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 18
         */
        CA_CERT_SYSTEM = 0,
        /**
         * User CA certificate.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 18
         */
        CA_CERT_USER = 1
    }
    /**
     * Installs a private credential and specifies its storage level. This API uses a promise to return the result.
     *
     * @permission ohos.permission.ACCESS_CERT_MANAGER
     * @param { Uint8Array } keystore - Keystore file with a key pair and certificate. The value contains up to 20480
     *     bytes.
     * @param { string } keystorePwd - Password of the keystore file.<br>The value contains up to 32 bytes.
     * @param { string } certAlias - Alias of the credential entered by the user. Only digits, letters, and underscores (_
     *     ) are supported.<br>The value should contain up to 32 bytes.
     * @param { AuthStorageLevel } level - Credential storage level.
     * @returns { Promise<CMResult> } Promise used to return the operation result, that is, **uri** in the
     *     [CMResult]{@link certificateManager.CMResult} object.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17500001 - Internal error. Possible causes: 1. IPC communication failed;
     *     <br>2. Memory operation error; 3. File operation error. Please try again.
     * @throws { BusinessError } 17500003 - The keystore is in an invalid format or the keystore password is incorrect.
     * @throws { BusinessError } 17500004 - The number of certificates or credentials reaches the maximum allowed.
     * @syscap SystemCapability.Security.CertificateManager
     * @since 18
     */
    function installPrivateCertificate(keystore: Uint8Array, keystorePwd: string, certAlias: string, level: AuthStorageLevel): Promise<CMResult>;
    /**
     * Obtains the user root CA certificates based on the certificate scope. This API uses a promise to return the result.
     *
     * @permission ohos.permission.ACCESS_CERT_MANAGER
     * @param { CertScope } scope - Scope of the certificates to obtain.
     * @returns { Promise<CMResult> } Promise used to return the operation result, that is, **certList** in the
     *     [CMResult]{@link certificateManager.CMResult} object.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17500001 - Internal error. Possible causes: 1. IPC communication failed;
     *     <br>2. Memory operation error; 3. File operation error. Please try again.
     * @syscap SystemCapability.Security.CertificateManager
     * @since 18
     */
    function getAllUserTrustedCertificates(scope: CertScope): Promise<CMResult>;
    /**
     * Enumerates the certificate scopes.
     *
     * @syscap SystemCapability.Security.CertificateManager
     * @since 18
     */
    export enum CertScope {
        /**
         * The certificate is accessible only to the current user.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 18
         */
        CURRENT_USER = 1,
        /**
         * The certificate is accessible to all users.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 18
         */
        GLOBAL_USER = 2
    }
    /**
     * Uninstalls a user CA certificate.
     *
     * @permission ohos.permission.ACCESS_ENTERPRISE_USER_TRUSTED_CERT or ohos.permission.ACCESS_USER_TRUSTED_CERT
     * @param { string } certUri - Unique identifier of the certificate to be uninstalled. The value contains a maximum of
     *     256 bytes.
     * @throws { BusinessError } 201 - Permission verification failed. The application does not have the permission
     *     required to call the API.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
     * @throws { BusinessError } 17500001 - Internal error. Possible causes: 1. IPC communication failed;
     *     <br>2. Memory operation error; 3. File operation error. Please try again.
     * @throws { BusinessError } 17500002 - Indicates that the certificate does not exist.
     * @syscap SystemCapability.Security.CertificateManager
     * @since 18
     */
    function uninstallUserTrustedCertificateSync(certUri: string): void;
    /**
     * Enumerates the certificate algorithms.
     *
     * @syscap SystemCapability.Security.CertificateManager
     * @since 20
     */
    export enum CertAlgorithm {
        /**
         * International cryptographic algorithm, such as RSA and NIST ECC.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 20
         */
        INTERNATIONAL = 1,
        /**
         * Indicates the commercial cryptographic algorithm, such as SM2 and SM4.
         * Devices outside China do not support certificates using this algorithm.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 20
         */
        SM = 2
    }
    /**
     * Enumerates the usage of a credential.
     *
     * @syscap SystemCapability.Security.CertificateManager
     * @since 22
     */
    export enum CertificatePurpose {
        /**
         * Default usage, which is used for credential signing.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 22
         */
        PURPOSE_DEFAULT = 0,
        /**
         * Query of all credentials.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 22
         */
        PURPOSE_ALL = 1,
        /**
         * Credential signing.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 22
         */
        PURPOSE_SIGN = 2,
        /**
         * Credential encryption.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 22
         */
        PURPOSE_ENCRYPT = 3
    }
    /**
     * Obtains the details of a USB Key credential. This API uses a promise to return the result.
     *
     * @permission ohos.permission.ACCESS_CERT_MANAGER
     * @param { string } keyUri - Unique identifier of a USB Key credential. The value contains up to 256 bytes
     * @param { UkeyInfo } ukeyInfo - Attributes of a USB Key credential
     * @returns { Promise<CMResult> } Promise used to return the obtained USB Key credential details.
     *     The return value is the credentialDetailList attribute of the
     *     [CMResult]{@link certificateManager.CMResult} object.
     * @throws { BusinessError } 201 - Permission verification failed.
     * @throws { BusinessError } 801 - Capability not supported.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 17500001 - Internal error. Possible causes: 1. IPC communication failed;
     *     <br>2. Memory operation error; 3. File operation error. Please try again.
     * @throws { BusinessError } 17500002 - Indicates that the certificate does not exist.
     * @throws { BusinessError } 17500010 - Indicates that access USB Key service failed.
     * @throws { BusinessError } 17500011 - Indicates that the input parameters validation failed.
     *     For example, the parameter format is incorrect or the value range is invalid.
     * @syscap SystemCapability.Security.CertificateManager
     * @since 22
     */
    function getUkeyCertificate(keyUri: string, ukeyInfo: UkeyInfo): Promise<CMResult>;
    /**
     * Provides USB Key certificate credential attribute information.
     *
     * @syscap SystemCapability.Security.CertificateManager
     * @since 22
     */
    export interface UkeyInfo {
        /**
         * Credential usage.
         * Default value: PURPOSE_DEFAULT.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @since 22
         */
        certPurpose?: CertificatePurpose;
    }
    /**
     * Represents the certificate file format.
     *
     * @syscap SystemCapability.Security.CertificateManager
     * @stagemodelonly
     * @since 26.0.0
     */
    export enum CertFileFormat {
        /**
         * The certificate file format is PEM or DER.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @stagemodelonly
         * @since 26.0.0
         */
        PEM_DER = 0,
        /**
         * The certificate file format is P7B.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @stagemodelonly
         * @since 26.0.0
         */
        P7B = 1
    }
    /**
     * Indicates the certificate file data.
     *
     * @syscap SystemCapability.Security.CertificateManager
     * @stagemodelonly
     * @since 26.0.0
     */
    export interface CertBlob {
        /**
         * Certificate file data. When certFormat is transferred to PEM_DER, the maximum length is 8 KB. When certFormat is
         * set to P7B, the maximum length is 300 KB.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @stagemodelonly
         * @since 26.0.0
         */
        certData: Uint8Array;
        /**
         * Indicates the certificate file format.
         * Default value: PEM_DER.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @stagemodelonly
         * @since 26.0.0
         */
        certFormat?: CertFileFormat;
        /**
         * Indicates the storage location of the user CA certificate.
         * Default value: Current_USER.
         *
         * @syscap SystemCapability.Security.CertificateManager
         * @stagemodelonly
         * @since 26.0.0
         */
        certScope?: CertScope;
    }
    /**
     * Install the user CA certificate. Use Promise asynchronous callback.
     *
     * @permission ohos.permission.ACCESS_ENTERPRISE_USER_TRUSTED_CERT or ohos.permission.ACCESS_USER_TRUSTED_CERT
     * @param { CertBlob } certificate - Certificate information.
     * @returns { Promise<CMResult> } Promise used to return the operation result, that is, **uri** in the
     *     [CMResult]{@link certificateManager.CMResult} object.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     <br>The application does not have the permission required to call the API.
     * @throws { BusinessError } 401 - Parameter verification failed. Possible causes:
     *     <br>the certData parameter is empty or exceeds the maximum length .
     * @throws { BusinessError } 17500001 - Internal error. Possible causes: 1. IPC communication failed;
     *     <br>2. Memory operation error; 3. File operation error. Please try again.
     * @throws { BusinessError } 17500003 - Indicates that the certificate is in an invalid format.
     * @throws { BusinessError } 17500004 - Indicates that the number of certificates reaches the maximum allowed.
     * @throws { BusinessError } 17500007 - Indicates that the device enters advanced security mode.
     *     <br>In this mode, the user CA certificate cannot be installed.
     * @syscap SystemCapability.Security.CertificateManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function installUserTrustedCertificate(certificate: CertBlob): Promise<CMResult>;
    /**
     * Obtains the list of USB Key credential . This API uses a promise to return the result.
     *
     * @permission ohos.permission.ACCESS_CERT_MANAGER
     * @param { string } ukeyProvider - USB Key device provider
     * @param { UkeyInfo } ukeyInfo - Attributes of a USB Key credential
     * @returns { Promise<CMResult> } Promise used to return the operation result, that is, **credentialDetailList** in
     *     the [CMResult]{@link certificateManager.CMResult} object.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     <br>The application does not have the permission required to call the API.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 17500001 - Internal error. Possible causes: 1. IPC communication failed;
     *     <br>2. Memory operation error; 3. File operation error.
     * @throws { BusinessError } 17500010 - Indicates that access USB Key service failed.
     * @throws { BusinessError } 17500011 - Parameter verification failed.
     *     <br> Possible causes: the ukeyInfo parameter is invalid.
     *     For example, the parameter format is incorrect or the value range is invalid.
     * @syscap SystemCapability.Security.CertificateManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function getUkeyCertificateList(ukeyProvider: string, ukeyInfo: UkeyInfo): Promise<CMResult>;
    /**
     * Import the certificate to the USB Key.
     *
     * @permission ohos.permission.ACCESS_CERT_MANAGER
     * @param { string } keyUri - Indicates the USB Key credentials URI.
     *     <br>The maximum length is 256 and cannot be empty.
     *     <br>
     *     The keyUri parameter identifies a certificate entity, which can be obtained
     *     <br>by calling the [getUkeyCertificateList]{@link certificateManager.getUkeyCertificateList} interface.
     * @param { Uint8Array } cert - Indicates the certificate data to be imported.
     *     <br>The maximum length is 10240 and cannot be empty.
     *     <br>The certificate data format complies with the Smart Key Framework (SKF) specifications.
     * @param { UkeyInfo } ukeyInfo - Indicates USB Key certificate attribute information.
     *     <br>UkeyInfo.CertificatePurpose can only be set to PURPOSE_SIGN, PURPOSE_ENCRYPT or PURPOSE_DEFAULT.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 201 - Permission verification failed.
     *     The application does not have the permission required to call the API.
     * @throws { BusinessError } 801 - Capability not supported.
     * @throws { BusinessError } 17500001 - Internal error. Possible causes: 1. IPC communication failed;
     *     <br>2. Memory operation error; 3. File operation error. Please try again.
     * @throws { BusinessError } 17500002 - The certificate identified by keyUri does not exist
     * @throws { BusinessError } 17500010 - Indicates that access USB Key service failed.
     * @throws { BusinessError } 17500011 - Indicates that the input parameters validation failed.
     *     For example, the parameter format is incorrect or the value range is invalid.
     * @syscap SystemCapability.Security.CertificateManager
     * @stagemodelonly
     * @since 26.0.0
     */
    function importUkeyCertificate(keyUri: string, cert: Uint8Array, ukeyInfo: UkeyInfo): Promise<void>;
}
export default certificateManager;

```
