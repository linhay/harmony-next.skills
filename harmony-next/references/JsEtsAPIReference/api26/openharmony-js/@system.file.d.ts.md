# @system.file.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2020-2023 Huawei Device Co., Ltd.
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
/**
 * Returns a file, including the file information.
 *
 * @syscap SystemCapability.FileManagement.File.FileIO.Lite
 * @since 3
 * @deprecated since 10
 * @reserved ["liteWearable"]
 */
export interface FileResponse {
    /**
     * URI of the file.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    uri: string;
    /**
     * File length, in bytes.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    length: number;
    /**
     * Timestamp when the file is stored the last time, which is the number of milliseconds elapsed since
     * 1970/01/01 00:00:00 GMT. For lite wearables, the value is fixed to 0, because this parameter
     * is restricted by the underlying file system.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    lastModifiedTime: number;
    /**
     * File type. Available values are as follows:
     * **dir**: directory
     * **file**: file
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    type: 'dir' | 'file';
    /**
     * List of files. When the recursive value is true and the type is dir, the file information under the
     * subdirectory will be returned. Otherwise, no value will be returned.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    subFiles?: Array<FileResponse>;
}
/**
 * Defines the options used in move().
 *
 * @syscap SystemCapability.FileManagement.File.FileIO.Lite
 * @since 3
 * @deprecated since 10
 * @reserved ["liteWearable"]
 */
export interface FileMoveOption {
    /**
     * URI of the file to move. Restricted by the underlying file system of lite wearables, the value must meet the
     * following requirements:
     * 1. The URI cannot contain the following special characters: \"*+,:;<=>?[]|\x7F.
     * 2. The value can contain a maximum of 128 characters.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    srcUri: string;
    /**
     * URI of the location to which the file is to move. Restricted by the underlying file system of lite wearables, the
     * value must meet the following requirements:
     * 1. The URI cannot contain the following special characters: \"*+,:;<=>?[]|\x7F.
     * 2. The value can contain a maximum of 128 characters.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    dstUri: string;
    /**
     * Callback invoked when the API call is successful. This API returns the URI of the destination location.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    success?: (uri: string) => void;
    /**
     * Callback invoked when the API call fails.
     * **data** indicates the error information.
     * **code** indicates the returned error code:
     * **202**: invalid parameter
     * **300**: I/O error
     * **301**: file or directory not found
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    fail?: (data: string, code: number) => void;
    /**
     * Callback invoked when the API call is complete.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    complete?: () => void;
}
/**
 * Returns a file list, including the file list information.
 *
 * @syscap SystemCapability.FileManagement.File.FileIO.Lite
 * @since 3
 * @deprecated since 10
 * @reserved ["liteWearable"]
 */
export interface FileListResponse {
    /**
     * File list. The format of each file is as follows:
     * {
     * uri:'file1',
     * lastModifiedTime:1589965924479,
     * length:10240,
     * type:'file'
     * }
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    fileList: Array<FileResponse>;
}
/**
 * Defines the options used in list().
 *
 * @syscap SystemCapability.FileManagement.File.FileIO.Lite
 * @since 3
 * @deprecated since 10
 * @reserved ["liteWearable"]
 */
export interface FileListOption {
    /**
     * URI of the directory. Restricted by the underlying file system of lite wearables, the value must meet the following
     * requirements:
     * 1. The URI cannot contain the following special characters: \"*+,:;<=>?[]|\x7F.
     * 2. The value can contain a maximum of 128 characters.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    uri: string;
    /**
     * Callback invoked when the API call is successful. **data** is [FileListResponse]{@link FileListResponse}.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    success?: (data: FileListResponse) => void;
    /**
     * Callback invoked when the API call fails.
     * **data** indicates the error information.
     * **code** indicates the returned error code:
     * **202**: invalid parameter
     * **300**: I/O error
     * **301**: file or directory not found
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    fail?: (data: string, code: number) => void;
    /**
     * Callback invoked when the API call is complete.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    complete?: () => void;
}
/**
 * Defines the options used in copy().
 *
 * @syscap SystemCapability.FileManagement.File.FileIO.Lite
 * @since 3
 * @deprecated since 10
 * @reserved ["liteWearable"]
 */
export interface FileCopyOption {
    /**
     * URI of the file to copy. Restricted by the underlying file system of lite wearables, the value must meet the
     * following requirements:
     * 1. The URI cannot contain the following special characters: \"*+,:;<=>?[]|\x7F.
     * 2. The value can contain a maximum of 128 characters.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    srcUri: string;
    /**
     * URI of the location to which the copy is to be saved. The directory of application resources and URI of the tmp
     * type are not supported. Restricted by the underlying file system of lite wearables, the value must meet the
     * following requirements:
     * 1. The URI cannot contain the following special characters: \"*+,:;<=>?[]|\x7F.
     * 2. The value can contain a maximum of 128 characters.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    dstUri: string;
    /**
     * Callback invoked when the API call is successful. This API returns the URI of the destination location.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    success?: (uri: string) => void;
    /**
     * Callback invoked when the API call fails.
     * **data** indicates the error information.
     * **code** indicates the returned error code:
     * **202**: invalid parameter
     * **300**: I/O error
     * **301**: file or directory not found
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    fail?: (data: string, code: number) => void;
    /**
     * Callback invoked when the API call is complete.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    complete?: () => void;
}
/**
 * Defines the options used in get().
 *
 * @syscap SystemCapability.FileManagement.File.FileIO.Lite
 * @since 3
 * @deprecated since 10
 * @reserved ["liteWearable"]
 */
export interface FileGetOption {
    /**
     * URI of the file. Restricted by the underlying file system of lite wearables, the value must meet the following
     * requirements:
     * 1. The URI cannot contain the following special characters: \"*+,:;<=>?[]|\x7F.
     * 2. The value can contain a maximum of 128 characters.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    uri: string;
    /**
     * Indicates whether to recursively obtain the file list in a subdirectory. The value **true** indicates to
     * recursively obtain the file list, and **false** indicates the opposite. The default value is **false**.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    recursive?: boolean;
    /**
     * Callback invoked when the API call is successful. **file** is [FileResponse]{@link FileResponse}.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    success?: (file: FileResponse) => void;
    /**
     * Callback invoked when the API call fails.
     * **data** indicates the error information.
     * **code** indicates the returned error code:
     * **202**: invalid parameter
     * **300**: I/O error
     * **301**: file or directory not found
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    fail?: (data: string, code: number) => void;
    /**
     * Callback invoked when the API call is complete.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    complete?: () => void;
}
/**
 * Defines the options used in delete().
 *
 * @syscap SystemCapability.FileManagement.File.FileIO.Lite
 * @since 3
 * @deprecated since 10
 * @reserved ["liteWearable"]
 */
export interface FileDeleteOption {
    /**
     * URI of the file to delete, which cannot be an application resource path. Restricted by the underlying file system
     * of lite wearables, the value must meet the following requirements:
     * 1. The URI cannot contain the following special characters: \"*+,:;<=>?[]|\x7F.
     * 2. The value can contain a maximum of 128 characters.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    uri: string;
    /**
     * Callback invoked when the API call is successful.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    success?: () => void;
    /**
     * Callback invoked when the API call fails.
     * **data** indicates the error information.
     * **code** indicates the returned error code:
     * **202**: invalid parameter
     * **300**: I/O error
     * **301**: file or directory not found
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    fail?: (data: string, code: number) => void;
    /**
     * Callback invoked when the API call is complete.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    complete?: () => void;
}
/**
 * Defines the options used in writeText().
 *
 * @syscap SystemCapability.FileManagement.File.FileIO.Lite
 * @since 3
 * @deprecated since 10
 * @reserved ["liteWearable"]
 */
export interface FileWriteTextOption {
    /**
     * URI of a local file. If it does not exist, a file will be created. Restricted by the underlying file system of lite
     * wearables, the value must meet the following requirements:
     * 1. The URI cannot contain the following special characters: \"*+,:;<=>?[]|\x7F.
     * 2. The value can contain a maximum of 128 characters.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    uri: string;
    /**
     * String to write into the file.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    text: string;
    /**
     * Encoding format. The default format is **UTF-8**.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    encoding?: string;
    /**
     * Whether to enable the append mode. The default value is **false**. The value **true** means to enable the append
     * mode; the value **false** means the opposite.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    append?: boolean;
    /**
     * Callback invoked when the API call is successful.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    success?: () => void;
    /**
     * Callback invoked when the API call fails.
     * **data** indicates the error information.
     * **code** indicates the returned error code:
     * **202**: invalid parameter
     * **300**: I/O error
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    fail?: (data: string, code: number) => void;
    /**
     * Callback invoked when the API call is complete.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    complete?: () => void;
}
/**
 * Returns the text read, including the text content.
 *
 * @syscap SystemCapability.FileManagement.File.FileIO.Lite
 * @since 3
 * @deprecated since 10
 * @reserved ["liteWearable"]
 */
export interface FileReadTextResponse {
    /**
     * Text read from the specified file.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    text: string;
}
/**
 * Defines the options used in readText().
 *
 * @syscap SystemCapability.FileManagement.File.FileIO.Lite
 * @since 3
 * @deprecated since 10
 * @reserved ["liteWearable"]
 */
export interface FileReadTextOption {
    /**
     * URI of the file to which the content is written. Restricted by the underlying file system of lite wearables, the
     * value must meet the following requirements:
     * 1. The URI cannot contain the following special characters: \"*+,:;<=>?[]|\x7F.
     * 2. The value can contain a maximum of 128 characters.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    uri: string;
    /**
     * Encoding format. The default format is **UTF-8**.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    encoding?: string;
    /**
     * Position where the reading starts, in bytes. The default value is the start position of the file.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    position?: number;
    /**
     * Length of the text to be read, in bytes. The default value is **4096**.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    length?: number;
    /**
     * Callback invoked when the API call is successful. **data** is [FileReadTextResponse]{@link FileReadTextResponse}.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    success?: (data: FileReadTextResponse) => void;
    /**
     * Callback invoked when the API call fails.
     * **data** indicates the error information.
     * **code** indicates the returned error code:
     * **202**: invalid parameter
     * **300**: I/O error
     * **301**: file or directory not found
     * **302**: text to read exceeding 4 KB
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    fail?: (data: string, code: number) => void;
    /**
     * Callback invoked when the API call is complete.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    complete?: () => void;
}
/**
 * Defines the options used in writeArrayBuffer().
 *
 * @syscap SystemCapability.FileManagement.File.FileIO.Lite
 * @since 3
 * @deprecated since 10
 * @reserved ["liteWearable"]
 */
export interface FileWriteArrayBufferOption {
    /**
     * URI of a local file. If it does not exist, a file will be created. Restricted by the underlying file system of lite
     * wearables, the value must meet the following requirements:
     * 1. The URI cannot contain the following special characters: \"*+,:;<=>?[]|\x7F.
     * 2. The value can contain a maximum of 128 characters.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    uri: string;
    /**
     * Buffer from which the data is derived.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    buffer: Uint8Array;
    /**
     * Offset of the position in the file where writing starts, in bytes. The default value is **0**.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    position?: number;
    /**
     * Whether to enable the append mode. The default value is **false**. If the value is **true**, the **position**
     * parameter will become invalid. The value **true** means to enable the append mode; the value **false** means the
     * opposite.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    append?: boolean;
    /**
     * Callback invoked when the API call is successful.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    success?: () => void;
    /**
     * Callback invoked when the API call fails.
     * **data** indicates the error information.
     * **code** indicates the returned error code:
     * **202**: invalid parameter
     * **300**: I/O error
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    fail?: (data: string, code: number) => void;
    /**
     * Callback invoked when the API call is complete.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    complete?: () => void;
}
/**
 * Returns the file read, including the file content.
 *
 * @syscap SystemCapability.FileManagement.File.FileIO.Lite
 * @since 3
 * @deprecated since 10
 * @reserved ["liteWearable"]
 */
export interface FileReadArrayBufferResponse {
    /**
     * Data read.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    buffer: Uint8Array;
}
/**
 * Defines the options used in readArrayBuffer().
 *
 * @syscap SystemCapability.FileManagement.File.FileIO.Lite
 * @since 3
 * @deprecated since 10
 * @reserved ["liteWearable"]
 */
export interface FileReadArrayBufferOption {
    /**
     * URI of the file to which the content is written. Restricted by the underlying file system of lite wearables, the
     * value must meet the following requirements:
     * 1. The URI cannot contain the following special characters: \"*+,:;<=>?[]|\x7F.
     * 2. The value can contain a maximum of 128 characters.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    uri: string;
    /**
     * Position where the reading starts, in bytes. The default value is the start position of the file.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    position?: number;
    /**
     * Length of data to read, in bytes. If this parameter is not set, the reading proceeds until the end of the file.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    length?: number;
    /**
     * Callback invoked when the API call is successful. **data** is
     * [FileReadArrayBufferResponse]{@link FileReadArrayBufferResponse}.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    success?: (data: FileReadArrayBufferResponse) => void;
    /**
     * Callback invoked when the API call fails.
     * **data** indicates the error information.
     * **code** indicates the returned error code:
     * **202**: invalid parameter
     * **300**: I/O error
     * **301**: file or directory not found
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    fail?: (data: string, code: number) => void;
    /**
     * Callback invoked when the API call is complete.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    complete?: () => void;
}
/**
 * Defines the options used in access().
 *
 * @syscap SystemCapability.FileManagement.File.FileIO.Lite
 * @since 3
 * @deprecated since 10
 * @reserved ["liteWearable"]
 */
export interface FileAccessOption {
    /**
     * URI of the directory or file. Restricted by the underlying file system of lite wearables, the value must meet the
     * following requirements:
     * 1. The URI cannot contain the following special characters: \"*+,:;<=>?[]|\x7F.
     * 2. The value can contain a maximum of 128 characters.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    uri: string;
    /**
     * Callback invoked when the API call is successful.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    success?: () => void;
    /**
     * Callback invoked when the API call fails.
     * **data** indicates the error information.
     * **code** indicates the returned error code:
     * **202**: invalid parameter
     * **300**: I/O error
     * **301**: file or directory not found
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    fail?: (data: string, code: number) => void;
    /**
     * Callback invoked when the API call is complete.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    complete?: () => void;
}
/**
 * Defines the options used in mkdir().
 *
 * @syscap SystemCapability.FileManagement.File.FileIO.Lite
 * @since 3
 * @deprecated since 10
 * @reserved ["liteWearable"]
 */
export interface FileMkdirOption {
    /**
     * URI of the directory. Restricted by the underlying file system of lite wearables, the value must meet the following
     * requirements:
     * 1. The URI cannot contain the following special characters: \"*+,:;<=>?[]|\x7F.
     * 2. The value can contain a maximum of 128 characters.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    uri: string;
    /**
     * Whether to recursively create the upper-level directory of the specified directory. The default value is **false**.
     * The value **true** means to create upper-level directory recursively; the value false means the opposite.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    recursive?: boolean;
    /**
     * Callback invoked when the API call is successful.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    success?: () => void;
    /**
     * Callback invoked when the API call fails.
     * **data** indicates the error information.
     * **code** indicates the returned error code:
     * **202**: invalid parameter
     * **300**: I/O error
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    fail?: (data: string, code: number) => void;
    /**
     * Callback invoked when the API call is complete.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    complete?: () => void;
}
/**
 * Defines the options used in rmdir().
 *
 * @syscap SystemCapability.FileManagement.File.FileIO.Lite
 * @since 3
 * @deprecated since 10
 * @reserved ["liteWearable"]
 */
export interface FileRmdirOption {
    /**
     * URI of the directory. Restricted by the underlying file system of lite wearables, the value must meet the following
     * requirements:
     * 1. The URI cannot contain the following special characters: \"*+,:;<=>?[]|\x7F.
     * 2. The value can contain a maximum of 128 characters.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    uri: string;
    /**
     * Whether to recursively delete files and subdirectories of the specified directory. The default value is **false**.
     * The value **true** means to recursively delete files and subdirectories of the specified directory; the value
     * **false** means the opposite.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    recursive?: boolean;
    /**
     * Callback invoked when the API call is successful.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    success?: () => void;
    /**
     * Callback invoked when the API call fails.
     * **data** indicates the error information.
     * **code** indicates the returned error code:
     * **202**: invalid parameter
     * **300**: I/O error
     * **301**: file or directory not found
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    fail?: (data: string, code: number) => void;
    /**
     * Callback invoked when the API call is complete.
     *
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     */
    complete?: () => void;
}
/**
 * File
 *
 * @syscap SystemCapability.FileManagement.File.FileIO.Lite
 * @since 3
 * @deprecated since 10
 * @reserved ["liteWearable"]
 */
export default class File {
    /**
     * Moves a specified file to a given location.
     *
     * @param { FileMoveOption } options - Options for moving the files.
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     * @useinstead @ohos.file.fs:moveFile
     */
    static move(options: FileMoveOption): void;
    /**
     * Copies a file to the given URI.
     *
     * @param { FileCopyOption } options - Options for copying the files.
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     * @useinstead @ohos.file.fs:copyFile
     */
    static copy(options: FileCopyOption): void;
    /**
     * Obtains all files in the specified directory.
     *
     * @param { FileListOption } options - Options for obtaining all files in the specified directory.
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     * @useinstead @ohos.file.fs:listFile
     */
    static list(options: FileListOption): void;
    /**
     * Obtains information about a local file.
     *
     * @param { FileGetOption } options - Options for obtaining information about a local file.
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     * @useinstead @ohos.file.fs:stat
     */
    static get(options: FileGetOption): void;
    /**
     * Deletes a local file.
     *
     * @param { FileDeleteOption } options - Options for deleting a local file.
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     * @useinstead @ohos.file.fs:unlink
     */
    static delete(options: FileDeleteOption): void;
    /**
     * Writes text into a file. Only text files can be read and written.
     *
     * @param { FileWriteTextOption } options - Options for writing text into a file.
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     * @useinstead @ohos.file.fs:write
     */
    static writeText(options: FileWriteTextOption): void;
    /**
     * Reads text from a file. Only text files can be read and written.
     *
     * @param { FileReadTextOption } options - Options for reading text from a file.
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     * @useinstead @ohos.file.fs:readText
     */
    static readText(options: FileReadTextOption): void;
    /**
     * Writes buffer data into a file. Only text files can be read and written.
     *
     * @param { FileWriteArrayBufferOption } options - Options for writing buffer data into a file.
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     * @useinstead @ohos.file.fs:write
     */
    static writeArrayBuffer(options: FileWriteArrayBufferOption): void;
    /**
     * Reads buffer data from a file. Only text files can be read and written.
     *
     * @param { FileReadArrayBufferOption } options - Options for reading buffer data from a file.
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     * @useinstead @ohos.file.fs:read
     */
    static readArrayBuffer(options: FileReadArrayBufferOption): void;
    /**
     * Checks whether a file or directory exists.
     *
     * @param { FileAccessOption } options - Options for checking whether a file or directory exists.
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     * @useinstead @ohos.file.fs:access
     */
    static access(options: FileAccessOption): void;
    /**
     * Creates a directory.
     *
     * @param { FileMkdirOption } options - Options for creating a directory.
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     * @useinstead @ohos.file.fs:mkdir
     */
    static mkdir(options: FileMkdirOption): void;
    /**
     * Deletes a directory.
     *
     * @param { FileRmdirOption } options - Options for deleting a directory.
     * @syscap SystemCapability.FileManagement.File.FileIO.Lite
     * @since 3
     * @deprecated since 10
     * @reserved ["liteWearable"]
     * @useinstead @ohos.file.fs:rmdir
     */
    static rmdir(options: FileRmdirOption): void;
}

```
