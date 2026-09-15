# @ohos.fileio.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2021-2023 Huawei Device Co., Ltd.
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
 * fileio
 *
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 6
 */
declare namespace fileIO {
    export { access };
    export { accessSync };
    export { chmod };
    export { chmodSync };
    export { chown };
    export { chownSync };
    export { close };
    export { closeSync };
    export { copyFile };
    export { copyFileSync };
    export { createStream };
    export { createStreamSync };
    export { createWatcher };
    export { fchmod };
    export { fchmodSync };
    export { fchown };
    export { fchownSync };
    export { fdatasync };
    export { fdatasyncSync };
    export { fdopenStream };
    export { fdopenStreamSync };
    export { fstat };
    export { fstatSync };
    export { fsync };
    export { fsyncSync };
    export { ftruncate };
    export { ftruncateSync };
    export { hash };
    export { lchown };
    export { lchownSync };
    export { lstat };
    export { lstatSync };
    export { mkdir };
    export { mkdirSync };
    export { mkdtemp };
    export { mkdtempSync };
    export { open };
    export { openSync };
    export { opendir };
    export { opendirSync };
    export { read };
    export { readSync };
    export { readText };
    export { readTextSync };
    export { rename };
    export { renameSync };
    export { rmdir };
    export { rmdirSync };
    export { stat };
    export { statSync };
    export { symlink };
    export { symlinkSync };
    export { truncate };
    export { truncateSync };
    export { unlink };
    export { unlinkSync };
    export { write };
    export { writeSync };
    export { Dir };
    export { Dirent };
    export { ReadOut };
    export { Stat };
    export { Stream };
    export { Watcher };
}
/**
 * Checks whether this process can access a file. This API uses a promise to return the result.
 *
 * @param { string } path - Application sandbox path of the file.
 * @param { number } [mode] - Options for accessing the file. You can specify multiple options, separated with a bitwise
 *     OR operator (|). The default value is **0**.<br>The options are as follows:<br>- **0**: Check whether the file
 *     exists.<br>- **1**: Check whether the process has the execute permission on the file.<br>- **2**: Check whether
 *     the process has the write permission on the file.<br>- **4**: Check whether the process has the read permission
 *     on the file.
 * @returns { Promise<void> } Promise that returns no value.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 6
 * @deprecated since 9
 * @useinstead @ohos.file.fs:access
 */
declare function access(path: string, mode?: number): Promise<void>;
/**
 * Checks whether this process can access a file. This API uses an asynchronous callback to return the result.
 *
 * @param { string } path - Application sandbox path of the file.
 * @param { AsyncCallback<void> } [callback] - Callback invoked when the file is asynchronously checked.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 6
 * @deprecated since 9
 * @useinstead @ohos.file.fs:access
 */
declare function access(path: string, callback: AsyncCallback<void>): void;
/**
 * Checks whether this process can access a file. This API uses an asynchronous callback to return the result.
 *
 * @param { string } path - Application sandbox path of the file.
 * @param { number } [mode] - Options for accessing the file. You can specify multiple options, separated with a bitwise
 *     OR operator (|). The default value is **0**.<br>The options are as follows:<br>- **0**: Check whether the file
 *     exists.<br>- **1**: Check whether the process has the execute permission on the file.<br>- **2**: Check whether
 *     the process has the write permission on the file.<br>- **4**: Check whether the process has the read permission
 *     on the file.
 * @param { AsyncCallback<void> } [callback] - Callback invoked when the file is asynchronously checked.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 6
 * @deprecated since 9
 * @useinstead @ohos.file.fs:access
 */
declare function access(path: string, mode: number, callback: AsyncCallback<void>): void;
/**
 * Checks whether this process can access a file. This API returns the result synchronously.
 *
 * @param { string } path - Application sandbox path of the file.
 * @param { number } [mode] - Options for accessing the file. You can specify multiple options, separated with a bitwise
 *     OR operator (|). The default value is **0**.<br>The options are as follows:<br>- **0**: Check whether the file
 *     exists.<br>- **1**: Check whether the process has the execute permission on the file.<br>- **2**: Check whether
 *     the process has the write permission on the file.<br>- **4**: Check whether the process has the read permission
 *     on the file.
 * @throws { TypedError | Error } access fail
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 6
 * @deprecated since 9
 * @useinstead @ohos.file.fs:accessSync
 */
declare function accessSync(path: string, mode?: number): void;
/**
 * Closes a file. This API uses a promise to return the result.
 *
 * @param { number } fd - File descriptor of the file to close.
 * @returns { Promise<void> } Promise that returns no value.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.file.fs:close
 */
declare function close(fd: number): Promise<void>;
/**
 * Closes a file. This API uses an asynchronous callback to return the result.
 *
 * @param { number } fd - File descriptor of the file to close.
 * @param { AsyncCallback<void> } [callback] - Callback invoked when the file is closed asynchronously.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.file.fs:close
 */
declare function close(fd: number, callback: AsyncCallback<void>): void;
/**
 * Closes a file. This API returns the result synchronously.
 *
 * @param { number } fd - File descriptor of the file to close.
 * @throws { TypedError | Error } close fail
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 6
 * @deprecated since 9
 * @useinstead @ohos.file.fs:closeSync
 */
declare function closeSync(fd: number): void;
/**
 * Copies a file. This API uses a promise to return the result.
 *
 * @param { string | number } src - Path or file descriptor of the source file to copy.
 * @param { string | number } dest - Path or file descriptor of the destination file.
 * @param { number } [mode] - Option for overwriting the destination file. The default value is **0**, which is the only
 *     value supported.<br>**0**: Overwrite the file with the same name completely and truncate the part that is not
 *     overwritten.
 * @returns { Promise<void> } Promise that returns no value.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 6
 * @deprecated since 9
 * @useinstead @ohos.file.fs:copyFile
 */
declare function copyFile(src: string | number, dest: string | number, mode?: number): Promise<void>;
/**
 * Copies a file. This API uses an asynchronous callback to return the result.
 *
 * @param { string | number } src - Path or file descriptor of the source file to copy.
 * @param { string | number } dest - Path or file descriptor of the destination file.
 * @param { AsyncCallback<void> } [callback] - Callback invoked when the file is copied asynchronously.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 6
 * @deprecated since 9
 * @useinstead @ohos.file.fs:copyFile
 */
declare function copyFile(src: string | number, dest: string | number, callback: AsyncCallback<void>): void;
/**
 * Copies a file. This API uses an asynchronous callback to return the result.
 *
 * @param { string | number } src - Path or file descriptor of the source file to copy.
 * @param { string | number } dest - Path or file descriptor of the destination file.
 * @param { number } [mode] - Option for overwriting the destination file. The default value is **0**, which is the only
 *     value supported.<br>**0**: Overwrite the file with the same name completely and truncate the part that is not
 *     overwritten.
 * @param { AsyncCallback<void> } [callback] - Callback invoked when the file is copied asynchronously.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 6
 * @deprecated since 9
 * @useinstead @ohos.file.fs:copyFile
 */
declare function copyFile(src: string | number, dest: string | number, mode: number, callback: AsyncCallback<void>): void;
/**
 * Copies a file. This API returns the result synchronously.
 *
 * @param { string | number } src - Path or file descriptor of the source file to copy.
 * @param { string | number } dest - Path or file descriptor of the destination file.
 * @param { number } [mode] - Option for overwriting the destination file. The default value is **0**, which is the only
 *     value supported.<br>**0**: Overwrite the file with the same name completely and truncate the part that is not
 *     overwritten.
 * @throws { TypedError | Error } copyFile fail
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 6
 * @deprecated since 9
 * @useinstead @ohos.file.fs:copyFileSync
 */
declare function copyFileSync(src: string | number, dest: string | number, mode?: number): void;
/**
 * Creates a stream based on the file path. This API uses a promise to return the result.
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
 * @returns { Promise<Stream> } Promise that returns the file stream.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.file.fs:createStream
 */
declare function createStream(path: string, mode: string): Promise<Stream>;
/**
 * Creates a stream based on the file path. This API uses an asynchronous callback to return the result.
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
 * @param { AsyncCallback<Stream> } [callback] - Callback invoked when the stream is opened asynchronously.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.file.fs:createStream
 */
declare function createStream(path: string, mode: string, callback: AsyncCallback<Stream>): void;
/**
 * Creates a stream based on the file path. This API returns the result synchronously.
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
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.file.fs:createStreamSync
 */
declare function createStreamSync(path: string, mode: string): Stream;
/**
 * Changes the file owner based on the file path. This API uses a promise to return the result.
 *
 * @param { string } path - Application sandbox path of the file.
 * @param { number } uid - New user ID (UID).
 * @param { number } gid - New group ID (GID).
 * @returns { Promise<void> } Promise that returns no value.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 */
declare function chown(path: string, uid: number, gid: number): Promise<void>;
/**
 * Changes the file owner based on the file path. This API uses an asynchronous callback to return the result.
 *
 * @param { string } path - Application sandbox path of the file.
 * @param { number } uid - New UID.
 * @param { number } gid - New GID.
 * @param { AsyncCallback<void> } [callback] - Callback invoked when the file owner is changed asynchronously.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 */
declare function chown(path: string, uid: number, gid: number, callback: AsyncCallback<void>): void;
/**
 * Changes the file owner based on its path. This API returns the result synchronously.
 *
 * @param { string } path - Application sandbox path of the file.
 * @param { number } uid - New UID.
 * @param { number } gid - New GID.
 * @throws { TypedError | Error } chown fail
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 */
declare function chownSync(path: string, uid: number, gid: number): void;
/**
 * Changes file permissions. This API uses a promise to return the result.
 *
 * @param { string } path - Application sandbox path of the file.
 * @param { number } mode - Permissions on the file. You can specify multiple permissions, separated using a bitwise OR
 *     operator (|).<br>- **0o700**: The owner has the read, write, and execute permissions.<br>- **0o400**: The owner
 *     has the read permission.<br>- **0o200**: The owner has the write permission.<br>- **0o100**: The owner has the
 *     execute permission.<br>- **0o070**: The user group has the read, write, and execute permissions.<br>- **0o040**:
 *     The user group has the read permission.<br>- **0o020**: The user group has the write permission.<br>- **0o010**:
 *     The user group has the execute permission.<br>- **0o007**: Other users have the read, write, and execute
 *     permissions.<br>- **0o004**: Other users have the read permission.<br>- **0o002**: Other users have the write
 *     permission.<br>- **0o001**: Other users have the execute permission.
 * @returns { Promise<void> } Promise that returns no value.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 */
