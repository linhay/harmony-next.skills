# @system.request.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2020 Huawei Device Co., Ltd.
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
 * The **system.request** module provides applications with basic upload and download capabilities.
 *
 * > **NOTE**
 * >
 * > - The APIs of this module are deprecated since API version 9. You are advised to use
 * > [@ohos.request]{@link @ohos.request:request} instead.
 *
 * @file Upload and Download
 * @kit BasicServicesKit
 */
/**
 *
 * @syscap SystemCapability.MiscServices.Upload
 * @since 3
 * @deprecated since 9
 * @useinstead @ohos.request:request.UploadConfig
 */
export interface UploadResponse {
    /**
     * HTTP status code returned by the server.
     *
     * @syscap SystemCapability.MiscServices.Upload
     * @since 3
     * @deprecated since 9
     * @useinstead ohos.request.agent.HttpResponse.statusCode
     */
    code: number;
    /**
     * Content returned by the server. The value type is determined by the type in the returned headers.
     *
     * @syscap SystemCapability.MiscServices.Upload
     * @since 3
     * @deprecated since 9
     * @useinstead ohos.request.agent.Progress.extras
     */
    data: string;
    /**
     * Headers returned by the server.
     *
     * @syscap SystemCapability.MiscServices.Upload
     * @since 3
     * @deprecated since 9
     * @useinstead ohos.request.agent.HttpResponse.headers
     */
    headers: Object;
}
/**
 *
 * @syscap SystemCapability.MiscServices.Download
 * @since 3
 * @deprecated since 9
 * @useinstead @ohos.request:request.UploadConfig
 */
export interface DownloadResponse {
    /**
     * Download token, which is used to obtain the download status
     *
     * @syscap SystemCapability.MiscServices.Download
     * @since 3
     * @deprecated since 9
     * @useinstead ohos.request.agent.Task.tid
     */
    token: string;
}
/**
 *
 * @syscap SystemCapability.MiscServices.Download
 * @since 3
 * @deprecated since 9
 * @useinstead ohos.request.agent.Task.on
 */
export interface OnDownloadCompleteResponse {
    /**
     * URI of the download file.
     *
     * @syscap SystemCapability.MiscServices.Download
     * @since 3
     * @deprecated since 9
     * @useinstead ohos.request.agent.Task.config.saveas
     */
    uri: string;
}
/**
 *
 * @syscap SystemCapability.MiscServices.Upload
 * @since 3
 * @deprecated since 9
 * @useinstead @ohos.request:request.File
 */
export interface RequestFile {
    /**
     * File name in the header when **multipart** is used.
     *
     * @syscap SystemCapability.MiscServices.Upload
     * @since 3
     * @deprecated since 9
     * @useinstead ohos.request.agent.FileSpec.filename
     */
    filename?: string;
    /**
     * Name of a form item when **multipart** is used. The default value is **file**.
     *
     * @syscap SystemCapability.MiscServices.Upload
     * @since 3
     * @deprecated since 9
     * @useinstead ohos.request.agent.FormItem.name
     */
    name?: string;
    /**
     * Local path for storing files.
     *
     * @syscap SystemCapability.MiscServices.Upload
     * @since 3
     * @deprecated since 9
     * @useinstead ohos.request.agent.FileSpec.path
     */
    uri: string;
    /**
     * Type of the file content. By default, the type is obtained based on the extension of the file name or URI.
     *
     * @syscap SystemCapability.MiscServices.Upload
     * @since 3
     * @deprecated since 9
     * @useinstead ohos.request.agent.FileSpec.contentType
     */
    type?: string;
}
/**
 *
 * @syscap SystemCapability.MiscServices.Upload
 * @since 3
 * @deprecated since 9
 * @useinstead @ohos.request:request.RequestData
 */
export interface RequestData {
    /**
     * Name of the form element.
     *
     * @syscap SystemCapability.MiscServices.Upload
     * @since 3
     * @deprecated since 9
     * @useinstead ohos.request.agent.FormItem.name
     */
    name: string;
    /**
     * Value of the form element.
     *
     * @syscap SystemCapability.MiscServices.Upload
     * @since 3
     * @deprecated since 9
     * @useinstead ohos.request.agent.FormItem.value
     */
    value: string;
}
/**
 * > **NOTE**
 * >
 * > This API has been supported since API version 3 and deprecated since API version 9. You are advised to use
 * > [UploadConfig]{@link @ohos.request:request.agent.Config} instead.
 *
 * @syscap SystemCapability.MiscServices.Upload
 * @since 3
 * @deprecated since 9
 * @useinstead @ohos.request:request.UploadConfig
 */
