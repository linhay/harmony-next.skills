# @ohos.file.fs.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2022-2026 Huawei Device Co., Ltd.
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
import stream from './@ohos.util.stream';
/**
 * FileIO
 *
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare namespace fileIo {
    export { access };
    export { accessSync };
    export { close };
    export { closeSync };
    export { copy };
    export { copyDir };
    export { copyDirSync };
    export { copyFile };
    export { copyFileSync };
    export { createRandomAccessFile };
    export { createRandomAccessFileSync };
    export { createStream };
    export { createStreamSync };
    export { createReadStream };
    export { createWriteStream };
    export { createWatcher };
    export { dup };
    export { fdatasync };
    export { fdatasyncSync };
    export { fdopenStream };
    export { fdopenStreamSync };
    export { fsync };
    export { fsyncSync };
    export { getxattr };
    export { getxattrSync };
    export { listFile };
    export { listFileSync };
    export { listFileExt };
    export { listFileExtSync };
    export { lseek };
    export { lstat };
    export { lstatSync };
    export { mkdir };
    export { mkdirSync };
    export { mkdtemp };
    export { mkdtempSync };
    export { mmap };
    export { mmapSync };
    export { moveDir };
    export { moveDirSync };
    export { moveFile };
    export { moveFileSync };
    export { open };
    export { openSync };
    export { read };
    export { readSync };
    export { readLines };
    export { readLinesSync };
    export { readText };
    export { readTextSync };
    export { rename };
    export { renameSync };
    export { rmdir };
    export { rmdirSync };
    export { setxattr };
    export { setxattrSync };
    export { stat };
    export { statSync };
    export { symlink };
    export { symlinkSync };
    export { truncate };
    export { truncateSync };
    export { unlink };
    export { unlinkSync };
    export { utimes };
    export { write };
    export { writeSync };
    export { AccessModeType };
    export { AccessFlagType };
    export { File };
    export { FileMapping };
    export { MappingMode };
    export { OpenMode };
    export { RandomAccessFile };
    export { ReaderIterator };
    export { Stat };
    export { Stream };
    export { ReadStream };
    export { WriteStream };
    export { AtomicFile };
    export { Watcher };
    export { WhenceType };
    export { TaskSignal };
    export { connectDfs };
    export { disconnectDfs };
    export type { Progress };
    export type { CopyOptions };
    export type { ProgressListener };
    export type { DfsListeners };
    /**
     * Mode Indicates the open flags.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    namespace OpenMode {
        /**
         * Open the file in read-only mode.
         *
         * @syscap SystemCapability.FileManagement.File.FileIO
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        const READ_ONLY = 0o0;
        /**
         * Open the file in write-only mode.
         *
         * @syscap SystemCapability.FileManagement.File.FileIO
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        const WRITE_ONLY = 0o1;
        /**
         * Open the file in read/write mode.
         *
         * @syscap SystemCapability.FileManagement.File.FileIO
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        const READ_WRITE = 0o2;
        /**
         * Create a file if the specified file does not exist.
         *
         * @syscap SystemCapability.FileManagement.File.FileIO
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        const CREATE = 0o100;
        /**
         * If the file exists and is opened in write-only or read/write mode, truncate the file
         * length to 0.
         *
         * @syscap SystemCapability.FileManagement.File.FileIO
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        const TRUNC = 0o1000;
        /**
         * Open the file in append mode. New data will be written to the end of the file.
         *
         * @syscap SystemCapability.FileManagement.File.FileIO
         * @crossplatform [since 10]
         * @atomicservice [since 11]
         * @since 9
         */
        const APPEND = 0o2000;
        /**
         * If **path** points to a named pipe (FIFO), block special file, or character special
         * file, perform non-blocking operations on the open file and in subsequent I/Os.
         *
         * @syscap SystemCapability.FileManagement.File.FileIO
         * @crossplatform [since 10]
         * @since 9
         */
        const NONBLOCK = 0o4000;
        /**
         * If **path** does not point to a directory, throw an exception.
         *
         * @syscap SystemCapability.FileManagement.File.FileIO
         * @crossplatform [since 10]
         * @since 9
         */
        const DIR = 0o200000;
        /**
         * If **path** points to a symbolic link, throw an exception.
         *
         * @syscap SystemCapability.FileManagement.File.FileIO
         * @crossplatform [since 10]
         * @since 9
         */
        const NOFOLLOW = 0o400000;
        /**
         * Open the file in synchronous I/O mode.
         *
         * @syscap SystemCapability.FileManagement.File.FileIO
         * @crossplatform [since 10]
         * @since 9
         */
        const SYNC = 0o4010000;
        /**
         * UNCACHE IO.
         *
         * @syscap SystemCapability.FileManagement.File.FileIO
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        const UNCACHE = 0o10000000000;
    }
}
/**
 * Checks whether the file or directory exists or has the operation permission. This API uses a promise to return the
 * result.
 *
 * If the read, write, or read and write permission verification fails, the error code 13900012 (Permission denied) will
 * be thrown.
 *
 * @param { string } path - Application sandbox path of the file or directory.
 * @param { AccessModeType } [mode] - Permission on the file or directory to check. If this parameter is left blank, the
 *     system checks whether the file exists. [since 12]
 * @returns { Promise<boolean> } Promise used to return a Boolean value. The value **true** means the file exists; the
 *     value **false** means the opposite.
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900023 - Text file busy
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare function access(path: string, mode?: AccessModeType): Promise<boolean>;
/**
 * Checks whether a file or directory exists. This API uses an asynchronous callback to return the result.
 *
 * @param { string } path - Application sandbox path of the file or directory.
 * @param { AsyncCallback<boolean> } callback - Callback used to return the result. The value **true** means the file
 *     exists; the value **false** means the opposite.
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900023 - Text file busy
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare function access(path: string, callback: AsyncCallback<boolean>): void;
/**
 * Checks whether the file or directory is stored locally or has the operation permission. This API uses a promise to
 * return the result.
 *
 * If the read, write, or read and write permission verification fails, the error code 13900012 (Permission denied) will
 * be thrown.
 *
 * @param { string } path - Application sandbox path of the file or directory.
 * @param { AccessModeType } mode - Permission on the file or directory to check.
 * @param { AccessFlagType } flag - Position of the file or directory to check.
 * @returns { Promise<boolean> } Promise used to return a Boolean value. The value **true** means the file or directory
 *     is a local one and has the related permission. The value **false** means the file or directory does not exist or
 *     is on the cloud or a distributed device.
 * @throws { BusinessError } 401 - Parameter error. Possible causes:1.Mandatory parameters are left unspecified;
 *     <br>2.Incorrect parameter types.
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900023 - Text file busy
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 12
 */
declare function access(path: string, mode: AccessModeType, flag: AccessFlagType): Promise<boolean>;
/**
 * Checks whether a file or directory exists or has the operation permission. This API returns the result synchronously.
 *
 * If the read, write, or read and write permission verification fails, the error code 13900012 (Permission denied) will
 * be thrown.
 *
 * @param { string } path - Application sandbox path of the file or directory.
 * @param { AccessModeType } [mode] - Permission on the file or directory to check. If this parameter is left blank, the
 *     system checks whether the file or directory exists. [since 12]
 * @returns { boolean } The value **true** means the file exists; the value **false** means the opposite.
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900023 - Text file busy
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare function accessSync(path: string, mode?: AccessModeType): boolean;
/**
 * Checks whether a file or directory is stored locally or has the operation permission. This API returns the result
 * synchronously.
 *
 * If the read, write, or read and write permission verification fails, the error code 13900012 (Permission denied) will
 * be thrown.
 *
 * @param { string } path - Application sandbox path of the file to check.
 * @param { AccessModeType } mode - Permission on the file or directory to check.
 * @param { AccessFlagType } flag - Position of the file or directory to check.
 * @returns { boolean } The value **true** means the file is a local file and has the related permission. The value
 *     **false** means the file does not exist or is on the cloud or a distributed device.
 * @throws { BusinessError } 401 - Parameter error. Possible causes:1.Mandatory parameters are left unspecified;
 *     <br>2.Incorrect parameter types.
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900023 - Text file busy
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 12
 */
declare function accessSync(path: string, mode: AccessModeType, flag: AccessFlagType): boolean;
/**
 * Closes a file or directory. This API uses a promise to return the result.
 *
 * @param { number | File } file - **File** object or FD of the file to close. Once closed, the **File** object or FD
 *     cannot be used for read or write operations.
 * @returns { Promise<void> } Promise that returns no value.
 * @throws { BusinessError } 13900004 - Interrupted system call
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare function close(file: number | File): Promise<void>;
/**
 * Closes a file or directory. This API uses an asynchronous callback to return the result.
 *
 * @param { number | File } file - **File** object or FD of the file to close. Once closed, the **File** object or FD
 *     cannot be used for read or write operations.
 * @param { AsyncCallback<void> } callback - Callback used to return the result.
 * @throws { BusinessError } 13900004 - Interrupted system call
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare function close(file: number | File, callback: AsyncCallback<void>): void;
/**
 * Closes a file or directory. This API returns the result synchronously.
 *
 * @param { number | File } file - **File** object or FD of the file to close. Once closed, the **File** object or FD
 *     cannot be used for read or write operations.
 * @throws { BusinessError } 13900004 - Interrupted system call
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare function closeSync(file: number | File): void;
/**
 * Copies a file or directory. This API uses a promise to return the result.
 *
 * File copy across devices is supported. This API forcibly overwrites the file or directory. The input parameter can be
 * the URI of the file or directory.
 *
 * A maximum of 10 cross-device copy tasks are allowed at the same time, and the number of files to be copied at a time
 * cannot exceed 500.
 *
 * @param { string } srcUri - URI of the file or directory to copy.
 * @param { string } destUri - URI of the destination file or directory.
 * @param { CopyOptions } [options] - Callback invoked to provide the copy progress. If this parameter is not set, the
 *     callback will not be invoked.
 * @returns { Promise<void> } Promise that returns no value.
 * @throws { BusinessError } 401 - Parameter error. Possible causes:1.Mandatory parameters are left unspecified;
 *     <br>2.Incorrect parameter types.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900004 - Interrupted system call
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900010 - Try again
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied by the file system
 * @throws { BusinessError } 13900015 - File exists
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900021 - File table overflow
 * @throws { BusinessError } 13900022 - Too many open files
 * @throws { BusinessError } 13900024 - File too large
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900028 - Too many links
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900031 - Function not implemented
 * @throws { BusinessError } 13900034 - Operation would block
 * @throws { BusinessError } 13900038 - Value too large for defined data type
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @throws { BusinessError } 13900044 - Network is unreachable [since 12]
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 11
 */
declare function copy(srcUri: string, destUri: string, options?: CopyOptions): Promise<void>;
/**
 * Copies a file or directory. This API uses an asynchronous callback to return the result.
 *
 * File copy across devices is supported. This API forcibly overwrites the file or directory.
 * The input parameter can be the URI of the file or directory. A maximum of 10 cross-device copy tasks
 * are allowed at the same time, and the number of files to be copied at a time cannot exceed 500.
 *
 * @param { string } srcUri - URI of the file or directory to copy.
 * @param { string } destUri - URI of the destination file or directory.
 * @param { AsyncCallback<void> } callback - Callback used to return the result.
 * @throws { BusinessError } 401 - Parameter error. Possible causes:1.Mandatory parameters are left unspecified;
 *     <br>2.Incorrect parameter types.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900004 - Interrupted system call
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900010 - Try again
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied by the file system
 * @throws { BusinessError } 13900015 - File exists
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900021 - File table overflow
 * @throws { BusinessError } 13900022 - Too many open files
 * @throws { BusinessError } 13900024 - File too large
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900028 - Too many links
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900031 - Function not implemented
 * @throws { BusinessError } 13900034 - Operation would block
 * @throws { BusinessError } 13900038 - Value too large for defined data type
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 11
 */
declare function copy(srcUri: string, destUri: string, callback: AsyncCallback<void>): void;
/**
 * Copies a file or directory. This API uses an asynchronous callback to return the result.
 *
 * File copy across devices is supported. This API forcibly overwrites the file or directory.
 * The input parameter can be the URI of the file or directory. A maximum of 10 cross-device copy tasks
 * are allowed at the same time, and the number of files to be copied at a time cannot exceed 500.
 *
 * @param { string } srcUri - URI of the file or directory to copy.
 * @param { string } destUri - URI of the destination file or directory.
 * @param { CopyOptions } options - Callback used to return the copy progress.
 * @param { AsyncCallback<void> } callback - Callback used to return the result.
 * @throws { BusinessError } 401 - Parameter error. Possible causes:1.Mandatory parameters are left unspecified;
 *     <br>2.Incorrect parameter types.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900004 - Interrupted system call
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900010 - Try again
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied by the file system
 * @throws { BusinessError } 13900015 - File exists
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900021 - File table overflow
 * @throws { BusinessError } 13900022 - Too many open files
 * @throws { BusinessError } 13900024 - File too large
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900028 - Too many links
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900031 - Function not implemented
 * @throws { BusinessError } 13900034 - Operation would block
 * @throws { BusinessError } 13900038 - Value too large for defined data type
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 11
 */
declare function copy(srcUri: string, destUri: string, options: CopyOptions, callback: AsyncCallback<void>): void;
/**
 * Copies the source directory to the destination path. This API uses a promise to return the result.
 *
 * @param { string } src - Application sandbox path of the source directory.
 * @param { string } dest - Application sandbox path of the destination directory.
 * @param { number } [mode] - Copy mode. The default value is **0**.<br>- **0**: Throw an exception if a file conflict
 *     occurs.<br> An exception will be thrown if the destination directory contains a directory with the same name as
 *     the source directory, and a file with the same name exists in the conflict directory. All the non-conflicting
 *     files in the source directory will be moved to the destination directory, and the non-conflicting files in the
 *     destination directory will be retained. The data attribute in the error returned provides information about the
 *     conflicting files in the Array<[ConflictFiles]{@link ConflictFiles}> format.<br>- **1**: Forcibly overwrite the
 *     files with the same name in the destination directory.<br> When the destination directory contains a directory
 *     with the same name as the source directory, the files with the same names in the destination directory are
 *     overwritten forcibly; the files without conflicts in the destination directory are retained.
 * @returns { Promise<void> } Promise that returns no value.
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900004 - Interrupted system call
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900010 - Try again
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900031 - Function not implemented
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900034 - Operation would block
 * @throws { BusinessError } 13900038 - Value too large for defined data type
 * @throws { BusinessError } 13900042 - Unknown error
 * @throws { BusinessError } 13900044 - Network is unreachable [since 12]
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @since 10
 */
declare function copyDir(src: string, dest: string, mode?: number): Promise<void>;
/**
 * Copies the source directory to the destination directory.
 * This API uses an asynchronous callback to return the result.
 *
 * @param { string } src - Application sandbox path of the source directory.
 * @param { string } dest - Application sandbox path of the destination directory.
 * @param { AsyncCallback<void> } callback - Callback used to return the result.
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900004 - Interrupted system call
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900010 - Try again
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900031 - Function not implemented
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900034 - Operation would block
 * @throws { BusinessError } 13900038 - Value too large for defined data type
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @since 10
 */
declare function copyDir(src: string, dest: string, callback: AsyncCallback<void>): void;
/**
 * Copies the source directory to the destination path. This API uses an asynchronous callback to return the result.
 *
 * An exception will be thrown if the destination directory contains a directory with the same name as the source
 * directory and there are files with the same name in the conflicting directory. All the non-conflicting files in the
 * source directory will be moved to the destination directory, and the non-conflicting files in the destination
 * directory will be retained. The data attribute in the error returned provides information about the conflicting files
 * in the Array\<[ConflictFiles]{@link ConflictFiles}> format.
 *
 * @param { string } src - Application sandbox path of the source directory.
 * @param { string } dest - Application sandbox path of the destination directory.
 * @param { AsyncCallback<void, Array<ConflictFiles>> } callback - Callback used to return the result.
 * @throws { BusinessError } 13900015 - File exists
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @since 10
 */
declare function copyDir(src: string, dest: string, callback: AsyncCallback<void, Array<ConflictFiles>>): void;
/**
 * Copies the source directory to the destination directory. You can set the copy mode.
 * This API uses an asynchronous callback to return the result.
 *
 * @param { string } src - Application sandbox path of the source directory.
 * @param { string } dest - Application sandbox path of the destination directory.
 * @param { number } mode - Copy mode. The default value is 0.
 *     <br>0: Throw an exception if a file conflict occurs.
 *     <br>An exception will be thrown if the destination directory contains a directory with
 *     <br>the same name as the source directory, and a file with the same name exists in the conflict directory.
 *     <br>All the non-conflicting files in the source directory will be moved
 *     <br>to the destination directory, and the non-conflicting files in the destination directory will be retained.
 *     <br>The data attribute in the error returned provides information about the
 *     <br>conflicting files in the Array<ConflictFiles> format.
 *     <br>1: Forcibly overwrite the files with the same name in the destination directory.
 *     <br>When the destination directory contains a directory with the same name as the source directory,
 *     <br>the files with the same names in the destination directory are overwritten forcibly;
 *     <br>the files without conflicts in the destination directory are retained.
 * @param { AsyncCallback<void> } callback - Callback used to return the result.
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900004 - Interrupted system call
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900010 - Try again
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900031 - Function not implemented
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900034 - Operation would block
 * @throws { BusinessError } 13900038 - Value too large for defined data type
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @since 10
 */
declare function copyDir(src: string, dest: string, mode: number, callback: AsyncCallback<void>): void;
/**
 * Copies the source directory to the destination path. You can set the copy mode. This API uses an asynchronous
 * callback to return the result.
 *
 * @param { string } src - Application sandbox path of the source directory.
 * @param { string } dest - Application sandbox path of the destination directory.
 * @param { number } mode - Copy mode. The default value is **0**.<br>- **0**: Throw an exception if a file conflict
 *     occurs.<br> An exception will be thrown if the destination directory contains a directory with the same name as
 *     the source directory, and a file with the same name exists in the conflict directory. All the non-conflicting
 *     files in the source directory will be moved to the destination directory, and the non-conflicting files in the
 *     destination directory will be retained. The data attribute in the error returned provides information about the
 *     conflicting files in the Array<[ConflictFiles]{@link ConflictFiles}> format.<br>- **1**: Forcibly overwrite the
 *     files with the same name in the destination directory.<br> When the destination directory contains a directory
 *     with the same name as the source directory, the files with the same names in the destination directory are
 *     overwritten forcibly; the files without conflicts in the destination directory are retained.
 * @param { AsyncCallback<void, Array<ConflictFiles>> } callback - Callback used to return the result.
 * @throws { BusinessError } 13900015 - File exists
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @since 10
 */
declare function copyDir(src: string, dest: string, mode: number, callback: AsyncCallback<void, Array<ConflictFiles>>): void;
/**
 * Copies the source directory to the destination path. This API returns the result synchronously.
 *
 * @param { string } src - Application sandbox path of the source directory.
 * @param { string } dest - Application sandbox path of the destination directory.
 * @param { number } [mode] - Copy mode. The default value is **0**.<br>- **0**: Throw an exception if a file conflict
 *     occurs.<br> An exception will be thrown if the destination directory contains a directory with the same name as
 *     the source directory, and a file with the same name exists in the conflict directory. All the non-conflicting
 *     files in the source directory will be moved to the destination directory, and the non-conflicting files in the
 *     destination directory will be retained. The data attribute in the error returned provides information about the
 *     conflicting files in the Array<[ConflictFiles]{@link ConflictFiles}> format.<br>- **1**: Forcibly overwrite the
 *     files with the same name in the destination directory.<br> When the destination directory contains a directory
 *     with the same name as the source directory, the files with the same names in the destination directory are
 *     overwritten forcibly; the files without conflicts in the destination directory are retained.
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900004 - Interrupted system call
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900010 - Try again
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900015 - File exists
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900031 - Function not implemented
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900034 - Operation would block
 * @throws { BusinessError } 13900038 - Value too large for defined data type
 * @throws { BusinessError } 13900042 - Unknown error
 * @throws { BusinessError } 13900044 - Network is unreachable [since 12]
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @since 10
 */
