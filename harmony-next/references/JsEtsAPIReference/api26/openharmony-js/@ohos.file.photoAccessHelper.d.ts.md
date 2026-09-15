# @ohos.file.photoAccessHelper.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (C) 2023-2025 Huawei Device Co., Ltd.
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
 * @file Helper functions to access image and video assets
 * @kit MediaLibraryKit
 */
import type { AsyncCallback, Callback } from './@ohos.base';
import type Context from './application/Context';
import type image from './@ohos.multimedia.image';
import type dataSharePredicates from './@ohos.data.dataSharePredicates';
/**
 * The module provides APIs for album management, including creating an album and accessing and modifying media data in
 * an album.
 *
 * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
 * @crossplatform [since 12]
 * @atomicservice [since 11]
 * @since 10
 */
declare namespace photoAccessHelper {
    /**
     * Obtains a PhotoAccessHelper instance for accessing and modifying media files in the album.
     *
     * @param { Context } context - Context of the ability instance.
     * @returns { PhotoAccessHelper } PhotoAccessHelper instance obtained.
     * @throws { BusinessError } 401 - Parameter error. Possible causes:
     *     <br>1. Mandatory parameters are left unspecified;
     *     <br>2. Incorrect parameter types;
     *     <br>3. Parameter verification failed.
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @stagemodelonly
     * @crossplatform [since 12]
     * @atomicservice [since 11]
     * @since 10
     */
    function getPhotoAccessHelper(context: Context): PhotoAccessHelper;
    /**
     * Describes the information about the context of exiting the PhotoPicker. It can be used during the subsequent launch
     * of the PhotoPicker to restore the state from the previous exit.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @atomicservice
     * @since 21
     */
    export class ContextRecoveryInfo {
        /**
         * URI of the album in the media library when the user selects an image and exits.
         *
         * - If the user selects from all images, **albumUri** is a fixed **"allPhotos"** string.
         * - If the user exits after selecting from search results, text recommendations, or avatar recommendations, the
         * next restoration is not supported, and the returned **albumUri** is an empty string.
         *
         * The default value is an empty string.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 21
         */
        albumUri: string;
        /**
         * Time of the top-left image in the grid interface when the user last selected an image.
         *
         * - For albums sorted by capture time, the capture time is returned.
         * - For albums sorted by save time, the save time is returned. The default value is **0**.
         *
         * Unit: ms, The value must be greater than or equal to 0.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 21
         */
        time: number;
        /**
         * File name of the top-left image in the grid interface when the user last selected an image. The default value is
         * an empty string.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 21
         */
        displayName: string;
        /**
         * Enumerated value of the recommended content set by the user during the last selection. For details, see
         * [RecommendationType]{@link @ohos.file.photoAccessHelper:photoAccessHelper.RecommendationType}.
         *
         * If no recommendation was set during the last selection, the default value is **0**.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 21
         */
        recommendationType: number;
        /**
         * Enumerated value of the recommended content selected by the user during the last selection. For details, see
         * [RecommendationType]{@link @ohos.file.photoAccessHelper:photoAccessHelper.RecommendationType}.
         *
         * If no recommendation was selected during the last selection or **All** was selected, the default value is **0**.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 21
         */
        selectedRecommendationType: number;
        /**
         * Version number of the state data, used to verify the compatibility of the state information data with the state
         * recovery capability.
         *
         * The version number must be greater than or equal to 1.0.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 21
         */
        version: number;
        /**
         * Level of the grid when the user exits last time.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        gridLevel?: GridLevel;
        /**
         * Sorting rule of the grid interface when the user last selected an image. The default value is an empty string.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        sortRule?: string;
        /**
         * File size of the top-left image in the grid interface when the user last selected an image. The default value is
         * **0**.
         * Unit: Byte, The value must be an integer greater than or equal to 0.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        fileSize?: number;
    }
    /**
     * Enumerates the media file types.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @crossplatform [since 12]
     * @atomicservice [since 11]
     * @since 10
     */
    enum PhotoType {
        /**
         * Image.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        IMAGE = 1,
        /**
         * Video.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        VIDEO = 2
    }
    /**
     * Enumerates the [PhotoAsset]{@link photoAccessHelper.PhotoAsset} types.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @atomicservice
     * @since 12
     */
    export enum PhotoSubtype {
        /**
         * Photo, which is the default type.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 12
         */
        DEFAULT = 0,
        /**
         * Moving photo.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 12
         */
        MOVING_PHOTO = 3,
        /**
         * Burst photo.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 12
         */
        BURST = 4
    }
    /**
     * Enumerates the dynamic range types of media assets.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @since 12
     */
    export enum DynamicRangeType {
        /**
         * Standard dynamic range (SDR).
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 12
         */
        SDR = 0,
        /**
         * High dynamic range (HDR).
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 12
         */
        HDR = 1
    }
    /**
     * Enumerates the file locations.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @since 16
     */
    enum PositionType {
        /**
         * Stored only on a local device.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 16
         */
        LOCAL = 1,
        /**
         * Stored only on the cloud.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 16
         */
        CLOUD = 2,
        /**
         * Stored both on a local device and cloud.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 16
         */
        LOCAL_AND_CLOUD = 3
    }
    /**
     * Enumerates the types of recommended images.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @atomicservice
     * @since 11
     */
    enum RecommendationType {
        /**
         * QR code or barcode.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 11
         */
        QR_OR_BAR_CODE = 1,
        /**
         * QR code.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 11
         */
        QR_CODE = 2,
        /**
         * Barcode.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 11
         */
        BAR_CODE = 3,
        /**
         * ID card.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 11
         */
        ID_CARD = 4,
        /**
         * Profile.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 11
         */
        PROFILE_PICTURE = 5,
        /**
         * Passport.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 12
         */
        PASSPORT = 6,
        /**
         * Bank card.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 12
         */
        BANK_CARD = 7,
        /**
         * Driver license.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 12
         */
        DRIVER_LICENSE = 8,
        /**
         * Vehicle license.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 12
         */
        DRIVING_LICENSE = 9,
        /**
         * Recommended portrait.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 12
         */
        FEATURED_SINGLE_PORTRAIT = 10
    }
    /**
     * Enumerates the asset delivery modes.
     *
     * These modes are used for segmented photo or video delivery. If the device does not support segmentation, the three
     * delivery modes below work the same way and just return the requested image or video directly. The request result is
     * returned through the
     * [onDataPrepared]{@link @ohos.file.photoAccessHelper:photoAccessHelper.MediaAssetDataHandler.onDataPrepared(data: T, map?: Map<string, string>)}
     * callback.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @since 11
     */
    enum DeliveryMode {
        /**
         * Fast mode.
         *
         * For segmented photo or video delivery, if a high-quality version is available, it quickly returns the callback
         * for that high-quality version. If only a low-quality version is available, it returns the callback for the low-
         * quality version right away.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 11
         */
        FAST_MODE = 0,
        /**
         * High-quality mode.
         *
         * For segmented photo or video delivery, if a high-quality version is available, it quickly returns the callback
         * for that high-quality version. If only a low-quality version is available, it starts a task to generate a high-
         * quality version and returns the callback for the high-quality version once that version is ready.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 11
         */
        HIGH_QUALITY_MODE = 1,
        /**
         * Balance mode.
         *
         * - For segmented photo delivery, if a high-quality version is available, it quickly returns the callback for that
         * high-quality version. If only a low-quality version is available, it returns the callback for the low-quality
         * version, starts a task to generate a high-quality version, and returns the callback for the high-quality version
         * once that version is ready.
         * - For segmented video delivery, if a high-quality version is available, it quickly returns the callback for that
         * high-quality version. If only a low-quality version is available, it returns the callback for the low-quality
         * version right away.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 11
         */
        BALANCE_MODE = 2
    }
    /**
     * Enumerates the compatible modes.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @since 15
     */
    enum CompatibleMode {
        /**
         * Maintains the original video format.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 15
         */
        ORIGINAL_FORMAT_MODE = 0,
        /**
         * Converts the HDR content to SDR format.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 15
         */
        COMPATIBLE_FORMAT_MODE = 1
    }
    /**
     * **MediaAssetProgressHandler** is used to obtain the media asset processing progress from **onProgress()**.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @since 15
     */
    interface MediaAssetProgressHandler {
        /**
         * Called when the progress of the requested video is returned.
         *
         * @param { number } progress - Progress in percentage. <br>Value range: [0, 100]
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 15
         */
        onProgress(progress: number): void;
    }
    /**
     * Enumerates the text displayed on the complete button.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @atomicservice
     * @since 14
     */
    enum CompleteButtonText {
        /**
         * The text "Done" is displayed.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 14
         */
        TEXT_DONE = 0,
        /**
         * The text "Send" is displayed.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 14
         */
        TEXT_SEND = 1,
        /**
         * The text "Add" is displayed.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 14
         */
        TEXT_ADD = 2
    }
    /**
     * Represents request options.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @since 11
     */
    interface RequestOptions {
        /**
         * Delivery mode of the requested asset. The value can be **FAST_MODE**, **HIGH_QUALITY_MODE**, or **BALANCE_MODE**.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 11
         */
        deliveryMode: DeliveryMode;
        /**
         * HDR video transcoding policy, which can be **FAST_ORIGINAL_FORMAT_MODE** (maintaining the original HDR format) or
         * **COMPATIBLE_FORMAT_MODE** (converting HDR content to SDR format). The default value is
         * **FAST_ORIGINAL_FORMAT_MODE**.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 15
         */
        compatibleMode?: CompatibleMode;
        /**
         * Callback used to return the HDR-to-SDR conversion progress.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 15
         */
        mediaAssetProgressHandler?: MediaAssetProgressHandler;
    }
    /**
     * MediaAssetDataHandler is a media asset handler used to customize the media asset processing logic in
     * **onDataPrepared**.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @since 11
     */
    interface MediaAssetDataHandler<T> {
        /**
         * Called when the requested media asset is ready. If an error occurs, **data** returned by the callback is
         * **undefined**. Each media asset request corresponds to a callback.
         *
         * T supports the following data types: ArrayBuffer, [ImageSource]{@link @ohos.multimedia.image:image.ImageSource},
         * [MovingPhoto]{@link @ohos.file.photoAccessHelper:photoAccessHelper}, and boolean. ArrayBuffer indicates the image
         * or video asset data, [ImageSource]{@link @ohos.multimedia.image:image.ImageSource} indicates the image source,
         * [MovingPhoto]{@link @ohos.file.photoAccessHelper:photoAccessHelper} indicates a moving photo object, and boolean
         * indicates whether the image or video is successfully written to the application sandbox directory.
         *
         * Information returned by **map**:
         *
         * | Map Key | Description|
         * |----------|-------|
         * | 'quality'  | Image quality. The value **high** means high quality, and **low** means poor quality.|
         *
         * @param { T } data - Data of the image asset that is ready. It is of the generic type and supports the following
         *     data types: ArrayBuffer, [ImageSource]{@link @ohos.multimedia.image:image.ImageSource},
         *     [MovingPhoto]{@link @ohos.file.photoAccessHelper:photoAccessHelper}, and boolean.
         * @param { Map<string, string> } [map] - Additional information about the image asset, such as the image quality.
         *     Currently, only **quality** is supported. [since 12]
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 11
         */
        onDataPrepared(data: T, map?: Map<string, string>): void;
    }
    /**
     * QuickImageDataHandler is a media asset handler used to customize the media asset processing logic in
     * **onDataPrepared**.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @since 13
     */
    interface QuickImageDataHandler<T> {
        /**
         * Called when the requested image is ready. If an error occurs, **data** returned by the callback is **undefined**.
         *
         * Information returned by **map**:
         *
         * | Map Key | **Description**|
         * |----------|-------|
         * | 'quality'  | Image quality. The value **high** means high quality, and **low** means poor quality.|
         *
         * @param { T } data - Data of the image asset that is ready. It is of the generic type and supports the
         *     [Picture]{@link @ohos.multimedia.image:image.Picture} type.
         * @param { image.ImageSource } imageSource - Data of the image asset that is ready.
         * @param { Map<string, string> } map - Additional information about the image asset, such as the image quality.
         *     Currently, only **quality** is supported.
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 13
         */
        onDataPrepared(data: T, imageSource: image.ImageSource, map: Map<string, string>): void;
    }
    /**
     * The MediaAssetManager class is used for manipulating the read and write operations of media assets.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @atomicservice [since 14]
     * @since 11
     */
    class MediaAssetManager {
        /**
         * Requests an image. This API uses a promise to return the result.
         *
         * @permission ohos.permission.READ_IMAGEVIDEO
         * @param { Context } context - Context of the ability instance.
         * @param { PhotoAsset } asset - Image to request.
         * @param { RequestOptions } requestOptions - Options for requesting the image.
         * @param { MediaAssetDataHandler<image.ImageSource> } dataHandler - Media asset handler, which invokes a callback
         *     to return the image when the requested image is ready.
         * @returns { Promise<string> } Promise used to return the request ID, which can be used in
         *     [cancelRequest]{@link photoAccessHelper.MediaAssetManager.cancelRequest} to cancel a request.
         * @throws { BusinessError } 201 - Permission denied
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 14000011 - System inner fail. Possible causes:
         *     <br>1. The database is corrupted;
         *     <br>2. The file system is abnormal;
         *     <br>3. The IPC request timed out.
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 11
         */
        static requestImage(context: Context, asset: PhotoAsset, requestOptions: RequestOptions, dataHandler: MediaAssetDataHandler<image.ImageSource>): Promise<string>;
        /**
         * Requests an image quickly. This API uses a promise to return the result.
         *
         * @permission ohos.permission.READ_IMAGEVIDEO
         * @param { Context } context - Context of the ability instance.
         * @param { PhotoAsset } asset - Image to request.
         * @param { RequestOptions } requestOptions - Options for requesting the image.
         * @param { QuickImageDataHandler<image.Picture> } dataHandler - Media asset handler, which invokes a callback to
         *     return the image when the requested image is ready.
         * @returns { Promise<string> } Promise used to return the request ID, which can be used in
         *     [cancelRequest]{@link photoAccessHelper.MediaAssetManager.cancelRequest} to cancel a request.
         * @throws { BusinessError } 201 - Permission denied
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 14000011 - Internal system error
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 13
         */
        static quickRequestImage(context: Context, asset: PhotoAsset, requestOptions: RequestOptions, dataHandler: QuickImageDataHandler<image.Picture>): Promise<string>;
        /**
         * Requests image data. This API uses a promise to return the result.
         *
         * @permission ohos.permission.READ_IMAGEVIDEO
         * @param { Context } context - Context of the ability instance.
         * @param { PhotoAsset } asset - Image to request.
         * @param { RequestOptions } requestOptions - Options for requesting the image.
         * @param { MediaAssetDataHandler<ArrayBuffer> } dataHandler - Media asset handler, which invokes a callback to
         *     return the image when the requested image is ready.
         * @returns { Promise<string> } Promise used to return the request ID, which can be used in
         *     [cancelRequest]{@link photoAccessHelper.MediaAssetManager.cancelRequest} to cancel a request.
         * @throws { BusinessError } 201 - Permission denied
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 14000011 - System inner fail. Possible causes:
         *     <br>1. The database is corrupted;
         *     <br>2. The file system is abnormal;
         *     <br>3. The IPC request timed out.
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 11
         */
        static requestImageData(context: Context, asset: PhotoAsset, requestOptions: RequestOptions, dataHandler: MediaAssetDataHandler<ArrayBuffer>): Promise<string>;
        /**
         * Requests a moving photo object, which can be used to request the asset data of the moving photo. This API uses a
         * promise to return the result.
         *
         * @permission ohos.permission.READ_IMAGEVIDEO
         * @param { Context } context - Context of the ability instance.
         * @param { PhotoAsset } asset - Image to request.
         * @param { RequestOptions } requestOptions - Options for requesting the image.
         * @param { MediaAssetDataHandler<MovingPhoto> } dataHandler - Media asset handler, which invokes a callback to
         *     return the image when the requested image is ready.
         * @returns { Promise<string> } Promise used to return the request ID, which can be used in
         *     [cancelRequest]{@link photoAccessHelper.MediaAssetManager.cancelRequest} to cancel a request.
         * @throws { BusinessError } 201 - Permission denied
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 801 - Capability not supported. [since 18]
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 12
         */
        static requestMovingPhoto(context: Context, asset: PhotoAsset, requestOptions: RequestOptions, dataHandler: MediaAssetDataHandler<MovingPhoto>): Promise<string>;
        /**
         * Cancels a request for the asset, the callback of which has not been triggered yet. This API uses a promise to
         * return the result.
         *
         * @permission ohos.permission.READ_IMAGEVIDEO
         * @param { Context } context - Context of the ability instance.
         * @param { string } requestId - ID of the request to cancel. It is a valid request ID returned by **requestImage**.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 201 - Permission denied
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 12
         */
        static cancelRequest(context: Context, requestId: string): Promise<void>;
        /**
         * Requests a video and saves it to the specified sandbox directory. This API uses a promise to return the result.
         *
         * @permission ohos.permission.READ_IMAGEVIDEO
         * @param { Context } context - Context of the ability instance.
         * @param { PhotoAsset } asset - Image to request.
         * @param { RequestOptions } requestOptions - Options for requesting the video asset.
         * @param { string } fileUri - URI of the sandbox directory, to which the requested video asset is to be saved.
         *     Example: **'file://com.example.temptest/data/storage/el2/base/haps/entry/files/test.mp4'**.
         * @param { MediaAssetDataHandler<boolean> } dataHandler - Media asset handler. When the requested video is written
         *     to the specified directory, a callback is triggered.
         *     <br>If the video is successfully written, **true** is returned. Otherwise, **false** is returned.
         * @returns { Promise<string> } Promise used to return the request ID, which can be used in
         *     [cancelRequest]{@link photoAccessHelper.MediaAssetManager.cancelRequest} to cancel a request.
         * @throws { BusinessError } 201 - Permission denied
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 801 - Capability not supported. [since 15]
         * @throws { BusinessError } 14000011 - System inner fail. Possible causes:
         *     <br>1. The database is corrupted;
         *     <br>2. The file system is abnormal;
         *     <br>3. The IPC request timed out.
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 12
         */
        static requestVideoFile(context: Context, asset: PhotoAsset, requestOptions: RequestOptions, fileUri: string, dataHandler: MediaAssetDataHandler<boolean>): Promise<string>;
        /**
         * Loads a moving photo in the application sandbox. This API uses a promise to return the result.
         *
         * @param { Context } context - AbilityContext or UIExtensionContext instance.
         * @param { string } imageFileUri - URI of the image file of the moving photo in the application sandbox.
         *     <br>Example: **'file://com.example.temptest/data/storage/el2/base/haps/ImageFile.jpg'**.
         * @param { string } videoFileUri - URI of the video file of the moving photo in the application sandbox.
         *     <br>Example: **'file://com.example.temptest/data/storage/el2/base/haps/VideoFile.mp4'**.
         * @returns { Promise<MovingPhoto> } Promise used to return the
         *     [MovingPhoto]{@link @ohos.file.photoAccessHelper:photoAccessHelper} instance.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 14000011 - Internal system error
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice [since 14]
         * @since 12
         */
        static loadMovingPhoto(context: Context, imageFileUri: string, videoFileUri: string): Promise<MovingPhoto>;
    }
    /**
     * Defines the types of the PhotoAsset members.
     *
     * The member types are the union of the types listed in the following table.
     *
     * @unionmember { int } The member value is an integer.
     * @unionmember { long } The member value is a long integer.
     * @unionmember { double } The member value is a decimal number.
     * @unionmember { string } The member value is any string.
     * @unionmember { boolean } The member value is true or false.
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @crossplatform [since 12]
     * @since 10
     */
    type MemberType = number | string | boolean;
    /**
     * Defines the array of record types that map file property names to their values.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @since 21
     */
    type PhotoAssetParams = Record<string, MemberType>[];
    /**
     * PhotoAsset provides APIs for encapsulating file asset attributes.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @crossplatform [since 12]
     * @atomicservice [since 11]
     * @since 10
     */
    interface PhotoAsset {
        /**
         * Media asset URI, for example, **file://media/Photo/1/IMG_datetime_0001/displayName.jpg**. For details, see
         * [Media File URI](docroot://file-management/user-file-uri-intro.md#media-file-uri).
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 10
         */
        readonly uri: string;
        /**
         * Type of the file.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @atomicservice [since 20]
         * @since 10
         */
        readonly photoType: PhotoType;
        /**
         * File name, including the file name extension, to display. The string length ranges from 1 to 255.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @atomicservice [since 20]
         * @since 10
         */
        readonly displayName: string;
        /**
         * Obtains a **PhotoAsset** member parameter.
         *
         * @param { string } member - Name of the member parameter to obtain. Except **'uri'**, **'media_type'**,
         *     **'subtype'**, and **'display_name'**, you need to pass in
         *     [PhotoKeys]{@link @ohos.file.photoAccessHelper:photoAccessHelper.PhotoKeys} in **fetchColumns**. For example,
         *     to obtain the title, pass in **fetchColumns: ['title']**.
         * @returns { MemberType } **PhotoAsset** member parameter obtained.
         * @throws { BusinessError } 13900020 - Invalid argument
         * @throws { BusinessError } 14000014 - The provided member must be a property name of PhotoKey.
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @atomicservice [since 20]
         * @since 10
         */
        get(member: string): MemberType;
        /**
         * Sets a **PhotoAsset** member parameter.
         *
         * @param { string } member - Name of the member parameter to set, for example,
         *     [PhotoKeys]{@link @ohos.file.photoAccessHelper:photoAccessHelper.PhotoKeys}.TITLE. The string length ranges
         *     from 1 to 255.
         * @param { string } value - Value of the member parameter to set. Only the value of
         *     [PhotoKeys]{@link @ohos.file.photoAccessHelper:photoAccessHelper.PhotoKeys}.TITLE can be changed. The title
         *     must meet the following requirements:
         *     <br>- It must not contain a file name extension.
         *     <br>- The string length
         *     ranges from 1 to 255. (The asset file name is in the format of title + file name extension.)
         *     <br>- It must not contain any invalid characters, which are:\ / : * ? " ' ` < > | { } [ ]
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 13900020 - Invalid argument
         * @throws { BusinessError } 14000014 - The provided member must be a property name of PhotoKey.
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 10
         * @example : set(PhotoKeys.TITLE, "newTitle"), call commitModify after set
         */
        set(member: string, value: string): void;
        /**
         * Commits the modification on the file metadata to the database. This API uses an asynchronous callback to return
         * the result.
         *
         * @permission ohos.permission.WRITE_IMAGEVIDEO
         * @param { AsyncCallback<void> } callback - Callback function. If the file metadata is modified successfully,
         *     **err** is **undefined**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 201 - Permission denied [since 11]
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types.
         * @throws { BusinessError } 13900012 - Permission denied [since 10 - 10]
         * @throws { BusinessError } 13900020 - Invalid argument
         * @throws { BusinessError } 14000001 - Invalid display name
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice [since 11]
         * @since 10
         */
        commitModify(callback: AsyncCallback<void>): void;
        /**
         * Commits the modification on the file metadata to the database. This API uses a promise to return the result.
         *
         * @permission ohos.permission.WRITE_IMAGEVIDEO
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 201 - Permission denied [since 11]
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types.
         * @throws { BusinessError } 13900012 - Permission denied [since 10 - 10]
         * @throws { BusinessError } 13900020 - Invalid argument
         * @throws { BusinessError } 14000001 - Invalid display name
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice [since 11]
         * @since 10
         */
        commitModify(): Promise<void>;
        /**
         * Opens this file in read-only mode. This API uses an asynchronous callback to return the result.
         *
         * The returned FD must be closed when it is not required.
         *
         * @permission ohos.permission.READ_IMAGEVIDEO
         * @param { AsyncCallback<number> } callback - Callback function. If the current file is opened successfully,
         *     **err** is **undefined**, and **data** is the file descriptor. Otherwise, **err** is an error object.
         * @throws { BusinessError } 201 - Permission denied
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types.
         * @throws { BusinessError } 13900020 - Invalid argument
         * @throws { BusinessError } 14000011 - System inner fail. Possible causes:
         *     <br>1. The database is corrupted;
         *     <br>2. The file system is abnormal;
         *     <br>3. The IPC request timed out.
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 10
         * @deprecated since 11
         * @useinstead @ohos.file.fs:fileIo.open
         */
        getReadOnlyFd(callback: AsyncCallback<number>): void;
        /**
         * Opens this file in read-only mode. This API uses a promise to return the result.
         *
         * The returned FD must be closed when it is not required.
         *
         * @permission ohos.permission.READ_IMAGEVIDEO
         * @returns { Promise<number> } Promise used to return the FD of the file opened.
         * @throws { BusinessError } 201 - Permission denied
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types.
         * @throws { BusinessError } 13900020 - Invalid argument
         * @throws { BusinessError } 14000011 - System inner fail. Possible causes:
         *     <br>1. The database is corrupted;
         *     <br>2. The file system is abnormal;
         *     <br>3. The IPC request timed out.
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 10
         * @deprecated since 11
         * @useinstead @ohos.file.fs:fileIo.open
         */
        getReadOnlyFd(): Promise<number>;
        /**
         * Closes the current file. This API uses an asynchronous callback to return the result.
         *
         * @param { number } fd - FD of the file to close.
         * @param { AsyncCallback<void> } callback - Callback function. If the current file is closed successfully, **err**
         *     is **undefined**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 13900020 - Invalid argument.
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 10
         * @deprecated since 11
         * @useinstead @ohos.file.fs:fileIo.close
         */
        close(fd: number, callback: AsyncCallback<void>): void;
        /**
         * Closes the current file. This API uses a promise to return the result.
         *
         * @param { number } fd - FD of the file to close.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 13900020 - Invalid argument
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 10
         * @deprecated since 11
         * @useinstead @ohos.file.fs:fileIo.close
         */
        close(fd: number): Promise<void>;
        /**
         * Obtains the thumbnail of a file. This API uses an asynchronous callback to return the result.
         *
         * @permission ohos.permission.READ_IMAGEVIDEO
         * @param { AsyncCallback<image.PixelMap> } callback - Callback function. If the thumbnail of a file is successfully
         *     obtained, **err** is **undefined**, and **data** is the PixelMap of the thumbnail. Otherwise, **err** is an
         *     error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types.
         * @throws { BusinessError } 13900012 - Permission denied
         * @throws { BusinessError } 13900020 - Invalid argument
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice [since 22]
         * @since 10
         */
        getThumbnail(callback: AsyncCallback<image.PixelMap>): void;
        /**
         * Obtains the file thumbnail of the given size. This API uses an asynchronous callback to return the result.
         *
         * @permission ohos.permission.READ_IMAGEVIDEO
         * @param { image.Size } size - Size of the thumbnail.
         * @param { AsyncCallback<image.PixelMap> } callback - Callback function. If the thumbnail of a file is successfully
         *     obtained, **err** is **undefined**, and **data** is the PixelMap of the thumbnail. Otherwise, **err** is an
         *     error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 13900012 - Permission denied
         * @throws { BusinessError } 13900020 - Invalid argument
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice [since 22]
         * @since 10
         */
        getThumbnail(size: image.Size, callback: AsyncCallback<image.PixelMap>): void;
        /**
         * Obtains the file thumbnail of the given size. This API uses a promise to return the result.
         *
         * @permission ohos.permission.READ_IMAGEVIDEO
         * @param { image.Size } [size] - Size of the thumbnail.
         * @returns { Promise<image.PixelMap> } Promise used to return the PixelMap of the thumbnail.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 13900012 - Permission denied
         * @throws { BusinessError } 13900020 - Invalid argument
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice [since 22]
         * @since 10
         */
        getThumbnail(size?: image.Size): Promise<image.PixelMap>;
        /**
         * Clones a media asset. The file name can be set, but the file type cannot be changed. This API uses a promise to
         * return the result.
         *
         * @permission ohos.permission.WRITE_IMAGEVIDEO
         * @param { string } title - Title of the cloned asset. The title must meet the following requirements:
         *     <br>- It must not contain a file name extension.
         *     <br>- The string length ranges from 1 to 255. (The asset file name is in
         *     the format of title + file name extension.)
         *     <br>- It must not contain any invalid characters, which are:\ / : * ? " ' ` < > | { } [ ]
         * @returns { Promise<PhotoAsset> } Promise used to return the
         *     [PhotoAsset]{@link @ohos.file.photoAccessHelper:photoAccessHelper} instance.
         * @throws { BusinessError } 201 - Permission denied
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 14000011 - Internal system error. It is recommended to retry and check the logs.
         *     <br>Possible causes:
         *     <br>1. Database corrupted;
         *     <br>2. The file system is abnormal;
         *     <br>3. The IPC request timed out.
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 14
         */
        clone(title: string): Promise<PhotoAsset>;
    }
    /**
     * Defines the key information about an image or video file.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @crossplatform [since 12]
     * @atomicservice [since 20]
     * @since 10
     */
    enum PhotoKeys {
        /**
         * URI of the file.
         *
         * **Note**:
         *
         * Only the
         * [DataSharePredicates.equalTo]{@link @ohos.data.dataSharePredicates:dataSharePredicates.DataSharePredicates.equalTo}
         * predicate can be used for this field during photo query.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @atomicservice [since 20]
         * @since 10
         */
        URI = 'uri',
        /**
         * Type of the file.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @atomicservice [since 20]
         * @since 10
         */
        PHOTO_TYPE = 'media_type',
        /**
         * File name displayed. The file name must meet the following requirements:
         *
         * - A valid file name must include a base name and a supported image or video extension.
         * - The file name length ranges from 1 to 255.
         * - The base name must not contain any invalid characters, which are:.. \ / : * ? " ' ` < > | { } [ ]
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @atomicservice [since 20]
         * @since 10
         */
        DISPLAY_NAME = 'display_name',
        /**
         * File size, in bytes. The size of a moving photo includes the total size of the image and video.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @atomicservice [since 20]
         * @since 10
         */
        SIZE = 'size',
        /**
         * Unix timestamp when the file was created, in seconds.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @atomicservice [since 20]
         * @since 10
         */
        DATE_ADDED = 'date_added',
        /**
         * Unix timestamp when the file content (not the file name) was last modified, in seconds. This value is updated
         * when the file content is modified, but not when the file name is modified.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @atomicservice [since 20]
         * @since 10
         */
        DATE_MODIFIED = 'date_modified',
        /**
         * Duration, in ms.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @atomicservice [since 20]
         * @since 10
         */
        DURATION = 'duration',
        /**
         * Image width, in pixels.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @atomicservice [since 20]
         * @since 10
         */
        WIDTH = 'width',
        /**
         * Image height, in pixels.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @atomicservice [since 20]
         * @since 10
         */
        HEIGHT = 'height',
        /**
         * Unix timestamp when the photo was taken, in seconds.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @atomicservice [since 20]
         * @since 10
         */
        DATE_TAKEN = 'date_taken',
        /**
         * Orientation of the file, in degrees.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @atomicservice [since 20]
         * @since 10
         */
        ORIENTATION = 'orientation',
        /**
         * Whether the file is marked as favorites.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @atomicservice [since 20]
         * @since 10
         */
        FAVORITE = 'is_favorite',
        /**
         * Title of the file.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @atomicservice [since 20]
         * @since 10
         */
        TITLE = 'title',
        /**
         * File location type.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice [since 20]
         * @since 16
         */
        POSITION = 'position',
        /**
         * Unix timestamp when the file was created, in milliseconds.
         *
         * **Note**:
         *
         * The photos queried cannot be sorted based on this field.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice [since 20]
         * @since 12
         */
        DATE_ADDED_MS = 'date_added_ms',
        /**
         * Unix timestamp when the file was modified, in milliseconds. This value is updated when the file content is
         * modified, but not when the file name is modified.
         *
         * **Note**:
         *
         * The photos queried cannot be sorted based on this field.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice [since 20]
         * @since 12
         */
        DATE_MODIFIED_MS = 'date_modified_ms',
        /**
         * Subtype of the media file.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice [since 20]
         * @since 12
         */
        PHOTO_SUBTYPE = 'subtype',
        /**
         * Dynamic range type of the media asset.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice [since 20]
         * @since 12
         */
        DYNAMIC_RANGE_TYPE = 'dynamic_range_type',
        /**
         * Position of the moving photo cover, which is the video timestamp (in μs) corresponding to the cover frame.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice [since 20]
         * @since 12
         */
        COVER_POSITION = 'cover_position',
        /**
         * Unique ID of a group of burst photos.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice [since 20]
         * @since 12
         */
        BURST_KEY = 'burst_key',
        /**
         * Width and height of an LCD image, in the format of a **width:height** string.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice [since 20]
         * @since 12
         */
        LCD_SIZE = 'lcd_size',
        /**
         * Width and height of a thumbnail image, in the format of a **width:height** string.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice [since 20]
         * @since 12
         */
        THM_SIZE = 'thm_size',
        /**
         * Detailed time. The value is a string of time when the image or video was taken in the time zone and does not
         * change with the time zone.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice [since 20]
         * @since 13
         */
        DETAIL_TIME = 'detail_time',
        /**
         * Unix timestamp when the image was captured, in milliseconds.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice [since 20]
         * @since 13
         */
        DATE_TAKEN_MS = 'date_taken_ms',
        /**
         * ID of the album to which the photo belongs.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 22
         */
        OWNER_ALBUM_ID = 'owner_album_id',
        /**
         * File name extension.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 18
         */
        MEDIA_SUFFIX = 'media_suffix',
        /**
         * Aspect ratio of the image or video.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @since 22
         */
        ASPECT_RATIO = 'aspect_ratio',
        /**
         * Time when the photo is changed.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 23
         */
        CHANGE_TIME = 'change_time',
        /**
         * Size of local asset, which well matched the content read by the application.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        LOCAL_ASSET_SIZE = 'local_asset_size'
    }
    /**
     * Enumeration of fusion asset type
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @crossplatform
     * @since 22
     */
    enum FusionAssetType {
    }
    /**
     * Enumerates the album keys.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @crossplatform [since 12]
     * @since 10
     */
    enum AlbumKeys {
        /**
         * URI of the album.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @since 10
         */
        URI = 'uri',
        /**
         * Name of the album.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @since 10
         */
        ALBUM_NAME = 'album_name',
        /**
         * Virtual path of the album.
         *
         * Albums and their virtual path values:
         *
         * - Camera application album: '/DCIM/Camera'
         * - Screenshot application album: '/Pictures/Screenshots'
         * - Screen recording application album: '/Pictures/Screenrecords'
         * - User-created album: '/Pictures/Users/{Custom album name}'
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 23
         */
        ALBUM_LPATH = 'lpath',
        /**
         * Time when the album is changed.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 23
         */
        CHANGE_TIME = 'change_time'
    }
    /**
     * Defines the retrieval options.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @crossplatform [since 12]
     * @atomicservice [since 20]
     * @since 10
     */
    interface FetchOptions {
        /**
         * Names of the columns specified for query.
         *
         * If this parameter is left blank for photos, photos are fetched by **'uri'**, **'media_type'**, **'subtype'**, and
         * **'display_name'** by default. An error will be thrown if
         * [get]{@link @ohos.file.photoAccessHelper:photoAccessHelper.PhotoAsset.get} is used to obtain other attributes of
         * this object.
         *
         * Example: **fetchColumns: ['uri', 'title']**.
         *
         * If this parameter is left blank for albums, albums are fetched by **'uri'** and **'album_name'** by default.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @atomicservice [since 20]
         * @since 10
         */
        fetchColumns: Array<string>;
        /**
         * Predicates that specify the fetch criteria.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @atomicservice [since 20]
         * @since 10
         */
        predicates: dataSharePredicates.DataSharePredicates;
    }
    /**
     * Represents the configuration for saving a media asset (image or video) to the media library, including the file
     * name.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @atomicservice
     * @since 12
     */
    interface PhotoCreationConfig {
        /**
         * Title of the image or video. If this parameter is not passed, the system generates a title. The title must meet
         * the following requirements:
         *
         * - It must not contain a file name extension.
         * - The total length of the file name, which is in the format of title+file name extension, must be between 1 and 2
         * 55 characters.
         * - It must not contain any invalid characters, which are:\ / : * ? " ' ` < > | { } [ ]
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 12
         */
        title?: string;
        /**
         * File name extension, for example, **'jpg'**.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 12
         */
        fileNameExtension: string;
        /**
         * Type of the file to create, which can be **IMAGE** or **VIDEO**. See
         * [PhotoType]{@link @ohos.file.photoAccessHelper:photoAccessHelper.PhotoType}.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 12
         */
        photoType: PhotoType;
        /**
         * Image or video file subtype. The default value is **DEFAULT**. See
         * [PhotoSubtype]{@link @ohos.file.photoAccessHelper:photoAccessHelper.PhotoSubtype}.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 12
         */
        subtype?: PhotoSubtype;
    }
    /**
     * Represents the configuration for saving images or videos to the media library, including the file name, file type,
     * and other related parameters.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @stagemodelonly
     * @atomicservice
     * @since 23
     */
    export interface CreationSetting {
        /**
         * Title of the image or video.
         *
         * If this parameter is not passed, the system generates a value. The parameter specifications are as follows:
         *
         * - It must not contain a file name extension.
         * - It must not contain any invalid characters, which are:\ / : * ? " ' ` < > | { } [ ]
         * - The file name consists of the title and file name extension. The file name string length ranges from 1 to 255.
         * Therefore, the title length cannot be too long.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        title?: string;
        /**
         * File name extension, for example, **'jpg'**.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        fileNameExtension: string;
        /**
         * [PhotoType]{@link @ohos.file.photoAccessHelper:photoAccessHelper.PhotoType} of the created media file, which can
         * be **IMAGE** or **VIDEO**.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        photoType: PhotoType;
    }
    /**
     * Options for creating an image or video asset.
     *
     * The title must meet the following requirements:
     *
     * - It must not contain a file name extension.
     * - The total length of the file name must be between 1 and 255 characters.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @crossplatform [since 22]
     * @atomicservice [since 11]
     * @since 10
     */
    interface CreateOptions {
        /**
         * Title of the image or video.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 22]
         * @atomicservice [since 11]
         * @since 10
         */
        title?: string;
        /**
         * Subtype of the image or video file.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 12
         */
        subtype?: PhotoSubtype;
    }
    /**
     * FetchResult provides APIs to manage the file retrieval result.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @crossplatform [since 12]
     * @atomicservice [since 20]
     * @since 10
     */
    interface FetchResult<T> {
        /**
         * Obtains the total number of files in the result set.
         *
         * @returns { number } Total number of files obtained.
         * @throws { BusinessError } 13900020 - Invalid argument
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @atomicservice [since 20]
         * @since 10
         */
        getCount(): number;
        /**
         * Checks whether the cursor is in the last row of the result set.
         *
         * @returns { boolean } **true** is returned if the cursor is in the last row of the result set; **false**
         *     otherwise.
         * @throws { BusinessError } 13900020 - Invalid argument
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @atomicservice [since 20]
         * @since 10
         */
        isAfterLast(): boolean;
        /**
         * Obtains the first file asset in the result set. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<T> } callback - Callback function. If the first file asset in the result set is
         *     successfully obtained, **err** is **undefined**, and **data** is the specific search result. Otherwise,
         *     **err** is an error object.
         * @throws { BusinessError } 13900020 - Invalid argument
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @atomicservice [since 20]
         * @since 10
         */
        getFirstObject(callback: AsyncCallback<T>): void;
        /**
         * Obtains the first file asset in the result set. This API uses a promise to return the result.
         *
         * @returns { Promise<T> } Promise used to return the first object in the result set.
         * @throws { BusinessError } 13900020 - Invalid argument
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @atomicservice [since 20]
         * @since 10
         */
        getFirstObject(): Promise<T>;
        /**
         * Obtains the next file asset in the result set. This API uses an asynchronous callback to return the result.
         *
         * Before using this API, you must use [isAfterLast()]{@link photoAccessHelper.FetchResult.isAfterLast} to check
         * whether the current position is the end of the result set.
         *
         * @param { AsyncCallback<T> } callback - Callback function. If the next file asset in the result set is
         *     successfully obtained, **err** is **undefined**, and **data** is the specific search result. Otherwise,
         *     **err** is an error object.
         * @throws { BusinessError } 13900020 - Invalid argument
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @atomicservice [since 20]
         * @since 10
         */
        getNextObject(callback: AsyncCallback<T>): void;
        /**
         * Obtains the next file asset in the result set. This API uses a promise to return the result.
         *
         * Before using this API, you must use [isAfterLast()]{@link photoAccessHelper.FetchResult.isAfterLast} to check
         * whether the current position is the end of the result set.
         *
         * @returns { Promise<T> } Promise used to return the next object in the result set.
         * @throws { BusinessError } 13900020 - Invalid argument
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @atomicservice [since 20]
         * @since 10
         */
        getNextObject(): Promise<T>;
        /**
         * Obtains the last file asset in the result set. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<T> } callback - Callback function. If the last file asset in the result set is
         *     successfully obtained, **err** is **undefined**, and **data** is the specific search result. Otherwise,
         *     **err** is an error object.
         * @throws { BusinessError } 13900020 - Invalid argument
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @atomicservice [since 20]
         * @since 10
         */
        getLastObject(callback: AsyncCallback<T>): void;
        /**
         * Obtains the last file asset in the result set. This API uses a promise to return the result.
         *
         * @returns { Promise<T> } Promise used to return the last object in the result set.
         * @throws { BusinessError } 13900020 - Invalid argument
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @atomicservice [since 20]
         * @since 10
         */
        getLastObject(): Promise<T>;
        /**
         * Obtains a file asset with the specified index in the result set. This API uses an asynchronous callback to return
         * the result.
         *
         * @param { number } index - Index of the file asset to obtain. The value starts from **0**.
         * @param { AsyncCallback<T> } callback - Callback function. If the file asset with the specified index in the
         *     result set is successfully obtained, **err** is **undefined**, and **data** is the specific search result.
         *     Otherwise, **err** is an error object.
         * @throws { BusinessError } 13900020 - Invalid argument
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @atomicservice [since 20]
         * @since 10
         */
        getObjectByPosition(index: number, callback: AsyncCallback<T>): void;
        /**
         * Obtains a file asset with the specified index in the result set. This API uses a promise to return the result.
         *
         * @param { number } index - Index of the file asset to obtain. The value starts from **0**.
         * @returns { Promise<T> } Promise used to return the file asset obtained.
         * @throws { BusinessError } 13900020 - Invalid argument
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @atomicservice [since 20]
         * @since 10
         */
        getObjectByPosition(index: number): Promise<T>;
        /**
         * Obtains the file asset array of a specified length (second parameter) from the specified index (first parameter)
         * in the result set. This API uses a promise to return the result.
         *
         * @param { number } index - Index of the file asset to be obtained. The value must be greater than or equal to 0 and
         *     less than the number of objects in the result set.
         * @param { number } offset - Number of file assets to be obtained. The value must be greater than 0.
         *     <br>The sum of **index** and **offset** must be less than the total number of objects in the result set.
         *     Otherwise, error code **23800151** is thrown.
         * @returns { Promise<T[]> } Promise array.
         * @throws { BusinessError } 23800151 - The scenario parameter verification fails.
         *     <br>Possible causes: index or offset validity check failed.
         * @throws { BusinessError } 23800301 - Internal system error. You are advised to retry and check the logs.
         *     <br>Possible causes:
         *     <br>1. The database is corrupted.
         *     <br>2. The file system is abnormal.
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 23
         */
        getRangeObjects(index: number, offset: number): Promise<T[]>;
        /**
         * Obtains all the file assets in the result set. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<Array<T>> } callback - Callback function. If all file assets in the result set are
         *     successfully obtained, **err** is **undefined**, and **data** is the specific search result. Otherwise,
         *     **err** is an error object.
         * @throws { BusinessError } 13900020 - Invalid argument
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @atomicservice [since 20]
         * @since 10
         */
        getAllObjects(callback: AsyncCallback<Array<T>>): void;
        /**
         * Obtains all the file assets in the result set. This API uses a promise to return the result.
         *
         * @returns { Promise<Array<T>> } Promise used to return an array of all file assets.
         * @throws { BusinessError } 13900020 - Invalid argument
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @atomicservice [since 20]
         * @since 10
         */
        getAllObjects(): Promise<Array<T>>;
        /**
         * Closes this FetchResult instance to invalidate it. After this instance is released, the APIs in this instance
         * cannot be invoked.
         *
         * @throws { BusinessError } 13900020 - Invalid argument
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @atomicservice [since 20]
         * @since 10
         */
        close(): void;
        /**
         * Checks whether the specified file asset is contained in the result set. This API uses a promise to return the
         * result.
         *
         * @param { T } object - Specified file asset.
         * @returns { Promise<boolean> } Promise used to return the result. **true** indicates that the specified file asset
         *     is contained in the result set, and **false** indicates the opposite.
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        contains(object: T): Promise<boolean>;
        /**
         * Obtains the file asset array corresponding to the specified index set in the result set. This API uses a promise
         * to return the result.
         *
         * @param { number[] } indexSet - Specified index set.
         * @returns { Promise<T[]> } Promise object, which returns the file asset array corresponding to the specified index
         *     set.
         * @throws { BusinessError } 23800151 - The scenario parameter verification fails. Possible causes:
         *     <br>1.The indexSet is null, undefined or empty.
         *     <br>2.The indexSet length is bigger than 500.
         *     <br>3.The max value of indexSet is equal or bigger than the fetch result length.
         *     <br>4.The min value of indexSet is less than 0.
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        getObjectsByIndexSet(indexSet: number[]): Promise<T[]>;
        /**
         * Obtains the index of a specified file asset in the result set. This API uses a promise to return the result.
         *
         * @param { T } object - Specified file asset.
         * @returns { Promise<number> } Promise used to return the result. If the object exists in the result set, the
         *     corresponding index is returned. Otherwise, **-1** is returned.
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        getIndex(object: T): Promise<number>;
    }
    /**
     * Enumerates the album types,
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @crossplatform [since 12]
     * @since 10
     */
    enum AlbumType {
        /**
         * User album.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @since 10
         */
        USER = 0,
        /**
         * System album.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @since 10
         */
        SYSTEM = 1024,
        /**
         * Album created by an application.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 23
         */
        SOURCE = 2048
    }
    /**
     * Enumerate the album subtypes.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @crossplatform [since 12]
     * @since 10
     */
    enum AlbumSubtype {
        /**
         * User album.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @since 10
         */
        USER_GENERIC = 1,
        /**
         * Favorites.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @since 10
         */
        FAVORITE = 1025,
        /**
         * Video album.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @since 10
         */
        VIDEO,
        /**
         * Photo album.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 12
         */
        IMAGE = 1031,
        /**
         * Source album.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 23
         */
        SOURCE_GENERIC = 2049,
        /**
         * Source album from FileManager
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        SOURCE_GENERIC_FROM_FILE_MANAGER = 2050,
        /**
         * Any album.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @since 10
         */
        ANY = 2147483647
    }
    /**
     * Defines the abstract interface of albums.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @crossplatform [since 12]
     * @since 10
     */
    interface AbsAlbum {
        /**
         * Type of the album.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @since 10
         */
        readonly albumType: AlbumType;
        /**
         * Subtype of the album.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @since 10
         */
        readonly albumSubtype: AlbumSubtype;
        /**
         * Name of the album. System albums are not writable, whereas user albums can be written to.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @since 10
         */
        albumName: string;
        /**
         * URI of the album.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @since 10
         */
        readonly albumUri: string;
        /**
         * Number of files in the album.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @since 10
         */
        readonly count: number;
        /**
         * URI of the cover file of the album.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 10
         */
        readonly coverUri: string;
        /**
         * Virtual path of the album.
         *
         * Albums and their virtual path values:
         *
         * - Camera application album: '/DCIM/Camera'
         * - Screenshot application album: '/Pictures/Screenshots'
         * - Screen recording application album: '/Pictures/Screenrecords'
         * - User-created album: '/Pictures/Users/{Custom album name}'
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 23
         */
        readonly lpath?: string;
        /**
         * Time when the album is changed.
         * Unit: second, The value must be greater than or equal to 0.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 23
         */
        readonly changeTime?: number;
        /**
         * Obtains image and video assets. This API uses an asynchronous callback to return the result.
         *
         * @permission ohos.permission.READ_IMAGEVIDEO
         * @param { FetchOptions } options - Retrieval options.
         * @param { AsyncCallback<FetchResult<PhotoAsset>> } callback - Callback function. If files from the album are
         *     obtained successfully, **err** is **undefined**, and **data** is the result set of the obtained image and
         *     video data ([FetchResult]{@link @ohos.file.photoAccessHelper:photoAccessHelper}). Otherwise, **err** is an
         *     error object.
         * @throws { BusinessError } 201 - Permission denied [since 12]
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 13900012 - Permission denied [since 10 - 11]
         * @throws { BusinessError } 13900020 - Invalid argument
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @since 10
         */
        getAssets(options: FetchOptions, callback: AsyncCallback<FetchResult<PhotoAsset>>): void;
        /**
         * Obtains image and video assets. This API uses a promise to return the result.
         *
         * @permission ohos.permission.READ_IMAGEVIDEO
         * @param { FetchOptions } options - Retrieval options.
         * @returns { Promise<FetchResult<PhotoAsset>> } Promise used to return the image and video assets obtained.
         * @throws { BusinessError } 201 - Permission denied [since 20]
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 13900012 - Permission denied [since 10 - 19]
         * @throws { BusinessError } 13900020 - Invalid argument
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @atomicservice [since 20]
         * @since 10
         */
        getAssets(options: FetchOptions): Promise<FetchResult<PhotoAsset>>;
    }
    /**
     * Enumerates the types of changes that trigger the media asset or album change events.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @since 20
     */
    enum NotifyChangeType {
        /**
         * A media asset or an album is created.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 20
         */
        NOTIFY_CHANGE_ADD = 0,
        /**
         * A media asset or an album is modified.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 20
         */
        NOTIFY_CHANGE_UPDATE = 1,
        /**
         * A media asset or an album is deleted.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 20
         */
        NOTIFY_CHANGE_REMOVE = 2
    }
    /**
     * Provides APIs to manage albums.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @crossplatform [since 12]
     * @since 10
     */
    interface Album extends AbsAlbum {
        /**
         * Number of images in the album.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @since 11
         */
        readonly imageCount?: number;
        /**
         * Number of videos in the album.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @since 11
         */
        readonly videoCount?: number;
        /**
         * Commits the modification on the album attributes to the database. This API uses an asynchronous callback to
         * return the result.
         *
         * @permission ohos.permission.WRITE_IMAGEVIDEO
         * @param { AsyncCallback<void> } callback - Callback function. If the album properties are modified successfully,
         *     **err** is **undefined**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 201 - Permission denied
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types.
         * @throws { BusinessError } 13900020 - Invalid argument
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 10
         */
        commitModify(callback: AsyncCallback<void>): void;
        /**
         * Commits the modification on the album attributes to the database. This API uses a promise to return the result.
         *
         * @permission ohos.permission.WRITE_IMAGEVIDEO
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 201 - Permission denied
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types.
         * @throws { BusinessError } 13900020 - Invalid argument
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 10
         */
        commitModify(): Promise<void>;
        /**
         * Adds image and video assets to a user album. Before the operation, ensure that the image and video assets to add
         * and the album exist. This API uses an asynchronous callback to return the result.
         *
         * @permission ohos.permission.WRITE_IMAGEVIDEO
         * @param { Array<PhotoAsset> } assets - Array of the image and video assets to add.
         * @param { AsyncCallback<void> } callback - Callback function. If an image or video is added successfully, **err**
         *     is **undefined**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 201 - Permission denied
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 13900020 - Invalid argument
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 10
         * @deprecated since 11
         * @useinstead photoAccessHelper.MediaAlbumChangeRequest#addAssets
         */
        addAssets(assets: Array<PhotoAsset>, callback: AsyncCallback<void>): void;
        /**
         * Adds image and video assets to a user album. Before the operation, ensure that the image and video assets to add
         * and the album exist. This API uses a promise to return the result.
         *
         * @permission ohos.permission.WRITE_IMAGEVIDEO
         * @param { Array<PhotoAsset> } assets - Array of the image and video assets to add.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 201 - Permission denied
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 13900020 - Invalid argument
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 10
         * @deprecated since 11
         * @useinstead photoAccessHelper.MediaAlbumChangeRequest#addAssets
         */
        addAssets(assets: Array<PhotoAsset>): Promise<void>;
        /**
         * Removes image and video assets from a user album. The album and file resources must exist. This API uses an
         * asynchronous callback to return the result.
         *
         * @permission ohos.permission.WRITE_IMAGEVIDEO
         * @param { Array<PhotoAsset> } assets - Array of the image and video assets to remove.
         * @param { AsyncCallback<void> } callback - Callback function. If an image or video is removed successfully,
         *     **err** is **undefined**. Otherwise, **err** is an error object.
         * @throws { BusinessError } 201 - Permission denied
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 13900020 - Invalid argument
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 10
         * @deprecated since 11
         * @useinstead photoAccessHelper.MediaAlbumChangeRequest#removeAssets
         */
        removeAssets(assets: Array<PhotoAsset>, callback: AsyncCallback<void>): void;
        /**
         * Removes image and video assets from a user album. The album and file resources must exist. This API uses a
         * promise to return the result.
         *
         * @permission ohos.permission.WRITE_IMAGEVIDEO
         * @param { Array<PhotoAsset> } assets - Array of the image and video assets to remove.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 201 - Permission denied
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 13900020 - Invalid argument
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 10
         * @deprecated since 11
         * @useinstead photoAccessHelper.MediaAlbumChangeRequest#removeAssets
         */
        removeAssets(assets: Array<PhotoAsset>): Promise<void>;
    }
    /**
     * Helper functions to access photos and albums.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @crossplatform [since 12]
     * @atomicservice [since 11]
     * @since 10
     */
    interface PhotoAccessHelper {
        /**
         * Obtains image and video assets. This API uses an asynchronous callback to return the result.
         *
         * @permission ohos.permission.READ_IMAGEVIDEO
         * @param { FetchOptions } options - Retrieval options.
         * @param { AsyncCallback<FetchResult<PhotoAsset>> } callback - Callback function. If files from the album are
         *     obtained successfully, **err** is **undefined**, and **data** is the result set of the obtained image and
         *     video data ([FetchResult]{@link @ohos.file.photoAccessHelper:photoAccessHelper}). Otherwise, **err** is an
         *     error object.
         * @throws { BusinessError } 201 - Permission denied [since 12]
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 13900012 - Permission denied [since 10 - 11]
         * @throws { BusinessError } 13900020 - Invalid argument
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @since 10
         */
        getAssets(options: FetchOptions, callback: AsyncCallback<FetchResult<PhotoAsset>>): void;
        /**
         * Obtains image and video assets. This API uses a promise to return the result.
         *
         * @permission ohos.permission.READ_IMAGEVIDEO
         * @param { FetchOptions } options - Retrieval options.
         * @returns { Promise<FetchResult<PhotoAsset>> } Promise used to return the image and video assets obtained.
         * @throws { BusinessError } 201 - Permission denied [since 20]
         * @throws { BusinessError } 13900012 - Permission denied [since 10 - 19]
         * @throws { BusinessError } 13900020 - Invalid argument
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @atomicservice [since 20]
         * @since 10
         */
        getAssets(options: FetchOptions): Promise<FetchResult<PhotoAsset>>;
        /**
         * Obtains burst assets. This API uses a promise to return the result.
         *
         * @permission ohos.permission.READ_IMAGEVIDEO
         * @param { string } burstKey - Universally Unique Identifier (UUID) of a group of burst photos, that is,
         *     **BURST_KEY** of [PhotoKeys]{@link @ohos.file.photoAccessHelper:photoAccessHelper.PhotoKeys}. The string
         *     contains 36 bytes.
         * @param { FetchOptions } options - Retrieval options.
         * @returns { Promise<FetchResult<PhotoAsset>> } Promise used to return the result.
         * @throws { BusinessError } 201 - Permission denied
         * @throws { BusinessError } 14000011 - Internal system error
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice [since 20]
         * @since 12
         */
        getBurstAssets(burstKey: string, options: FetchOptions): Promise<FetchResult<PhotoAsset>>;
        /**
         * Creates an image or video asset with the specified file type, file name extension, and options. This API uses an
         * asynchronous callback to return the result.
         *
         * If you do not have the **ohos.permission.WRITE_IMAGEVIDEO** permission, you can create a media asset by using a
         * security component or an authorization pop-up. For details, see
         * [Saving Media Assets](docroot://media/medialibrary/photoAccessHelper-savebutton.md).
         *
         * @permission ohos.permission.WRITE_IMAGEVIDEO
         * @param { PhotoType } photoType - Type of the file to create, which can be **IMAGE** or **VIDEO**.
         * @param { string } extension - File name extension, for example, **'jpg'**.
         * @param { CreateOptions } options - Options used for creation. Currently, only **title** is supported, for example
         *     , **{title: 'testPhoto'}**.
         *     <br>**NOTE**
         *     <br>If a **subtype** option is passed, the configuration does not take effect. Only DEFAULT images can
         *     be saved.
         *     <br>The file name must not contain any invalid characters, which are:.. \ / : * ? " ' ` < > | { } [ ]
         * @param { AsyncCallback<string> } callback - Callback used to return the URI of the created image or video asset.
         * @throws { BusinessError } 201 - Permission denied [since 11]
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 13900012 - Permission denied [since 10 - 10]
         * @throws { BusinessError } 13900020 - Invalid argument
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 22]
         * @atomicservice [since 11]
         * @since 10
         */
        createAsset(photoType: PhotoType, extension: string, options: CreateOptions, callback: AsyncCallback<string>): void;
        /**
         * Creates an image or video asset with the specified file type and file name extension. This API uses an
         * asynchronous callback to return the result.
         *
         * If you do not have the **ohos.permission.WRITE_IMAGEVIDEO** permission, you can create a media asset by using a
         * security component or an authorization pop-up. For details, see
         * [Saving Media Assets](docroot://media/medialibrary/photoAccessHelper-savebutton.md).
         *
         * @permission ohos.permission.WRITE_IMAGEVIDEO
         * @param { PhotoType } photoType - Type of the file to create, which can be **IMAGE** or **VIDEO**.
         * @param { string } extension - File name extension, for example, **'jpg'**.
         * @param { AsyncCallback<string> } callback - Callback used to return the URI of the created image or video asset.
         * @throws { BusinessError } 201 - Permission denied [since 11]
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 13900012 - Permission denied [since 10 - 10]
         * @throws { BusinessError } 13900020 - Invalid argument
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 22]
         * @atomicservice [since 11]
         * @since 10
         */
        createAsset(photoType: PhotoType, extension: string, callback: AsyncCallback<string>): void;
        /**
         * Creates an image or video asset with the specified file type, file name extension, and options. This API uses a
         * promise to return the result.
         *
         * If you do not have the **ohos.permission.WRITE_IMAGEVIDEO** permission, you can create a media asset by using a
         * security component or an authorization pop-up. For details, see
         * [Saving Media Assets](docroot://media/medialibrary/photoAccessHelper-savebutton.md).
         *
         * @permission ohos.permission.WRITE_IMAGEVIDEO
         * @param { PhotoType } photoType - Type of the file to create, which can be **IMAGE** or **VIDEO**.
         * @param { string } extension - File name extension, for example, **'jpg'**.
         * @param { CreateOptions } [options] - Options used for creation. Currently, only **title** is supported, for
         *     example, **{title: 'testPhoto'}**.
         *     <br>**NOTE**
         *     <br>If a **subtype** option is passed, the configuration does
         *     not take effect. Only DEFAULT images can be saved.
         *     <br>The file name must not contain any invalid characters, which are:.. \ / : * ? " ' ` < > | { } [ ]
         * @returns { Promise<string> } Promise used to return the URI of the created image or video asset.
         * @throws { BusinessError } 201 - Permission denied [since 11]
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 13900012 - Permission denied [since 10 - 10]
         * @throws { BusinessError } 13900020 - Invalid argument
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 22]
         * @atomicservice [since 11]
         * @since 10
         */
        createAsset(photoType: PhotoType, extension: string, options?: CreateOptions): Promise<string>;
        /**
         * Creates an image or video resource with the specified file type, extension, and title. This API uses a promise to
         * return the result.
         *
         * If you do not have the **ohos.permission.WRITE_IMAGEVIDEO** permission, you can create a media asset by using a
         * security component or an authorization pop-up. For details, see
         * [Saving Media Assets](docroot://media/medialibrary/photoAccessHelper-savebutton.md).
         *
         * @permission ohos.permission.WRITE_IMAGEVIDEO
         * @param { PhotoType } photoType - Type of the file to be created. For example, **IMAGE** or **VIDEO**.
         * @param { string } extension - File name extension. For example, **'jpg'**.
         * @param { string } [title] - Title of the image or video resource.
         * @returns { Promise<string> } Promise used to return the URL of the created image or video.
         * @throws { BusinessError } 201 - Permission denied
         * @throws { BusinessError } 23800151 - The scenario parameter verification fails. Possible causes:
         *     <br>1. The extension format is unsupported
         *     <br>2. Title contains unsupported  character, such as . .. \ / : * ? " ' ` < > | { } [ ]
         *     <br>3. The title is an empty string
         *     <br>4. The total length of title and extension is more than 255
         * @throws { BusinessError } 23800301 - Internal system error. It is recommended to retry and check the logs.
         *     Possible causes:
         *     <br>1. Database corrupted;
         *     <br>2. The file system is abnormal;
         *     <br>3. The IPC request timed out.
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        createPhotoAsset(photoType: PhotoType, extension: string, title?: string): Promise<string>;
        /**
         * Obtains albums based on the specified options and album type. This API uses an asynchronous callback to return
         * the result.
         *
         * Before the operation, ensure that the albums to obtain exist.
         *
         * @permission ohos.permission.READ_IMAGEVIDEO
         * @param { AlbumType } type - Type of the album.
         * @param { AlbumSubtype } subtype - Subtype of the album.
         * @param { FetchOptions } options - Retrieval options.
         * @param { AsyncCallback<FetchResult<Album>> } callback - Callback used to return the result.
         * @throws { BusinessError } 201 - Permission denied [since 12]
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 13900012 - Permission denied [since 10 - 11]
         * @throws { BusinessError } 13900020 - Invalid argument
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @since 10
         */
        getAlbums(type: AlbumType, subtype: AlbumSubtype, options: FetchOptions, callback: AsyncCallback<FetchResult<Album>>): void;
        /**
         * Obtains albums by type. This API uses an asynchronous callback to return the result.
         *
         * Before the operation, ensure that the albums to obtain exist.
         *
         * @permission ohos.permission.READ_IMAGEVIDEO
         * @param { AlbumType } type - Type of the album.
         * @param { AlbumSubtype } subtype - Subtype of the album.
         * @param { AsyncCallback<FetchResult<Album>> } callback - Callback used to return the result.
         * @throws { BusinessError } 201 - Permission denied [since 12]
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 13900012 - Permission denied [since 10 - 11]
         * @throws { BusinessError } 13900020 - Invalid argument
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @since 10
         */
        getAlbums(type: AlbumType, subtype: AlbumSubtype, callback: AsyncCallback<FetchResult<Album>>): void;
        /**
         * Obtains albums based on the specified options and album type. This API uses a promise to return the result.
         *
         * Before the operation, ensure that the albums to obtain exist.
         *
         * @permission ohos.permission.READ_IMAGEVIDEO
         * @param { AlbumType } type - Type of the album.
         * @param { AlbumSubtype } subtype - Subtype of the album.
         * @param { FetchOptions } [options] - Retrieval options. If this parameter is not specified, the albums are
         *     obtained based on the album type by default.
         * @returns { Promise<FetchResult<Album>> } Promise used to return the result.
         * @throws { BusinessError } 201 - Permission denied [since 12]
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 13900012 - Permission denied [since 10 - 11]
         * @throws { BusinessError } 13900020 - Invalid argument
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @since 10
         */
        getAlbums(type: AlbumType, subtype: AlbumSubtype, options?: FetchOptions): Promise<FetchResult<Album>>;
        /**
         * Registers listening for the specified URI. This API uses a callback to return the result.
         *
         * @param { string } uri - URI of the photo asset, URI of the album, or
         *     [DefaultChangeUri]{@link @ohos.file.photoAccessHelper:photoAccessHelper.DefaultChangeUri}.
         * @param { boolean } forChildUris - Whether to perform fuzzy listening.
         *     <br> If **uri** is the URI of an album, the value **true** means to listen for the changes of the files in
         *     the album; the value **false** means to listen for the changes of the album only.
         *     <br>If **uri** is the URI of a photoAsset, there is no difference between
         *     **true** and false for **forChildUris**.
         *     <br>If **uri** is **DefaultChangeUri**, **forChildUris** must be set
         *     to **true**. If **forChildUris** is false, the URI cannot be found and no message can be received.
         * @param { Callback<ChangeData> } callback - Callback used to return
         *     [ChangeData]{@link @ohos.file.photoAccessHelper:photoAccessHelper.ChangeData}. **NOTE**: Multiple callback
         *     listeners can be registered for a URI. You can use
         *     [unRegisterChange]{@link photoAccessHelper.PhotoAccessHelper.unRegisterChange} to unregister all listeners
         *     for the URI or a specified callback listener.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 13900012 - Permission denied
         * @throws { BusinessError } 13900020 - Invalid argument
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 10
         */
        registerChange(uri: string, forChildUris: boolean, callback: Callback<ChangeData>): void;
        /**
         * Unregisters listening for the specified URI. Multiple callbacks can be registered for a URI for listening. You
         * can use this API to unregister the listening of the specified callbacks or all callbacks.
         *
         * @param { string } uri - URI of the photo asset, URI of the album, or
         *     [DefaultChangeUri]{@link @ohos.file.photoAccessHelper:photoAccessHelper.DefaultChangeUri}.
         * @param { Callback<ChangeData> } [callback] - Callback to unregister. If this parameter is not specified, all the
         *     callbacks for listening for the URI will be canceled. **NOTE**: The specified callback unregistered will not
         *     be invoked when the data changes.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 13900012 - Permission denied
         * @throws { BusinessError } 13900020 - Invalid argument
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 10
         */
        unRegisterChange(uri: string, callback?: Callback<ChangeData>): void;
        /**
         * Creates a dialog box for deleting media files. This API uses an asynchronous callback to return the result. The
         * deleted media files are moved to the trash.
         *
         * @permission ohos.permission.WRITE_IMAGEVIDEO
         * @param { Array<string> } uriList - URIs of the media files to delete. A maximum of 300 media files can be
         *     deleted.
         * @param { AsyncCallback<void> } callback - Callback that returns no value.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 13900012 - Permission denied
         * @throws { BusinessError } 13900020 - Invalid argument
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 10
         * @deprecated since 11
         * @useinstead photoAccessHelper.MediaAssetChangeRequest.deleteAssets
         */
        createDeleteRequest(uriList: Array<string>, callback: AsyncCallback<void>): void;
        /**
         * Creates a dialog box for deleting media files. This API uses a promise to return the result. The deleted media
         * files are moved to the trash.
         *
         * @permission ohos.permission.WRITE_IMAGEVIDEO
         * @param { Array<string> } uriList - URIs of the media files to delete. A maximum of 300 media files can be
         *     deleted.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 13900012 - Permission denied
         * @throws { BusinessError } 13900020 - Invalid argument
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 10
         * @deprecated since 11
         * @useinstead photoAccessHelper.MediaAssetChangeRequest.deleteAssets
         */
        createDeleteRequest(uriList: Array<string>): Promise<void>;
        /**
         * Displays a dialog box for the user to confirm whether to save the images or videos. If the user agrees to save
         * the images or videos, this API returns a list of URIs that have been created and granted save permissions (this
         * list is permanent), and the application can use these URIs to write the images or videos. If the user declines to
         * save the images or videos, this API returns an empty list.
         *
         * The dialog box must display the application name, but this cannot be directly obtained. Therefore, before calling
         * this API, ensure that the **label** and **icon** items are configured in the **abilities** tag in the
         * [module.json5 configuration file](docroot://quick-start/module-configuration-file.md). Note that the icon is not
         * affected by the **icon** item in the **abilities** tag and cannot be modified.
         *
         * > **NOTE**
         * >
         * > If the passed URI is a sandbox path, images or videos can be saved but cannot be previewed.
         *
         * @param { Array<string> } srcFileUris - [URIs](docroot://file-management/user-file-uri-intro.md#media-file-uri) of
         *     the images or videos to be saved to the media library.
         *     <br>**NOTE**
         *     <br>- A maximum of 100 images can be saved at a time.
         *     <br>- Only image and video URIs are supported.
         *     <br>- URIs cannot be manually constructed. You must call APIs to obtain them. For details, see
         *     [Obtaining a Media File URI](docroot://file-management/user-file-uri-intro.md#obtaining-a-media-file-uri).
         * @param { Array<PhotoCreationConfig> } photoCreationConfigs - Configuration for saving the images or videos,
         *     including the file names. The value must be consistent with that of **srcFileUris**.
         *     <br>**NOTE**
         *     <br>If a **subtype** option is passed, the configuration does not take effect. Only DEFAULT images can
         *     be saved.
         * @returns { Promise<Array<string>> } Promise used to return a URI list. The URIs are granted with the permission
         *     for the application to write data. If the URIs fail to be generated, a batch creation error code will be
         *     returned.
         *     <br>The return values are as follows:
         *     <br>- **-3006**: Invalid characters, which are not allowed.
         *     <br>-**-2004**: The image type does not match the file name extension.
         *     <br>-**-203**: Invalid file operation.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 14000011 - Internal system error
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 12
         */
        showAssetsCreationDialog(srcFileUris: Array<string>, photoCreationConfigs: Array<PhotoCreationConfig>): Promise<Array<string>>;
        /**
         * Displays a dialog box for the user to confirm whether to save the images or videos. This API uses a promise to
         * return the result.
         *
         * > **NOTE**
         * >
         * > - If the user agrees, the list of created URIs with the save permission granted is returned. The list is
         * > permanently valid and supports image or video writing. If the user rejects, an empty list is returned.
         * >
         * > - The application name and icon need to be displayed in the dialog box. The name and icon need to be configured
         * > in the **label** and **icon** items in the **abilities** tag of the
         * > [module.json5 configuration file](docroot://quick-start/module-configuration-file.md).
         * >
         * > - When the passed URI is a sandbox path, images or videos can be saved properly, but the preview is not
         * > displayed.
         *
         * @param { Array<string> } srcFileUris - [URIs](docroot://file-management/user-file-uri-intro.md#media-file-uri) of
         *     the images or videos to be saved to the media library.
         *     <br>**NOTE**
         *     <br>- A maximum of 100 images can be saved at a time.
         *     <br>- Only image and video URIs are supported.
         *     <br>- URIs cannot be manually constructed. You must call APIs to obtain them. For details, see
         *     [Obtaining a Media File URI](docroot://file-management/user-file-uri-intro.md#obtaining-a-media-file-uri).
         * @param { Array<CreationSetting> } creationSettings - Configuration for saving images or videos to the media
         *     library, including the file name. The URI in this parameter must correspond to that in the **srcFileUris**
         *     parameter.
         * @returns { Promise<Array<string>> } Promise used to return a URI list. The application can use the returned URI
         *     to write data.
         * @throws { BusinessError } 23800301 - Internal system error.
         *     It is recommended to retry and check the logs. Possible causes:
         *     <br>1. Database corrupted;
         *     <br>2. The file system is abnormal;
         *     <br>3. The IPC request timed out.
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        showAssetsCreationDialogEx(srcFileUris: Array<string>, creationSettings: Array<CreationSetting>): Promise<Array<string>>;
        /**
         * Displays a dialog box for the user to confirm whether to save an image or video. This API uses a promise to
         * return the result.
         *
         * > **NOTE**
         * >
         * > - If the user agrees to save the images or videos, this API returns a URI that has been created and granted
         * > with the save permission (this URI is permanent), and the application can use this URI to write the image or
         * > video. If the user declines to save the image or video, this API returns an empty string.
         * >
         * > - The dialog box must display the application name, but this cannot be directly obtained. Therefore, before
         * > calling this API, ensure that the **label** and **icon** items are configured in the **abilities** tag in the
         * > [module.json5 configuration file](docroot://quick-start/module-configuration-file.md). Note that the icon is
         * > not affected by the **icon** item in the **abilities** tag and cannot be modified.
         * >
         * > - If the passed URI is a sandbox path, images or videos can be saved but cannot be previewed.
         *
         * @param { string } srcFileUri - [URIs](docroot://file-management/user-file-uri-intro.md#media-file-uri) of the
         *     images or videos to be saved to the media library.
         *     <br>**NOTE**
         *     <br>- Only one image can be saved at a time.
         *     <br>- Only image and video URIs are supported.
         *     <br>- URIs cannot be manually constructed. You must call APIs to obtain them. For details, see
         *     [Obtaining a Media File URI](docroot://file-management/user-file-uri-intro.md#obtaining-a-media-file-uri).
         * @param { CreationSetting } creationSetting - Configuration for saving the image or video, including the file
         *     name. The value must be consistent with that of **srcFileUri **.
         * @param { boolean } isImageFullyDisplayed - Whether the image is displayed completely. The value **true**
         *     indicates that the image is displayed completely, and **false** indicates the opposite.
         * @returns { Promise<string> } Promise used to return the URI of the media library file to the application. The
         *     URIs are granted with the permission for the application to write data. If the URIs fail to be generated, a
         *     batch creation error code will be returned.
         *     <br>The return values are as follows:
         *     <br>- **-3006**: Invalid characters, which are not allowed.
         *     <br>-**-2004**: The image type does not match the file name extension.
         *     <br>-**-203**: Invalid file operation.
         * @throws { BusinessError } 23800301 - Internal system error.
         *     It is recommended to retry and check the logs. Possible causes:
         *     <br>1. Database corrupted;
         *     <br>2. The file system is abnormal;
         *     <br>3. The IPC request timed out.
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        showSingleAssetCreationDialogEx(srcFileUri: string, creationSetting: CreationSetting, isImageFullyDisplayed: boolean): Promise<string>;
        /**
         * Creates an asset with a temporary permission of the given period. When this API is called by an application for
         * the first time, a dialog box will be displayed for the user to confirm whether to save the asset. If the user
         * agrees to save the asset, the asset instance will be created and the file URI granted with the save permission
         * will be returned. The application can write the asset based on the URI.
         *
         * Within 5 minutes after the user agrees to save the asset, if the same application calls this API again, the
         * authorized URI can be automatically returned without the need to display the confirmation dialog box. Exiting the
         * application will terminate the authorization, and the user need to re-trigger the dialog box for authorization
         * confirmation when the application is re-launched.
         *
         * @permission ohos.permission.SHORT_TERM_WRITE_IMAGEVIDEO
         * @param { PhotoCreationConfig } photoCreationConfig - Configuration for saving a media asset (image or video) to
         *     the media library, including the file name.
         *     <br>**NOTE**
         *     <br>If a **subtype** option is passed, the configuration does not take effect. Only DEFAULT images can
         *     be saved.
         * @returns { Promise<string> } Promise used to return the URI of the asset saved. The URIs are granted with the
         *     permission for the application to write data. If the URIs fail to be generated, a batch creation error code
         *     will be returned.
         *     <br>The error code **-3006** means that there are invalid characters; **-2004** means that the image type
         *     does not match the file name extension; **-203** means that the file operation is abnormal.
         * @throws { BusinessError } 201 - Permission denied
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 14000011 - Internal system error
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 12
         */
        createAssetWithShortTermPermission(photoCreationConfig: PhotoCreationConfig): Promise<string>;
        /**
         * Displays the dialog box for the first time for the user to confirm whether to save the asset. This API uses a
         * promise to return the result.
         *
         * > **NOTE**
         * >
         * > - After the user agrees to save the asset, the API returns the URI of the created asset that has the save
         * > permission. The application can use the URI to write the image or video.
         * >
         * > - Within 5 minutes after the user agrees to save the asset, if the same application calls this API again, the
         * > system directly returns the authorized URI for the application to save the image or video without displaying a
         * > confirmation dialog box. Exiting the application will terminate the authorization, and the user need to re-
         * > trigger the dialog box for authorization confirmation when the application is re-launched.
         *
         * @permission ohos.permission.SHORT_TERM_WRITE_IMAGEVIDEO
         * @param { CreationSetting } creationSetting - Configuration for saving a media asset (image or video) to the media
         *     library, including the file name.
         * @returns { Promise<string> } Promise used to return the URI of the media library file to the application. The
         *     application can use the returned URI to write data.
         * @throws { BusinessError } 201 - Permission denied
         * @throws { BusinessError } 14000011 - Internal system error
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @since 23
         */
        createAssetWithShortTermPermissionEx(creationSetting: CreationSetting): Promise<string>;
        /**
         * <!--RP1--><!--RP1End-->Grants the read permission for unauthorized URIs, returning a list of URIs that have been created and granted the permission.
         *
         * @param { Array<string> } srcFileUris - [URIs](docroot://file-management/user-file-uri-intro.md#media-file-uri) of
         *     the images or videos to be granted with the permission.
         *     <br>**NOTE**
         *     <br>Only image and video URIs are supported, and the maximum number of URIs is 100.
         * @returns { Promise<Array<string>> } Promise used to return the URIs granted with the permission.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 14000011 - Internal system error
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 14
         */
        requestPhotoUrisReadPermission(srcFileUris: Array<string>): Promise<Array<string>>;
        /**
         * Grants the read permission for unauthorized URIs. This API uses a promise to return the authorization result.
         *
         * It contains the list of URIs that have been created and granted the save permission and the list of invalid URIs.
         *
         * @param { Array<string> } srcFileUris - [URIs](docroot://file-management/user-file-uri-intro.md#media-file-uri) of
         *     the images or videos to be granted with the permission.
         *     <br>**NOTE**
         *     <br>Only image and video URIs are supported, and the maximum number of URIs is 100.
         * @returns { Promise<RequestReadPermissionResult> } Promise used to return the list of URIs granted with the
         *     permission and the list of invalid URIs.
         * @throws { BusinessError } 23800301 - Internal system error.
         *     It is recommended to retry and check the logs. Possible causes:
         *     <br>1. Database corrupted;
         *     <br>2. The file system is abnormal;
         *     <br>3. The IPC request timed out.
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        requestPhotoUrisReadPermissionEx(srcFileUris: Array<string>): Promise<RequestReadPermissionResult>;
        /**
         * Releases the **PhotoAccessHelper** instance. This API uses an asynchronous callback to return the result.
         *
         * Call this API when the APIs of the PhotoAccessHelper instance are no longer used.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types.
         * @throws { BusinessError } 13900020 - Invalid argument
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 10
         */
        release(callback: AsyncCallback<void>): void;
        /**
         * Releases the **PhotoAccessHelper** instance. This API uses a promise to return the result.
         *
         * Call this API when the APIs of the PhotoAccessHelper instance are no longer used.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types.
         * @throws { BusinessError } 13900020 - Invalid argument
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 10
         */
        release(): Promise<void>;
        /**
         * Applies media changes. This API uses a promise to return the result.
         *
         * @permission ohos.permission.WRITE_IMAGEVIDEO
         * @param { MediaChangeRequest } mediaChangeRequest - Request for asset changes or album changes.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 201 - Permission denied
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 11
         */
        applyChanges(mediaChangeRequest: MediaChangeRequest): Promise<void>;
        /**
         * Obtains the list of image or video file name extensions supported by the media library.
         *
         * @param { PhotoType } photoType - Type of the file.
         * @returns { Promise<Array<string>> } Promise used to return an array of the supported image or video file name
         *     extensions.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 14000011 - Internal system error. It is recommended to retry and check the logs.
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 18
         */
        getSupportedPhotoFormats(photoType: PhotoType): Promise<Array<string>>;
        /**
         * Subscribes to changes of medialibrary availability.
         *
         * @permission ohos.permission.READ_IMAGEVIDEO
         * @param { Callback<MediaLibraryAvailability> } callback - Callback used to return the MediaLibraryAvailability.
         * @throws { BusinessError } 201 - Permission denied
         * @throws { BusinessError } 23800151 - Scenario-specific parameters are incorrect. Possible causes are as follows:
         *     <br>1. The input parameter is null or undefined.
         * @throws { BusinessError } 23800301 - Internal system error. It is recommended to retry and check the logs.
         *     Possible causes:
         *     <br>1. Database corrupted;
         *     <br>2. The file system is abnormal;
         *     <br>3. The IPC request timed out.
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        onMediaLibraryAvailability(callback: Callback<MediaLibraryAvailability>): void;
        /**
         * Unsubscribes to changes of medialibrary availability.
         *
         * @permission ohos.permission.READ_IMAGEVIDEO
         * @param { Callback<MediaLibraryAvailability> } [callback] - Callback used to return the MediaLibraryAvailability.
         * @throws { BusinessError } 201 - Permission denied
         * @throws { BusinessError } 23800301 - Internal system error. It is recommended to retry and check the logs.
         *     Possible causes:
         *     <br>1. Database corrupted;
         *     <br>2. The file system is abnormal;
         *     <br>3. The IPC request timed out.
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        offMediaLibraryAvailability(callback?: Callback<MediaLibraryAvailability>): void;
        /**
         * Registers a listener for the **'photoChange'** event to monitor media asset changes. This API uses a callback to
         * return the result, and it accepts multiple callbacks.
         *
         * @permission ohos.permission.READ_IMAGEVIDEO
         * @param { 'photoChange' } type - Event type. The value is fixed at **'photoChange'**. After the registration is
         *     complete, any change to the media assets is returned through the callback.
         * @param { Callback<PhotoAssetChangeInfos> } callback - Callback used to return the media asset information after
         *     change, which is
         *     [PhotoAssetChangeInfos]{@link @ohos.file.photoAccessHelper:photoAccessHelper.PhotoAssetChangeInfos}.
         *     <br>**NOTE**
         *     <br>You can register multiple listeners using this API, and you can call
         *     [off('photoChange')]{@link photoAccessHelper.PhotoAccessHelper.off(type: 'photoChange', callback?: Callback<PhotoAssetChangeInfos>)}
         *     to unregister all listeners or a specific one.
         * @throws { BusinessError } 201 - Permission denied
         * @throws { BusinessError } 23800151 The scenario parameter verification fails. Possible causes:
         *     <br>1. The type is not fixed at 'photoChange';
         *     <br>2. The same callback is registered repeatedly.
         * @throws { BusinessError } 23800301 - Internal system error. You are advised to retry and check the logs.
         *     <br>Possible causes:
         *     <br>1. The database is corrupted.
         *     <br>2. The file system is abnormal.
         *     <br>3. The IPC request timed out.
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 20
         */
        on(type: 'photoChange', callback: Callback<PhotoAssetChangeInfos>): void;
        /**
         * Unregisters the listener for the **'photoChange'** event to stop monitoring media asset changes. If multiple
         * listeners are registered, you can unregister a specific listener by specifying **callback**. Alternatively, you
         * can unregister all of them without specifying **callback**.
         *
         * @permission ohos.permission.READ_IMAGEVIDEO
         * @param { 'photoChange' } type - Event type. The value is fixed at **'photoChange'**. After the unregistration is
         *     complete, any change to the media assets is no longer returned through the callback.
         * @param { Callback<PhotoAssetChangeInfos> } [callback] - Exact callback you previously registered with
         *     [on('photoChange')]{@link photoAccessHelper.PhotoAccessHelper.on(type: 'photoChange', callback: Callback<PhotoAssetChangeInfos>)}
         *     . If this parameter is left unspecified, all listeners for the **'photoChange'** event are unregistered.<br>
         *     **NOTE**<br>Once a specific callback is unregistered, it will not be invoked when a media asset changes.
         * @throws { BusinessError } 201 - Permission denied
         * @throws { BusinessError } 23800151 The scenario parameter verification fails. Possible causes:
         *     <br>1. The type is not fixed at 'photoChange';
         *     <br>2. The same callback is unregistered repeatedly.
         * @throws { BusinessError } 23800301 - Internal system error. You are advised to retry and check the logs.
         *     Possible causes:
         *     <br>1. The database is corrupted.
         *     <br>2. The file system is abnormal.
         *     <br>3. The IPC request timed out.
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 20
         */
        off(type: 'photoChange', callback?: Callback<PhotoAssetChangeInfos>): void;
        /**
         * Registers a listener for the **'photoAlbumChange'** event to monitor album changes. This API uses a callback to
         * return the result, and it accepts multiple callbacks.
         *
         * @permission ohos.permission.READ_IMAGEVIDEO
         * @param { 'photoAlbumChange' } type - Event type. The value is fixed at **'photoAlbumChange'**. After the
         *     registration is complete, any change to the albums is returned through the callback.
         * @param { Callback<AlbumChangeInfos> } callback - Callback used to return the album information after change,
         *     which is [AlbumChangeInfos]{@link @ohos.file.photoAccessHelper:photoAccessHelper.AlbumChangeInfos}.
         *     <br>**NOTE**
         *     <br>You can register multiple listeners using this API, and you can call
         *     [off('photoAlbumChange')]{@link photoAccessHelper.PhotoAccessHelper.off(type: 'photoAlbumChange', callback?: Callback<AlbumChangeInfos>)}
         *     to unregister all listeners or a specific one.
         * @throws { BusinessError } 201 - Permission denied
         * @throws { BusinessError } 23800151 The scenario parameter verification fails. Possible causes:
         *     <br>1. The type is not fixed at 'photoAlbumChange';
         *     <br>2. The same callback is registered repeatedly.
         * @throws { BusinessError } 23800301 - Internal system error. You are advised to retry and check the logs.
         *     Possible causes:
         *     <br>1. The database is corrupted.
         *     <br>2. The file system is abnormal.
         *     <br>3. The IPC request timed out.
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 20
         */
        on(type: 'photoAlbumChange', callback: Callback<AlbumChangeInfos>): void;
        /**
         * Unregisters a listener for the **'photoAlbumChange'** event to stop monitoring album changes. If multiple
         * listeners are registered, you can unregister a specific listener by specifying **callback**. Alternatively, you
         * can unregister all of them without specifying **callback**.
         *
         * @permission ohos.permission.READ_IMAGEVIDEO
         * @param { 'photoAlbumChange' } type - Event type. The value is fixed at **'photoAlbumChange'**. After the
         *     unregistration is complete, any change to the albums is no longer returned through the callback.
         * @param { Callback<AlbumChangeInfos> } [callback] - Exact callback you previously registered with
         *     [on('photoAlbumChange')]{@link photoAccessHelper.PhotoAccessHelper.on(type: 'photoAlbumChange', callback: Callback<AlbumChangeInfos>)}
         *     . If this parameter is left unspecified, all listeners for the **'photoAlbumChange'** event are unregistered.
         *     <br>**NOTE**
         *     <br>Once a specific callback is unregistered, it will not be invoked when an album changes.
         * @throws { BusinessError } 201 - Permission denied
         * @throws { BusinessError } 23800151 The scenario parameter verification fails. Possible causes:
         *     <br>1. The type is not fixed at 'photoAlbumChange';
         *     <br>2. The same callback is unregistered repeatedly.
         * @throws { BusinessError } 23800301 - Internal system error. You are advised to retry and check the
         *     logs.
         *     <br>Possible causes:
         *     <br>1. The database is corrupted.
         *     <br>2. The file system is abnormal.
         *     <br>3. The IPC request timed out.
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 20
         */
        off(type: 'photoAlbumChange', callback?: Callback<AlbumChangeInfos>): void;
        /**
         * Registers a listener for changes of a single common asset. This API uses an asynchronous callback to return the
         * result.
         *
         * @permission ohos.permission.READ_IMAGEVIDEO
         * @param { Album } album - Album to be listened for. After the registration is complete, any change to the albums
         *     is returned through the callback.
         * @param { Callback<AlbumChangeInfos> } callback - Callback used to return the album information after change,
         *     which is [PhotoAssetChangeInfos]{@link @ohos.file.photoAccessHelper:photoAccessHelper.PhotoAssetChangeInfos}.
         *     <br>**NOTE**
         *     <br>This API can be used to register multiple different callbacks.
         * @throws { BusinessError } 201 - Permission denied
         * @throws { BusinessError } 23800151 The scenario parameter verification fails. Possible causes:
         *     1. The same callback is registered repeatedly. 2. Album has been removed. 3. The uri of the a invalid.
         * @throws { BusinessError } 23800301 - Internal system error. You are advised to retry and check the logs.
         *     Possible causes:
         *     <br>1. The database is corrupted.
         *     <br>2. The file system is abnormal.
         *     <br>3. The IPC request timed out.
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 23
         */
        onSinglePhotoAlbumChange(album: Album, callback: Callback<AlbumChangeInfos>): void;
        /**
         * Unregisters a listener for a single album. Note the following:
         *
         * 1. If no parameter is specified, all listeners for the single albums are unregistered.
         * 2. If **album** is specified but **callback** is not specified, all callback listeners of the album are unregistered.
         * 3. If both **album** and **callback** are specified, only the specified callback listener is unregistered.
         *
         * @permission ohos.permission.READ_IMAGEVIDEO
         * @param { Album } [album] - Album for which the listener is unregistered. After the unregistration is complete,
         *     any change to the album is no longer returned through the callback.
         * @param { Callback<AlbumChangeInfos> } [callback] - Callback used for the unregistration. If this parameter is not
         *     specified, all callbacks of the **album** parameter are unregistered.
         * @throws { BusinessError } 201 - Permission denied
         * @throws { BusinessError } 23800151 The scenario parameter verification fails. Possible causes:
         *     <br>1. The same callback is unregistered repeatedly.
         *     <br>2. The uri of the album invalid.
         * @throws { BusinessError } 23800301 - Internal system error. You are advised to retry and check the logs.
         *     Possible causes:
         *     <br>1. The database is corrupted.
         *     <br>2. The file system is abnormal.
         *     <br>3. The IPC request timed out.
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 23
         */
        offSinglePhotoAlbumChange(album?: Album, callback?: Callback<AlbumChangeInfos>): void;
        /**
         * Registers a listener for changes of a single common asset. This API uses an asynchronous callback to return the
         * result.
         *
         * @permission ohos.permission.READ_IMAGEVIDEO
         * @param { PhotoAsset } asset - Asset to be listened for. After the registration is complete, any change to the
         *     media assets is returned through the callback.
         * @param { Callback<PhotoAssetChangeInfos> } callback - Callback used to return the media asset information after
         *     change, which is
         *     [PhotoAssetChangeInfos]{@link @ohos.file.photoAccessHelper:photoAccessHelper.PhotoAssetChangeInfos}.
         *     <br>**NOTE**
         *     <br>This API can be used to register multiple different callbacks.
         * @throws { BusinessError } 201 - Permission denied
         * @throws { BusinessError } 23800151 The scenario parameter verification fails. Possible causes:
         *     <br>1. The same callback is registered repeatedly.
         *     <br>2. Asset has been removed.
         *     <br>3. The uri of the asset invalid.
         * @throws { BusinessError } 23800301 - Internal system error. You are advised to retry and check the logs.
         *     Possible causes:
         *     <br>1. The database is corrupted.
         *     <br>2. The file system is abnormal.
         *     <br>3. The IPC request timed out.
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 23
         */
        onSinglePhotoChange(asset: PhotoAsset, callback: Callback<PhotoAssetChangeInfos>): void;
        /**
         * Unregisters the listener for a single asset. Note the following:
         *
         * 1. If no parameter is specified, all listeners for the single assets are unregistered.
         * 2. If **asset** is specified but **callback** is not specified,
         *    all callback listeners of the **asset** are unregistered.
         * 3. If both **asset** and **callback** are specified, only the specified callback listener is unregistered.
         *
         * @permission ohos.permission.READ_IMAGEVIDEO
         * @param { PhotoAsset } [asset] - Asset for which the listener is canceled. After the unregistration is complete,
         *     any change to the **asset** is no longer returned through the **callback**. If this parameter is not
         *     specified, all listeners for a single asset are unregistered.
         * @param { Callback<PhotoAssetChangeInfos> } [callback] - Callback used for the unregistration. If this parameter
         *     is not specified, all callbacks of the **asset** parameter are unregistered.
         * @throws { BusinessError } 201 - Permission denied
         * @throws { BusinessError } 23800151 The scenario parameter verification fails. Possible causes:
         *     <br>1. The same callback is unregistered repeatedly.
         *     <br>2. The uri of the asset invalid.
         * @throws { BusinessError } 23800301 - Internal system error. You are advised to retry and check the logs.
         *     Possible causes:
         *     <br>1. The database is corrupted.
         *     <br>2. The file system is abnormal.
         *     <br>3. The IPC request timed out.
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 23
         */
        offSinglePhotoChange(asset?: PhotoAsset, callback?: Callback<PhotoAssetChangeInfos>): void;
        /**
         * Obtains the name of the album that the **PhotoPickerComponent** shows by default. The name string is localized to
         * match the current system language. This API uses a promise to return the result.
         *
         * @returns { Promise<string> } Promise used to return the name of the default album.
         * @throws { BusinessError } 23800301 - Internal system error. It is recommended to retry and check the logs.
         *     <br>Possible causes:
         *     <br>1. The IPC request timed out.
         *     <br>2. system running error
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 20
         */
        getPhotoPickerComponentDefaultAlbumName(): Promise<string>;
        /**
         * Obtains the information about the recent image or video when the application uses the **RecentPhotoComponent** to
         * view recent images or videos. This API uses a promise to return the result.
         *
         * @param { RecentPhotoOptions } [options] - Options for retrieving the recent image or video. If this parameter is
         *     not specified, the latest image is retrieved according to the creation time.
         *     <br>If this parameter is
         *     specified, it must match the **options** configuration in the **RecentPhotoComponent**. Otherwise, there may
         *     be discrepancies where the API finds a recent image or video but the component does not.
         * @returns { Promise<RecentPhotoInfo> } Promise used to return the information about the recent image or video.
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 20
         */
        getRecentPhotoInfo(options?: RecentPhotoOptions): Promise<RecentPhotoInfo>;
        /**
         * Obtains the album ID in the media library based on the album's virtual path. This API uses a promise to return
         * the result.
         *
         * This API supports the following albums: camera application album, screenshot application album,
         * and screen recording application album.
         *
         * @param { string } lpath - Virtual path of the album. The value can contain a maximum of 255 characters.
         * @returns { Promise<number> } Promise used to return the album ID.
         * @throws { BusinessError } 23800151 - The lpath is invalid, such as null, undefined and empty.
         * @throws { BusinessError } 23800301 - Internal system error. You are advised to retry and check the logs.
         *     Possible causes:
         *     <br>1. The database is corrupted.
         *     <br>2. The file system is abnormal.
         *     <br>3. The IPC request timed out.
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @since 22
         */
        getAlbumIdByLpath(lpath: string): Promise<number>;
        /**
             * Sets the asset compatibility capability. The system performs compatibility processing on special assets (such as
             * high-resolution assets). If you want to obtain the original assets, you need to register the compatibility
             * capability with the system.
             *
             * @param { AssetCompatibleCapability } capability - Asset compatibility capability.
             * @returns { Promise<void> } Promise that returns no value.
             * @throws { BusinessError } 23800151 - The capability is invalid.
             * @throws { BusinessError } 23800301 - Internal system error. It is recommended to retry and check the logs.
             *     Possible causes:
             *     <br>1. Database corrupted;
             *     <br>2. The file system is abnormal;
             *     <br>3. The IPC request timed out.
             * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
             * @stagemodelonly
             * @since 24
             */
        setAssetCompatibleCapability(capability: AssetCompatibleCapability): Promise<void>;
        /**
         * Query whether the assets exist and whether the invoker has read permission on the assets without permission.
         *
         * @param { string[] } uris - Asset URI list.
         * @returns {Promise<Map<string, MediaAssetPermissionState>>} - Returns
         *     whether the assets exist and whether the invoker has read permission on the assets without permission.
         * @throws { BusinessError } 23800151 - Scenario-specific parameters are incorrect. Possible causes are as follows:
         *     <br>1. The length of the input parameter queue is greater than 500.
         *     <br>2. The input parameter is null or undefined.
         * @throws { BusinessError } 23800301 - Internal system error. It is recommended to retry and check the logs.
         *     Possible causes:
         *     <br>1. Database corrupted;
         *     <br>2. The file system is abnormal;
         *     <br>3. The IPC request timed out.
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        checkPhotoUrisReadPermission(uris: string[]): Promise<Map<string, MediaAssetPermissionState>>;
    }
    /**
     * RecentPhotoOptions Object
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @atomicservice
     * @since 20
     */
    export class RecentPhotoOptions {
        /**
         * Time range for displaying the recent images or videos, measured in seconds. After setting, the system shows
         * images or videos taken within the specified time from the current moment. The longest duration you can set is 1
         * day (86400s).
         *
         * If the value is less than or equal to 0, greater than 86400, or not set, the system uses the longest duration (1
         * day) by default. If there are no images or videos within the set time range, the component does not show
         * anything.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 20
         */
        period?: number;
        /**
         * Types of the file displayed. The default value is **PhotoViewMIMETypes.IMAGE_VIDEO_TYPE**.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 20
         */
        MIMEType?: photoAccessHelper.PhotoViewMIMETypes;
        /**
         * Source of the recent image or video, for example, image or video taken by the camera or screenshot. By default,
         * the source is not restricted.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 20
         */
        photoSource?: PhotoSource;
    }
    /**
     * Recent photo info
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @atomicservice
     * @since 20
     */
    export class RecentPhotoInfo {
        /**
         * Time when the recent image or video was shot (in milliseconds since January 1, 1970). The unit is ms.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 20
         */
        dateTaken?: number;
        /**
         * Hash value of the name of the recent image or video, which is used to help the application determine whether the
         * image or video to be displayed is the same as the one displayed before.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 20
         */
        identifier?: string;
    }
    /**
     * Enumeration of PhotoSource type
     *
     * @enum { number } PhotoSource
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @atomicservice
     * @since 20
     */
    export enum PhotoSource {
        /**
         * Images and videos from all sources.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 20
         */
        ALL = 0,
        /**
         * Image or video taken by the camera.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 20
         */
        CAMERA = 1,
        /**
         * Screenshot or screen capture video.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 20
         */
        SCREENSHOT = 2
    }
    /**
     * Describes the notification information about the change of a media asset.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @since 20
     */
    interface PhotoAssetChangeInfos {
        /**
         * Type of the media asset change.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 20
         */
        type: NotifyChangeType;
        /**
         * Array of changed media assets. If all media assets need to be queried again, **assetChangeDatas** is null.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 20
         */
        assetChangeDatas: PhotoAssetChangeData[] | null;
        /**
         * Whether the application should query all media assets again. **true** if the application should query all assets
         * again, **false** otherwise.
         *
         * **NOTE**
         *
         * In scenarios involving bulk asset operations or abnormal notifications, **isForRecheck** will be **true**. In
         * this case, the application should query all assets again.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 20
         */
        isForRecheck: boolean;
    }
    /**
     * Describes the change data of a media asset.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @since 20
     */
    interface PhotoAssetChangeData {
        /**
         * Data of the media asset before change. In the case of asset addition, **assetBeforeChange** is null.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 20
         */
        assetBeforeChange: PhotoAssetChangeInfo | null;
        /**
         * Data of the media asset after change. In the case of asset deletion, **assetAfterChange** is null.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 20
         */
        assetAfterChange: PhotoAssetChangeInfo | null;
        /**
         * Whether the content of the media asset is changed. **true** if changed, **false** otherwise.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 20
         */
        isContentChanged: boolean;
        /**
         * Whether the media asset is deleted. **true** if deleted, **false** otherwise.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 20
         */
        isDeleted: boolean;
    }
    /**
     * Describes the information about a media asset.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @since 20
     */
    interface PhotoAssetChangeInfo {
        /**
         * URI of the media asset.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 20
         */
        uri: string;
        /**
         * Type of the media asset (image or video).
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 20
         */
        mediaType: PhotoType;
        /**
         * URI of the album that the media asset belongs to.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 20
         */
        albumUri: string;
        /**
         * Whether the media asset is marked as a favorite. **true** if marked, **false** otherwise.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 26.0.0
         */
        isFavorite: boolean;
    }
    /**
     * Describes the notification information about the change of an album.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @since 20
     */
    interface AlbumChangeInfos {
        /**
         * Type of the album change.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 20
         */
        type: NotifyChangeType;
        /**
         * Array of changed albums. If all albums need to be queried again, **albumChangeDatas** is null.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 20
         */
        albumChangeDatas: AlbumChangeData[] | null;
        /**
         * Whether the application should query all media assets again. **true** if the application should query all assets
         * again, **false** otherwise.
         *
         * **NOTE**
         *
         * In scenarios involving bulk asset operations or abnormal notifications, **isForRecheck** will be **true**. In
         * this case, the application should query all assets again.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 20
         */
        isForRecheck: boolean;
    }
    /**
     * Describes the change data of an album.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @since 20
     */
    interface AlbumChangeData {
        /**
         * Data of the album before change. If an album is added, **albumBeforeChange** is null.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 20
         */
        albumBeforeChange: AlbumChangeInfo | null;
        /**
         * Data of the album after change. In the case of album deletion, **albumAfterChange** is null.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 20
         */
        albumAfterChange: AlbumChangeInfo | null;
    }
    /**
     * Describes the information about an album.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @since 20
     */
    interface AlbumChangeInfo {
        /**
         * Type of the album.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 20
         */
        albumType: AlbumType;
        /**
         * Subtype of the album.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 20
         */
        albumSubtype: AlbumSubtype;
        /**
         * Album name.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 20
         */
        albumName: string;
        /**
         * URI of the album.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 20
         */
        albumUri: string;
        /**
         * Number of images in the album.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 20
         */
        imageCount: number;
        /**
         * Number of videos in the album.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 20
         */
        videoCount: number;
        /**
         * Total number of assets in the album, including images and videos.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 20
         */
        count: number;
        /**
         * URI of the album cover asset.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 20
         */
        coverUri: string;
    }
    /**
     * Enumerates the notification event types.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @since 10
     */
    enum NotifyType {
        /**
         * A file asset or album is added.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 10
         */
        NOTIFY_ADD,
        /**
         * A file asset or album is updated.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 10
         */
        NOTIFY_UPDATE,
        /**
         * A file asset or album is removed.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 10
         */
        NOTIFY_REMOVE,
        /**
         * A file asset is added to the album.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 10
         */
        NOTIFY_ALBUM_ADD_ASSET,
        /**
         * A file asset is removed from the album.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 10
         */
        NOTIFY_ALBUM_REMOVE_ASSET
    }
    /**
     * Enumerates the **DefaultChangeUri** subtypes.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @since 10
     */
    enum DefaultChangeUri {
        /**
         * Default **PhotoAsset** URI, which must be used with **forChildUris{true}** to subscribe to change notifications
         * of all photo assets.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 10
         */
        DEFAULT_PHOTO_URI = 'file://media/Photo',
        /**
         * Default album URI, which must be used with **forChildUris{true}** to subscribe to change notifications of all
         * albums.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 10
         */
        DEFAULT_ALBUM_URI = 'file://media/PhotoAlbum'
    }
    /**
     * Defines the return value of the listener callback.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @since 10
     */
    interface ChangeData {
        /**
         * Notification type.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 10
         */
        type: NotifyType;
        /**
         * All URIs with the same [NotifyType]{@link @ohos.file.photoAccessHelper:photoAccessHelper.NotifyType}, which can
         * be **PhotoAsset** or **Album**.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 10
         */
        uris: Array<string>;
        /**
         * URIs of the changed files in the album. The value may be undefined. Check whether the value is undefined before
         * using it.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 10
         */
        extraUris: Array<string>;
    }
    /**
     * Enumerates the media file types.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @crossplatform [since 12]
     * @atomicservice [since 11]
     * @since 10
     */
    export enum PhotoViewMIMETypes {
        /**
         * Image.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        IMAGE_TYPE = 'image/*',
        /**
         * Video.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        VIDEO_TYPE = 'video/*',
        /**
         * Image and video.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        IMAGE_VIDEO_TYPE = '*/*',
        /**
         * Moving photo.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 12
         */
        MOVING_PHOTO_IMAGE_TYPE = 'image/movingPhoto'
    }
    /**
     * Enumeration type of filter operator.
     *
     * @enum { number } FilterOperator
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @atomicservice
     * @since 19
     */
    export enum FilterOperator {
        /**
         * Equal to.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 19
         */
        EQUAL_TO = 0,
        /**
         * Not equal to.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 19
         */
        NOT_EQUAL_TO = 1,
        /**
         * Greater than.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 19
         */
        MORE_THAN = 2,
        /**
         * Less than.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 19
         */
        LESS_THAN = 3,
        /**
         * Greater than or equal to.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 19
         */
        MORE_THAN_OR_EQUAL_TO = 4,
        /**
         * Less than or equal to.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 19
         */
        LESS_THAN_OR_EQUAL_TO = 5,
        /**
         * Within the specified range.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 19
         */
        BETWEEN = 6
    }
    /**
     * Enumeration type of single selection mode
     *
     * @enum { number } SingleSelectionMode
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @atomicservice
     * @since 18
     */
    export enum SingleSelectionMode {
        /**
         * Mode for previewing large images.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 18
         */
        BROWSER_MODE = 0,
        /**
         * Mode for direct selection.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 18
         */
        SELECT_MODE = 1,
        /**
         * Compatibility mode. Tapping the bottom-right area enables direct selection, whereas tapping elsewhere switches to
         * large image preview mode.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 18
         */
        BROWSER_AND_SELECT_MODE = 2
    }
    /**
     * Defines the basic options for selecting media files from Gallery.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    export class BaseSelectOptions {
        /**
         * Available media file types. **IMAGE_VIDEO_TYPE** is used by default.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        MIMEType?: PhotoViewMIMETypes;
        /**
         * Maximum number of media files that can be selected. The maximum value is **500**, and the default value is **50**
         * .
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice [since 11]
         * @since 10
         */
        maxSelectNumber?: number;
        /**
         * Whether the image is searchable. **true** if searchable, **false** otherwise.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 11
         */
        isSearchSupported?: boolean;
        /**
         * Whether photo taking is supported. **true** if supported, **false** otherwise.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 11
         */
        isPhotoTakingSupported?: boolean;
        /**
         * Image recommendation parameters.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 11
         */
        recommendationOptions?: RecommendationOptions;
        /**
         * URI of the preselected image.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 11
         */
        preselectedUris?: Array<string>;
        /**
         * Whether to enable full image preview if a single image is selected. **true** to enable, **false** otherwise. The
         * default value is **true**.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 12
         */
        isPreviewForSingleSelectionSupported?: boolean;
        /**
         * Single selection mode. The default value is **SingleSelectionMode.BROWSER_MODE**.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 18
         */
        singleSelectionMode?: SingleSelectionMode;
        /**
         * Configuration for file type filtering. Multiple types can be specified.
         *
         * When this parameter is set, the **MIMEType** configuration automatically becomes invalid.
         *
         * When this parameter is set, only media files of the configured filter type are displayed. You are advised to
         * notify users that only images or videos of the specified type can be selected.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 19
         */
        mimeTypeFilter?: MimeTypeFilter;
        /**
         * Configuration for file size filtering.
         *
         * When this parameter is set, only media files within the specified size range are displayed. You are advised to
         * notify users that only images or videos of the specified size can be selected.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 19
         */
        fileSizeFilter?: FileSizeFilter;
        /**
         * Configuration for video duration filtering.
         *
         * When this parameter is set, only media files within the specified duration range are displayed. You are advised
         * to notify users that only videos of the specified length can be selected.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 19
         */
        videoDurationFilter?: VideoDurationFilter;
        /**
         * A string array of filter criteria, supporting combinations of various types.
         *
         * The string format is as follows: **photoType | photoSubType1,photoSubType2, ... | mimeType1,mimeType2, ...**
         *
         * - The first part specifies a single **photoType**, which is fixed at **image** or **video**.
         * - The second part lists 1 to *N* photoSubTypes, separated by commas, with an OR relationship. Currently, the
         * maximum value of *N* is **1**. Options include **movingPhoto** or "*" (ignore).
         * - The third part lists 1 to *N* mimeTypes, separated by commas, with an OR relationship. Currently, the maximum
         * value of *N* is **10**. The format is similar to [MimeTypeFilter]{@link photoAccessHelper.MimeTypeFilter}.
         *
         * Filters are combined using intersection logic.
         *
         * The NOT logic is supported. To exclude types, use parentheses. Each string can have only one set.
         *
         * If the filter string does not match the specifications, the result is empty.
         *
         * Only the first three array elements are used; **MIMETypes** and **mimeTypeFilter** are ignored.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 20
         */
        combinedMediaTypeFilter?: Array<string>;
        /**
         * An array used to filter media files by type and size.
         *
         * Only the first three array elements are used; **MIMETypes** and **fileSizeFilter** are ignored.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 20
         */
        photoViewMimeTypeFileSizeFilters?: Array<PhotoViewMimeTypeFileSizeFilter>;
        /**
         * Whether the moving photo badge is displayed in the photo browser page. **true** to display the badge, **false**
         * to hide it. The default is **false**.
         *
         * If this parameter is set to **true**, [Photoselectresult]{@link photoAccessHelper.PhotoSelectResult} returns the
         * **movingPhotoBadgeStates** array. The default status of a moving photo is
         * [MOVING_PHOTO_ENABLED]{@link @ohos.file.photoAccessHelper:photoAccessHelper.MovingPhotoBadgeStateType}.
         *
         * Note: Use both **isMovingPhotoBadgeShown** and **MovingPhotoBadgeStateType** to determine whether a photo is a
         * moving photo.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform
         * @atomicservice
         * @since 22
         */
        isMovingPhotoBadgeShown?: boolean;
        /**
         * Media asset filter, with a maximum length of 50 items. If the limit is exceeded, only the first 50 items are
         * used.
         *
         * **NOTE**
         *
         * 1. When this filter is applied, other filters become invalid.
         * 2. When setting multiple conditions, enclose the filter conditions in parentheses to prevent conflicts with
         *    internal filter items.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 22
         */
        assetFilter?: Array<OperationItem>;
        /**
         * Playback mode of the moving photo. The maximum array length is 2. If this limit is exceeded, the first two
         * elements are used, and the extra ones are automatically ignored.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        autoPlayScenes?: Array<AutoPlayScene>;
        /**
         * Pinch mode of the grid in the picker.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        gridPinchMode?: GridPinchMode;
        /**
         * Global effect of the moving photo. Currently, only **MOVING_PHOTO_ENABLED** and **MOVING_PHOTO_DISABLED** are
         * supported. The default value is **MOVING_PHOTO_ENABLED**.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        globalMovingPhotoState?: MovingPhotoBadgeStateType;
        /**
         * Whether to display the date group information when the scroll bar is dragged. **true**: yes; **false**: no. The
         * default value is **false**.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        showDateOnScrollbar?: boolean;
        /**
         * Configuration for asset compatibility capabilities.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        assetCompatibleCapability?: AssetCompatibleCapability;
        /**
         * Preferred compatibility mode.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        preferredCompatibleMode?: PreferredCompatibleMode;
    }
    /**
     * Enumerates the types of the moving photo badge.
     *
     * @enum { number } MovingPhotoBadgeStateType
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @atomicservice
     * @since 22
     */
    export enum MovingPhotoBadgeStateType {
        /**
         * The media file is not a moving photo.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform
         * @atomicservice
         * @since 22
         */
        NOT_MOVING_PHOTO = 0,
        /**
         * The moving photo effect is enabled.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform
         * @atomicservice
         * @since 22
         */
        MOVING_PHOTO_ENABLED = 1,
        /**
         * The moving photo effect is disabled.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform
         * @atomicservice
         * @since 22
         */
        MOVING_PHOTO_DISABLED = 2
    }
    /**
     * Describes the configuration for file type filtering.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @atomicservice
     * @since 19
     */
    class MimeTypeFilter {
        /**
         * Types of media files that PhotoPicker allows users to filter by. The maximum array length is 10, thus supporting
         * up to 10 specified types.
         *
         * The filter type is defined by the MIME type, for example, image/jpeg and video/mp4.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 19
         */
        mimeTypeArray: Array<string>;
    }
    /**
     * Describes the configuration for file size filtering.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @atomicservice
     * @since 19
     */
    class FileSizeFilter {
        /**
         * Filter operator.
         *
         * For example, files can be filtered based on being greater than or less than a certain file size.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 19
         */
        filterOperator: FilterOperator;
        /**
         * File size used for filtering.
         *
         * The unit is bytes.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 19
         */
        fileSize: number;
        /**
         * Maximum file size in **FilterOperator.BETWEEN** mode. The default value is **-1**.
         *
         * The unit is bytes.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 19
         */
        extraFileSize?: number;
    }
    /**
     * Describes the configuration for video duration filtering.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @atomicservice
     * @since 19
     */
    class VideoDurationFilter {
        /**
         * Filter operator.
         *
         * For example, files can be filtered based on being greater than or less than a certain file size.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 19
         */
        filterOperator: FilterOperator;
        /**
         * Video duration used for filtering.
         *
         * The unit is milliseconds (ms).
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 19
         */
        videoDuration: number;
        /**
         * Maximum video duration in **FilterOperator.BETWEEN** mode. The default value is **-1**.
         *
         * The unit is milliseconds (ms).
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 19
         */
        extraVideoDuration?: number;
    }
    /**
     * Describes the settings for filtering media files by type and size.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @atomicservice
     * @since 20
     */
    class PhotoViewMimeTypeFileSizeFilter {
        /**
         * Media file types used for filtering.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 20
         */
        photoViewMimeType: PhotoViewMIMETypes;
        /**
         * Media file size used for filtering.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 20
         */
        sizeFilter: FileSizeFilter;
    }
    /**
     * Indicates possible value types
     *
     * @typedef { number | string | boolean }
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @stagemodelonly
     * @atomicservice
     * @since 22
     */
    export type OperationValueType = number | string | boolean;
    /**
     * Describes the settings for filtering media files.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @stagemodelonly
     * @atomicservice
     * @since 22
     */
    export class OperationItem {
        /**
         * Predicates.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 22
         */
        operationType: OperationType;
        /**
         * Column name in the data table.
         *
         * Currently, only the following key fields are supported: **URI**, **PHOTO_TYPE**, **DISPLAY_NAME**, **SIZE**,
         * **DURATION**, **WIDTH**, **HEIGHT**, **ORIENTATION**, **FAVORITE**, **TITLE**, **POSITION**, **PHOTO_SUBTYPE**,
         * **DYNAMIC_RANGE_TYPE**, **COVER_POSITION**, **BURST_KEY**, **LCD_SIZE**, **THM_SIZE**, **DETAIL_TIME**,
         * **MEDIA_SUFFIX**, **OWNER_ALBUM_ID**, **ASPECT_RATIO** and **DATE_TAKEN_MS**.
         *
         * When
         * [select]{@link @ohos.file.photoAccessHelper:photoAccessHelper.PhotoViewPicker#select(option?: PhotoSelectOptions)}
         * is used to set this parameter, an invalid field results in error code 401. When
         * [@ohos.file.PhotoPickerComponent (PhotoPickerComponent)]{@link @ohos.file.PhotoPickerComponent} is used to set
         * this parameter, an invalid field does not trigger the **onPickerControllerReady** callback.
         *
         * This field is not involved in non-conditional predicates such as **and**, **or**, **beginWrap**, and **endWrap**.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 22
         */
        field?: PhotoKeys;
        /**
         * Values needed for matching different predicates.
         *
         * This field is not involved in non-conditional predicates such as **and**, **or**, **beginWrap**, and **endWrap**.
         *
         * The maximum length is 10; if exceeded, only the first 10 values are considered.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 22
         */
        value?: Array<OperationValueType>;
    }
    /**
     * Request read permission result
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @stagemodelonly
     * @atomicservice
     * @since 23
     */
    export class RequestReadPermissionResult {
        /**
         * URIs that have been created and granted the save permission.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        authorizedUris?: Array<string>;
        /**
         * URIs that may be deleted, hidden, or renamed.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        invalidUris?: Array<string>;
    }
    /**
     * Represents the pinch mode of the grid in the picker.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @stagemodelonly
     * @atomicservice
     * @since 23
     */
    export class GridPinchMode {
        /**
         * Grid pinch mode. If this parameter is set, the pinch function is supported. Otherwise, the pinch function is not
         * supported.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        gridPinchModeType?: GridPinchModeType;
        /**
         * Grid level after the picker is started. The default value is **STANDARD**.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        defaultGridLevel?: GridLevel;
    }
    /**
     * Defines additional options for selecting media assets from Gallery. It inherits from **BaseSelectOptions**. It is
     * used to start the picker of the corresponding user ID space.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @crossplatform [since 12]
     * @atomicservice [since 11]
     * @since 10
     */
    class PhotoSelectOptions extends BaseSelectOptions {
        /**
         * Whether the image can be edited. **true** if editable, **false** otherwise.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 11
         */
        isEditSupported?: boolean;
        /**
         * Whether to display the button for selecting the original image. **true** to display, **false** otherwise. The
         * default value is **false**.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 12
         */
        isOriginalSupported?: boolean;
        /**
         * Name of the child window.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 12
         */
        subWindowName?: string;
        /**
         * Text displayed on the complete button.
         *
         * The complete button is located in the lower-right corner of the page. It is used by users to signify that they
         * have finished selecting images.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 14
         */
        completeButtonText?: CompleteButtonText;
        /**
        * Information for restoring the PhotoPicker's state from the last exit.
        *
        * When the selection process is complete, the PhotoPicker returns **contextRecoveryInfo** to the application. The
        * application can then use the information to restore the PhotoPicker's state and the last viewed grid interface
        * the next time it starts the PhotoPicker.
        *
        * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
        * @atomicservice
        * @since 21
        */
        contextRecoveryInfo?: ContextRecoveryInfo;
        /**
         * Whether destruction with
         * [Navigation]{@link Navigation} is
         * supported. **true** if supported, **false** otherwise. The default value is **false**.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        isDestroyedWithNavigation?: boolean;
        /**
         * Maximum number of photos that can be selected.
         *
         * A maximum of 500 photos can be selected. The default value is **500**.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        maxPhotoSelectNumber?: number;
        /**
         * Maximum number of videos that can be selected.
         *
         * A maximum of 500 videos can be selected. The default value is **500**.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        maxVideoSelectNumber?: number;
        /**
         * Whether to automatically switch to the full image preview mode after a photo is taken in single-selection mode.
         * **true** means to switch, and **false** means the opposite. The default value is **false**.
         *
         * Note: This parameter takes effect only when
         * [SingleSelectionMode]{@link @ohos.file.photoAccessHelper:photoAccessHelper.SingleSelectionMode} is set to
         * **BROWSER_MODE** or **BROWSER_AND_SELECT_MODE** and
         * [BaseSelectOptions.isPreviewForSingleSelectionSupported]{@link @ohos.file.photoAccessHelper:photoAccessHelper.BaseSelectOptions}
         * is set to **true**.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        isReturnToPhotoBrowserEnabled?: boolean;
        /**
         * Support displaying index numbers.
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        isSelectionNumberVisible?: boolean;
        /**
         * Support selection order adjustment.
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        isSelectionOrderAdjustable?: boolean;
    }
    /**
     * Defines the image recommendation options. The image recommendation feature depends on the image data analysis
     * capability, which varies with devices.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @atomicservice
     * @since 11
     */
    class RecommendationOptions {
        /**
         * Type of the recommended image.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 11
         */
        recommendationType?: RecommendationType;
        /**
         * Text based on which images are recommended. If both **recommendationType** and **textContextInfo** are set,
         * **textContextInfo** takes precedence over **recommendationType**.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 12
         */
        textContextInfo?: TextContextInfo;
    }
    /**
     * Represents the text information about the recommended images.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @atomicservice
     * @since 12
     */
    interface TextContextInfo {
        /**
         * Text based on which images are recommended. The text cannot exceed 250 characters. The default value is an empty
         * string.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 12
         */
        text?: string;
    }
    /**
     * Defines information about the images or videos selected.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @crossplatform [since 12]
     * @atomicservice [since 11]
     * @since 10
     */
    class PhotoSelectResult {
        /**
         * URIs of the media files selected.
         *
         * This URI array can be used only by calling the
         * [photoAccessHelper.getAssets]{@link @ohos.file.photoAccessHelper:photoAccessHelper.PhotoAccessHelper.getAssets(options: FetchOptions, callback: AsyncCallback<FetchResult<PhotoAsset>>)}
         * API through temporary authorization. For details, see
         * [Using a Media File URI](docroot://file-management/user-file-uri-intro.md#using-a-media-file-uri).
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        photoUris: Array<string>;
        /**
         * Whether the selected media file is the original image. **true** if yes, **false** otherwise. The default value is
         * **false**.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        isOriginalPhoto: boolean;
        /**
         * Information about the context of exiting the PhotoPicker. This information is returned when the selection process
         * is complete and is used by the application within **PhotoSelectOptions** during the subsequent launch of the
         * PhotoPicker to restore the state from the previous exit.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 21
         */
        contextRecoveryInfo: ContextRecoveryInfo;
        /**
         * Array of moving photo badge states for the media files selected from Gallery.
         *
         * If **isMovingPhotoBadgeShown** is set to **true**, this array contains the moving photo badge states. Otherwise,
         * it is empty.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 22
         */
        movingPhotoBadgeStates: Array<MovingPhotoBadgeStateType>;
    }
    /**
     * PhotoViewPicker provides APIs for the user to select images and videos. Before using the APIs of PhotoViewPicker,
     * you need to create a PhotoViewPicker instance.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @crossplatform [since 12]
     * @atomicservice [since 11]
     * @since 10
     */
    class PhotoViewPicker {
        /**
         * Starts a **photoPicker** page for the user to select one or more images or videos. This API uses a promise to
         * return the result. You can pass in **PhotoSelectOptions** to specify the type and maximum number of the files to
         * select. A **PhotoSelectResult** object is returned.
         *
         * > **NOTE**
         * >
         * > **photoUris** in the PhotoSelectResult object returned by this API has permanent authorization and can be used
         * > only by calling
         * > [photoAccessHelper.getAssets]{@link @ohos.file.photoAccessHelper:photoAccessHelper.PhotoAccessHelper.getAssets(options: FetchOptions, callback: AsyncCallback<FetchResult<PhotoAsset>>)}
         * > . For details, see
         * > [Using a Media File URI](docroot://file-management/user-file-uri-intro.md#using-a-media-file-uri).
         *
         * @param { PhotoSelectOptions } [option] - Options for selecting files. If this parameter is not specified, up to 5
         *     0 images and videos are selected by default.
         * @returns { Promise<PhotoSelectResult> } Promise used to return information about the images or videos selected.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 13900042 - Unknown error
         * @throws { BusinessError } 23800151 - Scene parameters validate failed, possible causes:
         *     <br>1. An illegal enumeration value was passed to PhotoSelectOptions.globalMovingPhotoState.
         *     Only MOVING_PHOTO_ENABLED and MOVING_PHOTO_DISABLED are supported for configuration;
         *     <br>2. An illegal enumeration value was passed to PhotoSelectOptions.assetCompatibleAbility. [since 12]
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        select(option?: PhotoSelectOptions): Promise<PhotoSelectResult>;
        /**
         * Starts a **photoPicker** page for the user to select one or more images or videos. This API uses an asynchronous
         * callback to return the result. You can pass in **PhotoSelectOptions** to specify the media file type and the
         * maximum number of files to select.
         *
         * > **NOTE**
         * >
         * > **photoUris** in the PhotoSelectResult object returned by this API has permanent authorization and can be used
         * > only by calling
         * > [photoAccessHelper.getAssets]{@link @ohos.file.photoAccessHelper:photoAccessHelper.PhotoAccessHelper.getAssets(options: FetchOptions, callback: AsyncCallback<FetchResult<PhotoAsset>>)}
         * > . For details, see
         * > [Using a Media File URI](docroot://file-management/user-file-uri-intro.md#using-a-media-file-uri).
         *
         * @param { PhotoSelectOptions } option - Options for selecting images or videos.
         * @param { AsyncCallback<PhotoSelectResult> } callback - Callback used to return information about the images or
         *     videos selected.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 13900042 - Unknown error
         * @throws { BusinessError } 23800151 - Scene parameters validate failed, possible causes:
         *     <br>1. An illegal enumeration value was passed to PhotoSelectOptions.globalMovingPhotoState.
         *     Only MOVING_PHOTO_ENABLED and MOVING_PHOTO_DISABLED are supported for configuration; [since 12]
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        select(option: PhotoSelectOptions, callback: AsyncCallback<PhotoSelectResult>): void;
        /**
         * Starts a **photoPicker** page for the user to select one or more images or videos. This API uses an asynchronous
         * callback to return the result.
         *
         * > **NOTE**
         * >
         * > **photoUris** in the PhotoSelectResult object returned by this API has permanent authorization and can be used
         * > only by calling
         * > [photoAccessHelper.getAssets]{@link @ohos.file.photoAccessHelper:photoAccessHelper.PhotoAccessHelper.getAssets(options: FetchOptions, callback: AsyncCallback<FetchResult<PhotoAsset>>)}
         * > . For details, see
         * > [Using a Media File URI](docroot://file-management/user-file-uri-intro.md#using-a-media-file-uri).
         *
         * @param { AsyncCallback<PhotoSelectResult> } callback - Callback used to return information about the images or
         *     videos selected.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types.
         * @throws { BusinessError } 13900042 - Unknown error
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        select(callback: AsyncCallback<PhotoSelectResult>): void;
    }
    /**
     * Enumerates the types of the resources to write.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @atomicservice
     * @since 11
     */
    enum ResourceType {
        /**
         * Image resource.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 11
         */
        IMAGE_RESOURCE = 1,
        /**
         * Video resource.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 11
         */
        VIDEO_RESOURCE = 2
    }
    /**
     * Enumerates the types of image files to save.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @since 13
     */
    enum ImageFileType {
        /**
         * JPEG.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 13
         */
        JPEG = 1,
        /**
         * HEIF.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 13
         */
        HEIF = 2
    }
    /**
     * Enumerates the predicates.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @stagemodelonly
     * @atomicservice
     * @since 22
     */
    export enum OperationType {
        /**
         * Checks for equality, using the first element of the **value** array to match the predicate. If the array is
         * longer, only the first element is considered.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 22
         */
        EQUAL_TO = 1,
        /**
         * Checks for inequality, using the first element of the **value** array to match the predicate. If the array is
         * longer, only the first element is considered.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 22
         */
        NOT_EQUAL_TO = 2,
        /**
         * Checks whether the value is greater than the predicate, using the first element of the **value** array to match
         * the predicate. If the array is longer, only the first element is considered.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 22
         */
        GREATER_THAN = 3,
        /**
         * Checks whether the value is less than the predicate, using the first element of the **value** array to match the
         * predicate. If the array is longer, only the first element is considered.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 22
         */
        LESS_THAN = 4,
        /**
         * Checks whether the value is greater than or equal to the predicate, using the first element of the **value**
         * array to match the predicate. If the array is longer, only the first element is considered.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 22
         */
        GREATER_THAN_OR_EQUAL_TO = 5,
        /**
         * Checks whether the value is less than or equal to the predicate, using the first element of the **value** array
         * to match the predicate. If the array is longer, only the first element is considered.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 22
         */
        LESS_THAN_OR_EQUAL_TO = 6,
        /**
         * Logical 'AND', similar to 'and' in database queries. No **field** or **value** is needed.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 22
         */
        AND = 7,
        /**
         * Logical 'OR', similar to 'or' in database queries. No **field** or **value** is needed.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 22
         */
        OR = 8,
        /**
         * Matches fields within a specified range, with a maximum value length of 10.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 22
         */
        IN = 9,
        /**
         * Matches fields outside a specified range, with a maximum value length of 10.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 22
         */
        NOT_IN = 10,
        /**
         * Adds a left parenthesis to the predicate, similar to "(" in database queries. It must be used with a right
         * parenthesis. No **field** or **value** is needed.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 22
         */
        BEGIN_WRAP = 11,
        /**
         * Adds a right parenthesis to the predicate, similar to ")" in database queries. It must be used with a left
         * parenthesis. No **field** or **value** is needed.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 22
         */
        END_WRAP = 12,
        /**
         * Matches fields within a specified range,
         *
         * including both endpoints (closed interval). It uses the first two elements of the **value** array, where the
         * first element is the lower boundary and the second is the upper boundary. For example, in the array [1, 2, 3, 4],
         * the first two elements are used, with 1 as the lower boundary and 2 as the upper boundary.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 22
         */
        BETWEEN = 13,
        /**
         * Matches fields outside a specified range,
         *
         * excluding both endpoints (open interval). It uses the first two elements of the **value** array, where the first
         * element is the lower boundary and the second is the upper boundary. For example, in the array [1, 2, 3, 4], the
         * first two elements are used, with 1 as the lower boundary and 2 as the upper boundary.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 22
         */
        NOT_BETWEEN = 14
    }
    /**
     * Media change request, which is the parent class of the asset change request and album change request.
     *
     * > **NOTE**
     * >
     * > The media change request takes effect only after
     * > [applyChanges]{@link @ohos.file.photoAccessHelper:photoAccessHelper.PhotoAccessHelper.applyChanges} is called.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @atomicservice
     * @since 11
     */
    interface MediaChangeRequest {
        /**
         * A readonly member for type checking.
         *
         * @type { string }
         * @readonly
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        readonly comment: string;
    }
    /**
     * Represents a media asset change request.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @atomicservice
     * @since 11
     */
    class MediaAssetChangeRequest implements MediaChangeRequest {
        /**
         * A readonly member for type checking.
         *
         * @type { string }
         * @readonly
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        readonly comment: string;
        /**
         * Constructor used to initialize an asset change request.
         *
         * @param { PhotoAsset } asset - Assets to change.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice [since 12]
         * @since 11
         */
        constructor(asset: PhotoAsset);
        /**
         * Creates an image asset change request.
         *
         * For details about data source of the asset to be created, see
         * [@ohos.file.fileuri (File URI)]{@link @ohos.file.fileuri:fileUri}.
         *
         * @param { Context } context - Context of the ability instance.
         * @param { string } fileUri - Data source of the image asset, which is specified by a URI in the application
         *     sandbox directory. Example: **'file://com.example.temptest/data/storage/el2/base/haps/entry/files/test.jpg'**
         *     .
         * @returns { MediaAssetChangeRequest } **MediaAssetChangeRequest** created.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 13900002 - The file corresponding to the URI is not in the app sandbox.
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice [since 12]
         * @since 11
         */
        static createImageAssetRequest(context: Context, fileUri: string): MediaAssetChangeRequest;
        /**
         * Creates a video asset change request.
         *
         * For details about data source of the asset to be created, see
         * [@ohos.file.fileuri (File URI)]{@link @ohos.file.fileuri:fileUri}.
         *
         * @param { Context } context - Context of the ability instance.
         * @param { string } fileUri - Data source of the video asset, which is specified by a URI in the application
         *     sandbox directory. Example: **'file://com.example.temptest/data/storage/el2/base/haps/entry/files/test.mp4'**
         *     .
         * @returns { MediaAssetChangeRequest } **MediaAssetChangeRequest** created.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 13900002 - The file corresponding to the URI is not in the app sandbox.
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 11
         */
        static createVideoAssetRequest(context: Context, fileUri: string): MediaAssetChangeRequest;
        /**
         * Create an asset change request based on the file type and filename extension.
         *
         * @param { Context } context - Context of the ability instance.
         * @param { PhotoType } photoType - Type of the file to create, which can be **IMAGE** or **VIDEO**.
         * @param { string } extension - File name extension, for example, **'jpg'**.
         * @param { CreateOptions } [options] - Options for creating the image or video asset, for example,
         *     **{title: 'testPhoto'}**.
         *     <br>The file name must not contain any invalid characters, which are:.. \ / : * ? " ' ` < > | { } [ ]
         * @returns { MediaAssetChangeRequest } **MediaAssetChangeRequest** created.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 11
         */
        static createAssetRequest(context: Context, photoType: PhotoType, extension: string, options?: CreateOptions): MediaAssetChangeRequest;
        /**
         * Deletes media assets. The deleted assets are moved to the trash. This API uses a promise to return the result.
         *
         * @permission ohos.permission.WRITE_IMAGEVIDEO
         * @param { Context } context - Context of the ability instance.
         * @param { Array<PhotoAsset> } assets - Array of media assets to delete. The array can contain a maximum of 300
         *     elements. <!--Del-->System applications are not subject to this limitation.<!--DelEnd-->
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 201 - Permission denied
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 11
         */
        static deleteAssets(context: Context, assets: Array<PhotoAsset>): Promise<void>;
        /**
         * Deletes media assets. The deleted assets are moved to the trash. This API uses a promise to return the result.
         *
         * @permission ohos.permission.WRITE_IMAGEVIDEO
         * @param { Context } context - Context of the ability instance.
         * @param { Array<string> } uriList - URIs of the media assets to delete. The array can contain a maximum of 300
         *     elements. <!--Del-->System applications are not subject to this limitation.<!--DelEnd-->
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 201 - Permission denied
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 14000002 - The uri format is incorrect or does not exist.
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 11
         */
        static deleteAssets(context: Context, uriList: Array<string>): Promise<void>;
        /**
         * Obtains the asset in this asset change request.
         *
         * > **NOTE**
         * >
         * > For the change request used to create an asset, this API returns **null** before
         * > [applyChanges]{@link @ohos.file.photoAccessHelper:photoAccessHelper.PhotoAccessHelper.applyChanges} is called
         * > to apply the changes.
         *
         * @returns { PhotoAsset } Asset obtained.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types.
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice [since 12]
         * @since 11
         */
        getAsset(): PhotoAsset;
        /**
         * Favorites or unfavorites this file asset.
         *
         * @param { boolean } favoriteState - Whether to favorite the file. **true** to favorite, **false** otherwise.
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 26.0.0
         */
        setFavorite(favoriteState: boolean): void;
        /**
         * Sets the media asset title.
         *
         * @param { string } title - Title to set.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice [since 12]
         * @since 11
         */
        setTitle(title: string): void;
        /**
         * Obtains the handler used for writing a file to cache. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > For the same asset change request, this API cannot be repeatedly called after a temporary file write handle is
         * > successfully obtained.
         *
         * @permission ohos.permission.WRITE_IMAGEVIDEO
         * @returns { Promise<number> } Promise used to return the write handle obtained.
         * @throws { BusinessError } 201 - Permission denied
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types.
         * @throws { BusinessError } 14000011 - System inner fail. Possible causes:
         *     <br>1. The database is corrupted;
         *     <br>2. The file system is abnormal;
         *     <br>3. The IPC request timed out.
         * @throws { BusinessError } 14000016 - Operation Not Support
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 11
         */
        getWriteCacheHandler(): Promise<number>;
        /**
         * Adds resources from the application sandbox based on the file URI. For details about the data source, see
         * [@ohos.file.fileuri (File URI)]{@link @ohos.file.fileuri:fileUri}.
         *
         * > **NOTE**
         * >
         * > For the same asset change request, this API cannot be repeatedly called after the resource is successfully
         * > added. For a moving photo, you can call this API twice to add the image and video resources.
         *
         * @param { ResourceType } type - Type of the resource to add.
         * @param { string } fileUri - Data source of the resource to be added, which is specified by a URI in the
         *     application sandbox directory. Example:
         *     **'file://com.example.temptest/data/storage/el2/base/haps/entry/files/test.jpg'**.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 13900002 - The file corresponding to the URI is not in the app sandbox.
         * @throws { BusinessError } 14000011 - System inner fail
         * @throws { BusinessError } 14000016 - Operation Not Support
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 11
         */
        addResource(type: ResourceType, fileUri: string): void;
        /**
         * Adds a resource using **ArrayBuffer** data.
         *
         * > **NOTE**
         * >
         * > For the same asset change request, this API cannot be repeatedly called after the resource is successfully
         * > added. For a moving photo, you can call this API twice to add the image and video resources.
         *
         * @param { ResourceType } type - Type of the resource to add.
         * @param { ArrayBuffer } data - Data of the resource to add.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 14000011 - System inner fail
         * @throws { BusinessError } 14000016 - Operation Not Support
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 11
         */
        addResource(type: ResourceType, data: ArrayBuffer): void;
        /**
         * Saves the photo taken by the camera.
         *
         * @throws { BusinessError } 14000011 - System inner fail
         * @throws { BusinessError } 14000016 - Operation Not Support
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 12
         */
        saveCameraPhoto(): void;
        /**
         * Saves the photo taken by the camera.
         *
         * @param { ImageFileType } imageFileType - File type of the photo to save.
         * @throws { BusinessError } 14000011 - System inner fail
         * @throws { BusinessError } 14000016 - Operation Not Support
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 13
         */
        saveCameraPhoto(imageFileType: ImageFileType): void;
        /**
         * Discards the photo taken by the camera.
         *
         * @throws { BusinessError } 14000011 - Internal system error
         * @throws { BusinessError } 14000016 - Operation Not Support
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 12
         */
        discardCameraPhoto(): void;
        /**
         * Sets the orientation of this image.
         *
         * @param { number } orientation - Rotation angle of the image to set. The value can only be **0**, **90**, **180**, or
         *     **270**.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 14000011 - Internal system error
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 15
         */
        setOrientation(orientation: number): void;
    }
    /**
     * Represents a request for changing multiple assets.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @since 26.0.0
     */
    class MediaAssetsChangeRequest implements MediaChangeRequest {
        /**
         * Constructor.
         *
         * @param { Array<PhotoAsset> } assets - Assets to change.
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 26.0.0
         */
        constructor(assets: Array<PhotoAsset>);
        /**
         * Favorites or unfavorites this file asset.
         *
         * @param { boolean } favoriteState - Whether to favorite the file. **true** to favorite, **false** otherwise.
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 26.0.0
         */
        setFavorite(favoriteState: boolean): void;
    }
    /**
     * Provides APIs for managing the media album change request.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @since 11
     */
    class MediaAlbumChangeRequest implements MediaChangeRequest {
        /**
         * A readonly member for type checking.
         *
         * @type { string }
         * @readonly
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @since 23
         */
        readonly comment: string;
        /**
         * Constructor used to initialize a new object.
         *
         * @param { Album } album - Album to change.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 11
         */
        constructor(album: Album);
        /**
         * Obtains the album in the current album change request.
         *
         * > **NOTE**
         * >
         * > For the change request for creating an album, this API returns **null** before
         * > [applyChanges]{@link @ohos.file.photoAccessHelper:photoAccessHelper.PhotoAccessHelper.applyChanges} is called
         * > to apply the changes.
         *
         * @returns { Album } Album obtained.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types.
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 11
         */
        getAlbum(): Album;
        /**
         * Sets the album name.
         *
         * The album name must meet the following requirements:
         *
         * - The total length of the album name must be between 1 and 255 characters.
         * - It must not contain any invalid characters, which are:
         *
         * . \ / : * ? " ' ` < > | { } [ ]
         *
         * - It is case-insensitive.
         * - Duplicate album names are not allowed.
         *
         * @param { string } name - Album name to set.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 11
         */
        setAlbumName(name: string): void;
        /**
         * Add assets to the album.
         *
         * @param { Array<PhotoAsset> } assets - Array of assets to add.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 14000011 - System inner fail
         * @throws { BusinessError } 14000016 - Operation Not Support
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 11
         */
        addAssets(assets: Array<PhotoAsset>): void;
        /**
         * Removes assets from the album.
         *
         * @param { Array<PhotoAsset> } assets - Array of assets to remove.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 14000011 - System inner fail
         * @throws { BusinessError } 14000016 - Operation Not Support
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 11
         */
        removeAssets(assets: Array<PhotoAsset>): void;
    }
    /**
     * MovingPhoto provides APIs for managing a moving photo instance.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @atomicservice
     * @since 12
     */
    interface MovingPhoto {
        /**
         * Requests the image data and video data of this moving photo and writes them to the specified URIs, respectively.
         * This API uses a promise to return the result.
         *
         * @permission ohos.permission.READ_IMAGEVIDEO
         * @param { string } imageFileUri - URI to which the image data of the moving photo is to be written. Example:
         *     **"file://com.example.temptest/data/storage/el2/base/haps/ImageFile.jpg"**.
         * @param { string } videoFileUri - URI to which the video data of the moving photo is to be written. Example:
         *     **"file://com.example.temptest/data/storage/el2/base/haps/VideoFile.mp4"**.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 201 - Permission denied
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 14000011 - System inner fail. Possible causes:
         *     <br>1. The database is corrupted;
         *     <br>2. The file system is abnormal;
         *     <br>3. The IPC request timed out.
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 12
         */
        requestContent(imageFileUri: string, videoFileUri: string): Promise<void>;
        /**
         * Requests the moving photo content of the specified resource type and writes it to the specified URI. This API
         * uses a promise to return the result.
         *
         * @permission ohos.permission.READ_IMAGEVIDEO
         * @param { ResourceType } resourceType - Resource type of the moving photo content to request.
         * @param { string } fileUri - URI to which the moving photo content is to be written.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 201 - Permission denied
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 14000011 - System inner fail. Possible causes:
         *     <br>1. The database is corrupted;
         *     <br>2. The file system is abnormal;
         *     <br>3. The IPC request timed out.
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 12
         */
        requestContent(resourceType: ResourceType, fileUri: string): Promise<void>;
        /**
         * Requests the moving photo content of the specified resource type and returns it in ArrayBuffer format. This API
         * uses a promise to return the result.
         *
         * @permission ohos.permission.READ_IMAGEVIDEO
         * @param { ResourceType } resourceType - Resource type of the moving photo content to request.
         * @returns { Promise<ArrayBuffer> } Promise used to return the requested content in an ArrayBuffer.
         * @throws { BusinessError } 201 - Permission denied
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types;
         *     <br>3. Parameter verification failed.
         * @throws { BusinessError } 14000011 - System inner fail. Possible causes:
         *     <br>1. The database is corrupted;
         *     <br>2. The file system is abnormal;
         *     <br>3. The IPC request timed out.
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 12
         */
        requestContent(resourceType: ResourceType): Promise<ArrayBuffer>;
        /**
         * Obtains the URI of this moving photo.
         *
         * @returns { string } URI of the moving photo obtained.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     <br>1. Mandatory parameters are left unspecified;
         *     <br>2. Incorrect parameter types.
         * @throws { BusinessError } 14000011 - System inner fail
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @atomicservice
         * @since 12
         */
        getUri(): string;
    }
    /**
     * Defines the playback mode of the moving photo in different scenarios.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @stagemodelonly
     * @atomicservice
     * @since 23
     */
    export class AutoPlayScene {
        /**
         * Scene of the moving photo playback.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        sceneType: SceneType;
        /**
         * Whether to support automatic playback of the moving photo.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        playMode: PlayMode;
    }
    /**
     * Enumeration type of scene.
     *
     * @enum { number } SceneType
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @stagemodelonly
     * @atomicservice
     * @since 23
     */
    export enum SceneType {
        /**
         * Tap the grid icon to browse the large image.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        GRID_TO_PHOTO_BROWSER = 0,
        /**
         * Swipe left or right in the large image scene.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        PHOTO_BROWSER_SWIPE = 1
    }
    /**
     * Enumeration type of grid pinch mode.
     *
     * @enum { number } GridPinchModeType
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @stagemodelonly
     * @atomicservice
     * @since 23
     */
    export enum GridPinchModeType {
        /**
         * Users are allowed to pinch the grid, and then select it or click it to operate the large image.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        FULL_FUNCTION_GRID = 0
    }
    /**
     * Enumeration type of grid level.
     *
     * @enum { number } GridLevel
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @stagemodelonly
     * @atomicservice
     * @since 23
     */
    export enum GridLevel {
        /**
         * Spacious grid level. This level is the number of standard grid columns minus 1.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        SPACIOUS = 0,
        /**
         * Standard grid level. The number of standard grid columns varies with the device size. If no number of standard
         * grid columns is configured, the system uses the default number of columns.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        STANDARD = 1,
        /**
         * Compact grid level. This level is the number of standard grid columns plus 1.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        COMPACT = 2
    }
    /**
     * Enumerates whether to support automatic playback of the moving photo.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @stagemodelonly
     * @atomicservice
     * @since 23
     */
    export enum PlayMode {
        /**
         * The automatic playback of the moving photo is not supported.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        DEFAULT = 0,
        /**
         * The automatic playback of the moving photo is supported.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        AUTO_PLAY = 1
    }
    /**
     * Enumerates the log modes of video files.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @since 22
     */
    export enum VideoMode {
        /**
         * Default type.
         *
         * A value of **0** indicates that the video is either not in log mode or its type has not yet been determined. This
         * value may later be updated to **1** for some videos after type determination, so it is not recommended for use in
         * queries.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 22
         */
        DEFAULT = 0,
        /**
         * Video file in log mode.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @since 22
         */
        LOG_VIDEO = 1
    }
    /**
     * Defines the asset compatibility capability.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @stagemodelonly
     * @atomicservice
     * @since 24
     */
    interface AssetCompatibleCapability {
        /**
         * Whether high-resolution assets are supported. **true**: yes; **false**: no.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        supportedHighResolution: boolean;
        /**
         * Supported MIME types.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        supportedMimeType?: Array<string>;
    }
    /**
     * Preferred compatible mode.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    enum PreferredCompatibleMode {
        /**
         * Performs transcoding based on the configured asset compatibility capabilities.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        DEFAULT = 0,
        /**
         * No transcoding is performed. The asset is returned in its original format.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        CURRENT = 1,
        /**
         * All assets are transcoded to the most widely compatible format.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        COMPATIBLE = 2
    }
    /**
     * Enumeration of permission level for an application to access asset.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    enum MediaAssetPermissionState {
        /**
         * Not media asset uri.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        URI_FORMAT_ERROR = 0,
        /**
         * Asset not exists.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        FILE_NOT_EXIST = 1,
        /**
         * The application has read permission when accessing the asset.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        READ_PERMISSION = 2,
        /**
         * The application has no read permission when accessing the asset.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        NO_READ_PERMISSION = 3
    }
    /**
     * MediaLibrary availability.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    interface MediaLibraryAvailability {
        /**
         * MediaLibrary availability status.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        availabilityStatus: AvailabilityStatus;
        /**
         * MediaLibrary unavailability reason.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        unavailabilityReason: string;
    }
    /**
     * Enumeration of medialibrary availability status.
     *
     * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    enum AvailabilityStatus {
        /**
         * MediaLibrary available.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        AVAILABLE = 'available',
        /**
         * MediaLibrary unavailable.
         *
         * @syscap SystemCapability.FileManagement.PhotoAccessHelper.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        UNAVAILABLE = 'unavailable'
    }
}
export default photoAccessHelper;

```