declare function chmod(path: string, mode: number): Promise<void>;
/**
 * Changes file permissions. This API uses an asynchronous callback to return the result.
 *
 * @param { string } path - Application sandbox path of the file.
 * @param { number } mode - Permissions on the file. You can specify multiple permissions, separated using a bitwise OR
 *     operator (|).<br>- **0o700**: The owner has the read, write, and execute permissions.<br>- **0o400**: The owner
 *     has the read permission.<br>- **0o200**: The owner has the write permission.<br>- **0o100**: The owner has the
 *     execute permission.<br>- **0o070**: The user group has the read, write, and execute permissions.<br>- **0o040**:
 *     The user group has the read permission.<br>- **0o020**: The user group has the write permission.<br>- **0o010**:
 *     The user group has the execute permission.<br>- **0o007**: Other users have the read, write, and execute
 *     permissions.<br>- **0o004**: Other users have the read permission.<br>- **0o002**: Other users have the write
 *     permission.<br>- **0o001**: Other users have the execute permission.
 * @param { AsyncCallback<void> } [callback] - Callback invoked when the file permissions are changed asynchronously.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 */
declare function chmod(path: string, mode: number, callback: AsyncCallback<void>): void;
/**
 * Changes file permissions. This API returns the result synchronously.
 *
 * @param { string } path - Application sandbox path of the file.
 * @param { number } mode - Permissions on the file. You can specify multiple permissions, separated using a bitwise OR
 *     operator (|).<br>- **0o700**: The owner has the read, write, and execute permissions.<br>- **0o400**: The owner
 *     has the read permission.<br>- **0o200**: The owner has the write permission.<br>- **0o100**: The owner has the
 *     execute permission.<br>- **0o070**: The user group has the read, write, and execute permissions.<br>- **0o040**:
 *     The user group has the read permission.<br>- **0o020**: The user group has the write permission.<br>- **0o010**:
 *     The user group has the execute permission.<br>- **0o007**: Other users have the read, write, and execute
 *     permissions.<br>- **0o004**: Other users have the read permission.<br>- **0o002**: Other users have the write
 *     permission.<br>- **0o001**: Other users have the execute permission.
 * @throws { TypedError | Error } chmod fail
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 */
declare function chmodSync(path: string, mode: number): void;
/**
 * Truncates a file based on the file descriptor. This API uses a promise to return the result.
 *
 * @param { number } fd - File descriptor of the file to truncate.
 * @param { number } [len] - File length after truncation, in bytes. The default value is **0**.
 * @returns { Promise<void> } Promise that returns no value.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.file.fs:truncate
 */
declare function ftruncate(fd: number, len?: number): Promise<void>;
/**
 * Truncates a file based on the file descriptor. This API uses an asynchronous callback to return the result.
 *
 * @param { number } fd - File descriptor of the file to truncate.
 * @param { AsyncCallback<void> } [callback] - Callback that returns no value.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.file.fs:truncate
 */
declare function ftruncate(fd: number, callback: AsyncCallback<void>): void;
/**
 * Truncates a file based on the file descriptor. This API uses an asynchronous callback to return the result.
 *
 * @param { number } fd - File descriptor of the file to truncate.
 * @param { number } [len] - File length after truncation, in bytes. The default value is **0**.
 * @param { AsyncCallback<void> } [callback] - Callback that returns no value.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.file.fs:truncate
 */
declare function ftruncate(fd: number, len: number, callback: AsyncCallback<void>): void;
/**
 * Truncates a file based on the file descriptor. This API returns the result synchronously.
 *
 * @param { number } fd - File descriptor of the file to truncate.
 * @param { number } [len] - File length after truncation, in bytes. The default value is **0**.
 * @throws { TypedError | Error } ftruncate fail
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.file.fs:truncateSync
 */
declare function ftruncateSync(fd: number, len?: number): void;
/**
 * Synchronizes a file. This API uses a promise to return the result.
 *
 * @param { number } fd - File descriptor of the file to synchronize.
 * @returns { Promise<void> } Promise that returns no value.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.file.fs:fsync
 */
declare function fsync(fd: number): Promise<void>;
/**
 * Synchronizes a file. This API uses an asynchronous callback to return the result.
 *
 * @param { number } fd - File descriptor of the file to synchronize.
 * @param { AsyncCallback<void> } [callback] - Callback invoked when the file is synchronized in asynchronous mode.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.file.fs:fsync
 */
declare function fsync(fd: number, callback: AsyncCallback<void>): void;
/**
 * Synchronizes a file. This API returns the result synchronously.
 *
 * @param { number } fd - File descriptor of the file to synchronize.
 * @throws { TypedError | Error } fsync fail
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.file.fs:fsyncSync
 */
declare function fsyncSync(fd: number): void;
/**
 * Obtains file status based on the file descriptor. This API uses a promise to return the result.
 *
 * @param { number } fd - File descriptor of the file whose status is to be obtained.
 * @returns { Promise<Stat> } Promise that returns the detailed file status obtained.
 * @throws { TypedError } fstat fail
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.file.fs:stat
 */
declare function fstat(fd: number): Promise<Stat>;
/**
 * Obtains file status based on the file descriptor. This API uses an asynchronous callback to return the result.
 *
 * @param { number } fd - File descriptor of the file whose status is to be obtained.
 * @param { AsyncCallback<Stat> } callback - Callback used to return the file status obtained.
 * @throws { TypedError } fstat fail
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.file.fs:stat
 */
declare function fstat(fd: number, callback: AsyncCallback<Stat>): void;
/**
 * Obtains file status based on the file descriptor. This API returns the result synchronously.
 *
 * @param { number } fd - File descriptor of the file whose status is to be obtained.
 * @returns { Stat } Detailed file status obtained.
 * @throws { TypedError | Error } fstat fail
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.file.fs:statSync
 */
declare function fstatSync(fd: number): Stat;
/**
 * Synchronizes the data of a file. This API uses a promise to return the result.
 *
 * @param { number } fd - File descriptor of the file to synchronize.
 * @returns { Promise<void> } Promise that returns no value.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.file.fs:fdatasync
 */
declare function fdatasync(fd: number): Promise<void>;
/**
 * Synchronizes the data of a file. This API uses an asynchronous callback to return the result.
 *
 * @param { number } fd - File descriptor of the file to synchronize.
 * @param { AsyncCallback<void> } [callback] - Callback invoked when the file data is synchronized in asynchronous mode.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.file.fs:fdatasync
 */
declare function fdatasync(fd: number, callback: AsyncCallback<void>): void;
/**
 * Synchronizes the data of a file. This API returns the result synchronously.
 *
 * @param { number } fd - File descriptor of the file to synchronize.
 * @throws { TypedError | Error } fdatasync fail
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.file.fs:fdatasyncSync
 */
declare function fdatasyncSync(fd: number): void;
/**
 * Changes the file owner based on the file descriptor. This API uses a promise to return the result.
 *
 * @param { number } fd - File descriptor of the target file.
 * @param { number } uid - New UID.
 * @param { number } gid - New GID.
 * @returns { Promise<void> } Promise that returns no value.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 */
declare function fchown(fd: number, uid: number, gid: number): Promise<void>;
/**
 * Changes the file owner based on the file descriptor. This API uses an asynchronous callback to return the result.
 *
 * @param { number } fd - File descriptor of the target file.
 * @param { number } uid - New UID.
 * @param { number } gid - New GID.
 * @param { AsyncCallback<void> } [callback] - Callback invoked when the file owner is changed asynchronously.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 */
declare function fchown(fd: number, uid: number, gid: number, callback: AsyncCallback<void>): void;
/**
 * Changes the file owner based on the file descriptor. This API returns the result synchronously.
 *
 * @param { number } fd - File descriptor of the target file.
 * @param { number } uid - New UID.
 * @param { number } gid - New GID.
 * @throws { TypedError | Error } fchown fail
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 */
declare function fchownSync(fd: number, uid: number, gid: number): void;
/**
 * Changes file permissions based on the file descriptor. This API uses a promise to return the result.
 *
 * @param { number } fd - File descriptor of the target file.
 * @param { number } mode - Permissions on the file. You can specify multiple permissions, separated using a bitwise OR
 *     operator (|).<br>- **0o700**: The owner has the read, write, and execute permissions.<br>- **0o400**: The owner
 *     has the read permission.<br>- **0o200**: The owner has the write permission.<br>- **0o100**: The owner has the
 *     execute permission.<br>- **0o070**: The user group has the read, write, and execute permissions.<br>- **0o040**:
 *     The user group has the read permission.<br>- **0o020**: The user group has the write permission.<br>- **0o010**:
 *     The user group has the execute permission.<br>- **0o007**: Other users have the read, write, and execute
 *     permissions.<br>- **0o004**: Other users have the read permission.<br>- **0o002**: Other users have the write
 *     permission.<br>- **0o001**: Other users have the execute permission.
 * @returns { Promise<void> } Promise that returns no value.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 */
declare function fchmod(fd: number, mode: number): Promise<void>;
/**
 * Changes file permissions based on the file descriptor. This API uses an asynchronous callback to return the result.
 *
 * @param { number } fd - File descriptor of the target file.
 * @param { number } mode - Permissions on the file. You can specify multiple permissions, separated using a bitwise OR
 *     operator (|).<br>- **0o700**: The owner has the read, write, and execute permissions.<br>- **0o400**: The owner
 *     has the read permission.<br>- **0o200**: The owner has the write permission.<br>- **0o100**: The owner has the
 *     execute permission.<br>- **0o070**: The user group has the read, write, and execute permissions.<br>- **0o040**:
 *     The user group has the read permission.<br>- **0o020**: The user group has the write permission.<br>- **0o010**:
 *     The user group has the execute permission.<br>- **0o007**: Other users have the read, write, and execute
 *     permissions.<br>- **0o004**: Other users have the read permission.<br>- **0o002**: Other users have the write
 *     permission.<br>- **0o001**: Other users have the execute permission.
 * @param { AsyncCallback<void> } [callback] - Callback invoked when the file permissions are changed asynchronously.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 */