declare function copyDirSync(src: string, dest: string, mode?: number): void;
/**
 * Copies a file. This API uses a promise to return the result.
 *
 * @param { string | number } src - Path or FD of the file to copy.
 * @param { string | number } dest - Destination path of the file or FD of the file created.
 * @param { number } [mode] - Whether to overwrite the file with the same name in the destination directory. The default
 *     value is **0**, which is the only value supported.<br>**0**: overwrite the file with the same name and truncate
 *     the part that is not overwritten.
 * @returns { Promise<void> } Promise that returns no value.
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900004 - Interrupted system call
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900010 - Try again
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900031 - Function not implemented
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900034 - Operation would block
 * @throws { BusinessError } 13900038 - Value too large for defined data type
 * @throws { BusinessError } 13900042 - Unknown error
 * @throws { BusinessError } 13900044 - Network is unreachable [since 12]
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare function copyFile(src: string | number, dest: string | number, mode?: number): Promise<void>;
/**
 * Copies a file. This API overwrites the file with the same name in the destination directory and truncates the part
 * that is not overwritten. This API uses an asynchronous callback to return the result.
 *
 * @param { string | number } src - Path or FD of the file to copy.
 * @param { string | number } dest - Destination path of the file or FD of the file created.
 * @param { AsyncCallback<void> } callback - Callback invoked immediately after the file is copied.
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900004 - Interrupted system call
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900010 - Try again
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900031 - Function not implemented
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900034 - Operation would block
 * @throws { BusinessError } 13900038 - Value too large for defined data type
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare function copyFile(src: string | number, dest: string | number, callback: AsyncCallback<void>): void;
/**
 * Copies a file with the specified mode. This API uses an asynchronous callback to return the result.
 *
 * @param { string | number } src - Path or FD of the file to copy.
 * @param { string | number } dest - Destination path of the file or FD of the file created.
 * @param { number } [mode] - Whether to overwrite the file with the same name in the destination directory. The default
 *     value is **0**, which is the only value supported.<br>**0**: overwrite the file with the same name and truncate
 *     the part that is not overwritten.
 * @param { AsyncCallback<void> } callback - Callback invoked immediately after the file is copied.
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900004 - Interrupted system call
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900010 - Try again
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900031 - Function not implemented
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900034 - Operation would block
 * @throws { BusinessError } 13900038 - Value too large for defined data type
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare function copyFile(src: string | number, dest: string | number, mode: number, callback: AsyncCallback<void>): void;
/**
 * Copies a file. This API returns the result synchronously.
 *
 * @param { string | number } src - Path or FD of the file to copy.
 * @param { string | number } dest - Destination path of the file or FD of the file created.
 * @param { number } [mode] - Whether to overwrite the file with the same name in the destination directory. The default
 *     value is **0**, which is the only value supported.<br>**0**: overwrite the file with the same name and truncate
 *     the part that is not overwritten.
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900004 - Interrupted system call
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900010 - Try again
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900031 - Function not implemented
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900034 - Operation would block
 * @throws { BusinessError } 13900038 - Value too large for defined data type
 * @throws { BusinessError } 13900042 - Unknown error
 * @throws { BusinessError } 13900044 - Network is unreachable [since 12]
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare function copyFileSync(src: string | number, dest: string | number, mode?: number): void;
/**
 * Creates a stream based on a file path. This API uses a promise to return the result. To close the stream, use
 * **close()** of [Stream]{@link Stream}.
 *
 * @param { string } path - Application sandbox path of the file.
 * @param { string } mode - - **r**: Open a file for reading. The file must exist.<br>- **r+**: Open a file for both
 *     reading and writing. The file must exist.<br>- **w**: Open a file for writing. If the file exists, clear its
 *     content. If the file does not exist, create a file.<br>- **w+**: Open a file for both reading and writing. If the
 *     file exists, clear its content. If the file does not exist, create a file.<br>- **a**: Open a file in append mode
 *     for writing at the end of the file. If the file does not exist, create a file. If the file exists, write data to
 *     the end of the file (the original content of the file is reserved).<br>- **a+**: Open a file in append mode for
 *     reading or updating at the end of the file. If the file does not exist, create a file. If the file exists, write
 *     data to the end of the file (the original content of the file is reserved).
 * @returns { Promise<Stream> } Promise used to return the file stream.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900004 - Interrupted system call
 * @throws { BusinessError } 13900006 - No such device or address
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900014 - Device or resource busy
 * @throws { BusinessError } 13900015 - File exists
 * @throws { BusinessError } 13900017 - No such device
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900022 - Too many open files
 * @throws { BusinessError } 13900023 - Text file busy
 * @throws { BusinessError } 13900024 - File too large
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900029 - Resource deadlock would occur
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900034 - Operation would block
 * @throws { BusinessError } 13900038 - Value too large for defined data type
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @throws { BusinessError } 13900044 - Network is unreachable [since 12]
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @atomicservice [since 20]
 * @since 9
 */
declare function createStream(path: string, mode: string): Promise<Stream>;
/**
 * Creates a stream based on a file path. This API uses an asynchronous callback to return the result. To close the
 * stream, use **close()** of [Stream]{@link Stream}.
 *
 * @param { string } path - Application sandbox path of the file.
 * @param { string } mode - - **r**: Open a file for reading. The file must exist.<br>- **r+**: Open a file for both
 *     reading and writing. The file must exist.<br>- **w**: Open a file for writing. If the file exists, clear its
 *     content. If the file does not exist, create a file.<br>- **w+**: Open a file for both reading and writing. If the
 *     file exists, clear its content. If the file does not exist, create a file.<br>- **a**: Open a file in append mode
 *     for writing at the end of the file. If the file does not exist, create a file. If the file exists, write data to
 *     the end of the file (the original content of the file is reserved).<br>- **a+**: Open a file in append mode for
 *     reading or updating at the end of the file. If the file does not exist, create a file. If the file exists, write
 *     data to the end of the file (the original content of the file is reserved).
 * @param { AsyncCallback<Stream> } callback - Callback used to return the result.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900004 - Interrupted system call
 * @throws { BusinessError } 13900006 - No such device or address
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900014 - Device or resource busy
 * @throws { BusinessError } 13900015 - File exists
 * @throws { BusinessError } 13900017 - No such device
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900022 - Too many open files
 * @throws { BusinessError } 13900023 - Text file busy
 * @throws { BusinessError } 13900024 - File too large
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900029 - Resource deadlock would occur
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900034 - Operation would block
 * @throws { BusinessError } 13900038 - Value too large for defined data type
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @atomicservice [since 20]
 * @since 9
 */
declare function createStream(path: string, mode: string, callback: AsyncCallback<Stream>): void;
/**
 * Creates a stream based on a file path. This API returns the result synchronously. To close the stream, use
 * **close()** of [Stream]{@link Stream}.
 *
 * @param { string } path - Application sandbox path of the file.
 * @param { string } mode - - **r**: Open a file for reading. The file must exist.<br>- **r+**: Open a file for both
 *     reading and writing. The file must exist.<br>- **w**: Open a file for writing. If the file exists, clear its
 *     content. If the file does not exist, create a file.<br>- **w+**: Open a file for both reading and writing. If the
 *     file exists, clear its content. If the file does not exist, create a file.<br>- **a**: Open a file in append mode
 *     for writing at the end of the file. If the file does not exist, create a file. If the file exists, write data to
 *     the end of the file (the original content of the file is reserved).<br>- **a+**: Open a file in append mode for
 *     reading or updating at the end of the file. If the file does not exist, create a file. If the file exists, write
 *     data to the end of the file (the original content of the file is reserved).
 * @returns { Stream } File stream.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900004 - Interrupted system call
 * @throws { BusinessError } 13900006 - No such device or address
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900014 - Device or resource busy
 * @throws { BusinessError } 13900015 - File exists
 * @throws { BusinessError } 13900017 - No such device
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900022 - Too many open files
 * @throws { BusinessError } 13900023 - Text file busy
 * @throws { BusinessError } 13900024 - File too large
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900029 - Resource deadlock would occur
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900034 - Operation would block
 * @throws { BusinessError } 13900038 - Value too large for defined data type
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @throws { BusinessError } 13900044 - Network is unreachable [since 12]
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @atomicservice [since 20]
 * @since 9
 */
declare function createStreamSync(path: string, mode: string): Stream;
/**
 * Creates a **RandomAccessFile** instance based on the specified file path or file object. This API uses a promise to
 * return the result.
 *
 * @param { string | File } file - Application sandbox path of the file or an opened file object.
 * @param { number } [mode] - [Mode](docroot://reference/apis-core-file-kit/js-apis-file-fs.md#openmode) for creating
 *     the **RandomAccessFile** instance. This parameter is valid only when the application sandbox path of the file is
 *     passed in. One of the following options must be specified:<br>- **OpenMode.READ_ONLY(0o0)**: Create the file in
 *     read-only mode. This is the default value.<br>- **OpenMode.WRITE_ONLY(0o1)**: Create the file in write-only mode.
 *     <br>- **OpenMode.READ_WRITE(0o2)**: Create the file in read/write mode.<br>You can also specify the following
 *     options, separated by a bitwise OR operator (|). By default, no additional options are given.<br>-
 *     **OpenMode.CREATE(0o100)**: If the file does not exist, create it.<br>- **OpenMode.TRUNC(0o1000)**: If the
 *     **RandomAccessFile** object already exists and is created in write mode, truncate the file length to 0.<br>-
 *     **OpenMode.APPEND(0o2000)**: Create the file in append mode. New data will be added to the end of the
 *     **RandomAccessFile** object. <br>- **OpenMode.NONBLOCK(0o4000)**: If **path** points to a named pipe (also known
 *     as a FIFO), block special file, or character special file, perform non-blocking operations on the opened file and
 *     in subsequent I/Os.<br>- **OpenMode.DIR(0o200000)**: If **path** does not point to a directory, throw an
 *     exception. The write permission is not allowed.<br>- **OpenMode.NOFOLLOW(0o400000)**: If **path** points to a
 *     symbolic link, throw an exception.<br>- **OpenMode.SYNC(0o4010000)**: Create a **RandomAccessFile** instance in
 *     synchronous I/O mode.
 * @param { RandomAccessFileOptions } [options] - The options are as follows:<br>- **start** (number): start position to
 *     read data, in bytes. This parameter is optional. By default, data is read from the current position.<br>- **end**
 *     (number): end position to read data, in bytes. This parameter is optional. The default value is the end of the
 *     file.<br>This parameter takes effect only for file stream objects obtained by
 *     [getreadstream]{@link RandomAccessFile.getReadStream} and [getwritestream]{@link RandomAccessFile.getWriteStream}
 *     . [since 12]
 * @returns { Promise<RandomAccessFile> } Promise used to return the **RandomAccessFile** instance created.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900004 - Interrupted system call
 * @throws { BusinessError } 13900006 - No such device or address
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900014 - Device or resource busy
 * @throws { BusinessError } 13900015 - File exists
 * @throws { BusinessError } 13900017 - No such device
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900022 - Too many open files
 * @throws { BusinessError } 13900023 - Text file busy
 * @throws { BusinessError } 13900024 - File too large
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900029 - Resource deadlock would occur
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900034 - Operation would block
 * @throws { BusinessError } 13900038 - Value too large for defined data type
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @throws { BusinessError } 13900044 - Network is unreachable [since 12]
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @since 10
 */
declare function createRandomAccessFile(file: string | File, mode?: number, options?: RandomAccessFileOptions): Promise<RandomAccessFile>;
/**
 * Creates a **RandomAccessFile** object in read-only mode based on a file path or file object. This API uses an
 * asynchronous callback to return the result.
 *
 * @param { string | File } file - Application sandbox path of the file or an opened file object.
 * @param { AsyncCallback<RandomAccessFile> } callback - Callback used to return the **RandomAccessFile** instance
 *     created.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900004 - Interrupted system call
 * @throws { BusinessError } 13900006 - No such device or address
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900014 - Device or resource busy
 * @throws { BusinessError } 13900015 - File exists
 * @throws { BusinessError } 13900017 - No such device
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900022 - Too many open files
 * @throws { BusinessError } 13900023 - Text file busy
 * @throws { BusinessError } 13900024 - File too large
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900029 - Resource deadlock would occur
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900034 - Operation would block
 * @throws { BusinessError } 13900038 - Value too large for defined data type
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @since 10
 */
declare function createRandomAccessFile(file: string | File, callback: AsyncCallback<RandomAccessFile>): void;
/**
 * Creates a **RandomAccessFile** instance based on a file path or file object. This API uses an asynchronous callback
 * to return the result.
 *
 * @param { string | File } file - Application sandbox path of the file or an opened file object.
 * @param { number } [mode] - [Mode](docroot://reference/apis-core-file-kit/js-apis-file-fs.md#openmode) for creating
 *     the **RandomAccessFile** instance. This parameter is valid only when the application sandbox path of the file is
 *     passed in. One of the following options must be specified:<br>- **OpenMode.READ_ONLY(0o0)**: Create the file in
 *     read-only mode. This is the default value.<br>- **OpenMode.WRITE_ONLY(0o1)**: Create the file in write-only mode.
 *     <br>- **OpenMode.READ_WRITE(0o2)**: Create the file in read/write mode.<br>You can also specify the following
 *     options, separated by a bitwise OR operator (|). By default, no additional options are given.<br>-
 *     **OpenMode.CREATE(0o100)**: If the file does not exist, create it.<br>- **OpenMode.TRUNC(0o1000)**: If the
 *     **RandomAccessFile** object already exists and is created in write mode, truncate the file length to 0.<br>-
 *     **OpenMode.APPEND(0o2000)**: Create the file in append mode. New data will be added to the end of the
 *     **RandomAccessFile** object. <br>- **OpenMode.NONBLOCK(0o4000)**: If **path** points to a named pipe (also known
 *     as a FIFO), block special file, or character special file, perform non-blocking operations on the opened file and
 *     in subsequent I/Os.<br>- **OpenMode.DIR(0o200000)**: If **path** does not point to a directory, throw an
 *     exception. The write permission is not allowed.<br>- **OpenMode.NOFOLLOW(0o400000)**: If **path** points to a
 *     symbolic link, throw an exception.<br>- **OpenMode.SYNC(0o4010000)**: Create a **RandomAccessFile** instance in
 *     synchronous I/O mode.
 * @param { AsyncCallback<RandomAccessFile> } callback - Callback used to return the **RandomAccessFile** instance
 *     created.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900004 - Interrupted system call
 * @throws { BusinessError } 13900006 - No such device or address
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900014 - Device or resource busy
 * @throws { BusinessError } 13900015 - File exists
 * @throws { BusinessError } 13900017 - No such device
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900022 - Too many open files
 * @throws { BusinessError } 13900023 - Text file busy
 * @throws { BusinessError } 13900024 - File too large
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900029 - Resource deadlock would occur
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900034 - Operation would block
 * @throws { BusinessError } 13900038 - Value too large for defined data type
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @since 10
 */
declare function createRandomAccessFile(file: string | File, mode: number, callback: AsyncCallback<RandomAccessFile>): void;
/**
 * Creates a **RandomAccessFile** instance based on a file path or file object.
 *
 * @param { string | File } file - Application sandbox path of the file or an opened file object.
 * @param { number } [mode] - [Mode](docroot://reference/apis-core-file-kit/js-apis-file-fs.md#openmode) for creating
 *     the **RandomAccessFile** instance. This parameter is valid only when the application sandbox path of the file is
 *     passed in. One of the following options must be specified:<br>- **OpenMode.READ_ONLY(0o0)**: Create the file in
 *     read-only mode. This is the default value.<br>- **OpenMode.WRITE_ONLY(0o1)**: Create the file in write-only mode.
 *     <br>- **OpenMode.READ_WRITE(0o2)**: Create the file in read/write mode.<br>You can also specify the following
 *     options, separated by a bitwise OR operator (|). By default, no additional options are given.<br>-
 *     **OpenMode.CREATE(0o100)**: If the file does not exist, create it.<br>- **OpenMode.TRUNC(0o1000)**: If the
 *     **RandomAccessFile** object already exists and is created in write mode, truncate the file length to 0.<br>-
 *     **OpenMode.APPEND(0o2000)**: Create the file in append mode. New data will be added to the end of the
 *     **RandomAccessFile** object. <br>- **OpenMode.NONBLOCK(0o4000)**: If **path** points to a named pipe (also known
 *     as a FIFO), block special file, or character special file, perform non-blocking operations on the opened file and
 *     in subsequent I/Os.<br>- **OpenMode.DIR(0o200000)**: If **path** does not point to a directory, throw an
 *     exception. The write permission is not allowed.<br>- **OpenMode.NOFOLLOW(0o400000)**: If **path** points to a
 *     symbolic link, throw an exception.<br>- **OpenMode.SYNC(0o4010000)**: Create a **RandomAccessFile** instance in
 *     synchronous I/O mode.
 * @param { RandomAccessFileOptions } [options] - The options are as follows:<br>- **start** (number): start position to
 *     read data, in bytes. This parameter is optional. By default, data is read from the current position.<br>- **end**
 *     (number): end position to read data, in bytes. This parameter is optional. The default value is the end of the
 *     file.<br>This parameter takes effect only for file stream objects obtained by
 *     [getreadstream]{@link RandomAccessFile.getReadStream} and [getwritestream]{@link RandomAccessFile.getWriteStream}
 *     . [since 12]
 * @returns { RandomAccessFile } **RandomAccessFile** instance created.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900004 - Interrupted system call
 * @throws { BusinessError } 13900006 - No such device or address
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900014 - Device or resource busy
 * @throws { BusinessError } 13900015 - File exists
 * @throws { BusinessError } 13900017 - No such device
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900022 - Too many open files
 * @throws { BusinessError } 13900023 - Text file busy
 * @throws { BusinessError } 13900024 - File too large
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900029 - Resource deadlock would occur
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900034 - Operation would block
 * @throws { BusinessError } 13900038 - Value too large for defined data type
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @throws { BusinessError } 13900044 - Network is unreachable [since 12]
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @since 10
 */
declare function createRandomAccessFileSync(file: string | File, mode?: number, options?: RandomAccessFileOptions): RandomAccessFile;
/**
 * Creates a readable stream. This API returns the result synchronously.
 *
 * @param { string } path - Path of the file.
 * @param { ReadStreamOptions } [options] - The options are as follows:<br>- **start** (number): start position to read
 *     data, in bytes. This parameter is optional. By default, data is read from the current position.<br>- **end** (
 *     number): end position to read data, in bytes. This parameter is optional. The default value is the end of the
 *     file.
 * @returns { ReadStream } **ReadStream** instance obtained.
 * @throws { BusinessError } 401 - Parameter error
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900004 - Interrupted system call
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900017 - No such device
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900022 - Too many open files
 * @throws { BusinessError } 13900024 - File too large
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900038 - Value too large for defined data type
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @throws { BusinessError } 13900044 - Network is unreachable
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @since 12
 */
declare function createReadStream(path: string, options?: ReadStreamOptions): ReadStream;
/**
 * Creates a writeable stream. This API returns the result synchronously.
 *
 * @param { string } path - Path of the file.
 * @param { WriteStreamOptions } [options] - The options are as follows:<br>- **start** (number): start position to
 *     write the data, in bytes. This parameter is optional. By default, data is written from the current position.<br>-
 *     **mode** (number): [mode](docroot://reference/apis-core-file-kit/js-apis-file-fs.md#openmode) for creating the
 *     writeable stream. This parameter is optional. The default value is the write-only mode.
 * @returns { WriteStream } **WriteStream** instance obtained.
 * @throws { BusinessError } 401 - Parameter error
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900004 - Interrupted system call
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900015 - File exists
 * @throws { BusinessError } 13900017 - No such device
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900022 - Too many open files
 * @throws { BusinessError } 13900024 - File too large
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900038 - Value too large for defined data type
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @since 12
 */
declare function createWriteStream(path: string, options?: WriteStreamOptions): WriteStream;
/**
 * Creates a **Watcher** object to listen for file or directory changes.
 *
 * @param { string } path - Application sandbox path of the file or directory to observe.
 * @param { number } events - Events to observe. Multiple events can be separated by vertical bars (
 * @param { WatchEventListener } listener - Callback invoked when an observed event occurs. The callback will be invoked
 *     each time an observed event occurs.
 * @returns { Watcher } **Watcher** object created.
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900015 - File exists
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900021 - File table overflow
 * @throws { BusinessError } 13900022 - Too many open files
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @since 10
 */
declare function createWatcher(path: string, events: number, listener: WatchEventListener): Watcher;
/**
 * Duplicates the file descriptor and returns the corresponding **File** object.
 *
 * @param { number } fd - File descriptor.
 * @returns { File } File object opened.
 * @throws { BusinessError } 13900004 - Interrupted system call
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900014 - Device or resource busy
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900022 - Too many open files
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 10
 */
declare function dup(fd: number): File;
/**
 * Synchronizes the data of a file. This API uses a promise to return the result.
 *
 * @param { number } fd - FD of the file.
 * @returns { Promise<void> } Promise that returns no value.
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @since 9
 */
declare function fdatasync(fd: number): Promise<void>;
/**
 * Synchronizes the data of a file. This API uses an asynchronous callback to return the result.
 *
 * @param { number } fd - FD of the file.
 * @param { AsyncCallback<void> } callback - Callback used to return the result.
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @since 9
 */
declare function fdatasync(fd: number, callback: AsyncCallback<void>): void;
/**
 * Synchronizes the data of a file. This API returns the result synchronously.
 *
 * @param { number } fd - FD of the file.
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @since 9
 */
declare function fdatasyncSync(fd: number): void;
/**
 * Opens a stream based on an FD. This API uses a promise to return the result. To close the stream, use **close()** of
 * [Stream]{@link Stream}.
 *
 * @param { number } fd - FD of the file.
 * @param { string } mode - - **r**: Open a file for reading. The file must exist.<br>- **r+**: Open a file for both
 *     reading and writing. The file must exist.<br>- **w**: Open a file for writing. If the file exists, clear its
 *     content. If the file does not exist, create a file.<br>- **w+**: Open a file for both reading and writing. If the
 *     file exists, clear its content. If the file does not exist, create a file.<br>- **a**: Open a file in append mode
 *     for writing at the end of the file. If the file does not exist, create a file. If the file exists, write data to
 *     the end of the file (the original content of the file is reserved).<br>- **a+**: Open a file in append mode for
 *     reading or updating at the end of the file. If the file does not exist, create a file. If the file exists, write
 *     data to the end of the file (the original content of the file is reserved).
 * @returns { Promise<Stream> } Promise used to return the file stream.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900004 - Interrupted system call
 * @throws { BusinessError } 13900006 - No such device or address
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900010 - Try again
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900014 - Device or resource busy
 * @throws { BusinessError } 13900015 - File exists
 * @throws { BusinessError } 13900017 - No such device
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900022 - Too many open files
 * @throws { BusinessError } 13900023 - Text file busy
 * @throws { BusinessError } 13900024 - File too large
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900029 - Resource deadlock would occur
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900034 - Operation would block
 * @throws { BusinessError } 13900038 - Value too large for defined data type
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @atomicservice [since 20]
 * @since 9
 */
declare function fdopenStream(fd: number, mode: string): Promise<Stream>;
/**
 * Opens a stream based on an FD. This API uses an asynchronous callback to return the result. To close the stream, use
 * **close()** of [Stream]{@link Stream}.
 *
 * @param { number } fd - FD of the file.
 * @param { string } mode - - **r**: Open a file for reading. The file must exist.<br>- **r+**: Open a file for both
 *     reading and writing. The file must exist.<br>- **w**: Open a file for writing. If the file exists, clear its
 *     content. If the file does not exist, create a file.<br>- **w+**: Open a file for both reading and writing. If the
 *     file exists, clear its content. If the file does not exist, create a file.<br>- **a**: Open a file in append mode
 *     for writing at the end of the file. If the file does not exist, create a file. If the file exists, write data to
 *     the end of the file (the original content of the file is reserved).<br>- **a+**: Open a file in append mode for
 *     reading or updating at the end of the file. If the file does not exist, create a file. If the file exists, write
 *     data to the end of the file (the original content of the file is reserved).
 * @param { AsyncCallback<Stream> } callback - Callback used to return the result.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900004 - Interrupted system call
 * @throws { BusinessError } 13900006 - No such device or address
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900010 - Try again
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900014 - Device or resource busy
 * @throws { BusinessError } 13900015 - File exists
 * @throws { BusinessError } 13900017 - No such device
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900022 - Too many open files
 * @throws { BusinessError } 13900023 - Text file busy
 * @throws { BusinessError } 13900024 - File too large
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900029 - Resource deadlock would occur
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900034 - Operation would block
 * @throws { BusinessError } 13900038 - Value too large for defined data type
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @atomicservice [since 20]
 * @since 9
 */
