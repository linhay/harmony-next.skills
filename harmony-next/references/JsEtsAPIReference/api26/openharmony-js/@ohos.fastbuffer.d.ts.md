# @ohos.fastbuffer.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2025 Huawei Device Co., Ltd.
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
 * The FastBuffer class is a container type for dealing with binary data directly. It can be constructed in a variety of ways.
 *
 * @namespace fastbuffer
 * @syscap SystemCapability.Utils.Lang
 * @crossplatform
 * @atomicservice
 * @since 20
 */
declare namespace fastbuffer {
    /**
     * This parameter specifies the type of a common encoding format.
     *
     * @typedef { 'ascii' | 'utf8' | 'utf-8' | 'utf16le' | 'ucs2' | 'ucs-2' | 'base64' | 'base64url' | 'latin1' | 'binary' | 'hex' }
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice
     * @since 20
     */
    type BufferEncoding = 'ascii' | 'utf8' | 'utf-8' | 'utf16le' | 'ucs2' | 'ucs-2' | 'base64' | 'base64url' | 'latin1' | 'binary' | 'hex';
    /**
     * TypedArray inherits the features and methods of Int8Array
     *
     * @extends Int8Array
     * @typedef TypedArray
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice
     * @since 20
     */
    interface TypedArray extends Int8Array {
    }
    /**
     * Allocates a new FastBuffer for a fixed size bytes. If fill is undefined, the FastBuffer will be zero-filled.
     *
     * @param { number } size - The desired size (in bytes) of the new FastBuffer
     * @param { string | FastBuffer | number } [fill] - fill [fill=0] A value to pre-fill the new FastBuffer with
     * @param { BufferEncoding } [encoding] - encoding [encoding='utf8']  If `fill` is a string, this is its encoding
     * @returns { FastBuffer } Return a new allocated FastBuffer
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice
     * @since 20
     */
    function alloc(size: number, fill?: string | FastBuffer | number, encoding?: BufferEncoding): FastBuffer;
    /**
     * Allocates a new FastBuffer for a fixed size bytes. The FastBuffer will not be initially filled.
     *
     * @param { number } size - The desired size (in bytes) of the new FastBuffer
     * @returns { FastBuffer } Return a new allocated FastBuffer
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice
     * @since 20
     */
    function allocUninitializedFromPool(size: number): FastBuffer;
    /**
     * Allocates a new un-pooled FastBuffer for a fixed size bytes. The FastBuffer will not be initially filled.
     *
     * @param { number } size - The desired size (in bytes) of the new FastBuffer
     * @returns { FastBuffer } Return a new allocated FastBuffer
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice
     * @since 20
     */
    function allocUninitialized(size: number): FastBuffer;
    /**
     * Returns the byte length of a string when encoded using `encoding`.
     * This is not the same as [`String.prototype.length`], which does not account
     * for the encoding that is used to convert the string into bytes.
     *
     * @param { string | FastBuffer | TypedArray | DataView | ArrayBuffer | SharedArrayBuffer } value - Target string.
     * @param { BufferEncoding } [encoding] - Encoding format of the string. The default value is 'utf8'.
     * @returns { number } The number of bytes contained within `string`
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice
     * @since 20
     */
    function byteLength(value: string | FastBuffer | TypedArray | DataView | ArrayBuffer | SharedArrayBuffer, encoding?: BufferEncoding): number;
    /**
     * Returns a new `FastBuffer` which is the result of concatenating all the `FastBuffer`instances in the `list` together.
     *
     * @param { FastBuffer[] | Uint8Array[] } list - Array of FastBuffer or Uint8Array instances to concatenate
     * @param { number } [totalLength] - Total length of the FastBuffer instances when concatenated
     * @returns { FastBuffer } Return a new allocated FastBuffer
     * @throws { BusinessError } 10200001 - Range error. Possible causes:
     * The value of the parameter is not within the specified range.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice
     * @since 20
     */
    function concat(list: FastBuffer[] | Uint8Array[], totalLength?: number): FastBuffer;
    /**
     * Allocates a new FastBuffer using an array of bytes in the range 0 – 255. Array entries outside that range will be truncated to fit into it.
     *
     * @param { number[] } array - An array of bytes (integers in 0-255 range)
     * @returns { FastBuffer } Return a new allocated FastBuffer
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice
     * @since 20
     */
    function from(array: number[]): FastBuffer;
    /**
     * This creates a view of the ArrayBuffer without copying the underlying memory.
     *
     * @param { ArrayBuffer | SharedArrayBuffer } arrayBuffer - The ArrayBuffer or SharedArrayBuffer to create a view from
     * @param { number } [byteOffset] - byteOffset [byteOffset = 0] Index of first byte to expose
     * @param { number } [length] - length [length = arrayBuffer.byteLength - byteOffset] Number of bytes to expose
     * @returns { FastBuffer } Return a view of the ArrayBuffer
     * @throws { BusinessError } 10200001 - Range error. Possible causes:
     * The value of the parameter is not within the specified range.
     * @throws { BusinessError } 10200068 - The underlying ArrayBuffer is null or detach.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice
     * @since 20
     */
    function from(arrayBuffer: ArrayBuffer | SharedArrayBuffer, byteOffset?: number, length?: number): FastBuffer;
    /**
     * Copies the passed buffer data onto a new FastBuffer instance.
     *
     * @param { FastBuffer | Uint8Array } buffer - The buffer to copy data from
     * @returns { FastBuffer } Return a new allocated FastBuffer
     * @throws { BusinessError } 10200068 - The underlying ArrayBuffer is null or detach.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice
     * @since 20
     */
    function from(buffer: FastBuffer | Uint8Array): FastBuffer;
    /**
     * Creates a new FastBuffer containing string. The encoding parameter identifies the character encoding
     * to be used when converting string into bytes.
     *
     * @param { string } value - The string to encode into a FastBuffer
     * @param { BufferEncoding } [encoding] - encoding [encoding='utf8'] The encoding of string
     * @returns { FastBuffer } Return a new FastBuffer containing string
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice
     * @since 20
     */
    function from(value: string, encoding?: BufferEncoding): FastBuffer;
    /**
     * Returns true if obj is a FastBuffer, false otherwise
     *
     * @param { Object } obj - The object to check if it's a FastBuffer
     * @returns { boolean } true or false
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice
     * @since 20
     */
    function isBuffer(obj: Object): boolean;
    /**
     * Returns true if encoding is the name of a supported character encoding, or false otherwise.
     *
     * @param { string } encoding - The character encoding name to validate
     *
     * @returns { boolean } true or false
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice
     * @since 20
     */
    function isEncoding(encoding: string): boolean;
    /**
     * Compares buf1 to buf2
     *
     * @param { FastBuffer | Uint8Array } buf1 - First buffer for comparison
     * @param { FastBuffer | Uint8Array } buf2 - Second buffer for comparison
     * @returns { -1 | 0 | 1 } 0 is returned if target is the same as buf
     *         1 is returned if target should come before buf when sorted.
     *        -1 is returned if target should come after buf when sorted.
     * @throws { BusinessError } 10200068 - The underlying ArrayBuffer is null or detach.
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice
     * @since 20
     */
    function compare(buf1: FastBuffer | Uint8Array, buf2: FastBuffer | Uint8Array): -1 | 0 | 1;
    /**
     * Re-encodes the given FastBuffer or Uint8Array instance from one character encoding to another.
     *
     * @param { FastBuffer | Uint8Array } source - The buffer to re-encode
     * @param { string } fromEnc - The source character encoding
     * @param { string } toEnc - The target character encoding
     * @returns { FastBuffer } Returns a new FastBuffer instance
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice
     * @since 20
     */
    function transcode(source: FastBuffer | Uint8Array, fromEnc: string, toEnc: string): FastBuffer;
    /**
     * The FastBuffer object is a method of handling buffers dedicated to binary data.
     *
     * @syscap SystemCapability.Utils.Lang
     * @crossplatform
     * @atomicservice
     * @since 20
     */
    class FastBuffer {
        /**
         * Returns the number of bytes in buf
         *
         * @type { number }
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        length: number;
        /**
         * The arraybuffer underlying the FastBuffer object
         *
         * @type { ArrayBuffer }
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        buffer: ArrayBuffer;
        /**
         * The byteOffset of the Buffers underlying ArrayBuffer object
         *
         * @type { number }
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        byteOffset: number;
        /**
         * Fills buf with the specified value. If the offset and end are not given, the entire buf will be filled.
         *
         * @param { string | FastBuffer | Uint8Array | number } value - The value to fill into the buffer
         * @param { number } [offset] - offset [offset = 0] Number of bytes to skip before starting to fill buf
         * @param { number } [end] - end [end = buf.length] Where to stop filling buf (not inclusive)
         * @param { BufferEncoding } [encoding] - encoding [encoding='utf8'] The encoding for value if value is a string
         * @returns { FastBuffer } A reference to buf
         * @throws { BusinessError } 10200001 - Range error. Possible causes:
         * The value of the parameter is not within the specified range.
         * @throws { BusinessError } 10200068 - The underlying ArrayBuffer is null or detach.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        fill(value: string | FastBuffer | Uint8Array | number, offset?: number, end?: number, encoding?: BufferEncoding): FastBuffer;
        /**
         * Compares buf with target and returns a number indicating whether buf comes before, after,
         * or is the same as target in sort order. Comparison is based on the actual sequence of bytes in each FastBuffer.
         *
         * @param { FastBuffer | Uint8Array } target - The buffer to compare with this buffer
         * @param { number } [targetStart] - targetStart [targetStart = 0] The offset within target at which to begin comparison
         * @param { number } [targetEnd] - targetEnd [targetEnd = target.length] The offset within target at which to end comparison (not inclusive)
         * @param { number } [sourceStart] - sourceStart [sourceStart = 0] The offset within buf at which to begin comparison
         * @param { number } [sourceEnd] - sourceEnd [sourceEnd = buf.length] The offset within buf at which to end comparison (not inclusive)
         * @returns { -1 | 0 | 1 } 0 is returned if target is the same as buf
         *         1 is returned if target should come before buf when sorted.
         *        -1 is returned if target should come after buf when sorted.
         * @throws { BusinessError } 10200001 - Range error. Possible causes:
         * The value of the parameter is not within the specified range.
         * @throws { BusinessError } 10200068 - The underlying ArrayBuffer is null or detach.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        compare(target: FastBuffer | Uint8Array, targetStart?: number, targetEnd?: number, sourceStart?: number, sourceEnd?: number): -1 | 0 | 1;
        /**
         * Copies data from a region of buf to a region in target, even if the target memory region overlaps with buf.
         * If sourceEnd is greater than the length of the target, the length of the target shall prevail, and the extra part will not be overwritten.
         *
         * @param { FastBuffer | Uint8Array } target - The buffer to copy data into
         * @param { number } [targetStart] - targetStart [targetStart = 0] The offset within target at which to begin writing
         * @param { number } [sourceStart] - sourceStart [sourceStart = 0] The offset within buf from which to begin copying
         * @param { number } [sourceEnd] - sourceEnd [sourceEnd = buf.length] The offset within buf at which to stop copying (not inclusive)
         * @returns { number } The number of bytes copied
         * @throws { BusinessError } 10200001 - Range error. Possible causes:
         * The value of the parameter is not within the specified range.
         * @throws { BusinessError } 10200068 - The underlying ArrayBuffer is null or detach.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        copy(target: FastBuffer | Uint8Array, targetStart?: number, sourceStart?: number, sourceEnd?: number): number;
        /**
         * Returns true if both buf and otherBuffer have exactly the same bytes, false otherwise
         *
         * @param { Uint8Array | FastBuffer } otherBuffer - The buffer to compare with this buffer for equality
         * @returns { boolean } true or false
         * @throws { BusinessError } 10200068 - The underlying ArrayBuffer is null or detach.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        equals(otherBuffer: Uint8Array | FastBuffer): boolean;
        /**
         * Returns true if value was found in buf, false otherwise
         *
         * @param { string | number | FastBuffer | Uint8Array } value - The value to search for in the buffer
         * @param { number } [byteOffset] - byteOffset [byteOffset = 0] Where to begin searching in buf. If negative, then offset is calculated from the end of buf
         * @param { BufferEncoding } [encoding] - encoding [encoding='utf8'] If value is a string, this is its encoding
         * @returns { boolean } true or false
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        includes(value: string | number | FastBuffer | Uint8Array, byteOffset?: number, encoding?: BufferEncoding): boolean;
        /**
         * The index of the first occurrence of value in buf
         *
         * @param { string | number | FastBuffer | Uint8Array } value - The value to find the index for in the buffer
         * @param { number } [byteOffset] - byteOffset [byteOffset = 0] Where to begin searching in buf
         * @param { BufferEncoding } [encoding] - encoding [encoding='utf8'] If value is a string,
         * this is the encoding used to determine the binary representation of the string that will be searched for in buf
         * @returns { number } The index of the first occurrence of value in buf, or -1 if buf does not contain value
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        indexOf(value: string | number | FastBuffer | Uint8Array, byteOffset?: number, encoding?: BufferEncoding): number;
        /**
         * Creates and returns an iterator of buf keys (indices).
         *
         * @returns { IterableIterator<number> }
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        keys(): IterableIterator<number>;
        /**
         * Creates and returns an iterator for buf values (bytes).
         *
         * @returns { IterableIterator<number> }
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        values(): IterableIterator<number>;
        /**
         * Creates and returns an iterator of [index, byte] pairs from the contents of buf.
         *
         * @returns { IterableIterator<[ number, number ]> }
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        entries(): IterableIterator<[
            number,
            number
        ]>;
        /**
         * The index of the last occurrence of value in buf
         *
         * @param { string | number | FastBuffer | Uint8Array } value - The value to find the last index for in the buffer
         * @param { number } [byteOffset] - byteOffset [byteOffset = 0] Where to begin searching in buf
         * @param { BufferEncoding } [encoding] - encoding [encoding='utf8'] If value is a string,
         * this is the encoding used to determine the binary representation of the string that will be searched for in buf
         * @returns { number } The index of the last occurrence of value in buf, or -1 if buf does not contain value
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        lastIndexOf(value: string | number | FastBuffer | Uint8Array, byteOffset?: number, encoding?: BufferEncoding): number;
        /**
         * Reads a signed, big-endian 64-bit integer from buf at the specified offset
         *
         * @param { number } [offset] - offset [offset = 0] Number of bytes to skip before starting to read. Must satisfy: 0 <= offset <= buf.length - 8
         * @returns { bigint } Return a signed, big-endian 64-bit integer
         * @throws { BusinessError } 10200001 - The value of "offset" is out of range. It must be >= 0 and <= buf.length - 8. Received value is: [offset]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        readBigInt64BE(offset?: number): bigint;
        /**
         * Reads a signed, little-endian 64-bit integer from buf at the specified offset
         *
         * @param { number } [offset] - offset [offset = 0] Number of bytes to skip before starting to read. Must satisfy: 0 <= offset <= buf.length - 8
         * @returns { bigint } Return a signed, little-endian 64-bit integer
         * @throws { BusinessError } 10200001 - The value of "offset" is out of range. It must be >= 0 and <= buf.length - 8. Received value is: [offset]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        readBigInt64LE(offset?: number): bigint;
        /**
         * Reads a unsigned, big-endian 64-bit integer from buf at the specified offset
         *
         * @param { number } [offset] - offset [offset = 0] Number of bytes to skip before starting to read. Must satisfy: 0 <= offset <= buf.length - 8
         * @returns { bigint } Return a unsigned, big-endian 64-bit integer
         * @throws { BusinessError } 10200001 - The value of "offset" is out of range. It must be >= 0 and <= buf.length - 8. Received value is: [offset]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        readBigUInt64BE(offset?: number): bigint;
        /**
         * Reads a unsigned, little-endian 64-bit integer from buf at the specified offset
         *
         * @param { number } [offset] - offset [offset = 0] Number of bytes to skip before starting to read. Must satisfy: 0 <= offset <= buf.length - 8
         * @returns { bigint } Return a unsigned, little-endian 64-bit integer
         * @throws { BusinessError } 10200001 - The value of "offset" is out of range. It must be >= 0 and <= buf.length - 8. Received value is: [offset]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        readBigUInt64LE(offset?: number): bigint;
        /**
         * Reads a 64-bit, big-endian double from buf at the specified offset
         *
         * @param { number } [offset] - offset [offset = 0] Number of bytes to skip before starting to read. Must satisfy: 0 <= offset <= buf.length - 8
         * @returns { number } Return a 64-bit, big-endian double
         * @throws { BusinessError } 10200001 - The value of "offset" is out of range. It must be >= 0 and <= buf.length - 8. Received value is: [offset]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        readDoubleBE(offset?: number): number;
        /**
         * Reads a 64-bit, little-endian double from buf at the specified offset
         *
         * @param { number } [offset] - offset [offset = 0] Number of bytes to skip before starting to read. Must satisfy: 0 <= offset <= buf.length - 8
         * @returns { number } Return a 64-bit, little-endian double
         * @throws { BusinessError } 10200001 - The value of "offset" is out of range. It must be >= 0 and <= buf.length - 8. Received value is: [offset]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        readDoubleLE(offset?: number): number;
        /**
         * Reads a 32-bit, big-endian float from buf at the specified offset
         *
         * @param { number } [offset] - offset [offset = 0] Number of bytes to skip before starting to read. Must satisfy: 0 <= offset <= buf.length - 4
         * @returns { number } Return a 32-bit, big-endian float
         * @throws { BusinessError } 10200001 - The value of "offset" is out of range. It must be >= 0 and <= buf.length - 4. Received value is: [offset]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        readFloatBE(offset?: number): number;
        /**
         * Reads a 32-bit, little-endian float from buf at the specified offset
         *
         * @param { number } [offset] - offset [offset = 0] Number of bytes to skip before starting to read. Must satisfy: 0 <= offset <= buf.length - 4
         * @returns { number } Return a 32-bit, little-endian float
         * @throws { BusinessError } 10200001 - The value of "offset" is out of range. It must be >= 0 and <= buf.length - 4. Received value is: [offset]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        readFloatLE(offset?: number): number;
        /**
         * Reads a signed 8-bit integer from buf at the specified offset
         *
         * @param { number } [offset] - offset [offset = 0] Number of bytes to skip before starting to read. Must satisfy: 0 <= offset <= buf.length - 1
         * @returns { number } Return a signed 8-bit integer
         * @throws { BusinessError } 10200001 - The value of "offset" is out of range. It must be >= 0 and <= buf.length - 1. Received value is: [offset]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        readInt8(offset?: number): number;
        /**
         * Reads a signed, big-endian 16-bit integer from buf at the specified offset
         *
         * @param { number } [offset] - offset [offset = 0] Number of bytes to skip before starting to read. Must satisfy: 0 <= offset <= buf.length - 2
         * @returns { number } Return a signed, big-endian 16-bit integer
         * @throws { BusinessError } 10200001 - The value of "offset" is out of range. It must be >= 0 and <= buf.length - 2. Received value is: [offset]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        readInt16BE(offset?: number): number;
        /**
         * Reads a signed, little-endian 16-bit integer from buf at the specified offset
         *
         * @param { number } [offset] - offset [offset = 0] Number of bytes to skip before starting to read. Must satisfy: 0 <= offset <= buf.length - 2
         * @returns { number } Return a signed, little-endian 16-bit integer
         * @throws { BusinessError } 10200001 - The value of "offset" is out of range. It must be >= 0 and <= buf.length - 2. Received value is: [offset]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        readInt16LE(offset?: number): number;
        /**
         * Reads a signed, big-endian 32-bit integer from buf at the specified offset
         *
         * @param { number } [offset] - offset [offset = 0] Number of bytes to skip before starting to read. Must satisfy: 0 <= offset <= buf.length - 4
         * @returns { number } Return a signed, big-endian 32-bit integer
         * @throws { BusinessError } 10200001 - The value of "offset" is out of range. It must be >= 0 and <= buf.length - 4. Received value is: [offset]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        readInt32BE(offset?: number): number;
        /**
         * Reads a signed, little-endian 32-bit integer from buf at the specified offset
         *
         * @param { number } [offset] - offset [offset = 0] Number of bytes to skip before starting to read. Must satisfy: 0 <= offset <= buf.length - 4
         * @returns { number } Return a signed, little-endian 32-bit integer
         * @throws { BusinessError } 10200001 - The value of "offset" is out of range. It must be >= 0 and <= buf.length - 4. Received value is: [offset]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        readInt32LE(offset?: number): number;
        /**
         * Reads byteLength number of bytes from buf at the specified offset and interprets the result as a big-endian,
         * two's complement signed value supporting up to 48 bits of accuracy
         *
         * @param { number } offset - Number of bytes to skip before starting to read. Must satisfy: 0 <= offset <= buf.length - byteLength
         * @param { number } byteLength - Number of bytes to read. Must satisfy 0 < byteLength <= 6
         * @returns { number }
         * @throws { BusinessError } 10200001 - The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        readIntBE(offset: number, byteLength: number): number;
        /**
         * Reads byteLength number of bytes from buf at the specified offset and interprets the result as a little-endian,
         * two's complement signed value supporting up to 48 bits of accuracy.
         *
         * @param { number } offset - Number of bytes to skip before starting to read. Must satisfy: 0 <= offset <= buf.length - byteLength
         * @param { number } byteLength - Number of bytes to read. Must satisfy 0 < byteLength <= 6
         * @returns { number }
         * @throws { BusinessError } 10200001 - The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        readIntLE(offset: number, byteLength: number): number;
        /**
         * Reads an unsigned 8-bit integer from buf at the specified offset
         *
         * @param { number } [offset] - offset [offset = 0] Number of bytes to skip before starting to read. Must satisfy 0 <= offset <= buf.length - 1
         * @returns { number } Reads an unsigned 8-bit integer
         * @throws { BusinessError } 10200001 - The value of "offset" is out of range. It must be >= 0 and <= buf.length - 1. Received value is: [offset]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        readUInt8(offset?: number): number;
        /**
         * Reads an unsigned, big-endian 16-bit integer from buf at the specified offset
         *
         * @param { number } [offset] - offset [offset = 0] Number of bytes to skip before starting to read. Must satisfy 0 <= offset <= buf.length - 2
         * @returns { number } Reads an unsigned, big-endian 16-bit integer
         * @throws { BusinessError } 10200001 - The value of "offset" is out of range. It must be >= 0 and <= buf.length - 2. Received value is: [offset]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        readUInt16BE(offset?: number): number;
        /**
         * Reads an unsigned, little-endian 16-bit integer from buf at the specified offset
         *
         * @param { number } [offset] - offset [offset = 0] Number of bytes to skip before starting to read. Must satisfy 0 <= offset <= buf.length - 2
         * @returns { number } Reads an unsigned, little-endian 16-bit integer
         * @throws { BusinessError } 10200001 - The value of "offset" is out of range. It must be >= 0 and <= buf.length - 2. Received value is: [offset]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        readUInt16LE(offset?: number): number;
        /**
         * Reads an unsigned, big-endian 32-bit integer from buf at the specified offset
         *
         * @param { number } [offset] - offset [offset = 0] Number of bytes to skip before starting to read. Must satisfy 0 <= offset <= buf.length - 4
         * @returns { number } Reads an unsigned, big-endian 32-bit integer
         * @throws { BusinessError } 10200001 - The value of "offset" is out of range. It must be >= 0 and <= buf.length - 4. Received value is: [offset]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        readUInt32BE(offset?: number): number;
        /**
         * Reads an unsigned, little-endian 32-bit integer from buf at the specified offset
         *
         * @param { number } [offset] - offset [offset = 0] Number of bytes to skip before starting to read. Must satisfy 0 <= offset <= buf.length - 4
         * @returns { number } Reads an unsigned, little-endian 32-bit integer
         * @throws { BusinessError } 10200001 - The value of "offset" is out of range. It must be >= 0 and <= buf.length - 4. Received value is: [offset]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        readUInt32LE(offset?: number): number;
        /**
         * Reads byteLength number of bytes from buf at the specified offset and interprets the result as
         * an unsigned big-endian integer supporting up to 48 bits of accuracy.
         *
         * @param { number } offset - Number of bytes to skip before starting to read. Must satisfy: 0 <= offset <= buf.length - byteLength
         * @param { number } byteLength - Number of bytes to read. Must satisfy 0 < byteLength <= 6
         * @returns { number }
         * @throws { BusinessError } 10200001 - The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        readUIntBE(offset: number, byteLength: number): number;
        /**
         * Reads byteLength number of bytes from buf at the specified offset and interprets the result as an unsigned,
         * little-endian integer supporting up to 48 bits of accuracy.
         *
         * @param { number } offset - Number of bytes to skip before starting to read. Must satisfy: 0 <= offset <= buf.length - byteLength
         * @param { number } byteLength - Number of bytes to read. Must satisfy 0 < byteLength <= 6
         * @returns { number }
         * @throws { BusinessError } 10200001 - The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        readUIntLE(offset: number, byteLength: number): number;
        /**
         * Returns a new FastBuffer that references the same memory as the original, but offset and cropped by the start and end indices.
         *
         * @param { number } [start] - start [start = 0] Where the new FastBuffer will start
         * @param { number } [end] - end [end = buf.length] Where the new FastBuffer will end (not inclusive)
         * @returns { FastBuffer } Returns a new FastBuffer that references the same memory as the original
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        subarray(start?: number, end?: number): FastBuffer;
        /**
         * Interprets buf as an array of unsigned 16-bit integers and swaps the byte order in-place.
         *
         * @returns { FastBuffer } A reference to buf
         * @throws { BusinessError } 10200009 - The fastbuffer size must be a multiple of 16-bits
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        swap16(): FastBuffer;
        /**
         * Interprets buf as an array of unsigned 32-bit integers and swaps the byte order in-place.
         *
         * @returns { FastBuffer } A reference to buf
         * @throws { BusinessError } 10200009 - The fastbuffer size must be a multiple of 32-bits
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        swap32(): FastBuffer;
        /**
         * Interprets buf as an array of unsigned 64-bit integers and swaps the byte order in-place.
         *
         * @returns { FastBuffer } A reference to buf
         * @throws { BusinessError } 10200009 - The fastbuffer size must be a multiple of 64-bits
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        swap64(): FastBuffer;
        /**
         * Returns a JSON representation of buf
         *
         * @returns { Object } Returns a JSON
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        toJSON(): Object;
        /**
         * Decodes buf to a string according to the specified character encoding in encoding
         *
         * @param { string } [encoding] - encoding [encoding='utf8'] The character encoding to use
         * @param { number } [start] - start [start = 0] The byte offset to start decoding at
         * @param { number } [end] - end [end = buf.length] The byte offset to stop decoding at (not inclusive)
         * @returns { string }
         * @throws { BusinessError } 10200068 - The underlying ArrayBuffer is null or detach.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        toString(encoding?: string, start?: number, end?: number): string;
        /**
         * Writes string to buf at offset according to the character encoding in encoding
         *
         * @param { string } str - The string to write into the buffer
         * @param { number } [offset] - offset [offset = 0] Number of bytes to skip before starting to write string
         * @param { number } [length] - length [length = buf.length - offset] Maximum number of bytes to write (written bytes will not exceed buf.length - offset)
         * @param { string } [encoding] - encoding [encoding='utf8'] The character encoding of string.
         * @returns { number } Number of bytes written.
         * @throws { BusinessError } 10200001 - Range error. Possible causes:
         * The value of the parameter is not within the specified range.
         * @throws { BusinessError } 10200068 - The underlying ArrayBuffer is null or detach.
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        write(str: string, offset?: number, length?: number, encoding?: string): number;
        /**
         * Writes value to buf at the specified offset as big-endian.
         *
         * @param { bigint } value - The 64-bit big-endian integer value to write
         * @param { number } [offset] - offset [offset = 0]  Number of bytes to skip before starting to write. Must satisfy: 0 <= offset <= buf.length - 8
         * @returns { number } offset plus the number of bytes written
         * @throws { BusinessError } 10200001 - The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        writeBigInt64BE(value: bigint, offset?: number): number;
        /**
         * Writes value to buf at the specified offset as little-endian.
         *
         * @param { bigint } value - The 64-bit little-endian integer value to write
         * @param { number } [offset] - offset [offset = 0]  Number of bytes to skip before starting to write. Must satisfy: 0 <= offset <= buf.length - 8
         * @returns { number } offset plus the number of bytes written
         * @throws { BusinessError } 10200001 - The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        writeBigInt64LE(value: bigint, offset?: number): number;
        /**
         * Writes value to buf at the specified offset as big-endian.
         *
         * @param { bigint } value - The unsigned 64-bit big-endian integer value to write
         * @param { number } [offset] - offset [offset = 0]  Number of bytes to skip before starting to write. Must satisfy: 0 <= offset <= buf.length - 8
         * @returns { number } offset plus the number of bytes written
         * @throws { BusinessError } 10200001 - The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        writeBigUInt64BE(value: bigint, offset?: number): number;
        /**
         * Writes value to buf at the specified offset as little-endian.
         *
         * @param { bigint } value - The unsigned 64-bit little-endian integer value to write
         * @param { number } [offset] - offset [offset = 0]  Number of bytes to skip before starting to write. Must satisfy: 0 <= offset <= buf.length - 8
         * @returns { number } offset plus the number of bytes written
         * @throws { BusinessError } 10200001 - The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        writeBigUInt64LE(value: bigint, offset?: number): number;
        /**
         * Writes value to buf at the specified offset as big-endian.
         *
         * @param { number } value - The 64-bit big-endian double value to write
         * @param { number } [offset] - offset [offset = 0]  Number of bytes to skip before starting to write. Must satisfy: 0 <= offset <= buf.length - 8
         * @returns { number } offset plus the number of bytes written
         * @throws { BusinessError } 10200001 - The value of "offset" is out of range. It must be >= 0 and <= buf.length - 8. Received value is: [offset]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        writeDoubleBE(value: number, offset?: number): number;
        /**
         * Writes value to buf at the specified offset as little-endian.
         *
         * @param { number } value - The 64-bit little-endian double value to write
         * @param { number } [offset] - offset [offset = 0]  Number of bytes to skip before starting to write. Must satisfy: 0 <= offset <= buf.length - 8
         * @returns { number } offset plus the number of bytes written
         * @throws { BusinessError } 10200001 - The value of "offset" is out of range. It must be >= 0 and <= buf.length - 8. Received value is: [offset]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        writeDoubleLE(value: number, offset?: number): number;
        /**
         * Writes value to buf at the specified offset as big-endian.
         *
         * @param { number } value - The 32-bit big-endian float value to write
         * @param { number } [offset] - offset [offset = 0]  Number of bytes to skip before starting to write. Must satisfy: 0 <= offset <= buf.length - 4
         * @returns { number } offset plus the number of bytes written
         * @throws { BusinessError } 10200001 - The value of "offset" is out of range. It must be >= 0 and <= buf.length - 4. Received value is: [offset]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        writeFloatBE(value: number, offset?: number): number;
        /**
         * Writes value to buf at the specified offset as little-endian.
         *
         * @param { number } value - The 32-bit little-endian float value to write
         * @param { number } [offset] - offset [offset = 0]  Number of bytes to skip before starting to write. Must satisfy: 0 <= offset <= buf.length - 4
         * @returns { number } offset plus the number of bytes written
         * @throws { BusinessError } 10200001 - The value of "offset" is out of range. It must be >= 0 and <= buf.length - 4. Received value is: [offset]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        writeFloatLE(value: number, offset?: number): number;
        /**
         * Writes value to buf at the specified offset. value must be a valid signed 8-bit integer.
         *
         * @param { number } value - The signed 8-bit integer value to write
         * @param { number } [offset] - offset [offset = 0] Number of bytes to skip before starting to write. Must satisfy: 0 <= offset <= buf.length - 1
         * @returns { number } offset plus the number of bytes written
         * @throws { BusinessError } 10200001 - The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        writeInt8(value: number, offset?: number): number;
        /**
         * Writes value to buf at the specified offset as big-endian. The value must be a valid signed 16-bit integer
         *
         * @param { number } value - The signed 16-bit big-endian integer value to write
         * @param { number } [offset] - offset [offset = 0] Number of bytes to skip before starting to write. Must satisfy: 0 <= offset <= buf.length - 2
         * @returns { number } offset plus the number of bytes written
         * @throws { BusinessError } 10200001 - The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        writeInt16BE(value: number, offset?: number): number;
        /**
         * Writes value to buf at the specified offset as little-endian. The value must be a valid signed 16-bit integer
         *
         * @param { number } value - The signed 16-bit little-endian integer value to write
         * @param { number } [offset] - offset [offset = 0] Number of bytes to skip before starting to write. Must satisfy: 0 <= offset <= buf.length - 2
         * @returns { number } offset plus the number of bytes written
         * @throws { BusinessError } 10200001 - The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        writeInt16LE(value: number, offset?: number): number;
        /**
         * Writes value to buf at the specified offset as big-endian. The value must be a valid signed 32-bit integer.
         *
         * @param { number } value - The signed 32-bit big-endian integer value to write
         * @param { number } [offset] - offset [offset = 0] Number of bytes to skip before starting to write. Must satisfy: 0 <= offset <= buf.length - 4
         * @returns { number } offset plus the number of bytes written
         * @throws { BusinessError } 10200001 - The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        writeInt32BE(value: number, offset?: number): number;
        /**
         * Writes value to buf at the specified offset as little-endian. The value must be a valid signed 32-bit integer.
         *
         * @param { number } value - The signed 32-bit little-endian integer value to write
         * @param { number } [offset] - offset [offset = 0] Number of bytes to skip before starting to write. Must satisfy: 0 <= offset <= buf.length - 4
         * @returns { number } offset plus the number of bytes written
         * @throws { BusinessError } 10200001 - The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        writeInt32LE(value: number, offset?: number): number;
        /**
         * Writes byteLength bytes of value to buf at the specified offset as big-endian
         *
         * @param { number } value - The big-endian integer value to write
         * @param { number } offset - Number of bytes to skip before starting to write. Must satisfy: 0 <= offset <= buf.length - byteLength
         * @param { number } byteLength - Number of bytes to write. Must satisfy 0 < byteLength <= 6
         * @returns { number } offset plus the number of bytes written
         * @throws { BusinessError } 10200001 - The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        writeIntBE(value: number, offset: number, byteLength: number): number;
        /**
         * Writes byteLength bytes of value to buf at the specified offset as little-endian
         *
         * @param { number } value - The little-endian integer value to write
         * @param { number } offset - Number of bytes to skip before starting to write. Must satisfy: 0 <= offset <= buf.length - byteLength
         * @param { number } byteLength - Number of bytes to write. Must satisfy 0 < byteLength <= 6
         * @returns { number } offset plus the number of bytes written
         * @throws { BusinessError } 10200001 - The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        writeIntLE(value: number, offset: number, byteLength: number): number;
        /**
         * Writes value to buf at the specified offset. value must be a valid unsigned 8-bit integer
         *
         * @param { number } value - The unsigned 8-bit integer value to write
         * @param { number } [offset] - offset [offset = 0] Number of bytes to skip before starting to write. Must satisfy 0 <= offset <= buf.length - 1
         * @returns { number } offset plus the number of bytes written
         * @throws { BusinessError } 10200001 - The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        writeUInt8(value: number, offset?: number): number;
        /**
         * Writes value to buf at the specified offset as big-endian. The value must be a valid unsigned 16-bit integer.
         *
         * @param { number } value - The unsigned 16-bit big-endian integer value to write
         * @param { number } [offset] - offset [offset = 0] Number of bytes to skip before starting to write. Must satisfy 0 <= offset <= buf.length - 2
         * @returns { number } offset plus the number of bytes written
         * @throws { BusinessError } 10200001 - The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        writeUInt16BE(value: number, offset?: number): number;
        /**
         * Writes value to buf at the specified offset as little-endian. The value must be a valid unsigned 16-bit integer.
         *
         * @param { number } value - The unsigned 16-bit little-endian integer value to write
         * @param { number } [offset] - offset [offset = 0] Number of bytes to skip before starting to write. Must satisfy 0 <= offset <= buf.length - 2
         * @returns { number } offset plus the number of bytes written
         * @throws { BusinessError } 10200001 - The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        writeUInt16LE(value: number, offset?: number): number;
        /**
         * Writes value to buf at the specified offset as big-endian. The value must be a valid unsigned 32-bit integer.
         *
         * @param { number } value - The unsigned 32-bit big-endian integer value to write
         * @param { number } [offset] - offset [offset = 0] Number of bytes to skip before starting to write. Must satisfy 0 <= offset <= buf.length - 4
         * @returns { number } offset plus the number of bytes written
         * @throws { BusinessError } 10200001 - The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        writeUInt32BE(value: number, offset?: number): number;
        /**
         * Writes value to buf at the specified offset as little-endian. The value must be a valid unsigned 32-bit integer.
         *
         * @param { number } value - The unsigned 32-bit little-endian integer value to write
         * @param { number } [offset] - offset [offset = 0] Number of bytes to skip before starting to write. Must satisfy 0 <= offset <= buf.length - 4
         * @returns { number } offset plus the number of bytes written
         * @throws { BusinessError } 10200001 - The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        writeUInt32LE(value: number, offset?: number): number;
        /**
         * Writes byteLength bytes of value to buf at the specified offset as big-endian
         *
         * @param { number } value - The unsigned big-endian integer value to write
         * @param { number } offset - Number of bytes to skip before starting to write. Must satisfy: 0 <= offset <= buf.length - byteLength
         * @param { number } byteLength - Number of bytes to write. Must satisfy 0 < byteLength <= 6
         * @returns { number } offset plus the number of bytes written
         * @throws { BusinessError } 10200001 - The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        writeUIntBE(value: number, offset: number, byteLength: number): number;
        /**
         * Writes byteLength bytes of value to buf at the specified offset as little-endian
         *
         * @param { number } value - The unsigned little-endian integer value to write
         * @param { number } offset - Number of bytes to skip before starting to write. Must satisfy: 0 <= offset <= buf.length - byteLength
         * @param { number } byteLength - Number of bytes to write. Must satisfy 0 < byteLength <= 6
         * @returns { number } offset plus the number of bytes written
         * @throws { BusinessError } 10200001 - The value of "[param]" is out of range. It must be >= [left range] and <= [right range]. Received value is: [param]
         * @syscap SystemCapability.Utils.Lang
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        writeUIntLE(value: number, offset: number, byteLength: number): number;
    }
}
export default fastbuffer;

```
