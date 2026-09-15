# @ohos.file.storageStatistics.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (C) 2022-2026 Huawei Device Co., Ltd.
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
import { AsyncCallback } from './@ohos.base';
/**
 * The **storageStatistics** module provides APIs for obtaining storage space information, including the space of
 * built-in and plug-in memory cards, space occupied by different types of data, and space of application data.
 *
 * @syscap SystemCapability.FileManagement.StorageService.SpatialStatistics
 * @since 8
 */
declare namespace storageStatistics {
    /**
     * Get the bundle statistics.
     *
     * @syscap SystemCapability.FileManagement.StorageService.SpatialStatistics
     * @since 9
     */
    export interface BundleStats {
        /**
         * Size of the application installation files, in bytes.
         *
         * @syscap SystemCapability.FileManagement.StorageService.SpatialStatistics
         * @since 9
         */
        appSize: number;
        /**
         * Size of the application cache files, in bytes.
         *
         * @syscap SystemCapability.FileManagement.StorageService.SpatialStatistics
         * @since 9
         */
        cacheSize: number;
        /**
         * Size of other files of the application, in bytes.
         *
         * @syscap SystemCapability.FileManagement.StorageService.SpatialStatistics
         * @since 9
         */
        dataSize: number;
    }
    /**
     * Obtains the storage space (in bytes) of this application. This API uses an asynchronous callback to return the
     * result.
     *
     * @param { AsyncCallback<BundleStats> } callback - Callback used to return the application space obtained.
     * @throws { BusinessError } 401 - The input parameter is invalid.Possible causes:Mandatory
     *     parameters are left unspecified;
     * @throws { BusinessError } 13600001 - IPC error.
     * @throws { BusinessError } 13900042 - Unknown error.
     * @syscap SystemCapability.FileManagement.StorageService.SpatialStatistics
     * @since 9
     */
    function getCurrentBundleStats(callback: AsyncCallback<BundleStats>): void;
    /**
     * Obtains the storage space (in bytes) of this application. This API uses a promise to return the result.
     *
     * @returns { Promise<BundleStats> } Promise used to return the application storage space obtained.
     * @throws { BusinessError } 401 - The input parameter is invalid.Possible causes:Mandatory
     *     parameters are left unspecified;
     * @throws { BusinessError } 13600001 - IPC error.
     * @throws { BusinessError } 13900042 - Unknown error.
     * @syscap SystemCapability.FileManagement.StorageService.SpatialStatistics
     * @since 9
     */
    function getCurrentBundleStats(): Promise<BundleStats>;
    /**
     * Obtains the total size (in bytes) of the built-in storage. This API uses an asynchronous callback to return the
     * result.
     *
     * @param { AsyncCallback<number> } callback - Callback used to return the built-in storage space obtained.
     * @throws { BusinessError } 401 - The input parameter is invalid.Possible causes:Mandatory
     *     parameters are left unspecified;
     * @throws { BusinessError } 13600001 - IPC error.
     * @throws { BusinessError } 13900042 - Unknown error.
     * @syscap SystemCapability.FileManagement.StorageService.SpatialStatistics
     * @since 15
     */
    function getTotalSize(callback: AsyncCallback<number>): void;
    /**
     * Obtains the total size (in bytes) of the built-in storage. This API uses a promise to return the result.
     *
     * @returns { Promise<number> } Promise used to return the total built-in storage space obtained.
     * @throws { BusinessError } 13600001 - IPC error.
     * @throws { BusinessError } 13900042 - Unknown error.
     * @syscap SystemCapability.FileManagement.StorageService.SpatialStatistics
     * @since 15
     */
    function getTotalSize(): Promise<number>;
    /**
     * Obtains the total space of the built-in storage, in bytes. This API returns the result synchronously.
     *
     * @returns { number } Built-in storage space obtained.
     * @throws { BusinessError } 13600001 - IPC error.
     * @throws { BusinessError } 13900042 - Unknown error.
     * @syscap SystemCapability.FileManagement.StorageService.SpatialStatistics
     * @since 15
     */
    function getTotalSizeSync(): number;
    /**
     * Obtains the available space (in bytes) of the built-in storage. This API uses an asynchronous callback to return the
     * result.
     *
     * @param { AsyncCallback<number> } callback - Callback used to return the available space of the built-in storage
     *     obtained.
     * @throws { BusinessError } 401 - The input parameter is invalid.Possible causes:Mandatory
     *     parameters are left unspecified;
     * @throws { BusinessError } 13600001 - IPC error.
     * @throws { BusinessError } 13900042 - Unknown error.
     * @syscap SystemCapability.FileManagement.StorageService.SpatialStatistics
     * @since 15
     */
    function getFreeSize(callback: AsyncCallback<number>): void;
    /**
     * Obtains the available space (in bytes) of the built-in storage. This API uses a promise to return the result.
     *
     * @returns { Promise<number> } Promise used to return the available space of the built-in storage obtained.
     * @throws { BusinessError } 13600001 - IPC error.
     * @throws { BusinessError } 13900042 - Unknown error.
     * @syscap SystemCapability.FileManagement.StorageService.SpatialStatistics
     * @since 15
     */
    function getFreeSize(): Promise<number>;
    /**
     * Obtains the available space of the built-in storage, in bytes. This API returns the result synchronously.
     *
     * @returns { number } Available space of the built-in storage obtained.
     * @throws { BusinessError } 13600001 - IPC error.
     * @throws { BusinessError } 13900042 - Unknown error.
     * @syscap SystemCapability.FileManagement.StorageService.SpatialStatistics
     * @since 15
     */
    function getFreeSizeSync(): number;
    /**
     * Obtains the total number of inode resources in the file system. Only the system data partition can be queried.
     * This API uses a promise to return the result.
     *
     * @returns { Promise<number> } Promise object, which returns the total number of inode resources in the file system.
     * @throws { BusinessError } 13600001 - IPC error.
     * @throws { BusinessError } 13600016 - Failed to query the inode information of the data partition.
     * @syscap SystemCapability.FileManagement.StorageService.SpatialStatistics
     * @stagemodelonly
     * @since 24
     */
    function getTotalInodes(): Promise<number>;
    /**
     * Obtains the remaining inode resources of a file system. Only the system data partition can be queried.
     * This API uses a promise to return the result.
     *
     * @returns { Promise<number> } Promise object, which returns the remaining inode resources of the file system.
     * @throws { BusinessError } 13600001 - IPC error.
     * @throws { BusinessError } 13600016 - Failed to query the inode information of the data partition.
     * @syscap SystemCapability.FileManagement.StorageService.SpatialStatistics
     * @stagemodelonly
     * @since 24
     */
    function getFreeInodes(): Promise<number>;
    /**
     * Obtaining the inode Usage of the Current Application.This API uses a promise to return the result.
     *
     * @returns { Promise<number> } Promise object, which returns the inode usage of the current application.
     * @throws { BusinessError } 13600001 - IPC error.
     * @throws { BusinessError } 13600002 - File system not supported.
     * @throws { BusinessError } 13600017 - Failed to query the inode information of the application.
     * @syscap SystemCapability.FileManagement.StorageService.SpatialStatistics
     * @stagemodelonly
     * @since 24
     */
    function getCurrentBundleInodes(): Promise<number>;
}
export default storageStatistics;

```
