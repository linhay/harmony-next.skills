# @ohos.buffer.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022 Huawei Device Co., Ltd.
 * Licensed under the Apache License, Version 2.0 (The type of "License");
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
 * A **Buffer** object represents a byte sequence of a fixed length. It is used to store binary data.
 * **Recommended use case**: Use Buffer when you need to process images and a large amount of binary data, and receive
 * or upload files.
 *
 * @syscap SystemCapability.Utils.Lang
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare namespace buffer {
    /**
     * Enumerates the supported encoding formats.
     *
     * @unionmember { 'ascii' } ASCII format.
     * @unionmember { 'utf8' } UTF-8 format.
     * @unionmember { 'utf-8' } UTF-8 format.
     * @unionmember { 'utf16le' } UTF-16LE format.
     * @unionmember { 'ucs2' } Alias of UTF-16LE.
     * @unionmember { 'ucs-2' } Alias of UTF-16LE.
     * @unionmember { 'base64' } Base64 format.
     * @unionmember { 'base64url' } Base64URL format.
     * @unionmember { 'latin1' } Alias of iso-8859-1, which is backward compatible with the ASCII format.
     * @unionmember { 'binary' } Binary format.
     * @unionmember { 'hex' } Hexadecimal format.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    type BufferEncoding = 'ascii' | 'utf8' | 'utf-8' | 'utf16le' | 'ucs2' | 'ucs-2' | 'base64' | 'base64url' | 'latin1' | 'binary' | 'hex';
    /**
     * TypedArray inherits the features and methods of Int8Array
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    interface TypedArray extends Int8Array {
    }
    /**
     * Creates and initializes a **Buffer** object of the specified length.
     *
     * @param { number } size - Size of the **Buffer** object to create, in bytes.
     * @param { string | Buffer | number } [fill] - Value to be filled in the buffer. The default value is
     *     **0**. [since 11]
     * @param { string | Buffer | number } [fill] - Value to be filled in the buffer. The default value is **0**.
     *     [since 9 - 10]
     * @param { BufferEncoding } [encoding] - Encoding format (valid only when **fill** is a string). The default value is
     *     **'utf8'**.
     * @returns { Buffer } **Buffer** object created.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    function alloc(size: number, fill?: string | Buffer | number, encoding?: BufferEncoding): Buffer;
    /**
     * Creates a **Buffer** object of the specified size from the buffer pool, without initializing it.
     * You need to use [fill()]{@link buffer.Buffer#fill} to initialize the **Buffer** object created.
     *
     * @param { number } size - Size of the **Buffer** object to create, in bytes.
     * @returns { Buffer } Uninitialized **Buffer** object.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    function allocUninitializedFromPool(size: number): Buffer;
    /**
     * Creates a **Buffer** object of the specified size, without initializing it. This API does not allocate memory from
     * the buffer pool.
     * You need to use [fill()]{@link buffer.Buffer#fill} to initialize the **Buffer** object created.
     *
     * @param { number } size - Size of the **Buffer** object to create, in bytes.
     * @returns { Buffer } Uninitialized **Buffer** object.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    function allocUninitialized(size: number): Buffer;
    /**
     * Obtains the number of bytes of a string based on the encoding format.
     *
     * @param { string | Buffer | TypedArray | DataView | ArrayBuffer | SharedArrayBuffer } string - Target string.
     * @param { BufferEncoding } [encoding] - Encoding format. The default value is **'utf8'**.
     * @returns { number } Number of bytes of the string.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    function byteLength(string: string | Buffer | TypedArray | DataView | ArrayBuffer | SharedArrayBuffer, encoding?: BufferEncoding): number;
    /**
     * Concatenates an array of **Buffer** objects of the specified length into a new object.
     *
     * @param { Buffer[] | Uint8Array[] } list - Array of objects to concatenate.
     * @param { number } [totalLength] - Total length of bytes to be copied. The default value is **0**.
     * @returns { Buffer } **Buffer** object created.
     * @throws { BusinessError } 10200001 - The value of "length" is out of range. It must be >= 0 and <= uint32 max.
     *     Received value is: [length]
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    function concat(list: Buffer[] | Uint8Array[], totalLength?: number): Buffer;
    /**
     * Creates a **Buffer** object with the specified array.
     *
     * @param { number[] } array - Array to create a **Buffer** object.
     * @returns { Buffer } **Buffer** object created.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    function from(array: number[]): Buffer;
    /**
     * Creates a **Buffer** object of the specified length that shares memory with ArrayBuffer.
     *
     * @param { ArrayBuffer | SharedArrayBuffer } arrayBuffer - **ArrayBuffer** or **SharedArrayBuffer** object whose
     *     memory is to be shared.
     * @param { number } [byteOffset] - Byte offset. The default value is **0**.
     * @param { number } [length] - Length of the **Buffer** object to create, in bytes. The default value is
     *     **arrayBuffer.byteLength** minus **byteOffset**.
     * @returns { Buffer } **Buffer** object created.
     * @throws { BusinessError } 10200001 - The value of "[byteOffset/length]" is out of range.
     *     It must be >= [left range] and <= [right range]. Received value is: [byteOffset/length]
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    function from(arrayBuffer: ArrayBuffer | SharedArrayBuffer, byteOffset?: number, length?: number): Buffer;
    /**
     * Copies the data of a passed **Buffer** object to create a new **Buffer** object and returns the new one.
     * Creates a **Buffer** object based on the memory of a passed **Uint8Array** object and returns the new object,
     * maintaining the memory association of the data.
     *
     * @param { Buffer | Uint8Array } buffer - Target object.
     * @returns { Buffer } **Buffer** object created.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    function from(buffer: Buffer | Uint8Array): Buffer;
    /**
     * Creates a **Buffer** object based on the specified object.
     *
     * @param { Object } object - Object that supports **Symbol.toPrimitive** or **valueOf()**.
     * @param { number | string } offsetOrEncoding - Byte offset or encoding format.
     * @param { number } length - Length of the **Buffer** object to create, in bytes. This parameter is valid only when the
     *     return value of **valueOf()** of **object** is **ArrayBuffer**. Value range: 0 <= length <=
     *     ArrayBuffer.byteLength. Error 10200001 is reported if a value outside this range is reported. In other cases,
     *     you can set this parameter to any value of the number type. This parameter does not affect the result.
     * @returns { Buffer } **Buffer** object created.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    function from(object: Object, offsetOrEncoding: number | string, length: number): Buffer;
    /**
     * Creates a **Buffer** object based on a string in the given encoding format.
     *
     * @param { String } string - String.
     * @param { BufferEncoding } [encoding] - Encoding format. The default value is **'utf8'**.
     * @returns { Buffer } **Buffer** object created.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    function from(string: String, encoding?: BufferEncoding): Buffer;
    /**
     * Checks whether the specified object is a **Buffer** object.
     *
     * @param { Object } obj - Object to check.
     * @returns { boolean } Check result. The value **true** is returned if the object is a **Buffer** object; otherwise,
     *     **false** is returned.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    function isBuffer(obj: Object): boolean;
    /**
     * Checks whether the encoding format is supported.
     *
     * @param { string } encoding - Encoding format.
     * @returns { boolean } Check result. The value **true** is returned if the encoding format is supported; otherwise,
     *     **false** is returned.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    function isEncoding(encoding: string): boolean;
    /**
     * Compares two **Buffer** objects. This API is used for sorting **Buffer** objects.
     *
     * @param { Buffer | Uint8Array } buf1 - **Buffer** object to compare.
     * @param { Buffer | Uint8Array } buf2 - **Buffer** object to compare.
     * @returns { -1 | 0 | 1 } Returns **0** if **buf1** is the same as **buf2**.
     *     <br>Returns **1** if **buf1** comes after **buf2** when sorted.
     *     <br>Returns **-1** if **buf1** comes before **buf2** when sorted.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    function compare(buf1: Buffer | Uint8Array, buf2: Buffer | Uint8Array): -1 | 0 | 1;
    /**
     * Transcodes a **Buffer** or **Uint8Array** object from one encoding format to another.
     *
     * @param { Buffer | Uint8Array } source - Instance object.
     * @param { string } fromEnc - Current encoding format. For details about the supported formats, see
     *     [BufferEncoding]{@link buffer.BufferEncoding}.
     * @param { string } toEnc - Target encoding format. For details about the supported formats, see
     *     [BufferEncoding]{@link buffer.BufferEncoding}.
     * @returns { Buffer } New **Buffer** object in the target encoding format.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    function transcode(source: Buffer | Uint8Array, fromEnc: string, toEnc: string): Buffer;
    /**
     * The Buffer object is a method of handling buffers dedicated to binary data.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    class Buffer {
        /**
         * Length of the **Buffer** object, in bytes.
         *
         * @throws { BusinessError } 10200013 - Length  cannot be set for the buffer that has only a getter.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        length: number;
        /**
         * **ArrayBuffer** object.
         *
         * @throws { BusinessError } 10200013 - Buffer cannot be set for the buffer that has only a getter.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        buffer: ArrayBuffer;
        /**
         * Offset of the **Buffer** object in the memory pool.
         *
         * @throws { BusinessError } 10200013 - ByteOffset  cannot be set for the buffer that has only a getter.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        byteOffset: number;
        /**
         * Fills this **Buffer** object at the specified position. By default, data is filled cyclically.
         *
         * @param { string | Buffer | Uint8Array | number } value - Value to fill. [since 9 - 10]
         * @param { string | Buffer | Uint8Array | number } value - Value to fill. [since 11]
         * @param { number } [offset] - Offset to the start position in this **Buffer** object where data is filled. The
         *     default value is **0**.
         * @param { number } [end] - Offset to the end position in this **Buffer** object (not inclusive). The default value is
         *     the length of this **Buffer** object.
         * @param { BufferEncoding } [encoding] - Encoding format (valid only when **value** is a string). The default value
         *     is **'utf8'**.
         * @returns { Buffer } **Buffer** object filled with the specified value.
         * @throws { BusinessError } 10200001 - The value of "[offset/end]" is out of range. It must be >= 0 and <=
         *     [right range]. Received value is: [offset/end]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        fill(value: string | Buffer | Uint8Array | number, offset?: number, end?: number, encoding?: BufferEncoding): Buffer;
        /**
         * Compares this **Buffer** object with another object.
         *
         * @param { Buffer | Uint8Array } target - Target **Buffer** object to compare.
         * @param { number } [targetStart] - Offset to the start of the data to compare in the target **Buffer** object. The
         *     default value is **0**.
         * @param { number } [targetEnd] - Offset to the end of the data to compare in the target **Buffer** object (not
         *     inclusive). The default value is the length of the target **Buffer** object.
         * @param { number } [sourceStart] - Offset to the start of the data to compare in this **Buffer** object. The
         *     default value is **0**.
         * @param { number } [sourceEnd] - Offset to the end of the data to compare in this **Buffer** object (not inclusive
         *     ). The default value is the length of this **Buffer** object.
         * @returns { -1 | 0 | 1 } Comparison result. The value **0** is returned if the two **Buffer** objects are the same
         *     ; **1** is returned if this object comes after the target object when sorted; **-1** is returned if this
         *     object comes before the target object when sorted.
         * @throws { BusinessError } 10200001 - The value of "[targetStart/targetEnd/sourceStart/sourceEnd]" is out of
         *     range.
         *     It must be >= 0 and <= [right range]. Received value is: [targetStart/targetEnd/sourceStart/sourceEnd]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        compare(target: Buffer | Uint8Array, targetStart?: number, targetEnd?: number, sourceStart?: number, sourceEnd?: number): -1 | 0 | 1;
        /**
         * Copies data at the specified position in this **Buffer** object to the specified position in another **Buffer**
         * object.
         *
         * @param { Buffer | Uint8Array } target - **Buffer** or **Uint8Array** object to which data is copied.
         * @param { number } [targetStart] - Offset to the start position in the target object where data is copied. The
         *     default value is **0**.
         * @param { number } [sourceStart] - Offset to the start position in this **Buffer** object where data is copied. The
         *     default value is **0**.
         * @param { number } [sourceEnd] - Offset to the end position in this **Buffer** object (not inclusive). The default
         *     value is the length of this **Buffer** object.
         * @returns { number } Total length of the data copied, in bytes.
         * @throws { BusinessError } 10200001 - The value of "[targetStart/sourceStart/sourceEnd]" is out of range. It must
         *     be >= 0.
         *     Received value is: [targetStart/sourceStart/sourceEnd]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        copy(target: Buffer | Uint8Array, targetStart?: number, sourceStart?: number, sourceEnd?: number): number;
        /**
         * Checks whether this **Buffer** object is the same as another **Buffer** object.
         *
         * @param { Uint8Array | Buffer } otherBuffer - **Buffer** object to compare.
         * @returns { boolean } Check result. The value **true** is returned if the two objects are the same; otherwise,
         *     **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        equals(otherBuffer: Uint8Array | Buffer): boolean;
        /**
         * Checks whether this **Buffer** object contains the specified value.
         *
         * @param { string | number | Buffer | Uint8Array } value - Value to match. [since 9 - 10]
         * @param { string | number | Buffer | Uint8Array } value - Value to match. [since 11]
         * @param { number } [byteOffset] - Number of bytes to skip before starting to check data. If the offset is a negative
         *     number, data is checked from the end of the **Buffer** object. The default value is **0**.
         * @param { BufferEncoding } [encoding] - Encoding format (valid only when **value** is a string). The default value
         *     is **'utf8'**.
         * @returns { boolean } Check result. The value **true** is returned if the object contains the specified value;
         *     otherwise, **false** is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        includes(value: string | number | Buffer | Uint8Array, byteOffset?: number, encoding?: BufferEncoding): boolean;
        /**
         * Obtains the index of the first occurrence of the specified value in this **Buffer** object. If no match is found,
         * **-1** is returned.
         *
         * @param { string | number | Buffer | Uint8Array } value - Value to match. [since 9 - 10]
         * @param { string | number | Buffer | Uint8Array } value - Value to match. [since 11]
         * @param { number } [byteOffset] - Number of bytes to skip before starting to check data. If the offset is a negative
         *     number, data is checked from the end of the **Buffer** object. The default value is **0**.
         * @param { BufferEncoding } [encoding] - Encoding format (valid only when **value** is a string). The default value
         *     is **'utf8'**.
         * @returns { number } Index obtained.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        indexOf(value: string | number | Buffer | Uint8Array, byteOffset?: number, encoding?: BufferEncoding): number;
        /**
         * Creates and returns an iterator that contains the keys of this **Buffer** object.
         *
         * @returns { IterableIterator<number> } Iterator created.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        keys(): IterableIterator<number>;
        /**
         * Creates and returns an iterator that contains the values of this **Buffer** object.
         *
         * @returns { IterableIterator<number> } Iterator.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        values(): IterableIterator<number>;
        /**
         * Creates and returns an iterator that contains key-value pairs of this **Buffer** object.
         *
         * @returns { IterableIterator<[ number, number ]> } Iterator that contains the key and value, both of which are of
         *     the number type. [since 9 - 10]
         * @returns { IterableIterator<[ number, number ]> } [since 11]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        entries(): IterableIterator<[
            number,
            number
        ]>;
        /**
         * Obtains the index of the last occurrence of the specified value in this **Buffer** object. If no match is found,
         * **-1** is returned.
         *
         * @param { string | number | Buffer | Uint8Array } value - Value to match. [since 9 - 10]
         * @param { string | number | Buffer | Uint8Array } value - Value to match. [since 11]
         * @param { number } [byteOffset] - Number of bytes to skip before starting to check data. If the offset is a negative
         *     number, data is checked from the end of the **Buffer** object. The default value is the length of this
         *     **Buffer** object.
         * @param { BufferEncoding } [encoding] - Encoding format (valid only when **value** is a string). The default value
         *     is **'utf8'**.
         * @returns { number } Index obtained.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        lastIndexOf(value: string | number | Buffer | Uint8Array, byteOffset?: number, encoding?: BufferEncoding): number;
        /**
         * Reads a 64-bit, big-endian, signed big integer from this **Buffer** object at the specified offset.
         *
         * @param { number } [offset] - Offset. The default value is **0**. Value range: 0 <= offset <= Buffer.length - 8
         * @returns { bigint } Data read.
         * @throws { BusinessError } 10200001 - The value of "offset" is out of range. It must be >= 0 and <= buf.length - 8
         *     . Received value is: [offset]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        readBigInt64BE(offset?: number): bigint;
        /**
         * Reads a 64-bit, little-endian, signed big integer from this **Buffer** object at the specified offset.
         *
         * @param { number } [offset] - Offset. The default value is **0**. Value range: 0 <= offset <= Buffer.length - 8
         * @returns { bigint } Data read.
         * @throws { BusinessError } 10200001 - The value of "offset" is out of range. It must be >= 0 and <= buf.length - 8
         *     . Received value is: [offset]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        readBigInt64LE(offset?: number): bigint;
        /**
         * Reads a 64-bit, big-endian, unsigned big integer from this **Buffer** object at the specified offset.
         *
         * @param { number } [offset] - Offset. The default value is **0**. Value range: 0 <= offset <= Buffer.length - 8
         * @returns { bigint } Data read.
         * @throws { BusinessError } 10200001 - The value of "offset" is out of range. It must be >= 0 and <= buf.length - 8
         *     . Received value is: [offset]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        readBigUInt64BE(offset?: number): bigint;
        /**
         * Reads a 64-bit, little-endian, unsigned big integer from this **Buffer** object at the specified offset.
         *
         * @param { number } [offset] - Offset. The default value is **0**. Value range: 0 <= offset <= Buffer.length - 8
         * @returns { bigint } Data read.
         * @throws { BusinessError } 10200001 - The value of "offset" is out of range. It must be >= 0 and <= buf.length - 8
         *     . Received value is: [offset]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        readBigUInt64LE(offset?: number): bigint;
        /**
         * Reads a 64-bit, big-endian, double-precision floating-point number from this **Buffer** object at the specified
         * offset.
         *
         * @param { number } [offset] - Offset. The default value is **0**. Value range: 0 <= offset <= Buffer.length - 8
         * @returns { number } Data read.
         * @throws { BusinessError } 10200001 - The value of "offset" is out of range. It must be >= 0 and <= buf.length - 8
         *     . Received value is: [offset]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        readDoubleBE(offset?: number): number;
        /**
         * Reads a 64-bit, little-endian, double-precision floating-point number from this **Buffer** object at the
         * specified offset.
         *
         * @param { number } [offset] - Offset. The default value is **0**. Value range: 0 <= offset <= Buffer.length - 8
         * @returns { number } Data read.
         * @throws { BusinessError } 10200001 - The value of "offset" is out of range. It must be >= 0 and <= buf.length - 8
         *     . Received value is: [offset]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        readDoubleLE(offset?: number): number;
        /**
         * Reads a 32-bit, big-endian, single-precision floating-point number from this **Buffer** object at the specified
         * offset.
         *
         * @param { number } [offset] - Offset. The default value is **0**. Value range: 0 <= offset <= Buffer.length - 4
         * @returns { number } Data read.
         * @throws { BusinessError } 10200001 - The value of "offset" is out of range. It must be >= 0 and <= buf.length - 4
         *     . Received value is: [offset]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        readFloatBE(offset?: number): number;
        /**
         * Reads a 32-bit, little-endian, single-precision floating-point number from this **Buffer** object at the
         * specified offset.
         *
         * @param { number } [offset] - Offset. The default value is **0**. Value range: 0 <= offset <= Buffer.length - 4
         * @returns { number } Data read.
         * @throws { BusinessError } 10200001 - The value of "offset" is out of range. It must be >= 0 and <= buf.length - 4
         *     . Received value is: [offset]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        readFloatLE(offset?: number): number;
        /**
         * Reads an 8-bit signed integer from this **Buffer** object at the specified offset.
         *
         * @param { number } [offset] - Offset. The default value is **0**. Value range: 0 <= offset <= Buffer.length - 1
         * @returns { number } Data read.
         * @throws { BusinessError } 10200001 - The value of "offset" is out of range. It must be >= 0 and <= buf.length - 1
         *     . Received value is: [offset]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        readInt8(offset?: number): number;
        /**
         * Reads a 16-bit, big-endian, signed integer from this **Buffer** object at the specified offset.
         *
         * @param { number } [offset] - Offset. The default value is **0**. Value range: 0 <= offset <= Buffer.length - 2
         * @returns { number } Data read.
         * @throws { BusinessError } 10200001 - The value of "offset" is out of range. It must be >= 0 and <= buf.length - 2
         *     . Received value is: [offset]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        readInt16BE(offset?: number): number;
        /**
         * Reads a 16-bit, little-endian, signed integer from this **Buffer** object at the specified offset.
         *
         * @param { number } [offset] - Offset. The default value is **0**. Value range: 0 <= offset <= Buffer.length - 2
         * @returns { number } Data read.
         * @throws { BusinessError } 10200001 - The value of "offset" is out of range. It must be >= 0 and <= buf.length - 2
         *     . Received value is: [offset]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        readInt16LE(offset?: number): number;
        /**
         * Reads a 32-bit, big-endian, signed integer from this **Buffer** object at the specified offset.
         *
         * @param { number } [offset] - Offset. The default value is **0**. Value range: 0 <= offset <= Buffer.length - 4
         * @returns { number } Data read.
         * @throws { BusinessError } 10200001 - The value of "offset" is out of range. It must be >= 0 and <= buf.length - 4
         *     . Received value is: [offset]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        readInt32BE(offset?: number): number;
        /**
         * Reads a 32-bit, little-endian, signed integer from this **Buffer** object at the specified offset.
         *
         * @param { number } [offset] - Offset. The default value is **0**. Value range: 0 <= offset <= Buffer.length - 4
         * @returns { number } Data read.
         * @throws { BusinessError } 10200001 - The value of "offset" is out of range. It must be >= 0 and <= buf.length - 4
         *     . Received value is: [offset]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        readInt32LE(offset?: number): number;
        /**
         * Reads the specified number of bytes from this **Buffer** object at the specified offset, and interprets the
         * result as a big-endian, two's complement signed value that supports up to 48 bits of precision.
         *
         * @param { number } offset - Offset. The default value is **0**. Value range: 0 <= offset <= Buffer.length -
         *     byteLength
         * @param { number } byteLength - Number of bytes to read. Value range: 1 <= byteLength <= 6
         * @returns { number } Data read. If the offset is a decimal, undefined is returned.
         * @throws { BusinessError } 10200001 - The value of "[param]" is out of range. It must be >= [left range] and <=
         *     [right range]. Received value is: [param]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        readIntBE(offset: number, byteLength: number): number;
        /**
         * Reads the specified number of bytes from this **Buffer** object at the specified offset and interprets the result
         * as a little-endian, two's complement signed value that supports up to 48 bits of precision.
         *
         * @param { number } offset - Offset. The default value is **0**. Value range: 0 <= offset <= Buffer.length -
         *     byteLength
         * @param { number } byteLength - Number of bytes to read. Value range: 1 <= byteLength <= 6
         * @returns { number } Data read. If the offset is a decimal, undefined is returned.
         * @throws { BusinessError } 10200001 - The value of "[param]" is out of range. It must be >= [left range] and <=
         *     [right range]. Received value is: [param]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        readIntLE(offset: number, byteLength: number): number;
        /**
         * Reads an 8-bit unsigned integer from this **Buffer** object at the specified offset.
         *
         * @param { number } [offset] - Offset. The default value is **0**. Value range: 0 <= offset <= Buffer.length - 1
         * @returns { number } Data read.
         * @throws { BusinessError } 10200001 - The value of "offset" is out of range. It must be >= 0 and <= buf.length - 1
         *     . Received value is: [offset]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        readUInt8(offset?: number): number;
        /**
         * Reads a 16-bit, big-endian, unsigned integer from this **Buffer** object at the specified offset.
         *
         * @param { number } [offset] - Offset. The default value is **0**. Value range: 0 <= offset <= Buffer.length - 2
         * @returns { number } Data read.
         * @throws { BusinessError } 10200001 - The value of "offset" is out of range. It must be >= 0 and <= buf.length - 2
         *     . Received value is: [offset]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        readUInt16BE(offset?: number): number;
        /**
         * Reads a 16-bit, little-endian, unsigned integer from this **Buffer** object at the specified offset.
         *
         * @param { number } [offset] - Offset. The default value is **0**. Value range: 0 <= offset <= Buffer.length - 2
         * @returns { number } Data read.
         * @throws { BusinessError } 10200001 - The value of "offset" is out of range. It must be >= 0 and <= buf.length - 2
         *     . Received value is: [offset]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        readUInt16LE(offset?: number): number;
        /**
         * Reads a 32-bit, big-endian, unsigned integer from this **Buffer** object at the specified offset.
         *
         * @param { number } [offset] - Offset. The default value is **0**. Value range: 0 <= offset <= Buffer.length - 4
         * @returns { number } Data read.
         * @throws { BusinessError } 10200001 - The value of "offset" is out of range. It must be >= 0 and <= buf.length - 4
         *     . Received value is: [offset]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        readUInt32BE(offset?: number): number;
        /**
         * Reads a 32-bit, little-endian, unsigned integer from this **Buffer** object at the specified offset.
         *
         * @param { number } [offset] - Offset. The default value is **0**. Value range: 0 <= offset <= Buffer.length - 4
         * @returns { number } Data read.
         * @throws { BusinessError } 10200001 - The value of "offset" is out of range. It must be >= 0 and <= buf.length - 4
         *     . Received value is: [offset]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        readUInt32LE(offset?: number): number;
        /**
         * Reads the specified number of bytes from this **Buffer** object at the specified offset, and interprets the
         * result as an unsigned, big-endian integer that supports up to 48 bits of precision.
         *
         * @param { number } offset - Offset. The default value is **0**. Value range: 0 <= offset <= Buffer.length -
         *     byteLength
         * @param { number } byteLength - Number of bytes to read.  Value range: 1 <= byteLength <= 6
         * @returns { number } Data read. If the offset is a decimal, undefined is returned.
         * @throws { BusinessError } 10200001 - The value of "[param]" is out of range. It must be >= [left range] and <=
         *     [right range]. Received value is: [param]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        readUIntBE(offset: number, byteLength: number): number;
        /**
         * Reads the specified number of bytes from this **Buffer** object at the specified offset, and interprets the
         * result as an unsigned, little-endian integer that supports up to 48 bits of precision.
         *
         * @param { number } offset - Offset. The default value is **0**. Value range: 0 <= offset <= Buffer.length -
         *     byteLength
         * @param { number } byteLength - Number of bytes to read. Value range: 1 <= byteLength <= 6
         * @returns { number } Data read. If the offset is a decimal, undefined is returned.
         * @throws { BusinessError } 10200001 - The value of "[param]" is out of range. It must be >= [left range] and <=
         *     [right range]. Received value is: [param]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        readUIntLE(offset: number, byteLength: number): number;
        /**
         * Truncates this **Buffer** object from the specified position to create a new **Buffer** object.
         *
         * @param { number } [start] - Offset to the start position in this **Buffer** object where data is truncated. The
         *     default value is **0**.
         * @param { number } [end] - Offset to the end position in this **Buffer** object (not inclusive). The default value is
         *     the length of this **Buffer** object.
         * @returns { Buffer } **Buffer** object created. When the value of **start** or **end** is less than **0**, an
         *     empty buffer is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        subarray(start?: number, end?: number): Buffer;
        /**
         * Converts this **Buffer** object into an array of unsigned 16-bit integers and swaps the byte order in place.
         *
         * @returns { Buffer } **Buffer** object swapped.
         * @throws { BusinessError } 10200009 - The buffer size must be a multiple of 16-bits
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        swap16(): Buffer;
        /**
         * Converts this **Buffer** object into an array of unsigned 32-bit integers and swaps the byte order in place.
         *
         * @returns { Buffer } **Buffer** object swapped.
         * @throws { BusinessError } 10200009 - The buffer size must be a multiple of 32-bits
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        swap32(): Buffer;
        /**
         * Converts this **Buffer** object into an array of unsigned 64-bit integers and swaps the byte order in place.
         *
         * @returns { Buffer } **Buffer** object swapped.
         * @throws { BusinessError } 10200009 - The buffer size must be a multiple of 64-bits
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        swap64(): Buffer;
        /**
         * Converts this **Buffer** object into a JSON object.
         *
         * @returns { Object } JSON object.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        toJSON(): Object;
        /**
         * Converts the data at the specified position in this **Buffer** object into a string in the specified encoding
         * format.
         *
         * @param { string } [encoding] - Encoding format (valid only when **value** is a string). The default value is
         *     **'utf8'**.
         * @param { number } [start] - Offset to the start position of the data to convert. The default value is **0**.
         * @param { number } [end] - Offset to the end position of data. The default value is the length of this **Buffer**
         *     object.
         * @returns { string } String. When the value of **start** is greater than or equal to **Buffer.length** or
         *     **start** is greater than **end**, an empty string is returned.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        toString(encoding?: string, start?: number, end?: number): string;
        /**
         * Writes a string of the specified length to this **Buffer** object at the specified position in the given encoding
         * format.
         *
         * @param { string } str - String to write.
         * @param { number } [offset] - Offset. The default value is **0**.
         * @param { number } [length] - Maximum number of bytes to write. The default value is **Buffer.length** minus
         *     **offset**.
         * @param { string } [encoding] - Encoding format of the string. The default value is **'utf8'**.
         * @returns { number } Number of bytes written.
         * @throws { BusinessError } 10200001 - The value of "[offset/length]" is out of range. It must be >= 0 and <=
         *     buf.length. Received value is: [offset/length]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        write(str: string, offset?: number, length?: number, encoding?: string): number;
        /**
         * Writes a 64-bit, big-endian, signed big integer to this **Buffer** object at the specified offset.
         *
         * @param { bigint } value - Data to write.
         * @param { number } [offset] - Offset. The default value is **0**. Value range: 0 <= offset <= Buffer.length - 8
         * @returns { number } Offset plus the number of written bytes.
         * @throws { BusinessError } 10200001 - The value of "[param]" is out of range. It must be >= [left range] and <=
         *     [right range]. Received value is: [param]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        writeBigInt64BE(value: bigint, offset?: number): number;
        /**
         * Writes a 64-bit, little-endian, signed big integer to this **Buffer** object at the specified offset.
         *
         * @param { bigint } value - Data to write.
         * @param { number } [offset] - Offset. The default value is **0**. Value range: 0 <= offset <= Buffer.length - 8
         * @returns { number } Offset plus the number of written bytes.
         * @throws { BusinessError } 10200001 - The value of "[param]" is out of range. It must be >= [left range] and <=
         *     [right range]. Received value is: [param]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        writeBigInt64LE(value: bigint, offset?: number): number;
        /**
         * Writes a 64-bit, big-endian, signed big integer to this **Buffer** object at the specified offset.
         *
         * @param { bigint } value - Data to write.
         * @param { number } [offset] - Offset. The default value is **0**. Value range: 0 <= offset <= Buffer.length - 8
         * @returns { number } Offset plus the number of written bytes.
         * @throws { BusinessError } 10200001 - The value of "[param]" is out of range. It must be >= [left range] and <=
         *     [right range]. Received value is: [param]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        writeBigUInt64BE(value: bigint, offset?: number): number;
        /**
         * Writes a 64-bit, little-endian, unsigned big integer to this **Buffer** object at the specified offset.
         *
         * @param { bigint } value - Data to write.
         * @param { number } [offset] - Offset. The default value is **0**. Value range: 0 <= offset <= Buffer.length - 8
         * @returns { number } Offset plus the number of written bytes.
         * @throws { BusinessError } 10200001 - The value of "[param]" is out of range. It must be >= [left range] and <=
         *     [right range]. Received value is: [param]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        writeBigUInt64LE(value: bigint, offset?: number): number;
        /**
         * Writes a 64-bit, big-endian, double-precision floating-point number to this **Buffer** object at the specified
         * offset.
         *
         * @param { number } value - Data to write.
         * @param { number } [offset] - Offset. The default value is **0**. Value range: 0 <= offset <= Buffer.length - 8
         * @returns { number } Offset plus the number of written bytes.
         * @throws { BusinessError } 10200001 - The value of "offset" is out of range. It must be >= 0 and <= buf.length - 8
         *     . Received value is: [offset]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        writeDoubleBE(value: number, offset?: number): number;
        /**
         * Writes a 64-bit, little-endian, double-precision floating-point number to this **Buffer** object at the specified
         * offset.
         *
         * @param { number } value - Data to write.
         * @param { number } [offset] - Offset. The default value is **0**. Value range: 0 <= offset <= Buffer.length - 8
         * @returns { number } Offset plus the number of written bytes.
         * @throws { BusinessError } 10200001 - The value of "offset" is out of range. It must be >= 0 and <= buf.length - 8
         *     . Received value is: [offset]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        writeDoubleLE(value: number, offset?: number): number;
        /**
         * Writes a 32-bit, big-endian, single-precision floating-point number to this **Buffer** object at the specified
         * offset.
         *
         * @param { number } value - Data to write.
         * @param { number } [offset] - Offset. The default value is **0**. Value range: 0 <= offset <= Buffer.length - 4
         * @returns { number } Offset plus the number of written bytes.
         * @throws { BusinessError } 10200001 - The value of "offset" is out of range. It must be >= 0 and <= buf.length - 4
         *     . Received value is: [offset]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        writeFloatBE(value: number, offset?: number): number;
        /**
         * Writes a 32-bit, little-endian, single-precision floating-point number to this **Buffer** object at the specified
         * offset.
         *
         * @param { number } value - Data to write.
         * @param { number } [offset] - Offset. The default value is **0**. Value range: 0 <= offset <= Buffer.length - 4
         * @returns { number } Offset plus the number of written bytes.
         * @throws { BusinessError } 10200001 - The value of "offset" is out of range. It must be >= 0 and <= buf.length - 4
         *     . Received value is: [offset]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        writeFloatLE(value: number, offset?: number): number;
        /**
         * Writes an 8-bit signed integer to this **Buffer** object at the specified offset.
         *
         * @param { number } value - Data to write.
         * @param { number } [offset] - Offset. The default value is **0**. Value range: 0 <= offset <= Buffer.length - 1
         * @returns { number } Offset plus the number of written bytes.
         * @throws { BusinessError } 10200001 - The value of "[param]" is out of range. It must be >= [left range] and <=
         *     [right range]. Received value is: [param]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        writeInt8(value: number, offset?: number): number;
        /**
         * Writes a 16-bit, big-endian, signed integer to this **Buffer** object at the specified offset.
         *
         * @param { number } value - Data to write.
         * @param { number } [offset] - Offset. The default value is **0**. Value range: 0 <= offset <= Buffer.length - 2
         * @returns { number } Offset plus the number of written bytes.
         * @throws { BusinessError } 10200001 - The value of "[param]" is out of range. It must be >= [left range] and <=
         *     [right range]. Received value is: [param]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        writeInt16BE(value: number, offset?: number): number;
        /**
         * Writes a 16-bit, little-endian, signed integer to this **Buffer** object at the specified offset.
         *
         * @param { number } value - Data to write.
         * @param { number } [offset] - Offset. The default value is **0**. Value range: 0 <= offset <= Buffer.length - 2
         * @returns { number } Offset plus the number of written bytes.
         * @throws { BusinessError } 10200001 - The value of "[param]" is out of range. It must be >= [left range] and <=
         *     [right range]. Received value is: [param]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        writeInt16LE(value: number, offset?: number): number;
        /**
         * Writes a 32-bit, big-endian, signed integer to this **Buffer** object at the specified offset.
         *
         * @param { number } value - Data to write.
         * @param { number } [offset] - Offset. The default value is **0**. Value range: 0 <= offset <= Buffer.length - 4
         * @returns { number } Offset plus the number of written bytes.
         * @throws { BusinessError } 10200001 - The value of "[param]" is out of range. It must be >= [left range] and <=
         *     [right range]. Received value is: [param]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        writeInt32BE(value: number, offset?: number): number;
        /**
         * Writes a 32-bit, little-endian, signed integer to this **Buffer** object at the specified offset.
         *
         * @param { number } value - Data to write.
         * @param { number } [offset] - Offset. The default value is **0**. Value range: 0 <= offset <= Buffer.length - 4
         * @returns { number } Offset plus the number of written bytes.
         * @throws { BusinessError } 10200001 - The value of "[param]" is out of range. It must be >= [left range] and <=
         *     [right range]. Received value is: [param]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        writeInt32LE(value: number, offset?: number): number;
        /**
         * Writes a big-endian signed value of the specified length to this **Buffer** object at the specified offset.
         *
         * @param { number } value - Data to write.
         * @param { number } offset - Offset. The default value is **0**. Value range: 0 <= offset <= Buffer.length -
         *     byteLength
         * @param { number } byteLength - Number of bytes to write.
         * @returns { number } Offset plus the number of written bytes.
         * @throws { BusinessError } 10200001 - The value of "[param]" is out of range. It must be >= [left range] and <=
         *     [right range]. Received value is: [param]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        writeIntBE(value: number, offset: number, byteLength: number): number;
        /**
         * Writes a little-endian signed value of the specified length to this **Buffer** object at the specified offset.
         *
         * @param { number } value - Data to write.
         * @param { number } offset - Offset. The default value is **0**. Value range: 0 <= offset <= Buffer.length -
         *     byteLength
         * @param { number } byteLength - Number of bytes to write.
         * @returns { number } Offset plus the number of written bytes.
         * @throws { BusinessError } 10200001 - The value of "[param]" is out of range. It must be >= [left range] and <=
         *     [right range]. Received value is: [param]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        writeIntLE(value: number, offset: number, byteLength: number): number;
        /**
         * Writes an 8-bit unsigned integer to this **Buffer** object at the specified offset.
         *
         * @param { number } value - Data to write.
         * @param { number } [offset] - Offset. The default value is **0**. Value range: 0 <= offset <= Buffer.length - 1
         * @returns { number } Offset plus the number of written bytes.
         * @throws { BusinessError } 10200001 - The value of "[param]" is out of range. It must be >= [left range] and <=
         *     [right range]. Received value is: [param]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        writeUInt8(value: number, offset?: number): number;
        /**
         * Writes a 16-bit, big-endian, unsigned integer to this **Buffer** object at the specified offset.
         *
         * @param { number } value - Data to write.
         * @param { number } [offset] - Offset. The default value is **0**. Value range: 0 <= offset <= Buffer.length - 2
         * @returns { number } Offset plus the number of written bytes.
         * @throws { BusinessError } 10200001 - The value of "[param]" is out of range. It must be >= [left range] and <=
         *     [right range]. Received value is: [param]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        writeUInt16BE(value: number, offset?: number): number;
        /**
         * Writes a 16-bit, little-endian, unsigned integer to this **Buffer** object at the specified offset.
         *
         * @param { number } value - Data to write.
         * @param { number } [offset] - Offset. The default value is **0**. Value range: 0 <= offset <= Buffer.length - 2
         * @returns { number } Offset plus the number of written bytes.
         * @throws { BusinessError } 10200001 - The value of "[param]" is out of range. It must be >= [left range] and <=
         *     [right range]. Received value is: [param]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        writeUInt16LE(value: number, offset?: number): number;
        /**
         * Writes a 32-bit, big-endian, unsigned integer to this **Buffer** object at the specified offset.
         *
         * @param { number } value - Data to write.
         * @param { number } [offset] - Offset. The default value is **0**. Value range: 0 <= offset <= Buffer.length - 4
         * @returns { number } Offset plus the number of written bytes.
         * @throws { BusinessError } 10200001 - The value of "[param]" is out of range. It must be >= [left range] and <=
         *     [right range]. Received value is: [param]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        writeUInt32BE(value: number, offset?: number): number;
        /**
         * Writes a 32-bit, little-endian, unsigned integer to this **Buffer** object at the specified offset.
         *
         * @param { number } value - Data to write.
         * @param { number } [offset] - Offset. The default value is **0**. Value range: 0 <= offset <= Buffer.length - 4
         * @returns { number } Offset plus the number of written bytes.
         * @throws { BusinessError } 10200001 - The value of "[param]" is out of range. It must be >= [left range] and <=
         *     [right range]. Received value is: [param]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        writeUInt32LE(value: number, offset?: number): number;
        /**
         * Writes an unsigned big-endian value of the specified length to this **Buffer** object at the specified offset.
         *
         * @param { number } value - Data to write.
         * @param { number } offset - Offset. The default value is **0**. Value range: 0 <= offset <= Buffer.length -
         *     byteLength
         * @param { number } byteLength - Number of bytes to write.
         * @returns { number } Offset plus the number of written bytes.
         * @throws { BusinessError } 10200001 - The value of "[param]" is out of range. It must be >= [left range] and <=
         *     [right range]. Received value is: [param]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        writeUIntBE(value: number, offset: number, byteLength: number): number;
        /**
         * Writes an unsigned little-endian value of the specified length to this **Buffer** object at the specified offset.
         *
         * @param { number } value - Data to write.
         * @param { number } offset - Offset. The default value is **0**. Value range: 0 <= offset <= Buffer.length -
         *     byteLength
         * @param { number } byteLength - Number of bytes to write.
         * @returns { number } Offset plus the number of written bytes.
         * @throws { BusinessError } 10200001 - The value of "[param]" is out of range. It must be >= [left range] and <=
         *     [right range]. Received value is: [param]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        writeUIntLE(value: number, offset: number, byteLength: number): number;
    }
    /**
     * Process data as blob type
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    class Blob {
        /**
         * A constructor used to create a **Blob** object.
         *
         * @param { string[] | ArrayBuffer[] | TypedArray[] | DataView[] | Blob[] } sources - Data sources of the **Blob**
         *     object.
         * @param { Object } [options] - options:<br>- **endings**: specifies how the terminator **'\n'** is output. The
         *     value can be **'native'** or **'transparent'**. **'native'** means that the terminator follows the system.
         *     **'transparent'** means that the terminator stored in the **Blob** object remains unchanged. The default
         *     value is **'transparent'**.<br>- **type**: type of the data in the **Blob** object. This type represents the
         *     MIME type of the data. However, it is not used for type format validation. The default value is **''**.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        constructor(sources: string[] | ArrayBuffer[] | TypedArray[] | DataView[] | Blob[], options?: Object);
        /**
         * Total size of the Blob instance, in bytes.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        get size(): number;
        /**
         * Type of the data in the Blob instance.
         *
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        get type(): string;
        /**
         * Puts the **Blob** data into an **ArrayBuffer** object. This API uses a promise to return the result.
         *
         * @returns { Promise<ArrayBuffer> }
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        arrayBuffer(): Promise<ArrayBuffer>;
        /**
         * Creates and returns a **Blob** object that contains specified data from this **Blob** object.
         *
         * @param { number } [start] - Offset to the start position of data. The default value is **0**.
         * @param { number } [end] - Offset to the end position of data. The default value is the data length in the original
         *     **Blob** object.
         * @param { string } [type] - Type of the data in the new **Blob** object. The default value is **''**.
         * @returns { Blob }
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        slice(start?: number, end?: number, type?: string): Blob;
        /**
         * Decodes data using UTF-8 and returns a string. This API uses a promise to return the result.
         *
         * @returns { Promise<string> }
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        text(): Promise<string>;
    }
}
export default buffer;

```