declare function fchmod(fd: number, mode: number, callback: AsyncCallback<void>): void;
/**
 * Changes the file permissions based on the file descriptor. This API returns the result synchronously.
 *
 * @param { number } fd - File descriptor of the target file.
 * @param { number } mode - Permissions on the file. You can specify multiple permissions, separated using a bitwise OR
 *     operator (|).<br>- **0o700**: The owner has the read, write, and execute permissions.<br>- **0o400**: The owner
 *     has the read permission.<br>- **0o200**: The owner has the write permission.<br>- **0o100**: The owner has the
 *     execute permission.<br>- **0o070**: The user group has the read, write, and execute permissions.<br>- **0o040**:
 *     The user group has the read permission.<br>- **0o020**: The user group has the write permission.<br>- **0o010**:
 *     The user group has the execute permission.<br>- **0o007**: Other users have the read, write, and execute
 *     permissions.<br>- **0o004**: Other users have the read permission.<br>- **0o002**: Other users have the write
 *     permission.<br>- **0o001**: Other users have the execute permission.
 * @throws { TypedError | Error } fchmod fail
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 */
declare function fchmodSync(fd: number, mode: number): void;
/**
 * Opens a stream based on the file descriptor. This API uses a promise to return the result.
 *
 * @param { number } fd - File descriptor of the target file.
 * @param { string } mode - - **r**: Open a file for reading. The file must exist.<br>- **r+**: Open a file for both
 *     reading and writing. The file must exist.<br>- **w**: Open a file for writing. If the file exists, clear its
 *     content. If the file does not exist, create a file.<br>- **w+**: Open a file for both reading and writing. If the
 *     file exists, clear its content. If the file does not exist, create a file.<br>- **a**: Open a file in append mode
 *     for writing at the end of the file. If the file does not exist, create a file. If the file exists, write data to
 *     the end of the file (the original content of the file is reserved).<br>- **a+**: Open a file in append mode for
 *     reading or updating at the end of the file. If the file does not exist, create a file. If the file exists, write
 *     data to the end of the file (the original content of the file is reserved).
 * @returns { Promise<Stream> } Promise that returns the file stream.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.file.fs:fdopenStream
 */
declare function fdopenStream(fd: number, mode: string): Promise<Stream>;
/**
 * Opens a stream based on the file descriptor. This API uses an asynchronous callback to return the result.
 *
 * @param { number } fd - File descriptor of the target file.
 * @param { string } mode - - **r**: Open a file for reading. The file must exist.<br>- **r+**: Open a file for both
 *     reading and writing. The file must exist.<br>- **w**: Open a file for writing. If the file exists, clear its
 *     content. If the file does not exist, create a file.<br>- **w+**: Open a file for both reading and writing. If the
 *     file exists, clear its content. If the file does not exist, create a file.<br>- **a**: Open a file in append mode
 *     for writing at the end of the file. If the file does not exist, create a file. If the file exists, write data to
 *     the end of the file (the original content of the file is reserved).<br>- **a+**: Open a file in append mode for
 *     reading or updating at the end of the file. If the file does not exist, create a file. If the file exists, write
 *     data to the end of the file (the original content of the file is reserved).
 * @param { AsyncCallback<Stream> } [callback] - Callback invoked when the stream is opened asynchronously.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.file.fs:fdopenStream
 */
declare function fdopenStream(fd: number, mode: string, callback: AsyncCallback<Stream>): void;
/**
 * Opens a stream based on the file descriptor. This API returns the result synchronously.
 *
 * @param { number } fd - File descriptor of the target file.
 * @param { string } mode - - **r**: Open a file for reading. The file must exist.<br>- **r+**: Open a file for both
 *     reading and writing. The file must exist.<br>- **w**: Open a file for writing. If the file exists, clear its
 *     content. If the file does not exist, create a file.<br>- **w+**: Open a file for both reading and writing. If the
 *     file exists, clear its content. If the file does not exist, create a file.<br>- **a**: Open a file in append mode
 *     for writing at the end of the file. If the file does not exist, create a file. If the file exists, write data to
 *     the end of the file (the original content of the file is reserved).<br>- **a+**: Open a file in append mode for
 *     reading or updating at the end of the file. If the file does not exist, create a file. If the file exists, write
 *     data to the end of the file (the original content of the file is reserved).
 * @returns { Stream } File stream.
 * @throws { TypedError | Error } open fail
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.file.fs:fdopenStreamSync
 */
declare function fdopenStreamSync(fd: number, mode: string): Stream;
/**
 * Calculates the hash value of a file. This API uses a promise to return the result.
 *
 * @param { string } path - Application sandbox path of the file.
 * @param { string } algorithm - Algorithm used to calculate the hash value. The value can be **md5**, **sha1**, or
 *     **sha256**. **sha256** is recommended for security purposes.
 * @returns { Promise<string> } Promise that returns the hash value. The hash value is a hexadecimal string consisting
 *     of digits and uppercase letters.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 6
 * @deprecated since 9
 * @useinstead @ohos.file.hash:hash
 */
declare function hash(path: string, algorithm: string): Promise<string>;
/**
 * Calculates the hash value of a file. This API uses an asynchronous callback to return the result.
 *
 * @param { string } path - Application sandbox path of the file.
 * @param { string } algorithm - Algorithm used to calculate the hash value. The value can be **md5**, **sha1**, or
 *     **sha256**. **sha256** is recommended for security purposes.
 * @param { AsyncCallback<string> } [callback] - Callback used to return the hash value obtained. The hash value is a
 *     hexadecimal string consisting of digits and uppercase letters.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 6
 * @deprecated since 9
 * @useinstead @ohos.file.hash:hash
 */
declare function hash(path: string, algorithm: string, callback: AsyncCallback<string>): void;
/**
 * Changes the file owner (owner of the symbolic link, not the file referred to by the symbolic link) based on the file
 * path. This API uses a promise to return the result.
 *
 * @param { string } path - Application sandbox path of the file.
 * @param { number } uid - New UID.
 * @param { number } gid - New GID.
 * @returns { Promise<void> } Promise that returns no value.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 */
declare function lchown(path: string, uid: number, gid: number): Promise<void>;
/**
 * Changes the file owner (owner of the symbolic link, not the file referred to by the symbolic link) based on a file
 * path. This API uses an asynchronous callback to return the result.
 *
 * @param { string } path - Application sandbox path of the file.
 * @param { number } uid - New UID.
 * @param { number } gid - New GID.
 * @param { AsyncCallback<void> } [callback] - Callback invoked when the file owner is changed asynchronously.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 */
declare function lchown(path: string, uid: number, gid: number, callback: AsyncCallback<void>): void;
/**
 * Changes the file owner based on a file path and changes the owner of the symbolic link (not the referenced file).
 * This API returns the result synchronously.
 *
 * @param { string } path - Application sandbox path of the file.
 * @param { number } uid - New UID.
 * @param { number } gid - New GID.
 * @throws { TypedError | Error } lchown fail
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 */
declare function lchownSync(path: string, uid: number, gid: number): void;
/**
 * Obtains information about a symbolic link that is used to refer to a file or directory. This API uses a promise to
 * return the result.
 *
 * @param { string } path - Application sandbox path of the target file.
 * @returns { Promise<Stat> } Promise that returns the symbolic link information obtained. For details, see **stat**.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.file.fs:lstat
 */
declare function lstat(path: string): Promise<Stat>;
/**
 * Obtains information about a symbolic link that is used to refer to a file or directory. This API uses an asynchronous
 * callback to return the result.
 *
 * @param { string } path - Application sandbox path of the target file.
 * @param { AsyncCallback<Stat> } [callback] - Callback used to return the symbolic link information obtained.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.file.fs:lstat
 */
declare function lstat(path: string, callback: AsyncCallback<Stat>): void;
/**
 * Obtains information about a symbolic link that is used to refer to a file or directory. This API returns the result
 * synchronously.
 *
 * @param { string } path - Application sandbox path of the target file.
 * @returns { Stat } File information obtained.
 * @throws { TypedError | Error } lstat fail
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.file.fs:lstatSync
 */
declare function lstatSync(path: string): Stat;
/**
 * Creates a directory. This API uses a promise to return the result.
 *
 * @param { string } path - Application sandbox path of the directory.
 * @param { number } [mode] - Permission on the directory to create. You can specify multiple permissions, separated
 *     using a bitwise OR operator (|). The default value is **0o775**.<br>- **0o775**: The owner has the read, write,
 *     and execute permissions, and other users have the read and execute permissions.<br>- **0o700**: The owner has the
 *     read, write, and execute permissions.<br>- **0o400**: The owner has the read permission.<br>- **0o200**: The
 *     owner has the write permission.<br>- **0o100**: The owner has the execute permission.<br>- **0o070**: The user
 *     group has the read, write, and execute permissions.<br>- **0o040**: The user group has the read permission.<br>-
 *     **0o020**: The user group has the write permission.<br>- **0o010**: The user group has the execute permission.<br
 *     >- **0o007**: Other users have the read, write, and execute permissions.<br>- **0o004**: Other users have the
 *     read permission.<br>- **0o002**: Other users have the write permission.<br>- **0o001**: Other users have the
 *     execute permission.
 * @returns { Promise<void> } Promise that returns no value.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 6
 * @deprecated since 9
 * @useinstead @ohos.file.fs:mkdir
 */
declare function mkdir(path: string, mode?: number): Promise<void>;
/**
 * Creates a directory. This API uses an asynchronous callback to return the result.
 *
 * @param { string } path - Application sandbox path of the directory.
 * @param { AsyncCallback<void> } [callback] - Callback invoked when the directory is created asynchronously.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 6
 * @deprecated since 9
 * @useinstead @ohos.file.fs:mkdir
 */
declare function mkdir(path: string, callback: AsyncCallback<void>): void;
/**
 * Creates a directory. This API uses an asynchronous callback to return the result.
 *
 * @param { string } path - Application sandbox path of the directory.
 * @param { number } [mode] - Permission on the directory to create. You can specify multiple permissions, separated
 *     using a bitwise OR operator (|). The default value is **0o775**.<br>- **0o775**: The owner has the read, write,
 *     and execute permissions, and other users have the read and execute permissions.<br>- **0o700**: The owner has the
 *     read, write, and execute permissions.<br>- **0o400**: The owner has the read permission.<br>- **0o200**: The
 *     owner has the write permission.<br>- **0o100**: The owner has the execute permission.<br>- **0o070**: The user
 *     group has the read, write, and execute permissions.<br>- **0o040**: The user group has the read permission.<br>-
 *     **0o020**: The user group has the write permission.<br>- **0o010**: The user group has the execute permission.<br
 *     >- **0o007**: Other users have the read, write, and execute permissions.<br>- **0o004**: Other users have the
 *     read permission.<br>- **0o002**: Other users have the write permission.<br>- **0o001**: Other users have the
 *     execute permission.
 * @param { AsyncCallback<void> } [callback] - Callback invoked when the directory is created asynchronously.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 6
 * @deprecated since 9
 * @useinstead @ohos.file.fs:mkdir
 */
