# @ohos.file.picker.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2023-2026 Huawei Device Co., Ltd.
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
import { AsyncCallback } from './@ohos.base';
import Context from './application/Context';
/**
 * The **Picker** module encapsulates APIs such as **DocumentViewPicker**, **AudioViewPicker**, and **PhotoViewPicker**
 * to provide capabilities of selecting and saving files of different types. An application can select the API as
 * required. The APIs of this module must be called in UIAbility. Otherwise, the **FilePicker**, **AudioPicker**, or
 * **PhotoPicker** cannot be started.
 * Chinese characters and non-digit characters in the URI are compiled into the corresponding ASCII code and
 * concatenated to the URI returned by calling these APIs.
 *
 * @syscap SystemCapability.FileManagement.UserFileService
 * @crossplatform [since 12]
 * @atomicservice [since 11]
 * @since 9
 */
declare namespace picker {
    /**
     * Enumerates the media file types that can be selected.
     *
     * @syscap SystemCapability.FileManagement.UserFileService
     * @atomicservice [since 11]
     * @since 9
     * @deprecated since 12
     * @useinstead @ohos.file.photoAccessHelper:photoAccessHelper.PhotoViewMIMETypes
     */
    export enum PhotoViewMIMETypes {
        /**
         * Image.
         *
         * @syscap SystemCapability.FileManagement.UserFileService
         * @atomicservice [since 11]
         * @since 9
         * @deprecated since 18
         * @useinstead @ohos.file.photoAccessHelper:photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE
         */
        IMAGE_TYPE = 'image/*',
        /**
         * Video.
         *
         * @syscap SystemCapability.FileManagement.UserFileService
         * @atomicservice [since 11]
         * @since 9
         * @deprecated since 18
         * @useinstead @ohos.file.photoAccessHelper:photoAccessHelper.PhotoViewMIMETypes.VIDEO_TYPE
         */
        VIDEO_TYPE = 'video/*',
        /**
         * Image and video.
         *
         * @syscap SystemCapability.FileManagement.UserFileService
         * @atomicservice [since 11]
         * @since 9
         * @deprecated since 18
         * @useinstead @ohos.file.photoAccessHelper:photoAccessHelper.PhotoViewMIMETypes.IMAGE_VIDEO_TYPE
         */
        IMAGE_VIDEO_TYPE = '*/*'
    }
    /**
     * Defines the options for selecting images or videos.
     *
     * @syscap SystemCapability.FileManagement.UserFileService
     * @atomicservice [since 11]
     * @since 9
     * @deprecated since 12
     * @useinstead @ohos.file.photoAccessHelper:photoAccessHelper.PhotoSelectOptions
     */
    class PhotoSelectOptions {
        /**
         * Media file types to select. If this parameter is not specified, **IMAGE_VIDEO_TYPE** is used by default.
         *
         * **Note**: This API is supported since API version 9 and deprecated since API version 18.
         *
         * @syscap SystemCapability.FileManagement.UserFileService
         * @atomicservice [since 11]
         * @since 9
         * @deprecated since 18
         * @useinstead @ohos.file.photoAccessHelper:photoAccessHelper.PhotoSelectOptions#MIMEType
         */
        MIMEType?: PhotoViewMIMETypes;
        /**
         * Maximum number of media files that can be selected. The default value is **50**,
         * and the maximum value is **500**.
         *
         * @syscap SystemCapability.FileManagement.UserFileService
         * @atomicservice [since 11]
         * @since 9
         * @deprecated since 18
         * @useinstead @ohos.file.photoAccessHelper:photoAccessHelper.PhotoSelectOptions#maxSelectNumber
         */
        maxSelectNumber?: number;
    }
    /**
     * Defines information about the images or videos selected.
     *
     * @syscap SystemCapability.FileManagement.UserFileService
     * @atomicservice [since 11]
     * @since 9
     * @deprecated since 12
     * @useinstead @ohos.file.photoAccessHelper:photoAccessHelper.PhotoSelectResult
     */
    class PhotoSelectResult {
        /**
         * URIs of the media files selected. This URI array can be used only by
         * [photoAccessHelper.getAssets]{@link @ohos.file.photoAccessHelper:photoAccessHelper.PhotoAccessHelper.getAssets(options: FetchOptions, callback: AsyncCallback<FetchResult<PhotoAsset>>)}
         * . For details, see
         * [Using a Media File URI](docroot://file-management/user-file-uri-intro.md#using-a-media-file-uri).
         *
         * @syscap SystemCapability.FileManagement.UserFileService
         * @atomicservice [since 11]
         * @since 9
         * @deprecated since 18
         * @useinstead @ohos.file.photoAccessHelper:photoAccessHelper.PhotoSelectResult#photoUris
         */
        photoUris: Array<string>;
        /**
         * Whether the selected image is the original one. The value **true** means the selected image is the original one;
         * the value **false** means the opposite.
         *
         * @syscap SystemCapability.FileManagement.UserFileService
         * @atomicservice [since 11]
         * @since 9
         * @deprecated since 18
         * @useinstead @ohos.file.photoAccessHelper:photoAccessHelper.PhotoSelectResult#isOriginalPhoto
         */
        isOriginalPhoto: boolean;
    }
    /**
     * Defines the options for saving images or videos.
     *
     * @syscap SystemCapability.FileManagement.UserFileService
     * @since 9
     * @deprecated since 12
     * @useinstead SaveButtonOptions
     */
    class PhotoSaveOptions {
        /**
         * File name of the image or video to save. If this parameter is not specified, the user needs to enter the file
         * name.
         *
         * @syscap SystemCapability.FileManagement.UserFileService
         * @since 9
         * @deprecated since 18
         * @useinstead SaveButtonOptions
         */
        newFileNames?: Array<string>;
    }
    /**
     * Provides APIs for selecting and saving images or videos. You are advised to use
     * [PhotoViewPicker of PhotoAccessHelper]{@link @ohos.file.photoAccessHelper:photoAccessHelper} to select a file.
     * Before using the APIs of **PhotoViewPicker**, you need to create a **PhotoViewPicker** instance.
     *
     * @syscap SystemCapability.FileManagement.UserFileService
     * @atomicservice [since 11]
     * @since 9
     * @deprecated since 12
     * @useinstead @ohos.file.photoAccessHelper:photoAccessHelper.PhotoViewPicker
     */
    class PhotoViewPicker {
        /**
         * A constructor used to create a PhotoViewPicker instance. This constructor is not recommended due to
         * the potential risk of operation failure.
         *
         * @syscap SystemCapability.FileManagement.UserFileService
         * @atomicservice
         * @since 12
         * @deprecated since 18
         * @useinstead @ohos.file.photoAccessHelper:photoAccessHelper.PhotoViewPicker
         */
        constructor();
        /**
         * A constructor used to create a PhotoViewPicker instance. This constructor is recommended. For details about how
         * to obtain the context, see [getHostContext]{@link @ohos.arkui.UIContext.UIContext#getHostContext}.
         *
         * @param { Context } context - Application context (only **UIAbilityContext** is supported). For details about the
         *     application context of the stage model, see [Context]{@link ./app/context}.
         * @syscap SystemCapability.FileManagement.UserFileService
         * @since 12
         * @deprecated since 18
         * @useinstead @ohos.file.photoAccessHelper:photoAccessHelper.PhotoViewPicker
         */
        constructor(context: Context);
        /**
         * Starts a **photoPicker** page for the user to select one or more images or videos. This API uses a promise to
         * return the result. You can pass in **PhotoSelectOptions** to specify the type and maximum number of the files to
         * select.
         *
         * @param { PhotoSelectOptions } option - Options for selecting images or videos. If this parameter is not
         *     specified, images and videos are selected by default. A maximum of 50 files can be selected.
         * @returns { Promise<PhotoSelectResult> } Promise used to return the URIs of the images or videos selected.
         *     <br>**Note**: The **photoUris** in the **PhotoSelectResult** object returned by this API can be used only by
         *     [photoAccessHelper.getAssets]{@link @ohos.file.photoAccessHelper:photoAccessHelper.PhotoAccessHelper.getAssets(options: FetchOptions, callback: AsyncCallback<FetchResult<PhotoAsset>>)}
         *     . For details, see
         *     [Using a Media File URI](docroot://file-management/user-file-uri-intro.md#using-a-media-file-uri).
         * @syscap SystemCapability.FileManagement.UserFileService
         * @atomicservice [since 11]
         * @since 9
         * @deprecated since 12
         * @useinstead @ohos.file.photoAccessHelper:photoAccessHelper.PhotoViewPicker#select(option?: PhotoSelectOptions)
         */
        select(option?: PhotoSelectOptions): Promise<PhotoSelectResult>;
        /**
         * Starts a **photoPicker** page for the user to select one or more images or videos. This API uses an asynchronous
         * callback to return the result. You can pass in **PhotoSelectOptions** to specify the type and maximum number of
         * the files to select.
         *
         * @param { PhotoSelectOptions } option - Options for selecting images or videos.
         * @param { AsyncCallback<PhotoSelectResult> } callback - Callback used to return the images or videos selected.
         *     <br>**Note**: The **photoUris** in the **PhotoSelectResult** object returned by this API can be used only by
         *     [photoAccessHelper.getAssets]{@link @ohos.file.photoAccessHelper:photoAccessHelper.PhotoAccessHelper.getAssets(options: FetchOptions, callback: AsyncCallback<FetchResult<PhotoAsset>>)}
         *     . For details, see
         *     [Using a Media File URI](docroot://file-management/user-file-uri-intro.md#using-a-media-file-uri).
         * @syscap SystemCapability.FileManagement.UserFileService
         * @atomicservice [since 11]
         * @since 9
         * @deprecated since 12
         * @useinstead @ohos.file.photoAccessHelper:photoAccessHelper.PhotoViewPicker#select(option: PhotoSelectOptions, callback: AsyncCallback<PhotoSelectResult>)
         */
        select(option: PhotoSelectOptions, callback: AsyncCallback<PhotoSelectResult>): void;
        /**
         * Starts a **photoPicker** page for the user to select one or more images or videos. This API uses an asynchronous
         * callback to return the result.
         *
         * @param { AsyncCallback<PhotoSelectResult> } callback - Callback used to return the images or videos selected.
         *     <br>**Note**: The **photoUris** in the **PhotoSelectResult** object returned by this API can be used only by
         *     [photoAccessHelper.getAssets]{@link @ohos.file.photoAccessHelper:photoAccessHelper.PhotoAccessHelper.getAssets(options: FetchOptions, callback: AsyncCallback<FetchResult<PhotoAsset>>)}
         *     . For details, see
         *     [Using a Media File URI](docroot://file-management/user-file-uri-intro.md#using-a-media-file-uri).
         * @syscap SystemCapability.FileManagement.UserFileService
         * @atomicservice [since 11]
         * @since 9
         * @deprecated since 12
         * @useinstead @ohos.file.photoAccessHelper:photoAccessHelper.PhotoViewPicker#select(callback: AsyncCallback<PhotoSelectResult>)
         */
        select(callback: AsyncCallback<PhotoSelectResult>): void;
        /**
         * Starts a **photoPicker** page for the user to save one or more images or videos. This API uses a promise to
         * return the result. You can pass in **PhotoSaveOptions** to specify the URIs of the images or videos to save.
         *
         * @param { PhotoSaveOptions } option - Options for saving images or videos. If this parameter is not specified, a
         *     **photoPicker** page will be displayed for the user to enter the names of the files to save.
         * @returns { Promise<Array<string>> } Promise used to return the URIs of the images or videos saved.
         *     <br>**Note**: This API saves files in **Files**, not in **Gallery**. For details about how to use the
         *     returned URIs, see [Using a Document URI](docroot://file-management/user-file-uri-intro.md#using-a-document-uri).
         * @syscap SystemCapability.FileManagement.UserFileService
         * @since 9
         * @deprecated since 12
         * @useinstead SaveButton
         */
        save(option?: PhotoSaveOptions): Promise<Array<string>>;
        /**
         * Starts a **photoPicker** page for the user to save one or more images or videos. This API uses an asynchronous
         * callback to return the result. You can pass in **PhotoSaveOptions** to specify the URIs of the images or videos
         * to save.
         *
         * @param { PhotoSaveOptions } option - Options for saving images or videos.
         * @param { AsyncCallback<Array<string>> } callback - Callback invoked to return the URIs of the images or videos
         *     saved.
         *     <br>**Note**: This API saves files in **Files**, not in **Gallery**. For details about how to use the
         *     returned URIs, see [Using a Document URI](docroot://file-management/user-file-uri-intro.md#using-a-document-uri).
         * @syscap SystemCapability.FileManagement.UserFileService
         * @since 9
         * @deprecated since 12
         * @useinstead SaveButton
         */
        save(option: PhotoSaveOptions, callback: AsyncCallback<Array<string>>): void;
        /**
         * Starts a **photoPicker** page for the user to save one or more images or videos. This API uses an asynchronous
         * callback to return the URIs of the images or videos to save.
         *
         * @param { AsyncCallback<Array<string>> } callback - Callback invoked to return the URIs of the images or videos
         *     saved.
         *     <br>**Note**: This API saves files in **Files**, not in **Gallery**. For details about how to use the
         *     returned URIs, see [Using a Document URI](docroot://file-management/user-file-uri-intro.md#using-a-document-uri).
         * @syscap SystemCapability.FileManagement.UserFileService
         * @since 9
         * @deprecated since 12
         * @useinstead SaveButton
         */
        save(callback: AsyncCallback<Array<string>>): void;
    }
    /**
     * Enumerates the types of documents selected.
     *
     * @syscap SystemCapability.FileManagement.UserFileService.FolderSelection
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 11
     */
    export enum DocumentSelectMode {
        /**
         * File (default).
         *
         * @syscap SystemCapability.FileManagement.UserFileService.FolderSelection
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 11
         */
        FILE = 0,
        /**
         * Folder.
         *
         * @syscap SystemCapability.FileManagement.UserFileService.FolderSelection
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 11
         */
        FOLDER = 1,
        /**
         * Mixed type of files and folders.
         *
         * @syscap SystemCapability.FileManagement.UserFileService.FolderSelection
         * @atomicservice [since 12]
         * @since 11
         */
        MIXED = 2
    }
    /**
     * Enumerates the modes for saving documents.
     *
     * @syscap SystemCapability.FileManagement.UserFileService
     * @atomicservice
     * @since 12
     */
    export enum DocumentPickerMode {
        /**
         * Standard mode.
         *
         * @syscap SystemCapability.FileManagement.UserFileService
         * @atomicservice
         * @since 12
         */
        DEFAULT = 0,
        /**
         * Download mode.
         *
         * **Note**: The directories created in DOWNLOAD mode are used only to save files. There is no access isolation
         * between directories. You are advised not to save sensitive application data.
         *
         * @syscap SystemCapability.FileManagement.UserFileService
         * @atomicservice
         * @since 12
         */
        DOWNLOAD = 1
    }
    /**
     * Enumerates file aggregation types.
     *
     * @syscap SystemCapability.FileManagement.UserFileService
     * @atomicservice
     * @since 15
     */
    export enum MergeTypeMode {
        /**
         * Default mode, indicating that this parameter does not take effect.
         *
         * @syscap SystemCapability.FileManagement.UserFileService
         * @atomicservice
         * @since 15
         */
        DEFAULT = 0,
        /**
         * Audio mode.
         *
         * @syscap SystemCapability.FileManagement.UserFileService
         * @atomicservice
         * @since 15
         */
        AUDIO = 1,
        /**
         * Video mode.
         *
         * @syscap SystemCapability.FileManagement.UserFileService
         * @atomicservice
         * @since 15
         */
        VIDEO = 2,
        /**
         * Document mode.
         *
         * @syscap SystemCapability.FileManagement.UserFileService
         * @atomicservice
         * @since 15
         */
        DOCUMENT = 3,
        /**
         * Image mode.
         *
         * @syscap SystemCapability.FileManagement.UserFileService
         * @atomicservice
         * @since 15
         */
        PICTURE = 4
    }
    /**
     * Defines the options for selecting documents.
     *
     * @syscap SystemCapability.FileManagement.UserFileService
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 9
     */
    class DocumentSelectOptions {
        /**
         * URI of the file or directory that can be selected. It is empty by
         * default (the recently opened page is displayed).
         *
         * @syscap SystemCapability.FileManagement.UserFileService
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 10
         */
        defaultFilePathUri?: string;
        /**
         * Suffix of the document to select.
         *
         * The value is a string array. Each element specifies an option, which includes at most two parts with a vertical
         * bar (|) in between. The first part is the description, and the second part is the document suffix.
         * If there is no "|", the option does not have the description. Each filter suffix can contain multiple suffixes,
         * separated by a comma (,). The length of the input array cannot exceed 100 characters, for example,
         * ['Images (.png, .jpg)|.png,.jpg', 'Documents|.txt', 'Videos|.mp4', '.pdf'].
         *
         * By default, no filtering is performed, that is, all documents are selected. The wildcard ['All files (*.*)|.*']
         * can be used on 2-in-1 devices to display all files. (Mobile phones can support this configuration since API
         * version 17.)
         *
         * This parameter is available only to the devices that have the required system capability.
         *
         * @syscap SystemCapability.FileManagement.UserFileService
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 10
         */
        fileSuffixFilters?: Array<string>;
        /**
         * Maximum number of files that can be selected.
         *
         * In API version 20 and earlier versions, a maximum of 500 files can be selected at a time.
         * The default value is 500. Directories can be selected only on devices that have the system capability.
         * A maximum of one directory can be selected at a time.
         *
         * In API version 21 and later versions, the maximum number of files that can be selected at a time is not limited.
         * Due to system capability restrictions, if too many files are selected at a time, the functionality may be
         * abnormal or the processing performance may be poor. It is recommended that a maximum of 10,000 files be selected
         * at a time.
         *
         * In API version 23 and later versions, the maximum number of files that can be selected at a time is not limited.
         *
         * @syscap SystemCapability.FileManagement.UserFileService
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 10
         */
        maxSelectNumber?: number;
        /**
         * Type of the document selected by Picker. The default value is **FILE** (file type).
         *
         * @syscap SystemCapability.FileManagement.UserFileService.FolderSelection
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 11
         */
        selectMode?: DocumentSelectMode;
        /**
         * Whether to start Picker.
         *
         * Default value: **false**. If **authMode** is **true**, **defaultFilePathUri** is mandatory, which specifies the
         * URI of the file allowed to access.
         *
         * This parameter can be used on 2-in-1 devices but has no effect on other devices.
         *
         * This API can be used in atomic services since API version 12.
         *
         * SystemCapability.FileManagement.UserFileService.FolderSelection
         *
         * @syscap SystemCapability.FileManagement.UserFileService.FolderSelection
         * @atomicservice
         * @since 12
         */
        authMode?: boolean;
        /**
         * Whether to enable the batch authorization mode.
         *
         * The value **false** (default) means to disable the batch authorization mode; the value **true** means to enable
         * the batch authorization mode. The **multiUriArray** parameter only takes effect when **multiAuthMode** is set to
         * **true**.
         *
         * This parameter can be used on smartphones but has no effect on other devices.
         *
         * @syscap SystemCapability.FileManagement.UserFileService
         * @atomicservice
         * @since 15
         */
        multiAuthMode?: boolean;
        /**
         * Whether to pass the URIs for batch authorization (only files are supported). This parameter is used together with
         * **multiAuthMode** and does not take effect when **multiAuthMode** is set to **false**. By default, this parameter
         * is left empty. (The files displayed on the batch authorization page are empty.)
         *
         * This parameter can be used on smartphones but has no effect on other devices.
         *
         * @syscap SystemCapability.FileManagement.UserFileService
         * @atomicservice
         * @since 15
         */
        multiUriArray?: Array<string>;
        /**
         * Whether to enable the aggregation view mode for a file management application. The default value is **DEFAULT**,
         * indicating that this parameter does not take effect and the aggregation view is disabled. If this parameter is
         * set to a value other than **DEFAULT**, other parameters do not take effect.
         *
         * This parameter can be used on smartphones but has no effect on other devices.
         *
         * @syscap SystemCapability.FileManagement.UserFileService
         * @atomicservice
         * @since 15
         */
        mergeMode?: MergeTypeMode;
        /**
         * Whether to support encryption (only files are supported). The default value is **false**. If this parameter is
         * set to **true**, files can be encrypted on the Picker page.
         *
         * @syscap SystemCapability.FileManagement.UserFileService
         * @atomicservice
         * @since 19
         */
        isEncryptionSupported?: boolean;
        /**
         * Whether to support for selecting folders, Only 2-in-1 devices are supported.
         * The value false (default) means not support folder selection;
         *
         * @syscap SystemCapability.FileManagement.UserFileService.FolderSelection
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        allowsMulFolderSelection?: boolean;
    }
    /**
     * Defines the options for saving documents.
     *
     * @syscap SystemCapability.FileManagement.UserFileService
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 9
     */
    class DocumentSaveOptions {
        /**
         * Name of the document to save. If this parameter is not specified, the user needs to enter the file name.
         *
         * @syscap SystemCapability.FileManagement.UserFileService
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        newFileNames?: Array<string>;
        /**
         * URI of the file or directory that can be selected. It is empty by
         * default (the recently opened page is displayed).
         *
         * @syscap SystemCapability.FileManagement.UserFileService
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 10
         */
        defaultFilePathUri?: string;
        /**
         * Document suffix of the document to save.
         *
         * The value is a string array. Each element specifies an option, which includes at most two parts with a vertical
         * bar (|) in between. The first part is the description, and the second part is the document suffix.
         * If there is no "|", the option does not have the description. By default, all documents are saved.
         *
         * @syscap SystemCapability.FileManagement.UserFileService
         * @atomicservice [since 12]
         * @since 10
         */
        fileSuffixChoices?: Array<string>;
        /**
         * Mode for starting Picker.
         *
         * Default value: **DEFAULT**. If **pickerMode** is **DOWNLOAD**, the settings of **newFileNames**,
         * **defaultFilePathUri**, and **fileSuffixChoices** do not take effect.
         *
         * @syscap SystemCapability.FileManagement.UserFileService
         * @atomicservice
         * @since 12
         */
        pickerMode?: DocumentPickerMode;
        /**
         * A Boolean value indicates whether to pre-create empty files when saving files. The default value is **true**, in
         * which case the Picker pre-creates empty files and returns an array of the file URIs. If it is set to **false**,
         * no empty files are pre-created, and only an array of the file URIs is returned.
         *
         * @default true
         * @syscap SystemCapability.FileManagement.UserFileService.FolderSelection
         * @stagemodelonly
         * @since 23
         */
        autoCreateEmptyFile?: boolean;
    }
    /**
     * Provides APIs for selecting and saving documents in different formats. Before using the APIs of
     * **DocumentViewPicker**, you need to create a **DocumentViewPicker** instance.
     *
     * @syscap SystemCapability.FileManagement.UserFileService
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 9
     */
    class DocumentViewPicker {
        /**
         * A constructor used to create a **DocumentViewPicker** instance. This constructor is not recommended due to the
         * potential risk of operation failure.
         *
         * @syscap SystemCapability.FileManagement.UserFileService
         * @atomicservice
         * @since 12
         */
        constructor();
        /**
         * A constructor used to create a **DocumentViewPicker** instance. This constructor is recommended. For details
         * about how to obtain the context, see
         * [getHostContext](docroot://reference/apis-arkui/arkts-apis-uicontext-uicontext.md#gethostcontext12).
         *
         * @param { Context } context - Application context (only **UIAbilityContext** is supported). For details about the
         *     application context of the stage model, see [Context]{@link ./app/context}.
         * @syscap SystemCapability.FileManagement.UserFileService
         * @atomicservice
         * @since 12
         */
        constructor(context: Context);
        /**
         * A constructor used to create a **DocumentViewPicker** object in a window created by an application. In other
         * scenarios, you are advised to use **constructor(context: Context)** to create a **DocumentViewPicker** object.
         *
         * > **NOTE**
         * >
         * > This method is supported on 2-in-1 devices and tablets since API version 19.
         *
         * @param { Context } context - Application context (only **UIAbilityContext** is supported). For details about the
         *     application context of the stage model, see [Context]{@link ./app/context}.
         * @param { window.Window } window - Window instance created by the application.
         * @syscap SystemCapability.FileManagement.UserFileService
         * @since 13
         */
        constructor(context: Context, window: window.Window);
        /**
         * Starts a **documentPicker** page for the user to select one or more documents. This API uses a promise to return
         * the result.
         *
         * @param { DocumentSelectOptions } option - Options for selecting documents. If this parameter is not specified,
         *     the **documentPicker** page is displayed by default.
         * @returns { Promise<Array<string>> } Promise used to return the URIs of the documents selected.
         *     <br> **Note**: For details about how to use the returned URIs, see
         *     [Using a Document URI](docroot://file-management/user-file-uri-intro.md#using-a-document-uri).
         * @syscap SystemCapability.FileManagement.UserFileService
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        select(option?: DocumentSelectOptions): Promise<Array<string>>;
        /**
         * Starts a **documentPicker** page for the user to select one or more documents. This API uses an asynchronous
         * callback to return the result.
         *
         * @param { DocumentSelectOptions } option - Options for selecting documents.
         * @param { AsyncCallback<Array<string>> } callback - Callback invoked to return the URIs of the documents selected.
         *     <br>**Note**: For details about how to use the returned URIs, see
         *     [Using a Document URI](docroot://file-management/user-file-uri-intro.md#using-a-document-uri).
         * @syscap SystemCapability.FileManagement.UserFileService
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        select(option: DocumentSelectOptions, callback: AsyncCallback<Array<string>>): void;
        /**
         * Starts a **documentPicker** page for the user to select one or more documents. This API uses an asynchronous
         * callback to return the result.
         *
         * @param { AsyncCallback<Array<string>> } callback - Callback invoked to return the URIs of the documents selected.
         *     <br>**Note**: For details about how to use the returned URIs, see
         *     [Using a Document URI](docroot://file-management/user-file-uri-intro.md#using-a-document-uri).
         * @syscap SystemCapability.FileManagement.UserFileService
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        select(callback: AsyncCallback<Array<string>>): void;
        /**
         * Starts a **documentPicker** page for the user to save one or more documents. This API uses a promise to return
         * the result.
         *
         * @param { DocumentSaveOptions } option - Options for saving the documents. If this parameter is not specified, a
         *     **documentPicker** page will be displayed for the user to enter the names of the documents to save.
         * @returns { Promise<Array<string>> } Promise used to return the URIs of the documents saved.
         *     <br>**Note**: For details about how to use the returned URIs, see
         *     [Using a Document URI](docroot://file-management/user-file-uri-intro.md#using-a-document-uri).
         * @syscap SystemCapability.FileManagement.UserFileService
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        save(option?: DocumentSaveOptions): Promise<Array<string>>;
        /**
         * Starts a **documentPicker** page for the user to save one or more documents. This API uses an asynchronous
         * callback to return the result.
         *
         * @param { DocumentSaveOptions } option - Options for saving the documents.
         * @param { AsyncCallback<Array<string>> } callback - Callback invoked to return the URIs of the documents saved.
         *     <br>**Note**: For details about how to use the returned URIs, see
         *     [Using a Document URI](docroot://file-management/user-file-uri-intro.md#using-a-document-uri).
         * @syscap SystemCapability.FileManagement.UserFileService
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        save(option: DocumentSaveOptions, callback: AsyncCallback<Array<string>>): void;
        /**
         * Starts a **documentPicker** page for the user to save one or more documents. This API uses an asynchronous
         * callback to return the result.
         *
         * @param { AsyncCallback<Array<string>> } callback - Callback invoked to return the URIs of the documents saved.
         *     <br>**Note**: For details about how to use the returned URIs, see
         *     [Using a Document URI](docroot://file-management/user-file-uri-intro.md#using-a-document-uri).
         * @syscap SystemCapability.FileManagement.UserFileService
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        save(callback: AsyncCallback<Array<string>>): void;
        /**
         * Obtains the index of the file suffix type of the file saved.
         * This method takes effect only when used with
         * [save()]{@link picker.DocumentViewPicker#save(option?: DocumentSaveOptions)}.
         * This method can be used only after [DocumentSaveOptions.fileSuffixChoices]{@link picker.DocumentSaveOptions} is
         * configured.
         * The index (number) returned by this method indicates the location of the file suffix specified in
         * [DocumentSaveOptions.fileSuffixChoices]{@link picker.DocumentSaveOptions}. If no file suffix is specified,
         * **getSelectedIndex()** returns **-1**.
         *
         * @returns { number } Subscript (number) of the selected suffix type in
         *     [DocumentSaveOptions.fileSuffixChoices]{@link picker.DocumentSaveOptions}. The default value is **-1**.
         * @syscap SystemCapability.FileManagement.UserFileService.FolderSelection
         * @crossplatform
         * @atomicservice
         * @since 14
         */
        getSelectedIndex(): number;
    }
    /**
     * Defines the options for selecting audio clips.
     *
     * @syscap SystemCapability.FileManagement.UserFileService
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 9
     */
    class AudioSelectOptions {
        /**
         * Maximum number of audio clips that can be selected.
         *
         * Default value: **1**
         *
         * Value range: 1 to 500
         *
         * @syscap SystemCapability.FileManagement.UserFileService
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        maxSelectNumber?: number;
    }
    /**
     * Defines the options for saving audio clips.
     *
     * @syscap SystemCapability.FileManagement.UserFileService
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 9
     */
    class AudioSaveOptions {
        /**
         * Name of the document to save. If this parameter is not specified, the user needs to enter the file name.
         *
         * @syscap SystemCapability.FileManagement.UserFileService
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        newFileNames?: Array<string>;
    }
    /**
     * Provides APIs for selecting and saving audio clips. Before using the APIs of **AudioViewPicker**, you need to
     * create an **AudioViewPicker** instance.
     *
     * @syscap SystemCapability.FileManagement.UserFileService
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 9
     */
    class AudioViewPicker {
        /**
         * A constructor used to create an **AudioViewPicker** instance. This constructor is not recommended due to the
         * potential risk of operation failure.
         *
         * @syscap SystemCapability.FileManagement.UserFileService
         * @atomicservice
         * @since 12
         */
        constructor();
        /**
         * A constructor used to create an **AudioViewPicker** instance. This constructor is recommended. For details about
         * how to obtain the context, see
         * [getHostContext](docroot://reference/apis-arkui/arkts-apis-uicontext-uicontext.md#gethostcontext12).
         *
         * @param { Context } context - Application context (only **UIAbilityContext** is supported). For details about the
         *     application context of the stage model, see [Context]{@link ./app/context}.
         * @syscap SystemCapability.FileManagement.UserFileService
         * @atomicservice
         * @since 12
         */
        constructor(context: Context);
        /**
         * Starts an **audioPicker** page for the user to select one or more audio clips. This API uses a promise to return
         * the result.
         *
         * @param { AudioSelectOptions } option - Options for selecting audio clips. If this parameter is not specified, the
         *     **audioPicker** page is displayed by default.
         * @returns { Promise<Array<string>> } Promise used to return the URIs of the audio clips selected.
         *     <br>**Note**: For details about how to use the returned URIs, see
         *     [Using a Media File URI](docroot://file-management/user-file-uri-intro.md#using-a-media-file-uri).
         * @syscap SystemCapability.FileManagement.UserFileService
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        select(option?: AudioSelectOptions): Promise<Array<string>>;
        /**
         * Starts an **audioPicker** page for the user to select one or more audio clips. This API uses an asynchronous
         * callback to return the result.
         *
         * @param { AudioSelectOptions } option - Options for selecting audio clips.
         * @param { AsyncCallback<Array<string>> } callback - Callback invoked to return the URIs of the audio clips
         *     selected.
         *     <br>**Note**: For details about how to use the returned URIs, see
         *     [Using a Media File URI](docroot://file-management/user-file-uri-intro.md#using-a-media-file-uri).
         * @syscap SystemCapability.FileManagement.UserFileService
         * @crossplatform [since 12]
         * @since 9
         */
        select(option: AudioSelectOptions, callback: AsyncCallback<Array<string>>): void;
        /**
         * Starts an **audioPicker** page for the user to select one or more audio clips. This API uses an asynchronous
         * callback to return the result.
         * **System capability**: SystemCapability.FileManagement.UserFileService
         *
         * @param { AsyncCallback<Array<string>> } callback - Callback invoked to return the URIs of the audio clips
         *     selected.
         *     <br>**Note**: For details about how to use the returned URIs, see
         *     [Using a Media File URI](docroot://file-management/user-file-uri-intro.md#using-a-media-file-uri).
         * @syscap SystemCapability.FileManagement.UserFileService
         * @crossplatform [since 12]
         * @since 9
         */
        select(callback: AsyncCallback<Array<string>>): void;
        /**
         * Starts an **audioPicker** page (currently, a **documentPicker** page is displayed) for the user to save one or
         * more audio clips. This API uses a promise to return the result.
         *
         * @param { AudioSaveOptions } option - Options for saving audio clips. If this parameter is not specified, an
         *     **audioPicker** page will be displayed for the user to enter the names of the files to save.
         * @returns { Promise<Array<string>> } Promise used to return the URIs of the audio clips saved.
         *     <br>**Note**: For details about how to use the returned URIs, see
         *     [Using a Document URI](docroot://file-management/user-file-uri-intro.md#using-a-document-uri).
         * @syscap SystemCapability.FileManagement.UserFileService
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        save(option?: AudioSaveOptions): Promise<Array<string>>;
        /**
         * Starts an **audioPicker** page (currently, a **documentPicker** page is displayed) for the user to save one or
         * more audio clips. This API uses an asynchronous callback to return the result.
         *
         * @param { AudioSaveOptions } option - Options for saving audio clips.
         * @param { AsyncCallback<Array<string>> } callback - Callback invoked to return the URIs of the audio clips saved.
         *     <br>**Note**: For details about how to use the returned URIs, see
         *     [Using a Document URI](docroot://file-management/user-file-uri-intro.md#using-a-document-uri).
         * @syscap SystemCapability.FileManagement.UserFileService
         * @crossplatform [since 12]
         * @since 9
         */
        save(option: AudioSaveOptions, callback: AsyncCallback<Array<string>>): void;
        /**
         * Starts an **audioPicker** page (currently, a **documentPicker** page is displayed) for the user to save one or
         * more audio clips. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<Array<string>> } callback - Callback invoked to return the URIs of the audio clips saved.
         *     <br>**Note**: For details about how to use the returned URIs, see
         *     [Using a Document URI](docroot://file-management/user-file-uri-intro.md#using-a-document-uri).
         * @syscap SystemCapability.FileManagement.UserFileService
         * @crossplatform [since 12]
         * @since 9
         */
        save(callback: AsyncCallback<Array<string>>): void;
    }
}
export default picker;

```
