# @ohos.request.cacheDownload.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2024 Huawei Device Co., Ltd.
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
 * @file Download and Cache
 * @kit BasicServicesKit
 */
import { Callback } from './@ohos.base';
/**
 * The **request** module provides applications with the basic capabilities of file upload and download and background
 * transfer proxy.
 *
 * - The child component **cacheDownload** provides the basic capability of caching application resources in advance.
 * - **cacheDownload** uses the HTTP to download data and caches data resources to the application memory or specified
 * files in the application sandbox directory.
 * - The cached data can be used by specific ArkUI components (such as **Image**) to improve resource loading
 * efficiency. Check whether the ArkUI components support this function by referring to the ArkUI component topics.
 *
 * @syscap SystemCapability.Request.FileTransferAgent
 * @since 18
 */
declare namespace cacheDownload {
    /**
     * Enumerates secure communication protocols.
     *
     * @syscap SystemCapability.Request.FileTransferAgent
     * @since 21
     */
    enum SslType {
        /**
         * TLS.
         *
         * @syscap SystemCapability.Request.FileTransferAgent
         * @since 21
         */
        TLS = 'TLS',
        /**
         * TLCP.
         *
         * @syscap SystemCapability.Request.FileTransferAgent
         * @since 21
         */
        TLCP = 'TLCP'
    }
    /**
     * Enumerates cache update strategies.
     *
     * @syscap SystemCapability.Request.FileTransferAgent
     * @since 23
     */
    enum CacheStrategy {
        /**
         * Forcibly updates the cache, regardless of whether the cache already exists.
         *
         * @syscap SystemCapability.Request.FileTransferAgent
         * @since 23
         */
        FORCE = 0,
        /**
         * Updates the cache only when the cache does not exist.
         *
         * @syscap SystemCapability.Request.FileTransferAgent
         * @since 23
         */
        LAZY = 1
    }
    /**
     * Enumerates the specific types of returned error code.
     *
     * @syscap SystemCapability.Request.FileTransferAgent
     * @since 23
     */
    enum ErrorCode {
        /**
         * Other types of errors that are not classified.
         *
         * @syscap SystemCapability.Request.FileTransferAgent
         * @since 23
         */
        OTHERS = 0xFF,
        /**
         * DNS-related errors.
         *
         * @syscap SystemCapability.Request.FileTransferAgent
         * @since 23
         */
        DNS = 0x00,
        /**
         * TCP-related errors.
         *
         * @syscap SystemCapability.Request.FileTransferAgent
         * @since 23
         */
        TCP = 0x10,
        /**
         * SSL-related errors.
         *
         * @syscap SystemCapability.Request.FileTransferAgent
         * @since 23
         */
        SSL = 0x20,
        /**
         * HTTP-related errors.
         *
         * @syscap SystemCapability.Request.FileTransferAgent
         * @since 23
         */
        HTTP = 0x30
    }
    /**
     * Task timeout configuration.
     *
     * @syscap SystemCapability.Request.FileTransferAgent
     * @stagemodelonly
     * @since 26.0.0
     */
    interface TimeoutOptions {
        /**
         * Network availability check timeout, in seconds.
         * The default value is 20.
         * The minimum value is 0.
         * The maximum value is 20.
         * When set to 0, no check will be performed.
         * The value should be an integer.
         *
         * @syscap SystemCapability.Request.FileTransferAgent
         * @stagemodelonly
         * @since 26.0.0
         */
        networkCheckTimeout?: number;
        /**
         * Complete HTTP request-response cycle timeout, in seconds.
         * The default value is 60.
         * The minimum value is 1.
         * The value should be an integer.
         *
         * @syscap SystemCapability.Request.FileTransferAgent
         * @stagemodelonly
         * @since 26.0.0
         */
        httpTotalTimeout?: number;
    }
    /**
     * Task retry configuration.
     *
     * @syscap SystemCapability.Request.FileTransferAgent
     * @stagemodelonly
     * @since 26.0.0
     */
    interface RetryOptions {
        /**
         * Maximum number of retry attempts.
         * The default value is 1.
         * The minimum value is 0.
         * The maximum value is 10.
         * When set to 0, no retries will be performed.
         *
         * @syscap SystemCapability.Request.FileTransferAgent
         * @stagemodelonly
         * @since 26.0.0
         */
        maxRetryCount?: number;
    }
    /**
     * Provides configuration options for download and cache, including HTTP options, transmission options, and task
     * options.
     *
     * @syscap SystemCapability.Request.FileTransferAgent
     * @since 18
     */
    interface CacheDownloadOptions {
        /**
         * Request header used by a download task during HTTP transfer. The default value is empty.
         *
         * @syscap SystemCapability.Request.FileTransferAgent
         * @since 18
         */
        headers?: Record<string, string>;
        /**
         * Secure communication protocol, such as TSL or TLCP. TLS is used by default. Currently, TLS and TLCP do not
         * support two-way authentication.
         *
         * @syscap SystemCapability.Request.FileTransferAgent
         * @since 21
         */
        sslType?: SslType;
        /**
         * CA certificate path. Currently, only the .pem certificate is supported. The CA certificate preset by the
         * system is used by default.
         *
         * @syscap SystemCapability.Request.FileTransferAgent
         * @since 21
         */
        caPath?: string;
        /**
         * Cache update strategies, including **FORCE** or **LAZY**. The **FORCE** policy is used by default.
         *
         * @syscap SystemCapability.Request.FileTransferAgent
         * @since 23
         */
        cacheStrategy?: CacheStrategy;
        /**
         * Task retry configuration.
         *
         * @syscap SystemCapability.Request.FileTransferAgent
         * @stagemodelonly
         * @since 26.0.0
         */
        retry?: RetryOptions;
        /**
         * Task timeout configuration.
         *
         * @syscap SystemCapability.Request.FileTransferAgent
         * @stagemodelonly
         * @since 26.0.0
         */
        timeout?: TimeoutOptions;
    }
    /**
     * Describes the pre-downloaded resource information.
     *
     * @syscap SystemCapability.Request.FileTransferAgent
     * @since 20
     */
    interface ResourceInfo {
        /**
         * Size of a pre-downloaded resource after decompression, in bytes. If the value is a positive integer, the
         * resource is successfully downloaded; if the value is **-1**, the resource fails to be downloaded.
         *
         * @syscap SystemCapability.Request.FileTransferAgent
         * @since 20
         */
        readonly size: number;
    }
    /**
     * Describes the pre-downloaded network information.
     *
     * @syscap SystemCapability.Request.FileTransferAgent
     * @since 20
     */
    interface NetworkInfo {
        /**
         * DNS servers used for downloading resources.
         *
         * @syscap SystemCapability.Request.FileTransferAgent
         * @since 20
         */
        readonly dnsServers: string[];
        /**
         * IP address of the URL used for downloading resources. When the DNS resolution fails, the IP address is
         * undefined.
         *
         * @syscap SystemCapability.Request.FileTransferAgent
         * @since 23
         */
        readonly ip?: string;
    }
    /**
     * Describes the pre-downloaded performance information.
     *
     * @syscap SystemCapability.Request.FileTransferAgent
     * @since 20
     */
    interface PerformanceInfo {
        /**
         * Time taken from DNS startup to resolution completion, in milliseconds.
         *
         * @syscap SystemCapability.Request.FileTransferAgent
         * @since 20
         */
        readonly dnsTime: number;
        /**
         * Time taken from TCP startup to connection completion, in milliseconds.
         *
         * @syscap SystemCapability.Request.FileTransferAgent
         * @since 20
         */
        readonly connectTime: number;
        /**
         * Time taken from TLS startup to connection completion, in milliseconds.
         *
         * @syscap SystemCapability.Request.FileTransferAgent
         * @since 20
         */
        readonly tlsTime: number;
        /**
         * Time taken from startup to sending the first byte, in milliseconds.
         *
         * @syscap SystemCapability.Request.FileTransferAgent
         * @since 20
         */
        readonly firstSendTime: number;
        /**
         * Time taken from startup to receiving the first byte, in milliseconds.
         *
         * @syscap SystemCapability.Request.FileTransferAgent
         * @since 20
         */
        readonly firstReceiveTime: number;
        /**
         * Time taken from startup to request completion, in milliseconds.
         *
         * @syscap SystemCapability.Request.FileTransferAgent
         * @since 20
         */
        readonly totalTime: number;
        /**
         * Time taken from startup to redirection completion, in milliseconds.
         *
         * @syscap SystemCapability.Request.FileTransferAgent
         * @since 20
         */
        readonly redirectTime: number;
    }
    /**
     * Describes the pre-downloaded download information.
     *
     * @syscap SystemCapability.Request.FileTransferAgent
     * @since 20
     */
    interface DownloadInfo {
        /**
         * Pre-downloaded resource information.
         *
         * @syscap SystemCapability.Request.FileTransferAgent
         * @since 20
         */
        readonly resource: ResourceInfo;
        /**
         * Pre-downloaded network information.
         *
         * @syscap SystemCapability.Request.FileTransferAgent
         * @since 20
         */
        readonly network: NetworkInfo;
        /**
         * Pre-downloaded performance information.
         *
         * @syscap SystemCapability.Request.FileTransferAgent
         * @since 20
         */
        readonly performance: PerformanceInfo;
    }
    /**
     * Describes the error message returned when a pre-download error occurs.
     *
     * @syscap SystemCapability.Request.FileTransferAgent
     * @since 23
     */
    interface DownloadError {
        /**
         * Specific error type returned by the pre-download error callback.
         *
         * @syscap SystemCapability.Request.FileTransferAgent
         * @since 23
         */
        readonly errorCode: ErrorCode;
        /**
         * Error message. A [universal error code](docroot://reference/errorcode-universal.md) or
         * [HTTP error code](docroot://reference/apis-network-kit/errorcode-net-http.md) is returned.
         *
         * @syscap SystemCapability.Request.FileTransferAgent
         * @since 23
         */
        readonly message: string;
    }
    /**
     * Downloads a task from a specified URL. If the transfer is successful, the data is downloaded to the memory cache
     * and file cache.
     *
     * - After automatically decompressing during HTTP transmission, the size of the target resource cannot exceed 20971
     * 520 bytes (20 MB). Otherwise, the resource fails to store in the memory cache or file cache.
     * - When caching the downloaded data, if the data already exists in the destination URL, the new data will
     * overwrite the old one.
     * - In addition, the system determines whether to store the target resource in a specified location based on each
     * cache type's size limit in **cacheDownload**. By default, the LRU mode is used to replace the existing cached
     * data.
     * - This API returns the result synchronously, without blocking the calling thread.
     *
     * @permission ohos.permission.INTERNET
     * @param { string } url - URL of the target resource. HTTP and HTTPS are supported. The URL length cannot exceed 81
     *     92 bytes.
     * @param { CacheDownloadOptions } options - Cache download options for the target resource.
     * @throws { BusinessError } 201 - permission denied.
     * @throws { BusinessError } 401 - parameter error. Possible causes:
     *     <br> 1. Missing mandatory parameters.
     *     <br> 2. Incorrect parameter type.
     *     <br> 3. Parameter verification failed.
     * @syscap SystemCapability.Request.FileTransferAgent
     * @since 18
     */
    function download(url: string, options: CacheDownloadOptions): void;
    /**
     * Cancels an ongoing download task based on the URL. The saved memory cache and file cache are not affected.
     *
     * - If there is no download task with the specified URL, this API does not take effect.
     * - When this API is used for synchronous execution, the calling thread is not blocked.
     *
     * @param { string } url - URL of the target resource. HTTP and HTTPS are supported. The URL length cannot exceed 81
     *     92 bytes.
     * @throws { BusinessError } 401 - parameter error. Possible causes:
     *     <br> 1. Missing mandatory parameters.
     *     <br> 2. Incorrect parameter type.
     *     <br> 3. Parameter verification failed.
     * @syscap SystemCapability.Request.FileTransferAgent
     * @since 18
     */
    function cancel(url: string): void;
    /**
     * Sets the upper limit of the memory cache size for the **cacheDownload** component.
     *
     * - When this API is used to adjust the cache size, the LRU mode is used by default to clear redundant cached data
     * in the memory.
     * - This API returns the result synchronously, without blocking the calling thread.
     *
     * @param { number } bytes - Upper limit of the cache, in bytes. The default value is **0**, and the maximum value
     *     cannot exceed **1073741824** (1 GB).
     * @throws { BusinessError } 401 - parameter error. Possible causes:
     *     <br> 1. Missing mandatory parameters.
     *     <br> 2. Incorrect parameter type.
     *     <br> 3. Parameter verification failed.
     * @syscap SystemCapability.Request.FileTransferAgent
     * @since 18
     */
    function setMemoryCacheSize(bytes: number): void;
    /**
     * Sets the upper limit of the file cache size for the **cacheDownload** component.
     *
     * - When this API is used to adjust the cache size, the LRU mode is used by default to clear redundant cached data
     * in the file.
     * - If **bytes** is set to **0**, all cached files will be deleted.
     * - This API returns the result synchronously, without blocking the calling thread.
     *
     * @param { number } bytes - Upper limit of the cache, in bytes. The default value is **104857600** (100 MB), and the
     *     maximum value is **4294967296** (4 GB).
     * @throws { BusinessError } 401 - parameter error. Possible causes:
     *     <br> 1. Missing mandatory parameters.
     *     <br> 2. Incorrect parameter type.
     *     <br> 3. Parameter verification failed.
     * @syscap SystemCapability.Request.FileTransferAgent
     * @since 18
     */
    function setFileCacheSize(bytes: number): void;
    /**
     * Obtains the download information based on the URL. The download information is stored in the download information
     * list in memory and is cleared when the application exits.
     *
     * - If the specified URL is found in the download information list, the latest
     * [DownloadInfo]{@link cacheDownload.DownloadInfo} corresponding to the URL is returned.
     * - If the specified URL cannot be found in the download information list, **undefined** is returned.
     * - If the download information has already cached in the URL, the new cached information will overwrite the old
     * one.
     * - When the target information is stored in the memory, the existing cache data is replaced in the LRU mode.
     *
     * @permission ohos.permission.GET_NETWORK_INFO
     * @param { string } url - URL to be queried, with a maximum length of 8192 bytes.
     * @returns { DownloadInfo | undefined } Returns the download information of the corresponding URL if the operation
     *     is successful; returns **undefined** if the specified URL does not exist.
     * @throws { BusinessError } 201 - permission denied.
     * @syscap SystemCapability.Request.FileTransferAgent
     * @since 20
     */
    function getDownloadInfo(url: string): DownloadInfo | undefined;
    /**
     * Sets the size of the download information list.
     *
     * - The download information list is used to store pre-downloaded information.
     * - Each pre-download generates a piece of download information with a unique URL. Only the latest download
     * information is saved for the same URL.
     * - If the list size is increased using this API, the original information in the list remains unchanged; if the
     * list size is decreased, the LRU mode is used by default to clear excess cached data in the list.
     *
     * @param { number } size - Size of the download information list. The value ranges from 0 to 8192. The default value
     *     is **0**, indicating that no download information is stored.
     * @syscap SystemCapability.Request.FileTransferAgent
     * @since 20
     */
    function setDownloadInfoListSize(size: number): void;
    /**
     * Clears this memory cache.
     *
     * @syscap SystemCapability.Request.FileTransferAgent
     * @since 23
     */
    function clearMemoryCache(): void;
    /**
     * Clears this file cache.
     *
     * @syscap SystemCapability.Request.FileTransferAgent
     * @since 23
     */
    function clearFileCache(): void;
    /**
     * Subscribes to the pre-download completion events. This API uses an asynchronous callback to return the result.
     *
     * @param { string } url - Callback URL to be registered, with a maximum of 8,192 bytes.
     * @param { Callback<void> } callback - Callback used to return the result.
     * @syscap SystemCapability.Request.FileTransferAgent
     * @since 23
     */
    function onDownloadSuccess(url: string, callback: Callback<void>): void;
    /**
     * Subscribes to the pre-download error events. This API uses an asynchronous callback to return the result.
     *
     * @param { string } url - URL to be registered, with a maximum of 8192 bytes.
     * @param { Callback<DownloadError> } callback - Callback used to return the error information about the pre-
     *     download.
     * @syscap SystemCapability.Request.FileTransferAgent
     * @since 23
     */
    function onDownloadError(url: string, callback: Callback<DownloadError>): void;
    /**
     * Unsubscribes from the pre-download completion events. This API uses an asynchronous callback to return the
     * result.
     *
     * @param { string } url - Callback URL to be registered, with a maximum of 8,192 bytes.
     * @param { Callback<void> } [callback] - Callback to unregister. If this parameter is left blank, all completion
     *     callback functions of the URL are unregistered.
     * @syscap SystemCapability.Request.FileTransferAgent
     * @since 23
     */
    function offDownloadSuccess(url: string, callback?: Callback<void>): void;
    /**
     * Unsubscribes from the pre-download error events. This API uses an asynchronous callback to return the result.
     *
     * @param { string } url - URL to be unregistered, with a maximum of 8192 bytes.
     * @param { Callback<DownloadError> } [callback] - Callback used to return the error information about the pre-
     *     download. If this parameter is left blank, all error callback functions of the URL are unregistered.
     * @syscap SystemCapability.Request.FileTransferAgent
     * @since 23
     */
    function offDownloadError(url: string, callback?: Callback<DownloadError>): void;
    /**
     * Sets retry options for all tasks.
     * Used when task-specific retry configuration is not configured.
     *
     * @param { RetryOptions } [options] - Task retry configurations.
     *     <br>Default value: Refer to the default value of RetryOptions.
     * @syscap SystemCapability.Request.FileTransferAgent
     * @stagemodelonly
     * @since 26.0.0
     */
    function setGlobalRetryOptions(options?: RetryOptions): void;
    /**
     * Sets timeout configuration for all tasks.
     * Used when task-specific timeout configuration is not configured.
     *
     * @param { TimeoutOptions } [options] - Task timeout configuration.
     *     <br>Default value: Refer to the default value of TimeoutOptions.
     * @syscap SystemCapability.Request.FileTransferAgent
     * @stagemodelonly
     * @since 26.0.0
     */
    function setGlobalTimeoutOptions(options?: TimeoutOptions): void;
}
export default cacheDownload;

```