declare function fdopenStream(fd: number, mode: string, callback: AsyncCallback<Stream>): void;
/**
 * Opens a stream based on an FD. This API returns the result synchronously. To close the stream, use **close()** of
 * [Stream]{@link Stream}.
 *
 * @param { number } fd - FD of the file.
 * @param { string } mode - - **r**: Open a file for reading. The file must exist.<br>- **r+**: Open a file for both
 *     reading and writing. The file must exist.<br>- **w**: Open a file for writing. If the file exists, clear its
 *     content. If the file does not exist, create a file.<br>- **w+**: Open a file for both reading and writing. If the
 *     file exists, clear its content. If the file does not exist, create a file.<br>- **a**: Open a file in append mode
 *     for writing at the end of the file. If the file does not exist, create a file. If the file exists, write data to
 *     the end of the file (the original content of the file is reserved).<br>- **a+**: Open a file in append mode for
 *     reading or updating at the end of the file. If the file does not exist, create a file. If the file exists, write
 *     data to the end of the file (the original content of the file is reserved).
 * @returns { Stream } File stream.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900004 - Interrupted system call
 * @throws { BusinessError } 13900006 - No such device or address
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900010 - Try again
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900014 - Device or resource busy
 * @throws { BusinessError } 13900015 - File exists
 * @throws { BusinessError } 13900017 - No such device
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900022 - Too many open files
 * @throws { BusinessError } 13900023 - Text file busy
 * @throws { BusinessError } 13900024 - File too large
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900029 - Resource deadlock would occur
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900034 - Operation would block
 * @throws { BusinessError } 13900038 - Value too large for defined data type
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @atomicservice [since 20]
 * @since 9
 */
declare function fdopenStreamSync(fd: number, mode: string): Stream;
/**
 * Synchronizes the cached data of a file to storage. This API uses a promise to return the result.
 *
 * @param { number } fd - FD of the file.
 * @returns { Promise<void> } Promise that returns no value.
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @since 9
 */
declare function fsync(fd: number): Promise<void>;
/**
 * Synchronizes the cached data of a file to storage. This API uses an asynchronous callback to return the result.
 *
 * @param { number } fd - FD of the file.
 * @param { AsyncCallback<void> } callback - Callback used to return the result.
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @since 9
 */
declare function fsync(fd: number, callback: AsyncCallback<void>): void;
/**
 * Synchronizes the cached data of a file to storage. This API returns the result synchronously.
 *
 * @param { number } fd - FD of the file.
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @since 9
 */
declare function fsyncSync(fd: number): void;
/**
 * Lists the names of all files and directories in the current path. Filtering is supported. This API uses a promise to
 * return the result.
 *
 * You can configure the **recursion** parameter in **options** to recursively list the relative paths of all files. The
 * relative path starts with a slash (/).
 *
 * @param { string } path - Application sandbox path of the directory.
 * @param { object } [options] - Options for filtering files. The files are not filtered by default. [since 9 - 10]
 * @param { ListFileOptions } [options] - Options for filtering files. The files are not filtered by default. [since 11]
 * @returns { Promise<string[]> } Promise used to return the file name array, which is encoded in UTF-8 format by
 *     default.
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare function listFile(path: string, options?: ListFileOptions): Promise<string[]>;
/**
 * Lists the names of all files and directories in the current path. Filtering is supported. This API uses an
 * asynchronous callback to return the result.
 *
 * You can configure the **recursion** parameter in **options** to recursively list the relative paths of all files. The
 * relative path starts with a slash (/).
 *
 * @param { string } path - Application sandbox path of the directory.
 * @param { AsyncCallback<string[]> } callback - Callback used to return the file names listed. The files are encoded in
 *     UTF-8 by default.
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare function listFile(path: string, callback: AsyncCallback<string[]>): void;
/**
 * Lists the names of all files and directories in the current path. Filtering is supported. This API uses an
 * asynchronous callback to return the result.
 *
 * You can configure the **recursion** parameter in **options** to recursively list the relative paths of all files. The
 * relative path starts with a slash (/).
 *
 * @param { string } path - Application sandbox path of the directory.
 * @param { object } [options] - Options for filtering files. The files are not filtered by default. [since 9 - 10]
 * @param { ListFileOptions } [options] - Options for filtering files. The files are not filtered by default. [since 11]
 * @param { AsyncCallback<string[]> } callback - Callback used to return the file names listed. The files are encoded in
 *     UTF-8 by default.
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare function listFile(path: string, options: ListFileOptions, callback: AsyncCallback<string[]>): void;
/**
 * Lists the names of all files and directories in the current directory. This API returns the result synchronously.
 * Filtering is supported.
 *
 * You can configure the **recursion** parameter in **options** to recursively list the relative paths of all files. The
 * relative path starts with a slash (/).
 *
 * @param { string } path - Application sandbox path of the directory.
 * @param { object } [options] - Options for filtering files. The files are not filtered by default. [since 9 - 10]
 * @param { ListFileOptions } [options] - Options for filtering files. The files are not filtered by default. [since 11]
 * @returns { string[] } File name array, which is encoded in UTF-8 format by default.
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare function listFileSync(path: string, options?: ListFileOptions): string[];
/**
 * Lists all file names in a directory. This API uses a promise to return the result.
 * This API supports recursive listing of all file names and custom file name filtering.
 * The returned result starts with a slash (/) and contains the subdirectory.
 *
 * @param { string } path - Application sandbox path of the directory.
 * @param { ListFileExtOptions } [options] - Options for filtering files. The files are not filtered by default.
 * @returns { Promise<string[]> } Promise used to return the file names listed.
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @stagemodelonly
 * @since 26.0.0
 */
declare function listFileExt(path: string, options?: ListFileExtOptions): Promise<string[]>;
/**
 * Lists all file names in a directory. This API returns the result synchronously.
 * This API supports recursive listing of all file names and custom file name filtering.
 * The returned result starts with a slash (/) and contains the subdirectory.
 *
 * @param { string } path - Application sandbox path of the directory.
 * @param { ListFileExtOptions } [options] - Options for filtering files. The files are not filtered by default.
 * @returns { string[] } List of the file names obtained.
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @stagemodelonly
 * @since 26.0.0
 */
declare function listFileExtSync(path: string, options?: ListFileExtOptions): string[];
/**
 * Adjusts the position of the file offset pointer.
 *
 * @param { number } fd - File descriptor.
 * @param { number } offset - Relative offset, in bytes.
 * @param { WhenceType } [whence] - Where to start the offset. If this parameter is not specified, the file start
 *     position is used by default.
 * @returns { number } Position of the current offset as measured from the beginning of the file, in bytes.
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900026 - Illegal seek
 * @throws { BusinessError } 13900038 - Value too large for defined data type
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 12]
 * @since 11
 */
declare function lseek(fd: number, offset: number, whence?: WhenceType): number;
/**
 * Obtains information about a symbolic link that is used to refer to a file or directory. This API uses a promise to
 * return the result.
 *
 * @param { string } path - Application sandbox path or URI of the file.<br>**Note**: URIs can be passed since API
 *     version 22.
 * @returns { Promise<Stat> } Promise used to return the symbolic link information obtained. For details, see **Stat**.
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900038 - Value too large for defined data type
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @since 9
 */
declare function lstat(path: string): Promise<Stat>;
/**
 * Obtains information about a symbolic link that is used to refer to a file or directory. This API uses an asynchronous
 * callback to return the result.
 *
 * @param { string } path - Application sandbox path or URI of the file.<br>**Note**: URIs can be passed since API
 *     version 22.
 * @param { AsyncCallback<Stat> } callback - Callback used to return the symbolic link information obtained.
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900038 - Value too large for defined data type
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @since 9
 */
declare function lstat(path: string, callback: AsyncCallback<Stat>): void;
/**
 * Obtains information about a symbolic link that is used to refer to a file or directory. This API returns the result
 * synchronously.
 *
 * @param { string } path - Application sandbox path or URI of the file.<br>**Note**: URIs can be passed since API
 *     version 22.
 * @returns { Stat } File information obtained.
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900038 - Value too large for defined data type
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @since 9
 */
declare function lstatSync(path: string): Stat;
/**
 * Creates a directory. This API uses a promise to return the result.
 *
 * @param { string } path - Application sandbox path of the directory.
 * @returns { Promise<void> } Promise that returns no value.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900015 - File exists
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900028 - Too many links
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare function mkdir(path: string): Promise<void>;
/**
 * Creates a directory. This API uses a promise to return the result. The value **true** means to create a directory
 * recursively.
 *
 * @param { string } path - Application sandbox path of the directory.
 * @param { boolean } recursion - Whether to create a directory recursively.<br> The value **true** means to create a
 *     directory recursively. The value **false** means to create a single-level directory.
 * @returns { Promise<void> } Promise that returns no value.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900015 - File exists
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900028 - Too many links
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @atomicservice
 * @since 11
 */
declare function mkdir(path: string, recursion: boolean): Promise<void>;
/**
 * Creates a directory. This API uses an asynchronous callback to return the result.
 *
 * @param { string } path - Application sandbox path of the directory.
 * @param { AsyncCallback<void> } callback - Callback used to return the result.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900015 - File exists
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900028 - Too many links
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare function mkdir(path: string, callback: AsyncCallback<void>): void;
/**
 * Creates a directory. This API uses an asynchronous callback to return the result. The value **true** means to create
 * a directory recursively.
 *
 * @param { string } path - Application sandbox path of the directory.
 * @param { boolean } recursion - Whether to create a directory recursively.<br> The value **true** means to create a
 *     directory recursively. The value **false** means to create a single-level directory.
 * @param { AsyncCallback<void> } callback - Callback used to return the result.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900015 - File exists
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900028 - Too many links
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @atomicservice
 * @since 11
 */
declare function mkdir(path: string, recursion: boolean, callback: AsyncCallback<void>): void;
/**
 * Creates a directory. This API returns the result synchronously.
 *
 * @param { string } path - Application sandbox path of the directory.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900015 - File exists
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900028 - Too many links
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare function mkdirSync(path: string): void;
/**
 * Creates a directory. This API returns the result synchronously. The value **true** means to create a directory
 * recursively.
 *
 * @param { string } path - Application sandbox path of the directory.
 * @param { boolean } recursion - Whether to create a directory recursively.<br> The value **true** means to create a
 *     directory recursively. The value **false** means to create a single-level directory.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900015 - File exists
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900028 - Too many links
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @atomicservice
 * @since 11
 */
declare function mkdirSync(path: string, recursion: boolean): void;
/**
 * Creates a temporary directory. This API uses a promise to return the result.
 *
 * @param { string } prefix - String to be replaced with six randomly generated characters to create a unique temporary
 *     directory.
 * @returns { Promise<string> } Promise used to return the directory created.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900015 - File exists
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900028 - Too many links
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @since 9
 */
declare function mkdtemp(prefix: string): Promise<string>;
/**
 * Creates a temporary directory. This API uses an asynchronous callback to return the result.
 *
 * @param { string } prefix - String to be replaced with six randomly generated characters to create a unique temporary
 *     directory.
 * @param { AsyncCallback<string> } callback - Callback used to return the result.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900015 - File exists
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900028 - Too many links
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @since 9
 */
declare function mkdtemp(prefix: string, callback: AsyncCallback<string>): void;
/**
 * Creates a temporary directory. This API returns the result synchronously.
 *
 * @param { string } prefix - String to be replaced with six randomly generated characters to create a unique temporary
 *     directory.
 * @returns { string } Unique directory generated.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900015 - File exists
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900028 - Too many links
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @since 9
 */
declare function mkdtempSync(prefix: string): string;
/**
 * Creates a file mapping object based on a file descriptor or file object, using promise asynchronous callback. Maps
 * file contents to memory for efficient read and write access to files.
 * Note: In the read/write mode (MappingMode.READ_WRITE), if the mapping range exceeds the raw file size, the file size
 * will be automatically expanded.
 *
 * @param { number | File } file - File object or open file descriptor fd that has been opened.
 * @param { MappingMode } mode - Option to create a file memory-mapped object. You must specify one of the following
 *     options:
 *     <br>MappingMode.READ_ONLY(0): read-only mode. The file mapping area is not writable. An exception is thrown
 *     when the file mapping area is modified.
 *     <br>MappingMode.READ_WRITE(1): read/write mode. The modification is written to the file mapping area and then
 *     synchronized to the file by the operating system (non-real-time).
 *     <br>MappingMode.PRIVATE(2): private mode. It is a copy-on-write mapping mechanism. Modifications to the mapping
 *     area are visible only to the current process and do not affect the original file.
 * @param { number } offset - Start position of the file mapping area, in bytes.
 * @param { number } size - Size of the file mapping area, in bytes.
 * @returns { Promise<FileMapping> } Promise object. Returns a FileMapping object.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900004 - Interrupted system call
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900010 - Try again
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900015 - File exists
 * @throws { BusinessError } 13900017 - No such device
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900021 - File table overflow
 * @throws { BusinessError } 13900023 - Text file busy
 * @throws { BusinessError } 13900024 - File too large
 * @throws { BusinessError } 13900038 - Value too large for defined data type
 * @throws { BusinessError } 13900050 - Internal resource error
 * @throws { BusinessError } 13900056 - Mmap does not support mapping this file
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @stagemodelonly
 * @since 26.0.0
 */
declare function mmap(file: number | File, mode: MappingMode, offset: number, size: number): Promise<FileMapping>;
/**
 * Creates a file mapping object based on a file descriptor or file object by using the synchronization method. Maps
 * file contents to memory for efficient read and write access to files.
 * Note: In the read/write mode (MappingMode.READ_WRITE), if the mapping range exceeds the raw file size, the file size
 * will be automatically expanded.
 *
 * @param { number | File } file - File object or open file descriptor fd that has been opened.
 * @param { MappingMode } mode - Option to create a file memory-mapped object. You must specify one of the following
 *     options:
 *     <br>MappingMode.READ_ONLY(0): read-only mode. The file mapping area is not writable. An exception is thrown
 *     when the file mapping area is modified.
 *     <br>MappingMode.READ_WRITE(1): read/write mode. The modification is written to the file mapping area and then
 *     synchronized to the file by the operating system (non-real-time).
 *     <br>MappingMode.PRIVATE(2): private mode. It is a copy-on-write mapping mechanism. Modifications to the mapping
 *     area are visible only to the current process and do not affect the original file.
 * @param { number } offset - Start position of the file mapping area, in bytes.
 * @param { number } size - Size of the file mapping area, in bytes.
 * @returns { FileMapping } - FileMapping object.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900004 - Interrupted system call
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900010 - Try again
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900015 - File exists
 * @throws { BusinessError } 13900017 - No such device
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900021 - File table overflow
 * @throws { BusinessError } 13900023 - Text file busy
 * @throws { BusinessError } 13900024 - File too large
 * @throws { BusinessError } 13900038 - Value too large for defined data type
 * @throws { BusinessError } 13900050 - Internal resource error
 * @throws { BusinessError } 13900056 - Mmap does not support mapping this file
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @stagemodelonly
 * @since 26.0.0
 */
declare function mmapSync(file: number | File, mode: MappingMode, offset: number, size: number): FileMapping;
/**
 * Moves the source directory to the destination directory. This API uses a promise to return the result.
 *
 * > **NOTE**
 * >
 * > This API is not supported in a distributed directory.
 *
 * @param { string } src - Application sandbox path of the source directory.
 * @param { string } dest - Application sandbox path of the destination directory.
 * @param { number } [mode] - Move mode. The default value is **0**.<br>- **0**: Throw an exception if a directory
 *     conflict occurs.<br> An exception will be thrown if the destination directory contains a non-empty directory with
 *     the same name as the source directory.<br>- **1**: Throw an exception if a file conflict occurs.<br> An exception
 *     will be thrown if the destination directory contains a directory with the same name as the source directory, and
 *     a file with the same name exists in the conflict directory. All the non-conflicting files in the source directory
 *     will be moved to the destination directory, and the non-conflicting files in the destination directory will be
 *     retained. The data attribute in the error returned provides information about the conflicting files in the Array<
 *     [ConflictFiles]{@link ConflictFiles}> format.<br>- **2**: Forcibly overwrite the conflicting files in the
 *     destination directory.<br> When the destination directory contains a directory with the same name as the source
 *     directory, the files with the same names in the destination directory are overwritten forcibly; the files without
 *     conflicts in the destination directory are retained.<br>- **3**: Forcibly overwrite the conflicting directory.<br
 *     > The source directory is moved to the destination directory, and the content of the moved directory is the same
 *     as that of the source directory. If the destination directory contains a directory with the same name as the
 *     source directory, all original files in the directory will be deleted.
 * @returns { Promise<void> } Promise that returns no value.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900014 - Device or resource busy
 * @throws { BusinessError } 13900015 - File exists
 * @throws { BusinessError } 13900016 - Cross-device link
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900028 - Too many links
 * @throws { BusinessError } 13900032 - Directory not empty
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @since 10
 */
declare function moveDir(src: string, dest: string, mode?: number): Promise<void>;
/**
 * Moves the source directory to the destination directory. This API uses an asynchronous callback to return the result.
 *
 * @param { string } src - Application sandbox path of the source directory.
 * @param { string } dest - Application sandbox path of the destination directory.
 * @param { AsyncCallback<void> } callback - Callback used to return the result.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900014 - Device or resource busy
 * @throws { BusinessError } 13900016 - Cross-device link
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900028 - Too many links
 * @throws { BusinessError } 13900032 - Directory not empty
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @since 10
 */
declare function moveDir(src: string, dest: string, callback: AsyncCallback<void>): void;
/**
 * Moves the source directory to the destination directory. This API uses an asynchronous callback to return the result.
 *
 * An exception will be thrown if a directory conflict occurs, that is, the destination directory contains a directory
 * with the same name as the source directory.
 *
 * > **NOTE**
 * >
 * > This API is not supported in a distributed directory.
 *
 * @param { string } src - Application sandbox path of the source directory.
 * @param { string } dest - Application sandbox path of the destination directory.
 * @param { AsyncCallback<void, Array<ConflictFiles>> } callback - Callback used to return the result.
 * @throws { BusinessError } 13900015 - File exists
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @since 10
 */
declare function moveDir(src: string, dest: string, callback: AsyncCallback<void, Array<ConflictFiles>>): void;
/**
 * Moves the source directory to the destination directory. You can set the move mode.
 * This API uses an asynchronous callback to return the result.
 *
 * @param { string } src - Application sandbox path of the source directory.
 * @param { string } dest - Application sandbox path of the destination directory.
 * @param { number } mode - Move mode. The default value is 0.
 *     <br>0: Throw an exception if a directory conflict occurs.
 *     <br>An exception will be thrown if the destination directory contains a non-empty directory with
 *     <br>the same name as the source directory.
 *     <br>1: Throw an exception if a file conflict occurs.
 *     <br>An exception will be thrown if the destination directory contains a directory with
 *     <br>the same name as the source directory, and a file with the same name exists in the conflict directory.
 *     <br>All the non-conflicting files in the source directory will be moved to the destination directory,
 *     <br>and the non-conflicting files in the destination directory will be retained.
 *     <br>The data attribute in the error returned provides information about the conflicting files in
 *     <br>the Array<ConflictFiles> format.
 *     <br>2: Forcibly overwrite the conflicting files in the destination directory.
 *     <br>When the destination directory contains a directory with the same name as the source directory,
 *     <br>the files with the same names in the destination directory are overwritten forcibly;
 *     <br>the files without conflicts in the destination directory are retained.
 *     <br>3: Forcibly overwrite the conflicting directory.
 *     <br>The source directory is moved to the destination directory, and the content of the moved directory is the
 *     <br>same as that of the source directory. If the destination directory contains a directory with the same name
 *     <br>as the source directory, all original files in the directory will be deleted.
 * @param { AsyncCallback<void> } callback - Return the callback function.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900014 - Device or resource busy
 * @throws { BusinessError } 13900016 - Cross-device link
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900028 - Too many links
 * @throws { BusinessError } 13900032 - Directory not empty
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @since 10
 */
declare function moveDir(src: string, dest: string, mode: number, callback: AsyncCallback<void>): void;
/**
 * Moves the source directory to the destination directory. You can set the move mode. This API uses an asynchronous
 * callback to return the result.
 *
 * > **NOTE**
 * >
 * > This API is not supported in a distributed directory.
 *
 * @param { string } src - Application sandbox path of the source directory.
 * @param { string } dest - Application sandbox path of the destination directory.
 * @param { number } mode - Move mode. The default value is **0**.<br>- **0**: Throw an exception if a directory
 *     conflict occurs.<br> An exception will be thrown if the destination directory contains a directory with the same
 *     name as the source directory.<br>- **1**: Throw an exception if a file conflict occurs.<br> An exception will be
 *     thrown if the destination directory contains a directory with the same name as the source directory, and a file
 *     with the same name exists in the conflict directory. All the non-conflicting files in the source directory will
 *     be moved to the destination directory, and the non-conflicting files in the destination directory will be
 *     retained. The data attribute in the error returned provides information about the conflicting files in the Array<
 *     [ConflictFiles]{@link ConflictFiles}> format.<br>- **2**: Forcibly overwrite the conflicting files in the
 *     destination directory.<br> When the destination directory contains a directory with the same name as the source
 *     directory, the files with the same names in the destination directory are overwritten forcibly; the files without
 *     conflicts in the destination directory are retained.<br>- **3**: Forcibly overwrite the conflicting directory.<br
 *     > The source directory is moved to the destination directory, and the content of the moved directory is the same
 *     as that of the source directory. If the destination directory contains a directory with the same name as the
 *     source directory, all original files in the directory will be deleted.
 * @param { AsyncCallback<void, Array<ConflictFiles>> } callback - Callback used to return the result.
 * @throws { BusinessError } 13900015 - File exists
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @since 10
 */