declare function mkdir(path: string, mode: number, callback: AsyncCallback<void>): void;
/**
 * Creates a directory. This API returns the result synchronously.
 *
 * @param { string } path - Application sandbox path of the directory.
 * @param { number } [mode] - Permission on the directory to create. You can specify multiple permissions, separated
 *     using a bitwise OR operator (|). The default value is **0o775**.<br>- **0o775**: The owner has the read, write,
 *     and execute permissions, and other users have the read and execute permissions.<br>- **0o700**: The owner has the
 *     read, write, and execute permissions.<br>- **0o400**: The owner has the read permission.<br>- **0o200**: The
 *     owner has the write permission.<br>- **0o100**: The owner has the execute permission.<br>- **0o070**: The user
 *     group has the read, write, and execute permissions.<br>- **0o040**: The user group has the read permission.<br>-
 *     **0o020**: The user group has the write permission.<br>- **0o010**: The user group has the execute permission.<br
 *     >- **0o007**: Other users have the read, write, and execute permissions.<br>- **0o004**: Other users have the
 *     read permission.<br>- **0o002**: Other users have the write permission.<br>- **0o001**: Other users have the
 *     execute permission.
 * @throws { TypedError | Error } mkdir fail
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 6
 * @deprecated since 9
 * @useinstead @ohos.file.fs:mkdirSync
 */
declare function mkdirSync(path: string, mode?: number): void;
/**
 * Creates a temporary directory. This API uses a promise to return the result.
 *
 * @param { string } prefix - String to be replaced with six randomly generated characters to create a unique temporary
 *     directory.
 * @returns { Promise<string> } Promise that returns the directory created.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.file.fs:mkdtemp
 */
declare function mkdtemp(prefix: string): Promise<string>;
/**
 * Creates a temporary directory. This API uses an asynchronous callback to return the result.
 *
 * @param { string } prefix - String to be replaced with six randomly generated characters to create a unique temporary
 *     directory.
 * @param { AsyncCallback<string> } [callback] - Callback invoked when a temporary directory is created asynchronously.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.file.fs:mkdtemp
 */
declare function mkdtemp(prefix: string, callback: AsyncCallback<string>): void;
/**
 * Creates a temporary directory. This API returns the result synchronously.
 *
 * @param { string } prefix - String to be replaced with six randomly generated characters to create a unique temporary
 *     directory.
 * @returns { string } Unique directory generated.
 * @throws { TypedError | Error } mkdtemp fail
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.file.fs:mkdtempSync
 */
declare function mkdtempSync(prefix: string): string;
/**
 * Opens a file. This API uses a promise to return the result.
 *
 * @param { string } path - Application sandbox path of the file.
 * @param { number } [flags] - Option for opening the file. You must specify one of the following options. By default,
 *     the file is opened in read-only mode.<br>- **0o0**: Open the file in read-only mode.<br>- **0o1**: Open the file
 *     in write-only mode.<br>- **0o2**: Open the file in read/write mode.<br>In addition, you can specify the following
 *     options, separated using a bitwise OR operator (|). By default, no additional option is specified.<br>- **0o100**
 *     : If the file does not exist, create it. If you use this option, you must also specify **mode**.<br>- **0o200**:
 *     If **0o100** is added and the file already exists, throw an exception.<br>- **0o1000**: If the file exists and is
 *     opened in write mode, truncate the file length to 0.<br>- **0o2000**: Open the file in append mode. New data will
 *     be appended to the file (added to the end of the file).<br>- **0o4000**: If **path** points to a named pipe (also
 *     known as a FIFO), block special file, or character special file, perform non-blocking operations on the open file
 *     and in subsequent I/Os.<br>- **0o200000**: If **path** does not point to a directory, throw an exception.<br>-
 *     **0o400000**: If **path** points to a symbolic link, throw an exception.<br>- **0o4010000**: Open the file in
 *     synchronous I/O mode.
 * @param { number } [mode] - Permissions on the file. You can specify multiple permissions, separated using a bitwise
 *     OR operator (|). The default value is **0o660**.<br>- **0o660**: The owner and user group have the read and write
 *     permissions.<br>- **0o700**: The owner has the read, write, and execute permissions.<br>- **0o400**: The owner
 *     has the read permission.<br>- **0o200**: The owner has the write permission.<br>- **0o100**: The owner has the
 *     execute permission.<br>- **0o070**: The user group has the read, write, and execute permissions.<br>- **0o040**:
 *     The user group has the read permission.<br>- **0o020**: The user group has the write permission.<br>- **0o010**:
 *     The user group has the execute permission.<br>- **0o007**: Other users have the read, write, and execute
 *     permissions.<br>- **0o004**: Other users have the read permission.<br>- **0o002**: Other users have the write
 *     permission.<br>- **0o001**: Other users have the execute permission.
 * @returns { Promise<number> } Promise that returns the file descriptor of the file opened.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.file.fs:open
 */
declare function open(path: string, flags?: number, mode?: number): Promise<number>;
/**
 * Opens a file. This API uses an asynchronous callback to return the result.
 *
 * @param { string } path - Application sandbox path of the file.
 * @param { AsyncCallback<number> } [callback] - Callback invoked when the file is opened asynchronously, which is used
 *     to return the file descriptor.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.file.fs:open
 */
declare function open(path: string, callback: AsyncCallback<number>): void;
/**
 * Opens a file. This API uses an asynchronous callback to return the result.
 *
 * @param { string } path - Application sandbox path of the file.
 * @param { number } [flags] - Option for opening the file. You must specify one of the following options. By default,
 *     the file is opened in read-only mode.<br>- **0o0**: Open the file in read-only mode.<br>- **0o1**: Open the file
 *     in write-only mode.<br>- **0o2**: Open the file in read/write mode.<br>In addition, you can specify the following
 *     options, separated using a bitwise OR operator (|). By default, no additional option is specified.<br>- **0o100**
 *     : If the file does not exist, create it. If you use this option, you must also specify **mode**.<br>- **0o200**:
 *     If **0o100** is added and the file already exists, throw an exception.<br>- **0o1000**: If the file exists and is
 *     opened in write mode, truncate the file length to 0.<br>- **0o2000**: Open the file in append mode. New data will
 *     be appended to the file (added to the end of the file).<br>- **0o4000**: If **path** points to a named pipe (also
 *     known as a FIFO), block special file, or character special file, perform non-blocking operations on the open file
 *     and in subsequent I/Os.<br>- **0o200000**: If **path** does not point to a directory, throw an exception.<br>-
 *     **0o400000**: If **path** points to a symbolic link, throw an exception.<br>- **0o4010000**: Open the file in
 *     synchronous I/O mode.
 * @param { AsyncCallback<number> } [callback] - Callback invoked when the file is opened asynchronously, which is used
 *     to return the file descriptor.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.file.fs:open
 */
declare function open(path: string, flags: number, callback: AsyncCallback<number>): void;
/**
 * Opens a file. This API uses an asynchronous callback to return the result.
 *
 * @param { string } path - Application sandbox path of the file.
 * @param { number } [flags] - Option for opening the file. You must specify one of the following options. By default,
 *     the file is opened in read-only mode.<br>- **0o0**: Open the file in read-only mode.<br>- **0o1**: Open the file
 *     in write-only mode.<br>- **0o2**: Open the file in read/write mode.<br>In addition, you can specify the following
 *     options, separated using a bitwise OR operator (|). By default, no additional option is specified.<br>- **0o100**
 *     : If the file does not exist, create it. If you use this option, you must also specify **mode**.<br>- **0o200**:
 *     If **0o100** is added and the file already exists, throw an exception.<br>- **0o1000**: If the file exists and is
 *     opened in write mode, truncate the file length to 0.<br>- **0o2000**: Open the file in append mode. New data will
 *     be appended to the file (added to the end of the file).<br>- **0o4000**: If **path** points to a named pipe (also
 *     known as a FIFO), block special file, or character special file, perform non-blocking operations on the open file
 *     and in subsequent I/Os.<br>- **0o200000**: If **path** does not point to a directory, throw an exception.<br>-
 *     **0o400000**: If **path** points to a symbolic link, throw an exception.<br>- **0o4010000**: Open the file in
 *     synchronous I/O mode.
 * @param { number } [mode] - Permissions on the file. You can specify multiple permissions, separated using a bitwise
 *     OR operator (|). The default value is **0o660**.<br>- **0o660**: The owner and user group have the read and write
 *     permissions.<br>- **0o700**: The owner has the read, write, and execute permissions.<br>- **0o400**: The owner
 *     has the read permission.<br>- **0o200**: The owner has the write permission.<br>- **0o100**: The owner has the
 *     execute permission.<br>- **0o070**: The user group has the read, write, and execute permissions.<br>- **0o040**:
 *     The user group has the read permission.<br>- **0o020**: The user group has the write permission.<br>- **0o010**:
 *     The user group has the execute permission.<br>- **0o007**: Other users have the read, write, and execute
 *     permissions.<br>- **0o004**: Other users have the read permission.<br>- **0o002**: Other users have the write
 *     permission.<br>- **0o001**: Other users have the execute permission.
 * @param { AsyncCallback<number> } [callback] - Callback invoked when the file is opened asynchronously, which is used
 *     to return the file descriptor.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.file.fs:open
 */
