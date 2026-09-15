# @ohos.security.cert.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022-2026 Huawei Device Co., Ltd.
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
import cryptoFramework from './@ohos.security.cryptoFramework';
/**
 * The certificate algorithm library framework provides certificate-related APIs. The **certFramework** module depends
 * on the basic algorithm capabilities of the Crypto framework. For details, see
 * [cryptoFramework]{@link @ohos.security.cryptoFramework:cryptoFramework}.
 *
 * @syscap SystemCapability.Security.Cert
 * @crossplatform [since 11]
 * @atomicservice [since 12]
 * @since 9
 */
declare namespace cert {
    /**
     * Enumerates the error codes.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform [since 11]
     * @atomicservice [since 12]
     * @since 9
     */
    enum CertResult {
        /**
         * Invalid parameters.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        INVALID_PARAMS = 401,
        /**
         * This operation is not supported.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        NOT_SUPPORT = 801,
        /**
         * Memory error.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        ERR_OUT_OF_MEMORY = 19020001,
        /**
         * Runtime error.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        ERR_RUNTIME_ERROR = 19020002,
        /**
         * Parameter check failed.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        ERR_PARAMETER_CHECK_FAILED = 19020003,
        /**
         * Crypto operation error.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        ERR_CRYPTO_OPERATION = 19030001,
        /**
         * The certificate signature verification failed.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        ERR_CERT_SIGNATURE_FAILURE = 19030002,
        /**
         * The certificate has not taken effect.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        ERR_CERT_NOT_YET_VALID = 19030003,
        /**
         * The certificate has expired.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        ERR_CERT_HAS_EXPIRED = 19030004,
        /**
         * Failed to obtain the certificate issuer.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        ERR_UNABLE_TO_GET_ISSUER_CERT_LOCALLY = 19030005,
        /**
         * The key cannot be used for signing a certificate.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        ERR_KEYUSAGE_NO_CERTSIGN = 19030006,
        /**
         * The key cannot be used for a digital signature.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        ERR_KEYUSAGE_NO_DIGITAL_SIGNATURE = 19030007,
        /**
         * The password for the private key may be incorrect.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        ERR_MAYBE_WRONG_PASSWORD = 19030008,
        /**
         * Untrusted certificate.
         *
         * @syscap SystemCapability.Security.Cert
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        ERR_CERT_UNTRUSTED = 19030009,
        /**
         * The certificate has been revoked.
         *
         * @syscap SystemCapability.Security.Cert
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        ERR_CERT_HAS_REVOKED = 19030010,
        /**
         * Unsupported critical extension.
         *
         * @syscap SystemCapability.Security.Cert
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        ERR_UNKNOWN_CRITICAL_EXTENSION = 19030011,
        /**
         * Hostname mismatch in the certificate.
         *
         * @syscap SystemCapability.Security.Cert
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        ERR_CERT_HOSTNAME_MISMATCH = 19030012,
        /**
         * Email address mismatch in the certificate.
         *
         * @syscap SystemCapability.Security.Cert
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        ERR_CERT_EMAIL_ADDRESS_MISMATCH = 19030013,
        /**
         * Key usage mismatch in the certificate.
         *
         * @syscap SystemCapability.Security.Cert
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        ERR_CERT_KEYUSAGE_MISMATCH = 19030014,
        /**
         * Failed to obtain the certificate revocation list.
         *
         * @syscap SystemCapability.Security.Cert
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        ERR_CRL_NOT_FOUND = 19030015,
        /**
         * The certificate revocation list has not taken effect.
         *
         * @syscap SystemCapability.Security.Cert
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        ERR_CRL_NOT_YET_VALID = 19030016,
        /**
         * The certificate revocation list has expired.
         *
         * @syscap SystemCapability.Security.Cert
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        ERR_CRL_HAS_EXPIRED = 19030017,
        /**
         * Failed to verify the signature of the certificate revocation list.
         *
         * @syscap SystemCapability.Security.Cert
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        ERR_CRL_SIGNATURE_FAILURE = 19030018,
        /**
         * Failed to find the issuer of the certificate revocation list.
         *
         * @syscap SystemCapability.Security.Cert
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        ERR_CRL_ISSUER_NOT_FOUND = 19030019,
        /**
         * Failed to obtain the OCSP response.
         *
         * @syscap SystemCapability.Security.Cert
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        ERR_OCSP_RESPONSE_NOT_FOUND = 19030020,
        /**
         * Invalid OCSP response.
         *
         * @syscap SystemCapability.Security.Cert
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        ERR_OCSP_RESPONSE_INVALID = 19030021,
        /**
         * Failed to verify the OCSP signature.
         *
         * @syscap SystemCapability.Security.Cert
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        ERR_OCSP_SIGNATURE_FAILURE = 19030022,
        /**
         * Unknown OCSP certificate status.
         *
         * @syscap SystemCapability.Security.Cert
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        ERR_OCSP_CERT_STATUS_UNKNOWN = 19030023,
        /**
         * Network connection timed out.
         *
         * @syscap SystemCapability.Security.Cert
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        ERR_NETWORK_TIMEOUT = 19030024
    }
    /**
     * Encapsulates binary data. The core field **data** is of the Uint8Array type.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform [since 11]
     * @atomicservice [since 12]
     * @since 9
     */
    interface DataBlob {
        /**
         * Indicates the content of the data blob.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        data: Uint8Array;
    }
    /**
     * Defines a list of data arrays.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform [since 11]
     * @atomicservice [since 12]
     * @since 9
     */
    interface DataArray {
        /**
         * Indicates the content of the data array.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        data: Array<Uint8Array>;
    }
    /**
     * Enumerates the certificate encoding formats.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform [since 11]
     * @atomicservice [since 12]
     * @since 9
     */
    enum EncodingFormat {
        /**
         * Distinguished Encoding Rules (DER) format.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        FORMAT_DER = 0,
        /**
         * Privacy-Enhanced Mail (PEM) format.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        FORMAT_PEM = 1,
        /**
         * PKCS #7 format.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        FORMAT_PKCS7 = 2
    }
    /**
     * Enumerates the certificate fields that can be obtained.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform [since 11]
     * @atomicservice [since 12]
     * @since 10
     */
    enum CertItemType {
        /**
         * Information to be signed.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 10
         */
        CERT_ITEM_TYPE_TBS = 0,
        /**
         * Public key of the certificate.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 10
         */
        CERT_ITEM_TYPE_PUBLIC_KEY = 1,
        /**
         * Unique ID of the certificate issuer.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 10
         */
        CERT_ITEM_TYPE_ISSUER_UNIQUE_ID = 2,
        /**
         * Unique ID of the certificate subject.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 10
         */
        CERT_ITEM_TYPE_SUBJECT_UNIQUE_ID = 3,
        /**
         * Certificate extensions, each of which is identified by a unique object identifier (OID).
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 10
         */
        CERT_ITEM_TYPE_EXTENSIONS = 4
    }
    /**
     * Enumerates the OID types of the certificate extensions that can be obtained.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform [since 11]
     * @atomicservice [since 12]
     * @since 10
     */
    enum ExtensionOidType {
        /**
         * All object identifiers.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 10
         */
        EXTENSION_OID_TYPE_ALL = 0,
        /**
         * Object identifier whose **critical** is **true**.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 10
         */
        EXTENSION_OID_TYPE_CRITICAL = 1,
        /**
         * Object identifier whose **critical** is **false**.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 10
         */
        EXTENSION_OID_TYPE_UNCRITICAL = 2
    }
    /**
     * Enumerates the entry types in certificate extensions that can be obtained.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform [since 11]
     * @atomicservice [since 12]
     * @since 10
     */
    enum ExtensionEntryType {
        /**
         * Entire extension entry.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 10
         */
        EXTENSION_ENTRY_TYPE_ENTRY = 0,
        /**
         * Critical attribute (**critical** flag) of the extension entry.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 10
         */
        EXTENSION_ENTRY_TYPE_ENTRY_CRITICAL = 1,
        /**
         * Value (extension-specific data) of the extension entry.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 10
         */
        EXTENSION_ENTRY_TYPE_ENTRY_VALUE = 2
    }
    /**
     * Represents an encoded binary data block.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform [since 11]
     * @atomicservice [since 12]
     * @since 9
     */
    interface EncodingBlob {
        /**
         * Encoded data.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        data: Uint8Array;
        /**
         * Encoding format.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        encodingFormat: EncodingFormat;
    }
    /**
     * Defines the certificate chain data, which is passed in as input parameters during certificate chain verification.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform [since 11]
     * @atomicservice [since 12]
     * @since 9
     */
    interface CertChainData {
        /**
         * Certificate data.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        data: Uint8Array;
        /**
         * Number of certificates contained in the input data.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        count: number;
        /**
         * Certificate encoding format.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        encodingFormat: EncodingFormat;
    }
    /**
     * Enumerates the encoding formats.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    enum EncodingType {
        /**
         * UTF-8.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        ENCODING_UTF8 = 0
    }
    /**
     * Provides APIs for X.509 certificate operations.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform [since 11]
     * @atomicservice [since 12]
     * @since 9
     */
    interface X509Cert {
        /**
         * Verifies the certificate signature. This API uses an asynchronous callback to return the result.
         *
         * @param { cryptoFramework.PubKey } key - Public key used for signature verification.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        verify(key: cryptoFramework.PubKey, callback: AsyncCallback<void>): void;
        /**
         * Verifies the certificate signature. This API uses a promise to return the result.
         *
         * @param { cryptoFramework.PubKey } key - Public key used for signature verification.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        verify(key: cryptoFramework.PubKey): Promise<void>;
        /**
         * Obtains the serialized X.509 certificate data. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<EncodingBlob> } callback - Callback used to return the result. If the operation is
         *     successful, **err** is **undefined**, and **data** is the serialized X.509 certificate data obtained.
         *     Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        getEncoded(callback: AsyncCallback<EncodingBlob>): void;
        /**
         * Obtains the serialized X.509 certificate data. This API uses a promise to return the result.
         *
         * @returns { Promise<EncodingBlob> } Promise used to return the serialized X.509 certificate data obtained.
         * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        getEncoded(): Promise<EncodingBlob>;
        /**
         * Obtains the public key of this X.509 certificate.
         *
         * @returns { cryptoFramework.PubKey } Public key of the X.509 certificate obtained. This object is used only for
         *     **verify()** of **X509Cert**.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        getPublicKey(): cryptoFramework.PubKey;
        /**
         * Checks the validity period of this X.509 certificate.
         *
         * @param { string } date - Date in an ASN.1 time format, specifically UTCTime or GeneralizedTime.
         * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @throws { BusinessError } 19030003 - The certificate has not taken effect.
         * @throws { BusinessError } 19030004 - The certificate has expired.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        checkValidityWithDate(date: string): void;
        /**
         * Obtains the X.509 certificate version.
         *
         * @returns { number } X.509 certificate version obtained.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        getVersion(): number;
        /**
         * Obtains the X.509 certificate serial number.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 9 and deprecated since API version 10. Use
         * > [X509Cert.getCertSerialNumber()]{@link cert.X509Cert.getCertSerialNumber} instead.
         *
         * @returns { number } X.509 certificate serial number obtained.
         * @syscap SystemCapability.Security.Cert
         * @since 9
         * @deprecated since 10
         * @useinstead ohos.security.cert.X509Cert.getCertSerialNumber
         */
        getSerialNumber(): number;
        /**
         * Obtains the X.509 certificate serial number.
         *
         * @returns { bigint } X.509 certificate serial number obtained.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 10
         */
        getCertSerialNumber(): bigint;
        /**
         * Obtains the issuer name of this X.509 certificate.
         *
         * > **NOTE**
         * >
         * > - The obtained X.509 certificate issuer name ends with a NUL terminator (value 0). Determine whether to remove
         * > this terminator based on your business requirements.
         * > - The obtained certificate issuer name is ASCII-encoded. When converted to a string, it is a distinguished name
         * > string that starts with a slash (/) and uses slashes (/) to separate relative distinguished names.
         *
         * @returns { DataBlob } X.509 certificate issuer obtained.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        getIssuerName(): DataBlob;
        /**
         * Obtains the issuer name of this X.509 certificate based on the encoding type.
         *
         * @param { EncodingType } encodingType - Encoding type.
         * @returns { string } Issuer name of an X.509 certificate, separated by commas (,).
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19020003 - Parameter check failed. Possible causes:
         *     <br>1. The value of encodingType is not in the EncodingType enumeration range.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        getIssuerName(encodingType: EncodingType): string;
        /**
         * Obtains the subject name of this X.509 certificate.
         *
         * > **NOTE**
         * >
         * > - If the encodingType parameter is not set, the obtained certificate subject name ends with a
         * > NUL terminator (value 0). Determine whether to remove this terminator based on your business requirements.
         * > - If the encodingType parameter is not set, the obtained certificate subject name is ASCII-encoded. When
         * > converted to a string, it is a distinguished name string that starts with a slash (/) and uses slashes (/) to
         * > separate relative distinguished names.
         * > - It is recommended to set the encodingType parameter to EncodingType.ENCODING_UTF8. The obtained certificate
         * > subject name is a distinguished name string that uses commas (,) to separate relative distinguished names.
         *
         * @param { EncodingType } [encodingType] - Encoding type. If this parameter is set, the subject name in UTF-8
         *     format is to be obtained. If this parameter is not set, the subject name in ASCII encoding format is obtained
         *     by default.<br>This parameter is available since API version 12. [since 12]
         * @returns { DataBlob } Represents the subject name of an X.509 certificate.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
         *     <br>1. Incorrect parameter types;
         *     <br>2. Parameter verification failed. [since 12]
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        getSubjectName(encodingType?: EncodingType): DataBlob;
        /**
         * Obtains the start time of this X.509 certificate.
         *
         * @returns { string } Certificate start time obtained, in an ASN.1 time format, specifically UTCTime or
         *     GeneralizedTime.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        getNotBeforeTime(): string;
        /**
         * Obtains the expiration time of this X.509 certificate.
         *
         * @returns { string } Certificate expiration time obtained, in an ASN.1 time format, specifically UTCTime or
         *     GeneralizedTime.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        getNotAfterTime(): string;
        /**
         * Obtains the signature data of this X.509 certificate.
         *
         * @returns { DataBlob } Signature data obtained.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        getSignature(): DataBlob;
        /**
         * Obtains the signing algorithm of this X.509 certificate.
         *
         * @returns { string } X.509 certificate signing algorithm obtained.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        getSignatureAlgName(): string;
        /**
         * Obtains the object identifier (OID) of the X.509 certificate signing algorithm. OIDs are allocated by the
         * International Organization for Standardization (ISO).
         *
         * @returns { string } OID obtained. It will be truncated if the length exceeds 127 bytes.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        getSignatureAlgOid(): string;
        /**
         * Obtains the signing algorithm parameters of this X.509 certificate.
         *
         * @returns { DataBlob } X.509 certificate signing algorithm parameters obtained.
         * @throws { BusinessError } 801 - This operation is not supported.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        getSignatureAlgParams(): DataBlob;
        /**
         * Obtains the key usage of this X.509 certificate.
         *
         * @returns { DataBlob } Key usage of the X.509 certificate obtained.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        getKeyUsage(): DataBlob;
        /**
         * Obtains the usage of the extended key of this X.509 certificate.
         *
         * @returns { DataArray } Usage of the extended key obtained.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        getExtKeyUsage(): DataArray;
        /**
         * Obtains the basic constraints of this X.509 certificate.
         *
         * @returns { number } Basic constraints obtained.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        getBasicConstraints(): number;
        /**
         * Obtains the Subject Alternative Names (SANs) of this X.509 certificate.
         *
         * > **NOTE**
         * >
         * > The obtained SANs contain a string terminator.
         *
         * @returns { DataArray } SANs obtained.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        getSubjectAltNames(): DataArray;
        /**
         * Obtains the Issuer Alternative Names (IANs) of this X.509 certificate.
         *
         * > **NOTE**
         * >
         * > The obtained IANs contain a string terminator.
         *
         * @returns { DataArray } IANs obtained.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        getIssuerAltNames(): DataArray;
        /**
         * Obtains the fields in the X.509 certificate.
         *
         * @param { CertItemType } itemType - Certificate field to obtain.
         * @returns { DataBlob } Fields in DER format.
         * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 10
         */
        getItem(itemType: CertItemType): DataBlob;
        /**
         * Checks whether this certificate matches the specified parameters.
         *
         * @param { X509CertMatchParameters } param - Parameters specified for matching the certificate.
         * @returns { boolean } Returns **true** if the certificate matches the parameters specified; returns **false**
         *     otherwise.
         * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        match(param: X509CertMatchParameters): boolean;
        /**
         * Obtains the CRL distribution points of this X.509 certificate.
         *
         * @returns { DataArray } URIs of the CRL distribution points from this X.509 certificate obtained.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        getCRLDistributionPoint(): DataArray;
        /**
         * Obtains the X.500 distinguished name object of the X.509 certificate issuer.
         *
         * @returns { X500DistinguishedName } X.500 distinguished name object.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        getIssuerX500DistinguishedName(): X500DistinguishedName;
        /**
         * Obtains the X.500 distinguished name object of the X.509 certificate subject.
         *
         * @returns { X500DistinguishedName } X.500 distinguished name object.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        getSubjectX500DistinguishedName(): X500DistinguishedName;
        /**
         * Converts the object data into a string.
         *
         * @returns { string } String obtained.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        toString(): string;
        /**
         * Converts this object into a string in the specified encoding format.
         *
         * @param { EncodingType } encodingType - Encoding type.
         * @returns { string } String obtained.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19020003 - Parameter check failed. Possible causes:
         *     <br>1. The value of encodingType is not in the EncodingType enumeration range.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        toString(encodingType: EncodingType): string;
        /**
         * Obtains the hash value of the data in DER format.
         *
         * @returns { Uint8Array } Hash value obtained.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        hashCode(): Uint8Array;
        /**
         * Obtains the certificate extension object.
         *
         * @returns { CertExtension } Certificate extensions object obtained.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        getExtensionsObject(): CertExtension;
    }
    /**
     * Creates an **X509Cert** instance. This API uses an asynchronous callback to return the result.
     *
     * @param { EncodingBlob } inStream - X.509 certificate serialization data.
     * @param { AsyncCallback<X509Cert> } callback - Callback used to return the result. If the operation is successful,
     *     **err** is **undefined**, and **data** is the **X509Cert** instance created. Otherwise, **err** is an error
     *     object.
     * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
     *     <br>1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types;
     *     <br>3. Parameter verification failed.
     * @throws { BusinessError } 801 - This operation is not supported.
     * @throws { BusinessError } 19020001 - Memory malloc failed.
     * @throws { BusinessError } 19030001 - Crypto operation error.
     * @syscap SystemCapability.Security.Cert
     * @crossplatform [since 11]
     * @atomicservice [since 12]
     * @since 9
     */
    function createX509Cert(inStream: EncodingBlob, callback: AsyncCallback<X509Cert>): void;
    /**
     * Creates an **X509Cert** instance. This API uses a promise to return the result.
     *
     * @param { EncodingBlob } inStream - X.509 certificate serialization data.
     * @returns { Promise<X509Cert> } Promise used to return the **X509Cert** instance created.
     * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
     *     <br>1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types;
     *     <br>3. Parameter verification failed.
     * @throws { BusinessError } 801 - This operation is not supported.
     * @throws { BusinessError } 19020001 - Memory malloc failed.
     * @throws { BusinessError } 19030001 - Crypto operation error.
     * @syscap SystemCapability.Security.Cert
     * @crossplatform [since 11]
     * @atomicservice [since 12]
     * @since 9
     */
    function createX509Cert(inStream: EncodingBlob): Promise<X509Cert>;
    /**
     * Provides APIs for operating on certificate extensions.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform [since 11]
     * @atomicservice [since 12]
     * @since 10
     */
    interface CertExtension {
        /**
         * Obtains the serialized data of the certificate extensions.
         *
         * @returns { EncodingBlob } Serialized data obtained.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 10
         */
        getEncoded(): EncodingBlob;
        /**
         * Obtains the OIDs of the certificate extensions.
         *
         * @param { ExtensionOidType } valueType - Type of the OIDs to obtain.
         * @returns { DataArray } OIDs obtained.
         * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 10
         */
        getOidList(valueType: ExtensionOidType): DataArray;
        /**
         * Obtains the value of a specific certificate extension entry by OID.
         *
         * @param { ExtensionEntryType } valueType - Type of the information to obtain.
         * @param { DataBlob } oid - OID of the certificate extension to obtain.
         * @returns { DataBlob } Certificate extension object information obtained.
         * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 10
         */
        getEntry(valueType: ExtensionEntryType, oid: DataBlob): DataBlob;
        /**
         * Checks whether the certificate is a CA certificate.
         *
         * @returns { number } If the key usage extension contains the keyCertSign bit and the CA field in the basic
         *     constraints is **true**, the certificate is a CA certificate. Returns **-1** if the certificate is not a CA
         *     certificate; returns the path length in the basic constraints otherwise. Returns **-2** if the certificate is
         *     a CA certificate but the path length is not specified in the basic constraints, which means the path length
         *     is not limited.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 10
         */
        checkCA(): number;
        /**
         * Checks whether there is a critical extension that is not supported.
         *
         * @returns { boolean } Returns **true** if an unsupported critical extension is found; returns **false** otherwise.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        hasUnsupportedCriticalExtension(): boolean;
    }
    /**
     * Creates a certificate extension object. This API uses an asynchronous callback to return the result.
     *
     * @param { EncodingBlob } inStream - Serialized certificate extension data.
     * @param { AsyncCallback<CertExtension> } callback - Callback used to return the result. If the operation is
     *     successful, **err** is **undefined**, and **data** is the **CertExtension** instance created. Otherwise,
     *     **err** is an error object.
     * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
     *     <br>1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types;
     *     <br>3. Parameter verification failed.
     * @throws { BusinessError } 801 - This operation is not supported.
     * @throws { BusinessError } 19020001 - Memory malloc failed.
     * @throws { BusinessError } 19030001 - Crypto operation error.
     * @syscap SystemCapability.Security.Cert
     * @crossplatform [since 11]
     * @atomicservice [since 12]
     * @since 10
     */
    function createCertExtension(inStream: EncodingBlob, callback: AsyncCallback<CertExtension>): void;
    /**
     * Creates a certificate extension object. This API uses a promise to return the result.
     *
     * @param { EncodingBlob } inStream - Serialized certificate extension data.
     * @returns { Promise<CertExtension> } Promise used to return the **CertExtension** instance created.
     * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
     *     <br>1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types;
     *     <br>3. Parameter verification failed.
     * @throws { BusinessError } 801 - This operation is not supported.
     * @throws { BusinessError } 19020001 - Memory malloc failed.
     * @throws { BusinessError } 19030001 - Crypto operation error.
     * @syscap SystemCapability.Security.Cert
     * @crossplatform [since 11]
     * @atomicservice [since 12]
     * @since 10
     */
    function createCertExtension(inStream: EncodingBlob): Promise<CertExtension>;
    /**
     * Provides APIs for operating on a revoked certificate entry in a CRL.
     *
     * > **NOTE**
     * >
     * > This API is supported since API version 9 and deprecated since API version 11. Use
     * > [X509CRLEntry()]{@link cert.X509CRLEntry} instead.
     *
     * @syscap SystemCapability.Security.Cert
     * @since 9
     * @deprecated since 11
     * @useinstead ohos.security.cert.X509CRLEntry
     */
    interface X509CrlEntry {
        /**
         * Obtains the serialized data of this revoked certificate entry. This API uses an asynchronous callback to return the
         * result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 9 and deprecated since API version 11. Use
         * > [X509CRLEntry.getEncoded()]{@link cert.X509CRLEntry.getEncoded(callback: AsyncCallback<EncodingBlob>)} instead.
         *
         * @param { AsyncCallback<EncodingBlob> } callback - Callback used to return the result. If the operation is
         *     successful, **err** is **undefined**, and **data** is the serialized data of the revoked certificate entry
         *     obtained. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @since 9
         * @deprecated since 11
         * @useinstead ohos.security.cert.X509CRLEntry#getEncoded
         */
        getEncoded(callback: AsyncCallback<EncodingBlob>): void;
        /**
         * Obtains the serialized data of this revoked certificate entry. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 9 and deprecated since API version 11. Use
         * > [X509CRLEntry.getEncoded()]{@link cert.X509CRLEntry.getEncoded()} instead.
         *
         * @returns { Promise<EncodingBlob> } Promise used to return the serialized data of the revoked certificate entry
         *     obtained.
         * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @since 9
         * @deprecated since 11
         * @useinstead ohos.security.cert.X509CRLEntry#getEncoded
         */
        getEncoded(): Promise<EncodingBlob>;
        /**
         * Obtains the serial number of this revoked certificate.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 9 and deprecated since API version 11. Use
         * > [X509CRLEntry.getSerialNumber()]{@link cert.X509CRLEntry.getSerialNumber} instead.
         *
         * @returns { number } Serial number of the revoked certificate obtained.
         * @syscap SystemCapability.Security.Cert
         * @since 9
         * @deprecated since 11
         * @useinstead ohos.security.cert.X509CRLEntry#getSerialNumber
         */
        getSerialNumber(): number;
        /**
         * Obtains the issuer name of the revoked certificate.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 9 and deprecated since API version 11. Use
         * > [X509CRLEntry.getCertIssuer()]{@link cert.X509CRLEntry.getCertIssuer()} instead.
         *
         * @returns { DataBlob } Issuer name of the revoked certificate obtained.
         * @throws { BusinessError } 801 - This operation is not supported.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @syscap SystemCapability.Security.Cert
         * @since 9
         * @deprecated since 11
         * @useinstead ohos.security.cert.X509CRLEntry#getCertIssuer
         */
        getCertIssuer(): DataBlob;
        /**
         * Obtains the certificate's revocation date.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 9 and deprecated since API version 11. Use
         * > [X509CRLEntry.getRevocationDate()]{@link cert.X509CRLEntry.getRevocationDate} instead.
         *
         * @returns { string } Certificate revocation date,  in an ASN.1 time format, specifically UTCTime or
         *     GeneralizedTime.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @since 9
         * @deprecated since 11
         * @useinstead ohos.security.cert.X509CRLEntry#getRevocationDate
         */
        getRevocationDate(): string;
    }
    /**
     * Provides APIs for operating on a revoked certificate entry in a CRL.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice [since 12]
     * @since 11
     */
    interface X509CRLEntry {
        /**
         * Obtains the serialized data of this revoked certificate entry. This API uses an asynchronous callback to return
         * the result.
         *
         * @param { AsyncCallback<EncodingBlob> } callback - Callback used to return the result. If the operation is
         *     successful, **err** is **undefined**, and **data** is the serialized data of the revoked certificate entry
         *     obtained. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        getEncoded(callback: AsyncCallback<EncodingBlob>): void;
        /**
         * Obtains the serialized data of this revoked certificate entry. This API uses a promise to return the result.
         *
         * @returns { Promise<EncodingBlob> } Promise used to return the serialized data of the revoked certificate entry
         *     obtained.
         * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        getEncoded(): Promise<EncodingBlob>;
        /**
         * Obtains the serial number of this revoked certificate.
         *
         * @returns { bigint } Serial number of the revoked certificate obtained.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        getSerialNumber(): bigint;
        /**
         * Obtains the issuer name of the revoked certificate.
         *
         * > **NOTE**
         * >
         * > The obtained issuer name of this revoked certificate contains a string terminator.
         *
         * @returns { DataBlob } Issuer name of the revoked certificate obtained.
         * @throws { BusinessError } 801 - This operation is not supported.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        getCertIssuer(): DataBlob;
        /**
         * Obtains the issuer name of the revoked certificate based on the encoding type.
         *
         * @param { EncodingType } encodingType - Encoding type.
         * @returns { string } Issuer name of the revoked certificate, separated by commas (,).
         * @throws { BusinessError } 801 - This operation is not supported.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19020003 - Parameter check failed. Possible causes:
         *     <br>1. The value of encodingType is not in the EncodingType enumeration range.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        getCertIssuer(encodingType: EncodingType): string;
        /**
         * Obtains the certificate's revocation date.
         *
         * @returns { string } The certificate revocation date obtained.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        getRevocationDate(): string;
        /**
         * Obtains the CRL entry extensions in DER format.
         *
         * @returns { DataBlob } X.509 CRL entry extensions obtained.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        getExtensions(): DataBlob;
        /**
         * Checks whether this CRL entry has extensions.
         *
         * @returns { boolean } Returns **true** if the CRL entry has an extension; returns **false** otherwise.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        hasExtensions(): boolean;
        /**
         * Obtains the distinguished name (DN) of the issuer of the revoked certificate.
         *
         * @returns { X500DistinguishedName } DN object obtained.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        getCertIssuerX500DistinguishedName(): X500DistinguishedName;
        /**
         * Converts the object data into a string.
         *
         * @returns { string } String obtained.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        toString(): string;
        /**
         * Obtains the hash value of the data in DER format.
         *
         * @returns { Uint8Array } Hash value obtained.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        hashCode(): Uint8Array;
        /**
         * Obtains the CRL entry extension object.
         *
         * @returns { CertExtension } CRL entry extensions.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        getExtensionsObject(): CertExtension;
    }
    /**
     * Provides APIs for X.509 CRL operations.
     *
     * > **NOTE**
     * >
     * > This API is supported since API version 9 and deprecated since API version 11. Use [X509CRL()]{@link cert.X509CRL}
     * > instead.
     *
     * @syscap SystemCapability.Security.Cert
     * @since 9
     * @deprecated since 11
     * @useinstead ohos.security.cert.X509CRL
     */
    interface X509Crl {
        /**
         * Checks whether an X.509 certificate is revoked.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 9 and deprecated since API version 11. Use
         * > [X509CRL.isRevoked()]{@link cert.X509CRL.isRevoked} instead.
         *
         * @param { X509Cert } cert - X.509 certificate to check.
         * @returns { boolean } Whether the certificate is revoked. The value **true** indicates that the certificate is
         *     revoked, and **false** indicates the opposite.
         * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @syscap SystemCapability.Security.Cert
         * @since 9
         * @deprecated since 11
         * @useinstead ohos.security.cert.X509CRL#isRevoked
         */
        isRevoked(cert: X509Cert): boolean;
        /**
         * Obtains the CRL type.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 9 and deprecated since API version 11. Use
         * > [X509CRL.getType()]{@link cert.X509CRL.getType} instead.
         *
         * @returns { string } CRL type obtained.
         * @syscap SystemCapability.Security.Cert
         * @since 9
         * @deprecated since 11
         * @useinstead ohos.security.cert.X509CRL#getType
         */
        getType(): string;
        /**
         * Obtains the serialized X.509 CRL data. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 9 and deprecated since API version 11. Use
         * > [X509CRL.getEncoded()]{@link cert.X509CRL.getEncoded(callback: AsyncCallback<EncodingBlob>)} instead.
         *
         * @param { AsyncCallback<EncodingBlob> } callback - Callback used to return the result. If the operation is
         *     successful, **err** is **undefined**, and **data** is the serialized X.509 CRL data obtained. Otherwise,
         *     **err** is an error object.
         * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @since 9
         * @deprecated since 11
         * @useinstead ohos.security.cert.X509CRL#getEncoded
         */
        getEncoded(callback: AsyncCallback<EncodingBlob>): void;
        /**
         * Obtains the serialized X.509 CRL data. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 9 and deprecated since API version 11. Use
         * > [X509CRL.getEncoded()]{@link cert.X509CRL.getEncoded()} instead.
         *
         * @returns { Promise<EncodingBlob> } Promise used to return the serialized X.509 CRL data obtained.
         * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @since 9
         * @deprecated since 11
         * @useinstead ohos.security.cert.X509CRL#getEncoded
         */
        getEncoded(): Promise<EncodingBlob>;
        /**
         * Verifies the signature of the X.509 CRL. The RSA algorithm is supported. This API uses an asynchronous callback
         * to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 9 and deprecated since API version 11. Use
         * > [X509CRL.verify()]{@link cert.X509CRL.verify(key: cryptoFramework.PubKey, callback: AsyncCallback<void>)}
         * > instead.
         *
         * @param { cryptoFramework.PubKey } key - Public key used for signature verification.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @since 9
         * @deprecated since 11
         * @useinstead ohos.security.cert.X509CRL#verify
         */
        verify(key: cryptoFramework.PubKey, callback: AsyncCallback<void>): void;
        /**
         * Verifies the signature of the X.509 CRL. The RSA algorithm is supported. This API uses a promise to return the
         * result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 9 and deprecated since API version 11. Use
         * > [X509CRL.verify()]{@link cert.X509CRL.verify(key: cryptoFramework.PubKey)} instead.
         *
         * @param { cryptoFramework.PubKey } key - Public key used for signature verification.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @since 9
         * @deprecated since 11
         * @useinstead ohos.security.cert.X509CRL#verify
         */
        verify(key: cryptoFramework.PubKey): Promise<void>;
        /**
         * Obtains the version of the X.509 CRL.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 9 and deprecated since API version 11. Use
         * > [X509CRL.getVersion()]{@link cert.X509CRL.getVersion} instead.
         *
         * @returns { number } Version of the X.509 CRL obtained.
         * @syscap SystemCapability.Security.Cert
         * @since 9
         * @deprecated since 11
         * @useinstead ohos.security.cert.X509CRL#getVersion
         */
        getVersion(): number;
        /**
         * Obtains the issuer of the X.509 CRL.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 9 and deprecated since API version 11. Use
         * > [X509CRL.getIssuerName()]{@link cert.X509CRL.getIssuerName()} instead.
         *
         * @returns { DataBlob } Issuer of the X.509 CRL obtained.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @since 9
         * @deprecated since 11
         * @useinstead ohos.security.cert.X509CRL#getIssuerName
         */
        getIssuerName(): DataBlob;
        /**
         * Obtains the last update date of this X.509 CRL.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 9 and deprecated since API version 11. Use
         * > [X509CRL.getLastUpdate()]{@link cert.X509CRL.getLastUpdate} instead.
         *
         * @returns { string } Last update date of the X.509 CRL, in an ASN.1 time format, specifically UTCTime or
         *     GeneralizedTime.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @since 9
         * @deprecated since 11
         * @useinstead ohos.security.cert.X509CRL#getLastUpdate
         */
        getLastUpdate(): string;
        /**
         * Obtains the next update date of this CRL.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 9 and deprecated since API version 11. Use
         * > [X509CRL.getNextUpdate()]{@link cert.X509CRL.getNextUpdate} instead.
         *
         * @returns { string } Next update date of the CRL, in an ASN.1 time format, specifically UTCTime or
         *     GeneralizedTime.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @since 9
         * @deprecated since 11
         * @useinstead ohos.security.cert.X509CRL#getNextUpdate
         */
        getNextUpdate(): string;
        /**
         * Obtains the revoked certificate entry from the X.509 CRL based on the specified serial number of the certificate.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 9 and deprecated since API version 11. Use
         * > [X509CRL.getRevokedCert()]{@link cert.X509CRL.getRevokedCert} instead.
         *
         * @param { number } serialNumber - Serial number of the certificate.
         * @returns { X509CrlEntry } Revoked certificate entry obtained.
         * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @since 9
         * @deprecated since 11
         * @useinstead ohos.security.cert.X509CRL#getRevokedCert
         */
        getRevokedCert(serialNumber: number): X509CrlEntry;
        /**
         * Obtains the revoked certificate entry from the X.509 CRL based on the specified certificate.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 9 and deprecated since API version 11. Use
         * > [X509CRL.getRevokedCertWithCert()]{@link cert.X509CRL.getRevokedCertWithCert} instead.
         *
         * @param { X509Cert } cert - Certificate based on which the revoked certificate is obtained.
         * @returns { X509CrlEntry } Revoked certificate entry obtained.
         * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @since 9
         * @deprecated since 11
         * @useinstead ohos.security.cert.X509CRL#getRevokedCertWithCert
         */
        getRevokedCertWithCert(cert: X509Cert): X509CrlEntry;
        /**
         * Obtains all the revoked certificate entries from the X.509 CRL. This API uses an asynchronous callback to return
         * the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 9 and deprecated since API version 11. Use
         * > [X509CRL.getRevokedCerts()]{@link cert.X509CRL.getRevokedCerts(callback: AsyncCallback<Array<X509CRLEntry>>)}
         * > instead.
         *
         * @param { AsyncCallback<Array<X509CrlEntry>> } callback - Callback used to return the result. If the operation is
         *     successful, **err** is **undefined**, and **data** is the revoked certificate entries obtained. Otherwise,
         *     **err** is an error object.
         * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @since 9
         * @deprecated since 11
         * @useinstead ohos.security.cert.X509CRL#getRevokedCerts
         */
        getRevokedCerts(callback: AsyncCallback<Array<X509CrlEntry>>): void;
        /**
         * Obtains all the revoked certificate entries from the X.509 CRL. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 9 and deprecated since API version 11. Use
         * > [X509CRL.getRevokedCerts()]{@link cert.X509CRL.getRevokedCerts()} instead.
         *
         * @returns { Promise<Array<X509CrlEntry>> } Promise used to return the revoked certificate entries obtained.
         * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @since 9
         * @deprecated since 11
         * @useinstead ohos.security.cert.X509CRL#getRevokedCerts
         */
        getRevokedCerts(): Promise<Array<X509CrlEntry>>;
        /**
         * Obtains the DER-encoded CRL information, that is, **tbsCertList** from this CRL.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 9 and deprecated since API version 11. Use
         * > [X509CRL.getTBSInfo()]{@link cert.X509CRL.getTBSInfo} instead.
         *
         * @returns { DataBlob } **tbsCertList** information obtained.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @since 9
         * @deprecated since 11
         * @useinstead ohos.security.cert.X509CRL#getTBSInfo
         */
        getTbsInfo(): DataBlob;
        /**
         * Obtains the signature data of the X.509 CRL.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 9 and deprecated since API version 11. Use
         * > [X509CRL.getSignature()]{@link cert.X509CRL.getSignature} instead.
         *
         * @returns { DataBlob } Signature data of the X.509 CRL obtained.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @since 9
         * @deprecated since 11
         * @useinstead ohos.security.cert.X509CRL#getSignature
         */
        getSignature(): DataBlob;
        /**
         * Obtains the signing algorithm of the X.509 CRL.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 9 and deprecated since API version 11. Use
         * > [X509CRL.getSignatureAlgName()]{@link cert.X509CRL.getSignatureAlgName} instead.
         *
         * @returns { string } Signing algorithm obtained.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @since 9
         * @deprecated since 11
         * @useinstead ohos.security.cert.X509CRL#getSignatureAlgName
         */
        getSignatureAlgName(): string;
        /**
         * Obtains the OID of the X.509 CRL signing algorithm. OIDs are allocated by the International Organization for
         * Standardization (ISO).
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 9 and deprecated since API version 11. Use
         * > [X509CRL.getSignatureAlgOid()]{@link cert.X509CRL.getSignatureAlgOid} instead.
         *
         * @returns { string } OID of the X.509 CRL signing algorithm obtained.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @since 9
         * @deprecated since 11
         * @useinstead ohos.security.cert.X509CRL#getSignatureAlgOid
         */
        getSignatureAlgOid(): string;
        /**
         * Obtains the parameters of the X.509 CRL signing algorithm.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 9 and deprecated since API version 11. Use
         * > [X509CRL.getSignatureAlgParams()]{@link cert.X509CRL.getSignatureAlgParams} instead.
         *
         * @returns { DataBlob } Algorithm parameters obtained.
         * @throws { BusinessError } 801 - This operation is not supported.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @since 9
         * @deprecated since 11
         * @useinstead ohos.security.cert.X509CRL#getSignatureAlgParams
         */
        getSignatureAlgParams(): DataBlob;
    }
    /**
     * Creates an **X509Crl** instance. This API uses an asynchronous callback to return the result.
     *
     * > **NOTE**
     * >
     * > This API is supported since API version 9 and deprecated since API version 11. Use
     * > [cert.createX509CRL()]{@link cert.createX509CRL(inStream: EncodingBlob, callback: AsyncCallback<X509CRL>)} instead.
     *
     * @param { EncodingBlob } inStream - Serialized CRL data.
     * @param { AsyncCallback<X509Crl> } callback - Callback used to return the result. If the operation is successful,
     *     **err** is **undefined**, and **data** is the **X509Crl** instance created. Otherwise, **err** is an error
     *     object.
     * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
     *     <br>1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types;
     *     <br>3. Parameter verification failed.
     * @throws { BusinessError } 801 - This operation is not supported.
     * @throws { BusinessError } 19020001 - Memory malloc failed.
     * @syscap SystemCapability.Security.Cert
     * @since 9
     * @deprecated since 11
     * @useinstead ohos.security.cert#createX509CRL
     */
    function createX509Crl(inStream: EncodingBlob, callback: AsyncCallback<X509Crl>): void;
    /**
     * Creates an **X509Crl** instance. This API uses a promise to return the result.
     *
     * > **NOTE**
     * >
     * > This API is supported since API version 9 and deprecated since API version 11. Use
     * > [cert.createX509CRL()]{@link cert.createX509CRL(inStream: EncodingBlob)} instead.
     *
     * @param { EncodingBlob } inStream - Serialized CRL data.
     * @returns { Promise<X509Crl> } Promise used to return the **X509Crl** instance created.
     * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
     *     <br>1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types;
     *     <br>3. Parameter verification failed.
     * @throws { BusinessError } 801 - This operation is not supported.
     * @throws { BusinessError } 19020001 - Memory malloc failed.
     * @syscap SystemCapability.Security.Cert
     * @since 9
     * @deprecated since 11
     * @useinstead ohos.security.cert#createX509CRL
     */
    function createX509Crl(inStream: EncodingBlob): Promise<X509Crl>;
    /**
     * Provides APIs for X.509 CRL operations.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice [since 12]
     * @since 11
     */
    interface X509CRL {
        /**
         * Checks whether an X.509 certificate is revoked.
         *
         * @param { X509Cert } cert - X.509 certificate to check.
         * @returns { boolean } Whether the certificate is revoked. The value **true** indicates that the certificate is
         *     revoked, and **false** indicates the opposite.
         * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        isRevoked(cert: X509Cert): boolean;
        /**
         * Obtains the CRL type.
         *
         * @returns { string } CRL type obtained.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        getType(): string;
        /**
         * Obtains the serialized X.509 CRL data. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<EncodingBlob> } callback - Callback used to return the result. If the operation is
         *     successful, **err** is **undefined**, and **data** is the serialized X.509 CRL data obtained. Otherwise,
         *     **err** is an error object.
         * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        getEncoded(callback: AsyncCallback<EncodingBlob>): void;
        /**
         * Obtains the serialized X.509 CRL data. This API uses a promise to return the result.
         *
         * @returns { Promise<EncodingBlob> } Promise used to return the serialized X.509 CRL data obtained.
         * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        getEncoded(): Promise<EncodingBlob>;
        /**
         * Verifies the signature of the X.509 CRL. The RSA algorithm is supported. This API uses an asynchronous callback
         * to return the result.
         *
         * @param { cryptoFramework.PubKey } key - Public key used for signature verification.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        verify(key: cryptoFramework.PubKey, callback: AsyncCallback<void>): void;
        /**
         * Verifies the signature of the X.509 CRL. The RSA algorithm is supported. This API uses a promise to return the
         * result.
         *
         * @param { cryptoFramework.PubKey } key - Public key used for signature verification.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        verify(key: cryptoFramework.PubKey): Promise<void>;
        /**
         * Obtains the version of the X.509 CRL.
         *
         * @returns { number } Version of the X.509 CRL obtained.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        getVersion(): number;
        /**
         * Obtains the issuer of the X.509 CRL.
         *
         * > **NOTE**
         * >
         * > The obtained X.509 CRL issuer name contains a string terminator.
         *
         * @returns { DataBlob } Issuer of the X.509 CRL obtained.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        getIssuerName(): DataBlob;
        /**
         * Obtains the issuer name of an X.509 CRL based on the encoding type.
         *
         * @param { EncodingType } encodingType - Encoding type.
         * @returns { string } Issuer name of an X.509 CRL, separated by commas (,).
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19020003 - Parameter check failed. Possible causes:
         *     <br>1. The value of encodingType is not in the EncodingType enumeration range.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        getIssuerName(encodingType: EncodingType): string;
        /**
         * Obtains the last update date of this X.509 CRL.
         *
         * @returns { string } Last update date of the X.509 CRL, in an ASN.1 time format, specifically UTCTime or
         *     GeneralizedTime.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        getLastUpdate(): string;
        /**
         * Obtains the next update date of this CRL.
         *
         * @returns { string } Next update date of the CRL, in an ASN.1 time format, specifically UTCTime or
         *     GeneralizedTime.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        getNextUpdate(): string;
        /**
         * Obtains the revoked certificate entry from the X.509 CRL based on the specified serial number.
         *
         * @param { bigint } serialNumber - Serial number of the certificate.
         * @returns { X509CRLEntry } Revoked certificate entry obtained.
         * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        getRevokedCert(serialNumber: bigint): X509CRLEntry;
        /**
         * Obtains the revoked certificate entry from the X.509 CRL based on the specified certificate.
         *
         * @param { X509Cert } cert - Certificate based on which the revoked certificate is obtained.
         * @returns { X509CRLEntry } Revoked certificate entry obtained.
         * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        getRevokedCertWithCert(cert: X509Cert): X509CRLEntry;
        /**
         * Obtains all the revoked certificate entries from the X.509 CRL. This API uses an asynchronous callback to return
         * the result.
         *
         * @param { AsyncCallback<Array<X509CRLEntry>> } callback - Callback used to return the result. If the operation is
         *     successful, **err** is **undefined**, and **data** is the revoked certificate entries obtained. Otherwise,
         *     **err** is an error object.
         * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        getRevokedCerts(callback: AsyncCallback<Array<X509CRLEntry>>): void;
        /**
         * Obtains all the revoked certificate entries from the X.509 CRL. This API uses a promise to return the result.
         *
         * @returns { Promise<Array<X509CRLEntry>> } Promise used to return the revoked certificate entries obtained.
         * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        getRevokedCerts(): Promise<Array<X509CRLEntry>>;
        /**
         * Obtains the DER-encoded CRL information, that is, **tbsCertList** from this CRL.
         *
         * @returns { DataBlob } **tbsCertList** information obtained.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        getTBSInfo(): DataBlob;
        /**
         * Obtains the signature data of the X.509 CRL.
         *
         * @returns { DataBlob } Signature data of the X.509 CRL obtained.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        getSignature(): DataBlob;
        /**
         * Obtains the signing algorithm of the X.509 CRL.
         *
         * @returns { string } Signing algorithm obtained.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        getSignatureAlgName(): string;
        /**
         * Obtains the OID of the X.509 CRL signing algorithm. OIDs are allocated by the International Organization for
         * Standardization (ISO).
         *
         * @returns { string } OID of the X.509 CRL signing algorithm obtained.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        getSignatureAlgOid(): string;
        /**
         * Obtains the parameters of the X.509 CRL signing algorithm.
         *
         * @returns { DataBlob } Algorithm parameters obtained.
         * @throws { BusinessError } 801 - This operation is not supported.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        getSignatureAlgParams(): DataBlob;
        /**
         * Obtains the CRL extensions data in DER format.
         *
         * @returns { DataBlob } CRL extensions data in DER format obtained.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        getExtensions(): DataBlob;
        /**
         * Checks whether this CRL matches the specified parameters.
         *
         * @param { X509CRLMatchParameters } param - Parameters specified for matching the CRL.
         * @returns { boolean } Returns **true** if the CRL matches the parameters specified; returns **false**
         *     otherwise.
         * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        match(param: X509CRLMatchParameters): boolean;
        /**
         * Obtains the distinguished name (DN) of the X.509 CRL issuer.
         *
         * @returns { X500DistinguishedName } DN object obtained.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        getIssuerX500DistinguishedName(): X500DistinguishedName;
        /**
         * Converts the object data into a string.
         *
         * @returns { string } String obtained.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        toString(): string;
        /**
         * Converts this object into a string in the specified encoding format.
         *
         * @param { EncodingType } encodingType - Encoding type.
         * @returns { string } String obtained.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19020003 - Parameter check failed. Possible causes:
         *     <br>1. The value of encodingType is not in the EncodingType enumeration range.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        toString(encodingType: EncodingType): string;
        /**
         * Obtains the hash value of the data in DER format.
         *
         * @returns { Uint8Array } Hash value obtained.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        hashCode(): Uint8Array;
        /**
         * Obtains the CRL extension object.
         *
         * @returns { CertExtension } CRL extensions object obtained.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        getExtensionsObject(): CertExtension;
    }
    /**
     * Creates an **X509CRL** instance. This API uses an asynchronous callback to return the result.
     *
     * @param { EncodingBlob } inStream - Serialized CRL data. The data length cannot exceed 8192 bytes.
     * @param { AsyncCallback<X509CRL> } callback - Callback used to return the result. If the operation is successful,
     *     **err** is **undefined**, and **data** is the **X509CRL** instance created. Otherwise, **err** is an error
     *     object.
     * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
     *     <br>1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types;
     *     <br>3. Parameter verification failed.
     * @throws { BusinessError } 801 - This operation is not supported.
     * @throws { BusinessError } 19020001 - Memory malloc failed.
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice [since 12]
     * @since 11
     */
    function createX509CRL(inStream: EncodingBlob, callback: AsyncCallback<X509CRL>): void;
    /**
     * Creates an **X509CRL** instance. This API uses a promise to return the result.
     *
     * @param { EncodingBlob } inStream - Serialized CRL data. The data length cannot exceed 8192 bytes.
     * @returns { Promise<X509CRL> } Promise used to return the **X509CRL** instance created.
     * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
     *     <br>1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types;
     *     <br>3. Parameter verification failed.
     * @throws { BusinessError } 801 - This operation is not supported.
     * @throws { BusinessError } 19020001 - Memory malloc failed.
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice [since 12]
     * @since 11
     */
    function createX509CRL(inStream: EncodingBlob): Promise<X509CRL>;
    /**
     * Enumerates the certificate revocation flags.
     *
     * @syscap SystemCapability.Security.Cert
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    enum CertRevocationFlag {
        /**
         * OCSP check is preferred. This flag is valid only when CERT_REVOCATION_CRL_CHECK and CERT_REVOCATION_OCSP_CHECK
         * are both set.
         *
         * - If this flag is set, OCSP check is performed first, and CRL check is performed if no OCSP response is found or
         * a timeout occurs;
         * - If this flag is not set, CRL check is performed first, and OCSP check is performed if no CRL is found or a
         * timeout occurs.
         *
         * @syscap SystemCapability.Security.Cert
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        CERT_REVOCATION_PREFER_OCSP = 0,
        /**
         * Enables the CRL check. Checks the certificate status using a certificate revocation list.
         *
         * <br>First, the **crls** parameter of [X509CertRevokedParams]{@link cert.X509CertRevokedParams} is used. If no
         * matching CRL is found and **allowDownloadCrl** of [X509CertRevokedParams]{@link cert.X509CertRevokedParams} is
         * set to **true**, the CDP extension of the certificate is used to download the CRL.
         *
         * @syscap SystemCapability.Security.Cert
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        CERT_REVOCATION_CRL_CHECK = 1,
        /**
         * Enables OCSP check. Checks the certificate status using the Online Certificate Status Protocol.
         *
         * <br>First, the **ocspResponses** parameter of [X509CertRevokedParams]{@link cert.X509CertRevokedParams} is used.
         * If no matching OCSP response is found and **allowOcspCheckOnline** of
         * [X509CertRevokedParams]{@link cert.X509CertRevokedParams} is set to **true**, the system attempts to obtain the
         * OCSP URL from the certificate AIA extension and sends a request to obtain the response.
         *
         * > **NOTE**
         * >
         * > - Always verify the validity period of the OCSP response against the current system time, and allow a time
         * > tolerance of ±5 minutes.
         * > - The validity period of the OCSP signature certificate chain is always verified using the current system time.
         * > - Allows ocsp response to be missing nonce and nextUpdate.
         *
         * @syscap SystemCapability.Security.Cert
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        CERT_REVOCATION_OCSP_CHECK = 2,
        /**
         * Checks the revocation status of all certificates.
         *
         * - If this flag is set, revocation check is performed on all certificates in the certificate chain
         * (skips self-signed certificates);
         * - If this flag is not set, only the end-entity certificate (the first certificate in the certificate chain) is
         * checked.
         *
         * @syscap SystemCapability.Security.Cert
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        CERT_REVOCATION_CHECK_ALL_CERT = 3
    }
    /**
     * Enumerates the OCSP digest algorithm.
     *
     * @syscap SystemCapability.Security.Cert
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    enum OcspDigest {
        /**
         * SHA1 digest algorithm.
         *
         * @syscap SystemCapability.Security.Cert
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        SHA1 = 0,
        /**
         * SHA224 digest algorithm.
         *
         * @syscap SystemCapability.Security.Cert
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        SHA224 = 1,
        /**
         * SHA256 digest algorithm.
         *
         * @syscap SystemCapability.Security.Cert
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        SHA256 = 2,
        /**
         * SHA384 digest algorithm.
         *
         * @syscap SystemCapability.Security.Cert
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        SHA384 = 3,
        /**
         * SHA512 digest algorithm.
         *
         * @syscap SystemCapability.Security.Cert
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        SHA512 = 4
    }
    /**
     * Parameters for checking certificate revocation status.
     *
     * @syscap SystemCapability.Security.Cert
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    interface X509CertRevokedParams {
        /**
         * Revocation check flag. Array length range: [1,4]. The array must contain either CERT_REVOCATION_CRL_CHECK or
         * CERT_REVOCATION_OCSP_CHECK.
         *
         * @syscap SystemCapability.Security.Cert
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        revocationFlags: Array<CertRevocationFlag>;
        /**
         * CRL list. Maximum count: 100.
         *
         * @syscap SystemCapability.Security.Cert
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        crls?: Array<X509CRL>;
        /**
         * Indicates whether to allow CRL download. The default value is false. true: The CDP extension of the certificate
         * is used to download the CRL. false: Do not attempt to download the CRL.
         *
         * > **NOTE**
         * >
         * > Skip download if matching CRL exists in crls.
         *
         * @default false
         * @syscap SystemCapability.Security.Cert
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        allowDownloadCrl?: boolean;
        /**
         * Preconfigured OCSP response data. Maximum count: 100.
         *
         * @syscap SystemCapability.Security.Cert
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        ocspResponses?: Array<Uint8Array>;
        /**
         * Indicates whether to allow online OCSP check. The default value is false.
         * - **true**: performs online OCSP check, that is, attempts to obtain the OCSP URL from the AIA extension of the
         * certificate and send a request to obtain a response;
         * - **false**: does not perform online OCSP check.
         *
         * > **NOTE**
         * >
         * > Skip online OCSP check if a matching OCSP response is found in ocspResponses.
         *
         * @default false
         * @syscap SystemCapability.Security.Cert
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        allowOcspCheckOnline?: boolean;
        /**
         * Digest algorithm used by OCSP requests. The default value is SHA256.
         *
         * @default SHA256
         * @syscap SystemCapability.Security.Cert
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        ocspDigest?: OcspDigest;
    }
    /**
     * Parameters for certificate validation.
     *
     * @syscap SystemCapability.Security.Cert
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    interface CertValidationParams {
        /**
         * Indicates the list of untrusted certificates. An intermediate certificate is used only to construct a certificate
         * chain and is not used as a trust anchor. Maximum count: 100.
         *
         * @syscap SystemCapability.Security.Cert
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        untrustedCerts?: Array<X509Cert>;
        /**
         * Trust certificate list. Specifies the trusted root certificate or intermediate CA certificate as the trust anchor
         * for validation. Maximum count: 100.
         * <br>During verification, the certificate chain must trace back to a trusted certificate. You must set this
         * parameter or set trustSystemCa to true.
         *
         * @syscap SystemCapability.Security.Cert
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        trustedCerts?: Array<X509Cert>;
        /**
         * Whether to trust the system CA. The default value is **false**.
         * - **true**: uses the system preset CA certificate library as a trust anchor;
         * - **false**: does not use the system preset CA certificate library as a trust anchor.
         *
         * @default false
         * @syscap SystemCapability.Security.Cert
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        trustSystemCa?: boolean;
        /**
         * Whether to allow partial chain validation. The default value is **false**.
         * - **true**: any certificate in the trusted certificates can be used as the trust anchor instead of the root
         * certificate;
         * - **false**: the root certificate must be traced during certificate chain construction.
         *
         * @default false
         * @syscap SystemCapability.Security.Cert
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        partialChain?: boolean;
        /**
         * Whether to allow intermediate CA certificates to be downloaded from the network. The default value is **false**.
         * - **true**: attempts to use the issuer address in the certificate AIA extension to download the issuer
         * certificate when an intermediate certificate is missing in the certificate chain, resolving the incomplete
         * certificate chain issue;
         * - **false**: intermediate CA certificates cannot be downloaded from the network.
         * <br>The download address is obtained from the certificate AIA extension. Only HTTP is supported. To use the
         * network for download, you need to request the **ohos.permission.INTERNET** permission. For details about the
         * permission configuration, see [Declaring Permissions](docroot://security/AccessToken/declare-permissions.md).
         *
         * @default false
         * @syscap SystemCapability.Security.Cert
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        allowDownloadIntermediateCa?: boolean;
        /**
         * Validation date, in the format of YYMMDDHHMMSSZ or YYYYMMDDHHMMSSZ. By default, the current system time is
         * used.
         * <br>Custom verification time is supported, which is applicable to scenarios such as offline verification of
         * historical signatures.
         *
         * @syscap SystemCapability.Security.Cert
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        date?: string;
        /**
         * Indicates whether to verify the date. true: Verify the validity period of the certificate and CRL. false: The
         * validity period of the certificate and CRL is not verified.
         *
         * @default true
         * @syscap SystemCapability.Security.Cert
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        validateDate?: boolean;
        /**
         * Allows specific validation errors to be ignored. Maximum count: 8.
         * <br>The errors that can be ignored include: ERR_CERT_NOT_YET_VALID, ERR_CERT_HAS_EXPIRED,
         * ERR_UNKNOWN_CRITICAL_EXTENSION, ERR_CRL_NOT_FOUND, ERR_CRL_NOT_YET_VALID, ERR_CRL_HAS_EXPIRED,
         * ERR_OCSP_RESPONSE_NOT_FOUND, ERR_NETWORK_TIMEOUT.
         *
         * @syscap SystemCapability.Security.Cert
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        ignoreErrs?: Array<CertResult>;
        /**
         * List of hostnames. Verify that the certificate's subject alternative name (SAN) or common name (CN) contains the
         * specified hostname. Maximum number: 100; maximum length of each host name: 128.
         * <br>Verification is successful as long as one of the hostnames is matched.
         *
         * @syscap SystemCapability.Security.Cert
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        hostnames?: Array<string>;
        /**
         * Email address list. Verify that the certificate contains the specified email address. The maximum number is 1.
         * The maximum length of the email address is 128.
         *
         * @syscap SystemCapability.Security.Cert
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        emailAddresses?: Array<string>;
        /**
         * Key usage list. Verify that the certificate's key usage extension includes the specified usage.
         * Maximum count: 9.
         * <br>The certificate must contain all specified key usages for verification to be successful.
         *
         * @syscap SystemCapability.Security.Cert
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        keyUsage?: Array<KeyUsageType>;
        /**
         * User ID. Used to set the user identifier required for signature verification when verifying the SM2 certificate.
         * Maximum length: 128 characters.
         * <br>The most commonly used value in the SM2 certificate scenario is
         * [0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38].
         * (The corresponding ASCII character string is 1234567812345678, 16 bytes.)
         * Certificate revocation check is not supported after userId is set.
         *
         * @syscap SystemCapability.Security.Cert
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        userId?: Uint8Array;
        /**
         * Indicates the certificate revocation check parameter. Used to check whether a certificate is revoked. The
         * configuration includes the CRL list, OCSP response data, and whether online check is allowed.
         *
         * @syscap SystemCapability.Security.Cert
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        revokedParams?: X509CertRevokedParams;
    }
    /**
     * Result of certificate validation.
     *
     * @syscap SystemCapability.Security.Cert
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    interface CertValidationResult {
        /**
         * Indicates the authenticated certificate chain. Upon successful authentication, the complete certificate chain is
         * returned, from the end-entity certificate to the trust anchor. It can be used for subsequent certificate
         * information query or other verification operations.
         *
         * @syscap SystemCapability.Security.Cert
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        readonly certChain: Array<X509Cert>;
    }
    /**
     * Provides APIs for certificate chain validator operations.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform [since 11]
     * @atomicservice [since 12]
     * @since 9
     */
    interface CertChainValidator {
        /**
         * Validates an X.509 certificate chain. This API uses an asynchronous callback to return the result.
         *
         * <br>Because the system time on the device is untrusted, the certificate chain validator does not verify the
         * certificate validity period. To check the validity period of a certificate, use the
         * [checkValidityWithDate()]{@link cert.X509Cert.checkValidityWithDate} API of the **X509Cert** class. For details
         * about certificate specifications, see
         * [Certificate Specifications](docroot://security/DeviceCertificateKit/certificate-framework-overview.md#certificate-specifications)
         * .
         *
         * @param { CertChainData } certChain - Serialized X.509 certificate chain data.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @throws { BusinessError } 19030002 - The certificate signature verification failed.
         * @throws { BusinessError } 19030003 - The certificate has not taken effect.
         * @throws { BusinessError } 19030004 - The certificate has expired.
         * @throws { BusinessError } 19030005 - Failed to obtain the certificate issuer.
         * @throws { BusinessError } 19030006 - The key cannot be used for signing a certificate.
         * @throws { BusinessError } 19030007 - The key cannot be used for a digital signature.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        validate(certChain: CertChainData, callback: AsyncCallback<void>): void;
        /**
         * Validates an X.509 certificate chain. This API uses a promise to return the result.
         *
         * <br>Because the system time on the device is untrusted, the certificate chain validator does not verify the
         * certificate validity period. To check the validity period of a certificate, use the
         * [checkValidityWithDate()]{@link cert.X509Cert.checkValidityWithDate} API of the **X509Cert** class. For details
         * about certificate specifications, see
         * [Certificate Specifications](docroot://security/DeviceCertificateKit/certificate-framework-overview.md#certificate-specifications)
         * .
         *
         * @param { CertChainData } certChain - Serialized X.509 certificate chain data.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @throws { BusinessError } 19030002 - The certificate signature verification failed.
         * @throws { BusinessError } 19030003 - The certificate has not taken effect.
         * @throws { BusinessError } 19030004 - The certificate has expired.
         * @throws { BusinessError } 19030005 - Failed to obtain the certificate issuer.
         * @throws { BusinessError } 19030006 - The key cannot be used for signing a certificate.
         * @throws { BusinessError } 19030007 - The key cannot be used for a digital signature.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        validate(certChain: CertChainData): Promise<void>;
        /**
         * Validates a certificate by building and verifying its certificate chain. This API uses a promise to return the
         * result.
         *
         * <br>The certificate chain construction process complies with the following rules:
         * 1. Trusted anchor source: The trusted certificate list (trustedCerts) is always used as the trust anchor source.
         * The preconfigured certificate is used as the trust anchor source only when trustSystemCa is set to true.
         * 2. Issuer search sequence: The system searches for the issuer from the trust anchor source first. If the issuer
         * cannot be found, the system searches for the issuer in the untrusted certificate list (untrustedCerts). The
         * intermediate CA certificate downloaded online is an untrusted certificate.
         * 3. Trust anchor locking: Once the issuer is found in the trust anchor source, the subsequent lookup process does
         * not roll back to the untrusted certificate, that is, the subsequent certificates must come from the trust anchor
         * source.
         * 4. Construction completion conditions:
         * If partialChain is false (default value), the build is complete only when the root certificate (self-signed
         * certificate) is found.
         * If partialChain is true, the first time the issuer is found in the trust anchor source, the build is complete.
         * 5. Follow-up verification: After the certificate chain is constructed, perform other verification operations,
         * such as certificate signature verification and certificate revocation check.
         *
         * @param { X509Cert } cert - Certificate to verify.
         * @param { CertValidationParams } params - Certificate validation parameters.
         * @returns { Promise<CertValidationResult> } Promise used to return the result of certificate validation.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19020003 - Parameter check failed.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @throws { BusinessError } 19030002 - The certificate signature verification failed.
         * @throws { BusinessError } 19030003 - The certificate has not taken effect.
         * @throws { BusinessError } 19030004 - The certificate has expired.
         * @throws { BusinessError } 19030005 - Failed to obtain the certificate issuer.
         * @throws { BusinessError } 19030006 - The key cannot be used for signing a certificate.
         * @throws { BusinessError } 19030007 - The key cannot be used for a digital signature.
         * @throws { BusinessError } 19030009 - Untrusted certificate.
         * @throws { BusinessError } 19030010 - The certificate has been revoked.
         * @throws { BusinessError } 19030011 - Unsupported critical extension.
         * @throws { BusinessError } 19030012 - Hostname mismatch in the certificate.
         * @throws { BusinessError } 19030013 - Email address mismatch in the certificate.
         * @throws { BusinessError } 19030014 - Key usage mismatch in the certificate.
         * @throws { BusinessError } 19030015 - Failed to obtain the certificate revocation list.
         * @throws { BusinessError } 19030016 - The certificate revocation list has not taken effect.
         * @throws { BusinessError } 19030017 - The certificate revocation list has expired.
         * @throws { BusinessError } 19030018 - Failed to verify the signature of the certificate revocation list.
         * @throws { BusinessError } 19030019 - Failed to find the issuer of the certificate revocation list.
         * @throws { BusinessError } 19030020 - Failed to obtain the OCSP response.
         * @throws { BusinessError } 19030021 - Invalid OCSP response.
         * @throws { BusinessError } 19030022 - Failed to verify the OCSP signature.
         * @throws { BusinessError } 19030023 - Unknown OCSP certificate status.
         * @throws { BusinessError } 19030024 - Network connection timed out.
         * @syscap SystemCapability.Security.Cert
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        validateCert(cert: X509Cert, params: CertValidationParams): Promise<CertValidationResult>;
        /**
         * Algorithm used by the X.509 certificate chain validator.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform [since 11]
         * @atomicservice [since 12]
         * @since 9
         */
        readonly algorithm: string;
    }
    /**
     * Creates a **CertChainValidator** object.
     *
     * @param { string } algorithm - Certificate chain validator algorithm. Currently, only **PKIX** is supported.
     * @returns { CertChainValidator } **CertChainValidator** object created.
     * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
     *     <br>1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types;
     *     <br>3. Parameter verification failed.
     * @throws { BusinessError } 801 - This operation is not supported.
     * @throws { BusinessError } 19020001 - Memory malloc failed.
     * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
     *     <br>1. Memory copy failed;
     *     <br>2. A null pointer occurs inside the system;
     *     <br>3. Failed to obtain the native object or convert parameters.
     * @throws { BusinessError } 19030001 - Crypto operation error.
     * @syscap SystemCapability.Security.Cert
     * @crossplatform [since 11]
     * @atomicservice [since 12]
     * @since 9
     */
    function createCertChainValidator(algorithm: string): CertChainValidator;
    /**
     * Enumerates the types of GeneralName as defined in X.509, which can appear in Subject Alternative Name and other
     * extensions.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    enum GeneralNameType {
        /**
         * Indicates an otherName.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        GENERAL_NAME_TYPE_OTHER_NAME = 0,
        /**
         * Indicates an email address.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        GENERAL_NAME_TYPE_RFC822_NAME = 1,
        /**
         * Indicates a DNS name.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        GENERAL_NAME_TYPE_DNS_NAME = 2,
        /**
         * Indicates an X.400 address.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        GENERAL_NAME_TYPE_X400_ADDRESS = 3,
        /**
         * Indicates a directory name.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        GENERAL_NAME_TYPE_DIRECTORY_NAME = 4,
        /**
         * Indicates an Electronic Data Interchange (EDI) entity.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        GENERAL_NAME_TYPE_EDI_PARTY_NAME = 5,
        /**
         * Indicates a uniform resource identifier.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        GENERAL_NAME_TYPE_UNIFORM_RESOURCE_ID = 6,
        /**
         * Indicates an IP address.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        GENERAL_NAME_TYPE_IP_ADDRESS = 7,
        /**
         * Indicates a registered object identifier.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        GENERAL_NAME_TYPE_REGISTERED_ID = 8
    }
    /**
     * Represents an X.509 GeneralName as defined in RFC 5280, which can appear in Subject Alternative Name and other
     * extensions.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    interface GeneralName {
        /**
         * Type of the GeneralName.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        type: GeneralNameType;
        /**
         * DER-encoded value of the GeneralName.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        name?: Uint8Array;
    }
    /**
     * Defines the parameters used to match a certificate. If no parameter is specified, all certificates are matched.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice [since 12]
     * @since 11
     */
    interface X509CertMatchParameters {
        /**
         * Subject Alternative Names (SANs) of the certificate.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        subjectAlternativeNames?: Array<GeneralName>;
        /**
         * Whether to match all SANs of the certificate. **true**: yes; **false**: no.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        matchAllSubjectAltNames?: boolean;
        /**
         * Key of the certificate authority (CA).
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        authorityKeyIdentifier?: Uint8Array;
        /**
         * Minimum length of the certification path (chain of trust) that can be built from the certificate to a trusted
         * root CA.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        minPathLenConstraint?: number;
        /**
         * Certificate object.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        x509Cert?: X509Cert;
        /**
         * Certificate validity period.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        validDate?: string;
        /**
         * Certificate issuer, in DER format.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        issuer?: Uint8Array;
        /**
         * Extended key usage.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        extendedKeyUsage?: Array<string>;
        /**
         * Constraints on the subject names that can be included in certificates.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        nameConstraints?: Uint8Array;
        /**
         * Certificate policy.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        certPolicy?: Array<string>;
        /**
         * Validity period of the certificate private key.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        privateKeyValid?: string;
        /**
         * Whether to match the key usage. **true**: yes; **false**: no.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        keyUsage?: Array<boolean>;
        /**
         * Serial number of the certificate.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        serialNumber?: bigint;
        /**
         * Certificate subject name, in DER format.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        subject?: Uint8Array;
        /**
         * Identifier of the public key of the certificate's subject.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        subjectKeyIdentifier?: Uint8Array;
        /**
         * Public key of the certificate, in DER format.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        publicKey?: DataBlob;
        /**
         * Algorithm of the certificate public key.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        publicKeyAlgID?: string;
        /**
         * Specifies the certificate private key. string indicates a private key in PEM format, and Uint8Array indicates a
         * private key in DER format.
         *
         * @syscap SystemCapability.Security.Cert
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        privateKey?: string | Uint8Array;
    }
    /**
     * Represents the parameters used to match a certificate revocation list (CRL). If no parameter is specified, all CRLs
     * are matched.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice [since 12]
     * @since 11
     */
    interface X509CRLMatchParameters {
        /**
         * CRL issuer, in DER format.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        issuer?: Array<Uint8Array>;
        /**
         * Certificate object.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        x509Cert?: X509Cert;
        /**
         * CRL update time.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        updateDateTime?: string;
        /**
         * Maximum value of the CRL number.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        maxCRL?: bigint;
        /**
         * Minimum value of the CRL number.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        minCRL?: bigint;
    }
    /**
     * Provides APIs for locating certificates or CRLs in a **CertCRLCollection** object.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice [since 12]
     * @since 11
     */
    interface CertCRLCollection {
        /**
         * Selects certificates that match the specified parameters. This API uses a promise to return the result.
         *
         * @param { X509CertMatchParameters } param - Parameters used to match the certificates.
         * @returns { Promise<Array<X509Cert>> } Promise used to return the matched certificates.
         * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        selectCerts(param: X509CertMatchParameters): Promise<Array<X509Cert>>;
        /**
         * Selects certificates that match the specified parameters. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { X509CertMatchParameters } param - Parameters used to match the certificates.
         * @param { AsyncCallback<Array<X509Cert>> } callback - Callback used to return the result. If the operation is
         *     successful, **err** is **undefined**, and **data** is the matched certificates obtained. Otherwise, **err**
         *     is an error object.
         * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        selectCerts(param: X509CertMatchParameters, callback: AsyncCallback<Array<X509Cert>>): void;
        /**
         * Selects CRLs that match the specified parameters. This API uses a promise to return the result.
         *
         * @param { X509CRLMatchParameters } param - Parameters used to match the CRLs.
         * @returns { Promise<Array<X509CRL>> } Promise used to return the matched CRLs.
         * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        selectCRLs(param: X509CRLMatchParameters): Promise<Array<X509CRL>>;
        /**
         * Selects CRLs that match the specified parameters. This API uses an asynchronous callback to return the result.
         *
         * @param { X509CRLMatchParameters } param - Parameters used to match the CRLs.
         * @param { AsyncCallback<Array<X509CRL>> } callback - Callback used to return the result. If the operation is
         *     successful, **err** is **undefined**, and **data** is the matched CRLs obtained. Otherwise, **err** is an
         *     error object.
         * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        selectCRLs(param: X509CRLMatchParameters, callback: AsyncCallback<Array<X509CRL>>): void;
    }
    /**
     * Creates an object for a collection of X.509 certificates and CRLs.
     *
     * @param { Array<X509Cert> } certs - X.509 certificates.
     * @param { Array<X509CRL> } [options] crls - Array of X509CRL. [since 11 - 11]
     * @param { Array<X509CRL> } [crls] - Array of X509CRL.
     * @returns { CertCRLCollection } **CertCRLCollection** object created.
     * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
     *     <br>1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types;
     *     <br>3. Parameter verification failed.
     * @throws { BusinessError } 19020001 - Memory malloc failed.
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice [since 12]
     * @since 11
     */
    function createCertCRLCollection(certs: Array<X509Cert>, crls?: Array<X509CRL>): CertCRLCollection;
    /**
     * Provides APIs for managing the X.509 certificate chain.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice [since 12]
     * @since 11
     */
    interface X509CertChain {
        /**
         * Obtains the X.509 certificate list.
         *
         * @returns { Array<X509Cert> } X.509 certificate list obtained.
         * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        getCertList(): Array<X509Cert>;
        /**
         * Validates a certificate chain. This API uses a promise to return the result.
         *
         * @param { CertChainValidationParameters } param - Parameters for validating the X.509 certificate chain.
         * @returns { Promise<CertChainValidationResult> } Promise used to return the certificate chain validation result.
         * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @throws { BusinessError } 19030002 - The certificate signature verification failed.
         * @throws { BusinessError } 19030003 - The certificate has not taken effect.
         * @throws { BusinessError } 19030004 - The certificate has expired.
         * @throws { BusinessError } 19030005 - Failed to obtain the certificate issuer.
         * @throws { BusinessError } 19030006 - The key cannot be used for signing a certificate.
         * @throws { BusinessError } 19030007 - The key cannot be used for a digital signature.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        validate(param: CertChainValidationParameters): Promise<CertChainValidationResult>;
        /**
         * Validates a certificate chain. This API uses an asynchronous callback to return the result.
         *
         * @param { CertChainValidationParameters } param - Parameters for validating the X.509 certificate chain.
         * @param { AsyncCallback<CertChainValidationResult> } callback - Callback used to return the result. If the operation
         *     is successful, **err** is **undefined**, and **data** is the certificate chain validation result obtained.
         *     Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @throws { BusinessError } 19030002 - The certificate signature verification failed.
         * @throws { BusinessError } 19030003 - The certificate has not taken effect.
         * @throws { BusinessError } 19030004 - The certificate has expired.
         * @throws { BusinessError } 19030005 - Failed to obtain the certificate issuer.
         * @throws { BusinessError } 19030006 - The key cannot be used for signing a certificate.
         * @throws { BusinessError } 19030007 - The key cannot be used for a digital signature.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        validate(param: CertChainValidationParameters, callback: AsyncCallback<CertChainValidationResult>): void;
        /**
         * Converts the object data into a string.
         *
         * @returns { string } String obtained.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        toString(): string;
        /**
         * Obtains the hash value of the data in DER format.
         *
         * @returns { Uint8Array } Hash value obtained.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        hashCode(): Uint8Array;
    }
    /**
     * Creates an **X509CertChain** instance. This API uses a promise to return the result.
     *
     * @param { EncodingBlob } inStream - X.509 certificate serialization data.
     * @returns { Promise<X509CertChain> } Promise used to return the **X509CertChain** instance created.
     * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
     *     <br>1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types;
     *     <br>3. Parameter verification failed.
     * @throws { BusinessError } 19020001 - Memory malloc failed.
     * @throws { BusinessError } 19030001 - Crypto operation error.
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice [since 12]
     * @since 11
     */
    function createX509CertChain(inStream: EncodingBlob): Promise<X509CertChain>;
    /**
     * Creates an **X509CertChain** instance. This API uses an asynchronous callback to return the result.
     *
     * @param { EncodingBlob } inStream - X.509 certificate serialization data.
     * @param { AsyncCallback<X509CertChain> } callback - Callback used to return the result. If the operation is
     *     successful, **err** is **undefined**, and **data** is the **X509CertChain** instance created. Otherwise,
     *     **err** is an error object.
     * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
     *     <br>1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types;
     *     <br>3. Parameter verification failed.
     * @throws { BusinessError } 19020001 - Memory malloc failed.
     * @throws { BusinessError } 19030001 - Crypto operation error.
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice [since 12]
     * @since 11
     */
    function createX509CertChain(inStream: EncodingBlob, callback: AsyncCallback<X509CertChain>): void;
    /**
     * Creates an X.509 certificate chain object based on the specified certificates. This API returns the result
     * synchronously.
     *
     * @param { Array<X509Cert> } certs - Array of X.509 certificates.
     * @returns { X509CertChain } **X509CertChain** object created.
     * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
     *     <br>1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types;
     *     <br>3. Parameter verification failed.
     * @throws { BusinessError } 19020001 - Memory malloc failed.
     * @throws { BusinessError } 19030001 - Crypto operation error.
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice [since 12]
     * @since 11
     */
    function createX509CertChain(certs: Array<X509Cert>): X509CertChain;
    /**
     * Builds an X.509 certificate chain with a CertChainBuildParameters object. This API uses a promise to return the
     * result.
     *
     * @param { CertChainBuildParameters } param - Object used to build the certificate chain.<br> The value of
     *     **maxLength** in [CertChainBuildParameters]{@link cert.CertChainBuildParameters} must be less than the number
     *     of certificates in the certificate set.
     * @returns { Promise<CertChainBuildResult> } Promise used to return the **CertChainBuildResult** object created.
     * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
     *     <br>1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types;
     *     <br>3. Parameter verification failed.
     * @throws { BusinessError } 19020001 - Memory malloc failed.
     * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
     *     <br>1. Memory copy failed;
     *     <br>2. A null pointer occurs inside the system;
     *     <br>3. Failed to obtain the native object or convert parameters.
     * @throws { BusinessError } 19030001 - Crypto operation error.
     * @throws { BusinessError } 19030002 - The certificate signature verification failed.
     * @throws { BusinessError } 19030003 - The certificate has not taken effect.
     * @throws { BusinessError } 19030004 - The certificate has expired.
     * @throws { BusinessError } 19030005 - Failed to obtain the certificate issuer.
     * @throws { BusinessError } 19030006 - The key cannot be used for signing a certificate.
     * @throws { BusinessError } 19030007 - The key cannot be used for a digital signature.
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    function buildX509CertChain(param: CertChainBuildParameters): Promise<CertChainBuildResult>;
    /**
     * Enumerates the encoding formats for certificate-related data.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    enum EncodingBaseFormat {
        /**
         * Privacy-Enhanced Mail (PEM) format.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        PEM = 0,
        /**
         * Distinguished Encoding Rules (DER) format.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        DER = 1
    }
    /**
     * P12(PKCS #12) data, which includes private key, certificate, and other certificates.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    interface Pkcs12Data {
        /**
         * Private key. **string** corresponds to PEM format, and **Uint8Array** corresponds to DER format.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        privateKey?: string | Uint8Array;
        /**
         * The certificate that matches the private key.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        cert?: X509Cert;
        /**
         * Other certificates.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        otherCerts?: Array<X509Cert>;
    }
    /**
     * Represents the configuration for parsing P12.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    interface Pkcs12ParsingConfig {
        /**
         * Password.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        password: string;
        /**
         * Whether to obtain the private key. The default value is **true**.
         *
         * **true**: To obtain the private key in PKCS #8 format; **false**: Not to obtain the private key.
         *
         * @default true
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        needsPrivateKey?: boolean;
        /**
         * Format of the private key to be obtained. Currently, the PEM and DER formats are supported. If this parameter is
         * not specified, the PEM format is used by default.
         *
         * > **NOTE**
         * >
         * > This parameter is valid only when **needsPrivateKey** is set to **true**.
         *
         * @default EncodingBaseFormat.PEM
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        privateKeyFormat?: EncodingBaseFormat;
        /**
         * Whether to obtain the certificate. The default value is **true**. **true**: yes; **false**: no.
         *
         * @default true
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        needsCert?: boolean;
        /**
         * Whether to obtain other certificates. The default value is **false**. **true**: yes; **false**: no.
         *
         * @default false
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        needsOtherCerts?: boolean;
    }
    /**
     * Parses P12.
     *
     * @param { Uint8Array } data - Raw data of P12 file, in DER format.
     * @param { Pkcs12ParsingConfig } config - Configuration for parsing the P12.
     * @returns { Pkcs12Data } Indicates the parsed P12 data.
     * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
     *     <br>1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types;
     *     <br>3. Parameter verification failed.
     * @throws { BusinessError } 19020001 - Memory malloc failed.
     * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
     *     <br>1. Memory copy failed;
     *     <br>2. A null pointer occurs inside the system;
     *     <br>3. Failed to obtain the native object or convert parameters.
     * @throws { BusinessError } 19030001 - Crypto operation error.
     * @throws { BusinessError } 19030008 - Maybe wrong password.
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    function parsePkcs12(data: Uint8Array, config: Pkcs12ParsingConfig): Pkcs12Data;
    /**
     * Parses P12. This API uses a promise to return the result.
     *
     * @param { Uint8Array } data - Raw data of P12 file, in DER format.
     * @param { string } password - Password.
     * @returns { Promise<Pkcs12Data> } Promise used to return the parsed P12 data. The private key in the returned
     *     **Pkcs12Data** is encoded in PEM format.
     * @throws { BusinessError } 19020001 - Memory malloc failed.
     * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
     *     <br>1. Memory copy failed;
     *     <br>2. A null pointer occurs inside the system;
     *     <br>3. Failed to obtain the native object or convert parameters.
     * @throws { BusinessError } 19020003 - Parameter check failed. Possible causes:
     *     <br>1. The length of the data is zero or too large;
     *     <br>2. The length of the password is too large.
     * @throws { BusinessError } 19030001 - Crypto operation error.
     * @throws { BusinessError } 19030008 - Maybe wrong password.
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice
     * @since 21
     */
    function parsePkcs12(data: Uint8Array, password: string): Promise<Pkcs12Data>;
    /**
     * Creates a [TrustAnchor]{@link cert.X509TrustAnchor} object array by using the CA certificate parsed from a .p12
     * keystore file. This API uses a promise to return the result.
     *
     * @param { Uint8Array } keystore - Raw data of P12 file, in DER format.
     * @param { string } pwd - Password.
     * @returns { Promise<Array<X509TrustAnchor>> } Promise used to return the **X509TrustAnchor** object array created.
     * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
     *     <br>1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types;
     *     <br>3. Parameter verification failed.
     * @throws { BusinessError } 19020001 - Memory malloc failed.
     * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
     *     <br>1. Memory copy failed;
     *     <br>2. A null pointer occurs inside the system;
     *     <br>3. Failed to obtain the native object or convert parameters.
     * @throws { BusinessError } 19030001 - Crypto operation error.
     * @throws { BusinessError } 19030002 - The certificate signature verification failed.
     * @throws { BusinessError } 19030003 - The certificate has not taken effect.
     * @throws { BusinessError } 19030004 - The certificate has expired.
     * @throws { BusinessError } 19030005 - Failed to obtain the certificate issuer.
     * @throws { BusinessError } 19030006 - The key cannot be used for signing a certificate.
     * @throws { BusinessError } 19030007 - The key cannot be used for a digital signature.
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    function createTrustAnchorsWithKeyStore(keystore: Uint8Array, pwd: string): Promise<Array<X509TrustAnchor>>;
    /**
     * Creates an **X500DistinguishedName** object with a name in the form of a string. This API uses a promise to return
     * the result.
     *
     * @param { string } nameStr - Name in a slash-separated format, each relative distinguished name is in the format of
     *     **attribute=value**. Common attributes include **CN** (common name), **O** (organization name),
     *     **OU** (organization unit), **C** (country/region), **ST** (province/state), and **L** (city/district).
     *     For example, **\/CN=example.com/O=Example/C=CN**.
     * @returns { Promise<X500DistinguishedName> } Promise used to return the **X500DistinguishedName** object created.
     * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
     *     <br>1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types;
     *     <br>3. Parameter verification failed.
     * @throws { BusinessError } 19020001 - Memory malloc failed.
     * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
     *     <br>1. Memory copy failed;
     *     <br>2. A null pointer occurs inside the system;
     *     <br>3. Failed to obtain the native object or convert parameters.
     * @throws { BusinessError } 19030001 - Crypto operation error.
     * @throws { BusinessError } 19030002 - The certificate signature verification failed.
     * @throws { BusinessError } 19030003 - The certificate has not taken effect.
     * @throws { BusinessError } 19030004 - The certificate has expired.
     * @throws { BusinessError } 19030005 - Failed to obtain the certificate issuer.
     * @throws { BusinessError } 19030006 - The key cannot be used for signing a certificate.
     * @throws { BusinessError } 19030007 - The key cannot be used for a digital signature.
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    function createX500DistinguishedName(nameStr: string): Promise<X500DistinguishedName>;
    /**
     * Creates an **X500DistinguishedName** object with a name in DER format. This API uses a promise to return the
     * result.
     *
     * @param { Uint8Array } nameDer - X.500 Distinguished Name in DER format.
     * @returns { Promise<X500DistinguishedName> } Promise used to return the **X500DistinguishedName** object created.
     * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
     *     <br>1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types;
     *     <br>3. Parameter verification failed.
     * @throws { BusinessError } 19020001 - Memory malloc failed.
     * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
     *     <br>1. Memory copy failed;
     *     <br>2. A null pointer occurs inside the system;
     *     <br>3. Failed to obtain the native object or convert parameters.
     * @throws { BusinessError } 19030001 - Crypto operation error.
     * @throws { BusinessError } 19030002 - The certificate signature verification failed.
     * @throws { BusinessError } 19030003 - The certificate has not taken effect.
     * @throws { BusinessError } 19030004 - The certificate has expired.
     * @throws { BusinessError } 19030005 - Failed to obtain the certificate issuer.
     * @throws { BusinessError } 19030006 - The key cannot be used for signing a certificate.
     * @throws { BusinessError } 19030007 - The key cannot be used for a digital signature.
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    function createX500DistinguishedName(nameDer: Uint8Array): Promise<X500DistinguishedName>;
    /**
     * Provides APIs for X.500 distinguished name operations.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    interface X500DistinguishedName {
        /**
         * Obtains the DN in the form of a string.
         *
         * @returns { string } DN obtained as a string.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        getName(): string;
        /**
         * Obtains RDN strings based on the specified encoding format.
         *
         * @param { EncodingType } encodingType - Encoding format.
         * @returns { string } RDN string. Multiple strings are separated by commas (,).
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19020003 - Parameter check failed. Possible causes:
         *     <br>1. The value of encodingType is not in the EncodingType enumeration range.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        getName(encodingType: EncodingType): string;
        /**
         * Obtains relative distinguished name (RDN) strings of the specified type.
         *
         * @param { string } type - Type of the RDNs to obtain. For example, **CN** and **OU**.
         * @returns { Array<string> } Array of RDN strings.
         * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        getName(type: string): Array<string>;
        /**
         * Obtains an array of RDN strings based on the specified type and encoding format.
         *
         * @param { string } type - Type of the RDNs to obtain. For example, **CN** and **OU**.
         * @param { EncodingType } encodingType - Encoding format.
         * @returns { Array<string> } Array of RDN strings.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19020003 - Parameter check failed. Possible causes:
         *     <br>1. The value of encodingType is invalid.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        getName(type: string, encodingType: EncodingType): Array<string>;
        /**
         * Obtains the DER-encoded data of the X.500 Distinguished Name.
         *
         * @returns { EncodingBlob } DER-encoded X.500 Distinguished Name data obtained.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        getEncoded(): EncodingBlob;
    }
    /**
     * Represents an X.509 trust anchor, which is used to verify the certificate chain. The certificate or public key in
     * the trust anchor is used as the trusted root to verify the certificate chain.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice [since 12]
     * @since 11
     */
    interface X509TrustAnchor {
        /**
         * Trusted CA certificate. If **CACert** is set, only **CACert** is used to validate the certificate chain.
         * **CAPubKey** and **CASubject** are not used.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        CACert?: X509Cert;
        /**
         * Public key of the trusted CA certificate, in DER format. This parameter takes effect only when **CACert** is not
         * set.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        CAPubKey?: Uint8Array;
        /**
         * Subject of the trusted CA certificate, in DER format. This parameter takes effect only when **CAPubKey** is set.
         * The validation object is determined based on the **CAPubKey** type (self-signed or upper-level), and can be the
         * subject or issuer of the root certificate.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        CASubject?: Uint8Array;
        /**
         * Name constraints, in DER format. Only the leaf certificate of the current certificate chain is validated.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        nameConstraints?: Uint8Array;
    }
    /**
     * Enumerates the options for checking the certificate revocation status.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    enum RevocationCheckOptions {
        /**
         * Use OCSP over CRL (default).
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        REVOCATION_CHECK_OPTION_PREFER_OCSP = 0,
        /**
         * Obtain the CRL/OCSP response over the network. By default, it is disabled. Only the first CRL distribution point
         * address can be obtained from the CDP extension of the certificate to check the certificate revocation status, or
         * the first OCSP server address can be obtained from the AIA extension of the certificate to check the certificate
         * revocation status. Moreover, only HTTP is supported. You must declare the ohos.permission.INTERNET permission.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        REVOCATION_CHECK_OPTION_ACCESS_NETWORK = 1,
        /**
         * This parameter is valid when the **ACCESS_NETWORK** option is enabled. It allows the alternative solution to be
         * used to obtain the certificate revocation status if the preferred solution cannot be used due to network
         * problems.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        REVOCATION_CHECK_OPTION_FALLBACK_NO_PREFER = 2,
        /**
         * This parameter is valid when the **ACCESS_NETWORK** option is enabled. It allows the locally configured CRL/OCSP
         * response to be used to check the certificate revocation status if the online CRL/OCSP response cannot be used due
         * to network problems.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        REVOCATION_CHECK_OPTION_FALLBACK_LOCAL = 3,
        /**
         * This parameter is valid when the **ACCESS_NETWORK** option is enabled. If this capability is enabled, the system
         * continues to check the revocation status of the intermediate certificate if the OCSP or CRL check of the leaf
         * certificate succeeds. This capability is disabled by default.
         *
         * > **NOTE**
         * >
         * > This capability and **REVOCATION_CHECK_OPTION_LOCAL_CRL_ONLY_CHECK_END_ENTITY_CERT** cannot be enabled at
         * > the same time.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 22
         */
        REVOCATION_CHECK_OPTION_CHECK_INTERMEDIATE_CA_ONLINE = 4,
        /**
         * If this capability is enabled, the system checks the revocation status of the leaf certificate based on the local
         * CRL. This capability is disabled by default.
         *
         * > **NOTE**
         * >
         * > This capability and **REVOCATION_CHECK_OPTION_CHECK_INTERMEDIATE_CA_ONLINE** cannot be enabled at the same
         * > time.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 22
         */
        REVOCATION_CHECK_OPTION_LOCAL_CRL_ONLY_CHECK_END_ENTITY_CERT = 5,
        /**
         * If this capability is enabled, the system ignores the network unreachable error when obtaining the CRL or OCSP
         * response over the network for revocation status check. This capability is disabled by default. By default, the
         * network unreachable error may cause certificate chain validation failure.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 23
         */
        REVOCATION_CHECK_OPTION_IGNORE_NETWORK_ERROR = 6
    }
    /**
     * Enumerates the types of the online certificate chain validation policy.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    enum ValidationPolicyType {
        /**
         * Do not verify **sslHostname** or **dNSName** in the certificate. It is the default value.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        VALIDATION_POLICY_TYPE_X509 = 0,
        /**
         * Verify **sslHostname** or **dNSName** in the certificate.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        VALIDATION_POLICY_TYPE_SSL = 1
    }
    /**
     * Enumerates the purposes for which the key in the certificate is used.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    enum KeyUsageType {
        /**
         * The certificate holder can use the private key contained in the certificate to generate a digital signature.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        KEYUSAGE_DIGITAL_SIGNATURE = 0,
        /**
         * The certificate holder can use the key to create a digital signature as part of a non-repudiation service.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        KEYUSAGE_NON_REPUDIATION = 1,
        /**
         * The certificate holder can use the public key contained in the certificate for key encryption.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        KEYUSAGE_KEY_ENCIPHERMENT = 2,
        /**
         * The certificate holder can use the public key contained in the certificate for data encryption.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        KEYUSAGE_DATA_ENCIPHERMENT = 3,
        /**
         * The certificate holder can use the private key contained in the certificate to perform key agreement operations.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        KEYUSAGE_KEY_AGREEMENT = 4,
        /**
         * The certificate holder can use the private key contained in the certificate to sign other certificates.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        KEYUSAGE_KEY_CERT_SIGN = 5,
        /**
         * The certificate holder can use the private key contained in the certificate to sign CRLs.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        KEYUSAGE_CRL_SIGN = 6,
        /**
         * The certificate holder can use the key to perform encryption operations only.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        KEYUSAGE_ENCIPHER_ONLY = 7,
        /**
         * The certificate holder can use the key to perform decryption operations only.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        KEYUSAGE_DECIPHER_ONLY = 8
    }
    /**
     * Represents the parameters for checking the certificate revocation status for a certificate chain.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    interface RevocationCheckParameter {
        /**
         * OCSP request extensions.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        ocspRequestExtension?: Array<Uint8Array>;
        /**
         * URI of the alternative server used to send OCSP requests. HTTP and HTTPS are supported. The specific
         * configuration is determined via the negotiation with the server.
         *
         * > **NOTE**
         * >
         * > The URI takes effect only for the leaf certificate.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        ocspResponderURI?: string;
        /**
         * Signing certificate used for verifying the signature of the OCSP response.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        ocspResponderCert?: X509Cert;
        /**
         * Alternative OCSP responses.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        ocspResponses?: Uint8Array;
        /**
         * Address used to download the CRLs.
         *
         * > **NOTE**
         * >
         * > The URI takes effect only for the leaf certificate.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        crlDownloadURI?: string;
        /**
         * A set of rules for obtaining the certificate revocation status.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        options?: Array<RevocationCheckOptions>;
        /**
         * Hash algorithm used to create a certificate ID during OCSP communication. The options **MD5**, **SHA1**,
         * **SHA224**, **SHA256**, **SHA384**, and **SHA512** are supported. The default value is **SHA256**.
         *
         * @default SHA256
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        ocspDigest?: string;
    }
    /**
     * Represents the parameters for certificate chain validation.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice [since 12]
     * @since 11
     */
    interface CertChainValidationParameters {
        /**
         * Date for checking certificate validity.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        date?: string;
        /**
         * List of trusted anchors.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        trustAnchors: Array<X509TrustAnchor>;
        /**
         * Whether to use the prebuilt CA certificate to validate the certificate chain. **true** means yes; **false**
         * otherwise.
         *
         * @default false
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        trustSystemCa?: boolean;
        /**
         * Whether to allow the application to download the missing intermediate CA certificate from the network.
         * **true** means yes; **false** otherwise. The default value is **false**.
         * <br>The download address is obtained from the certificate AIA extension. Only HTTP is supported. To use the
         * network for download, you need to request the **ohos.permission.INTERNET** permission. For details about the
         * permission configuration, see [Declaring Permissions](docroot://security/AccessToken/declare-permissions.md).
         *
         * @default false
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 23
         */
        allowDownloadIntermediateCa?: boolean;
        /**
         * CRL collections used to check whether the certificate is revoked.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        certCRLs?: Array<CertCRLCollection>;
        /**
         * Parameters for checking the certificate revocation status.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        revocationCheckParam?: RevocationCheckParameter;
        /**
         * Type of the policy for certificate validation.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        policy?: ValidationPolicyType;
        /**
         * Host name in the certificate to be verified. This parameter must be used together with **policy**.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        sslHostname?: string;
        /**
         * Usage of the key in the certificate to be validated.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        keyUsage?: Array<KeyUsageType>;
    }
    /**
     * Represents the return value of certificate chain validation.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice [since 12]
     * @since 11
     */
    interface CertChainValidationResult {
        /**
         * Trust anchor.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        readonly trustAnchor: X509TrustAnchor;
        /**
         * Entity certificate.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        readonly entityCert: X509Cert;
    }
    /**
     * Represents the parameters for building a certificate chain.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    interface CertChainBuildParameters {
        /**
         * Filter criteria.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        certMatchParameters: X509CertMatchParameters;
        /**
         * Maximum number of CA certificates in the certificate chain.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        maxLength?: number;
        /**
         * Parameters for certificate chain validation.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        validationParameters: CertChainValidationParameters;
    }
    /**
     * Represents the certificate chain build result.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    interface CertChainBuildResult {
        /**
         * Certificate chain object created.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        readonly certChain: X509CertChain;
        /**
         * Result of the certificate chain validation.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        readonly validationResult: CertChainValidationResult;
    }
    /**
     * Enumerates the Cryptographic Message Syntax (CMS) message types.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    enum CmsContentType {
        /**
         * Signed data.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        SIGNED_DATA = 0,
        /**
         * Enveloped data, including authenticated enveloped data.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 22
         */
        ENVELOPED_DATA = 1
    }
    /**
     * Enumerates the CMS message formats.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    enum CmsContentDataFormat {
        /**
         * Binary.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        BINARY = 0,
        /**
         * Text.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        TEXT = 1
    }
    /**
     * Enumerates the CMS encoding formats.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    enum CmsFormat {
        /**
         * Privacy-Enhanced Mail (PEM) format.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        PEM = 0,
        /**
         * Distinguished Encoding Rules (DER) format.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        DER = 1
    }
    /**
     * Represents the private key information.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    interface PrivateKeyInfo {
        /**
         * Encrypted or unencrypted private key in PEM or DER format.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        key: string | Uint8Array;
        /**
         * Password of the private key, if the private key is encrypted.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        password?: string;
    }
    /**
     * Enumerates the RSA CMS signature padding modes.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice
     * @since 22
     */
    enum CmsRsaSignaturePadding {
        /**
         * PKCS #1 padding mode.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 22
         */
        PKCS1_PADDING = 0,
        /**
         * PKCS #1 PSS padding mode.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 22
         */
        PKCS1_PSS_PADDING = 1
    }
    /**
     * Represents the configuration of the CMS signer.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    interface CmsSignerConfig {
        /**
         * Message digest algorithm, for example, **SHA384**. Currently, **SHA1**, **SHA256**, **SHA384**, and **SHA512**
         * are supported.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        mdName: string;
        /**
         * Padding mode for an RSA signature. The default value is **PKCS1_PADDING**.
         * <br>When **PKCS1_PSS_PADDING** is set, **mdName** must be set to **SHA256**, **SHA384**, or
         * **SHA512**.
         *
         * > **NOTE**
         * >
         * > This parameter is valid only when the private key type of the signature is RSA.
         *
         * @default CmsRsaSignaturePadding.PKCS1_PADDING
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 22
         */
        rsaSignaturePadding?: CmsRsaSignaturePadding;
        /**
         * Whether to add a certificate. The default value is **true**. **true**: yes; **false**: no.
         *
         * @default true
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        addCert?: boolean;
        /**
         * Whether to add the signature attribute. The default value is **true**. **true**: yes; **false**: no.
         *
         * @default true
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        addAttr?: boolean;
        /**
         * Whether to add the SMIME capability to the CMS object. The default value is **true**. **true**: yes; **false**:
         * no.
         *
         * @default true
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        addSmimeCapAttr?: boolean;
    }
    /**
     * Enumerates the digest algorithms of the CMS KeyAgree type.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice
     * @since 22
     */
    enum CmsKeyAgreeRecipientDigestAlgorithm {
        /**
         * SHA-256.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 22
         */
        SHA256 = 0,
        /**
         * SHA-384.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 22
         */
        SHA384 = 1,
        /**
         * SHA-512.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 22
         */
        SHA512 = 2
    }
    /**
     * Enumerates the content-encryption algorithms for CMS enveloped data.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice
     * @since 22
     */
    enum CmsRecipientEncryptionAlgorithm {
        /**
         * AES_128_CBC.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 22
         */
        AES_128_CBC = 0,
        /**
         * AES_192_CBC.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 22
         */
        AES_192_CBC = 1,
        /**
         * AES_256_CBC.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 22
         */
        AES_256_CBC = 2,
        /**
         * AES_128_GCM.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 22
         */
        AES_128_GCM = 3,
        /**
         * AES_192_GCM.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 22
         */
        AES_192_GCM = 4,
        /**
         * AES_256_GCM.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 22
         */
        AES_256_GCM = 5
    }
    /**
     * Represents KeyTrans recipient information for CMS enveloped data.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice
     * @since 22
     */
    interface CmsKeyTransRecipientInfo {
        /**
         * RSA certificate.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 22
         */
        cert: X509Cert;
    }
    /**
     * Represents KeyAgree recipient information for CMS enveloped data.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice
     * @since 22
     */
    interface CmsKeyAgreeRecipientInfo {
        /**
         * EC certificate.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 22
         */
        cert: X509Cert;
        /**
         * KDF digest algorithm. The default value is **SHA256**.
         *
         * @default CmsKeyAgreeRecipientDigestAlgorithm.SHA256
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 22
         */
        digestAlgorithm?: CmsKeyAgreeRecipientDigestAlgorithm;
    }
    /**
     * Represents recipient information for the CMS message.
     *
     * > **NOTE**
     * >
     * > At least one recipient needs to be set.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice
     * @since 22
     */
    interface CmsRecipientInfo {
        /**
         * KeyTrans recipient information.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 22
         */
        keyTransInfo?: CmsKeyTransRecipientInfo;
        /**
         * KeyAgree recipient information.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 22
         */
        keyAgreeInfo?: CmsKeyAgreeRecipientInfo;
    }
    /**
     * Represents the configuration for generating a CMS message.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    interface CmsGeneratorOptions {
        /**
         * Format of the content. The default value is **CmsContentDataFormat.BINARY**.
         *
         * @default CmsContentDataFormat.BINARY
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        contentDataFormat?: CmsContentDataFormat;
        /**
         * Format of the CMS message generated. The default value is **DER**.
         *
         * @default CmsFormat.DER
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        outFormat?: CmsFormat;
        /**
         * Whether the final CMS message does not contain the raw data. The default value is **false**. **true**: raw data
         * is not contained; **false**: raw data is contained.
         *
         * @default false
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        isDetached?: boolean;
    }
    /**
     * Provides APIs for generating the messages in CMS format.
     *
     * > **NOTE**
     * >
     * > PKCS #7 is a standard syntax for storing signed or encrypted data. CMS is an extension of PKCS #7. PKCS #7
     * > supports data types including data, signed data, enveloped data, signed and enveloped data, digested
     * > data, and encrypted data. It is often used to protect data integrity and confidentiality.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    interface CmsGenerator {
        /**
         * Adds signer information to the CMS whose content type is **SIGNED_DATA**.
         *
         * @param { X509Cert } cert - X.509 certificate.
         * @param { PrivateKeyInfo } keyInfo - Private key information.
         * @param { CmsSignerConfig } config - Signer configuration.
         * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @throws { BusinessError } 19030008 - Maybe wrong password.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        addSigner(cert: X509Cert, keyInfo: PrivateKeyInfo, config: CmsSignerConfig): void;
        /**
         * Adds a CMS certificate of the **SIGNED_DATA** content type, for example, the issuer certificate of a signing
         * certificate.
         *
         * <br>If the **addSigner** API is not called and only the certificate is added, the generated CMS signed data
         * contains only the certificate.
         *
         * @param { X509Cert } cert - X.509 certificate to add.
         * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        addCert(cert: X509Cert): void;
        /**
         * Sets the encryption algorithm for the CMS whose content type is **ENVELOPED_DATA**.
         *
         * <br>This method should be called immediately after the **CmsGenerator** of the **ENVELOPED_DATA** type is
         * created. If this method is not called, AES_256_GCM is used as the encryption algorithm by default.
         *
         * @param { CmsRecipientEncryptionAlgorithm } algorithm - Encryption algorithm used by the CMS to encapsulate data.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19020003 - Parameter check failed. Possible causes:
         *     <br>1. The type of algorithm is invalid or not supported.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 22
         */
        setRecipientEncryptionAlgorithm(algorithm: CmsRecipientEncryptionAlgorithm): void;
        /**
         * Adds recipient information to a CMS with the content type of **ENVELOPED_DATA**. This API uses a promise to
         * return the result.
         *
         * <br>At least one recipient needs to be set.
         *
         * @param { CmsRecipientInfo } recipientInfo - Recipient information.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19020003 - Parameter check failed. Possible causes:
         *     <br>1. The type of recipient certificate is invalid or not supported;
         *     <br>2. The digestAlgorithm of CmsKeyAgreeRecipientInfo is invalid or not supported;
         *     <br>3. The recipientInfo does not have any recipient info.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 22
         */
        addRecipientInfo(recipientInfo: CmsRecipientInfo): Promise<void>;
        /**
         * Obtains the CMS message, for example, the CMS signed data or CMS enveloped data. This API uses a promise to
         * return the result.
         *
         * @param { Uint8Array } data - Data to be operated.
         * @param { CmsGeneratorOptions } [options] - Configuration of the CMS operation.
         * @returns { Promise<Uint8Array | string> } Promise used to return the CMS message.
         * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        doFinal(data: Uint8Array, options?: CmsGeneratorOptions): Promise<Uint8Array | string>;
        /**
         * Obtains the CMS message, for example, the CMS signed data or CMS enveloped data. This API returns the result
         * synchronously.
         *
         * @param { Uint8Array } data - Data to be operated.
         * @param { CmsGeneratorOptions } [options] - Configuration of the CMS operation.
         * @returns { Uint8Array | string } CMS message generated.
         * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        doFinalSync(data: Uint8Array, options?: CmsGeneratorOptions): Uint8Array | string;
        /**
         * Obtains the encrypted content data of the CMS whose content type is **ENVELOPED_DATA**. This API uses a promise
         * to return the result.
         *
         * <br>Obtains the encrypted content data if the **CmsGenerator** of the **ENVELOPED_DATA** type is created and
         * data separation is used to generate detached CMS enveloped data.
         *
         * @returns { Promise<Uint8Array> } Promise used to return the encrypted data.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 22
         */
        getEncryptedContentData(): Promise<Uint8Array>;
    }
    /**
     * Creates a **CmsGenerator** object.
     *
     * @param { CmsContentType } contentType - CMS message type.
     * @returns { CmsGenerator } **CmsGenerator** object created.
     * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
     *     <br>1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types;
     *     <br>3. Parameter verification failed.
     * @throws { BusinessError } 19020001 - Memory malloc failed.
     * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
     *     <br>1. Memory copy failed;
     *     <br>2. A null pointer occurs inside the system;
     *     <br>3. Failed to obtain the native object or convert parameters.
     * @throws { BusinessError } 19030001 - Crypto operation error.
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    function createCmsGenerator(contentType: CmsContentType): CmsGenerator;
    /**
     * Represents CMS verification configuration.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice
     * @since 22
     */
    interface CmsVerificationConfig {
        /**
         * Trusted certificates.
         *
         * > **NOTE**
         * >
         * > You need to configure the trust certificates of all signers.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 22
         */
        trustCerts: Array<X509Cert>;
        /**
         * Signer certificates.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 22
         */
        signerCerts?: Array<X509Cert>;
        /**
         * Content data. If the detached mode is used, you need to specify the plaintext data. This parameter can be left
         * empty in attached mode.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 22
         */
        contentData?: Uint8Array;
        /**
         * Format of the content. The default value is **CmsContentDataFormat.BINARY**.
         *
         * @default CmsContentDataFormat.BINARY
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 22
         */
        contentDataFormat?: CmsContentDataFormat;
    }
    /**
     * Configuration used for decrypting CMS enveloped data.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice
     * @since 22
     */
    interface CmsEnvelopedDecryptionConfig {
        /**
         * Private key parameter. This parameter is left empty by default.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 22
         */
        keyInfo?: PrivateKeyInfo;
        /**
         * Public key certificate. This parameter is left empty by default.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 22
         */
        cert?: X509Cert;
        /**
         * Encrypted content data for detached CMS enveloped data, used when the CMS structure does not contain the
         * encrypted content inline.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 22
         */
        encryptedContentData?: Uint8Array;
        /**
         * Format of the content.
         *
         * @default CmsContentDataFormat.BINARY
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 22
         */
        contentDataFormat?: CmsContentDataFormat;
    }
    /**
     * Enumerates certificate types obtained from CMS.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice
     * @since 22
     */
    enum CmsCertType {
        /**
         * Signer certificates.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 22
         */
        SIGNER_CERTS = 0,
        /**
         * All certificates.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 22
         */
        ALL_CERTS = 1
    }
    /**
     * Provides APIs for parsing, verifying, and decrypting CMS messages.
     *
     * > **NOTE**
     * >
     * > PKCS #7 is a standard syntax for storing signed or encrypted data. CMS is an extension of PKCS #7. PKCS #7
     * > supports data types including data, signed data, enveloped data, signed and enveloped data, digested
     * > data, and encrypted data. It is often used to protect data integrity and confidentiality.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice
     * @since 22
     */
    interface CmsParser {
        /**
         * Set the CMS message data. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > CMS message in PEM and DER formats is supported. **string** corresponds to the PEM format, and **Uint8Array**
         * > corresponds to the DER format.
         *
         * @param { Uint8Array | string } data - CMS message content.
         * @param { CmsFormat } cmsFormat - Input CMS format.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19020003 - Parameter check failed. Possible causes:
         *     <br>1. The length of the data is zero or too large;
         *     <br>2. The type of the cmsFormat is invalid or not supported.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 22
         */
        setRawData(data: Uint8Array | string, cmsFormat: CmsFormat): Promise<void>;
        /**
         * Obtains the CMS content type.
         *
         * @returns { CmsContentType } CMS content type.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 22
         */
        getContentType(): CmsContentType;
        /**
         * Verifies the CMS message of the **SIGNED_DATA** content type. This API uses a promise to return the result.
         *
         * @param { CmsVerificationConfig } config - CMS signature verification configuration.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19020003 - Parameter check failed. Possible causes:
         *     <br>1. The trustCerts of config is empty;
         *     <br>2. The length of the contentData of config is zero or too large;
         *     <br>3. The contentDataFormat of config is invalid or not supported.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @throws { BusinessError } 19030003 - The certificate has not taken effect.
         * @throws { BusinessError } 19030004 - The certificate has expired.
         * @throws { BusinessError } 19030005 - Failed to obtain the certificate issuer.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 22
         */
        verifySignedData(config: CmsVerificationConfig): Promise<void>;
        /**
         * Obtains the content data from CMS message of the **SIGNED_DATA** type. This API uses a promise to return the
         * result.
         *
         * @returns { Promise<Uint8Array> } Promise used to return the content data.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 22
         */
        getContentData(): Promise<Uint8Array>;
        /**
         * Obtains the certificate from CMS message of the **SIGNED_DATA** type by passing enumerated values. The signer
         * certificates or all certificates can be obtained. This API uses a promise to return the result.
         *
         * @param { CmsCertType } type - Type of the certificate obtained from the CMS.
         * @returns { Promise<Array<X509Cert>> } Promise used to return a certificate set.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19020003 - Parameter check failed. Possible causes:
         *     <br>1. The value of type is invalid or not supported.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 22
         */
        getCerts(type: CmsCertType): Promise<Array<X509Cert>>;
        /**
         * Decrypts the CMS message of the **ENVELOPED_DATA** content type. This API uses a promise to return the result.
         *
         * @param { CmsEnvelopedDecryptionConfig } config - CMS decryption configuration.
         * @returns { Promise<Uint8Array> } Promise used to return the decryption result.
         * @throws { BusinessError } 19020001 - Memory malloc failed.
         * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
         *     <br>1. Memory copy failed;
         *     <br>2. A null pointer occurs inside the system;
         *     <br>3. Failed to obtain the native object or convert parameters.
         * @throws { BusinessError } 19020003 - Parameter check failed. Possible causes:
         *     <br>1. The private key is invalid or not supported;
         *     <br>2. The recipient certificate is invalid or not supported.
         * @throws { BusinessError } 19030001 - Crypto operation error.
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 22
         */
        decryptEnvelopedData(config: CmsEnvelopedDecryptionConfig): Promise<Uint8Array>;
    }
    /**
     * Creates a **CmsParser** object.
     *
     * @returns { CmsParser } CmsParser object.
     * @throws { BusinessError } 19020001 - Memory malloc failed.
     * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
     *     <br>1. Memory copy failed;
     *     <br>2. A null pointer occurs inside the system;
     *     <br>3. Failed to obtain the native object or convert parameters.
     * @throws { BusinessError } 19030001 - Crypto operation error.
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice
     * @since 22
     */
    function createCmsParser(): CmsParser;
    /**
     * Defines the CSR attribute representation.
     *
     * <br>CSR attribute field. Currently, only string-type attribute fields are supported. The attribute value added to
     * the CSR is encoded in UTF-8 format. The common type is challengePassword.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    interface CsrAttribute {
        /**
         * Attribute type defined in PKCS #9.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        type: string;
        /**
         * Attribute value.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        value: string;
    }
    /**
     * Configuration parameters for generating a CSR, including the subject name, digest algorithm, attribute,
     * and output format.
     *
     * > **NOTE**
     * >
     * > - subject is an X500DistinguishedName object.
     * >
     * > - mdName indicates the digest algorithm name. Currently, SHA1, SHA256, SHA384, and SHA512 are supported.
     * >
     * > - attributes is an optional parameter that specifies the attribute types and attribute values specified in
     * > PKCS #9 to generate a CSR. For example, challengePassword.
     * >
     * > - outFormat specifies the format of the output CSR. If the format is not specified, the PEM format is used by
     * > default.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    interface CsrGenerationConfig {
        /**
         * Subject name.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        subject: X500DistinguishedName;
        /**
         * Message digest algorithm name.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        mdName: string;
        /**
         * A collection of attributes.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        attributes?: Array<CsrAttribute>;
        /**
         * Output format.
         *
         * @default EncodingBaseFormat.PEM
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        outFormat?: EncodingBaseFormat;
    }
    /**
     * Generates a CSR.
     *
     * @param { PrivateKeyInfo } keyInfo - Private key information.
     * @param { CsrGenerationConfig } config - Configuration for generating the CSR.
     * @returns { string | Uint8Array } CSR generated.
     * @throws { BusinessError } 401 - Invalid parameters. Possible causes:
     *     <br>1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types;
     *     <br>3. Parameter verification failed.
     * @throws { BusinessError } 19020001 - Memory malloc failed.
     * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
     *     <br>1. Memory copy failed;
     *     <br>2. A null pointer occurs inside the system;
     *     <br>3. Failed to obtain the native object or convert parameters.
     * @throws { BusinessError } 19030001 - Crypto operation error.
     * @throws { BusinessError } 19030008 - Maybe wrong password.
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    function generateCsr(keyInfo: PrivateKeyInfo, config: CsrGenerationConfig): string | Uint8Array;
    /**
     * Enumerates password-based encryption scheme (PBES) algorithms.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice
     * @since 21
     */
    enum PbesEncryptionAlgorithm {
        /**
         * AES-128-CBC.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 21
         */
        AES_128_CBC = 0,
        /**
         * AES-192-CBC.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 21
         */
        AES_192_CBC = 1,
        /**
         * AES-256-CBC.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 21
         */
        AES_256_CBC = 2
    }
    /**
     * Represents PBES algorithm parameters. Currently, only PBES2 is supported.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice
     * @since 21
     */
    interface PbesParams {
        /**
         * Length of the salt value. The default value is **16**, and the minimum value is **8**.
         * The value must be an integer greater than or equal to 8.
         *
         * @default 16
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 21
         */
        saltLen?: number;
        /**
         * Number of iterations. The default value is **2048**.
         * The value must be a positive integer.
         *
         * @default 2048
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 21
         */
        iterations?: number;
        /**
         * PBES algorithm type. The default value is **AES_256_CBC**.
         *
         * @default PbesEncryptionAlgorithm.AES_256_CBC
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 21
         */
        encryptionAlgorithm?: PbesEncryptionAlgorithm;
    }
    /**
     * Enumerates the P12 MAC digest algorithms.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice
     * @since 21
     */
    enum Pkcs12MacDigestAlgorithm {
        /**
         * SHA-256.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 21
         */
        SHA256 = 0,
        /**
         * SHA-384.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 21
         */
        SHA384 = 1,
        /**
         * SHA-512.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 21
         */
        SHA512 = 2
    }
    /**
     * Represents the configuration for creating .p12 files.
     *
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice
     * @since 21
     */
    interface Pkcs12CreationConfig {
        /**
         * Password of the .p12 file. The minimum length is 4.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 21
         */
        password: string;
        /**
         * Algorithm parameters for encrypting the private key.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 21
         */
        keyEncParams?: PbesParams;
        /**
         * Whether to encrypt the certificate. The default value is **true**. **true** means to encrypt the certificate;
         * **false** otherwise.
         *
         * @default true
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 21
         */
        encryptCert?: boolean;
        /**
         * Algorithm parameters for encrypting the certificate.
         *
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 21
         */
        certEncParams?: PbesParams;
        /**
         * Length of the salt value of the P12 MAC. The minimum value is **8**, and the default value is **16**.
         * The value must be an integer greater than or equal to 8.
         *
         * @default 16
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 21
         */
        macSaltLen?: number;
        /**
         * Number of P12 MAC iterations. The default value is **2048**.
         * The value must be a positive integer.
         *
         * @default 2048
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 21
         */
        macIterations?: number;
        /**
         * MAC digest algorithm for the P12. The default value is **SHA256**.
         *
         * @default Pkcs12MacDigestAlgorithm.SHA256
         * @syscap SystemCapability.Security.Cert
         * @crossplatform
         * @atomicservice
         * @since 21
         */
        macDigestAlgorithm?: Pkcs12MacDigestAlgorithm;
    }
    /**
     * Creates P12. This API returns the result synchronously.
     *
     * @param { Pkcs12Data } data - P12 data object to be packed.
     * @param { Pkcs12CreationConfig } config - Configuration for creating the P12 file.
     * @returns { Uint8Array } P12 file created, in DER format.
     * @throws { BusinessError } 19020001 - Memory malloc failed.
     * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
     *     <br>1. Memory copy failed;
     *     <br>2. A null pointer occurs inside the system;
     *     <br>3. Failed to obtain the native object or convert parameters.
     * @throws { BusinessError } 19020003 - Parameter check failed. Possible causes:
     *     <br>1. The password is too short or too long;
     *     <br>2. The private key does not match the certificate;
     *     <br>3. Invalid encryption algorithm parameters.
     * @throws { BusinessError } 19030001 - Crypto operation error.
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice
     * @since 21
     */
    function createPkcs12Sync(data: Pkcs12Data, config: Pkcs12CreationConfig): Uint8Array;
    /**
     * Creates P12. This API uses a promise to return the result.
     *
     * @param { Pkcs12Data } data - P12 data object to be packed.
     * @param { Pkcs12CreationConfig } config - Configuration for creating the P12.
     * @returns { Promise<Uint8Array> } Promise used to return the P12 created, in DER format.
     * @throws { BusinessError } 19020001 - Memory malloc failed.
     * @throws { BusinessError } 19020002 - Runtime error. Possible causes:
     *     <br>1. Memory copy failed;
     *     <br>2. A null pointer occurs inside the system;
     *     <br>3. Failed to obtain the native object or convert parameters.
     * @throws { BusinessError } 19020003 - Parameter check failed. Possible causes:
     *     <br>1. The password is too short or too long;
     *     <br>2. The private key does not match the certificate;
     *     <br>3. Invalid encryption algorithm parameters.
     * @throws { BusinessError } 19030001 - Crypto operation error.
     * @syscap SystemCapability.Security.Cert
     * @crossplatform
     * @atomicservice
     * @since 21
     */
    function createPkcs12(data: Pkcs12Data, config: Pkcs12CreationConfig): Promise<Uint8Array>;
}
export default cert;

```