declare function moveDir(src: string, dest: string, mode: number, callback: AsyncCallback<void, Array<ConflictFiles>>): void;
/**
 * Moves the source directory to the destination directory. This API returns the result synchronously.
 *
 * > **NOTE**
 * >
 * > This API is not supported in a distributed directory.
 *
 * @param { string } src - Application sandbox path of the source directory.
 * @param { string } dest - Application sandbox path of the destination directory.
 * @param { number } [mode] - Move mode. The default value is **0**.<br>- **0**: Throw an exception if a directory
 *     conflict occurs.<br> An exception will be thrown if the destination directory contains a directory with the same
 *     name as the source directory.<br>- **1**: Throw an exception if a file conflict occurs.<br> An exception will be
 *     thrown if the destination directory contains a directory with the same name as the source directory, and a file
 *     with the same name exists in the conflict directory. All the non-conflicting files in the source directory will
 *     be moved to the destination directory, and the non-conflicting files in the destination directory will be
 *     retained. The data attribute in the error returned provides information about the conflicting files in the Array<
 *     [ConflictFiles]{@link ConflictFiles}> format.<br>- **2**: Forcibly overwrite the conflicting files in the
 *     destination directory.<br> When the destination directory contains a directory with the same name as the source
 *     directory, the files with the same names in the destination directory are overwritten forcibly; the files without
 *     conflicts in the destination directory are retained.<br>- **3**: Forcibly overwrite the conflicting directory.<br
 *     > The source directory is moved to the destination directory, and the content of the moved directory is the same
 *     as that of the source directory. If the destination directory contains a directory with the same name as the
 *     source directory, all original files in the directory will be deleted.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900014 - Device or resource busy
 * @throws { BusinessError } 13900015 - File exists
 * @throws { BusinessError } 13900016 - Cross-device link
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900028 - Too many links
 * @throws { BusinessError } 13900032 - Directory not empty
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @since 10
 */
declare function moveDirSync(src: string, dest: string, mode?: number): void;
/**
 * Moves a file. This API uses a promise to return the result.
 *
 * > **NOTE**
 * >
 * > This API is not supported in a distributed directory.
 *
 * @param { string } src - Application sandbox path of the file to move.
 * @param { string } dest - Application sandbox path of the destination file.
 * @param { number } [mode] - Move mode.<br> The value **0** means to overwrite the file with the same name in the
 *     destination directory; the value **1** means to throw an exception. The default value is **0**.
 * @returns { Promise<void> } Promise that returns no value.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900014 - Device or resource busy
 * @throws { BusinessError } 13900015 - File exists
 * @throws { BusinessError } 13900016 - Cross-device link
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900028 - Too many links
 * @throws { BusinessError } 13900032 - Directory not empty
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @since 9
 */
declare function moveFile(src: string, dest: string, mode?: number): Promise<void>;
/**
 * Moves a file and forcibly overwrites the file with the same name in the destination directory. This API uses an
 * asynchronous callback to return the result.
 *
 * > **NOTE**
 * >
 * > This API is not supported in a distributed directory.
 *
 * @param { string } src - Application sandbox path of the file to move.
 * @param { string } dest - Application sandbox path of the destination file.
 * @param { AsyncCallback<void> } callback - Callback used to return the result.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900014 - Device or resource busy
 * @throws { BusinessError } 13900015 - File exists
 * @throws { BusinessError } 13900016 - Cross-device link
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900028 - Too many links
 * @throws { BusinessError } 13900032 - Directory not empty
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @since 9
 */
declare function moveFile(src: string, dest: string, callback: AsyncCallback<void>): void;
/**
 * Moves a file with the specified mode. This API uses an asynchronous callback to return the result.
 *
 * > **NOTE**
 * >
 * > This API is not supported in a distributed directory.
 *
 * @param { string } src - Application sandbox path of the file to move.
 * @param { string } dest - Application sandbox path of the destination file.
 * @param { number } [mode] - Move mode.<br> The value **0** means to overwrite the file with the same name in the
 *     destination directory; the value **1** means to throw an exception. The default value is **0**.
 * @param { AsyncCallback<void> } callback - Callback used to return the result.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900014 - Device or resource busy
 * @throws { BusinessError } 13900015 - File exists
 * @throws { BusinessError } 13900016 - Cross-device link
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900028 - Too many links
 * @throws { BusinessError } 13900032 - Directory not empty
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @since 9
 */
declare function moveFile(src: string, dest: string, mode: number, callback: AsyncCallback<void>): void;
/**
 * Moves a file. This API returns the result synchronously.
 *
 * > **NOTE**
 * >
 * > This API is not supported in a distributed directory.
 *
 * @param { string } src - Application sandbox path of the file to move.
 * @param { string } dest - Application sandbox path of the destination file.
 * @param { number } [mode] - Move mode.<br> The value **0** means to overwrite the file with the same name in the
 *     destination directory; the value **1** means to throw an exception. The default value is **0**.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900014 - Device or resource busy
 * @throws { BusinessError } 13900015 - File exists
 * @throws { BusinessError } 13900016 - Cross-device link
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900028 - Too many links
 * @throws { BusinessError } 13900032 - Directory not empty
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @since 9
 */
declare function moveFileSync(src: string, dest: string, mode?: number): void;
/**
 * Opens a file or directory. This API uses a promise to return the result. This API supports the use of a URI.
 *
 * @param { string } path - Application sandbox path or URI of the file or directory.
 * @param { number } [mode] - [Mode](docroot://reference/apis-core-file-kit/js-apis-file-fs.md#openmode) for opening the
 *     file or directory. You must specify one of the following options. By default, the file is opened in read-only
 *     mode.<br>- **OpenMode.READ_ONLY(0o0)**: Open the file in read-only mode.<br>- **OpenMode.WRITE_ONLY(0o1)**: Open
 *     the file in write-only mode.<br>- **OpenMode.READ_WRITE(0o2)**: Open the file in read/write mode.<br>You can also
 *     specify the following options, separated by a bitwise OR operator (|). By default, no additional options are
 *     given.<br>- **OpenMode.CREATE(0o100)**: If the file does not exist, create it.<br>- **OpenMode.TRUNC(0o1000)**:
 *     If the file exists and is opened in write mode, truncate the file length to 0.<br>- **OpenMode.APPEND(0o2000)**:
 *     Open the file in append mode. New data will be added to the end of the file.<br>- **OpenMode.NONBLOCK(0o4000)**:
 *     If **path** points to a named pipe (also known as a FIFO), block special file, or character special file, perform
 *     non-blocking operations on the opened file and in subsequent I/Os.<br>- **OpenMode.DIR(0o200000)**: If **path**
 *     does not point to a directory, throw an exception. The write permission is not allowed.<br>-
 *     **OpenMode.NOFOLLOW(0o400000)**: If **path** points to a symbolic link, throw an exception.<br>-
 *     **OpenMode.SYNC(0o4010000)**: Open the file in synchronous I/O mode.<br>- **OpenMode.UNCACHE(0o10000000000)**:
 *     Open the file in uncache I/O mode, This option is supported starting from API version 26.0.0.
 * @returns { Promise<File> } Promise used to return the **File** object.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900004 - Interrupted system call
 * @throws { BusinessError } 13900006 - No such device or address
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900014 - Device or resource busy
 * @throws { BusinessError } 13900015 - File exists
 * @throws { BusinessError } 13900017 - No such device
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900022 - Too many open files
 * @throws { BusinessError } 13900023 - Text file busy
 * @throws { BusinessError } 13900024 - File too large
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900029 - Resource deadlock would occur
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900034 - Operation would block
 * @throws { BusinessError } 13900038 - Value too large for defined data type
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @throws { BusinessError } 13900044 - Network is unreachable [since 12]
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare function open(path: string, mode?: number): Promise<File>;
/**
 * Opens a file or directory. This API uses an asynchronous callback to return the result. This API supports the use of
 * a URI.
 *
 * @param { string } path - Application sandbox path or URI of a file or directory.
 * @param { AsyncCallback<File> } callback - Callback used to return the result.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900004 - Interrupted system call
 * @throws { BusinessError } 13900006 - No such device or address
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900014 - Device or resource busy
 * @throws { BusinessError } 13900015 - File exists
 * @throws { BusinessError } 13900017 - No such device
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900022 - Too many open files
 * @throws { BusinessError } 13900023 - Text file busy
 * @throws { BusinessError } 13900024 - File too large
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900029 - Resource deadlock would occur
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900034 - Operation would block
 * @throws { BusinessError } 13900038 - Value too large for defined data type
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare function open(path: string, callback: AsyncCallback<File>): void;
/**
 * Opens a file or directory with the specified mode. This API uses an asynchronous callback to return the result.
 *
 * This API supports the use of a URI.
 *
 * @param { string } path - Application sandbox path or URI of a file or directory.
 * @param { number } [mode] - [Mode](docroot://reference/apis-core-file-kit/js-apis-file-fs.md#openmode) for opening the
 *     file or directory. You must specify one of the following options. By default, the file is opened in read-only
 *     mode.<br>- **OpenMode.READ_ONLY(0o0)**: Open the file in read-only mode.<br>- **OpenMode.WRITE_ONLY(0o1)**: Open
 *     the file in write-only mode.<br>- **OpenMode.READ_WRITE(0o2)**: Open the file in read/write mode.<br>You can also
 *     specify the following options, separated by a bitwise OR operator (|). By default, no additional options are
 *     given.<br>- **OpenMode.CREATE(0o100)**: If the file does not exist, create it.<br>- **OpenMode.TRUNC(0o1000)**:
 *     If the file exists and is opened in write mode, truncate the file length to 0.<br>- **OpenMode.APPEND(0o2000)**:
 *     Open the file in append mode. New data will be added to the end of the file.<br>- **OpenMode.NONBLOCK(0o4000)**:
 *     If **path** points to a named pipe (also known as a FIFO), block special file, or character special file, perform
 *     non-blocking operations on the opened file and in subsequent I/Os.<br>- **OpenMode.DIR(0o200000)**: If **path**
 *     does not point to a directory, throw an exception. The write permission is not allowed.<br>-
 *     **OpenMode.NOFOLLOW(0o400000)**: If **path** points to a symbolic link, throw an exception.<br>-
 *     **OpenMode.SYNC(0o4010000)**: Open the file in synchronous I/O mode.<br>- **OpenMode.UNCACHE(0o10000000000)**:
 *     Open the file in uncache I/O mode, This option is supported starting from API version 26.0.0.
 * @param { AsyncCallback<File> } callback - Callback used to return the result.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900004 - Interrupted system call
 * @throws { BusinessError } 13900006 - No such device or address
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900014 - Device or resource busy
 * @throws { BusinessError } 13900015 - File exists
 * @throws { BusinessError } 13900017 - No such device
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900022 - Too many open files
 * @throws { BusinessError } 13900023 - Text file busy
 * @throws { BusinessError } 13900024 - File too large
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900029 - Resource deadlock would occur
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900034 - Operation would block
 * @throws { BusinessError } 13900038 - Value too large for defined data type
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare function open(path: string, mode: number, callback: AsyncCallback<File>): void;
/**
 * Opens a file or directory. This API returns the result synchronously. This API supports the use of a URI.
 *
 * @param { string } path - Application sandbox path or URI of a file or directory to open.
 * @param { number } [mode] - [Mode](docroot://reference/apis-core-file-kit/js-apis-file-fs.md#openmode) for opening the
 *     file or directory. You must specify one of the following options. By default, the file is opened in read-only
 *     mode.<br>- **OpenMode.READ_ONLY(0o0)**: Open the file in read-only mode.<br>- **OpenMode.WRITE_ONLY(0o1)**: Open
 *     the file in write-only mode.<br>- **OpenMode.READ_WRITE(0o2)**: Open the file in read/write mode.<br>You can also
 *     specify the following options, separated by a bitwise OR operator (|). By default, no additional options are
 *     given.<br>- **OpenMode.CREATE(0o100)**: If the file does not exist, create it.<br>- **OpenMode.TRUNC(0o1000)**:
 *     If the file exists and is opened in write mode, truncate the file length to 0.<br>- **OpenMode.APPEND(0o2000)**:
 *     Open the file in append mode. New data will be added to the end of the file.<br>- **OpenMode.NONBLOCK(0o4000)**:
 *     If **path** points to a named pipe (also known as a FIFO), block special file, or character special file, perform
 *     non-blocking operations on the opened file and in subsequent I/Os.<br>- **OpenMode.DIR(0o200000)**: If **path**
 *     does not point to a directory, throw an exception. The write permission is not allowed.<br>-
 *     **OpenMode.NOFOLLOW(0o400000)**: If **path** points to a symbolic link, throw an exception.<br>-
 *     **OpenMode.SYNC(0o4010000)**: Open the file in synchronous I/O mode.<br>- **OpenMode.UNCACHE(0o10000000000)**:
 *     Open the file in uncache I/O mode, This option is supported starting from API version 26.0.0.
 * @returns { File } File object opened.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900004 - Interrupted system call
 * @throws { BusinessError } 13900006 - No such device or address
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900014 - Device or resource busy
 * @throws { BusinessError } 13900015 - File exists
 * @throws { BusinessError } 13900017 - No such device
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900022 - Too many open files
 * @throws { BusinessError } 13900023 - Text file busy
 * @throws { BusinessError } 13900024 - File too large
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900029 - Resource deadlock would occur
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900034 - Operation would block
 * @throws { BusinessError } 13900038 - Value too large for defined data type
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @throws { BusinessError } 13900044 - Network is unreachable [since 12]
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare function openSync(path: string, mode?: number): File;
/**
 * Reads file data. This API uses a promise to return the result.
 *
 * @param { number } fd - FD of the file.
 * @param { ArrayBuffer } buffer - Buffer used to store the file data read.
 * @param { object } [options] - The options are as follows:<br>- **offset** (number): position of the data to read in
 *     the file, in bytes. This parameter is optional. By default, data is read from the current position.<br>-
 *     **length** (number): length of the data to read, in bytes. This parameter is optional. The default value is the
 *     buffer length. [since 9 - 10]
 * @param { ReadOptions } [options] - The options are as follows:<br>- **offset** (number): position of the data to read
 *     in the file, in bytes. This parameter is optional. By default, data is read from the current position.<br>-
 *     **length** (number): length of the data to read, in bytes. This parameter is optional. The default value is the
 *     buffer length. [since 11]
 * @returns { Promise<number> } Promise used to return the length of the data read, in bytes.
 * @throws { BusinessError } 13900004 - Interrupted system call
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900010 - Try again
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900034 - Operation would block
 * @throws { BusinessError } 13900042 - Unknown error
 * @throws { BusinessError } 13900044 - Network is unreachable [since 12]
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare function read(fd: number, buffer: ArrayBuffer, options?: ReadOptions): Promise<number>;
/**
 * Reads data from a file. This API uses an asynchronous callback to return the result.
 *
 * @param { number } fd - FD of the file.
 * @param { ArrayBuffer } buffer - Buffer used to store the file data read.
 * @param { AsyncCallback<number> } callback - Callback used to return the length of the data read, in bytes.
 * @throws { BusinessError } 13900004 - Interrupted system call
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900010 - Try again
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900034 - Operation would block
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare function read(fd: number, buffer: ArrayBuffer, callback: AsyncCallback<number>): void;
/**
 * Reads data from a file. This API uses an asynchronous callback to return the result.
 *
 * @param { number } fd - FD of the file.
 * @param { ArrayBuffer } buffer - Buffer used to store the file data read.
 * @param { object } [options] - The options are as follows:<br>- **offset** (number): position of the data to read in
 *     the file, in bytes. This parameter is optional. By default, data is read from the current position.<br>-
 *     **length** (number): length of the data to read, in bytes. This parameter is optional. The default value is the
 *     buffer length. [since 9 - 10]
 * @param { ReadOptions } [options] - The options are as follows:<br>- **offset** (number): position of the data to read
 *     in the file, in bytes. This parameter is optional. By default, data is read from the current position.<br>-
 *     **length** (number): length of the data to read, in bytes. This parameter is optional. The default value is the
 *     buffer length. [since 11]
 * @param { AsyncCallback<number> } callback - Callback used to return the length of the data read, in bytes.
 * @throws { BusinessError } 13900004 - Interrupted system call
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900010 - Try again
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900034 - Operation would block
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare function read(fd: number, buffer: ArrayBuffer, options: ReadOptions, callback: AsyncCallback<number>): void;
/**
 * Reads data from a file. This API returns the result synchronously.
 *
 * @param { number } fd - FD of the file.
 * @param { ArrayBuffer } buffer - Buffer used to store the file data read.
 * @param { object } [options] - The options are as follows:<br>- **offset** (number): position of the data to read in
 *     the file, in bytes. This parameter is optional. By default, data is read from the current position.<br>-
 *     **length** (number): length of the data to read, in bytes. This parameter is optional. The default value is the
 *     buffer length. [since 9 - 10]
 * @param { ReadOptions } [options] - The options are as follows:<br>- **offset** (number): position of the data to read
 *     in the file, in bytes. This parameter is optional. By default, data is read from the current position.<br>-
 *     **length** (number): length of the data to read, in bytes. This parameter is optional. The default value is the
 *     buffer length. [since 11]
 * @returns { number } Length of the data read, in bytes.
 * @throws { BusinessError } 13900004 - Interrupted system call
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900010 - Try again
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900034 - Operation would block
 * @throws { BusinessError } 13900042 - Unknown error
 * @throws { BusinessError } 13900044 - Network is unreachable [since 12]
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare function readSync(fd: number, buffer: ArrayBuffer, options?: ReadOptions): number;
/**
 * Reads the text content of a file line by line. This API uses a promise to return the result. Only the files in UTF-8
 * format are supported.
 *
 * @param { string } filePath - Application sandbox path of the file.
 * @param { Options } [options] - Options for reading the text. The options are as follows:<br>- **encoding** (string):
 *     format of the data to be encoded.<br>It is valid only when the data is of the string type.<br>The default value
 *     is **'utf-8'**, which is the only value supported.
 * @returns { Promise<ReaderIterator> } Promise used to return a **ReaderIterator** object.
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900015 - File exists
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900022 - Too many open files
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @throws { BusinessError } 13900044 - Network is unreachable [since 12]
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @since 11
 */
declare function readLines(filePath: string, options?: Options): Promise<ReaderIterator>;
/**
 * Reads a file text line by line. This API uses an asynchronous callback to return the result. Only the files in UTF-8
 * format are supported.
 *
 * @param { string } filePath - Application sandbox path of the file.
 * @param { AsyncCallback<ReaderIterator> } callback - Callback used to return a **ReaderIterator** object.
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900015 - File exists
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900022 - Too many open files
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @since 11
 */
declare function readLines(filePath: string, callback: AsyncCallback<ReaderIterator>): void;
/**
 * Reads a file text line by line. This API uses an asynchronous callback to return the result. Only the files in UTF-8
 * format are supported.
 *
 * @param { string } filePath - Application sandbox path of the file.
 * @param { Options } options - Options for reading the text. The options are as follows:<br>- **encoding** (string):
 *     format of the data to be encoded.<br>It is valid only when the data is of the string type.<br>The default value
 *     is **'utf-8'**, which is the only value supported.
 * @param { AsyncCallback<ReaderIterator> } callback - Callback used to return a **ReaderIterator** object.
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900015 - File exists
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900022 - Too many open files
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @since 11
 */
declare function readLines(filePath: string, options: Options, callback: AsyncCallback<ReaderIterator>): void;
/**
 * Reads the text content of a file line by line. This API returns the result synchronously.
 *
 * @param { string } filePath - Application sandbox path of the file.
 * @param { Options } [options] - Options for reading the text. The options are as follows:<br>- **encoding** (string):
 *     format of the data to be encoded.<br>It is valid only when the data is of the string type.<br>The default value
 *     is **'utf-8'**, which is the only value supported.
 * @returns { ReaderIterator } **ReaderIterator** object.
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900015 - File exists
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900022 - Too many open files
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @throws { BusinessError } 13900044 - Network is unreachable [since 12]
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @since 11
 */