declare function open(path: string, flags: number, mode: number, callback: AsyncCallback<number>): void;
/**
 * Opens a file. This API returns the result synchronously.
 *
 * @param { string } path - Application sandbox path of the file.
 * @param { number } [flags] - Option for opening the file. You must specify one of the following options. By default,
 *     the file is opened in read-only mode.<br>- **0o0**: Open the file in read-only mode.<br>- **0o1**: Open the file
 *     in write-only mode.<br>- **0o2**: Open the file in read/write mode.<br>In addition, you can specify the following
 *     options, separated using a bitwise OR operator (|). By default, no additional option is specified.<br>- **0o100**
 *     : If the file does not exist, create it. If you use this option, you must also specify **mode**.<br>- **0o200**:
 *     If **0o100** is added and the file already exists, throw an exception.<br>- **0o1000**: If the file exists and is
 *     opened in write mode, truncate the file length to 0.<br>- **0o2000**: Open the file in append mode. New data will
 *     be appended to the file (added to the end of the file).<br>- **0o4000**: If **path** points to a named pipe (also
 *     known as a FIFO), block special file, or character special file, perform non-blocking operations on the open file
 *     and in subsequent I/Os.<br>- **0o200000**: If **path** does not point to a directory, throw an exception.<br>-
 *     **0o400000**: If **path** points to a symbolic link, throw an exception.<br>- **0o4010000**: Open the file in
 *     synchronous I/O mode.
 * @param { number } [mode] - Permissions on the file. You can specify multiple permissions, separated using a bitwise
 *     OR operator (|). The default value is **0o660**.<br>- **0o660**: The owner and user group have the read and write
 *     permissions.<br>- **0o640**: The owner has the read and write permissions, and the user group has the read
 *     permission.<br>- **0o700**: The owner has the read, write, and execute permissions.<br>- **0o400**: The owner has
 *     the read permission.<br>- **0o200**: The owner has the write permission.<br>- **0o100**: The owner has the
 *     execute permission.<br>- **0o070**: The user group has the read, write, and execute permissions.<br>- **0o040**:
 *     The user group has the read permission.<br>- **0o020**: The user group has the write permission.<br>- **0o010**:
 *     The user group has the execute permission.<br>- **0o007**: Other users have the read, write, and execute
 *     permissions.<br>- **0o004**: Other users have the read permission.<br>- **0o002**: Other users have the write
 *     permission.<br>- **0o001**: Other users have the execute permission.<br>The file permissions on newly created
 *     files are affected by umask, which is set as the process starts. Currently, the modification of umask is not
 *     open.
 * @returns { number } File descriptor of the file opened.
 * @throws { TypedError | Error } open fail
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 6
 * @deprecated since 9
 * @useinstead @ohos.file.fs:openSync
 */
declare function openSync(path: string, flags?: number, mode?: number): number;
/**
 * Opens a directory. This API uses a promise to return the result.
 *
 * @param { string } path - Application sandbox path of the directory to open.
 * @returns { Promise<Dir> } Promise that returns the **Dir** object opened.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 6
 * @deprecated since 9
 * @useinstead @ohos.file.fs:listFile
 */
declare function opendir(path: string): Promise<Dir>;
/**
 * Opens a file directory. This API uses an asynchronous callback to return the result.
 *
 * @param { string } path - Application sandbox path of the directory to open.
 * @param { AsyncCallback<Dir> } [callback] - Callback invoked when the directory is opened asynchronously.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 6
 * @deprecated since 9
 * @useinstead @ohos.file.fs:listFile
 */
declare function opendir(path: string, callback: AsyncCallback<Dir>): void;
/**
 * Opens a directory. This API returns the result synchronously.
 *
 * @param { string } path - Application sandbox path of the directory to open.
 * @returns { Dir } **Dir** object opened.
 * @throws { TypedError | Error } opendir fail
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 6
 * @deprecated since 9
 * @useinstead @ohos.file.fs:listFileSync
 */
declare function opendirSync(path: string): Dir;
/**
 * Reads the text content of a file. This API uses a promise to return the result.
 *
 * @param { string } filePath - Application sandbox path of the file to read.
 * @param { object } [options] - The options are as follows:<br>- **position** (number): position of the data to read in
 *     the file, in bytes. This parameter is optional. By default, data is read from the current position.<br>-
 *     **length** (number): length of the data to read, in bytes. This parameter is optional. The default value is the
 *     buffer length minus the offset.<br>- **encoding** (string): format of the data to be encoded.<br>It is valid only
 *     when the data is of the string type.<br>The default value is **'utf-8'**, which is the only value supported.
 * @returns { Promise<string> } Promise that returns the file content read.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.file.fs:readText
 */
declare function readText(filePath: string, options?: {
    position?: number;
    length?: number;
    encoding?: string;
}): Promise<string>;
/**
 * Reads the text content of a file. This API uses an asynchronous callback to return the result.
 *
 * @param { string } filePath - Application sandbox path of the file to read.
 * @param { object } [options] - The options are as follows:<br>- **position** (number): position of the data to read in
 *     the file, in bytes. This parameter is optional. By default, data is read from the current position.<br>-
 *     **length** (number): length of the data to read, in bytes. This parameter is optional. The default value is the
 *     buffer length minus the offset.<br>- **encoding**: format of the data to be encoded. The default value is
 *     **'utf-8'**, which is the only value supported.
 * @param { AsyncCallback<string> } [callback] - Callback used to return the file content read.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.file.fs:readText
 */
declare function readText(filePath: string, options: {
    position?: number;
    length?: number;
    encoding?: string;
}, callback: AsyncCallback<string>): void;
/**
 * Reads the text content of a file. This API returns the result synchronously.
 *
 * @param { string } filePath - Application sandbox path of the file to read.
 * @param { object } [options] - The options are as follows:<br>- **position** (number): position of the data to read in
 *     the file, in bytes. This parameter is optional. By default, data is read from the current position.<br>-
 *     **length** (number): length of the data to read, in bytes. This parameter is optional. The default value is the
 *     buffer length minus the offset.<br>- **encoding** (string): format of the data to be encoded.<br>It is valid only
 *     when the data is of the string type.<br>The default value is **'utf-8'**, which is the only value supported.
 * @returns { string } File content read.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.file.fs:readTextSync
 */
declare function readTextSync(filePath: string, options?: {
    position?: number;
    length?: number;
    encoding?: string;
}): string;
/**
 * Reads data from a file. This API uses a promise to return the result.
 *
 * @param { number } fd - File descriptor of the file to read.
 * @param { ArrayBuffer } buffer - Buffer used to store the file data read.
 * @param { object } [options] - The options are as follows:<br>- **offset** (number): position to store the data read
 *     in the buffer relative to the start address of the buffer, in bytes. This parameter is optional. The default
 *     value is **0**.<br>- **length** (number): length of the data to read. This parameter is optional. The default
 *     value is the buffer length minus the offset, in bytes.<br>- **position** (number): position of the data to read
 *     in the file. This parameter is optional. By default, data is read from the current position, in bytes.<br>
 *     Constraints: offset + length <= Buffer size
 * @returns { Promise<ReadOut> } Promise that returns the data read.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 6
 * @deprecated since 9
 * @useinstead @ohos.file.fs:read
 */
declare function read(fd: number, buffer: ArrayBuffer, options?: {
    offset?: number;
    length?: number;
    position?: number;
}): Promise<ReadOut>;
/**
 * Reads data from a file. This API uses an asynchronous callback to return the result.
 *
 * @param { number } fd - File descriptor of the file to read.
 * @param { ArrayBuffer } buffer - Buffer used to store the file data read.
 * @param { AsyncCallback<ReadOut> } [callback] - Callback invoked when the data is read asynchronously.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 6
 * @deprecated since 9
 * @useinstead @ohos.file.fs:read
 */
declare function read(fd: number, buffer: ArrayBuffer, callback: AsyncCallback<ReadOut>): void;
/**
 * Reads data from a file. This API uses an asynchronous callback to return the result.
 *
 * @param { number } fd - File descriptor of the file to read.
 * @param { ArrayBuffer } buffer - Buffer used to store the file data read.
 * @param { object } [options] - The options are as follows:<br>- **offset** (number): byte offset from the start of the
 *     buffer where the read data is stored. This parameter is optional. The default value is **0**.<br>- **length** (
 *     number): length of the data to read, in bytes. This parameter is optional. The default value is the buffer length
 *     minus the offset.<br>- **position** (number): position in the file to read from, in bytes. This parameter is
 *     optional. By default, data is read from the current position.<br>Constraints: offset + length <= Buffer size
 * @param { AsyncCallback<ReadOut> } [callback] - Callback invoked when the data is read asynchronously.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 6
 * @deprecated since 9
 * @useinstead @ohos.file.fs:read
 */
declare function read(fd: number, buffer: ArrayBuffer, options: {
    offset?: number;
    length?: number;
    position?: number;
}, callback: AsyncCallback<ReadOut>): void;
/**
 * Reads data from a file. This API returns the result synchronously.
 *
 * @param { number } fd - File descriptor of the file to read.
 * @param { ArrayBuffer } buffer - Buffer used to store the file data read.
 * @param { object } [options] - The options are as follows:<br>- **offset** (number): position to store the data read
 *     in the buffer relative to the start address of the buffer, in bytes. This parameter is optional. The default
 *     value is **0**.<br>- **length** (number): length of the data to read. This parameter is optional. The default
 *     value is the buffer length minus the offset, in bytes.<br>- **position** (number): position of the data to read
 *     in the file. This parameter is optional. By default, data is read from the current position, in bytes.<br>
 *     Constraints: offset + length <= Buffer size
 * @returns { number } Length of the data read, in bytes.
 * @throws { TypedError | Error } read fail
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 6
 * @deprecated since 9
 * @useinstead @ohos.file.fs:readSync
 */
declare function readSync(fd: number, buffer: ArrayBuffer, options?: {
    offset?: number;
    length?: number;
    position?: number;
}): number;
/**
 * Renames a file. This API uses a promise to return the result.
 *
 * @param { string } oldPath - Application sandbox path of the file to rename.
 * @param { string } newPath - Application sandbox path of the file renamed.
 * @returns { Promise<void> } Promise that returns no value.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.file.fs:rename
 */
declare function rename(oldPath: string, newPath: string): Promise<void>;
/**
 * Renames a file. This API uses an asynchronous callback to return the result.
 *
 * @param { string } oldPath - Application sandbox path of the file to rename.
 * @param { string } newPath - Application sandbox path of the file renamed.
 * @param { AsyncCallback<void> } [callback] - Callback invoked when the file is asynchronously renamed.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.file.fs:rename
 */
declare function rename(oldPath: string, newPath: string, callback: AsyncCallback<void>): void;
/**
 * Renames a file. This API returns the result synchronously.
 *
 * @param { string } oldPath - Application sandbox path of the file to rename.
 * @param { string } newPath - Application sandbox path of the file renamed.
 * @throws { TypedError | Error } rename fail
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.file.fs:renameSync
 */
declare function renameSync(oldPath: string, newPath: string): void;
/**
 * Removes a directory. This API uses a promise to return the result.
 *
 * @param { string } path - Application sandbox path of the directory.
 * @returns { Promise<void> } Promise that returns no value.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.file.fs:rmdir
 */
declare function rmdir(path: string): Promise<void>;
/**
 * Removes a directory. This API uses an asynchronous callback to return the result.
 *
 * @param { string } path - Application sandbox path of the directory.
 * @param { AsyncCallback<void> } [callback] - Callback invoked when a directory is removed asynchronously.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.file.fs:rmdir
 */
declare function rmdir(path: string, callback: AsyncCallback<void>): void;
/**
 * Removes a directory. This API returns the result synchronously.
 *
 * @param { string } path - Application sandbox path of the directory.
 * @throws { TypedError | Error } rmdir fail
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.file.fs:rmdirSync
 */
