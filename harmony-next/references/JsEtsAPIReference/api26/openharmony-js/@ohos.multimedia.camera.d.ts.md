# @ohos.multimedia.camera.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (C) 2022 Huawei Device Co., Ltd.
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
import { ErrorCallback, AsyncCallback, Callback } from './@ohos.base';
import type Context from './application/BaseContext';
import image from './@ohos.multimedia.image';
import type colorSpaceManager from './@ohos.graphics.colorSpaceManager';
import photoAccessHelper from './@ohos.file.photoAccessHelper';
/**
 * The module provides a set of camera service APIs for you to easily develop a camera application. The application can
 * access and operate the camera hardware to implement basic operations, such as preview, taking photos, and recording
 * videos. It can also perform more operations, for example, controlling the flash and exposure time, and focusing or
 * adjusting the focus.
 *
 * @syscap SystemCapability.Multimedia.Camera.Core
 * @atomicservice [since 12]
 * @since 10
 */
declare namespace camera {
    /**
     * Obtains a CameraManager instance. This API returns the result synchronously.
     *
     * @param { Context } context - Application context.
     * @returns { CameraManager } CameraManager instance obtained.
     * @throws { BusinessError } 7400101 - Parameter missing or parameter type incorrect.
     * @throws { BusinessError } 7400201 - Camera service fatal error.
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 10
     */
    function getCameraManager(context: Context): CameraManager;
    /**
     * Enumerates the camera statuses.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 10
     */
    enum CameraStatus {
        /**
         * A camera appears.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        CAMERA_STATUS_APPEAR = 0,
        /**
         * The camera disappears.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        CAMERA_STATUS_DISAPPEAR = 1,
        /**
         * The camera is available.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        CAMERA_STATUS_AVAILABLE = 2,
        /**
         * The camera is unavailable.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        CAMERA_STATUS_UNAVAILABLE = 3
    }
    /**
     * Enumerates the fold states available for a fordable device.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 12
     */
    enum FoldStatus {
        /**
         * The device is not foldable.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        NON_FOLDABLE = 0,
        /**
         * The device is fully unfolded.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        EXPANDED = 1,
        /**
         * The device is folded.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        FOLDED = 2
    }
    /**
     * Enumerates the arrangement modes of the sensor color filter.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @stagemodelonly
     * @atomicservice
     * @since 24
     */
    enum SensorColorFilterArrangement {
        /**
         * Blue-green-green-red filter arrangement.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        BGGR = 0,
        /**
         * Green-blue-red-green filter arrangement.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        GBRG = 1,
        /**
         * Green-red-blue-green arrangement mode.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        GRBG = 2,
        /**
         * Red-green-green-blue arrangement mode.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        RGGB = 3
    }
    /**
     * Describes the camera profile.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 10
     */
    interface Profile {
        /**
         * Output format.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        readonly format: CameraFormat;
        /**
         * Resolution.
         *
         * The size setting corresponds to the camera's resolution width and height, rather than the actual dimensions of
         * the output image.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        readonly size: Size;
    }
    /**
     * Describes the frame rate range.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 10
     */
    interface FrameRateRange {
        /**
         * Minimum frame rate, in fps.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        readonly min: number;
        /**
         * Maximum frame rate, in fps.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        readonly max: number;
    }
    /**
     * Describes the video configuration information. It inherits from [Profile]{@link camera.Profile}.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 10
     */
    interface VideoProfile extends Profile {
        /**
         * Frame rate range, in units of frames per second (FPS).
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        readonly frameRateRange: FrameRateRange;
    }
    /**
     * Describes the camera output capability.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 10
     */
    interface CameraOutputCapability {
        /**
         * Supported preview profiles.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        readonly previewProfiles: Array<Profile>;
        /**
         * Supported photo profiles.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        readonly photoProfiles: Array<Profile>;
        /**
         * Supported video profiles.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        readonly videoProfiles: Array<VideoProfile>;
        /**
         * Supported metadata object types.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        readonly supportedMetadataObjectTypes: Array<MetadataObjectType>;
    }
    /**
     * Describes the effect status information of a camera controller.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice
     * @since 20
     */
    interface ControlCenterStatusInfo {
        /**
         * Effect type of the camera controller.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 20
         */
        readonly effectType: ControlCenterEffectType;
        /**
         * Whether the camera controller is activated. **true** if activated, **false** otherwise.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 20
         */
        readonly isActive: boolean;
    }
    /**
     * Enumerates the camera error codes,
     * which are returned when an API call is incorrect or the **on()** API is used to listen for the error status.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 10
     */
    enum CameraErrorCode {
        /**
         * A parameter is missing or the parameter type is incorrect.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        INVALID_ARGUMENT = 7400101,
        /**
         * The operation is not allowed.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        OPERATION_NOT_ALLOWED = 7400102,
        /**
         * The session is not configured.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        SESSION_NOT_CONFIG = 7400103,
        /**
         * The session is not running.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        SESSION_NOT_RUNNING = 7400104,
        /**
         * The session configuration is locked.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        SESSION_CONFIG_LOCKED = 7400105,
        /**
         * The device setting is locked.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        DEVICE_SETTING_LOCKED = 7400106,
        /**
         * The device is already started.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        CONFLICT_CAMERA = 7400107,
        /**
         * The camera is disabled for security reasons.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        DEVICE_DISABLED = 7400108,
        /**
         * The camera is preempted.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        DEVICE_PREEMPTED = 7400109,
        /**
         * The configuration conflicts with the current configuration.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        UNRESOLVED_CONFLICTS_WITH_CURRENT_CONFIGURATIONS = 7400110,
        /**
         * The camera service is abnormal.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        SERVICE_FATAL_ERROR = 7400201
    }
    /**
     * Implements camera management. Before calling any API in CameraManager, you must use
     * [getCameraManager]{@link camera.getCameraManager} to obtain a CameraManager instance.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 10
     */
    interface CameraManager {
        /**
         * Obtains the supported camera devices. This API returns the result synchronously.
         *
         * @returns { Array<CameraDevice> } Array of camera devices supported.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        getSupportedCameras(): Array<CameraDevice>;
        /**
         * Obtains the output capability supported by a camera device. This API returns the result synchronously.
         *
         * @param { CameraDevice } camera - Camera device.
         * @returns { CameraOutputCapability } Camera output capability obtained.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.CameraManager.getSupportedOutputCapability(camera: CameraDevice, mode: SceneMode)
         */
        getSupportedOutputCapability(camera: CameraDevice): CameraOutputCapability;
        /**
         * Obtains the scene modes supported by a camera device. This API returns the result synchronously.
         *
         * @param { CameraDevice } camera - Camera device.
         * @returns { Array<SceneMode> } Array of scene modes supported.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        getSupportedSceneModes(camera: CameraDevice): Array<SceneMode>;
        /**
         * Obtains the output capability supported by a camera device in a given scene mode. This API returns the result
         * synchronously.
         *
         * @param { CameraDevice } camera - Camera device.
         * @param { SceneMode } mode - Scene mode.
         * @returns { CameraOutputCapability } Camera output capability obtained.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        getSupportedOutputCapability(camera: CameraDevice, mode: SceneMode): CameraOutputCapability;
        /**
         * Obtains the complete output capabilities supported by a specified camera in a specified mode, including YUV, HEIF
         * , and HDR.
         *
         * > **NOTE**
         * >
         * > Before using YUV, HEIF, or HDR, you need to explicitly call this method to ensure that the complete output
         * > capabilities are obtained.
         *
         * @param { CameraDevice } camera - Camera device.
         * @param { SceneMode } mode - Scene mode.
         * @returns { CameraOutputCapability } Camera output capability obtained.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        getSupportedFullOutputCapability(camera: CameraDevice, mode: SceneMode): CameraOutputCapability;
        /**
         * Checks whether this camera is muted.
         *
         * @returns { boolean } Check result for whether the camera is muted. **true** if muted, **false** otherwise.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        isCameraMuted(): boolean;
        /**
         * Creates a **CameraInput** instance with the specified **CameraDevice** instance. This API returns the result
         * synchronously.
         * Before calling this API, call [getSupportedCameras]{@link camera.CameraManager.getSupportedCameras} to obtain the
         * list of supported camera devices, select the camera device that meets the requirements based on the actual usage
         * scenario, and then create the **CameraInput** instance.
         *
         * @permission ohos.permission.CAMERA
         * @param { CameraDevice } camera - **CameraDevice** instance, which is obtained through
         *     [getSupportedCameras]{@link camera.CameraManager.getSupportedCameras}.
         * @returns { CameraInput } **CameraInput** instance created. If the operation fails, an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode} is returned.
         * @throws { BusinessError } 7400101 - Parameter missing or parameter type incorrect.
         * @throws { BusinessError } 7400102 - Operation not allowed. [since 12]
         * @throws { BusinessError } 7400201 - Camera service fatal error. [since 12]
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        createCameraInput(camera: CameraDevice): CameraInput;
        /**
         * Creates a **CameraInput** instance with the specified camera position and type. This API returns the result
         * synchronously.
         * Before calling this API, specify the camera position and type based on the usage scenario. For example, open the
         * front camera for the selfie feature
         *
         * @permission ohos.permission.CAMERA
         * @param { CameraPosition } position - Camera position. You need to obtain the supported camera object by calling
         *     [getSupportedCameras]{@link camera.CameraManager.getSupportedCameras} and then obtain the device position
         *     information based on the returned camera object.
         * @param { CameraType } type - Camera type. You need to obtain the supported camera object by calling
         *     [getSupportedCameras]{@link camera.CameraManager.getSupportedCameras} and then obtain the camera type based
         *     on the returned camera object.
         * @returns { CameraInput } **CameraInput** instance created. If the operation fails, an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode} is returned.
         * @throws { BusinessError } 7400101 - Parameter missing or parameter type incorrect.
         * @throws { BusinessError } 7400102 - Operation not allowed. [since 12]
         * @throws { BusinessError } 7400201 - Camera service fatal error. [since 12]
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        createCameraInput(position: CameraPosition, type: CameraType): CameraInput;
        /**
         * Creates a **PreviewOutput** instance. This API returns the result synchronously.
         *
         * @param { Profile } profile - Supported preview profile, which is obtained through
         *     [getSupportedOutputCapability]{@link camera.CameraManager.getSupportedOutputCapability(camera: CameraDevice, mode: SceneMode)}.
         * @param { string } surfaceId - Surface ID, which is obtained from
         *     [XComponent]{@link XComponent} or [ImageReceiver]{@link @ohos.multimedia.image:image.ImageReceiver}.
         * @returns { PreviewOutput } **PreviewOutput** instance created. If the operation fails, an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode} is returned.
         * @throws { BusinessError } 7400101 - Parameter missing or parameter type incorrect.
         * @throws { BusinessError } 7400201 - Camera service fatal error. [since 12]
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        createPreviewOutput(profile: Profile, surfaceId: string): PreviewOutput;
        /**
         * Creates a **PreviewOutput** instance without configuration. This API returns the result synchronously. It must be
         * used with [preconfig]{@link camera.PhotoSession.preconfig}.
         *
         * @param { string } surfaceId - Surface ID, which is obtained from
         *     [XComponent]{@link XComponent} or [ImageReceiver]{@link @ohos.multimedia.image:image.ImageReceiver}.
         * @returns { PreviewOutput } **PreviewOutput** instance created. If the operation fails, an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode} is returned.
         * @throws { BusinessError } 7400101 - Parameter missing or parameter type incorrect.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        createPreviewOutput(surfaceId: string): PreviewOutput;
        /**
         * Creates a **PhotoOutput** instance. This API returns the result synchronously.
         *
         * > **NOTE**
         * >
         * > - This API can only be used to create a **PhotoOutput** object in JPEG format.
         *
         * @param { Profile } profile - Supported photo profile, which is obtained through
         *     [getSupportedOutputCapability]{@link camera.CameraManager.getSupportedOutputCapability(camera: CameraDevice, mode: SceneMode)}.
         * @param { string } surfaceId - Surface ID, which is obtained from
         *     [ImageReceiver]{@link @ohos.multimedia.image:image.ImageReceiver}.
         * @returns { PhotoOutput } **PhotoOutput** instance created. If the operation fails, an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode} is returned.
         * @throws { BusinessError } 7400101 - Parameter missing or parameter type incorrect.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.CameraManager.createPhotoOutput(profile?: Profile)
         */
        createPhotoOutput(profile: Profile, surfaceId: string): PhotoOutput;
        /**
         * Creates a **PhotoOutput** instance. This API returns the result synchronously.
         *
         * @param { Profile } profile - Supported photo profile, which is obtained through
         *     [getSupportedOutputCapability]{@link camera.CameraManager.getSupportedOutputCapability(camera: CameraDevice, mode: SceneMode)}.
         *     <br>In API version 11, this parameter is mandatory. Starting from API version 12, it will overwrite the
         *     preconfigured parameters passed in through [preconfig]{@link camera.PhotoSession.preconfig}.
         * @returns { PhotoOutput } **PhotoOutput** instance created. If the operation fails, an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode} is returned.
         * @throws { BusinessError } 7400101 - Parameter missing or parameter type incorrect.
         * @throws { BusinessError } 7400201 - Camera service fatal error. [since 12]
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        createPhotoOutput(profile?: Profile): PhotoOutput;
        /**
         * Creates a **VideoOutput** instance. This API returns the result synchronously.
         * In video recording mode, if SDR or HDR VIVID is enabled, the camera format and color space must be configured
         * according to the relationships specified in the table below. Configurations that do not match the table will
         * cause issues such as preview exceptions.
         * | SDR/HDR Photo Capture        | CameraFormat             | ColorSpace       |
         * |--------------------|--------------------------|------------------|
         * | SDR                | CAMERA_FORMAT_YUV_420_SP | BT709_LIMIT      |
         * | HDR_VIVID          | CAMERA_FORMAT_YCRCB_P010<br>CAMERA_FORMAT_YCBCR_P010 | BT2020_HLG_LIMIT<br>BT2020_HLG_FULL |
         *
         * @param { VideoProfile } profile - Supported video profile, which is obtained through
         *     [getSupportedOutputCapability]{@link camera.CameraManager.getSupportedOutputCapability(camera: CameraDevice, mode: SceneMode)}.
         * @param { string } surfaceId - Surface ID, which is obtained from [AVRecorder]{@link @ohos.multimedia.media:media}.
         * @returns { VideoOutput } **VideoOutput** instance created. If the operation fails, an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode} is returned.
         * @throws { BusinessError } 7400101 - Parameter missing or parameter type incorrect.
         * @throws { BusinessError } 7400201 - Camera service fatal error. [since 12]
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        createVideoOutput(profile: VideoProfile, surfaceId: string): VideoOutput;
        /**
         * Creates a **VideoOutput** instance without configuration. This API returns the result synchronously. It must be
         * used with [preconfig]{@link camera.VideoSession.preconfig}.
         *
         * @param { string } surfaceId - Surface ID, which is obtained from [AVRecorder]{@link @ohos.multimedia.media:media}.
         * @returns { VideoOutput } **VideoOutput** instance created. If the operation fails, an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode} is returned.
         * @throws { BusinessError } 7400101 - Parameter missing or parameter type incorrect.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        createVideoOutput(surfaceId: string): VideoOutput;
        /**
         * Creates a **MetadataOutput** instance. This API returns the result synchronously.
         *
         * @param { Array<MetadataObjectType> } metadataObjectTypes - Metadata object types, which are obtained through
         *     [getSupportedOutputCapability]{@link camera.CameraManager.getSupportedOutputCapability(camera: CameraDevice, mode: SceneMode)}.
         * @returns { MetadataOutput } **MetadataOutput** instance created. If the operation fails, an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode} is returned.
         * @throws { BusinessError } 7400101 - Parameter missing or parameter type incorrect.
         * @throws { BusinessError } 7400201 - Camera service fatal error. [since 12]
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        createMetadataOutput(metadataObjectTypes: Array<MetadataObjectType>): MetadataOutput;
        /**
         * Creates a **CaptureSession** instance. This API returns the result synchronously.
         *
         * @returns { CaptureSession } **CaptureSession** instance created. If the operation fails, an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode} is returned.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.CameraManager.createSession
         */
        createCaptureSession(): CaptureSession;
        /**
         * Creates a **Session** instance with a given scene mode. This API returns the result synchronously.
         *
         * @param { SceneMode } mode - Scene mode. The API does not take effect if the input parameter is invalid (for
         *     example, the value is out of range, null, or undefined).
         * @returns { T } **Session** instance created. If the operation fails, an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode} is returned.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @throws { BusinessError } 7400101 - Parameter error. Possible causes:
         *     1. Mandatory parameters are left unspecified; 2. Incorrect parameter types;
         *     3. Parameter verification failed. [since 19]
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        createSession<T extends Session>(mode: SceneMode): T;
        /**
         * Subscribes to camera status events. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.
         *
         * @param { 'cameraStatus' } type - Event type. The value is fixed at **'cameraStatus'**. The event can be listened
         *     for when a **CameraManager** instance is obtained. This event is triggered and the corresponding information
         *     is returned only when the camera device is enabled or disabled.
         * @param { AsyncCallback<CameraStatusInfo> } callback - Callback used to return the camera status change.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        on(type: 'cameraStatus', callback: AsyncCallback<CameraStatusInfo>): void;
        /**
         * Unsubscribes from camera status events. This API uses an asynchronous callback to return the result.
         *
         * @param { 'cameraStatus' } type - Event type. The value is fixed at **'cameraStatus'**. The event can be listened
         *     for when a **CameraManager** instance is obtained.
         * @param { AsyncCallback<CameraStatusInfo> } callback - Callback used to return the result. If this parameter is
         *     specified, the subscription to the specified event with the specified callback is canceled. (The callback
         *     object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the
         *     callbacks are canceled.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        off(type: 'cameraStatus', callback?: AsyncCallback<CameraStatusInfo>): void;
        /**
         * Subscribes to fold status change events of the foldable device. This API uses an asynchronous callback to return
         * the result.
         *
         * > **NOTE**
         * >
         * > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.
         *
         * @param { 'foldStatusChange' } type - Event type. The value is fixed at **'foldStatusChange'**. The event is
         *     triggered when the fold state of the foldable device changes.
         * @param { AsyncCallback<FoldStatusInfo> } callback - Callback used to return the fold state information about the
         *     foldable device.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        on(type: 'foldStatusChange', callback: AsyncCallback<FoldStatusInfo>): void;
        /**
         * Unsubscribes from fold state change events of the foldable device.
         *
         * @param { 'foldStatusChange' } type - Event type. The value is fixed at **'foldStatusChange'**. The event is
         *     triggered when the fold state of the foldable device changes.
         * @param { AsyncCallback<FoldStatusInfo> } callback - Callback used to return the fold state information about the
         *     foldable device. If this parameter is specified, the subscription to the specified event with the specified
         *     callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to
         *     the specified event with all the callbacks are canceled.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        off(type: 'foldStatusChange', callback?: AsyncCallback<FoldStatusInfo>): void;
        /**
         * Creates a deferred PreviewOutput instance.
         *
         * @param { Profile } profile - Preview output profile.
         * @returns { PreviewOutput } the PreviewOutput instance.
         * @throws { BusinessError } 7400101 - Parameter missing or parameter type incorrect.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 24
         */
        createDeferredPreviewOutput(profile: Profile): PreviewOutput;
        /**
         * Checks whether the camera device supports the flashlight.
         *
         * @returns { boolean } Check result for the support of the flashlight. **true** if supported, **false** otherwise.
         *     If the API call fails, undefined is returned.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        isTorchSupported(): boolean;
        /**
         * Checks whether a flashlight mode is supported.
         *
         * @param { TorchMode } mode - Flashlight mode. If the input parameter is null or undefined, it is treated as 0 and
         *     the flashlight is turned off.
         * @returns { boolean } Check result for the support of the flashlight mode. **true** if supported, **false**
         *     otherwise. If the API call fails, undefined is returned.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        isTorchModeSupported(mode: TorchMode): boolean;
        /**
         * Obtains the flashlight mode of this camera device.
         *
         * @returns { TorchMode } Flashlight mode.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        getTorchMode(): TorchMode;
        /**
         * Sets the flashlight mode.
         *
         * @param { TorchMode } mode - Flashlight mode. If the input parameter is null or undefined, it is treated as 0 and
         *     the flashlight is turned off.
         * @throws { BusinessError } 7400101 - Parameter missing or parameter type incorrect. [since 11 - 17]
         * @throws { BusinessError } 7400102 - Operation not allowed. [since 12]
         * @throws { BusinessError } 7400201 - Camera service fatal error. [since 12]
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        setTorchMode(mode: TorchMode): void;
        /**
         * Checks whether the device supports flashlight brightness control.
         *
         * @returns { boolean } Whether the device supports flashlight brightness control. Returns **true** if supported,
         *     **false** if not. If the API call fails, undefined is returned.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        isTorchLevelControlSupported(): boolean;
        /**
         * Sets the torch mode to {@link camera.TorchMode.ON} with the specified torch level.
         *
         * @param { number } torchLevel - the specified torch level, the value range is [0.0, 1.0]
         * @throws { BusinessError } 7400102 - Operation not allowed.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        setTorchModeOnWithLevel(torchLevel: number): void;
        /**
         * Subscribes to flashlight status change events. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.
         *
         * @param { 'torchStatusChange' } type - Event type. The value is fixed at **'torchStatusChange'**. The event can be
         *     listened for when a **CameraManager** instance is obtained. Currently, this event is triggered only in the
         *     following scenarios: The flashlight is turned on or turned off, or becomes unavailable or available.
         * @param { AsyncCallback<TorchStatusInfo> } callback - Callback used to return the flashlight status.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        on(type: 'torchStatusChange', callback: AsyncCallback<TorchStatusInfo>): void;
        /**
         * Unsubscribes from flashlight status change events. This API uses an asynchronous callback to return the result.
         *
         * @param { 'torchStatusChange' } type - Event type. The value is fixed at **'torchStatusChange'**. The event can be
         *     listened for when a **CameraManager** instance is obtained.
         * @param { AsyncCallback<TorchStatusInfo> } callback - Callback used to return the result. If this parameter is
         *     specified, the subscription to the specified event with the specified callback is canceled. (The callback
         *     object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the
         *     callbacks are canceled.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        off(type: 'torchStatusChange', callback?: AsyncCallback<TorchStatusInfo>): void;
        /**
         * Obtains the specified camera based on the camera position and type.
         * Obtains the camera lens of the specified [CameraPosition]{@link camera.CameraPosition}
         * and [CameraType]{@link camera.CameraType}. If the returned result is undefined, the
         * camera lens is not found on the current device.
         *
         * @param { CameraPosition } position - Camera position.
         * @param { CameraType } type - Camera type.
         * @returns { CameraDevice } Camera obtained.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 18
         */
        getCameraDevice(position: CameraPosition, type: CameraType): CameraDevice;
        /**
         * Obtains the concurrency information of the specified cameras. If the return value is an empty array, concurrency
         * is not supported.
         *
         * @param { Array<CameraDevice> } cameras - Array of **CameraDevice** objects. You are advised to use the front and
         *     rear cameras obtained by calling [getCameraDevice]{@link camera.CameraManager.getCameraDevice}.
         * @returns { Array<CameraConcurrentInfo> } Array of concurrency information corresponding to the provided
         *     CameraDevice objects, with a one-to-one mapping.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 18
         */
        getCameraConcurrentInfos(cameras: Array<CameraDevice>): Array<CameraConcurrentInfo>;
        /**
         * Obtains the list of cameras that meet the search criteria based on the camera position, camera types, and
         * connection type.
         *
         * @param { CameraPosition } position - Camera position.
         * @param { Array<CameraType> } types - Array of camera types.
         * @param { ConnectionType } connectType - Camera connection type.
         * @returns { Array<CameraDevice> } Array of cameras that meet the search criteria.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 23
         */
        getCameraDevices(position: CameraPosition, types: Array<CameraType>, connectType: ConnectionType): Array<CameraDevice>;
    }
    /**
     * Describes the flashlight status information.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 11
     */
    interface TorchStatusInfo {
        /**
         * Whether the flashlight is available. **true** if available, **false** otherwise.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        readonly isTorchAvailable: boolean;
        /**
         * Whether the flashlight is activated. **true** if activated, **false** otherwise.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        readonly isTorchActive: boolean;
        /**
         * Flashlight brightness level. The value range is [0, 1]. A larger value indicates a greater luminance.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        readonly torchLevel: number;
    }
    /**
     * Enumerates the flashlight modes.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 11
     */
    enum TorchMode {
        /**
         * The flashlight is off.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        OFF = 0,
        /**
         * The flashlight is on.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        ON = 1,
        /**
         * The system automatically adjusts the flashlight brightness according to the environment.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        AUTO = 2
    }
    /**
     * Describes the camera status information.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 10
     */
    interface CameraStatusInfo {
        /**
         * Camera device.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        camera: CameraDevice;
        /**
         * Camera status.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        status: CameraStatus;
    }
    /**
     * Describes the fold state information about a foldable device.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 12
     */
    interface FoldStatusInfo {
        /**
         * List of cameras supported in the current fold state.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        readonly supportedCameras: Array<CameraDevice>;
        /**
         * Fold state.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        readonly foldStatus: FoldStatus;
    }
    /**
     * Enumerates the camera positions.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 12]
     * @since 10
     */
    enum CameraPosition {
        /**
         * A camera that does not have a fixed orientation relative to the device screen.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 12]
         * @since 10
         */
        CAMERA_POSITION_UNSPECIFIED = 0,
        /**
         * Rear camera.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 12]
         * @since 10
         */
        CAMERA_POSITION_BACK = 1,
        /**
         * Front camera.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 12]
         * @since 10
         */
        CAMERA_POSITION_FRONT = 2,
        /**
         * Folded camera.
         *
         * This API is supported since API version 11 and deprecated since API version 12.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 12]
         * @since 11
         * @deprecated since 12
         * @useinstead null
         * @useinstead null
         */
        CAMERA_POSITION_FOLD_INNER = 3
    }
    /**
     * Enumerates the camera types.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 10
     */
    enum CameraType {
        /**
         * Default camera type.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        CAMERA_TYPE_DEFAULT = 0,
        /**
         * Wide camera.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        CAMERA_TYPE_WIDE_ANGLE = 1,
        /**
         * Ultra-wide camera.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        CAMERA_TYPE_ULTRA_WIDE = 2,
        /**
         * Telephoto camera.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        CAMERA_TYPE_TELEPHOTO = 3,
        /**
         * Camera with depth of field information.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        CAMERA_TYPE_TRUE_DEPTH = 4
    }
    /**
     * Enumerates the camera connection types.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 10
     */
    enum ConnectionType {
        /**
         * Built-in camera.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        CAMERA_CONNECTION_BUILT_IN = 0,
        /**
         * Camera connected using USB.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        CAMERA_CONNECTION_USB_PLUGIN = 1,
        /**
         * Remote camera.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        CAMERA_CONNECTION_REMOTE = 2
    }
    /**
     * Enumerates the remote camera types.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 15
     */
    enum HostDeviceType {
        /**
         * Unknown type.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 15
         */
        UNKNOWN_TYPE = 0,
        /**
         * Mobile phone.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 15
         */
        PHONE = 0x0E,
        /**
         * Tablet.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 15
         */
        TABLET = 0x11
    }
    /**
     * Describes the camera device information.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 10
     */
    interface CameraDevice {
        /**
         * Camera ID.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        readonly cameraId: string;
        /**
         * Camera position.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        readonly cameraPosition: CameraPosition;
        /**
         * Camera type.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        readonly cameraType: CameraType;
        /**
         * Camera connection type.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        readonly connectionType: ConnectionType;
        /**
         * Remote device name. If no remote device is available, an empty value is returned.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 15
         */
        readonly hostDeviceName: string;
        /**
         * Remote device type.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 15
         */
        readonly hostDeviceType: HostDeviceType;
        /**
         * Camera installation angle, which does not change as the screen rotates. The value range is [0, 360], in degrees.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        readonly cameraOrientation: number;
        /**
         * Equivalent focal length of the camera lens.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 24
         */
        readonly lensEquivalentFocalLength?: Array<number>;
        /**
         * Whether a camera is a logical camera (consisting of multiple physical cameras). **true** if the camera is a
         * logical camera, **false** otherwise.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        readonly isLogicalCamera?: boolean;
        /**
         * List of physical cameras that form the logical camera.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        readonly constituentCameraDevices?: Array<CameraDevice>;
        /**
         * Actual focal length of the lens.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        readonly lensFocalLength?: number;
        /**
         * Minimum focus distance of the camera.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        readonly minimumFocusDistance?: number;
        /**
         * Array of lens distortion parameters.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        readonly lensDistortion?: Array<number>;
        /**
         * Array of lens internal parameter calibration parameters.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        readonly lensIntrinsicCalibration?: Array<number>;
        /**
         * Physical dimensions (width and height) of the sensor.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        readonly sensorPhysicalSize?: Array<number>;
        /**
         * Pixel array dimensions (width and height, in pixels) of the sensor.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        readonly sensorPixelArraySize?: Array<number>;
        /**
         * Arrangement mode of the sensor color filter.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        readonly sensorColorFilterArrangement?: SensorColorFilterArrangement;
        /**
         * Automotive camera position attribute.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        readonly automotiveCameraPosition?: AutomotiveCameraPosition;
    }
    /**
     * Describes the image dimensions.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 10
     */
    interface Size {
        /**
         * Image height, in pixels.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        height: number;
        /**
         * Image width, in pixels.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        width: number;
    }
    /**
     * Describes the point coordinates, which are used for focus and exposure configuration.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 10
     */
    interface Point {
        /**
         * X coordinate of a point.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        x: number;
        /**
         * Y coordinate of a point.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        y: number;
    }
    /**
     * Defines the camera input object.
     * It provides camera device information used in [Session]{@link camera.Session}.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 10
     */
    interface CameraInput {
        /**
         * Opens this camera device. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the camera device is opened
         *     successfully, **err** is **undefined**; otherwise, **err** is an error object with an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode}.
         * @throws { BusinessError } 7400107 - Can not use camera cause of conflict.
         * @throws { BusinessError } 7400108 - Camera disabled cause of security reason.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        open(callback: AsyncCallback<void>): void;
        /**
         * Opens this camera device. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 7400102 - Operation not allowed.
         * @throws { BusinessError } 7400107 - Can not use camera cause of conflict.
         * @throws { BusinessError } 7400108 - Camera disabled cause of security reason.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        open(): Promise<void>;
        /**
         * Opens this camera device. This API uses a promise to return the result.
         *
         * @param { boolean } isSecureEnabled - Whether to open the camera device in secure mode. **true** to open in secure
         *     mode, **false** otherwise. If the operation fails, an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode} is returned.
         * @returns { Promise<bigint> } Promise used to return the handle to the camera device in secure mode.
         * @throws { BusinessError } 7400107 - Can not use camera cause of conflict.
         * @throws { BusinessError } 7400108 - Camera disabled cause of security reason.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        open(isSecureEnabled: boolean): Promise<bigint>;
        /**
         * Closes this camera device. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the camera device is closed
         *     successfully, **err** is **undefined**. Otherwise, **err** is an error object with an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode}.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        close(callback: AsyncCallback<void>): void;
        /**
         * Closes this camera device. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        close(): Promise<void>;
        /**
         * Subscribes to CameraInput error events. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.
         *
         * @param { 'error' } type - Event type. The value is fixed at **'error'**. The event can be listened for when a
         *     CameraInput instance is created. This event is triggered and the result is returned when an error occurs on
         *     the camera device. For example, if the camera device is unavailable or a conflict occurs, the error
         *     information is returned.
         * @param { CameraDevice } camera - Camera device.
         * @param { ErrorCallback } callback - Callback used to return an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode}.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        on(type: 'error', camera: CameraDevice, callback: ErrorCallback): void;
        /**
         * Unsubscribes from CameraInput error events.
         *
         * @param { 'error' } type - Event type. The value is fixed at **'error'**. The event can be listened for when a
         *     CameraInput instance is created. This event is triggered and the result is returned when an error occurs on
         *     the camera device. For example, if the camera device is unavailable or a conflict occurs, the error
         *     information is returned.
         * @param { CameraDevice } camera - Camera device.
         * @param { ErrorCallback } callback - Callback used to return the result. If this parameter is specified, only the
         *     corresponding callback will be unregistered (the callback object cannot be an anonymous function); otherwise,
         *     all registered callbacks will be unregistered.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        off(type: 'error', camera: CameraDevice, callback?: ErrorCallback): void;
        /**
         * Subscribes to **CameraInput** occlusion events. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.
         *
         * @param { 'cameraOcclusionDetection' } type - Event type. The value is fixed at **'cameraOcclusionDetection'**.
         *     The event can be listened for when a **CameraInput** instance is created. It is triggered when the occlusion
         *     status of the camera lens changes, and the occlusion status is returned.
         * @param { AsyncCallback<CameraOcclusionDetectionResult> } callback - Callback used to return the occlusion status.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 23
         */
        on(type: 'cameraOcclusionDetection', callback: AsyncCallback<CameraOcclusionDetectionResult>): void;
        /**
         * Unsubscribes from **CameraInput** occlusion events. This API uses an asynchronous callback to return the result.
         *
         * @param { 'cameraOcclusionDetection' } type - Event type. The value is fixed at **'cameraOcclusionDetection'**.
         *     The event can be listened for when a **CameraInput** instance is created. It is triggered when the occlusion
         *     status of the camera lens changes, and the occlusion status is returned.
         * @param { AsyncCallback<CameraOcclusionDetectionResult> } callback - Callback used to return the result. If this
         *     parameter is specified, the subscription to the specified event with the specified callback is canceled. (The
         *     callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with
         *     all the callbacks are canceled.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 23
         */
        off(type: 'cameraOcclusionDetection', callback?: AsyncCallback<CameraOcclusionDetectionResult>): void;
        /**
         * Checks whether the physical camera orientation is adjustable in different fold states of the device.
         *
         * @returns { boolean } Check result for whether the physical camera orientation is adjustable. **true** if
         *     adjustable, **false** otherwise. If the API call fails, undefined is returned.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 22
         */
        isPhysicalCameraOrientationVariable(): boolean;
        /**
         * Obtains the physical camera orientation in the current fold state of the device.
         *
         * @returns { number } Physical camera orientation. The unit is degree. The value range is [0, 360].
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 22
         */
        getPhysicalCameraOrientation(): number;
        /**
         * Enables or disables the use of the physical camera orientation.
         *
         * @param { boolean } isUsed - Whether to enable the use of the physical camera orientation. **true** to enable,
         *     **false** otherwise.
         * @throws { BusinessError } 7400102 - Operation not allowed.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 22
         */
        usePhysicalCameraOrientation(isUsed: boolean): void;
        /**
         * Opens the camera with the specified concurrency type. This API uses a promise to return the result.
         *
         * @param { CameraConcurrentType } type - Concurrency type. If the API fails to be called, an error code is
         *     returned.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 7400102 - Operation not allowed.
         * @throws { BusinessError } 7400107 - Can not use camera cause of conflict.
         * @throws { BusinessError } 7400108 - Camera disabled cause of security reason.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 18
         */
        open(type: CameraConcurrentType): Promise<void>;
    }
    /**
     * Enumerates the camera scene modes.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 11
     */
    enum SceneMode {
        /**
         * Normal photo mode. For details, see [PhotoSession]{@link camera.PhotoSession}.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        NORMAL_PHOTO = 1,
        /**
         * Normal record mode. For details, see [VideoSession]{@link camera.VideoSession}.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        NORMAL_VIDEO = 2,
        /**
         * Secure mode. For details, see [SecureSession]{@link camera.SecureSession}.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        SECURE_PHOTO = 12
    }
    /**
     * Enumerates the camera output formats.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 10
     */
    enum CameraFormat {
        /**
         * RGBA_8888 image.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        CAMERA_FORMAT_RGBA_8888 = 3,
        /**
         * Digital Negative (DNG) image.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 24
         */
        CAMERA_FORMAT_DNG = 4,
        /**
         * YUV_420_SP image, which corresponds to the NV21 image.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        CAMERA_FORMAT_YUV_420_SP = 1003,
        /**
         * JPEG image.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        CAMERA_FORMAT_JPEG = 2000,
        /**
         * YCBCR_P010 image.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        CAMERA_FORMAT_YCBCR_P010,
        /**
         * YCRCB_P010 image.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        CAMERA_FORMAT_YCRCB_P010 = 2002,
        /**
         * HEIF image.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 13
         */
        CAMERA_FORMAT_HEIC = 2003,
        /**
         * Enhanced DNG image format.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 26.0.0
         */
        CAMERA_FORMAT_DNG_XDRAW = 5
    }
    /**
     * Enumerates the flash modes.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 10
     */
    enum FlashMode {
        /**
         * The flash is off.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        FLASH_MODE_CLOSE = 0,
        /**
         * The flash is on.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        FLASH_MODE_OPEN = 1,
        /**
         * The flash mode is auto, indicating that the flash fires automatically depending on the photo capture conditions.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        FLASH_MODE_AUTO = 2,
        /**
         * The flash is steady on.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        FLASH_MODE_ALWAYS_OPEN = 3
    }
    /**
     * Provides APIs to obtain the flash information of a camera device, including whether the LCD flash is supported.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 12
     */
    interface FlashQuery {
        /**
         * Checks whether the camera device has flash.
         *
         * @returns { boolean } Check result for whether the camera device has flash. **true** if it has flash, **false**
         *     otherwise. If the operation fails, an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode} is returned.
         * @throws { BusinessError } 7400103 - Session not config, only throw in session usage.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        hasFlash(): boolean;
        /**
         * Checks whether a flash mode is supported.
         *
         * @param { FlashMode } flashMode - Flash mode. If the input parameter is null or undefined, it is treated as 0 and
         *     the flash is turned off.
         * @returns { boolean } Check result for the support of the flash mode. **true** if supported, **false** otherwise.
         *     If the operation fails, undefined is returned and an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode} is thrown.
         * @throws { BusinessError } 7400103 - Session not config, only throw in session usage.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        isFlashModeSupported(flashMode: FlashMode): boolean;
    }
    /**
     * Flash extends [FlashQuery]{@link camera.FlashQuery}
     * Provides APIs related to the flash.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 11
     */
    interface Flash extends FlashQuery {
        /**
         * Obtains the flash mode in use.
         *
         * @returns { FlashMode } Flash mode obtained. If the operation fails, undefined is returned and an error code
         *     defined in [CameraErrorCode]{@link camera.CameraErrorCode} is thrown.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        getFlashMode(): FlashMode;
        /**
         * Sets a flash mode.
         *
         * Before the setting, do the following checks:
         *
         * 1. Use [hasFlash]{@link camera.FlashQuery.hasFlash} to check whether the camera device has flash.
         * 2. Use [isFlashModeSupported]{@link camera.FlashQuery.isFlashModeSupported} to check whether the camera device supports the flash mode.
         *
         * @param { FlashMode } flashMode - Flash mode. If the input parameter is null or undefined, it is treated as 0 and
         *     the flash is turned off.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        setFlashMode(flashMode: FlashMode): void;
        /**
         * Subscribes flash state change event callback.
         *
         * @param { Callback<FlashState> } callback - Callback used to get the flash state change.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        onFlashStateChange(callback: Callback<FlashState>): void;
        /**
         * Unsubscribes flash state change event callback.
         *
         * @param { Callback<FlashState> } [callback] - Callback used to get the flash state change.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        offFlashStateChange(callback?: Callback<FlashState>): void;
    }
    /**
     * Enumerates the flash states.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @stagemodelonly
     * @atomicservice
     * @since 24
     */
    enum FlashState {
        /**
         * The flash is unavailable. This is the default value.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        FLASH_STATE_UNAVAILABLE = 0,
        /**
         * The flash is available.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        FLASH_STATE_READY = 1,
        /**
         * The flash is turned on.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        FLASH_STATE_FLASHING = 2
    }
    /**
     * Enumerates the exposure modes.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 10
     */
    enum ExposureMode {
        /**
         * Unspecified exposure.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        EXPOSURE_MODE_UNSPECIFIED = -1,
        /**
         * Exposure locked. The metering point cannot be set.
         *
         * After this mode is used, the exposure will be locked by default for each photo capture.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        EXPOSURE_MODE_LOCKED = 0,
        /**
         * Auto exposure. The metering point can be set by calling
         * [AutoExposure.setMeteringPoint]{@link camera.AutoExposure.setMeteringPoint}.
         *
         * After this mode is used, it takes effect only for the first photo capture.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        EXPOSURE_MODE_AUTO = 1,
        /**
         * Continuous auto exposure. The metering point cannot be set.
         *
         * After this mode is used, the camera system automatically adjusts the exposure based on the environment changes
         * each time.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        EXPOSURE_MODE_CONTINUOUS_AUTO = 2,
        /**
         * Manual exposure mode.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 24
         */
        EXPOSURE_MODE_MANUAL = 3
    }
    /**
     * Enumerates the exposure states.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    enum ExposureState {
        /**
         * Exposure is being scanned.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        EXPOSURE_STATE_SCAN = 0,
        /**
         * Exposure is converged.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        EXPOSURE_STATE_CONVERGED = 1
    }
    /**
     * Enumerates the exposure metering modes.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice
     * @since 24
     */
    enum ExposureMeteringMode {
        /**
         * Matrix metering mode. A wide area of the screen is selected, which is ideal for shooting natural landscapes.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 24
         */
        MATRIX = 0,
        /**
         * Center-weighted metering mode. Metering is performed on the entire image, with the center allocated with the
         * maximum weight, which is ideal for shooting portraits.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 24
         */
        CENTER = 1,
        /**
         * Spot metering mode. Metering is performed around 2.5% of the metering points, focusing on the light in a specific
         * small area, such as the eyes of the subject.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 24
         */
        SPOT = 2
    }
    /**
     * AutoExposureQuery provides APIs to query the automatic exposure feature of a camera device.
     *  >
     * > - In this version, a compatibility change was made that preserved the initial version information of inner
     * > elements. As a result, you might see outer element's @since version number being higher than that of the inner
     * > elements. However, this discrepancy does not affect the functionality of the interface.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 12
     */
    interface AutoExposureQuery {
        /**
         * Checks whether an exposure mode is supported.
         *
         * @param { ExposureMode } aeMode - Exposure mode. If the input parameter is null or undefined, it is treated as 0
         *     and exposure is locked.
         * @returns { boolean } Check result for the support of the exposure mode. **true** if supported, **false**
         *     otherwise. If the operation fails, undefined is returned and an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode} is thrown.
         * @throws { BusinessError } 7400103 - Session not config, only throw in session usage.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        isExposureModeSupported(aeMode: ExposureMode): boolean;
        /**
         * Obtains the exposure compensation values of the camera device.
         *
         * @returns { Array<number> } Array of compensation values. If the operation fails, an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode} is returned.
         * @throws { BusinessError } 7400103 - Session not config, only throw in session usage.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        getExposureBiasRange(): Array<number>;
        /**
         * Checks whether a specified exposure metering mode is supported.
         *
         * @param { ExposureMeteringMode } aeMeteringMode - Exposure metering mode
         * @returns { boolean } Is the exposure metering mode supported.
         * @throws { BusinessError } 7400103 - Session not config, only throw in session usage.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 24
         */
        isExposureMeteringModeSupported(aeMeteringMode: ExposureMeteringMode): boolean;
    }
    /**
     * AutoExposure inherits from [AutoExposureQuery]{@link camera.AutoExposureQuery}.
     * It provides APIs related to auto exposure.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 11
     */
    interface AutoExposure extends AutoExposureQuery {
        /**
         * Obtains the exposure mode in use.
         *
         * > **NOTE**
         * >
         * > This API directly returns an invalid value if you have not set the exposure mode using
         * > [setExposureMode]{@link camera.AutoExposure.setExposureMode}.
         *
         * @returns { ExposureMode } Exposure mode obtained. If the operation fails, undefined is returned and an error code
         *     defined in [CameraErrorCode]{@link camera.CameraErrorCode} is thrown.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        getExposureMode(): ExposureMode;
        /**
         * Sets an exposure mode. Before the setting, call
         * [isExposureModeSupported]{@link camera.AutoExposureQuery.isExposureModeSupported} to
         * check whether the exposure mode is supported.
         *
         * @param { ExposureMode } aeMode - Exposure mode. If the input parameter is null or undefined, it is treated as 0
         *     and exposure is locked.
         * @throws { BusinessError } 7400103 - Session not config.
         * @throws { BusinessError } 7400102 - Operation not allowed. [since 19]
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        setExposureMode(aeMode: ExposureMode): void;
        /**
         * Obtains the metering point of the camera device.
         *
         * @returns { Point } Metering point obtained. If the operation fails, an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode} is returned.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        getMeteringPoint(): Point;
        /**
         * Sets the metering point, which is the center point of the metering rectangle. The metering point must be in the
         * coordinate system (0-1), where the top-left corner is {0, 0} and the bottom-right corner is {1, 1}.
         *
         * The coordinate system is based on the horizontal device direction with the device's charging port on the right.
         * If the layout of the preview screen of an application is based on the vertical direction with the charging port
         * on the lower side, the layout width and height are {w, h}, and the touch point is {x, y}, then the coordinate
         * point after conversion is {y/h, 1-x/w}.
         *
         * @param { Point } point - Metering point. The value range of x and y must be within [0, 1]. If a value less than 0
         *     is passed, the value **0** is used. If a value greater than **1** is passed, the value **1** is used.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        setMeteringPoint(point: Point): void;
        /**
         * Sets an exposure compensation value (EV).
         * Before the setting, you are advised to use
         * [getExposureBiasRange]{@link camera.AutoExposureQuery.getExposureBiasRange} to obtain the
         * supported values.
         *
         * @param { number } exposureBias - EV. The supported EV range can be obtained by calling
         *     [getExposureBiasRange]{@link camera.AutoExposureQuery.getExposureBiasRange}. If the
         *     value passed is not within the supported range, the nearest critical point is used.<br>Exposure compensation
         *     is adjusted in steps, and the step size may vary across devices due to hardware differences. For example, if
         *     the step size is 0.5, setting a value of 1.2 would result in an actual effective exposure compensation value
         *     of 1.0.<br>If the operation fails, an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode} is returned.
         * @throws { BusinessError } 7400103 - Session not config.
         * @throws { BusinessError } 7400102 - Operation not allowed. [since 12]
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        setExposureBias(exposureBias: number): void;
        /**
         * Obtains the exposure value in use.
         *
         * @returns { number } Exposure value obtained. There is a step for EV. For example, if the step is 0.5 and this
         *     parameter is set to 1.2, the EV that takes effect is 1.0.
         *     <br>If the operation fails, an error code defined in [CameraErrorCode]{@link camera.CameraErrorCode} is
         *     returned.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        getExposureValue(): number;
        /**
         * Gets current exposure metering mode.
         *
         * @returns { ExposureMeteringMode } The current exposure metering mode.
         * @throws { BusinessError } 7400103 - Session not config, only throw in session usage.
         * @throws { BusinessError } 7400102 - Operation not allowed, the inputDevice or the session is abnormal.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 24
         */
        getExposureMeteringMode(): ExposureMeteringMode;
        /**
         * Sets exposure metering mode.
         *
         * @param { ExposureMeteringMode } aeMeteringMode - Exposure metering mode.
         * @throws { BusinessError } 7400103 - Session not config, only throw in session usage.
         * @throws { BusinessError } 7400102 - Operation not allowed, the inputDevice or the session is abnormal.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 24
         */
        setExposureMeteringMode(aeMeteringMode: ExposureMeteringMode): void;
        /**
        * Registers a callback to listen for exposure state changes.
        *
        * @param { Callback<ExposureState> } callback - Callback used to get the exposure state change.
        * @syscap SystemCapability.Multimedia.Camera.Core
        * @stagemodelonly
        * @atomicservice
        * @since 26.0.0
        */
        onExposureStateChange(callback: Callback<ExposureState>): void;
        /**
        * Unregisters the callback used to listen for exposure state changes.
        *
        * @param { Callback<ExposureState> } [callback] - Callback used to get the exposure state change.
        * @syscap SystemCapability.Multimedia.Camera.Core
        * @stagemodelonly
        * @atomicservice
        * @since 26.0.0
        */
        offExposureStateChange(callback?: Callback<ExposureState>): void;
    }
    /**
     * Enumerates the focus modes.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 10
     */
    enum FocusMode {
        /**
         * Manual focus. The focal length of the camera can be manually set to change the focus position. However, the focal
         * point cannot be set.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        FOCUS_MODE_MANUAL = 0,
        /**
         * Continuous auto focus. The focal point cannot be set.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        FOCUS_MODE_CONTINUOUS_AUTO = 1,
        /**
         * The flash mode is auto, indicating that the flash fires automatically depending on the photo capture conditions.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        FOCUS_MODE_AUTO = 2,
        /**
         * Focus locked. The focal point cannot be set.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        FOCUS_MODE_LOCKED = 3
    }
    /**
     * Enumerates the focus states.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 10
     */
    enum FocusState {
        /**
         * Focusing.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        FOCUS_STATE_SCAN = 0,
        /**
         * Focused.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        FOCUS_STATE_FOCUSED = 1,
        /**
         * Unfocused.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        FOCUS_STATE_UNFOCUSED = 2
    }
    /**
     * Provides the API to check whether the focus assist is supported.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 12
     */
    interface FocusQuery {
        /**
         * Checks whether a focus mode is supported.
         *
         * @param { FocusMode } afMode - Focus mode. If the input parameter is null or undefined, it is treated as 0 and
         *     manual focus is used.
         * @returns { boolean } Check result for the support of the focus mode. **true** if supported, **false** otherwise.
         *     If the operation fails, undefined is returned and an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode} is thrown.
         * @throws { BusinessError } 7400103 - Session not config, only throw in session usage.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        isFocusModeSupported(afMode: FocusMode): boolean;
        /**
         * Checks whether lock focus tracking is supported.
         *
         * @returns { boolean } Is the lock focus tracking supported.
         * @throws { BusinessError } 7400103 - Session not config, only throw in session usage.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        isLockFocusTrackingSupported(): boolean;
    }
    /**
     * Focus extends [FocusQuery]{@link camera.FocusQuery}
     * Provides APIs to obtain and set the camera focus mode and focus position.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 11
     */
    interface Focus extends FocusQuery {
        /**
         * Obtains the focus mode in use.
         *
         * @returns { FocusMode } Focus mode obtained. If the operation fails, undefined is returned and an error code
         *     defined in [CameraErrorCode]{@link camera.CameraErrorCode} is thrown.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        getFocusMode(): FocusMode;
        /**
         * Sets a focus mode.
         * Before the setting, call
         * [isFocusModeSupported]{@link camera.FocusQuery.isFocusModeSupported} to check whether the
         * focus mode is supported.
         *
         * @param { FocusMode } afMode - Focus mode. If the input parameter is null or undefined, it is treated as 0 and
         *     manual focus is used.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        setFocusMode(afMode: FocusMode): void;
        /**
         * Sets the focal point. The focal point must be in the coordinate system (0-1), where the top-left corner is {0, 0}
         * and the bottom-right corner is {1, 1}.
         *
         * The coordinate system is based on the horizontal device direction with the device's charging port on the right.
         * If the layout of the preview screen of an application is based on the vertical direction with the charging port
         * on the lower side, the layout width and height are {w, h}, and the touch point is {x, y}, then the coordinate
         * point after conversion is {y/h, 1-x/w}.
         *
         * @param { Point } point - Focal point. The value range of x and y must be within [0, 1]. If a value less than 0 is
         *     passed, the value **0** is used. If a value greater than **1** is passed, the value **1** is used.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        setFocusPoint(point: Point): void;
        /**
         * Obtains the focal point in use.
         *
         * @returns { Point } Focal point obtained. If the operation fails, an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode} is returned.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        getFocusPoint(): Point;
        /**
         * Obtains the focal length in use.
         *
         * @returns { number } Focal length, in units of mm. If the operation fails, an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode} is returned.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        getFocalLength(): number;
        /**
         * Lock focus tracking.
         *
         * @param { Point } focusPoint - lock focus tracking point.
         * @throws { BusinessError } 7400103 - Session not config, only throw in session usage.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        lockFocusTracking(focusPoint: Point): void;
        /**
         * Unlock focus tracking.
         *
         * @throws { BusinessError } 7400103 - Session not config, only throw in session usage.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        unlockFocusTracking(): void;
    }
    /**
     * Manual Focus Query object.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice
     * @since 24
     */
    interface ManualFocusQuery {
        /**
         * Checks whether a focus distance is supported.
         *
         * @returns { boolean } Is focus distance supported.
         * @throws { BusinessError } 7400103 - Session not config, only throw in session usage.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 24
         */
        isFocusDistanceSupported(): boolean;
    }
    /**
     * ManualFocus object.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice
     * @since 24
     */
    interface ManualFocus extends ManualFocusQuery {
        /**
         * Gets current focus distance, ranging from 0.0 to 1.0, with 0.0 being shortest
         * distance at which the lens can focus and 1.0 the furthest. The default value is 1.0.
         *
         * @returns { number } The current focus distance.
         * @throws { BusinessError } 7400103 - Session not config.
         * @throws { BusinessError } 7400102 - Operation not allowed, the inputDevice or the session is abnormal.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 24
         */
        getFocusDistance(): number;
        /**
         * Sets focus distance. Possible distance values range from 0.0 to 1.0, with 0.0 being shortest
         * distance at which the lens can focus and 1.0 the furthest. The default value is 1.0.
         *
         * @param { number } distance - Focus distance.
         * @throws { BusinessError } 7400103 - Session not config.
         * @throws { BusinessError } 7400102 - Operation not allowed, the inputDevice or the session is abnormal.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 24
         */
        setFocusDistance(distance: number): void;
    }
    /**
     * Enumerates the white balance modes.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice
     * @since 20
     */
    enum WhiteBalanceMode {
        /**
         * Automatic.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 20
         */
        AUTO = 0,
        /**
         * Cloudy.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 20
         */
        CLOUDY = 1,
        /**
         * Incandescent light.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 20
         */
        INCANDESCENT = 2,
        /**
         * Fluorescence light.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 20
         */
        FLUORESCENT = 3,
        /**
         * Daylight.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 20
         */
        DAYLIGHT = 4,
        /**
         * Manual.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 20
         */
        MANUAL = 5,
        /**
         * Locked.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 20
         */
        LOCKED = 6
    }
    /**
     * WhiteBalanceQuery provides APIs to check whether a white balance mode is supported and obtain the white balance
     * mode range supported.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice
     * @since 20
     */
    interface WhiteBalanceQuery {
        /**
         * Checks whether a white balance mode is supported.
         *
         * @param { WhiteBalanceMode } mode - White balance mode.
         * @returns { boolean } Check result for the support of the white balance mode. **true** if supported, **false**
         *     otherwise. If the API call fails, undefined is returned.
         * @throws { BusinessError } 7400101 - Parameter missing or parameter type incorrect.
         * @throws { BusinessError } 7400103 - Session not config, only throw in session usage.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 20
         */
        isWhiteBalanceModeSupported(mode: WhiteBalanceMode): boolean;
        /**
         * Obtains the range of white balance values in manual white balance mode.
         *
         * @returns { Array<number> } Range of white balance values, for example, [2800, ...,10000], in units of K (Kelvin).
         *     The actual value depends on the bottom-layer capability. If the API call fails, undefined is returned.
         * @throws { BusinessError } 7400103 - Session not config, only throw in session usage.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 20
         */
        getWhiteBalanceRange(): Array<number>;
        /**
         * Query the color tint range.
         *
         * @returns { Array<number> } The array of color tint range.
         * @throws { BusinessError } 7400103 - Session not config, only throw in session usage.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        getColorTintRange(): Array<number>;
    }
    /**
     * **WhiteBalance** inherits from [WhiteBalanceQuery]{@link camera.WhiteBalanceQuery}.
     * It provides APIs to process white balance, including obtaining and setting the white balance mode and white balance
     * value.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice
     * @since 20
     */
    interface WhiteBalance extends WhiteBalanceQuery {
        /**
         * Obtains the white balance mode in use.
         *
         * @returns { WhiteBalanceMode } White balance mode in use. If the API call fails, undefined is returned.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 20
         */
        getWhiteBalanceMode(): WhiteBalanceMode;
        /**
         * Sets a white balance mode. Before the setting, run
         * [isWhiteBalanceModeSupported]{@link camera.WhiteBalanceQuery.isWhiteBalanceModeSupported}
         * to check whether the device supports the specified white balance mode.
         *
         * @param { WhiteBalanceMode } mode - White balance mode.
         * @throws { BusinessError } 7400101 - Parameter missing or parameter type incorrect.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 20
         */
        setWhiteBalanceMode(mode: WhiteBalanceMode): void;
        /**
         * Obtains the current white balance value.
         *
         * @returns { number } White balance value, in units of K (Kelvin)
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 20
         */
        getWhiteBalance(): number;
        /**
         * Sets a white balance value.
         * Before the setting, run
         * [getWhiteBalanceRange]{@link camera.WhiteBalanceQuery.getWhiteBalanceRange} to check the
         * white balance value range supported by the device.
         *
         * @param { number } whiteBalance - White balance value, in units of K (Kelvin)
         * @throws { BusinessError } 7400101 - Parameter missing or parameter type incorrect.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 20
         */
        setWhiteBalance(whiteBalance: number): void;
        /**
         * Sets color tint.
         *
         * @param { number } colorTint - Color tint, the supported range can be obtained by calling
         *     [getColorTintRange]{@link camera.WhiteBalanceQuery.getColorTintRange}.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        setColorTint(colorTint: number): void;
        /**
         * Gets current color tint.
         *
         * @returns { number } The current color tint.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        getColorTint(): number;
    }
    /**
     * Provides APIs to check whether a camera device supports manual ISO setting and obtain the ISO range supported by
     * the device.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice
     * @since 24
     */
    interface ManualIsoQuery {
        /**
         * Get a array of supported standard ISO sensitivity values, as defined in ISO 12232:2006.
         *
         * @returns { number[] } The array of ISO sensitivity values.
         * @throws {BusinessError} 7400102 - Operation not allowed, the inputDevice or the session is abnormal.
         * @throws { BusinessError } 7400103 - Session not config, only throw in session usage.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 24
         */
        getSupportedIsoRange(): number[];
    }
    /**
     * ManualIso object.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice
     * @since 24
     */
    interface ManualIso extends ManualIsoQuery {
        /**
         * Gets current ISO.
         *
         * @returns { number } The current ISO.
         * @throws { BusinessError } 7400103 - Session not config.
         * @throws {BusinessError} 7400102 - Operation not allowed, the inputDevice or the session is abnormal.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 24
         */
        getIso(): number;
        /**
         * Sets ISO sensitivity value, within the range of getSupportedIsoRange. This control is only effective if
         * ExposureMode is set to EXPOSURE_MODE_LOCKED.
         *
         * @param { number } iso - ISO
         * @throws { BusinessError } 7400103 - Session not config.
         * @throws { BusinessError } 7400102 - Operation not allowed, the inputDevice or the session is abnormal.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 24
         */
        setIso(iso: number): void;
    }
    /**
     * Enumerates the smooth zoom modes.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 11
     */
    enum SmoothZoomMode {
        /**
         * Bessel curve mode.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        NORMAL = 0
    }
    /**
     * Describes the smooth zoom information.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 11
     */
    interface SmoothZoomInfo {
        /**
         * Total duration of smooth zoom, in ms.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        duration: number;
    }
    /**
     * Describes the equivalent focal length information.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice
     * @since 26.0.0
     */
    interface ZoomPointInfo {
        /**
         * Zoom ratio.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 26.0.0
         */
        readonly zoomRatio: number;
        /**
         * Equivalent focal length corresponding to the current focal length ratio.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 26.0.0
         */
        readonly equivalentFocalLength: number;
    }
    /**
     * Provides the API to obtain the equivalent focal length information list in the current mode.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 12
     */
    interface ZoomQuery {
        /**
         * Obtains the supported zoom ratio range.
         *
         * @returns { Array<number> } Array containing the minimum and maximum zoom ratios. If the operation fails,
         *     undefined is returned and an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode} is thrown.
         * @throws { BusinessError } 7400103 - Session not config, only throw in session usage.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        getZoomRatioRange(): Array<number>;
        /**
         * Obtains the equivalent focal length information list in the current mode.
         *
         * @returns { Array<ZoomPointInfo> } Equivalent focal length information list in the current mode.
         * @throws { BusinessError } 7400103 - Session not config, only throw in session usage.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 26.0.0
         */
        getZoomPointInfos(): Array<ZoomPointInfo>;
        /**
         * Gets supported zoom ratio range during raw-capture.
         *
         * @returns { Array<number> } The zoom ratio range.
         * @throws {BusinessError} 7400102 - Operation not allowed, the inputDevice or the session is abnormal.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        getRAWCaptureZoomRatioRange(): Array<number>;
    }
    /**
     * Zoom extend [ZoomQuery]{@link camera.ZoomQuery}
     * Provides APIs to process the zoom effect of a camera device, including obtaining the current zoom ratio, setting a
     * zoom ratio, setting a zoom ratio in a smooth manner, and preparing or unpreparing for zooming.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 11
     */
    interface Zoom extends ZoomQuery {
        /**
         * Obtains the zoom ratio in use.
         *
         * @returns { number } Zoom ratio obtained. If the operation fails, an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode} is returned.
         * @throws { BusinessError } 7400103 - Session not config.
         * @throws { BusinessError } 7400201 - Camera service fatal error. [since 12]
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        getZoomRatio(): number;
        /**
         * Sets a zoom ratio, with a maximum precision of two decimal places.
         *
         * @param { number } zoomRatio - Zoom ratio. The supported zoom ratio range can be obtained by calling
         *     [getZoomRatioRange]{@link camera.ZoomQuery.getZoomRatioRange}. If the value passed in
         *     is not within the supported range, the value within the precision range is retained.<br>It takes some time
         *     for the zoom ratio to take effect at the bottom layer. To obtain the correct zoom ratio, you need to wait for
         *     one to two frames.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        setZoomRatio(zoomRatio: number): void;
        /**
         * Sets smooth zoom.
         *
         * @param { number } targetRatio - Target zoom ratio. The supported zoom ratio range can be obtained by calling
         *     [getZoomRatioRange]{@link camera.ZoomQuery.getZoomRatioRange}. If the value passed in
         *     is not within the supported range, the value within the precision range is retained.
         * @param { SmoothZoomMode } mode - Smooth zoom mode. The default value is **0**.
         * @throws { BusinessError } 7400103 - Session not config. [since 11 - 17]
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        setSmoothZoom(targetRatio: number, mode?: SmoothZoomMode): void;
    }
    /**
     * Enumerates the video stabilization modes.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 10
     */
    enum VideoStabilizationMode {
        /**
         * Video stabilization is disabled.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        OFF = 0,
        /**
         * The basic video stabilization algorithm is used.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        LOW = 1,
        /**
         * A video stabilization algorithm with a stabilization effect better than that of the **LOW** type is used.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        MIDDLE = 2,
        /**
         * A video stabilization algorithm with a stabilization effect better than that of the **MIDDLE** type is used.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        HIGH = 3,
        /**
         * The system automatically selects a video stabilization algorithm.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        AUTO = 4
    }
    /**
     * StabilizationQuery provides APIs to check the support for video stabilization.
     *
     * > **NOTE**
     * >
     * > - This interface was first introduced in API version 12. In this version, a compatibility change was made that
     * > preserved the initial version information of inner elements. As a result, you might see outer element's @since
     * > version number being higher than that of the inner elements. However, this discrepancy does not affect the
     * > functionality of the interface.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 12
     */
    interface StabilizationQuery {
        /**
         * Checks whether a video stabilization mode is supported.
         *
         * @param { VideoStabilizationMode } vsMode - Video stabilization mode.
         * @returns { boolean } Check result for the support of the video stabilization mode. **true** if supported,
         *     **false** otherwise. If the operation fails, undefined is returned and an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode} is thrown.
         * @throws { BusinessError } 7400103 - Session not config, only throw in session usage.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        isVideoStabilizationModeSupported(vsMode: VideoStabilizationMode): boolean;
    }
    /**
     * **Stabilization** inherits from [StabilizationQuery]{@link camera.StabilizationQuery}.
     * It provides APIs to set video stabilization.
     * Video stabilization can be set only when the session has a recording stream (
     * [VideoOutput]{@link camera.VideoOutput}). Among the enums of
     * [VideoStabilizationMode]{@link camera.VideoStabilizationMode}, the **HIGH** mode only takes
     * effect when the resolution set in [Profile]{@link camera.Profile} is 1920×1080.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 11
     */
    interface Stabilization extends StabilizationQuery {
        /**
         * Obtains the video stabilization mode in use.
         *
         * @returns { VideoStabilizationMode } Video stabilization mode obtained. If the API call fails, undefined is
         *     returned.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        getActiveVideoStabilizationMode(): VideoStabilizationMode;
        /**
         * Sets a video stabilization mode. Before the setting, call
         * [isVideoStabilizationModeSupported]{@link camera.StabilizationQuery.isVideoStabilizationModeSupported}
         * to check whether the target video stabilization mode is supported. It is recommended that you set the video
         * stabilization mode between [commitConfig]{@link camera.Session.commitConfig()} and
         * [Start]{@link camera.Session.start()}.
         *
         * @param { VideoStabilizationMode } mode - Video stabilization mode.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        setVideoStabilizationMode(mode: VideoStabilizationMode): void;
    }
    /**
     * Enumerates the effect types supported by the camera controller.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice
     * @since 20
     */
    enum ControlCenterEffectType {
        /**
         * Beauty effect.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 20
         */
        BEAUTY = 0,
        /**
         * Portrait blur effect.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 20
         */
        PORTRAIT = 1,
        /**
         * Automatic composition.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 24
         */
        AUTO_FRAMING = 2,
        /**
         * Color effect.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        COLOR_EFFECT = 3
    }
    /**
     * ColorManagementQuery provides the APIs for color space query.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 12
     */
    interface ColorManagementQuery {
        /**
         * Obtains the supported color spaces.
         *
         * @returns { Array<colorSpaceManager.ColorSpace> } Array of color spaces supported. If the API call fails,
         *     undefined is returned.
         * @throws { BusinessError } 7400103 - Session not config, only throw in session usage. [since 12 - 17]
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        getSupportedColorSpaces(): Array<colorSpaceManager.ColorSpace>;
    }
    /**
     * **ColorManagement** inherits from [ColorManagementQuery]{@link camera.ColorManagementQuery}.
     * It provides the APIs for color space settings.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 12
     */
    interface ColorManagement extends ColorManagementQuery {
        /**
         * Obtains the color space in use.
         *
         * @returns { colorSpaceManager.ColorSpace } Color space.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        getActiveColorSpace(): colorSpaceManager.ColorSpace;
        /**
         * Sets a color space.
         *
         * Before the setting, call
         * [getSupportedColorSpaces]{@link camera.ColorManagementQuery.getSupportedColorSpaces} to obtain the supported
         * color spaces. You are advised to call this API after [addOutput]{@link camera.Session.addOutput} and before
         * [commitConfig]{@link camera.Session.commitConfig()}. If this API is called after
         * [commitConfig]{@link camera.Session.commitConfig()}, the camera session configuration will take a longer time.
         *
         * P3 wide color gamut and HDR imaging:
         *
         * An application can deliver different color space parameters to declare its support for P3 and HDR. If an
         * application does not proactively set the color space, SDR is used by default in photo and video recording modes.
         *
         * For different modes, enabling HDR, setting the color space, and configuring
         * [CameraFormat]{@link camera.CameraFormat} in the camera output stream [profile]{@link camera.Profile} should
         * match. For details, see the table below. For example, to enable HDR in video recording mode, set
         * [CameraFormat]{@link camera.CameraFormat} in the camera preview and video output stream
         * [profiles]{@link camera.Profile} to **CAMERA_FORMAT_YCRCB_P010** and the color space to **BT2020_HLG_LIMIT**.
         *
         * To obtain HDR images in photo mode, set the color space to **DISPLAY_P3** or **BT2020_HLG**. **BT2020_HLG**
         * provides a wider color gamut, and should be used together with the **CameraFormat**, including
         * **CAMERA_FORMAT_YCRCB_P010** and **CAMERA_FORMAT_YCBCR_P010**, to improve the image quality.
         *
         * Since API version 23, you can call the
         * [getSupportedFullOutputCapability]{@link camera.CameraManager.getSupportedFullOutputCapability}
         * API to check whether the preview format P010 is supported in photo mode.
         *
         * - If the application does not set the color space, the default color space in photo mode is SRGB when the
         * **CameraFormat** is **CAMERA_FORMAT_YUV_420_SP**, and the default color space is **BT2020_HLG** when the
         * **CameraFormat** is **CAMERA_FORMAT_YCRCB_P010** or **CAMERA_FORMAT_YCBCR_P010**.
         * - If the application sets the color space, in photo mode, the **CameraFormat** and **ColorSpace** must be
         * configured according to the following mapping table. Otherwise, an error code will be returned in
         * [setColorSpace]{@link camera.ColorManagement.setColorSpace} or
         * [commitConfig]{@link camera.Session.commitConfig()}.
         *
         * Photo mode:
         * | SDR/HDR Photo Capture       | CameraFormat| ColorSpace|
         *  |--------------------|------------| ------------|
         *  | SDR(Default)       | CAMERA_FORMAT_YUV_420_SP       | SRGB       |
         *  | HDR P3               | CAMERA_FORMAT_YUV_420_SP | DISPLAY_P3 |
         *  | HDR BT.2020 | CAMERA_FORMAT_YCRCB_P010,<br>CAMERA_FORMAT_YCBCR_P010 | BT2020_HLG |
         *
         * In video recording mode, if SDR or HDR VIVID is enabled, the camera format and color space must be configured
         * according to the relationships specified in the table below. Configurations that do not match the table will
         * cause issues such as preview exceptions.
         *
         * Recording mode:
         * | SDR/HDR Photo Capture        | CameraFormat             | ColorSpace       |
         * |--------------------|--------------------------|------------------|
         * | SDR(Default)               | CAMERA_FORMAT_YUV_420_SP | BT709_LIMIT      |
         * | HDR_VIVID          | CAMERA_FORMAT_YCRCB_P010 | BT2020_HLG_LIMIT,<br>BT2020_HLG |
         * | HDR_VIVID          | CAMERA_FORMAT_YCBCR_P010 | BT2020_HLG_LIMIT,<br>BT2020_HLG |
         *
         * @param { colorSpaceManager.ColorSpace } colorSpace - The type of color space.
         * @throws { BusinessError } 7400101 - Parameter missing or parameter type incorrect.
         * @throws { BusinessError } 7400102 - The colorSpace does not match the format.
         * @throws { BusinessError } 7400103 - Session not config.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        setColorSpace(colorSpace: colorSpaceManager.ColorSpace): void;
    }
    /**
     * ControlCenterQuery is used to check whether the camera controller is supported.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice
     * @since 20
     */
    interface ControlCenterQuery {
        /**
         * Checks whether the camera controller is supported.
         *
         * @returns { boolean } Check result for the support of the camera controller. **true** if supported, **false**
         *     otherwise.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 20
         */
        isControlCenterSupported(): boolean;
        /**
         * Obtains the effect types supported by the camera controller.
         *
         * @returns { Array<ControlCenterEffectType> } Array of effect types supported.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 20
         */
        getSupportedEffectTypes(): Array<ControlCenterEffectType>;
    }
    /**
     * ControlCenter inherits from [ControlCenterQuery]{@link camera.ControlCenterQuery}.
     * It is used to enable the camera controller.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice
     * @since 20
     */
    interface ControlCenter extends ControlCenterQuery {
        /**
         * Enables the camera controller.
         *
         * @param { boolean } enabled - Whether to enable or disable the camera controller. **true** to enable, **false**
         *     otherwise.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 20
         */
        enableControlCenter(enabled: boolean): void;
    }
    /**
     * **AutoDeviceSwitchQuery** is used to check whether a device supports automatic camera switch.
     * [Automatic Camera Switching](docroot://media/camera/camera-auto-switch.md) is supported only on foldable devices.
     *
     * For details about how to enable this capability, see
     * [enableAutoDeviceSwitch]{@link camera.AutoDeviceSwitch.enableAutoDeviceSwitch}.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 13
     */
    interface AutoDeviceSwitchQuery {
        /**
         * Checks whether the device supports automatic camera switch.
         *
         * @returns { boolean } Check result for the support of automatic camera switch. **true** if supported, **false**
         *     otherwise.
         * @throws { BusinessError } 7400103 - Session not config, only throw in session usage. [since 13 - 17]
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 13
         */
        isAutoDeviceSwitchSupported(): boolean;
    }
    /**
     * **AutoDeviceSwitch** inherits from [AutoDeviceSwitchQuery]{@link camera.AutoDeviceSwitchQuery} and is used to
     * enable or disable automatic camera switch. This capability can be used only on foldable devices. For details about
     * the development, see
     * [Practices for Automatic Camera Switching (ArkTS)](docroot://media/camera/camera-auto-switch.md).
     *
     * It is recommended that the system automatically handle input device switching, session configuration, and parameter
     * continuity during automatic camera switch. If the system detects that the zoom ranges of the two cameras are
     * different during camera switching, it will notify the application through the **isDeviceCapabilityChanged** field
     * in [AutoDeviceSwitchStatus]{@link camera.AutoDeviceSwitchStatus}. However, the application
     * still needs to handle the UX change. For example, for the zoom range adjustment, the application needs to call
     * [getZoomRatioRange]{@link camera.ZoomQuery.getZoomRatioRange} to obtain data and update the
     * UX. Therefore, **AutoDeviceSwitch** is more applicable to simplified UX interactions.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 13
     */
    interface AutoDeviceSwitch extends AutoDeviceSwitchQuery {
        /**
         * Enables or disables automatic camera switch. You can use
         * [isAutoDeviceSwitchSupported]{@link camera.AutoDeviceSwitchQuery.isAutoDeviceSwitchSupported}
         * to check whether the device supports automatic camera switch.
         *
         * > **NOTE**
         * >
         * > This API is used only for foldable devices with multiple front cameras. In different fold states, the system
         * > can automatically switch to an available front camera. It does not enable automatic switching between front and
         * > rear cameras.
         *
         * @param { boolean } enabled - Whether to enable automatic camera switch. **true** to enable, **false** otherwise.
         * @throws { BusinessError } 7400102 - Operation not allowed.
         * @throws { BusinessError } 7400103 - Session not config.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @throws { BusinessError } 7400101 - Parameter error. Possible causes:
         *     1. Mandatory parameters are left unspecified; 2. Incorrect parameter types;
         *     3. Parameters verification failed. [since 19]
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 13
         */
        enableAutoDeviceSwitch(enabled: boolean): void;
    }
    /**
     * Describes the information about the automatic camera switch status.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 13
     */
    interface AutoDeviceSwitchStatus {
        /**
         * Whether the camera is automatically switched. **true** if auto-switched, **false** otherwise.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 13
         */
        readonly isDeviceSwitched: boolean;
        /**
         * Whether the camera capability is changed after the camera is automatically switched. **true** if changed,
         * **false** otherwise.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 13
         */
        readonly isDeviceCapabilityChanged: boolean;
    }
    /**
     * MacroQuery provides the API to check the support for macro photography.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice
     * @since 19
     */
    interface MacroQuery {
        /**
         * Checks whether macro photography is supported in the current state. This API must be called after
         * [commitConfig]{@link camera.Session.commitConfig(callback: AsyncCallback<void>)}.
         *
         * @returns { boolean } Check result for the support of macro photography. **true** if supported, **false**
         *     otherwise.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 19
         */
        isMacroSupported(): boolean;
    }
    /**
     * Macro inherits from [MacroQuery]{@link camera.MacroQuery}.
     * It provides the API to enable macro photography.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice
     * @since 19
     */
    interface Macro extends MacroQuery {
        /**
         * Enables or disables macro photography.
         *
         * > **NOTE**
         * >
         * > Before calling this API, call
         * > [isMacroSupported]{@link camera.MacroQuery.isMacroSupported} to check whether the
         * > current device supports macro photography.
         *
         * @param { boolean } enabled - Whether to enable macro photography. **true** to enable, **false** otherwise.
         * @throws { BusinessError } 7400103 - Session not config.
         * @throws { BusinessError } 7400102 - Operation not allowed.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 19
         */
        enableMacro(enabled: boolean): void;
    }
    /**
     * **Session** implements a session, which saves all [CameraInput]{@link camera.CameraInput} and
     * [CameraOutput]{@link camera.CameraOutput} instances required to run the camera and requests the camera
     * to take a photo or record a video.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 11
     */
    interface Session {
        /**
         * Starts configuration for the session.
         *
         * @throws { BusinessError } 7400105 - Session config locked.
         * @throws { BusinessError } 7400201 - Camera service fatal error. [since 12]
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        beginConfig(): void;
        /**
         * Commits the configuration for this session. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the configuration is
         *     successfully committed, **err** is **undefined**; otherwise, **err** is an error object with an error code
         *     defined in [CameraErrorCode]{@link camera.CameraErrorCode}. For example, if the
         *     aspect ratio of the preview stream is different from that of the video output stream, error code 7400201 is
         *     returned.
         * @throws { BusinessError } 7400102 - Operation not allowed.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        commitConfig(callback: AsyncCallback<void>): void;
        /**
         * Commits the configuration for this session. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 7400102 - Operation not allowed.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        commitConfig(): Promise<void>;
        /**
         * Checks whether a **CameraInput** instance can be added to this session. This API must be called after
         * [beginConfig]{@link camera.Session.beginConfig} and before [commitConfig]{@link camera.Session.commitConfig()}.
         *
         * @param { CameraInput } cameraInput - **CameraInput** instance to add. The API does not take effect if the input
         *     parameter is invalid (for example, the value is out of range, null, or undefined).
         * @returns { boolean } Check result for adding the **CameraInput** instance. **true** if it can be added, **false**
         *     otherwise.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        canAddInput(cameraInput: CameraInput): boolean;
        /**
         * Adds a [CameraInput]{@link camera.CameraInput} instance to this session.
         *
         * @param { CameraInput } cameraInput - **CameraInput** instance to add.
         * @throws { BusinessError } 7400101 - Parameter missing or parameter type incorrect.
         * @throws { BusinessError } 7400102 - Operation not allowed.
         * @throws { BusinessError } 7400103 - Session not config. [since 11 - 17]
         * @throws { BusinessError } 7400201 - Camera service fatal error. [since 12]
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        addInput(cameraInput: CameraInput): void;
        /**
         * Removes a [CameraInput]{@link camera.CameraInput} instance from this session. This API must be called
         * after [beginConfig]{@link camera.Session.beginConfig} and before
         * [commitConfig]{@link camera.Session.commitConfig()}.
         *
         * @param { CameraInput } cameraInput - **CameraInput** instance to remove.
         * @throws { BusinessError } 7400101 - Parameter missing or parameter type incorrect.
         * @throws { BusinessError } 7400102 - Operation not allowed.
         * @throws { BusinessError } 7400103 - Session not config. [since 11 - 17]
         * @throws { BusinessError } 7400201 - Camera service fatal error. [since 12]
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        removeInput(cameraInput: CameraInput): void;
        /**
         * Determines whether a CameraOutput instance can be added to this session. This API must be called after
         * [addInput]{@link camera.Session.addInput} and before [commitConfig]{@link camera.Session.commitConfig()}.
         *
         * @param { CameraOutput } cameraOutput - **CameraOutput** instance to add. The API does not take effect if the
         *     input parameter is invalid (for example, the value is out of range, null, or undefined).
         * @returns { boolean } Check result for adding the **CameraOutput** instance. **true** if it can be added,
         *     **false** otherwise.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        canAddOutput(cameraOutput: CameraOutput): boolean;
        /**
         * Adds a [CameraOutput]{@link camera.CameraOutput} instance to this session.
         *
         * @param { CameraOutput } cameraOutput - **CameraOutput** instance to add.
         * @throws { BusinessError } 7400101 - Parameter missing or parameter type incorrect.
         * @throws { BusinessError } 7400102 - Operation not allowed.
         * @throws { BusinessError } 7400103 - Session not config. [since 11 - 17]
         * @throws { BusinessError } 7400201 - Camera service fatal error. [since 12]
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        addOutput(cameraOutput: CameraOutput): void;
        /**
         * Removes a [CameraOutput]{@link camera.CameraOutput} instance from this session.
         *
         * @param { CameraOutput } cameraOutput - **CameraOutput** instance to remove.
         * @throws { BusinessError } 7400101 - Parameter missing or parameter type incorrect.
         * @throws { BusinessError } 7400102 - Operation not allowed.
         * @throws { BusinessError } 7400103 - Session not config. [since 11 - 17]
         * @throws { BusinessError } 7400201 - Camera service fatal error. [since 12]
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        removeOutput(cameraOutput: CameraOutput): void;
        /**
         * Starts this session. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the session starts successfully,
         *     **err** is **undefined**; otherwise, **err** is an error object with an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode}.
         * @throws { BusinessError } 7400103 - Session not config.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @throws { BusinessError } 7400102 - Operation not allowed. [since 12]
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        start(callback: AsyncCallback<void>): void;
        /**
         * Starts this session. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 7400103 - Session not config.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @throws { BusinessError } 7400102 - Operation not allowed. [since 12]
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        start(): Promise<void>;
        /**
         * Stops this session. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the session stops successfully,
         *     **err** is **undefined**; otherwise, **err** is an error object with an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode}.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        stop(callback: AsyncCallback<void>): void;
        /**
         * Stops this session. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        stop(): Promise<void>;
        /**
         * Releases this session. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the session is released
         *     successfully, **err** is **undefined**; otherwise, **err** is an error object with an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode}.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        release(callback: AsyncCallback<void>): void;
        /**
         * Releases this session. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        release(): Promise<void>;
    }
    /**
     * Implements a capture session, which saves all [CameraInput]{@link camera.CameraInput} and
     * [CameraOutput]{@link camera.CameraOutput} instances required to run the camera and requests the camera
     * to complete shooting or video recording.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @since 10
     * @deprecated since 11
     * @useinstead camera.VideoSession
     */
    interface CaptureSession {
        /**
         * Starts configuration for the session.
         *
         * @throws { BusinessError } 7400105 - Session config locked.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.Session.beginConfig
         */
        beginConfig(): void;
        /**
         * Commits the configuration for this session. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the configuration is
         *     successfully committed, **err** is **undefined**; otherwise, **err** is an error object with an error code
         *     defined in [CameraErrorCode]{@link camera.CameraErrorCode}.
         * @throws { BusinessError } 7400102 - Operation not allowed.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.Session.commitConfig(callback: AsyncCallback<void>)
         */
        commitConfig(callback: AsyncCallback<void>): void;
        /**
         * Commits the configuration for this session. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 7400102 - Operation not allowed.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.Session.commitConfig()
         */
        commitConfig(): Promise<void>;
        /**
         * Adds a [CameraInput]{@link camera.CameraInput} instance to this session.
         *
         * @param { CameraInput } cameraInput - CameraInput instance to add.
         * @throws { BusinessError } 7400101 - Parameter missing or parameter type incorrect.
         * @throws { BusinessError } 7400102 - Operation not allowed.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.Session.addInput
         */
        addInput(cameraInput: CameraInput): void;
        /**
         * Removes a [CameraInput]{@link camera.CameraInput} instance from this session.
         *
         * @param { CameraInput } cameraInput - CameraInput instance to remove.
         * @throws { BusinessError } 7400101 - Parameter missing or parameter type incorrect.
         * @throws { BusinessError } 7400102 - Operation not allowed.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.Session.removeInput
         */
        removeInput(cameraInput: CameraInput): void;
        /**
         * Adds a [CameraOutput]{@link camera.CameraOutput} instance to this session.
         *
         * @param { CameraOutput } cameraOutput - CameraOutput instance to add.
         * @throws { BusinessError } 7400101 - Parameter missing or parameter type incorrect.
         * @throws { BusinessError } 7400102 - Operation not allowed.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.Session.addOutput
         */
        addOutput(cameraOutput: CameraOutput): void;
        /**
         * Removes a [CameraOutput]{@link camera.CameraOutput} instance from this session.
         *
         * @param { CameraOutput } cameraOutput - CameraOutput instance to remove.
         * @throws { BusinessError } 7400101 - Parameter missing or parameter type incorrect.
         * @throws { BusinessError } 7400102 - Operation not allowed.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.Session.removeOutput
         */
        removeOutput(cameraOutput: CameraOutput): void;
        /**
         * Starts this session. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the session starts successfully,
         *     **err** is **undefined**; otherwise, **err** is an error object with an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode}.
         * @throws { BusinessError } 7400103 - Session not config.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.Session.start(callback: AsyncCallback<void>)
         */
        start(callback: AsyncCallback<void>): void;
        /**
         * Starts this session. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 7400103 - Session not config.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.Session.start()
         */
        start(): Promise<void>;
        /**
         * Stops this session. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the session stops successfully,
         *     **err** is **undefined**; otherwise, **err** is an error object with an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode}.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.Session.stop(callback: AsyncCallback<void>)
         */
        stop(callback: AsyncCallback<void>): void;
        /**
         * Stops this session. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.Session.stop()
         */
        stop(): Promise<void>;
        /**
         * Releases this session. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the session is released
         *     successfully, **err** is **undefined**; otherwise, **err** is an error object with an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode}.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.Session.release(callback: AsyncCallback<void>)
         */
        release(callback: AsyncCallback<void>): void;
        /**
         * Releases this session. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.Session.release()
         */
        release(): Promise<void>;
        /**
         * Checks whether the camera device has flash.
         *
         * @returns { boolean } Check result for whether the camera device has flash. **true** if it has flash, **false**
         *     otherwise. If the operation fails, an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode} is returned.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.FlashQuery.hasFlash
         */
        hasFlash(): boolean;
        /**
         * Checks whether the flash mode is supported.
         *
         * @param { FlashMode } flashMode - Flash mode.
         * @returns { boolean } Check result for the support of the flash mode. **true** if supported, **false** otherwise.
         *     If the operation fails, an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode} is returned.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.FlashQuery.isFlashModeSupported
         */
        isFlashModeSupported(flashMode: FlashMode): boolean;
        /**
         * Obtains the flash mode in use.
         *
         * @returns { FlashMode } Flash mode obtained. If the operation fails, an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode} is returned.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.Flash.getFlashMode
         */
        getFlashMode(): FlashMode;
        /**
         * Sets a flash mode.
         * Before the setting, do the following checks:
         *
         * 1. Use [hasFlash]{@link camera.CaptureSession.hasFlash} to check whether the camera device has flash.
         * 2. Use [isFlashModeSupported]{@link camera.CaptureSession.isFlashModeSupported} to check whether the camera
         * device supports the flash mode.
         *
         * @param { FlashMode } flashMode - Flash mode.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.Flash.setFlashMode
         */
        setFlashMode(flashMode: FlashMode): void;
        /**
         * Checks whether an exposure mode is supported.
         *
         * @param { ExposureMode } aeMode - Exposure mode.
         * @returns { boolean } Check result for the support of the exposure mode. **true** if supported, **false**
         *     otherwise. If the operation fails, an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode} is returned.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.AutoExposureQuery.isExposureModeSupported
         */
        isExposureModeSupported(aeMode: ExposureMode): boolean;
        /**
         * Obtains the exposure mode in use.
         *
         * @returns { ExposureMode } Exposure mode obtained. If the operation fails, an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode} is returned.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.AutoExposure.getExposureMode
         */
        getExposureMode(): ExposureMode;
        /**
         * Sets an exposure mode. Before the setting, call
         * [isExposureModeSupported]{@link camera.CaptureSession.isExposureModeSupported} to check whether the target
         * exposure mode is supported.
         *
         * @param { ExposureMode } aeMode - Exposure mode.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.AutoExposure.setExposureMode
         */
        setExposureMode(aeMode: ExposureMode): void;
        /**
         * Obtains the metering point of the camera device.
         *
         * @returns { Point } Metering point obtained. If the operation fails, an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode} is returned.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.AutoExposure.getMeteringPoint
         */
        getMeteringPoint(): Point;
        /**
         * Sets the metering point, which is the center point of the metering rectangle. The metering point must be in the
         * coordinate system (0-1), where the top-left corner is {0, 0} and the bottom-right corner is {1, 1}.
         *
         * The coordinate system is based on the horizontal device direction with the device's charging port on the right.
         * If the layout of the preview screen of an application is based on the vertical direction with the charging port
         * on the lower side, the layout width and height are {w, h}, and the touch point is {x, y}, then the coordinate
         * point after conversion is {y/h, 1-x/w}.
         *
         * @param { Point } point - Metering point. The value range of x and y must be within [0,1]. If a value less than 0
         *     is passed, the value **0** is used. If a value greater than **1** is passed, the value **1** is used.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.AutoExposure.setMeteringPoint
         */
        setMeteringPoint(point: Point): void;
        /**
         * Obtains the exposure compensation values of the camera device.
         *
         * @returns { Array<number> } Array of compensation values. If the operation fails, an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode} is returned.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.AutoExposureQuery.getExposureBiasRange
         */
        getExposureBiasRange(): Array<number>;
        /**
         * Sets an exposure compensation value (EV).
         * Before the setting, you are advised to use
         * [getExposureBiasRange]{@link camera.CaptureSession.getExposureBiasRange} to obtain the supported values.
         *
         * @param { number } exposureBias - EV. The supported EV range can be obtained by calling
         *     [getExposureBiasRange]{@link camera.AutoExposureQuery.getExposureBiasRange}. If the
         *     value passed is not within the supported range, the nearest critical point is used. There is a step for EV.
         *     For example, if the step is 0.5 and this parameter is set to 1.2, the EV that takes effect is 1.0. If the
         *     operation fails, an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode} is returned. If the input parameter
         *     is null or undefined, the EV is set to 0.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.AutoExposure.setExposureBias
         */
        setExposureBias(exposureBias: number): void;
        /**
         * Obtains the exposure value in use.
         *
         * @returns { number } Exposure value obtained. There is a step for EV. For example, if the step is 0.5 and this
         *     parameter is set to 1.2, the EV that takes effect is 1.0. If the operation fails, an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode} is returned.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.AutoExposure.getExposureValue
         */
        getExposureValue(): number;
        /**
         * Checks whether a focus mode is supported.
         *
         * @param { FocusMode } afMode - Focus mode.
         * @returns { boolean } Check result for the support of the focus mode. **true** if supported, **false** otherwise.
         *     If the operation fails, an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode} is returned.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.FocusQuery.isFocusModeSupported
         */
        isFocusModeSupported(afMode: FocusMode): boolean;
        /**
         * Obtains the focus mode in use.
         *
         * @returns { FocusMode } Focus mode obtained. If the operation fails, an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode} is returned.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.Focus.getFocusMode
         */
        getFocusMode(): FocusMode;
        /**
         * Sets a focus mode.
         * Before the setting, call [isFocusModeSupported]{@link camera.CaptureSession.isFocusModeSupported} to check
         * whether the focus mode is supported.
         *
         * @param { FocusMode } afMode - Focus mode.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.Focus.setFocusMode
         */
        setFocusMode(afMode: FocusMode): void;
        /**
         * Sets the focal point. The focal point must be in the coordinate system (0-1), where the top-left corner is {0, 0}
         * and the bottom-right corner is {1, 1}.
         *
         * The coordinate system is based on the horizontal device direction with the device's charging port on the right.
         * If the layout of the preview screen of an application is based on the vertical direction with the charging port
         * on the lower side, the layout width and height are {w, h}, and the touch point is {x, y}, then the coordinate
         * point after conversion is {y/h, 1-x/w}.
         *
         * @param { Point } point - Focal point. The value range of x and y must be within [0,1]. If a value less than 0 is
         *     passed, the value **0** is used. If a value greater than **1** is passed, the value **1** is used.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.Focus.setFocusPoint
         */
        setFocusPoint(point: Point): void;
        /**
         * Obtains the focal point of the camera device.
         *
         * @returns { Point } Focal point obtained. If the operation fails, an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode} is returned.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.Focus.getFocusPoint
         */
        getFocusPoint(): Point;
        /**
         * Obtains the focal length of the camera device.
         *
         * @returns { number } Focal length obtained. If the operation fails, an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode} is returned.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.Focus.getFocalLength
         */
        getFocalLength(): number;
        /**
         * Obtains the supported zoom ratio range.
         *
         * @returns { Array<number> } Array containing the minimum and maximum zoom ratios. If the operation fails, an error
         *     code defined in [CameraErrorCode]{@link camera.CameraErrorCode} is returned.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.ZoomQuery.getZoomRatioRange
         */
        getZoomRatioRange(): Array<number>;
        /**
         * Obtains the zoom ratio in use.
         *
         * @returns { number } Zoom ratio obtained. If the operation fails, an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode} is returned.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.Zoom.getZoomRatio
         */
        getZoomRatio(): number;
        /**
         * Sets a zoom ratio, with a maximum precision of two decimal places.
         *
         * @param { number } zoomRatio - Zoom ratio. The supported zoom ratio range can be obtained by calling
         *     [getZoomRatioRange]{@link camera.ZoomQuery.getZoomRatioRange}. If the value passed in
         *     is not within the supported range, the value within the precision range is retained. If the input parameter
         *     is null or undefined, it is treated as 0 and the minimum zoom ratio is used.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.Zoom.setZoomRatio
         */
        setZoomRatio(zoomRatio: number): void;
        /**
         * Checks whether a video stabilization mode is supported.
         *
         * @param { VideoStabilizationMode } vsMode - Video stabilization mode. If the input parameter is null or undefined,
         *     it is treated as 0 and video stabilization is disabled.
         * @returns { boolean } Check result for the support of the video stabilization mode. **true** if supported,
         *     **false** otherwise. If the operation fails, an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode} is returned.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.StabilizationQuery.isVideoStabilizationModeSupported
         */
        isVideoStabilizationModeSupported(vsMode: VideoStabilizationMode): boolean;
        /**
         * Obtains the video stabilization mode in use.
         *
         * @returns { VideoStabilizationMode } Video stabilization mode obtained. If the operation fails, an error code
         *     defined in [CameraErrorCode]{@link camera.CameraErrorCode} is returned.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.Stabilization.getActiveVideoStabilizationMode
         */
        getActiveVideoStabilizationMode(): VideoStabilizationMode;
        /**
         * Sets a video stabilization mode. Before the setting, call
         * [isVideoStabilizationModeSupported]{@link camera.CaptureSession.isVideoStabilizationModeSupported} to check
         * whether the target video stabilization mode is supported.
         *
         * @param { VideoStabilizationMode } mode - Video stabilization mode. If the input parameter is null or undefined,
         *     it is treated as 0 and video stabilization is disabled.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.Stabilization.setVideoStabilizationMode
         */
        setVideoStabilizationMode(mode: VideoStabilizationMode): void;
        /**
         * Subscribes to focus state change events. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.
         *
         * @param { 'focusStateChange' } type - Event type. The value is fixed at **'focusStateChange'**. The event can be
         *     listened for when a session is created. This event is triggered only when the camera focus state changes in
         *     auto focus mode.
         * @param { AsyncCallback<FocusState> } callback - Callback used to return the focus state change.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.VideoSession.on(type: 'focusStateChange', callback: AsyncCallback<FocusState>)
         */
        on(type: 'focusStateChange', callback: AsyncCallback<FocusState>): void;
        /**
         * Unsubscribes from focus state change events.
         *
         * @param { 'focusStateChange' } type - Event type. The value is fixed at **'focusStateChange'**. The event can be
         *     listened for when a session is created.
         * @param { AsyncCallback<FocusState> } callback - Callback used to return the result. If this parameter is
         *     specified, the subscription to the specified event with the specified callback is canceled. (The callback
         *     object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the
         *     callbacks are canceled.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.VideoSession.off(type: 'focusStateChange', callback?: AsyncCallback<FocusState>)
         */
        off(type: 'focusStateChange', callback?: AsyncCallback<FocusState>): void;
        /**
         * Subscribes to CaptureSession error events. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.
         *
         * @param { 'error' } type - Event type. The value is fixed at **'error'**. The event can be listened for when a
         *     session is created. This event is triggered and the error message is returned when an error occurs during the
         *     calling of a session-related API such as [beginConfig]{@link camera.CaptureSession.beginConfig},
         *     [commitConfig]{@link camera.CaptureSession.commitConfig()}, and
         *     [addInput]{@link camera.CaptureSession.addInput}.
         * @param { ErrorCallback } callback - Callback used to return an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode}.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.VideoSession.on(type: 'error', callback: ErrorCallback)
         */
        on(type: 'error', callback: ErrorCallback): void;
        /**
         * Unsubscribes from CaptureSession error events. This API uses a callback to return the result.
         *
         * @param { 'error' } type - Event type. The value is fixed at **'error'**. The event can be listened for when a
         *     session is created.
         * @param { ErrorCallback } callback - Callback used to return the result. If this parameter is specified, the
         *     subscription to the specified event with the specified callback is canceled. (The callback object cannot be
         *     an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are
         *     canceled.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.VideoSession.off(type: 'error', callback?: ErrorCallback)
         */
        off(type: 'error', callback?: ErrorCallback): void;
    }
    /**
     * Enumerates the preconfigured resolution types.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 12
     */
    enum PreconfigType {
        /**
         * 720p resolution.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        PRECONFIG_720P = 0,
        /**
         * 1080p resolution.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        PRECONFIG_1080P = 1,
        /**
         * 4K resolution.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        PRECONFIG_4K = 2,
        /**
         * High-quality resolution.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        PRECONFIG_HIGH_QUALITY = 3,
        /**
         * Resolution that supports HDR preview and GIF photography.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        PRECONFIG_HIGH_QUALITY_PHOTOSESSION_BT2020 = 4
    }
    /**
     * Enumerates the preconfigured aspect ratios.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 12
     */
    enum PreconfigRatio {
        /**
         * 1:1 aspect ratio.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        PRECONFIG_RATIO_1_1 = 0,
        /**
         * 4:3 aspect ratio.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        PRECONFIG_RATIO_4_3 = 1,
        /**
         * 16:9 aspect ratio.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        PRECONFIG_RATIO_16_9 = 2
    }
    /**
     * Enumerates the photo quality prioritization strategies.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice
     * @since 21
     */
    enum PhotoQualityPrioritization {
        /**
         * Focuses on image quality, which may increase the time required for capturing photos to ensure high-quality
         * output.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 21
         */
        HIGH_QUALITY = 0,
        /**
         * Focuses on performance, trading off image quality for faster capture times.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 21
         */
        SPEED = 1
    }
    /**
     * Implements a photo session, which sets the parameters of the normal photo mode and saves all
     * [CameraInput]{@link camera.CameraInput} and [CameraOutput]{@link camera.CameraOutput}
     * instances required to run the camera. It inherits from [Session]{@link camera.Session}.
     *
     * @extends Session, Flash, AutoExposure, Focus, Zoom, ColorManagement [since 11 - 12]
     * @extends Session, Flash, AutoExposure, Focus, Zoom, ColorManagement, AutoDeviceSwitch [since 13 - 18]
     * @extends Session, Flash, AutoExposure, Focus, Zoom, ColorManagement, AutoDeviceSwitch, Macro [since 19 - 19]
     * @extends Session, Flash, AutoExposure, WhiteBalance, Focus, Zoom, ColorManagement, AutoDeviceSwitch,
     *     Macro [since 20 - 23]
     * @extends Session, Flash, AutoExposure, WhiteBalance, Focus, Zoom, ColorManagement, AutoDeviceSwitch,
     *     Macro, ManualExposure, ManualFocus, ManualIso, OIS, Aperture [since 24]
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 11
     */
    interface PhotoSession extends Session, Flash, AutoExposure, WhiteBalance, Focus, Zoom, ColorManagement, AutoDeviceSwitch, Macro, ManualExposure, ManualFocus, ManualIso, OIS, Aperture {
        /**
         * Checks whether this session supports a preconfigured resolution.
         *
         * @param { PreconfigType } preconfigType - Resolution type.
         * @param { PreconfigRatio } preconfigRatio - Aspect ratio. The default value is 4:3.
         * @returns { boolean } Whether a preconfigured resolution is supported. **true** if supported, **false** otherwise.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        canPreconfig(preconfigType: PreconfigType, preconfigRatio?: PreconfigRatio): boolean;
        /**
         * Preconfigures this session.
         *
         * @param { PreconfigType } preconfigType - Resolution type.
         * @param { PreconfigRatio } preconfigRatio - Aspect ratio. The default value is 4:3.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        preconfig(preconfigType: PreconfigType, preconfigRatio?: PreconfigRatio): void;
        /**
         * Subscribes to **PhotoSession** error events. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.
         *
         * @param { 'error' } type - Event type. The value is fixed at **'error'**. The event can be listened for when a
         *     session is created. This event is triggered and the error message is returned when an error occurs during the
         *     calling of a session-related API such as
         *     [beginConfig]{@link camera.Session.beginConfig},
         *     [commitConfig]{@link camera.Session.commitConfig(callback: AsyncCallback<void>)}, and
         *     [addInput]{@link camera.Session.addInput}.
         * @param { ErrorCallback } callback - Callback used to return an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode}.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        on(type: 'error', callback: ErrorCallback): void;
        /**
         * Unsubscribes from **PhotoSession** error events. This API uses a callback to return the result.
         *
         * @param { 'error' } type - Event type. The value is fixed at **'error'**. The event can be listened for when a
         *     session is created.
         * @param { ErrorCallback } callback - Callback used to return the result. If this parameter is specified, the
         *     subscription to the specified event with the specified callback is canceled. (The callback object cannot be
         *     an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are
         *     canceled.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        off(type: 'error', callback?: ErrorCallback): void;
        /**
         * Subscribes to focus state change events. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.
         *
         * @param { 'focusStateChange' } type - Event type. The value is fixed at **'focusStateChange'**. The event can be
         *     listened for when a session is created. This event is triggered only when the camera focus state changes in
         *     autofocus mode.
         * @param { AsyncCallback<FocusState> } callback - Callback used to return the focus state change.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        on(type: 'focusStateChange', callback: AsyncCallback<FocusState>): void;
        /**
         * Unsubscribes from focus state change events.
         *
         * @param { 'focusStateChange' } type - Event type. The value is fixed at **'focusStateChange'**. The event can be
         *     listened for when a session is created.
         * @param { AsyncCallback<FocusState> } callback - Callback used to return the result. If this parameter is
         *     specified, the subscription to the specified event with the specified callback is canceled. (The callback
         *     object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the
         *     callbacks are canceled.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        off(type: 'focusStateChange', callback?: AsyncCallback<FocusState>): void;
        /**
         * Subscribes to smooth zoom state change events. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.
         *
         * @param { 'smoothZoomInfoAvailable' } type - Event type. The value is fixed at **'smoothZoomInfoAvailable'**. The
         *     event can be listened for when a session is created.
         * @param { AsyncCallback<SmoothZoomInfo> } callback - Callback used to return the smooth zoom state change.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        on(type: 'smoothZoomInfoAvailable', callback: AsyncCallback<SmoothZoomInfo>): void;
        /**
         * Unsubscribes from smooth zoom state change events.
         *
         * @param { 'smoothZoomInfoAvailable' } type - Event type. The value is fixed at **'smoothZoomInfoAvailable'**. The
         *     event can be listened for when a session is created.
         * @param { AsyncCallback<SmoothZoomInfo> } callback - Callback used to return the result. If this parameter is
         *     specified, the subscription to the specified event with the specified callback is canceled. (The callback
         *     object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the
         *     callbacks are canceled.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        off(type: 'smoothZoomInfoAvailable', callback?: AsyncCallback<SmoothZoomInfo>): void;
        /**
         * Subscribes to macro state change events. This API uses an asynchronous callback to return the result.
         *
         * @param { 'macroStatusChanged' } type - Event type. The value is fixed at **'macroStatusChanged'**. The event can
         *     be listened for when a session is created.
         * @param { AsyncCallback<boolean> } callback - Callback used to return the macro state. **true** if enabled,
         *     **false** otherwise.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 20
         */
        on(type: 'macroStatusChanged', callback: AsyncCallback<boolean>): void;
        /**
         * Unsubscribes from macro state change events.
         *
         * @param { 'macroStatusChanged' } type - Event type. The value is fixed at **'macroStatusChanged'**. The event can
         *     be listened for when a session is created.
         * @param { AsyncCallback<boolean> } callback - Callback used to return the result. If this parameter is specified,
         *     the subscription to the specified event with the specified callback is canceled. (The callback object cannot
         *     be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are
         *     canceled.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 20
         */
        off(type: 'macroStatusChanged', callback?: AsyncCallback<boolean>): void;
        /**
         * Subscribes to automatic camera switch status change events. This API uses an asynchronous callback to return the
         * result.
         *
         * > **NOTE**
         * >
         * > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.
         *
         * @param { 'autoDeviceSwitchStatusChange' } type - Event type. The value is fixed at
         *     **'autoDeviceSwitchStatusChange'**. The event can be listened for when a session is created.
         * @param { AsyncCallback<AutoDeviceSwitchStatus> } callback - Callback function, which is used to obtain the status
         *     of automatic camera switch.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 13
         */
        on(type: 'autoDeviceSwitchStatusChange', callback: AsyncCallback<AutoDeviceSwitchStatus>): void;
        /**
         * Unsubscribes from automatic camera switch status change events.
         *
         * @param { 'autoDeviceSwitchStatusChange' } type - Event type. The value is fixed at
         *     **'autoDeviceSwitchStatusChange'**. The event can be listened for when a session is created.
         * @param { AsyncCallback<AutoDeviceSwitchStatus> } callback - Callback used to return the result. If this parameter
         *     is specified, the subscription to the specified event with the specified callback is canceled. (The callback
         *     object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the
         *     callbacks are canceled.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 13
         */
        off(type: 'autoDeviceSwitchStatusChange', callback?: AsyncCallback<AutoDeviceSwitchStatus>): void;
        /**
         * Subscribes to system pressure level change events. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.
         *
         * @param { 'systemPressureLevelChange' } type - Event type. The value is fixed at **'systemPressureLevelChange'**.
         *     The event can be listened for when a session is created.
         * @param { AsyncCallback<SystemPressureLevel> } callback - Callback used to return the current system pressure
         *     level.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 20
         */
        on(type: 'systemPressureLevelChange', callback: AsyncCallback<SystemPressureLevel>): void;
        /**
         * Unsubscribes from system pressure level change events.
         *
         * @param { 'systemPressureLevelChange' } type - Event type. The value is fixed at **'systemPressureLevelChange'**.
         *     The event can be listened for when a session is created.
         * @param { AsyncCallback<SystemPressureLevel> } [callback] - Callback used to return the result. If this parameter
         *     is specified, the subscription to the specified event with the specified callback is canceled. (The callback
         *     object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the
         *     callbacks are canceled.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 20
         */
        off(type: 'systemPressureLevelChange', callback?: AsyncCallback<SystemPressureLevel>): void;
        /**
         * Subscribes ISO info change event callback.
         *
         * @param { Callback<IsoInfo> } callback - Callback used to get the ISO info change.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        onIsoInfoChange(callback: Callback<IsoInfo>): void;
        /**
         * Unsubscribes from ISO info change event callback.
         *
         * @param { Callback<IsoInfo> } [callback] - Callback used to get the ISO info change.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        offIsoInfoChange(callback?: Callback<IsoInfo>): void;
        /**
         * Subscribes exposure info change event callback.
         * After exposure parameters are changed, the system will returns the updated exposure infos.
         *
         * @param { Callback<ExposureInfo> } callback - Callback used to get the exposure value change.
         *     <br>Exposure information callback listening.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        onExposureInfoChange(callback: Callback<ExposureInfo>): void;
        /**
         * Unsubscribes exposure info change event callback. Invoke this method after finishing camera operations.
         *
         * @param { Callback<ExposureInfo> } [callback] - Callback used to get the exposure value change.
         *     <br>Callback listening for canceling exposure information.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        offExposureInfoChange(callback?: Callback<ExposureInfo>): void;
    }
    /**
     * Enumerates the priority levels for video recording quality.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 14
     */
    enum QualityPrioritization {
        /**
         * Prioritizes high-quality video recording.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 14
         */
        HIGH_QUALITY = 0,
        /**
         * Prioritizes video recording quality while balancing power consumption.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 14
         */
        POWER_BALANCE = 1
    }
    /**
     * VideoSession extends Session, Flash, AutoExposure, Focus, Zoom, Stabilization, ColorManagement
     * Implements a video session, which sets the parameters of the normal video mode and saves all
     * [CameraInput]{@link camera.CameraInput} and [CameraOutput]{@link camera.CameraOutput}
     * instances required to run the camera. It inherits from [Session]{@link camera.Session}.
     *
     * @extends Session, Flash, AutoExposure, Focus, Zoom, Stabilization, ColorManagement [since 11 - 12]
     * @extends AutoDeviceSwitch [since 13 - 18]
     * @extends Session, Flash, AutoExposure, Focus, Zoom, Stabilization, ColorManagement,
     *     AutoDeviceSwitch, Macro [since 19 - 19]
     * @extends Session, Flash, AutoExposure, WhiteBalance, Focus, Zoom, Stabilization, ColorManagement, ControlCenter,
     *     AutoDeviceSwitch, Macro [since 20 - 24]
     * @extends Session, Flash, AutoExposure, WhiteBalance, Focus, Zoom, Stabilization, ColorManagement, ControlCenter,
     *     AutoDeviceSwitch, Macro, ManualExposure, ManualFocus, ManualIso, OIS, Aperture [since 26.0.0]
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 11
     */
    interface VideoSession extends Session, Flash, AutoExposure, WhiteBalance, Focus, Zoom, Stabilization, ColorManagement, ControlCenter, AutoDeviceSwitch, Macro, ManualExposure, ManualFocus, ManualIso, OIS, Aperture {
        /**
         * Checks whether this session supports a preconfigured resolution.
         *
         * @param { PreconfigType } preconfigType - Resolution type.
         * @param { PreconfigRatio } preconfigRatio - Aspect ratio. The default value is 16:9.
         * @returns { boolean } **true**: The preconfigured resolution is supported.
         *     <br>**false**: The preconfigured resolution is not supported.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        canPreconfig(preconfigType: PreconfigType, preconfigRatio?: PreconfigRatio): boolean;
        /**
         * Preconfigures this session.
         *
         * @param { PreconfigType } preconfigType - Resolution type.
         * @param { PreconfigRatio } preconfigRatio - Aspect ratio. The default value is 16:9.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        preconfig(preconfigType: PreconfigType, preconfigRatio?: PreconfigRatio): void;
        /**
         * Subscribes to **PhotoSession** error events. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.
         *
         * @param { 'error' } type - Event type. The value is fixed at **'error'**. The event can be listened for when a
         *     session is created. This event is triggered and the error message is returned when an error occurs during the
         *     calling of a session-related API such as
         *     [beginConfig]{@link camera.Session.beginConfig},
         *     [commitConfig]{@link camera.Session.commitConfig(callback: AsyncCallback<void>)}, and
         *     [addInput]{@link camera.Session.addInput}.
         * @param { ErrorCallback } callback - Callback used to return an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode}.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        on(type: 'error', callback: ErrorCallback): void;
        /**
         * Unsubscribes from **PhotoSession** error events. This API uses a callback to return the result.
         *
         * @param { 'error' } type - Event type. The value is fixed at **'error'**. The event can be listened for when a
         *     session is created.
         * @param { ErrorCallback } callback - Callback used to return the result. If this parameter is specified, the
         *     subscription to the specified event with the specified callback is canceled. (The callback object cannot be
         *     an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are
         *     canceled.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        off(type: 'error', callback?: ErrorCallback): void;
        /**
         * Subscribes to focus state change events. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.
         *
         * @param { 'focusStateChange' } type - Event type. The value is fixed at **'focusStateChange'**. The event can be
         *     listened for when a session is created. This event is triggered only when the camera focus state changes in
         *     autofocus mode.
         * @param { AsyncCallback<FocusState> } callback - Callback used to return the focus state change.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        on(type: 'focusStateChange', callback: AsyncCallback<FocusState>): void;
        /**
         * Unsubscribes from focus state change events.
         *
         * @param { 'focusStateChange' } type - Event type. The value is fixed at **'focusStateChange'**. The event can be
         *     listened for when a session is created.
         * @param { AsyncCallback<FocusState> } callback - Callback used to return the result. If this parameter is
         *     specified, the subscription to the specified event with the specified callback is canceled. (The callback
         *     object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the
         *     callbacks are canceled.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        off(type: 'focusStateChange', callback?: AsyncCallback<FocusState>): void;
        /**
         * Subscribes to smooth zoom state change events. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.
         *
         * @param { 'smoothZoomInfoAvailable' } type - Event type. The value is fixed at **'smoothZoomInfoAvailable'**. The
         *     event can be listened for when a session is created.
         * @param { AsyncCallback<SmoothZoomInfo> } callback - Callback used to return the smooth zoom state change.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        on(type: 'smoothZoomInfoAvailable', callback: AsyncCallback<SmoothZoomInfo>): void;
        /**
         * Unsubscribes from smooth zoom state change events.
         *
         * @param { 'smoothZoomInfoAvailable' } type - Event type. The value is fixed at **'smoothZoomInfoAvailable'**. The
         *     event can be listened for when a session is created.
         * @param { AsyncCallback<SmoothZoomInfo> } callback - Callback used to return the result. If this parameter is
         *     specified, the subscription to the specified event with the specified callback is canceled. (The callback
         *     object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the
         *     callbacks are canceled.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        off(type: 'smoothZoomInfoAvailable', callback?: AsyncCallback<SmoothZoomInfo>): void;
        /**
          * Subscribes to events indicating that the camera controller effect status changes. This API uses an asynchronous
          * callback to return the result.
          *
          * > **NOTE**
          * >
          * > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.
          *
          * @param { 'controlCenterEffectStatusChange' } type - Event type. The value is fixed at
          *     **'controlCenterEffectStatusChange'**. The event can be listened for when a session is created.
          * @param { AsyncCallback<ControlCenterStatusInfo> } callback - Callback used to return the effect status of the
          *     current controller.
          * @syscap SystemCapability.Multimedia.Camera.Core
          * @atomicservice
          * @since 20
          */
        on(type: 'controlCenterEffectStatusChange', callback: AsyncCallback<ControlCenterStatusInfo>): void;
        /**
         * Unsubscribes from events indicating that the camera controller effect status changes.
         *
         * @param { 'controlCenterEffectStatusChange' } type - Event type. The value is fixed at
         *     **'controlCenterEffectStatusChange'**. The event can be listened for when a session is created.
         * @param { AsyncCallback<ControlCenterStatusInfo> } [callback] - Callback used to return the result. If this
         *     parameter is specified, the subscription to the specified event with the specified callback is canceled. (
         *     The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event
         *     with all the callbacks are canceled.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 20
         */
        off(type: 'controlCenterEffectStatusChange', callback?: AsyncCallback<ControlCenterStatusInfo>): void;
        /**
         * Subscribes to macro state change events. This API uses an asynchronous callback to return the result.
         *
         * @param { 'macroStatusChanged' } type - Event type. The value is fixed at **'macroStatusChanged'**. The event can
         *     be listened for when a session is created.
         * @param { AsyncCallback<boolean> } callback - Callback used to return the macro state. **true** if enabled,
         *     **false** otherwise.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 20
         */
        on(type: 'macroStatusChanged', callback: AsyncCallback<boolean>): void;
        /**
         * Unsubscribes from macro state change events.
         *
         * @param { 'macroStatusChanged' } type - Event type. The value is fixed at **'macroStatusChanged'**. The event can
         *     be listened for when a session is created.
         * @param { AsyncCallback<boolean> } callback - Callback used to return the result. If this parameter is specified,
         *     the subscription to the specified event with the specified callback is canceled. (The callback object cannot
         *     be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are
         *     canceled.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 20
         */
        off(type: 'macroStatusChanged', callback?: AsyncCallback<boolean>): void;
        /**
         * Subscribes to automatic camera switch status change events. This API uses an asynchronous callback to return the
         * result.
         *
         * > **NOTE**
         * >
         * > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.
         *
         * @param { 'autoDeviceSwitchStatusChange' } type - Event type. The value is fixed at
         *     **'autoDeviceSwitchStatusChange'**. The event can be listened for when a session is created.
         * @param { AsyncCallback<AutoDeviceSwitchStatus> } callback - Callback function, which is used to obtain the status
         *     of automatic camera switch.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 13
         */
        on(type: 'autoDeviceSwitchStatusChange', callback: AsyncCallback<AutoDeviceSwitchStatus>): void;
        /**
         * Unsubscribes from automatic camera switch status change events.
         *
         * @param { 'autoDeviceSwitchStatusChange' } type - Event type. The value is fixed at
         *     **'autoDeviceSwitchStatusChange'**. The event can be listened for when a session is created.
         * @param { AsyncCallback<AutoDeviceSwitchStatus> } callback - Callback used to return the result. If this parameter
         *     is specified, the subscription to the specified event with the specified callback is canceled. (The callback
         *     object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the
         *     callbacks are canceled.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 13
         */
        off(type: 'autoDeviceSwitchStatusChange', callback?: AsyncCallback<AutoDeviceSwitchStatus>): void;
        /**
         * Subscribes to system pressure level change events. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.
         *
         * @param { 'systemPressureLevelChange' } type - Event type. The value is fixed at **'systemPressureLevelChange'**.
         *     The event can be listened for when a session is created.
         * @param { AsyncCallback<SystemPressureLevel> } callback - Callback used to return the current system pressure
         *     level.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 20
         */
        on(type: 'systemPressureLevelChange', callback: AsyncCallback<SystemPressureLevel>): void;
        /**
         * Unsubscribes from system pressure level change events.
         *
         * @param { 'systemPressureLevelChange' } type - Event type. The value is fixed at **'systemPressureLevelChange'**.
         *     The event can be listened for when a session is created.
         * @param { AsyncCallback<SystemPressureLevel> } callback - Callback used to return the result. If this parameter is
         *     specified, the subscription to the specified event with the specified callback is canceled. (The callback
         *     object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the
         *     callbacks are canceled.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 20
         */
        off(type: 'systemPressureLevelChange', callback?: AsyncCallback<SystemPressureLevel>): void;
        /**
         * Sets the priority level for video recording quality.
         *
         * > **NOTE**
         * >
         * > - The default value is **HIGH_QUALITY**. Switching to **POWER_BALANCE** will compromise video recording quality
         * > to achieve lower power usage. The extent of power conservation achieved varies depending on the platform.
         * >
         * > - It is recommended that this API be called between
         * > [commitConfig]{@link camera.Session.commitConfig(callback: AsyncCallback<void>)} and
         * > [start]{@link camera.Session.start()}.
         *
         * @param { QualityPrioritization } quality - Priority level to set. The default value is **HIGH_QUALITY**.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1. Mandatory parameters are left unspecified; 2. Incorrect parameter types;
         *     3. Parameter verification failed.
         * @throws { BusinessError } 7400103 - Session not config. The session has not been committed or configured.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 14
         */
        setQualityPrioritization(quality: QualityPrioritization): void;
        /**
         * Subscribes ISO info change event callback.
         *
         * @param { Callback<IsoInfo> } callback - Callback used to get the ISO info change.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 22
         */
        onIsoInfoChange(callback: Callback<IsoInfo>): void;
        /**
         * Unsubscribes from ISO info change event callback.
         *
         * @param { Callback<IsoInfo> } [callback] - Callback used to get the ISO info change.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 22
         */
        offIsoInfoChange(callback?: Callback<IsoInfo>): void;
        /**
         * Subscribes exposure info change event callback.
         *     After exposure parameters are changed, the system will returns the updated exposure infos.
         *
         * @param { Callback<ExposureInfo> } callback - Callback used to get the exposure value change
         *     Exposure information callback listening.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        onExposureInfoChange(callback: Callback<ExposureInfo>): void;
        /**
         * Unsubscribes exposure info change event callback. Invoke this method after finishing camera operations.
         *
         * @param { Callback<ExposureInfo> } [callback] - Callback used to get the exposure value change.
         *     Callback listening for canceling exposure information.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        offExposureInfoChange(callback?: Callback<ExposureInfo>): void;
    }
    /**
     * Enumerates the system pressure levels.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice
     * @since 20
     */
    enum SystemPressureLevel {
        /**
         * The system pressure is normal.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 20
         */
        SYSTEM_PRESSURE_NORMAL = 0,
        /**
         * The system pressure is elevated but not actively managed by the system.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 20
         */
        SYSTEM_PRESSURE_MILD = 1,
        /**
         * The system pressure may affect the overall image quality and performance.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 20
         */
        SYSTEM_PRESSURE_SEVERE = 2,
        /**
         * The system pressure has a significant impact on the image quality and performance.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 20
         */
        SYSTEM_PRESSURE_CRITICAL = 3,
        /**
         * The system pressure is too high, causing the system to shut down.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 20
         */
        SYSTEM_PRESSURE_SHUTDOWN = 4
    }
    /**
     * Describes the zoom range.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice
     * @since 24
     */
    interface ZoomRange {
        /**
         * Minimum zoom value.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 24
         */
        readonly min: number;
        /**
         * Maximum zoom value.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 24
         */
        readonly max: number;
    }
    /**
     * Describes the physical aperture object.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice
     * @since 24
     */
    interface PhysicalAperture {
        /**
         * Zoom range of a given physical aperture.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 24
         */
        zoomRange: ZoomRange;
        /**
         * Supported physical aperture.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 24
         */
        apertures: Array<number>;
    }
    /**
     * Provides the aperture query capability.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice
     * @since 24
     */
    interface ApertureQuery {
        /**
         * Gets the supported physical apertures.
         * Move to ApertureQuery interface from Aperture since 12.
         *
         * @returns { Array<PhysicalAperture> } The array of supported physical apertures.
         * @throws { BusinessError } 7400103 - Session not config.
         * @throws {BusinessError} 7400102 - Operation not allowed, the inputDevice or the session is abnormal.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 24
         */
        getSupportedPhysicalApertures(): Array<PhysicalAperture>;
    }
    /**
     * Provides the APIs for aperture settings. It inherits from [ApertureQuery]{@link camera.ApertureQuery}.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice
     * @since 24
     */
    interface Aperture extends ApertureQuery {
        /**
         * Gets current physical aperture value.
         *
         * @returns { number } The current physical aperture value.
         * @throws { BusinessError } 7400103 - Session not config.
         * @throws {BusinessError} 7400102 - Operation not allowed, the inputDevice or the session is abnormal.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 24
         */
        getPhysicalAperture(): number;
        /**
         * Sets physical aperture value.
         *
         * @param { number } aperture - physical aperture value. The supported physical aperture range can be obtained by
         *     calling [getSupportedPhysicalApertures]{@link camera.ApertureQuery.getSupportedPhysicalApertures}
         * @throws { BusinessError } 7400103 - Session not config.
         * @throws {BusinessError} 7400102 - Operation not allowed, the inputDevice or the session is abnormal.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 24
         */
        setPhysicalAperture(aperture: number): void;
    }
    /**
     * Provides APIs to obtain the manual exposure range supported.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice
     * @since 24
     */
    interface ManualExposureQuery {
        /**
         * Gets the supported manual exposure duration range, units: microseconds.
         *
         * @returns { Array<number> } The array of manual exposure range.
         * @throws { BusinessError } 7400102 - Operation not allowed, session or inputdevice maybe abnormal.
         * @throws { BusinessError } 7400103 - Session not config, only throw in session usage.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 24
         */
        getSupportedExposureDurationRange(): Array<number>;
        /**
         * Get exposure bias step.
         *
         * @returns { number } exposure bias step.
         * @throws { BusinessError } 7400102 - Operation not allowed, session or inputdevice maybe abnormal.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        getExposureBiasStep(): number;
    }
    /**
     * ManualExposure extends [ManualExposureQuery]{@link camera.ManualExposureQuery}
     * Provides APIs to obtain and set the exposure duration.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice
     * @since 24
     */
    interface ManualExposure extends ManualExposureQuery {
        /**
         * Gets current exposure value.
         *
         * @returns { number } The current exposure value, in units of microsecond
         * @throws { BusinessError } 7400102 - Operation not allowed, session or inputdevice maybe abnormal.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 24
         */
        getExposureDuration(): number;
        /**
         * Sets Exposure duration value, units: microseconds.
         *
         * @param { number } exposureDuration - Exposure duration value
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 24
         */
        setExposureDuration(exposureDuration: number): void;
    }
    /**
     * Describes the ISO information.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice
     * @since 22
     */
    interface IsoInfo {
        /**
         * ISO value.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 22
         */
        readonly iso?: number;
    }
    /**
     * Describes the exposure information object.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice
     * @since 24
     */
    interface ExposureInfo {
        /**
         * Exposure time, in microseconds.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 24
         */
        readonly exposureTime?: number;
    }
    /**
     * **SecureSession** inherits from [Session]{@link camera.Session},
     * [Flash]{@link camera.Flash}, [AutoExposure]{@link camera.AutoExposure},
     * [WhiteBalance]{@link camera.WhiteBalance}, [Focus]{@link camera.Focus}, and [Zoom]{@link camera.Zoom}.
     *
     * It implements a secure session, which provides operations on the flash, exposure, white balance, focus, and zoom.
     *
     * You can call [createSession]{@link camera.CameraManager.createSession} with
     * [SceneMode]{@link camera.SceneMode} set to **SECURE_PHOTO** to create a session in secure
     * mode. The secure mode is designed for applications with high security requirements, such as facial recognition
     * systems and banking services. It must be used together with the <!--RP1-->security TA<!--RP1End--> to support
     * service scenarios where both standard preview streams and security streams are output.<!--RP2-->
     *
     * The security TA can verify the signature of data delivered by the server, sign images, parse and assemble TLV logic
     * , and read, create, and operate keys. It applies to image processing.<!--RP2End-->
     *
     * @extends Session, Flash, AutoExposure, Focus, Zoom [since 12 - 19]
     * @extends Session, Flash, AutoExposure, WhiteBalance, Focus, Zoom [since 20]
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 12
     */
    interface SecureSession extends Session, Flash, AutoExposure, WhiteBalance, Focus, Zoom {
        /**
         * Marks a [PreviewOutput]{@link camera.PreviewOutput} stream as secure output.
         *
         * @param { PreviewOutput } previewOutput - Preview output stream. An error code is returned if the input parameter
         *     is invalid.
         * @throws { BusinessError } 7400101 - Parameter missing or parameter type incorrect.
         * @throws { BusinessError } 7400102 - Operation not allowed.
         * @throws { BusinessError } 7400103 - Session not config. [since 12 - 17]
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        addSecureOutput(previewOutput: PreviewOutput): void;
        /**
         * Subscribes to SecureSession error events. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.
         *
         * @param { 'error' } type - Event type. The value is fixed at **'error'**. The event can be listened for when a
         *     session is created. This event is triggered and the error message is returned when an error occurs during the
         *     calling of a session-related API such as
         *     [beginConfig]{@link camera.Session.beginConfig},
         *     [commitConfig]{@link camera.Session.commitConfig()}, and
         *     [addInput]{@link camera.Session.addInput}.
         * @param { ErrorCallback } callback - Callback used to return an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode}.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        on(type: 'error', callback: ErrorCallback): void;
        /**
         * Unsubscribes from SecureSession error events.
         *
         * @param { 'error' } type - Event type. The value is fixed at **'error'**. The event can be listened for when a
         *     session is created.
         * @param { ErrorCallback } callback - Callback used to return the result. If this parameter is specified, the
         *     subscription to the specified event with the specified callback is canceled. (The callback object cannot be
         *     an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are
         *     canceled.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        off(type: 'error', callback?: ErrorCallback): void;
        /**
         * Subscribes to focus state change events. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.
         *
         * @param { 'focusStateChange' } type - Event type. The value is fixed at **'focusStateChange'**. The event can be
         *     listened for when a session is created. This event is triggered only when the camera focus state changes in
         *     auto focus mode.
         * @param { AsyncCallback<FocusState> } callback - Callback used to return the focus state change.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        on(type: 'focusStateChange', callback: AsyncCallback<FocusState>): void;
        /**
         * Unsubscribes from focus state change events.
         *
         * @param { 'focusStateChange' } type - Event type. The value is fixed at **'focusStateChange'**. The event can be
         *     listened for when a session is created.
         * @param { AsyncCallback<FocusState> } callback - Callback used to return the result. If this parameter is
         *     specified, the subscription to the specified event with the specified callback is canceled. (The callback
         *     object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the
         *     callbacks are canceled.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        off(type: 'focusStateChange', callback?: AsyncCallback<FocusState>): void;
    }
    /**
     * CameraOutput implements output information used in [Session]{@link camera.Session}. It is the base
     * class of **output**.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 10
     */
    interface CameraOutput {
        /**
         * Releases output resources. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the output resources are
         *     released successfully, **err** is **undefined**; otherwise, **err** is an error object with an error code
         *     defined in [CameraErrorCode]{@link camera.CameraErrorCode}.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        release(callback: AsyncCallback<void>): void;
        /**
         * Releases output resources. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        release(): Promise<void>;
    }
    /**
     * Implements preview output. It inherits from [CameraOutput]{@link camera.CameraOutput}.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 10
     */
    interface PreviewOutput extends CameraOutput {
        /**
         * Starts to output preview streams. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the preview stream output starts
         *     successfully, **err** is **undefined**; otherwise, **err** is an error object with an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode}.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.Session.start(callback: AsyncCallback<void>)
         */
        start(callback: AsyncCallback<void>): void;
        /**
         * Starts to output preview streams. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.Session.start()
         */
        start(): Promise<void>;
        /**
         * Stops outputting preview streams. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the preview stream output stops
         *     successfully, **err** is **undefined**; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.Session.stop(callback: AsyncCallback<void>)
         */
        stop(callback: AsyncCallback<void>): void;
        /**
         * Stops outputting preview streams. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.Session.stop()
         */
        stop(): Promise<void>;
        /**
         * Subscribes to preview frame start events. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.
         *
         * @param { 'frameStart' } type - Event type. The value is fixed at **'frameStart'**. The event can be listened for
         *     when a previewOutput instance is created. This event is triggered and returned when the bottom layer starts
         *     exposure for the first time.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. The preview starts as long as this
         *     event is returned.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        on(type: 'frameStart', callback: AsyncCallback<void>): void;
        /**
         * Unsubscribes from preview frame start events.
         *
         * @param { 'frameStart' } type - Event type. The value is fixed at **'frameStart'**. The event can be listened for
         *     when a previewOutput instance is created.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If this parameter is specified, the
         *     subscription to the specified event with the specified callback is canceled. (The callback object cannot be
         *     an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are
         *     canceled.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        off(type: 'frameStart', callback?: AsyncCallback<void>): void;
        /**
         * Subscribes to preview frame end events. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.
         *
         * @param { 'frameEnd' } type - Event type. The value is fixed at **'frameEnd'**. The event can be listened for when
         *     a previewOutput instance is created. This event is triggered and returned when the last frame of preview
         *     ends.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. The preview ends as long as this
         *     event is returned.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        on(type: 'frameEnd', callback: AsyncCallback<void>): void;
        /**
         * Unsubscribes from preview frame end events.
         *
         * @param { 'frameEnd' } type - Event type. The value is fixed at **'frameEnd'**. The event can be listened for when
         *     a previewOutput instance is created.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If this parameter is specified, the
         *     subscription to the specified event with the specified callback is canceled. (The callback object cannot be
         *     an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are
         *     canceled.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        off(type: 'frameEnd', callback?: AsyncCallback<void>): void;
        /**
         * Subscribes to PreviewOutput error events. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.
         *
         * @param { 'error' } type - Event type. The value is fixed at **'error'**. The event can be listened for when a
         *     previewOutput instance is created. This event is triggered and the corresponding error message is returned
         *     when an error occurs during the use of a preview-related API such as
         *     [Session.start]{@link camera.Session.start()} or
         *     [CameraOutput.release]{@link camera.CameraOutput.release()}.
         * @param { ErrorCallback } callback - Callback used to return an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode}.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        on(type: 'error', callback: ErrorCallback): void;
        /**
         * Unsubscribes from PreviewOutput error events.
         *
         * @param { 'error' } type - Event type. The value is fixed at **'error'**. The event can be listened for when a
         *     previewOutput instance is created.
         * @param { ErrorCallback } callback - Callback used to return the result. If this parameter is specified, the
         *     subscription to the specified event with the specified callback is canceled. (The callback object cannot be
         *     an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are
         *     canceled.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        off(type: 'error', callback?: ErrorCallback): void;
        /**
         * Obtains the supported frame rates.
         *
         * @returns { Array<FrameRateRange> } Array of supported frame rates. If the API call fails, undefined is returned.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        getSupportedFrameRates(): Array<FrameRateRange>;
        /**
         * Sets a frame rate range for preview streams. The range must be within the supported frame rate range, which can
         * be obtained by calling [getSupportedFrameRates]{@link camera.PreviewOutput.getSupportedFrameRates}.
         *
         * > **NOTE**
         * >
         * > This API is valid only in [PhotoSession]{@link camera.PhotoSession} or
         * > [VideoSession]{@link camera.VideoSession} mode.
         *
         * @param { number } minFps - Minimum frame rate, in fps. When the maximum value is less than the minimum value, the
         *     API does not take effect.
         * @param { number } maxFps - Maximum frame rate, in fps. When the minimum value is greater than the maximum value, the
         *     API does not take effect.
         * @throws { BusinessError } 7400101 - Parameter missing or parameter type incorrect.
         * @throws { BusinessError } 7400110 - Unresolved conflicts with current configurations.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        setFrameRate(minFps: number, maxFps: number): void;
        /**
         * Obtains the configured frame rate range.
         * This API is valid only after [setFrameRate]{@link camera.PreviewOutput.setFrameRate} is called to set a frame
         * rate range for preview streams.
         *
         * @returns { FrameRateRange } Frame rate range.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        getActiveFrameRate(): FrameRateRange;
        /**
         * Obtains the preview rotation angle.
         *
         * - Device's natural orientation: the default orientation for using a device. For example, the default orientation
         * of the bar-type phone is in portrait mode, with the charging port facing downward.
         * - Camera lens angle: equivalent to the angle at which the camera is rotated clockwise to match the device's
         * natural orientation. For example, the rear camera sensor of a bar-type phone is installed in landscape mode.
         * Therefore, it needs to be rotated by 90 degrees clockwise to match the device's natural orientation.
         * - [Screen rotation](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-multi-device-window-direction#section15598121101615)
         * : indicates the clockwise rotation angle of the device screen.
         *
         * @param { number } displayRotation - Screen rotation angle of the display. It is obtained by calling
         *     [display.getDefaultDisplaySync]{@link @ohos.display:display.getDefaultDisplaySync}.<br> Since API version 23,
         *     the input parameter **displayRotation** is optional. If no parameter is passed, the system obtains the
         *     **displayRotation** value to calculate rotation angle of a video. [since 12 - 22]
         * @param { number } [displayRotation] - Screen rotation angle of the display. It is obtained by calling
         *     [display.getDefaultDisplaySync]{@link @ohos.display:display.getDefaultDisplaySync}.<br> Since API version 23,
         *     the input parameter **displayRotation** is optional. If no parameter is passed, the system obtains the
         *     **displayRotation** value to calculate rotation angle of a video. [since 23]
         * @returns { ImageRotation } The preview rotation angle obtained. If the API call fails, undefined is returned.
         * @throws { BusinessError } 7400101 - Parameter missing or parameter type incorrect. [since 12 - 22]
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice [since 19]
         * @since 12
         */
        getPreviewRotation(displayRotation?: number): ImageRotation;
        /**
         * Sets the preview rotation angle.
         *
         * @param { ImageRotation } previewRotation - Preview rotation angle.
         * @param { boolean } isDisplayLocked - Whether the orientation of the surface is locked when the screen rotates. If
         *     this parameter is not set, the default value **false** is used, indicating that the orientation is not
         *     locked. **true** if locked, **false** otherwise. For details, see
         *     [SurfaceRotationOptions]{@link SurfaceRotationOptions}.
         * @throws { BusinessError } 7400101 - Parameter missing or parameter type incorrect.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        setPreviewRotation(previewRotation: ImageRotation, isDisplayLocked?: boolean): void;
        /**
         * Obtains the profile that takes effect currently.
         *
         * @returns { Profile } Profile obtained.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        getActiveProfile(): Profile;
        /**
         * Adds a deferred surface.
         *
         * @param { string } surfaceId - Surface object id used in camera photo output.
         * @throws { BusinessError } 7400101 - Parameter missing or parameter type incorrect.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 24
         */
        addDeferredSurface(surfaceId: string): void;
        /**
         * Checks whether preview bandwidth compression is supported. This involves reducing data volume through encoding to
         * minimize bandwidth usage during transmission.
         *
         * @returns { boolean } Check result for the support of preview bandwidth compression. **true** if supported,
         *     **false** otherwise.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 23
         */
        isBandwidthCompressionSupported(): boolean;
        /**
         * Enables preview bandwidth compression.
         * Before enabling this feature, you can call
         * [isBandwidthCompressionSupported]{@link camera.PreviewOutput.isBandwidthCompressionSupported} to check whether
         * the device supports preview bandwidth compression.
         *
         * > **NOTE**
         * >
         * > This function must be called prior to
         * > [Session.commitConfig]{@link camera.Session.commitConfig(callback: AsyncCallback<void>)}.
         * > Otherwise, the preview output stream format will be affected.
         *
         * @param { boolean } enabled - Whether to enable preview bandwidth compression. **true** to enable, **false**
         *     otherwise.
         * @throws { BusinessError } 7400102 - Operation not allowed.
         * @throws { BusinessError } 7400103 - Session not config.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 23
         */
        enableBandwidthCompression(enabled: boolean): void;
        /**
         * Checks whether log video view assistance is supported.
         *
         * @returns { boolean } Check result for the support of log video view assistance. **true** if supported,
         *     **false** otherwise.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        isLogViewAssistSupported(): boolean;
        /**
         * Log video view assistance toggle. Before enabling this feature, you can call
         * [isLogViewAssistSupported]{@link camera.PreviewOutput.isLogViewAssistSupported} to check whether
         * the device supports log video view assistance.
         *
         * @param { boolean } enable - Whether to enable log video view assistance, **true** to enable, **false** otherwise.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 7400103 - Session not config.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        setLogViewAssistEnable(enable: boolean): void;
    }
    /**
     * Enumerates the image rotation angles.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 10
     */
    enum ImageRotation {
        /**
         * The image rotates 0 degrees.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        ROTATION_0 = 0,
        /**
         * The image rotates 90 degrees.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        ROTATION_90 = 90,
        /**
         * The image rotates 180 degrees.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        ROTATION_180 = 180,
        /**
         * The image rotates 270 degrees.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        ROTATION_270 = 270
    }
    /**
     * Describes the geolocation information.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 10
     */
    interface Location {
        /**
         * Latitude, in degrees, within the range [-90, 90].
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        latitude: number;
        /**
         * Longitude, in degrees, within the range [-180, 180].
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        longitude: number;
        /**
         * Altitude, in meters.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        altitude: number;
    }
    /**
     * Enumerates the image quality levels.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 10
     */
    enum QualityLevel {
        /**
         * High image quality.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        QUALITY_LEVEL_HIGH = 0,
        /**
         * Medium image quality.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        QUALITY_LEVEL_MEDIUM = 1,
        /**
         * Low image quality.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        QUALITY_LEVEL_LOW = 2
    }
    /**
     * Describes the settings for taking an image.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 10
     */
    interface PhotoCaptureSetting {
        /**
         * Image quality (low by default).
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        quality?: QualityLevel;
        /**
         * Rotation angle of the image. The default value is **0**, indicating clockwise rotation.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        rotation?: ImageRotation;
        /**
         * Geolocation information of the image (depending on the device hardware information by default).
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        location?: Location;
        /**
         * Whether mirror photography is enabled (disabled by default). Before using this enumerated value, call
         * [isMirrorSupported]{@link camera.PhotoOutput.isMirrorSupported} to check whether mirror
         * photography is supported. **true** if enabled, **false** otherwise.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        mirror?: boolean;
        /**
         * Photo image compression quality.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        compressionQuality?: number;
    }
    /**
     * Defines a higher-resolution image object.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 11
     */
    interface Photo {
        /**
         * Full-quality image.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        main: image.Image;
        /**
         * Releases output resources. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        release(): Promise<void>;
    }
    /**
     * Defines the image container type, which is used to obtain full-quality images or uncompressed images (YUV).
     *
     * @unionmember { image.Image } Image container type that obtains full-quality images.
     * @unionmember { image.Picture } Image container type that obtains uncompressed images (YUV).
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice
     * @since 23
     */
    type ImageType = image.Image | image.Picture;
    /**
     * **CapturePhoto** provides APIs for obtaining the objects of the full-quality image and the uncompressed image.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @stagemodelonly
     * @atomicservice
     * @since 23
     */
    interface CapturePhoto {
        /**
         * Object of the full-quality image and the uncompressed image.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        main: ImageType;
        /**
         * Releases output resources. This API uses a promise to return the result.
         * Model constraint: This API can be used only in the stage model.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        release(): Promise<void>;
    }
    /**
     * Enumerates the video codec types.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 13
     */
    enum VideoCodecType {
        /**
         * AVC.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 13
         */
        AVC = 0,
        /**
         * HEVC.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 13
         */
        HEVC = 1
    }
    /**
     * Implements output information used in a photo session. It inherits from
     * [CameraOutput]{@link camera.CameraOutput}.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 10
     */
    interface PhotoOutput extends CameraOutput {
        /**
         * Captures a photo with the default photo capture parameters. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the photo is successfully
         *     captured with the default parameters, **err** is **undefined**; otherwise, **err** is an error object with an
         *     error code defined in [CameraErrorCode]{@link camera.CameraErrorCode}.
         * @throws { BusinessError } 7400104 - Session not running.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        capture(callback: AsyncCallback<void>): void;
        /**
         * Captures a photo with the default photo capture parameters. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 7400104 - Session not running.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        capture(): Promise<void>;
        /**
         * Captures a photo with the specified photo capture parameters. This API uses an asynchronous callback to return
         * the result.
         *
         * @param { PhotoCaptureSetting } setting - Photo capture settings. If the input data is of the **undefined** type,
         *     a photo capture operation is triggered based on the default settings.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation fails, an error
         *     code defined in [CameraErrorCode]{@link camera.CameraErrorCode} is returned.
         * @throws { BusinessError } 7400101 - Parameter missing or parameter type incorrect.
         * @throws { BusinessError } 7400104 - Session not running.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        capture(setting: PhotoCaptureSetting, callback: AsyncCallback<void>): void;
        /**
         * Captures a photo with the specified photo capture parameters. This API uses a promise to return the result.
         *
         * @param { PhotoCaptureSetting } setting - Photo capture settings. If the input data is of the **undefined** type,
         *     a photo capture operation is triggered based on the default settings.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 7400101 - Parameter missing or parameter type incorrect.
         * @throws { BusinessError } 7400104 - Session not running.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        capture(setting: PhotoCaptureSetting): Promise<void>;
        /**
         * Obtains the supported video codec types of moving photos.
         *
         * @returns { Array<VideoCodecType> } Array holding the supported video codec types. If the API call fails,
         *     undefined is returned.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 13
         */
        getSupportedMovingPhotoVideoCodecTypes(): Array<VideoCodecType>;
        /**
         * Sets a video codec type for moving photos.
         *
         * @param { VideoCodecType } codecType - Video codec type.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 13
         */
        setMovingPhotoVideoCodecType(codecType: VideoCodecType): void;
        /**
         * Subscribes to the events of returning available photos. This API uses an asynchronous callback to return the
         * result.
         *
         * > **NOTE**
         * >
         * > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.
         *
         * @param { 'photoAvailable' } type - Event type. The value is fixed at **'photoAvailable'**. The event can be
         *     listened for when a **photoOutput** instance is created.
         * @param { AsyncCallback<Photo> } callback - Callback used to listen for the events of returning available photos.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        on(type: 'photoAvailable', callback: AsyncCallback<Photo>): void;
        /**
         * Unsubscribes from the events of returning available photos.
         *
         * @param { 'photoAvailable' } type - Event type. The value is fixed at **'photoAvailable'**. The event can be
         *     listened for when a photoOutput instance is created.
         * @param { AsyncCallback<Photo> } callback - Callback used to return the result. If this parameter is specified,
         *     the subscription to the specified event with the specified callback is canceled. (The callback object cannot
         *     be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are
         *     canceled.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        off(type: 'photoAvailable', callback?: AsyncCallback<Photo>): void;
        /**
         * Subscribes photo available event callback, which supports delivery of uncompressed photo.
         *
         * @param { Callback<CapturePhoto> } callback - Callback used to get the CapturePhoto.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        onCapturePhotoAvailable(callback: Callback<CapturePhoto>): void;
        /**
         * Unsubscribes photo available event callback, which supports delivery of uncompressed photo.
         *
         * @param { Callback<CapturePhoto> } [callback] - Callback used to get the CapturePhoto.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        offCapturePhotoAvailable(callback?: Callback<CapturePhoto>): void;
        /**
         * Subscribes to photo asset available events. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.
         *
         * @param { 'photoAssetAvailable' } type - Event type. The value is fixed at **'photoAssetAvailable'**. The event
         *     can be listened for when a photoOutput instance is created.
         * @param { AsyncCallback<photoAccessHelper.PhotoAsset> } callback - Callback used to return the photo asset.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        on(type: 'photoAssetAvailable', callback: AsyncCallback<photoAccessHelper.PhotoAsset>): void;
        /**
         * Unsubscribes from photo asset available events.
         *
         * @param { 'photoAssetAvailable' } type - Event type. The value is fixed at **'photoAssetAvailable'**. The event
         *     can be listened for when a photoOutput instance is created.
         * @param { AsyncCallback<photoAccessHelper.PhotoAsset> } callback - Callback used for unsubscription. If this
         *     parameter is specified, the subscription to the specified event with the specified callback is canceled. (The
         *     callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with
         *     all the callbacks are canceled.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        off(type: 'photoAssetAvailable', callback?: AsyncCallback<photoAccessHelper.PhotoAsset>): void;
        /**
         * Checks whether mirror photography is supported.
         *
         * @returns { boolean } Check result for the support of mirror photography. **true** if supported, **false**
         *     otherwise. If the API call fails, undefined is returned.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        isMirrorSupported(): boolean;
        /**
         * Enables or disables mirroring photo capture.
         * Before calling this API, check whether moving photo capture is supported by calling
         * [isMovingPhotoSupported]{@link camera.PhotoOutput.isMovingPhotoSupported} and whether mirroring is supported by
         * calling [isMirrorSupported]{@link camera.PhotoOutput.isMirrorSupported}.
         *
         * @param { boolean } enabled - Whether to enable mirroring photo capture. **true** to enable, **false** otherwise.
         * @throws { BusinessError } 7400101 - Parameter missing or parameter type incorrect.
         * @throws { BusinessError } 7400103 - Session not config.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 13
         */
        enableMirror(enabled: boolean): void;
        /**
         * Subscribes to capture start events. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.
         *
         * @param { 'captureStart' } type - Event type. The value is fixed at **'captureStart'**. The event can be listened
         *     for when a photoOutput instance is created. This event is triggered and returned when the bottom layer starts
         *     exposure each time a photo is taken.
         * @param { AsyncCallback<number> } callback - Callback used to return the capture ID.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.PhotoOutput.on(type: 'captureStartWithInfo', callback: AsyncCallback<CaptureStartInfo>)
         */
        on(type: 'captureStart', callback: AsyncCallback<number>): void;
        /**
         * Unsubscribes from capture start events.
         *
         * > **NOTE**
         * >
         * > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.
         *
         * @param { 'captureStart' } type - Event type. The value is fixed at **'captureStart'**. The event can be listened
         *     for when a photoOutput instance is created.
         * @param { AsyncCallback<number> } callback - Callback used to return the result. If this parameter is specified,
         *     the subscription to the specified event with the specified callback is canceled. (The callback object cannot
         *     be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are
         *     canceled.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @since 10
         * @deprecated since 11
         * @useinstead camera.PhotoOutput.off(type: 'captureStartWithInfo', callback?: AsyncCallback<CaptureStartInfo>)
         */
        off(type: 'captureStart', callback?: AsyncCallback<number>): void;
        /**
         * Subscribes to capture start events. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.
         *
         * @param { 'captureStartWithInfo' } type - Event type. The value is fixed at **'captureStartWithInfo'**. The event
         *     can be listened for when a photoOutput instance is created.
         * @param { AsyncCallback<CaptureStartInfo> } callback - Callback used to return the capture ID.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        on(type: 'captureStartWithInfo', callback: AsyncCallback<CaptureStartInfo>): void;
        /**
         * Unsubscribes from capture start events.
         *
         * @param { 'captureStartWithInfo' } type - Event type. The value is fixed at **'captureStartWithInfo'**. The event
         *     can be listened for when a photoOutput instance is created.
         * @param { AsyncCallback<CaptureStartInfo> } callback - Callback used to return the result. If this parameter is
         *     specified, the subscription to the specified event with the specified callback is canceled. (The callback
         *     object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the
         *     callbacks are canceled.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        off(type: 'captureStartWithInfo', callback?: AsyncCallback<CaptureStartInfo>): void;
        /**
         * Subscribes to frame shutter events. This API uses an asynchronous callback to return the result.
         *
         * @param { 'frameShutter' } type - Event type. The value is fixed at **'frameShutter'**. The event can be listened
         *     for when a photoOutput instance is created.
         * @param { AsyncCallback<FrameShutterInfo> } callback - Callback used to return the result. A new photo capture
         *     request can be delivered as long as this event is returned.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        on(type: 'frameShutter', callback: AsyncCallback<FrameShutterInfo>): void;
        /**
         * Unsubscribes from frame shutter events.
         *
         * @param { 'frameShutter' } type - Event type. The value is fixed at **'frameShutter'**. The event can be listened
         *     for when a photoOutput instance is created.
         * @param { AsyncCallback<FrameShutterInfo> } callback - Callback used to return the result. If this parameter is
         *     specified, the subscription to the specified event with the specified callback is canceled. (The callback
         *     object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the
         *     callbacks are canceled.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        off(type: 'frameShutter', callback?: AsyncCallback<FrameShutterInfo>): void;
        /**
         * Subscribes to frame shutter end events. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.
         *
         * @param { 'frameShutterEnd' } type - Event type. The value is fixed at **'frameShutterEnd'**. The event can be
         *     listened for when a photoOutput instance is created.
         * @param { AsyncCallback<FrameShutterEndInfo> } callback - Callback used to return the result. It is invoked when
         *     the frame shutter ends.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        on(type: 'frameShutterEnd', callback: AsyncCallback<FrameShutterEndInfo>): void;
        /**
         * Unsubscribes from frame shutter end events.
         *
         * @param { 'frameShutterEnd' } type - Event type. The value is fixed at **'frameShutterEnd'**. The event can be
         *     listened for when a photoOutput instance is created.
         * @param { AsyncCallback<FrameShutterEndInfo> } callback - Callback used to return the result. If this parameter is
         *     specified, the subscription to the specified event with the specified callback is canceled. (The callback
         *     object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the
         *     callbacks are canceled.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        off(type: 'frameShutterEnd', callback?: AsyncCallback<FrameShutterEndInfo>): void;
        /**
         * Subscribes to capture end events. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.
         *
         * @param { 'captureEnd' } type - Event type. The value is fixed at **'captureEnd'**. The event can be listened for
         *     when a photoOutput instance is created. This event is triggered and the corresponding information is returned
         *     when the photo capture is complete.
         * @param { AsyncCallback<CaptureEndInfo> } callback - Callback used to return the result.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        on(type: 'captureEnd', callback: AsyncCallback<CaptureEndInfo>): void;
        /**
         * Unsubscribes from capture end events.
         *
         * @param { 'captureEnd' } type - Event type. The value is fixed at **'captureEnd'**. The event can be listened for
         *     when a photoOutput instance is created.
         * @param { AsyncCallback<CaptureEndInfo> } callback - Callback used to return the result. If this parameter is
         *     specified, the subscription to the specified event with the specified callback is canceled. (The callback
         *     object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the
         *     callbacks are canceled.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        off(type: 'captureEnd', callback?: AsyncCallback<CaptureEndInfo>): void;
        /**
         * Subscribes to capture ready events. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.
         *
         * @param { 'captureReady' } type - Event type. The value is fixed at **'captureReady'**. The event can be listened
         *     for when a photoOutput instance is created. The event is triggered and the corresponding information is
         *     returned when it is ready to take the next photo.
         * @param { AsyncCallback<void> } callback - Callback used to return the result.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        on(type: 'captureReady', callback: AsyncCallback<void>): void;
        /**
         * Unsubscribes from capture ready events.
         *
         * @param { 'captureReady' } type - Event type. The value is fixed at **'captureReady'**. The event can be listened
         *     for when a photoOutput instance is created.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If this parameter is specified, the
         *     subscription to the specified event with the specified callback is canceled. (The callback object cannot be
         *     an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are
         *     canceled.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        off(type: 'captureReady', callback?: AsyncCallback<void>): void;
        /**
         * Subscribes to estimated capture duration events. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.
         *
         * @param { 'estimatedCaptureDuration' } type - Event type. The value is fixed at **'estimatedCaptureDuration'**.
         *     The event can be listened for when a photoOutput instance is created. This event is triggered and the
         *     corresponding information is returned when the photo capture is complete.
         * @param { AsyncCallback<number> } callback - Callback used to return the estimated duration when the sensor
         *     captures frames at the bottom layer in a single capture, measured in units of milliseconds. If **–1** is
         *     reported, there is no estimated duration.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        on(type: 'estimatedCaptureDuration', callback: AsyncCallback<number>): void;
        /**
         * Unsubscribes from estimated capture duration events.
         *
         * @param { 'estimatedCaptureDuration' } type - Event type. The value is fixed at **'estimatedCaptureDuration'**.
         *     The event can be listened for when a photoOutput instance is created.
         * @param { AsyncCallback<number> } callback - Callback used to return the result. If this parameter is specified,
         *     the subscription to the specified event with the specified callback is canceled. (The callback object cannot
         *     be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are
         *     canceled.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        off(type: 'estimatedCaptureDuration', callback?: AsyncCallback<number>): void;
        /**
         * Subscribes to PhotoOutput error events. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.
         *
         * @param { 'error' } type - Event type. The value is fixed at **'error'**. The event can be listened for when a
         *     photoOutput instance is created. This event is triggered and the corresponding error message is returned when
         *     an error occurs during the calling of a photo-related API.
         * @param { ErrorCallback } callback - Callback used to return an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode}.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        on(type: 'error', callback: ErrorCallback): void;
        /**
         * Unsubscribes from PhotoOutput error events.
         *
         * @param { 'error' } type - Event type. The value is fixed at **'error'**. The event can be listened for when a
         *     photoOutput instance is created.
         * @param { ErrorCallback } callback - Callback used to return the result. If this parameter is specified, the
         *     subscription to the specified event with the specified callback is canceled. (The callback object cannot be
         *     an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are
         *     canceled.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        off(type: 'error', callback?: ErrorCallback): void;
        /**
         * Obtains the profile that takes effect currently.
         *
         * @returns { Profile } Profile obtained.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        getActiveProfile(): Profile;
        /**
         * Checks whether taking moving photos is supported.
         *
         * @returns { boolean } Check result for the support of taking moving photos. **true** if supported, **false**
         *     otherwise. If the API call fails, undefined is returned.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        isMovingPhotoSupported(): boolean;
        /**
         * Enables or disables the feature of taking moving photos.
         *
         * @permission ohos.permission.MICROPHONE
         * @param { boolean } enabled - Whether to enable the feature of taking moving photos. **true** to enable, **false**
         *     otherwise.
         * @throws { BusinessError } 201 - permission denied.
         * @throws { BusinessError } 7400101 - Parameter missing or parameter type incorrect.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        enableMovingPhoto(enabled: boolean): void;
        /**
         * Checks whether the specified photo quality prioritization strategy is supported.
         *
         * @param { PhotoQualityPrioritization } qualityPrioritization - Photo quality prioritization strategy.
         * @returns { boolean } Check result for the support of the specified photo quality prioritization strategy.
         *     **true** if supported, **false** otherwise.
         * @throws { BusinessError } 7400201 - Camera service fatal error,
         *     reconfiguring streams is needed to recover from failure.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 21
         */
        isPhotoQualityPrioritizationSupported(qualityPrioritization: PhotoQualityPrioritization): boolean;
        /**
         * Sets the photo quality prioritization strategy.
         * Before setting the strategy, you can call
         * [isPhotoQualityPrioritizationSupported]{@link camera.PhotoOutput.isPhotoQualityPrioritizationSupported} to check
         * whether the device supports the specified photo quality prioritization strategy.
         *
         * @param { PhotoQualityPrioritization } qualityPrioritization - Photo quality prioritization strategy.
         * @throws { BusinessError } 7400201 - Camera service fatal error,
         *     reconfiguring streams is needed to recover from failure.
         * @throws { BusinessError } 7400102 - Operation not allowed.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 21
         */
        setPhotoQualityPrioritization(qualityPrioritization: PhotoQualityPrioritization): void;
        /**
         * Obtains the photo rotation angle.
         *
         * - Device's natural orientation: the default orientation for using a device. For example, the default orientation
         * of the bar-type phone is in portrait mode, with the charging port facing downward.
         * - Camera lens angle: equivalent to the angle at which the camera is rotated clockwise to match the device's
         * natural orientation. For example, the rear camera sensor of a bar-type phone is installed in landscape mode.
         * Therefore, it needs to be rotated by 90 degrees clockwise to match the device's natural orientation.
         *
         * @param { number } deviceDegree - Device rotation angle, measured in degrees, within the range of [0, 360].<br>If the
         *     input value goes beyond this range, the system uses the remainder of the input value divided by 360.<br>Since
         *     API version 23, the input parameter **deviceDegree** is optional. If no parameter is passed, the system
         *     obtains the **deviceDegree** value to calculate the photo rotation angle. [since 12 - 22]
         * @param { number } [deviceDegree] - Device rotation angle, measured in degrees, within the range of [0, 360].<br>If
         *     the input value goes beyond this range, the system uses the remainder of the input value divided by 360.<br>
         *     Since API version 23, the input parameter **deviceDegree** is optional. If no parameter is passed, the system
         *     obtains the **deviceDegree** value to calculate the photo rotation angle. [since 23]
         * @returns { ImageRotation } Rotation angle of the photo. If the API call fails, undefined is returned.
         * @throws { BusinessError } 7400101 - Parameter missing or parameter type incorrect. [since 12 - 22]
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice [since 19]
         * @since 12
         */
        getPhotoRotation(deviceDegree?: number): ImageRotation;
        /**
         * Confirm if auto extended gainmap delivery supported.
         *
         * @returns { boolean } TRUE if the auto extended gainmap delivery is supported.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        isAutoExtendedGainmapDeliverySupported(): boolean;
        /**
         * Enable auto extended gainmap delivery.
         *
         * @param { boolean } enabled - enable auto extended gainmap delivery if TRUE.
         * @throws { BusinessError } 7400102 - Operation not allowed.
         * @throws { BusinessError } 7400103 - Session not config, only throw in session usage.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        enableAutoExtendedGainmapDelivery(enabled: boolean): void;
    }
    /**
     * Describes the frame shutter information.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 10
     */
    interface FrameShutterInfo {
        /**
         * ID of this capture action.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        captureId: number;
        /**
         * Timestamp of the shutter, in milliseconds.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        timestamp: number;
    }
    /**
     * Describes the frame shutter end information during capture.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 12
     */
    interface FrameShutterEndInfo {
        /**
         * ID of this capture action.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        captureId: number;
    }
    /**
     * Describes the capture start information.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 11
     */
    interface CaptureStartInfo {
        /**
         * ID of this capture action.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        captureId: number;
        /**
         * Estimated duration when the sensor captures frames at the bottom layer in a single capture. If **–1** is reported
         * , there is no estimated duration.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 11
         */
        time: number;
    }
    /**
     * Describes the capture end information.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 10
     */
    interface CaptureEndInfo {
        /**
         * ID of this capture action.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        captureId: number;
        /**
         * Number of frames captured.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        frameCount: number;
    }
    /**
     * **VideoOutput** implements output information used in a video session. It inherits from
     * [CameraOutput]{@link camera.CameraOutput}.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 10
     */
    interface VideoOutput extends CameraOutput {
        /**
         * Starts video recording. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If video recording starts
         *     successfully, **err** is **undefined**; otherwise, **err** is an error object with an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode}.
         * @throws { BusinessError } 7400103 - Session not config.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        start(callback: AsyncCallback<void>): void;
        /**
         * Starts video recording. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 7400103 - Session not config.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        start(): Promise<void>;
        /**
         * Stops video recording. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If video recording stops
         *     successfully, **err** is **undefined**; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        stop(callback: AsyncCallback<void>): void;
        /**
         * Stops video recording. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        stop(): Promise<void>;
        /**
         * Checks whether mirror recording is supported.
         *
         * @returns { boolean } Check result for the support of mirror recording. **true** if supported, **false**
         *     otherwise. If the API call fails, undefined is returned.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 15
         */
        isMirrorSupported(): boolean;
        /**
         * Enables or disables mirror recording.
         *
         * - Before calling this API, check whether mirror recording is supported by using
         * [isMirrorSupported]{@link camera.VideoOutput.isMirrorSupported}.
         * - After enabling or disabling mirror recording, call
         * [getVideoRotation]{@link camera.VideoOutput.getVideoRotation} to obtain the rotation angle and
         * [updateRotation]{@link @ohos.multimedia.media:media.AVRecorder.updateRotation} to update the rotation angle.
         *
         * @param { boolean } enabled - Whether to enable mirror recording. **true** to enable, **false** otherwise.
         * @throws { BusinessError } 7400101 - Parameter missing or parameter type incorrect.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 15
         */
        enableMirror(enabled: boolean): void;
        /**
         * Obtains the supported frame rates.
         *
         * @returns { Array<FrameRateRange> } Array of supported frame rates. If the API call fails, undefined is returned.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        getSupportedFrameRates(): Array<FrameRateRange>;
        /**
         * Sets a frame rate range for preview streams. The range must be within the supported frame rate range, which can
         * be obtained by calling [getSupportedFrameRates]{@link camera.PreviewOutput.getSupportedFrameRates}.
         *
         * > **NOTE**
         * >
         * > This API is valid only in [PhotoSession]{@link camera.PhotoSession} or
         * > [VideoSession]{@link camera.VideoSession} mode.
         *
         * @param { number } minFps - Minimum frame rate, in fps. When the maximum value is less than the minimum value, the
         *     API does not take effect.
         * @param { number } maxFps - Maximum frame rate, in fps. When the minimum value is greater than the maximum value, the
         *     API does not take effect.
         * @throws { BusinessError } 7400101 - Parameter missing or parameter type incorrect.
         * @throws { BusinessError } 7400110 - Unresolved conflicts with current configurations.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        setFrameRate(minFps: number, maxFps: number): void;
        /**
         * Obtains the configured frame rate range.
         * This API is valid only after [setFrameRate]{@link camera.PreviewOutput.setFrameRate} is called to set a frame
         * rate range for preview streams.
         *
         * @returns { FrameRateRange } Frame rate range.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        getActiveFrameRate(): FrameRateRange;
        /**
         * Obtains the video rotation angle.
         *
         * - Device's natural orientation: the default orientation for using a device. For example, the default orientation
         * of the bar-type phone is in portrait mode, with the charging port facing downward.
         * - Camera lens angle: equivalent to the angle at which the camera is rotated clockwise to match the device's
         * natural orientation. For example, the rear camera sensor of a bar-type phone is installed in landscape mode.
         * Therefore, it needs to be rotated by 90 degrees clockwise to match the device's natural orientation.
         *
         * @param { number } deviceDegree - Device rotation angle, measured in degrees, within the range of [0, 360].<br>Since
         *     API version 23, the input parameter **deviceDegree** is optional. If no parameter is passed, the system
         *     obtains the **deviceDegree** value to calculate the video rotation angle. [since 12 - 22]
         * @param { number } [deviceDegree] - Device rotation angle, measured in degrees, within the range of [0, 360].<br>
         *     Since API version 23, the input parameter **deviceDegree** is optional. If no parameter is passed, the system
         *     obtains the **deviceDegree** value to calculate the video rotation angle. [since 23]
         * @returns { ImageRotation } Returns the rotation angle of a video. If the API call fails, undefined is returned.
         * @throws { BusinessError } 7400101 - Parameter missing or parameter type incorrect. [since 12 - 22]
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice [since 19]
         * @since 12
         */
        getVideoRotation(deviceDegree?: number): ImageRotation;
        /**
         * Subscribes to preview frame start events. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.
         *
         * @param { 'frameStart' } type - Event type. The value is fixed at **'frameStart'**. The event can be listened for
         *     when a previewOutput instance is created. This event is triggered and returned when the bottom layer starts
         *     exposure for the first time.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. The preview starts as long as this
         *     event is returned.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        on(type: 'frameStart', callback: AsyncCallback<void>): void;
        /**
         * Unsubscribes from preview frame start events.
         *
         * @param { 'frameStart' } type - Event type. The value is fixed at **'frameStart'**. The event can be listened for
         *     when a previewOutput instance is created.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If this parameter is specified, the
         *     subscription to the specified event with the specified callback is canceled. (The callback object cannot be
         *     an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are
         *     canceled.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        off(type: 'frameStart', callback?: AsyncCallback<void>): void;
        /**
         * Subscribes to preview frame end events. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.
         *
         * @param { 'frameEnd' } type - Event type. The value is fixed at **'frameEnd'**. The event can be listened for when
         *     a previewOutput instance is created. This event is triggered and returned when the last frame of preview
         *     ends.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. The preview ends as long as this
         *     event is returned.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        on(type: 'frameEnd', callback: AsyncCallback<void>): void;
        /**
         * Unsubscribes from preview frame end events.
         *
         * @param { 'frameEnd' } type - Event type. The value is fixed at **'frameEnd'**. The event can be listened for when
         *     a previewOutput instance is created.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If this parameter is specified, the
         *     subscription to the specified event with the specified callback is canceled. (The callback object cannot be
         *     an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are
         *     canceled.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        off(type: 'frameEnd', callback?: AsyncCallback<void>): void;
        /**
         * Subscribes to metadata error events. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.
         *
         * @param { 'error' } type - Event type. The value is fixed at **'error'**. The event can be listened for when a
         *     metadataOutput instance is created. This event is triggered and the corresponding error message is returned
         *     when an error occurs during the use of a metadata-related API such as
         *     [start]{@link camera.MetadataOutput.start()} or
         *     [CameraOutput.release]{@link camera.CameraOutput.release()}.
         * @param { ErrorCallback } callback - Callback used to return an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode}.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        on(type: 'error', callback: ErrorCallback): void;
        /**
         * Unsubscribes from metadata error events.
         *
         * @param { 'error' } type - Event type. The value is fixed at **'error'**. The event can be listened for when a
         *     metadataOutput instance is created.
         * @param { ErrorCallback } callback - Callback used to return the result. If this parameter is specified, the
         *     subscription to the specified event with the specified callback is canceled. (The callback object cannot be
         *     an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are
         *     canceled.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        off(type: 'error', callback?: ErrorCallback): void;
        /**
         * Obtains the profile that takes effect currently.
         *
         * @returns { VideoProfile } Profile obtained.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 12
         */
        getActiveProfile(): VideoProfile;
    }
    /**
     * Enumerates the types of metadata objects used for camera detection.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 10
     */
    enum MetadataObjectType {
        /**
         * Metadata object used for face detection.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        FACE_DETECTION = 0,
        /**
         * Metadata object used for human body detection.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 23
         */
        HUMAN_BODY = 1,
        /**
         * Metadata object used for cat face detection.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 26.0.0
         */
        CAT_FACE = 2,
        /**
         * Metadata object used for cat body detection.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 26.0.0
         */
        CAT_BODY = 3,
        /**
         * Metadata object used for dog face detection.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 26.0.0
         */
        DOG_FACE = 4,
        /**
         * Metadata object used for dog body detection.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 26.0.0
         */
        DOG_BODY = 5,
        /**
         * Metadata object used for salient detection.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 26.0.0
         */
        SALIENT_DETECTION = 6,
        /**
         * Barcode detection type.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 26.0.0
         */
        BAR_CODE_DETECTION = 7,
        /**
         * Basic face detection type.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 26.0.0
         */
        BASIC_FACE_DETECTION = 8
    }
    /**
     * Describes a rectangle. The coordinate system for the returned detection points is based on the landscape device
     * orientation, with the charging port on the right. In this coordinate system, the top-left corner is (0, 0), and the
     * bottom-right corner is (1, 1). Here, **topLeftX** and **topLeftY** represent the coordinates of the top-left corner
     * of the rectangle, whereas **width** and **height** represent the width and height of the rectangle, respectively.
     * When cropping or selecting a face region based on specific requirements, the x and y coordinates of the rectangle
     * must be multiplied by the width and height of the actual camera preview output stream to obtain the cropped face
     * region.
     * The width and height of the actual preview stream refer to the resolution of the camera output stream. For details,
     * see **size** in [profile]{@link camera.Profile}.
     * For details about how to obtain the preview stream data, see
     * [Dual-Channel Preview (ArkTS)](docroot://media/camera/camera-dual-channel-preview.md).
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 10
     */
    interface Rect {
        /**
         * X coordinate of the top-left corner of the rectangle, in the range of [0, 1].
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        topLeftX: number;
        /**
         * Y coordinate of the top-left corner of the rectangle, in the range of [0, 1].
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        topLeftY: number;
        /**
         * Width of the rectangle, in the range of [0, 1].
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        width: number;
        /**
         * Height of the rectangle, in the range of [0, 1].
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        height: number;
    }
    /**
     * Enumerates the types of emotions in the detected human face information.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice
     * @since 26.0.0
     */
    enum Emotion {
        /**
         * Quiet and calm.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 26.0.0
         */
        NEUTRAL = 0,
        /**
         * Sad.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 26.0.0
         */
        SADNESS = 1,
        /**
         * Smile.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 26.0.0
         */
        SMILE = 2,
        /**
         * Surprise.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 26.0.0
         */
        SURPRISE = 3
    }
    /**
     * Implements the basic metadata object used for camera detection. It serves as the data source of the camera
     * information in [CameraInput]{@link camera.CameraInput}. It is obtained by calling metadataOutput.
     * [on('metadataObjectsAvailable')]{@link camera.MetadataOutput.on(type: 'metadataObjectsAvailable', callback: AsyncCallback<Array<MetadataObject>>)}.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 10
     */
    interface MetadataObject {
        /**
         * Metadata object type.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        readonly type: MetadataObjectType;
        /**
         * Current timestamp, in nanoseconds (ns).
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        readonly timestamp: number;
        /**
         * Metadata rectangle.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        readonly boundingBox: Rect;
        /**
         * Whether the focus is locked and being tracked currently.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        readonly isLockFocusTracked?: boolean;
    }
    /**
     * Metadata object for basic face.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice
     * @since 26.0.0
     */
    interface MetadataBasicFaceObject extends MetadataObject {
        /**
         * Bounding box for left eye.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 26.0.0
         */
        readonly leftEyeBoundingBox?: Rect;
        /**
         * Bounding box for right eye.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 26.0.0
         */
        readonly rightEyeBoundingBox?: Rect;
        /**
         * Pitch angle for face.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 26.0.0
         */
        readonly pitchAngle?: number;
        /**
         * Yaw angle for face.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 26.0.0
         */
        readonly yawAngle?: number;
        /**
         * Roll angle for face.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 26.0.0
         */
        readonly rollAngle?: number;
    }
    /**
     * Implements the human face metadata object used for camera detection. It inherits from
     * [MetadataObject]{@link camera.MetadataObjectType} and is the data source of the camera information in
     * [CameraInput]{@link camera.CameraInput}. It is obtained by calling metadataOutput.
     * [on('metadataObjectsAvailable')]{@link camera.MetadataOutput.on(type: 'metadataObjectsAvailable', callback: AsyncCallback<Array<MetadataObject>>)}.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice
     * @since 26.0.0
     */
    interface MetadataFaceObject extends MetadataObject {
        /**
         * Left eye area.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 26.0.0
         */
        readonly leftEyeBoundingBox: Rect;
        /**
         * Right eye area.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 26.0.0
         */
        readonly rightEyeBoundingBox: Rect;
        /**
         * Detected emotion.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 26.0.0
         */
        readonly emotion: Emotion;
        /**
         * Confidence of the emotion detection, with a value range of [0, 1].
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 26.0.0
         */
        readonly emotionConfidence: number;
        /**
         * Pitch angle, with a value range of [-90, 90], where downward is positive.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 26.0.0
         */
        readonly pitchAngle: number;
        /**
         * Yaw angle, with a value range of [-90, 90], where rightward is positive.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 26.0.0
         */
        readonly yawAngle: number;
        /**
         * Row angle, with a value range of [-180, 180], where clockwise direction is positive.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 26.0.0
         */
        readonly rollAngle: number;
    }
    /**
     * Implements the human body metadata object used for camera detection. It inherits from
     * [MetadataObject]{@link camera.MetadataObjectType} and is the data source of the camera information in
     * [CameraInput]{@link camera.CameraInput}. It is obtained by calling metadataOutput.
     * [on('metadataObjectsAvailable')]{@link camera.MetadataOutput.on(type: 'metadataObjectsAvailable', callback: AsyncCallback<Array<MetadataObject>>)}.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice
     * @since 26.0.0
     */
    interface MetadataHumanBodyObject extends MetadataObject {
    }
    /**
     * Implements the cat face metadata object used for camera detection. It inherits from
     * [MetadataObject]{@link camera.MetadataObjectType} and is the data source of the camera information in
     * [CameraInput]{@link camera.CameraInput}. It is obtained by calling metadataOutput.
     * [on('metadataObjectsAvailable')]{@link camera.MetadataOutput.on(type: 'metadataObjectsAvailable', callback: AsyncCallback<Array<MetadataObject>>)}.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice
     * @since 26.0.0
     */
    interface MetadataCatFaceObject extends MetadataObject {
        /**
         * Left eye area.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 26.0.0
         */
        readonly leftEyeBoundingBox: Rect;
        /**
         * Right eye area.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 26.0.0
         */
        readonly rightEyeBoundingBox: Rect;
    }
    /**
     * Implements the cat body metadata object used for camera detection. It inherits from
     * [MetadataObject]{@link camera.MetadataObjectType} and is the data source of the camera information in
     * [CameraInput]{@link camera.CameraInput}. It is obtained by calling metadataOutput.
     * [on('metadataObjectsAvailable')]{@link camera.MetadataOutput.on(type: 'metadataObjectsAvailable', callback: AsyncCallback<Array<MetadataObject>>)}.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice
     * @since 26.0.0
     */
    interface MetadataCatBodyObject extends MetadataObject {
    }
    /**
     * Implements the dog face metadata object used for camera detection. It inherits from
     * [MetadataObject]{@link camera.MetadataObjectType} and is the data source of the camera information in
     * [CameraInput]{@link camera.CameraInput}. It is obtained by calling metadataOutput.
     * [on('metadataObjectsAvailable')]{@link camera.MetadataOutput.on(type: 'metadataObjectsAvailable', callback: AsyncCallback<Array<MetadataObject>>)}.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice
     * @since 26.0.0
     */
    interface MetadataDogFaceObject extends MetadataObject {
        /**
         * Left eye area.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 26.0.0
         */
        readonly leftEyeBoundingBox: Rect;
        /**
         * Right eye area.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 26.0.0
         */
        readonly rightEyeBoundingBox: Rect;
    }
    /**
     * Implements the dog body metadata object used for camera detection. It inherits from
     * [MetadataObject]{@link camera.MetadataObjectType} and is the data source of the camera information in
     * [CameraInput]{@link camera.CameraInput}. It is obtained by calling metadataOutput.
     * [on('metadataObjectsAvailable')]{@link camera.MetadataOutput.on(type: 'metadataObjectsAvailable', callback: AsyncCallback<Array<MetadataObject>>)}.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice
     * @since 26.0.0
     */
    interface MetadataDogBodyObject extends MetadataObject {
    }
    /**
     * Implements the salient detection metadata object used for camera detection. It inherits from
     * [MetadataObject]{@link camera.MetadataObjectType} and is the data source of the camera information in
     * [CameraInput]{@link camera.CameraInput}. It is obtained by calling metadataOutput.
     * [on('metadataObjectsAvailable')]{@link camera.MetadataOutput.on(type: 'metadataObjectsAvailable', callback: AsyncCallback<Array<MetadataObject>>)}.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice
     * @since 26.0.0
     */
    interface MetadataSalientDetectionObject extends MetadataObject {
    }
    /**
     * Implements the barcode metadata object used for camera detection. It inherits from
     * [MetadataObject]{@link camera.MetadataObjectType} and is the data source of the camera information in
     * [CameraInput]{@link camera.CameraInput}. It is obtained by calling metadataOutput.
     * [on('metadataObjectsAvailable')]{@link camera.MetadataOutput.on(type: 'metadataObjectsAvailable', callback: AsyncCallback<Array<MetadataObject>>)}.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice
     * @since 26.0.0
     */
    interface MetadataBarcodeObject extends MetadataObject {
    }
    /**
     * Describes the instance returned by the occlusion status callback, which indicates whether the camera lens is
     * blocked or dirty.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice
     * @since 23
     */
    interface CameraOcclusionDetectionResult {
        /**
         * Whether the camera lens is blocked. **true** if blocked, **false** otherwise.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 23
         */
        readonly isCameraOccluded: boolean;
        /**
         * Whether the camera lens is dirty. **true** if dirty, false otherwise.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 23
         */
        readonly isCameraLensDirty: boolean;
    }
    /**
     * Implements metadata streams. It inherits from [CameraOutput]{@link camera.CameraOutput}.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 10
     */
    interface MetadataOutput extends CameraOutput {
        /**
         * Starts to output metadata. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the metadata output starts
         *     successfully, **err** is **undefined**; otherwise, **err** is an error object with an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode}.
         * @throws { BusinessError } 7400103 - Session not config.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        start(callback: AsyncCallback<void>): void;
        /**
         * Starts to output metadata. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 7400103 - Session not config.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        start(): Promise<void>;
        /**
         * Stops outputting metadata. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the metadata output stops
         *     successfully, **err** is **undefined**; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        stop(callback: AsyncCallback<void>): void;
        /**
         * Stops outputting metadata. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        stop(): Promise<void>;
        /**
         * Adds the types of metadata objects to be detected.
         *
         * @param { Array<MetadataObjectType> } types - Metadata object types, which are obtained through
         *     **getSupportedOutputCapability**.
         * @throws { BusinessError } 7400101 - Parameter missing or parameter type incorrect.
         * @throws { BusinessError } 7400103 - Session not config.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 23
         */
        addMetadataObjectTypes(types: Array<MetadataObjectType>): void;
        /**
         * Removes the types of metadata objects to be detected.
         *
         * @param { Array<MetadataObjectType> } types - Metadata object types, which are obtained through
         *     **getSupportedOutputCapability**.
         * @throws { BusinessError } 7400101 - Parameter missing or parameter type incorrect.
         * @throws { BusinessError } 7400103 - Session not config.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice
         * @since 23
         */
        removeMetadataObjectTypes(types: Array<MetadataObjectType>): void;
        /**
         * Subscribes to events indicating available metadata objects. This API uses an asynchronous callback to return the
         * result.
         *
         * > **NOTE**
         * >
         * > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.
         *
         * @param { 'metadataObjectsAvailable' } type - Event type. The value is fixed at **'metadataObjectsAvailable'**.
         *     The event can be listened for when a metadataOutput instance is created.<br>This event is triggered and the
         *     corresponding metadata is returned when valid metadata is detected. If the input field is incorrect, no valid
         *     listening will be created.
         * @param { AsyncCallback<Array<MetadataObject>> } callback - Callback used to return the metadata.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        on(type: 'metadataObjectsAvailable', callback: AsyncCallback<Array<MetadataObject>>): void;
        /**
         * Unsubscribes from events indicating available metadata objects.
         *
         * @param { 'metadataObjectsAvailable' } type - Event type. The value is fixed at **'metadataObjectsAvailable'**.
         *     The event can be listened for when a metadataOutput instance is created.
         * @param { AsyncCallback<Array<MetadataObject>> } callback - Callback used to return the result. If this parameter
         *     is specified, the subscription to the specified event with the specified callback is canceled. (The callback
         *     object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the
         *     callbacks are canceled.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        off(type: 'metadataObjectsAvailable', callback?: AsyncCallback<Array<MetadataObject>>): void;
        /**
         * Subscribes to metadata error events. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > Currently, you cannot use **off()** to unregister the callback in the callback method of **on()**.
         *
         * @param { 'error' } type - Event type. The value is fixed at **'error'**. The event can be listened for when a
         *     metadataOutput instance is created. This event is triggered and the corresponding error message is returned
         *     when an error occurs during the use of a metadata-related API such as
         *     [start]{@link camera.MetadataOutput.start()} or
         *     [CameraOutput.release]{@link camera.CameraOutput.release()}.
         * @param { ErrorCallback } callback - Callback used to return an error code defined in
         *     [CameraErrorCode]{@link camera.CameraErrorCode}.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        on(type: 'error', callback: ErrorCallback): void;
        /**
         * Unsubscribes from metadata error events.
         *
         * @param { 'error' } type - Event type. The value is fixed at **'error'**. The event can be listened for when a
         *     metadataOutput instance is created.
         * @param { ErrorCallback } callback - Callback used to return the result. If this parameter is specified, the
         *     subscription to the specified event with the specified callback is canceled. (The callback object cannot be
         *     an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are
         *     canceled.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 10
         */
        off(type: 'error', callback?: ErrorCallback): void;
        /**
         * Confirm if lock metadata object tracking supported.
         *
         * @returns { boolean } TRUE if the lock metadata object tracking is supported.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        isLockMetadataObjectTrackingSupported(): boolean;
        /**
         * Lock metadata object tracking.
         *
         * @param { Point } point - lock metadata object tracking point.
         * @throws { BusinessError } 7400103 - Session not config, only throw in session usage.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        lockMetadataObjectTracking(point: Point): void;
        /**
         * Unlock metadata object tracking.
         *
         * @throws { BusinessError } 7400103 - Session not config, only throw in session usage.
         * @throws { BusinessError } 7400201 - Camera service fatal error.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        unlockMetadataObjectTracking(): void;
    }
    /**
     * Enumerates the camera concurrency types.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 18
     */
    enum CameraConcurrentType {
        /**
         * Full camera concurrency.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 18
         */
        CAMERA_FULL_CAPABILITY = 1,
        /**
         * Limited camera concurrency.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 18
         */
        CAMERA_LIMITED_CAPABILITY = 0
    }
    /**
     * Describes the camera's concurrency information.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @atomicservice [since 19]
     * @since 18
     */
    interface CameraConcurrentInfo {
        /**
         * Concurrent camera device.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 18
         */
        readonly device: CameraDevice;
        /**
         * Scene mode.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 18
         */
        readonly modes: Array<SceneMode>;
        /**
         * Output capabilities of the camera.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 18
         */
        readonly outputCapabilities: Array<CameraOutputCapability>;
        /**
         * Concurrency type.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @atomicservice [since 19]
         * @since 18
         */
        readonly type: CameraConcurrentType;
    }
    /**
     * Enumerates the optical image stabilization (OIS) mode.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @stagemodelonly
     * @atomicservice
     * @since 24
     */
    enum OISMode {
        /**
         * OIS is disabled.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        OFF = 0,
        /**
         * OIS is automatically controlled.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        AUTO = 1,
        /**
         * OIS is controlled by the application.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        CUSTOM = 2
    }
    /**
     * Enumerates the OIS axes.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @stagemodelonly
     * @atomicservice
     * @since 24
     */
    enum OISAxes {
        /**
         * Pitch axis. It controls the up-down rotation of the camera body, that is, the camera body rotates around the axis
         * horizontal to the lens.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        PITCH = 0,
        /**
         * Yaw axis. It controls the left-right rotation of the camera body, that is, the camera body rotates around the
         * axis perpendicular to the lens.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        YAW = 1
    }
    /**
     * OIS (Optical Image Stabilization) query interface.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @stagemodelonly
     * @atomicservice
     * @since 24
     */
    interface OISQuery {
        /**
         * Checks if the specified OIS mode is supported.
         *
         * @param { OISMode } mode - The OIS mode to check.
         * @returns { boolean } Whether the mode is supported.
         * @throws { BusinessError } 7400102 - Operation not allowed, the inputDevice or the session is abnormal.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        isOISModeSupported(mode: OISMode): boolean;
        /**
         * Gets the supported bias range for the specified OIS axis.
         *
         * @param { OISAxes } oisAxis - The OIS axis.
         * @returns { Array<number> } The bias range.
         * @throws { BusinessError } 7400102 - Operation not allowed, the inputDevice or the session is abnormal.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        getSupportedOISBiasRange(oisAxis: OISAxes): Array<number>;
        /**
         * Gets the bias step for the specified OIS axis.
         *
         * @param { OISAxes } oisAxis - The OIS axis.
         * @returns { number } The bias step value.
         * @throws { BusinessError } 7400102 - Operation not allowed, the inputDevice or the session is abnormal.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        getSupportedOISBiasStep(oisAxis: OISAxes): number;
        /**
         * Gets the current OIS mode.
         *
         * @returns { OISMode } The current OIS mode.
         * @throws { BusinessError } 7400102 - Operation not allowed, the inputDevice or the session is abnormal.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        getCurrentOISMode(): OISMode;
        /**
         * Gets the current custom bias value for the specified OIS axis.
         *
         * @param { OISAxes } oisAxis - The OIS axis
         * @returns { number } The current bias value.
         * @throws { BusinessError } 7400102 - Operation not allowed, the inputDevice or the session is abnormal.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        getCurrentCustomOISBias(oisAxis: OISAxes): number;
    }
    /**
     * OIS (Optical Image Stabilization) interface.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @stagemodelonly
     * @atomicservice
     * @since 24
     */
    interface OIS extends OISQuery {
        /**
         * Sets the OIS mode.
         *
         * @param { OISMode } mode - The OIS mode to set.
         * @throws { BusinessError } 7400102 - Operation not allowed, the inputDevice or the session is abnormal.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        setOISMode(mode: OISMode): void;
        /**
         * Sets custom OIS bias values for each axis.
         *
         * @param { number } pitch - Bias value for pitch axis.
         * @param { number } yaw - Bias value for yaw axis.
         * @throws { BusinessError } 7400102 - Operation not allowed, the inputDevice or the session is abnormal.
         * @throws { BusinessError } 7400103 - Session not config.
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 24
         */
        setOISModeCustom(pitch: number, yaw: number): void;
    }
    /**
     * Enum for automotive camera position.
     *
     * @syscap SystemCapability.Multimedia.Camera.Core
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    enum AutomotiveCameraPosition {
        /**
         * Exterior other position.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        AUTOMOTIVE_CAMERA_POSITION_EXTERIOR_OTHER = 0,
        /**
         * Exterior front position.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        AUTOMOTIVE_CAMERA_POSITION_EXTERIOR_FRONT = 1,
        /**
         * Exterior rear position.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        AUTOMOTIVE_CAMERA_POSITION_EXTERIOR_REAR = 2,
        /**
         * Exterior left position.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        AUTOMOTIVE_CAMERA_POSITION_EXTERIOR_LEFT = 3,
        /**
         * Exterior right position.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        AUTOMOTIVE_CAMERA_POSITION_EXTERIOR_RIGHT = 4,
        /**
         * Interior other position.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        AUTOMOTIVE_CAMERA_POSITION_INTERIOR_OTHER = 5,
        /**
         * Interior left side position of the first row.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        AUTOMOTIVE_CAMERA_POSITION_INTERIOR_ROW_1_LEFT = 6,
        /**
         * Interior center side position of the first row.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        AUTOMOTIVE_CAMERA_POSITION_INTERIOR_ROW_1_CENTER = 7,
        /**
         * Interior right side position of the first row.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        AUTOMOTIVE_CAMERA_POSITION_INTERIOR_ROW_1_RIGHT = 8,
        /**
         * Interior left side position of the second row.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        AUTOMOTIVE_CAMERA_POSITION_INTERIOR_ROW_2_LEFT = 9,
        /**
         * Interior center side position of the second row.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        AUTOMOTIVE_CAMERA_POSITION_INTERIOR_ROW_2_CENTER = 10,
        /**
         * Interior right side position of the second row.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        AUTOMOTIVE_CAMERA_POSITION_INTERIOR_ROW_2_RIGHT = 11,
        /**
         * Interior left side position of the third row.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        AUTOMOTIVE_CAMERA_POSITION_INTERIOR_ROW_3_LEFT = 12,
        /**
         * Interior center side position of the third row.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        AUTOMOTIVE_CAMERA_POSITION_INTERIOR_ROW_3_CENTER = 13,
        /**
         * Interior right side position of the third row.
         *
         * @syscap SystemCapability.Multimedia.Camera.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        AUTOMOTIVE_CAMERA_POSITION_INTERIOR_ROW_3_RIGHT = 14
    }
}
export default camera;

```
