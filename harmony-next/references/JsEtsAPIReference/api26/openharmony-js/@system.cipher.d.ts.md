# @system.cipher.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2020-2023 Huawei Device Co., Ltd.
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
 * @kit CryptoArchitectureKit
 */
/**
 * Defines the response to the cipher interface called.
 *
 * @syscap SystemCapability.Security.Cipher
 * @since 3
 * @deprecated since 11
 * @useinstead ohos.security.cryptoFramework.Cipher
 */
export interface CipherResponse {
    /**
     * Response content.
     *
     * @syscap SystemCapability.Security.Cipher
     * @since 3
     * @deprecated since 11
     * @useinstead ohos.security.cryptoFramework.Cipher
     */
    text: string;
}
/**
 * Defines the input parameters of **cipher.rsa()**.
 *
 * @syscap SystemCapability.Security.Cipher
 * @since 3
 * @deprecated since 11
 * @useinstead ohos.security.cryptoFramework.Cipher
 */
export interface CipherRsaOptions {
    /**
     * Action to perform. The options are as follows:
     *
     * 1. **encrypt**: Encrypts data.
     * 2. **decrypt**: Decrypts data.
     *
     * @syscap SystemCapability.Security.Cipher
     * @since 3
     * @deprecated since 11
     * @useinstead ohos.security.cryptoFramework.Cipher
     */
    action: string;
    /**
     * Text to be encrypted or decrypted.
     *
     * The text to be encrypted must be a common text and cannot exceed the length calculated based on the formula (
     * keySize/8 - 66). **keySize** indicates the key length. For example, if the key length is 1024 bytes, the text
     * cannot exceed 62 bytes (1024/8 - 66 = 62). The text to be decrypted must be a binary value encoded in Base64. The
     * default format is used for Base64 encoding.
     *
     * @syscap SystemCapability.Security.Cipher
     * @since 3
     * @deprecated since 11
     * @useinstead ohos.security.cryptoFramework.Cipher
     */
    text: string;
    /**
     * RSA key. It is a public key in encryption and a private key in decryption.
     *
     * @syscap SystemCapability.Security.Cipher
     * @since 3
     * @deprecated since 11
     * @useinstead ohos.security.cryptoFramework.Cipher
     */
    key: string;
    /**
     * RSA padding. The default value is **RSA/None/OAEPWithSHA256AndMGF1Padding**.
     *
     * @syscap SystemCapability.Security.Cipher
     * @since 3
     * @deprecated since 11
     * @useinstead ohos.security.cryptoFramework.Cipher
     */
    transformation?: string;
    /**
     * Called when data is encrypted or decrypted successfully.
     *
     * @syscap SystemCapability.Security.Cipher
     * @since 3
     * @deprecated since 11
     * @useinstead ohos.security.cryptoFramework.Cipher
     */
    success: (data: CipherResponse) => void;
    /**
     * Called when data fails to be encrypted or decrypted.
     *
     * @syscap SystemCapability.Security.Cipher
     * @since 3
     * @deprecated since 11
     * @useinstead ohos.security.cryptoFramework.Cipher
     */
    fail: (data: string, code: number) => void;
    /**
     * Called when the execution is complete.
     *
     * @syscap SystemCapability.Security.Cipher
     * @since 3
     * @deprecated since 11
     * @useinstead ohos.security.cryptoFramework.Cipher
     */
    complete: () => void;
}
/**
 * Defines the input parameters of **cipher.aes()**.
 *
 * @syscap SystemCapability.Security.Cipher
 * @since 3
 * @deprecated since 11
 * @useinstead ohos.security.cryptoFramework.Cipher
 */
export interface CipherAesOptions {
    /**
     * Action to perform. The options are as follows:
     *
     * 1. **encrypt**: Encrypts data.
     * 2. **decrypt**: Decrypts data.
     *
     * @syscap SystemCapability.Security.Cipher
     * @since 3
     * @deprecated since 11
     * @useinstead ohos.security.cryptoFramework.Cipher
     */
    action: string;
    /**
     * Text to be encrypted or decrypted.
     *
     * The text to be encrypted must be common text. The text to be decrypted must be a binary value encoded in Base64.
     * The default format is used for Base64 encoding.
     *
     * @syscap SystemCapability.Security.Cipher
     * @since 3
     * @deprecated since 11
     * @useinstead ohos.security.cryptoFramework.Cipher
     */
    text: string;
    /**
     * Key used for encryption or decryption. It is a Base64 encoded string.
     *
     * @syscap SystemCapability.Security.Cipher
     * @since 3
     * @deprecated since 11
     * @useinstead ohos.security.cryptoFramework.Cipher
     */
    key: string;
    /**
     * Encryption mode and padding of the AES algorithm. The default value is **AES/CBC/PKCS5Padding**.
     *
     * @syscap SystemCapability.Security.Cipher
     * @since 3
     * @deprecated since 11
     * @useinstead ohos.security.cryptoFramework.Cipher
     */
    transformation?: string;
    /**
     * Initialization vector (IV) for AES-based encryption and decryption. The value is a string encoded in Base64. The
     * default value is the key value.
     *
     * @syscap SystemCapability.Security.Cipher
     * @since 3
     * @deprecated since 11
     * @useinstead ohos.security.cryptoFramework.Cipher
     */
    iv?: string;
    /**
     * Offset of the IV for AES-based encryption and decryption. The default value is **0**, which is the only value
     * supported.
     *
     * @syscap SystemCapability.Security.Cipher
     * @since 3
     * @deprecated since 11
     * @useinstead ohos.security.cryptoFramework.Cipher
     */
    ivOffset?: string;
    /**
     * Length of the IV, in bytes. This field is reserved. The default value is **16**, which is the only value supported.
     *
     * @syscap SystemCapability.Security.Cipher
     * @since 3
     * @deprecated since 11
     * @useinstead ohos.security.cryptoFramework.Cipher
     */
    ivLen?: string;
    /**
     * Called when data is encrypted or decrypted successfully.
     *
     * @syscap SystemCapability.Security.Cipher
     * @since 3
     * @deprecated since 11
     * @useinstead ohos.security.cryptoFramework.Cipher
     */
    success: (data: CipherResponse) => void;
    /**
     * Called when data fails to be encrypted or decrypted.
     *
     * @syscap SystemCapability.Security.Cipher
     * @since 3
     * @deprecated since 11
     * @useinstead ohos.security.cryptoFramework.Cipher
     */
    fail: (data: string, code: number) => void;
    /**
     * Called when the execution is complete.
     *
     * @syscap SystemCapability.Security.Cipher
     * @since 3
     * @deprecated since 11
     * @useinstead ohos.security.cryptoFramework.Cipher
     */
    complete: () => void;
}
/**
 * Defines the cipher functions.
 *
 * @syscap SystemCapability.Security.Cipher
 * @since 3
 * @deprecated since 9
 * @useinstead ohos.security.cryptoFramework.Cipher
 */
export default class Cipher {
    /**
     * Encrypts or decrypts data using RSA.
     *
     * @param { CipherRsaOptions } options - RSA options.
     * @syscap SystemCapability.Security.Cipher
     * @since 3
     * @deprecated since 9
     * @useinstead ohos.security.cryptoFramework.Cipher
     */
    static rsa(options: CipherRsaOptions): void;
    /**
     * Encrypts or decrypts data using AES.
     *
     * @param { CipherAesOptions } options - AES options.
     * @syscap SystemCapability.Security.Cipher
     * @since 3
     * @deprecated since 9
     * @useinstead ohos.security.cryptoFramework.Cipher
     */
    static aes(options: CipherAesOptions): void;
}

```
