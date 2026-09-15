# @ohos.zlib.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2021-2025 Huawei Device Co., Ltd.
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
 * @file
 * @kit BasicServicesKit
 */
import { AsyncCallback } from './@ohos.base';
/**
 * The **Zip** module provides APIs for file compression and decompression.
 *
 * @syscap SystemCapability.BundleManager.Zlib
 * @crossplatform [since 12]
 * @atomicservice [since 11]
 * @since 7
 */
declare namespace zlib {
    /**
     * ErrorCode
     *
     * @syscap SystemCapability.BundleManager.Zlib
     * @since 7
     * @deprecated since 9
     */
    export enum ErrorCode {
        /**
         * @syscap SystemCapability.BundleManager.Zlib
         * @since 7
         * @deprecated since 9
         */
        ERROR_CODE_OK = 0,
        /**
         * @syscap SystemCapability.BundleManager.Zlib
         * @since 7
         * @deprecated since 9
         */
        ERROR_CODE_ERRNO = -1
    }
    /**
     * CompressLevel
     *
     * @syscap SystemCapability.BundleManager.Zlib
     * @crossplatform [since 11]
     * @atomicservice [since 11]
     * @since 7
     */
    export enum CompressLevel {
        /**
         * Compress level 0 that indicates uncompressed.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 7
         */
        COMPRESS_LEVEL_NO_COMPRESSION = 0,
        /**
         * Compression level 1 that gives the best speed.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 7
         */
        COMPRESS_LEVEL_BEST_SPEED = 1,
        /**
         * Compression level 9 that gives the best compression.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 7
         */
        COMPRESS_LEVEL_BEST_COMPRESSION = 9,
        /**
         * Default compression level.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 7
         */
        COMPRESS_LEVEL_DEFAULT_COMPRESSION = -1
    }
    /**
     * CompressStrategy
     *
     * @syscap SystemCapability.BundleManager.Zlib
     * @crossplatform [since 11]
     * @atomicservice [since 11]
     * @since 7
     */
    export enum CompressStrategy {
        /**
         * Default compression strategy.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 7
         */
        COMPRESS_STRATEGY_DEFAULT_STRATEGY = 0,
        /**
         * Filtered compression strategy.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 7
         */
        COMPRESS_STRATEGY_FILTERED = 1,
        /**
         * Huffman coding compression strategy.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 7
         */
        COMPRESS_STRATEGY_HUFFMAN_ONLY = 2,
        /**
         * RLE compression strategy.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 7
         */
        COMPRESS_STRATEGY_RLE = 3,
        /**
         * Fixed compression strategy.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 7
         */
        COMPRESS_STRATEGY_FIXED = 4
    }
    /**
     * ParallelStrategy
     *
     * @syscap SystemCapability.BundleManager.Zlib
     * @crossplatform
     * @atomicservice
     * @since 18
     */
    export enum ParallelStrategy {
        /**
         * Serial compression/decompression strategy (default).
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        PARALLEL_STRATEGY_SEQUENTIAL = 0,
        /**
         * Parallel decompression strategy.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        PARALLEL_STRATEGY_PARALLEL_DECOMPRESSION = 1
    }
    /**
     * Defines **PathSeparatorStrategy**, a property of [Options]{@link zlib.Options}, used to specify the separator
     * strategy for the file path in the compressed package specified for decompression.
     *
     * @syscap SystemCapability.BundleManager.Zlib
     * @atomicservice
     * @since 21
     */
    export enum PathSeparatorStrategy {
        /**
         * Default value, indicating that separators in the file path of the compressed package are not processed.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 21
         */
        PATH_SEPARATOR_STRATEGY_DEFAULT = 0,
        /**
         * Backslashes () in the file path of the package are replaced with slashes (/).
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 21
         */
        PATH_SEPARATOR_STRATEGY_REPLACE_BACKSLASH = 1
    }
    /**
     * MemLevel
     *
     * @syscap SystemCapability.BundleManager.Zlib
     * @crossplatform [since 11]
     * @atomicservice [since 11]
     * @since 7
     */
    export enum MemLevel {
        /**
         * Minimum memory used by the **zlib** API during compression.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 7
         */
        MEM_LEVEL_MIN = 1,
        /**
         * Maximum memory used by the **zlib** API during compression.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 7
         */
        MEM_LEVEL_MAX = 9,
        /**
         * Default memory used by the **zlib** API during compression.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 7
         */
        MEM_LEVEL_DEFAULT = 8
    }
    /**
     * CompressFlushMode
     *
     * @syscap SystemCapability.BundleManager.Zlib
     * @atomicservice
     * @since 12
     */
    export enum CompressFlushMode {
        /**
         * Default value, indicating a normal operation.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        NO_FLUSH = 0,
        /**
         * Generates some refresh points in the stream.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        PARTIAL_FLUSH = 1,
        /**
         * Forcibly outputs all compressed data while maintaining the compression stream state.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        SYNC_FLUSH = 2,
        /**
         * Resets the compression state.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        FULL_FLUSH = 3,
        /**
         * Ends the compression or decompression process.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        FINISH = 4,
        /**
         * Allows more precise control.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        BLOCK = 5,
        /**
         * Implements special purposes.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        TREES = 6
    }
    /**
     * Return codes for the compression/decompression functions.
     *
     * @syscap SystemCapability.BundleManager.Zlib
     * @atomicservice
     * @since 12
     */
    export enum ReturnStatus {
        /**
         * The API is successfully called. This API is supported for use in atomic services.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        OK = 0,
        /**
         * The API is successfully called, indicating that the entire data has been processed.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        STREAM_END = 1,
        /**
         * The API is successfully called, indicating that a preset dictionary is required to continue decompression.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        NEED_DICT = 2,
        /**
         * The API fails to be called, indicating that the file operation is incorrect.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 23
         */
        ERRNO = -1,
        /**
         * The API fails to be called, indicating that the compression or decompression stream is incorrect.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 23
         */
        STREAM_ERROR = -2,
        /**
         * The API fails to be called, indicating that the input data is incorrect.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 23
         */
        DATA_ERROR = -3,
        /**
         * The API fails to be called, indicating that the memory allocation fails.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 23
         */
        MEM_ERROR = -4,
        /**
         * The API fails to be called, indicating that the input buffer is incorrect.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 23
         */
        BUF_ERROR = -5
    }
    /**
     * The deflate compression method (the only one supported in this version).
     *
     * @syscap SystemCapability.BundleManager.Zlib
     * @atomicservice
     * @since 12
     */
    export enum CompressMethod {
        /**
         * Compression method.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        DEFLATED = 8
    }
    /**
     * Defines the reference point for the offset.
     *
     * @syscap SystemCapability.BundleManager.Zlib
     * @atomicservice
     * @since 12
     */
    export enum OffsetReferencePoint {
        /**
         * Searches from the beginning of a file.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        SEEK_SET = 0,
        /**
         * Searches from the current location.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        SEEK_CUR = 1
    }
    /**
     * Defines options used to compress or decompress a ZIP file.
     *
     * @syscap SystemCapability.BundleManager.Zlib
     * @crossplatform [since 11]
     * @atomicservice [since 11]
     * @since 7
     */
    interface Options {
        /**
         * Compression level specified for compression or decompression.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 7
         */
        level?: CompressLevel;
        /**
         * Memory level specified for compression.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 7
         */
        memLevel?: MemLevel;
        /**
         * Compression strategy specified for compression.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @crossplatform [since 11]
         * @atomicservice [since 11]
         * @since 7
         */
        strategy?: CompressStrategy;
        /**
         * Serial or parallel strategy specified for compression or decompression.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @crossplatform
         * @atomicservice
         * @since 18
         */
        parallel?: ParallelStrategy;
        /**
         * Separator strategy for the file path in the compressed package specified for decompression.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 21
         */
        pathSeparatorStrategy?: PathSeparatorStrategy;
        /**
         * Indicates whether to keep the top-level source folder in the compressed file. The default value is false.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        keepTopLevelFolder?: boolean;
    }
    /**
     * Process all the information required for compression and decompression.
     *
     * @syscap SystemCapability.BundleManager.Zlib
     * @atomicservice
     * @since 12
     */
    interface ZStream {
        /**
         * Input bytes to be compressed.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        nextIn?: ArrayBuffer;
        /**
         * Number of bytes available for **nextIn**.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        availableIn?: number;
        /**
         * Total number of input bytes read so far.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        totalIn?: number;
        /**
         * Output bytes after compression.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        nextOut?: ArrayBuffer;
        /**
         * Number of remaining bytes available for **nextOut**.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        availableOut?: number;
        /**
         * Total number of output bytes.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        totalOut?: number;
        /**
         * Binary or text of **deflate**, or decoding state of **inflate**.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        dataType?: number;
        /**
         * Adler-32 or CRC-32 value of uncompressed data.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        adler?: number;
    }
    /**
     * Gzip header information passed to and from zlib routines.
     *
     * @syscap SystemCapability.BundleManager.Zlib
     * @atomicservice
     * @since 12
     */
    interface GzHeader {
        /**
         * Returns **True** if the compressed data is considered text.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        isText?: boolean;
        /**
         * Operating system.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        os?: number;
        /**
         * Modification time.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        time?: number;
        /**
         * Extra flag.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        xflags?: number;
        /**
         * Extra field.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        extra?: ArrayBuffer;
        /**
         * Length of the extra field.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        extraLen?: number;
        /**
         * File name.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        name?: ArrayBuffer;
        /**
         * Comment.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        comment?: ArrayBuffer;
        /**
         * Returns **True** if the **crc** header exists.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        hcrc?: boolean;
        /**
         * Returns **True** after reading the gzip file header.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        done?: boolean;
    }
    /**
     * Compression and decompression return value information.
     *
     * @syscap SystemCapability.BundleManager.Zlib
     * @atomicservice
     * @since 12
     */
    interface ZipOutputInfo {
        /**
         * For details, see [ReturnStatus]{@link zlib.ReturnStatus}.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        status: ReturnStatus;
        /**
         * Total length of the destination buffer.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        destLen: number;
    }
    /**
     * InflateGetDictionary and deflateGetDictionary return value information.
     *
     * @syscap SystemCapability.BundleManager.Zlib
     * @atomicservice
     * @since 12
     */
    interface DictionaryOutputInfo {
        /**
         * For details, see [ReturnStatus]{@link zlib.ReturnStatus}.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        status: ReturnStatus;
        /**
         * Length of a dictionary.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        dictionaryLength: number;
    }
    /**
     * Uncompress2 return value information.
     *
     * @syscap SystemCapability.BundleManager.Zlib
     * @atomicservice
     * @since 12
     */
    interface DecompressionOutputInfo {
        /**
         * For details, see [ReturnStatus]{@link zlib.ReturnStatus}.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        status: ReturnStatus;
        /**
         * Total length of the destination buffer.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        destLength: number;
        /**
         * Length of the source buffer.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        sourceLength: number;
    }
    /**
     * DeflatePending return value information.
     *
     * @syscap SystemCapability.BundleManager.Zlib
     * @atomicservice
     * @since 12
     */
    interface DeflatePendingOutputInfo {
        /**
         * For details, see [ReturnStatus]{@link zlib.ReturnStatus}.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        status: ReturnStatus;
        /**
         * Number of output bytes that have been generated.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        pending: number;
        /**
         * Number of output bits that have been generated.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        bits: number;
    }
    /**
     * GzError return value information.
     *
     * @syscap SystemCapability.BundleManager.Zlib
     * @atomicservice
     * @since 12
     */
    interface GzErrorOutputInfo {
        /**
         * Return Zlib status ReturnStatus the specific meaning is defined as enum.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        status: ReturnStatus;
        /**
         * The last status message reported on the zlib file.
         *
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        statusMsg: string;
    }
    /**
     * A callback function for reading input data provided by a user. When the decompression process requires more
     * input data, zlib will call this function. This function should read data from the data source to the buffer.
     *
     * @param { object } inDesc - A universal user-defined data object.
     *     The specific type and content depend on the actual application scenario, which can include configuration data,
     *     file handles, etc.
     * @returns { ArrayBuffer } Return the buffer successfully read by the data source through the input descriptor.
     * @syscap SystemCapability.BundleManager.Zlib
     * @atomicservice
     * @since 12
     */
    type InflateBackInputCallback = (inDesc: object) => ArrayBuffer;
    /**
     * The output data provided by the user is written into the callback function. Whenever decompressed data is
     * ready for output, zlib calls this function to write the data from the buffer to the target location.
     *
     * @param { object } outDesc - Object passed to output function. Object dependency requirement implementation.
     * @param { ArrayBuffer } buf - Used to store data to be written.
     * @param { number } length - Write the length of the output buffer.
     * @returns { number } Return the number of bytes output.
     * @syscap SystemCapability.BundleManager.Zlib
     * @atomicservice
     * @since 12
     */
    type InflateBackOutputCallback = (outDesc: object, buf: ArrayBuffer, length: number) => number;
    /**
     * Zips a file. The execution result is returned after the compression is complete. This API uses a promise to return
     * the result.
     *
     * @param { string } inFile - Path of the folder or file to zip. The path must be an application sandbox path, which
     *     can be obtained from the context. For details about the context, see [FA Model]{@link ./app/context} and
     *     [Stage Model]{@link ./app/context}.
     * @param { string } outFile - Path of the zipped file. The file name extension is .zip.
     * @param { Options } options - Optional parameters for the zip operation.
     * @returns { Promise<void> } Promise that returns no value.
     * @syscap SystemCapability.BundleManager.Zlib
     * @since 7
     * @deprecated since 9
     * @useinstead zlib.compressFile(inFile: string, outFile: string, options: Options, callback: AsyncCallback<void>)
     */
    function zipFile(inFile: string, outFile: string, options: Options): Promise<void>;
    /**
     * Unzips a file. The execution result is returned after the decompression is complete. This API uses a promise to
     * return the result.
     *
     * > **NOTE**
     * >
     * > The name of the zipped file or zipped folder cannot contain two consecutive periods and a slash (../). Otherwise,
     * > the error code -1 is returned.
     *
     * @param { string } inFile - Path of the file to unzip. The path must be an application sandbox path, which can be
     *     obtained from the context. For details about the context, see [FA Model]{@link ./app/context} and
     *     [Stage Model]{@link ./app/context}. If the.zip file to be unzipped contains Chinese file names or folder names,
     *     use UTF-8 to encode them. Otherwise, garbled characters may be displayed after unzipping.
     * @param { string } outFile - Path of the unzipped file.
     * @param { Options } options - Optional parameters for the unzip operation.
     * @returns { Promise<void> } Promise that returns no value.
     * @syscap SystemCapability.BundleManager.Zlib
     * @since 7
     * @deprecated since 9
     * @useinstead zlib.decompressFile(inFile: string, outFile: string, options: Options, callback: AsyncCallback<void>)
     */
    function unzipFile(inFile: string, outFile: string, options: Options): Promise<void>;
    /**
     * Compresses a file. This API uses an asynchronous callback to return the result.
     *
     * > **NOTE**
     * >
     * > To avoid path traversal, the input parameters of **inFile** and **outFile** cannot contain two consecutive
     * > periods and a slash (../) since API version 13. Otherwise, error codes 900001 and 900002 are returned.
     *
     * @param { string } inFile - Path of the folder or file to compress. The path must be an application sandbox path,
     *     which can be obtained from the context. For details about the context, see [FA Model]{@link ./app/context} and
     *     [Stage Model]{@link ./app/context}. The folder to compress cannot be empty. Otherwise, an error will be
     *     reported when
     *     [decompressFile]{@link zlib.decompressFile(inFile: string, outFile: string, options: Options,
     *     callback: AsyncCallback<void>)} is used to decompress the folder.
     * @param { string } outFile - Path of the compressed file. When multiple threads compress files at the same time, the
     *     values of **outFile** must be different.
     * @param { Options } options - Compression parameters.
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
     *     **null** is returned; otherwise, a specific error code is returned.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types.
     * @throws { BusinessError } 900001 - The input source file is invalid.
     * @throws { BusinessError } 900002 - The input destination file is invalid.
     * @syscap SystemCapability.BundleManager.Zlib
     * @crossplatform [since 11]
     * @atomicservice [since 11]
     * @since 9
     */
    function compressFile(inFile: string, outFile: string, options: Options, callback: AsyncCallback<void>): void;
    /**
     * Compresses a file. This API uses a promise to return the result.
     *
     * > **NOTE**
     * >
     * > To avoid path traversal, the input parameters of **inFile** and **outFile** cannot contain two consecutive
     * > periods and a slash (../) since API version 13. Otherwise, error codes 900001 and 900002 are returned.
     *
     * @param { string } inFile - Path of the folder or file to compress. The path must be an application sandbox path,
     *     which can be obtained from the context. For details about the context, see [FA Model]{@link ./app/context} and
     *     [Stage Model]{@link ./app/context}. The folder to compress cannot be empty. Otherwise, an error will be
     *     reported when
     *     [decompressFile]{@link zlib.decompressFile(inFile: string, outFile: string, options: Options,
     *     callback: AsyncCallback<void>)} is used to decompress the folder.
     * @param { string } outFile - Path of the compressed file. When multiple threads compress files at the same time, the
     *     values of **outFile** must be different.
     * @param { Options } options - Compression parameters.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types.
     * @throws { BusinessError } 900001 - The input source file is invalid.
     * @throws { BusinessError } 900002 - The input destination file is invalid.
     * @syscap SystemCapability.BundleManager.Zlib
     * @crossplatform [since 11]
     * @atomicservice [since 11]
     * @since 9
     */
    function compressFile(inFile: string, outFile: string, options: Options): Promise<void>;
    /**
     * Compresses multiple specified files. This API uses a promise to return the result.
     *
     * @param { Array<string> } inFiles - Path of the folder or file to compress. The path must be an application sandbox
     *     path, which can be obtained from the context. For details about the context, see
     *     [FA Model]{@link ./app/context} and [Stage Model]{@link ./app/context}. The folder to compress cannot be empty.
     *     Otherwise, an error will be reported when
     *     [decompressFile]{@link zlib.decompressFile(inFile: string, outFile: string, options: Options,
     *     callback: AsyncCallback<void>)} is used to decompress the folder.
     * @param { string } outFile - Path of the compressed file. When multiple threads compress files at the same time, the
     *     values of **outFile** must be different.
     * @param { Options } options - Compression parameters.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types.
     * @throws { BusinessError } 900001 - The input source file is invalid.
     * @throws { BusinessError } 900002 - The input destination file is invalid.
     * @syscap SystemCapability.BundleManager.Zlib
     * @atomicservice
     * @since 12
     */
    function compressFiles(inFiles: Array<string>, outFile: string, options: Options): Promise<void>;
    /**
     * Decompresses a file. This API uses an asynchronous callback to return the result.
     *
     * > **NOTE**
     * >
     * > To avoid path traversal, the input parameters of **inFile** and **outFile** cannot contain two consecutive
     * > periods and a slash (../) since API version 13. Otherwise, error codes 900001 and 900002 are returned.
     * >
     * > The name of the zipped file or zipped folder cannot contain two consecutive periods and a slash (../). Otherwise,
     * > the error code 900003 is returned.
     *
     * @param { string } inFile - Path of the file to decompress. The file name extension must be .zip. The path must be
     *     an application sandbox path, which can be obtained from the context. For details about the context, see
     *     [FA Model]{@link ./app/context} and [Stage Model]{@link ./app/context}. If the.zip file to be unzipped contains
     *     Chinese file names or folder names, use UTF-8 to encode them. Otherwise, garbled characters may be displayed
     *     after unzipping.
     * @param { string } outFile - Path of the decompressed file. The path must exist in the system. Otherwise, the
     *     decompression fails. The path must be an application sandbox path, which can be obtained from the context. For
     *     details about the context, see [FA Model]{@link ./app/context} and [Stage Model]{@link ./app/context}. If a
     *     file or folder with the same name already exists in the path, they will be overwritten. When multiple threads
     *     decompress files at the same time, the values of **outFile** must be different.
     * @param { Options } options - Decompression parameters.
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
     *     **null** is returned; otherwise, a specific error code is returned.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types.
     * @throws { BusinessError } 900001 - The input source file is invalid.
     * @throws { BusinessError } 900002 - The input destination file is invalid.
     * @throws { BusinessError } 900003 - The input source file is not in ZIP format or is damaged. [since 10]
     * @syscap SystemCapability.BundleManager.Zlib
     * @crossplatform [since 11]
     * @atomicservice [since 11]
     * @since 9
     */
    function decompressFile(inFile: string, outFile: string, options: Options, callback: AsyncCallback<void>): void;
    /**
     * Decompresses a file. This API uses an asynchronous callback to return the result.
     *
     * > **NOTE**
     * >
     * > To avoid path traversal, the input parameters of **inFile** and **outFile** cannot contain two consecutive
     * > periods and a slash (../) since API version 13. Otherwise, error codes 900001 and 900002 are returned.
     * >
     * > The name of the zipped file or zipped folder cannot contain two consecutive periods and a slash (../). Otherwise,
     * > the error code 900003 is returned.
     *
     * @param { string } inFile - Path of the file to decompress. The file name extension must be .zip. The path must be
     *     an application sandbox path, which can be obtained from the context. For details about the context, see
     *     [FA Model]{@link ./app/context} and [Stage Model]{@link ./app/context}. If the.zip file to be unzipped contains
     *     Chinese file names or folder names, use UTF-8 to encode them. Otherwise, garbled characters may be displayed
     *     after unzipping.
     * @param { string } outFile - Path of the decompressed file. The path must exist in the system. Otherwise, the
     *     decompression fails. The path must be an application sandbox path, which can be obtained from the context. For
     *     details about the context, see [FA Model]{@link ./app/context} and [Stage Model]{@link ./app/context}. If a
     *     file or folder with the same name already exists in the path, they will be overwritten. When multiple threads
     *     decompress files at the same time, the values of **outFile** must be different.
     * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
     *     **null** is returned; otherwise, a specific error code is returned.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types.
     * @throws { BusinessError } 900001 - The input source file is invalid.
     * @throws { BusinessError } 900002 - The input destination file is invalid.
     * @throws { BusinessError } 900003 - The input source file is not in ZIP format or is damaged.
     * @syscap SystemCapability.BundleManager.Zlib
     * @crossplatform [since 11]
     * @atomicservice [since 11]
     * @since 10
     */
    function decompressFile(inFile: string, outFile: string, callback: AsyncCallback<void>): void;
    /**
     * Decompresses a file. This API uses a promise to return the result.
     *
     * > **NOTE**
     * >
     * > To avoid path traversal, the input parameters of **inFile** and **outFile** cannot contain two consecutive
     * > periods and a slash (../) since API version 13. Otherwise, error codes 900001 and 900002 are returned.
     * >
     * > The name of the zipped file or zipped folder cannot contain two consecutive periods and a slash (../). Otherwise,
     * > the error code 900003 is returned.
     *
     * @param { string } inFile - Path of the file to decompress. The file name extension must be .zip. The path must be
     *     an application sandbox path, which can be obtained from the context. For details about the context, see
     *     [FA Model]{@link ./app/context} and [Stage Model]{@link ./app/context}. If the.zip file to be unzipped contains
     *     Chinese file names or folder names, use UTF-8 to encode them. Otherwise, garbled characters may be displayed
     *     after unzipping.
     * @param { string } outFile - Path of the decompressed file. The path must exist in the system. Otherwise, the
     *     decompression fails. The path must be an application sandbox path, which can be obtained from the context. For
     *     details about the context, see [FA Model]{@link ./app/context} and [Stage Model]{@link ./app/context}. If a
     *     file or folder with the same name already exists in the path, they will be overwritten. When multiple threads
     *     decompress files at the same time, the values of **outFile** must be different.
     * @param { Options } options - Decompression parameters.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.
     *     Incorrect parameter types.
     * @throws { BusinessError } 900001 - The input source file is invalid.
     * @throws { BusinessError } 900002 - The input destination file is invalid.
     * @throws { BusinessError } 900003 - The input source file is not in ZIP format or is damaged. [since 10]
     * @syscap SystemCapability.BundleManager.Zlib
     * @crossplatform [since 11]
     * @atomicservice [since 11]
     * @since 9
     */
    function decompressFile(inFile: string, outFile: string, options?: Options): Promise<void>;
    /**
     * Obtains the original size of a compressed file. This API uses a promise to return the result.
     *
     * @param { string } compressedFile - Specifies the path of the compressed file. Only .zip files are supported. The
     *     path must be an application sandbox path, which can be obtained from the context. For details about the context
     *     , see [FA Model]{@link ./app/context} and [Stage Model]{@link ./app/context}.
     * @returns { Promise<number> } Promise object, which returns the original size of the compressed file, in bytes.
     * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
     *     unspecified; 2. Incorrect parameter types.
     * @throws { BusinessError } 900001 - The input source file is invalid.
     * @throws { BusinessError } 900003 - The input source file is not in ZIP format or is damaged.
     * @syscap SystemCapability.BundleManager.Zlib
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    function getOriginalSize(compressedFile: string): Promise<number>;
    /**
     * Creates this checksum object. This API uses a promise to return the result.
     *
     * @returns { Promise<Checksum> } Promise used to return the created checksum object.
     * @syscap SystemCapability.BundleManager.Zlib
     * @atomicservice
     * @since 12
     */
    function createChecksum(): Promise<Checksum>;
    /**
     * Creates this checksum object. A checksum instance is returned upon a success.
     *
     * @returns { Checksum } Checksum object instance.
     * @syscap SystemCapability.BundleManager.Zlib
     * @atomicservice
     * @since 12
     */
    function createChecksumSync(): Checksum;
    /**
     * Creates this **Zip** instance. This API uses a promise to return the result.
     *
     * @returns { Promise<Zip> } Promise used to return the **Zip** instance created.
     * @syscap SystemCapability.BundleManager.Zlib
     * @atomicservice
     * @since 12
     */
    function createZip(): Promise<Zip>;
    /**
     * Creates this **Zip** instance. A **Zip** instance is returned upon a success.
     *
     * @returns { Zip } The **Zip** instance created.
     * @syscap SystemCapability.BundleManager.Zlib
     * @atomicservice
     * @since 12
     */
    function createZipSync(): Zip;
    /**
     * Creates this **GZip** object. This API uses a promise to return the result.
     *
     * @returns { Promise<GZip> } Promise used to return the **GZip** object created.
     * @syscap SystemCapability.BundleManager.Zlib
     * @atomicservice
     * @since 12
     */
    function createGZip(): Promise<GZip>;
    /**
     * Creates this **GZip** object. A **GZip** instance is returned upon a success.
     *
     * @returns { GZip } gzip object instance.
     * @syscap SystemCapability.BundleManager.Zlib
     * @atomicservice
     * @since 12
     */
    function createGZipSync(): GZip;
    /**
     * Checksum object.
     *
     * @syscap SystemCapability.BundleManager.Zlib
     * @atomicservice
     * @since 12
     */
    interface Checksum {
        /**
         * Calculates the Adler-32 checksum. This API uses a promise to return the result.
         *
         * @param { number } adler - Initial value of the Adler-32 checksum.
         * @param { ArrayBuffer } buf - Data buffer for calculating the checksum.
         * @returns { Promise<number> } Promise used to return the calculated Adler-32 checksum.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        adler32(adler: number, buf: ArrayBuffer): Promise<number>;
        /**
         * Combines two Adler-32 checksums. This API uses a promise to return the result.
         *
         * @param { number } adler1 - The first Adler-32 checksum to be combined.
         * @param { number } adler2 - The second Adler-32 checksum to be combined.
         * @param { number } len2 - Length of the data block of the second Adler-32 checksum.
         * @returns { Promise<number> } Promise used to return the combined Adler-32 checksum.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        adler32Combine(adler1: number, adler2: number, len2: number): Promise<number>;
        /**
         * Updates a CRC-32 checksum. This API uses a promise to return the result.
         *
         * @param { number } crc - Initial value of the CRC-32 checksum.
         * @param { ArrayBuffer } buf - Data buffer for calculating the checksum.
         * @returns { Promise<number> } Promise used to return the updated CRC-32 checksum.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        crc32(crc: number, buf: ArrayBuffer): Promise<number>;
        /**
         * Combines two CRC-32 checksums. This API uses a promise to return the result.
         *
         * @param { number } crc1 - The first CRC-32 checksum to be combined.
         * @param { number } crc2 - The second CRC-32 checksum to be combined.
         * @param { number } len2 - Indicates the length of the second data block checked by CRC-32
         * @returns { Promise<number> } Promise used to return the combined CRC-32 checksum.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        crc32Combine(crc1: number, crc2: number, len2: number): Promise<number>;
        /**
         * Updates a CRC-64 checksum. This API uses a promise to return the result.
         *
         * @param { number } crc - Initial value of the CRC-64 checksum.
         * @param { ArrayBuffer } buf - Data buffer for calculating the checksum.
         * @returns { Promise<number> } Promise used to return the updated CRC-64 checksum.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types; 3. Parameter verification failed.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        crc64(crc: number, buf: ArrayBuffer): Promise<number>;
        /**
         * Obtains this CRC-32 checksum table. This API uses a promise to return the result.
         *
         * @returns { Promise<Array<number>> } Promise used to return the CRC-32 checksum table.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        getCrcTable(): Promise<Array<number>>;
        /**
         * Obtains this CRC-64 checksum table. This API uses a promise to return the result.
         *
         * @returns { Promise<Array<number>> } Promise used to return the CRC-64 checksum table.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        getCrc64Table(): Promise<Array<number>>;
    }
    /**
     * Defines the **Zip** instance. It provides APIs to zip or unzip data in Zlib, Deflate, or Gzip format.
     *
     * @syscap SystemCapability.BundleManager.Zlib
     * @atomicservice
     * @since 12
     */
    interface Zip {
        /**
         * Obtains this stream. This API uses a promise to return the result.
         *
         * @returns { Promise<ZStream> } Promise used to return the **ZStream** object.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        getZStream(): Promise<ZStream>;
        /**
         * Obtains the version information of this zlib library connected. This API uses a promise to return the result.
         *
         * @returns { Promise<string> } Promise used to return the version of the current zlib library.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        zlibVersion(): Promise<string>;
        /**
         * Returns the flags indicating compile-time options. This API uses a promise to return the result.
         *
         * @returns { Promise<number> } Promise used to return the flags indicating compile-time options.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        zlibCompileFlags(): Promise<number>;
        /**
         * Compresses the source buffer into the destination buffer. This API uses a promise to return the result.
         *
         * @param { ArrayBuffer } dest - Destination buffer.
         * @param { ArrayBuffer } source - Source buffer.
         * @param { number } sourceLen - Length of the source data. The default value is **0**.
         * @returns { Promise<ZipOutputInfo> } Promise used to return the result status and the total size of the
         *     destination buffer.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800007 - The input buffer is incorrect, and the output buffer is too small to
         *     accommodate the compressed or decompressed data.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        compress(dest: ArrayBuffer, source: ArrayBuffer, sourceLen?: number): Promise<ZipOutputInfo>;
        /**
         * Compresses the source buffer into the destination buffer. This API uses a promise to return the result.
         *
         * @param { ArrayBuffer } dest - Destination buffer.
         * @param { ArrayBuffer } source - Source buffer.
         * @param { CompressLevel } level - For details, see [CompressLevel]{@link zlib.CompressLevel}.
         * @param { number } sourceLen - Length of the source data. The default value is **0**.
         * @returns { Promise<ZipOutputInfo> } Promise used to return the result status and the total size of the
         *     destination buffer.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800004 - Compression or decompression stream error, which may be caused by an
         *     initialization error in the zlib stream structure or a modified structure.
         * @throws { BusinessError } 17800007 - The input buffer is incorrect, and the output buffer is too small to
         *     accommodate the compressed or decompressed data.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        compress2(dest: ArrayBuffer, source: ArrayBuffer, level: CompressLevel, sourceLen?: number): Promise<ZipOutputInfo>;
        /**
         * Calculates the maximum size of the compressed data to be returned. This API uses a promise to return the result.
         *
         * @param { number } sourceLen - Length of the source data.
         * @returns { Promise<number> } Promise used to return the maximum size of the compressed data.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        compressBound(sourceLen: number): Promise<number>;
        /**
         * Decompresses the compressed data into the raw data. This API uses a promise to return the result.
         *
         * @param { ArrayBuffer } dest - Destination buffer.
         * @param { ArrayBuffer } source - Source buffer.
         * @param { number } sourceLen - Length of the source data. The default value is **0**.
         * @returns { Promise<ZipOutputInfo> } Promise used to return the result status and the total size of the
         *     destination buffer.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800005 - The input data is incorrect. For example, the data does not conform to the
         *     zlib compression format, the compressed data is corrupted, or the data is not compressed.
         * @throws { BusinessError } 17800007 - The input buffer is incorrect, and the output buffer is too small to
         *     accommodate the compressed or decompressed data.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        uncompress(dest: ArrayBuffer, source: ArrayBuffer, sourceLen?: number): Promise<ZipOutputInfo>;
        /**
         * Decompresses the compressed data into the raw data. This API uses a promise to return the result.
         *
         * @param { ArrayBuffer } dest - Destination buffer.
         * @param { ArrayBuffer } source - Source buffer.
         * @param { number } sourceLen - Length of the source data. The default value is **0**.
         * @returns { Promise<DecompressionOutputInfo> } Promise used to return the result status, total size of the
         *     destination buffer, and the length of the source data.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800005 - The input data is incorrect. For example, the data does not conform to the
         *     zlib compression format, the compressed data is corrupted, or the data is not compressed.
         * @throws { BusinessError } 17800007 - The input buffer is incorrect, and the output buffer is too small to
         *     accommodate the compressed or decompressed data.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        uncompress2(dest: ArrayBuffer, source: ArrayBuffer, sourceLen?: number): Promise<DecompressionOutputInfo>;
        /**
         * Validates the checksum inside the compression stream. This API uses a promise to return the result.
         *
         * @param { ZStream } strm - For details, see [ZStream<sup>12+</sup>]{@link zlib.ZStream}.
         * @param { number } check - Expected checksum.
         * @returns { Promise<ReturnStatus> } Promise used to return the result status.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800004 - Compression or decompression stream error, which may be caused by an
         *     initialization error in the zlib stream structure or a modified structure.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        inflateValidate(strm: ZStream, check: number): Promise<ReturnStatus>;
        /**
         * Finds the synchronization point of a decompression stream. This API uses a promise to return the result.
         *
         * @param { ZStream } strm - For details, see [ZStream<sup>12+</sup>]{@link zlib.ZStream}.
         * @returns { Promise<ReturnStatus> } Promise used to return the result status.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800004 - Compression or decompression stream error, which may be caused by an
         *     initialization error in the zlib stream structure or a modified structure.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        inflateSyncPoint(strm: ZStream): Promise<ReturnStatus>;
        /**
         * Skips invalid compressed data until a possible complete refresh point is found. This API uses a promise to return
         * the result.
         *
         * @param { ZStream } strm - For details, see [ZStream<sup>12+</sup>]{@link zlib.ZStream}.
         * @returns { Promise<ReturnStatus> } Promise used to return the result status.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800004 - Compression or decompression stream error, which may be caused by an
         *     initialization error in the zlib stream structure or a modified structure.
         * @throws { BusinessError } 17800005 - The input data is incorrect. For example, the data does not conform to the
         *     zlib compression format, the compressed data is corrupted, or the data is not compressed.
         * @throws { BusinessError } 17800007 - The input buffer is incorrect, and the output buffer is too small to
         *     accommodate the compressed or decompressed data.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        inflateSync(strm: ZStream): Promise<ReturnStatus>;
        /**
         * Initializes the dictionary content of a decompression stream based on the given dictionary data. This API uses a
         * promise to return the result.
         *
         * @param { ZStream } strm - For details, see [ZStream<sup>12+</sup>]{@link zlib.ZStream}.
         * @param { ArrayBuffer } dictionary - Dictionary data.
         * @returns { Promise<ReturnStatus> } Promise used to return the result status.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800004 - Compression or decompression stream error, which may be caused by an
         *     initialization error in the zlib stream structure or a modified structure.
         * @throws { BusinessError } 17800005 - The input data is incorrect. For example, the data does not conform to the
         *     zlib compression format, the compressed data is corrupted, or the data is not compressed.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        inflateSetDictionary(strm: ZStream, dictionary: ArrayBuffer): Promise<ReturnStatus>;
        /**
         * Resets the state of the decompression stream to retain the allocated Huffman tree and preset dictionary. This API
         * uses a promise to return the result.
         *
         * @param { ZStream } strm - For details, see [ZStream<sup>12+</sup>]{@link zlib.ZStream}.
         * @returns { Promise<ReturnStatus> } Promise used to return the result status.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800004 - Compression or decompression stream error, which may be caused by an
         *     initialization error in the zlib stream structure or a modified structure.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        inflateResetKeep(strm: ZStream): Promise<ReturnStatus>;
        /**
         * Resets the status of the specified decompression stream and updates the window size to start a new decompression
         * operation. The internal buffer is not released or reallocated. This API uses a promise to return the result.
         *
         * @param { ZStream } strm - For details, see [ZStream<sup>12+</sup>]{@link zlib.ZStream}.
         * @param { number } windowBits - Memory window size. The value is restricted in certain range based on the data
         *     formats. The options are as follows:<br>Zlib: [1, 15]<br>Gzip: (15, +∞)<br>Raw Deflate: [-15, -1]
         * @returns { Promise<ReturnStatus> } Promise used to return the result status.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800004 - Compression or decompression stream error, which may be caused by an
         *     initialization error in the zlib stream structure or a modified structure.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        inflateReset2(strm: ZStream, windowBits: number): Promise<ReturnStatus>;
        /**
         * Resets the status of the specified decompression stream to the initial state to start a new decompression
         * operation. The internal buffer is not released or reallocated. This API uses a promise to return the result.
         *
         * @param { ZStream } strm - For details, see [ZStream<sup>12+</sup>]{@link zlib.ZStream}.
         * @returns { Promise<ReturnStatus> } Promise used to return the result status.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800004 - Compression or decompression stream error, which may be caused by an
         *     initialization error in the zlib stream structure or a modified structure.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        inflateReset(strm: ZStream): Promise<ReturnStatus>;
        /**
         * Sets the initial number of bits and bit value in the specified decompression stream to pre-fill the bit buffer at
         * the beginning of the decompression stream to correctly process the data. This API uses a promise to return the
         * result.
         *
         * @param { ZStream } strm - For details, see [ZStream<sup>12+</sup>]{@link zlib.ZStream}.
         * @param { number } bits - Number of bits to be written to the bit buffer.
         * @param { number } value - Bit value used to fill the bit buffer.
         * @returns { Promise<ReturnStatus> } Promise used to return the result status.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800004 - Compression or decompression stream error, which may be caused by an
         *     initialization error in the zlib stream structure or a modified structure.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        inflatePrime(strm: ZStream, bits: number, value: number): Promise<ReturnStatus>;
        /**
         * Marks the location of the input data for random access. This API uses a promise to return the result.
         *
         * @param { ZStream } strm - For details, see [ZStream<sup>12+</sup>]{@link zlib.ZStream}.
         * @returns { Promise<number> } Promise used to return the current location.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        inflateMark(strm: ZStream): Promise<number>;
        /**
         * Initializes a decompression stream with the specified **windowBits**. This API uses a promise to return the
         * result.
         *
         * @param { ZStream } strm - For details, see [ZStream<sup>12+</sup>]{@link zlib.ZStream}.
         * @param { number } windowBits - Memory window size. The value is restricted in certain range based on the data
         *     formats. The options are as follows:<br>Zlib: [1, 15]<br>Gzip: (15, +∞)<br>Raw Deflate: [-15, -1]
         * @returns { Promise<ReturnStatus> } Promise used to return the result status.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800004 - Compression or decompression stream error, which may be caused by an
         *     initialization error in the zlib stream structure or a modified structure.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        inflateInit2(strm: ZStream, windowBits: number): Promise<ReturnStatus>;
        /**
         * Initializes a decompression stream. This API uses a promise to return the result.
         *
         * @param { ZStream } strm - For details, see [ZStream<sup>12+</sup>]{@link zlib.ZStream}.
         * @returns { Promise<ReturnStatus> } Promise used to return the result status.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        inflateInit(strm: ZStream): Promise<ReturnStatus>;
        /**
         * Obtains the header information of a gzip file before decompressing data. This API uses a promise to return the
         * result.
         *
         * @param { ZStream } strm - For details, see [ZStream<sup>12+</sup>]{@link zlib.ZStream}.
         * @param { GzHeader } header - Header information of a gzip file extracted from the compressed data stream.
         * @returns { Promise<ReturnStatus> } Promise used to return the result status.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800004 - Compression or decompression stream error, which may be caused by an
         *     initialization error in the zlib stream structure or a modified structure.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        inflateGetHeader(strm: ZStream, header: GzHeader): Promise<ReturnStatus>;
        /**
         * Obtains the content and length of the decompression dictionary used in a decompression stream. This API uses a
         * promise to return the result.
         *
         * @param { ZStream } strm - For details, see [ZStream<sup>12+</sup>]{@link zlib.ZStream}.
         * @param { ArrayBuffer } dictionary - Receives the actual contents of the decompression dictionary.
         * @returns { Promise<DictionaryOutputInfo> } Promise used to return the result status and length of the dictionary.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800004 - Compression or decompression stream error, which may be caused by an
         *     initialization error in the zlib stream structure or a modified structure.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        inflateGetDictionary(strm: ZStream, dictionary: ArrayBuffer): Promise<DictionaryOutputInfo>;
        /**
         * Releases all dynamically allocated data structs of a decompression stream. This API uses a promise to return the
         * result.
         *
         * @param { ZStream } strm - For details, see [ZStream<sup>12+</sup>]{@link zlib.ZStream}.
         * @returns { Promise<ReturnStatus> } Promise used to return the result status.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800004 - Compression or decompression stream error, which may be caused by an
         *     initialization error in the zlib stream structure or a modified structure.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        inflateEnd(strm: ZStream): Promise<ReturnStatus>;
        /**
         * Copies a decompression stream. This API uses a promise to return the result.
         *
         * @param { Zip } source - For details, see [Zip<sup>12+</sup>]{@link zlib.Zip}.
         * @returns { Promise<ReturnStatus> } Promise used to return the result status.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800004 - Compression or decompression stream error, which may be caused by an
         *     initialization error in the zlib stream structure or a modified structure.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        inflateCopy(source: Zip): Promise<ReturnStatus>;
        /**
         * Describes the number of Huffman trees used in a decompression stream. This API uses a promise to return the
         * result.
         *
         * @param { ZStream } strm - For details, see [ZStream<sup>12+</sup>]{@link zlib.ZStream}.
         * @returns { Promise<number> } Promise used to return the number of Huffman trees that have been used.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        inflateCodesUsed(strm: ZStream): Promise<number>;
        /**
         * Initializes the internal stream state for decompression before using the **inflateBack()** function. This API
         * uses a promise to return the result.
         *
         * @param { ZStream } strm - For details, see [ZStream<sup>12+</sup>]{@link zlib.ZStream}.
         * @param { number } windowBits - Memory window size. The value is restricted in certain range based on the data
         *     formats. The options are as follows:<br>Zlib: [1, 15]<br>Gzip: (15, +∞)<br>Raw Deflate: [-15, -1]
         * @param { ArrayBuffer } window - Preset window buffer.
         * @returns { Promise<ReturnStatus> } Promise used to return the result status.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800004 - Compression or decompression stream error, which may be caused by an
         *     initialization error in the zlib stream structure or a modified structure.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        inflateBackInit(strm: ZStream, windowBits: number, window: ArrayBuffer): Promise<ReturnStatus>;
        /**
         * Releases all memory allocated by the **inflateBackInit()** function. This API uses a promise to return the
         * result.
         *
         * @param { ZStream } strm - For details, see [ZStream<sup>12+</sup>]{@link zlib.ZStream}.
         * @returns { Promise<ReturnStatus> } Promise used to return the result status.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800004 - Compression or decompression stream error, which may be caused by an
         *     initialization error in the zlib stream structure or a modified structure.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        inflateBackEnd(strm: ZStream): Promise<ReturnStatus>;
        /**
         * Implements decompression and uses callbacks to process input and output data. This API uses a promise to return
         * the result.
         *
         * @param { ZStream } strm - For details, see [ZStream<sup>12+</sup>]{@link zlib.ZStream}.
         * @param { InflateBackInputCallback } backIn - A function used to decompress data from the end of the array to read
         *     the original compressed data from the input source.
         * @param { object } inDesc - Common object.
         * @param { InflateBackOutputCallback } backOut - Writes the decompressed data to the destination buffer.
         * @param { object } outDesc - Common object.
         * @returns { Promise<ReturnStatus> } Promise used to return the result status.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800004 - Compression or decompression stream error, which may be caused by an
         *     initialization error in the zlib stream structure or a modified structure.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        inflateBack(strm: ZStream, backIn: InflateBackInputCallback, inDesc: object, backOut: InflateBackOutputCallback, outDesc: object): Promise<ReturnStatus>;
        /**
         * Inflates data. This API uses a promise to return the result.
         *
         * @param { ZStream } strm - For details, see [ZStream<sup>12+</sup>]{@link zlib.ZStream}.
         * @param { CompressFlushMode } flush - For details, see [CompressFlushMode]{@link zlib.CompressFlushMode}.
         * @returns { Promise<ReturnStatus> } Promise used to return the result status.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800004 - Compression or decompression stream error, which may be caused by an
         *     initialization error in the zlib stream structure or a modified structure.
         * @throws { BusinessError } 17800005 - The input data is incorrect. For example, the data does not conform to the
         *     zlib compression format, the compressed data is corrupted, or the data is not compressed.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        inflate(strm: ZStream, flush: CompressFlushMode): Promise<ReturnStatus>;
        /**
         * Initializes a compression stream with a specified compression level. This API uses a promise to return the
         * result.
         *
         * @param { ZStream } strm - For details, see [ZStream<sup>12+</sup>]{@link zlib.ZStream}.
         * @param { CompressLevel } level - For details, see [CompressLevel]{@link zlib.CompressLevel}.
         * @returns { Promise<ReturnStatus> } Promise used to return the result status.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800004 - Compression or decompression stream error, which may be caused by an
         *     initialization error in the zlib stream structure or a modified structure.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        deflateInit(strm: ZStream, level: CompressLevel): Promise<ReturnStatus>;
        /**
         * Initializes a compression stream with the specified compression level, compression method, window size, memory
         * level, and compression strategy. This API uses a promise to return the result.
         *
         * @param { ZStream } strm - For details, see [ZStream<sup>12+</sup>]{@link zlib.ZStream}.
         * @param { CompressLevel } level - For details, see [CompressLevel]{@link zlib.CompressLevel}.
         * @param { CompressMethod } method - For details, see [CompressMethod]{@link zlib.CompressMethod}.
         * @param { number } windowBits - Memory window size. The value is restricted in certain range based on the data
         *     formats. The options are as follows:<br>Zlib: [1, 15]<br>Gzip: (15, +∞)<br>Raw Deflate: [-15, -1]
         * @param { MemLevel } memLevel - For details, see [MemLevel]{@link zlib.MemLevel}.
         * @param { CompressStrategy } strategy - For details, see [CompressStrategy]{@link zlib.CompressStrategy}.
         * @returns { Promise<ReturnStatus> } Promise used to return the result status.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800004 - Compression or decompression stream error, which may be caused by an
         *     initialization error in the zlib stream structure or a modified structure.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        deflateInit2(strm: ZStream, level: CompressLevel, method: CompressMethod, windowBits: number, memLevel: MemLevel, strategy: CompressStrategy): Promise<ReturnStatus>;
        /**
         * Deflates data. This API uses a promise to return the result.
         *
         * @param { ZStream } strm - For details, see [ZStream<sup>12+</sup>]{@link zlib.ZStream}.
         * @param { CompressFlushMode } flush - For details, see [CompressFlushMode]{@link zlib.CompressFlushMode}.
         * @returns { Promise<ReturnStatus> } Promise used to return the result status.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800004 - Compression or decompression stream error, which may be caused by an
         *     initialization error in the zlib stream structure or a modified structure.
         * @throws { BusinessError } 17800007 - The input buffer is incorrect, and the output buffer is too small to
         *     accommodate the compressed or decompressed data.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        deflate(strm: ZStream, flush: CompressFlushMode): Promise<ReturnStatus>;
        /**
         * Releases all dynamically allocated data structs of a decompression stream. This API uses a promise to return the
         * result.
         *
         * @param { ZStream } strm - For details, see [ZStream<sup>12+</sup>]{@link zlib.ZStream}.
         * @returns { Promise<ReturnStatus> } Promise used to return the result status.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800004 - Compression or decompression stream error, which may be caused by an
         *     initialization error in the zlib stream structure or a modified structure.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        deflateEnd(strm: ZStream): Promise<ReturnStatus>;
        /**
         * Calculates the maximum size of the compressed data. This API uses a promise to return the result.
         *
         * @param { ZStream } strm - For details, see [ZStream<sup>12+</sup>]{@link zlib.ZStream}.
         * @param { number } sourceLength - Length of the source data.
         * @returns { Promise<number> } Promise used to return the maximum size of the compressed data.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        deflateBound(strm: ZStream, sourceLength: number): Promise<number>;
        /**
         * Provides the header information of a gzip file when **deflateInit2()** requests a gzip stream. This API uses a
         * promise to return the result.
         *
         * @param { ZStream } strm - For details, see [ZStream<sup>12+</sup>]{@link zlib.ZStream}.
         * @param { GzHeader } head - Header information of a gzip file extracted from the compressed data stream.
         * @returns { Promise<ReturnStatus> } Promise used to return the result status.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800004 - Compression or decompression stream error, which may be caused by an
         *     initialization error in the zlib stream structure or a modified structure.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        deflateSetHeader(strm: ZStream, head: GzHeader): Promise<ReturnStatus>;
        /**
         * Copies a compression stream. This API uses a promise to return the result.
         *
         * @param { Zip } source - For details, see [Zip<sup>12+</sup>]{@link zlib.Zip}.
         * @returns { Promise<ReturnStatus> } Promise used to return the result status.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800004 - Compression or decompression stream error, which may be caused by an
         *     initialization error in the zlib stream structure or a modified structure.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        deflateCopy(source: Zip): Promise<ReturnStatus>;
        /**
         * Initializes the compression dictionary from a given sequence of bytes. This API uses a promise to return the
         * result.
         *
         * @param { ZStream } strm - For details, see [ZStream<sup>12+</sup>]{@link zlib.ZStream}.
         * @param { ArrayBuffer } dictionary - Dictionary data.
         * @returns { Promise<ReturnStatus> } Promise used to return the result status.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800004 - Compression or decompression stream error, which may be caused by an
         *     initialization error in the zlib stream structure or a modified structure.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        deflateSetDictionary(strm: ZStream, dictionary: ArrayBuffer): Promise<ReturnStatus>;
        /**
         * Obtains the content and length of the decompression dictionary used in a compression stream. This API uses a
         * promise to return the result.
         *
         * @param { ZStream } strm - For details, see [ZStream<sup>12+</sup>]{@link zlib.ZStream}.
         * @param { ArrayBuffer } dictionary - Buffer that receives the actual contents of the decompression dictionary.
         * @returns { Promise<DictionaryOutputInfo> } Promise used to return the result status and length of the dictionary.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800004 - Compression or decompression stream error, which may be caused by an
         *     initialization error in the zlib stream structure or a modified structure.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        deflateGetDictionary(strm: ZStream, dictionary: ArrayBuffer): Promise<DictionaryOutputInfo>;
        /**
         * Fine-tunes the internal compression parameters of **deflate**. This API uses a promise to return the result.
         *
         * @param { ZStream } strm - For details, see [ZStream<sup>12+</sup>]{@link zlib.ZStream}.
         * @param { number } goodLength - Matched length threshold.
         * @param { number } maxLazy - Delay matching strategy used when the compression algorithm builds a Huffman tree. The
         *     value is an integer ranging from 0 to 4. **1**–**4**: A larger value indicates a lazier algorithm, which
         *     performs a slower matching process but generates a better compression result. **0**: Lazy matching is
         *     disabled. The algorithm builds a Huffman tree as soon as possible. The compression speed is fast, but the
         *     compression ratio is low.
         * @param { number } niceLength - Appropriate delay length threshold.
         * @param { number } maxChain - Maximum chain length.
         * @returns { Promise<ReturnStatus> } Promise used to return the result status.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800004 - Compression or decompression stream error, which may be caused by an
         *     initialization error in the zlib stream structure or a modified structure.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        deflateTune(strm: ZStream, goodLength: number, maxLazy: number, niceLength: number, maxChain: number): Promise<ReturnStatus>;
        /**
         * Equivalent to call the **deflateEnd** API and then the **deflateInit** API. However, this API does not release or
         * reallocate the internal decompression state. This API uses a promise to return the result.
         *
         * @param { ZStream } strm - For details, see [ZStream<sup>12+</sup>]{@link zlib.ZStream}.
         * @returns { Promise<ReturnStatus> } Promise used to return the result status.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800004 - Compression or decompression stream error, which may be caused by an
         *     initialization error in the zlib stream structure or a modified structure.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        deflateReset(strm: ZStream): Promise<ReturnStatus>;
        /**
         * Resets the initialized compression stream, but retains the compression parameters and dictionaries set by it.
         * This API uses a promise to return the result.
         *
         * @param { ZStream } strm - For details, see [ZStream<sup>12+</sup>]{@link zlib.ZStream}.
         * @returns { Promise<ReturnStatus> } Promise used to return the result status.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800004 - Compression or decompression stream error, which may be caused by an
         *     initialization error in the zlib stream structure or a modified structure.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        deflateResetKeep(strm: ZStream): Promise<ReturnStatus>;
        /**
         * Returns the number of bytes and bits of output that has been generated but not yet provided in the available
         * output. This API uses a promise to return the result.
         *
         * @param { ZStream } strm - For details, see [ZStream<sup>12+</sup>]{@link zlib.ZStream}.
         * @returns { Promise<DeflatePendingOutputInfo> } Promise used to return the result status, and number of bits and
         *     bytes for output.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800004 - Compression or decompression stream error, which may be caused by an
         *     initialization error in the zlib stream structure or a modified structure.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        deflatePending(strm: ZStream): Promise<DeflatePendingOutputInfo>;
        /**
         * Dynamically updates the compression level and compression strategy. This API uses a promise to return the result.
         *
         * @param { ZStream } strm - For details, see [ZStream<sup>12+</sup>]{@link zlib.ZStream}.
         * @param { CompressLevel } level - For details, see [CompressLevel]{@link zlib.CompressLevel}.
         * @param { CompressStrategy } strategy - For details, see [CompressStrategy]{@link zlib.CompressStrategy}.
         * @returns { Promise<ReturnStatus> } Promise used to return the result status.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800004 - Compression or decompression stream error, which may be caused by an
         *     initialization error in the zlib stream structure or a modified structure.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        deflateParams(strm: ZStream, level: CompressLevel, strategy: CompressStrategy): Promise<ReturnStatus>;
        /**
         * Inserts bits and values into the compression stream. This API uses a promise to return the result.
         *
         * @param { ZStream } strm - For details, see [ZStream<sup>12+</sup>]{@link zlib.ZStream}.
         * @param { number } bits - Number of bits to be inserted. The value ranges from 0 to 16.
         * @param { number } value - Bit value corresponding to the number of bits.
         * @returns { Promise<ReturnStatus> } Promise used to return the result status.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800004 - Compression or decompression stream error, which may be caused by an
         *     initialization error in the zlib stream structure or a modified structure.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        deflatePrime(strm: ZStream, bits: number, value: number): Promise<ReturnStatus>;
    }
    /**
     * Describes gzip-related APIs.
     *
     * @syscap SystemCapability.BundleManager.Zlib
     * @atomicservice
     * @since 12
     */
    interface GZip {
        /**
         * Associates gzip file with the file descriptor (fd) and opens the file for reading and decompressing, or
         * compressing and writing. This API uses a promise to return the result.
         *
         * @param { number } fd - File descriptor. Generally, the value is obtained by calling the **open** method or other
         *     methods.
         * @param { string } mode - Specifies the access mode. For details, see the description of
         *     [gzopen]{@link zlib.GZip.gzopen}.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800002 - No such file or access mode error.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        gzdopen(fd: number, mode: string): Promise<void>;
        /**
         * Sets the internal buffer size for the current library function. This API uses a promise to return the result.
         *
         * @param { number } size - Size of the internal buffer to be set.
         * @returns { Promise<number> } Promise used to return the result. If the operation is successful, **0** is returned.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800009 - Internal structure error.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        gzbuffer(size: number): Promise<number>;
        /**
         * Opens the .gz file in the specified path for reading and decompressing, or compressing and writing. This API uses
         * a promise to return the result.
         *
         * @param { string } path - Path of the file to be opened.
         * @param { string } mode - Specifies a mode for opening a file.<br>Basic modes (one of the following must be
         *     selected):<br>- **"r"** or **"rb"**: read mode. The system automatically detects and decompresses the gzip
         *     file. If the file is not in gzip format, the original data is directly read.<br>- **"w"** or **"wb"**: write
         *     mode. The system creates a new file and compresses data.<br>- **"a"** or **"ab"**: append mode. The system
         *     appends a new gzip stream to the end of the existing file without verifying the format of the original file.<
         *     br>Optional function parameters (can be used together):<br>- Compression level: **0** (no compression) to
         *     **9** (maximum compression). The default compression level is **6**. This parameter must be used together
         *     with the write or append mode.<br>- Compression strategy: **"f"** (filtering strategy), **"h"** (Huffman
         *     coding strategy), **"R"** (RLE compression strategy), or **"F"** (fixed encoding strategy). You can only
         *     select one of the strategies.<br>- Transparent mode: **"T"**. In this mode, data is not compressed and no
         *     gzip header is generated during writing (a common file is generated). This parameter is mutually exclusive
         *     with the compression strategy parameter.<br>- Exclusive creation: **"x"**. The file fails to be opened if it
         *     already exists. This parameter must be used together with the write or append mode.<br>- Close-on-exec flag:
         *     **"e"**. This parameter is used to set the **FD_CLOEXEC** property of the file descriptor (system-dependent).
         *     <br>Examples:<br>- **"r"**: read mode. Data is read in binary format.<br>- **"rb"**: read mode. Data is read
         *     in binary format.<br>- **"wb6"**: write mode. Data is written in binary format with the compression level of
         *     6.<br>- **"wb9f"**: write mode. Data is written in binary format with the maximum compression level and
         *     filtering strategy.<br>- **"wbT"**: write mode. Data is not compressed and a common file is generated.<br>-
         *     **"wbx"**: write mode. Data is written to the exclusively created file in binary format.<br>- **"abx"**:
         *     append mode. Data is appended and written to the exclusively created file in binary format.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800002 - No such file or access mode error.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        gzopen(path: string, mode: string): Promise<void>;
        /**
         * Checks whether the position from which data is read has reached the end of the gzip file. This API uses a promise
         * to return the result.
         *
         * @returns { Promise<number> } Promise used to return the result. If the end-of-file indicator is set while reading,
         *     **1** is returned.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        gzeof(): Promise<number>;
        /**
         * Checks whether the specified gzip file handle directly accesses the original uncompressed data and reallocates
         * the buffer. This API uses a promise to return the result.
         *
         * @returns { Promise<number> } Promise used to return the result. If the original uncompressed data is directly
         *     accessed, **1** is returned.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        gzdirect(): Promise<number>;
        /**
         * Clears all pending output of the file. Closes the file and releases the decompression or compression state if
         * necessary. This API uses a promise to return the result.
         *
         * @returns { Promise<ReturnStatus> } Promise used to return the result.
         * @throws { BusinessError } 17800004 - Compression or decompression stream error, which may be caused by an
         *     initialization error in the zlib stream structure or a modified structure.
         * @throws { BusinessError } 17800006 - Memory allocation failed.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        gzclose(): Promise<ReturnStatus>;
        /**
         * Clears the errors and end-of-file flags of a file. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        gzclearerr(): Promise<void>;
        /**
         * Describes the last error message that reported for the file. This API uses a promise to return the result.
         *
         * @returns { Promise<GzErrorOutputInfo> } Promise used to return the result.
         * @throws { BusinessError } 17800004 - Compression or decompression stream error, which may be caused by an
         *     initialization error in the zlib stream structure or a modified structure.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        gzerror(): Promise<GzErrorOutputInfo>;
        /**
         * Reads and decompresses a byte from a file. This API uses a promise to return the result.
         *
         * @returns { Promise<number> } Promise used to return the result.
         * @throws { BusinessError } 17800009 - Internal structure error.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        gzgetc(): Promise<number>;
        /**
         * Flushes all pending output into a compressed file. This API uses a promise to return the result.
         *
         * @param { CompressFlushMode } flush - Controls the flushing mode. For details, see
         *     [CompressFlushMode]{@link zlib.CompressFlushMode}.
         * @returns { Promise<ReturnStatus> } Promise used to return the result.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800004 - Compression or decompression stream error, which may be caused by an
         *     initialization error in the zlib stream structure or a modified structure.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        gzflush(flush: CompressFlushMode): Promise<ReturnStatus>;
        /**
         * Compresses data blocks that are declared with size and nitems from the buffer and writes the data blocks to a
         * file. This API uses a promise to return the result.
         *
         * @param { ArrayBuffer } buf - Buffer to which data is to be written.
         * @param { number } size - Number of bytes in a single data block.
         * @param { number } nitems - Number of data blocks to be written.
         * @returns { Promise<number> } Promise used to return the result.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800009 - Internal structure error.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        gzfwrite(buf: ArrayBuffer, size: number, nitems: number): Promise<number>;
        /**
         * Decompresses and reads data from a gzip file. This API uses a promise to return the result.
         *
         * @param { ArrayBuffer } buf - Destination buffer for storing read results.
         * @param { number } size - Number of bytes in a single data block.
         * @param { number } nitems - Number of data blocks to be written.
         * @returns { Promise<number> } Promise used to return the result.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800009 - Internal structure error.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        gzfread(buf: ArrayBuffer, size: number, nitems: number): Promise<number>;
        /**
         * Implements the same functions as that of **gzclose()** for writing or appending. This API uses a promise to
         * return the result.
         *
         * @returns { Promise<ReturnStatus> } Promise used to return the result.
         * @throws { BusinessError } 17800004 - Compression or decompression stream error, which may be caused by an
         *     initialization error in the zlib stream structure or a modified structure.
         * @throws { BusinessError } 17800006 - Memory allocation failed.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        gzclosew(): Promise<ReturnStatus>;
        /**
         * Implements the same functions as that of **gzclose()** for reading only. This API uses a promise to return the
         * result.
         *
         * @returns { Promise<ReturnStatus> } Promise used to return the result.
         * @throws { BusinessError } 17800004 - Compression or decompression stream error, which may be caused by an
         *     initialization error in the zlib stream structure or a modified structure.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        gzcloser(): Promise<ReturnStatus>;
        /**
         * Compresses the uncompressed bytes of the declared length in the buffer and writes them to the file. This API uses
         * a promise to return the result.
         *
         * @param { ArrayBuffer } buf - Data buffer pointed by an object to be written.
         * @param { number } len - Length of uncompressed bytes.
         * @returns { Promise<number> } Promise used to return the result.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800009 - Internal structure error.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        gzwrite(buf: ArrayBuffer, len: number): Promise<number>;
        /**
         * Pushes **c** back into the input stream so that it will be read as the first character the next time the file is
         * read. This API uses a promise to return the result.
         *
         * @param { number } c - Characters before being pushed into the input stream.
         * @returns { Promise<number> } Promise used to return the result.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800009 - Internal structure error.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        gzungetc(c: number): Promise<number>;
        /**
         * Returns the start position of the next **gzread** or **gzwrite** in the file. This API uses a promise to return
         * the result.
         *
         * @returns { Promise<number> } Promise used to return the result.
         * @throws { BusinessError } 17800009 - Internal structure error.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        gztell(): Promise<number>;
        /**
         * Dynamically updates the compression level and compression strategy of a file. This API uses a promise to return
         * the result.
         *
         * @param { CompressLevel } level - Compression level. For details, see [CompressLevel]{@link zlib.CompressLevel}.
         * @param { CompressStrategy } strategy - Compression strategy. For details, see
         *     [CompressStrategy]{@link zlib.CompressStrategy}.
         * @returns { Promise<ReturnStatus> } Promise used to return the result.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800004 - Compression or decompression stream error, which may be caused by an
         *     initialization error in the zlib stream structure or a modified structure.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        gzsetparams(level: CompressLevel, strategy: CompressStrategy): Promise<ReturnStatus>;
        /**
         * Sets the start position to the offset position relative to the next **gzread** or **gzwrite** in the file.
         *
         * @param { number } offset - Target offset position.
         * @param { OffsetReferencePoint } whence - Defines the reference point for the offset. For details, see
         *     [OffsetReferencePoint]{@link zlib.OffsetReferencePoint}.
         * @returns { Promise<number> } Promise used to return the result.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800009 - Internal structure error.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        gzseek(offset: number, whence: OffsetReferencePoint): Promise<number>;
        /**
         * Repositions the file pointer to the beginning of the file. This feature is applied only for reading. This API
         * uses a promise to return the result.
         *
         * @returns { Promise<ReturnStatus> } Promise used to return the result.
         * @throws { BusinessError } 17800009 - Internal structure error.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        gzrewind(): Promise<ReturnStatus>;
        /**
         * Reads a maximum of **len** uncompressed bytes from a file and decompresses them into the buffer. This API uses a
         * promise to return the result.
         *
         * @param { ArrayBuffer } buf - Target offset position.
         * @returns { Promise<number> } Promise used to return the result.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800009 - Internal structure error.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        gzread(buf: ArrayBuffer): Promise<number>;
        /**
         * Compresses the given null-terminated strings and writes them to the file, excluding the null operator. This API
         * uses a promise to return the result.
         *
         * @param { string } str - Format descriptors and plain text.
         * @returns { Promise<number> } Promise used to return the result.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800009 - Internal structure error.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        gzputs(str: string): Promise<number>;
        /**
         * Compresses **char** converted to an unsigned character and writes it to a file. This API uses a promise to return
         * the result.
         *
         * @param { number } ch - Write character ASCII.
         * @returns { Promise<number> } Promise used to return the result.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800009 - Internal structure error.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        gzputc(ch: number): Promise<number>;
        /**
         * Converts and formats the parameters under the control of the string format and then compresses and writes them
         * into a file, as shown in the **fprintf()**. This API uses a promise to return the result.
         *
         * @param { string } format - Format descriptors and plain text.
         * @param { Array<string | number> } args - List of variable parameters. If variable parameters are passed, for
         *     example, **gzprintf("name is %s, age is %d", "Tom", 23)**, the content **"name is Tom, age is 23"** is
         *     written. If no variable parameter is passed, for example, **gzprintf("name is %s, age is %d")**, the content
         *     **"name is %s, age is %d"** is written.
         * @returns { Promise<number> } Return the number of uncompressed bytes actually written.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800004 - Compression or decompression stream error, which may be caused by an
         *     initialization error in the zlib stream structure or a modified structure.
         * @throws { BusinessError } 17800009 - Internal structure error.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        gzprintf(format: string, ...args: Array<string | number>): Promise<number>;
        /**
         * Returns the current compressed read or write offset of the file. This API uses a promise to return the result.
         *
         * @returns { Promise<number> } Promise used to return the result.
         * @throws { BusinessError } 17800009 - Internal structure error.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        gzoffset(): Promise<number>;
        /**
         * Reads bytes from a compressed file until len-1 characters are read, a newline character is read and transferred
         * to a buffer, or an end-of-file condition is encountered. This API uses a promise to return the result.
         *
         * @param { ArrayBuffer } buf - Stores the read row data.
         * @returns { Promise<string> } Promise used to return a string ended with **null**.
         * @throws { BusinessError } 401 - The parameter check failed. Possible causes: 1. Mandatory parameters are left
         *     unspecified;
         *     2. Incorrect parameter types; 3. Parameter verification failed.
         * @throws { BusinessError } 17800009 - Internal structure error.
         * @syscap SystemCapability.BundleManager.Zlib
         * @atomicservice
         * @since 12
         */
        gzgets(buf: ArrayBuffer): Promise<string>;
    }
}
export default zlib;

```