export interface UploadRequestOptions {
    /**
     * Resource URL.
     *
     * @syscap SystemCapability.MiscServices.Upload
     * @since 3
     * @deprecated since 9
     * @useinstead ohos.request.agent.Config.url
     */
    url: string;
    /**
     * Form data in the request body.
     *
     * @syscap SystemCapability.MiscServices.Upload
     * @since 3
     * @deprecated since 9
     * @useinstead ohos.request.agent.Config.data
     */
    data?: Array<RequestData>;
    /**
     * List of files to upload, which is submitted through multipart/form-data.
     *
     * @syscap SystemCapability.MiscServices.Upload
     * @since 3
     * @deprecated since 9
     * @useinstead ohos.request.agent.Config.data
     */
    files: Array<RequestFile>;
    /**
     * Request header.
     *
     * @syscap SystemCapability.MiscServices.Upload
     * @since 3
     * @deprecated since 9
     * @useinstead ohos.request.agent.Config.headers
     */
    header?: Object;
    /**
     * Request methods available: POST and PUT. The default value is POST.
     *
     * @syscap SystemCapability.MiscServices.Upload
     * @since 3
     * @deprecated since 9
     * @useinstead ohos.request.agent.Config.method
     */
    method?: string;
    /**
     * Called when the files are uploaded successfully.
     *
     * @syscap SystemCapability.MiscServices.Upload
     * @since 3
     * @deprecated since 9
     * @useinstead ohos.request.agent.Task.on
     */
    success?: (data: UploadResponse) => void;
    /**
     * Called when uploading fails.
     *
     * @syscap SystemCapability.MiscServices.Upload
     * @since 3
     * @deprecated since 9
     * @useinstead ohos.request.agent.Task.on
     */
    fail?: (data: any, code: number) => void;
    /**
     * Called when the execution is completed.
     *
     * @syscap SystemCapability.MiscServices.Upload
     * @since 3
     * @deprecated since 9
     * @useinstead ohos.request.agent.Task.on
     */
    complete?: () => void;
}
/**
 * > **NOTE**
 * >
 * > This API has been supported since API version 3 and deprecated since API version 9. You are advised to use
 * > [UploadConfig]{@link @ohos.request:request.agent.Config} instead.
 *
 * @syscap SystemCapability.MiscServices.Download
 * @since 3
 * @deprecated since 9
 * @useinstead @ohos.request:request.UploadConfig
 */
export interface DownloadRequestOptions {
    /**
     * Resource URL.
     *
     * @syscap SystemCapability.MiscServices.Download
     * @since 3
     * @deprecated since 9
     * @useinstead ohos.request.agent.Config.url
     */
    url: string;
    /**
     * Name of the file to downloaded.
     * The value is obtained from the current request or resource URL by default.
     *
     * @syscap SystemCapability.MiscServices.Download
     * @since 3
     * @deprecated since 9
     * @useinstead ohos.request.agent.Config.saveas
     */
    filename?: string;
    /**
     * Request header.
     *
     * @syscap SystemCapability.MiscServices.Download
     * @since 3
     * @deprecated since 9
     * @useinstead ohos.request.agent.Config.headers
     */
    header?: string;
    /**
     * Download description.
     * The default value is the file name.
     *
     * @syscap SystemCapability.MiscServices.Download
     * @since 3
     * @deprecated since 9
     * @useinstead ohos.request.agent.Config.description
     */
    description?: string;
    /**
     * Called when the files are successfully downloaded.
     *
     * @syscap SystemCapability.MiscServices.Download
     * @since 3
     * @deprecated since 9
     * @useinstead ohos.request.agent.Task.on
     */
    success?: (data: DownloadResponse) => void;
    /**
     * Called when downloading fails.
     *
     * @syscap SystemCapability.MiscServices.Download
     * @since 3
     * @deprecated since 9
     * @useinstead ohos.request.agent.Task.on
     */
    fail?: (data: any, code: number) => void;
    /**
     * Called when API call is complete.
     *
     * @syscap SystemCapability.MiscServices.Download
     * @since 3
     * @deprecated since 9
     * @useinstead ohos.request.agent.Task.on
     */
    complete?: () => void;
}
/**
 *
 * @syscap SystemCapability.MiscServices.Download
 * @since 3
 * @deprecated since 9
 * @useinstead ohos.request.agent.Task.on
 */
export interface OnDownloadCompleteOptions {
    /**
     * Result token returned by the download API.
     *
     * @syscap SystemCapability.MiscServices.Download
     * @since 3
     * @deprecated since 9
     * @useinstead ohos.request.agent.Task.tid
     */
    token: string;
    /**
     * Called when API call is successful.
     *
     * @syscap SystemCapability.MiscServices.Download
     * @since 3
     * @deprecated since 9
     * @useinstead ohos.request.agent.Task.on
     */
    success?: (data: OnDownloadCompleteResponse) => void;
    /**
     * Called when API call has failed. Header information and HTTP status code returned when the upload task fails.
     *
     * @syscap SystemCapability.MiscServices.Download
     * @since 3
     * @deprecated since 9
     * @useinstead ohos.request.agent.Task.on
     */
    fail?: (data: any, code: number) => void;
    /**
     * Called when API call is complete.
     *
     * @syscap SystemCapability.MiscServices.Download
     * @since 3
     * @deprecated since 9
     * @useinstead ohos.request.agent.Task.on
     */
    complete?: () => void;
}
/**
 *
 * @syscap SystemCapability.MiscServices.Download
 * @since 3
 * @deprecated since 9
 * @useinstead @ohos.request:request
 */
export default class Request {
    /**
     * Uploads a file. This API returns no value.
     *
     * @param { UploadRequestOptions } options - Upload configurations.
     * @syscap SystemCapability.MiscServices.Upload
     * @since 3
     * @deprecated since 9
     * @useinstead @ohos.request:request.uploadFile(context: BaseContext, config: UploadConfig)
     */
    static upload(options: UploadRequestOptions): void;
    /**
     * Downloads a file. This API returns no value.
     *
     * @param { DownloadRequestOptions } options - Download configurations.
     * @syscap SystemCapability.MiscServices.Download
     * @since 3
     * @deprecated since 9
     * @useinstead @ohos.request:request.downloadFile(context: BaseContext, config: DownloadConfig)
     */
    static download(options: DownloadRequestOptions): void;
    /**
     * Listens for download task status. This API returns no value.
     *
     * @param { OnDownloadCompleteOptions } options - Configurations of the download task.
     * @syscap SystemCapability.MiscServices.Download
     * @since 3
     * @deprecated since 9
     * @useinstead ohos.request.agent.Task.show(id: string)
     */
    static onDownloadComplete(options: OnDownloadCompleteOptions): void;
}

```