declare function rmdirSync(path: string): void;
/**
 * Obtains file information. This API uses a promise to return the result.
 *
 * @param { string } path - Application sandbox path of the file.
 * @returns { Promise<Stat> } Promise that returns the file information obtained.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 6
 * @deprecated since 9
 * @useinstead @ohos.file.fs:stat
 */
declare function stat(path: string): Promise<Stat>;
/**
 * Obtains file information. This API uses an asynchronous callback to return the result.
 *
 * @param { string } path - Application sandbox path of the file.
 * @param { AsyncCallback<Stat> } [callback] - Callback used to return the file information obtained.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 6
 * @deprecated since 9
 * @useinstead @ohos.file.fs:stat
 */
declare function stat(path: string, callback: AsyncCallback<Stat>): void;
/**
 * Obtains file information. This API returns the result synchronously.
 *
 * @param { string } path - Application sandbox path of the file.
 * @returns { Stat } File information obtained.
 * @throws { TypedError | Error } stat fail
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 6
 * @deprecated since 9
 * @useinstead @ohos.file.fs:statSync
 */
declare function statSync(path: string): Stat;
/**
 * Creates a symbolic link based on the file path. This API uses a promise to return the result.
 *
 * @param { string } target - Application sandbox path of the target file.
 * @param { string } srcPath - Application sandbox path of the symbolic link.
 * @returns { Promise<void> } Promise that returns no value.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.file.fs:symlink
 */
declare function symlink(target: string, srcPath: string): Promise<void>;
/**
 * Creates a symbolic link based on the file path. This API uses an asynchronous callback to return the result.
 *
 * @param { string } target - Application sandbox path of the target file.
 * @param { string } srcPath - Application sandbox path of the symbolic link.
 * @param { AsyncCallback<void> } [callback] - Callback invoked when the symbolic link is created asynchronously.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.file.fs:symlink
 */
declare function symlink(target: string, srcPath: string, callback: AsyncCallback<void>): void;
/**
 * Creates a symbolic link based on the file path. This API returns the result synchronously.
 *
 * @param { string } target - Application sandbox path of the target file.
 * @param { string } srcPath - Application sandbox path of the symbolic link.
 * @throws { TypedError | Error } symlink fail
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.file.fs:symlinkSync
 */
declare function symlinkSync(target: string, srcPath: string): void;
/**
 * Truncates a file based on the file path. This API uses a promise to return the result.
 *
 * @param { string } path - Application sandbox path of the file to truncate.
 * @param { number } [len] - File length after truncation, in bytes. The default value is **0**.
 * @returns { Promise<void> } Promise that returns no value.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.file.fs:truncate
 */
declare function truncate(path: string, len?: number): Promise<void>;
/**
 * Truncates a file based on the file path. This API uses an asynchronous callback to return the result.
 *
 * @param { string } path - Application sandbox path of the file to truncate.
 * @param { AsyncCallback<void> } [callback] - Callback that returns no value.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.file.fs:truncate
 */
declare function truncate(path: string, callback: AsyncCallback<void>): void;
/**
 * Truncates a file based on the file path. This API uses an asynchronous callback to return the result.
 *
 * @param { string } path - Application sandbox path of the file to truncate.
 * @param { number } [len] - File length after truncation, in bytes. The default value is **0**.
 * @param { AsyncCallback<void> } [callback] - Callback that returns no value.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.file.fs:truncate
 */
declare function truncate(path: string, len: number, callback: AsyncCallback<void>): void;
/**
 * Truncates a file based on the file path. This API returns the result synchronously.
 *
 * @param { string } path - Application sandbox path of the file to truncate.
 * @param { number } [len] - File length after truncation, in bytes. The default value is **0**.
 * @throws { TypedError | Error } truncate fail
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 9
 * @useinstead @ohos.file.fs:truncateSync
 */
declare function truncateSync(path: string, len?: number): void;
/**
 * Removes a file. This API uses a promise to return the result.
 *
 * @param { string } path - Application sandbox path of the file.
 * @returns { Promise<void> } Promise that returns no value.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 6
 * @deprecated since 9
 * @useinstead @ohos.file.fs:unlink
 */
declare function unlink(path: string): Promise<void>;
/**
 * Removes a file. This API uses an asynchronous callback to return the result.
 *
 * @param { string } path - Application sandbox path of the file.
 * @param { AsyncCallback<void> } [callback] - Callback invoked when the file is removed asynchronously.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 6
 * @deprecated since 9
 * @useinstead @ohos.file.fs:unlink
 */
declare function unlink(path: string, callback: AsyncCallback<void>): void;
/**
 * Removes a file. This API returns the result synchronously.
 *
 * @param { string } path - Application sandbox path of the file.
 * @throws { TypedError | Error } unlink fail
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 6
 * @deprecated since 9
 * @useinstead @ohos.file.fs:unlinkSync
 */
declare function unlinkSync(path: string): void;
/**
 * Writes data into a file. This API uses a promise to return the result.
 *
 * @param { number } fd - File descriptor of the file to write.
 * @param { ArrayBuffer | string } buffer - Data to write. It can be a string or data from a buffer.
 * @param { object } [options] - The options are as follows:<br>- **offset** (number): offset of the write position
 *     relative to the start address of the data, in bytes. This parameter is optional. The default value is **0**.<br>-
 *     **length** (number): length of the data to write, in bytes. This parameter is optional. The default value is the
 *     buffer length minus the offset.<br>- **position** (number): start position to write the data into the file, in
 *     bytes. This parameter is optional. By default, data is written from the current position.<br>- **encoding** (
 *     string): format of the data to be encoded when the data is a string. The default value is **'utf-8'**, which is
 *     the only value supported.<br>Constraints: offset + length <= Buffer size
 * @returns { Promise<number> } Promise that returns the length of the data written, in bytes.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 6
 * @deprecated since 9
 * @useinstead @ohos.file.fs:write
 */
declare function write(fd: number, buffer: ArrayBuffer | string, options?: {
    offset?: number;
    length?: number;
    position?: number;
    encoding?: string;
}): Promise<number>;
/**
 * Writes data to a file. This API uses an asynchronous callback to return the result.
 *
 * @param { number } fd - File descriptor of the file to write.
 * @param { ArrayBuffer | string } buffer - Data to write. It can be a string or data from a buffer.
 * @param { AsyncCallback<number> } [callback] - Callback invoked when the data is written asynchronously. return the
 *     length of the data written, in bytes.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 6
 * @deprecated since 9
 * @useinstead @ohos.file.fs:write
 */
declare function write(fd: number, buffer: ArrayBuffer | string, callback: AsyncCallback<number>): void;
/**
 * Writes data to a file. This API uses an asynchronous callback to return the result.
 *
 * @param { number } fd - File descriptor of the file to write.
 * @param { ArrayBuffer | string } buffer - Data to write. It can be a string or data from a buffer.
 * @param { object } [options] - The options are as follows:<br>- **offset** (number): offset of the write position
 *     relative to the start address of the data, in bytes. This parameter is optional. The default value is **0**.<br>-
 *     **length** (number): length of the data to write, in bytes. This parameter is optional. The default value is the
 *     buffer length minus the offset.<br>- **position** (number): start position to write the data into the file, in
 *     bytes. This parameter is optional. By default, data is written from the current position.<br>- **encoding** (
 *     string): format of the data to be encoded when the data is a string. The default value is **'utf-8'**, which is
 *     the only value supported.<br>Constraints: offset + length <= Buffer size
 * @param { AsyncCallback<number> } [callback] - Callback invoked when the data is written asynchronously. return the
 *     length of the data written, in bytes.
 * @throws { TypedError } Parameter check failed
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 6
 * @deprecated since 9
 * @useinstead @ohos.file.fs:write
 */
declare function write(fd: number, buffer: ArrayBuffer | string, options: {
    offset?: number;
    length?: number;
    position?: number;
    encoding?: string;
}, callback: AsyncCallback<number>): void;
/**
 * Writes data to a file. This API returns the result synchronously.
 *
 * @param { number } fd - File descriptor of the file to write.
 * @param { ArrayBuffer | string } buffer - Data to write. It can be a string or data from a buffer.
 * @param { object } [options] - The options are as follows:<br>- **offset** (number): offset of the write position
 *     relative to the start address of the data, in bytes. This parameter is optional. The default value is **0**.<br>-
 *     **length** (number): length of the data to write, in bytes. This parameter is optional. The default value is the
 *     buffer length minus the offset.<br>- **position** (number): start position to write the data into the file, in
 *     bytes. This parameter is optional. By default, data is written from the current position.<br>- **encoding** (
 *     string): format of the data to be encoded when the data is a string. The default value is **'utf-8'**, which is
 *     the only value supported.<br>Constraints: offset + length <= Buffer size
 * @returns { number } Length of the data written in the file, in bytes.
 * @throws { TypedError | Error } write fail
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 6
 * @deprecated since 9
 * @useinstead @ohos.file.fs:writeSync
 */
declare function writeSync(fd: number, buffer: ArrayBuffer | string, options?: {
    offset?: number;
    length?: number;
    position?: number;
    encoding?: string;
}): number;
/**
 * Listens for file or directory changes. This API uses an asynchronous callback to return the result.
 *
 * @param { string } filename - Application sandbox path of the file.
 * @param { number } events - - **1**: The file or directory is renamed.<br>- **2**: The file or directory is modified.<
 *     br>- **3**: The file or directory is modified and renamed.
 * @param { AsyncCallback<number> } [callback] - Called each time a change is detected.
 * @returns { Watcher } Promise that returns the file change.
 * @throws { TypedError | Error } watch fail
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 10
 * @useinstead @ohos.file.fs:createWatcher
 */
declare function createWatcher(filename: string, events: number, callback: AsyncCallback<number>): Watcher;
/**
 * Manages directories. Before calling a method of the **Dir** class, use the **opendir()** method synchronously or
 * asynchronously to create a **Dir** instance.
 *
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 6
 * @deprecated since 9
 * @useinstead @ohos.file.fs:listFile
 */