declare function readLinesSync(filePath: string, options?: Options): ReaderIterator;
/**
 * Reads the text content of a file. This API uses a promise to return the result.
 *
 * @param { string } filePath - Application sandbox path of the file.
 * @param { object } [options] - The options are as follows:<br>- **offset** (number): position of the data to read in
 *     the file, in bytes. This parameter is optional. By default, data is read from the current position.<br>-
 *     **length** (number): length of the data to read, in bytes. This parameter is optional. The default value is the
 *     file length.<br>- **encoding** (string): format of the data to be encoded.<br>It is valid only when the data is
 *     of the string type. The default value is **'utf-8'**, which is the only value supported. [since 9 - 10]
 * @param { ReadTextOptions } [options] - The options are as follows:<br>- **offset** (number): position of the data to
 *     read in the file, in bytes. This parameter is optional. By default, data is read from the current position.<br>-
 *     **length** (number): length of the data to read, in bytes. This parameter is optional. The default value is the
 *     file length.<br>- **encoding** (string): format of the data to be encoded.<br>It is valid only when the data is
 *     of the string type. The default value is **'utf-8'**, which is the only value supported. [since 11]
 * @returns { Promise<string> } Promise used to return the file content read.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900004 - Interrupted system call
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900010 - Try again
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900024 - File too large
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900034 - Operation would block
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @throws { BusinessError } 13900044 - Network is unreachable [since 12]
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare function readText(filePath: string, options?: ReadTextOptions): Promise<string>;
/**
 * Reads the text content of a file. This API uses an asynchronous callback to return the result.
 *
 * @param { string } filePath - Application sandbox path of the file.
 * @param { AsyncCallback<string> } callback - Callback used to return the content read.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900004 - Interrupted system call
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900010 - Try again
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900024 - File too large
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900034 - Operation would block
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare function readText(filePath: string, callback: AsyncCallback<string>): void;
/**
 * Reads the text content of a file. This API uses an asynchronous callback to return the result.
 *
 * @param { string } filePath - Application sandbox path of the file.
 * @param { object } [options] - The options are as follows:<br>- **offset** (number): position of the data to read in
 *     the file, in bytes. This parameter is optional. By default, data is read from the current position.<br>-
 *     **length** (number): length of the data to read, in bytes. This parameter is optional. The default value is the
 *     file length.<br>- **encoding** (string): format of the data to be encoded. The default value is **'utf-8'**,
 *     which is the only value supported. [since 9 - 10]
 * @param { ReadTextOptions } [options] - The options are as follows:<br>- **offset** (number): position of the data to
 *     read in the file, in bytes. This parameter is optional. By default, data is read from the current position.<br>-
 *     **length** (number): length of the data to read, in bytes. This parameter is optional. The default value is the
 *     file length.<br>- **encoding** (string): format of the data to be encoded. The default value is **'utf-8'**,
 *     which is the only value supported. [since 11]
 * @param { AsyncCallback<string> } callback - Callback used to return the content read.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900004 - Interrupted system call
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900010 - Try again
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900024 - File too large
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900034 - Operation would block
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare function readText(filePath: string, options: ReadTextOptions, callback: AsyncCallback<string>): void;
/**
 * Reads the text content of a file. This API returns the result synchronously.
 *
 * @param { string } filePath - Application sandbox path of the file.
 * @param { object } [options] - The options are as follows:<br>- **offset** (number): position of the data to read in
 *     the file, in bytes. This parameter is optional. By default, data is read from the current position.<br>-
 *     **length** (number): length of the data to read, in bytes. This parameter is optional. The default value is the
 *     file length.<br>- **encoding** (string): format of the data to be encoded.<br>It is valid only when the data is
 *     of the string type. The default value is **'utf-8'**, which is the only value supported. [since 9 - 10]
 * @param { ReadTextOptions } [options] - The options are as follows:<br>- **offset** (number): position of the data to
 *     read in the file, in bytes. This parameter is optional. By default, data is read from the current position.<br>-
 *     **length** (number): length of the data to read, in bytes. This parameter is optional. The default value is the
 *     file length.<br>- **encoding** (string): format of the data to be encoded.<br>It is valid only when the data is
 *     of the string type. The default value is **'utf-8'**, which is the only value supported. [since 11]
 * @returns { string } File content read.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900004 - Interrupted system call
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900010 - Try again
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900024 - File too large
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900034 - Operation would block
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @throws { BusinessError } 13900044 - Network is unreachable [since 12]
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare function readTextSync(filePath: string, options?: ReadTextOptions): string;
/**
 * Renames a file or directory. This API uses a promise to return the result.
 *
 * > **NOTE**
 * >
 * > This API is not supported in a distributed directory.
 *
 * @param { string } oldPath - Application sandbox path of the file or directory to rename.
 * @param { string } newPath - Application sandbox path of the renamed file or directory.
 * @returns { Promise<void> } Promise that returns no value.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900014 - Device or resource busy
 * @throws { BusinessError } 13900015 - File exists
 * @throws { BusinessError } 13900016 - Cross-device link
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900028 - Too many links
 * @throws { BusinessError } 13900032 - Directory not empty
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare function rename(oldPath: string, newPath: string): Promise<void>;
/**
 * Renames a file or directory. This API uses an asynchronous callback to return the result.
 *
 * > **NOTE**
 * >
 * > This API is not supported in a distributed directory.
 *
 * @param { string } oldPath - Application sandbox path of the file or directory to rename.
 * @param { string } newPath - Application sandbox path of the renamed file or directory.
 * @param { AsyncCallback<void> } callback - Callback used to return the result.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900014 - Device or resource busy
 * @throws { BusinessError } 13900015 - File exists
 * @throws { BusinessError } 13900016 - Cross-device link
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900028 - Too many links
 * @throws { BusinessError } 13900032 - Directory not empty
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare function rename(oldPath: string, newPath: string, callback: AsyncCallback<void>): void;
/**
 * Renames a file or directory. This API returns the result synchronously.
 *
 * > **NOTE**
 * >
 * > This API is not supported in a distributed directory.
 *
 * @param { string } oldPath - Application sandbox path of the file or directory to rename.
 * @param { string } newPath - Application sandbox path of the renamed file or directory.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900014 - Device or resource busy
 * @throws { BusinessError } 13900015 - File exists
 * @throws { BusinessError } 13900016 - Cross-device link
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900028 - Too many links
 * @throws { BusinessError } 13900032 - Directory not empty
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare function renameSync(oldPath: string, newPath: string): void;
/**
 * Removes a directory and all its subdirectories and files. This API uses a promise to return the result.
 *
 * > **NOTE**
 * >
 * > This API can be used to remove a single file. However, you are advised to use **unlink()** instead.
 *
 * @param { string } path - Application sandbox path of the directory.
 * @returns { Promise<void> } Promise that returns no value.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900014 - Device or resource busy
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900032 - Directory not empty
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare function rmdir(path: string): Promise<void>;
/**
 * Removes a directory and all its subdirectories and files. This API uses an asynchronous callback to return the
 * result.
 *
 * > **NOTE**
 * >
 * > This API can be used to remove a single file. However, you are advised to use **unlink()** instead.
 *
 * @param { string } path - Application sandbox path of the directory.
 * @param { AsyncCallback<void> } callback - Callback used to return the result.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900014 - Device or resource busy
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900032 - Directory not empty
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare function rmdir(path: string, callback: AsyncCallback<void>): void;
/**
 * Removes a directory and all its subdirectories and files synchronously.
 *
 * > **NOTE**
 * >
 * > This API can be used to remove a single file. However, you are advised to use **unlinkSync** instead.
 *
 * @param { string } path - Application sandbox path of the directory.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900014 - Device or resource busy
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900032 - Directory not empty
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare function rmdirSync(path: string): void;
/**
 * Obtains detailed attribute information of a file or directory. This API uses a promise to return the result.
 *
 * @param { string | number } file - Application sandbox path, URI, or FD of the file or directory.<br>**Note**: URIs
 *     can be passed since API version 22.
 * @returns { Promise<Stat> } Promise used to return the file or directory information.
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
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare function stat(file: string | number): Promise<Stat>;
/**
 * Obtains detailed attribute information of a file or directory. This API uses an asynchronous callback to return the
 * result.
 *
 * @param { string | number } file - Application sandbox path, URI, or FD of the file or directory.<br>**Note**: URIs
 *     can be passed since API version 22.
 * @param { AsyncCallback<Stat> } callback - Callback used to return the file or directory information obtained.
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
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare function stat(file: string | number, callback: AsyncCallback<Stat>): void;
/**
 * Obtains detailed attribute information of a file or directory. This API returns the result synchronously.
 *
 * @param { string | number } file - Application sandbox path, URI, or FD of the file or directory.<br>**Note**: URIs
 *     can be passed since API version 22.
 * @returns { Stat } Detailed information of a file or directory.
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
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare function statSync(file: string | number): Stat;
/**
 * Creates a symbolic link based on a file path. This API uses a promise to return the result.
 *
 * > **NOTE**
 * >
 * > Since API version 11, this API cannot be used by third-party applications.
 *
 * @param { string } target - Application sandbox path of the target file.
 * @param { string } srcPath - Application sandbox path of the symbolic link.
 * @returns { Promise<void> } Promise that returns no value.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900015 - File exists
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 9
 */
declare function symlink(target: string, srcPath: string): Promise<void>;
/**
 * Creates a symbolic link based on the file path. This API uses an asynchronous callback to return the result.
 *
 * > **NOTE**
 * >
 * > Since API version 11, this API cannot be used by third-party applications.
 *
 * @param { string } target - Application sandbox path of the target file.
 * @param { string } srcPath - Application sandbox path of the symbolic link.
 * @param { AsyncCallback<void> } callback - Callback used to return the result.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900015 - File exists
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 9
 */
declare function symlink(target: string, srcPath: string, callback: AsyncCallback<void>): void;
/**
 * Creates a symbolic link based on the file path. This API returns the result synchronously.
 *
 * > **NOTE**
 * >
 * > Since API version 11, this API cannot be used by third-party applications.
 *
 * @param { string } target - Application sandbox path of the target file.
 * @param { string } srcPath - Application sandbox path of the symbolic link.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900015 - File exists
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 9
 */
declare function symlinkSync(target: string, srcPath: string): void;
/**
 * Truncates a file. This API uses a promise to return the result.
 *
 * @param { string | number } file - Application sandbox path or FD of the file.
 * @param { number } [len] - File length after truncation, in bytes. The default value is **0**.
 * @returns { Promise<void> } Promise that returns no value.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900004 - Interrupted system call
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900023 - Text file busy
 * @throws { BusinessError } 13900024 - File too large
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare function truncate(file: string | number, len?: number): Promise<void>;
/**
 * Truncates a file. This API uses an asynchronous callback to return the result.
 *
 * @param { string | number } file - Application sandbox path or FD of the file.
 * @param { AsyncCallback<void> } callback - Callback that returns no value.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900004 - Interrupted system call
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900023 - Text file busy
 * @throws { BusinessError } 13900024 - File too large
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare function truncate(file: string | number, callback: AsyncCallback<void>): void;
/**
 * Truncates a file. This API uses an asynchronous callback to return the result.
 *
 * @param { string | number } file - Application sandbox path or FD of the file.
 * @param { number } [len] - File length after truncation, in bytes. The default value is **0**. [since 9 - 10]
 * @param { number } len - File length after truncation, in bytes. The default value is **0**. [since 11]
 * @param { AsyncCallback<void> } callback - Callback that returns no value.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900004 - Interrupted system call
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900023 - Text file busy
 * @throws { BusinessError } 13900024 - File too large
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare function truncate(file: string | number, len: number, callback: AsyncCallback<void>): void;
/**
 * Truncates the file content. This API returns the result synchronously.
 *
 * @param { string | number } file - Application sandbox path or FD of the file.
 * @param { number } [len] - File length after truncation, in bytes. The default value is **0**.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900004 - Interrupted system call
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900023 - Text file busy
 * @throws { BusinessError } 13900024 - File too large
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare function truncateSync(file: string | number, len?: number): void;
/**
 * Removes a file. This API uses a promise to return the result.
 *
 * @param { string } path - Application sandbox path of the file.
 * @returns { Promise<void> } Promise that returns no value.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900014 - Device or resource busy
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare function unlink(path: string): Promise<void>;
/**
 * Removes a file. This API uses an asynchronous callback to return the result.
 *
 * @param { string } path - Application sandbox path of the file.
 * @param { AsyncCallback<void> } callback - Callback invoked immediately after the file is removed.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900014 - Device or resource busy
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare function unlink(path: string, callback: AsyncCallback<void>): void;
/**
 * Removes a file. This API returns the result synchronously.
 *
 * @param { string } path - Application sandbox path of the file.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900014 - Device or resource busy
 * @throws { BusinessError } 13900018 - Not a directory
 * @throws { BusinessError } 13900019 - Is a directory
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900030 - File name too long
 * @throws { BusinessError } 13900033 - Too many symbolic links encountered
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare function unlinkSync(path: string): void;
/**
 * Changes the time when the file was last modified.
 *
 * @param { string } path - Application sandbox path of the file.
 * @param { number } mtime - New timestamp. The value is the number of milliseconds elapsed since the Epoch
 *     time (00:00:00 UTC on January 1, 1970). Only the time when the file was last modified can be changed.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900027 - Read-only file system
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 12]
 * @since 11
 */
declare function utimes(path: string, mtime: number): void;
/**
 * Writes data into a file. This API uses a promise to return the result.
 *
 * @param { number } fd - FD of the file.
 * @param { ArrayBuffer | string } buffer - Data to write. It can be a string or data from a buffer.
 * @param { object } [options] - The options are as follows:<br>- **offset** (number): start position to write the data
 *     in the file, in bytes. This parameter is optional. By default, data is written from the current position.<br>-
 *     **length** (number): length of the data to write, in bytes. This parameter is optional. The default value is the
 *     buffer length.<br>- **encoding** (string): format of the data to be encoded when the data is a string. The
 *     default value is **'utf-8'**, which is the only value supported currently. [since 9 - 10]
 * @param { WriteOptions } [options] - The options are as follows:<br>- **offset** (number): start position to write the
 *     data in the file, in bytes. This parameter is optional. By default, data is written from the current position.<br
 *     >- **length** (number): length of the data to write, in bytes. This parameter is optional. The default value is
 *     the buffer length.<br>- **encoding** (string): format of the data to be encoded when the data is a string. The
 *     default value is **'utf-8'**, which is the only value supported currently. [since 11]
 * @returns { Promise<number> } Promise used to return the length of the data written, in bytes.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900004 - Interrupted system call
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900010 - Try again
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900024 - File too large
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900034 - Operation would block
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare function write(fd: number, buffer: ArrayBuffer | string, options?: WriteOptions): Promise<number>;
/**
 * Writes data to a file. This API uses an asynchronous callback to return the result.
 *
 * @param { number } fd - FD of the file.
 * @param { ArrayBuffer | string } buffer - Data to write. It can be a string or data from a buffer.
 * @param { AsyncCallback<number> } callback - Callback used to return the result. The callback returns the length of
 *     the data written, in bytes.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900004 - Interrupted system call
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900010 - Try again
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900024 - File too large
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900034 - Operation would block
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare function write(fd: number, buffer: ArrayBuffer | string, callback: AsyncCallback<number>): void;
/**
 * Writes data to a file. This API uses an asynchronous callback to return the result.
 *
 * @param { number } fd - FD of the file.
 * @param { ArrayBuffer | string } buffer - Data to write. It can be a string or data from a buffer.
 * @param { object } [options] - The options are as follows:<br>- **offset** (number): start position to write the data
 *     in the file, in bytes. This parameter is optional. By default, data is written from the current position.<br>-
 *     **length** (number): length of the data to write, in bytes. This parameter is optional. The default value is the
 *     buffer length.<br>- **encoding** (string): format of the data to be encoded when the data is a string. The
 *     default value is **'utf-8'**, which is the only value supported currently. [since 9 - 10]
 * @param { WriteOptions } [options] - The options are as follows:<br>- **offset** (number): start position to write the
 *     data in the file, in bytes. This parameter is optional. By default, data is written from the current position.<br
 *     >- **length** (number): length of the data to write, in bytes. This parameter is optional. The default value is
 *     the buffer length.<br>- **encoding** (string): format of the data to be encoded when the data is a string. The
 *     default value is **'utf-8'**, which is the only value supported currently. [since 11]
 * @param { AsyncCallback<number> } callback - Callback used to return the result. The callback returns the length of
 *     the data written, in bytes.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900004 - Interrupted system call
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900010 - Try again
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900024 - File too large
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900034 - Operation would block
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare function write(fd: number, buffer: ArrayBuffer | string, options: WriteOptions, callback: AsyncCallback<number>): void;
/**
 * Writes data to a file. This API returns the result synchronously.
 *
 * @param { number } fd - FD of the file.
 * @param { ArrayBuffer | string } buffer - Data to write. It can be a string or data from a buffer.
 * @param { object } [options] - The options are as follows:<br>- **offset** (number): start position to write the data
 *     in the file, in bytes. This parameter is optional. By default, data is written from the current position.<br>-
 *     **length** (number): length of the data to write, in bytes. This parameter is optional. The default value is the
 *     buffer length.<br>- **encoding** (string): format of the data to be encoded when the data is a string. The
 *     default value is **'utf-8'**, which is the only value supported currently. [since 9 - 10]
 * @param { WriteOptions } [options] - The options are as follows:<br>- **offset** (number): start position to write the
 *     data in the file, in bytes. This parameter is optional. By default, data is written from the current position.<br
 *     >- **length** (number): length of the data to write, in bytes. This parameter is optional. The default value is
 *     the buffer length.<br>- **encoding** (string): format of the data to be encoded when the data is a string. The
 *     default value is **'utf-8'**, which is the only value supported currently. [since 11]
 * @returns { number } Length of the data written, in bytes.
 * @throws { BusinessError } 13900001 - Operation not permitted
 * @throws { BusinessError } 13900004 - Interrupted system call
 * @throws { BusinessError } 13900005 - I/O error
 * @throws { BusinessError } 13900008 - Bad file descriptor
 * @throws { BusinessError } 13900010 - Try again
 * @throws { BusinessError } 13900013 - Bad address
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900024 - File too large
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900034 - Operation would block
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare function writeSync(fd: number, buffer: ArrayBuffer | string, options?: WriteOptions): number;
/**
 * Triggers connection. If the peer device is abnormal, [onStatus]{@link DfsListeners.onStatus} in **DfsListeners** will
 * be called to notify the application.
 *
 * @permission ohos.permission.DISTRIBUTED_DATASYNC
 * @param { string } networkId - Network ID of the device. The device network ID can be obtained from
 *     [DeviceBasicInfo]{@link @ohos.distributedDeviceManager:distributedDeviceManager.DeviceBasicInfo} using the
 *     related [distributedDeviceManager]{@link @ohos.distributedDeviceManager:distributedDeviceManager} API.
 * @param { DfsListeners } listeners - Listeners for distributed file system status.
 * @returns { Promise<void> } Promise that returns no value.
 * @throws { BusinessError } 201 - Permission denied.
 * @throws { BusinessError } 401 - The parameter check failed.Possible causes:
 *     1.Mandatory parameters are left unspecified;
 *     <br>2.Incorrect parameter types.
 * @throws { BusinessError } 13900045 - Connection failed.
 * @throws { BusinessError } 13900046 - Software caused connection abort.
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 12
 */
declare function connectDfs(networkId: string, listeners: DfsListeners): Promise<void>;
/**
 * Triggers disconnection.
 *
 * @permission ohos.permission.DISTRIBUTED_DATASYNC
 * @param { string } networkId - Network ID of the device. The device network ID can be obtained from
 *     [DeviceBasicInfo]{@link @ohos.distributedDeviceManager:distributedDeviceManager.DeviceBasicInfo} using the
 *     related [distributedDeviceManager]{@link @ohos.distributedDeviceManager:distributedDeviceManager} API.
 * @returns { Promise<void> } Promise that returns no value.
 * @throws { BusinessError } 201 - Permission denied.
 * @throws { BusinessError } 401 - The parameter check failed.Possible causes:
 *     1.Mandatory parameters are left unspecified;
 *     <br>2.Incorrect parameter types.
 * @throws { BusinessError } 13600004 - Unmount failed.
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 12
 */
declare function disconnectDfs(networkId: string): Promise<void>;
/**
 * Sets an extended attribute of a file or directory. This API uses a promise to return the result.
 *
 * @param { string } path - Application sandbox path of the file or directory.
 * @param { string } key - Key of the extended attribute to obtain. The value is a string of less than 256 bytes and can
 *     contain only the **user.** prefix.
 * @param { string } value - Value of the extended attribute to set.
 * @returns { Promise<void> } Promise that returns no value.
 * @throws { BusinessError } 401 - Parameter error. Possible causes:1.Mandatory parameters are left unspecified;
 *     <br>2.Incorrect parameter types.
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900031 - Function not implemented
 * @throws { BusinessError } 13900038 - Value too large for defined data type
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @since 12
 */
declare function setxattr(path: string, key: string, value: string): Promise<void>;
/**
 * Sets an extended attribute of a file or directory.
 *
 * @param { string } path - Application sandbox path of the file or directory.
 * @param { string } key - Key of the extended attribute to obtain. The value is a string of less than 256 bytes and can
 *     contain only the **user.** prefix.
 * @param { string } value - Value of the extended attribute to set.
 * @throws { BusinessError } 401 - Parameter error. Possible causes:1.Mandatory parameters are left unspecified;
 *     <br>2.Incorrect parameter types.
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900011 - Out of memory
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900020 - Invalid argument
 * @throws { BusinessError } 13900025 - No space left on device
 * @throws { BusinessError } 13900031 - Function not implemented
 * @throws { BusinessError } 13900038 - Value too large for defined data type
 * @throws { BusinessError } 13900041 - Quota exceeded
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @since 12
 */
declare function setxattrSync(path: string, key: string, value: string): void;
/**
 * Obtains an extended attribute of a file or directory. This API uses a promise to return the result.
 *
 * @param { string } path - Application sandbox path of the file or directory.
 * @param { string } key - Key of the extended attribute to obtain.
 * @returns { Promise<string> } Promise used to return the value of the extended attribute obtained.
 * @throws { BusinessError } 401 - Parameter error. Possible causes:1.Mandatory parameters are left unspecified;
 *     <br>2.Incorrect parameter types.
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900007 - Arg list too long
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900031 - Function not implemented
 * @throws { BusinessError } 13900037 - No data available
 * @throws { BusinessError } 13900038 - Value too large for defined data type
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @since 12
 */
declare function getxattr(path: string, key: string): Promise<string>;
/**
 * Obtains an extended attribute of a file or directory. This API returns the result synchronously.
 *
 * @param { string } path - Application sandbox path of the file or directory.
 * @param { string } key - Key of the extended attribute to obtain.
 * @returns { string } Value of the extended attribute obtained.
 * @throws { BusinessError } 401 - Parameter error. Possible causes:1.Mandatory parameters are left unspecified;
 *     <br>2.Incorrect parameter types.
 * @throws { BusinessError } 13900002 - No such file or directory
 * @throws { BusinessError } 13900007 - Arg list too long
 * @throws { BusinessError } 13900012 - Permission denied
 * @throws { BusinessError } 13900031 - Function not implemented
 * @throws { BusinessError } 13900037 - No data available
 * @throws { BusinessError } 13900038 - Value too large for defined data type
 * @throws { BusinessError } 13900042 - Unknown error
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @since 12
 */
declare function getxattrSync(path: string, key: string): string;
/**
 * Defines the copy progress information.
 *
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 11
 */
interface Progress {
    /**
     * Size of the copied data, in bytes.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 11
     */
    readonly processedSize: number;
    /**
     * Total size of the data to be copied, in bytes.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 11
     */
    readonly totalSize: number;
}
/**
 * Provides APIs for interrupting a copy task.
 *
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 12
 */
export class TaskSignal {
    /**
     * Cancels a copy task.
     *
     * @throws { BusinessError } 13900010 - Try again
     * @throws { BusinessError } 13900012 - Permission denied by the file system
     * @throws { BusinessError } 13900043 - No task can be canceled.
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 12
     */
    cancel(): void;
    /**
     * > **NOTE**
     * >
     * > This API is supported since API version 12 and deprecated since API version 24.
     *
     * Subscribes to the event reported when a copy task is canceled.
     *
     * @returns { Promise<string> } Promise used to return the path of the last file copied.
     * @throws { BusinessError } 13900004 - Interrupted system call
     * @throws { BusinessError } 13900008 - Bad file descriptor
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 12
     * @deprecated since 24
     */
    onCancel(): Promise<string>;
}
/**
 * Defines the callback for listening for the copy progress.
 *
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 11
 */
