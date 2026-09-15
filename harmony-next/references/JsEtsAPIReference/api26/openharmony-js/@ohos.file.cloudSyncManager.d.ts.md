# @ohos.file.cloudSyncManager.d.ts

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
/**
 * The **cloudSyncManager** module provides APIs for managing device-cloud sync for applications. You can use the APIs
 * to manage the full download state, the reason why the full download stops, and number of local and cloud files.
 *
 * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSyncManager
 * @since 10
 */
declare namespace cloudSyncManager {
    /**
     * Enumerates the reasons why the full download stops. The default value is **NO_STOP**.
     *
     * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSyncManager
     * @since 20
     */
    enum DownloadStopReason {
        /**
         * Downloading.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSyncManager
         * @since 20
         */
        NO_STOP = 0,
        /**
         * Downloading. Mobile network and Wi-Fi are unavailable.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSyncManager
         * @since 20
         */
        NETWORK_UNAVAILABLE = 1,
        /**
         * Downloading. The device storage is full.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSyncManager
         * @since 20
         */
        LOCAL_STORAGE_FULL = 2,
        /**
         * Downloading. The device temperature exceeds the upper limit.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSyncManager
         * @since 20
         */
        TEMPERATURE_LIMIT = 3,
        /**
         * Downloading. The user stops the download.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSyncManager
         * @since 20
         */
        USER_STOPPED = 4,
        /**
         * Downloading. The application is uninstalled.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSyncManager
         * @since 20
         */
        APP_UNLOAD = 5,
        /**
         * Downloading. The download stops due to other reasons, for example, the cloud server does not respond.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSyncManager
         * @since 20
         */
        OTHER_REASON = 6
    }
    /**
     * Enumerates the full download states.
     *
     * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSyncManager
     * @since 20
     */
    enum DownloadState {
        /**
         * Downloading.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSyncManager
         * @since 20
         */
        RUNNING = 0,
        /**
         * Downloaded.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSyncManager
         * @since 20
         */
        COMPLETED = 1,
        /**
         * Downloading stopped.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSyncManager
         * @since 20
         */
        STOPPED = 2
    }
    /**
     * Represents the number and size of local and cloud files of an application.
     *
     * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSyncManager
     * @since 20
     */
    interface CloudFileInfo {
        /**
         * Total number of cloud files that are not downloaded locally. The value range is [0, INT32_MAX].
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSyncManager
         * @since 20
         */
        cloudFileCount: number;
        /**
         * Total size of cloud files that are not downloaded locally, in bytes. The value range is [0, INT64_MAX].
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSyncManager
         * @since 20
         */
        cloudFileTotalSize: number;
        /**
         * Total number of local files that are not uploaded to the cloud. The value range is [0, INT32_MAX].
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSyncManager
         * @since 20
         */
        localFileCount: number;
        /**
         * Total size of local files that are not uploaded to the cloud, in bytes. The value range is [0, INT64_MAX].
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSyncManager
         * @since 20
         */
        localFileTotalSize: number;
        /**
         * Total number of local files that have been uploaded to the cloud. The value range is [0, INT32_MAX].
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSyncManager
         * @since 20
         */
        bothFileCount: number;
        /**
         * Total size of local files that have been uploaded to the cloud, in bytes. The value range is [0, INT64_MAX].
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSyncManager
         * @since 20
         */
        bothFileTotalSize: number;
    }
    /**
     * Describes the full download progress.
     *
     * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSyncManager
     * @since 20
     */
    class DownloadProgress {
        /**
         * Download state.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSyncManager
         * @since 20
         */
        state: DownloadState;
        /**
         * Number of downloaded files. The value range is [0, INT32_MAX]. If the progress is abnormal, **-1** is returned.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSyncManager
         * @since 20
         */
        successfulCount: number;
        /**
         * Number of files that fail to be downloaded. The value range is [0, INT32_MAX]. If the progress is abnormal,
         * **-1** is returned.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSyncManager
         * @since 20
         */
        failedCount: number;
        /**
         * Total number of files to be downloaded. The value range is [0, INT32_MAX]. If the progress is abnormal, **-1** is
         * returned.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSyncManager
         * @since 20
         */
        totalCount: number;
        /**
         * Size of the downloaded data, in bytes. The value range is
         * [0, INT64_MAX). If the progress is abnormal, **INT64_MAX** is returned.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSyncManager
         * @since 20
         */
        downloadedSize: number;
        /**
         * Total size of the files to be downloaded, in bytes. The value range is
         * [0, INT64_MAX). If the progress is abnormal, **INT64_MAX** is returned.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSyncManager
         * @since 20
         */
        totalSize: number;
        /**
         * Reason why the download stops.
         *
         * @syscap SystemCapability.FileManagement.DistributedFileService.CloudSyncManager
         * @since 20
         */
        stopReason: DownloadStopReason;
    }
}
export default cloudSyncManager;

```
