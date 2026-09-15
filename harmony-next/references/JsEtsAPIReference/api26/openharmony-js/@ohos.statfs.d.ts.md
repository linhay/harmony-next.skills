# @ohos.statfs.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (C) 2021-2023 Huawei Device Co., Ltd.
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
 * @kit API10LessDeprecatedModules
 */
import { AsyncCallback } from './@ohos.base';
/**
 * The **statfs** module provides APIs for obtaining file system information, including the total size and free size of
 * a file system, in bytes.
 *
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 8
 * @deprecated since 9
 * @useinstead @ohos.file.statvfs:statfs
 */
declare namespace Statfs {
    /**
     * Obtains the free size of the specified file system, in bytes. This API uses an asynchronous callback to return the
     * result.
     *
     * @param { string } path - Path of the file system.
     * @param { AsyncCallback<number> } callback - Callback used to return the free size obtained, in bytes.
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.file.statvfs:statfs.getFreeBytes
     */
    function getFreeBytes(path: string, callback: AsyncCallback<number>): void;
    /**
     * Obtains the free size of the specified file system, in bytes. This API uses a promise to return the result.
     *
     * @param { string } path - Path of the file system.
     * @returns { Promise<number> } Promise used to return the free size obtained, in bytes.
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.file.statvfs:statfs.getFreeBytes
     */
    function getFreeBytes(path: string): Promise<number>;
    /**
     * Obtains the total size of the specified file system, in bytes. This API uses an asynchronous callback to return the
     * result.
     *
     * @param { string } path - Path of the file system.
     * @param { AsyncCallback<number> } callback - Callback used to return the total size obtained, in bytes.
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.file.statvfs:statfs.getTotalBytes
     */
    function getTotalBytes(path: string, callback: AsyncCallback<number>): void;
    /**
     * Obtains the total size of the specified file system, in byte. This API uses a promise to return the result.
     *
     * @param { string } path - Path of the file system.
     * @returns { Promise<number> } Promise used to return the total size obtained, in bytes.
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.file.statvfs:statfs.getTotalBytes
     */
    function getTotalBytes(path: string): Promise<number>;
}
export default Statfs;

```