declare interface Dir {
    /**
     * Reads the next directory entry. This API uses a promise to return the result.
     *
     * @returns { Promise<Dirent> } Promise that returns the next directory entry.
     * @throws { TypedError } Parameter check failed if read to end, Error.msg = "NoMore"
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 6
     * @deprecated since 9
     * @useinstead @ohos.file.fs:listFile
     */
    read(): Promise<Dirent>;
    /**
     * Reads the next directory entry. This API uses an asynchronous callback to return the result.
     *
     * @param { AsyncCallback<Dirent> } [callback] - Callback invoked when the next directory entry is asynchronously
     *     read.
     * @throws { TypedError } Parameter check failed if read to end, Error.msg = "NoMore"
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 6
     * @deprecated since 9
     * @useinstead @ohos.file.fs:listFile
     */
    read(callback: AsyncCallback<Dirent>): void;
    /**
     * Reads the next directory entry. This API returns the result synchronously.
     *
     * @returns { Dirent } Directory entry read.
     * @throws { TypedError | Error } read fail if read to end, Error.msg = "NoMore"
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 6
     * @deprecated since 9
     * @useinstead @ohos.file.fs:listFile
     */
    readSync(): Dirent;
    /**
     * Closes a directory. This API uses a promise to return the result. After a directory is closed, the file descriptor
     * in **Dir** will be released and no directory entry can be read from **Dir**.
     *
     * @returns { Promise<void> } return Promise
     * @throws { TypedError } close fail
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.file.fs:listFile
     */
    close(): Promise<void>;
    /**
     * Closes a directory. This API uses an asynchronous callback to return the result. After a directory is closed, the
     * file descriptor in **Dir** will be released and no directory entry can be read from **Dir**.
     *
     * @param { AsyncCallback<void> } [callback] - callback.
     * @throws { TypedError } close fail
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.file.fs:listFile
     */
    close(callback: AsyncCallback<void>): void;
    /**
     * Closes a directory. After a directory is closed, the file descriptor in **Dir** will be released and no directory
     * entry can be read from **Dir**.
     *
     * @throws { TypedError | Error } close fail
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 6
     * @deprecated since 9
     * @useinstead @ohos.file.fs:listFile
     */
    closeSync(): void;
}
/**
 * Provides information about files and directories. Before calling an API of the **Dirent** class, use
 * [dir.read()]{@link read} synchronously or asynchronously to create a **Dirent** instance.
 *
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 6
 * @deprecated since 9
 * @useinstead @ohos.file.fs:listFile
 */
declare interface Dirent {
    /**
     * Directory entry name.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 6
     * @deprecated since 9
     * @useinstead @ohos.file.fs:listFile
     */
    readonly name: string;
    /**
     * Checks whether this directory entry is a block special file. A block special file supports access by block only,
     * and it is cached when accessed.
     *
     * @returns { boolean } Returns **true** if it is a block special file; returns **false** otherwise.
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 6
     * @deprecated since 9
     * @useinstead @ohos.file.fs:listFile
     */
    isBlockDevice(): boolean;
    /**
     * Checks whether this directory entry is a character special file. A character special file supports random access,
     * and it is not cached when accessed.
     *
     * @returns { boolean } Returns **true** if it is a character special file; returns **false** otherwise.
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 6
     * @deprecated since 9
     * @useinstead @ohos.file.fs:listFile
     */
    isCharacterDevice(): boolean;
    /**
     * Checks whether this directory entry is a directory.
     *
     * @returns { boolean } Returns **true** if it is a directory; returns **false** otherwise.
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 6
     * @deprecated since 9
     * @useinstead @ohos.file.fs:listFile
     */
    isDirectory(): boolean;
    /**
     * Checks whether this directory entry is a named pipe (also called FIFO). Named pipes are used for inter-process
     * communication.
     *
     * @returns { boolean } Returns **true** if it is a named pipe; returns **false** otherwise.
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 6
     * @deprecated since 9
     * @useinstead @ohos.file.fs:listFile
     */
    isFIFO(): boolean;
    /**
     * Checks whether this directory entry is a regular file.
     *
     * @returns { boolean } Returns **true** if it is a regular file; returns **false** otherwise.
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 6
     * @deprecated since 9
     * @useinstead @ohos.file.fs:listFile
     */
    isFile(): boolean;
    /**
     * Checks whether this directory entry is a socket.
     *
     * @returns { boolean } Returns **true** if it is a socket; returns **false** otherwise.
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 6
     * @deprecated since 9
     * @useinstead @ohos.file.fs:listFile
     */
    isSocket(): boolean;
    /**
     * Checks whether this directory entry is a symbolic link.
     *
     * @returns { boolean } Returns **true** if it is a symbolic link; returns **false** otherwise.
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 6
     * @deprecated since 9
     * @useinstead @ohos.file.fs:listFile
     */
    isSymbolicLink(): boolean;
}
/**
 * Provides detailed file information. Before calling a method of the **Stat** class, use the [stat()]{@link stat}
 * method synchronously or asynchronously to create a **Stat** instance.
 *
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 6
 * @deprecated since 9
 * @useinstead @ohos.file.fs:Stat
 */
declare interface Stat {
    /**
     * Major device number.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 6
     * @deprecated since 9
     */
    readonly dev: number;
    /**
     * File identifier, which varies with files on the same device.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 6
     * @deprecated since 9
     * @useinstead ohos.file.fs.Stat.ino
     */
    readonly ino: number;
    /**
     * File type and permissions. The first four bits indicate the file type, and the last 12 bits indicate the
     * permissions. The bit fields are described as follows:
     * - **0o170000**: mask used to obtain the file type.
     * - **0o140000**: The file is a socket.
     * - **0o120000**: The file is a symbolic link.
     * - **0o100000**: The file is a regular file.
     * - **0o060000**: The file is a block device.
     * - **0o040000**: The file is a directory.
     * - **0o020000**: The file is a character device.
     * - **0o010000**: The file is a named pipe (FIFO).
     * - **0o0700**: mask used to obtain the owner permissions.
     * - **0o0400**: The owner has the permission to read a regular file or a directory entry.
     * - **0o0200**: The owner has the permission to write a regular file or create and delete a directory entry.
     * - **0o0100**: The owner has the permission to execute a regular file or search for the specified path in a
     * directory.
     * - **0o0070**: mask used to obtain the user group permissions.
     * - **0o0040**: The user group has the permission to read a regular file or a directory entry.
     * - **0o0020**: The user group has the permission to write a regular file or create and delete a directory entry.
     * - **0o0010**: The user group has the permission to execute a regular file or search for the specified path in a
     * directory.
     * - **0o0007**: mask used to obtain the permissions of other users.
     * - **0o0004**: Other users have the permission to read a regular file or a directory entry.
     * - **0o0002**: Other users have the permission to write a regular file or create and delete a directory entry.
     * - **0o0001**: Other users have the permission to execute a regular file or search for the specified path in a
     * directory.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 6
     * @deprecated since 9
     * @useinstead @ohos.file.fs:Stat.mode
     */
    readonly mode: number;
    /**
     * Number of hard links in the file.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 6
     * @deprecated since 9
     */
    readonly nlink: number;
    /**
     * ID of the file owner.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 6
     * @deprecated since 9
     * @useinstead @ohos.file.fs:Stat.uid
     */
    readonly uid: number;
    /**
     * ID of the user group of the file.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 6
     * @deprecated since 9
     * @useinstead @ohos.file.fs:Stat.gid
     */
    readonly gid: number;
    /**
     * Minor device number.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 6
     * @deprecated since 9
     */
    readonly rdev: number;
    /**
     * File size, in bytes. This parameter is valid only for regular files.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 6
     * @deprecated since 9
     * @useinstead @ohos.file.fs:Stat.size
     */
    readonly size: number;
    /**
     * Number of blocks occupied by a file. Each block is 512 bytes.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 6
     * @deprecated since 9
     */
    readonly blocks: number;
    /**
     * Time when the file was last accessed. The value is the number of seconds elapsed since 00:00:00 on January 1, 1970.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 6
     * @deprecated since 9
     * @useinstead @ohos.file.fs:Stat.atime
     */
    readonly atime: number;
    /**
     * Time when the file content was last modified. The value is the number of seconds elapsed since 00:00:00 on January
     * 1, 1970.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 6
     * @deprecated since 9
     * @useinstead @ohos.file.fs:Stat.mtime
     */
    readonly mtime: number;
    /**
     * Time of the last status change of the file. The value is the number of seconds elapsed since 00:00:00 on January 1,
     * 1970.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 6
     * @deprecated since 9
     * @useinstead @ohos.file.fs:Stat.ctime
     */
    readonly ctime: number;
    /**
     * Checks whether this file is a block special file. A block special file supports access by block only, and it is
     * cached when accessed.
     *
     * @returns { boolean } Returns **true** if it is a block special file; returns **false** otherwise.
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 6
     * @deprecated since 9
     * @useinstead @ohos.file.fs:Stat.isBlockDevice
     */
    isBlockDevice(): boolean;
    /**
     * Checks whether this file is a character special file. A character special file supports random access, and it is
     * not cached when accessed.
     *
     * @returns { boolean } Returns **true** if it is a character special file; returns **false** otherwise.
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 6
     * @deprecated since 9
     * @useinstead @ohos.file.fs:Stat.isCharacterDevice
     */
    isCharacterDevice(): boolean;
    /**
     * Checks whether this file is a directory.
     *
     * @returns { boolean } Returns **true** if it is a directory; returns **false** otherwise.
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 6
     * @deprecated since 9
     * @useinstead @ohos.file.fs:Stat.isDirectory
     */
    isDirectory(): boolean;
    /**
     * Checks whether this file is a named pipe (or FIFO). Named pipes are used for inter-process communication.
     *
     * @returns { boolean } Returns **true** if it is a named pipe; returns **false** otherwise.
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 6
     * @deprecated since 9
     * @useinstead @ohos.file.fs:Stat.isFIFO
     */
    isFIFO(): boolean;
    /**
     * Checks whether this file is a regular file.
     *
     * @returns { boolean } Returns **true** if it is a regular file; returns **false** otherwise.
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 6
     * @deprecated since 9
     * @useinstead @ohos.file.fs:Stat.isFile
     */
    isFile(): boolean;
    /**
     * Checks whether this file is a socket.
     *
     * @returns { boolean } Returns **true** if it is a socket; returns **false** otherwise.
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 6
     * @deprecated since 9
     * @useinstead @ohos.file.fs:Stat.isSocket
     */
    isSocket(): boolean;
    /**
     * Checks whether this file is a symbolic link.
     *
     * @returns { boolean } Returns **true** if it is a symbolic link; returns **false** otherwise.
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 6
     * @deprecated since 9
     * @useinstead @ohos.file.fs:Stat.isSymbolicLink
     */
    isSymbolicLink(): boolean;
}
/**
 * Provides a stream for file operations. Before calling any API of the **Stream** class, use **createStream()** to
 * create a **Stream** instance synchronously or asynchronously.
 *
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 6
 * @deprecated since 9
 * @useinstead @ohos.file.fs:Stream
 */
