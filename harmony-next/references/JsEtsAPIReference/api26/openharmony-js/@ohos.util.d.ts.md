# @ohos.util.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2021-2022 Huawei Device Co., Ltd.
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
 * @kit ArkTS
 */
/**
 * The util module provides common utility functions, such as [TextEncoder]{@link util.TextEncoder} and
 * [TextDecoder]{@link util.TextDecoderOptions} for string encoding and decoding,
 * [RationalNumber<sup>8+</sup>]{@link util.RationalNumber} for rational number operations,
 * [LRUCache<sup>9+</sup>]{@link util.LRUCache} for cache management, [ScopeHelper<sup>9+</sup>]{@link util.ScopeHelper}
 * for range determination, [Base64Helper<sup>9+</sup>]{@link util.Base64Helper} for Base64 encoding and decoding,
 * [types<sup>8+</sup>]{@link util.types} for built-in object type check, and [Aspect<sup>11+</sup>]{@link util.Aspect}
 * for instrumentation and replacement on methods.
 *
 * @syscap SystemCapability.Utils.Lang
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 7
 */
declare namespace util {
    /**
     * Formats a string by replacing the placeholders in it.
     *
     * @param { string } format - Format string.
     * @param { Object[] } args - Data used to replace the placeholders in **format**. If **null** is passed in, the first
     *     argument is returned by default.
     * @returns { string } String containing the formatted values.
     * @syscap SystemCapability.Utils.Lang
     * @since 7
     * @deprecated since 9
     * @useinstead util.format
     */
    function printf(format: string, ...args: Object[]): string;
    /**
     * Formats a string by replacing the placeholders in it.
     *
     * @param { string } format - Format string. This string contains zero or more placeholders, which specify the
     *     position and format of the arguments to be inserted.
     * @param { Object[] } args - Data used to replace the placeholders in **format**. If **null** is passed in, the first
     *     argument is returned by default.
     * @returns { string } Formatted string.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 9
     */
    function format(format: string, ...args: Object[]): string;
    /**
     * Obtains detailed information about a system error code.
     *
     * @param { number } errno - Error code generated.
     * @returns { string } Detailed information about the error code.
     * @syscap SystemCapability.Utils.Lang
     * @since 7
     * @deprecated since 9
     * @useinstead util.errnoToString
     */
    function getErrorString(errno: number): string;
    /**
     * Obtains detailed information about a system error code.
     *
     * @param { number } errno - Error code generated.
     * @returns { string } Detailed information about the error code.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 9
     */
    function errnoToString(errno: number): string;
    /**
     * Calls back an asynchronous function. In the callback, the first parameter indicates the cause of the rejection (the
     * value is **null** if the promise has been resolved), and the second parameter indicates the resolved value.
     *
     * > **NOTE**
     * >
     * > - **original** must be an asynchronous function. If a non-asynchronous function is passed in, the function is not
     * > intercepted, but the error message "callbackWrapper: The type of Parameter must be AsyncFunction" is displayed.
     * >
     * > - This API converts an async function that returns a promise into an error-first callback function. The function
     * > returned by this API accepts a callback as its second input parameter. When this method is called, the original
     * > function is executed first. When the promise of **original** returns **resolve**, the first parameter of the
     * > callback function is **null**, and the second parameter is the value of **resolve**. When the promise of
     * > **original** returns **reject**, the first parameter of the callback function is an error object, and the second
     * > parameter is **null**. When **original** is a function without input parameters, the first input parameter of the
     * > function returned by this API must be an invalid placeholder parameter.
     *
     * @param { Function } original - Asynchronous function.
     * @returns { function } Callback function, in which the first parameter **err** indicates
     *     the cause of the rejection
     *     (the value is **null** if the promise has been resolved) and the second parameter **value** indicates the
     *     resolved value.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 7
     */
    function callbackWrapper(original: Function): (err: Object, value: Object) => void;
    /**
     * Receives a function that uses the error-first callback mode, that is, uses `(err, value) => callback` as the last
     * parameter, and uses a promise to return the result.
     *
     * @param { function } original - Function, in which the first parameter **err** indicates the cause of the rejection
     *     (the value is **null** if the promise has been resolved) and the second parameter **value** indicates the
     *     resolved value.
     * @returns { function } Return a function that returns promises [since 9 - 11]
     * @returns { Function } Promise function. [since 10]
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 9
     */
    function promisify(original: (err: Object, value: Object) => void): Function;
    /**
     * Receives a function that uses the error-first callback mode, that is, uses `(err, value) => callback` as the last
     * parameter, and uses a promise to return the result.
     *
     * @param { function } original - Asynchronous function.
     * @returns { Object } Promise in the error-first style (that is, (err, value) => ... is called as the last parameter)
     *     .
     * @syscap SystemCapability.Utils.Lang
     * @since 7
     * @deprecated since 9
     * @useinstead util.promisify
     */
    function promiseWrapper(original: (err: Object, value: Object) => void): Object;
    /**
     * Uses a secure random number generator to generate a random universally unique identifier (UUID) of the string type
     * in RFC 4122 version 4. To improve performance, this API uses cached UUIDs by default, in which **entropyCache** is
     * set to **true**. A maximum of 128 random UUIDs can be cached. After all the 128 UUIDs in the cache are used, a new
     * set of UUIDs is generated to maintain their random distribution. If you do not need to use the cached UUID, set
     * **entropyCache** to **false**.
     *
     * @param { boolean } [entropyCache] - Whether to use a cached UUID. The value **true** means to use a cached UUID,
     *     and **false** means the opposite. The default value is **true**.
     * @returns { string } A string representing the UUID generated.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 9
     */
    function generateRandomUUID(entropyCache?: boolean): string;
    /**
     * Uses a secure random number generator to generate a random universally unique identifier (UUID) of RFC 4122 version
     * 4.
     *
     * @param { boolean } [entropyCache] - Whether to use a cached UUID. The value **true** means to use a cached UUID,
     *     and **false** means the opposite. The default value is **true**.
     * @returns { Uint8Array } A Uint8Array value representing the UUID generated.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 9
     */
    function generateRandomBinaryUUID(entropyCache?: boolean): Uint8Array;
    /**
     * Converts a UUID of the string type generated by **generateRandomUUID** to a UUID generated by
     * **generateRandomBinaryUUID**, as described in RFC 4122.
     *
     * @param { string } uuid - A string representing the UUID.
     * @returns { Uint8Array } A Uint8Array value representing the UUID parsed. If the parsing fails, **SyntaxError** is
     *     thrown.
     * @throws { BusinessError } 10200002 - Invalid uuid string.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 9
     */
    function parseUUID(uuid: string): Uint8Array;
    /**
     * Obtains the hash value of an object.
     * If no hash value has been obtained, a random hash value is generated, saved to the **hash** field of the object,
     * and returned. If a hash value has been obtained, the hash value saved in the **hash** field is returned (the same
     * value is returned for the same object).
     *
     * @param { object } [object] - Object whose hash value is to be obtained.
     * @returns { number } Hash value.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    function getHash(object: object): number;
    /**
     * Describes decoding-related options, which include **fatal** and **ignoreBOM**.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice
     * @since 11
     */
    interface TextDecoderOptions {
        /**
         * Whether to display fatal errors. The value **true** means to display fatal errors, and **false** means the
         * opposite. The default value is **false**.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 11
         */
        fatal?: boolean;
        /**
         * Whether to ignore the BOM. The value **true** means to ignore the BOM, and **false** means the opposite. The
         * default value is **false**.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 11
         */
        ignoreBOM?: boolean;
    }
    /**
     * Defines whether decoding follows data blocks.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice
     * @since 11
     */
    interface DecodeWithStreamOptions {
        /**
         * Whether to allow data blocks in subsequent **decodeWithStream()**. If data is processed in blocks, set this
         * parameter to **true**. If this is the last data block to process or data is not divided into blocks, set this
         * parameter to **false**. The default value is **false**.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 11
         */
        stream?: boolean;
    }
    /**
     * Describes the behavioral parameters for the **decodeToString** method when decoding byte streams.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    interface DecodeToStringOptions {
        /**
         * Whether the incomplete byte sequence at the end of the input needs to be appended to the parameter for the next
         * call of **decodeToString**. The value **true** means that the incomplete byte sequence is stored in the internal
         * buffer until the function is called next time. If the value is false, the byte sequence is directly decoded when
         * the function is called currently. The default value is **false**.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        stream?: boolean;
    }
    /**
     * Provides APIs to decode byte arrays into strings. It supports multiple formats, including UTF-8, UTF-16LE, UTF-16BE
     * , ISO-8859, and Windows-1251.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 7
     */
    class TextDecoder {
        /**
         * A constructor used to create a **TextDecoder** object.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        constructor();
        /**
         * Encoding format.<br>The following formats are supported: utf-8, ibm866, iso-8859-2, iso-8859-3, iso-8859-4, iso-8
         * 859-5, iso-8859-6, iso-8859-7, iso-8859-8, iso-8859-8-i, iso-8859-10, iso-8859-13, iso-8859-14, iso-8859-15, koi8
         * -r, koi8-u, macintosh, windows-874, windows-1250, windows-1251, windows-1252, windows-1253, windows-1254, windows
         * -1255, windows-1256, windows-1257, windows-1258, x-mac-cyrillic, gbk, gb18030, big5, euc-jp, iso-2022-jp,
         * shift_jis, euc-kr, utf-16be, utf-16le, gb2312, and iso-8859-1.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 7
         */
        readonly encoding: string;
        /**
         * Whether to display fatal errors. The value **true** means to display fatal errors, and **false** means the
         * opposite.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 7
         */
        readonly fatal: boolean;
        /**
         * Whether to ignore the byte order marker (BOM). The default value is **false**, which indicates that the result
         * contains the BOM.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 7
         */
        readonly ignoreBOM = false;
        /**
         * A constructor used to create a **TextDecoder** object.
         *
         * @param { string } encoding - Encoding format. The default format is **'utf-8'**.
         * @param { object } options - Decoding-related options, which include **fatal** and **ignoreBOM**.
         * @syscap SystemCapability.Utils.Lang
         * @since 7
         * @deprecated since 9
         * @useinstead util.TextDecoder.create
         */
        constructor(encoding?: string, options?: {
            fatal?: boolean;
            ignoreBOM?: boolean;
        });
        /**
         * Creates a **TextDecoder** object. It provides the same function as the deprecated argument constructor.
         *
         * @param { string } encoding - Encoding format. The default format is **'utf-8'**. [since 9 - 10]
         * @param { object } options - Decoding-related options, which include **fatal** and **ignoreBOM**. [since 9 - 10]
         * @param { string } [encoding] - Encoding format. The default format is **'utf-8'**. [since 11]
         * @param { TextDecoderOptions } [options] - Decoding-related options, which include **fatal** and **ignoreBOM**.
         *     [since 11]
         * @returns { TextDecoder } **TextDecoder** object created.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        static create(encoding?: string, options?: TextDecoderOptions): TextDecoder;
        /**
         * Decodes the input content into a string.
         *
         * @param { Uint8Array } input - Uint8Array object to decode.
         * @param { object } options - Decoding-related options.
         * @returns { string } String obtained.
         * @syscap SystemCapability.Utils.Lang
         * @since 7
         * @deprecated since 9
         * @useinstead util.TextDecoder.decodeToString
         */
        decode(input: Uint8Array, options?: {
            stream?: false;
        }): string;
        /**
         * Decodes the input content into a string. If **input** is an empty array, **undefined** is returned.
         *
         * @param { Uint8Array } input - Uint8Array object to decode.
         * @param { object } options - Decoding-related options. [since 9 - 10]
         * @param { DecodeWithStreamOptions } [options] - Decoding-related options. [since 11]
         * @returns { string } String obtained.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         * @deprecated since 12
         * @useinstead util.TextDecoder.decodeToString
         */
        decodeWithStream(input: Uint8Array, options?: DecodeWithStreamOptions): string;
        /**
         * Decodes the input content into a string.
         *
         * @param { Uint8Array } input - Uint8Array object to decode.
         * @param { DecodeToStringOptions } [options] - Decoding-related options. The default value is **undefined**.
         * @returns { string } String obtained.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        decodeToString(input: Uint8Array, options?: DecodeToStringOptions): string;
    }
    /**
     * Encrypted information, including the number of read characters and the number of written bytes.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice
     * @since 11
     */
    interface EncodeIntoUint8ArrayInfo {
        /**
         * Number of characters that have been read.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 11
         */
        read: number;
        /**
         * Number of bytes that have been written.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 11
         */
        written: number;
    }
    /**
     * Provides APIs to encode strings into byte arrays. Multiple encoding formats are supported.
     * When **TextEncoder** is used for encoding, the number of bytes occupied by a character varies according to the
     * encoding format. You must explicitly specify the encoding format to obtain the required encoding result.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 7
     */
    class TextEncoder {
        /**
         * Encoding format.<br>The following formats are supported: utf-8, gb2312, gb18030, ibm866, iso-8859-1, iso-8859-2,
         * iso-8859-3, iso-8859-4, iso-8859-5, iso-8859-6, iso-8859-7, iso-8859-8, iso-8859-8-i, iso-8859-10, iso-8859-13,
         * iso-8859-14, iso-8859-15, koi8-r, koi8-u, macintosh, windows-874, windows-1250, windows-1251, windows-1252,
         * windows-1253, windows-1254, windows-1255, windows-1256, windows-1257, windows-1258, gbk, big5, euc-jp, iso-2022-
         * jp, shift_jis, euc-kr, x-mac-cyrillic, utf-16be, and utf-16le.<br>The default value is **'utf-8'**.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 7
         */
        readonly encoding = 'utf-8';
        /**
         * A constructor used to create a **TextEncoder** object.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 7
         */
        constructor();
        /**
         * A constructor used to create a **TextEncoder** object.
         *
         * @param { string } [encoding] - Encoding format. The default format is **'utf-8'**.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        constructor(encoding?: string);
        /**
         * Creates a **TextEncoder** object.
         *
         * @param { string } [encoding] - Encoding format. The default format is **'utf-8'**.
         * @returns { TextEncoder } **TextEncoder** object.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        static create(encoding?: string): TextEncoder;
        /**
         * Encodes the input content in to a Uint8Array object.
         *
         * @param { string } [input] - String to encode. The default value is an empty string.
         * @returns { Uint8Array } Uint8Array object obtained.
         * @syscap SystemCapability.Utils.Lang
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.util.encodeInto
         */
        encode(input?: string): Uint8Array;
        /**
         * Encodes the input content into a Uint8Array object.
         *
         * @param { string } [input] - String to encode. The default value is an empty string. If the input parameter is an
         *     empty string, the return value is undefined.
         * @returns { Uint8Array } Uint8Array object obtained.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        encodeInto(input?: string): Uint8Array;
        /**
         * Writes the generated UTF-8 encoded text to an array.
         *
         * @param { string } input - String to encode.
         * @param { Uint8Array } dest - Uint8Array object used to store the UTF-8 encoded text.
         * @returns { object } Object obtained. **read** indicates the number of encoded characters, and **written**
         *     indicates the number of bytes in the encoded characters.
         * @syscap SystemCapability.Utils.Lang
         * @since 7
         * @deprecated since 9
         * @useinstead util.TextEncoder.encodeIntoUint8Array
         */
        encodeInto(input: string, dest: Uint8Array): {
            read: number;
            written: number;
        };
        /**
         * Encodes the input content and stores the result into a Uint8Array object.
         *
         * @param { string } input - String to encode.
         * @param { Uint8Array } dest - Uint8Array object used to store the UTF-8 encoded text.
         * @returns { object } Return the object, where read represents
         *     the number of characters that have been encoded, and written
         *     represents the number of bytes occupied by the encoded characters. [since 9 - 10]
         * @returns { EncodeIntoUint8ArrayInfo } Object obtained. **read** indicates the number of encoded characters, and
         *     **written** indicates the number of bytes in the encoded characters. [since 11]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        encodeIntoUint8Array(input: string, dest: Uint8Array): EncodeIntoUint8ArrayInfo;
    }
    /**
     * Provides APIs to compare rational numbers and obtain numerators and denominators. For example, the **toString()**
     * API can be used to convert a rational number into a string.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    class RationalNumber {
        /**
         * A constructor used to create a **RationalNumber** object.
         *
         * @param { number } numerator - Numerator, which is an integer.
         * @param { number } denominator - Denominator, which is an integer.
         * @syscap SystemCapability.Utils.Lang
         * @since 8
         * @deprecated since 9
         * @useinstead util.RationalNumber.parseRationalNumber
         */
        constructor(numerator: number, denominator: number);
        /**
         * A constructor used to create a **RationalNumber** object.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        constructor();
        /**
         * Creates a **RationalNumber** instance with a given numerator and denominator.
         *
         * > **NOTE**
         * >
         * > The **numerator** and **denominator** parameters must be integers. If a decimal number is passed in, the
         * > function is not intercepted, but the error message "parseRationalNumber: The type of Parameter must be integer"
         * > is displayed.
         *
         * @param { number } numerator - Numerator, which is an integer. Value range: -Number.MAX_VALUE <= numerator <=
         *     Number.MAX_VALUE.
         * @param { number } denominator - Denominator, which is an integer. Value range: -Number.MAX_VALUE <= denominator <
         *     = Number.MAX_VALUE.
         * @returns { RationalNumber } **RationalNumber** object obtained.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        static parseRationalNumber(numerator: number, denominator: number): RationalNumber;
        /**
         * Creates a **RationalNumber** object based on the given string.
         *
         * > **NOTE**
         * >
         * > The **rationalString** parameter must be a string. If a decimal string is passed in, the function is not
         * > intercepted, but the error message "createRationalFromString: The type of Parameter must be integer string" is
         * > displayed.
         *
         * @param { string } rationalString - String used to create the **RationalNumber** object.
         * @returns { RationalNumber } Returns a RationalNumber object generated based on the given string.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        static createRationalFromString(rationalString: string): RationalNumber;
        /**
         * Compares the current RationalNumber object to the given object.
         *
         * @param { RationalNumber } another - An object of other rational numbers
         * @returns { number } Returns 0 or 1, or -1, depending on the comparison.
         * @syscap SystemCapability.Utils.Lang
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.util.compare
         */
        compareTo(another: RationalNumber): number;
        /**
         * Compares the current RationalNumber object to the given object.
         *
         * @param { RationalNumber } another - An object of other rational numbers
         * @returns { number } Returns 0 or 1, or -1, depending on the comparison.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        compare(another: RationalNumber): number;
        /**
         * Checks whether this **RationalNumber** object equals the given object.
         *
         * @param { Object } obj - Object used to compare with this **RationalNumber** object.
         * @returns { boolean } Check result. The value **true** is returned if the two objects are equal; otherwise,
         *     **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        equals(obj: Object): boolean;
        /**
         * Obtains the integer or floating-point value of this **RationalNumber** object.
         *
         * @returns { number } An integer or a floating-point number.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        valueOf(): number;
        /**
         * Obtains the greatest common divisor of two specified integers.
         *
         * @param { number } number1 - The first integer used to get the greatest common divisor.
         * @param { number } number2 - The second integer used to get the greatest common divisor.
         * @returns { number } Greatest common divisor obtained.
         * @syscap SystemCapability.Utils.Lang
         * @since 8
         * @deprecated since 9
         * @useinstead util.RationalNumber.getCommonFactor
         */
        static getCommonDivisor(number1: number, number2: number): number;
        /**
         * Obtains the greatest common divisor of two specified integers.
         *
         * > **NOTE**
         * >
         * > The **number1** and **number2** parameters must be integers. If a decimal number is passed in, the function is
         * > not intercepted, but the error message "getCommonFactor: The type of Parameter must be integer" is displayed.
         *
         * @param { number } number1 - The first integer used to get the greatest common divisor. Value range: -
         *     Number.MAX_VALUE <= number1 <= Number.MAX_VALUE.
         * @param { number } number2 - The second integer used to get the greatest common divisor. Value range: -
         *     Number.MAX_VALUE <= number2 <= Number.MAX_VALUE.
         * @returns { number } Greatest common divisor obtained.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        static getCommonFactor(number1: number, number2: number): number;
        /**
         * Obtains the denominator of this **RationalNumber** object.
         *
         * @returns { number } Denominator of this **RationalNumber** object.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        getDenominator(): number;
        /**
         * Obtains the numerator of this **RationalNumber** object.
         *
         * @returns { number } Numerator of this **RationalNumber** object.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        getNumerator(): number;
        /**
         * Checks whether this **RationalNumber** object represents a finite value.
         *
         * @returns { boolean } Check result. The value **true** is returned if this **RationalNumber** object represents a
         *     finite value (the denominator is not **0**); otherwise, **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        isFinite(): boolean;
        /**
         * Checks whether this **RationalNumber** object is a Not a Number (NaN).
         *
         * @returns { boolean } Check result. The value **true** is returned if this **RationalNumber** object is a NaN (the
         *     denominator and numerator are both **0**); otherwise, **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        isNaN(): boolean;
        /**
         * Checks whether this **RationalNumber** object is **0**.
         *
         * @returns { boolean } Check result. The value **true** is returned if the value of this **RationalNumber** object
         *     is **0**; otherwise, **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        isZero(): boolean;
        /**
         * Obtains the string representation of this **RationalNumber** object.
         *
         * @returns { string } Returns a string in Numerator/Denominator format in normal cases, for example, 3/5; returns
         *     **0/1** if the numerator of this object is **0**; returns **Infinity** if the denominator is **0**; returns
         *     **NaN** if the numerator and denominator are both **0**.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        toString(): string;
    }
    /**
     * The LruBuffer algorithm replaces the least used data with new data when the buffer space is insufficient.
     *
     * @syscap SystemCapability.Utils.Lang
     * @since 8
     * @deprecated since 9
     * @useinstead util.LRUCache
     */
    class LruBuffer<K, V> {
        /**
         * A constructor used to create a **LruBuffer** instance. The default capacity of the cache is 64.
         *
         * @param { number } capacity - Capacity of the cache to create. The default value is **64**.
         * @syscap SystemCapability.Utils.Lang
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.util.LRUCache.constructor
         */
        constructor(capacity?: number);
        /**
         * Changes the cache capacity. If the new capacity is less than or equal to **0**, an exception will be thrown.
         *
         * @param { number } newCapacity - New capacity of the cache.
         * @syscap SystemCapability.Utils.Lang
         * @since 8
         * @deprecated since 9
         * @useinstead util.LRUCache.updateCapacity
         */
        updateCapacity(newCapacity: number): void;
        /**
         * Obtains the string representation of this cache.
         *
         * @returns { string } String representation of this cache.
         * @syscap SystemCapability.Utils.Lang
         * @since 8
         * @deprecated since 9
         * @useinstead util.LRUCache.toString
         */
        toString(): string;
        /**
         * Total number of values in this cache.
         *
         * @syscap SystemCapability.Utils.Lang
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.util.LRUCache.length
         */
        length: number;
        /**
         * Obtains the capacity of this cache.
         *
         * @returns { number } Capacity of the cache.
         * @syscap SystemCapability.Utils.Lang
         * @since 8
         * @deprecated since 9
         * @useinstead util.LRUCache.getCapacity
         */
        getCapacity(): number;
        /**
         * Clears key-value pairs from this cache. The **afterRemoval()** API will be called to perform subsequent
         * operations.
         *
         * @syscap SystemCapability.Utils.Lang
         * @since 8
         * @deprecated since 9
         * @useinstead util.LRUCache.clear
         */
        clear(): void;
        /**
         * Obtains the number of return values for **createDefault()**.
         *
         * @returns { number } Number of return values for **createDefault()**.
         * @syscap SystemCapability.Utils.Lang
         * @since 8
         * @deprecated since 9
         * @useinstead util.LRUCache.getCreateCount
         */
        getCreateCount(): number;
        /**
         * Obtains the number of times that the queried values are mismatched.
         *
         * @returns { number } Number of times that the queried values are mismatched.
         * @syscap SystemCapability.Utils.Lang
         * @since 8
         * @deprecated since 9
         * @useinstead util.LRUCache.getMissCount
         */
        getMissCount(): number;
        /**
         * Obtains the number of removals from this cache.
         *
         * @returns { number } Number of removals from the cache.
         * @syscap SystemCapability.Utils.Lang
         * @since 8
         * @deprecated since 9
         * @useinstead util.LRUCache.getRemovalCount
         */
        getRemovalCount(): number;
        /**
         * Obtains the number of times that the queried values are matched.
         *
         * @returns { number } Number of times that the queried values are matched.
         * @syscap SystemCapability.Utils.Lang
         * @since 8
         * @deprecated since 9
         * @useinstead util.LRUCache.getMatchCount
         */
        getMatchCount(): number;
        /**
         * Obtains the number of additions to this cache.
         *
         * @returns { number } Number of additions to the cache.
         * @syscap SystemCapability.Utils.Lang
         * @since 8
         * @deprecated since 9
         * @useinstead util.LRUCache.getPutCount
         */
        getPutCount(): number;
        /**
         * Checks whether this cache is empty.
         *
         * @returns { boolean } Returns **true** if the cache does not contain any value.
         * @syscap SystemCapability.Utils.Lang
         * @since 8
         * @deprecated since 9
         * @useinstead util.LRUCache.isEmpty
         */
        isEmpty(): boolean;
        /**
         * Obtains the value of the specified key.
         *
         * @param { K } key - Key based on which the value is queried.
         * @returns { V | undefined } Value of the key. If no match is found, **undefined** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @since 8
         * @deprecated since 9
         * @useinstead util.LRUCache.get
         */
        get(key: K): V | undefined;
        /**
         * Adds a key-value pair to this cache.
         *
         * @param { K } key - Key of the key-value pair to add.
         * @param { V } value - Value of the key-value pair to add.
         * @returns { V } Value added. If the key already exists, the existing value is returned; if **null** is passed in
         *     for **key** or **value**, an error is thrown.
         * @syscap SystemCapability.Utils.Lang
         * @since 8
         * @deprecated since 9
         * @useinstead util.LRUCache.put
         */
        put(key: K, value: V): V;
        /**
         * Obtains all values in this cache, listed from the most to the least recently accessed.
         *
         * @returns { V[] } All values in the cache, listed from the most to the least recently accessed.
         * @syscap SystemCapability.Utils.Lang
         * @since 8
         * @deprecated since 9
         * @useinstead util.LRUCache.values
         */
        values(): V[];
        /**
         * Obtains all keys in this cache, listed from the most to the least recently accessed.
         *
         * @returns { K[] } All keys in the cache, listed from the most to the least recently accessed.
         * @syscap SystemCapability.Utils.Lang
         * @since 8
         * @deprecated since 9
         * @useinstead util.LRUCache.keys
         */
        keys(): K[];
        /**
         * Removes the specified key and its value from this cache.
         *
         * @param { K } key - Key to remove.
         * @returns { V | undefined } **Optional** object containing the removed key-value pair. If the key does not exist,
         *     an empty **Optional** object is returned; if **null** is passed in for **key**, an error is thrown.
         * @syscap SystemCapability.Utils.Lang
         * @since 8
         * @deprecated since 9
         * @useinstead util.LRUCache.remove
         */
        remove(key: K): V | undefined;
        /**
         * Performs subsequent operations after a value is removed.
         *
         * @param { boolean } isEvict - Whether the capacity is insufficient. If the value is **true**, this API is called
         *     due to insufficient capacity.
         * @param { K } key - Key removed.
         * @param { V } value - Value removed.
         * @param { V } newValue - New value for the key if the **put()** method is called and the key to be added already
         *     exists. In other cases, this parameter is left blank.
         * @syscap SystemCapability.Utils.Lang
         * @since 8
         * @deprecated since 9
         * @useinstead util.LRUCache.afterRemoval
         */
        afterRemoval(isEvict: boolean, key: K, value: V, newValue: V): void;
        /**
         * Checks whether this cache contains the specified key.
         *
         * @param { K } key - Key to check.
         * @returns { boolean } Check result. The value **true** is returned if the cache contains the specified key;
         *     otherwise, **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @since 8
         * @deprecated since 9
         * @useinstead util.LRUCache.contains
         */
        contains(key: K): boolean;
        /**
         * Creates a value if the value of the specified key is not available.
         *
         * @param { K } key - Key of which the value is missing.
         * @returns { V } Value of the key.
         * @syscap SystemCapability.Utils.Lang
         * @since 8
         * @deprecated since 9
         * @useinstead util.LRUCache.createDefault
         */
        createDefault(key: K): V;
        /**
         * Obtains a new iterator object that contains all key-value pairs in this object.
         *
         * @returns { IterableIterator<[K, V]> } Iterable array.
         * @syscap SystemCapability.Utils.Lang
         * @since 8
         * @deprecated since 9
         * @useinstead util.LRUCache.entries
         */
        entries(): IterableIterator<[
            K,
            V
        ]>;
        /**
         * Specifies the default iterator for an object.
         *
         * @returns { IterableIterator<[K, V]> } Returns a two - dimensional array in the form of key - value pairs.
         * @syscap SystemCapability.Utils.Lang
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.util.LRUCache.[Symbol.iterator]
         */
        [Symbol.iterator](): IterableIterator<[
            K,
            V
        ]>;
    }
    /**
     * Provides APIs to discard the least recently used data to make rooms for new elements when the cache is full. This
     * class uses the Least Recently Used (LRU) algorithm, which believes that the recently used data may be accessed
     * again in the near future and the least accessed data is the least valuable data and should be removed from the
     * cache.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 9
     */
    class LRUCache<K, V> {
        /**
         * A constructor used to create a **LRUCache** instance. The default capacity of the cache is 64.
         *
         * @param { number } [capacity] - Capacity of the cache to create. The default value is **64**, and the maximum
         *     value is **2147483647**. [since 12]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        constructor(capacity?: number);
        /**
         * Changes the cache capacity. If the new capacity is less than or equal to **0**, an exception will be thrown. If
         * the total number of values in the cache is greater than the specified capacity, the deletion operation is
         * performed.
         *
         * @param { number } newCapacity - New capacity of the cache. The maximum value is **2147483647**.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        updateCapacity(newCapacity: number): void;
        /**
         * Obtains the string representation of this cache.
         *
         * @returns { string } String representation of this cache.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        toString(): string;
        /**
         * Total number of values in this cache.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        length: number;
        /**
         * Obtains the capacity of this cache.
         *
         * @returns { number } Capacity of the cache.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        getCapacity(): number;
        /**
         * Clears key-value pairs from this cache.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        clear(): void;
        /**
         * Obtains the number of times that an object is created.
         *
         * @returns { number } Number of times that objects are created.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        getCreateCount(): number;
        /**
         * Obtains the number of times that the queried values are mismatched.
         *
         * @returns { number } Number of times that the queried values are mismatched.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        getMissCount(): number;
        /**
         * Obtains the number of times that key-value pairs in the cache are recycled.
         *
         * @returns { number } Number of times that key-value pairs in the cache are recycled.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        getRemovalCount(): number;
        /**
         * Obtains the number of times that the queried values are matched.
         *
         * @returns { number } Number of times that the queried values are matched.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        getMatchCount(): number;
        /**
         * Obtains the number of additions to this cache.
         *
         * @returns { number } Number of additions to the cache.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        getPutCount(): number;
        /**
         * Checks whether this cache is empty.
         *
         * @returns { boolean } Returns **true** if the cache does not contain any value.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        isEmpty(): boolean;
        /**
         * Obtains the value of a key. If the key is not in the cache,
         * [createDefault<sup>9+</sup>]{@link util.LRUCache.createDefault} is called to create the key. If the value
         * specified in **createDefault** is not **undefined**,
         * [afterRemoval<sup>9+</sup>]{@link util.LRUCache.afterRemoval} is called to return the value specified in
         * **createDefault**.
         *
         * @param { K } key - Key based on which the value is queried.
         * @returns { V | undefined } Value of the key. If no match is found, the value specified in **createDefault** is
         *     returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        get(key: K): V | undefined;
        /**
         * Adds a key-value pair to this cache and returns the value associated with the key. If the total number of values
         * in the cache is greater than the specified capacity, the deletion operation is performed.
         *
         * @param { K } key - Key of the key-value pair to add.
         * @param { V } value - Value of the key-value pair to add.
         * @returns { V } Value of the key-value pair added. If the key or value is empty, an exception is thrown.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        put(key: K, value: V): V;
        /**
         * Obtains all values in this cache, listed from the least to the most recently accessed.
         *
         * @returns { V[] } The list of all values in this cache, listed from the least to the most recently accessed.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        values(): V[];
        /**
         * Obtains all keys in this cache, listed from the least to the most recently accessed.
         *
         * @returns { K[] } The list of all keys in this cache, listed from the least to the most recently accessed.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        keys(): K[];
        /**
         * Removes a key and its associated value from this cache and returns the value associated with the key. If the key
         * does not exist, **undefined** is returned.
         *
         * @param { K } key - Key to remove.
         * @returns { V | undefined } Returns an **Optional** object containing the removed key-value pair if the key exists
         *     in the cache; returns **undefined** if the key does not exist; throws an error if **null** is passed in for
         *     **key**.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        remove(key: K): V | undefined;
        /**
         * Performs subsequent operations after a value is removed. The subsequent operations must be implemented by
         * developers. This API is called during deletion operations, such as [get<sup>9+</sup>]{@link util.LRUCache.get},
         * [put<sup>9+</sup>]{@link util.LRUCache.put}, [remove<sup>9+</sup>]{@link util.LRUCache.remove},
         * [clear<sup>9+</sup>]{@link util.LRUCache.clear}, and
         * [updateCapacity<sup>9+</sup>]{@link util.LRUCache.updateCapacity}.
         *
         * > **NOTE**
         * >
         * > If the callback method is executed after [clear<sup>9+</sup>]{@link util.LRUCache.clear} and
         * > [updateCapacity<sup>9+</sup>]{@link util.LRUCache.updateCapacity} are called and the input **key** and
         * > **value** parameters are of the MapIterator type, perform subsequent operations by referring to example 2.
         *
         * @param { boolean } isEvict - Whether the capacity is insufficient. If the value is **true**, this API is called
         *     due to insufficient capacity.
         * @param { K } key - Key removed.
         * @param { V } value - Value removed.
         * @param { V } newValue - New value for the key if the **put()** method is called and the key to be added already
         *     exists. In other cases, this parameter is left blank.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        afterRemoval(isEvict: boolean, key: K, value: V, newValue: V): void;
        /**
         * Checks whether this cache contains the specified key.
         *
         * @param { K } key - Key to check.
         * @returns { boolean } Check result. The value **true** is returned if the cache contains the specified key;
         *     otherwise, **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        contains(key: K): boolean;
        /**
         * Performs subsequent operations if no key is matched in the cache and returns the value (**undefined** by default)
         * associated with the key.
         *
         * @param { K } key - Key.
         * @returns { V } Value of the key.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        createDefault(key: K): V;
        /**
         * Returns an iterator object that traverses all key-value pairs ([key, value]) in this object in the insertion
         * order.
         *
         * @returns { IterableIterator<[K, V]> } Iterable array.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        entries(): IterableIterator<[
            K,
            V
        ]>;
        /**
         * Specifies the default iterator for an object.
         *
         * @returns { IterableIterator<[K, V]> } Returns a two - dimensional array in the form of key - value pairs.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        [Symbol.iterator](): IterableIterator<[
            K,
            V
        ]>;
    }
    /**
     * The values of the **ScopeComparable** type are used to implement the **compareTo** method. Therefore, ensure that
     * the input parameters are comparable.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 7
     */
    interface ScopeComparable {
        /**
         * Compares two values and returns a Boolean value.
         *
         * @param { ScopeComparable } other - The other value to be compared with the current value.
         * @returns { boolean } Check result. The value **true** is returned if the current value is greater than or equal
         *     to the input value; otherwise, **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        compareTo(other: ScopeComparable): boolean;
    }
    /**
     * Defines the type of values in a **Scope** object.
     *
     * @unionmember { ScopeComparable } The value type is ScopeComparable.
     * @unionmember { number } The value type is a number.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    type ScopeType = ScopeComparable | number;
    /**
     * The Scope interface is used to describe the valid range of a field.
     *
     * @syscap SystemCapability.Utils.Lang
     * @since 8
     * @deprecated since 9
     * @useinstead util.ScopeHelper
     */
    class Scope {
        /**
         * A constructor used to create a **Scope** object with the specified upper and lower limits.
         *
         * @param { ScopeType } lowerObj - Lower limit of the **Scope** object.
         * @param { ScopeType } upperObj - Upper limit of the **Scope** object.
         * @syscap SystemCapability.Utils.Lang
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.util.ScopeHelper.constructor
         */
        constructor(lowerObj: ScopeType, upperObj: ScopeType);
        /**
         * Obtains a string representation that contains this **Scope**.
         *
         * @returns { string } String representation containing the **Scope**.
         * @syscap SystemCapability.Utils.Lang
         * @since 8
         * @deprecated since 9
         * @useinstead util.LRUCache.toString
         */
        toString(): string;
        /**
         * Obtains the intersection of this **Scope** and the given **Scope**.
         *
         * @param { Scope } range - **Scope** specified.
         * @returns { Scope } Intersection of this **Scope** and the given **Scope**.
         * @syscap SystemCapability.Utils.Lang
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.util.ScopeHelper.intersect
         */
        intersect(range: Scope): Scope;
        /**
         * Obtains the intersection of this **Scope** and the given lower and upper limits.
         *
         * @param { ScopeType } lowerObj - Lower limit.
         * @param { ScopeType } upperObj - Upper limit.
         * @returns { Scope } Intersection of this **Scope** and the given lower and upper limits.
         * @syscap SystemCapability.Utils.Lang
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.util.ScopeHelper.intersect
         */
        intersect(lowerObj: ScopeType, upperObj: ScopeType): Scope;
        /**
         * Obtains the upper limit of this **Scope**.
         *
         * @returns { ScopeType } Upper limit of this **Scope**.
         * @syscap SystemCapability.Utils.Lang
         * @since 8
         * @deprecated since 9
         * @useinstead util.ScopeHelper.getUpper
         */
        getUpper(): ScopeType;
        /**
         * Obtains the lower limit of this **Scope**.
         *
         * @returns { ScopeType } Lower limit of this **Scope**.
         * @syscap SystemCapability.Utils.Lang
         * @since 8
         * @deprecated since 9
         * @useinstead util.ScopeHelper.getLower
         */
        getLower(): ScopeType;
        /**
         * Obtains the union set of this **Scope** and the given lower and upper limits.
         *
         * @param { ScopeType } lowerObj - Lower limit.
         * @param { ScopeType } upperObj - Upper limit.
         * @returns { Scope } Union set of this **Scope** and the given lower and upper limits.
         * @syscap SystemCapability.Utils.Lang
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.util.ScopeHelper.expand
         */
        expand(lowerObj: ScopeType, upperObj: ScopeType): Scope;
        /**
         * Obtains the union set of this **Scope** and the given **Scope**.
         *
         * @param { Scope } range - **Scope** specified.
         * @returns { Scope } Union set of this **Scope** and the given **Scope**.
         * @syscap SystemCapability.Utils.Lang
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.util.ScopeHelper.expand
         */
        expand(range: Scope): Scope;
        /**
         * Obtains the union set of this **Scope** and the given value.
         *
         * @param { ScopeType } value - Value specified.
         * @returns { Scope } Union set of this **Scope** and the given value.
         * @syscap SystemCapability.Utils.Lang
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.util.ScopeHelper.expand
         */
        expand(value: ScopeType): Scope;
        /**
         * Checks whether a value is within this **Scope**.
         *
         * @param { ScopeType } value - Value specified.
         * @returns { boolean } Check result. The value **true** is returned if the value is within this **Scope**;
         *     otherwise, **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @since 8
         * @deprecated since 9
         * @useinstead util.LRUCache.contains
         */
        contains(value: ScopeType): boolean;
        /**
         * Checks whether a range is within this **Scope**.
         *
         * @param { Scope } range - **Scope** specified.
         * @returns { boolean } Check result. The value **true** is returned if the range is within this **Scope**;
         *     otherwise, **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @since 8
         * @deprecated since 9
         * @useinstead util.LRUCache.contains
         */
        contains(range: Scope): boolean;
        /**
         * Limits a value to this **Scope**.
         *
         * @param { ScopeType } value - Value specified.
         * @returns { ScopeType } Returns **lowerObj** if the specified value is less than the lower limit; returns
         *     **upperObj** if the specified value is greater than the upper limit; returns the specified value if it is
         *     within this **Scope**.
         * @syscap SystemCapability.Utils.Lang
         * @since 8
         * @deprecated since 9
         * @useinstead util.ScopeHelper.clamp
         */
        clamp(value: ScopeType): ScopeType;
    }
    /**
     * Provides APIs to define the valid range of a field. The constructor of this class creates comparable objects with
     * lower and upper limits.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 9
     */
    class ScopeHelper {
        /**
         * A constructor used to create a **ScopeHelper** object with the specified upper and lower limits.
         *
         * @param { ScopeType } lowerObj - Lower limit of the **Scope** object.
         * @param { ScopeType } upperObj - Upper limit of the **Scope** object.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        constructor(lowerObj: ScopeType, upperObj: ScopeType);
        /**
         * Obtains a string representation that contains this **Scope**.
         *
         * @returns { string } String representation containing the **Scope**.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        toString(): string;
        /**
         * Obtains the intersection of this **Scope** and the given **Scope**. If the intersection is empty, an exception is
         * thrown.
         *
         * @param { ScopeHelper } range - **Scope** specified.
         * @returns { ScopeHelper } Intersection of this **Scope** and the given **Scope**.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        intersect(range: ScopeHelper): ScopeHelper;
        /**
         * Obtains the intersection of this **Scope** and the given lower and upper limits. If the intersection is empty, an
         * exception is thrown.
         *
         * @param { ScopeType } lowerObj - Lower limit.
         * @param { ScopeType } upperObj - Upper limit.
         * @returns { ScopeHelper } Intersection of this **Scope** and the given lower and upper limits.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        intersect(lowerObj: ScopeType, upperObj: ScopeType): ScopeHelper;
        /**
         * Obtains the upper limit of this **Scope**.
         *
         * @returns { ScopeType } Upper limit of this **Scope**.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        getUpper(): ScopeType;
        /**
         * Obtains the lower limit of this **Scope**.
         *
         * @returns { ScopeType } Lower limit of this **Scope**.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        getLower(): ScopeType;
        /**
         * Obtains the union set of this **Scope** and the given lower and upper limits.
         *
         * @param { ScopeType } lowerObj - Lower limit.
         * @param { ScopeType } upperObj - Upper limit.
         * @returns { ScopeHelper } Union set of this **Scope** and the given lower and upper limits.
         * @syscap SystemCapability.Utils.Lang
         * @atomicservice [since 12]
         * @since 9
         */
        expand(lowerObj: ScopeType, upperObj: ScopeType): ScopeHelper;
        /**
         * Obtains the union set of this **Scope** and the given **Scope**.
         *
         * @param { ScopeHelper } range - **Scope** specified.
         * @returns { ScopeHelper } Union set of this **Scope** and the given **Scope**.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        expand(range: ScopeHelper): ScopeHelper;
        /**
         * Obtains the union set of this **Scope** and the given value.
         *
         * @param { ScopeType } value - Value specified.
         * @returns { ScopeHelper } Union set of this **Scope** and the given value.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        expand(value: ScopeType): ScopeHelper;
        /**
         * Checks whether a range is within this **Scope**.
         *
         * @param { ScopeType } value - Value specified.
         * @returns { boolean } Check result. The value **true** is returned if the value is within this **Scope**;
         *     otherwise, **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        contains(value: ScopeType): boolean;
        /**
         * Checks whether a range is within this **Scope**.
         *
         * @param { ScopeHelper } range - **Scope** specified.
         * @returns { boolean } Check result. The value **true** is returned if the range is within this **Scope**;
         *     otherwise, **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        contains(range: ScopeHelper): boolean;
        /**
         * Limits a value to this **Scope**.
         *
         * @param { ScopeType } value - Value specified.
         * @returns { ScopeType } Returns **lowerObj** if the specified value is less than the lower limit; returns
         *     **upperObj** if the specified value is greater than the upper limit; returns the specified value if it is
         *     within this **Scope**.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        clamp(value: ScopeType): ScopeType;
    }
    /**
     * Decodes a string or Uint8Array containing Base64 data into a newly allocated Uint8Array.
     *
     * @syscap SystemCapability.Utils.Lang
     * @since 8
     * @deprecated since 9
     * @useinstead util.Base64Helper
     */
    class Base64 {
        /**
         * A constructor used to create a **Base64** object.
         *
         * @syscap SystemCapability.Utils.Lang
         * @since 8
         * @deprecated since 9
         * @useinstead util.Base64Helper.constructor
         */
        constructor();
        /**
         * Performs Base64 encoding on the input Uint8Array byte array and returns the encoded Uint8Array.
         *
         * @param { Uint8Array } src - Uint8Array object to encode.
         * @returns { Uint8Array } Uint8Array object obtained.
         * @syscap SystemCapability.Utils.Lang
         * @since 8
         * @deprecated since 9
         * @useinstead util.Base64Helper.encodeSync
         */
        encodeSync(src: Uint8Array): Uint8Array;
        /**
         * Performs Base64 encoding on the input Uint8Array byte array and returns the encoded string.
         *
         * @param { Uint8Array } src - Uint8Array object to encode.
         * @returns { string } String obtained.
         * @syscap SystemCapability.Utils.Lang
         * @since 8
         * @deprecated since 9
         * @useinstead util.Base64Helper.encodeToStringSync
         */
        encodeToStringSync(src: Uint8Array): string;
        /**
         * Decodes the input content into a Uint8Array object.
         *
         * @param { Uint8Array | string } src - Uint8Array object or string to decode.
         * @returns { Uint8Array } Uint8Array object obtained.
         * @syscap SystemCapability.Utils.Lang
         * @since 8
         * @deprecated since 9
         * @useinstead util.Base64Helper.decodeSync
         */
        decodeSync(src: Uint8Array | string): Uint8Array;
        /**
         * Encodes the input content into a Uint8Array object. This API uses a promise to return the result.
         *
         * @param { Uint8Array } src - Uint8Array object to encode.
         * @returns { Promise<Uint8Array> } Promise used to return the Uint8Array object obtained.
         * @syscap SystemCapability.Utils.Lang
         * @since 8
         * @deprecated since 9
         * @useinstead util.Base64Helper.encode
         */
        encode(src: Uint8Array): Promise<Uint8Array>;
        /**
         * Encodes the input content into a string. This API uses a promise to return the result.
         *
         * @param { Uint8Array } src - Uint8Array object to encode.
         * @returns { Promise<string> } Promise used to return the string obtained.
         * @syscap SystemCapability.Utils.Lang
         * @since 8
         * @deprecated since 9
         * @useinstead util.Base64Helper.encodeToString
         */
        encodeToString(src: Uint8Array): Promise<string>;
        /**
         * Decodes the input content into a Uint8Array object. This API uses a promise to return the result.
         *
         * @param { Uint8Array | string } src - Uint8Array object or string to decode.
         * @returns { Promise<Uint8Array> } Promise used to return the Uint8Array object obtained.
         * @syscap SystemCapability.Utils.Lang
         * @since 8
         * @deprecated since 9
         * @useinstead util.Base64Helper.decode
         */
        decode(src: Uint8Array | string): Promise<Uint8Array>;
    }
    /**
     * Enumerates the Base64 encoding formats.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice [since 11]
     * @since 10
     */
    enum Type {
        /**
         * Basic format.
         * This API can be used in atomic services since API version 11.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice [since 11]
         * @since 10
         */
        BASIC = 0,
        /**
         * MIME format.
         * This API can be used in atomic services since API version 11.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice [since 11]
         * @since 10
         */
        MIME = 1,
        /**
         * BASIC_URL_SAFE format.
         *
         * This value is supported since API version 12.
         * This API can be used in atomic services since API version 12.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        BASIC_URL_SAFE = 2,
        /**
         * MIME_URL_SAFE format.
         *
         * This value is supported since API version 12.
         * This API can be used in atomic services since API version 12.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        MIME_URL_SAFE = 3
    }
    /**
     * Provides encoding and decoding for Base64 and Base64URL. The Base64 encoding table contains 64 characters, which
     * are the uppercase letters (A-Z), lowercase letters (a-z), digits (0-9), and the special characters plus sign (+)
     * and slash (/). During encoding, the original data is divided into groups of three bytes, and each group contains a
     * 6-bit number. Then, the corresponding characters in the Base64 encoding table are used to represent these numbers.
     * If the last group contains only one or two bytes, the equal sign (=) is used for padding. The Base64URL encoding
     * table contains 64 characters, which are the uppercase letters (A-Z), lowercase letters (a-z), digits (0-9), and the
     * special characters plus sign (+) and slash (/). The Base64URL encoding result does not contain equal signs (=).
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    class Base64Helper {
        /**
         * A constructor used to create a **Base64Helper** instance.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        constructor();
        /**
         * Encodes the input content into a Uint8Array object.
         *
         * @param { Uint8Array } src - Uint8Array object to encode.
         * @param { Type } [options] - Encoding format.<br>The following values are available:<br>- **util.Type.BASIC** (
         *     default): Base64 encoding.<br>- **util.Type.BASIC_URL_SAFE**: Base64URL encoding. [since 12]
         * @returns { Uint8Array } Uint8Array object obtained.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        encodeSync(src: Uint8Array, options?: Type): Uint8Array;
        /**
         * Performs Base64 encoding on the input Uint8Array byte array and returns a string. This method supports multiple
         * encoding formats, including standard Base64 encoding, MIME-compliant Base64 encoding (with line breaks), and URL-
         * safe Base64 encoding.
         *
         * @param { Uint8Array } src - Uint8Array object to encode.
         * @param { Type } [options] - Encoding format.<br>The following values are available:<br>- **util.Type.BASIC** (
         *     default): Base64 encoding. The return value does not contain carriage return characters or newline
         *     characters.<br>- **util.Type.MIME**: Base64 encoding. If the return value exceeds 76 characters, a line break
         *     is inserted every 76 characters, and each line ends with '\r\n'. If the return value is fewer than 76
         *     characters, an exception is thrown.<br>- **util.Type.BASIC_URL_SAFE**: Base64URL encoding. The return value
         *     does not contain carriage return characters or newline characters.<br>- **util.Type.MIME_URL_SAFE**: Base64
         *     URL encoding. Each line in the return value contains a maximum of 76 characters and ends with '\r\n'.
         *     [since 10 - 11]
         * @param { Type } options - Encoding format.<br>The following values are available:<br>- **util.Type.BASIC** (
         *     default): Base64 encoding. The return value does not contain carriage return characters or newline
         *     characters.<br>- **util.Type.MIME**: Base64 encoding. If the return value exceeds 76 characters, a line break
         *     is inserted every 76 characters, and each line ends with '\r\n'. If the return value is fewer than 76
         *     characters, an exception is thrown.<br>- **util.Type.BASIC_URL_SAFE**: Base64URL encoding. The return value
         *     does not contain carriage return characters or newline characters.<br>- **util.Type.MIME_URL_SAFE**: Base64
         *     URL encoding. Each line in the return value contains a maximum of 76 characters and ends with '\r\n'.
         *     [since 12]
         * @returns { string } String obtained.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        encodeToStringSync(src: Uint8Array, options?: Type): string;
        /**
         * Decodes a string into a Uint8Array object. This API returns the result synchronously.
         *
         * @param { Uint8Array | string } src - Uint8Array object or string to decode.
         * @param { Type } [options] - Decoding format.<br>The following values are available:<br>- **util.Type.BASIC** (
         *     default): Base64 decoding.<br>- **util.Type.MIME**: Base64 decoding. The input parameter **src** contains
         *     carriage return characters and newline characters.<br>- **util.Type.BASIC_URL_SAFE**: Base64URL decoding.<br>
         *     - **util.Type.MIME_URL_SAFE**: Base64 URL decoding. The input parameter **src** contains carriage return
         *     characters and newline characters. [since 10]
         * @returns { Uint8Array } Uint8Array object obtained.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        decodeSync(src: Uint8Array | string, options?: Type): Uint8Array;
        /**
         * Encodes the input content into a Uint8Array object. This API uses a promise to return the result.
         *
         * @param { Uint8Array } src - Uint8Array object to encode.
         * @param { Type } [options] - Encoding format.<br>The following values are available:<br>- **util.Type.BASIC** (
         *     default): Base64 encoding.<br>- **util.Type.BASIC_URL_SAFE**: Base64URL encoding. [since 12]
         * @returns { Promise<Uint8Array> } Promise used to return the Uint8Array object obtained.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        encode(src: Uint8Array, options?: Type): Promise<Uint8Array>;
        /**
         * Encodes the input content into a string. This API uses a promise to return the result.
         *
         * @param { Uint8Array } src - Uint8Array object to encode.
         * @param { Type } [options] - Encoding format.<br>The following values are available:<br>- **util.Type.BASIC** (
         *     default): Base64 encoding. The return value does not contain carriage return characters or newline
         *     characters.<br>- **util.Type.MIME**: Base64 encoding. Each line of the return value contains a maximum of 76
         *     characters and ends with '\r\n'.<br>- **util.Type.BASIC_URL_SAFE**: Base64URL encoding. The return value does
         *     not contain carriage return characters or newline characters.<br>- **util.Type.MIME_URL_SAFE**: Base64URL
         *     encoding. Each line in the return value contains a maximum of 76 characters and ends with '\r\n'. [since 10]
         * @returns { Promise<string> } Promise used to return the string obtained.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        encodeToString(src: Uint8Array, options?: Type): Promise<string>;
        /**
         * Decodes the input content into a Uint8Array object. This API uses a promise to return the result.
         *
         * @param { Uint8Array | string } src - Uint8Array object or string to decode.
         * @param { Type } [options] - Decoding format.<br>The following values are available:<br>- **util.Type.BASIC** (
         *     default): Base64 decoding.<br>- **util.Type.MIME**: Base64 decoding. The input parameter **src** contains
         *     carriage return characters and newline characters.<br>- **util.Type.BASIC_URL_SAFE**: Base64URL decoding.<br>
         *     - **util.Type.MIME_URL_SAFE**: Base64 URL decoding. The input parameter **src** contains carriage return
         *     characters and newline characters. [since 10]
         * @returns { Promise<Uint8Array> } Promise used to return the Uint8Array object obtained.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 9
         */
        decode(src: Uint8Array | string, options?: Type): Promise<Uint8Array>;
    }
    /**
     * Provides APIs to check different types of built-in objects, such as ArrayBuffer, Map, and Set, so as to avoid
     * exceptions caused by type errors.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 12]
     * @since 8
     */
    class types {
        /**
         * A constructor used to create a **Types** object.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        constructor();
        /**
         * Checks whether the value is of the ArrayBuffer or SharedArrayBuffer type.
         *
         * @param { Object } value - Object to check.
         * @returns { boolean } Check result. The value **true** is returned if the value is of the ArrayBuffer or
         *     SharedArrayBuffer type; otherwise, **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        isAnyArrayBuffer(value: Object): boolean;
        /**
         * Checks whether the value is of the ArrayBufferView type.
         *
         * @param { Object } value - Object to check.
         * @returns { boolean } Check result. The value **true** is returned if the value is of the ArrayBufferView type;
         *     otherwise, **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        isArrayBufferView(value: Object): boolean;
        /**
         * Checks whether the value is an **arguments** object.
         *
         * @param { Object } value - Object to check.
         * @returns { boolean } Check result. The value **true** is returned if the value is an **arguments** object;
         *     otherwise, **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        isArgumentsObject(value: Object): boolean;
        /**
         * Checks whether the value is of the ArrayBuffer type.
         *
         * @param { Object } value - Object to check.
         * @returns { boolean } Check result. The value **true** is returned if the value is of the ArrayBuffer type;
         *     otherwise, **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        isArrayBuffer(value: Object): boolean;
        /**
         * Checks whether the value is an asynchronous function.
         *
         * @param { Object } value - Object to check.
         * @returns { boolean } Check result. The value **true** is returned if the value is an asynchronous function;
         *     otherwise, **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        isAsyncFunction(value: Object): boolean;
        /**
         * Checks whether the value is of the BigInt64Array type.
         *
         * @param { Object } value - Object to check.
         * @returns { boolean } Check result. The value **true** is returned if the value is of the BigInt64Array type;
         *     otherwise, **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        isBigInt64Array(value: Object): boolean;
        /**
         * Checks whether the value is of the BigUint64Array type.
         *
         * @param { Object } value - Object to check.
         * @returns { boolean } Check result. The value **true** is returned if the value is of the BigUint64Array type;
         *     otherwise, **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        isBigUint64Array(value: Object): boolean;
        /**
         * Checks whether the value is of the Boolean type.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 8 and deprecated since API version 14. No substitute is provided.
         *
         * @param { Object } value - Object to check.
         * @returns { boolean } Check result. The value **true** is returned if the value is of the Boolean type; otherwise,
         *     **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         * @deprecated since 14
         */
        isBooleanObject(value: Object): boolean;
        /**
         * Checks whether the value is of the Boolean, Number, String, or Symbol type.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 8 and deprecated since API version 14. No substitute is provided.
         *
         * @param { Object } value - Object to check.
         * @returns { boolean } Check result. The value **true** is returned if the value is of the Boolean, Number, String,
         *     or Symbol type; otherwise, **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         * @deprecated since 14
         */
        isBoxedPrimitive(value: Object): boolean;
        /**
         * Checks whether the value is of the DataView type.
         *
         * @param { Object } value - Object to check.
         * @returns { boolean } Check result. The value **true** is returned if the value is of the DataView type; otherwise
         *     , **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        isDataView(value: Object): boolean;
        /**
         * Checks whether the value is of the Date type.
         *
         * @param { Object } value - Object to check.
         * @returns { boolean } Check result. The value **true** is returned if the value is of the Date type; otherwise,
         *     **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        isDate(value: Object): boolean;
        /**
         * Checks whether the value is of the native external type.
         *
         * @param { Object } value - Object to check.
         * @returns { boolean } Check result. The value **true** is returned if the value is of the native external type;
         *     otherwise, **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        isExternal(value: Object): boolean;
        /**
         * Checks whether the value is of the Float32Array type.
         *
         * @param { Object } value - Object to check.
         * @returns { boolean } Check result. The value **true** is returned if the value is of the Float32Array type;
         *     otherwise, **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        isFloat32Array(value: Object): boolean;
        /**
         * Checks whether the value is of the Float64Array type.
         *
         * @param { Object } value - Object to check.
         * @returns { boolean } Check result. The value **true** is returned if the value is of the Float64Array type;
         *     otherwise, **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        isFloat64Array(value: Object): boolean;
        /**
         * Checks whether the value is a generator function.
         *
         * @param { Object } value - Object to check.
         * @returns { boolean } Check result. The value **true** is returned if the value is a generator function; otherwise
         *     , **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        isGeneratorFunction(value: Object): boolean;
        /**
         * Checks whether the value is a generator object.
         *
         * @param { Object } value - Object to check.
         * @returns { boolean } Check result. The value **true** is returned if the value is a generator object; otherwise,
         *     **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        isGeneratorObject(value: Object): boolean;
        /**
         * Checks whether the value is of the Int8Array type.
         *
         * @param { Object } value - Object to check.
         * @returns { boolean } Check result. The value **true** is returned if the value is of the Int8Array type;
         *     otherwise, **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        isInt8Array(value: Object): boolean;
        /**
         * Checks whether the value is of the Int16Array type.
         *
         * @param { Object } value - Object to check.
         * @returns { boolean } Check result. The value **true** is returned if the value is of the Int16Array type;
         *     otherwise, **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        isInt16Array(value: Object): boolean;
        /**
         * Checks whether the value is of the Int32Array type.
         *
         * @param { Object } value - Object to check.
         * @returns { boolean } Check result. The value **true** is returned if the value is of the Int32Array type;
         *     otherwise, **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        isInt32Array(value: Object): boolean;
        /**
         * Checks whether the value is of the Map type.
         *
         * @param { Object } value - Object to check.
         * @returns { boolean } Check result. The value **true** is returned if the value is of the Map type; otherwise,
         *     **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        isMap(value: Object): boolean;
        /**
         * Checks whether the value is of the MapIterator type.
         *
         * @param { Object } value - Object to check.
         * @returns { boolean } Check result. The value **true** is returned if the value is of the MapIterator type;
         *     otherwise, **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        isMapIterator(value: Object): boolean;
        /**
         * Checks whether the value is a module namespace object.
         *
         * @param { Object } value - Object to check.
         * @returns { boolean } Check result. The value **true** is returned if the value is a module namespace object;
         *     otherwise, **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        isModuleNamespaceObject(value: Object): boolean;
        /**
         * Checks whether the value is of the Error type.
         *
         * @param { Object } value - Object to check.
         * @returns { boolean } Check result. The value **true** is returned if the value is of the Error type; otherwise,
         *     **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        isNativeError(value: Object): boolean;
        /**
         * Checks whether the value is of the Number type.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 8 and deprecated since API version 14. No substitute is provided.
         *
         * @param { Object } value - Object to check.
         * @returns { boolean } Check result. The value **true** is returned if the value is of the Number type; otherwise,
         *     **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         * @deprecated since 14
         */
        isNumberObject(value: Object): boolean;
        /**
         * Checks whether the value is a promise.
         *
         * @param { Object } value - Object to check.
         * @returns { boolean } Check result. The value **true** is returned if the value is a promise; otherwise, **false**
         *     is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        isPromise(value: Object): boolean;
        /**
         * Checks whether the value is a proxy.
         *
         * @param { Object } value - Object to check.
         * @returns { boolean } Check result. The value **true** is returned if the value is a proxy; otherwise, **false**
         *     is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        isProxy(value: Object): boolean;
        /**
         * Checks whether the value is of the RegExp type.
         *
         * @param { Object } value - Object to check.
         * @returns { boolean } Check result. The value **true** is returned if the value is of the RegExp type; otherwise,
         *     **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        isRegExp(value: Object): boolean;
        /**
         * Checks whether the value is of the Set type.
         *
         * @param { Object } value - Object to check.
         * @returns { boolean } Check result. The value **true** is returned if the value is of the Set type; otherwise,
         *     **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        isSet(value: Object): boolean;
        /**
         * Checks whether the value is of the SetIterator type.
         *
         * @param { Object } value - Object to check.
         * @returns { boolean } Check result. The value **true** is returned if the value is of the SetIterator type;
         *     otherwise, **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        isSetIterator(value: Object): boolean;
        /**
         * Checks whether the value is of the SharedArrayBuffer type.
         *
         * @param { Object } value - Object to check.
         * @returns { boolean } Check result. The value **true** is returned if the value is of the SharedArrayBuffer type;
         *     otherwise, **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        isSharedArrayBuffer(value: Object): boolean;
        /**
         * Checks whether the value is a string object.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 8 and deprecated since API version 14. No substitute is provided.
         *
         * @param { Object } value - Object to check.
         * @returns { boolean } Check result. The value **true** is returned if the value is a string object; otherwise,
         *     **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         * @deprecated since 14
         */
        isStringObject(value: Object): boolean;
        /**
         * Checks whether the value is a symbol object.
         *
         * > **NOTE**
         * >
         * > This API is supported since API version 8 and deprecated since API version 14. No substitute is provided.
         *
         * @param { Object } value - Object to check.
         * @returns { boolean } Check result. The value **true** is returned if the value is a symbol object; otherwise,
         *     **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         * @deprecated since 14
         */
        isSymbolObject(value: Object): boolean;
        /**
         * Checks whether the value is of the TypedArray type.
         *
         * @param { Object } value - Object to check.
         * @returns { boolean } Check result. The value **true** is returned if the value is of the TypedArray type;
         *     otherwise, **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        isTypedArray(value: Object): boolean;
        /**
         * Checks whether the value is of the Uint8Array type.
         *
         * @param { Object } value - Object to check.
         * @returns { boolean } Check result. The value **true** is returned if the value is of the Uint8Array type;
         *     otherwise, **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        isUint8Array(value: Object): boolean;
        /**
         * Checks whether the value is of the Uint8ClampedArray type.
         *
         * @param { Object } value - Object to check.
         * @returns { boolean } Check result. The value **true** is returned if the value is of the Uint8ClampedArray type;
         *     otherwise, **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        isUint8ClampedArray(value: Object): boolean;
        /**
         * Checks whether the value is of the Uint16Array type.
         *
         * @param { Object } value - Object to check.
         * @returns { boolean } Check result. The value **true** is returned if the value is of the Uint16Array type;
         *     otherwise, **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        isUint16Array(value: Object): boolean;
        /**
         * Checks whether the value is of the Uint32Array type.
         *
         * @param { Object } value - Object to check.
         * @returns { boolean } Check result. The value **true** is returned if the value is of the Uint32Array type;
         *     otherwise, **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        isUint32Array(value: Object): boolean;
        /**
         * Checks whether the value is of the WeakMap type.
         *
         * @param { Object } value - Object to check.
         * @returns { boolean } Check result. The value **true** is returned if the value is of the WeakMap type; otherwise,
         *     **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        isWeakMap(value: Object): boolean;
        /**
         * Checks whether the value is of the WeakSet type.
         *
         * @param { Object } value - Object to check.
         * @returns { boolean } Check result. The value **true** is returned if the value is of the WeakSet type; otherwise,
         *     **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 12]
         * @since 8
         */
        isWeakSet(value: Object): boolean;
    }
    /**
     * Provides APIs that support Aspect Oriented Programming (AOP). These APIs can be used to perform instrumentation or
     * replacement on class methods.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice [since 12]
     * @since 11
     */
    class Aspect {
        /**
         * Inserts a function before a method of a class object. The inserted function is executed in prior to the original
         * method of the class object.
         *
         * @param { Object } targetClass - Target class object.
         * @param { string } methodName - Name of the method. Read-only methods are not supported.
         * @param { boolean } isStatic - Whether the method is a static method. The value **true** means a static method,
         *     and **false** means an instance method.
         * @param { Function } before - Function to insert. If the function carries parameters, then the first parameter is
         *     the **this** object, which is the target class object (specified by **targetClass**) if **isStatic** is
         *     **true** or the instance object of the method if **isStatic** is **false**; other parameters are the
         *     parameters carried in the original method. If the function does not carry any parameter, no processing is
         *     performed.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        static addBefore(targetClass: Object, methodName: string, isStatic: boolean, before: Function): void;
        /**
         * Inserts a function after a method of a class object. The final return value is the return value of the function
         * inserted.
         *
         * @param { Object } targetClass - Target class object.
         * @param { string } methodName - Name of the method. Read-only methods are not supported.
         * @param { boolean } isStatic - Whether the method is a static method. The value **true** means a static method,
         *     and **false** means an instance method.
         * @param { Function } after - Function to insert. If the function carries parameters, then the first parameter is
         *     the **this** object, which is the target class object (specified by **targetClass**) if **isStatic** is
         *     **true** or the instance object of the method if **isStatic** is **false**; the second parameter is the
         *     return value of the original method (**undefined** if the original method does not have a return value);
         *     other parameters are the parameters carried by the original method. If the function does not carry any
         *     parameter, no processing is performed.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        static addAfter(targetClass: Object, methodName: string, isStatic: boolean, after: Function): void;
        /**
         * Replaces a method of a class object with another function. After the replacement, only the new function logic is
         * executed. The final return value is the return value of the new function.
         *
         * @param { Object } targetClass - Target class object.
         * @param { string } methodName - Name of the method. Read-only methods are not supported.
         * @param { boolean } isStatic - Whether the method is a static method. The value **true** means a static method,
         *     and **false** means an instance method.
         * @param { Function } instead - Function to be used replacement. If the function carries parameters, then the first
         *     parameter is the **this** object, which is the target class object (specified by **targetClass**) if
         *     **isStatic** is **true** or the instance object of the method if **isStatic** is **false**; other parameters
         *     are the parameters carried in the original method. If the function does not carry any parameter, no
         *     processing is performed.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice [since 12]
         * @since 11
         */
        static replace(targetClass: Object, methodName: string, isStatic: boolean, instead: Function): void;
    }
    /**
     * Provides the capability of decoding binary streams into strings. The following encoding types are supported: utf-8,
     * iso-8859-2, koi8-r, macintosh, windows-1250, windows-1251, gbk, gb18030, big5, utf-16be, and UTF-16le.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    class StringDecoder {
        /**
         * Constructor used to create a **StringDecoder** instance.
         *
         * @param { string } [encoding] - Encoding type of the input data. The default value is **utf-8**.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        constructor(encoding?: string);
        /**
         * Decodes a string. Any incomplete multi-byte characters at the end of Uint8Array are filtered out from the
         * returned string and stored in an internal buffer for the next call.
         *
         * @param { string | Uint8Array } chunk - String to decode. Decoding is performed based on the input encoding type.
         *     If the input is of the Uint8Array type, decoding is performed normally. If the input is of the string type,
         *     the parameter is directly returned.
         * @returns { string } String decoded.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        write(chunk: string | Uint8Array): string;
        /**
         * Ends the decoding process and returns any remaining input stored in the internal buffer as a string.
         *
         * @param { string | Uint8Array } [chunk] - String to decode. The default value is **undefined**.
         * @returns { string } String decoded.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        end(chunk?: string | Uint8Array): string;
    }
    /**
     * Obtains the stack trace information of the main thread. A maximum of 64 call frames can be returned.
     * This API may affect the performance of the main thread. You are advised to use this API only when necessary, such
     * as in log recording, error analysis, or debugging scenarios.
     *
     * @returns { string } Stack trace information of the main thread. If the main thread is not executing JavaScript code
     *     , an empty string is returned.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice
     * @since 20
     */
    function getMainThreadStackTrace(): string;
    /**
     * Provides an interface that can be implemented for releasing a resource
     * which is managed by developers through a developer-defined callback.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice
     * @since 22
     */
    interface AutoFinalizer<T> {
        /**
         * The developer-defined callback used to release resources.
         *
         * @param { T } heldValue - The value to pass to the finalizer.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 22
         */
        onFinalization(heldValue: T): void;
    }
    /**
     * A cleaner for releasing resources managed by developers through a developer-defined callback.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice
     * @since 22
     */
    class AutoFinalizerCleaner<T> {
        /**
         * Register objects that release resources managed by developers.
         *
         * @param { AutoFinalizer<T> } obj - The object is registered to the cleaner.
         * @param { T } heldValue - The value to pass to the finalizer.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 22
         */
        static register<T>(obj: AutoFinalizer<T>, heldValue: T): void;
    }
    /**
     * Multi-thread detection functional parameter configuration
     *
     * @syscap SystemCapability.Utils.Lang
     * @stagemodelonly
     * @crossplatform
     * @since 26.0.0
     */
    interface MultithreadingDetectionOptions {
        /**
         * If abort is **true**, the application will crash, if abort is **false**, the application will not crash.
         * Default **true**.
         *
         * @syscap SystemCapability.Utils.Lang
         * @stagemodelonly
         * @crossplatform
         * @since 26.0.0
         */
        abort?: boolean;
        /**
         * The sampling frequency of multi-thread detection
         * The value must be an integer, minimum is **100**, maxmium is **2147483647**. (default **100**)
         * The value should be an integer.
         *
         * @syscap SystemCapability.Utils.Lang
         * @stagemodelonly
         * @crossplatform
         * @since 26.0.0
         */
        frequency?: number;
        /**
         * The interval of multi-thread detection(min)
         * Errors will be reported again only if the time since the last detection exceeds this interval.
         * The value must be an integer within [0,1440] (default 5min).
         *
         * @syscap SystemCapability.Utils.Lang
         * @stagemodelonly
         * @crossplatform
         * @since 26.0.0
         */
        interval?: number;
    }
    /**
     * A class that provides VM maintenance and test capabilities for developers.
     *
     * @syscap SystemCapability.Utils.Lang
     * @stagemodelonly
     * @crossplatform
     * @since 23
     */
    class ArkTSVM {
        /**
         * Sets whether to enable multithreading detection. When **enabled** is set to **true**, the detection is turned on,
         * and multithreading-related details will be included in the cppcrash files generated for multithreading issues.
         * When **enabled** is set to **false**, the detection is turned off, and no such details will be present in the
         * corresponding cppcrash files.
         *
         * @param { boolean } enabled - Controls whether to enable multithreading detection. **true** means enabling the
         *     detection, and **false** means disabling it.
         * @param { MultithreadingDetectionOptions } [options] - Optional configuration items [since 26.0.0]
         * @syscap SystemCapability.Utils.Lang
         * @stagemodelonly
         * @crossplatform
         * @since 23
         */
        static setMultithreadingDetectionEnabled(enabled: boolean, options?: MultithreadingDetectionOptions): void;
        /**
         * Register a callback that is triggered if the heap memory exceeds the critical warning threshold after a GC.
         * It must be called on the main thread and only one callback can be registered.
         *
         * NOTE:
         * There is no guarantee that the callback will be triggered before OOM.
         *
         * @param { Callback<string> } callback - This callback is triggered if the memory reaches the threshold after a GC.
         *     The string parameter indicates the type of memory pressure event:
         *     "LocalHeapMemPressure", "SharedHeapMemPressure", or "ProcessHeapMemPressure".
         * @param { HeapMemoryThreshold } heapMemoryThreshold - Indicates
         *     the percentage threshold of the heap memory to trigger the callback after a GC. The value range is [70, 95].
         * @returns { boolean } Returns {@code true} if the registration succeeds;
         *     returns {@code false} if not called on the main thread or if the callback is already registered.
         * @static
         * @syscap SystemCapability.Utils.Lang
         * @stagemodelonly
         * @since 24
         */
        static onVMHeapMemoryPressure(callback: Callback<string>, heapMemoryThreshold: HeapMemoryThreshold): boolean;
        /**
         * Unregister the callback that is triggered when the heap memory exceeds the critical warning threshold after a GC.
         *
         * @static
         * @syscap SystemCapability.Utils.Lang
         * @stagemodelonly
         * @since 24
         */
        static offVMHeapMemoryPressure(): void;
        /**
         * Get all heap memory information from ArkTS-VMs and the shared heap.
         *
         * @returns { Promise<HeapMemoryInfo[]> } Returns a promise containing all the heap memory information
         *     from ArkTS-VMs' local heap and the shared heap.
         * @syscap SystemCapability.Utils.Lang
         * @stagemodelonly
         * @since 24
         */
        static getAllVMHeapMemoryInfo(): Promise<HeapMemoryInfo[]>;
        /**
         * Enable the local handle detection to avoid memory leakage in the event looper of Libuv or EventHandler.
         *
         * @syscap SystemCapability.Utils.Lang
         * @stagemodelonly
         * @crossplatform
         * @since 24
         */
        static enableLocalHandleDetection(): void;
        /**
         * Enable or disable tracking of the relationship between napi_ref and global handle. When enabled, heap snapshot
         * will include native reference address information. When disabled (enable is false), the tracking will be stopped
         * and heap snapshot will not display the relationship between native reference and global handle.
         *
         * @param { boolean } enable - The boolean flag enable to Indicates whether to turn on or off tracking, **true** means
         *                           to turn on tracking, and **false** means to turn off it.
         * @syscap SystemCapability.Utils.Lang
         * @stagemodelonly
         * @crossplatform
         * @since 26.0.0
         */
        static setTrackGlobalRef(enable: boolean): void;
    }
    /**
     * Describes heap memory information of either an ArkTS-VM, or the shared heap memory of current process.
     *
     * @syscap SystemCapability.Utils.Lang
     * @stagemodelonly
     * @since 24
     */
    interface HeapMemoryInfo {
        /**
         * If this memory information describes an ArkTS-VM local heap,
         * the value is a number representing the running thread;
         * If this memory information describes the shared heap, the value is undefined.
         *
         * @syscap SystemCapability.Utils.Lang
         * @stagemodelonly
         * @since 24
         */
        threadId?: number;
        /**
         * If this memory information describes an ArkTS-VM local heap,
         * the value is a string representing the name of the running thread;
         * If this memory information describes the shared heap, the value is undefined.
         *
         * @syscap SystemCapability.Utils.Lang
         * @stagemodelonly
         * @since 24
         */
        threadName?: string;
        /**
         * The value is a string representing whether this memory information is from an ArkTS-VM local heap,
         * or the shared heap.
         *
         * @syscap SystemCapability.Utils.Lang
         * @stagemodelonly
         * @since 24
         */
        heapType: string;
        /**
         * The value is a number representing the total size of all heap objects in KB, from either an ArkTS-VM local heap
         * or the shared heap.
         *
         * @syscap SystemCapability.Utils.Lang
         * @stagemodelonly
         * @since 24
         */
        heapObjectSize: number;
    }
    /**
     * Describes the heap memory threshold at which the registered callback is triggered after a GC.
     *
     * @interface HeapMemoryThreshold
     * @syscap SystemCapability.Utils.Lang
     * @stagemodelonly
     * @since 24
     */
    interface HeapMemoryThreshold {
        /**
         * This number is on a scale of 70 to 95, representing the percentage threshold of the local heap memory
         * at which the callback is triggered after a GC. Values outside this range are automatically clamped to the valid range.
         * If not set, the callback will not be triggered by local heap memory pressure.
         *
         * @type { ?number }
         * @syscap SystemCapability.Utils.Lang
         * @stagemodelonly
         * @since 24
         */
        localHeapThreshold?: number;
        /**
         * This number is on a scale of 70 to 95, representing the percentage threshold of the shared heap memory
         * at which the callback is triggered after a GC. Values outside this range are automatically clamped to the valid range.
         * If not set, the callback will not be triggered by shared heap memory pressure.
         *
         * @type { ?number }
         * @syscap SystemCapability.Utils.Lang
         * @stagemodelonly
         * @since 24
         */
        sharedHeapThreshold?: number;
        /**
         * This number is on a scale of 70 to 95, representing the percentage threshold of the process's total heap memory
         * at which the callback is triggered after a GC. Values outside this range are automatically clamped to the valid range.
         * If not set, the callback will not be triggered by process heap memory pressure.
         *
         * @type { ?number }
         * @syscap SystemCapability.Utils.Lang
         * @stagemodelonly
         * @since 24
         */
        processHeapThreshold?: number;
    }
}
import type { Callback } from './@ohos.base';
export default util;

```
