# @ohos.multimedia.cameraPicker.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (C) 2023 Huawei Device Co., Ltd.
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
/**
 * @file
 * @kit CameraKit
 */
import type Context from './application/Context';
import type camera from './@ohos.multimedia.camera';
/**
 * The module provides APIs for an application to use the system camera to take photos or record videos, depending on
 * the media type specified by the application. The application must call these APIs within a UIAbility. Otherwise, the
 * camera picker cannot be started.
 *
 * @syscap SystemCapability.Multimedia.Camera.Core
 * @atomicservice [since 12]
 * @since 11
 */
declare namespace cameraPicker {
    /**
     * Defines the configuration information about the camera picker.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 12]
     * @since 11
     */
    class PickerProfile {
        /**
         * Camera position.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 12]
         * @since 11
         */
        cameraPosition: camera.CameraPosition;
        /**
         * URI for saving the configuration information. For details about the default value, see
         * [File URI]{@link @ohos.file.fileuri:fileUri.FileUri.constructor}. The **saveUri** parameter is optional. If it is
         * not specified, images and videos are automatically saved to the media library. To prevent them from being saved
         * to the media library, specify a valid file path within your application's sandbox. When you use your own resource
         * path, ensure that the file exists and is writable; otherwise, the save operation fails.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 12]
         * @since 11
         */
        saveUri?: string;
        /**
         * Maximum video duration, in seconds. The default value is **0**, indicating that the maximum video duration is not
         * set.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 12]
         * @since 11
         */
        videoDuration?: number;
    }
    /**
     * Enumerates the media types displayed in the camera picker.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 12]
     * @since 11
     */
    enum PickerMediaType {
        /**
         * Photo mode.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 12]
         * @since 11
         */
        PHOTO = 'photo',
        /**
         * Video mode.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 12]
         * @since 11
         */
        VIDEO = 'video'
    }
    /**
     * Defines the processing result of the camera picker.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 12]
     * @since 11
     */
    class PickerResult {
        /**
         * Result code. The value **0** means that the processing is successful, and **-1** means that the processing fails.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 12]
         * @since 11
         */
        resultCode: number;
        /**
         * URI of the result. If **saveUri** is empty, **resultUri** is a public media path. If **saveUri** is not empty and
         * the application has the write permission on the URI, the value of **resultUri** is the same as that of
         * **saveUri**. If **saveUri** is not empty and the application does not have the write permission on the URI,
         * **resultUri** cannot be obtained.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 12]
         * @since 11
         */
        resultUri: string;
        /**
         * Media type.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 12]
         * @since 11
         */
        mediaType: PickerMediaType;
    }
    /**
     * Starts the camera picker and enters the corresponding mode based on the media type. This API uses a promise to
     * return the result.
     *
     * > **NOTE**
     * >
     * > When an application is running on a widescreen foldable device and the camera picker is launched while the device
     * > is unfolded, switching the device from unfolded to folded will automatically move the camera picker to the
     * > background.
     *
     * @param { Context } context - Application context.
     * @param { Array<PickerMediaType> } mediaTypes - Media type.
     * @param { PickerProfile } pickerProfile - Profile of the camera picker.
     * @returns { Promise<PickerResult> } Promise used to return the processing result (
     *     [PickerResult]{@link cameraPicker.PickerResult}) of the camera picker.
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 12]
     * @since 11
     */
    function pick(context: Context, mediaTypes: Array<PickerMediaType>, pickerProfile: PickerProfile): Promise<PickerResult>;
}
export default cameraPicker;

```