declare interface Stream {
    /**
     * Closes the file stream. This API uses a promise to return the result.
     *
     * @returns { Promise<void> } Promise that returns the file stream closed.
     * @throws { TypedError } close fail
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.file.fs:Stream.close
     */
    close(): Promise<void>;
    /**
     * Closes the file stream. This API uses an asynchronous callback to return the result.
     *
     * @param { AsyncCallback<void> } [callback] - Callback invoked when the file stream is closed asynchronously.
     * @throws { TypedError } close fail
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.file.fs:Stream.close
     */
    close(callback: AsyncCallback<void>): void;
    /**
     * Closes the file stream. This API returns the result synchronously.
     *
     * @throws { TypedError | Error } close fail
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 6
     * @deprecated since 9
     * @useinstead @ohos.file.fs:Stream.closeSync
     */
    closeSync(): void;
    /**
     * Flushes the file stream. This API uses a promise to return the result.
     *
     * @returns { Promise<void> } Promise that returns the file stream flushed.
     * @throws { TypedError } Parameter check failed
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.file.fs:Stream.flush
     */
    flush(): Promise<void>;
    /**
     * Flushes the file stream. This API uses an asynchronous callback to return the result.
     *
     * @param { AsyncCallback<void> } [callback] - Callback invoked when the file stream is asynchronously flushed.
     * @throws { TypedError } Parameter check failed
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.file.fs:Stream.flush
     */
    flush(callback: AsyncCallback<void>): void;
    /**
     * Flushes the file stream. This API returns the result synchronously.
     *
     * @throws { TypedError | Error } flush fail
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.file.fs:Stream.flushSync
     */
    flushSync(): void;
    /**
     * Writes data to a stream file. This API uses a promise to return the result.
     *
     * @param { ArrayBuffer | string } buffer - Data to write. It can be a string or data from a buffer.
     * @param { object } [options] - The options are as follows:<br>- **offset** (number): offset of the write position
     *     relative to the start address of the data, in bytes. This parameter is optional. The default value is **0**.<br
     *     >- **length** (number): length of the data to write, in bytes. This parameter is optional. The default value is
     *     the buffer length minus the offset.<br>- **position** (number): start position to write the data into the file,
     *     in bytes. This parameter is optional. By default, data is written from the current position.<br>- **encoding**
     *     (string): format of the data to be encoded when the data is a string. The default value is **'utf-8'**, which
     *     is the only value supported.<br>Constraints: offset + length <= Buffer size
     * @returns { Promise<number> } Promise that returns the length of the data written, in bytes.
     * @throws { TypedError } Parameter check failed
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.file.fs:Stream.write
     */
    write(buffer: ArrayBuffer | string, options?: {
        offset?: number;
        length?: number;
        position?: number;
        encoding?: string;
    }): Promise<number>;
    /**
     * Writes data to a stream file. This API uses an asynchronous callback to return the result.
     *
     * @param { ArrayBuffer | string } buffer - Data to write. It can be a string or data from a buffer.
     * @param { AsyncCallback<number> } [callback] - Callback invoked when the data is written asynchronously, which is
     *     used to return the length of the data written, in bytes.
     * @throws { TypedError } Parameter check failed
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.file.fs:Stream.write
     */
    write(buffer: ArrayBuffer | string, callback: AsyncCallback<number>): void;
    /**
     * Writes data to a stream file. This API uses an asynchronous callback to return the result.
     *
     * @param { ArrayBuffer | string } buffer - Data to write. It can be a string or data from a buffer.
     * @param { object } [options] - The options are as follows:<br>- **offset** (number): offset of the write position
     *     relative to the start address of the data, in bytes. This parameter is optional. The default value is **0**.<br
     *     >- **length** (number): length of the data to write, in bytes. This parameter is optional. The default value is
     *     the buffer length minus the offset.<br>- **position** (number): start position to write the data into the file,
     *     in bytes. This parameter is optional. By default, data is written from the current position.<br>- **encoding**
     *     (string): format of the data to be encoded when the data is a string. The default value is **'utf-8'**, which
     *     is the only value supported.<br>Constraints: offset + length <= Buffer size
     * @param { AsyncCallback<number> } [callback] - Callback invoked when the data is written asynchronously, which is
     *     used to return the length of the data written, in bytes.
     * @throws { TypedError } Parameter check failed
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.file.fs:Stream.write
     */
    write(buffer: ArrayBuffer | string, options: {
        offset?: number;
        length?: number;
        position?: number;
        encoding?: string;
    }, callback: AsyncCallback<number>): void;
    /**
     * Writes data to a stream file. This API returns the result synchronously.
     *
     * @param { ArrayBuffer | string } buffer - Data to write. It can be a string or data from a buffer.
     * @param { object } [options] - The options are as follows:<br>- **offset** (number): offset of the write position
     *     relative to the start address of the data, in bytes. This parameter is optional. The default value is **0**.<br
     *     >- **length** (number): length of the data to write. This parameter is optional. The default value is the
     *     buffer length minus the offset.<br>- **position** (number): start position to write the data into the file, in
     *     bytes. This parameter is optional. By default, data is written from the current position.<br>- **encoding** (
     *     string): format of the data to be encoded when the data is a string. The default value is **'utf-8'**, which is
     *     the only value supported.<br>Constraints: offset + length <= Buffer size
     * @returns { number } Length of the data written in the file, in bytes.
     * @throws { TypedError | Error } write fail
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.file.fs:Stream.writeSync
     */
    writeSync(buffer: ArrayBuffer | string, options?: {
        offset?: number;
        length?: number;
        position?: number;
        encoding?: string;
    }): number;
    /**
     * Reads data from a stream file. This API uses a promise to return the result.
     *
     * @param { ArrayBuffer } buffer - Buffer used to store the file read.
     * @param { object } [options] - The options are as follows:<br>- **offset** (number): position to store the data read
     *     in the buffer relative to the start address of the buffer, in bytes. This parameter is optional. The default
     *     value is **0**.<br>- **length** (number): length of the data to read. This parameter is optional. The default
     *     value is the buffer length minus the offset, in bytes.<br>- **position** (number): position of the data to read
     *     in the file. This parameter is optional. By default, data is read from the current position, in bytes.<br>
     *     Constraints: offset + length <= Buffer size
     * @returns { Promise<ReadOut> } Promise that returns the data read.
     * @throws { TypedError } Parameter check failed
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.file.fs:Stream.read
     */
    read(buffer: ArrayBuffer, options?: {
        position?: number;
        offset?: number;
        length?: number;
    }): Promise<ReadOut>;
    /**
     * read.
     *
     * @param { ArrayBuffer } buffer - buffer.
     * @param { AsyncCallback<ReadOut> } [callback] - callback.
     * @throws { TypedError } Parameter check failed
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.file.fs:Stream.read
     */
    read(buffer: ArrayBuffer, callback: AsyncCallback<ReadOut>): void;
    /**
     * Reads data from a stream file. This API uses an asynchronous callback to return the result.
     *
     * @param { ArrayBuffer } buffer - Buffer used to store the file read.
     * @param { object } [options] - The options are as follows:<br>- **offset** (number): position to store the data read
     *     in the buffer relative to the start address of the buffer, in bytes. This parameter is optional. The default
     *     value is **0**.<br>- **length** (number): length of the data to read, in bytes. This parameter is optional. The
     *     default value is the buffer length minus the offset.<br>- **position** (number): position of the data to read
     *     in the file, in bytes. This parameter is optional. By default, data is read from the current position.<br>
     *     Constraints: offset + length <= Buffer size
     * @param { AsyncCallback<ReadOut> } [callback] - Callback invoked when data is read asynchronously from the stream
     *     file.
     * @throws { TypedError } Parameter check failed
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.file.fs:Stream.read
     */
    read(buffer: ArrayBuffer, options: {
        position?: number;
        offset?: number;
        length?: number;
    }, callback: AsyncCallback<ReadOut>): void;
    /**
     * Reads data from a stream file. This API returns the result synchronously.
     *
     * @param { ArrayBuffer } buffer - Buffer used to store the file read.
     * @param { object } [options] - The options are as follows:<br>- **offset** (number): position to store the data read
     *     in the buffer relative to the start address of the buffer, in bytes. This parameter is optional. The default
     *     value is **0**.<br>- **length** (number): length of the data to read. This parameter is optional. The default
     *     value is the buffer length minus the offset, in bytes.<br>- **position** (number): position of the data to read
     *     in the file, in bytes. This parameter is optional. By default, data is read from the current position.<br>
     *     Constraints: offset + length <= Buffer size
     * @returns { number } Length of the data read, in bytes.
     * @throws { TypedError | Error } read fail
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 7
     * @deprecated since 9
     * @useinstead @ohos.file.fs:Stream.readSync
     */
    readSync(buffer: ArrayBuffer, options?: {
        position?: number;
        offset?: number;
        length?: number;
    }): number;
}
/**
 * Obtains the file read result. This class applies only to the **read()** method.
 *
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 6
 * @deprecated since 9
 */
declare interface ReadOut {
    /**
     * Length of the data read, in bytes.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 6
     * @deprecated since 9
     */
    bytesRead: number;
    /**
     * Position of the buffer to which the data will be read relative to the
     * start address of the buffer, in bytes.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 6
     * @deprecated since 9
     */
    offset: number;
    /**
     * Buffer for storing the data read.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 6
     * @deprecated since 9
     */
    buffer: ArrayBuffer;
}
/**
 * Listens for file change. You can call the **Watcher.stop()** method synchronously or asynchronously to stop the
 * listening.
 *
 * @syscap SystemCapability.FileManagement.File.FileIO
 * @since 7
 * @deprecated since 10
 * @useinstead @ohos.file.fs:Watcher
 */
declare interface Watcher {
    /**
     * Stops the **watcher** instance. This API uses a promise to return the result.
     *
     * @returns { Promise<void> } return Promise
     * @throws { TypedError | Error } stop fail
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 7
     * @deprecated since 10
     * @useinstead @ohos.file.fs:Watcher.stop
     */
    stop(): Promise<void>;
    /**
     * Stops the **watcher** instance. This API uses an asynchronous callback to return the result.
     *
     * @param { AsyncCallback<void> } [callback] - Callback invoked when **watcher** is stopped asynchronously.
     * @throws { TypedError | Error } stop fail
     * @syscap SystemCapability.FileManagement.File.FileIO
     * @since 7
     * @deprecated since 10
     * @useinstead @ohos.file.fs:Watcher.stop
     */
    stop(callback: AsyncCallback<void>): void;
}
export default fileIO;

```
