# @ohos.file.statvfs.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (C) 2022-2025 Huawei Device Co., Ltd.
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
/**
 * This module provides APIs for obtaining file system information, including the total size and free size of a file
 * system, in bytes.
 *
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @since 9
 */
declare namespace statfs {
    /**
     * Obtains the free size of the specified file system, in bytes. This API uses a promise to return the result.
     *
     * @param { string } path - File path of the file system.
     * @returns { Promise<number> } Promise used to return the free size obtained, in bytes.
     * @throws { BusinessError } 13900002 - No such file or directory
     * @throws { BusinessError } 13900004 - Interrupted system call
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900008 - Bad file descriptor
     * @throws { BusinessError } 13900011 - Out of memory
     * @throws { BusinessError } 13900012 - Permission denied
     * @throws { BusinessError } 13900013 - Bad address
     * @throws { BusinessError } 13900018 - Not a directory
     * @throws { BusinessError } 13900030 - File name too long
     * @throws { BusinessError } 13900031 - Function not implemented
     * @throws { BusinessError } 13900033 - Too many symbolic links encountered
     * @throws { BusinessError } 13900038 - Value too large for defined data type
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 9
     */
    function getFreeSize(path: string): Promise<number>;
    /**
     * Obtains the free size of the specified file system, in bytes. This API uses an asynchronous callback to return the
     * result.
     *
     * @param { string } path - File path of the file system.
     * @param { AsyncCallback<number> } [callback] - Callback used to return the free size obtained, in bytes.
     * @throws { BusinessError } 13900002 - No such file or directory
     * @throws { BusinessError } 13900004 - Interrupted system call
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900008 - Bad file descriptor
     * @throws { BusinessError } 13900011 - Out of memory
     * @throws { BusinessError } 13900012 - Permission denied
     * @throws { BusinessError } 13900013 - Bad address
     * @throws { BusinessError } 13900018 - Not a directory
     * @throws { BusinessError } 13900030 - File name too long
     * @throws { BusinessError } 13900031 - Function not implemented
     * @throws { BusinessError } 13900033 - Too many symbolic links encountered
     * @throws { BusinessError } 13900038 - Value too large for defined data type
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 9
     */
    function getFreeSize(path: string, callback: AsyncCallback<number>): void;
    /**
     * Obtains the free size of the specified file system, in bytes. This API returns the result synchronously.
     *
     * @param { string } path - File path of the file system.
     * @returns { number } Free size obtained, in bytes.
     * @throws { BusinessError } 13900002 - No such file or directory
     * @throws { BusinessError } 13900004 - Interrupted system call
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900008 - Bad file descriptor
     * @throws { BusinessError } 13900011 - Out of memory
     * @throws { BusinessError } 13900012 - Permission denied
     * @throws { BusinessError } 13900013 - Bad address
     * @throws { BusinessError } 13900018 - Not a directory
     * @throws { BusinessError } 13900030 - File name too long
     * @throws { BusinessError } 13900031 - Function not implemented
     * @throws { BusinessError } 13900033 - Too many symbolic links encountered
     * @throws { BusinessError } 13900038 - Value too large for defined data type
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 10
     */
    function getFreeSizeSync(path: string): number;
    /**
     * Obtains the total size of the specified file system, in bytes. This API uses a promise to return the result.
     *
     * @param { string } path - File path of the file system.
     * @returns { Promise<number> } Promise used to return the total size obtained, in bytes.
     * @throws { BusinessError } 13900002 - No such file or directory
     * @throws { BusinessError } 13900004 - Interrupted system call
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900008 - Bad file descriptor
     * @throws { BusinessError } 13900011 - Out of memory
     * @throws { BusinessError } 13900012 - Permission denied
     * @throws { BusinessError } 13900013 - Bad address
     * @throws { BusinessError } 13900018 - Not a directory
     * @throws { BusinessError } 13900030 - File name too long
     * @throws { BusinessError } 13900031 - Function not implemented
     * @throws { BusinessError } 13900033 - Too many symbolic links encountered
     * @throws { BusinessError } 13900038 - Value too large for defined data type
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 9
     */
    function getTotalSize(path: string): Promise<number>;
    /**
     * Obtains the total size of the specified file system, in bytes. This API uses an asynchronous callback to return the
     * result.
     *
     * @param { string } path - File path of the file system.
     * @param { AsyncCallback<number> } [callback] - Callback used to return the total size obtained, in bytes.
     * @throws { BusinessError } 13900002 - No such file or directory
     * @throws { BusinessError } 13900004 - Interrupted system call
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900008 - Bad file descriptor
     * @throws { BusinessError } 13900011 - Out of memory
     * @throws { BusinessError } 13900012 - Permission denied
     * @throws { BusinessError } 13900013 - Bad address
     * @throws { BusinessError } 13900018 - Not a directory
     * @throws { BusinessError } 13900030 - File name too long
     * @throws { BusinessError } 13900031 - Function not implemented
     * @throws { BusinessError } 13900033 - Too many symbolic links encountered
     * @throws { BusinessError } 13900038 - Value too large for defined data type
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 9
     */
    function getTotalSize(path: string, callback: AsyncCallback<number>): void;
    /**
     * Obtains the total size of the specified file system, in bytes. This API returns the result synchronously.
     *
     * @param { string } path - File path of the file system.
     * @returns { number } Total size obtained, in bytes.
     * @throws { BusinessError } 13900002 - No such file or directory
     * @throws { BusinessError } 13900004 - Interrupted system call
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900008 - Bad file descriptor
     * @throws { BusinessError } 13900011 - Out of memory
     * @throws { BusinessError } 13900012 - Permission denied
     * @throws { BusinessError } 13900013 - Bad address
     * @throws { BusinessError } 13900018 - Not a directory
     * @throws { BusinessError } 13900030 - File name too long
     * @throws { BusinessError } 13900031 - Function not implemented
     * @throws { BusinessError } 13900033 - Too many symbolic links encountered
     * @throws { BusinessError } 13900038 - Value too large for defined data type
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 10
     */
    function getTotalSizeSync(path: string): number;
}
export default statfs;

```
