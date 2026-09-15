# @ohos.file.hash.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022-2025 Huawei Device Co., Ltd.
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
 * @kit CoreFileKit
 */
import type { AsyncCallback } from './@ohos.base';
import stream from './@ohos.util.stream';
/**
 * The **FileHash** module implements hash processing on files.
 *
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @atomicservice [since 11]
 * @since 9
 */
declare namespace hash {
    /**
     * Calculates a hash value for a file. This API uses a promise to return the result.
     *
     * @param { string } path - Path of the file in the application sandbox.
     * @param { string } algorithm - Algorithm used to calculate the hash value. The value can be **md5**, **sha1**, or
     *     **sha256**. **sha256** is recommended for security purposes.
     * @returns { Promise<string> } Promise used to return the hash value. The hash value is a hexadecimal string
     *     consisting of digits and uppercase letters.
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @atomicservice [since 11]
     * @since 9
     */
    function hash(path: string, algorithm: string): Promise<string>;
    /**
     * Calculates a hash value for a file. This API uses an asynchronous callback to return the result.
     *
     * @param { string } path - Path of the file in the application sandbox.
     * @param { string } algorithm - Algorithm used to calculate the hash value. The value can be **md5**, **sha1**, or
     *     **sha256**. **sha256** is recommended for security purposes.
     * @param { AsyncCallback<string> } [callback] - Callback used to return the hash value obtained. The hash value is a
     *     hexadecimal string consisting of digits and uppercase letters.
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @atomicservice [since 11]
     * @since 9
     */
    function hash(path: string, algorithm: string, callback: AsyncCallback<string>): void;
    /**
     * The **HashStream** class is a utility for creating a message digest of data. You can use
     * [createHash](docroot://reference/apis-core-file-kit/js-apis-file-hash.md#hashcreatehash12) to create a
     * **HashStream** instance.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 12
     */
    class HashStream extends stream.Transform {
        /**
         * Generates a message digest.
         *
         * @returns { string } Hash value, which is a hexadecimal string consisting of digits and uppercase letters.
         * @throws { BusinessError } 401 - Parameter error
         * @throws { BusinessError } 13900042 - Unknown error
         * @syscap SystemCapability.FileManagement.File.FileIO
         * @crossplatform [since 20]
         * @since 12
         */
        digest(): string;
        /**
         * Updates the data for generating a message digest. This API can be called multiple times.
         *
         * @param { ArrayBuffer } data - Data to be calculated.
         * @throws { BusinessError } 401 - Parameter error
         * @throws { BusinessError } 13900042 - Unknown error
         * @syscap SystemCapability.FileManagement.File.FileIO
         * @crossplatform [since 20]
         * @since 12
         */
        update(data: ArrayBuffer): void;
    }
    /**
     * Creates a **HashStream** instance, which can be used to generate a message digest (a hash value) using the given
     * algorithm.
     *
     * @param { string } algorithm - Algorithm used to calculate the hash value. The value can be **md5**, **sha1**, or
     *     **sha256**. **sha256** is recommended for security purposes.
     * @returns { HashStream } **HashStream** instance created.
     * @throws { BusinessError } 401 - Parameter error
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 12
     */
    function createHash(algorithm: string): HashStream;
}
export default hash;

```
