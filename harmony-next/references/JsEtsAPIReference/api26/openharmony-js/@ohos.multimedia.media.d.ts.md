# @ohos.multimedia.media.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
* Copyright (C) 2021-2024 Huawei Device Co., Ltd.
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
 * @kit MediaKit
 */
import { ErrorCallback, AsyncCallback, Callback, BusinessError } from './@ohos.base';
import audio from './@ohos.multimedia.audio';
import photoAccessHelper from './@ohos.file.photoAccessHelper';
import type image from './@ohos.multimedia.image';
import type { SoundPool as _SoundPool } from './multimedia/soundPool';
import type { PlayParameters as _PlayParameters } from './multimedia/soundPool';
import type drm from './@ohos.multimedia.drm';
/**
 * The multimedia subsystem provides a set of simple and easy-to-use APIs for you to access the system and use media
 * resources.
 *
 * @syscap SystemCapability.Multimedia.Media.Core [since 12]
 * @crossplatform [since 12]
 * @atomicservice [since 11]
 * @since 6
 */
declare namespace media {
    /**
     * Creates an AVPlayer instance. This API uses an asynchronous callback to return the result.
     *
     * > **NOTE**
     * >
     * > - You are advised to create a maximum of 16 AVPlayer instances for an application in both audio and video
     * > playback scenarios.<!--Del-->
     * >
     * > - The actual number of instances that can be created may be different. It depends on the specifications of the
     * > device chip in use. For example, in the case of RK3568, you are advised to create a maximum of 6 AVPlayer
     * > instances for an application in audio and video playback scenarios.<!--DelEnd-->
     * >
     * > - Applications must properly manage AVPlayer instances according to their specific needs, creating and freeing
     * > them when necessary. Holding too many AVPlayer instances can lead to high memory usage, and in some cases, the
     * > system might terminate applications to free up resources.
     *
     * @param { AsyncCallback<AVPlayer> } callback - Callback used to return the result. If the operation is successful,
     *     an AVPlayer instance is returned; otherwise, **null** is returned. The instance can be used to play audio and
     *     video.
     * @throws { BusinessError } 5400101 - No memory. Return by callback.
     * @syscap SystemCapability.Multimedia.Media.AVPlayer
     * @crossplatform [since 12]
     * @atomicservice [since 11]
     * @since 9
     */
    function createAVPlayer(callback: AsyncCallback<AVPlayer>): void;
    /**
     * Creates an AVPlayer instance. This API uses a promise to return the result.
     *
     * > **NOTE**
     * >
     * > - You are advised to create a maximum of 16 AVPlayer instances for an application in both audio and video
     * > playback scenarios.<!--Del-->
     * >
     * > - The actual number of instances that can be created may be different. It depends on the specifications of the
     * > device chip in use. For example, in the case of RK3568, you are advised to create a maximum of 6 AVPlayer
     * > instances for an application in audio and video playback scenarios.<!--DelEnd-->
     * >
     * > - Applications should reasonably use AVPlayer objects in accordance with actual service requirements, create them
     * > on demand, and release them in a timely manner. This avoids excessive memory consumption caused by holding too
     * > many AVPlayer instances, which may result in the system terminating the application.
     *
     * @returns { Promise<AVPlayer> } Promise used to return the result. If the operation is successful, an AVPlayer
     *     instance is returned for audio and video playback. Otherwise, **null** is returned.
     * @throws { BusinessError } 5400101 - No memory. Return by promise.
     * @syscap SystemCapability.Multimedia.Media.AVPlayer
     * @crossplatform [since 12]
     * @atomicservice [since 11]
     * @since 9
     */
    function createAVPlayer(): Promise<AVPlayer>;
    /**
     * Creates an AVRecorder instance. This API uses an asynchronous callback to return the result.
     *
     * > **NOTE**
     * >
     * > An application can create multiple AVRecorder instances. However, because the device shares a common audio
     * > channel, only one instance can record audio at a time. Any attempt to create the second instance for audio
     * > recording fails due to audio channel conflicts.
     *
     * @param { AsyncCallback<AVRecorder> } callback - Callback function, which returns an **AVRecorder** instance for
     *     recording audio and video. Otherwise, **null** is returned.
     * @throws { BusinessError } 5400101 - No memory. Return by callback.
     * @syscap SystemCapability.Multimedia.Media.AVRecorder
     * @crossplatform [since 12]
     * @since 9
     */
    function createAVRecorder(callback: AsyncCallback<AVRecorder>): void;
    /**
     * Creates an AVRecorder instance. This API uses a promise to return the result.
     *
     * > **NOTE**
     * >
     * > An application can create multiple AVRecorder instances. However, because the device shares a common audio
     * > channel, only one instance can record audio at a time. Any attempt to create the second instance for audio
     * > recording fails due to audio channel conflicts.
     *
     * @returns { Promise<AVRecorder> } Promise used to return an **AVRecorder** instance, which can be used to record
     *     audio and video. Otherwise, **null** is returned.
     * @throws { BusinessError } 5400101 - No memory. Return by promise.
     * @syscap SystemCapability.Multimedia.Media.AVRecorder
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 9
     */
    function createAVRecorder(): Promise<AVRecorder>;
    /**
     * Creates an AudioPlayer instance in synchronous mode.
     *
     * @returns { AudioPlayer } If the operation is successful, an AudioPlayer instance is returned; otherwise, **null**
     *     is returned. After the instance is created, you can start, pause, or stop audio playback.
     * @syscap SystemCapability.Multimedia.Media.AudioPlayer
     * @since 6
     * @deprecated since 9
     * @useinstead media.createAVPlayer(callback: AsyncCallback<AVPlayer>)
     */
    function createAudioPlayer(): AudioPlayer;
    /**
     * Creates an AudioRecorder instance to control audio recording. Only one AudioRecorder instance can be created per
     * device.
     *
     * @returns { AudioRecorder } If the operation is successful, an AudioRecorder instance is returned; otherwise,
     *     **null** is returned. The instance can be used to record audio.
     * @syscap SystemCapability.Multimedia.Media.AudioRecorder
     * @since 6
     * @deprecated since 9
     * @useinstead media.createAVRecorder(callback: AsyncCallback<AVRecorder>)
     */
    function createAudioRecorder(): AudioRecorder;
    /**
     * Creates a media source from file descriptor.
     *
     * @param { AVFileDescriptor } fdSrc - file descriptor handler.
     *     <br>file descriptor handler.
     * @returns { MediaSource | undefined } MediaSource instance if the operation is successful; returns undefined otherwise.
     * @syscap SystemCapability.Multimedia.Media.Core
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    function createMediaSourceWithFd(fdSrc: AVFileDescriptor): MediaSource | undefined;
    /**
     * Creates a media source from a custom data source.
     *
     * @param { AVDataSrcDescriptor } dataSrc - Interface definition for obtaining media data.
     * @returns { MediaSource | undefined } MediaSource instance if the operation is successful; returns undefined otherwise.
     * @syscap SystemCapability.Multimedia.Media.Core
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    function createMediaSourceWithDataSource(dataSrc: AVDataSrcDescriptor): MediaSource | undefined;
    /**
     * Creates a media source for streaming media to be pre-downloaded.
     *
     * @param { string } url - - URL of the media source. The following streaming media formats are supported: HLS, HTTP-
     *     FLV, DASH, and HTTPS.<br> - FD path of the local M3U8 file.
     * @param { Record<string, string> } headers - HTTP header customized for streaming media pre-download. If this
     *     parameter is not passed, the default HTTP header of the network request is used. [since 12 - 12]
     * @param { Record<string, string> } [headers] - HTTP header customized for streaming media pre-download. If this
     *     parameter is not passed, the default HTTP header of the network request is used. [since 13]
     * @returns { MediaSource } MediaSource instance.
     * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
     *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
     * @throws { BusinessError } 5400101 - No memory.
     * @syscap SystemCapability.Multimedia.Media.Core
     * @atomicservice [since 13]
     * @since 12
     */
    function createMediaSourceWithUrl(url: string, headers?: Record<string, string>): MediaSource;
    /**
     * Creates a multi-bitrate media source for streaming media. Currently, only the HTTP-FLV multi-bitrate media source
     * is supported.
     *
     * @param { Array<MediaStream> } streams - Array of MediaStream objects. The supported streaming media format is HTTP-
     *     FLV.
     * @returns { MediaSource } MediaSource instance.
     * @syscap SystemCapability.Multimedia.Media.Core
     * @atomicservice
     * @since 19
     */
    function createMediaSourceWithStreamData(streams: Array<MediaStream>): MediaSource;
    /**
     * Interface for defining time base metadata
     *
     * @syscap SystemCapability.Multimedia.Media.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    interface AVTimedMetaData {
        /**
         * Defines the unique token of the time base metadata,
         * The tag must be unique in other time metadata of the video source.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        id?: string;
        /**
         * The classification label of the time base metadata.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        classify?: string;
        /**
         * Defines the offset value of the time primitive information relative to the start time of the entire media.
         * The value should be an integer.
         * <br>Unit:milliseconds.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        start: number;
        /**
         * Duration of the time primitive information
         * The value should be an integer.
         * <br>Unit:milliseconds.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        duration: number;
        /**
         * Key-value pair set corresponding to time primitive information
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        contents: Record<string, object>;
    }
    /**
     * Create an ad playback controller associated with the player instance.
     *
     * @param { AVPlayer } player - Created player instance.
     * @returns { Promise<AVAdsController | undefined> } If success, an Controller is returned. Otherwise returns null.
     * @throws { BusinessError } 5400108 - The player object corresponding to player does not exist or is invalid.
     * @syscap SystemCapability.Multimedia.Media.AVPlayer
     * @stagemodelonly
     * @since 26.0.0
     */
    function createAVAdsController(player: AVPlayer): Promise<AVAdsController | undefined>;
    /**
     * Describes the callback function for the ad media resource loading error event.
     *
     * @param { string } adsId - ID of the advertisement resource that fails to be loaded.
     * @param { BusinessError } reason - Indicates the reason of the loading failure.
     * @syscap SystemCapability.Multimedia.Media.AVPlayer
     * @stagemodelonly
     * @since 26.0.0
     */
    type OnAdsEventLoadingErrorHandle = (adsId: string, reason: BusinessError) => void;
    /**
     * Describes the callback function of the ad content playback start event.
     *
     * @param { string } adsId - ID of the ad resource that is being played.
     * @param { number } duration - Playing duration of the advertisement, in milliseconds.
     *     <br>The value should be an integer.
     * @syscap SystemCapability.Multimedia.Media.AVPlayer
     * @stagemodelonly
     * @since 26.0.0
     */
    type OnAdsEventAdsStartedHandle = (adsId: string, duration: number) => void;
    /**
     * Definition of the Ad Content Control Interface
     *
     * @syscap SystemCapability.Multimedia.Media.AVPlayer
     * @stagemodelonly
     * @since 26.0.0
     */
    interface AVAdsController {
        /**
         * Add an advertisement film source to the advertisement controller,
         * The insertion time (relative to the playback progress of the main media asset) can be specified.
         *
         * @param { MediaSource } src - Video source to be inserted into the main content for playback.
         * @param { number } start - Progress value of inserting data to the main media asset.
         *     <br>Unit: milliseconds. The value should be an integer.
         * @returns { Promise<string> } Returns the ID of the added media source in the ad controller.
         * @throws { BusinessError } 5400108 - Insert a media asset whose start value exceeds the value of the main content.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @stagemodelonly
         * @since 26.0.0
         */
        addAdsMediaSource(src: MediaSource, start: number): Promise<string>;
        /**
         * Remove the ad source specified in the AdsController.
         *
         * @param { string } id - UUID value of the MediaSource.
         * @throws { BusinessError } 5400108 - If the specified ID is not in the AdsController.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @stagemodelonly
         * @since 26.0.0
         */
        removeAdsMediaSource(id: string): void;
        /**
         * Skip the ad content that is being played.
         *
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @stagemodelonly
         * @since 26.0.0
         */
        skipCurrentAdsMediaSource(): void;
        /**
         * Disable playback of the remaining broadcast content in the current session
         *
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @stagemodelonly
         * @since 26.0.0
         */
        disableAllAdsMediaSource(): void;
        /**
         * Release the AVAdsController object.
         *
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @stagemodelonly
         * @since 26.0.0
         */
        release(): void;
        /**
         * Registers the event processing function when the ad content fails to be loaded.
         *
         * @param { OnAdsEventLoadingErrorHandle } callback - This function is used to process ad content loading failures.
         *     This function needs to be implemented by the application.
         *     <br>The first parameter is used to transfer the advertisement ID, and the second parameter is used to
         *     transfer the failure cause.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @stagemodelonly
         * @since 26.0.0
         */
        onAdsEventListenerLoadingError(callback: OnAdsEventLoadingErrorHandle): void;
        /**
         * Registers the processing function for the event triggered when a new ad content is played.
         *
         * @param { OnAdsEventAdsStartedHandle } callback - Processing function when the ad content starts to be played.
         *     The logic for switching the playback page is commonly used.
         *     <br>The first parameter indicates the ID of the advertisement that is being played, and the second parameter
         *     indicates the duration of the advertisement.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @stagemodelonly
         * @since 26.0.0
         */
        onAdsListenerAdsStarted(callback: OnAdsEventAdsStartedHandle): void;
        /**
         * Registers the processing function of the event triggered when advertisement is skipped.
         *
         * @param { Callback<string> } callback - Processing function for the advertisement to be jumped out of date. The
         *     parameter is passed as the ID of the skipped advertisement.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @stagemodelonly
         * @since 26.0.0
         */
        onAdsListenerAdsSkipped(callback: Callback<string>): void;
        /**
         * Registers the processing function of the event triggered by the completion of ad content playing.
         *
         * @param { Callback<string> } callback - Processing function of the ad event, which contains the ID of the ad that
         *     is played.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @stagemodelonly
         * @since 26.0.0
         */
        onAdsListenerAdsCompleted(callback: Callback<string>): void;
        /**
         * Unregisters the event processing function when the ad content fails to be loaded.
         *
         * @param { OnAdsEventLoadingErrorHandle } [callback] - Ad content loading failure processing function.
         *     <br>Default value: If this parameter is not specified, all processing functions of the event are
         *     deregistered.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @stagemodelonly
         * @since 26.0.0
         */
        offAdsEventListenerLoadingError(callback?: OnAdsEventLoadingErrorHandle): void;
        /**
         * Unregisters the processing function for the event triggered when a new ad content is played.
         *
         * @param { OnAdsEventAdsStartedHandle } [callback] - Processing function when the ad content starts to be played.
         *     It is usually used to switch the logic of the playback page.
         *     <br>Default value: If this parameter is not specified, all processing functions of the event are
         *     deregistered.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @stagemodelonly
         * @since 26.0.0
         */
        offAdsListenerAdsStarted(callback?: OnAdsEventAdsStartedHandle): void;
        /**
         * Unregisters the processing function of the event triggered when advertisement is skipped.
         *
         * @param { Callback<string> } [callback] - Advertisement Skipped Processing Function.
         *     <br>Default value: If this parameter is not specified, all processing functions of the event are
         *     deregistered.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @stagemodelonly
         * @since 26.0.0
         */
        offAdsListenerAdsSkipped(callback?: Callback<string>): void;
        /**
         * Unregisters the processing function of the event triggered by the completion of ad content playing.
         *
         * @param { Callback<string> } [callback] - Processing function of the advertisement playing completion event.
         *     <br>Default value: If this parameter is not specified, all processing functions of the event are
         *     deregistered.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @stagemodelonly
         * @since 26.0.0
         */
        offAdsListenerAdsCompleted(callback?: Callback<string>): void;
    }
    /**
     * Creates a **VideoPlayer** instance. This API uses an asynchronous callback to return the result.
     *
     * @param { AsyncCallback<VideoPlayer> } callback - Callback used to return the result. If the operation is successful
     *     , **err** is **undefined** and **data** is the VideoPlayer instance created; otherwise, **err** is an error
     *     object.
     * @syscap SystemCapability.Multimedia.Media.VideoPlayer
     * @since 8
     * @deprecated since 9
     * @useinstead media.createAVPlayer(callback: AsyncCallback<AVPlayer>)
     */
    function createVideoPlayer(callback: AsyncCallback<VideoPlayer>): void;
    /**
     * Creates a VideoPlayer instance. This API uses a promise to return the result.
     *
     * @returns { Promise<VideoPlayer> } Promise used to return the result. If the operation is successful, a VideoPlayer
     *     instance is returned; otherwise, **null** is returned. The instance can be used to manage and play video.
     * @syscap SystemCapability.Multimedia.Media.VideoPlayer
     * @since 8
     * @deprecated since 9
     * @useinstead media.createAVPlayer()
     */
    function createVideoPlayer(): Promise<VideoPlayer>;
    /**
     * Creates a SoundPool instance. This API uses an asynchronous callback to return the result.
     *
     * > **NOTE**
     * >
     * > - In versions earlier than API version 18, the bottom layer of the created SoundPool object is in singleton mode.
     * > Therefore, an application process can create only one SoundPool instance.
     * >
     * > - In API version 18 and later, the bottom layer of the created SoundPool object is in multiton mode. Therefore,
     * > an application process can create a maximum of 128 SoundPool instances.
     *
     * @param {number} maxStreams - Maximum number of streams that can be played by the SoundPool instance. The value is
     *     an integer ranging from 1 to 32.
     * @param {audio.AudioRendererInfo} audioRenderInfo - Audio renderer parameters. When the **usage** parameter in
     *     **audioRenderInfo** is set to **STREAM_USAGE_UNKNOWN**, **STREAM_USAGE_MUSIC**, **STREAM_USAGE_MOVIE**, or
     *     **STREAM_USAGE_AUDIOBOOK**, the SoundPool uses the audio mixing mode when playing a short sound, without
     *     interrupting the playback of other audios. SoundPool supports setting **rendererFlags** to **1** for low-
     *     latency playback.
     * @param {AsyncCallback<SoundPool>} callback - Callback used to return the result. If the operation is successful, a
     *     SoundPool instance is returned; otherwise, **null** is returned. The instance is used for loading and playback.
     * @throws { BusinessError } 5400101 - No memory. Return by callback.
     * @syscap SystemCapability.Multimedia.Media.SoundPool
     * @since 10
     */
    function createSoundPool(maxStreams: number, audioRenderInfo: audio.AudioRendererInfo, callback: AsyncCallback<SoundPool>): void;
    /**
     * Creates a SoundPool instance. This API uses a promise to return the result.
     *
     * > **NOTE**
     * >
     * > - In versions earlier than API version 18, the bottom layer of the created SoundPool object is in singleton mode.
     * > Therefore, an application process can create only one SoundPool instance.
     * >
     * > - In API version 18 and later, the bottom layer of the created SoundPool object is in multiton mode. Therefore,
     * > an application process can create a maximum of 128 SoundPool instances.
     *
     * @param {number} maxStreams - Maximum number of streams that can be played by the SoundPool instance. The value is
     *     an integer ranging from 1 to 32.
     * @param {audio.AudioRendererInfo} audioRenderInfo - Audio renderer parameters.
     * @returns {Promise<SoundPool>} Promise used to return the result. If the operation is successful, a SoundPool
     *     instance is returned; otherwise, **null** is returned. The instance is used for loading and playback.
     * @throws { BusinessError } 5400101 - No memory. Return by promise.
     * @syscap SystemCapability.Multimedia.Media.SoundPool
     * @since 10
     */
    function createSoundPool(maxStreams: number, audioRenderInfo: audio.AudioRendererInfo): Promise<SoundPool>;
    /**
     * Creates an AVScreenCaptureRecorder instance. This API uses a promise to return the result.
     *
     * @returns { Promise<AVScreenCaptureRecorder> } Promise used to return the result. If the operation is successful, an
     *     AVScreenCaptureRecorder instance is returned; otherwise, **null** is returned. The instance can be used for
     *     screen capture.
     * @throws { BusinessError } 5400101 - No memory. Return by promise.
     * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
     * @since 12
     */
    function createAVScreenCaptureRecorder(): Promise<AVScreenCaptureRecorder>;
    /**
     * Creates an AVTranscoder instance. This API uses a promise to return the result.
     *
     * > **NOTE**
     * >
     * > A maximum of 2 AVTranscoder instances can be created.
     *
     * @returns {  Promise<AVTranscoder>  } Promise used to return the result. If the operation is successful, an
     *     AVTranscoder instance is returned; otherwise, **null** is returned. The instance can be used for video
     *     transcoding.
     * @throws {  BusinessError  } 5400101 - No memory. Return by promise.
     * @syscap SystemCapability.Multimedia.Media.AVTranscoder
     * @atomicservice [since 22]
     * @since 12
     */
    function createAVTranscoder(): Promise<AVTranscoder>;
    /**
     * SoundPool, which provides APIs for loading, unloading, playing, and stopping playing system sounds, setting the
     * volume, and setting the number of loops.
     *
     * @syscap SystemCapability.Multimedia.Media.SoundPool
     * @since 10
     */
    type SoundPool = _SoundPool;
    /**
     * Describes the playback parameters of the sound pool.
     *
     * @syscap SystemCapability.Multimedia.Media.SoundPool
     * @since 10
     */
    type PlayParameters = _PlayParameters;
    /**
     * Enumerates the interruption modes of the audio files with the same ID in SoundPool.
     *
     * @syscap SystemCapability.Multimedia.Media.SoundPool
     * @stagemodelonly
     * @since 23
     */
    enum SoundInterruptMode {
        /**
         * If the former audio file is not completely played, the latter audio file with the same ID does not interrupt the
         * former audio file. Two audio files are played concurrently.
         *
         * @syscap SystemCapability.Multimedia.Media.SoundPool
         * @stagemodelonly
         * @since 23
         */
        NO_INTERRUPT = 0,
        /**
         * If the former audio file is not completely played, the latter audio file with the same ID interrupts the former
         * audio file.
         *
         * @syscap SystemCapability.Multimedia.Media.SoundPool
         * @stagemodelonly
         * @since 23
         */
        SAME_SOUND_INTERRUPT = 1
    }
    /**
     * Enumerates the reasons for the state transition of the AVPlayer or AVRecorder instance. The enum value is reported
     * together with **state**.
     *
     * @syscap SystemCapability.Multimedia.Media.Core
     * @crossplatform [since 12]
     * @atomicservice [since 11]
     * @since 9
     */
    enum StateChangeReason {
        /**
         * State transition triggered by user behavior. It happens when a user or the client calls an API.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        USER = 1,
        /**
         * State transition caused by background system behavior. For example, if an application does not have the
         * permission of Media Controller, the application is forcibly suspended or stopped by the system when it switches
         * to the background.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        BACKGROUND = 2
    }
    /**
     * Creates an AVMetadataExtractor instance. This API uses a promise to return the result.
     *
     * @returns { Promise<AVMetadataExtractor> } Promise used to return the AVMetadataExtractor instance.
     * @throws { BusinessError } 5400101 - No memory. Returned by promise.
     * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
     * @crossplatform [since 12]
     * @since 11
     */
    function createAVMetadataExtractor(): Promise<AVMetadataExtractor>;
    /**
     * Creates an AVMetadataExtractor instance. This API uses an asynchronous callback to return the result.
     *
     * @param { AsyncCallback<AVMetadataExtractor> } callback - Callback used to return the result. If the operation is
     *     successful, **err** is **undefined** and **data** is the AVMetadataExtractor instance created; otherwise,
     *     **err** is an error object.
     * @throws { BusinessError } 5400101 - No memory. Returned by callback.
     * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
     * @crossplatform [since 12]
     * @since 11
     */
    function createAVMetadataExtractor(callback: AsyncCallback<AVMetadataExtractor>): void;
    /**
     * Creates an AVImageGenerator instance. This API uses a promise to return the result.
     *
     * @returns { Promise<AVImageGenerator> } Promise used to return the result. If the operation is successful, an
     *     AVImageGenerator instance is returned; otherwise, **null** is returned. The API can be used to obtain a video
     *     thumbnail.
     * @throws { BusinessError } 5400101 - No memory. Returned by promise.
     * @syscap SystemCapability.Multimedia.Media.AVImageGenerator
     * @since 12
     */
    function createAVImageGenerator(): Promise<AVImageGenerator>;
    /**
     * Creates an AVImageGenerator instance. This API uses an asynchronous callback to return the result.
     *
     * @param { AsyncCallback<AVImageGenerator> } callback - Callback used to return the result. If the operation is
     *     successful, an AVImageGenerator instance is returned; otherwise, **null** is returned. The API can be used to
     *     obtain a video thumbnail.
     * @throws { BusinessError } 5400101 - No memory. Returned by callback.
     * @syscap SystemCapability.Multimedia.Media.AVImageGenerator
     * @since 12
     */
    function createAVImageGenerator(callback: AsyncCallback<AVImageGenerator>): void;
    /**
     * AVMetadataExtractor is a class for metadata retrieval. It provides APIs to obtain metadata and thumbnails from
     * media assets. Before calling any API of AVMetadataExtractor, you must use
     * [media.createAVMetadataExtractor]{@link @ohos.multimedia.media:media.createAVMetadataExtractor(callback: AsyncCallback<AVMetadataExtractor>)}
     * to create an AVMetadataExtractor instance.
     *
     * For details about the demo of obtaining audio or video metadata and video thumbnails, see
     * [Using AVMetadataExtractor to Extract Audio and Video Metadata (ArkTS)](docroot://media/media/avmetadataextractor.md).
     *
     *
     * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
     * @crossplatform [since 12]
     * @since 11
     */
    interface AVMetadataExtractor {
        /**
         * Media file descriptor, which specifies the data source. Before obtaining metadata, you must set the data source
         * through either **fdSrc** or **dataSrc**.
         *
         * There is a media file that stores continuous assets, the address offset is 0, and the byte length is 100. Its
         * file descriptor is **AVFileDescriptor { fd = resourceHandle; offset = 0; length = 100; }**.
         *
         * **NOTE**
         *
         * After the resource handle (FD) is transferred to an AVMetadataExtractor instance, do not use the resource handle
         * to perform other read and write operations, including but not limited to transferring this handle to other
         * AVPlayer, AVMetadataExtractor, AVImageGenerator, or AVTranscoder instance. Competition occurs when multiple
         * AVMetadataExtractor use the same resource handle to read and write files at the same time, resulting in errors in
         * obtaining data.
         *
         * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
         * @crossplatform [since 12]
         * @since 11
         */
        fdSrc?: AVFileDescriptor;
        /**
         * Streaming media resource descriptor, which specifies the data source. Before obtaining metadata, you must set the
         * data source through either **fdSrc** or **dataSrc**.
         *
         * When an application obtains a media file from the remote, you can set **dataSrc** to obtain the metadata before
         * the application finishes the downloading.
         *
         * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
         * @crossplatform [since 12]
         * @since 11
         */
        dataSrc?: AVDataSrcDescriptor;
        /**
         * Obtains the media metadata. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<AVMetadata> } callback - Callback used to return the result, which is an AVMetadata
         *     instance.
         * @throws { BusinessError } 5400102 - Operation not allowed. Returned by callback.
         * @throws { BusinessError } 5400106 - Unsupported format. Returned by callback.
         * @throws { BusinessError } 5411012 - Http cleartext traffic is not permitted. [since 23]
         * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
         * @crossplatform [since 12]
         * @since 11
         */
        fetchMetadata(callback: AsyncCallback<AVMetadata>): void;
        /**
         * Obtains the media metadata. This API uses a promise to return the result.
         *
         * @returns { Promise<AVMetadata> } Promise used to return the result, which is an AVMetadata instance.
         * @throws { BusinessError } 5400102 - Operation not allowed. Returned by promise.
         * @throws { BusinessError } 5400106 - Unsupported format. Returned by promise.
         * @throws { BusinessError } 5411012 - Http cleartext traffic is not permitted. [since 23]
         * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
         * @crossplatform [since 12]
         * @since 11
         */
        fetchMetadata(): Promise<AVMetadata>;
        /**
         * Obtains the media metadata. You can set the maximum timeout interval (**timeoutMs**) for obtaining the metadata.
         * This API uses a promise to return the result.
         *
         * @param { number } timeoutMs - Timeout interval for obtaining media metadata. The value range is (0, 20000], in
         *     milliseconds.<br>If no metadata is returned within the specified timeout interval, error code 5400104 is
         *     returned.
         * @returns { Promise<AVMetadata | undefined> } Promise used to return the audio and video metadata object (
         *     **AVMetadata**) asynchronously.
         * @throws { BusinessError } 5400102 - Operation not allowed. Returned by promise.
         * @throws { BusinessError } 5400104 - Operation timeout.
         * @throws { BusinessError } 5400106 - Unsupported format. Returned by promise.
         * @throws { BusinessError } 5400108 - Parameter check failed. Returned by promise.
         * @throws { BusinessError } 5411012 - Http cleartext traffic is not permitted.
         * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
         * @stagemodelonly
         * @since 26.0.0
         */
        fetchMetadataWithTimeout(timeoutMs: number): Promise<AVMetadata | undefined>;
        /**
         * Obtains the cover of the audio album. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<image.PixelMap> } callback - Callback used to return the album cover.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by callback.
         * @throws { BusinessError } 5400106 - Unsupported format. Returned by callback.
         * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
         * @crossplatform [since 12]
         * @since 11
         */
        fetchAlbumCover(callback: AsyncCallback<image.PixelMap>): void;
        /**
         * Obtains the cover of the audio album. This API uses a promise to return the result.
         *
         * @returns { Promise<image.PixelMap> } Promise used to return the album cover.
         * @throws { BusinessError } 5400102 - Operation not allowed. Returned by promise.
         * @throws { BusinessError } 5400106 - Unsupported format. Returned by promise.
         * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
         * @crossplatform [since 12]
         * @since 11
         */
        fetchAlbumCover(): Promise<image.PixelMap>;
        /**
         * Sets the data source for a network on-demand resource. Only network metadata (
         * [fetchMetadata]{@link media.AVMetadataExtractor.fetchMetadata(callback: AsyncCallback<AVMetadata>)}) and
         * thumbnails (
         * [fetchFrameByTime]{@link media.AVMetadataExtractor.fetchFrameByTime(timeUs: number, options: AVImageQueryOptions, param: PixelMapParams)}
         * ) can be obtained. The media resource URL must be set before the retrieval.
         *
         * @param { string } url - URL of the media resource.<br>1. The video formats MP4, MPEG-TS, and MKV are supported.<
         *     br>2. The audio formats M4A, AAC, MP3, OGG, WAV, FLAC, and AMR are supported.<br>
         *     **Example of supported URLs**:<br>1. HTTP: http://xx<br>2. HTTPS: https://xx<br>Note: HLS/DASH and live
         *     streaming resources are not supported.
         * @param { Record<string, string> } [headers] - Custom HTTP headers for accessing the network resource. The default
         *     value is empty.
         * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
         * @since 20
         */
        setUrlSource(url: string, headers?: Record<string, string>): void;
        /**
         * Obtains a video thumbnail. This API uses a promise to return the result.
         *
         * @param { number } timeUs - Time of the video for which a thumbnail is to be obtained, in us.
         * @param { AVImageQueryOptions } options - Relationship between the time passed in and the video frame.
         * @param { PixelMapParams } param - Format parameters of the thumbnail to be obtained.
         * @returns { Promise<image.PixelMap> } Promise used to return the video thumbnail.
         * @throws { BusinessError } 5400102 - Operation not allowed. Returned by promise.
         * @throws { BusinessError } 5400106 - Unsupported format. Returned by promise.
         * @throws { BusinessError } 5400108 - Parameter check failed. Returned by promise.
         * @throws { BusinessError } 5411012 - Http cleartext traffic is not permitted. [since 23]
         * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
         * @since 20
         */
        fetchFrameByTime(timeUs: number, options: AVImageQueryOptions, param: PixelMapParams): Promise<image.PixelMap>;
        /**
         * Obtains a video thumbnail. You can set the maximum timeout interval (**timeoutMs**) for obtaining the thumbnail.
         * This API uses a promise to return the result.
         *
         * @param { number } timeUs - Time of the video for which a thumbnail is to be obtained, in μs.
         * @param { AVImageQueryOptions } options - Relationship between the time passed in and the video frame.
         * @param { PixelMapParams } param - Format parameters of the thumbnail to be obtained.
         * @param { number } timeoutMs - Timeout interval for obtaining the thumbnail. The value range is (0, 20000], in
         *     milliseconds.<br>If the thumbnail is not obtained within the specified timeout interval, error code 5400104
         *     is returned.
         * @returns { Promise<image.PixelMap | undefined> } Promise used to return the video thumbnail.
         * @throws { BusinessError } 5400102 - Operation not allowed. Returned by promise.
         * @throws { BusinessError } 5400104 - Operation timeout.
         * @throws { BusinessError } 5400106 - Unsupported format. Returned by promise.
         * @throws { BusinessError } 5400108 - Parameter check failed. Returned by promise.
         * @throws { BusinessError } 5411012 - Http cleartext traffic is not permitted.
         * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
         * @stagemodelonly
         * @since 26.0.0
         */
        fetchFrameByTimeWithTimeout(timeUs: number, options: AVImageQueryOptions, param: PixelMapParams, timeoutMs: number): Promise<image.PixelMap | undefined>;
        /**
         * Obtains video thumbnails in batches. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > - The given video resource is decoded first, and then image frames are extracted from each time point in the
         * > **timesUs** array based on the provided **options** and **param**.
         * >
         * > - When each image extraction is complete, the system calls the callback function and passes the extraction
         * > result. Note that the execution order of the callback function may be inconsistent with the time points in the
         * > **timesUs** array.
         *
         * @param { number[] } timesUs - Set of time points of all thumbnails to be obtained in the video.<br>The unit is
         *     microsecond (μs), and the value range of the array length is (0, 4096].
         * @param { AVImageQueryOptions } queryOption - Relationship between the time passed in and the video frame.
         * @param { PixelMapParams } param - Format parameters of the thumbnail to be obtained.
         * @param { OnFrameFetched } callback - Thumbnail information to be returned and possible exception types.<br>For
         *     details about the exception types, see the returned error code information.
         * @throws { BusinessError } 5400102 - Operation not allowed. Returned by callback.
         * @throws { BusinessError } 5400104 - Fetch timeout, Returned by callback.
         * @throws { BusinessError } 5400106 - Unsupported format. Returned by callback.
         * @throws { BusinessError } 5400105 - Service died.
         * @throws { BusinessError } 5400108 - Parameter check failed. e.g. The size of timesUs is larger than 4096.
         * @throws { BusinessError } 5411012 - Http cleartext not permitted.
         * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
         * @stagemodelonly
         * @since 23
         */
        fetchFramesByTimes(timesUs: number[], queryOption: AVImageQueryOptions, param: PixelMapParams, callback: OnFrameFetched): void;
        /**
         * Obtains video thumbnails in batches. You can set the maximum timeout interval (**timeoutMs**) for obtaining each
         * thumbnail. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > - The given video resource is decoded first, and then image frames are extracted from each time point in the
         * > **timesUs** array based on the provided **options** and **param**.
         * >
         * > - When each image extraction is complete, the system calls the callback function and passes the extraction
         * > result. Note that the execution order of the callback function may be inconsistent with the time points in the
         * > **timesUs** array.
         * >
         * > - The **timeoutMs** parameter indicates the maximum timeout interval for obtaining each thumbnail frame, not
         * > the entire batch thumbnail extraction process.
         *
         * @param { number[] } timesUs - Set of time points of all thumbnails to be obtained in the video.<br>The unit is
         *     microsecond (μs), and the value range of the array length is (0, 4096].
         * @param { AVImageQueryOptions } queryOption - Relationship between the time passed in and the video frame.
         * @param { PixelMapParams } param - Format parameters of the thumbnail to be obtained.
         * @param { number } timeoutMs - Timeout interval for obtaining each thumbnail. The value range is (0, 20000], in
         *     milliseconds.<br>If a thumbnail is not obtained within the specified timeout interval, error code 5400104 is
         *     returned.
         * @param { OnFrameFetched } callback - Thumbnail information to be returned and possible exception types.<br>For
         *     details about the exception types, see the returned error code information.
         * @throws { BusinessError } 5400102 - Operation not allowed. Returned by callback.
         * @throws { BusinessError } 5400104 - Fetch timeout, Returned by callback.
         * @throws { BusinessError } 5400106 - Unsupported format. Returned by callback.
         * @throws { BusinessError } 5400105 - Service died.
         * @throws { BusinessError } 5400108 - Parameter check failed. e.g. The size of timesUs is larger than 4096.
         * @throws { BusinessError } 5411012 - Http cleartext not permitted.
         * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
         * @stagemodelonly
         * @since 26.0.0
         */
        fetchFramesByTimesWithTimeout(timesUs: number[], queryOption: AVImageQueryOptions, param: PixelMapParams, timeoutMs: number, callback: OnFrameFetched): void;
        /**
         * Cancels the ongoing task of obtaining thumbnails in batches. (The thumbnails that have been obtained are not
         * affected.)
         *
         * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
         * @stagemodelonly
         * @since 23
         */
        cancelAllFetchFrames(): void;
        /**
         * Releases this AVMetadataExtractor instance. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @throws { BusinessError } 5400102 - Operation not allowed. Returned by callback.
         * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
         * @crossplatform [since 12]
         * @since 11
         */
        release(callback: AsyncCallback<void>): void;
        /**
         * Releases this AVMetadataExtractor instance. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 5400102 - Operation not allowed. Returned by promise.
         * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
         * @crossplatform [since 12]
         * @since 11
         */
        release(): Promise<void>;
    }
    /**
     * Defines the audio and video metadata. Parameters that are not declared as read-only in
     * [AVRecorderConfig]{@link #AVRecorderConfig} can be used as input parameters for recording of
     * [AVRecorder]{@link #AVRecorder}.
     *
     * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
     * @crossplatform [since 12]
     * @since 11
     */
    interface AVMetadata {
        /**
         * Title of the album. This parameter is not supported in AVRecorder settings.
         *
         * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
         * @crossplatform [since 12]
         * @since 11
         */
        album?: string;
        /**
         * Artist of the album. This parameter is not supported in AVRecorder settings.
         *
         * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
         * @crossplatform [since 12]
         * @since 11
         */
        albumArtist?: string;
        /**
         * Artist of the media asset. This parameter is not supported in AVRecorder settings.
         *
         * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
         * @crossplatform [since 12]
         * @since 11
         */
        artist?: string;
        /**
         * Author of the media asset. This parameter is not supported in AVRecorder settings.
         *
         * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
         * @crossplatform [since 12]
         * @since 11
         */
        author?: string;
        /**
         * Time when the media asset is created. This parameter is not supported in AVRecorder settings.
         *
         * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
         * @crossplatform [since 12]
         * @since 11
         */
        dateTime?: string;
        /**
         * Time when the media asset is created. The value is in the YYYY-MM-DD HH:mm:ss format.
         * This parameter is not supported in AVRecorder settings.
         *
         * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
         * @crossplatform [since 12]
         * @since 11
         */
        dateTimeFormat?: string;
        /**
         * Composer of the media asset. This parameter is not supported in AVRecorder settings.
         *
         * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
         * @crossplatform [since 12]
         * @since 11
         */
        composer?: string;
        /**
         * Duration of the media asset. This parameter is not supported in AVRecorder settings.
         *
         * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
         * @crossplatform [since 12]
         * @since 11
         */
        duration?: string;
        /**
         * Type or genre of the media asset.
         *
         * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
         * @crossplatform [since 12]
         * @since 11
         */
        genre?: string;
        /**
         * Whether the media asset contains audio. This parameter is not supported in AVRecorder settings.
         *
         * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
         * @crossplatform [since 12]
         * @since 11
         */
        hasAudio?: string;
        /**
         * Whether the media asset contains a video. This parameter is not supported in AVRecorder settings.
         *
         * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
         * @crossplatform [since 12]
         * @since 11
         */
        hasVideo?: string;
        /**
         * MIME type of the media asset. This parameter is not supported in AVRecorder settings.
         * Some example mime types include: "video/mp4", "audio/mp4", "audio/amr-wb".
         *
         * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
         * @crossplatform [since 12]
         * @since 11
         */
        mimeType?: string;
        /**
         * Number of tracks of the media asset. This parameter is not supported in AVRecorder settings.
         *
         * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
         * @crossplatform [since 12]
         * @since 11
         */
        trackCount?: string;
        /**
         * Audio sampling rate, in Hz. This parameter is not supported in AVRecorder settings.
         *
         * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
         * @crossplatform [since 12]
         * @since 11
         */
        sampleRate?: string;
        /**
         * Title of the media asset. This parameter is not supported in AVRecorder settings.
         * This parameter is read-only in the current version.
         *
         * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
         * @crossplatform [since 12]
         * @since 11
         */
        title?: string;
        /**
       * Description of the media asset. This parameter is not supported in AVRecorder settings.
       *
       * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
       * @since 23
       */
        description?: string;
        /**
         * Video height, in px. This parameter is not supported in AVRecorder settings.
         *
         * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
         * @crossplatform [since 12]
         * @since 11
         */
        videoHeight?: string;
        /**
         * Video width, in px. This parameter is not supported in AVRecorder settings.
         *
         * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
         * @crossplatform [since 12]
         * @since 11
         */
        videoWidth?: string;
        /**
         * Video rotation direction, in degrees.
         *
         * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
         * @crossplatform [since 12]
         * @since 11
         */
        videoOrientation?: string;
        /**
         * HDR type of the media asset. This parameter is not supported in AVRecorder settings.
         *
         * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
         * @crossplatform
         * @since 12
         */
        hdrType?: HdrType;
        /**
         * Geographical location of the media asset.
         *
         * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
         * @since 12
         */
        location?: Location;
        /**
         * Custom key-value mappings obtained from **moov.meta.list**.
         *
         * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
         * @since 12
         */
        customInfo?: Record<string, string>;
        /**
         * Tracks info of the media asset. This parameter is not supported in AVRecorder settings.
         *
         * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
         * @since 20
         */
        tracks?: Array<MediaDescription>;
        /**
         * The identifier that represents the software or hardware and settings used for encoding.
         * This parameter is not supported in AVRecorder settings.
         *
         * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
         * @stagemodelonly
         * @since 26.0.0
         */
        encoder?: string;
    }
    /**
     * This interface is used to define the output image size.
     *
     * @syscap SystemCapability.Multimedia.Media.AVImageGenerator
     * @since 20
     */
    interface OutputSize {
        /**
         * The expected output frame image width.
         * If the value is less than 0, the width will be the orginal width of the video.
         * If the value is 0 or no value is assigned, the scaling ratio will follow the specified height.
         * If both width and height is not assigned, the output will be the original size of video frame.
         *
         * @syscap SystemCapability.Multimedia.Media.AVImageGenerator
         * @since 20
         */
        width?: number;
        /**
         * The expected output frame image height.
         * If the value is less than 0, the height will be the orginal height of the video.
         * If the value is 0 or no value is assigned, the scaling ratio will follow the specified width.
         * If both width and height is not assigned, the output will be the original size of video frame.
         *
         * @syscap SystemCapability.Multimedia.Media.AVImageGenerator
         * @since 20
         */
        height?: number;
    }
    /**
     * Enumerates the HDR types.
     *
     * @syscap SystemCapability.Multimedia.Media.Core
     * @crossplatform
     * @since 12
     */
    enum HdrType {
        /**
         * No HDR.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform
         * @since 12
         */
        AV_HDR_TYPE_NONE = 0,
        /**
         * HDR VIVID.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform
         * @since 12
         */
        AV_HDR_TYPE_VIVID = 1
    }
    /**
     * AVImageGenerator is a class for video thumbnail retrieval. It provides APIs to obtain a thumbnail from a video.
     * Before calling any API in AVImageGenerator, you must use
     * [createAVImageGenerator()]{@link @ohos.multimedia.media:media.createAVImageGenerator(callback: AsyncCallback<AVImageGenerator>)}
     * to create an AVImageGenerator instance.
     *
     * For details about the demo for obtaining video thumbnails, see
     * [Obtaining Video Thumbnails](docroot://media/media/avimagegenerator.md).
     *
     * @syscap SystemCapability.Multimedia.Media.AVImageGenerator
     * @since 12
     */
    interface AVImageGenerator {
        /**
         * Media file descriptor, which specifies the data source.
         *
         * There is a media file that stores continuous assets, the address offset is 0, and the byte length is 100. Its
         * file descriptor is **AVFileDescriptor { fd = resourceHandle; offset = 0; length = 100; }**.
         *
         * **NOTE**
         *
         * After the resource handle (FD) is transferred to an AVImageGenerator instance, do not use the resource handle to
         * perform other read and write operations, including but not limited to transferring this handle to other AVPlayer,
         * AVMetadataExtractor, AVImageGenerator, or AVTranscoder instance. Competition occurs when multiple
         * AVImageGenerator use the same resource handle to read and write files at the same time, resulting in errors in
         * obtaining data.
         *
         * @syscap SystemCapability.Multimedia.Media.AVImageGenerator
         * @since 12
         */
        fdSrc?: AVFileDescriptor;
        /**
         * Obtains a video thumbnail. This API uses an asynchronous callback to return the result.
         *
         * @param { number } timeUs - Time of the video for which a thumbnail is to be obtained, in μs.
         * @param { AVImageQueryOptions } options - Relationship between the thumbnail timestamp in and the video frame.
         * @param { PixelMapParams } param - Format parameters of the thumbnail to be obtained.
         * @param { AsyncCallback<image.PixelMap> } callback - Callback used to return the result. If the operation is
         *     successful, **err** is **undefined** and **data** is the PixelMap instance obtained; otherwise, **err** is an
         *     error object.
         * @throws { BusinessError } 5400102 - Operation not allowed. Returned by callback.
         * @throws { BusinessError } 5400106 - Unsupported format. Returned by callback.
         * @syscap SystemCapability.Multimedia.Media.AVImageGenerator
         * @since 12
         */
        fetchFrameByTime(timeUs: number, options: AVImageQueryOptions, param: PixelMapParams, callback: AsyncCallback<image.PixelMap>): void;
        /**
         * Obtains a video thumbnail. This API uses a promise to return the result.
         *
         * @param { number } timeUs - Time of the video for which a thumbnail is to be obtained, in μs.
         * @param { AVImageQueryOptions } options - Relationship between the thumbnail timestamp in and the video frame.
         * @param { PixelMapParams } param - Format parameters of the thumbnail to be obtained.
         * @returns { Promise<image.PixelMap> } Promise used to return the video thumbnail.
         * @throws { BusinessError } 5400102 - Operation not allowed. Returned by promise.
         * @throws { BusinessError } 5400106 - Unsupported format. Returned by promise.
         * @syscap SystemCapability.Multimedia.Media.AVImageGenerator
         * @since 12
         */
        fetchFrameByTime(timeUs: number, options: AVImageQueryOptions, param: PixelMapParams): Promise<image.PixelMap>;
        /**
         * Fetches a scaled thumbnail from the video at a particular timestamp. This API uses a promise to return the
         * result.
         *
         * @param { number } timeUs - Timestamp, in microseconds (μs), at which the thumbnail is to be fetched from the
         *     video.
         * @param { AVImageQueryOptions } queryMode - Relationship between the thumbnail timestamp in and the video frame.
         * @param { OutputSize } outputSize - Output size of the thumbnail. By default, the original image size is used.
         * @returns { Promise<image.PixelMap> } Promise used to return the video thumbnail.
         * @throws { BusinessError  } 5400102 Operation not allowed. Returned by promise.
         * @throws { BusinessError  } 5400106 Unsupported format. Returned by promise.
         * @syscap SystemCapability.Multimedia.Media.AVImageGenerator
         * @since 20
         */
        fetchScaledFrameByTime(timeUs: number, queryMode: AVImageQueryOptions, outputSize?: OutputSize): Promise<image.PixelMap>;
        /**
         * Releases this AVImageGenerator instance. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @throws { BusinessError } 5400102 - Operation not allowed. Returned by callback.
         * @syscap SystemCapability.Multimedia.Media.AVImageGenerator
         * @since 12
         */
        release(callback: AsyncCallback<void>): void;
        /**
         * Releases this AVImageGenerator instance. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 5400102 - Operation not allowed. Returned by promise.
         * @syscap SystemCapability.Multimedia.Media.AVImageGenerator
         * @since 12
         */
        release(): Promise<void>;
    }
    /**
     * Enumerates the relationship between the video frame and the time at which the video thumbnail is obtained.
     *
     * The time passed in for obtaining the thumbnail may be different from the time of the video frame for which the
     * thumbnail is actually obtained. Therefore, you need to specify their relationship.
     *
     * @syscap SystemCapability.Multimedia.Media.AVImageGenerator
     * @since 12
     */
    enum AVImageQueryOptions {
        /**
         * The key frame at or next to the specified time is selected.
         *
         * @syscap SystemCapability.Multimedia.Media.AVImageGenerator
         * @since 12
         */
        AV_IMAGE_QUERY_NEXT_SYNC = 0,
        /**
         * The key frame at or prior to the specified time is selected.
         *
         * @syscap SystemCapability.Multimedia.Media.AVImageGenerator
         * @since 12
         */
        AV_IMAGE_QUERY_PREVIOUS_SYNC,
        /**
         * The key frame closest to the specified time is selected.
         *
         * @syscap SystemCapability.Multimedia.Media.AVImageGenerator
         * @since 12
         */
        AV_IMAGE_QUERY_CLOSEST_SYNC,
        /**
         * The frame (not necessarily a key frame) closest to the specified time is selected.
         *
         * @syscap SystemCapability.Multimedia.Media.AVImageGenerator
         * @since 12
         */
        AV_IMAGE_QUERY_CLOSEST
    }
    /**
     * Defines the format parameters of the video thumbnail to be obtained.
     *
     * @syscap SystemCapability.Multimedia.Media.AVImageGenerator
     * @since 12
     */
    interface PixelMapParams {
        /**
         * Width of the thumbnail. Unit: px.
         * The value must be greater than 0 and less than or equal to the width of the original video.
         * Otherwise, the returned thumbnail will not be scaled.
         *
         * @syscap SystemCapability.Multimedia.Media.AVImageGenerator
         * @since 12
         */
        width?: number;
        /**
         * Height of the thumbnail. Unit: px.
         * The value must be greater than 0 and less than or equal to the height of the original video.
         * Otherwise, the returned thumbnail will not be scaled.
         *
         * @syscap SystemCapability.Multimedia.Media.AVImageGenerator
         * @since 12
         */
        height?: number;
    }
    /**
     * Enumerates the results of obtaining thumbnails in batches.
     *
     * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
     * @stagemodelonly
     * @since 23
     */
    enum FetchResult {
        /**
         * Failed to obtain the thumbnail from the video.
         *
         * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
         * @stagemodelonly
         * @since 23
         */
        FETCH_FAILED = 0,
        /**
         * Succeeded in obtaining the thumbnail from the video.
         *
         * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
         * @stagemodelonly
         * @since 23
         */
        FETCH_SUCCEEDED = 1,
        /**
         * The operation of obtaining the thumbnail from the video is canceled.
         *
         * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
         * @stagemodelonly
         * @since 23
         */
        FETCH_CANCELED = 2
    }
    /**
     * Defines the frame info when fetch picture form a video.
     *
     * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
     * @stagemodelonly
     * @since 23
     */
    interface FrameInfo {
        /**
         * The requested frame time.
         *
         * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
         * @stagemodelonly
         * @since 23
         */
        requestedTimeUs: number;
        /**
         * The actual frame time.
         *
         * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
         * @stagemodelonly
         * @since 23
         */
        actualTimeUs?: number;
        /**
         * The image extracted from video.
         *
         * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
         * @stagemodelonly
         * @since 23
         */
        image?: image.PixelMap;
        /**
         * The fetch result code - succeed, failed or cancelled.
         *
         * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
         * @stagemodelonly
         * @since 23
         */
        result: FetchResult;
    }
    /**
     * Describes the callback invoked when thumbnails are obtained in batches.
     *
     * @param { FrameInfo } frameInfo - Thumbnail information.
     * @param { BusinessError<void> } [err] - Error that occurs when the thumbnail is obtained. The default value is
     *     **null**.
     * @syscap SystemCapability.Multimedia.Media.AVMetadataExtractor
     * @stagemodelonly
     * @since 23
     */
    type OnFrameFetched = (frameInfo: FrameInfo, err?: BusinessError<void>) => void;
    /**
     * Enumerates the types of [Media error codes](docroot://reference/apis-media-kit/errorcode-media.md).
     *
     * @syscap SystemCapability.Multimedia.Media.Core
     * @crossplatform [since 12]
     * @atomicservice [since 11]
     * @since 9
     */
    enum AVErrorCode {
        /**
         * The operation is successful.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        AVERR_OK = 0,
        /**
         * No permission to perform the operation.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        AVERR_NO_PERMISSION = 201,
        /**
         * Invalid input parameter.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        AVERR_INVALID_PARAMETER = 401,
        /**
         * Unsupported API.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        AVERR_UNSUPPORT_CAPABILITY = 801,
        /**
         * The system memory is insufficient or the number of services reaches the upper limit.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        AVERR_NO_MEMORY = 5400101,
        /**
         * The operation is not allowed in the current state or you do not have the permission to perform the operation.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        AVERR_OPERATE_NOT_PERMIT = 5400102,
        /**
         * The data stream is abnormal.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        AVERR_IO = 5400103,
        /**
         * The system or network response times out.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        AVERR_TIMEOUT = 5400104,
        /**
         * The service process is dead.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        AVERR_SERVICE_DIED = 5400105,
        /**
         * The format of the media asset is not supported.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        AVERR_UNSUPPORT_FORMAT = 5400106,
        /**
         * The audio focus is interrupted.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform [since 12]
         * @atomicservice
         * @since 11
         */
        AVERR_AUDIO_INTERRUPTED = 5400107,
        /**
         * Failed to parse the server address or connect to the server.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform
         * @atomicservice
         * @since 14
         */
        AVERR_IO_HOST_NOT_FOUND = 5411001,
        /**
         * Network connection times out.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform
         * @atomicservice
         * @since 14
         */
        AVERR_IO_CONNECTION_TIMEOUT = 5411002,
        /**
         * Data or links are abnormal due to network exceptions.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform
         * @atomicservice
         * @since 14
         */
        AVERR_IO_NETWORK_ABNORMAL = 5411003,
        /**
         * The network is disabled.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform
         * @atomicservice
         * @since 14
         */
        AVERR_IO_NETWORK_UNAVAILABLE = 5411004,
        /**
         * No access permission.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform
         * @atomicservice
         * @since 14
         */
        AVERR_IO_NO_PERMISSION = 5411005,
        /**
         * The client request parameter is incorrect or exceeds the processing capability.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform
         * @atomicservice
         * @since 14
         */
        AVERR_IO_REQUEST_DENIED = 5411006,
        /**
         * No network resource is available.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform
         * @atomicservice
         * @since 14
         */
        AVERR_IO_RESOURCE_NOT_FOUND = 5411007,
        /**
         * The server fails to verify the client certificate.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform
         * @atomicservice
         * @since 14
         */
        AVERR_IO_SSL_CLIENT_CERT_NEEDED = 5411008,
        /**
         * The SSL connection fails.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform
         * @atomicservice
         * @since 14
         */
        AVERR_IO_SSL_CONNECTION_FAILED = 5411009,
        /**
         * The client fails to verify the server certificate.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform
         * @atomicservice
         * @since 14
         */
        AVERR_IO_SSL_SERVER_CERT_UNTRUSTED = 5411010,
        /**
         * The request is not supported due to a network protocol error.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform
         * @atomicservice
         * @since 14
         */
        AVERR_IO_UNSUPPORTED_REQUEST = 5411011,
        /**
         * The seek operation in SEEK_CONTINUOUS mode is not supported.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 18
         */
        AVERR_SEEK_CONTINUOUS_UNSUPPORTED = 5410002,
        /**
         * Super resolution is not supported.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 18
         */
        AVERR_SUPER_RESOLUTION_UNSUPPORTED = 5410003,
        /**
         * Super resolution is not enabled.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 18
         */
        AVERR_SUPER_RESOLUTION_NOT_ENABLED = 5410004,
        /**
         * HTTP plaintext access is not allowed.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 23
         */
        AVERR_IO_CLEARTEXT_NOT_PERMITTED = 5411012,
        /**
         * The parameter value is out of range.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 20
         */
        AVERR_PARAMETER_OUT_OF_RANGE = 5400108
    }
    /**
     * Describes the video Dimensions.
     *
     * @syscap SystemCapability.Multimedia.Media.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    interface VideoSize {
        /**
         * width of the video resolution.
         * The value should be an integer.Value constraint:The value must be a positive integer.
         * <br>Unit:Pixel.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        width?: number;
        /**
         * height of the video resolution.
         * The value should be an integer.Value constraint:The value must be a positive integer.
         * <br>Unit:Pixel.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        height?: number;
    }
    /**
     * Describes the filter conditions for track selection.
     *
     * @syscap SystemCapability.Multimedia.Media.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    interface TrackSelectionFilter {
        /**
         * Maximum allowed video bitrate.
         * The value should be an integer.Value constraint:The value must be a positive integer.
         * <br>Unit:Bits/sec.Default value:If this parameter is not specified, the maximum video bitrate is not limited.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        maxVideoBitrate?: number;
        /**
         * Minimum allowed video bitrate.
         * The value should be an integer.Value constraint:The value must be a positive integer.
         * <br>Unit:Bits/sec.Default value:If no value is assigned, the minimum video bitrate is not limited.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        minVideoBitrate?: number;
        /**
         * Maximum allowed video frame rate.
         * The value should be an integer.Value constraint:The value must be a positive integer.
         * <br>Unit:frame/sec.Default value:If not specified, the maximum video frame rate is not limited.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        maxVideoFrameRate?: number;
        /**
         * Minimum allowed video frame rate.
         * The value should be an integer.Value constraint:The value must be a positive integer.
         * <br>Unit:frame/sec.Default value:If not specified, the minimum frame rate is not specified.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        minVideoFrameRate?: number;
        /**
         * Maximum allowed video resolution.
         * <br>Default value:If not specified, the maximum video resolution is not limited.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        maxVideoResolution?: VideoSize;
        /**
         * Minimum allowed video resolution.
         * <br>Default value:If not specified, the minimum video resolution is not limited.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        minVideoResolution?: VideoSize;
        /**
         * The preferred sample MIME types for video tracks in order of preference,
         * Multiple MIMEs are arranged in the order of the array, with priorities in descending order.
         * Value constraint:Format as a MIME string or a codec string in HLS or DASH.
         * <br>Default value:If not specified or an empty array is set, the Mime type is not limited.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        preferredVideoMimeTypes?: Array<string>;
        /**
         * Maximum allowed audio bitrate.
         * The value should be an integer.Value constraint:The value must be a positive integer (greater than 0).
         * <br>Unit:bit/s.Default value:If this parameter is not set, the maximum audio bitrate is not limited.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        maxAudioBitrate?: number;
        /**
         * Minimum allowed audio bitrate.
         * The value should be an integer.Value constraint:The value must be a positive integer.
         * <br>Unit:Bits/sec.Default value:If this parameter is not set, the minimum audio bitrate is not limited.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        minAudioBitrate?: number;
        /**
         * Maximum allowed audio channel count.
         * The value should be an integer.Value constraint:The value must be a positive integer.
         * <br>Default value:If this parameter is not specified, the number of audio channels is not limited.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        maxAudioChannels?: number;
        /**
         * Indicates the preferred encoding MIME type of the audio track.
         * Multiple MIMEs are arranged in the order of the array, with priorities in descending order.
         * Value constraint:Format as a MIME string or a codec string in HLS or DASH.
         * <br>Default value:If not specified or an empty array is set, the MIME type of the audio is not restricted.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        preferredAudioMimeTypes?: Array<string>;
        /**
         * The preferred languages for audio tracks.
         * Multiple languages are arranged in the order of the array, with priorities in descending order.
         * Value constraint:Language strings comply with the IETF BCP 47 definition.
         * <br>Default value:If this parameter is not specified or the array is empty, the audio language is not restricted.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        preferredAudioLanguages?: Array<string>;
        /**
         * Preferred language set for subtitles.
         * Multiple languages are arranged in the order of the array, with priorities in descending order.
         * Value constraint:The language string complies with the IETF BCP 47 definition.
         * <br>Default value:If this parameter is not specified or the array is empty, the subtitle language is not
         * restricted.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        preferredSubtitleLanguages?: Array<string>;
    }
    /**
   * Describes the state of the [AVPlayer]{@link @ohos.multimedia.media:media}. Your application can proactively obtain
   * the AVPlayer state through the **state** property or obtain the reported AVPlayer state by subscribing to the
   * [stateChange]{@link @ohos.multimedia.media:media.AVPlayer.on(type: 'stateChange', callback: OnAVPlayerStateChangeHandle)}
   * event. For details about the rules for state transition, see
   * [Audio Playback](docroot://media/media/using-avplayer-for-playback.md).
   *
   * @unionmember { 'idle' } The AVPlayer enters this state after
   *     [createAVPlayer()]{@link @ohos.multimedia.media:media.createAVPlayer(callback: AsyncCallback<AVPlayer>)} or
   *     [reset()]{@link @ohos.multimedia.media:media.AVPlayer.reset(callback: AsyncCallback<void>)} is called.
   *     <br>In case [createAVPlayer()]{@link @ohos.multimedia.media:media.createAVPlayer(callback: AsyncCallback<AVPlayer>)}
   *     is used, all properties are set to their default values.
   *     <br>In case [reset()]{@link @ohos.multimedia.media:media.AVPlayer.reset(callback: AsyncCallback<void>) } The
   *     AVPlayer enters this state after
   *     [createAVPlayer()]{@link @ohos.multimedia.media:media.createAVPlayer(callback: AsyncCallback<AVPlayer>)} or
   *     [reset()]{@link @ohos.multimedia.media:media.AVPlayer.reset(callback: AsyncCallback<void>)} is called.
   *     <br>In case [createAVPlayer()]{@link @ohos.multimedia.media:media.createAVPlayer(callback: AsyncCallback<AVPlayer>)}
   *     is used, all properties are set to their default values.
   *     <br>In case [reset()]{@link @ohos.multimedia.media:media.AVPlayer.reset(callback: AsyncCallback<void>)} is called,
   *     the **url<sup>9+</sup>**, **fdSrc<sup>9+</sup>**, or **dataSrc<sup>10+</sup>** property and the **loop**
   *     property are reset, and other properties are retained.
   * @unionmember { 'initialized' } The AVPlayer enters this state after **url<sup>9+</sup>** or **fdSrc<sup>9+</sup>**
   *     property is set in the idle state. In this case, you can configure static properties such as the window and
   *     audio.
   * @unionmember { 'prepared' } The AVPlayer enters this state when
   *     [prepare()]{@link @ohos.multimedia.media:media.AVPlayer.prepare(callback: AsyncCallback<void>) } The AVPlayer
   *     enters this state when
   *     [prepare()]{@link @ohos.multimedia.media:media.AVPlayer.prepare(callback: AsyncCallback<void>)} is called in
   *     the initialized state. In this case, the playback engine has prepared the resources.
   * @unionmember { 'playing' } The AVPlayer enters this state when
   *     [play()]{@link @ohos.multimedia.media:media.AVPlayer.play(callback: AsyncCallback<void>) } The AVPlayer enters
   *     this state when [play()]{@link @ohos.multimedia.media:media.AVPlayer.play(callback: AsyncCallback<void>)} is
   *     called in the prepared, paused, or completed state.
   * @unionmember { 'paused' } The AVPlayer enters this state when **pause()** is called in the playing state.
   * @unionmember { 'completed' } The AVPlayer enters this state when a media asset finishes playing and loop playback
   *     is not set (no **loop = true**). In this case, if
   *     [play()]{@link @ohos.multimedia.media:media.AVPlayer.play(callback: AsyncCallback<void>)} is called, the
   *     AVPlayer enters the playing state and replays the media asset; if
   *     [stop()]{@link @ohos.multimedia.media:media.AVPlayer.stop(callback: AsyncCallback<void>) } The AVPlayer enters
   *     this state when a media asset finishes playing and loop playback is not set (no **loop = true**). In this case,
   *     if [play()]{@link @ohos.multimedia.media:media.AVPlayer.play(callback: AsyncCallback<void>)} is called, the
   *     AVPlayer enters the playing state and replays the media asset; if
   *     [stop()]{@link @ohos.multimedia.media:media.AVPlayer.stop(callback: AsyncCallback<void>)} is called, the
   *     AVPlayer enters the stopped state.
   * @unionmember { 'stopped' } The AVPlayer enters this state when
   *     [stop()]{@link @ohos.multimedia.media:media.AVPlayer.stop(callback: AsyncCallback<void>)} is called in the
   *     prepared, playing, paused, or completed state. In this case, the playback engine retains the properties but
   *     releases the memory resources. You can call
   *     [prepare()]{@link @ohos.multimedia.media:media.AVPlayer.prepare(callback: AsyncCallback<void>)} to prepare the
   *     resources again, call
   *     [reset()]{@link @ohos.multimedia.media:media.AVPlayer.reset(callback: AsyncCallback<void>)} to reset the
   *     properties, or call
   *     [release()]{@link @ohos.multimedia.media:media.AVPlayer.release(callback: AsyncCallback<void>) } The AVPlayer
   *     enters this state when
   *     [stop()]{@link @ohos.multimedia.media:media.AVPlayer.stop(callback: AsyncCallback<void>)} is called in the
   *     prepared, playing, paused, or completed state. In this case, the playback engine retains the properties but
   *     releases the memory resources. You can call
   *     [prepare()]{@link @ohos.multimedia.media:media.AVPlayer.prepare(callback: AsyncCallback<void>)} to prepare the
   *     resources again, call
   *     [reset()]{@link @ohos.multimedia.media:media.AVPlayer.reset(callback: AsyncCallback<void>)} to reset the
   *     properties, or call
   *     [release()]{@link @ohos.multimedia.media:media.AVPlayer.release(callback: AsyncCallback<void>)} to destroy the
   *     playback engine.
   * @unionmember { 'released' } The AVPlayer enters this state when
   *     [release()]{@link @ohos.multimedia.media:media.AVPlayer.release(callback: AsyncCallback<void>) } The AVPlayer
   *     enters this state when
   *     [release()]{@link @ohos.multimedia.media:media.AVPlayer.release(callback: AsyncCallback<void>)} is called. The
   *     playback engine associated with the AVPlayer instance is destroyed, and the playback process ends. This is the
   *     final state.
   * @unionmember { 'error' } The AVPlayer enters this state when an irreversible error occurs in the playback engine.
   *     You can call [reset()]{@link @ohos.multimedia.media:media.AVPlayer.reset(callback: AsyncCallback<void>)} to
   *     reset the properties or call
   *     [release()]{@link @ohos.multimedia.media:media.AVPlayer.release(callback: AsyncCallback<void>)} to destroy the
   *     playback engine. For details about the error codes, see
   *     [Media Error Codes](docroot://reference/apis-media-kit/errorcode-media.md).
   *     <br>**NOTE**
   *     <br>Distinguishing the error state from the
   *     [on('error')]{@link @ohos.multimedia.media:media.AVPlayer.on(type: 'error', callback: ErrorCallback)} state:
   *     <br>1. When the AVPlayer enters the error state, the **on('error')** event is triggered. You can obtain the detailed
   *     error information through this event.
   *     <br>2. When the AVPlayer enters the error state, the playback service stops. This requires the client to design a
   *     fault tolerance mechanism to call
   *     [reset()]{@link @ohos.multimedia.media:media.AVPlayer.reset(callback: AsyncCallback<void>)} or
   *     [release()]{@link @ohos.multimedia.media:media.AVPlayer.release(callback: AsyncCallback<void>) } The AVPlayer
   *     enters this state when an irreversible error occurs in the playback engine. You can call
   *     [reset()]{@link @ohos.multimedia.media:media.AVPlayer.reset(callback: AsyncCallback<void>)} to reset the
   *     properties or call
   *     [release()]{@link @ohos.multimedia.media:media.AVPlayer.release(callback: AsyncCallback<void>)} to destroy the
   *     playback engine. For details about the error codes, see
   *     [Media Error Codes](docroot://reference/apis-media-kit/errorcode-media.md).
   *     <br>**NOTE**
   *     <br>Distinguishing the error state from the
   *     [on('error')]{@link @ohos.multimedia.media:media.AVPlayer.on(type: 'error', callback: ErrorCallback)} state:
   *     <br>1. When the AVPlayer enters the error state, the **on('error')** event is triggered. You can obtain the detailed
   *     error information through this event.
   *     <br>2. When the AVPlayer enters the error state, the playback service stops. This requires the client to design a
   *     fault tolerance mechanism to call
   *     [reset()]{@link @ohos.multimedia.media:media.AVPlayer.reset(callback: AsyncCallback<void>)} or
   *     [release()]{@link @ohos.multimedia.media:media.AVPlayer.release(callback: AsyncCallback<void>)}.
   *     <br>3. The client receives **on('error')** event but the AVPlayer does not enter the error state. This situation
   *     occurs due to either of the following reasons:
   *     <br>Cause 1: The client calls an API in an incorrect state or passes in an incorrect parameter, and the AVPlayer
   *     intercepts the call. If this is the case, the client must correct its code logic.
   *     <br>Cause 2: A stream error is detected during playback. As a result, the container and decoding are abnormal for a
   *     short period of time, but continuous playback and playback control operations are not affected. If this is the
   *     case, the client does not need to design a fault tolerance mechanism.
   * @syscap SystemCapability.Multimedia.Media.AVPlayer
   * @crossplatform [since 12]
   * @atomicservice [since 11]
   * @since 9
   */
    type AVPlayerState = 'idle' | 'initialized' | 'prepared' | 'playing' | 'paused' | 'completed' | 'stopped' | 'released' | 'error';
    /**
     * Describes the callback invoked for the track change event.
     *
     * @param { number } index - Index of the track that has changed.
     * @param { boolean } isSelected - Whether the track at the current index is selected. **true** if selected, **false**
     *     otherwise.
     * @syscap SystemCapability.Multimedia.Media.AVPlayer
     * @atomicservice
     * @since 12
     */
    type OnTrackChangeHandler = (index: number, isSelected: boolean) => void;
    /**
     * Describes the callback invoked for the AVPlayer state change event.
     *
     * @param { AVPlayerState } state - State of the AVPlayer.
     * @param { StateChangeReason } reason - Reason for the state change.
     * @syscap SystemCapability.Multimedia.Media.AVPlayer
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    type OnAVPlayerStateChangeHandle = (state: AVPlayerState, reason: StateChangeReason) => void;
    /**
     * Describes the callback invoked for the buffering update event.
     *
     * @param { BufferingInfoType } infoType - Buffering information type.
     * @param { number } value - Value of the buffering information type.
     * @syscap SystemCapability.Multimedia.Media.AVPlayer
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    type OnBufferingUpdateHandler = (infoType: BufferingInfoType, value: number) => void;
    /**
     * Describes the callback invoked for the video size change event.
     *
     * @param { number } width - Video width, in px.
     * @param { number } height - Video height, in px.
     * @syscap SystemCapability.Multimedia.Media.AVPlayer
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    type OnVideoSizeChangeHandler = (width: number, height: number) => void;
    /**
     * Describes the callback used to listen for video super resolution status changes. If super resolution is enabled by
     * using [PlaybackStrategy]{@link @ohos.multimedia.media:media.PlaybackStrategy}, this callback is invoked to report
     * the super resolution status changes. It is also invoked to report the initial status when the video starts. However,
     * this callback is not invoked when super resolution is not enabled.
     *
     * Super resolution is automatically disabled in either of the following cases:
     *
     * * The current super resolution algorithm only works with videos that have a frame rate of 30 fps or lower. If the
     * video frame rate exceeds 30 fps, or if the input frame rate exceeds the processing capability of the super
     * resolution algorithm in scenarios such as fast playback, super resolution is automatically disabled.
     * * The current super resolution algorithm supports input resolutions from 320 × 320 to 1920 × 1080, in px. If the
     * input video resolution exceeds the range during playback, super resolution is automatically disabled.
     *
     * @param { boolean } enabled - Whether super resolution is enabled. **true** if enabled, **false** otherwise.
     * @syscap SystemCapability.Multimedia.Media.AVPlayer
     * @atomicservice
     * @since 18
     */
    type OnSuperResolutionChanged = (enabled: boolean) => void;
    /**
     * Describes the information of an SEI message.
     *
     * @syscap SystemCapability.Multimedia.Media.Core
     * @atomicservice
     * @since 18
     */
    interface SeiMessage {
        /**
         * Payload type of SEI message.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 18
         */
        payloadType: number;
        /**
         * Payload data of SEI message.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 18
         */
        payload: ArrayBuffer;
    }
    /**
     * Describes the handle used to obtain SEI messages. This is used when in subscriptions to SEI message events, and the
     * callback returns detailed SEI information.
     *
     * @param { Array<SeiMessage> } messages - Array of SEI messages.
     * @param { number } [playbackPosition] - Current playback position, in milliseconds.
     * @syscap SystemCapability.Multimedia.Media.AVPlayer
     * @atomicservice
     * @since 18
     */
    type OnSeiMessageHandle = (messages: Array<SeiMessage>, playbackPosition?: number) => void;
    /**
     * Describes the callback invoked for the event indicating that the playback rate setting is complete.
     *
     * @param { number } rate - Playback rate.
     * @syscap SystemCapability.Multimedia.Media.AVPlayer
     * @atomicservice
     * @since 20
     */
    type OnPlaybackRateDone = (rate: number) => void;
    /**
     * Enumerates the metric events supported by the media service.
     *
     * @syscap SystemCapability.Multimedia.Media.Core
     * @since 23
     */
    enum AVMetricsEventType {
        /**
         * Metric event indicating playback stalling.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @since 23
         */
        AV_METRICS_EVENT_STALLING = 1,
        /**
         * It is reported when the video sending and rendering time deviation is greater than expected,
         * for example, video frame alignment or display in advance.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        AV_METRICS_EVENT_LIP_ASYNC = 2,
        /**
         * Load rate change event. This event is triggered when the difference
         * between the data loading rate and the previous data loading rate is greater than 10%.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        AV_METRICS_EVENT_LOADINGRATE_CHANGE = 3,
        /**
         * Data loading failure event, which carries the error information returned during data loading,
         * such as connection timeout, access error, and server rejection.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        AV_METRICS_EVENT_LOADING_ERROR = 4,
        /**
         * Reported when the played media content changes, for example, advertisement insertion.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        AV_METRICS_EVENT_CONTENT_CHANGED = 5,
        /**
         * Content discontinuity event.
         * This event is triggered when audio and video parameter changes are detected.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        AV_METRICS_EVENT_CONTENT_DISCONTINUITY = 6,
        /**
         * Audio device status change event, including underload or out-of-focus.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        AV_METRICS_EVENT_AUDIO_ABNORMAL = 7
    }
    /**
     * Describes the information of an Metrics Event.
     *
     * @syscap SystemCapability.Multimedia.Media.AVPlayer
     * @since 23
     */
    interface AVMetricsEvent {
        /**
         * Type of the metrics event.
         *
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @stagemodelonly
         * @since 23
         */
        event: AVMetricsEventType;
        /**
         * Absolute timestamp when the event occurred.
         *
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @since 23
         */
        timeStamp: number;
        /**
         * The playback progress position when the event occurs.
         *
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @since 23
         */
        playbackPosition: number;
        /**
         * The detailed information of the event.
         *
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @stagemodelonly
         * @since 23
         */
        details: Record<string, Object>;
    }
    /**
     * AVPlayer is a playback management class. It provides APIs to manage and play media assets. Before calling any API
     * in AVPlayer, you must use
     * [createAVPlayer()]{@link @ohos.multimedia.media:media.createAVPlayer(callback: AsyncCallback<AVPlayer>)} to create
     * an AVPlayer instance.
     *
     * When using the AVPlayer instance, you are advised to register the following callbacks to proactively obtain status
     * changes: [on('stateChange')]{@link media.AVPlayer.on(type: 'stateChange', callback: OnAVPlayerStateChangeHandle)}:
     * listens for AVPlayer state changes. [on('error')]{@link media.AVPlayer.on(type: 'error', callback: ErrorCallback)}:
     * listens for error events.
     *
     * Applications must properly manage AVPlayer instances according to their specific needs, creating and freeing them
     * when necessary. Holding too many AVPlayer instances can lead to high memory usage, and in some cases, the system
     * might terminate applications to free up resources.
     *
     * For details about the audio and video playback demo, see
     * [Audio Playback](docroot://media/media/using-avplayer-for-playback.md) and
     * [Video Playback](docroot://media/media/video-playback.md).
     *
     * @syscap SystemCapability.Multimedia.Media.AVPlayer
     * @crossplatform [since 12]
     * @atomicservice [since 11]
     * @since 9
     */
    interface AVPlayer {
        /**
         * Prepares for audio and video playback. This API can be called only when the AVPlayer is in the initialized state.
         * The state changes can be detected by subscribing to the
         * [stateChange]{@link media.AVPlayer.on(type: 'stateChange', callback: OnAVPlayerStateChangeHandle)} event. This
         * API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by callback.
         * @throws { BusinessError } 5400106 - Unsupported format. Return by callback.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        prepare(callback: AsyncCallback<void>): void;
        /**
         * Prepares for audio and video playback. This API can be called only when the AVPlayer is in the initialized state.
         * The state changes can be detected by subscribing to the
         * [stateChange]{@link media.AVPlayer.on(type: 'stateChange', callback: OnAVPlayerStateChangeHandle)} event. This
         * API uses a promise to return the result.
         *
         * If your application frequently switches between short videos, you can create multiple AVPlayer objects to prepare
         * the next video in advance, thereby improving the switching performance. For details, see
         * [Smooth Switchover Between Online Short Videos](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-smooth-switching).
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by promise.
         * @throws { BusinessError } 5400106 - Unsupported format. Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        prepare(): Promise<void>;
        /**
         * Starts to play an audio and video asset. This API can be called only when the AVPlayer is in the prepared, paused,
         * or completed state. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by callback.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        play(callback: AsyncCallback<void>): void;
        /**
         * Starts to play an audio and video asset. This API can be called only when the AVPlayer is in the prepared, paused,
         * or completed state. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        play(): Promise<void>;
        /**
         * Pauses audio and video playback. This API can be called only when the AVPlayer is in the playing state. This API
         * uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by callback.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        pause(callback: AsyncCallback<void>): void;
        /**
         * Pauses audio and video playback. This API can be called only when the AVPlayer is in the playing state. This API
         * uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        pause(): Promise<void>;
        /**
         * Stops audio and video playback. This API can be called only when the AVPlayer is in the prepared, playing, paused,
         * or completed state. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by callback.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        stop(callback: AsyncCallback<void>): void;
        /**
         * Stops audio and video playback. This API can be called only when the AVPlayer is in the prepared, playing, paused,
         * or completed state. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        stop(): Promise<void>;
        /**
         * Resets audio and video playback. This API can be called only when the AVPlayer is in the initialized, prepared,
         * playing, paused, completed, stopped, or error state. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by callback.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        reset(callback: AsyncCallback<void>): void;
        /**
         * Resets audio and video playback. This API can be called only when the AVPlayer is in the initialized, prepared,
         * playing, paused, completed, stopped, or error state. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        reset(): Promise<void>;
        /**
         * Releases the playback resources. This API can be called when the AVPlayer is in any state except released. This
         * API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by callback.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        release(callback: AsyncCallback<void>): void;
        /**
         * Releases the playback resources. This API can be called when the AVPlayer is in any state except released. This
         * API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        release(): Promise<void>;
        /**
         * Seeks to the specified playback position. This API can be called only when the AVPlayer is in the prepared,
         * playing, paused, or completed state. You can check whether the seek operation takes effect by subscribing to the
         * [on('seekDone')]{@link media.AVPlayer.on(type: 'seekDone', callback: Callback<number>)} event.
         *
         * > **NOTE**
         * >
         * > Since API version 24, **seek** is supported in live streaming scenarios.
         *
         * @param { number } timeMs - Position to seek to, in ms. The value range is
         *     [0, [duration](docroot://reference/apis-media-kit/arkts-apis-media-AVPlayer.md#properties)].<br>When the seek
         *     mode is [SEEK_CONTINUOUS]{@link @ohos.multimedia.media:media.SeekMode}, you can set this parameter to **-1**
         *     to end the **SEEK_CONTINUOUS** mode.
         * @param { SeekMode } mode - Seek mode based on the video I frame. The default value is **SEEK_PREV_SYNC**.
         *     **Set this parameter only for video playback.**
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @stagemodelonly
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        seek(timeMs: number, mode?: SeekMode): void;
        /**
         * Sets the playback volume. This API can be called only when the AVPlayer is in the prepared, playing, paused, or
         * completed state. You can check whether the volume setting takes effect by subscribing to the
         * [on('volumeChange')]{@link media.AVPlayer.on(type: 'volumeChange', callback: Callback<number>)} event.
         *
         * @param { number } volume - Relative volume. The value ranges from 0.00 to 1.00. The value **1.00** indicates the
         *     maximum volume (100%).
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        setVolume(volume: number): void;
        /**
         * Obtains the audio and video track information. This API can be called only when the AVPlayer is in the prepared,
         * playing, or paused state. To obtain information about all audio and video tracks, this API must be called after
         * the data loading callback is triggered. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<Array<MediaDescription>> } callback - Callback used to return the result. If the operation
         *     is successful, **err** is **undefined** and **data** is the MediaDescription array obtained; otherwise,
         *     **err** is an error object.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by callback.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        getTrackDescription(callback: AsyncCallback<Array<MediaDescription>>): void;
        /**
         * Obtains the audio and video track information. This API can be called only when the AVPlayer is in the prepared,
         * playing, or paused state. This API uses a promise to return the result.
         *
         * @returns { Promise<Array<MediaDescription>> } Promise used to return the MediaDescription array that holds the
         *     audio and video track information.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        getTrackDescription(): Promise<Array<MediaDescription>>;
        /**
         * Obtains the indexes of the selected audio or video tracks. This API can be called only when the AVPlayer is in
         * the prepared, playing, or paused state. This API uses a promise to return the result.
         *
         * @returns { Promise<Array<number>> } Promise used to return the index array.
         * @throws { BusinessError } 5400102 - Operation not allowed.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @atomicservice
         * @since 12
         */
        getSelectedTracks(): Promise<Array<number>>;
        /**
         * Selects a track when the AVPlayer plays multimedia resources with multiple audio or video tracks. This API uses a
         * promise to return the result.
         *
         * @param { number } index - Index of the track. You can call
         *     [getTrackDescription]{@link media.AVPlayer.getTrackDescription()} to obtain all track information
         *     [MediaDescription]{@link @ohos.multimedia.media:media.MediaDescription} of the current resource.
         * @param { SwitchMode } mode - Video track mode. The default mode is **SMOOTH**. This parameter takes effect only
         *     for DASH/HLS network stream video track switching.<br>HLS network stream video is supported since API version
         *     24. [since 12 - 24]
         * @param { SwitchMode } [mode] - Video track mode. The default mode is **SMOOTH**. This parameter takes effect only
         *     for DASH/HLS network stream video track switching.<br>HLS network stream video is supported since API version
         *     24. [since 26.0.0]
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - The parameter check failed. Return by promise.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @stagemodelonly
         * @atomicservice
         * @since 12
         */
        selectTrack(index: number, mode?: SwitchMode): Promise<void>;
        /**
         * Deselects the specified track when the AVPlayer plays multimedia resources with multiple audio or video tracks.
         * This API uses a promise to return the result.
         *
         * @param { number } index - Track index, which is obtained from
         *     [MediaDescription]{@link @ohos.multimedia.media:media.MediaDescription} by calling
         *     [getTrackDescription]{@link media.AVPlayer.getTrackDescription()}.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - The parameter check failed. Return by promise.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @atomicservice
         * @since 12
         */
        deselectTrack(index: number): Promise<void>;
        /**
         * Obtains the selected track by the specified media type. This API can be called only when the AVPlayer
         * is in the prepared, playing, or paused state. This API uses a promise to return the result.
         *
         * @param { MediaType } trackType - specified media Type, see [MediaType]{@link #MediaType}.
         * @returns { Promise<number> } A Promise instance used to return selected track index.
         * @throws { BusinessError } 5400101 - No memory. Return by promise.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by promise.
         * @throws { BusinessError } 5400103 - I/O error. Return by promise.
         * @throws { BusinessError } 5400105 - Service died. Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @stagemodelonly
         * @since 26.0.0
         */
        getCurrentTrack(trackType: MediaType): Promise<number>;
        /**
         * Sets a source of streaming media that can be pre-downloaded, downloads the media data, and temporarily stores the
         * data in the memory. This API uses a promise to return the result.
         *
         * @param { MediaSource } src - Source of the streaming media to pre-download.
         * @param { PlaybackStrategy } strategy - strategy for playing the pre-downloaded streaming media.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @atomicservice
         * @since 12
         */
        setMediaSource(src: MediaSource, strategy?: PlaybackStrategy): Promise<void>;
        /**
         * Obtains the track selection filter configured for the player. This API uses a promise to return the result.
         *
         * @returns { Promise<TrackSelectionFilter> } Promise used to return the track selection filter configured for the
         *     player.
         * @throws { BusinessError } 5400102 - Operation not allowed.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @stagemodelonly
         * @since 26.0.0
         */
        getTrackSelectionFilter(): Promise<TrackSelectionFilter>;
        /**
         * Sets a track selection filter for the player. The player will use this filter to select available tracks for
         * playback. This API uses a promise to return the result.
         *
         * @param { TrackSelectionFilter } filter - Track selection filter.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 5400102 - Operation not allowed.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @stagemodelonly
         * @since 26.0.0
         */
        setTrackSelectionFilter(filter: TrackSelectionFilter): Promise<void>;
        /**
         * Adds an external subtitle to a video based on the FD. Currently, the external subtitle must be set after
         * **fdSrc** of the video resource is set in an AVPlayer instance. This API uses a promise to return the result.
         *
         * @param { number } fd - Resource handle, which is obtained by calling
         *     [resourceManager.getRawFd]{@link @ohos.resourceManager:resourceManager.ResourceManager.getRawFd(path: string, callback: _AsyncCallback<RawFileDescriptor>)}.
         * @param { number } offset - Resource offset, which needs to be entered based on the preset asset information. An
         *     invalid value causes a failure to parse subtitle assets. The default value is **0**.unit:Byte.
         * @param { number } length - Resource length, which needs to be entered based on the preset asset information. The
         *     default value is the remaining bytes from the offset in the file. An invalid value causes a failure to parse
         *     subtitle assets. The default value is **0**.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - The parameter check failed. Return by promise.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @atomicservice
         * @since 12
         */
        addSubtitleFromFd(fd: number, offset?: number, length?: number): Promise<void>;
        /**
         * Adds an external subtitle to a video based on the URL. Currently, the external subtitle must be set after
         * **fdSrc** of the video resource is set in an AVPlayer instance. This API uses a promise to return the result.
         *
         * @param { string } url - Address of the external subtitle file.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - The parameter check failed. Return by promise.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @atomicservice
         * @since 12
         */
        addSubtitleFromUrl(url: string): Promise<void>;
        /**
         * Obtains the playback information. This API can be called only when the AVPlayer is in the prepared, playing, or
         * paused state. This API uses a promise to return the result.
         *
         * @returns { Promise<PlaybackInfo> } Promise used to return **PlaybackInfo**.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @since 12
         */
        getPlaybackInfo(): Promise<PlaybackInfo>;
        /**
         * Obtains the playback speed of an AVPlayer. This API uses a promise to return the result.
         *
         * @returns { Promise<number> } Promise object, which returns the playback speed.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @since 23
         */
        getPlaybackRate(): Promise<number>;
        /**
         * Obtains the list of loaded time ranges. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > - For local media resources, the time range is from 0 to the entire media duration.
         * >
         * > - For network media resources, the list of locally loaded time ranges is returned.
         *
         * @returns { Promise<Array<Range>> } Promise used to return the list of loaded time ranges on the player.
         *     <br>The time range is represented by the **[start, end]** position on the playback timeline, in milliseconds.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @stagemodelonly
         * @since 26.0.0
         */
        getLoadedTimeRanges(): Promise<Array<Range>>;
        /**
         * Obtains the list of seekable time ranges. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > - For local media resources and media resources that support segment-based requests, the time range is from 0
         * > to the entire media duration.
         * >
         * > - For media resources that support only chunk-based transmission, there is no seekable time range.
         *
         * @returns { Promise<Array<Range>> } Promise used to return the list of seekable time ranges on the player.
         *     <br>The time range is represented by the **[start, end]** position on the playback timeline, in milliseconds.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @stagemodelonly
         * @since 26.0.0
         */
        getSeekableTimeRanges(): Promise<Array<Range>>;
        /**
         * Seeks to the default access point of the playback source. For live streams, the latest recommended access point
         * is used. For on-demand videos, the start position of the video is used (equivalent to **seek(0)**).
         *
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by callback.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @stagemodelonly
         * @since 26.0.0
         */
        seekToDefaultPosition(): void;
        /**
         * Obtains the statistic metrics of the current player. This API can be called when the AVPlayer is in the prepared,
         * playing, paused, completed, or stopped state. This API uses a promise to return the result.
         *
         * @returns { Promise<PlaybackMetrics> } Promise used to return the playback metrics of the current AVPlayer.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @since 23
         */
        getPlaybackStatisticMetrics(): Promise<PlaybackMetrics>;
        /**
         * Sets a playback strategy. This API can be called only when the AVPlayer is in the initialized state. This API
         * uses a promise to return the result.
         *
         * @param { PlaybackStrategy } strategy - Playback strategy.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Incorrect parameter types. 2. Parameter
         *     verification failed.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @atomicservice
         * @since 12
         */
        setPlaybackStrategy(strategy: PlaybackStrategy): Promise<void>;
        /**
         * Mutes or unmutes the audio. Since API version 20, this API also supports whether to display the video image. This
         * API uses a promise to return the result.
         *
         * This API can be called only when the AVPlayer is in the prepared, playing, paused, or completed state.
         *
         * @param { MediaType } mediaType - Media type.<br>For API version 12 to 19, only **MEDIA_TYPE_AUD** is supported.<
         *     br>Since API version 20, **MEDIA_TYPE_VID** is supported.
         * @param { boolean } muted - For API version 12 to 19, only audio playback strategies are supported. This parameter
         *     specifies whether to mute or unmute the audio. **true** to mute, **false** otherwise.<br>Since API version 20
         *     , video playback strategies are also supported. This parameter specifies whether to disable or enable the
         *     video image. **true** to disable, false otherwise.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - The parameter check failed. Return by promise.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @atomicservice
         * @since 12
         */
        setMediaMuted(mediaType: MediaType, muted: boolean): Promise<void>;
        /**
         * Sets the playback range and seeks to the start position of the range based on the specified
         * [SeekMode]{@link @ohos.multimedia.media:media.SeekMode}. After the setting, only the content in the specified
         * range of the audio or video file is played. This API uses a promise to return the result. It can be used in the
         * initialized, prepared, paused, stopped, or completed state.
         *
         * @param { number } startTimeMs - Start position of the range, in ms. The value range is
         *     [0, duration). If **-1** is passed in, the system starts playing from position 0.
         * @param { number } endTimeMs - End position of the range, in ms. The value range is (startTimeMs, duration]. If
         *     **-1** is passed in, the system plays the content until it reaches the final part of the asset.
         * @param { SeekMode } [mode] - Seek mode, which can be **SeekMode.SEEK_PREV_SYNC** or **SeekMode.SEEK_CLOSEST**.<br
         *     >The default value is **SeekMode.SEEK_PREV_SYNC**.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - The parameter check failed. Return by promise.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @atomicservice
         * @since 18
         */
        setPlaybackRange(startTimeMs: number, endTimeMs: number, mode?: SeekMode): Promise<void>;
        /**
         * Checks whether the media source supports [seek]{@link media.AVPlayer.seek} in SEEK_CONTINUOUS mode (specified by
         * [SeekMode]{@link @ohos.multimedia.media:media.SeekMode}). The actual value is returned when this API is called in
         * the prepared, playing, paused, or completed state. The value **false** is returned if it is called in other
         * states. For devices that do not support the seek operation in SEEK_CONTINUOUS mode, **false** is returned.
         *
         * @returns { boolean } Check result for the support of the seek operation in **SEEK_CONTINUOUS** mode. **true** to
         *     support, **false** otherwise.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @atomicservice
         * @since 18
         */
        isSeekContinuousSupported(): boolean;
        /**
         * Obtains the current playback position. This API can be called only when the AVPlayer is in the prepared, playing,
         * paused, or completed state.
         *
         * @returns { number } Current playback time, in milliseconds.
         * @throws { BusinessError } 5400102 - Operation not allowed.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @atomicservice
         * @since 18
         */
        getPlaybackPosition(): number;
        /**
         * Obtains the current playback time. This API can be called only when the AVPlayer is in the **playing**,
         * **paused**, or **completed** state.
         *
         * @returns { number } Current playback time, in microseconds.
         * @throws { BusinessError } 5400102 - Operation not allowed.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @stagemodelonly
         * @atomicservice
         * @since 23
         */
        getCurrentPresentationTimestamp(): number;
        /**
         * Enables or disables super resolution. This API can be called when the AVPlayer is in the initialized, prepared,
         * playing, paused, completed, or stopped state. This API uses a promise to return the result.
         *
         * Before calling [prepare()]{@link media.AVPlayer.prepare(callback: AsyncCallback<void>)}, enable super resolution
         * by using [PlaybackStrategy]{@link @ohos.multimedia.media:media.PlaybackStrategy}.
         *
         * @param { boolean } enabled - Whether to enable or disable super resolution. **true** to enable, **false**
         *     otherwise.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by promise.
         * @throws { BusinessError } 5410003 - Super-resolution not supported. Return by promise.
         * @throws { BusinessError } 5410004 - Missing enable super-resolution feature in {@link PlaybackStrategy}.
         *     Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @atomicservice
         * @since 18
         */
        setSuperResolution(enabled: boolean): Promise<void>;
        /**
         * Sets the resolution of the output video after super resolution. This API can be called when the AVPlayer is in
         * the initialized, prepared, playing, paused, completed, or stopped state. This API uses a promise to return the
         * result.
         *
         * The input parameter values must be in the range of 320 × 320 to 1920 × 1080 (in px).
         *
         * Before calling [prepare()]{@link media.AVPlayer.prepare(callback: AsyncCallback<void>)}, enable super resolution
         * by using [PlaybackStrategy]{@link @ohos.multimedia.media:media.PlaybackStrategy}.
         *
         * @param { number } width - Target width of the output video after super resolution. The value range is [320-1920], in
         *     px.
         * @param { number } height - Target height of the output video after super resolution. The value range is [320-1080],
         *     in px.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error. Return by promise.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by promise.
         * @throws { BusinessError } 5410003 - Super-resolution not supported. Return by promise.
         * @throws { BusinessError } 5410004 - Missing enable super-resolution feature in {@link PlaybackStrategy}.
         *     Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @atomicservice
         * @since 18
         */
        setVideoWindowSize(width: number, height: number): Promise<void>;
        /**
         * Ends playback of the current mediasource and starts playback of the next mediasource in the mediasource list.
         *
         * @returns { Promise<void> } Promise used to return the result.
         * @throws { BusinessError } 5400102 - Operation not allowed . Return by promise.
         * @throws { BusinessError } 5400108 - The previous mediasource does not exist in the playlist. Returned via
         *     promise.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        advanceToNextMediaSource(): Promise<void>;
        /**
         * Ends playback of the current mediasource and starts playback of the previous mediasource in the mediasource list.
         *
         * @returns { Promise<void> } Promise used to return the result.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by promise.
         * @throws { BusinessError } 5400108 - The next mediasource does not exist in the playlist. Returned via promise.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        advanceToPrevMediaSource(): Promise<void>;
        /**
         * Return the current mediasource.
         *
         * @returns { MediaSource | undefined } current mediasource if the operation is successful; returns undefined otherwise.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        getCurrentMediaSource(): MediaSource | undefined;
        /**
         * Add a new playback source to the player's playlist.
         *
         * @param { MediaSource } src - Playback source to be added to the playlist.
         * @param { string } [id] - Indicates the ID of a media source in the playlist.
         *     The newly added media source is inserted before the specified media source.
         *     <br>Default value:if empty, it means adding to the end of the list
         * @returns { Promise<string> } Promise used to return the result,
         *     if success, a unique ID corresponding to the media resource will be returned.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by promise.
         * @throws { BusinessError } 5400108 - The media source ID does not exist in the playlist. Returned by promise.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        addPlaybackMediaSource(src: MediaSource, id?: string): Promise<string>;
        /**
         * Removes the specified playback media source from the player's playlist.
         * If the id does not exist in the current playlist, the method returns immediately.
         *
         * @param { string } id - ID returned after a media source is added to the playlist.
         * @returns { Promise<void> } Promise used to return the result.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by promise.
         * @throws { BusinessError } 5400108 - The media source ID does not exist in the playlist. Returned via promise.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        removePlaybackMediaSource(id: string): Promise<void>;
        /**
         * Clears all the items in the player's playlist. Currently playing media will be terminated immediately.
         *
         * @returns { Promise<void> } Promise is used to return the result.
         * @throws { BusinessError } 5400102 - operation not allowed . Returned via promise.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        clearPlaybackList(): Promise<void>;
        /**
         * Ends playback of the current mediasource and starts playback of the specified mediasource in the mediasource
         * list.
         *
         * @param { string } id - Indicates the ID of the media source to play.
         * @returns { Promise<void> } Promise used to return the result.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by promise.
         * @throws { BusinessError } 5400108 - The mediasource does not exist in the playlist. Returned via promise.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        advanceToMediaSource(id: string): Promise<void>;
        /**
         * Return the array of mediasources in the playlist.
         *
         * @returns { Array<MediaSource | undefined> } array of mediasources in the playlist.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        getMediaSources(): Array<MediaSource | undefined>;
        /**
         * URL of the media asset. It can be set only when the AVPlayer is in the idle state.
         *
         * Supported video formats: MP4, MPEG-TS, and MKV.
         *
         * Supported audio formats: M4A, AAC, MP3, OGG, WAV, FLAC, AMR, and APE.
         *
         * **Example of supported URLs**:
         *
         * 1. FD: fd://xx
         *
         * ![](docroot://reference/apis-media-kit/figures/en-us_image_url.png)
         *
         * 2. HTTP: http://xx
         * 3. HTTPS: https://xx
         * 4. HLS: http://xx or https://xx
         *
         * **NOTE**
         *
         * - To set the playback URL, you need to declare the
         * [ohos.permission.INTERNET](docroot://security/AccessToken/permissions-for-all.md#ohospermissioninternet)
         * permission. The related error code is
         * [201 Permission Denied](docroot://reference/errorcode-universal.md#201-permission-denied).
         * - WebM is no longer supported since API version 11.
         * - After the resource handle (FD) is transferred to an AVPlayer instance, do not use the resource handle to
         * perform other read and write operations, including but not limited to transferring this handle to other AVPlayer,
         * AVMetadataExtractor, AVImageGenerator, or AVTranscoder instance. Competition occurs when multiple AVPlayers use
         * the same resource handle to read and write files at the same time, resulting in errors in obtaining data.
         *
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        url?: string;
        /**
         * FD of the media asset. It can be set only when the AVPlayer is in the idle state.
         *
         * **Use scenario**: This property is required when media assets of an application are continuously stored in a
         * file.
         *
         * The video formats MP4, MPEG-TS, and MKV are supported.
         *
         * The audio formats M4A, AAC, MP3, OGG, WAV, FLAC, AMR, and APE are supported.
         *
         * Assume that a media file that stores continuous assets consists of the following:
         *
         * Video 1 (address offset: 0, byte length: 100)
         *
         * Video 2 (address offset: 101; byte length: 50)
         *
         * Video 3 (address offset: 151, byte length: 150)
         *
         * 1. To play video 1: AVFileDescriptor { fd = resource handle; offset = 0; length = 100; }
         * 2. To play video 2: AVFileDescriptor { fd = resource handle; offset = 101; length = 50; }
         * 3. To play video 3: AVFileDescriptor { fd = resource handle; offset = 151; length = 150; }
         *
         * To play an independent media file, use **src=fd://xx**.
         *
         * **NOTE**
         *
         * WebM is no longer supported since API version 11.
         *
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        fdSrc?: AVFileDescriptor;
        /**
         * Descriptor of a streaming media asset. It can be set only when the AVPlayer is in the idle state.
         *
         * **Use scenario**: An application plays a file that has been downloaded from a remote source and saved locally.
         * When the application has not yet downloaded the complete audio or video resources, it can start playing the data
         * that has already been retrieved. By writing the retrieved data to a local file and simultaneously reading from
         * that file, the application can achieve the capability of playing while caching.
         *
         * The video formats MP4, MPEG-TS, and MKV are supported.
         *
         * The audio formats M4A, AAC, MP3, OGG, WAV, FLAC, AMR, and APE are supported.
         *
         * A user is obtaining an audio and video file from a remote server and wants to play the downloaded file content.
         * To implement this scenario, do as follows:
         *
         * 1. Obtain the total file size, in bytes. If the total size cannot be obtained, set **fileSize** to **-1**.
         * 2. Implement the **func** callback to fill in data. If **fileSize** is **-1**, the format of **func** is **func(buffer: ArrayBuffer, length: number)**, and the AVPlayer obtains data in sequence; otherwise, the format is **func(buffer: ArrayBuffer, length: number, pos: number)**, and the AVPlayer seeks and obtains data in the required positions.
         * 3. Set **AVDataSrcDescriptor {fileSize = size, callback = func}**.
         *
         * **Notes:**
         *
         * If the media file to play is in MP4/M4A format, ensure that the **moov** field (specifying the media information)
         * is before the **mdat** field (specifying the media data) or the fields before the **moov** field is less than 10
         * MB. Otherwise, the parsing fails and the media file cannot be played.
         *
         * **NOTE**
         *
         * WebM is no longer supported since API version 11.
         *
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        dataSrc?: AVDataSrcDescriptor;
        /**
         * Whether to loop playback. **true** to loop, **false** otherwise. The default value is **false**. It is a dynamic
         * property
         *
         * and can be set only when the AVPlayer is in the prepared, playing, paused, or completed state.
         *
         * This setting is not supported in live mode.
         *
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        loop: boolean;
        /**
         * Set the loop mode when playing the media source playlist.
         * <br>Default value:PLAYLIST_LOOP_MODE_ALL, which means loops all items in the playlist.
         *
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        playlistLoopMode?: PlaylistLoopMode;
        /**
         * Audio interruption mode. The default value is **SHARE_MODE**. It is a dynamic property
         *
         * and can be set only when the AVPlayer is in the prepared, playing, paused, or completed state.
         *
         * To take effect, this property must be set before
         * [play()]{@link media.AVPlayer.play(callback: AsyncCallback<void>)} is called for the first time.
         *
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @atomicservice [since 12]
         * @since 9
         */
        audioInterruptMode?: audio.InterruptMode;
        /**
         * Audio renderer information. If the media source contains videos, the default value of **usage** is
         * **STREAM_USAGE_MOVIE**. Otherwise, the default value of **usage** is **STREAM_USAGE_MUSIC**. The default value of
         * **rendererFlags** is 0. If the default value of **usage** does not meet the requirements, configure
         * [audio.AudioRendererInfo]{@link @ohos.multimedia.audio:audio.AudioRendererInfo}.
         *
         * This parameter can be set only when the AVPlayer is in the initialized state.
         *
         * To take effect, this property must be set before
         * [prepare()]{@link media.AVPlayer.prepare(callback: AsyncCallback<void>)} is called for the first time.
         *
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @atomicservice [since 12]
         * @since 10
         */
        audioRendererInfo?: audio.AudioRendererInfo;
        /**
         * Audio effect mode. The audio effect mode is a dynamic property and is restored to the default value
         * **EFFECT_DEFAULT** when **usage** of **audioRendererInfo** is changed. It can be set only when the AVPlayer is in
         * the prepared, playing, paused, or completed state.
         *
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @atomicservice [since 12]
         * @since 10
         */
        audioEffectMode?: audio.AudioEffectMode;
        /**
         * Current video playback position, in ms. It can be used as a query parameter when the AVPlayer is in the prepared,
         * playing, paused, or completed state.
         *
         * The value **-1** indicates an invalid value.
         *
         * In live mode, **-1** is returned by default.
         *
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        readonly currentTime: number;
        /**
         * Video duration, in ms. It can be used as a query parameter when the AVPlayer is in the prepared, playing, paused,
         * or completed state.
         *
         * The value **-1** indicates an invalid value.
         *
         * In live mode, **-1** is returned by default.
         *
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        readonly duration: number;
        /**
         * AVPlayer state. It can be used as a query parameter when the AVPlayer is in any state.
         *
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        readonly state: AVPlayerState;
        /**
         * Video window ID. By default, there is no video window.
         *
         * This property can be set for the first time only when the AVPlayer is in the initialized state.
         *
         * It can be updated when the AVPlayer is in the prepared, playing, paused, completed, or stopped state. After the
         * reset, the video is played in the new window.
         *
         * **Use scenario**: It is used to render the window for video playback (not involved in audio-only playback
         * scenarios).
         *
         * [Create a surface ID through XComponent]{@link ./@internal/component/ets/xcomponent:XComponentController.getXComponentSurfaceId}.
         *
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        surfaceId?: string;
        /**
         * Video width, in px. It can be used as a query parameter when the AVPlayer is in the prepared, playing, paused, or
         * completed state.
         *
         * The value **0** indicates an invalid value.
         *
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        readonly width: number;
        /**
         * Video height, in px. It can be used as a query parameter when the AVPlayer is in the prepared, playing, paused,
         * or completed state.
         *
         * The value **0** indicates an invalid value.
         *
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        readonly height: number;
        /**
         * Video scale type. The default value is **VIDEO_SCALE_TYPE_FIT**. It is a dynamic property
         *
         * and can be set only when the AVPlayer is in the prepared, playing, paused, or completed state.
         *
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        videoScaleType?: VideoScaleType;
        /**
         * Audio privacy configuration. For more information, see {@link #audio.AudioPrivacyType}.
         * Default value: PRIVACY_TYPE_PUBLIC.
         *
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @stagemodelonly
         * @crossplatform
         * @since 26.0.0
         */
        privacyType?: audio.AudioPrivacyType;
        /**
         * Sets the playback speed. This API can be called only when the AVPlayer is in the prepared, playing, paused, or
         * completed state. You can check whether the speed setting takes effect by subscribing to the
         * [on('speedDone')]{@link media.AVPlayer.on(type: 'speedDone', callback: Callback<number>)} event.
         *
         * > **NOTE**
         * >
         * > This method is not supported in live streaming scenarios.
         *
         * @param { PlaybackSpeed } speed - Playback speed to set.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        setSpeed(speed: PlaybackSpeed): void;
        /**
         * Sets the playback rate. This API can be called only when the AVPlayer is in the prepared, playing, paused, or
         * completed state. The value range is [0.125, 8.0], on API 24 and below, the range is [0.125, 4.0].
         * You can check whether the setting takes effect through the
         * [playbackRateDone]{@link media.AVPlayer.on(type: 'playbackRateDone', callback: OnPlaybackRateDone)} event.
         *
         * > **NOTE**
         * >
         * > This API is not supported in live mode.
         *
         * @param { number } rate - Playback rate, which is in the range [0.125, 8.0]
         *     on API 24 and below, the range is [0.125, 4.0].
         * @throws { BusinessError } 5400108 - The parameter check failed, parameter value out of range.
         * @throws { BusinessError } 5400102 - Operation not allowed, if invalid state or live stream.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @atomicservice
         * @since 20
         */
        setPlaybackRate(rate: number): void;
        /**
         * Sets the bitrate for the streaming media. This API is valid only for HLS/DASH streams. By default, the AVPlayer
         * selects a proper bitrate based on the network connection speed. This API can be called only when the AVPlayer is
         * in the prepared, playing, paused, or completed state. You can check whether the setting takes effect by
         * subscribing to the [bitrateDone]{@link media.AVPlayer.on(type: 'bitrateDone', callback: Callback<number>)} event.
         *
         * @param { number } bitrate - Bitrate to set. You can obtain the available bitrates of the current HLS/DASH stream by
         *     subscribing to the
         *     [availableBitrates]{@link media.AVPlayer.on(type: 'availableBitrates', callback: Callback<Array<number>>)}
         *     event. If the bitrate to set is not in the list of the available bitrates, the AVPlayer selects from the list
         *     the bitrate that is closed to the bitrate to set. If the length of the available bitrate list obtained
         *     through the event is 0, no bitrate can be set and the **bitrateDone** callback will not be triggered.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        setBitrate(bitrate: number): void;
        /**
      * Sets the loudness gain of the AVPlayer. After this API is called, the loudness gain takes effect immediately. This
      * API uses a promise to return the result.
      *
      * > **NOTE**
      * >
      * > - This API can be called when the AVPlayer is in the prepared, playing, paused, completed, or stopped state.
      * >
      * > - Before calling this API, ensure that the audio rendering information has been set in
      * > **AVPlayer.audioRendererInfo** and the **usage** parameter in **audioRendererInfo** has been set to
      * > [STREAM_USAGE_MUSIC]{@link @ohos.multimedia.audio:audio.StreamUsage},
      * > [STREAM_USAGE_MOVIE]{@link @ohos.multimedia.audio:audio.StreamUsage}, or
      * > [STREAM_USAGE_AUDIOBOOK]{@link @ohos.multimedia.audio:audio.StreamUsage}.
      *
      * @param { number } loudnessGain - Loudness gain, in the range [-90.0, 24.0], in dB. The default value is 0.0 dB.
      * @returns { Promise<void> } Promise that returns no value.
      * @syscap SystemCapability.Multimedia.Media.AVPlayer
      * @since 21
      */
        setLoudnessGain(loudnessGain: number): Promise<void>;
        /**
         * Sets the decryption configuration. When receiving an
         * [on('mediaKeySystemInfoUpdate')]{@link media.AVPlayer.on(type: 'mediaKeySystemInfoUpdate', callback: Callback<Array<drm.MediaKeySystemInfo>>)}
         * event, create the related configuration and set the decryption configuration based on the information in the
         * reported event. Otherwise, the playback fails.
         *
         * @param { drm.MediaKeySession } mediaKeySession - Decryption session.
         * @param { boolean } secureVideoPath - Secure video channel. **true** if a secure video channel is selected,
         *     **false** otherwise.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @atomicservice [since 12]
         * @since 11
         */
        setDecryptionConfig(mediaKeySession: drm.MediaKeySession, secureVideoPath: boolean): void;
        /**
         * Obtains the media key system information of the media asset that is being played. This API can be called only
         * after the
         * [on('mediaKeySystemInfoUpdate')]{@link media.AVPlayer.on(type: 'mediaKeySystemInfoUpdate', callback: Callback<Array<drm.MediaKeySystemInfo>>)}
         * event is successfully triggered.
         *
         * @returns { Array<drm.MediaKeySystemInfo> } Array of MediaKeySystemInfo objects, each of which contains the
         *     **uuid** and **pssh** properties. If the return value is undefined, the mediaKeySystemInfoUpdate event is not
         *     triggered.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @atomicservice [since 12]
         * @since 11
         */
        getMediaKeySystemInfos(): Array<drm.MediaKeySystemInfo>;
        /**
         * Subscribes to media key system information changes.
         *
         * @param { 'mediaKeySystemInfoUpdate' } type - Event type, which is **'mediaKeySystemInfoUpdate'** in this case.
         *     This event is triggered when the copyright protection information of the media asset being played changes.
         * @param { function } callback - Callback invoked when the event is triggered. It reports a **MediaKeySystemInfo**
         *     array. [since 11 - 11]
         * @param { Callback<Array<drm.MediaKeySystemInfo>> } callback - Callback invoked when the event is triggered. It
         *     reports a **MediaKeySystemInfo** array. [since 12]
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @atomicservice [since 12]
         * @since 11
         */
        on(type: 'mediaKeySystemInfoUpdate', callback: Callback<Array<drm.MediaKeySystemInfo>>): void;
        /**
         * Unsubscribes from media key system information changes.
         *
         * @param { 'mediaKeySystemInfoUpdate' } type - Event type, which is **'mediaKeySystemInfoUpdate'** in this case.
         * @param { function } callback - Callback invoked when the event is triggered. It reports a **MediaKeySystemInfo**
         *     array. If this parameter is specified, only the specified callback is unregistered. Otherwise, all callbacks
         *     associated with the **mediaKeySystemInfoUpdate** event will be unregistered. [since 11 - 11]
         * @param { Callback<Array<drm.MediaKeySystemInfo>> } callback - Callback invoked when the event is triggered. It
         *     reports a **MediaKeySystemInfo** array. If this parameter is specified, only the specified callback is
         *     unregistered. Otherwise, all callbacks associated with the **mediaKeySystemInfoUpdate** event will be
         *     unregistered. [since 12]
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @atomicservice [since 12]
         * @since 11
         */
        off(type: 'mediaKeySystemInfoUpdate', callback?: Callback<Array<drm.MediaKeySystemInfo>>): void;
        /**
         * Subscribes to AVPlayer state changes.
         *
         * @param { 'stateChange' } type - Event type, which is **'stateChange'** in this case. This event can be triggered
         *     by both user operations and the system.
         * @param { function } callback - Callback invoked when the event is triggered. [since 9 - 11]
         * @param { OnAVPlayerStateChangeHandle } callback - Callback invoked when the event is triggered. [since 12]
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        on(type: 'stateChange', callback: OnAVPlayerStateChangeHandle): void;
        /**
         * Unsubscribes from [AVPlayerState]{@link @ohos.multimedia.media:media.AVPlayerState} state changes.
         *
         * @param { 'stateChange' } type - Event type, which is **'stateChange'** in this case.
         * @param { OnAVPlayerStateChangeHandle } callback - Callback invoked when the event is triggered. If this parameter
         *     is specified, only the specified callback is unregistered. Otherwise, all callbacks associated with the
         *     **stateChange** event will be unregistered. [since 12]
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        off(type: 'stateChange', callback?: OnAVPlayerStateChangeHandle): void;
        /**
         * Subscribes to the event to check whether the volume is successfully set.
         *
         * @param { 'volumeChange' } type - Event type, which is **'volumeChange'** in this case. This event is triggered
         *     each time **setVolume()** is called.
         * @param { Callback<number> } callback - Callback invoked when the event is triggered. It reports the effective
         *     volume.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        on(type: 'volumeChange', callback: Callback<number>): void;
        /**
         * Unsubscribes from the event that checks whether the volume is successfully set.
         *
         * @param { 'volumeChange' } type - Event type, which is **'volumeChange'** in this case.
         * @param { Callback<number> } callback - Callback invoked when the event is triggered. It reports the effective
         *     volume. If this parameter is specified, only the specified callback is unregistered. Otherwise, all callbacks
         *     associated with the **volumeChange** event will be unregistered. [since 12]
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 19]
         * @since 9
         */
        off(type: 'volumeChange', callback?: Callback<number>): void;
        /**
         * Subscribes to the event that indicates the end of the stream being played. If
         * **[loop](docroot://reference/apis-media-kit/arkts-apis-media-AVPlayer.md#properties) = true** is set, the
         * AVPlayer seeks to the beginning of the stream and plays the stream again. If **loop** is not set, the completed
         * state is reported through the
         * [stateChange]{@link media.AVPlayer.on(type: 'stateChange', callback: OnAVPlayerStateChangeHandle)} event.
         *
         * @param { 'endOfStream' } type - Event type, which is **'endOfStream'** in this case. This event is triggered when
         *     the AVPlayer finishes playing the media asset.
         * @param { Callback<void> } callback - Callback invoked when the event is triggered.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        on(type: 'endOfStream', callback: Callback<void>): void;
        /**
         * Unsubscribes from the event that indicates the end of the stream being played.
         *
         * @param { 'endOfStream' } type - Event type, which is **'endOfStream'** in this case.
         * @param { Callback<void> } callback - Callback invoked when the event is triggered. If this parameter is specified
         *     , only the specified callback is unregistered. Otherwise, all callbacks associated with the **endOfStream**
         *     event will be unregistered. [since 12 - 18]
         * @param { Callback<void> } [callback] - Callback invoked when the event is triggered. If this parameter is
         *     specified, only the specified callback is unregistered. Otherwise, all callbacks associated with the
         *     **endOfStream** event will be unregistered. [since 19]
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 19]
         * @since 9
         */
        off(type: 'endOfStream', callback?: Callback<void>): void;
        /**
         * Subscribes to the event to check whether the seek operation takes effect.
         *
         * @param { 'seekDone' } type - Event type, which is **'seekDone'** in this case. This event is triggered each time
         *     **seek()** is called, except in SEEK_CONTINUOUS mode.
         * @param { Callback<number> } callback - Callback invoked when the event is triggered. It reports the time position
         *     requested by the user.<br>For video playback, [SeekMode]{@link @ohos.multimedia.media:media.SeekMode} may
         *     cause the actual position to be different from that requested by the user. The exact position can be obtained
         *     from the **currentTime** property. The time in this callback only means that the requested seek operation is
         *     complete.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        on(type: 'seekDone', callback: Callback<number>): void;
        /**
         * Unsubscribes from the event that checks whether the seek operation takes effect.
         *
         * @param { 'seekDone' } type - Event type, which is **'seekDone'** in this case.
         * @param { Callback<number> } callback - Callback invoked when the event is triggered. It reports the time position
         *     requested by the user.<br>For video playback, [SeekMode]{@link @ohos.multimedia.media:media.SeekMode} may
         *     cause the actual position to be different from that requested by the user. The exact position can be obtained
         *     from the **currentTime** property. The time in this callback only means that the requested seek operation is
         *     complete. If this parameter is specified, only the specified callback is unregistered. Otherwise, all
         *     callbacks associated with the **seekDone** event will be unregistered. [since 12]
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        off(type: 'seekDone', callback?: Callback<number>): void;
        /**
         * Subscribes to the event to check whether the playback speed is successfully set.
         *
         * @param { 'speedDone' } type - Event type, which is **'speedDone'** in this case. This event is triggered each
         *     time **setSpeed()** is called.
         * @param { Callback<number> } callback - Callback used to return the result. When the call of **setSpeed** is
         *     successful, the effective speed mode is reported. For details, see
         *     [PlaybackSpeed]{@link @ohos.multimedia.media:media.PlaybackSpeed}.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        on(type: 'speedDone', callback: Callback<number>): void;
        /**
         * Unsubscribes from the event that checks whether the playback speed is successfully set.
         *
         * @param { 'speedDone' } type - Event type, which is **'speedDone'** in this case.
         * @param { Callback<number> } callback - Callback used to return the result. When the call of **setSpeed** is
         *     successful, the effective speed mode is reported. For details, see
         *     [PlaybackSpeed]{@link @ohos.multimedia.media:media.PlaybackSpeed}. If this parameter is specified, only the
         *     specified callback is unregistered. Otherwise, all callbacks associated with the **speedDone** event will be
         *     unregistered. [since 12]
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 19]
         * @since 9
         */
        off(type: 'speedDone', callback?: Callback<number>): void;
        /**
         * Subscribes to the event indicating that the playback rate set by calling
         * [setPlaybackRate]{@link media.AVPlayer.setPlaybackRate} is applied.
         *
         * @param { 'playbackRateDone' } type - Event type, which is **'playbackRateDone'** in this case. This event is
         *     triggered each time **setPlaybackRate** is called.
         * @param { OnPlaybackRateDone } callback - Callback invoked when the event is triggered. It reports the new
         *     playback rate.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @atomicservice
         * @since 20
         */
        on(type: 'playbackRateDone', callback: OnPlaybackRateDone): void;
        /**
         * Unsubscribes from the event indicating that the playback rate set by calling
         * [setPlaybackRate]{@link media.AVPlayer.setPlaybackRate} is applied.
         *
         * @param { 'playbackRateDone' } type - Event type, which is **'playbackRateDone'** in this case.
         * @param { OnPlaybackRateDone } [callback] - Callback invoked when the event is triggered. It reports the new
         *     playback rate. If this parameter is specified, only the specified callback is unregistered. Otherwise, all
         *     callbacks associated with the **playbackRateDone** event will be unregistered.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @atomicservice
         * @since 20
         */
        off(type: 'playbackRateDone', callback?: OnPlaybackRateDone): void;
        /**
         * Subscribes to the event to check whether the bitrate is successfully set.
         *
         * @param { 'bitrateDone' } type - Event type, which is **'bitrateDone'** in this case. This event is triggered each
         *     time **setBitrate()** is called.
         * @param { Callback<number> } callback - Callback invoked when the event is triggered. It reports the effective
         *     bitrate.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @atomicservice [since 12]
         * @since 9
         */
        on(type: 'bitrateDone', callback: Callback<number>): void;
        /**
         * Unsubscribes from the event that checks whether the bitrate is successfully set.
         *
         * @param { 'bitrateDone' } type - Event type, which is **'bitrateDone'** in this case.
         * @param { Callback<number> } callback - Callback invoked when the event is triggered. It reports the effective
         *     bitrate. If this parameter is specified, only the specified callback is unregistered. Otherwise, all
         *     callbacks associated with the **bitrateDone** event will be unregistered. [since 12 - 18]
         * @param { Callback<number> } [callback] - Callback invoked when the event is triggered. It reports the effective
         *     bitrate. If this parameter is specified, only the specified callback is unregistered. Otherwise, all
         *     callbacks associated with the **bitrateDone** event will be unregistered. [since 19]
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @atomicservice [since 19]
         * @since 9
         */
        off(type: 'bitrateDone', callback?: Callback<number>): void;
        /**
         * Subscribes to playback position changes. It is used to refresh the current position of the progress bar. By
         * default, this event is reported every 100 ms. However, it is reported immediately upon a successful seek
         * operation.
         *
         * > **NOTE**
         * >
         * > - The **'timeUpdate'** event is not supported in live streaming scenarios.
         * >
         * > - When a seek operation is performed, the progress bar can be updated based on the **'timeUpdate'** event only
         * > after the seek operation is complete (**'seekdone'** received).
         * >
         * > - In the **pause** state, the player reports the timeUpdate event when the buffering ends.
         *
         * @param { 'timeUpdate' } type - Event type, which is **'timeUpdate'** in this case.
         * @param { Callback<number> } callback - Callback used to return the current time.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        on(type: 'timeUpdate', callback: Callback<number>): void;
        /**
         * Unsubscribes from playback position changes.
         *
         * @param { 'timeUpdate' } type - Event type, which is **'timeUpdate'** in this case.
         * @param { Callback<number> } [callback] - Callback used to return the current time. If this parameter is specified,
         *     only the specified callback is unregistered. Otherwise, all callbacks associated with the **timeUpdate**
         *     event will be unregistered. [since 12]
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        off(type: 'timeUpdate', callback?: Callback<number>): void;
        /**
         * Subscribes to media asset duration changes. It is used to refresh the length of the progress bar. By default,
         * this event is reported once in the prepared state. However, it can be repeatedly reported for special streams
         * that trigger duration changes.
         *
         * > **NOTE**
         * >
         * > The **durationUpdate** event is not supported in live streaming scenarios.
         *
         * @param { 'durationUpdate' } type - Event type, which is **'durationUpdate'** in this case.
         * @param { Callback<number> } callback - Callback used to return the resource duration.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        on(type: 'durationUpdate', callback: Callback<number>): void;
        /**
         * Unsubscribes from media asset duration changes.
         *
         * @param { 'durationUpdate' } type - Event type, which is **'durationUpdate'** in this case.
         * @param { Callback<number> } callback - Callback used to return the resource duration. If this parameter is
         *     specified, only the specified callback is unregistered. Otherwise, all callbacks associated with the
         *     **durationUpdate** event will be unregistered. [since 12 - 18]
         * @param { Callback<number> } [callback] - Callback used to return the resource duration. If this parameter is
         *     specified, only the specified callback is unregistered. Otherwise, all callbacks associated with the
         *     **durationUpdate** event will be unregistered. [since 19]
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 19]
         * @since 9
         */
        off(type: 'durationUpdate', callback?: Callback<number>): void;
        /**
         * Subscribes to audio and video buffer changes. This subscription is supported only in network playback scenarios.
         *
         * @param { 'bufferingUpdate' } type - Event type, which is **'bufferingUpdate'** in this case.
         * @param { function } callback - Callback invoked when the event is triggered. [since 9 - 11]
         * @param { OnBufferingUpdateHandler } callback - Callback invoked when the event is triggered. [since 12]
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        on(type: 'bufferingUpdate', callback: OnBufferingUpdateHandler): void;
        /**
         * Unsubscribes from audio and video buffer changes.
         *
         * @param { 'bufferingUpdate' } type - Event type, which is **'bufferingUpdate'** in this case.
         * @param { OnBufferingUpdateHandler } [callback] - Callback invoked when the event is triggered. If this parameter
         *     is specified, only the specified callback is unregistered. Otherwise, all callbacks associated with the
         *     **bufferingUpdate** event will be unregistered. [since 12]
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        off(type: 'bufferingUpdate', callback?: OnBufferingUpdateHandler): void;
        /**
         * Subscribes to the event that indicates rendering starts for the first frame. This subscription is supported only
         * in video playback scenarios. This event only means that the playback service sends the first frame to the display
         * module. The actual rendering effect depends on the rendering performance of the display service.
         *
         * @param { 'startRenderFrame' } type - Event type, which is **'startRenderFrame'** in this case.
         * @param { Callback<void> } callback - Callback invoked when the event is triggered.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @atomicservice [since 12]
         * @since 9
         */
        on(type: 'startRenderFrame', callback: Callback<void>): void;
        /**
         * Unsubscribes from the event that indicates rendering starts for the first frame.
         *
         * @param { 'startRenderFrame' } type - Event type, which is **'startRenderFrame'** in this case.
         * @param { Callback<void> } callback - Callback invoked when the event is triggered. If this parameter is specified
         *     , only the specified callback is unregistered. Otherwise, all callbacks associated with the
         *     **startRenderFrame** event will be unregistered. [since 12 - 18]
         * @param { Callback<void> } [callback] - Callback invoked when the event is triggered. If this parameter is
         *     specified, only the specified callback is unregistered. Otherwise, all callbacks associated with the
         *     **startRenderFrame** event will be unregistered. [since 19]
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @atomicservice [since 19]
         * @since 9
         */
        off(type: 'startRenderFrame', callback?: Callback<void>): void;
        /**
         * Subscribes to video size (width and height) changes. This subscription is supported only in video playback
         * scenarios. By default, this event is reported only once in the prepared state. However, it is also reported upon
         * resolution changes in the case of HLS streams.
         *
         * @param { 'videoSizeChange' } type - Event type, which is **'videoSizeChange'** in this case.
         * @param { function } callback - Callback invoked when the event is triggered. [since 9 - 11]
         * @param { OnVideoSizeChangeHandler } callback - Callback invoked when the event is triggered. [since 12]
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        on(type: 'videoSizeChange', callback: OnVideoSizeChangeHandler): void;
        /**
         * Unsubscribes from video size changes.
         *
         * @param { 'videoSizeChange' } type - Event type, which is **'videoSizeChange'** in this case.
         * @param { OnVideoSizeChangeHandler } [callback] - Callback invoked when the event is triggered. If this parameter
         *     is specified, only the specified callback is unregistered. Otherwise, all callbacks associated with the
         *     **videoSizeChange** event will be unregistered. [since 12]
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        off(type: 'videoSizeChange', callback?: OnVideoSizeChangeHandler): void;
        /**
         * Subscribes to the audio interruption event. When multiple audio and video assets are played at the same time,
         * this event is triggered based on the audio interruption mode
         * [audio.InterruptMode]{@link @ohos.multimedia.audio:audio.InterruptMode}. The application needs to perform
         * corresponding processing based on different audio interruption events. For details, see
         * [Handling Audio Interruption Events](docroot://media/audio/audio-playback-concurrency.md).
         *
         * @param { 'audioInterrupt' } type - Event type, which is **'audioInterrupt'** in this case.
         * @param { function } callback - Callback invoked when the event is triggered. [since 9 - 11]
         * @param { Callback<audio.InterruptEvent> } callback - Callback invoked when the event is triggered. [since 12]
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        on(type: 'audioInterrupt', callback: Callback<audio.InterruptEvent>): void;
        /**
         * Unsubscribes from the audio interruption event.
         *
         * @param { 'audioInterrupt' } type - Event type, which is **'audioInterrupt'** in this case.
         * @param { Callback<audio.InterruptEvent> } callback - Callback invoked when the event is triggered. If this
         *     parameter is specified, only the specified callback is unregistered. Otherwise, all callbacks associated with
         *     the **audioInterrupt** event will be unregistered. [since 12]
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        off(type: 'audioInterrupt', callback?: Callback<audio.InterruptEvent>): void;
        /**
         * Subscribes to available bitrates of HLS/DASH streams. This event is reported only after the AVPlayer switches to
         * the prepared state.
         *
         * @param { 'availableBitrates' } type - Event type, which is **'availableBitrates'** in this case. This event is
         *     triggered once after the AVPlayer switches to the prepared state.
         * @param { function } callback - Callback invoked when the event is triggered. It returns an array that holds the
         *     available bitrates. If the array length is 0, no bitrate can be set. [since 9 - 11]
         * @param { Callback<Array<number>> } callback - Callback invoked when the event is triggered. It returns an array that
         *     holds the available bitrates. If the array length is 0, no bitrate can be set. [since 12]
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        on(type: 'availableBitrates', callback: Callback<Array<number>>): void;
        /**
         * Unsubscribes from available bitrates of HLS/DASH streams. This event is reported after
         * [prepare]{@link media.AVPlayer.prepare(callback: AsyncCallback<void>)} is called.
         *
         * @param { 'availableBitrates' } type - Event type, which is **'availableBitrates'** in this case.
         * @param { Callback<Array<number>> } callback - Callback invoked when the event is triggered. It returns an array that
         *     holds the available bitrates. If the array length is 0, no bitrate can be set. If this parameter is specified
         *     , only the specified callback is unregistered. Otherwise, all callbacks associated with the
         *     **availableBitrates** event will be unregistered. [since 12]
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        off(type: 'availableBitrates', callback?: Callback<Array<number>>): void;
        /**
         * Subscribes to [AVPlayer]{@link @ohos.multimedia.media:media} errors. This event is used only for error prompt and
         * does not require the user to stop playback control. If the
         * [AVPlayerState]{@link @ohos.multimedia.media:media.AVPlayerState} is also switched to error, call
         * [reset()]{@link media.AVPlayer.reset(callback: AsyncCallback<void>)} or
         * [release()]{@link media.AVPlayer.release(callback: AsyncCallback<void>)} to exit the playback. If the playback
         * remains in the error state after the [reset()]{@link media.AVPlayer.reset(callback: AsyncCallback<void>)} method
         * is called, you are advised to directly invoke the
         * [release()]{@link media.AVPlayer.release(callback: AsyncCallback<void>)} method to exit the playback operation.
         *
         * @param { 'error' } type - Event type, which is **'error'** in this case. This event can be triggered by both user
         *     operations and the system.
         * @param { ErrorCallback } callback - Callback used to return the error code ID and error message.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 401 - The parameter check failed.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 5400101 - No memory.
         * @throws { BusinessError } 5400102 - Operation not allowed.
         * @throws { BusinessError } 5400103 - I/O error. [since 9 - 13]
         * @throws { BusinessError } 5400104 - Time out.
         * @throws { BusinessError } 5400105 - Service died.
         * @throws { BusinessError } 5400106 - Unsupported format.
         * @throws { BusinessError } 5411001 - IO can not find host. [since 14]
         * @throws { BusinessError } 5411002 - IO connection timeout. [since 14]
         * @throws { BusinessError } 5411003 - IO network abnormal. [since 14]
         * @throws { BusinessError } 5411004 - IO network unavailable. [since 14]
         * @throws { BusinessError } 5411005 - IO no permission. [since 14]
         * @throws { BusinessError } 5411006 - IO request denied. [since 14]
         * @throws { BusinessError } 5411007 - IO resource not found. [since 14]
         * @throws { BusinessError } 5411008 - IO SSL client cert needed. [since 14]
         * @throws { BusinessError } 5411009 - IO SSL connect fail. [since 14]
         * @throws { BusinessError } 5411010 - IO SSL server cert untrusted. [since 14]
         * @throws { BusinessError } 5411011 - IO unsupported request. [since 14]
         * @throws { BusinessError } 5410002 - Seek continuous unsupported. [since 18]
         * @throws { BusinessError } 5411012 - Http cleartext traffic is not permitted. [since 23]
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        on(type: 'error', callback: ErrorCallback): void;
        /**
         * Unsubscribes from AVPlayer errors.
         *
         * @param { 'error' } type - Event type, which is **'error'** in this case.
         * @param { ErrorCallback } callback - Callback used to return the error code ID and error message. If this
         *     parameter is specified, only the specified callback is unregistered. Otherwise, all callbacks associated with
         *     the **error** event will be unregistered. [since 12]
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        off(type: 'error', callback?: ErrorCallback): void;
        /**
         * Subscribes to audio stream output device changes and reasons. This API uses an asynchronous callback to return
         * the result.
         *
         * When subscribing to this event, you are advised to implement the player behavior when the device is connected or
         * disconnected by referring to
         * [Handling Output Device Changes Gracefully](docroot://media/audio/audio-output-device-change.md).
         *
         * @param { 'audioOutputDeviceChangeWithInfo' } type - Event type, which is **'audioOutputDeviceChangeWithInfo'** in
         *     this case.
         * @param { Callback<audio.AudioStreamDeviceChangeInfo> } callback - Callback used to return the output device
         *     descriptor of the current audio stream and the change reason.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @atomicservice [since 12]
         * @since 11
         */
        on(type: 'audioOutputDeviceChangeWithInfo', callback: Callback<audio.AudioStreamDeviceChangeInfo>): void;
        /**
         * Unsubscribes from audio stream output device changes and reasons. This API uses an asynchronous callback to
         * return the result.
         *
         * @param { 'audioOutputDeviceChangeWithInfo' } type - Event type, which is **'audioOutputDeviceChangeWithInfo'** in
         *     this case.
         * @param { Callback<audio.AudioStreamDeviceChangeInfo> } callback - Callback used to return the output device
         *     descriptor of the current audio stream and the change reason. If this parameter is specified, only the
         *     specified callback is unregistered. Otherwise, all callbacks associated with the
         *     **audioOutputDeviceChangeWithInfo** event will be unregistered.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3.Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @atomicservice [since 12]
         * @since 11
         */
        off(type: 'audioOutputDeviceChangeWithInfo', callback?: Callback<audio.AudioStreamDeviceChangeInfo>): void;
        /**
         * Subscribes to subtitle update events. When external subtitles exist, the system notifies the application through
         * the subscribed-to callback. An application can subscribe to only one subtitle update event. When the application
         * initiates multiple subscriptions to this event, the last subscription is applied.
         *
         * @param { 'subtitleUpdate' } type - Event type, which is **'subtitleUpdate'** in this case. The event is triggered
         *     when the external subtitle is updated.
         * @param { Callback<SubtitleInfo> } callback - Callback invoked when the subtitle is updated.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @atomicservice
         * @since 12
         */
        on(type: 'subtitleUpdate', callback: Callback<SubtitleInfo>): void;
        /**
         * Unsubscribes from subtitle update events.
         *
         * @param { 'subtitleUpdate' } type - Event type, which is **'subtitleUpdate'** in this case. The event is triggered
         *     when the external subtitle is updated.
         * @param { Callback<SubtitleInfo> } callback - Callback that has been registered to listen for subtitle update
         *     events. If this parameter is specified, only the specified callback is unregistered. Otherwise, all callbacks
         *     associated with the **subtitleUpdate** event will be unregistered.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @atomicservice
         * @since 12
         */
        off(type: 'subtitleUpdate', callback?: Callback<SubtitleInfo>): void;
        /**
         * Subscribes to track change events. When the track changes, the system notifies the application through the
         * subscribed-to callback. An application can subscribe to only one track change event. When the application
         * initiates multiple subscriptions to this event, the last subscription is applied.
         *
         * @param { 'trackChange' } type - Event type, which is **'trackChange'** in this case. The event is triggered when
         *     the track changes.
         * @param { OnTrackChangeHandler } callback - Callback invoked when the event is triggered.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @atomicservice
         * @since 12
         */
        on(type: 'trackChange', callback: OnTrackChangeHandler): void;
        /**
         * Unsubscribes from track change events.
         *
         * @param { 'trackChange' } type - Event type, which is **'trackChange'** in this case. The event is triggered when
         *     the track changes.
         * @param { OnTrackChangeHandler } callback - Callback that has been registered to listen for track changes. If this
         *     parameter is specified, only the specified callback is unregistered. Otherwise, all callbacks associated with
         *     the **trackChange** event will be unregistered.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @atomicservice
         * @since 12
         */
        off(type: 'trackChange', callback?: OnTrackChangeHandler): void;
        /**
         * Subscribes to track information update events. When the track information is updated, the system notifies the
         * application through the subscribed-to callback. An application can subscribe to only one track change event. When
         * the application initiates multiple subscriptions to this event, the last subscription is applied.
         *
         * @param { 'trackInfoUpdate' } type - Event type, which is **'trackInfoUpdate'** in this case. The event is
         *     triggered when the track information is updated.
         * @param { Callback<Array<MediaDescription>> } callback - Callback invoked when the event is triggered.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @atomicservice
         * @since 12
         */
        on(type: 'trackInfoUpdate', callback: Callback<Array<MediaDescription>>): void;
        /**
         * Unsubscribes from track information update events.
         *
         * @param { 'trackInfoUpdate' } type - Event type, which is **'trackInfoUpdate'** in this case. The event is
         *     triggered when the track information is updated.
         * @param { Callback<Array<MediaDescription>> } callback - Callback that has been registered to listen for track
         *     information updates. If this parameter is specified, only the specified callback is unregistered. Otherwise,
         *     all callbacks associated with the **trackInfoUpdate** event will be unregistered.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @atomicservice
         * @since 12
         */
        off(type: 'trackInfoUpdate', callback?: Callback<Array<MediaDescription>>): void;
        /**
         * Subscribes to update events of the maximum audio level value, which is periodically reported when audio resources
         * are played.
         *
         * @param { 'amplitudeUpdate' } type - Event type, which is **'amplitudeUpdate'** in this case. The event is
         *     triggered when the amplitude changes.
         * @param { Callback<Array<number>> } callback - Callback invoked when the event is triggered.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @since 13
         */
        on(type: 'amplitudeUpdate', callback: Callback<Array<number>>): void;
        /**
         * Unsubscribes from update events of the maximum amplitude.
         *
         * @param { 'amplitudeUpdate' } type - Event type, which is **'amplitudeUpdate'** in this case. The event is
         *     triggered when the amplitude changes.
         * @param { Callback<Array<number>> } callback - Callback that has been registered to listen for amplitude updates.
         *     If this parameter is specified, only the specified callback is unregistered. Otherwise, all callbacks
         *     associated with the **amplitudeUpdate** event will be unregistered.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @since 13
         */
        off(type: 'amplitudeUpdate', callback?: Callback<Array<number>>): void;
        /**
         * Subscribes to events indicating that a Supplemental Enhancement Information (SEI) message is received. This
         * applies only to HTTP-FLV live streaming and is triggered when SEI messages are present in the video stream. You
         * must initiate the subscription before calling **prepare**. If you initiate multiple subscriptions to this event,
         * the last subscription is applied.
         *
         * @param { 'seiMessageReceived' } type - Event type, which is **'seiMessageReceived'** in this case. The event is
         *     triggered when an SEI message is received.
         * @param { Array<number> } payloadTypes - Array of subscribed-to payload types of SEI messages. Currently, only
         *     payloadType = 5 is supported.
         * @param { OnSeiMessageHandle } callback - Callback used to listen for SEI message events and receive the
         *     subscribed-to payload types.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @atomicservice
         * @since 18
         */
        on(type: 'seiMessageReceived', payloadTypes: Array<number>, callback: OnSeiMessageHandle): void;
        /**
         * Unsubscribes from the events indicating that an SEI message is received.
         *
         * @param { 'seiMessageReceived' } type - Event type, which is **'seiMessageReceived'** in this case. The event is
         *     triggered when an SEI message is received.
         * @param { Array<number> } [payloadTypes] - Array of subscribed-to payload types of SEI messages.
         * @param { OnSeiMessageHandle } [callback] - Callback used to listen for SEI message events and receive the
         *     subscribed-to payload types. If this parameter is specified, only the specified callback is unregistered.
         *     Otherwise, all callbacks associated with the **seiMessageReceived** event will be unregistered.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @atomicservice
         * @since 18
         */
        off(type: 'seiMessageReceived', payloadTypes?: Array<number>, callback?: OnSeiMessageHandle): void;
        /**
         * Subscribes to the event indicating that super resolution is enabled or disabled.
         *
         * @param { 'superResolutionChanged' } type - Event type, which is **'superResolutionChanged'** in this case. The
         *     event is triggered when super resolution is enabled or disabled.
         * @param { OnSuperResolutionChanged } callback - Callback used to listen for super resolution status changes.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @atomicservice
         * @since 18
         */
        on(type: 'superResolutionChanged', callback: OnSuperResolutionChanged): void;
        /**
         * Unsubscribes from the event indicating that super resolution is enabled or disabled.
         *
         * @param { 'superResolutionChanged' } type - Event type, which is **'superResolutionChanged'** in this case. The
         *     event is triggered when super resolution is enabled or disabled.
         * @param { OnSuperResolutionChanged } callback - Callback used to listen for super resolution status changes. If
         *     this parameter is specified, only the specified callback is unregistered. Otherwise, all callbacks associated
         *     with the **superResolutionChanged** event will be unregistered.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @atomicservice
         * @since 18
         */
        off(type: 'superResolutionChanged', callback?: OnSuperResolutionChanged): void;
        /**
         * Subscribes to metric events during playback.
         *
         * @param { Callback<Array<AVMetricsEvent>> } callback - Callback invoked for metric events. This API uses an
         *     asynchronous callback to return the result.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @since 23
         */
        onMetricsEvent(callback: Callback<Array<AVMetricsEvent>>): void;
        /**
         * Unsubscribes from metric events during playback.
         *
         * @param { Callback<Array<AVMetricsEvent>> } [callback] - Callback invoked for metric events. This API uses an
         *     asynchronous callback to return the result.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @since 23
         */
        offMetricsEvent(callback?: Callback<Array<AVMetricsEvent>>): void;
        /**
         * Registers a listener to detect when the playback content has changed.
         * The value carried in the callback function is the ID of the media source that is being played in the playlist.
         *
         * @param { Callback<string> } callback - Callback invoked when the event is triggered.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        onPlaybackContentChanged(callback: Callback<string>): void;
        /**
         * Unregisters listener to detect when changes occur in the playback content.
         *
         * @param { Callback<string> } [callback] - Callback invoked when the event is triggered.
         *     <br>Default value:If this parameter is not specified, all callback functions for the event are unsubscribed.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        offPlaybackContentChanged(callback?: Callback<string>): void;
        /**
         * Register listener to detect time-based metadata,
         * Currently, only the #EXT-X-DATERANGE data of HLS and the Event Streams information of DASH are supported.
         *
         * @param { Callback<AVTimedMetaData> } callback - Callback invoked when the event is triggered.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        onTimedMetaData(callback: Callback<AVTimedMetaData>): void;
        /**
         * Unregister listener to detect time-based metadata,
         * Currently, only the #EXT-X-DATERANGE data of HLS and the Event Streams information of DASH are supported.
         *
         * @param { Callback<AVTimedMetaData> } [callback] - Callback invoked when the event is triggered.
         *     <br>Default value:If this parameter is not specified, all callback functions for the event are unsubscribed.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        offTimedMetaData(callback?: Callback<AVTimedMetaData>): void;
    }
    /**
     * Enumerates loop mode keys for playback.
     *
     * @syscap SystemCapability.Multimedia.Media.Core
     * @stagemodelonly
     * @atomicservice
     * @since 26.0.0
     */
    enum PlaylistLoopMode {
        /**
         * loops all items in the playlist
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        PLAYLIST_LOOP_MODE_ALL = 1,
        /**
         * Loops a single playback item.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        PLAYLIST_LOOP_MODE_ONE = 2,
        /**
         * Loops shuffle playback item.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        PLAYLIST_LOOP_MODE_SHUFFLE = 3,
        /**
         * No looping
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        PLAYLIST_LOOP_MODE_NONE = 4
    }
    /**
     * Enumerates the playback metric keys.
     *
     * @syscap SystemCapability.Multimedia.Media.AVPlayer
     * @since 23
     */
    enum PlaybackMetricsKey {
        /**
         * Preparation duration, in milliseconds.
         *
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @since 23
         */
        PREPARE_DURATION = 'prepare_duration',
        /**
         * Duration for establishing a resource connection, in milliseconds.
         *
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @since 23
         */
        RESOURCE_CONNECTION_DURATION = 'resource_connection_duration',
        /**
         * Duration for decapsulating the first frame, in milliseconds.
         *
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @since 23
         */
        FIRST_FRAME_DECAPSULATION_DURATION = 'first_frame_decapsulation_duration',
        /**
         * Total playback duration, in milliseconds.
         *
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @since 23
         */
        TOTAL_PLAYING_TIME = 'total_playback_time',
        /**
         * Total number of requests.
         *
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @stagemodelonly
         * @since 23
         */
        DOWNLOAD_REQUESTS_COUNT = 'loading_requests_count',
        /**
         * Total loading duration, in milliseconds.
         *
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @since 23
         */
        TOTAL_DOWNLOAD_TIME = 'total_loading_time',
        /**
         * Total loading size, in bytes.
         *
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @stagemodelonly
         * @since 23
         */
        TOTAL_DOWNLOAD_SIZE = 'total_loading_bytes',
        /**
         * Total number of stalling times.
         *
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @since 23
         */
        STALLING_COUNT = 'stalling_count',
        /**
         * Total stalling duration, in milliseconds.
         *
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @since 23
         */
        TOTAL_STALLING_TIME = 'total_stalling_time',
        /**
         * Cumulative lip async count.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @stagemodelonly
         * @since 26.0.0
         */
        LIP_ASYNC_COUNT = 'lip_async_count',
        /**
         * Total lip async duration during the playback, in milliseconds.
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @stagemodelonly
         * @since 26.0.0
         */
        TOTAL_LIP_ASYNC_TIME = 'total_lip_async_time'
    }
    /**
     * Describes the container for the key-value pairs of playback metrics.
     *
     * @syscap SystemCapability.Multimedia.Media.Core
     * @since 23
     */
    type PlaybackMetrics = Record<PlaybackMetricsKey, Object>;
    /**
     * Provides player statistic info.
     *
     * @syscap SystemCapability.Multimedia.Media.Core
     * @since 12
     */
    interface PlaybackInfo {
        /**
         * key:value pair, key see @PlaybackInfoKey.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @since 12
         */
        [key: string]: Object;
    }
    /**
     * Enumerates the playback description keys.
     *
     * @syscap SystemCapability.Multimedia.Media.Core
     * @since 12
     */
    enum PlaybackInfoKey {
        /**
         * IP address of the server. The corresponding key value type is string.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @since 12
         */
        SERVER_IP_ADDRESS = 'server_ip_address',
        /**
         * Average download rate. The corresponding key value type is number, measured in bit/s.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @since 12
         */
        AVG_DOWNLOAD_RATE = 'average_download_rate',
        /**
         * Download rate in one second. The corresponding key value type is number, measured in bit/s.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @since 12
         */
        DOWNLOAD_RATE = 'download_rate',
        /**
         * Download status. The corresponding key value type is number. The value **1** means that the downloaded is in
         * progress, and **0** means that the download is complete.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @since 12
         */
        IS_DOWNLOADING = 'is_downloading',
        /**
         * Duration that the cached data can be played. The corresponding key value type is number, measured in seconds.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @since 12
         */
        BUFFER_DURATION = 'buffer_duration'
    }
    /**
     * Enumerates the media error codes.
     *
     * @syscap SystemCapability.Multimedia.Media.Core
     * @since 8
     * @deprecated since 11
     * @useinstead media.AVErrorCode
     */
    enum MediaErrorCode {
        /**
         * The operation is successful.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @since 8
         * @deprecated since 11
         * @useinstead ohos.multimedia.media/media.AVErrorCode#AVERR_OK
         */
        MSERR_OK = 0,
        /**
         * Failed to allocate memory. The system may have no available memory.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @since 8
         * @deprecated since 11
         * @useinstead ohos.multimedia.media/media.AVErrorCode#AVERR_NO_MEMORY
         */
        MSERR_NO_MEMORY = 1,
        /**
         * No permission to perform the operation.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @since 8
         * @deprecated since 11
         * @useinstead ohos.multimedia.media/media.AVErrorCode#AVERR_OPERATE_NOT_PERMIT
         */
        MSERR_OPERATION_NOT_PERMIT = 2,
        /**
         * Invalid input parameter.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @since 8
         * @deprecated since 11
         * @useinstead ohos.multimedia.media/media.AVErrorCode#AVERR_INVALID_PARAMETER
         */
        MSERR_INVALID_VAL = 3,
        /**
         * An I/O error occurs.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @since 8
         * @deprecated since 11
         * @useinstead ohos.multimedia.media/media.AVErrorCode#AVERR_IO
         */
        MSERR_IO = 4,
        /**
         * The operation times out.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @since 8
         * @deprecated since 11
         * @useinstead ohos.multimedia.media/media.AVErrorCode#AVERR_TIMEOUT
         */
        MSERR_TIMEOUT = 5,
        /**
         * An unknown error occurs.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @since 8
         * @deprecated since 11
         * @useinstead ohos.multimedia.media/media.AVErrorCode#AVERR_INVALID_PARAMETER
         */
        MSERR_UNKNOWN = 6,
        /**
         * Invalid server.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @since 8
         * @deprecated since 11
         * @useinstead ohos.multimedia.media/media.AVErrorCode#AVERR_SERVICE_DIED
         */
        MSERR_SERVICE_DIED = 7,
        /**
         * The operation is not allowed in the current state.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @since 8
         * @deprecated since 11
         * @useinstead ohos.multimedia.media/media.AVErrorCode#AVERR_INVALID_PARAMETER
         */
        MSERR_INVALID_STATE = 8,
        /**
         * The operation is not supported in the current version.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @since 8
         * @deprecated since 11
         * @useinstead ohos.multimedia.media/media.AVErrorCode#AVERR_UNSUPPORT_CAPABILITY
         */
        MSERR_UNSUPPORTED = 9
    }
    /**
     * Enumerates the buffering event types.
     *
     * @syscap SystemCapability.Multimedia.Media.Core
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 8
     */
    enum BufferingInfoType {
        /**
         * Buffering starts. When this event is triggered, the player pauses the playback.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 8
         */
        BUFFERING_START = 1,
        /**
         * Buffering ends. When this event is triggered, the player resumes the playback.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 8
         */
        BUFFERING_END = 2,
        /**
         * Buffering percentage. You can use this event to monitor the buffering status.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 8
         */
        BUFFERING_PERCENT = 3,
        /**
         * Estimated duration, in ms, that the buffered data can be played. This event is triggered once the data change
         * amount in the buffer exceeds 500 ms. You can use this event to develop a progress bar.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 8
         */
        CACHED_DURATION = 4
    }
    /**
     * This callback function is implemented by applications to handle resource open requests and return a unique handle
     * for the opened resource.
     *
     * > **NOTE**
     * >
     * > The client must return the handle immediately after processing the request.
     *
     * @param { MediaSourceLoadingRequest } request - Parameters for the resource open request, including detailed
     *     information about the requested resource and the data push method.
     * @returns { number } Handle for the current resource open request. A value greater than 0 means the request is
     *     successful, whereas a value less than or equal to 0 means it fails.
     *     <br> - The handle for the request object is unique.
     * @syscap SystemCapability.Multimedia.Media.Core
     * @atomicservice
     * @since 18
     */
    type SourceOpenCallback = (request: MediaSourceLoadingRequest) => number;
    /**
     * This callback function is implemented by applications to handle resource read requests. When data is available,
     * applications should push it to the player using the
     * [respondData]{@link @ohos.multimedia.media:media.MediaSourceLoadingRequest.respondData(uuid: number, offset: number, buffer: ArrayBuffer)}
     * API of the corresponding MediaSourceLoadingRequest object.
     *
     * > **NOTE**
     * >
     * > The client must return the handle immediately after processing the request.
     *
     * @param { number } uuid - ID for the resource handle.
     * @param { number } requestedOffset - Offset of the current media data relative to the start of the resource.
     * @param { number } requestedLength - Length of the current request. The value **-1** indicates reaching the end of the
     *     resource. After pushing the data, call
     *     [finishLoading]{@link @ohos.multimedia.media:media.MediaSourceLoadingRequest.finishLoading} to notify the
     *     player that the push is complete.
     * @returns { void } - client should return immediately.
     * @syscap SystemCapability.Multimedia.Media.Core
     * @atomicservice
     * @since 18
     */
    type SourceReadCallback = (uuid: number, requestedOffset: number, requestedLength: number) => void;
    /**
     * This callback function is implemented by applications to release related resources.
     *
     * > **NOTE**
     * >
     * > The client must return the handle immediately after processing the request.
     *
     * @param { number } uuid - ID for the resource handle.
     * @returns { void } - client should return immediately.
     * @syscap SystemCapability.Multimedia.Media.Core
     * @atomicservice
     * @since 18
     */
    type SourceCloseCallback = (uuid: number) => void;
    /**
     * Defines a media data loader, which needs to be implemented by applications.
     *
     * @syscap SystemCapability.Multimedia.Media.Core
     * @atomicservice
     * @since 18
     */
    interface MediaSourceLoader {
        /**
         * Callback function is implemented by application, which is used to handle resource opening requests.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 18
         */
        open: SourceOpenCallback;
        /**
         * Callback function is implemented by application, which is used to handle resource read requests.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 18
         */
        read: SourceReadCallback;
        /**
         * Callback function is implemented by application, which is used to handle resource close request.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 18
         */
        close: SourceCloseCallback;
    }
    /**
     * Enumerates the reasons for data loading status changes.
     *
     * @syscap SystemCapability.Multimedia.Media.Core
     * @atomicservice
     * @since 18
     */
    enum LoadingRequestError {
        /**
         * Returned by the client to indicate that the end of the resource.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 18
         */
        LOADING_ERROR_SUCCESS = 0,
        /**
         * Returned by the client to indicate that the resource is not ready for access.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 18
         */
        LOADING_ERROR_NOT_READY = 1,
        /**
         * Returned by the client to indicate that the requested resource URL does not exist.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 18
         */
        LOADING_ERROR_NO_RESOURCE = 2,
        /**
         * Returned by the client to indicate that the ID of the requested resource handle (specified by **uuid**) is
         * invalid.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 18
         */
        LOADING_ERROR_INVAID_HANDLE = 3,
        /**
         * Returned by the client to indicate that the client does not have permission to request the resource.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 18
         */
        LOADING_ERROR_ACCESS_DENIED = 4,
        /**
         * Returned by the client to indicate that the access to the resource times out.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 18
         */
        LOADING_ERROR_ACCESS_TIMEOUT = 5,
        /**
         * Returned by the client to indicate that authorization fails.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 18
         */
        LOADING_ERROR_AUTHORIZE_FAILED = 6
    }
    /**
     * The MediaSourceLoadingRequest class defines a loading request object. Applications use this object to obtain the
     * location of the requested resource and to interact with the player for data exchange.
     *
     * @syscap SystemCapability.Multimedia.Media.Core
     * @atomicservice
     * @since 18
     */
    interface MediaSourceLoadingRequest {
        /**
         * Resource URL, which is the path to the resource that the application needs to open.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 18
         */
        url: string;
        /**
         * HTTP request header. If the header exists, the application should set the header information in the HTTP request
         * when downloading data.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 18
         */
        header?: Record<string, string>;
        /**
         * Sends data to the player.
         *
         * @param { number } uuid - ID for the resource handle. The source is
         *     [SourceOpenCallback]{@link @ohos.multimedia.media:media.SourceOpenCallback}.
         * @param { number } offset - Offset of the current media data relative to the start of the resource. The value
         *     cannot be less than 0.
         * @param { ArrayBuffer } buffer - Media data sent to the player.<br>**Note**: Do not transmit irrelevant data, as
         *     it can affect normal data parsing and playback.
         * @returns { number } Number of bytes received by the server.
         *     <br>- A return value less than 0 indicates failure.
         *     <br>- A return value of -2 indicates that the player no longer needs the current data, and the client should stop
         *     the current read process.
         *     <br>- A return value of -3 indicates that the player's buffer is full, and the client should wait for the next read.
         * @syscap  SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 18
         */
        respondData(uuid: number, offset: number, buffer: ArrayBuffer): number;
        /**
         * Sends response header information to the player. This API must be called before the first call to
         * [respondData]{@link media.MediaSourceLoadingRequest.respondData(uuid: number, offset: number, buffer: ArrayBuffer)}.
         *
         * @param { number } uuid - ID for the resource handle. The source is
         *     [SourceOpenCallback]{@link @ohos.multimedia.media:media.SourceOpenCallback}.
         * @param { Record<string, string> } [header] - Header information in the HTTP response. The application can
         *     intersect the header fields with the fields supported by the underlying layer for parsing or directly pass in
         *     all corresponding header information.<br> - The following fields need to be parsed by the underlying player:
         *     Transfer-Encoding, Location, Content-Type, Content-Range, Content-Encode, Accept-Ranges, and content-length.
         * @param { string } [redirectUrl] - Redirect URL in the HTTP response.
         * @syscap  SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 18
         */
        respondHeader(uuid: number, header?: Record<string, string>, redirectUrl?: string): void;
        /**
         * Notifies the player of the current request status. After pushing all the data for a single resource, the
         * application should send the **LOADING_ERROR_SUCCESS** state to notify the player that the resource push is
         * complete.
         *
         * @param { number } uuid - ID for the resource handle. The source is
         *     [SourceOpenCallback]{@link @ohos.multimedia.media:media.SourceOpenCallback}.
         * @param { LoadingRequestError } state - Request status.
         * @syscap  SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 18
         */
        finishLoading(uuid: number, state: LoadingRequestError): void;
    }
    /**
     * Media Stream. AVPlayer use this for mediaData access, current version only support live stream.
     *
     * @syscap SystemCapability.Multimedia.Media.Core
     * @atomicservice
     * @since 19
     */
    interface MediaStream {
        /**
         * url for this mediaStream
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 19
         */
        url: string;
        /**
         * video width.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 19
         */
        width: number;
        /**
         * video height.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 19
         */
        height: number;
        /**
         * biterate of this mediaStream.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 19
         */
        bitrate: number;
    }
    /**
     * The MediaSource class defines the media data information, which is from
     * [createMediaSourceWithUrl]{@link @ohos.multimedia.media:media.createMediaSourceWithUrl(url: string, headers?: Record<string, string>)}.
     *
     * @syscap SystemCapability.Multimedia.Media.Core
     * @atomicservice
     * @since 12
     */
    interface MediaSource {
        /**
         * Sets the MIME type to help the player process extended media sources.
         *
         * @param { AVMimeTypes } mimeType - MIME type.
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 12
         */
        setMimeType(mimeType: AVMimeTypes): void;
        /**
         * Sets a MediaSourceLoader object, which is used to help the player request media data.
         *
         * @param { MediaSourceLoader } resourceLoader - **MediaSourceLoader** object used to obtain media data for the
         *     player.
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 18
         */
        setMediaResourceLoaderDelegate(resourceLoader: MediaSourceLoader): void;
        /**
        * Sets whether to enable offline caching during video playback.
        *
        * @param { boolean } enable - Whether to enable offline caching during video playback. **true** to enable, **false**
        *     otherwise.
        * @syscap SystemCapability.Multimedia.Media.Core
        * @since 23
        */
        enableOfflineCache(enable: boolean): void;
        /**
         * Gets the identifier of the media source.
         *
         * @returns { string } Identifier of the media source. Empty string means call failed.
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        getID(): string;
    }
    /**
     * Enumerates the MIME type, which is set by using
     * [setMimeType]{@link @ohos.multimedia.media:media.MediaSource.setMimeType}.
     *
     * @syscap SystemCapability.Multimedia.Media.Core
     * @atomicservice
     * @since 12
     */
    enum AVMimeTypes {
        /**
         * Local M3U8 file.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 12
         */
        APPLICATION_M3U8 = 'application/m3u8'
    }
    /**
     * Provides preferred playback settings for player.
     *
     * @syscap SystemCapability.Multimedia.Media.Core
     * @atomicservice
     * @since 12
     */
    interface PlaybackStrategy {
        /**
         * Choose a stream with width close to it.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 12
         */
        preferredWidth?: number;
        /**
         * Choose a stream with height close to it.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 12
         */
        preferredHeight?: number;
        /**
         * Chooses a preferred buffer duration.
         *
         * <p>The preferred buffer duration in the playback policy, is used to set the buffer size. For details,
         * see [Online Video Frame Freezing Optimization Practice]{@link
         * https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-online-video-playback-lags-practice}.</p>
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 12
         */
        preferredBufferDuration?: number;
        /**
         * If true, the player should choose HDR stream if exist.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 12
         */
        preferredHdr?: boolean;
        /**
         * mute the specified media stream when playing.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @since 12
         */
        mutedMediaType?: MediaType;
        /**
         * Audio language.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 13
         */
        preferredAudioLanguage?: string;
        /**
         * Subtitle language.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 13
         */
        preferredSubtitleLanguage?: string;
        /**
         * Show first frame on prepare.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 17
         */
        showFirstFrameOnPrepare?: boolean;
        /**
         * Customize the buffering threshold for start or restart playing. The unit is second.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 18
         */
        preferredBufferDurationForPlaying?: number;
        /**
         * Enable super-resolution feature. default is false.
         * Must enable super-resolution feature before calling {@link #setSuperResolution} and {@link #setVideoWindowSize}.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 18
         */
        enableSuperResolution?: boolean;
        /**
         * set max buffering threshold for liveStreaming or avplayer while change the speed.
         * It is recommended that the value be 2 seconds greater than the starting waterline.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 18
         */
        thresholdForAutoQuickPlay?: number;
        /**
         * Indicates whether to keep the decoder working when closing the media,
         * which is used to facilitate quick opening of the media. Currently only supports video
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 20
         */
        keepDecodingOnMute?: boolean;
    }
    /**
     * Media file descriptor. The caller needs to ensure that the fd is valid and
     * the offset and length are correct.
     *
     * @syscap SystemCapability.Multimedia.Media.Core
     * @crossplatform [since 12]
     * @atomicservice [since 11]
     * @since 9
     */
    interface AVFileDescriptor {
        /**
         * The file descriptor of audio or video source from file system. The caller
         * is responsible to close the file descriptor.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        fd: number;
        /**
         * The offset into the file where the data to be read, in bytes. By default,
         * the offset is zero.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        offset?: number;
        /**
         * The length in bytes of the data to be read. By default, the length is the
         * rest of bytes in the file from the offset.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 9
         */
        length?: number;
    }
    /**
     * Defines the descriptor of an audio and video file, which is used in DataSource playback mode.
     * Use scenario: An application can create a playback instance and start playback before it finishes
     * downloading the audio and video resources.
     *
     * @syscap SystemCapability.Multimedia.Media.AVPlayer
     * @crossplatform [since 12]
     * @atomicservice [since 11]
     * @since 10
     */
    interface AVDataSrcDescriptor {
        /**
         * Size of the file, -1 means the file size is unknown, in this case,
         * seek and setSpeed can't be executed, loop can't be set, and can't replay.
         *
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        fileSize: number;
        /**
         * Callback function implemented by users, which is used to fill data.
         * buffer - The buffer need to fill.
         * length - The stream length player want to get.
         * pos - The stream position player want get start, and is an optional parameter.
         * When fileSize set to -1, this parameter is not used.
         * Returns length of the data to be filled, Return -1 to indicate that the end of the stream is reached,
         * Return -2 to indicate that an unrecoverable error has been encountered.
         *
         * @syscap SystemCapability.Multimedia.Media.AVPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 10
         */
        callback: (buffer: ArrayBuffer, length: number, pos?: number) => number;
    }
    /**
     * Provides subtitle information. When a subtitle update event is subscribed to, the information about the
     * external subtitle is returned through a callback.
     * Can be synchronized to the time reported by AVPlayer#timeUpdate event
     *
     * @syscap SystemCapability.Multimedia.Media.Core
     * @atomicservice
     * @since 12
     */
    interface SubtitleInfo {
        /**
         * Duration of the text to be displayed, as milliseconds.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 12
         */
        duration?: number;
        /**
         * Display start time of the text, as milliseconds.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 12
         */
        startTime?: number;
        /**
         * Text information of current update event.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 12
         */
        text?: string;
    }
    /**
   * Describes the audio playback state. You can obtain the state through the **state** property.
   *
   * @unionmember { 'idle' } No audio playback is in progress. The audio player is in this state after the
   *     **'dataload'** or **'reset'** event is triggered.
   * @unionmember { 'playing' } Audio playback is in progress. The audio player is in this state after the **'play'**
   *     event is triggered.
   * @unionmember { 'paused' } Audio playback is paused. The audio player is in this state after the **'pause'** event
   *     is triggered.
   * @unionmember { 'stopped' } Audio playback is stopped. The audio player is in this state after the **'stop'** event
   *     is triggered.
   * @unionmember { 'error' } Audio playback is in the error state.
   * @syscap SystemCapability.Multimedia.Media.AudioPlayer
   * @since 6
   * @deprecated since 9
   * @useinstead media.AVPlayerState
   */
    type AudioState = 'idle' | 'playing' | 'paused' | 'stopped' | 'error';
    /**
     * AudioPlayer is a class for audio playback management. It provides APIs to manage and play audio. Before calling any
     * API in AudioPlayer, you must use [createAudioPlayer()]{@link @ohos.multimedia.media:media.createAudioPlayer} to
     * create an AudioPlayer instance.
     *
     * @syscap SystemCapability.Multimedia.Media.AudioPlayer
     * @since 6
     * @deprecated since 9
     * @useinstead @ohos.multimedia.media:media
     */
    interface AudioPlayer {
        /**
         * Starts to play an audio asset. This API can be called only after the **'dataLoad'** event is triggered.
         *
         * @syscap SystemCapability.Multimedia.Media.AudioPlayer
         * @since 6
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVPlayer.play(callback: AsyncCallback<void>)
         */
        play(): void;
        /**
         * Pauses audio playback.
         *
         * @syscap SystemCapability.Multimedia.Media.AudioPlayer
         * @since 6
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVPlayer.pause(callback: AsyncCallback<void>)
         */
        pause(): void;
        /**
         * Stops audio playback.
         *
         * @syscap SystemCapability.Multimedia.Media.AudioPlayer
         * @since 6
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVPlayer.stop(callback: AsyncCallback<void>)
         */
        stop(): void;
        /**
         * Resets the audio asset to be played.
         *
         * @syscap SystemCapability.Multimedia.Media.AudioPlayer
         * @since 7
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVPlayer.reset(callback: AsyncCallback<void>)
         */
        reset(): void;
        /**
         * Seeks to the specified playback position.
         *
         * @param { number } timeMs - Position to seek to, in ms. The value range is [0, duration].
         * @syscap SystemCapability.Multimedia.Media.AudioPlayer
         * @since 6
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVPlayer.seek
         */
        seek(timeMs: number): void;
        /**
         * Sets the volume.
         *
         * @param { number } vol - Relative volume. The value ranges from 0.00 to 1.00. The value **1.00** indicates the
         *     maximum volume (100%).
         * @syscap SystemCapability.Multimedia.Media.AudioPlayer
         * @since 6
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVPlayer.setVolume
         */
        setVolume(vol: number): void;
        /**
         * Releases the audio playback resources.
         *
         * @syscap SystemCapability.Multimedia.Media.AudioPlayer
         * @since 6
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVPlayer.release(callback: AsyncCallback<void>)
         */
        release(): void;
        /**
         * Obtains the audio track information. It can be called only after the **'dataLoad'** event is triggered. This API
         * uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<Array<MediaDescription>> } callback - Callback used to return the result. If the operation
         *     is successful, **err** is **undefined** and **data** is the MediaDescription array obtained; otherwise,
         *     **err** is an error object.
         * @syscap SystemCapability.Multimedia.Media.AudioPlayer
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVPlayer.getTrackDescription(callback: AsyncCallback<Array<MediaDescription>>)
         */
        getTrackDescription(callback: AsyncCallback<Array<MediaDescription>>): void;
        /**
         * Obtains the audio track information. It can be called only after the **'dataLoad'** event is triggered. This API
         * uses a promise to return the result.
         *
         * @returns { Promise<Array<MediaDescription>> } Promise used to return a **MediaDescription** array, which records
         *     the audio track information.
         * @syscap SystemCapability.Multimedia.Media.AudioPlayer
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVPlayer.getTrackDescription()
         */
        getTrackDescription(): Promise<Array<MediaDescription>>;
        /**
         * Subscribes to the audio buffering update event. This API works only under online playback.
         *
         * @param { 'bufferingUpdate' } type - Event type, which is **'bufferingUpdate'** in this case.
         * @param { function } callback - Callback invoked when the event is triggered.<br>The value of
         *     [BufferingInfoType]{@link @ohos.multimedia.media:media.BufferingInfoType} is fixed at **0**.
         * @syscap SystemCapability.Multimedia.Media.AudioPlayer
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVPlayer.on(type: 'bufferingUpdate', callback: OnBufferingUpdateHandler)
         */
        on(type: 'bufferingUpdate', callback: (infoType: BufferingInfoType, value: number) => void): void;
        /**
         * Audio file URI. The mainstream audio formats (M4A, AAC, MP3, OGG, WAV, and AMR) are supported.
         *
         * **Example of supported URLs**:
         *
         * 1. FD: fd://xx
         *
         * ![](docroot://reference/apis-media-kit/figures/en-us_image_url.png)
         *
         * 2. HTTP: http://xx
         * 3. HTTPS: https://xx
         * 4. HLS: http://xx or https://xx
         *
         * ohos.permission.READ_MEDIA or ohos.permission.INTERNET
         *
         * @permission ohos.permission.READ_MEDIA or ohos.permission.INTERNET
         * @syscap SystemCapability.Multimedia.Media.AudioPlayer
         * @since 6
         * @deprecated since 9
         * @useinstead ohos.multimedia.media/media.AVPlayer#url
         */
        src: string;
        /**
         * Description of the audio file. This property is required when audio assets of an application are continuously
         * stored in a file.
         *
         * Assume that a music file that stores continuous music assets consists of the following:
         *
         * Music 1 (address offset: 0, byte length: 100)
         *
         * Music 2 (address offset: 101; byte length: 50)
         *
         * Music 3 (address offset: 151, byte length: 150)
         *
         * 1. To play music 1: AVFileDescriptor { fd = resource handle; offset = 0; length = 100; }
         * 2. To play music 2: AVFileDescriptor { fd = resource handle; offset = 101; length = 50; }
         * 3. To play music 3: AVFileDescriptor { fd = resource handle; offset = 151; length = 150; }
         *
         * To play an independent music file, use **src=fd://xx**.
         *
         * @syscap SystemCapability.Multimedia.Media.AudioPlayer
         * @since 9
         * @deprecated since 9
         * @useinstead ohos.multimedia.media/media.AVPlayer#fdSrc
         */
        fdSrc: AVFileDescriptor;
        /**
         * Whether to loop audio playback. **true** to loop, **false** otherwise.
         *
         * @syscap SystemCapability.Multimedia.Media.AudioPlayer
         * @since 6
         * @deprecated since 9
         * @useinstead ohos.multimedia.media/media.AVPlayer#loop
         */
        loop: boolean;
        /**
         * Audio interruption mode.
         *
         * @syscap SystemCapability.Multimedia.Media.AudioPlayer
         * @since 9
         * @deprecated since 9
         * @useinstead ohos.multimedia.media/media.AVPlayer#audioInterruptMode
         */
        audioInterruptMode?: audio.InterruptMode;
        /**
         * Current audio playback position, in ms.
         *
         * @syscap SystemCapability.Multimedia.Media.AudioPlayer
         * @since 6
         * @deprecated since 9
         * @useinstead ohos.multimedia.media/media.AVPlayer#currentTime
         */
        readonly currentTime: number;
        /**
         * Audio duration, in ms.
         *
         * @syscap SystemCapability.Multimedia.Media.AudioPlayer
         * @since 6
         * @deprecated since 9
         * @useinstead ohos.multimedia.media/media.AVPlayer#duration
         */
        readonly duration: number;
        /**
         * Audio playback state. This state cannot be used as the condition for triggering the call of **play()**,
         * **pause()**, or **stop()**.
         *
         * @syscap SystemCapability.Multimedia.Media.AudioPlayer
         * @since 6
         * @deprecated since 9
         * @useinstead ohos.multimedia.media/media.AVPlayer#state
         */
        readonly state: AudioState;
        /**
         * Subscribes to the audio playback events.
         *
         * @param { 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange' } type - Event type. The
         *     following events are supported:<br>- 'play': triggered when the [play()]{@link media.AudioPlayer.play} API is
         *     called and audio playback starts.<br>- 'pause': triggered when the [pause()]{@link media.AudioPlayer.pause}
         *     API is called and audio playback is paused.<br>- 'stop': triggered when the
         *     [stop()]{@link media.AudioPlayer.stop} API is called and audio playback stops.<br>- 'reset': triggered when
         *     the [reset()]{@link media.AudioPlayer.reset} API is called and audio playback is reset.<br>- 'dataLoad':
         *     triggered when the audio data is loaded, that is, when the **src** property is configured.<br>- 'finish':
         *     triggered when the audio playback is finished.<br>- 'volumeChange': triggered when the
         *     [setVolume()]{@link media.AudioPlayer.setVolume} API is called and the playback volume is changed.
         * @param { function } callback - Callback invoked when the event is triggered.
         * @syscap SystemCapability.Multimedia.Media.AudioPlayer
         * @since 6
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVPlayer.on(type: 'stateChange', callback: OnAVPlayerStateChangeHandle)
         */
        on(type: 'play' | 'pause' | 'stop' | 'reset' | 'dataLoad' | 'finish' | 'volumeChange', callback: () => void): void;
        /**
         * Subscribes to the **'timeUpdate'** event. This event is reported every second when the audio playback is in
         * progress.
         *
         * @param { 'timeUpdate' } type - Event type, which is **'timeUpdate'** in this case.<br>The **'timeUpdate'** event
         *     is triggered when the audio playback starts after an audio playback timestamp update.
         * @param { Callback<number> } callback - Callback invoked when the event is triggered. The input parameter is the
         *     updated timestamp.
         * @syscap SystemCapability.Multimedia.Media.AudioPlayer
         * @since 6
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVPlayer.on(type: 'timeUpdate', callback: Callback<int>)
         */
        on(type: 'timeUpdate', callback: Callback<number>): void;
        /**
         * Subscribes to the audio interruption event. For details, see
         * [audio.InterruptEvent]{@link @ohos.multimedia.audio:audio.InterruptEvent}.
         *
         * @param { 'audioInterrupt' } type - Event type, which is **'audioInterrupt'** in this case.
         * @param { function } callback - Callback invoked when the event is triggered.
         * @syscap SystemCapability.Multimedia.Media.AudioPlayer
         * @since 9
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVPlayer.on(type: 'audioInterrupt', callback: Callback<audio.InterruptEvent>)
         */
        on(type: 'audioInterrupt', callback: (info: audio.InterruptEvent) => void): void;
        /**
         * Subscribes to audio playback error events. After an error event is reported, you must handle the event and exit
         * the playback.
         *
         * @param { 'error' } type - Event type, which is **'error'** in this case.<br>This event is triggered when an error
         *     occurs during audio playback.
         * @param { ErrorCallback } callback - Callback invoked when the event is triggered.
         * @syscap SystemCapability.Multimedia.Media.AudioPlayer
         * @since 6
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVPlayer.on(type: 'error', callback: ErrorCallback)
         */
        on(type: 'error', callback: ErrorCallback): void;
    }
    /**
     * Enumerates the AVRecorder states. You can obtain the state through the **state** property.
     *
     * @unionmember { 'idle' } The AVRecorder enters this state after it is just created or the
     *     [AVRecorder.reset()]{@link @ohos.multimedia.media:media.AVRecorder.reset(callback: AsyncCallback<void>)} API is
     *     called when the AVRecorder is in any state except released. In this state, you can call
     *     [AVRecorder.prepare()]{@link @ohos.multimedia.media:media.AVRecorder.prepare(config: AVRecorderConfig, callback: AsyncCallback<void>)}
     *     to set recording parameters.
     * @unionmember { 'prepared' } The AVRecorder enters this state when the parameters are set. In this state, you can
     *     call [AVRecorder.start()]{@link @ohos.multimedia.media:media.AVRecorder.start(callback: AsyncCallback<void>)}
     *     to start recording.
     * @unionmember { 'started' } The AVRecorder enters this state when the recording starts. In this state, you can call
     *     [AVRecorder.pause()]{@link @ohos.multimedia.media:media.AVRecorder.pause(callback: AsyncCallback<void>)} to
     *     pause recording or call
     *     [AVRecorder.stop()]{@link @ohos.multimedia.media:media.AVRecorder.stop(callback: AsyncCallback<void>)} to stop
     *     recording.
     * @unionmember { 'paused' } The AVRecorder enters this state when the recording is paused. In this state, you can
     *     call [AVRecorder.resume()]{@link @ohos.multimedia.media:media.AVRecorder.resume(callback: AsyncCallback<void>)}
     *     to continue recording or call
     *     [AVRecorder.stop()]{@link @ohos.multimedia.media:media.AVRecorder.stop(callback: AsyncCallback<void>)} to stop
     *     recording.
     * @unionmember { 'stopped' } The AVRecorder enters this state when the recording stops. In this state, you can call
     *     [AVRecorder.prepare()]{@link @ohos.multimedia.media:media.AVRecorder.prepare(config: AVRecorderConfig, callback: AsyncCallback<void>)}
     *     to set recording parameters so that the AVRecorder enters the prepared state again.
     * @unionmember { 'released' } The AVRecorder enters this state when the recording resources are released. In this
     *     state, no operation can be performed. In any other state, you can call
     *     [AVRecorder.release()]{@link @ohos.multimedia.media:media.AVRecorder.release(callback: AsyncCallback<void>)} to
     *     enter the released state.
     * @unionmember { 'error' } The AVRecorder enters this state when an irreversible error occurs in the AVRecorder
     *     instance. In this state, the
     *     [AVRecorder.on('error') event]{@link @ohos.multimedia.media:media.AVRecorder.on(type: 'error', callback: ErrorCallback)}
     *     is reported, with the detailed error cause. In the error state, you must call
     *     [AVRecorder.reset()]{@link @ohos.multimedia.media:media.AVRecorder.reset(callback: AsyncCallback<void>)} to
     *     reset the AVRecorder instance or call
     *     [AVRecorder.release()]{@link @ohos.multimedia.media:media.AVRecorder.release(callback: AsyncCallback<void>)} to
     *     release the resources.
     * @syscap SystemCapability.Multimedia.Media.AVRecorder
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 9
     */
    type AVRecorderState = 'idle' | 'prepared' | 'started' | 'paused' | 'stopped' | 'released' | 'error';
    /**
     * Describes the callback invoked for the AVRecorder state change event.
     *
     * @param { AVRecorderState } state - AVRecorder state.
     * @param { StateChangeReason } reason - Reason for the state change.
     * @syscap SystemCapability.Multimedia.Media.AVRecorder
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    type OnAVRecorderStateChangeHandler = (state: AVRecorderState, reason: StateChangeReason) => void;
    /**
     * AVRecorder is a class for audio and video recording management. It provides APIs to record media assets. Before
     * calling any API in AVRecorder, you must use
     * [createAVRecorder()]{@link @ohos.multimedia.media:media.createAVRecorder(callback: AsyncCallback<AVRecorder>)} to
     * create an AVRecorder instance.
     *
     * For details about the audio and video recording demo, see
     * [Audio Recording](docroot://media/media/using-avrecorder-for-recording.md) and
     * [Video Recording](docroot://media/media/video-recording.md).
     *
     * > **NOTE**
     * >
     * > > To use the camera to record videos, the camera module is required. For details about how to use the APIs
     * > provided by the camera module, see [Camera Management]{@link @ohos.multimedia.camera:camera}.
     *
     * @syscap SystemCapability.Multimedia.Media.AVRecorder
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 9
     */
    interface AVRecorder {
        /**
         * Sets audio and video recording parameters. This API uses an asynchronous callback to return the result.
         *
         * @permission ohos.permission.MICROPHONE
         * @param { AVRecorderConfig } config - Audio and video recording parameters to set.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @throws { BusinessError } 201 - Permission denied. Return by callback.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3. Parameter verification failed.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by callback.
         * @throws { BusinessError } 5400105 - Service died. Return by callback.
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @crossplatform [since 12]
         * @since 9
         */
        prepare(config: AVRecorderConfig, callback: AsyncCallback<void>): void;
        /**
         * Sets audio and video recording parameters. This API uses a promise to return the result.
         *
         * @permission ohos.permission.MICROPHONE [since 9 - 11]
         * @permission ohos.permission.MICROPHONE
         *     This permission is required only if audio recording is involved. [since 12]
         * @param { AVRecorderConfig } config - Audio and video recording parameters to set.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 201 - Permission denied. Return by promise.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3. Parameter verification failed.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by promise.
         * @throws { BusinessError } 5400105 - Service died. Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        prepare(config: AVRecorderConfig): Promise<void>;
        /**
         * Obtains the real-time configuration of this AVRecorder. This API uses an asynchronous callback to return the
         * result.
         *
         * This API can be called only after
         * [prepare()]{@link media.AVRecorder.prepare(config: AVRecorderConfig, callback: AsyncCallback<void>)} is called.
         *
         * @param { AsyncCallback<AVRecorderConfig> } callback - Callback used to return the result. If the operation is
         *     successful, **err** is **undefined** and **data** is the real-time configuration obtained; otherwise, **err**
         *     is an error object.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by callback.
         * @throws { BusinessError } 5400103 - IO error. Return by callback.
         * @throws { BusinessError } 5400105 - Service died. Return by callback.
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @since 11
         */
        getAVRecorderConfig(callback: AsyncCallback<AVRecorderConfig>): void;
        /**
         * Obtains the real-time configuration of this AVRecorder. This API uses a promise to return the result.
         *
         * This API can be called only after [prepare()]{@link media.AVRecorder.prepare(config: AVRecorderConfig)} is
         * called.
         *
         * @returns { Promise<AVRecorderConfig> } Promise used to return the real-time configuration.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by promise.
         * @throws { BusinessError } 5400103 - IO error. Return by promise.
         * @throws { BusinessError } 5400105 - Service died. Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @since 11
         */
        getAVRecorderConfig(): Promise<AVRecorderConfig>;
        /**
         * Obtains the surface required for recording. This API uses an asynchronous callback to return the result.
         *
         * The caller obtains the surface buffer from this surface and fills in the corresponding video data.
         *
         * Note that the video data must carry the timestamp (in ns) and buffer size, and the start time of the timestamp
         * must be based on the system startup time.
         *
         * This API can be called only after the
         * [prepare()]{@link media.AVRecorder.prepare(config: AVRecorderConfig, callback: AsyncCallback<void>)} API is
         * called.
         *
         * @param { AsyncCallback<string> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **data** is the surface ID obtained; otherwise, **err** is an error object.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by callback.
         * @throws { BusinessError } 5400103 - IO error. Return by callback.
         * @throws { BusinessError } 5400105 - Service died. Return by callback.
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @since 9
         */
        getInputSurface(callback: AsyncCallback<string>): void;
        /**
         * Obtains the surface required for recording. This API uses a promise to return the result.
         *
         * The caller obtains the surface buffer from this surface and fills in the corresponding video data.
         *
         * Note that the video data must carry the timestamp (in ns) and buffer size, and the start time of the timestamp
         * must be based on the system startup time.
         *
         * This API can be called only after the [prepare()]{@link media.AVRecorder.prepare(config: AVRecorderConfig)} API
         * is called.
         *
         * @returns { Promise<string> } Promise used to return the surface buffer obtained from the surface.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by promise.
         * @throws { BusinessError } 5400103 - IO error. Return by promise.
         * @throws { BusinessError } 5400105 - Service died. Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @since 9
         */
        getInputSurface(): Promise<string>;
        /**
         * add a watermark for the AVRecorder. This API uses a promise to return the result.
         * App can add up to 5 watermarks.
         * This API can be called only before the prepared state.
         *
         * @param { image.PixelMap } watermark - : Watermark image.
         * @param { WatermarkConfiguration } config - : Configuration of the watermark.
         * @returns { Promise<number> } Promise that returns the watermark id.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by promise.
         * @throws { BusinessError } 5400103 - IO error. Return by promise.
         * @throws { BusinessError } 5400105 - Service died. Return by promise.
         * @throws { BusinessError } 5400108 - The parameter check failed, parameter value out of range.
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @stagemodelonly
         * @since 26.0.0
         */
        addWatermark(watermark: image.PixelMap, config: WatermarkConfiguration): Promise<number>;
        /**
         * Set metadata (key-value pairs) for the recording file of the recorder.
         * This metadata overwrites the value in config.metadata.customInfo (see {prepare()} and {AVRecorderConfig})
         * if they have same key.
         *
         * This API can be called only after the prepare() event is successfully triggered and
         * before the stop() API is called.
         *
         * @param { Record<string, string> } metadata - Tag and value of the metadata in key-value pairs.
         *     <br>- The first string is the key.<br>- The second string is the value.
         *     <br> The key string should start with "com.openharmony.", the length of value can't be more than 256 bytes.
         * @throws { BusinessError } 5400101 - No memory.
         * @throws { BusinessError } 5400102 - Operation not allowed.
         * @throws { BusinessError } 5400108 - Parameter check failed.
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @since 26.0.0
         */
        setMetadata(metadata: Record<string, string>): void;
        /**
         * Updates the video rotation angle, in degrees. This API uses a promise to return the result.
         *
         * This API can be called only after the [prepare()]{@link media.AVRecorder.prepare(config: AVRecorderConfig)} event
         * is triggered and before the [start()]{@link media.AVRecorder.start(callback: AsyncCallback<void>)} API is called.
         *
         * @param { number } rotation - Rotation angle, which can only be 0, 90, 180, or 270 degrees.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     2. Incorrect parameter types. 3. Parameter verification failed.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by promise.
         * @throws { BusinessError } 5400103 - IO error. Return by promise.
         * @throws { BusinessError } 5400105 - Service died. Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @since 12
         */
        updateRotation(rotation: number): Promise<void>;
        /**
         * Sets whether to mute the current audio recording stream when an audio interruption occurs. This API uses a
         * promise to return the result.
         *
         * @param { boolean } muteWhenInterrupted - Whether to mute the current audio recording stream during an audio
         *     interruption. **true** to mute, **false** otherwise.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by promise.
         * @throws { BusinessError } 5400105 - Service died. Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @since 20
         */
        setWillMuteWhenInterrupted(muteWhenInterrupted: boolean): Promise<void>;
        /**
         * Starts video recording. This API uses an asynchronous callback to return the result.
         *
         * For audio-only recording, this API can be called only after the
         * [prepare()]{@link media.AVRecorder.prepare(config: AVRecorderConfig, callback: AsyncCallback<void>)} API is
         * called. For video-only recording, this API can be called only after the
         * [getInputSurface()]{@link media.AVRecorder.getInputSurface(callback: AsyncCallback<string>)} API is called.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by callback.
         * @throws { BusinessError } 5400103 - IO error. Return by callback.
         * @throws { BusinessError } 5400105 - Service died. Return by callback.
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @crossplatform [since 12]
         * @since 9
         */
        start(callback: AsyncCallback<void>): void;
        /**
         * Starts video recording. This API uses a promise to return the result.
         *
         * For audio-only recording, this API can be called only after the
         * [prepare()]{@link media.AVRecorder.prepare(config: AVRecorderConfig)} API is called. For video-only recording,
         * this API can be called only after the [getInputSurface()]{@link media.AVRecorder.getInputSurface()} API is
         * called.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by promise.
         * @throws { BusinessError } 5400103 - IO error. Return by promise.
         * @throws { BusinessError } 5400105 - Service died. Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        start(): Promise<void>;
        /**
         * Pauses video recording. This API uses an asynchronous callback to return the result.
         *
         * This API can be called only after the [start()]{@link media.AVRecorder.start(callback: AsyncCallback<void>)} API
         * is called. You can call [resume()]{@link media.AVRecorder.resume(callback: AsyncCallback<void>)} to resume
         * recording.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by callback.
         * @throws { BusinessError } 5400103 - IO error. Return by callback.
         * @throws { BusinessError } 5400105 - Service died. Return by callback.
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @crossplatform [since 12]
         * @since 9
         */
        pause(callback: AsyncCallback<void>): void;
        /**
         * Pauses video recording. This API uses a promise to return the result.
         *
         * This API can be called only after the [start()]{@link media.AVRecorder.start()} API is called. You can call
         * [resume()]{@link media.AVRecorder.resume()} to resume recording.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by promise.
         * @throws { BusinessError } 5400103 - IO error. Return by promise.
         * @throws { BusinessError } 5400105 - Service died. Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        pause(): Promise<void>;
        /**
         * Resumes video recording. This API uses an asynchronous callback to return the result.
         *
         * This API can be called only after the [pause()]{@link media.AVRecorder.pause(callback: AsyncCallback<void>)} API
         * is called.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by callback.
         * @throws { BusinessError } 5400103 - IO error. Return by callback.
         * @throws { BusinessError } 5400105 - Service died. Return by callback.
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @crossplatform [since 12]
         * @since 9
         */
        resume(callback: AsyncCallback<void>): void;
        /**
         * Resumes video recording. This API uses a promise to return the result.
         *
         * This API can be called only after the [pause()]{@link media.AVRecorder.pause()} API is called.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by promise.
         * @throws { BusinessError } 5400103 - IO error. Return by promise.
         * @throws { BusinessError } 5400105 - Service died. Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        resume(): Promise<void>;
        /**
         * Stops video recording. This API uses an asynchronous callback to return the result.
         *
         * This API can be called only after the [start()]{@link media.AVRecorder.start(callback: AsyncCallback<void>)} or
         * [pause()]{@link media.AVRecorder.pause(callback: AsyncCallback<void>)} API is called.
         *
         * For audio-only recording, you can call
         * [prepare()]{@link media.AVRecorder.prepare(config: AVRecorderConfig, callback: AsyncCallback<void>)} again for re
         * -recording. For video-only recording or audio and video recording, you can call
         * [prepare()]{@link media.AVRecorder.prepare(config: AVRecorderConfig, callback: AsyncCallback<void>)} and
         * [getInputSurface()]{@link media.AVRecorder.getInputSurface(callback: AsyncCallback<string>)} again for re-
         * recording.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by callback.
         * @throws { BusinessError } 5400103 - IO error. Return by callback.
         * @throws { BusinessError } 5400105 - Service died. Return by callback.
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @crossplatform [since 12]
         * @since 9
         */
        stop(callback: AsyncCallback<void>): void;
        /**
         * Stops video recording. This API uses a promise to return the result.
         *
         * This API can be called only after the [start()]{@link media.AVRecorder.start()} or
         * [pause()]{@link media.AVRecorder.pause()} API is called.
         *
         * For audio-only recording, you can call [prepare()]{@link media.AVRecorder.prepare(config: AVRecorderConfig)}
         * again for re-recording. For video-only recording or audio and video recording, you can call
         * [prepare()]{@link media.AVRecorder.prepare(config: AVRecorderConfig)} and
         * [getInputSurface()]{@link media.AVRecorder.getInputSurface()} again for re-recording.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by promise.
         * @throws { BusinessError } 5400103 - IO error. Return by promise.
         * @throws { BusinessError } 5400105 - Service died. Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        stop(): Promise<void>;
        /**
         * Resets audio and video recording. This API uses an asynchronous callback to return the result.
         *
         * For audio-only recording, you can call
         * [prepare()]{@link media.AVRecorder.prepare(config: AVRecorderConfig, callback: AsyncCallback<void>)} again for re
         * -recording. For video-only recording or audio and video recording, you can call
         * [prepare()]{@link media.AVRecorder.prepare(config: AVRecorderConfig, callback: AsyncCallback<void>)} and
         * [getInputSurface()]{@link media.AVRecorder.getInputSurface(callback: AsyncCallback<string>)} again for re-
         * recording.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @throws { BusinessError } 5400103 - IO error. Return by callback.
         * @throws { BusinessError } 5400105 - Service died. Return by callback.
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @crossplatform [since 12]
         * @since 9
         */
        reset(callback: AsyncCallback<void>): void;
        /**
         * Resets audio and video recording. This API uses a promise to return the result.
         *
         * For audio-only recording, you can call [prepare()]{@link media.AVRecorder.prepare(config: AVRecorderConfig)}
         * again for re-recording. For video-only recording or audio and video recording, you can call
         * [prepare()]{@link media.AVRecorder.prepare(config: AVRecorderConfig)} and
         * [getInputSurface()]{@link media.AVRecorder.getInputSurface()} again for re-recording.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 5400103 - IO error. Return by promise.
         * @throws { BusinessError } 5400105 - Service died. Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @crossplatform [since 12]
         * @since 9
         */
        reset(): Promise<void>;
        /**
         * Releases the audio and video recording resources. This API uses an asynchronous callback to return the result.
         *
         * After the resources are released, you can no longer perform any operation on the AVRecorder instance.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @throws { BusinessError } 5400105 - Service died. Return by callback.
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @crossplatform [since 12]
         * @since 9
         */
        release(callback: AsyncCallback<void>): void;
        /**
         * Releases the audio and video recording resources. This API uses a promise to return the result.
         *
         * After the resources are released, you can no longer perform any operation on the AVRecorder instance.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 5400105 - Service died. Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        release(): Promise<void>;
        /**
         * Obtains the information about the current audio capturer. This API uses an asynchronous callback to return the
         * result.
         *
         * This API can be called only after the
         * [prepare()]{@link media.AVRecorder.prepare(config: AVRecorderConfig, callback: AsyncCallback<void>)} API is
         * called. If this API is called after [stop()]{@link media.AVRecorder.stop(callback: AsyncCallback<void>)} is
         * successfully called, an error is reported.
         *
         * @param { AsyncCallback<audio.AudioCapturerChangeInfo> } callback - Callback used to return the result. If the
         *     operation is successful, **err** is **undefined** and **data** is the audio.AudioCapturerChangeInfo object
         *     obtained; otherwise, **err** is an error object.
         * @throws { BusinessError } 5400102 - Operation not allowed.
         * @throws { BusinessError } 5400103 - I/O error.
         * @throws { BusinessError } 5400105 - Service died. Return by callback.
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @since 11
         */
        getCurrentAudioCapturerInfo(callback: AsyncCallback<audio.AudioCapturerChangeInfo>): void;
        /**
         * Obtains the information about the current audio capturer. This API uses a promise to return the result.
         *
         * This API can be called only after the
         * [prepare()]{@link media.AVRecorder.prepare(config: AVRecorderConfig, callback: AsyncCallback<void>)} API is
         * called. If this API is called after [stop()]{@link media.AVRecorder.stop(callback: AsyncCallback<void>)} is
         * successfully called, an error is reported.
         *
         * @returns { Promise<audio.AudioCapturerChangeInfo> } Promise used to return the audio capturer information.
         * @throws { BusinessError } 5400102 - Operation not allowed.
         * @throws { BusinessError } 5400103 - I/O error.
         * @throws { BusinessError } 5400105 - Service died. Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @since 11
         */
        getCurrentAudioCapturerInfo(): Promise<audio.AudioCapturerChangeInfo>;
        /**
         * Obtains the maximum amplitude of the current audio capturer. This API uses an asynchronous callback to return the
         * result.
         *
         * This API can be called only after the
         * [prepare()]{@link media.AVRecorder.prepare(config: AVRecorderConfig, callback: AsyncCallback<void>)} API is
         * called. If this API is called after [stop()]{@link media.AVRecorder.stop(callback: AsyncCallback<void>)} is
         * successfully called, an error is reported.
         *
         * The return value is the maximum amplitude within the duration from the time the maximum amplitude is obtained
         * last time to the current time. For example, if you have obtained the maximum amplitude at 1s and you call this
         * API again at 2s, then the return value is the maximum amplitude within the duration from 1s to 2s.
         *
         * @param { AsyncCallback<number> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **data** is the maximum amplitude obtained; otherwise, **err** is an error
         *     object.
         * @throws { BusinessError } 5400102 - Operation not allowed.
         * @throws { BusinessError } 5400105 - Service died. Return by callback.
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @since 11
         */
        getAudioCapturerMaxAmplitude(callback: AsyncCallback<number>): void;
        /**
         * Obtains the maximum amplitude of the current audio capturer. This API uses a promise to return the result.
         *
         * This API can be called only after the
         * [prepare()]{@link media.AVRecorder.prepare(config: AVRecorderConfig, callback: AsyncCallback<void>)} API is
         * called. If this API is called after [stop()]{@link media.AVRecorder.stop(callback: AsyncCallback<void>)} is
         * successfully called, an error is reported.
         *
         * The return value is the maximum amplitude within the duration from the time the maximum amplitude is obtained
         * last time to the current time. For example, if you have obtained the maximum amplitude at 1s and you call this
         * API again at 2s, then the return value is the maximum amplitude within the duration from 1s to 2s.
         *
         * @returns { Promise<number> } Promise used to return the maximum amplitude obtained.
         * @throws { BusinessError } 5400102 - Operation not allowed.
         * @throws { BusinessError } 5400105 - Service died. Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @since 11
         */
        getAudioCapturerMaxAmplitude(): Promise<number>;
        /**
         * Obtains available encoders. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<Array<EncoderInfo>> } callback - Callback used to return the result. If the operation is
         *     successful, **err** is **undefined** and **data** is the available encoders obtained; otherwise, **err** is
         *     an error object.
         * @throws { BusinessError } 5400102 - Operation not allowed.
         * @throws { BusinessError } 5400105 - Service died. Return by callback.
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @since 11
         */
        getAvailableEncoder(callback: AsyncCallback<Array<EncoderInfo>>): void;
        /**
         * Obtains available encoders. This API uses a promise to return the result.
         *
         * @returns { Promise<Array<EncoderInfo>> } Promise used to return the information about the available encoders.
         * @throws { BusinessError } 5400102 - Operation not allowed.
         * @throws { BusinessError } 5400105 - Service died. Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @since 11
         */
        getAvailableEncoder(): Promise<Array<EncoderInfo>>;
        /**
         * AVRecorder state.
         *
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        readonly state: AVRecorderState;
        /**
         * Subscribes to audio capturer configuration changes. Any configuration change triggers the callback that returns
         * the entire configuration information. This API uses an asynchronous callback to return the result.
         *
         * When the application initiates multiple subscriptions to this event, the last subscription is applied.
         *
         * @param { 'audioCapturerChange' } type - Event type, which is **'audioCapturerChange'** in this case.
         * @param { Callback<audio.AudioCapturerChangeInfo> } callback - Callback used to return the changed audio capturer
         *     configuration.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     2. Incorrect parameter types. 3. Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @since 11
         */
        on(type: 'audioCapturerChange', callback: Callback<audio.AudioCapturerChangeInfo>): void;
        /**
         * Subscribes to media asset callback events. When
         * [FileGenerationMode]{@link @ohos.multimedia.media:media.FileGenerationMode} is used during media file creation,
         * the [PhotoAsset]{@link @ohos.file.photoAccessHelper:photoAccessHelper} object is called back to the application
         * after the [stop]{@link media.AVRecorder.stop(callback: AsyncCallback<void>)} operation is complete. This API uses
         * an asynchronous callback to return the result.
         *
         * When the application initiates multiple subscriptions to this event, the last subscription is applied.
         *
         * @param { 'photoAssetAvailable' } type - Event type, which is **'photoAssetAvailable'** in this case. The event is
         *     triggered when a photo asset is available.
         * @param { Callback<photoAccessHelper.PhotoAsset> } callback - Callback used to return the PhotoAsset object
         *     corresponding to the resource file created by the system.
         * @throws { BusinessError } 5400103 - IO error. Return by callback.
         * @throws { BusinessError } 5400105 - Service died. Return by callback.
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @since 12
         */
        on(type: 'photoAssetAvailable', callback: Callback<photoAccessHelper.PhotoAsset>): void;
        /**
         * Subscribes to AVRecorder state changes. An application can subscribe to only one AVRecorder state change event.
         * When the application initiates multiple subscriptions to this event, the last subscription is applied. This API
         * uses an asynchronous callback to return the result.
         *
         * @param { 'stateChange' } type - Event type, which is **'stateChange'** in this case. This event can be triggered
         *     by both user operations and the system.
         * @param { function } callback - Callback used to return the state change event. [since 9 - 11]
         * @param { OnAVRecorderStateChangeHandler } callback - Callback used to return the state change event. [since 12]
         * @throws { BusinessError } 5400103 - IO error. Return by callback.
         * @throws { BusinessError } 5400105 - Service died. Return by callback.
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        on(type: 'stateChange', callback: OnAVRecorderStateChangeHandler): void;
        /**
         * Subscribes to AVRecorder errors. This event is used only for error prompt and does not require the user to stop
         * recording control. If the [AVRecorderState]{@link @ohos.multimedia.media:media.AVRecorderState} is also switched
         * to error, call [reset()]{@link media.AVRecorder.reset(callback: AsyncCallback<void>)} or [release()]
         * [release()]{@link media.AVRecorder.release(callback: AsyncCallback<void>)} to exit the recording. This API uses
         * an asynchronous callback to return the result.
         *
         * An application can subscribe to only one AVRecorder error event. When the application initiates multiple
         * subscriptions to this event, the last subscription is applied.
         *
         * @param { 'error' } type - Event type, which is **'error'** in this case.<br>This event is triggered when an error
         *     occurs during recording.
         * @param { ErrorCallback } callback - Callback used to return the recording error event.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3. Parameter verification failed.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 5400101 - No memory.
         * @throws { BusinessError } 5400102 - Operation not allowed.
         * @throws { BusinessError } 5400103 - I/O error.
         * @throws { BusinessError } 5400104 - Operation timeout.
         * @throws { BusinessError } 5400105 - Service died.
         * @throws { BusinessError } 5400106 - Unsupported format.
         * @throws { BusinessError } 5400107 - Audio interrupted. [since 11]
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        on(type: 'error', callback: ErrorCallback): void;
        /**
         * Unsubscribes from AVRecorder state changes. This API uses an asynchronous callback to return the result.
         *
         * @param { 'stateChange' } type - Event type, which is **'stateChange'** in this case. This event can be triggered
         *     by both user operations and the system.
         * @param { OnAVRecorderStateChangeHandler } callback - Callback used to return the state change event. If this
         *     parameter is specified, the subscription to the specified event with the specified callback is canceled. (The
         *     callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with
         *     all the callbacks are canceled.<br>This parameter is supported since API version 12. [since 12]
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        off(type: 'stateChange', callback?: OnAVRecorderStateChangeHandler): void;
        /**
         * Unsubscribes from AVRecorder errors. After the unsubscription, your application can no longer receive AVRecorder
         * errors. This API uses an asynchronous callback to return the result.
         *
         * @param { 'error' } type - Event type, which is **'error'** in this case.<br>This event is triggered when an error
         *     occurs during recording.
         * @param { ErrorCallback } callback - Callback used to return the recording error event. If this parameter is
         *     specified, the subscription to the specified event with the specified callback is canceled. (The callback
         *     object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the
         *     callbacks are canceled.<br>This parameter is supported since API version 12. [since 12]
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        off(type: 'error', callback?: ErrorCallback): void;
        /**
         * Subscribes to audio capturer configuration changes. This API uses an asynchronous callback to return the result.
         *
         * @param { 'audioCapturerChange' } type - Event type, which is **'audioCapturerChange'** in this case.
         * @param { Callback<audio.AudioCapturerChangeInfo> } callback - Callback used to return the changed audio capturer
         *     configuration. If this parameter is specified, the subscription to the specified event with the specified
         *     callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to
         *     the specified event with all the callbacks are canceled.<br>This parameter is supported since API version 12
         *     . [since 12]
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @since 11
         */
        off(type: 'audioCapturerChange', callback?: Callback<audio.AudioCapturerChangeInfo>): void;
        /**
         * Unsubscribes from media asset callback events. This API uses an asynchronous callback to return the result.
         *
         * @param { 'photoAssetAvailable' } type - Event type, which is **'photoAssetAvailable'** in this case.
         * @param { Callback<photoAccessHelper.PhotoAsset> } callback - Callback used to return the PhotoAsset object
         *     corresponding to the resource file created by the system. If this parameter is specified, the subscription to
         *     the specified event with the specified callback is canceled. (The callback object cannot be an anonymous
         *     function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled.
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @since 12
         */
        off(type: 'photoAssetAvailable', callback?: Callback<photoAccessHelper.PhotoAsset>): void;
    }
    /**
     * Enumerates the audio encoding formats.
     *
     * @syscap SystemCapability.Multimedia.Media.AudioRecorder
     * @since 6
     * @deprecated since 8
     * @useinstead media.CodecMimeType
     */
    enum AudioEncoder {
        /**
         * Default encoding format.
         *
         * This API is defined but not implemented yet.
         *
         * Note: It is supported since API version 6 and deprecated since API version 8. You are advised to use
         * **AUDIO_AAC** in [CodecMimeType]{@link media.CodecMimeType} instead.
         *
         * @syscap SystemCapability.Multimedia.Media.AudioRecorder
         * @since 6
         * @deprecated since 8
         */
        DEFAULT = 0,
        /**
         * AMR-NB.
         *
         * This API is defined but not implemented yet.
         *
         * Note: It is supported since API version 6 and deprecated since API version 8. You are advised to use
         * **AUDIO_AMR_NB** in [CodecMimeType]{@link media.CodecMimeType} instead.
         *
         * @syscap SystemCapability.Multimedia.Media.AudioRecorder
         * @since 6
         * @deprecated since 8
         * @useinstead ohos.multimedia.media/media.CodecMimeType#AUDIO_AMR_NB
         */
        AMR_NB = 1,
        /**
         * Adaptive Multi Rate-Wide Band Speech Codec (AMR-WB).
         *
         * This API is defined but not implemented yet.
         *
         * Note: It is supported since API version 6 and deprecated since API version 8. You are advised to use
         * **AUDIO_AMR_WB** in [CodecMimeType]{@link media.CodecMimeType} instead.
         *
         * @syscap SystemCapability.Multimedia.Media.AudioRecorder
         * @since 6
         * @deprecated since 8
         * @useinstead ohos.multimedia.media/media.CodecMimeType#AUDIO_AMR_WB
         */
        AMR_WB = 2,
        /**
         * Advanced Audio Coding Low Complexity (AAC-LC).
         *
         * Note: It is supported since API version 6 and deprecated since API version 8. You are advised to use
         * **AUDIO_AAC** in [CodecMimeType]{@link media.CodecMimeType} instead.
         *
         * @syscap SystemCapability.Multimedia.Media.AudioRecorder
         * @since 6
         * @deprecated since 8
         * @useinstead ohos.multimedia.media/media.CodecMimeType#AUDIO_AAC
         */
        AAC_LC = 3,
        /**
         * High-Efficiency Advanced Audio Coding (HE_AAC).
         *
         * This API is defined but not implemented yet.
         *
         * Note: It is supported since API version 6 and deprecated since API version 8. You are advised to use
         * **AUDIO_AAC** in [CodecMimeType]{@link media.CodecMimeType} instead.
         *
         * @syscap SystemCapability.Multimedia.Media.AudioRecorder
         * @since 6
         * @deprecated since 8
         * @useinstead ohos.multimedia.media/media.CodecMimeType#AUDIO_AAC
         */
        HE_AAC = 4
    }
    /**
     * Enumerates the audio output formats.
     *
     * @syscap SystemCapability.Multimedia.Media.AudioRecorder
     * @since 6
     * @deprecated since 8
     * @useinstead media.ContainerFormatType
     */
    enum AudioOutputFormat {
        /**
         * Default output format.
         *
         * This API is defined but not implemented yet.
         *
         * Note: It is supported since API version 6 and deprecated since API version 8. You are advised to select one from
         * [ContainerFormatType]{@link media.ContainerFormatType} as required.
         *
         * @syscap SystemCapability.Multimedia.Media.AudioRecorder
         * @since 6
         * @deprecated since 8
         */
        DEFAULT = 0,
        /**
         * MPEG-4.
         *
         * Note: It is supported since API version 6 and deprecated since API version 8. You are advised to use
         * **CFT_MPEG_4** in [ContainerFormatType]{@link media.ContainerFormatType} instead.
         *
         * @syscap SystemCapability.Multimedia.Media.AudioRecorder
         * @since 6
         * @deprecated since 8
         * @useinstead ohos.multimedia.media/media.ContainerFormatType#CFT_MPEG_4
         */
        MPEG_4 = 2,
        /**
         * AMR_NB.
         *
         * This API is defined but not implemented yet.
         *
         * Note: It is supported since API version 6 and deprecated since API version 8. You are advised to use **CFT_AMR**
         * in [ContainerFormatType]{@link media.ContainerFormatType} instead. For the encoding format, use **AUDIO_AMR_NB**
         * in [CodecMimeType]{@link media.CodecMimeType}.
         *
         * @syscap SystemCapability.Multimedia.Media.AudioRecorder
         * @since 6
         * @deprecated since 8
         * @useinstead ohos.multimedia.media/media.ContainerFormatType#CFT_AMR
         */
        AMR_NB = 3,
        /**
         * AMR_WB.
         *
         * This API is defined but not implemented yet.
         *
         * Note: It is supported since API version 6 and deprecated since API version 8. You are advised to use **CFT_AMR**
         * in [ContainerFormatType]{@link media.ContainerFormatType} instead. For the encoding format, use **AUDIO_AMR_WB**
         * in [CodecMimeType]{@link media.CodecMimeType}.
         *
         * @syscap SystemCapability.Multimedia.Media.AudioRecorder
         * @since 6
         * @deprecated since 8
         * @useinstead ohos.multimedia.media/media.ContainerFormatType#CFT_AMR
         */
        AMR_WB = 4,
        /**
         * Audio Data Transport Stream (ADTS), which is a transport stream format of AAC-based audio.
         *
         * Note: It is supported since API version 6 and deprecated since API version 8. You are advised to use **CFT_AAC**
         * in [ContainerFormatType]{@link media.ContainerFormatType} instead.
         *
         * @syscap SystemCapability.Multimedia.Media.AudioRecorder
         * @since 6
         * @deprecated since 8
         * @useinstead ohos.multimedia.media/media.ContainerFormatType#CFT_AAC
         */
        AAC_ADTS = 6
    }
    /**
     * Provides the geographical location definitions for media resources.
     *
     * @syscap SystemCapability.Multimedia.Media.Core
     * @crossplatform [since 12]
     * @since 6
     */
    interface Location {
        /**
         * Latitude.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform [since 12]
         * @since 6
         */
        latitude: number;
        /**
         * Longitude.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform [since 12]
         * @since 6
         */
        longitude: number;
    }
    /**
     * Provides the audio recorder configuration definitions.
     *
     * @syscap SystemCapability.Multimedia.Media.AudioRecorder
     * @since 6
     * @deprecated since 9
     * @useinstead ohos.multimedia.media/media.AVRecorderConfig
     */
    interface AudioRecorderConfig {
        /**
         * Audio encoding format. The default value is DEFAULT, it will be deprecated after API8.
         * use "audioEncoderMime" instead.
         *
         * @syscap SystemCapability.Multimedia.Media.AudioRecorder
         * @since 6
         * @deprecated since 8
         * @useinstead ohos.multimedia.media/media.AudioRecorderConfig.audioEncoderMime
         */
        audioEncoder?: AudioEncoder;
        /**
         * Audio encoding bit rate, in bit/s.
         *
         * @syscap SystemCapability.Multimedia.Media.AudioRecorder
         * @since 6
         * @deprecated since 9
         * @useinstead ohos.multimedia.media/media.AVRecorderProfile#audioBitrate
         */
        audioEncodeBitRate?: number;
        /**
         * Audio sampling rate, in Hz.
         *
         * @syscap SystemCapability.Multimedia.Media.AudioRecorder
         * @since 6
         * @deprecated since 9
         * @useinstead ohos.multimedia.media/media.AVRecorderProfile#audioSampleRate
         */
        audioSampleRate?: number;
        /**
         * Number of audio channels.
         *
         * @syscap SystemCapability.Multimedia.Media.AudioRecorder
         * @since 6
         * @deprecated since 9
         * @useinstead ohos.multimedia.media/media.AVRecorderProfile#audioChannels
         */
        numberOfChannels?: number;
        /**
         * Audio output format. The default value is DEFAULT, it will be deprecated after API8.
         * it will be replaced with "fileFormat".
         *
         * @syscap SystemCapability.Multimedia.Media.AudioRecorder
         * @since 6
         * @deprecated since 8
         * @useinstead ohos.multimedia.media/media.AudioRecorderConfig.fileFormat
         */
        format?: AudioOutputFormat;
        /**
         * Audio output uri.support two kind of uri now.
         * format like: scheme + "://" + "context".
         * file:  file://path
         * fd:    fd://fd
         *
         * @syscap SystemCapability.Multimedia.Media.AudioRecorder
         * @since 6
         * @deprecated since 9
         * @useinstead ohos.multimedia.media/media.AVRecorderConfig#url
         */
        uri: string;
        /**
         * Geographical location information.
         *
         * @syscap SystemCapability.Multimedia.Media.AudioRecorder
         * @since 6
         * @deprecated since 9
         * @useinstead ohos.multimedia.media/media.AVMetadata#location
         */
        location?: Location;
        /**
         * audio encoding format MIME. it used to replace audioEncoder.
         *
         * @syscap SystemCapability.Multimedia.Media.AudioRecorder
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.multimedia.media/media.AVRecorderProfile#audioCodec
         */
        audioEncoderMime?: CodecMimeType;
        /**
         * output file format. see @ContainerFormatType , it used to replace "format".
         *
         * @syscap SystemCapability.Multimedia.Media.AudioRecorder
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.multimedia.media/media.AVRecorderProfile#fileFormat
         */
        fileFormat?: ContainerFormatType;
    }
    /**
     * AudioRecorder is a class for audio recording management. It provides APIs to record audio. Before calling any API
     * in AudioRecorder, you must use [createAudioRecorder()]{@link @ohos.multimedia.media:media.createAudioRecorder} to
     * create an AudioRecorder instance.
     *
     * @syscap SystemCapability.Multimedia.Media.AudioRecorder
     * @since 6
     * @deprecated since 9
     * @useinstead @ohos.multimedia.media:media
     */
    interface AudioRecorder {
        /**
         * Prepares for recording.
         *
         * @permission ohos.permission.MICROPHONE
         * @param { AudioRecorderConfig } config - Audio recording parameters, including the audio output URI, encoding
         *     format, sample rate, audio channel count, and output format.
         * @throws { BusinessError } 201 - permission denied. [since 12]
         * @syscap SystemCapability.Multimedia.Media.AudioRecorder
         * @since 6
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVRecorder.prepare(config: AVRecorderConfig, callback: AsyncCallback<void>)
         */
        prepare(config: AudioRecorderConfig): void;
        /**
         * Starts audio recording. This API can be called only after the **'prepare'** event is triggered.
         *
         * @syscap SystemCapability.Multimedia.Media.AudioRecorder
         * @since 6
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVRecorder.start(callback: AsyncCallback<void>)
         */
        start(): void;
        /**
         * Pauses audio recording. This API can be called only after the **'start'** event is triggered.
         *
         * @syscap SystemCapability.Multimedia.Media.AudioRecorder
         * @since 6
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVRecorder.pause(callback: AsyncCallback<void>)
         */
        pause(): void;
        /**
         * Resumes audio recording. This API can be called only after the **'pause'** event is triggered.
         *
         * @syscap SystemCapability.Multimedia.Media.AudioRecorder
         * @since 6
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVRecorder.resume(callback: AsyncCallback<void>)
         */
        resume(): void;
        /**
         * Stops audio recording.
         *
         * @syscap SystemCapability.Multimedia.Media.AudioRecorder
         * @since 6
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVRecorder.stop(callback: AsyncCallback<void>)
         */
        stop(): void;
        /**
         * Releases the audio recording resources.
         *
         * @syscap SystemCapability.Multimedia.Media.AudioRecorder
         * @since 6
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVRecorder.release(callback: AsyncCallback<void>)
         */
        release(): void;
        /**
         * Resets audio recording.
         *
         * Before resetting audio recording, you must call **stop()** to stop recording. After audio recording is reset, you
         * must call **prepare()** to set the recording configurations for another recording.
         *
         * @syscap SystemCapability.Multimedia.Media.AudioRecorder
         * @since 6
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVRecorder.reset(callback: AsyncCallback<void>)
         */
        reset(): void;
        /**
         * Subscribes to the audio recording events.
         *
         * @param { 'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset' } type - Event type. The
         *     following events are supported: 'prepare'|'start'|  'pause' | 'resume' |'stop'|'release'|'reset'<br>- '
         *     prepare': triggered when the **prepare()** API is called and the audio recording parameters are set.<br>- '
         *     start': triggered when the **start()** API is called and audio recording starts.<br>- 'pause': triggered when
         *     the **pause()** API is called and audio recording is paused.<br>- 'resume': triggered when the **resume()**
         *     API is called and audio recording is resumed.<br>- 'stop': triggered when the **stop()** API is called and
         *     audio recording stops.<br>- 'release': triggered when the **release()** API is called and the recording
         *     resources are released.<br>- 'reset': triggered when the **reset()** API is called and audio recording is
         *     reset.
         * @param { function } callback - Callback invoked when the event is triggered.
         * @syscap SystemCapability.Multimedia.Media.AudioRecorder
         * @since 6
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVRecorder.on(type: 'stateChange', callback: OnAVRecorderStateChangeHandler)
         */
        on(type: 'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset', callback: () => void): void;
        /**
         * Subscribes to audio recording error events. After an error event is reported, you must handle the event and exit
         * the recording.
         *
         * @param { 'error' } type - Event type, which is **'error'** in this case.<br>This event is triggered when an error
         *     occurs during audio recording.
         * @param { ErrorCallback } callback - Callback invoked when the event is triggered.
         * @syscap SystemCapability.Multimedia.Media.AudioRecorder
         * @since 6
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVRecorder.on(type: 'error', callback: ErrorCallback)
         */
        on(type: 'error', callback: ErrorCallback): void;
    }
    /**
     * Describes the video playback state. You can obtain the state through the **state** property.
     *
     * @unionmember { 'idle' } The video player is idle.
     * @unionmember { 'prepared' } Video playback is being prepared.
     * @unionmember { 'playing' } Video playback is in progress.
     * @unionmember { 'paused' } Video playback is paused.
     * @unionmember { 'stopped' } Video playback is stopped.
     * @unionmember { 'error' } Video playback is in the error state.
     * @syscap SystemCapability.Multimedia.Media.VideoPlayer
     * @since 8
     * @deprecated since 9
     * @useinstead media.AVPlayerState
     */
    type VideoPlayState = 'idle' | 'prepared' | 'playing' | 'paused' | 'stopped' | 'error';
    /**
     * Enumerates the video playback speeds, which can be passed in the **setSpeed** API.
     *
     * @syscap SystemCapability.Multimedia.Media.VideoPlayer
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 8
     */
    enum PlaybackSpeed {
        /**
         * Plays the video at 0.75 times the normal speed.
         *
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 8
         */
        SPEED_FORWARD_0_75_X = 0,
        /**
         * Plays the video at the normal speed.
         *
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 8
         */
        SPEED_FORWARD_1_00_X = 1,
        /**
         * Plays the video at 1.25 times the normal speed.
         *
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 8
         */
        SPEED_FORWARD_1_25_X = 2,
        /**
         * Plays the video at 1.75 times the normal speed.
         *
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 8
         */
        SPEED_FORWARD_1_75_X = 3,
        /**
         * Plays the video at 2.00 times the normal speed.
         *
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 8
         */
        SPEED_FORWARD_2_00_X = 4,
        /**
         * Plays the video at 0.50 times the normal speed.
         *
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @atomicservice
         * @since 12
         */
        SPEED_FORWARD_0_50_X = 5,
        /**
         * Plays the video at 1.50 times the normal speed.
         *
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @atomicservice
         * @since 12
         */
        SPEED_FORWARD_1_50_X = 6,
        /**
         * Plays the video at 3.00 times the normal speed.
         *
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @atomicservice
         * @since 13
         */
        SPEED_FORWARD_3_00_X = 7,
        /**
         * Plays the video at 0.25 times the normal speed.
         *
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @atomicservice
         * @since 12
         */
        SPEED_FORWARD_0_25_X = 8,
        /**
         * Plays the video at 0.125 times the normal speed.
         *
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @atomicservice
         * @since 12
         */
        SPEED_FORWARD_0_125_X = 9
    }
    /**
     * VideoPlayer is a class for video playback management. It provides APIs to manage and play videos. Before calling
     * any API in VideoPlayer, you must use
     * [createVideoPlayer()]{@link @ohos.multimedia.media:media.createVideoPlayer(callback: AsyncCallback<VideoPlayer>)}
     * to create a VideoPlayer instance.
     *
     * @syscap SystemCapability.Multimedia.Media.VideoPlayer
     * @since 8
     * @deprecated since 9
     * @useinstead @ohos.multimedia.media:media
     */
    interface VideoPlayer {
        /**
         * Sets a surface ID. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > - **SetDisplaySurface** must be called between the URL setting and the calling of **prepare**. A surface must
         * > be set for video streams without audio. Otherwise, the calling of **prepare** fails.
         *
         * @param {string} surfaceId - Surface ID, which is obtained from the **XComponent**. For details about how to
         *     obtain it, see [XComponent]{@link ./@internal/component/ets/xcomponent}.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the setting is successful,
         *     **err** is **undefined**. Otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @since 8
         * @deprecated since 9
         * @useinstead null
         */
        setDisplaySurface(surfaceId: string, callback: AsyncCallback<void>): void;
        /**
         * Sets a surface ID. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > - **SetDisplaySurface** must be called between the URL setting and the calling of **prepare**. A surface must
         * > be set for video streams without audio. Otherwise, the calling of **prepare** fails.
         *
         * @param {string} surfaceId - Surface ID, which is obtained from the **XComponent**. For details about how to
         *     obtain it, see [XComponent]{@link ./@internal/component/ets/xcomponent}.
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @since 8
         * @deprecated since 9
         * @useinstead null
         */
        setDisplaySurface(surfaceId: string): Promise<void>;
        /**
         * Prepares for video playback. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVPlayer.prepare(callback: AsyncCallback<void>)
         */
        prepare(callback: AsyncCallback<void>): void;
        /**
         * Prepares for video playback. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVPlayer.prepare()
         */
        prepare(): Promise<void>;
        /**
         * Starts video playback. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVPlayer.play(callback: AsyncCallback<void>)
         */
        play(callback: AsyncCallback<void>): void;
        /**
         * Starts video playback. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVPlayer.play()
         */
        play(): Promise<void>;
        /**
         * Pauses video playback. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVPlayer.pause(callback: AsyncCallback<void>)
         */
        pause(callback: AsyncCallback<void>): void;
        /**
         * Pauses video playback. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVPlayer.pause()
         */
        pause(): Promise<void>;
        /**
         * Stops video playback. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVPlayer.stop(callback: AsyncCallback<void>)
         */
        stop(callback: AsyncCallback<void>): void;
        /**
         * Stops video playback. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVPlayer.stop()
         */
        stop(): Promise<void>;
        /**
         * Resets video playback. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVPlayer.reset(callback: AsyncCallback<void>)
         */
        reset(callback: AsyncCallback<void>): void;
        /**
         * Resets video playback. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVPlayer.reset()
         */
        reset(): Promise<void>;
        /**
         * Seeks to the specified playback position. The previous key frame at the specified position is played. This API
         * uses an asynchronous callback to return the result.
         *
         * @param { number } timeMs - Position to seek to, in ms. The value range is [0, duration].
         * @param { AsyncCallback<number> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **data** is the new playback position; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVPlayer.seek
         */
        seek(timeMs: number, callback: AsyncCallback<number>): void;
        /**
         * Seeks to the specified playback position. This API uses an asynchronous callback to return the result.
         *
         * @param { number } timeMs - Position to seek to, in ms. The value range is [0, duration].
         * @param { SeekMode } mode - Seek mode.
         * @param { AsyncCallback<number> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **data** is the new playback position; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVPlayer.seek
         */
        seek(timeMs: number, mode: SeekMode, callback: AsyncCallback<number>): void;
        /**
         * Seeks to the specified playback position. If **mode** is not specified, the previous key frame at the specified
         * position is played. This API uses a promise to return the result.
         *
         * @param { number } timeMs - Position to seek to, in ms. The value range is [0, duration].
         * @param { SeekMode } mode - Seek mode based on the video I frame. The default value is **SEEK_PREV_SYNC**.
         * @returns { Promise<number> } Promise used to return the playback position, in ms.
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVPlayer.seek
         */
        seek(timeMs: number, mode?: SeekMode): Promise<number>;
        /**
         * Sets the volume. This API uses an asynchronous callback to return the result.
         *
         * @param { number } vol - Relative volume. The value ranges from 0.00 to 1.00. The value **1.00** indicates the
         *     maximum volume (100%).
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the setting is successful,
         *     **err** is **undefined**. Otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVPlayer.setVolume
         */
        setVolume(vol: number, callback: AsyncCallback<void>): void;
        /**
         * Sets the volume. This API uses a promise to return the result.
         *
         * @param { number } vol - Relative volume. The value ranges from 0.00 to 1.00. The value **1.00** indicates the
         *     maximum volume (100%).
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVPlayer.setVolume
         */
        setVolume(vol: number): Promise<void>;
        /**
         * Releases the video playback resources. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVPlayer.release(callback: AsyncCallback<void>)
         */
        release(callback: AsyncCallback<void>): void;
        /**
         * Releases the video playback resources. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVPlayer.release()
         */
        release(): Promise<void>;
        /**
         * Obtains the video track information. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<Array<MediaDescription>> } callback - Callback used to return the result. If the operation
         *     is successful, **err** is **undefined** and **data** is the MediaDescription array obtained; otherwise,
         *     **err** is an error object.
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVPlayer.getTrackDescription(callback: AsyncCallback<Array<MediaDescription>>)
         */
        getTrackDescription(callback: AsyncCallback<Array<MediaDescription>>): void;
        /**
         * Obtains the video track information. This API uses a promise to return the result.
         *
         * @returns { Promise<Array<MediaDescription>> } Promise used to return the MediaDescription array that holds the
         *     video track information.
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVPlayer.getTrackDescription()
         */
        getTrackDescription(): Promise<Array<MediaDescription>>;
        /**
         * Video URL. The video formats MP4, MPEG-TS, and MKV are supported.
         *
         * **Example of supported URLs**:
         *
         * 1. FD: fd://xx
         *
         * ![](docroot://reference/apis-media-kit/figures/en-us_image_url.png)
         *
         * 2. HTTP: http://xx
         * 3. HTTPS: https://xx
         * 4. HLS: http://xx or https://xx
         * 5. File type: file://xx
         *
         * **NOTE**
         *
         * WebM is no longer supported since API version 11.
         *
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.multimedia.media/media.AVPlayer#url
         */
        url: string;
        /**
         * Description of a video file. This property is required when video assets of an application are continuously
         * stored in a file.
         *
         * Assume that a music file that stores continuous music assets consists of the following:
         *
         * Video 1 (address offset: 0, byte length: 100)
         *
         * Video 2 (address offset: 101; byte length: 50)
         *
         * Video 3 (address offset: 151, byte length: 150)
         *
         * 1. To play video 1: AVFileDescriptor { fd = resource handle; offset = 0; length = 100; }
         * 2. To play video 2: AVFileDescriptor { fd = resource handle; offset = 101; length = 50; }
         * 3. To play video 3: AVFileDescriptor { fd = resource handle; offset = 151; length = 150; }
         *
         * To play an independent video file, use **src=fd://xx**.
         *
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @since 9
         * @deprecated since 9
         * @useinstead ohos.multimedia.media/media.AVPlayer#fdSrc
         */
        fdSrc: AVFileDescriptor;
        /**
         * Whether to loop video playback. **true** to loop, **false** otherwise.
         *
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.multimedia.media/media.AVPlayer#loop
         */
        loop: boolean;
        /**
         * Current video playback position, in ms.
         *
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.multimedia.media/media.AVPlayer#currentTime
         */
        readonly currentTime: number;
        /**
         * Video duration, in ms. The value **-1** indicates the live mode.
         *
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.multimedia.media/media.AVPlayer#duration
         */
        readonly duration: number;
        /**
         * Video playback state.
         *
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.multimedia.media/media.AVPlayer#state
         */
        readonly state: VideoPlayState;
        /**
         * Video width, in px.
         *
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.multimedia.media/media.AVPlayer#width
         */
        readonly width: number;
        /**
         * Video height, in px.
         *
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @since 8
         * @deprecated since 9
         * @useinstead ohos.multimedia.media/media.AVPlayer#height
         */
        readonly height: number;
        /**
         * Audio interruption mode.
         *
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @since 9
         * @deprecated since 9
         * @useinstead ohos.multimedia.media/media.AVPlayer#audioInterruptMode
         */
        audioInterruptMode?: audio.InterruptMode;
        /**
         * Video scale type. The default value is **VIDEO_SCALE_TYPE_FIT**.
         *
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @since 9
         * @deprecated since 9
         * @useinstead ohos.multimedia.media/media.AVPlayer#videoScaleType
         */
        videoScaleType?: VideoScaleType;
        /**
         * Sets the playback speed. This API uses an asynchronous callback to return the result.
         *
         * @param { number } speed - Video playback speed. For details, see
         *     [PlaybackSpeed]{@link @ohos.multimedia.media:media.PlaybackSpeed}.
         * @param { AsyncCallback<number> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **data** is the playback speed; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVPlayer.setSpeed
         */
        setSpeed(speed: number, callback: AsyncCallback<number>): void;
        /**
         * Sets the playback speed. This API uses a promise to return the result.
         *
         * @param { number } speed - Video playback speed. For details, see
         *     [PlaybackSpeed]{@link @ohos.multimedia.media:media.PlaybackSpeed}.
         * @returns { Promise<number> } Promise used to return the playback speed. For details, see
         *     [PlaybackSpeed]{@link @ohos.multimedia.media:media.PlaybackSpeed}.
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVPlayer.setSpeed
         */
        setSpeed(speed: number): Promise<number>;
        /**
         * Subscribes to the video playback completion event.
         *
         * @param { 'playbackCompleted' } type - Event type, which is **'playbackCompleted'** in this case.
         * @param { Callback<void> } callback - Callback invoked when the event is triggered.
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVPlayer.on(type: 'stateChange', callback: OnAVPlayerStateChangeHandle)
         */
        on(type: 'playbackCompleted', callback: Callback<void>): void;
        /**
         * Subscribes to the video buffering update event. This API works only under online playback.
         *
         * @param { 'bufferingUpdate' } type - Event type, which is **'bufferingUpdate'** in this case.
         * @param { function } callback - Callback invoked when the event is triggered.<br>The value of
         *     [BufferingInfoType]{@link @ohos.multimedia.media:media.BufferingInfoType} is fixed at **0**.
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVPlayer.on(type: 'bufferingUpdate', callback: OnBufferingUpdateHandler)
         */
        on(type: 'bufferingUpdate', callback: (infoType: BufferingInfoType, value: number) => void): void;
        /**
         * Subscribes to the frame rendering start event.
         *
         * @param { 'startRenderFrame' } type - Event type, which is **'startRenderFrame'** in this case.
         * @param { Callback<void> } callback - Callback invoked when the event is triggered.
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVPlayer.on(type: 'startRenderFrame', callback: Callback<void>)
         */
        on(type: 'startRenderFrame', callback: Callback<void>): void;
        /**
         * Subscribes to the video width and height change event.
         *
         * @param { 'videoSizeChanged' } type - Event type, which is **'videoSizeChanged'** in this case.
         * @param { function } callback - Callback invoked when the event is triggered. **width** indicates the video width,
         *     and **height** indicates the video height.
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVPlayer.on(type: 'videoSizeChange', callback: OnVideoSizeChangeHandler)
         */
        on(type: 'videoSizeChanged', callback: (width: number, height: number) => void): void;
        /**
         * Subscribes to the audio interruption event. For details, see
         * [audio.InterruptEvent]{@link @ohos.multimedia.audio:audio.InterruptEvent}.
         *
         * @param { 'audioInterrupt' } type - Event type, which is **'audioInterrupt'** in this case.
         * @param { function } callback - Callback invoked when the event is triggered.
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @since 9
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVPlayer.on(type: 'audioInterrupt', callback: Callback<audio.InterruptEvent>)
         */
        on(type: 'audioInterrupt', callback: (info: audio.InterruptEvent) => void): void;
        /**
         * Subscribes to video playback error events. After an error event is reported, you must handle the event and exit
         * the playback.
         *
         * @param { 'error' } type - Event type, which is **'error'** in this case.<br>This event is triggered when an error
         *     occurs during video playback.
         * @param { ErrorCallback } callback - Callback invoked when the event is triggered.
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @since 8
         * @deprecated since 9
         * @useinstead @ohos.multimedia.media:media.AVPlayer.on(type: 'error', callback: ErrorCallback)
         */
        on(type: 'error', callback: ErrorCallback): void;
    }
    /**
     * Enumerates the video scale modes.
     *
     * @syscap SystemCapability.Multimedia.Media.VideoPlayer
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 9
     */
    enum VideoScaleType {
        /**
         * Default mode. The video will be stretched to fit the window.
         *
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        VIDEO_SCALE_TYPE_FIT = 0,
        /**
         * Maintains the video's aspect ratio, and scales to fill the shortest side of the window, with the longer side
         * cropped.
         *
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        VIDEO_SCALE_TYPE_FIT_CROP = 1,
        /**
         * Maintains the video's aspect ratio, and scales to fill the longer side of the window, with the shorter side
         * centered and unfilled parts left black.
         *
         * @syscap SystemCapability.Multimedia.Media.VideoPlayer
         * @crossplatform
         * @atomicservice
         * @since 20
         */
        VIDEO_SCALE_TYPE_SCALED_ASPECT = 2
    }
    /**
     * Enumerates the container format types (CFTs).
     *
     * @syscap SystemCapability.Multimedia.Media.Core
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 8
     */
    enum ContainerFormatType {
        /**
         * Video container format MP4.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform [since 12]
         * @atomicservice [since 22]
         * @since 8
         */
        CFT_MPEG_4 = 'mp4',
        /**
         * Audio container format M4A.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 8
         */
        CFT_MPEG_4A = 'm4a',
        /**
         * Audio container format MP3.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @since 12
         */
        CFT_MP3 = 'mp3',
        /**
         * Audio container format WAV.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @since 12
         */
        CFT_WAV = 'wav',
        /**
         * Audio container format AMR.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @since 18
         */
        CFT_AMR = 'amr',
        /**
         * Audio container format AAC. The default format is ADTS frame header.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @since 20
         */
        CFT_AAC = 'aac'
    }
    /**
     * Enumerates the media types.
     *
     * @syscap SystemCapability.Multimedia.Media.Core
     * @crossplatform [since 12]
     * @atomicservice [since 11]
     * @since 8
     */
    enum MediaType {
        /**
         * The media type is not supported.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 20
         */
        MEDIA_TYPE_UNSUPPORTED = -1,
        /**
         * Media.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 8
         */
        MEDIA_TYPE_AUD = 0,
        /**
         * Video.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 8
         */
        MEDIA_TYPE_VID = 1,
        /**
         * Subtitle.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 12
         */
        MEDIA_TYPE_SUBTITLE = 2,
        /**
         * Attachment information (for example, an embedded external file).
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 20
         */
        MEDIA_TYPE_ATTACHMENT = 3,
        /**
         * Data.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 20
         */
        MEDIA_TYPE_DATA = 4,
        /**
         * Metadata with a timestamp.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 20
         */
        MEDIA_TYPE_TIMED_METADATA = 5,
        /**
         * Auxiliary (track) information.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 20
         */
        MEDIA_TYPE_AUXILIARY = 6
    }
    /**
     * Enumerates the media description keys.
     *
     * @syscap SystemCapability.Multimedia.Media.Core
     * @crossplatform [since 12]
     * @atomicservice [since 11]
     * @since 8
     */
    enum MediaDescriptionKey {
        /**
         * Track index. The corresponding key value type is number.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 8
         */
        MD_KEY_TRACK_INDEX = 'track_index',
        /**
         * Track type. The corresponding key value type is number. For details, see [MediaType]{@link media.MediaType}.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 8
         */
        MD_KEY_TRACK_TYPE = 'track_type',
        /**
         * Codec MIME type. The corresponding key value type is string.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 8
         */
        MD_KEY_CODEC_MIME = 'codec_mime',
        /**
         * Media duration. The corresponding key value type is number, measured in ms.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 8
         */
        MD_KEY_DURATION = 'duration',
        /**
         * Bit rate. The corresponding key value type is number, measured in bit/s. If the value is **undefined** or **0**,
         * the bit rate is abnormal.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 8
         */
        MD_KEY_BITRATE = 'bitrate',
        /**
         * Video width. The corresponding key value type is number, measured in px.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 8
         */
        MD_KEY_WIDTH = 'width',
        /**
         * Video height. The corresponding key value type is number, measured in px.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 8
         */
        MD_KEY_HEIGHT = 'height',
        /**
         * Video frame rate. The corresponding key value type is number, measured in frames per 100 seconds.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 8
         */
        MD_KEY_FRAME_RATE = 'frame_rate',
        /**
         * Audio channel count. The corresponding key value type is number.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 8
         */
        MD_KEY_AUD_CHANNEL_COUNT = 'channel_count',
        /**
         * Sample rate. The corresponding key value type is number, measured in Hz.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 8
         */
        MD_KEY_AUD_SAMPLE_RATE = 'sample_rate',
        /**
         * Bit depth. The corresponding key value type is number, measured in bits.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 12
         */
        MD_KEY_AUD_SAMPLE_DEPTH = 'sample_depth',
        /**
         * Subtitle language. The corresponding key value type is string.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 12
         */
        MD_KEY_LANGUAGE = 'language',
        /**
         * Track name. The corresponding key value type is string.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 12
         */
        MD_KEY_TRACK_NAME = 'track_name',
        /**
         * Codec track type. The corresponding key value type is string.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 12
         */
        MD_KEY_HDR_TYPE = 'hdr_type',
        /**
         * Original video width. The corresponding key value type is number, measured in px.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 21
         */
        MD_KEY_ORIGINAL_WIDTH = 'original_width',
        /**
         * Original video height. The corresponding key value type is number, measured in px.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 21
         */
        MD_KEY_ORIGINAL_HEIGHT = 'original_height',
        /**
         * MIME type of the track. The corresponding key value type is string. For audio and video tracks, the value is the
         * same as that of **MD_KEY_CODEC_MIME**.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 23
         */
        MD_KEY_MIME_TYPE = 'mime_type',
        /**
         * Reference relationships between this track and other tracks. The corresponding key value type is string, with
         * values separated by commas (,).
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 23
         */
        MD_KEY_REFERENCE_TRACK_IDS = 'ref_track_ids',
        /**
         * Auxiliary type of this track when it acts as a reference track. The corresponding key value type is string.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 23
         */
        MD_KEY_TRACK_REFERENCE_TYPE = 'track_ref_type'
    }
    /**
     * Enumerates the audio source types for video recording.
     *
     * @syscap SystemCapability.Multimedia.Media.AVRecorder
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 9
     */
    enum AudioSourceType {
        /**
         * Default audio input source.
         *
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @crossplatform [since 12]
         * @since 9
         */
        AUDIO_SOURCE_TYPE_DEFAULT = 0,
        /**
         * Microphone audio input source.
         *
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        AUDIO_SOURCE_TYPE_MIC = 1,
        /**
         * Audio source in speech recognition scenarios.
         *
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @since 12
         */
        AUDIO_SOURCE_TYPE_VOICE_RECOGNITION = 2,
        /**
         * Voice communication source.
         *
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @since 12
         */
        AUDIO_SOURCE_TYPE_VOICE_COMMUNICATION = 7,
        /**
         * Voice message source.
         *
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @since 12
         */
        AUDIO_SOURCE_TYPE_VOICE_MESSAGE = 10,
        /**
         * Audio source in camera recording scenarios.
         *
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @since 12
         */
        AUDIO_SOURCE_TYPE_CAMCORDER = 13
    }
    /**
     * Enumerates the video source types for video recording.
     *
     * @syscap SystemCapability.Multimedia.Media.AVRecorder
     * @crossplatform [since 12]
     * @since 9
     */
    enum VideoSourceType {
        /**
         * The input surface carries raw data.
         *
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @crossplatform [since 12]
         * @since 9
         */
        VIDEO_SOURCE_TYPE_SURFACE_YUV = 0,
        /**
         * The input surface carries ES data.
         *
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @crossplatform [since 12]
         * @since 9
         */
        VIDEO_SOURCE_TYPE_SURFACE_ES = 1
    }
    /**
     * Enumerates the modes for creating media files.
     *
     * @syscap SystemCapability.Multimedia.Media.AVRecorder
     * @since 12
     */
    enum FileGenerationMode {
        /**
         * The application creates a media file in the sandbox.
         *
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @since 12
         */
        APP_CREATE = 0,
        /**
         * The system creates a media file. Currently, this mode takes effect only in camera recording scenarios. The URL
         * set by the application is ignored.
         *
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @since 12
         */
        AUTO_CREATE_CAMERA_SCENE = 1
    }
    /**
     * Describes the information about an encoder.
     *
     * @syscap SystemCapability.Multimedia.Media.AVRecorder
     * @since 11
     */
    interface EncoderInfo {
        /**
         * MIME type of the encoder.
         *
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @since 11
         */
        mimeType: CodecMimeType;
        /**
         * Encoder type. The value **audio** means an audio encoder, and **video** means a video encoder.
         *
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @since 11
         */
        type: string;
        /**
         * Bit rate range of the encoder, with the minimum and maximum bit rates specified, in bit/s.
         *
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @since 11
         */
        bitRate?: Range;
        /**
         * Video frame rate range, with the minimum and maximum frame rates specified, in fps.
         * This parameter is available only for video encoders.
         *
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @since 11
         */
        frameRate?: Range;
        /**
         * Video frame width range, with the minimum and maximum widths specified, in px.
         * This parameter is available only for video encoders.
         *
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @since 11
         */
        width?: Range;
        /**
         * Video frame height range, with the minimum and maximum heights specified, in px.
         * This parameter is available only for video encoders.
         *
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @since 11
         */
        height?: Range;
        /**
         * Number of audio channels for the audio capturer, with the minimum and maximum numbers of audio channels
         * specified.
         * This parameter is available only for audio encoders.
         *
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @since 11
         */
        channels?: Range;
        /**
         * Audio sampling rate, including all available audio sampling rates, in Hz. The value depends on the encoder type,
         * and this parameter is available only for audio encoders.
         *
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @since 11
         */
        sampleRate?: Array<number>;
    }
    /**
     * Provides Range with lower and upper limit.
     *
     * @syscap SystemCapability.Multimedia.Media.AVRecorder
     * @since 11
     */
    interface Range {
        /**
         * Minimum value.
         *
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @since 11
         */
        min: number;
        /**
         * Maximum value.
         *
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @since 11
         */
        max: number;
    }
    /**
     * Enumerates the supported Advanced Audio Coding (AAC) formats.
     *
     * @syscap SystemCapability.Multimedia.Media.AVRecorder
     * @atomicservice
     * @since 22
     */
    enum AacProfile {
        /**
         * Standard AAC Low Complexity profile.
         *
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @atomicservice
         * @since 22
         */
        AAC_LC = 0,
        /**
         * Standard AAC High Efficiency profile.
         *
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @atomicservice
         * @since 22
         */
        AAC_HE = 1,
        /**
         * AAC High Efficiency Version 2 profile (also known as HE-AAC v2).
         *
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @atomicservice
         * @since 22
         */
        AAC_HE_V2 = 2
    }
    /**
     * Describes the audio and video recording profile.
     *
     * @syscap SystemCapability.Multimedia.Media.AVRecorder
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 9
     */
    interface AVRecorderProfile {
        /**
         * Audio encoding bit rate, in bit/s. This parameter is mandatory for audio recording.<br>Supported bit rate ranges:
         * <br>- Range [32000 - 500000] for the AAC encoding format.<br>- Range [64000] for the G.711 μ-law encoding format.
         * <br>- Range [8000, 16000, 32000, 40000, 48000, 56000, 64000, 80000, 96000, 112000, 128000, 160000, 192000,
         * 224000, 256000, 320000] for the MP3 encoding format.<br>When the MP3 encoding format is used,
         * the mapping between the sampling rate and bit rate is as follows:<br>- When the sampling rate is lower than
         * 16 kHZ, the bit rate range is [8000 - 64000].<br>- When the sampling rate ranges from 16 kHz to 32 kHz,
         * the bit rate range is [8000 - 160000].<br>- When the sampling rate is greater than 32 kHz, the bit rate range
         * is [32000 - 320000].<br>- Range [4750, 5150, 5900, 6700, 7400, 7950, 10200, 12200] for
         * the AMR-NB encoding format.<br>- Range [6600, 8850, 12650, 14250, 15850, 18250, 19850, 23050, 23850] for the
         * AMR-WB encoding format.<br>**Atomic service API**: This API can be used in atomic services since API version 12.
         *
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        audioBitrate?: number;
        /**
         * Number of audio channels. This parameter is mandatory for audio recording.<br>- Range [1 - 2] for the
         * AAC encoding format.<br>- Range [1] for the G.711 μ-law encoding format.<br>- Range [1 - 2] for the MP3 encoding
         * format.<br>- Range [1] for the AMR-NB and AMR-WB encoding formats.<br>**Atomic service API**: This API can be
         * used in atomic services since API version 12.
         *
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        audioChannels?: number;
        /**
         * Audio encoding format. This parameter is mandatory for audio recording. Currently, AUDIO_AAC, AUDIO_MP3,
         * AUDIO_G711MU, AUDIO_AMR_NB, and AUDIO_AMR_WB are supported.<br>**Atomic service API**: This API can be used in
         * atomic services since API version 12.
         *
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        audioCodec?: CodecMimeType;
        /**
         * AAC profile for AAC audio encoder. If not set, use AAC_LC profile as default.
         *
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @atomicservice
         * @since 22
         */
        aacProfile?: AacProfile;
        /**
         * Audio sampling rate, in Hz. This parameter is mandatory for audio recording.<br>Supported sampling rate ranges:
         * <br>- Range [8000, 11025, 12000, 16000, 22050, 24000, 32000, 44100, 48000, 64000, 88200, 96000] for the AAC
         * encoding format.<br>- Range [8000] for the G.711 μ-law encoding format.<br>- Range [8000, 11025, 12000, 16000,
         * 22050, 24000, 32000, 44100, 48000] for the MP3 encoding format.<br>- Range [8000] for the AMR-NB encoding format.
         * <br>- Range [16000] for the AMR-WB encoding format.<br>Variable bit rate. The bit rate is for reference only.
         * <br>**Atomic service API**: This API can be used in atomic services since API version 12.
         *
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        audioSampleRate?: number;
        /**
         * Container format of a file. This parameter is mandatory. Currently, the MP4, M4A, MP3, WAV, AMR, and AAC
         * container formats are supported. The AUDIO_MP3 encoding format cannot be used in the MP4 container format.
         * <br>**Atomic service API**: This API can be used in atomic services since API version 12.
         *
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        fileFormat: ContainerFormatType;
        /**
         * Video encoding bit rate, in bit/s. This parameter is mandatory for video recording. The value range is
         * [10000 - 100000000], in bit/s.
         *
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @crossplatform [since 12]
         * @since 9
         */
        videoBitrate?: number;
        /**
         * Video encoding format. This parameter is mandatory for video recording.
         * Currently, VIDEO_AVC and VIDEO_HEVC is supported.
         *
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @crossplatform [since 12]
         * @since 9
         */
        videoCodec?: CodecMimeType;
        /**
         * Width of a video frame, in px. This parameter is mandatory for video recording. The value range is [176 - 4096].
         *
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @crossplatform [since 12]
         * @since 9
         */
        videoFrameWidth?: number;
        /**
         * Height of a video frame, in px. This parameter is mandatory for video recording. The value range is [144 - 4096].
         *
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @crossplatform [since 12]
         * @since 9
         */
        videoFrameHeight?: number;
        /**
         * Video frame rate, in fps. This parameter is mandatory for video recording. The value range is [1 - 60].
         *
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @crossplatform [since 12]
         * @since 9
         */
        videoFrameRate?: number;
        /**
         * HDR encoding. This parameter is optional for video recording. The default value is **false**, and there is no
         * requirement on the encoding format. When **isHdr** is set to **true**, the encoding format must be **video/hevc**.
         *
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @crossplatform [since 12]
         * @since 11
         */
        isHdr?: boolean;
        /**
         * Whether temporal layered encoding is supported. This parameter is optional for video recording. The default value
         * is **false**. If this parameter is set to **true**, some frames in the video output streams can be skipped
         * without being encoded.
         *
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @crossplatform
         * @since 12
         */
        enableTemporalScale?: boolean;
        /**
         * Indicates whether enable B Frame. Default is disabled.
         *
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @since 20
         */
        enableBFrame?: boolean;
    }
    /**
     * Describes the audio and video recording parameters.
     *
     * The **audioSourceType** and **videoSourceType** parameters are used to distinguish audio-only recording,
     * video-only recording, and audio and video recording. For audio-only recording, set only **audioSourceType**.
     * For video-only recording, set only **videoSourceType**. For audio and video recording, set both **audioSourceType**
     * and **videoSourceType**.
     *
     * @syscap SystemCapability.Multimedia.Media.AVRecorder
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 9
     */
    interface AVRecorderConfig {
        /**
         * Type of the audio source to record. This parameter is mandatory for audio recording.<br>**Atomic service API**:
         * This API can be used in atomic services since API version 12.
         *
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        audioSourceType?: AudioSourceType;
        /**
         * Type of the video source to record. This parameter is mandatory for video recording.
         *
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @crossplatform [since 12]
         * @since 9
         */
        videoSourceType?: VideoSourceType;
        /**
         * Recording profile. This parameter is mandatory.<br>**Atomic service API**: This API can be used in atomic
         * services since API version 12.
         *
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        profile: AVRecorderProfile;
        /**
         * Recording output URL: fd://xx (fd number).<br>This parameter is mandatory.<br>**Atomic service API**:
         * This API can be used in atomic services since API version 12.
         *
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        url: string;
        /**
         * Mode for creating the file, which is used together with on('photoAssetAvailable').
         *
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @since 12
         */
        fileGenerationMode?: FileGenerationMode;
        /**
         * Rotation angle of the recorded video, in degrees. The value can be 0 (default), 90, 180, or 270 for MP4 videos.
         * <br>This API is supported since API version 6 and deprecated since API version 12. You are advised to use.
         * **AVMetadata.videoOrientation** instead. If both parameters are set, **AVMetadata.videoOrientation** is used.
         *
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @since 9
         * @deprecated since 12
         * @useinstead ohos.multimedia.media/media.AVMetadata#videoOrientation
         */
        rotation?: number;
        /**
         * Geographical location of the recorded video. By default, the geographical location information is not recorded.
         * <br>This API is supported since API version 6 and deprecated since API version 12. You are advised to use
         * **AVMetadata.location** instead. If both parameters are set, **AVMetadata.location** is used.
         *
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @since 9
         * @deprecated since 12
         * @useinstead ohos.multimedia.media/media.AVMetadata#location
         */
        location?: Location;
        /**
         * Metadata. For details, see @AVMetadata.
         *
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @since 12
         */
        metadata?: AVMetadata;
        /**
         * Maximum recording duration, in seconds. The value range is [1, 2^31-1]. If an invalid value is provided,
         * it is reset to the maximum allowed duration. Once the recording reaches the specified duration,
         * it stops automatically and notifies via the **stateChange** callback that the recording has stopped:
         * AVRecorderState = 'stopped', StateChangeReason = BACKGROUND.
         *
         * @syscap SystemCapability.Multimedia.Media.AVRecorder
         * @since 18
         */
        maxDuration?: number;
    }
    /**
     * Provides the container definition for media description key-value pairs.
     *
     * @syscap SystemCapability.Multimedia.Media.Core
     * @crossplatform [since 12]
     * @atomicservice [since 11]
     * @since 8
     */
    interface MediaDescription {
        /**
         * key:value pair, key see @MediaDescriptionKey .
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 8
         */
        [key: string]: Object;
    }
    /**
     * Enumerates the video playback seek modes, which can be passed in the **seek** API.
     *
     * @syscap SystemCapability.Multimedia.Media.Core
     * @crossplatform [since 12]
     * @atomicservice [since 11]
     * @since 8
     */
    enum SeekMode {
        /**
         * Seeks to the next key frame at the specified position. You are advised to use this value for the rewind
         * operation.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 8
         */
        SEEK_NEXT_SYNC = 0,
        /**
         * Seeks to the previous key frame at the specified position. You are advised to use this value for the fast-forward
         * operation.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform [since 12]
         * @atomicservice [since 11]
         * @since 8
         */
        SEEK_PREV_SYNC = 1,
        /**
         * Seeks to the frame closest to the specified position. You are advised to use this value for accurate seek.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 12
         */
        SEEK_CLOSEST = 2,
        /**
         * Offers a smooth and fluid visual experience for seeking. Applications can use a progress bar component to
         * continuously invoke the **seek** method, and the AVPlayer will update the video frames smoothly in response to
         * these calls.
         *
         * Applications can call
         * [isSeekContinuousSupported]{@link @ohos.multimedia.media:media.AVPlayer.isSeekContinuousSupported} to check
         * whether the video source supports this seeking mode.
         *
         * If the video source does not support this mode, calling **seek** will result in an
         * **AVERR_SEEK_CONTINUOUS_UNSUPPORTED** error (see [AVErrorCode]{@link media.AVErrorCode}), and the smoothness of
         * frame updates will be compromised.
         *
         * This seek mode does not trigger the
         * [on('seekDone')]{@link @ohos.multimedia.media:media.AVPlayer.on(type: 'seekDone', callback: Callback<number>)}
         * event.
         *
         * To exit this seeking mode, applications must call **seek(-1, SeekMode.SEEK_CONTINUOUS)** to end the seeking
         * process.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 18
         */
        SEEK_CONTINUOUS = 3
    }
    /**
     * Enumerates the **selectTrack** modes for video playback.
     *
     * SwitchMode can be passed as a parameter through the **selectTrack** method. Currently, both DASH and HLS video
     * tracks support this extended parameter. (HLS video tracks support this extended parameter since API version 24.)
     *
     * @syscap SystemCapability.Multimedia.Media.Core
     * @crossplatform
     * @atomicservice
     * @since 12
     */
    enum SwitchMode {
        /**
         * Smooth playback is ensured after the switching. This mode has a delay, that is, the switching does not take
         * effect immediately.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        SMOOTH = 0,
        /**
         * The playback starts from the start position of the current segment after the switching. In this mode, the
         * switching takes effect immediately and repeated playback may occur.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform
         * @atomicservice
         * @since 12
         */
        SEGMENT = 1,
        /**
         * The playback starts from the frame closest to the current playback time. In this mode, the switching takes effect
         * immediately, and the playback is suspended for 3s to 5s and then resumed.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @atomicservice
         * @since 12
         */
        CLOSEST = 2
    }
    /**
     * Enumerates the codec MIME types.
     *
     * @syscap SystemCapability.Multimedia.Media.Core
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 8
     */
    enum CodecMimeType {
        /**
         * Video in H.263 format.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform [since 12]
         * @since 8
         */
        VIDEO_H263 = 'video/h263',
        /**
         * Video in AVC format.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform [since 12]
         * @atomicservice [since 22]
         * @since 8
         */
        VIDEO_AVC = 'video/avc',
        /**
         * Video in MPEG-2 format.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform [since 12]
         * @since 8
         */
        VIDEO_MPEG2 = 'video/mpeg2',
        /**
         * Video in MPEG-4 format.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform [since 12]
         * @since 8
         */
        VIDEO_MPEG4 = 'video/mp4v-es',
        /**
         * Video in VP8 format.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform [since 12]
         * @since 8
         */
        VIDEO_VP8 = 'video/x-vnd.on2.vp8',
        /**
         * Audio in MP4A-LATM format.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 8
         */
        AUDIO_AAC = 'audio/mp4a-latm',
        /**
         * Audio in Vorbis format.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform [since 12]
         * @since 8
         */
        AUDIO_VORBIS = 'audio/vorbis',
        /**
         * Audio in FLAC format.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform [since 12]
         * @since 8
         */
        AUDIO_FLAC = 'audio/flac',
        /**
         * Video in H.265 format.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @crossplatform [since 12]
         * @atomicservice [since 22]
         * @since 11
         */
        VIDEO_HEVC = 'video/hevc',
        /**
         * Audio in MPEG format.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @since 12
         */
        AUDIO_MP3 = 'audio/mpeg',
        /**
         * Audio in G.711 μ-law format.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @since 12
         */
        AUDIO_G711MU = 'audio/g711mu',
        /**
         * Audio in AMR-NB format.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @since 18
         */
        AUDIO_AMR_NB = 'audio/3gpp',
        /**
         * Audio in AMR-WB format.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @since 18
         */
        AUDIO_AMR_WB = 'audio/amr-wb',
        /**
         * Audio in raw streams format.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        AUDIO_RAW = 'audio/raw'
    }
    /**
     * Enumerates the encoding and container formats used during screen capture.
     *
     * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
     * @since 12
     */
    enum AVScreenCaptureRecordPreset {
        /**
         * The H.264 video encoding format, AAC audio encoding format, and MP4 container format are used.
         *
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @since 12
         */
        SCREEN_RECORD_PRESET_H264_AAC_MP4 = 0,
        /**
         * The H.265 video encoding format, AAC audio encoding format, and MP4 container format are used.
         *
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @since 12
         */
        SCREEN_RECORD_PRESET_H265_AAC_MP4 = 1
    }
    /**
     * Enumerates the video fill modes during screen capture.
     *
     * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
     * @since 18
     */
    enum AVScreenCaptureFillMode {
        /**
         * Keeps the original aspect ratio, matching the aspect ratio of the physical screen.
         *
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @since 18
         */
        PRESERVE_ASPECT_RATIO = 0,
        /**
         * Stretches the image to fit the specified dimensions.
         *
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @since 18
         */
        SCALE_TO_FILL = 1
    }
    /**
     * Enumerates the screen capture states used in callbacks.
     *
     * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
     * @since 12
     */
    enum AVScreenCaptureStateCode {
        /**
         * Screen capture is started.
         *
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @since 12
         */
        SCREENCAPTURE_STATE_STARTED = 0,
        /**
         * Screen capture is canceled.
         *
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @since 12
         */
        SCREENCAPTURE_STATE_CANCELED = 1,
        /**
         * Screen capture is manually stopped by the user.
         *
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @since 12
         */
        SCREENCAPTURE_STATE_STOPPED_BY_USER = 2,
        /**
         * Screen capture is interrupted by another screen capture.
         *
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @since 12
         */
        SCREENCAPTURE_STATE_INTERRUPTED_BY_OTHER = 3,
        /**
         * Screen capture is interrupted by an incoming call.
         *
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @since 12
         */
        SCREENCAPTURE_STATE_STOPPED_BY_CALL = 4,
        /**
         * The microphone is unavailable during screen capture.
         *
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @since 12
         */
        SCREENCAPTURE_STATE_MIC_UNAVAILABLE = 5,
        /**
         * The microphone is muted by the user.
         *
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @since 12
         */
        SCREENCAPTURE_STATE_MIC_MUTED_BY_USER = 6,
        /**
         * The microphone is unmuted by the user.
         *
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @since 12
         */
        SCREENCAPTURE_STATE_MIC_UNMUTED_BY_USER = 7,
        /**
         * The system enters a privacy page during screen capture.
         *
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @since 12
         */
        SCREENCAPTURE_STATE_ENTER_PRIVATE_SCENE = 8,
        /**
         * The system exits a privacy page during screen capture.
         *
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @since 12
         */
        SCREENCAPTURE_STATE_EXIT_PRIVATE_SCENE = 9,
        /**
         * Screen capture is interrupted by system user switchover.
         *
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @since 12
         */
        SCREENCAPTURE_STATE_STOPPED_BY_USER_SWITCHES = 10,
        /**
         * Screen capture paused by user.
         *
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @stagemodelonly
         * @since 26.0.0
         */
        SCREENCAPTURE_STATE_PAUSED_BY_USER = 11,
        /**
         * Screen capture resumed by user.
         *
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @stagemodelonly
         * @since 26.0.0
         */
        SCREENCAPTURE_STATE_RESUMED_BY_USER = 12,
        /**
         * Screen capture paused by app.
         *
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @stagemodelonly
         * @since 26.0.0
         */
        SCREENCAPTURE_STATE_PAUSED_BY_APP = 13,
        /**
         * Screen capture resumed by app.
         *
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @stagemodelonly
         * @since 26.0.0
         */
        SCREENCAPTURE_STATE_RESUMED_BY_APP = 14
    }
    /**
     * Provides the media AVScreenCaptureStrategy definition.
     *
     * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
     * @since 20
     */
    interface AVScreenCaptureStrategy {
        /**
         * Allows starting or maintaining screen capture during a call
         *
         * @default {false} [Required if provided]
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @since 20
         */
        keepCaptureDuringCall?: boolean;
        /**
         * Indicates whether to enable B-frame encoding, which is used to reduce the size of the recorded file.
         *
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @since 20
         */
        enableBFrame?: boolean;
        /**
         * Set the fill mode for screen capture when a privacy window exists.
         *
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @stagemodelonly
         * @since 23
         */
        privacyMaskMode?: number;
        /**
         * Enable pausing the screen capture. The default value is false.
         *
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @stagemodelonly
         * @since 26.0.0
         */
        enablePause?: boolean;
    }
    /**
     * Defines the screen capture parameters.
     *
     * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
     * @since 12
     */
    interface AVScreenCaptureRecordConfig {
        /**
         * FD of the file output.
         *
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @since 12
         */
        fd: number;
        /**
         * Video width, in px. The default value varies according to the display in use.
         *
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @since 12
         */
        frameWidth?: number;
        /**
         * Video height, in px. The default value varies according to the display in use.
         *
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @since 12
         */
        frameHeight?: number;
        /**
         * Video bit rate, in bit/s. The default value is **10000000**.
         *
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @since 12
         */
        videoBitrate?: number;
        /**
         * Audio sampling rate, in Hz. This value is used for both internal capture
         * and external capture (using microphones), in Hz. Only **48000** (default value) and **16000** are supported.
         *
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @since 12
         */
        audioSampleRate?: number;
        /**
         * Number of audio channels. This value is used for both internal capture and external capture (using microphones).
         * Only **1** and **2** (default) are supported.
         *
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @since 12
         */
        audioChannelCount?: number;
        /**
         * Audio bit rate, in bit/s. This value is used for both internal capture and external capture (using microphones).
         * The default value is **96000**.
         *
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @since 12
         */
        audioBitrate?: number;
        /**
         * Encoding and container format used. The default value is **SCREEN_RECORD_PRESET_H264_AAC_MP4**.
         *
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @since 12
         */
        preset?: AVScreenCaptureRecordPreset;
        /**
         * ID of the display used for screen capture. By default, the main screen is captured.
         *
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @since 15
         */
        displayId?: number;
        /**
         * Video fill mode during screen capture.
         *
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @since 18
         */
        fillMode?: AVScreenCaptureFillMode;
        /**
         * Screen Capture Policy Configuration Fields
         *
         * @default {default value of the property} [Required if provided]
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @since 20
         */
        strategy?: AVScreenCaptureStrategy;
    }
    /**
    * Enumerates the display mode for the screen capture picker.
    *
    * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
    * @since 22
    */
    enum PickerMode {
        /**
         * Displays only a list of windows.
         *
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @since 22
         */
        WINDOW_ONLY = 0,
        /**
         * Displays only a list of screens.
         *
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @since 22
         */
        SCREEN_ONLY = 1,
        /**
         * Displays both screens and windows.
         *
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @since 22
         */
        SCREEN_AND_WINDOW = 2,
        /**
         * Show application options only.
         *
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @stagemodelonly
         * @since 26.0.0
         */
        APP_ONLY = 3,
        /**
         * Show both window and application options.
         *
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @stagemodelonly
         * @since 26.0.0
         */
        WINDOW_AND_APP = 4,
        /**
         * Show both screen and application options.
         *
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @stagemodelonly
         * @since 26.0.0
         */
        SCREEN_AND_APP = 5,
        /**
         * Show screen, window, and application options.
         *
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @stagemodelonly
         * @since 26.0.0
         */
        SCREEN_WINDOW_AND_APP = 6
    }
    /**
     * AVScreenCaptureRecorder is a class for screen capture management. It provides APIs for screen capture. Before
     * calling any API in AVScreenCaptureRecorder, you must use
     * [createAVScreenCaptureRecorder()]{@link @ohos.multimedia.media:media.createAVScreenCaptureRecorder()} to create an
     * AVScreenCaptureRecorder instance.
     *
     * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
     * @since 12
     */
    interface AVScreenCaptureRecorder {
        /**
         * Initializes screen capture and sets screen capture parameters. This API uses a promise to return the result.
         *
         * @param { AVScreenCaptureRecordConfig } config - Screen capture parameters to set.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.
         *     <br>2. Incorrect parameter types. 3. Parameter verification failed. Return by promise.
         * @throws { BusinessError } 5400103 - IO error. Return by promise.
         * @throws { BusinessError } 5400105 - Service died. Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @since 12
         */
        init(config: AVScreenCaptureRecordConfig): Promise<void>;
        /**
         * Starts screen recording. Before using this API, you must call
         * [init]{@link @ohos.multimedia.media:media.AVScreenCaptureRecorder.init}. This API uses a promise to return the
         * result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 5400103 - IO error. Return by promise.
         * @throws { BusinessError } 5400105 - Service died. Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @since 12
         */
        startRecording(): Promise<void>;
        /**
         * Stops screen recording. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 5400103 - IO error. Return by promise.
         * @throws { BusinessError } 5400105 - Service died. Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @since 12
         */
        stopRecording(): Promise<void>;
        /**
         * Pause screen capture. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 5400102 - Operation not be permitted. Return by promise.
         * @throws { BusinessError } 5400103 - IO error. Return by promise.
         * @throws { BusinessError } 5400105 - Service died. Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @stagemodelonly
         * @since 26.0.0
         */
        pauseRecording(): Promise<void>;
        /**
         * Resume screen capture. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 5400102 - Operation not be permitted. Return by promise.
         * @throws { BusinessError } 5400103 - IO error. Return by promise.
         * @throws { BusinessError } 5400105 - Service died. Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @stagemodelonly
         * @since 26.0.0
         */
        resumeRecording(): Promise<void>;
        /**
         * During screen capture, the application can exempt its privacy windows from security purposes. This API uses a
         * promise to return the result.
         *
         * For example, if a user enters a password in this application during screen capture, the application will not
         * display a black screen.
         *
         * @param { Array<number> } windowIDs - IDs of windows that require privacy exemption, including the main window IDs
         *     and subwindow IDs. For details about how to obtain window properties, see
         *     [getWindowProperties](docroot://reference/apis-arkui/arkts-apis-window-Window.md#getwindowproperties9).
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 5400103 - IO error. Return by promise.
         * @throws { BusinessError } 5400105 - Service died. Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @since 12
         */
        skipPrivacyMode(windowIDs: Array<number>): Promise<void>;
        /**
         * Sets the display mode of the picker. The setting takes effect the next time the picker is displayed. This API
         * uses a promise to return the result.
         *
         * @param { PickerMode } pickerMode - Picker mode.<br>It defines the content type displayed in the picker. The
         *     options are as follows:<br>- **SCREEN_ONLY**: Displays only a list of screens.<br>- **WINDOW_ONLY**: Displays
         *     only a list of windows.<br>- **SCREEN_AND_WINDOW**: Displays both screens and windows. It is the default
         *     value.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by promise.
         * @throws { BusinessError } 5400103 - IO error. Return by promise.
         * @throws { BusinessError } 5400105 - Service died. Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @since 22
         */
        setPickerMode(pickerMode: PickerMode): Promise<void>;
        /**
         * Sets the list of windows to be hidden in the picker. The setting takes effect the next time the picker is
         * displayed. This API uses a promise to return the result.
         *
         * @param { Array<number> } excludedWindows - List of windows to be hidden in the picker. For details about how to
         *     obtain window properties, see
         *     [getWindowProperties](docroot://reference/apis-arkui/arkts-apis-window-Window.md#getwindowproperties9).
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by promise.
         * @throws { BusinessError } 5400103 - IO error. Return by promise.
         * @throws { BusinessError } 5400105 - Service died. Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @since 22
         */
        excludePickerWindows(excludedWindows: Array<number>): Promise<void>;
        /**
         * Displays the Picker once more after the screen capture starts, allowing for dynamic updates to the recording
         * source, such as changing the window or screen being recorded. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > - The ongoing capture process remains uninterrupted while updating the recording source.
         * >
         * > - Following the dynamic update of the recording source through the Picker, the capture proceeds with the newly
         * > selected source.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by promise.
         * @throws { BusinessError } 5400103 - IO error. Return by promise.
         * @throws { BusinessError } 5400105 - Service died. Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @since 22
         */
        presentPicker(): Promise<void>;
        /**
         * Enables or disables the microphone. This API uses a promise to return the result.
         *
         * @param { boolean } enable - Whether to enable the microphone. **true** to enable, **false** otherwise.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 5400103 - IO error. Return by promise.
         * @throws { BusinessError } 5400105 - Service died. Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @since 12
         */
        setMicEnabled(enable: boolean): Promise<void>;
        /**
         * Releases this AVScreenCaptureRecorder instance. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 5400103 - IO error. Return by promise.
         * @throws { BusinessError } 5400105 - Service died. Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @since 12
         */
        release(): Promise<void>;
        /**
         * add a watermark for the AVScreenCaptureRecorder. This API uses a promise to return the result.
         * App can add up to 5 watermarks.
         * This API can be called only before calling startRecording().
         *
         * @param { image.PixelMap } watermark - : Watermark image.
         * @param { WatermarkConfiguration } config - : Configuration of the watermark.
         * @returns { Promise<number> } Promise that returns the watermark id.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by promise.
         * @throws { BusinessError } 5400103 - IO error. Return by promise.
         * @throws { BusinessError } 5400105 - Service died. Return by promise.
         * @throws { BusinessError } 5400108 - The parameter check failed, parameter value out of range.
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @stagemodelonly
         * @since 26.0.0
         */
        addWatermark(watermark: image.PixelMap, config: WatermarkConfiguration): Promise<number>;
        /**
         * Sets whether the captured screen content automatically rotates to keep the image upright.
         *
         * @param { boolean } enable - Indicates whether to enable automatic rotation. The default value is **false**.
         *     A value of **true** indicates automatic rotation and the image content in the output frame remains upright.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by promise.
         * @throws { BusinessError } 5400105 - Service died. Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @stagemodelonly
         * @since 26.0.0
         */
        setContentAutoRotation(enable: boolean): Promise<void>;
        /**
         * Subscribes to screen capture state changes. An application can subscribe to only one screen capture state change
         * event. When the application initiates multiple subscriptions to this event, the last subscription is applied.
         *
         * @param { 'stateChange' } type - Event type, which is **'stateChange'** in this case.
         * @param { Callback<AVScreenCaptureStateCode> } callback - Callback invoked when the event is triggered.
         *     [AVScreenCaptureStateCode]{@link @ohos.multimedia.media:media.AVScreenCaptureStateCode} indicates the new
         *     state.
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @since 12
         */
        on(type: 'stateChange', callback: Callback<AVScreenCaptureStateCode>): void;
        /**
         * Subscribes to AVScreenCaptureRecorder errors. You can handle the errors based on the application logic. An
         * application can subscribe to only one AVScreenCaptureRecorder error event. When the application initiates
         * multiple subscriptions to this event, the last subscription is applied.
         *
         * @param { 'error' } type - Event type, which is **'error'** in this case.
         * @param { ErrorCallback } callback - Callback invoked when the event is triggered.
         * @throws { BusinessError } 201 - permission denied.
         * @throws { BusinessError } 5400103 - IO error. Return by ErrorCallback.
         * @throws { BusinessError } 5400105 - Service died. Return by ErrorCallback.
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @since 12
         */
        on(type: 'error', callback: ErrorCallback): void;
        /**
         * Unsubscribes from screen capture state changes. You can specify a callback to cancel the specified subscription.
         *
         * @param { 'stateChange' } type - Event type, which is **'stateChange'** in this case.
         * @param { Callback<AVScreenCaptureStateCode> } callback - Callback used for unsubscription.
         *     [AVScreenCaptureStateCode]{@link @ohos.multimedia.media:media.AVScreenCaptureStateCode} indicates the new
         *     state. If this parameter is not specified, the last subscription is canceled.
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @since 12
         */
        off(type: 'stateChange', callback?: Callback<AVScreenCaptureStateCode>): void;
        /**
         * Unsubscribes from AVScreenCaptureRecorder errors. You can specify a callback to cancel the specified
         * subscription.
         *
         * @param { 'error' } type - Event type, which is **'error'** in this case.
         * @param { ErrorCallback } callback - Callback used for unsubscription. If this parameter is not specified, the
         *     last subscription is canceled.
         * @syscap SystemCapability.Multimedia.Media.AVScreenCapture
         * @since 12
         */
        off(type: 'error', callback?: ErrorCallback): void;
    }
    /**
     * Describes the video transcoding parameters.
     *
     * @syscap SystemCapability.Multimedia.Media.AVTranscoder
     * @atomicservice [since 22]
     * @since 12
     */
    interface AVTranscoderConfig {
        /**
         * Bitrate of the output audio, in bit/s. The value range is [1-500000]. The default value is 48 kbit/s.
         *
         * @syscap SystemCapability.Multimedia.Media.AVTranscoder
         * @atomicservice [since 22]
         * @since 12
         */
        audioBitrate?: number;
        /**
         * Encoding format of the output audio. Currently, only AAC is supported. The default value is **AAC**.
         *
         * @syscap SystemCapability.Multimedia.Media.AVTranscoder
         * @atomicservice [since 22]
         * @since 12
         */
        audioCodec?: CodecMimeType;
        /**
         * Encoding format of the output audio. If the specified format is not supported, prepare will fail.
         * Default value: AUDIO_AAC.
         *
         * @syscap SystemCapability.Multimedia.Media.AVTranscoder
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        audioCodecV2?: CodecMimeType;
        /**
         * Container format of the output video file. Currently, only MP4 is supported.
         *
         * @syscap SystemCapability.Multimedia.Media.AVTranscoder
         * @atomicservice [since 22]
         * @since 12
         */
        fileFormat: ContainerFormatType;
        /**
         * Bitrate of the output video, in bit/s. The default bitrate depends on the resolution of the output video.
         * The default bitrate is 1 Mbit/s for the resolution in the range [240p, 480P],
         * 2 Mbit/s for the range (480P,720P], 4 Mbit/s for the range (720P,1080P], and 8 Mbit/s for 1080p or higher.
         *
         * @syscap SystemCapability.Multimedia.Media.AVTranscoder
         * @atomicservice [since 22]
         * @since 12
         */
        videoBitrate?: number;
        /**
         * Encoding format of the output video. Currently, only AVC and HEVC are supported.
         * If the source video is in HEVC format, the default value is **HEVC**. Otherwise, the default value is **AVC**.
         *
         * @syscap SystemCapability.Multimedia.Media.AVTranscoder
         * @atomicservice [since 22]
         * @since 12
         */
        videoCodec?: CodecMimeType;
        /**
         * Width of the output video frame, in px. The value range is [240 - 3840].
         * The default value is the width of the source video frame.
         *
         * @syscap SystemCapability.Multimedia.Media.AVTranscoder
         * @atomicservice [since 22]
         * @since 12
         */
        videoFrameWidth?: number;
        /**
         * Height of the output video frame, in px. The value range is [240 - 2160].
         * The default value is the height of the source video frame.
         *
         * @syscap SystemCapability.Multimedia.Media.AVTranscoder
         * @atomicservice [since 22]
         * @since 12
         */
        videoFrameHeight?: number;
        /**
         * Indicates whether to enable B Frame Encoding for reduce file size.
         *
         * @syscap SystemCapability.Multimedia.Media.AVTranscoder
         * @atomicservice [since 22]
         * @since 20
         */
        enableBFrame?: boolean;
    }
    /**
     * AVTranscoder is a transcoding management class. It provides APIs to transcode videos. Before calling any API in
     * AVTranscoder, you must use [createAVTranscoder()]{@link @ohos.multimedia.media:media.createAVTranscoder()} to
     * create an AVTranscoder instance.
     *
     * For details about the AVTranscoder demo, see
     * [Using AVTranscoder for Transcoding](docroot://media/media/using-avtranscoder-for-transcodering.md).
     *
     * @syscap SystemCapability.Multimedia.Media.AVTranscoder
     * @atomicservice [since 22]
     * @since 12
     */
    interface AVTranscoder {
        /**
         * Source media file descriptor, which specifies the data source.
         *
         * There is a media file that stores continuous assets, the address offset is 0, and the byte length is 100. Its
         * file descriptor is **AVFileDescriptor { fd = resourceHandle; offset = 0; length = 100; }**.
         *
         * **NOTE**
         *
         * - After the resource handle (FD) is transferred to an AVTranscoder instance, do not use the resource handle to
         * perform other read and write operations, including but not limited to transferring this handle to other AVPlayer,
         * AVMetadataExtractor, AVImageGenerator, or AVTranscoder instance.
         * - Competition occurs when multiple AVTranscoders use the same resource handle to read and write files at the same
         * time, resulting in errors in obtaining data.
         *
         * @syscap SystemCapability.Multimedia.Media.AVTranscoder
         * @atomicservice [since 22]
         * @since 12
         */
        fdSrc: AVFileDescriptor;
        /**
         * Destination media file descriptor, which specifies the data source. After creating an AVTranscoder instance, you
         * must set both **fdSrc** and **fdDst**.
         *
         * **NOTE**
         *
         * - After the resource handle (FD) is transferred to an AVTranscoder instance, do not use the resource handle to
         * perform other read and write operations, including but not limited to transferring this handle to other AVPlayer,
         * AVMetadataExtractor, AVImageGenerator, or AVTranscoder instance.
         * - Competition occurs when multiple AVTranscoders use the same resource handle to read and write files at the same
         * time, resulting in errors in obtaining data.
         *
         * @syscap SystemCapability.Multimedia.Media.AVTranscoder
         * @atomicservice [since 22]
         * @since 12
         */
        fdDst: number;
        /**
         * Sets video transcoding parameters. This API uses a promise to return the result.
         *
         * @param {  AVTranscoderConfig  } config - Video transcoding parameters to set.<!--RP1--><!--RP1End-->
         * @returns {  Promise<void>  } Promise that returns no value.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by promise.
         * @throws { BusinessError } 5400103 - IO error. Return by promise.
         * @throws { BusinessError } 5400105 - Service died. Return by promise.
         * @throws { BusinessError } 5400106 - Unsupported format. Returned by promise.
         * @throws { BusinessError } 401 - The parameter check failed. Return by promise. [since 22]
         * @syscap SystemCapability.Multimedia.Media.AVTranscoder
         * @atomicservice [since 22]
         * @since 12
         */
        prepare(config: AVTranscoderConfig): Promise<void>;
        /**
         * Starts video transcoding. This API uses a promise to return the result.
         *
         * This API can be called only after the [prepare()]{@link media.AVTranscoder.prepare} API is called.
         *
         * @returns {  Promise<void>  } Promise that returns no value.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by promise.
         * @throws { BusinessError } 5400103 - IO error. Return by promise.
         * @throws { BusinessError } 5400105 - Service died. Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVTranscoder
         * @atomicservice [since 22]
         * @since 12
         */
        start(): Promise<void>;
        /**
         * Pauses video transcoding. This API uses a promise to return the result.
         *
         * This API can be called only after the [start()]{@link media.AVTranscoder.start} API is called. You can call
         * [resume()]{@link media.AVTranscoder.resume} to resume transcoding.
         *
         * @returns {  Promise<void>  } Promise that returns no value.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by promise.
         * @throws { BusinessError } 5400103 - IO error. Return by promise.
         * @throws { BusinessError } 5400105 - Service died. Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVTranscoder
         * @atomicservice [since 22]
         * @since 12
         */
        pause(): Promise<void>;
        /**
         * Resumes video transcoding. This API uses a promise to return the result.
         *
         * This API can be called only after the [pause()]{@link media.AVTranscoder.pause} API is called.
         *
         * @returns {  Promise<void>  } Promise that returns no value.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by promise.
         * @throws { BusinessError } 5400103 - IO error. Return by promise.
         * @throws { BusinessError } 5400105 - Service died. Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVTranscoder
         * @atomicservice [since 22]
         * @since 12
         */
        resume(): Promise<void>;
        /**
         * Cancels video transcoding. This API uses a promise to return the result.
         *
         * This API can be called only after the [prepare()]{@link media.AVTranscoder.prepare},
         * [start()]{@link media.AVTranscoder.start}, [pause()]{@link media.AVTranscoder.pause}, or
         * [resume()]{@link media.AVTranscoder.resume} API is called.
         *
         * @returns {  Promise<void>  } Promise that returns no value.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by promise.
         * @throws { BusinessError } 5400103 - IO error. Return by promise.
         * @throws { BusinessError } 5400105 - Service died. Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVTranscoder
         * @atomicservice [since 22]
         * @since 12
         */
        cancel(): Promise<void>;
        /**
         * Releases video transcoding resources. This API uses a promise to return the result.
         *
         * After the resources are released, you can no longer perform any operation on the AVTranscoder instance.
         *
         * @returns {  Promise<void>  } Promise that returns no value.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by promise.
         * @throws { BusinessError } 5400105 - Service died. Return by promise.
         * @syscap SystemCapability.Multimedia.Media.AVTranscoder
         * @atomicservice [since 22]
         * @since 12
         */
        release(): Promise<void>;
        /**
         * Subscribes to the event indicating that transcoding is complete. An application can subscribe to only one
         * transcoding progress update event. When the application initiates multiple subscriptions to this event, the last
         * subscription is applied. This API uses an asynchronous callback to return the result.
         *
         * When this event is reported, the current transcoding operation is complete. You need to call
         * [release()]{@link media.AVTranscoder.release} to exit the transcoding.
         *
         * @param { 'complete' } type - Event type, which is **'complete'** in this case. This event is triggered by the
         *     system during transcoding.
         * @param { Callback<void> } callback - Callback used to return the event callback method.
         * @syscap SystemCapability.Multimedia.Media.AVTranscoder
         * @atomicservice [since 22]
         * @since 12
         */
        on(type: 'complete', callback: Callback<void>): void;
        /**
         * Subscribes to AVTranscoder errors. If this event is reported, call [release()]{@link media.AVTranscoder.release}
         * to exit the transcoding. This API uses an asynchronous callback to return the result.
         *
         * An application can subscribe to only one AVTranscoder error event. When the application initiates multiple
         * subscriptions to this event, the last subscription is applied.
         *
         * @param { 'error' } type - Event type, which is **'error'** in this case.<br>This event is triggered when an error
         *     occurs during recording.
         * @param { ErrorCallback } callback - Callback invoked when the event is triggered.
         * @throws { BusinessError } 401 - The parameter check failed.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 5400101 - No memory.
         * @throws { BusinessError } 5400102 - Operation not allowed.
         * @throws { BusinessError } 5400103 - I/O error.
         * @throws { BusinessError } 5400104 - Time out.
         * @throws { BusinessError } 5400105 - Service died.
         * @throws { BusinessError } 5400106 - Unsupported format.
         * @syscap SystemCapability.Multimedia.Media.AVTranscoder
         * @atomicservice [since 22]
         * @since 12
         */
        on(type: 'error', callback: ErrorCallback): void;
        /**
         * Subscribes to transcoding progress updates. An application can subscribe to only one transcoding progress update
         * event. When the application initiates multiple subscriptions to this event, the last subscription is applied.
         * This API uses an asynchronous callback to return the result.
         *
         * @param { 'progressUpdate' } type - Event type, which is **'progressUpdate'** in this case. This event is
         *     triggered by the system during transcoding.
         * @param { Callback<number> } callback - Callback used to return the progress update event. The **number** parameter
         *     in the function indicates the current transcoding progress, in percentage.
         * @syscap SystemCapability.Multimedia.Media.AVTranscoder
         * @atomicservice [since 22]
         * @since 12
         */
        on(type: 'progressUpdate', callback: Callback<number>): void;
        /**
         * Unsubscribes from the event indicating that transcoding is complete.
         *
         * @param { 'complete' } type - Event type, which is **'complete'** in this case.
         * @param { Callback<void> } callback - Callback that has been registered to listen for transcoding completion
         *     events.
         * @syscap SystemCapability.Multimedia.Media.AVTranscoder
         * @atomicservice [since 22]
         * @since 12
         */
        off(type: 'complete', callback?: Callback<void>): void;
        /**
         * Unsubscribes from AVTranscoder errors. After the unsubscription, your application can no longer receive
         * AVTranscoder errors.
         *
         * @param { 'error' } type - Event type, which is **'error'** in this case.<br>This event is triggered when an error
         *     occurs during transcoding.
         * @param { ErrorCallback } callback - Callback that has been registered to listen for AVTranscoder errors.
         * @syscap SystemCapability.Multimedia.Media.AVTranscoder
         * @atomicservice [since 22]
         * @since 12
         */
        off(type: 'error', callback?: ErrorCallback): void;
        /**
         * Unsubscribes from transcoding progress updates.
         *
         * @param { 'progressUpdate' } type - Event type, which is **'progressUpdate'** in this case.
         * @param { Callback<number> } callback - Called that has been registered to listen for progress updates. You are
         *     advised to use the default value because only the last registered callback is retained in the current
         *     callback mechanism.
         * @syscap SystemCapability.Multimedia.Media.AVTranscoder
         * @atomicservice [since 22]
         * @since 12
         */
        off(type: 'progressUpdate', callback?: Callback<number>): void;
        /**
         * add a watermark for the AVTranscoder. This API uses a promise to return the result.
         * App can add up to 5 watermarks.
         * This API can be called only before the prepared state.
         *
         * @param { image.PixelMap } watermark - : Watermark image.
         * @param { WatermarkConfiguration } config - : Configuration of the watermark.
         * @returns { Promise<number> } Promise that returns the watermark id.
         * @throws { BusinessError } 5400102 - Operation not allowed. Return by promise.
         * @throws { BusinessError } 5400103 - IO error. Return by promise.
         * @throws { BusinessError } 5400105 - Service died. Return by promise.
         * @throws { BusinessError } 5400108 - The parameter check failed, parameter value out of range.
         * @syscap SystemCapability.Multimedia.Media.AVTranscoder
         * @stagemodelonly
         * @since 26.0.0
         */
        addWatermark(watermark: image.PixelMap, config: WatermarkConfiguration): Promise<number>;
    }
    /**
     * Set configuration of a watermark. The position starts at top left corner.
     *
     * @typedef WatermarkConfiguration
     * @syscap SystemCapability.Multimedia.Media.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    interface WatermarkConfiguration {
        /**
         * Offset of the watermark to the top line of pixel
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        top: number;
        /**
         * Offset of the watermark to the left line of pixel
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        left: number;
        /**
         * target width of the watermark in pixel
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        width?: number;
        /**
         * target height of the watermark in pixel
         * The value range is all integers.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        height?: number;
    }
    /**
     * Create a MediaSource object from the given directory.
     *
     * @param { string } path - Buffer path information for creating a media source.
     * @returns { Promise<MediaSource | undefined> } If success, a MediaSource is returned. Otherwise returns null.
     * @throws { BusinessError } 5411007 - The directory specified by the path parameter does not exist or inaccessible.
     * @syscap SystemCapability.Multimedia.Media.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    function createMediaSourceWithDirectory(path: string): Promise<MediaSource | undefined>;
    /**
     * Creating a Streaming Resource Download Task Manager
     *
     * @returns { Promise<AVDownloaderManager> } Promise used to return AVDownloaderManager.
     * @syscap SystemCapability.Multimedia.Media.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    function createAVDownloaderManager(): Promise<AVDownloaderManager>;
    /**
     * Enumerates the states of the download task.
     * @syscap SystemCapability.Multimedia.Media.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    type AVDownloadTaskState = 'init' | 'queued' | 'running' | 'completed' | 'paused' | 'removing' | 'error';
    /**
     * Describes the callback invoked for the AVDownloader state change event.
     *
     * @param { string } taskId - ID of the task whose status changes.
     * @param { AVDownloadTaskState } status - New status of the task switchover.
     * @syscap SystemCapability.Multimedia.Media.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    type OnAVDownloadTaskStateHandle = (taskId: string, state: AVDownloadTaskState) => void;
    /**
     * Describes the callback invoked for the AVDownloader progress change event.
     *
     * @param { string } taskId - ID of the task whose status changes.
     * @param { number } status - Progress value ranges from 0.0 to 1.0.
     * @syscap SystemCapability.Multimedia.Media.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    type OnAVDownloadProgressChangeHandle = (taskId: string, progress: number) => void;
    /**
     * Definition of the Offline Download Management Interface
     *
     * @syscap SystemCapability.Multimedia.Media.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    interface AVDownloaderManager {
        /**
         * Set the network environment for the download. By default, the download is performed only in the Wi-Fi environment.
         *
         * @param { boolean } value - If is set to true, the download can be performed in any network environment,
         *     Otherwise, the download is performed only in the free Wi-Fi network environment.
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        allowsCellularAccess(value: boolean): void;
        /**
         * Sets the network timeout interval for HTTP requests. If the timeout interval is exceeded, the download fails.
         *
         * @param { number } timeout - Timeout duration, in ms. If is not set, the default timeout duration is used.
         *     The value should be an integer.
         *     <br>**Description**</br>
         *     <ul><li>If the value is less than 0, there is no timeout duration.</li></ul>.
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        setRequestTimeout(timeout: number): void;
        /**
         * Create a download task based on the media description.
         *
         * @param { MediaSource } source - Media description, including at least the resource URL.
         *     <br>Value constraint:The value cannot be null.
         * @returns { string } ID of the offline download task that is successfully added.
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        addAVDownloadTask(source: MediaSource): string;
        /**
         * Remove a download task from the offline download manager
         *
         * @param { string } [taskId] - Specifies the ID of an offline download task.
         *     <br>Default value:    If this parameter is not specified, all offline download tasks are cleared..
         * @throws { BusinessError } 5400108 - If the specified ID is not in the offline download task manager.
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        removeDownloadTask(taskId?: string): void;
        /**
         * Suspending the download of a specified task
         *
         * @param { string } [taskId] - ID of the task whose download needs to be suspended.
         *     Value constraint:If the task ID is not transferred, all download tasks are suspended..
         * @throws { BusinessError } 5400108 - If the specified ID is not in the offline download task manager.
         * @throws { BusinessError } 5400102 - Operation not allowed.
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        pauseDownloadTask(taskId?: string): void;
        /**
         * Resuming Offline Download of a Specified Task
         *
         * @param { string } [taskId] - Specifies the ID of an offline download task.
         *     Value constraint:If this parameter is not specified, all suspended offline download tasks are resumed..
         * @throws { BusinessError } 5400108 - If the specified ID is not in the offline download task manager.
         * @throws { BusinessError } 5400102 - Operation not allowed.
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        resumeDownloadTask(taskId?: string): void;
        /**
         * Obtains all offline download tasks in the Task Manager. Ended download tasks are automatically cleared.
         *
         * @returns { Array<string> } If a task exists in the task manager, the task ID array is returned. Otherwise null.
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        getDownloadTasks(): Array<string>;
        /**
         * Obtains the offline download cache directory of a specified task.
         *
         * @param { string } taskId - ID of a task whose download cache directory is queried.
         * @returns { string } Return the accessible path of the offline download task on the disk.
         * @throws { BusinessError } 5400108 - If the specified ID is not in the manager, an error is returned.
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        getTaskCacheDirectory(taskId: string): string;
        /**
         * Obtains the status of a specified offline download task. For details, see #AVDownloadTaskState.
         *
         * @param { string } taskId - ID of a task whose status is queried.
         * @returns { AVDownloadTaskState } Returns the task status of a specified task.
         * @throws { BusinessError } 5400108 - If the specified ID is not in the manager, an error is returned.
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        getTaskStatus(taskId: string): AVDownloadTaskState;
        /**
         * Obtains the progress of a specified offline download task.
         *
         * @param { string } taskId - ID of the task for querying the progress.
         * @returns { number } Returns the approximate ratio of the download progress of a specified task.
         *     Value range: [0.0-1.0] If the returned value range is -1, the resource size is unknown.
         * @throws { BusinessError } 5400108 - If the specified ID is not in the manager, an error is returned.
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        getTaskProgress(taskId: string): number;
        /**
         * Registering a Function for Listening on Status Changes of Offline Download Tasks
         *
         * @param { OnAVDownloadTaskStateHandle } callback - Prototype of the function invoked by the event.
         *     The first parameter indicates the ID of the task whose status changes.
         *     The second parameter indicates the new status of the task switchover.
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        onStatusChange(callback: OnAVDownloadTaskStateHandle): void;
        /**
         * Registers a function to listen to the progress change value of an offline download task.
         * The progress change of the offline download task exceeds 1% compared with that of the last time.
         * The event is triggered after the interval exceeds 500 ms.
         *
         * @param { OnAVDownloadProgressChangeHandle } callback - Prototype of the function called by the event.
         *     The first parameter indicates the offline download task ID.
         *     The second parameter indicates the progress of an offline download task.
         *     The progress value ranges from 0.0 to 1.0,
         *     If the value is -1, the size of the resource is unknown.
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        onProgressChange(callback: OnAVDownloadProgressChangeHandle): void;
        /**
         * Deregisters a specified function's listening on task status change events.
         *
         * @param { OnAVDownloadTaskStateHandle } [callback] - Prototype of the function invoked by the event.
         *     The first parameter indicates the ID of the offline download task.
         *     The second parameter indicates the latest status of the offline download task.
         *     <br>Default value: If no parameter is set, all listening functions for the event are canceled.
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        offStatusChange(callback?: OnAVDownloadTaskStateHandle): void;
        /**
         * Deregisters a specified function's listening on task progress change events.
         *
         * @param { OnAVDownloadProgressChangeHandle } [callback] - Prototype of the function called by the event.
         *     The first parameter indicates the offline download task ID.
         *     The second parameter indicates the progress of an offline download task.
         *     The progress value ranges from 0.0 to 1.0,
         *     If the value is -1, the size of the resource is unknown.
         *     <br>Default value: If no parameter is set, all listening functions for the event are canceled.
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        offProgressChange(callback?: OnAVDownloadProgressChangeHandle): void;
        /**
         * Release resources used for AVDownloaderManager.
         *
         * @syscap SystemCapability.Multimedia.Media.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        release(): void;
    }
}
export default media;

```
