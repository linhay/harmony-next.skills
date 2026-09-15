# @ohos.file.cloudSync.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2023 Huawei Device Co., Ltd.
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
 * @kit CoreFileKit
 */
import type { AsyncCallback, Callback } from './@ohos.base';
/**
 * The **cloudSync** module provides the device-cloud sync capabilities for applications. You can use the APIs to start
 * or stop device-cloud sync and start or stop the download of images.
 *
 * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
 * @since 11
 */
declare namespace cloudSync {
    /**
     * Enumerates the device-cloud sync states.
     *
     * > **NOTE**
     * >
     * > If a sync progress event listener is registered for an application, a callback will be invoked to notify the
     * > application when the device-cloud sync state is changed.
     *
     * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
     * @since 12
     */
    enum SyncState {
        /**
         * The file is being uploaded.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 12
         */
        UPLOADING = 0,
        /**
         * Upload failed.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 12
         */
        UPLOAD_FAILED = 1,
        /**
         * The file is being downloaded.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 12
         */
        DOWNLOADING = 2,
        /**
         * Download failed.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 12
         */
        DOWNLOAD_FAILED = 3,
        /**
         * Sync completed.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 12
         */
        COMPLETED = 4,
        /**
         * Sync stopped.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 12
         */
        STOPPED = 5
    }
    /**
     * Enumerates the device-cloud sync errors.
     *
     * - In the current phase, **NETWORK_UNAVAILABLE** is returned only when the mobile data network and Wi-Fi are
     * unavailable. If the mobile data network is available, the synchronization can be performed normally.
     * - During the sync process, if the battery level is lower than 10% in non-charging scenarios, **BATTERY_LEVEL_LOW**
     * will be return when the current upload is complete.
     * - When sync is being triggered, if the battery level is lower than 10% in non-charging scenarios, sync is not
     * allowed.
     * - If the cloud space is insufficient when a file is uploaded, the upload will fail and there is no such a file in
     * the cloud.
     *
     * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
     * @since 12
     */
    enum ErrorType {
        /**
         * No error.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 12
         */
        NO_ERROR = 0,
        /**
         * No network is available.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 12
         */
        NETWORK_UNAVAILABLE = 1,
        /**
         * Wi-Fi is unavailable.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 12
         */
        WIFI_UNAVAILABLE = 2,
        /**
         * The battery level is lower than 10%.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 12
         */
        BATTERY_LEVEL_LOW = 3,
        /**
         * The battery level is lower than 15%.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 12
         */
        BATTERY_LEVEL_WARNING = 4,
        /**
         * The cloud space is insufficient.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 12
         */
        CLOUD_STORAGE_FULL = 5,
        /**
         * The local space is insufficient.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 12
         */
        LOCAL_STORAGE_FULL = 6,
        /**
         * The device temperature is too high.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 12
         */
        DEVICE_TEMPERATURE_TOO_HIGH = 7,
        /**
         * The remote service is unavailable.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 20
         */
        REMOTE_SERVER_ABNORMAL = 8
    }
    /**
     * Represents information about the device-cloud sync progress.
     *
     * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
     * @since 12
     */
    interface SyncProgress {
        /**
         * Device-cloud sync state.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 12
         */
        state: SyncState;
        /**
         * Sync error.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 12
         */
        error: ErrorType;
    }
    /**
     * Enumerates the download states of a cloud file.
     *
     * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
     * @since 11
     */
    enum State {
        /**
         * The cloud file is being downloaded.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 11
         */
        RUNNING = 0,
        /**
         * The cloud file download is complete.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 11
         */
        COMPLETED = 1,
        /**
         * The cloud file download failed.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 11
         */
        FAILED = 2,
        /**
         * The cloud file download is stopped.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 11
         */
        STOPPED = 3
    }
    /**
     * Enumerates the device-cloud download error types.
     *
     * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
     * @since 11
     */
    enum DownloadErrorType {
        /**
         * No error.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 11
         */
        NO_ERROR = 0,
        /**
         * Unknown error.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 11
         */
        UNKNOWN_ERROR = 1,
        /**
         * The network is unavailable.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 11
         */
        NETWORK_UNAVAILABLE = 2,
        /**
         * The local space is insufficient.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 11
         */
        LOCAL_STORAGE_FULL = 3,
        /**
         * The file is not found in the cloud space.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 11
         */
        CONTENT_NOT_FOUND = 4,
        /**
         * The user requests are too frequent to respond.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 11
         */
        FREQUENT_USER_REQUESTS = 5
    }
    /**
     * Represents information about the download progress of a cloud file.
     *
     * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
     * @since 11
     */
    interface DownloadProgress {
        /**
         * File download state.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 11
         */
        state: State;
        /**
         * Size of the downloaded data, in bytes. The value range is [0, 9223372036854775807].
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 11
         */
        processed: number;
        /**
         * Size of the cloud file, in bytes. The value range is [0, 9223372036854775807].
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 11
         */
        size: number;
        /**
         * URI of the cloud file.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 11
         */
        uri: string;
        /**
         * Download error type.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 11
         */
        error: DownloadErrorType;
    }
    /**
     * Enumerates the download file types from the Drive Kit.
     *
     * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
     * @since 20
     */
    enum DownloadFileType {
        /**
         * Content file.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 20
         */
        CONTENT = 0,
        /**
         * Thumbnail file.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 20
         */
        THUMBNAIL = 1,
        /**
         * LCD file.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 20
         */
        LCD = 2
    }
    /**
     * Represents a list of files that fail to be downloaded from the Drive Kit and failure causes.
     *
     * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
     * @since 20
     */
    interface FailedFileInfo {
        /**
         * URI of the file that fails to be downloaded.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 20
         */
        uri: string;
        /**
         * Error type of the file download failure.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 20
         */
        error: DownloadErrorType;
    }
    /**
     * Represents the batch download progress of a file from the Drive Kit.
     *
     * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
     * @since 20
     */
    class MultiDownloadProgress {
        /**
         * Execution state of the batch download.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 20
         */
        state: State;
        /**
         * ID of a batch download task. The value ranges from 0 to INT64_MAX. If the progress is abnormal, the value **-1**
         * is returned.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 20
         */
        taskId: number;
        /**
         * Number of successfully downloaded files. The value ranges from 0 to 400. If the progress is abnormal, the value
         * **-1** is returned.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 20
         */
        successfulCount: number;
        /**
         * Number of files that fail to be downloaded. The value ranges from 0 to 400. If the progress is abnormal, the
         * value **-1** is returned.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 20
         */
        failedCount: number;
        /**
         * Total number of files. The value ranges from 0 to 400. If the progress is abnormal, the value **-1** is returned.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 20
         */
        totalCount: number;
        /**
         * Size of the downloaded file, in bytes. The value range is
         * [0, INT64_MAX). If the progress is abnormal, the value **INT64_MAX** is returned.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 20
         */
        downloadedSize: number;
        /**
         * Total size of the files to be downloaded, in bytes. The value range is
         * [0, INT64_MAX). If the progress is abnormal, the value **INT64_MAX** is returned.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 20
         */
        totalSize: number;
        /**
         * Type of the error returned when the batch download fails.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 20
         */
        errType: DownloadErrorType;
        /**
         * Obtains the list of files that fail to be downloaded in batches.
         *
         * @returns { Array<FailedFileInfo> } List of file URIs that fail to be downloaded and the corresponding error
         *     types.
         * @throws { BusinessError } 22400005 - Inner error. Possible causes:
         *     <br>1.Failed to access the database or execute the SQL statement.
         *     <br>2.System error, such as a null pointer, insufficient memory or a JS engine exception.
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 20
         */
        getFailedFiles(): Array<FailedFileInfo>;
        /**
         * Obtains the list of files that are successfully downloaded in batches.
         *
         * @returns { Array<string> } List of URIs of the files that are successfully downloaded. The value is an array.
         * @throws { BusinessError } 22400005 - Inner error. Possible causes:
         *     <br>1.Failed to access the database or execute the SQL statement.
         *     <br>2.System error, such as a null pointer, insufficient memory or a JS engine exception.
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 20
         */
        getSuccessfulFiles(): Array<string>;
    }
    /**
     * Provides APIs for the file manager application to perform device-cloud sync of the files stored in the Drive Kit.
     * Before using the APIs of this class, you need to create a **FileSync** instance.
     *
     * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
     * @since 12
     */
    class FileSync {
        /**
         * A constructor used to create a **FileSync** instance.
         *
         * @throws { BusinessError } 401 - The input parameter is invalid.Possible causes:Incorrect parameter types.
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 12
         */
        constructor();
        /**
         * Registers a listener for the device-cloud sync progress.
         *
         * @param { 'progress' } event - Event type. The value is **progress**, which indicates the sync progress event.
         * @param { Callback<SyncProgress> } callback - Callback used to return the sync progress.
         * @throws { BusinessError } 401 - The input parameter is invalid.Possible causes:1.Mandatory parameters are left
         *     unspecified;
         *     <br>2.Incorrect parameter types.
         * @throws { BusinessError } 13600001 - IPC error
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 12
         */
        on(event: 'progress', callback: Callback<SyncProgress>): void;
        /**
         * Removes the specified callback from the device-cloud sync progress.
         *
         * @param { 'progress' } event - Event type. The value is **progress**, which indicates the sync progress event.
         * @param { Callback<SyncProgress> } [callback] - Callback used to return the sync progress. The default value is
         *     null.
         * @throws { BusinessError } 401 - The input parameter is invalid.Possible causes:1.Mandatory parameters are left
         *     unspecified;2.Incorrect parameter types.
         * @throws { BusinessError } 13600001 - IPC error
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 12
         */
        off(event: 'progress', callback?: Callback<SyncProgress>): void;
        /**
         * Starts device-cloud sync of a file. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - The input parameter is invalid.Possible causes:Incorrect parameter types.
         * @throws { BusinessError } 13600001 - IPC error.
         * @throws { BusinessError } 22400001 - Cloud status not ready.
         * @throws { BusinessError } 22400002 - Network unavailable.
         * @throws { BusinessError } 22400003 - Low battery level.
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 12
         */
        start(): Promise<void>;
        /**
         * Starts device-cloud sync of a file. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to start device-cloud sync.
         * @throws { BusinessError } 401 - The input parameter is invalid.Possible causes:1.Mandatory parameters are left
         *     unspecified;2.Incorrect parameter types.
         * @throws { BusinessError } 13600001 - IPC error.
         * @throws { BusinessError } 22400001 - Cloud status not ready.
         * @throws { BusinessError } 22400002 - Network unavailable.
         * @throws { BusinessError } 22400003 - Low battery level.
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 12
         */
        start(callback: AsyncCallback<void>): void;
        /**
         * Stops device-cloud sync of a file. This API uses a promise to return the result.
         *
         * Calling **stop** will stop the sync process. To resume the sync, call [start]{@link cloudSync.FileSync#start()}.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - The input parameter is invalid.Possible causes:Incorrect parameter types.
         * @throws { BusinessError } 13600001 - IPC error.
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 12
         */
        stop(): Promise<void>;
        /**
         * Stops device-cloud sync of a file. This API uses an asynchronous callback to return the result.
         *
         * Calling **stop** will stop the sync process. To resume the sync, call [start]{@link cloudSync.FileSync#start()}.
         *
         * @param { AsyncCallback<void> } callback - Callback used to stop device-cloud sync.
         * @throws { BusinessError } 401 - The input parameter is invalid.Possible causes:1.Mandatory parameters are left
         *     unspecified;
         *     <br>2.Incorrect parameter types.
         * @throws { BusinessError } 13600001 - IPC error.
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 12
         */
        stop(callback: AsyncCallback<void>): void;
        /**
         * Obtains the last sync time. This API uses a promise to return the result.
         *
         * @returns { Promise<number> } Promise used to return the last sync time.
         * @throws { BusinessError } 401 - The input parameter is invalid.Possible causes:Incorrect parameter types.
         * @throws { BusinessError } 13600001 - IPC error.
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 12
         */
        getLastSyncTime(): Promise<number>;
        /**
         * Obtains the last sync time. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<number> } callback - Callback used to obtain the last sync time.
         * @throws { BusinessError } 401 - The input parameter is invalid.Possible causes:1.Mandatory parameters are left
         *     unspecified;
         *     <br>2.Incorrect parameter types.
         * @throws { BusinessError } 13600001 - IPC error.
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 12
         */
        getLastSyncTime(callback: AsyncCallback<number>): void;
    }
    /**
     * Provides APIs for the file manager application to download files from the Drive Kit to a local device.
     *
     * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
     * @since 11
     */
    class CloudFileCache {
        /**
         * A constructor used to create a **CloudFileCache** instance. Data is not shared between multiple instances.
         *
         * @throws { BusinessError } 401 - The input parameter is invalid.Possible causes:Incorrect parameter types.
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 11
         */
        constructor();
        /**
         * Registers a listener for the download progress of a file from the Drive Kit.
         *
         * @param { 'progress' } event - Event. The value is **progress**, which indicates the download progress event of a
         *     cloud file.
         * @param { Callback<DownloadProgress> } callback - Callback used to return the file download progress.
         * @throws { BusinessError } 401 - The input parameter is invalid.Possible causes:1.Mandatory parameters are left
         *     unspecified;
         *     <br>2.Incorrect parameter types.
         * @throws { BusinessError } 13600001 - IPC error
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 11
         */
        on(event: 'progress', callback: Callback<DownloadProgress>): void;
        /**
         * Registers a listener for the batch download of a file from the Drive Kit.
         *
         * @param { 'batchDownload' } event - Event type. The value is **'batchDownload'**, indicating the batch download
         *     event.
         * @param { Callback<MultiDownloadProgress> } callback - Callback used to return the download progress of a file.
         * @throws { BusinessError } 13900020 - Invalid argument. Possible causes:
         *     <br>1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @throws { BusinessError } 22400005 - Inner error. Possible causes:
         *     <br>1.Failed to access the database or execute the SQL statement.
         *     <br>2.System error, such as a null pointer, insufficient memory or a JS engine exception.
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 20
         */
        on(event: 'batchDownload', callback: Callback<MultiDownloadProgress>): void;
        /**
         * Removes the specified callback from the device-cloud file cache progress.
         *
         * @param { 'progress' } event - Event type. The value is **progress**, which indicates the sync progress event.
         * @param { Callback<DownloadProgress> } [callback] - Callback used to return the file download progress. If this
         *     parameter is not specified, this API unregisters all callbacks for the download progress event.
         * @throws { BusinessError } 401 - The input parameter is invalid.Possible causes:1.Mandatory parameters are left
         *     unspecified;
         *     <br>2.Incorrect parameter types.
         * @throws { BusinessError } 13600001 - IPC error
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 11
         */
        off(event: 'progress', callback?: Callback<DownloadProgress>): void;
        /**
         * Removes the listener added via the
         * [on]{@link cloudSync.CloudFileCache#on(event: 'batchDownload', callback: Callback<MultiDownloadProgress>)} API
         * for file batch downloads.
         *
         * @param { 'batchDownload' } event - Event type. The value is **'batchDownload'**, indicating the batch download
         *     event.
         * @param { Callback<MultiDownloadProgress> } [callback] - Callback used to return the download progress of a file.
         *     If this parameter is set, the specified callback will be canceled; otherwise, all currently subscribed
         *     callbacks of the same event type will be canceled.
         * @throws { BusinessError } 13900020 - Invalid argument. Possible causes:
         *     <br>1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @throws { BusinessError } 22400005 - Inner error. Possible causes:
         *     <br>1.Failed to access the database or execute the SQL statement.
         *     <br>2.System error, such as a null pointer, insufficient memory or a JS engine exception.
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 20
         */
        off(event: 'batchDownload', callback?: Callback<MultiDownloadProgress>): void;
        /**
         * Starts downloading a file from the Drive Kit to the local device. This API uses a promise to return the result.
         *
         * @param { string } uri - URI of the file to download.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - The input parameter is invalid.Possible causes:1.Mandatory parameters are left
         *     unspecified;
         *     <br>2.Incorrect parameter types.
         * @throws { BusinessError } 13600001 - IPC error.
         * @throws { BusinessError } 13900002 - No such file or directory.
         * @throws { BusinessError } 13900025 - No space left on device.
         * @throws { BusinessError } 14000002 - Invalid uri.
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 11
         */
        start(uri: string): Promise<void>;
        /**
         * Starts downloading a file from the Drive Kit to the local device. This API uses an asynchronous callback to
         * return the result.
         *
         * @param { string } uri - URI of the file to download.
         * @param { AsyncCallback<void> } callback - Callback used to start downloading a cloud file asynchronously.
         * @throws { BusinessError } 401 - The input parameter is invalid.Possible causes:1.Mandatory parameters are left
         *     unspecified;
         *     <br>2.Incorrect parameter types.
         * @throws { BusinessError } 13600001 - IPC error.
         * @throws { BusinessError } 13900002 - No such file or directory.
         * @throws { BusinessError } 13900025 - No space left on device.
         * @throws { BusinessError } 14000002 - Invalid uri.
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 11
         */
        start(uri: string, callback: AsyncCallback<void>): void;
        /**
         * Starts the batch download of a file from the Drive Kit. This API uses a promise to return the result.
         *
         * Different batch download tasks can be distinguished by the task ID returned.
         *
         * @param { Array<string> } uris - URI list. A maximum of 400 URIs can be transferred at a time. An error (22400004)
         *     will be thrown if the number of URIs exceeds 400.
         * @param { DownloadFileType } [fileType] - File type. The default value is **CONTENT**.
         * @returns { Promise<number> } Promise used to return the ID of the batch download task.
         * @throws { BusinessError } 13600001 - IPC error. Possible causes:
         *     <br>1.IPC failed or timed out. 2.Failed to load the service.
         * @throws { BusinessError } 13900020 - Invalid argument. Possible causes:
         *     <br>1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @throws { BusinessError } 14000002 - Invalid uri.
         * @throws { BusinessError } 22400004 - Exceed the maximum limit.
         * @throws { BusinessError } 22400005 - Inner error. Possible causes:
         *     <br>1.Failed to access the database or execute the SQL statement.
         *     <br>2.System error, such as a null pointer, insufficient memory or a JS engine exception.
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 20
         */
        startBatch(uris: Array<string>, fileType?: DownloadFileType): Promise<number>;
        /**
         * Stop the cloud file cache download task.
         *
         * @param { string } uri - URI of the file to download.
         * @returns { Promise<void> } - Promise that returns no value.
         * @throws { BusinessError } 401 - The input parameter is invalid.Possible causes:1.Mandatory parameters are left
         *     unspecified;
         *     <br>2.Incorrect parameter types.
         * @throws { BusinessError } 13600001 - IPC error.
         * @throws { BusinessError } 13900002 - No such file or directory.
         * @throws { BusinessError } 14000002 - Invalid uri.
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 11
         */
        /**
         * Stops downloading a file from the Drive Kit to the local device. This API uses a promise to return the result.
         *
         * When **stop()** is called, the current file download process terminates, and downloaded files are retained by
         * default. You can call **start()** to resume the download.
         *
         * @param { string } uri - URI of the file to download.
         * @param { boolean } [needClean] - Whether to delete the downloaded files. The default value **false** means not to
         *     delete the downloaded files; the value **true** means the opposite.<br>This parameter is available since API
         *     version 12.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - The input parameter is invalid.Possible causes:1.Mandatory parameters are left
         *     unspecified;
         *     <br>2.Incorrect parameter types.
         * @throws { BusinessError } 13600001 - IPC error.
         * @throws { BusinessError } 13900002 - No such file or directory.
         * @throws { BusinessError } 14000002 - Invalid uri.
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 12
         */
        stop(uri: string, needClean?: boolean): Promise<void>;
        /**
         * Stops downloading a file from the Drive Kit to the local device. This API uses an asynchronous callback to return
         * the result.
         *
         * When **stop()** is called, the current file download process terminates, and downloaded files are retained. You
         * can call **start()** to resume the download.
         *
         * @param { string } uri - URI of the file to download.
         * @param { AsyncCallback<void> } callback - Callback used to stop downloading a cloud file asynchronously.
         * @throws { BusinessError } 401 - The input parameter is invalid.Possible causes:1.Mandatory parameters are left
         *     unspecified;
         *     <br>2.Incorrect parameter types.
         * @throws { BusinessError } 13600001 - IPC error.
         * @throws { BusinessError } 13900002 - No such file or directory.
         * @throws { BusinessError } 14000002 - Invalid uri.
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 11
         */
        stop(uri: string, callback: AsyncCallback<void>): void;
        /**
         * Stops the batch download task enabled by [startBatch]{@link cloudSync.CloudFileCache.startBatch} of a file from
         * the Drive Kit. This API uses a promise to return the result.
         *
         * When **stopBatch()** is called, the batch download terminates. The **needClean** parameter determines whether to
         * delete incompletely downloaded files.
         *
         * @param { number } downloadId - ID of the download task to be stopped.
         * @param { boolean } [needClean] - Whether to delete incompletely downloaded files. The default value **false**
         *     means not to delete the files; the value **true** means the opposite.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 13600001 - IPC error. Possible causes:
         *     <br>1.IPC failed or timed out. 2.Failed to load the service.
         * @throws { BusinessError } 13900020 - Invalid argument. Possible causes:
         *     <br>1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @throws { BusinessError } 22400005 - Inner error. Possible causes:
         *     <br>1.Failed to access the database or execute the SQL statement.
         *     <br>2.System error, such as a null pointer, insufficient memory or a JS engine exception.
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 20
         */
        stopBatch(downloadId: number, needClean?: boolean): Promise<void>;
        /**
         * Deletes a cache file. This API returns the result synchronously.
         *
         * @param { string } uri - URI of the cache file to delete.
         * @throws { BusinessError } 13600001 - IPC error. Possible causes:
         *     <br>1.IPC failed or timed out. 2.Failed to load the service.
         * @throws { BusinessError } 13900002 - No such file or directory.
         * @throws { BusinessError } 13900010 - Try again.
         * @throws { BusinessError } 13900012 - Permission denied by the file system
         * @throws { BusinessError } 13900020 - Invalid argument. Possible causes:
         *     <br>1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @throws { BusinessError } 14000002 - Invalid URI.
         * @throws { BusinessError } 22400005 - Inner error. Possible causes:
         *     <br>1.Failed to access the database or execute the SQL statement.
         *     <br>2.System error, such as a null pointer, insufficient memory or a JS engine exception.
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 20
         */
        cleanFileCache(uri: string): void;
        /**
         * Query the total size of cached files.
         *
         * @returns { Promise<number> } - Return the total size of cached files.
         * @throws { BusinessError } 13900010 - Try again.
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        getCachedTotalSize(): Promise<number>;
        /**
         * Clean all downloaded files except those not yet migrated to the cloud or those that are being written to.
         *
         * @returns { Promise<void> } - Promise that returns no value.
         * @throws { BusinessError } 13900010 - Try again.
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        cleanAllFileCache(): Promise<void>;
    }
    /**
     * Enumerates the device-cloud file sync states.
     *
     * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
     * @since 20
     */
    enum FileState {
        /**
         * Initial state after the first download.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 20
         */
        INITIAL_AFTER_DOWNLOAD = 0,
        /**
         * The file is being uploaded.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 20
         */
        UPLOADING = 1,
        /**
         * The upload has been stopped.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 20
         */
        STOPPED = 2,
        /**
         * The file is going to be uploaded.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 20
         */
        TO_BE_UPLOADED = 3,
        /**
         * The file has been successfully uploaded.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 20
         */
        UPLOAD_SUCCESS = 4,
        /**
         * The file fails to be uploaded.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 20
         */
        UPLOAD_FAILURE = 5
    }
    /**
     * Obtains the upload sync state of a cloud file. This API returns the result synchronously.
     *
     * @param { string } uri - URI of the file whose sync state is to be obtained.
     * @returns { FileState } Upload sync state of the given cloud file.
     * @throws { BusinessError } 13600001 - IPC error. Possible causes:
     *     <br>1.IPC failed or timed out. 2.Failed to load the service.
     * @throws { BusinessError } 13900002 - No such file or directory.
     * @throws { BusinessError } 13900004 - Interrupted system call
     * @throws { BusinessError } 13900010 - Try again
     * @throws { BusinessError } 13900012 - Permission denied by the file system
     * @throws { BusinessError } 13900020 - Invalid argument. Possible causes:
     *     <br>1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
     * @throws { BusinessError } 13900031 - Function not implemented
     * @throws { BusinessError } 14000002 - Invalid URI.
     * @throws { BusinessError } 22400005 - Inner error. Possible causes:
     *     <br>1.Failed to access the database or execute the SQL statement.
     *     <br>2.System error, such as a null pointer, insufficient memory or a JS engine exception.
     * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
     * @since 20
     */
    function getCoreFileSyncState(uri: string): FileState;
    /**
     * Subscribes to the change of a file. The callback returns the changed data.
     *
     * @param { string } uri - URI of the file to download.
     * @param { boolean } recursion - Whether to listen for the change of the URI, subfiles, and subdirectories. The value
     *     **true** means to listen for the change of the URI, subfiles, and subdirectories; the value **false** means to
     *     only listen for the change of the URI.
     * @param { Callback<ChangeData> } callback - Callback used to return the changed data.
     * @throws { BusinessError } 401 - The input parameter is invalid.Possible causes:1.Mandatory parameters are left
     *     unspecified;
     *     <br>2.Incorrect parameter types.
     * @throws { BusinessError } 13900001 - Operation not permitted
     * @throws { BusinessError } 13900002 - No such file or directory.
     * @throws { BusinessError } 13900012 - Permission denied
     * @throws { BusinessError } 14000002 - Invalid uri.
     * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
     * @since 12
     */
    function registerChange(uri: string, recursion: boolean, callback: Callback<ChangeData>): void;
    /**
     * Unsubscribes from the change of a file.
     *
     * @param { string } uri - URI of the file to download.
     * @throws { BusinessError } 401 - The input parameter is invalid.Possible causes:1.Mandatory parameters are left
     *     unspecified;
     *     <br>2.Incorrect parameter types.
     * @throws { BusinessError } 13900001 - Operation not permitted
     * @throws { BusinessError } 13900002 - No such file or directory.
     * @throws { BusinessError } 13900012 - Permission denied
     * @throws { BusinessError } 14000002 - Invalid uri.
     * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
     * @since 12
     */
    function unregisterChange(uri: string): void;
    /**
     * Enumerates the data change types.
     *
     * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
     * @since 12
     */
    enum NotifyType {
        /**
         * A file is created.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 12
         */
        NOTIFY_ADDED = 0,
        /**
         * The file is modified.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 12
         */
        NOTIFY_MODIFIED = 1,
        /**
         * The file is deleted.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 12
         */
        NOTIFY_DELETED = 2,
        /**
         * The file is renamed or moved.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 12
         */
        NOTIFY_RENAMED = 3
    }
    /**
     * Represents the data change information.
     *
     * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
     * @since 12
     */
    interface ChangeData {
        /**
         * Type of the data change.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 12
         */
        type: NotifyType;
        /**
         * Whether the URIs with data changed are of directories. The value **true** means the URIs are of directories; the
         * value **false** means the opposite.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 12
         */
        isDirectory: Array<boolean>;
        /**
         * List of URIs whose data needs to be changed.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 12
         */
        uris: Array<string>;
    }
    /**
     * Represents the historical version information of the device-cloud file when the
     * [gethistoryversionlist]{@link cloudSync.FileVersion.getHistoryVersionList} method of the
     * [FileVersion]{@link cloudSync.FileVersion} class is called.
     *
     * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
     * @since 20
     */
    interface HistoryVersion {
        /**
         * File content modification timestamp, in milliseconds.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 20
         */
        editedTime: number;
        /**
         * File size in bytes.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 20
         */
        fileSize: number;
        /**
         * File version.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 20
         */
        versionId: string;
        /**
         * File name of the current version.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 20
         */
        originalFileName: string;
        /**
         * Hash value of the file content of the current version.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 20
         */
        sha256: string;
        /**
         * Whether the current version is the one where conflicts were automatically resolved.
         *
         * When the application is set to manually resolve conflicts, **false** is returned by default, which is
         * meaningless.
         *
         * When the application is set to automatically resolve conflicts, the device side automatically resolves conflicts.
         * The value **true** means conflicts exist in the current version and have been automatically resolved by the
         * device-cloud service; the value **false** means no conflict exists and conflicts are not automatically resolved.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 20
         */
        autoResolved: boolean;
    }
    /**
     * Represents the download state and progress information of historical version files when the
     * [downloadHistoryVersion]{@link cloudSync.FileVersion.downloadHistoryVersion} method of the
     * [FileVersion]{@link cloudSync.FileVersion} class is called.
     *
     * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
     * @since 20
     */
    interface VersionDownloadProgress {
        /**
         * Download state of the cloud file of the selected version.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 20
         */
        state: State;
        /**
         * Download progress, in percentage.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 20
         */
        progress: number;
        /**
         * Type of the error returned when the batch download fails.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 20
         */
        errType: DownloadErrorType;
    }
    /**
     * Represents the device-cloud file version management class. It allows you to manage historical versions of client-
     * cloud files, obtain the list of historical versions, download historical versions to the local device, replace the
     * current local file with a historical version file, and query and remove conflict flags for version conflicts.
     *
     * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
     * @since 20
     */
    class FileVersion {
        /**
         * A constructor used to create a **FileVersion** instance.
         *
         * @throws { BusinessError } 22400005 - Inner error. Possible causes:
         *     <br>1.Failed to access the database or execute the SQL statement.
         *     <br>2.System error, such as a null pointer, insufficient memory or a JS engine exception.
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 20
         */
        constructor();
        /**
         * Obtains the list of historical versions. The returned versions are sorted by modification time. The earlier the
         * modification time, the later the version. This API uses a promise to return the result.
         *
         * If the number of cloud versions is less than the length limit, the list will be returned with the actual number
         * of versions.
         *
         * If the number of cloud versions is greater than or equal to the length limit, the number of the latest versions (
         * specified by **versionNumLimit**) will be returned.
         *
         * @param { string } uri - File URI.
         * @param { number } versionNumLimit - Length limit of the historical version list. The value range is [0, 100000] (
         *     unit: number). If the input value is greater than 100,000, the list is returned according to the maximum
         *     value.
         * @returns { Promise<Array<HistoryVersion>> } Promise used to return the list of historical versions.
         * @throws { BusinessError } 13600001 - IPC error. Possible causes:
         *     <br>1.IPC failed or timed out. 2.Failed to load the service.
         * @throws { BusinessError } 13900002 - No such file or directory.
         * @throws { BusinessError } 13900010 - Try again.
         * @throws { BusinessError } 13900012 - Permission denied by the file system.
         * @throws { BusinessError } 13900020 - Invalid argument. Possible causes:
         *     <br>1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @throws { BusinessError } 14000002 - Invalid URI.
         * @throws { BusinessError } 22400002 - Network unavailable.
         * @throws { BusinessError } 22400005 - Inner error. Possible causes:
         *     <br>1.Failed to access the database or execute the SQL statement.
         *     <br>2.System error, such as a null pointer, insufficient memory or a JS engine exception.
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 20
         */
        getHistoryVersionList(uri: string, versionNumLimit: number): Promise<Array<HistoryVersion>>;
        /**
         * Obtains the content of a file of a specified version based on the version number. You can download a file of a
         * specified version from the cloud to a temporary local path. The application determines whether to replace the
         * original file with the temporary file, or retain or delete the temporary file. The callback returns the file
         * download progress, and the promise returns the URI of the temporary file of an earlier version.
         *
         * @param { string } uri - File URI.
         * @param { string } versionId - Version ID of a file. The format is returned by the
         *     [gethistoryversionlist]{@link cloudSync.FileVersion.getHistoryVersionList} API.
         * @param { Callback<VersionDownloadProgress> } callback - Callback used to return the download progress.
         * @returns { Promise<string> } Promise used to return the URI of the temporary file of a historical version.
         * @throws { BusinessError } 13600001 - IPC error. Possible causes:
         *     <br>1.IPC failed or timed out. 2.Failed to load the service.
         * @throws { BusinessError } 13900002 - No such file or directory.
         * @throws { BusinessError } 13900010 - Try again.
         * @throws { BusinessError } 13900012 - Permission denied by the file system.
         * @throws { BusinessError } 13900020 - Invalid argument. Possible causes:
         *     <br>1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @throws { BusinessError } 14000002 - Invalid URI.
         * @throws { BusinessError } 22400002 - Network unavailable.
         * @throws { BusinessError } 22400005 - Inner error. Possible causes:
         *     <br>1.Failed to access the database or execute the SQL statement.
         *     <br>2.System error, such as a null pointer, insufficient memory or a JS engine exception.
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 20
         */
        downloadHistoryVersion(uri: string, versionId: string, callback: Callback<VersionDownloadProgress>): Promise<string>;
        /**
         * Replaces the local file with the file of a historical version. Before replacement, call the
         * [downloadHistoryVersion]{@link cloudSync.FileVersion.downloadHistoryVersion} method to download the selected
         * historical version and obtain its version URI. If this API is called directly without prior download or the
         * version URI is invalid, an exception will be thrown. Once replacement is complete, the temporary file will be
         * automatically deleted. This API uses a promise to return the result.
         *
         * @param { string } originalUri - URI of the local file.
         * @param { string } versionUri - URI of the historical file.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 13600001 - IPC error. Possible causes:
         *     <br>1.IPC failed or timed out. 2.Failed to load the service.
         * @throws { BusinessError } 13900002 - No such file or directory.
         * @throws { BusinessError } 13900005 - I/O error.
         * @throws { BusinessError } 13900008 - Bad file descriptor.
         * @throws { BusinessError } 13900010 - Try again.
         * @throws { BusinessError } 13900012 - Permission denied by the file system.
         * @throws { BusinessError } 13900020 - Invalid argument. Possible causes:
         *     <br>1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @throws { BusinessError } 14000002 - Invalid URI. Possible causes: 1.originalUri invalid; 2.versionUri invalid.
         * @throws { BusinessError } 22400005 - Inner error. Possible causes:
         *     <br>1.Failed to access the database or execute the SQL statement.
         *     <br>2.System error, such as a null pointer, insufficient memory or a JS engine exception.
         * @throws { BusinessError } 22400007 - The version file specified to replace the original file does not exist.
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 20
         */
        replaceFileWithHistoryVersion(originalUri: string, versionUri: string): Promise<void>;
        /**
         * Obtains the version conflict flag of a local file. This API uses a promise to return the result. This API takes
         * effect only when the application is configured for manual conflict resolution. Otherwise, conflicts are
         * automatically resolved during synchronization, and the return value will be **false**.
         *
         * Once the application is configured for manual conflict resolution, calling this API returns whether the current
         * local file conflicts with the cloud file. The application then prompts the user to handle the conflict. After the
         * conflict is resolved, you need to call the [clearFileConflict]{@link cloudSync.FileVersion.clearFileConflict}
         * method to clear the conflict flag and synchronize the file to the cloud.
         *
         * @param { string } uri - File URI.
         * @returns { Promise<boolean> } Promise used to return the conflict flag between the local file and the cloud file.
         *     The value **true** indicates that the local file conflicts with the cloud file, and the value **false**
         *     indicates the opposite.
         * @throws { BusinessError } 13600001 - IPC error. Possible causes:
         *     <br>1.IPC failed or timed out. 2.Failed to load the service.
         * @throws { BusinessError } 13900002 - No such file or directory.
         * @throws { BusinessError } 13900010 - Try again.
         * @throws { BusinessError } 13900012 - Permission denied by the file system.
         * @throws { BusinessError } 13900020 - Invalid argument. Possible causes:
         *     <br>1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @throws { BusinessError } 14000002 - Invalid URI.
         * @throws { BusinessError } 22400005 - Inner error. Possible causes:
         *     <br>1.Failed to access the database or execute the SQL statement.
         *     <br>2.System error, such as a null pointer, insufficient memory or a JS engine exception.
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 20
         */
        isFileConflict(uri: string): Promise<boolean>;
        /**
         * Clears the version conflict flag of the local file. If a conflict occurs, you need to call this API to clear the
         * conflict flag after the conflict is resolved locally and trigger automatic synchronization. This API uses a
         * promise to return the result.
         *
         * @param { string } uri - URI of the file for which the conflict flag is to be cleared.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 13600001 - IPC error. Possible causes:
         *     <br>1.IPC failed or timed out. 2.Failed to load the service.
         * @throws { BusinessError } 13900002 - No such file or directory.
         * @throws { BusinessError } 13900010 - Try again.
         * @throws { BusinessError } 13900012 - Permission denied by the file system.
         * @throws { BusinessError } 13900020 - Invalid argument. Possible causes:
         *     <br>1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.
         * @throws { BusinessError } 14000002 - Invalid URI.
         * @throws { BusinessError } 22400005 - Inner error. Possible causes:
         *     <br>1.Failed to access the database or execute the SQL statement.
         *     <br>2.System error, such as a null pointer, insufficient memory or a JS engine exception.
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSync.Core
         * @since 20
         */
        clearFileConflict(uri: string): Promise<void>;
    }
}
export default cloudSync;

```