interface CopyOptions {
    /**
     * Listener used to observe the copy progress.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 11
     */
    progressListener?: ProgressListener;
    /**
     * Signal used to cancel a copy task.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 12
     */
    copySignal?: TaskSignal;
}
/**
 * Listener used to observe the copy progress.
 *
 * @param { Progress } progress - indicates the progress data of copyFile
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 11
 */
type ProgressListener = (progress: Progress) => void;
/**
 * Represents a **File** object opened by **open()**.
 *
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare interface File {
    /**
     * FD of the file.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    readonly fd: number;
    /**
     * Path of the file.
     *
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900042 - Unknown error
     * @throws { BusinessError } 14300002 - Invalid URI
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 10
     */
    readonly path: string;
    /**
     * Name of the file.
     *
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 10
     */
    readonly name: string;
    /**
     * Obtains the parent directory of this file object.
     *
     * @returns { string } Parent directory obtained.
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900042 - Unknown error
     * @throws { BusinessError } 14300002 - Invalid URI
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 11
     */
    getParent(): string;
    /**
     * Applies an exclusive lock or a shared lock on this file in blocking mode. This API uses a promise to return the
     * result.
     *
     * @param { boolean } exclusive - Lock to apply.<br> The value **true** means an exclusive lock, and the value
     *     **false** (default) means a shared lock.
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 13900004 - Interrupted system call
     * @throws { BusinessError } 13900008 - Bad file descriptor
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900034 - Operation would block
     * @throws { BusinessError } 13900042 - Unknown error
     * @throws { BusinessError } 13900043 - No record locks available
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 9
     */
    lock(exclusive?: boolean): Promise<void>;
    /**
     * Applies an exclusive lock or a shared lock on this file in blocking mode. This API uses an asynchronous callback to
     * return the result.
     *
     * @param { AsyncCallback<void> } callback - Callback used to return the result.
     * @throws { BusinessError } 13900004 - Interrupted system call
     * @throws { BusinessError } 13900008 - Bad file descriptor
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900034 - Operation would block
     * @throws { BusinessError } 13900042 - Unknown error
     * @throws { BusinessError } 13900043 - No record locks available
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 9
     */
    lock(callback: AsyncCallback<void>): void;
    /**
     * Applies an exclusive lock or a shared lock on this file in blocking mode. This API uses an asynchronous callback to
     * return the result.
     *
     * @param { boolean } exclusive - Lock to apply.<br> The value **true** means an exclusive lock, and the value
     *     **false** (default) means a shared lock.
     * @param { AsyncCallback<void> } callback - Callback used to return the result.
     * @throws { BusinessError } 13900004 - Interrupted system call
     * @throws { BusinessError } 13900008 - Bad file descriptor
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900034 - Operation would block
     * @throws { BusinessError } 13900042 - Unknown error
     * @throws { BusinessError } 13900043 - No record locks available
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 9
     */
    lock(exclusive: boolean, callback: AsyncCallback<void>): void;
    /**
     * Applies an exclusive lock or a shared lock on this file in non-blocking mode.
     *
     * @param { boolean } exclusive - Lock to apply.<br> The value **true** means an exclusive lock, and the value
     *     **false** (default) means a shared lock.
     * @throws { BusinessError } 13900004 - Interrupted system call
     * @throws { BusinessError } 13900008 - Bad file descriptor
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900034 - Operation would block
     * @throws { BusinessError } 13900042 - Unknown error
     * @throws { BusinessError } 13900043 - No record locks available
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 9
     */
    tryLock(exclusive?: boolean): void;
    /**
     * Unlocks a file. This API returns the result synchronously.
     *
     * @throws { BusinessError } 13900004 - Interrupted system call
     * @throws { BusinessError } 13900008 - Bad file descriptor
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900034 - Operation would block
     * @throws { BusinessError } 13900042 - Unknown error
     * @throws { BusinessError } 13900043 - No record locks available
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 9
     */
    unlock(): void;
}
/**
 * File mapping object. Before invoking the FileMapping method, you need to use the mmap() method (synchronous or
 * asynchronous) to construct a FileMapping instance.
 *
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @stagemodelonly
 * @since 26.0.0
 */
declare interface FileMapping {
    /**
     * Sets the current location of the file mapping area.
     *
     * @param { number } position - Target location, in bytes. The value must be a non-negative number and cannot
     *     be greater than the current upper bound (limit).
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900050 - Internal resource error
     * @throws { BusinessError } 13900052 - Mmap buffer released
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @stagemodelonly
     * @since 26.0.0
     */
    setPosition(position: number): void;
    /**
     * Gets the current location of the file mapping area.
     *
     * @returns { number } - Current location of the file mapping area, in bytes.
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900050 - Internal resource error
     * @throws { BusinessError } 13900052 - Mmap buffer released
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @stagemodelonly
     * @since 26.0.0
     */
    getPosition(): number;
    /**
     * Obtains the capacity of the file mapping area.
     *
     * @returns { number } - Size of the file mapping area, in bytes.
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900050 - Internal resource error
     * @throws { BusinessError } 13900052 - Mmap buffer released
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @stagemodelonly
     * @since 26.0.0
     */
    capacity(): number;
    /**
     * Sets the upper bound of the readable and writable area of the file mapping area. The upper bound does not exceed
     * the total capacity of the mapping area (0 <= limit <= capacity).
     *
     * @param { number } limit - Upper bound of the readable and writable area to be set, in bytes. If the current
     *     position is greater than the new upper bound, the value is automatically adjusted to limit.
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900050 - Internal resource error
     * @throws { BusinessError } 13900052 - Mmap buffer released
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @stagemodelonly
     * @since 26.0.0
     */
    setLimit(limit: number): void;
    /**
     * Obtains the upper bound of the readable and writable area of the file mapping area.
     *
     * @returns { number } - Upper bound of the current readable and writable area, in bytes.
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900050 - Internal resource error
     * @throws { BusinessError } 13900052 - Mmap buffer released
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @stagemodelonly
     * @since 26.0.0
     */
    getLimit(): number;
    /**
     * Mode reversal. That is, the limit attribute is set to the current position, and then the current position is set
     * to 0.
     *
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900050 - Internal resource error
     * @throws { BusinessError } 13900052 - Mmap buffer released
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @stagemodelonly
     * @since 26.0.0
     */
    flip(): void;
    /**
     * Obtains the number of remaining bytes between the current position (position) and the upper bound (limit) of the
     * readable and writable area.
     *
     * @returns { number } - Number of remaining readable or writable bytes.
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900050 - Internal resource error
     * @throws { BusinessError } 13900052 - Mmap buffer released
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @stagemodelonly
     * @since 26.0.0
     */
    remaining(): number;
    /**
     * Reads data from the current position and moves the position backward by the number of bytes actually read.
     *
     * @param { ArrayBuffer } buffer - Buffer for storing the read file data.
     * @param { number } [length] - Length of the data to be read, in bytes. This parameter is optional.
     *     The default value is the buffer length.
     * @returns { number } - Length of the actually read data, in bytes.
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900050 - Internal resource error
     * @throws { BusinessError } 13900051 - Buffer read/write out of bounds
     * @throws { BusinessError } 13900052 - Mmap buffer released
     * @throws { BusinessError } 13900054 - Mmap buffer is inaccessible
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @stagemodelonly
     * @since 26.0.0
     */
    read(buffer: ArrayBuffer, length?: number): number;
    /**
     * Reads data from the specified location without affecting the current location.
     *
     * @param { number } position - Start position to read from.
     * @param { ArrayBuffer } buffer - Buffer for storing the read file data.
     * @param { number } [length] - Length of the data to be read, in bytes. This parameter is optional.
     *     The default value is the buffer length.
     * @returns { number } - Length of the actually read data, in bytes.
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900050 - Internal resource error
     * @throws { BusinessError } 13900051 - Buffer read/write out of bounds
     * @throws { BusinessError } 13900052 - Mmap buffer released
     * @throws { BusinessError } 13900054 - Mmap buffer is inaccessible
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @stagemodelonly
     * @since 26.0.0
     */
    read(position: number, buffer: ArrayBuffer, length?: number): number;
    /**
     * Writes data from the current location and moves the location backward by the number of bytes actually written.
     *
     * @param { ArrayBuffer } data - Buffer data to be written to the file.
     * @param { number } [length] - Length of the data to be written, in bytes. This parameter is optional.
     *     The default value is the buffer length.
     * @returns { number } - Length of the data written.
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900050 - Internal resource error
     * @throws { BusinessError } 13900051 - Buffer read/write out of bounds
     * @throws { BusinessError } 13900052 - Mmap buffer released
     * @throws { BusinessError } 13900053 - Read-only mmap buffer
     * @throws { BusinessError } 13900054 - Mmap buffer is inaccessible
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @stagemodelonly
     * @since 26.0.0
     */
    write(data: ArrayBuffer, length?: number): number;
    /**
     * Writes data from the specified location without affecting the current location.
     *
     * @param { number } position - Start position of the expected write.
     * @param { ArrayBuffer } data - Buffer data to be written to the file.
     * @param { number } [length] - Length of the data to be written, in bytes. This parameter is optional.
     *     The default value is the buffer length.
     * @returns { number } - Length of the data written, in bytes.
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900050 - Internal resource error
     * @throws { BusinessError } 13900051 - Buffer read/write out of bounds
     * @throws { BusinessError } 13900052 - Mmap buffer released
     * @throws { BusinessError } 13900053 - Read-only mmap buffer
     * @throws { BusinessError } 13900054 - Mmap buffer is inaccessible
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @stagemodelonly
     * @since 26.0.0
     */
    write(position: number, data: ArrayBuffer, length?: number): number;
    /**
     * Synchronizes the dirty page data in the entire file mapping area to the disk file and uses the promise
     * asynchronous callback function.
     * Note: If the file is not stored on the local device, calling this API does not ensure that all changes are
     * stored persistently.
     *
     * @returns { Promise<void> } - Promise object. No return value.
     * @throws { BusinessError } 13900011 - Out of memory
     * @throws { BusinessError } 13900014 - Device or resource busy
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900050 - Internal resource error
     * @throws { BusinessError } 13900052 - Mmap buffer released
     * @throws { BusinessError } 13900055 - Mmap operation not supported
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @stagemodelonly
     * @since 26.0.0
     */
    msync(): Promise<void>;
    /**
     * Synchronizes the dirty page data in the specified range of the file mapping area to the disk file and uses the
     * promise asynchronous callback function.
     * Note: If the file is not stored on the local device, calling this API does not ensure that all changes are
     * stored persistently.
     *
     * @param { number } position - Start position to synchronize from, in bytes.
     * @param { number } length - Length of the data to be synchronized, in bytes.
     * @returns { Promise<void> } - Promise object. No return value.
     * @throws { BusinessError } 13900011 - Out of memory
     * @throws { BusinessError } 13900014 - Device or resource busy
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900050 - Internal resource error
     * @throws { BusinessError } 13900052 - Mmap buffer released
     * @throws { BusinessError } 13900055 - Mmap operation not supported
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @stagemodelonly
     * @since 26.0.0
     */
    msync(position: number, length: number): Promise<void>;
    /**
     * Synchronizes the dirty page data of the entire file mapping area to the disk file by using the synchronization
     * method.
     * Note: If the file is not stored on the local device, calling this API does not ensure that all changes are
     * stored persistently.
     *
     * @throws { BusinessError } 13900011 - Out of memory
     * @throws { BusinessError } 13900014 - Device or resource busy
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900050 - Internal resource error
     * @throws { BusinessError } 13900052 - Mmap buffer released
     * @throws { BusinessError } 13900055 - Mmap operation not supported
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @stagemodelonly
     * @since 26.0.0
     */
    msyncSync(): void;
    /**
     * Synchronize the dirty page data in the specified range of the file mapping area to the disk file by using the
     * synchronization method.
     * Note: If the file is not stored on the local device, calling this API does not ensure that all changes are
     * stored persistently.
     *
     * @param { number } position - Start position to synchronize from, in bytes.
     * @param { number } length - Length of the data to be synchronized, in bytes.
     * @throws { BusinessError } 13900011 - Out of memory
     * @throws { BusinessError } 13900014 - Device or resource busy
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900050 - Internal resource error
     * @throws { BusinessError } 13900052 - Mmap buffer released
     * @throws { BusinessError } 13900055 - Mmap operation not supported
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @stagemodelonly
     * @since 26.0.0
     */
    msyncSync(position: number, length: number): void;
    /**
     * Releases the file mapping area and use the promise asynchronous callback function.
     *
     * @returns { Promise<void> } - Promise object. No return value.
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900050 - Internal resource error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @stagemodelonly
     * @since 26.0.0
     */
    unmap(): Promise<void>;
    /**
     * Releases the file mapping area by using the synchronization method.
     *
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900050 - Internal resource error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @stagemodelonly
     * @since 26.0.0
     */
    unmapSync(): void;
}
/**
 * Provides APIs for randomly reading and writing a stream. Before invoking any API of **RandomAccessFile**, you need to
 * use **createRandomAccessFile()** to create a **RandomAccessFile** instance synchronously or asynchronously.
 *
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @since 10
 */
declare interface RandomAccessFile {
    /**
     * FD of the file.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 10
     */
    readonly fd: number;
    /**
     * Offset pointer to the **RandomAccessFile** instance, in bytes.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 10
     */
    readonly filePointer: number;
    /**
     * Sets the file offset pointer.
     *
     * @param { number } filePointer - Offset pointer to the **RandomAccessFile** instance, in bytes.
     * @throws { BusinessError } 13900004 - Interrupted system call
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900008 - Bad file descriptor
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 10
     */
    setFilePointer(filePointer: number): void;
    /**
     * Closes the **RandomAccessFile** instance. This API returns the result synchronously.
     *
     * @throws { BusinessError } 13900004 - Interrupted system call
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900008 - Bad file descriptor
     * @throws { BusinessError } 13900025 - No space left on device
     * @throws { BusinessError } 13900041 - Quota exceeded
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 10
     */
    close(): void;
    /**
     * Writes data into a file. This API uses a promise to return the result.
     *
     * @param { ArrayBuffer | string } buffer - Data to write. It can be a string or data from a buffer.
     * @param { object } [options] - The options are as follows:<br>- **length** (number): length of the data to write, in
     *     bytes. The default value is the buffer length.<br>- **offset** (number): start position to write the data, in
     *     bytes (it is determined by **filePointer** plus **offset**). This parameter is optional. By default, data is
     *     written from the **filePointer**.<br>- **encoding** (string): format of the data to be encoded when the data is
     *     a string. The default value is **'utf-8'**, which is the only value supported. [since 10 - 10]
     * @param { WriteOptions } [options] - The options are as follows:<br>- **length** (number): length of the data to
     *     write, in bytes. The default value is the buffer length.<br>- **offset** (number): start position to write the
     *     data, in bytes (it is determined by **filePointer** plus **offset**). This parameter is optional. By default,
     *     data is written from the **filePointer**.<br>- **encoding** (string): format of the data to be encoded when the
     *     data is a string. The default value is **'utf-8'**, which is the only value supported. [since 11]
     * @returns { Promise<number> } Promise used to return the length of the data written, in bytes.
     * @throws { BusinessError } 13900001 - Operation not permitted
     * @throws { BusinessError } 13900004 - Interrupted system call
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900008 - Bad file descriptor
     * @throws { BusinessError } 13900010 - Try again
     * @throws { BusinessError } 13900013 - Bad address
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900024 - File too large
     * @throws { BusinessError } 13900025 - No space left on device
     * @throws { BusinessError } 13900034 - Operation would block
     * @throws { BusinessError } 13900041 - Quota exceeded
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 10
     */
    write(buffer: ArrayBuffer | string, options?: WriteOptions): Promise<number>;
    /**
     * Writes data to a file. This API uses an asynchronous callback to return the result.
     *
     * @param { ArrayBuffer | string } buffer - Data to write. It can be a string or data from a buffer.
     * @param { AsyncCallback<number> } callback - Callback used to return the result. The call back returns the length of
     *     the data written, in bytes.
     * @throws { BusinessError } 13900001 - Operation not permitted
     * @throws { BusinessError } 13900004 - Interrupted system call
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900008 - Bad file descriptor
     * @throws { BusinessError } 13900010 - Try again
     * @throws { BusinessError } 13900013 - Bad address
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900024 - File too large
     * @throws { BusinessError } 13900025 - No space left on device
     * @throws { BusinessError } 13900034 - Operation would block
     * @throws { BusinessError } 13900041 - Quota exceeded
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 10
     */
    write(buffer: ArrayBuffer | string, callback: AsyncCallback<number>): void;
    /**
     * Writes data to a file. This API uses an asynchronous callback to return the result.
     *
     * @param { ArrayBuffer | string } buffer - Data to write. It can be a string or data from a buffer.
     * @param { object } [options] - The options are as follows:<br>- **length** (number): length of the data to write, in
     *     bytes. This parameter is optional. The default value is the buffer length.<br>- **offset** (number): start
     *     position to write the data, in bytes (it is determined by **filePointer** plus **offset**). This parameter is
     *     optional. By default, data is written from the **filePointer**.<br>- **encoding** (string): format of the data
     *     to be encoded when the data is a string. The default value is **'utf-8'**, which is the only value
     *     supported. [since 10 - 10]
     * @param { WriteOptions } [options] - The options are as follows:<br>- **length** (number): length of the data to
     *     write, in bytes. This parameter is optional. The default value is the buffer length.<br>- **offset** (number):
     *     start position to write the data, in bytes (it is determined by **filePointer** plus **offset**). This
     *     parameter is optional. By default, data is written from the **filePointer**.<br>- **encoding** (string): format
     *     of the data to be encoded when the data is a string. The default value is **'utf-8'**, which is the only value
     *     supported. [since 11]
     * @param { AsyncCallback<number> } callback - Callback used to return the result. The call back returns the length of
     *     the data written, in bytes.
     * @throws { BusinessError } 13900001 - Operation not permitted
     * @throws { BusinessError } 13900004 - Interrupted system call
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900008 - Bad file descriptor
     * @throws { BusinessError } 13900010 - Try again
     * @throws { BusinessError } 13900013 - Bad address
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900024 - File too large
     * @throws { BusinessError } 13900025 - No space left on device
     * @throws { BusinessError } 13900034 - Operation would block
     * @throws { BusinessError } 13900041 - Quota exceeded
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 10
     */
    write(buffer: ArrayBuffer | string, options: WriteOptions, callback: AsyncCallback<number>): void;
    /**
     * Writes data to a file. This API returns the result synchronously.
     *
     * @param { ArrayBuffer | string } buffer - Data to write. It can be a string or data from a buffer.
     * @param { object } [options] - The options are as follows:<br>- **length** (number): length of the data to write, in
     *     bytes. This parameter is optional. The default value is the buffer length.<br>- **offset** (number): start
     *     position to write the data, in bytes (it is determined by **filePointer** plus **offset**). This parameter is
     *     optional. By default, data is written from the **filePointer**.<br>- **encoding** (string): format of the data
     *     to be encoded when the data is a string. The default value is **'utf-8'**, which is the only value
     *     supported. [since 10 - 10]
     * @param { WriteOptions } [options] - The options are as follows:<br>- **length** (number): length of the data to
     *     write, in bytes. This parameter is optional. The default value is the buffer length.<br>- **offset** (number):
     *     start position to write the data, in bytes (it is determined by **filePointer** plus **offset**). This
     *     parameter is optional. By default, data is written from the **filePointer**.<br>- **encoding** (string): format
     *     of the data to be encoded when the data is a string. The default value is **'utf-8'**, which is the only value
     *     supported. [since 11]
     * @returns { number } Length of the data written in the file, in bytes.
     * @throws { BusinessError } 13900001 - Operation not permitted
     * @throws { BusinessError } 13900004 - Interrupted system call
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900008 - Bad file descriptor
     * @throws { BusinessError } 13900010 - Try again
     * @throws { BusinessError } 13900013 - Bad address
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900024 - File too large
     * @throws { BusinessError } 13900025 - No space left on device
     * @throws { BusinessError } 13900034 - Operation would block
     * @throws { BusinessError } 13900041 - Quota exceeded
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 10
     */
    writeSync(buffer: ArrayBuffer | string, options?: WriteOptions): number;
    /**
     * Reads data from a file. This API uses a promise to return the result.
     *
     * @param { ArrayBuffer } buffer - Buffer used to store the file read.
     * @param { object } [options] - The options are as follows:<br>- **length** (number): length of the data to read, in
     *     bytes. This parameter is optional. The default value is the buffer length.<br>- **offset** (number): start
     *     position to read the data, in bytes (it is determined by **filePointer** plus **offset**). This parameter is
     *     optional. By default, data is read from the **filePointer**. [since 10 - 10]
     * @param { ReadOptions } [options] - The options are as follows:<br>- **length** (number): length of the data to read
     *     , in bytes. This parameter is optional. The default value is the buffer length.<br>- **offset** (number): start
     *     position to read the data, in bytes (it is determined by **filePointer** plus **offset**). This parameter is
     *     optional. By default, data is read from the **filePointer**. [since 11]
     * @returns { Promise<number> } Promise used to return the data read, in bytes.
     * @throws { BusinessError } 13900004 - Interrupted system call
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900008 - Bad file descriptor
     * @throws { BusinessError } 13900010 - Try again
     * @throws { BusinessError } 13900013 - Bad address
     * @throws { BusinessError } 13900019 - Is a directory
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900034 - Operation would block
     * @throws { BusinessError } 13900042 - Unknown error
     * @throws { BusinessError } 13900044 - Network is unreachable [since 12]
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 10
     */
    read(buffer: ArrayBuffer, options?: ReadOptions): Promise<number>;
    /**
     * Reads data from a file. This API uses an asynchronous callback to return the result.
     *
     * @param { ArrayBuffer } buffer - Buffer used to store the file read.
     * @param { AsyncCallback<number> } callback - Callback used to return the result. return the length of the data read,
     *     in bytes.
     * @throws { BusinessError } 13900004 - Interrupted system call
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900008 - Bad file descriptor
     * @throws { BusinessError } 13900010 - Try again
     * @throws { BusinessError } 13900013 - Bad address
     * @throws { BusinessError } 13900019 - Is a directory
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900034 - Operation would block
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 10
     */
    read(buffer: ArrayBuffer, callback: AsyncCallback<number>): void;
    /**
     * Reads data from a file. This API uses an asynchronous callback to return the result.
     *
     * @param { ArrayBuffer } buffer - Buffer used to store the file read.
     * @param { object } [options] - The options are as follows:<br>- **length** (number): length of the data to read, in
     *     bytes. This parameter is optional. The default value is the buffer length.<br>- **offset** (number): start
     *     position to read the data, in bytes (it is determined by **filePointer** plus **offset**). This parameter is
     *     optional. By default, data is read from the **filePointer**. [since 10 - 10]
     * @param { ReadOptions } [options] - The options are as follows:<br>- **length** (number): length of the data to read
     *     , in bytes. This parameter is optional. The default value is the buffer length.<br>- **offset** (number): start
     *     position to read the data, in bytes (it is determined by **filePointer** plus **offset**). This parameter is
     *     optional. By default, data is read from the **filePointer**. [since 11]
     * @param { AsyncCallback<number> } callback - Callback used to return the result. return the length of the data read,
     *     in bytes.
     * @throws { BusinessError } 13900004 - Interrupted system call
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900008 - Bad file descriptor
     * @throws { BusinessError } 13900010 - Try again
     * @throws { BusinessError } 13900013 - Bad address
     * @throws { BusinessError } 13900019 - Is a directory
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900034 - Operation would block
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 10
     */
    read(buffer: ArrayBuffer, options: ReadOptions, callback: AsyncCallback<number>): void;
    /**
     * Reads data from a file. This API returns the result synchronously.
     *
     * @param { ArrayBuffer } buffer - Buffer used to store the file read.
     * @param { object } [options] - The options are as follows:<br>- **length** (number): length of the data to read, in
     *     bytes. This parameter is optional. The default value is the buffer length.<br>- **offset** (number): start
     *     position to read the data, in bytes (it is determined by **filePointer** plus **offset**). This parameter is
     *     optional. By default, data is read from the **filePointer**.<br> [since 10 - 10]
     * @param { ReadOptions } [options] - The options are as follows:<br>- **length** (number): length of the data to read
     *     , in bytes. This parameter is optional. The default value is the buffer length.<br>- **offset** (number): start
     *     position to read the data, in bytes (it is determined by **filePointer** plus **offset**). This parameter is
     *     optional. By default, data is read from the **filePointer**.<br> [since 11]
     * @returns { number } Length of the data read, in bytes.
     * @throws { BusinessError } 13900004 - Interrupted system call
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900008 - Bad file descriptor
     * @throws { BusinessError } 13900010 - Try again
     * @throws { BusinessError } 13900013 - Bad address
     * @throws { BusinessError } 13900019 - Is a directory
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900034 - Operation would block
     * @throws { BusinessError } 13900042 - Unknown error
     * @throws { BusinessError } 13900044 - Network is unreachable [since 12]
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 10
     */
    readSync(buffer: ArrayBuffer, options?: ReadOptions): number;
    /**
     * Obtains a **ReadStream** instance of this **RandomAccessFile**.
     *
     * @returns { ReadStream } **ReadStream** instance obtained.
     * @throws { BusinessError } 401 - Parameter error
     * @throws { BusinessError } 13900008 - Bad file descriptor
     * @throws { BusinessError } 13900011 - Out of memory
     * @throws { BusinessError } 13900012 - Permission denied
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 12
     */
    getReadStream(): ReadStream;
    /**
     * Obtains a **WriteStream** instance of this **RandomAccessFile**.
     *
     * @returns { WriteStream } **WriteStream** instance obtained.
     * @throws { BusinessError } 401 - Parameter error
     * @throws { BusinessError } 13900008 - Bad file descriptor
     * @throws { BusinessError } 13900011 - Out of memory
     * @throws { BusinessError } 13900012 - Permission denied
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 12
     */
    getWriteStream(): WriteStream;
}
/**
 * Defines a readable stream. You need to use
 * [fileIo.createReadStream](docroot://reference/apis-core-file-kit/js-apis-file-fs.md#fileiocreatereadstream12) to
 * create a **ReadStream** instance, which is inherited from
 * [stream.Readable]{@link @ohos.util.stream:stream.ReadableOptions}.
 *
 * The data obtained by **ReadStream** is a decoded string. Currently, only the UTF-8 format is supported.
 *
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @since 12
 */
declare class ReadStream extends stream.Readable {
    /**
     * The ReadStream constructor.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 12
     */
    constructor();
    /**
     * Number of bytes read by the readable stream.
     *
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 12
     */
    readonly bytesRead: number;
    /**
     * Path of the file corresponding to the readable stream.
     *
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 12
     */
    readonly path: string;
    /**
     * Adjusts the position of the readable stream offset pointer.
     *
     * @param { number } offset - Relative offset, in bytes.
     * @param { WhenceType } [whence] - Where to start the offset. The default value is **SEEK_SET**, which indicates the
     *     beginning of the file.
     * @returns { number } Position of the current offset pointer (offset relative to the file header, in bytes).
     * @throws { BusinessError } 401 - Parameter error
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900026 - Illegal seek
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 12
     */
    seek(offset: number, whence?: WhenceType): number;
    /**
     * Closes this readable stream.
     *
     * @throws { BusinessError } 13900004 - Interrupted system call
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900008 - Bad file descriptor
     * @throws { BusinessError } 13900025 - No space left on device
     * @throws { BusinessError } 13900041 - Quota exceeded
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 12
     */
    close(): void;
}
/**
 * Defines a writeable stream. You need to use
 * [fileIo.createWriteStream](docroot://reference/apis-core-file-kit/js-apis-file-fs.md#fileiocreatewritestream12) to
 * create a **WriteStream** instance, which is inherited from [stream.Writable]{@link @ohos.util.stream:stream.Writable}
 * .
 *
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @since 12
 */
declare class WriteStream extends stream.Writable {
    /**
     * The WriteStream constructor.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 12
     */
    constructor();
    /**
     * Number of bytes written to the writable stream.
     *
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 12
     */
    readonly bytesWritten: number;
    /**
     * Path of the file corresponding to the writeable stream.
     *
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 12
     */
    readonly path: string;
    /**
     * Adjusts the position of the writeable stream offset pointer.
     *
     * @param { number } offset - Relative offset, in bytes.
     * @param { WhenceType } [whence] - Where to start the offset. The default value is **SEEK_SET**, which indicates the
     *     beginning of the file.
     * @returns { number } Position of the current offset pointer (offset relative to the file header, in bytes).
     * @throws { BusinessError } 401 - Parameter error
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900026 - Illegal seek
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 12
     */
    seek(offset: number, whence?: WhenceType): number;
    /**
     * Closes this writeable stream.
     *
     * @throws { BusinessError } 13900004 - Interrupted system call
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900008 - Bad file descriptor
     * @throws { BusinessError } 13900025 - No space left on device
     * @throws { BusinessError } 13900041 - Quota exceeded
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 12
     */
    close(): void;
}
/**
 * AtomicFile is a class used to perform atomic read and write operations on files.
 *
 * A temporary file is written and renamed to the original file location, which ensures file integrity. If the write
 * operation fails, the temporary file is deleted without modifying the original file content.
 *
 * You can call **finishWrite()** or **failWrite()** to write or roll back file content.
 *
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @since 15
 */
export class AtomicFile {
    /**
     * Creates an **AtomicFile** class for a file in a specified path.
     *
     * @param { string } path - Application sandbox path of the file.
     * @throws { BusinessError } 401 Parameter error. Possible causes:1.Mandatory parameters are left unspecified;
     *     <br>2.Incorrect parameter types.
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 15
     */
    constructor(path: string);
    /**
     * Obtains the file object through the **AtomicFile** object.
     *
     * The FD needs to be closed by calling **close()**.
     *
     * @returns { File } File object opened.
     * @throws { BusinessError } 13900002 No such file or directory
     * @throws { BusinessError } 13900005 IO error
     * @throws { BusinessError } 13900012 Permission denied
     * @throws { BusinessError } 13900042 Internal error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 15
     */
    getBaseFile(): File;
    /**
     * Creates a **ReadStream** instance.
     *
     * @returns { ReadStream } **ReadStream** instance obtained.
     * @throws { BusinessError } 13900001 Operation not permitted
     * @throws { BusinessError } 13900002 No such file or directory
     * @throws { BusinessError } 13900012 Permission denied
     * @throws { BusinessError } 13900042 Internal error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 15
     */
    openRead(): ReadStream;
    /**
     * Reads all content of a file.
     *
     * @returns { ArrayBuffer } Full content of a file.
     * @throws { BusinessError } 13900005 I/O error
     * @throws { BusinessError } 13900042 Internal error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 15
     */
    readFully(): ArrayBuffer;
    /**
     * Starts to write new file data in the **WriteStream** object returned.
     *
     * If the file does not exist, create a file.
     *
     * Call **finishWrite()** if the write operation is successful; call **failWrite()** if the write operation fails.
     *
     * @returns { WriteStream } **WriteStream** instance obtained.
     * @throws { BusinessError } 13900001 Operation not permitted
     * @throws { BusinessError } 13900002 No such file or directory
     * @throws { BusinessError } 13900012 Permission denied
     * @throws { BusinessError } 13900027 Read-only file system
     * @throws { BusinessError } 13900042 Internal error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 15
     */
    startWrite(): WriteStream;
    /**
     * Finishes writing file data when the write operation is complete.
     *
     * @throws { BusinessError } 13900042 Internal error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 15
     */
    finishWrite(): void;
    /**
     * Rolls back the file after the file fails to be written.
     *
     * @throws { BusinessError } 13900042 Internal error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 15
     */
    failWrite(): void;
    /**
     * Deletes the **AtomicFile** class, including the original files and temporary files.
     *
     * @throws { BusinessError } 13900001 Operation not permitted
     * @throws { BusinessError } 13900002 No such file or directory
     * @throws { BusinessError } 13900012 Permission denied
     * @throws { BusinessError } 13900027 Read-only file system
     * @throws { BusinessError } 13900042 Internal error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 15
     */
    delete(): void;
}
/**
 * Represents detailed file information. Before calling any API of the **Stat()** class, use
 * [stat()](docroot://reference/apis-core-file-kit/js-apis-file-fs.md#fileiostat) to create a **Stat** instance.
 *
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 10]
 * @atomicservice [since 11]
 * @since 9
 */
declare interface Stat {
    /**
     * File ID. Different files on the same device have different **ino**s.
     *
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 10]
     * @since 9
     */
    readonly ino: bigint;
    /**
     * File permissions. The meaning of each bit is as follows:
     *
     * Note: The following values are in octal format. The return values are in decimal format. You need to convert the
     * values.
     *
     * - **0o400**: The user has the read permission on a regular file or a directory entry.
     * - **0o200**: The user has the permission to write a regular file or create and delete a directory entry.
     * - **0o100**: The user has the permission to execute a regular file or search for the specified path in a directory.
     * - **0o040**: The user group has the read permission on a regular file or a directory entry.
     * - **0o020**: The user group has the permission to write a regular file or create and delete a directory entry.
     * - **0o010**: The user group has the permission to execute a regular file or search for the specified path in a
     * directory.
     * - **0o004**: Other users have the permission to read a regular file or read a directory entry.
     * - **0o002**: Other users have the permission to write a regular file or create and delete a directory entry.
     * - **0o001**: Other users have the permission to execute a regular file or search for the specified path in a
     * directory.
     *
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    readonly mode: number;
    /**
     * ID of the file owner.
     *
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900042 - Unknown error
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 10]
     * @since 9
     */
    readonly uid: number;
    /**
     * ID of the user group of the file.
     *
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 10]
     * @since 9
     */
    readonly gid: number;
    /**
     * File size, in bytes. This parameter is valid only for regular files.
     *
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    readonly size: number;
    /**
     * Time when the file was last accessed. The value is the number of seconds elapsed since 00:00:00 on January 1, 1970.
     *
     * **Note**: Currently, user data partitions are mounted in **noatime** mode by default, and **atime** update is
     * disabled.
     *
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    readonly atime: number;
    /**
     * Time when the file content was last modified. The value is the number of seconds elapsed since 00:00:00 on January
     * 1, 1970.
     *
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    readonly mtime: number;
    /**
     * Time when the file metadata was last modified. The value is the number of seconds elapsed since 00:00:00 on January
     * 1, 1970.
     *
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 10]
     * @since 9
     */
    readonly ctime: number;
    /**
     * Time of the last access to the file. The value is the number of nanoseconds elapsed since 00:00:00 on January 1, 19
     * 70.
     *
     * **Note**: Currently, user data partitions are mounted in **noatime** mode by default, and **atime** update is
     * disabled.
     *
     * @throws { BusinessError } 13900042 - Internal error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 15
     */
    readonly atimeNs?: bigint;
    /**
     * Time of the last modification to the file. The value is the number of nanoseconds elapsed since 00:00:00 on January
     * 1, 1970.
     *
     * @throws { BusinessError } 13900042 - Internal error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 15
     */
    readonly mtimeNs?: bigint;
    /**
     * Time of the last status change of the file. The value is the number of nanoseconds elapsed since 00:00:00 on
     * January 1, 1970.
     *
     * @throws { BusinessError } 13900042 - Internal error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 15
     */
    readonly ctimeNs?: bigint;
    /**
     * File location, which indicates whether the file is stored in a local device or in the cloud.
     *
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 11
     */
    readonly location: LocationType;
    /**
     * Checks whether this file is a block special file. A block special file supports access by block only, and it is
     * cached when accessed.
     *
     * @returns { boolean } Whether the file is a block special file. The value **true** means the file is a block special
     *     file; the value **false** means the file is not a block special file.
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 10]
     * @since 9
     */
    isBlockDevice(): boolean;
    /**
     * Checks whether this file is a character special file. A character special device supports random access, and it is
     * not cached when accessed.
     *
     * @returns { boolean } Whether the file is a character special device. The value **true** means the file is a
     *     character special device; the value **false** means the opposite.
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 10]
     * @since 9
     */
    isCharacterDevice(): boolean;
    /**
     * Checks whether this file is a directory.
     *
     * @returns { boolean } Whether the file is a directory. The value **true** means the file is a directory; the value
     *     **false** means the opposite.
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    isDirectory(): boolean;
    /**
     * Checks whether this file is a named pipe (or FIFO). Named pipes are used for inter-process communication.
     *
     * @returns { boolean } Whether the file is an FIFO. The value **true** means the file is an FIFO; the value **false**
     *     means the opposite.
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 10]
     * @since 9
     */
    isFIFO(): boolean;
    /**
     * Checks whether this file is a regular file.
     *
     * @returns { boolean } Whether the file is a regular file. The value **true** means that the file is a regular file;
     *     the value **false** means the opposite.
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 10]
     * @atomicservice [since 11]
     * @since 9
     */
    isFile(): boolean;
    /**
     * Checks whether this file is a socket.
     *
     * @returns { boolean } Whether the file is a socket. The value **true** means that the file is a socket; the value
     *     **false** means the opposite.
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 10]
     * @since 9
     */
    isSocket(): boolean;
    /**
     * Checks whether this file is a symbolic link.
     *
     * @returns { boolean } Whether the file is a symbolic link. The value **true** means that the file is a symbolic link
     *     ; the value **false** means the opposite.
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 10]
     * @since 9
     */
    isSymbolicLink(): boolean;
}
/**
 * Provides API for stream operations. Before calling any API of **Stream**, you need to create a **Stream** instance by
 * using [fileIo.createStream](docroot://reference/apis-core-file-kit/js-apis-file-fs.md#fileiocreatestream) or
 * [fileIo.fdopenStream](docroot://reference/apis-core-file-kit/js-apis-file-fs.md#fileiofdopenstream).
 *
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @atomicservice [since 20]
 * @since 9
 */
declare interface Stream {
    /**
     * Closes the file stream. This API uses a promise to return the result.
     *
     * @returns { Promise<void> } Promise that returns no value.
     * @throws { BusinessError } 13900004 - Interrupted system call
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900008 - Bad file descriptor
     * @throws { BusinessError } 13900025 - No space left on device
     * @throws { BusinessError } 13900041 - Quota exceeded
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @atomicservice [since 20]
     * @since 9
     */
    close(): Promise<void>;
    /**
     * Closes the file stream. This API uses an asynchronous callback to return the result.
     *
     * @param { AsyncCallback<void> } callback - Callback invoked immediately after the stream is closed.
     * @throws { BusinessError } 13900004 - Interrupted system call
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900008 - Bad file descriptor
     * @throws { BusinessError } 13900025 - No space left on device
     * @throws { BusinessError } 13900041 - Quota exceeded
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @atomicservice [since 20]
     * @since 9
     */
    close(callback: AsyncCallback<void>): void;
    /**
     * Closes the file stream. This API returns the result synchronously.
     *
     * @throws { BusinessError } 13900004 - Interrupted system call
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900008 - Bad file descriptor
     * @throws { BusinessError } 13900025 - No space left on device
     * @throws { BusinessError } 13900041 - Quota exceeded
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @atomicservice [since 20]
     * @since 9
     */
    closeSync(): void;
    /**
     * Flushes the file stream. This API uses a promise to return the result.
     *
     * @returns { Promise<void> } Promise used to return the result.
     * @throws { BusinessError } 13900001 - Operation not permitted
     * @throws { BusinessError } 13900004 - Interrupted system call
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900008 - Bad file descriptor
     * @throws { BusinessError } 13900010 - Try again
     * @throws { BusinessError } 13900013 - Bad address
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900024 - File too large
     * @throws { BusinessError } 13900025 - No space left on device
     * @throws { BusinessError } 13900034 - Operation would block
     * @throws { BusinessError } 13900041 - Quota exceeded
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @atomicservice [since 20]
     * @since 9
     */
    flush(): Promise<void>;
    /**
     * Flushes the file stream. This API uses an asynchronous callback to return the result.
     *
     * @param { AsyncCallback<void> } callback - Callback used to return the result.
     * @throws { BusinessError } 13900001 - Operation not permitted
     * @throws { BusinessError } 13900004 - Interrupted system call
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900008 - Bad file descriptor
     * @throws { BusinessError } 13900010 - Try again
     * @throws { BusinessError } 13900013 - Bad address
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900024 - File too large
     * @throws { BusinessError } 13900025 - No space left on device
     * @throws { BusinessError } 13900034 - Operation would block
     * @throws { BusinessError } 13900041 - Quota exceeded
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @atomicservice [since 20]
     * @since 9
     */
    flush(callback: AsyncCallback<void>): void;
    /**
     * Flushes the file stream. This API returns the result synchronously.
     *
     * @throws { BusinessError } 13900001 - Operation not permitted
     * @throws { BusinessError } 13900004 - Interrupted system call
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900008 - Bad file descriptor
     * @throws { BusinessError } 13900010 - Try again
     * @throws { BusinessError } 13900013 - Bad address
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900024 - File too large
     * @throws { BusinessError } 13900025 - No space left on device
     * @throws { BusinessError } 13900034 - Operation would block
     * @throws { BusinessError } 13900041 - Quota exceeded
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @atomicservice [since 20]
     * @since 9
     */
    flushSync(): void;
    /**
     * Writes data to a stream file. This API uses a promise to return the result.
     *
     * @param { ArrayBuffer | string } buffer - Data to write. It can be a string or data from a buffer.
     * @param { object } [options] - The options are as follows:<br>- **length** (number): length of the data to write, in
     *     bytes. The default value is the buffer length.<br>- **offset** (number): start position to write the data in
     *     the file, in bytes. This parameter is optional. By default, data is written from the current position.<br>-
     *     **encoding** (string): format of the data to be encoded when the data is a string. The default value is
     *     **'utf-8'**, which is the only value supported. [since 9 - 10]
     * @param { WriteOptions } [options] - The options are as follows:<br>- **length** (number): length of the data to
     *     write, in bytes. The default value is the buffer length.<br>- **offset** (number): start position to write the
     *     data in the file, in bytes. This parameter is optional. By default, data is written from the current position.<
     *     br>- **encoding** (string): format of the data to be encoded when the data is a string. The default value is
     *     **'utf-8'**, which is the only value supported. [since 11]
     * @returns { Promise<number> } Promise used to return the length of the data written, in bytes.
     * @throws { BusinessError } 13900001 - Operation not permitted
     * @throws { BusinessError } 13900004 - Interrupted system call
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900008 - Bad file descriptor
     * @throws { BusinessError } 13900010 - Try again
     * @throws { BusinessError } 13900013 - Bad address
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900024 - File too large
     * @throws { BusinessError } 13900025 - No space left on device
     * @throws { BusinessError } 13900034 - Operation would block
     * @throws { BusinessError } 13900041 - Quota exceeded
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @atomicservice [since 20]
     * @since 9
     */
    write(buffer: ArrayBuffer | string, options?: WriteOptions): Promise<number>;
    /**
     * Writes data to a stream file. This API uses an asynchronous callback to return the result.
     *
     * @param { ArrayBuffer | string } buffer - Data to write. It can be a string or data from a buffer.
     * @param { AsyncCallback<number> } callback - Callback used to return the result. The callback returns the length of
     *     the data written, in bytes.
     * @throws { BusinessError } 13900001 - Operation not permitted
     * @throws { BusinessError } 13900004 - Interrupted system call
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900008 - Bad file descriptor
     * @throws { BusinessError } 13900010 - Try again
     * @throws { BusinessError } 13900013 - Bad address
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900024 - File too large
     * @throws { BusinessError } 13900025 - No space left on device
     * @throws { BusinessError } 13900034 - Operation would block
     * @throws { BusinessError } 13900041 - Quota exceeded
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @atomicservice [since 20]
     * @since 9
     */
    write(buffer: ArrayBuffer | string, callback: AsyncCallback<number>): void;
    /**
     * Writes data to a stream file. This API uses an asynchronous callback to return the result.
     *
     * @param { ArrayBuffer | string } buffer - Data to write. It can be a string or data from a buffer.
     * @param { object } [options] - The options are as follows:<br>- **length** (number): length of the data to write, in
     *     bytes. This parameter is optional. The default value is the buffer length.<br>- **offset** (number): start
     *     position to write the data in the file, in bytes. This parameter is optional. By default, data is written from
     *     the current position.<br>- **encoding** (string): format of the data to be encoded when the data is a string.
     *     The default value is **'utf-8'**, which is the only value supported. [since 9 - 10]
     * @param { WriteOptions } [options] - The options are as follows:<br>- **length** (number): length of the data to
     *     write, in bytes. This parameter is optional. The default value is the buffer length.<br>- **offset** (number):
     *     start position to write the data in the file, in bytes. This parameter is optional. By default, data is written
     *     from the current position.<br>- **encoding** (string): format of the data to be encoded when the data is a
     *     string. The default value is **'utf-8'**, which is the only value supported. [since 11]
     * @param { AsyncCallback<number> } callback - Callback used to return the result. The callback returns the length of
     *     the data written, in bytes.
     * @throws { BusinessError } 13900001 - Operation not permitted
     * @throws { BusinessError } 13900004 - Interrupted system call
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900008 - Bad file descriptor
     * @throws { BusinessError } 13900010 - Try again
     * @throws { BusinessError } 13900013 - Bad address
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900024 - File too large
     * @throws { BusinessError } 13900025 - No space left on device
     * @throws { BusinessError } 13900034 - Operation would block
     * @throws { BusinessError } 13900041 - Quota exceeded
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @atomicservice [since 20]
     * @since 9
     */
    write(buffer: ArrayBuffer | string, options: WriteOptions, callback: AsyncCallback<number>): void;
    /**
     * Writes data to a stream file. This API returns the result synchronously.
     *
     * @param { ArrayBuffer | string } buffer - Data to write. It can be a string or data from a buffer.
     * @param { object } [options] - The options are as follows:<br>- **length** (number): length of the data to write, in
     *     bytes. This parameter is optional. The default value is the buffer length.<br>- **offset** (number): start
     *     position to write the data in the file, in bytes. This parameter is optional. By default, data is written from
     *     the current position.<br>- **encoding** (string): format of the data to be encoded when the data is a string.
     *     The default value is **'utf-8'**, which is the only value supported. [since 9 - 10]
     * @param { WriteOptions } [options] - The options are as follows:<br>- **length** (number): length of the data to
     *     write, in bytes. This parameter is optional. The default value is the buffer length.<br>- **offset** (number):
     *     start position to write the data in the file, in bytes. This parameter is optional. By default, data is written
     *     from the current position.<br>- **encoding** (string): format of the data to be encoded when the data is a
     *     string. The default value is **'utf-8'**, which is the only value supported. [since 11]
     * @returns { number } Length of the data written in the file, in bytes.
     * @throws { BusinessError } 13900001 - Operation not permitted
     * @throws { BusinessError } 13900004 - Interrupted system call
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900008 - Bad file descriptor
     * @throws { BusinessError } 13900010 - Try again
     * @throws { BusinessError } 13900013 - Bad address
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900024 - File too large
     * @throws { BusinessError } 13900025 - No space left on device
     * @throws { BusinessError } 13900034 - Operation would block
     * @throws { BusinessError } 13900041 - Quota exceeded
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @atomicservice [since 20]
     * @since 9
     */
    writeSync(buffer: ArrayBuffer | string, options?: WriteOptions): number;
    /**
     * Reads data from a stream file. This API uses a promise to return the result.
     *
     * @param { ArrayBuffer } buffer - Buffer used to store the file read.
     * @param { object } [options] - The options are as follows:<br>- **length** (number): length of the data to read, in
     *     bytes. This parameter is optional. The default value is the buffer length.<br>- **offset** (number): position
     *     of the data to read in the file, in bytes. This parameter is optional. By default, data is read from the
     *     current position. [since 9 - 10]
     * @param { ReadOptions } [options] - The options are as follows:<br>- **length** (number): length of the data to read
     *     , in bytes. This parameter is optional. The default value is the buffer length.<br>- **offset** (number):
     *     position of the data to read in the file, in bytes. This parameter is optional. By default, data is read from
     *     the current position. [since 11]
     * @returns { Promise<number> } Promise used to return the data read, in bytes.
     * @throws { BusinessError } 13900004 - Interrupted system call
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900008 - Bad file descriptor
     * @throws { BusinessError } 13900010 - Try again
     * @throws { BusinessError } 13900013 - Bad address
     * @throws { BusinessError } 13900019 - Is a directory
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900034 - Operation would block
     * @throws { BusinessError } 13900042 - Unknown error
     * @throws { BusinessError } 13900044 - Network is unreachable [since 12]
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @atomicservice [since 20]
     * @since 9
     */
    read(buffer: ArrayBuffer, options?: ReadOptions): Promise<number>;
    /**
     * Reads data from a stream file. This API uses an asynchronous callback to return the result.
     *
     * @param { ArrayBuffer } buffer - Buffer used to store the file read.
     * @param { AsyncCallback<number> } callback - Callback used to return the result. The callback returns the data read,
     *     in bytes.
     * @throws { BusinessError } 13900004 - Interrupted system call
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900008 - Bad file descriptor
     * @throws { BusinessError } 13900010 - Try again
     * @throws { BusinessError } 13900013 - Bad address
     * @throws { BusinessError } 13900019 - Is a directory
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900034 - Operation would block
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @atomicservice [since 20]
     * @since 9
     */
    read(buffer: ArrayBuffer, callback: AsyncCallback<number>): void;
    /**
     * Reads data from a stream file. This API uses an asynchronous callback to return the result.
     *
     * @param { ArrayBuffer } buffer - Buffer used to store the file read.
     * @param { object } [options] - The options are as follows:<br>- **length** (number): length of the data to read, in
     *     bytes. This parameter is optional. The default value is the buffer length.<br>- **offset** (number): position
     *     of the data to read in the file, in bytes. This parameter is optional. By default, data is read from the
     *     current position. [since 9 - 10]
     * @param { ReadOptions } [options] - The options are as follows:<br>- **length** (number): length of the data to read
     *     , in bytes. This parameter is optional. The default value is the buffer length.<br>- **offset** (number):
     *     position of the data to read in the file, in bytes. This parameter is optional. By default, data is read from
     *     the current position. [since 11]
     * @param { AsyncCallback<number> } callback - Callback used to return the result. The callback returns the data read,
     *     in bytes.
     * @throws { BusinessError } 13900004 - Interrupted system call
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900008 - Bad file descriptor
     * @throws { BusinessError } 13900010 - Try again
     * @throws { BusinessError } 13900013 - Bad address
     * @throws { BusinessError } 13900019 - Is a directory
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900034 - Operation would block
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @atomicservice [since 20]
     * @since 9
     */
    read(buffer: ArrayBuffer, options: ReadOptions, callback: AsyncCallback<number>): void;
    /**
     * Reads data from a stream file. This API returns the result synchronously.
     *
     * @param { ArrayBuffer } buffer - Buffer used to store the file read.
     * @param { object } [options] - The options are as follows:<br>- **length** (number): length of the data to read, in
     *     bytes. This parameter is optional. The default value is the buffer length.<br>- **offset** (number): position
     *     of the data to read in the file, in bytes. This parameter is optional. By default, data is read from the
     *     current position.<br> [since 9 - 10]
     * @param { ReadOptions } [options] - The options are as follows:<br>- **length** (number): length of the data to read
     *     , in bytes. This parameter is optional. The default value is the buffer length.<br>- **offset** (number):
     *     position of the data to read in the file, in bytes. This parameter is optional. By default, data is read from
     *     the current position.<br> [since 11]
     * @returns { number } Length of the data read, in bytes.
     * @throws { BusinessError } 13900004 - Interrupted system call
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900008 - Bad file descriptor
     * @throws { BusinessError } 13900010 - Try again
     * @throws { BusinessError } 13900013 - Bad address
     * @throws { BusinessError } 13900019 - Is a directory
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900034 - Operation would block
     * @throws { BusinessError } 13900042 - Unknown error
     * @throws { BusinessError } 13900044 - Network is unreachable [since 12]
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @atomicservice [since 20]
     * @since 9
     */
    readSync(buffer: ArrayBuffer, options?: ReadOptions): number;
}
/**
 * (event: WatchEvent): void
 *
 * Provides APIs for observing events.
 *
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @since 10
 */
export interface WatchEventListener {
    /**
     * Specifies the callback function to be invoked.
     *
     * @param { WatchEvent } event - Event for the callback to invoke.
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 10
     */
    (event: WatchEvent): void;
}
/**
 * Defines the event to observe.
 *
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @since 10
 */
export interface WatchEvent {
    /**
     * Sandbox path of the file to observe. The sandbox path contains the file name.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 10
     */
    readonly fileName: string;
    /**
     * Events to observe. Multiple events can be separated by vertical bars (
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 10
     */
    readonly event: number;
    /**
     * Cookie bound with the event.
     *
     * Currently, only the **IN_MOVED_FROM** and **IN_MOVED_TO** events are supported. The **IN_MOVED_FROM** and
     * **IN_MOVED_TO** events of the same file have the same **cookie** value.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 10
     */
    readonly cookie: number;
}
/**
 * Provides APIs for observing the changes of files or directories. Before using the APIs of **Watcher**, call
 * **createWatcher()** to create a **Watcher** object.
 *
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @since 10
 */
export interface Watcher {
    /**
     * Starts listening.
     *
     * @throws { BusinessError } 13900002 - No such file or directory
     * @throws { BusinessError } 13900008 - Bad file descriptor
     * @throws { BusinessError } 13900011 - Out of memory
     * @throws { BusinessError } 13900012 - Permission denied
     * @throws { BusinessError } 13900013 - Bad address
     * @throws { BusinessError } 13900015 - File exists
     * @throws { BusinessError } 13900018 - Not a directory
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900021 - File table overflow
     * @throws { BusinessError } 13900022 - Too many open files
     * @throws { BusinessError } 13900025 - No space left on device
     * @throws { BusinessError } 13900030 - File name too long
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 10
     */
    start(): void;
    /**
     * Stops listening and removes the **Watcher** object.
     *
     * @throws { BusinessError } 13900002 - No such file or directory
     * @throws { BusinessError } 13900008 - Bad file descriptor
     * @throws { BusinessError } 13900011 - Out of memory
     * @throws { BusinessError } 13900012 - Permission denied
     * @throws { BusinessError } 13900013 - Bad address
     * @throws { BusinessError } 13900015 - File exists
     * @throws { BusinessError } 13900018 - Not a directory
     * @throws { BusinessError } 13900020 - Invalid argument
     * @throws { BusinessError } 13900021 - File table overflow
     * @throws { BusinessError } 13900022 - Too many open files
     * @throws { BusinessError } 13900025 - No space left on device
     * @throws { BusinessError } 13900030 - File name too long
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 10
     */
    stop(): void;
}
/**
 * Represents the information obtained by the **ReaderIterator** object.
 *
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @since 11
 */
export interface ReaderIteratorResult {
    /**
     * Whether the iteration is complete. The value **true** means the iteration is complete; the value **false** means
     * the opposite.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 11
     */
    done: boolean;
    /**
     * File text content read line by line.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 11
     */
    value: string;
}
/**
 * Provides a **ReaderIterator** object. Before calling APIs of **ReaderIterator**, you need to use **readLines()** to
 * create a **ReaderIterator** instance.
 *
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @since 11
 */
declare interface ReaderIterator {
    /**
     * Obtains the **ReaderIterator** result.
     *
     * @returns { ReaderIteratorResult } **ReaderIteratorResult** object obtained.
     * @throws { BusinessError } 13900005 - I/O error
     * @throws { BusinessError } 13900037 - No data available
     * @throws { BusinessError } 13900042 - Unknown error
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 11
     */
    next(): ReaderIteratorResult;
}
/**
 * Defines the file filtering configuration used by **listFile()**.
 *
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform
 * @atomicservice [since 11]
 * @since 10
 */
export interface Filter {
    /**
     * Locate files that fully match the specified file name extensions, which are of the OR relationship.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 11]
     * @atomicservice [since 11]
     * @since 10
     */
    suffix?: Array<string>;
    /**
     * Locate files that fuzzy match the specified file names, which are of the OR relationship. Currently, only the
     * wildcard * is supported.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 11]
     * @atomicservice [since 11]
     * @since 10
     */
    displayName?: Array<string>;
    /**
     * Locate files that fully match the specified MIME types, which are of the OR relationship. This parameter is
     * reserved.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 11]
     * @atomicservice [since 11]
     * @since 10
     */
    mimeType?: Array<string>;
    /**
     * Locate files that are greater than the specified size, in bytes.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 11]
     * @atomicservice [since 11]
     * @since 10
     */
    fileSizeOver?: number;
    /**
     * Locate files whose last modification time is the same or later than the specified time.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 11]
     * @atomicservice [since 11]
     * @since 10
     */
    lastModifiedAfter?: number;
    /**
     * Whether to exclude the files already in **Media**.
     *
     * The value **true** means to exclude the files already in **Media**; the value **false** means not to exclude the
     * files already in **Media**.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 11]
     * @atomicservice [since 11]
     * @since 10
     */
    excludeMedia?: boolean;
}
/**
 * Defines conflicting file information used in **copyDir()** or **moveDir()**.
 *
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @since 10
 */
export interface ConflictFiles {
    /**
     * Path of the source file.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 10
     */
    srcFile: string;
    /**
     * Path of the destination file.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 10
     */
    destFile: string;
}
/**
 * Defines the options used in **readLines()**.
 *
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @since 11
 */
export interface Options {
    /**
     * File encoding format. It is optional.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 11
     */
    encoding?: string;
}
/**
 * Defines the options used in **read()**.
 *
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @atomicservice
 * @since 11
 */
export interface ReadOptions {
    /**
     * Start position of the file to read (current **filePointer** plus **offset**), in bytes. This parameter is optional.
     * By default, data is read from the **filePointer**.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @atomicservice
     * @since 11
     */
    offset?: number;
    /**
     * Length of the data to read, in bytes. This parameter is optional. The default value is the buffer length.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @atomicservice
     * @since 11
     */
    length?: number;
}
/**
 * Defines the options used in **readText()**. It inherits from [ReadOptions]{@link ReadOptions}.
 *
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @atomicservice
 * @since 11
 */
export interface ReadTextOptions extends ReadOptions {
    /**
     * Format of the data to be encoded. This parameter is valid only when the data type is string. The default value is
     * **'utf-8'**, which is the only value supported.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @atomicservice
     * @since 11
     */
    encoding?: string;
}
/**
 * Defines the options used in **write()**. It inherits from [Options]{@link Options}.
 *
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @atomicservice
 * @since 11
 */
export interface WriteOptions extends Options {
    /**
     * Start position of the file to write (current **filePointer** plus **offset**), in bytes. This parameter is
     * optional. By default, data is written from the **filePointer**.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @atomicservice
     * @since 11
     */
    offset?: number;
    /**
     * Length of the data to write, in bytes. This parameter is optional. The default value is the buffer length.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @atomicservice
     * @since 11
     */
    length?: number;
}
/**
 * Defines the options used in **listFile()**.
 *
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @atomicservice
 * @since 11
 */
export interface ListFileOptions {
    /**
     * Whether to list all files in the subdirectories recursively. This parameter is optional. The default value is
     * **false**. If **recursion** is **false**, the names of files and directories that meet the filtering requirements
     * in the current directory are returned. If **recursion** is **true**, relative paths (starting with"/") of all files
     * that meet the specified conditions in the current directory are returned.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @atomicservice
     * @since 11
     */
    recursion?: boolean;
    /**
     * Number of file names to list. This parameter is optional. The default value is **0**, which means to list all
     * files.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @atomicservice
     * @since 11
     */
    listNum?: number;
    /**
     * File filtering configuration. This parameter is optional. It specifies the file filtering conditions.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @atomicservice
     * @since 11
     */
    filter?: Filter;
}
/**
 * Defines the file name filtering interface used by listFileExt().
 *
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @stagemodelonly
 * @since 26.0.0
 */
export interface FileFilter {
    /**
     * Filtering function, which determines whether the specified file name should be included in the file list.
     *
     * Note: This function is frequently invoked. Avoid time-consuming operations, such as file I/O and network requests.
     *
     * @param { string } name - Name of the file to be filtered.
     * @returns { boolean } Returns true if the file should be included, false otherwise.
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @stagemodelonly
     * @since 26.0.0
     */
    filter(name: string): boolean;
}
/**
 * Defines the options used in listFileExt().
 *
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @stagemodelonly
 * @since 26.0.0
 */
export interface ListFileExtOptions {
    /**
     * Whether to list all files in the subdirectories recursively. This parameter is optional.
     * The default value is false. If recursion is false, the names of files and directories that meet the filtering
     * requirements in the current directory are returned. If recursion is true, relative paths (starting with"/")
     * of all files that meet the specified conditions in the current directory are returned.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @stagemodelonly
     * @since 26.0.0
     */
    recursion?: boolean;
    /**
     * Number of file names to list. This parameter is optional. The default value is 0, which means to list all files.
     * The value should be an integer.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @stagemodelonly
     * @since 26.0.0
     */
    listNum?: number;
    /**
     * File name filtering interface. This parameter is optional.
     * Filtering rules can be defined based on file names.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @stagemodelonly
     * @since 26.0.0
     */
    fileFilter?: FileFilter;
}
/**
 * Defines the options used in **createRandomAccessFile()**.
 *
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @since 12
 */
export interface RandomAccessFileOptions {
    /**
     * Start position to read the data, in bytes. This parameter is optional. By default, data is read from the current
     * position.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 12
     */
    start?: number;
    /**
     * End position to read the data, in bytes. This parameter is optional. The default value is the end of the file.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 12
     */
    end?: number;
}
/**
 * Defines the options used in **createReadStream()**.
 *
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @since 12
 */
export interface ReadStreamOptions {
    /**
     * Start position to read the data, in bytes. This parameter is optional. By default, data is read from the current
     * position.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 12
     */
    start?: number;
    /**
     * End position to read the data, in bytes. This parameter is optional. The default value is the end of the file.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 12
     */
    end?: number;
}
/**
 * Defines the options used in **createWriteStream()**.
 *
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @since 12
 */
export interface WriteStreamOptions {
    /**
     * [Option](docroot://reference/apis-core-file-kit/js-apis-file-fs.md#openmode) for creating the writeable stream. You
     * must specify one of the following options.
     *
     * - **OpenMode.READ_ONLY(0o0)**: read-only, which is the default value.
     * - **OpenMode.WRITE_ONLY(0o1)**: write-only.
     * - **OpenMode.READ_WRITE(0o2)**: read/write.
     *
     * You can also specify the following options, separated by a bitwise OR operator (|). By default, no additional
     * options are given.
     *
     * - **OpenMode.CREATE(0o100)**: If the file does not exist, create it.
     * - **OpenMode.TRUNC(0o1000)**: If the file exists and is opened in write mode, truncate the file length to 0.
     * - **OpenMode.APPEND(0o2000)**: Open the file in append mode. New data will be added to the end of the file.
     * - **OpenMode.NONBLOCK(0o4000)**: If **path** points to a named pipe (also known as a FIFO), block special file, or
     * character special file, perform non-blocking operations on the opened file and in subsequent I/Os.
     * - **OpenMode.DIR(0o200000)**: If **path** does not point to a directory, throw an exception. The write permission
     * is not allowed.
     * - **OpenMode.NOFOLLOW(0o400000)**: If **path** points to a symbolic link, throw an exception.
     * - **OpenMode.SYNC(0o4010000)**: Open the file in synchronous I/O mode.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 12
     */
    mode?: number;
    /**
     * Start position to write the data, in bytes. This parameter is optional. By default, data is written from the
     * current position.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 12
     */
    start?: number;
}
/**
 * Provides APIs for observing events. listening for the distributed file system status.
 *
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 12
 */
export interface DfsListeners {
    /**
     * Called to return the specified status. Its parameters are passed in by
     * [connectDfs](docroot://reference/apis-core-file-kit/js-apis-file-fs.md#fileioconnectdfs12).
     *
     * @param { string } networkId - Network ID of the device.
     * @param { number } status - Status code of the distributed file system. The status code is the error code returned
     *     by **onStatus** invoked by **connectDfs**. If the device is abnormal when **connectDfs()** is called,
     *     **onStatus** will be called to return the error code:<br>-
     *     [13900046](docroot://reference/apis-core-file-kit/errorcode-filemanagement.md#13900046-connection-interrupted-by-software)
     *     : The connection is interrupted by software.
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 12
     */
    onStatus(networkId: string, status: number): void;
}
/**
 * Enumerated type of the file memory mapping mode, which can be used by the mmap API.
 *
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @stagemodelonly
 * @since 26.0.0
 */
declare enum MappingMode {
    /**
     * Read-only mode. The file mapping area is not writable. An exception is thrown when the file mapping area is
     * modified.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @stagemodelonly
     * @since 26.0.0
     */
    READ_ONLY = 0,
    /**
     * Read/Write mode. The modification is written to the file mapping area and then synchronized to the file by the
     * operating system (non-real-time).
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @stagemodelonly
     * @since 26.0.0
     */
    READ_WRITE = 1,
    /**
     * Private mode. It is a copy-on-write mapping mechanism. Modifications to the mapping area are visible only to the
     * current process and do not affect the raw file.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @stagemodelonly
     * @since 26.0.0
     */
    PRIVATE = 2
}
/**
 * Enumerates the types of the relative offset position used in **lseek()**.
 *
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @since 11
 */
declare enum WhenceType {
    /**
     * Beginning of the file.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 11
     */
    SEEK_SET = 0,
    /**
     * Current offset position.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 11
     */
    SEEK_CUR = 1,
    /**
     * End of the file.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @since 11
     */
    SEEK_END = 2
}
/**
 * Enumerates the file locations.
 *
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 11
 */
declare enum LocationType {
    /**
     * The file is stored in a local device.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 11
     */
    LOCAL = 1 << 0,
    /**
     * The file is stored in the cloud.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 11
     */
    CLOUD = 1 << 1
}
/**
 * Enumerates the access modes to verify. If this parameter is left blank, the system checks whether the file exists.
 *
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @crossplatform [since 20]
 * @atomicservice
 * @since 12
 */
declare enum AccessModeType {
    /**
     * Whether the file exists.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @atomicservice
     * @since 12
     */
    EXIST = 0,
    /**
     * Verify the write permission on the file.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @atomicservice
     * @since 12
     */
    WRITE = 2,
    /**
     * Verify the read permission on the file.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @atomicservice
     * @since 12
     */
    READ = 4,
    /**
     * Verify the read/write permission on the file.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @crossplatform [since 20]
     * @atomicservice
     * @since 12
     */
    READ_WRITE = 6
}
/**
 * Enumerates the locations of the file to verify.
 *
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 12
 */
declare enum AccessFlagType {
    /**
     * The file is stored locally.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 12
     */
    LOCAL = 0
}
export default fileIo;

```
