# @ohos.multimedia.audio.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2021-2025 Huawei Device Co., Ltd.
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
 * @kit AudioKit
 */
import { AsyncCallback, Callback } from './@ohos.base';
/**
 * The module provides basic audio control capabilities, including volume adjustment, device management, data capture,
 * and rendering.
 *
 * This module provides the following common audio-related functions:
 *
 * - [AudioManager]{@link @ohos.multimedia.audio:audio}: audio manager.
 * - [AudioRenderer]{@link @ohos.multimedia.audio:audio}: audio renderer, used to play Pulse Code Modulation (PCM) audio
 * data.
 * - [AudioCapturer]{@link @ohos.multimedia.audio:audio}: audio capturer, used to record PCM audio data.
 *
 * @syscap SystemCapability.Multimedia.Audio.Core [since 12]
 * @crossplatform [since 12]
 * @atomicservice [since 12]
 * @since 7
 */
declare namespace audio {
    /**
     * Enumerates the error codes available for audio management.
     *
     * @syscap SystemCapability.Multimedia.Audio.Core
     * @crossplatform [since 12]
     * @since 9
     */
    enum AudioErrors {
        /**
         * Invalid parameter.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 9
         */
        ERROR_INVALID_PARAM = 6800101,
        /**
         * Memory allocation failure.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 9
         */
        ERROR_NO_MEMORY = 6800102,
        /**
         * Unsupported state.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 9
         */
        ERROR_ILLEGAL_STATE = 6800103,
        /**
         * Unsupported parameter value.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 9
         */
        ERROR_UNSUPPORTED = 6800104,
        /**
         * Processing timeout.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 9
         */
        ERROR_TIMEOUT = 6800105,
        /**
         * Too many audio streams.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 9
         */
        ERROR_STREAM_LIMIT = 6800201,
        /**
         * System error.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 9
         */
        ERROR_SYSTEM = 6800301
    }
    /**
     * Define default volume group id for audio.
     *
     * @syscap SystemCapability.Multimedia.Audio.Volume
     * @crossplatform [since 12]
     * @since 9
     */
    const DEFAULT_VOLUME_GROUP_ID: number;
    /**
     * Define default interrupt group id for audio.
     *
     * @syscap SystemCapability.Multimedia.Audio.Interrupt
     * @since 9
     */
    const DEFAULT_INTERRUPT_GROUP_ID: number;
    /**
     * Obtains an AudioManager instance.
     *
     * @returns { AudioManager } AudioManager instance.
     * @syscap SystemCapability.Multimedia.Audio.Core
     * @crossplatform [since 12]
     * @atomicservice [since 23]
     * @since 7
     */
    function getAudioManager(): AudioManager;
    /**
     * Creates an AudioCapturer instance. This API uses an asynchronous callback to return the result.
     *
     * @param { AudioCapturerOptions } options - Capturer configurations.
     * @param { AsyncCallback<AudioCapturer> } callback - Callback used to return the result. If the operation is
     *     successful, **err** is **undefined** and **data** is the AudioCapturer instance obtained; otherwise, **err** is
     *     an error object. If the operation fails, an error object with one of the following error codes is returned:<br>
     *     Error code 6800301: indicates a parameter verification exception, permission verification exception, or system
     *     processing exception. For details, see system logs.<br>Error code 6800101: indicates that a mandatory parameter
     *     is null or the parameter type is incorrect.
     * @syscap SystemCapability.Multimedia.Audio.Capturer
     * @crossplatform [since 12]
     * @since 8
     */
    function createAudioCapturer(options: AudioCapturerOptions, callback: AsyncCallback<AudioCapturer>): void;
    /**
     * Creates an AudioCapturer instance. This API uses a promise to return the result.
     *
     * @param { AudioCapturerOptions } options - Capturer configurations.
     * @returns { Promise<AudioCapturer> } Promise used to return the result. If the operation is successful, an
     *     AudioCapturer instance is returned; otherwise, an error object with either of the following error codes is
     *     returned:
     *     <br>Error code 6800301: indicates a parameter verification exception, permission verification exception, or system
     *     processing exception. For details, see system logs.
     *     <br>Error code 6800101: indicates that a mandatory parameter is null or the parameter type is incorrect.
     * @syscap SystemCapability.Multimedia.Audio.Capturer
     * @crossplatform [since 12]
     * @since 8
     */
    function createAudioCapturer(options: AudioCapturerOptions): Promise<AudioCapturer>;
    /**
     * Obtains an {@link AudioRenderer} instance.
     * This method uses a promise to return the renderer instance.
     *
     * The AudioRenderer instance is used to play streaming audio data.
     * When using AudioRenderer apis, there are many instructions for application
     * to achieve better performance and lower power consumption:
     * In music or audiobook background playback situation, you can have low power
     * consumption by following this best practices document **Low-Power Rules in Music Playback Scenarios**.
     * And for navigation situation, you can follow **Low-Power Rules in Navigation and Positioning Scenarios**.
     *
     * Application developer should also be careful when app goes to background, please check if your audio playback
     * is still needed, see **Audio Resources** in best practices document.
     * And avoiding to send silence audio data continuously to waste system resources, otherwise system will take
     * control measures when this behavior is detected, see **Audio Playback** in best practices document.
     *
     * If you want to use AudioRenderer api to implement a music playback application, there are also many interactive
     * scenes to consider, see **Developing an Audio Application** in best practices document.
     *
     * @param { AudioRendererOptions } options - Renderer configurations.
     * @param { AsyncCallback<AudioRenderer> } callback - Callback used to return the result. If the operation is
     *     successful, **err** is **undefined** and **data** is the AudioRenderer instance obtained; otherwise, **err** is
     *     an error object.
     * @syscap SystemCapability.Multimedia.Audio.Renderer
     * @crossplatform [since 12]
     * @since 8
     */
    function createAudioRenderer(options: AudioRendererOptions, callback: AsyncCallback<AudioRenderer>): void;
    /**
     * Obtains an {@link AudioRenderer} instance.
     * This method uses a promise to return the renderer instance.
     *
     * The AudioRenderer instance is used to play streaming audio data.
     * When using AudioRenderer apis, there are many instructions for application
     * to achieve better performance and lower power consumption:
     * In music or audiobook background playback situation, you can have low power
     * consumption by following this best practices document **Low-Power Rules in Music Playback Scenarios**.
     * And for navigation situation, you can follow **Low-Power Rules in Navigation and Positioning Scenarios**.
     *
     * Application developer should also be careful when app goes to background, please check if your audio playback
     * is still needed, see **Audio Resources** in best practices document.
     * And avoiding to send silence audio data continuously to waste system resources, otherwise system will take
     * control measures when this behavior is detected, see **Audio Playback** in best practices document.
     *
     * If you want to use AudioRenderer api to implement a music playback application, there are also many interactive
     * scenes to consider, see **Developing an Audio Application** in best practices document.
     *
     * @param { AudioRendererOptions } options - Renderer configurations.
     * @returns { Promise<AudioRenderer> } Promise used to return the AudioRenderer instance.
     * @syscap SystemCapability.Multimedia.Audio.Renderer
     * @crossplatform [since 12]
     * @since 8
     */
    function createAudioRenderer(options: AudioRendererOptions): Promise<AudioRenderer>;
    /**
     * Creates an <b>AudioLoopback</b> instance, which provides low-latency in-ear
     * monitoring using a fast capturer and renderer.
     *
     * @permission ohos.permission.MICROPHONE
     * @param { AudioLoopbackMode } mode Audio loopback mode.
     * @returns { Promise<AudioLoopback> } Promise used to return the <b>AudioLoopback</b> instance.
     * @throws { BusinessError } 201 - Permission denied.
     * @throws { BusinessError } 801 - Unsupported API.
     * @throws { BusinessError } 6800101 - Parameter verification failed.
     * @throws { BusinessError } 6800104 - Loopback mode is unsupported.
     * @syscap SystemCapability.Multimedia.Audio.Capturer
     * @since 20
     */
    /**
     * Creates an <b>AudioLoopback</b> instance, which provides low-latency in-ear
     * monitoring using a fast capturer and renderer.
     *
     * @param { AudioLoopbackMode } mode Audio loopback mode.
     * @returns { Promise<AudioLoopback> } Promise used to return the <b>AudioLoopback</b> instance.
     * @throws { BusinessError } 6800101 - Parameter verification failed.
     * @throws { BusinessError } 6800104 - Loopback mode is unsupported.
     * @syscap SystemCapability.Multimedia.Audio.Capturer
     * @since 26.0.0
     */
    function createAudioLoopback(mode: AudioLoopbackMode): Promise<AudioLoopback>;
    /**
     * Enumerates the audio states.
     *
     * @syscap SystemCapability.Multimedia.Audio.Core
     * @crossplatform [since 12]
     * @since 8
     */
    enum AudioState {
        /**
         * Invalid state.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 8
         */
        STATE_INVALID = -1,
        /**
         * Creating instance state.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 8
         */
        STATE_NEW = 0,
        /**
         * Prepared.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 8
         */
        STATE_PREPARED = 1,
        /**
         * Running.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 8
         */
        STATE_RUNNING = 2,
        /**
         * Stopped.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 8
         */
        STATE_STOPPED = 3,
        /**
         * Released.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 8
         */
        STATE_RELEASED = 4,
        /**
         * Paused.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 8
         */
        STATE_PAUSED = 5
    }
    /**
     * Enumerates the audio loopback modes.
     *
     * @syscap SystemCapability.Multimedia.Audio.Capturer
     * @since 20
     */
    enum AudioLoopbackMode {
        /**
         * Hardware loopback.
         *
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @since 20
         */
        HARDWARE = 0
    }
    /**
     * Enumerates the audio loopback statuses.
     *
     * @syscap SystemCapability.Multimedia.Audio.Capturer
     * @since 20
     */
    enum AudioLoopbackStatus {
        /**
         * Loopback is unavailable due to issues with the input or output device (for example, changes in the audio output
         * device).
         *
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @since 20
         */
        UNAVAILABLE_DEVICE = -2,
        /**
         * Loopback is unavailable due to restrictions in the audio scene (for example, audio focus or low-latency
         * management).
         *
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @since 20
         */
        UNAVAILABLE_SCENE = -1,
        /**
         * Loopback is available but currently idle.
         *
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @since 20
         */
        AVAILABLE_IDLE = 0,
        /**
         * Loopback is actively running.
         *
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @since 20
         */
        AVAILABLE_RUNNING = 1
    }
    /**
     * Enumerates the reverb modes of audio loopback.
     *
     * @syscap SystemCapability.Multimedia.Audio.Capturer
     * @since 21
     */
    enum AudioLoopbackReverbPreset {
        /**
         * Maintains the original reverb without enhancement.
         *
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @since 21
         */
        ORIGINAL = 1,
        /**
         * Provides a Karaoke-style reverb effect.
         *
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @since 21
         */
        KTV = 2,
        /**
         * Provides a theater-style reverb effect (default).
         *
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @since 21
         */
        THEATER = 3,
        /**
         * Provides a concert-style reverb effect.
         *
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @since 21
         */
        CONCERT = 4
    }
    /**
     * Enumerates the equalizer types of audio loopback.
     *
     * @syscap SystemCapability.Multimedia.Audio.Capturer
     * @since 21
     */
    enum AudioLoopbackEqualizerPreset {
        /**
         * Maintains the original sound without equalization.
         *
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @since 21
         */
        FLAT = 1,
        /**
         * Enhances the fullness of vocals (default).
         *
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @since 21
         */
        FULL = 2,
        /**
         * Enhances the brightness of vocals.
         *
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @since 21
         */
        BRIGHT = 3
    }
    /**
     * Enumerates the audio volume types.
     *
     * @syscap SystemCapability.Multimedia.Audio.Volume
     * @crossplatform [since 12]
     * @since 7
     */
    enum AudioVolumeType {
        /**
         * Audio volume type for voice calls.
         *
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @crossplatform [since 12]
         * @since 8
         */
        VOICE_CALL = 0,
        /**
         * Audio volume type for ringtones.
         *
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @crossplatform [since 12]
         * @since 7
         */
        RINGTONE = 2,
        /**
         * Audio volume type for media purpose.
         *
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @crossplatform [since 12]
         * @since 7
         */
        MEDIA = 3,
        /**
         * Audio volume type for alarming.
         *
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @crossplatform [since 12]
         * @since 10
         */
        ALARM = 4,
        /**
         * Audio volume type for accessibility.
         *
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @crossplatform [since 12]
         * @since 10
         */
        ACCESSIBILITY = 5,
        /**
         * Audio volume type for voice assistant.
         *
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @since 8
         */
        VOICE_ASSISTANT = 9
    }
    /**
     * Enumerates the audio device flags.
     *
     * @syscap SystemCapability.Multimedia.Audio.Device
     * @crossplatform [since 12]
     * @since 7
     */
    enum DeviceFlag {
        /**
         * Output devices.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @since 7
         */
        OUTPUT_DEVICES_FLAG = 1,
        /**
         * Input devices.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @since 7
         */
        INPUT_DEVICES_FLAG = 2,
        /**
         * All devices.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @since 7
         */
        ALL_DEVICES_FLAG = 3
    }
    /**
     * Enumerates the audio device types by usage.
     *
     * @syscap SystemCapability.Multimedia.Audio.Device
     * @since 12
     */
    enum DeviceUsage {
        /**
         * Media output device.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 12
         */
        MEDIA_OUTPUT_DEVICES = 1,
        /**
         * Media input device.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 12
         */
        MEDIA_INPUT_DEVICES = 2,
        /**
         * All media devices.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 12
         */
        ALL_MEDIA_DEVICES = 3,
        /**
         * Call output device.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 12
         */
        CALL_OUTPUT_DEVICES = 4,
        /**
         * Call input device.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 12
         */
        CALL_INPUT_DEVICES = 8,
        /**
         * All call devices.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 12
         */
        ALL_CALL_DEVICES = 12
    }
    /**
     * Enumerates the device roles.
     *
     * @syscap SystemCapability.Multimedia.Audio.Device
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 7
     */
    enum DeviceRole {
        /**
         * Input role.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 7
         */
        INPUT_DEVICE = 1,
        /**
         * Output role.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 7
         */
        OUTPUT_DEVICE = 2
    }
    /**
     * Enumerates the device types.
     *
     * @syscap SystemCapability.Multimedia.Audio.Device
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 7
     */
    enum DeviceType {
        /**
         * Invalid device.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 7
         */
        INVALID = 0,
        /**
         * Built-in earpiece.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 7
         */
        EARPIECE = 1,
        /**
         * Built-in speaker.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 7
         */
        SPEAKER = 2,
        /**
         * Wired headset with a microphone.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 7
         */
        WIRED_HEADSET = 3,
        /**
         * Wired headset without a microphone.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 7
         */
        WIRED_HEADPHONES = 4,
        /**
         * Bluetooth device using Synchronous Connection Oriented (SCO) links.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 7
         */
        BLUETOOTH_SCO = 7,
        /**
         * Bluetooth device using Advanced Audio Distribution Profile (A2DP) links.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 7
         */
        BLUETOOTH_A2DP = 8,
        /**
         * Built-in microphone.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 7
         */
        MIC = 15,
        /**
         * USB Type-C headset.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 7
         */
        USB_HEADSET = 22,
        /**
         * Display port (DP), which is used to connect to external devices.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @atomicservice
         * @since 12
         */
        DISPLAY_PORT = 23,
        /**
         * Remote cast device.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @atomicservice
         * @since 12
         */
        REMOTE_CAST = 24,
        /**
         * USB device (excluding USB headsets).
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 18
         */
        USB_DEVICE = 25,
        /**
         * HDMI device (such as HDMI, ARC, and eARC).
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 19
         */
        HDMI = 27,
        /**
         * Wired digital device (such as S/PDIF)
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 19
         */
        LINE_DIGITAL = 28,
        /**
         * Distributed device.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @atomicservice
         * @since 18
         */
        REMOTE_DAUDIO = 29,
        /**
         * Hearing aid audio device.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 20
         */
        /**
         * Hearing aid audio device.
         * Note: This original device type can be obtained after it is declared via
         *     {@link AudioRoutingManager#declareDeviceTypesCompatibility}.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 26.0.0
         */
        HEARING_AID = 30,
        /**
         * Nearlink device.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 20
         */
        /**
         * Nearlink device.
         * Note: This original device type can be obtained after it is declared via
         *     {@link AudioRoutingManager#declareDeviceTypesCompatibility}.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 26.0.0
         */
        NEARLINK = 31,
        /**
         * System private device. (This device is a private device within the system, and applications can ignore it.)
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 22
         */
        SYSTEM_PRIVATE = 200,
        /**
         * Default device type.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        DEFAULT = 1000
    }
    /**
     * Defines the device type array.
     *
     * @syscap SystemCapability.Multimedia.Audio.Device
     * @stagemodelonly
     * @since 26.0.0
     */
    type DeviceTypeArray = Array<DeviceType>;
    /**
     * Enumerates the active device types.
     *
     * @syscap SystemCapability.Multimedia.Audio.Device
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.multimedia.audio.CommunicationDeviceType
     */
    enum ActiveDeviceType {
        /**
         * Speaker.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.multimedia.audio.CommunicationDeviceType.SPEAKER
         */
        SPEAKER = 2,
        /**
         * Bluetooth device using Synchronous Connection Oriented (SCO) links.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.multimedia.audio.DeviceType#BLUETOOTH_SCO
         */
        BLUETOOTH_SCO = 7
    }
    /**
     * Enumerates the available device types for communication.
     * @enum { number }
     * @syscap SystemCapability.Multimedia.Audio.Communication
     * @since 9
     */
    /**
     * Enumerates the available device types for communication.
     * @enum { number }
     * @syscap SystemCapability.Multimedia.Audio.Communication
     * @crossplatform
     * @since 12
     */
    enum CommunicationDeviceType {
        /**
         * Speaker.
         * @syscap SystemCapability.Multimedia.Audio.Communication
         * @since 9
         */
        /**
         * Speaker.
         * @syscap SystemCapability.Multimedia.Audio.Communication
         * @crossplatform
         * @since 12
         */
        SPEAKER = 2
    }
    /**
     * Enumerates the audio ring modes.
     *
     * @syscap SystemCapability.Multimedia.Audio.Communication
     * @crossplatform [since 12]
     * @since 7
     */
    enum AudioRingMode {
        /**
         * Silent mode.
         *
         * @syscap SystemCapability.Multimedia.Audio.Communication
         * @crossplatform [since 12]
         * @since 7
         */
        RINGER_MODE_SILENT = 0,
        /**
         * Vibration mode.
         *
         * @syscap SystemCapability.Multimedia.Audio.Communication
         * @crossplatform [since 12]
         * @since 7
         */
        RINGER_MODE_VIBRATE = 1,
        /**
         * Normal mode.
         *
         * @syscap SystemCapability.Multimedia.Audio.Communication
         * @crossplatform [since 12]
         * @since 7
         */
        RINGER_MODE_NORMAL = 2
    }
    /**
     * Enumerates the audio sample formats.
     *
     * @syscap SystemCapability.Multimedia.Audio.Core
     * @crossplatform [since 12]
     * @since 8
     */
    enum AudioSampleFormat {
        /**
         * Invalid format.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 8
         */
        SAMPLE_FORMAT_INVALID = -1,
        /**
         * Unsigned 8-bit integer.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 8
         */
        SAMPLE_FORMAT_U8 = 0,
        /**
         * Signed 16-bit integer, little endian.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 8
         */
        SAMPLE_FORMAT_S16LE = 1,
        /**
         * Signed 24-bit integer, little endian.
         *
         * Due to system restrictions, only some devices support this sampling format.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 8
         */
        SAMPLE_FORMAT_S24LE = 2,
        /**
         * Signed 32-bit integer, little endian.
         *
         * Due to system restrictions, only some devices support this sampling format.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 8
         */
        SAMPLE_FORMAT_S32LE = 3,
        /**
         * Signed 32-bit floating-point number, little endian.
         *
         * Due to system restrictions, only some devices support this sampling format.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 9
         */
        SAMPLE_FORMAT_F32LE = 4
    }
    /**
     * Enumerates the audio channels.
     *
     * @syscap SystemCapability.Multimedia.Audio.Core
     * @crossplatform [since 12]
     * @since 8
     */
    enum AudioChannel {
        /**
         * One audio channel (mono).
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 8
         */
        CHANNEL_1 = 1,
        /**
         * Two audio channels (stereo).
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 8
         */
        CHANNEL_2 = 2,
        /**
         * Three audio channels.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 11
         */
        CHANNEL_3 = 3,
        /**
         * Four audio channels.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 11
         */
        CHANNEL_4 = 4,
        /**
         * Five audio channels.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 11
         */
        CHANNEL_5 = 5,
        /**
         * Six audio channels.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 11
         */
        CHANNEL_6 = 6,
        /**
         * Seven audio channels.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 11
         */
        CHANNEL_7 = 7,
        /**
         * Eight audio channels.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 11
         */
        CHANNEL_8 = 8,
        /**
         * Nine audio channels.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 11
         */
        CHANNEL_9 = 9,
        /**
         * Ten audio channels.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 11
         */
        CHANNEL_10 = 10,
        /**
         * Twelve audio channels.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 11
         */
        CHANNEL_12 = 12,
        /**
         * Fourteen audio channels.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 11
         */
        CHANNEL_14 = 14,
        /**
         * Sixteen audio channels.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 11
         */
        CHANNEL_16 = 16
    }
    /**
     * Enumerates the audio sampling rates. The sampling rates supported vary according to the device in use.
     *
     * @syscap SystemCapability.Multimedia.Audio.Core
     * @crossplatform [since 12]
     * @since 8
     */
    enum AudioSamplingRate {
        /**
         * The sampling rate is 8000.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 8
         */
        SAMPLE_RATE_8000 = 8000,
        /**
         * The sampling rate is 11025.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 8
         */
        SAMPLE_RATE_11025 = 11025,
        /**
         * The sampling rate is 12000.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 8
         */
        SAMPLE_RATE_12000 = 12000,
        /**
         * The sampling rate is 16000.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 8
         */
        SAMPLE_RATE_16000 = 16000,
        /**
         * The sampling rate is 22050.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 8
         */
        SAMPLE_RATE_22050 = 22050,
        /**
         * The sampling rate is 24000.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 8
         */
        SAMPLE_RATE_24000 = 24000,
        /**
         * The sampling rate is 32000.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 8
         */
        SAMPLE_RATE_32000 = 32000,
        /**
         * The sampling rate is 44100.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 8
         */
        SAMPLE_RATE_44100 = 44100,
        /**
         * The sampling rate is 48000.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 8
         */
        SAMPLE_RATE_48000 = 48000,
        /**
         * The sampling rate is 64000.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 8
         */
        SAMPLE_RATE_64000 = 64000,
        /**
         * The sampling rate is 88200.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 12
         */
        SAMPLE_RATE_88200 = 88200,
        /**
         * The sampling rate is 96000.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 8
         */
        SAMPLE_RATE_96000 = 96000,
        /**
         * The sampling rate is 176400.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 12
         */
        SAMPLE_RATE_176400 = 176400,
        /**
         * The sampling rate is 192000.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 12
         */
        SAMPLE_RATE_192000 = 192000,
        /**
         * The sampling rate is 384000.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        SAMPLE_RATE_384000 = 384000
    }
    /**
     * Enumerates the audio encoding types.
     *
     * @syscap SystemCapability.Multimedia.Audio.Core
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 8
     */
    enum AudioEncodingType {
        /**
         * Invalid.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 8
         */
        ENCODING_TYPE_INVALID = -1,
        /**
         * PCM encoding.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 8
         */
        ENCODING_TYPE_RAW = 0
    }
    /**
     * Enumerates the audio content types.
     *
     * @syscap SystemCapability.Multimedia.Audio.Core
     * @since 7
     * @deprecated since 10
     * @useinstead ohos.multimedia.audio.StreamUsage
     */
    enum ContentType {
        /**
         * Unknown content.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 7
         * @deprecated since 10
         * @useinstead ohos.multimedia.audio.StreamUsage.STREAM_USAGE_UNKNOWN
         */
        CONTENT_TYPE_UNKNOWN = 0,
        /**
         * Speech.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 7
         * @deprecated since 10
         * @useinstead ohos.multimedia.audio.StreamUsage.STREAM_USAGE_VOICE_COMMUNICATION
         */
        CONTENT_TYPE_SPEECH = 1,
        /**
         * Music.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 7
         * @deprecated since 10
         * @useinstead ohos.multimedia.audio.StreamUsage.STREAM_USAGE_MUSIC
         */
        CONTENT_TYPE_MUSIC = 2,
        /**
         * Movie.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 7
         * @deprecated since 10
         * @useinstead ohos.multimedia.audio.StreamUsage.STREAM_USAGE_MOVIE
         */
        CONTENT_TYPE_MOVIE = 3,
        /**
         * Notification tone.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 7
         * @deprecated since 10
         * @useinstead ohos.multimedia.audio.StreamUsage.STREAM_USAGE_NOTIFICATION
         */
        CONTENT_TYPE_SONIFICATION = 4,
        /**
         * Ringtone.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 8
         * @deprecated since 10
         * @useinstead ohos.multimedia.audio.StreamUsage.STREAM_USAGE_RINGTONE
         */
        CONTENT_TYPE_RINGTONE = 5
    }
    /**
     * Enumerates the types of audio streams played.
     *
     * @syscap SystemCapability.Multimedia.Audio.Core
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 7
     */
    enum StreamUsage {
        /**
         * Unknown content.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 7
         */
        STREAM_USAGE_UNKNOWN = 0,
        /**
         * Media.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 7
         * @deprecated since 10
         * @useinstead ohos.multimedia.audio.StreamUsage.STREAM_USAGE_MUSIC or
         *             ohos.multimedia.audio.StreamUsage.STREAM_USAGE_MOVIE or
         *             ohos.multimedia.audio.StreamUsage.STREAM_USAGE_GAME or
         *             ohos.multimedia.audio.StreamUsage.STREAM_USAGE_AUDIOBOOK
         */
        STREAM_USAGE_MEDIA = 1,
        /**
         * Music.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 10
         */
        STREAM_USAGE_MUSIC = 1,
        /**
         * VoIP voice call. (The 3A algorithm is enabled when this stream starts.)
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 7
         */
        STREAM_USAGE_VOICE_COMMUNICATION = 2,
        /**
         * Voice assistant.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        STREAM_USAGE_VOICE_ASSISTANT = 3,
        /**
         * Audio stream for alarming.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 10
         */
        STREAM_USAGE_ALARM = 4,
        /**
         * Voice message.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @atomicservice [since 12]
         * @since 10
         */
        STREAM_USAGE_VOICE_MESSAGE = 5,
        /**
         * Notification or ringtone usage.
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 7
         * @deprecated since 10
         * @useinstead ohos.multimedia.audio.StreamUsage#STREAM_USAGE_RINGTONE
         */
        STREAM_USAGE_NOTIFICATION_RINGTONE = 6,
        /**
         * Ringtone.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 10
         */
        STREAM_USAGE_RINGTONE = 6,
        /**
         * Notification.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 10
         */
        STREAM_USAGE_NOTIFICATION = 7,
        /**
         * Accessibility.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 10
         */
        STREAM_USAGE_ACCESSIBILITY = 8,
        /**
         * Movie or video.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 10
         */
        STREAM_USAGE_MOVIE = 10,
        /**
         * Gaming.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 10
         */
        STREAM_USAGE_GAME = 11,
        /**
         * Audiobooks (including crosstalks and storytelling), news radio, and podcasts.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 10
         */
        STREAM_USAGE_AUDIOBOOK = 12,
        /**
         * Navigation.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 10
         */
        STREAM_USAGE_NAVIGATION = 13,
        /**
         * VoIP video call. (The 3A algorithm is enabled when this stream starts.)
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @atomicservice
         * @since 12
         */
        STREAM_USAGE_VIDEO_COMMUNICATION = 17
    }
    /**
     * Describes audio stream information.
     *
     * @syscap SystemCapability.Multimedia.Audio.Core
     * @crossplatform [since 12]
     * @since 8
     */
    interface AudioStreamInfo {
        /**
         * Audio sampling rate.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @FaAndStageModel [since 26.0.0]
         * @crossplatform [since 12]
         * @since 8
         */
        samplingRate: AudioSamplingRate | number;
        /**
         * Number of audio channels.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 8
         */
        channels: AudioChannel;
        /**
         * Audio sample format.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 8
         */
        sampleFormat: AudioSampleFormat;
        /**
         * Audio encoding type.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 8
         */
        encodingType: AudioEncodingType;
        /**
         * Audio channel layout. The default value is **0x0**.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 11
         */
        channelLayout?: AudioChannelLayout;
    }
    /**
     * Describes audio renderer information.
     *
     * @syscap SystemCapability.Multimedia.Audio.Core
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 8
     */
    interface AudioRendererInfo {
        /**
         * Audio content type.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 8
         * @deprecated since 10
         * @useinstead ohos.multimedia.audio.AudioRendererInfo#usage
         */
        content?: ContentType;
        /**
         * Audio stream usage.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 8
         */
        usage: StreamUsage;
        /**
         * Flags that control the renderer behavior.
         *
         * Set this parameter to **0**.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 8
         */
        rendererFlags: number;
        /**
         * Audio volume mode config. If volumeMode is set to {@link AudioVolumeMode.APP_INDIVIDUAL}, this audio renderer
         * will be affected by app volume percentage set by {@link setAppVolumePercentage}
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @since 19
         */
        volumeMode?: AudioVolumeMode;
    }
    /**
     * Describes audio renderer configurations.
     *
     * @syscap SystemCapability.Multimedia.Audio.Renderer
     * @crossplatform [since 12]
     * @since 8
     */
    interface AudioRendererOptions {
        /**
         * Describes audio stream information.
         *
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 8
         */
        streamInfo: AudioStreamInfo;
        /**
         * Describes audio renderer information.
         *
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 8
         */
        rendererInfo: AudioRendererInfo;
        /**
         * Whether the audio stream can be recorded by other applications. The default value is **0**.
         *
         * @syscap SystemCapability.Multimedia.Audio.PlaybackCapture
         * @crossplatform [since 12]
         * @since 10
         */
        privacyType?: AudioPrivacyType;
    }
    /**
     * Enumerates whether an audio stream can be recorded by other applications.
     *
     * @syscap SystemCapability.Multimedia.Audio.PlaybackCapture
     * @crossplatform [since 12]
     * @since 10
     */
    enum AudioPrivacyType {
        /**
         * The audio stream can be recorded or screen-projected by other applications and is not privacy-related.
         *
         * @syscap SystemCapability.Multimedia.Audio.PlaybackCapture
         * @crossplatform [since 12]
         * @since 10
         */
        PRIVACY_TYPE_PUBLIC = 0,
        /**
         * The audio stream cannot be recorded or screen-projected by other applications.
         *
         * @syscap SystemCapability.Multimedia.Audio.PlaybackCapture
         * @crossplatform [since 12]
         * @since 10
         */
        PRIVACY_TYPE_PRIVATE = 1,
        /**
         * The audio stream can be recorded or screen-projected by other applications and is privacy-related.
         *
         * For example, if the privacy policy is **PRIVACY_TYPE_PUBLIC**, audio streams of the
         * [STREAM_USAGE_VOICE_COMMUNICATION]{@link audio.StreamUsage} type cannot be recorded or screen-projected by other
         * applications.
         *
         * However, if the privacy policy is **PRIVACY_TYPE_SHARED**, these audio streams can be recorded or screen-
         * projected by other applications.
         *
         * @syscap SystemCapability.Multimedia.Audio.PlaybackCapture
         * @since 21
         */
        PRIVACY_TYPE_SHARED = 2
    }
    /**
     * Enumerates the audio interruption modes.
     *
     * @syscap SystemCapability.Multimedia.Audio.Interrupt
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 9
     */
    enum InterruptMode {
        /**
         * Mode that different stream share one interrupt unit.
         *
         * @syscap SystemCapability.Multimedia.Audio.Interrupt
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        SHARE_MODE = 0,
        /**
         * Mode that each stream has independent interrupt unit.
         *
         * @syscap SystemCapability.Multimedia.Audio.Interrupt
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        INDEPENDENT_MODE = 1
    }
    /**
     * Enumerates the audio renderer rates.
     *
     * @syscap SystemCapability.Multimedia.Audio.Renderer
     * @since 8
     */
    enum AudioRendererRate {
        /**
         * Normal rate.
         *
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @since 8
         */
        RENDER_RATE_NORMAL = 0,
        /**
         * Double rate.
         *
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @since 8
         */
        RENDER_RATE_DOUBLE = 1,
        /**
         * 0.5x rate.
         *
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @since 8
         */
        RENDER_RATE_HALF = 2
    }
    /**
     * Enumerates the audio interruption types.
     *
     * @syscap SystemCapability.Multimedia.Audio.Renderer
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 7
     */
    enum InterruptType {
        /**
         * Audio interruption started.
         *
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 7
         */
        INTERRUPT_TYPE_BEGIN = 1,
        /**
         * Audio interruption ended.
         *
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 7
         */
        INTERRUPT_TYPE_END = 2
    }
    /**
     * Enumerates the hints provided along with audio interruption.
     *
     * The hint is obtained when an [InterruptEvent]{@link @ohos.multimedia.audio:audio.InterruptEvent} is received.
     *
     * The hint specifies the operation (such as audio pause or volume adjustment) to be performed on audio streams based
     * on the focus strategy.
     *
     * You can determine whether the operation is forcibly performed by the system based on
     * [InterruptForceType]{@link audio.InterruptForceType} in **InterruptEvent**. For details, see
     * [Introduction to Audio Focus](docroot://media/audio/audio-playback-concurrency.md).
     *
     * @syscap SystemCapability.Multimedia.Audio.Renderer
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 7
     */
    enum InterruptHint {
        /**
         * None.
         *
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @atomicservice [since 12]
         * @since 8
         */
        INTERRUPT_HINT_NONE = 0,
        /**
         * A hint is displayed, indicating that the audio stream is restored. The application can proactively trigger
         * operations related to rendering or recording.
         *
         * This operation cannot be forcibly performed by the system, and the corresponding
         * [InterruptForceType]{@link audio.InterruptForceType} must be **INTERRUPT_SHARE**.
         *
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 7
         */
        INTERRUPT_HINT_RESUME = 1,
        /**
         * A hint is displayed, indicating that the audio stream is paused and the audio focus is lost temporarily.
         *
         * When the audio focus is available, the **INTERRUPT_HINT_RESUME** event is received.
         *
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @atomicservice [since 12]
         * @since 7
         */
        INTERRUPT_HINT_PAUSE = 2,
        /**
         * A hint is displayed, indicating that the audio stream stops and the audio focus is lost.
         *
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @atomicservice [since 12]
         * @since 7
         */
        INTERRUPT_HINT_STOP = 3,
        /**
         * A hint is displayed, indicating that audio ducking starts and the audio is played at a lower volume.
         *
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @atomicservice [since 12]
         * @since 7
         */
        INTERRUPT_HINT_DUCK = 4,
        /**
         * A hint is displayed, indicating that audio ducking ends and the audio is played at the normal volume.
         *
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @atomicservice [since 12]
         * @since 8
         */
        INTERRUPT_HINT_UNDUCK = 5,
        /**
         * A hint is displayed, indicating that the audio is muted.
         *
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @since 20
         */
        INTERRUPT_HINT_MUTE = 6,
        /**
         * A hint is displayed, indicating that the audio is unmuted.
         *
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @since 20
         */
        INTERRUPT_HINT_UNMUTE = 7
    }
    /**
     * Enumerates the types of force that causes audio interruption.
     *
     * The force type is obtained when an [InterruptEvent]{@link @ohos.multimedia.audio:audio.InterruptEvent} is received.
     *
     * This type specifies whether audio interruption is forcibly performed by the system. The operation information (such
     * as audio pause or stop) can be obtained through [InterruptHint]{@link audio.InterruptHint}. For details about the
     * audio interruption policy, see [Introduction to Audio Focus](docroot://media/audio/audio-playback-concurrency.md).
     *
     * @syscap SystemCapability.Multimedia.Audio.Renderer
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 9
     */
    enum InterruptForceType {
        /**
         * The operation is forcibly performed by the system.
         *
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        INTERRUPT_FORCE = 0,
        /**
         * The operation will not be performed by the system. [InterruptHint]{@link audio.InterruptHint} is used to provide
         * recommended operations for the application, and the application can determine the next processing mode.
         *
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @atomicservice [since 12]
         * @since 9
         */
        INTERRUPT_SHARE = 1
    }
    /**
     * Describes the interruption event received by the application when the audio is interrupted.
     *
     * @syscap SystemCapability.Multimedia.Audio.Renderer
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 9
     */
    interface InterruptEvent {
        /**
         * Whether the audio interruption has started or ended.
         *
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        eventType: InterruptType;
        /**
         * Whether the audio interruption is forcibly taken by the system or taken by an application.
         *
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        forceType: InterruptForceType;
        /**
         * Hint provided along the interruption to provide information related to the interruption event.
         *
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        hintType: InterruptHint;
    }
    /**
     * Enumerates the returned event types for audio interruption events.
     *
     * @syscap SystemCapability.Multimedia.Audio.Renderer
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.multimedia.audio.InterruptType
     */
    enum InterruptActionType {
        /**
         * Focus gain event.
         *
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.multimedia.audio.InterruptType#INTERRUPT_TYPE_BEGIN
         */
        TYPE_ACTIVATED = 0,
        /**
         * Audio interruption event.
         *
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.multimedia.audio.InterruptType#INTERRUPT_TYPE_END
         */
        TYPE_INTERRUPT = 1
    }
    /**
     * Enumerates the device connection statuses.
     *
     * @syscap SystemCapability.Multimedia.Audio.Device
     * @crossplatform [since 12]
     * @since 7
     */
    enum DeviceChangeType {
        /**
         * Connected.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @since 7
         */
        CONNECT = 0,
        /**
         * Disconnected.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @since 7
         */
        DISCONNECT = 1
    }
    /**
     * Enumerates the audio scenes.
     *
     * @syscap SystemCapability.Multimedia.Audio.Communication
     * @crossplatform [since 12]
     * @since 8
     */
    enum AudioScene {
        /**
         * Default audio scene.
         *
         * @syscap SystemCapability.Multimedia.Audio.Communication
         * @crossplatform [since 12]
         * @since 8
         */
        AUDIO_SCENE_DEFAULT = 0,
        /**
         * Ringing audio scene.
         *
         * @syscap SystemCapability.Multimedia.Audio.Communication
         * @since 12
         */
        AUDIO_SCENE_RINGING = 1,
        /**
         * Phone call audio scene.
         *
         * @syscap SystemCapability.Multimedia.Audio.Communication
         * @since 12
         */
        AUDIO_SCENE_PHONE_CALL = 2,
        /**
         * Voice chat audio scene.
         *
         * @syscap SystemCapability.Multimedia.Audio.Communication
         * @crossplatform [since 12]
         * @since 8
         */
        AUDIO_SCENE_VOICE_CHAT = 3
    }
    /**
     * This interface implements audio volume and device management.
     *
     * Before calling any API in AudioManager, you must use
     * [getAudioManager]{@link @ohos.multimedia.audio:audio.getAudioManager} to obtain an AudioManager instance.
     *
     * @syscap SystemCapability.Multimedia.Audio.Core
     * @crossplatform [since 12]
     * @atomicservice [since 23]
     * @since 7
     */
    interface AudioManager {
        /**
         * Sets the volume for a volume type. This method uses an asynchronous callback to return the result.
         * @permission ohos.permission.ACCESS_NOTIFICATION_POLICY
         * @param { AudioVolumeType } volumeType - Audio volume type.
         * @param { number } volume - Volume to set. The value range can be obtained by calling getMinVolume and getMaxVolume.
         * @param { AsyncCallback<void> } callback - Callback used to return the result.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.multimedia.avVolumePanel.AVVolumePanel
         */
        setVolume(volumeType: AudioVolumeType, volume: number, callback: AsyncCallback<void>): void;
        /**
         * Sets the volume for a volume type. This method uses a promise to return the result.
         * @permission ohos.permission.ACCESS_NOTIFICATION_POLICY
         * @param { AudioVolumeType } volumeType - Audio volume type.
         * @param { number } volume - Volume to set. The value range can be obtained by calling getMinVolume and getMaxVolume.
         * @returns { Promise<void> } Promise used to return the result.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.multimedia.avVolumePanel.AVVolumePanel
         */
        setVolume(volumeType: AudioVolumeType, volume: number): Promise<void>;
        /**
         * Obtains the volume of a stream. This API uses an asynchronous callback to return the result.
         *
         * @param { AudioVolumeType } volumeType - Audio volume type.
         * @param { AsyncCallback<number> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **data** is the stream volume obtained; otherwise, **err** is an error object.
         *     The volume range of a specified stream can be obtained by calling
         *     [getMinVolume]{@link audio.AudioManager.getMinVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>)}
         *     and
         *     [getMaxVolume]{@link audio.AudioManager.getMaxVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>)}
         *     .
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.multimedia.audio.AudioVolumeGroupManager#getVolume
         */
        getVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void;
        /**
         * Obtains the volume of a stream. This API uses a promise to return the result.
         *
         * @param { AudioVolumeType } volumeType - Audio volume type.
         * @returns { Promise<number> } Promise used to return the volume of the stream. The volume range of a specified
         *     stream can be obtained by calling
         *     [getMinVolume]{@link audio.AudioManager.getMinVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>)}
         *     and
         *     [getMaxVolume]{@link audio.AudioManager.getMaxVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>)}
         *     .
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.multimedia.audio.AudioVolumeGroupManager#getVolume
         */
        getVolume(volumeType: AudioVolumeType): Promise<number>;
        /**
         * Obtains the minimum volume allowed for a stream. This API uses an asynchronous callback to return the result.
         *
         * @param { AudioVolumeType } volumeType - Audio volume type.
         * @param { AsyncCallback<number> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **data** is the minimum stream volume obtained; otherwise, **err** is an error
         *     object.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.multimedia.audio.AudioVolumeGroupManager#getMinVolume
         */
        getMinVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void;
        /**
         * Obtains the minimum volume allowed for a stream. This API uses a promise to return the result.
         *
         * @param { AudioVolumeType } volumeType - Audio volume type.
         * @returns { Promise<number> } Promise used to return the minimum volume.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.multimedia.audio.AudioVolumeGroupManager#getMinVolume
         */
        getMinVolume(volumeType: AudioVolumeType): Promise<number>;
        /**
         * Obtains the maximum volume allowed for a stream. This API uses an asynchronous callback to return the result.
         *
         * @param { AudioVolumeType } volumeType - Audio volume type.
         * @param { AsyncCallback<number> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **data** is the maximum stream volume obtained; otherwise, **err** is an error
         *     object.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.multimedia.audio.AudioVolumeGroupManager#getMaxVolume
         */
        getMaxVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void;
        /**
         * Obtains the maximum volume allowed for a stream. This API uses a promise to return the result.
         *
         * @param { AudioVolumeType } volumeType - Audio volume type.
         * @returns { Promise<number> } Promise used to return the maximum volume.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.multimedia.audio.AudioVolumeGroupManager#getMaxVolume
         */
        getMaxVolume(volumeType: AudioVolumeType): Promise<number>;
        /**
         * Obtains the audio devices with a specific flag. This API uses an asynchronous callback to return the result.
         *
         * @param { DeviceFlag } deviceFlag - Audio device flag.
         * @param { AsyncCallback<AudioDeviceDescriptors> } callback - Callback used to return the result. If the operation
         *     is successful, **err** is **undefined** and **data** is the audio devices obtained; otherwise, **err** is an
         *     error object.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.multimedia.audio.AudioRoutingManager#getDevices
         */
        getDevices(deviceFlag: DeviceFlag, callback: AsyncCallback<AudioDeviceDescriptors>): void;
        /**
         * Obtains the audio devices with a specific flag. This API uses a promise to return the result.
         *
         * @param { DeviceFlag } deviceFlag - Audio device flag.
         * @returns { Promise<AudioDeviceDescriptors> } Promise used to return the device list.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.multimedia.audio.AudioRoutingManager#getDevices
         */
        getDevices(deviceFlag: DeviceFlag): Promise<AudioDeviceDescriptors>;
        /**
         * Mutes a volume type. This method uses an asynchronous callback to return the result.
         * @param { AudioVolumeType } volumeType - Audio volume type.
         * @param { boolean } mute - Mute status to set. The value true means to mute the volume type, and false means the opposite.
         * @param { AsyncCallback<void> } callback - Callback used to return the result.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.multimedia.avVolumePanel.AVVolumePanel
         */
        mute(volumeType: AudioVolumeType, mute: boolean, callback: AsyncCallback<void>): void;
        /**
         * Mutes a volume type. This method uses a promise to return the result.
         * @param { AudioVolumeType } volumeType - Audio volume type.
         * @param { boolean } mute -  Mute status to set. The value true means to mute the volume type, and false means the opposite.
         * @returns { Promise<void> } Promise used to return the result.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.multimedia.avVolumePanel.AVVolumePanel
         */
        mute(volumeType: AudioVolumeType, mute: boolean): Promise<void>;
        /**
         * Checks whether a stream is muted. This API uses an asynchronous callback to return the result.
         *
         * @param { AudioVolumeType } volumeType - Audio volume type.
         * @param { AsyncCallback<boolean> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **data** is **true** if the stream is muted or **false** if not muted; otherwise
         *     , **err** is an error object.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.multimedia.audio.AudioVolumeGroupManager#isMute
         */
        isMute(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void;
        /**
         * Checks whether a stream is muted. This API uses a promise to return the result.
         *
         * @param { AudioVolumeType } volumeType - Audio volume type.
         * @returns { Promise<boolean> } Promise used to return the result, indicating whether the stream is muted. **true**
         *     if muted, **false** otherwise.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.multimedia.audio.AudioVolumeGroupManager#isMute
         */
        isMute(volumeType: AudioVolumeType): Promise<boolean>;
        /**
         * Checks whether a stream is active. This API uses an asynchronous callback to return the result.
         *
         * @param { AudioVolumeType } volumeType - Audio volume type.
         * @param { AsyncCallback<boolean> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **data** is **true** if the stream is active or **false** if not active;
         *     otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.multimedia.audio.AudioStreamManager#isActive
         */
        isActive(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void;
        /**
         * Checks whether a stream is active. This API uses a promise to return the result.
         *
         * @param { AudioVolumeType } volumeType - Audio volume type.
         * @returns { Promise<boolean> } Promise used to return the result, indicating whether the stream is active.
         *     **true** if active, **false** otherwise.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.multimedia.audio.AudioStreamManager#isActive
         */
        isActive(volumeType: AudioVolumeType): Promise<boolean>;
        /**
         * Mutes or unmutes the microphone. This method uses an asynchronous callback to return the result.
         * @permission ohos.permission.MICROPHONE
         * @param { boolean } mute - Mute status to set. The value true means to mute the microphone, and false means the opposite.
         * @param { AsyncCallback<void> } callback - Callback used to return the result.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 7
         * @deprecated since 9
         */
        setMicrophoneMute(mute: boolean, callback: AsyncCallback<void>): void;
        /**
         * Mutes or unmutes the microphone. This method uses a promise to return the result.
         * @permission ohos.permission.MICROPHONE
         * @param { boolean } mute - Mute status to set. The value true means to mute the microphone, and false means the opposite.
         * @returns { Promise<void> } Promise used to return the result.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 7
         * @deprecated since 9
         */
        setMicrophoneMute(mute: boolean): Promise<void>;
        /**
         * Checks whether the microphone is muted. This API uses an asynchronous callback to return the result.
         *
         * @permission ohos.permission.MICROPHONE
         * @param { AsyncCallback<boolean> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **data** is **true** if the microphone is muted or **false** if not muted;
         *     otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.multimedia.audio.AudioVolumeGroupManager#isMicrophoneMute
         */
        isMicrophoneMute(callback: AsyncCallback<boolean>): void;
        /**
         * Checks whether the microphone is muted. This API uses a promise to return the result.
         *
         * @permission ohos.permission.MICROPHONE
         * @returns { Promise<boolean> } Promise used to return the result, indicating whether the microphone is muted.
         *     **true** if muted, **false** otherwise.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.multimedia.audio.AudioVolumeGroupManager#isMicrophoneMute
         */
        isMicrophoneMute(): Promise<boolean>;
        /**
         * Sets the ringer mode. This method uses an asynchronous callback to return the result.
         * @permission ohos.permission.ACCESS_NOTIFICATION_POLICY
         * @param { AudioRingMode } mode - Ringer mode.
         * @param { AsyncCallback<void> } callback - Callback used to return the result.
         * @syscap SystemCapability.Multimedia.Audio.Communication
         * @since 7
         * @deprecated since 9
         */
        setRingerMode(mode: AudioRingMode, callback: AsyncCallback<void>): void;
        /**
         * Sets the ringer mode. This method uses a promise to return the result.
         * @permission ohos.permission.ACCESS_NOTIFICATION_POLICY
         * @param { AudioRingMode } mode - Ringer mode.
         * @returns { Promise<void> } Promise used to return the result.
         * @syscap SystemCapability.Multimedia.Audio.Communication
         * @since 7
         * @deprecated since 9
         */
        setRingerMode(mode: AudioRingMode): Promise<void>;
        /**
         * Obtains the ringer mode. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<AudioRingMode> } callback - Callback used to return the result. If the operation is
         *     successful, **err** is **undefined** and **data** is the ringer mode obtained; otherwise, **err** is an error
         *     object.
         * @syscap SystemCapability.Multimedia.Audio.Communication
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.multimedia.audio.AudioVolumeGroupManager#getRingerMode
         */
        getRingerMode(callback: AsyncCallback<AudioRingMode>): void;
        /**
         * Obtains the ringer mode. This API uses a promise to return the result.
         *
         * @returns { Promise<AudioRingMode> } Promise used to return the ringer mode.
         * @syscap SystemCapability.Multimedia.Audio.Communication
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.multimedia.audio.AudioVolumeGroupManager#getRingerMode
         */
        getRingerMode(): Promise<AudioRingMode>;
        /**
         * Sets an audio parameter. This method uses an asynchronous callback to return the result.
         * @permission ohos.permission.MODIFY_AUDIO_SETTINGS
         * @param { string } key - Key of the audio parameter to set.
         * @param { string } value -  Value of the audio parameter to set.
         * @param { AsyncCallback<void> } callback - Callback used to return the result.
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 7
         * @deprecated since 11
         */
        setAudioParameter(key: string, value: string, callback: AsyncCallback<void>): void;
        /**
         * Sets an audio parameter. This method uses a promise to return the result.
         * @permission ohos.permission.MODIFY_AUDIO_SETTINGS
         * @param { string } key - Key of the audio parameter to set.
         * @param { string } value - Value of the audio parameter to set.
         * @returns { Promise<void> } Promise used to return the result.
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 7
         * @deprecated since 11
         */
        setAudioParameter(key: string, value: string): Promise<void>;
        /**
         * Obtains the value of an audio parameter. This method uses an asynchronous callback to return the query result.
         * @param { string } key - Key of the audio parameter whose value is to be obtained.
         * @param { AsyncCallback<string> } callback - Callback used to return the value of the audio parameter.
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 7
         * @deprecated since 11
         */
        getAudioParameter(key: string, callback: AsyncCallback<string>): void;
        /**
         * Obtains the value of an audio parameter. This method uses a promise to return the query result.
         * @param { string } key - Key of the audio parameter whose value is to be obtained.
         * @returns { Promise<string> } Promise used to return the value of the audio parameter.
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 7
         * @deprecated since 11
         */
        getAudioParameter(key: string): Promise<string>;
        /**
         * Sets a device to the active state. This API uses an asynchronous callback to return the result.
         *
         * @param { ActiveDeviceType } deviceType - Active audio device type.
         * @param { boolean } active - Active state to set. **true** to set the device to the active state, **false**
         *     otherwise.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.multimedia.audio.AudioRoutingManager#setCommunicationDevice
         */
        setDeviceActive(deviceType: ActiveDeviceType, active: boolean, callback: AsyncCallback<void>): void;
        /**
         * Sets a device to the active state. This API uses a promise to return the result.
         *
         * @param { ActiveDeviceType } deviceType - Active audio device type.
         * @param { boolean } active - Active state to set. **true** to set the device to the active state, **false**
         *     otherwise.
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.multimedia.audio.AudioRoutingManager#setCommunicationDevice
         */
        setDeviceActive(deviceType: ActiveDeviceType, active: boolean): Promise<void>;
        /**
         * Checks whether a device is active. This API uses an asynchronous callback to return the result.
         *
         * @param { ActiveDeviceType } deviceType - Active audio device type.
         * @param { AsyncCallback<boolean> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **data** is **true** if the device is active or **false** if not active;
         *     otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.multimedia.audio.AudioRoutingManager#isCommunicationDeviceActive
         */
        isDeviceActive(deviceType: ActiveDeviceType, callback: AsyncCallback<boolean>): void;
        /**
         * Checks whether a device is active. This API uses a promise to return the result.
         *
         * @param { ActiveDeviceType } deviceType - Active audio device type.
         * @returns { Promise<boolean> } Promise used to return the result, indicating whether the device is active.
         *     **true** if active, **false** otherwise.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.multimedia.audio.AudioRoutingManager#isCommunicationDeviceActive
         */
        isDeviceActive(deviceType: ActiveDeviceType): Promise<boolean>;
        /**
         * Obtains the audio scene. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<AudioScene> } callback - Callback used to return the result. If the operation is
         *     successful, **err** is **undefined** and **data** is the audio scene obtained; otherwise, **err** is an error
         *     object.
         * @syscap SystemCapability.Multimedia.Audio.Communication
         * @crossplatform [since 12]
         * @since 8
         */
        getAudioScene(callback: AsyncCallback<AudioScene>): void;
        /**
         * Obtains the audio scene. This API uses a promise to return the result.
         *
         * @returns { Promise<AudioScene> } Promise used to return the audio scene.
         * @syscap SystemCapability.Multimedia.Audio.Communication
         * @crossplatform [since 12]
         * @since 8
         */
        getAudioScene(): Promise<AudioScene>;
        /**
         * Obtains the audio scene. This API returns the result synchronously.
         *
         * @returns { AudioScene } Audio scene.
         * @syscap SystemCapability.Multimedia.Audio.Communication
         * @crossplatform [since 12]
         * @since 10
         */
        getAudioSceneSync(): AudioScene;
        /**
         * Subscribes to the audio scene change event. This API uses an asynchronous callback to return the result.
         *
         * @param { 'audioSceneChange' } type - Event type. The event **'audioSceneChange'** is triggered when the audio
         *     scene is changed.
         * @param { Callback<AudioScene> } callback - Callback used to return the current audio scene.
         * @syscap SystemCapability.Multimedia.Audio.Communication
         * @since 20
         */
        on(type: 'audioSceneChange', callback: Callback<AudioScene>): void;
        /**
         * Unsubscribes from the audio scene change event. This API uses an asynchronous callback to return the result.
         *
         * @param { 'audioSceneChange' } type - Event type. The event **'audioSceneChange'** is triggered when the audio
         *     scene is changed.
         * @param { Callback<AudioScene> } [callback] - Callback used to return the current audio scene.
         * @syscap SystemCapability.Multimedia.Audio.Communication
         * @since 20
         */
        off(type: 'audioSceneChange', callback?: Callback<AudioScene>): void;
        /**
         * Subscribes to the event indicating that the connection status of an audio device is changed. This API uses an
         * asynchronous callback to return the result.
         *
         * @param { 'deviceChange' } type - Event type. The event **'deviceChange'** is triggered when the connection status
         *     of an audio device is changed.
         * @param { Callback<DeviceChangeAction> } callback - Callback used to return the device change details.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.multimedia.audio.AudioRoutingManager#event:deviceChange
         */
        on(type: 'deviceChange', callback: Callback<DeviceChangeAction>): void;
        /**
         * Unsubscribes from the audio device change event. This API uses an asynchronous callback to return the result.
         *
         * @param { 'deviceChange' } type - Event type. The event **'deviceChange'** is triggered when the connection status
         *     of an audio device is changed.
         * @param { Callback<DeviceChangeAction> } callback - Callback used to return the device change details.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.multimedia.audio.AudioRoutingManager#event:deviceChange
         */
        off(type: 'deviceChange', callback?: Callback<DeviceChangeAction>): void;
        /**
         * Subscribes to the audio interruption event, which is triggered when the audio focus is changed. This API uses an
         * asynchronous callback to return the result.
         *
         * Same as
         * [on('audioInterrupt')]{@link @ohos.multimedia.audio:audio.AudioRenderer.on(type: 'audioInterrupt', callback: Callback<InterruptEvent>)}
         * , this API is used to listen for focus changes. However, this API is used in scenarios without audio streams (no
         * AudioRenderer instance is created), such as frequency modulation (FM) and voice wakeup.
         *
         * @param { 'interrupt' } type - Event type. The event **'interrupt'** is triggered when the audio focus is changed.
         * @param { AudioInterrupt } interrupt - Audio interruption event type.
         * @param { Callback<InterruptAction> } callback - Callback used to return the event information.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @since 7
         * @deprecated since 11
         * @useinstead ohos.multimedia.audio.AudioRenderer#event:audioInterrupt
         */
        on(type: 'interrupt', interrupt: AudioInterrupt, callback: Callback<InterruptAction>): void;
        /**
         * Unsubscribes from the audio interruption event. This API uses an asynchronous callback to return the result.
         *
         * @param { 'interrupt' } type - Event type. The event **'interrupt'** is triggered when the audio focus is changed.
         * @param { AudioInterrupt } interrupt - Audio interruption event type.
         * @param { Callback<InterruptAction> } callback - Callback used to return the event information.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @since 7
         * @deprecated since 11
         * @useinstead ohos.multimedia.audio.AudioRenderer#event:audioInterrupt
         */
        off(type: 'interrupt', interrupt: AudioInterrupt, callback?: Callback<InterruptAction>): void;
        /**
         * Obtains an AudioVolumeManager instance.
         *
         * @returns { AudioVolumeManager } AudioVolumeManager instance.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @crossplatform [since 12]
         * @atomicservice [since 23]
         * @since 9
         */
        getVolumeManager(): AudioVolumeManager;
        /**
         * Obtains an AudioStreamManager instance.
         *
         * @returns { AudioStreamManager } AudioStreamManager instance.
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 9
         */
        getStreamManager(): AudioStreamManager;
        /**
         * Obtains an AudioRoutingManager instance.
         *
         * @returns { AudioRoutingManager } AudioRoutingManager instance.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @since 9
         */
        getRoutingManager(): AudioRoutingManager;
        /**
         * Obtains an AudioSessionManager instance.
         *
         * @returns { AudioSessionManager } AudioSessionManager instance.
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform
         * @atomicservice [since 26.0.0]
         * @since 12
         */
        getSessionManager(): AudioSessionManager;
        /**
         * Obtains an AudioSpatializationManager instance.
         *
         * @returns { AudioSpatializationManager } AudioSpatializationManager instance.
         * @syscap SystemCapability.Multimedia.Audio.Spatialization
         * @since 18
         */
        getSpatializationManager(): AudioSpatializationManager;
        /**
         * Obtains a device enhancement manager instance.
         *
         * @returns { AudioDeviceEnhanceManager } Returns an instance of audio device enhancement manager.
         * @syscap SystemCapability.Multimedia.Audio.DeviceEnhance
         * @stagemodelonly
         * @since 26.0.0
         */
        getDeviceEnhanceManager(): AudioDeviceEnhanceManager;
        /**
         * Obtains an AudioDebuggingManager instance.
         * <p><strong>NOTE</strong>:
         * The {@link #AudioDebuggingManager} instance is a singleton.
         * </p>
         *
         * @returns { AudioDebuggingManager } this {@link #AudioDebuggingManager} object.
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        getDebuggingManager(): AudioDebuggingManager;
        /**
         * Obtains a recording manager instance. Provides recording strategy management, including collaborative recording and recording control capabilities.
         *
         * @returns { AudioRecordingManager } Returns an instance of audio record manager.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @stagemodelonly
         * @since 26.0.0
         */
        getRecordingManager(): AudioRecordingManager;
    }
    /**
     * Enumerates the blocked statuses of audio devices.
     *
     * @syscap SystemCapability.Multimedia.Audio.Device
     * @since 13
     */
    enum DeviceBlockStatus {
        /**
         * The audio device is not blocked.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 13
         */
        UNBLOCKED = 0,
        /**
         * The audio device is blocked.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 13
         */
        BLOCKED = 1
    }
    /**
     * Describes the audio device blocked status and device information.
     *
     * @syscap SystemCapability.Multimedia.Audio.Device
     * @since 13
     */
    interface DeviceBlockStatusInfo {
        /**
         * Blocked status of the audio device.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 13
         */
        blockStatus: DeviceBlockStatus;
        /**
         * Device information.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 13
         */
        devices: AudioDeviceDescriptors;
    }
    /**
     * This interface implements audio routing management.
     *
     * Before calling any API in AudioRoutingManager, you must use
     * [getRoutingManager]{@link @ohos.multimedia.audio:audio.AudioManager.getRoutingManager} to obtain an
     * AudioRoutingManager instance.
     *
     * > **NOTE**
     * >
     * > - The initial APIs of this interface are supported since API version 9.
     *
     * @syscap SystemCapability.Multimedia.Audio.Device
     * @crossplatform [since 12]
     * @since 9
     */
    interface AudioRoutingManager {
        /**
         * Obtains the audio devices with a specific flag. This API uses an asynchronous callback to return the result.
         *
         * @param { DeviceFlag } deviceFlag - Audio device flag.
         * @param { AsyncCallback<AudioDeviceDescriptors> } callback - Callback used to return the result. If the operation
         *     is successful, **err** is **undefined** and **data** is the audio devices obtained; otherwise, **err** is an
         *     error object.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @since 9
         */
        getDevices(deviceFlag: DeviceFlag, callback: AsyncCallback<AudioDeviceDescriptors>): void;
        /**
         * Obtains the audio devices with a specific flag. This API uses a promise to return the result.
         *
         * @param { DeviceFlag } deviceFlag - Audio device flag.
         * @returns { Promise<AudioDeviceDescriptors> } Promise used to return the device list.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @since 9
         */
        getDevices(deviceFlag: DeviceFlag): Promise<AudioDeviceDescriptors>;
        /**
         * Obtains the audio devices with a specific flag. This API returns the result synchronously.
         *
         * @param { DeviceFlag } deviceFlag - Audio device flag.
         * @returns { AudioDeviceDescriptors } Device list.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @since 10
         */
        getDevicesSync(deviceFlag: DeviceFlag): AudioDeviceDescriptors;
        /**
         * Subscribes to the event indicating that the connection status of an audio device is changed. This API uses an
         * asynchronous callback to return the result.
         *
         * @param { 'deviceChange' } type - Event type. The event **'deviceChange'** is triggered when the connection status
         *     of an audio device is changed.
         * @param { DeviceFlag } deviceFlag - Audio device flag.
         * @param { Callback<DeviceChangeAction> } callback - Callback used to return the device change details.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @since 9
         */
        on(type: 'deviceChange', deviceFlag: DeviceFlag, callback: Callback<DeviceChangeAction>): void;
        /**
         * Unsubscribes from the event indicating that the connection status of an audio device is changed. This API uses an
         * asynchronous callback to return the result.
         *
         * @param { 'deviceChange' } type - Event type. The event **'deviceChange'** is triggered when the connection status
         *     of an audio device is changed.
         * @param { Callback<DeviceChangeAction> } callback - Callback used to return the device change details.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @since 9
         */
        off(type: 'deviceChange', callback?: Callback<DeviceChangeAction>): void;
        /**
         * Obtains the available audio devices. This API returns the result synchronously.
         *
         * @param { DeviceUsage } deviceUsage - Audio device type (classified by usage).
         * @returns { AudioDeviceDescriptors } Device list.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 12
         */
        getAvailableDevices(deviceUsage: DeviceUsage): AudioDeviceDescriptors;
        /**
         * Subscribes to the event indicating that the connection status of an available audio device is changed. This API
         * uses an asynchronous callback to return the result.
         *
         * @param { 'availableDeviceChange' } type - Event type. The event **'availableDeviceChange'** is triggered when the
         *     connection status of available audio devices is changed.
         * @param { DeviceUsage } deviceUsage - Audio device type (classified by usage).
         * @param { Callback<DeviceChangeAction> } callback - Callback used to return the device change details.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 12
         */
        on(type: 'availableDeviceChange', deviceUsage: DeviceUsage, callback: Callback<DeviceChangeAction>): void;
        /**
         * Unsubscribes from the event indicating that the connection status of an available audio device is changed. This
         * API uses an asynchronous callback to return the result.
         *
         * @param { 'availableDeviceChange' } type - Event type. The event **'availableDeviceChange'** is triggered when the
         *     connection status of available audio devices is changed.
         * @param { Callback<DeviceChangeAction> } callback - Callback used to return the available device change details.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 12
         */
        off(type: 'availableDeviceChange', callback?: Callback<DeviceChangeAction>): void;
        /**
         * Sets a communication device to the active state. This API uses an asynchronous callback to return the result.
         *
         * This API will be deprecated in a later version due to function design is changed. You are not advised to use it.
         *
         * You are advised to use the [AVCastPicker component](docroot://media/avsession/using-switch-call-devices.md)
         * provided by AVSession to switch between call devices.
         *
         * @param { CommunicationDeviceType } deviceType - Audio device flag.
         * @param { boolean } active - Active state to set. **true** to set the device to the active state, **false**
         *     otherwise.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Audio.Communication
         * @crossplatform [since 12]
         * @since 9
         */
        setCommunicationDevice(deviceType: CommunicationDeviceType, active: boolean, callback: AsyncCallback<void>): void;
        /**
         * Sets a communication device to the active state. This API uses a promise to return the result.
         *
         * This API will be deprecated in a later version due to function design is changed. You are not advised to use it.
         *
         * You are advised to use the [AVCastPicker component](docroot://media/avsession/using-switch-call-devices.md)
         * provided by AVSession to switch between call devices.
         *
         * @param { CommunicationDeviceType } deviceType - Active audio device type.
         * @param { boolean } active - Active state to set. **true** to set the device to the active state, **false**
         *     otherwise.
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Multimedia.Audio.Communication
         * @crossplatform [since 12]
         * @since 9
         */
        setCommunicationDevice(deviceType: CommunicationDeviceType, active: boolean): Promise<void>;
        /**
         * Checks whether a communication device is active. This API uses an asynchronous callback to return the result.
         *
         * @param { CommunicationDeviceType } deviceType - Active audio device type.
         * @param { AsyncCallback<boolean> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **data** is **true** if the device is active or **false** if not active;
         *     otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Audio.Communication
         * @crossplatform [since 12]
         * @since 9
         */
        isCommunicationDeviceActive(deviceType: CommunicationDeviceType, callback: AsyncCallback<boolean>): void;
        /**
         * Checks whether a communication device is active. This API uses a promise to return the result.
         *
         * @param { CommunicationDeviceType } deviceType - Active audio device type.
         * @returns { Promise<boolean> } Promise used to return the result, indicating whether the device is active.
         *     **true** if active, **false** otherwise.
         * @syscap SystemCapability.Multimedia.Audio.Communication
         * @crossplatform [since 12]
         * @since 9
         */
        isCommunicationDeviceActive(deviceType: CommunicationDeviceType): Promise<boolean>;
        /**
         * Checks whether a communication device is active. This API returns the result synchronously.
         *
         * @param { CommunicationDeviceType } deviceType - Active audio device type.
         * @returns { boolean } Check result for whether the device is active. **true** if active, **false** otherwise.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Communication
         * @crossplatform [since 12]
         * @since 10
         */
        isCommunicationDeviceActiveSync(deviceType: CommunicationDeviceType): boolean;
        /**
         * Obtains the output device with the highest priority based on the audio renderer information. This API uses an
         * asynchronous callback to return the result.
         *
         * @param { AudioRendererInfo } rendererInfo - Audio renderer information.
         * @param { AsyncCallback<AudioDeviceDescriptors> } callback - Callback used to return the result. If the operation
         *     is successful, **err** is **undefined** and **data** is the output device with the highest priority obtained;
         *     otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed. Return by callback.
         * @throws { BusinessError } 6800301 - System error. Return by callback.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @since 10
         */
        getPreferOutputDeviceForRendererInfo(rendererInfo: AudioRendererInfo, callback: AsyncCallback<AudioDeviceDescriptors>): void;
        /**
         * Obtains the output device with the highest priority based on the audio renderer information. This API uses a
         * promise to return the result.
         *
         * @param { AudioRendererInfo } rendererInfo - Audio renderer information.
         * @returns { Promise<AudioDeviceDescriptors> } Promise used to return the information about the output device with
         *     the highest priority.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed. Return by promise.
         * @throws { BusinessError } 6800301 - System error. Return by promise.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @since 10
         */
        getPreferOutputDeviceForRendererInfo(rendererInfo: AudioRendererInfo): Promise<AudioDeviceDescriptors>;
        /**
         * Obtains the output device with the highest priority based on the audio renderer information. This API returns the
         * result synchronously.
         *
         * @param { AudioRendererInfo } rendererInfo - Audio renderer information.
         * @returns { AudioDeviceDescriptors } Information about the output device with the highest priority.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @since 10
         */
        getPreferredOutputDeviceForRendererInfoSync(rendererInfo: AudioRendererInfo): AudioDeviceDescriptors;
        /**
         * Subscribes to the change event of the output device with the highest priority, which is triggered when the output
         * device with the highest priority is changed. This API uses an asynchronous callback to return the result.
         *
         * @param { 'preferOutputDeviceChangeForRendererInfo' } type - Event type. The event
         *     **'preferOutputDeviceChangeForRendererInfo'** is triggered when the output device with the highest priority
         *     is changed.
         * @param { AudioRendererInfo } rendererInfo - Audio renderer information.
         * @param { Callback<AudioDeviceDescriptors> } callback - Callback used to return the information about the output
         *     device with the highest priority.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @since 10
         */
        on(type: 'preferOutputDeviceChangeForRendererInfo', rendererInfo: AudioRendererInfo, callback: Callback<AudioDeviceDescriptors>): void;
        /**
         * Unsubscribes from the change event of the output device with the highest priority. This API uses an asynchronous
         * callback to return the result.
         *
         * @param { 'preferOutputDeviceChangeForRendererInfo' } type - Event type. The event
         *     **'preferOutputDeviceChangeForRendererInfo'** is triggered when the output device with the highest priority
         *     is changed.
         * @param { Callback<AudioDeviceDescriptors> } callback - Callback used to return the information about the output
         *     device with the highest priority.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @since 10
         */
        off(type: 'preferOutputDeviceChangeForRendererInfo', callback?: Callback<AudioDeviceDescriptors>): void;
        /**
         * Obtains the input device with the highest priority based on the audio capturer information. This API uses an
         * asynchronous callback to return the result.
         *
         * @param { AudioCapturerInfo } capturerInfo - Audio capturer information.
         * @param { AsyncCallback<AudioDeviceDescriptors> } callback - Callback used to return the result. If the operation
         *     is successful, **err** is **undefined** and **data** is the input device with the highest priority obtained;
         *     otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed. Return by callback.
         * @throws { BusinessError } 6800301 - System error. Return by callback.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @since 10
         */
        getPreferredInputDeviceForCapturerInfo(capturerInfo: AudioCapturerInfo, callback: AsyncCallback<AudioDeviceDescriptors>): void;
        /**
         * Obtains the input device with the highest priority based on the audio capturer information. This API uses a
         * promise to return the result.
         *
         * @param { AudioCapturerInfo } capturerInfo - Audio capturer information.
         * @returns { Promise<AudioDeviceDescriptors> } Promise used to return the information about the input device with
         *     the highest priority.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed. Return by promise.
         * @throws { BusinessError } 6800301 - System error. Return by promise.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @since 10
         */
        getPreferredInputDeviceForCapturerInfo(capturerInfo: AudioCapturerInfo): Promise<AudioDeviceDescriptors>;
        /**
         * Subscribes to the change event of the input device with the highest priority, which is triggered when the input
         * device with the highest priority is changed. This API uses an asynchronous callback to return the result.
         *
         * @param { 'preferredInputDeviceChangeForCapturerInfo' } type - Event type. The event
         *     **'preferredInputDeviceChangeForCapturerInfo'** is triggered when the input device with the highest priority
         *     is changed.
         * @param { AudioCapturerInfo } capturerInfo - Audio capturer information.
         * @param { Callback<AudioDeviceDescriptors> } callback - Callback used to return the information about the input
         *     device with the highest priority.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @since 10
         */
        on(type: 'preferredInputDeviceChangeForCapturerInfo', capturerInfo: AudioCapturerInfo, callback: Callback<AudioDeviceDescriptors>): void;
        /**
         * Unsubscribes from the change event of the input device with the highest priority. This API uses an asynchronous
         * callback to return the result.
         *
         * @param { 'preferredInputDeviceChangeForCapturerInfo' } type - Event type. The event
         *     **'preferredInputDeviceChangeForCapturerInfo'** is triggered when the input device with the highest priority
         *     is changed.
         * @param { Callback<AudioDeviceDescriptors> } callback - Callback used to return the information about the input
         *     device with the highest priority.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @since 10
         */
        off(type: 'preferredInputDeviceChangeForCapturerInfo', callback?: Callback<AudioDeviceDescriptors>): void;
        /**
         * Gets preferred input device for target audio capturer info.
         * @param { AudioCapturerInfo } capturerInfo - Audio capturer information.
         * @returns { AudioDeviceDescriptors } Information about the input device with the highest priority.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @since 10
         */
        getPreferredInputDeviceForCapturerInfoSync(capturerInfo: AudioCapturerInfo): AudioDeviceDescriptors;
        /**
         * Checks whether the current device supports microphone blocking detection. This API uses a promise to return the
         * result.
         *
         * @returns { Promise<boolean> } Promise used to return the result, indicating the support for microphone blocking
         *     detection. **true** if supported, **false** otherwise.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 13
         */
        isMicBlockDetectionSupported(): Promise<boolean>;
        /**
         * Subscribes to the microphone blocked status change event. This API uses an asynchronous callback to return the
         * result.
         *
         * Before using this API, check whether the current device supports microphone blocking detection. This event is
         * triggered when the microphone blocked status changes during recording. Currently, this API takes effect only for
         * the microphone on the local device.
         *
         * @param { 'micBlockStatusChanged' } type - Event type. The event **'micBlockStatusChanged'** is triggered when the
         *     microphone blocked status is changed.
         * @param { Callback<DeviceBlockStatusInfo> } callback - Callback used to return the microphone blocked status and
         *     device information.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 13
         */
        on(type: 'micBlockStatusChanged', callback: Callback<DeviceBlockStatusInfo>): void;
        /**
         * Unsubscribes from the microphone blocked status change event. This API uses an asynchronous callback to return
         * the result.
         *
         * @param { 'microphoneBlockStatusChanged' } type - Event type. The event **'micBlockStatusChanged'** is triggered
         *     when the microphone blocked status is changed.
         * @param { Callback<DeviceBlockStatusInfo> } callback - Callback used to return the microphone blocked status and
         *     device information.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 13
         */
        off(type: 'micBlockStatusChanged', callback?: Callback<DeviceBlockStatusInfo>): void;
        /**
         * Declares the original device types that the application has adapted to.
         * By default, the system returns anonymous device types. This method allows applications to
         * declare which specific device types they have explicitly adapted to. Once declared, the system
         * will return the original device types to the application instead of the anonymous ones.
         * Note: This method only supports device types introduced from API 20 onwards (such as hearing aids
         * and nearlink devices). If this interface is not called for these new device types, the application
         * will only be able to obtain anonymous device types.
         * Legacy device types prior to API 20 do not need this declaration.
         *
         * @param { DeviceTypeArray } deviceTypes - Array of original device types the application has adapted to.
         * @throws { BusinessError } 6800101 - Parameter verification failed, the param deviceTypes contains value
         *     that is invalid enum or is not device type introduced in API 20 onwards.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @stagemodelonly
         * @since 26.0.0
         */
        declareDeviceTypesCompatibility(deviceTypes: DeviceTypeArray): void;
    }
    /**
     * This interface implements audio stream management.
     *
     * Before calling any API in AudioStreamManager, you must use
     * [getStreamManager]{@link @ohos.multimedia.audio:audio.AudioManager.getStreamManager} to obtain an
     * AudioStreamManager instance.
     *
     * > **NOTE**
     * >
     * > - The initial APIs of this interface are supported since API version 9.
     *
     * @syscap SystemCapability.Multimedia.Audio.Core
     * @crossplatform [since 12]
     * @since 9
     */
    interface AudioStreamManager {
        /**
         * Obtains the information about this audio renderer. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > The audio renderer information returned by this API may include internal audio playback streams, such as
         * > cellular calls and ultrasonic streams.
         *
         * @param { AsyncCallback<AudioRendererChangeInfoArray> } callback - Callback used to return the result. If the
         *     operation is successful, **err** is **undefined** and **data** is the audio renderer information obtained;
         *     otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 9
         */
        getCurrentAudioRendererInfoArray(callback: AsyncCallback<AudioRendererChangeInfoArray>): void;
        /**
         * Obtains the information about this audio renderer. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > The audio renderer information returned by this API may include internal audio playback streams, such as
         * > cellular calls and ultrasonic streams.
         *
         * @returns { Promise<AudioRendererChangeInfoArray> } Promise used to return the audio renderer information.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 9
         */
        getCurrentAudioRendererInfoArray(): Promise<AudioRendererChangeInfoArray>;
        /**
         * Obtains the information about this audio renderer. This API returns the result synchronously.
         *
         * > **NOTE**
         * >
         * > The audio renderer information returned by this API may include internal audio playback streams, such as
         * > cellular calls and ultrasonic streams.
         *
         * @returns { AudioRendererChangeInfoArray } Audio renderer information.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 10
         */
        getCurrentAudioRendererInfoArraySync(): AudioRendererChangeInfoArray;
        /**
         * Obtains the information about this audio capturer. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > The audio capturer information returned by this API may include internal audio recording streams, such as voice
         * > wakeup and cellular calls.
         *
         * @param { AsyncCallback<AudioCapturerChangeInfoArray> } callback - Callback used to return the result. If the
         *     operation is successful, **err** is **undefined** and **data** is the audio capturer information obtained;
         *     otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 9
         */
        getCurrentAudioCapturerInfoArray(callback: AsyncCallback<AudioCapturerChangeInfoArray>): void;
        /**
         * Obtains the information about this audio capturer. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > The audio capturer information returned by this API may include internal audio recording streams, such as voice
         * > wakeup and cellular calls.
         *
         * @returns { Promise<AudioCapturerChangeInfoArray> } Promise used to return the audio capturer information.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 9
         */
        getCurrentAudioCapturerInfoArray(): Promise<AudioCapturerChangeInfoArray>;
        /**
         * Obtains the information about this audio capturer. This API returns the result synchronously.
         *
         * > **NOTE**
         * >
         * > The audio capturer information returned by this API may include internal audio recording streams, such as voice
         * > wakeup and cellular calls.
         *
         * @returns { AudioCapturerChangeInfoArray } Audio capturer information.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @crossplatform [since 12]
         * @since 10
         */
        getCurrentAudioCapturerInfoArraySync(): AudioCapturerChangeInfoArray;
        /**
         * Obtains information about the audio effect mode in use. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { StreamUsage } usage - Audio stream usage.
         * @param { AsyncCallback<AudioEffectInfoArray> } callback - Callback used to return the result. If the operation is
         *     successful, **err** is **undefined** and **data** is the information about the audio effect mode obtained;
         *     otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed. Return by callback.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @since 10
         */
        getAudioEffectInfoArray(usage: StreamUsage, callback: AsyncCallback<AudioEffectInfoArray>): void;
        /**
         * Obtains information about the audio effect mode in use. This API uses a promise to return the result.
         *
         * @param { StreamUsage } usage - Audio stream usage.
         * @returns { Promise<AudioEffectInfoArray> } Promise used to return the information about the audio effect mode
         *     obtained.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed. Return by promise.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @since 10
         */
        getAudioEffectInfoArray(usage: StreamUsage): Promise<AudioEffectInfoArray>;
        /**
         * Obtains information about the audio effect mode in use. This API returns the result synchronously.
         *
         * @param { StreamUsage } usage - Audio stream usage.
         * @returns { AudioEffectInfoArray } Information about the audio effect mode.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @since 10
         */
        getAudioEffectInfoArraySync(usage: StreamUsage): AudioEffectInfoArray;
        /**
         * Subscribes to the audio renderer change event, which is triggered when the audio playback stream status or device
         * is changed. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > The audio renderer information returned by this API may include internal audio playback streams, such as
         * > cellular calls and ultrasonic streams.
         *
         * @param { 'audioRendererChange' } type - Event type. The event **'audioRendererChange'** is triggered when the
         *     audio playback stream status or device is changed.
         * @param { Callback<AudioRendererChangeInfoArray> } callback - Callback used to return the audio renderer
         *     information.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 9
         */
        on(type: 'audioRendererChange', callback: Callback<AudioRendererChangeInfoArray>): void;
        /**
         * Unsubscribes from the audio renderer change event. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > The audio renderer information returned by this API may include internal audio playback streams, such as
         * > cellular calls and ultrasonic streams.
         *
         * @param { 'audioRendererChange' } type - Event type. The event **'audioRendererChange'** is triggered when the
         *     audio playback stream status or device is changed.
         * @param { Callback<AudioRendererChangeInfoArray> } callback - Callback used to return the audio renderer
         *     information. [since 18]
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 9
         */
        off(type: 'audioRendererChange', callback?: Callback<AudioRendererChangeInfoArray>): void;
        /**
         * Subscribes to the audio capturer change event, which is triggered when the audio recording stream status or
         * device is changed. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > The audio capturer information returned by this API may include internal audio recording streams, such as voice
         * > wakeup and cellular calls.
         *
         * @param { 'audioCapturerChange' } type - Event type. The event **'audioCapturerChange'** is triggered when the
         *     audio recording stream status or device is changed.
         * @param { Callback<AudioCapturerChangeInfoArray> } callback - Callback used to return the audio capturer
         *     information.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @crossplatform [since 12]
         * @since 9
         */
        on(type: 'audioCapturerChange', callback: Callback<AudioCapturerChangeInfoArray>): void;
        /**
         * Unsubscribes from the audio capturer change event. This API uses an asynchronous callback to return the result.
         *
         * > **NOTE**
         * >
         * > The audio capturer information returned by this API may include internal audio recording streams, such as voice
         * > wakeup and cellular calls.
         *
         * @param { 'audioCapturerChange' } type - Event type. The event **'audioCapturerChange'** is triggered when the
         *     audio capturer is changed.
         * @param { Callback<AudioCapturerChangeInfoArray> } callback - Callback used to return the audio capturer
         *     information. [since 18]
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @crossplatform [since 12]
         * @since 9
         */
        off(type: 'audioCapturerChange', callback?: Callback<AudioCapturerChangeInfoArray>): void;
        /**
         * Checks whether a stream is active. This API uses an asynchronous callback to return the result.
         *
         * @param { AudioVolumeType } volumeType - Audio stream types.
         * @param { AsyncCallback<boolean> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **data** is **true** if the stream is active or **false** if not active;
         *     otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 9
         * @deprecated since 20
         * @useinstead ohos.multimedia.audio.AudioStreamManager#isStreamActive
         */
        isActive(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void;
        /**
         * Checks whether a stream is active. This API uses a promise to return the result.
         *
         * @param { AudioVolumeType } volumeType - Audio stream types.
         * @returns { Promise<boolean> } Promise used to return the result, indicating whether the stream is active.
         *     **true** if active, **false** otherwise.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 9
         * @deprecated since 20
         * @useinstead ohos.multimedia.audio.AudioStreamManager#isStreamActive
         */
        isActive(volumeType: AudioVolumeType): Promise<boolean>;
        /**
         * Checks whether a stream is active. This API returns the result synchronously.
         *
         * @param { AudioVolumeType } volumeType - Audio stream types.
         * @returns { boolean } Check result for whether the stream is active. **true** if active, **false** otherwise.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 10
         * @deprecated since 20
         * @useinstead ohos.multimedia.audio.AudioStreamManager#isStreamActive
         */
        isActiveSync(volumeType: AudioVolumeType): boolean;
        /**
         * Checks whether a stream is active. This API returns the result synchronously.
         *
         * @param { StreamUsage } streamUsage - Audio stream usage.
         * @returns { boolean } Check result for whether the stream is active. **true** if active, **false** otherwise.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @since 20
         */
        isStreamActive(streamUsage: StreamUsage): boolean;
        /**
         * Checks whether the specified audio source type supports echo cancellation.
         *
         * @param { SourceType } sourceType - Audio source type.
         * @returns { boolean } Check result for whether echo cancellation is supported. **true** if supported, **false**
         *     otherwise.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @since 20
         */
        isAcousticEchoCancelerSupported(sourceType: SourceType): boolean;
        /**
         * Checks whether the current system supports the specified audio loopback mode.
         *
         * @param { AudioLoopbackMode } mode - Audio loopback mode.
         * @returns { boolean } Check result for whether the audio loopback mode is supported. **true** if supported,
         *     **false** otherwise.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @since 20
         */
        isAudioLoopbackSupported(mode: AudioLoopbackMode): boolean;
        /**
         * Checks whether recording can be started based on the audio source type in the audio capturer information.
         *
         * @param { AudioCapturerInfo } capturerInfo - Audio capturer information.
         * @returns { boolean } Check result for whether recording can be started. **true** if recording can be started,
         *     **false** otherwise.
         *     <br>This API checks whether the specified audio source type in the capturer information can acquire focus. It should
         *     be called before starting audio recording to avoid conflicts with existing recording streams.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @since 20
         */
        isRecordingAvailable(capturerInfo: AudioCapturerInfo): boolean;
        /**
         * Checks whether the intelligent noise reduction feature is enabled for the audio stream of the specified source
         * type.
         *
         * @param { SourceType } sourceType - Audio source type.
         * @returns { boolean } Check result for whether the intelligent noise reduction feature is enabled. **true** if
         *     enabled, **false** otherwise.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 21
         */
        isIntelligentNoiseReductionEnabledForCurrentDevice(sourceType: SourceType): boolean;
        /**
         * Return if fast playback is supported for the specific audio stream info and usage type
         * in current device situation.
         *
         * @param { AudioStreamInfo } streamInfo - reference of stream info structure to describe basic audio format.
         * @param { StreamUsage } usage - stream usage type used to decide the audio device and pipe type selection result.
         * @returns { boolean } True if fast playback is supported in this situation.
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        isFastPlaybackSupported(streamInfo: AudioStreamInfo, usage: StreamUsage): boolean;
        /**
         * Return if offload playback is supported for the specific audio stream info and usage type
         * in current device situation.
         *
         * @param { AudioStreamInfo } streamInfo - reference of stream info structure to describe basic audio format.
         * @param { StreamUsage } usage - stream usage type used to decide the audio device and pipe type selection result.
         * @returns { boolean } True if offload playback is supported in this situation.
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        isOffloadPlaybackSupported(streamInfo: AudioStreamInfo, usage: StreamUsage): boolean;
        /**
         * Return if direct playback is supported for the specific audio stream info and usage type
         * in current device situation.
         *
         * @param { AudioStreamInfo } streamInfo - reference of stream info structure to describe basic audio format.
         * @param { StreamUsage } usage - stream usage type used to decide the audio device and pipe type selection result.
         * @returns { boolean } True if direct playback is supported in this situation.
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        isDirectPlaybackSupported(streamInfo: AudioStreamInfo, usage: StreamUsage): boolean;
        /**
         * Return if fast recording is supported for the specific audio stream info and usage type
         * in current device situation.
         *
         * @param { AudioStreamInfo } streamInfo - reference of stream info structure to describe basic audio format.
         * @param { SourceType } source - stream source type used to decide the audio device and pipe type selection result.
         * @returns { boolean } True if fast recording is supported in this situation.
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        isFastRecordingSupported(streamInfo: AudioStreamInfo, source: SourceType): boolean;
        /**
         * Return if multichannel playback is supported for the specific audio stream info and usage type
         * in current device situation.
         *
         * @param { AudioStreamInfo } streamInfo - reference of stream info structure to describe basic audio format.
         * @param { StreamUsage } usage - stream usage type used to decide the audio device and pipe type selection result.
         * @returns { boolean } True if multichannel playback is supported in this situation.
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        isMultichannelPlaybackSupported(streamInfo: AudioStreamInfo, usage: StreamUsage): boolean;
    }
    /**
     * Enumerates the audio concurrency modes.
     *
     * @enum { number } [since 12 - 24]
     * @syscap SystemCapability.Multimedia.Audio.Core
     * @crossplatform
     * @atomicservice [since 26.0.0]
     * @since 12
     */
    enum AudioConcurrencyMode {
        /**
         * Uses the system strategy by default.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform
         * @atomicservice [since 26.0.0]
         * @since 12
         */
        CONCURRENCY_DEFAULT = 0,
        /**
         * Concurrent with other audio streams, that is, audio mixing.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform
         * @atomicservice [since 26.0.0]
         * @since 12
         */
        CONCURRENCY_MIX_WITH_OTHERS = 1,
        /**
         * Ducks other audio streams.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform
         * @atomicservice [since 26.0.0]
         * @since 12
         */
        CONCURRENCY_DUCK_OTHERS = 2,
        /**
         * Pauses other audio streams.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform
         * @atomicservice [since 26.0.0]
         * @since 12
         */
        CONCURRENCY_PAUSE_OTHERS = 3
    }
    /**
     * Enumerates the reasons for deactivating an audio session.
     *
     * @syscap SystemCapability.Multimedia.Audio.Core
     * @crossplatform
     * @since 12
     */
    enum AudioSessionDeactivatedReason {
        /**
         * The application focus is preempted.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform
         * @since 12
         */
        DEACTIVATED_LOWER_PRIORITY = 0,
        /**
         * The audio session times out.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform
         * @since 12
         */
        DEACTIVATED_TIMEOUT = 1
    }
    /**
     * Enumerates the audio session scenes.
     *
     * @syscap SystemCapability.Multimedia.Audio.Core
     * @since 20
     */
    enum AudioSessionScene {
        /**
         * Scene for media.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 20
         */
        AUDIO_SESSION_SCENE_MEDIA = 0,
        /**
         * Scene for game.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 20
         */
        AUDIO_SESSION_SCENE_GAME = 1,
        /**
         * Scene for voice communication.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 20
         */
        AUDIO_SESSION_SCENE_VOICE_COMMUNICATION = 2
    }
    /**
     * Enumerates the hints for audio session state changes.
     *
     * The hint is obtained when an
     * [AudioSessionStateChangedEvent]{@link @ohos.multimedia.audio:audio.AudioSessionStateChangedEvent} is received.
     *
     * The hint specifies the action (such as audio pause or volume adjustment) to take on the audio session based on the
     * focus strategy.
     *
     * For details, see [Audio Session Management](docroot://media/audio/audio-session-management.md).
     *
     * @syscap SystemCapability.Multimedia.Audio.Core
     * @since 20
     */
    enum AudioSessionStateChangeHint {
        /**
         * A hint is displayed, indicating that the audio session is resuming. The application can proactively trigger
         * operations such as rendering.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 20
         */
        AUDIO_SESSION_STATE_CHANGE_HINT_RESUME = 0,
        /**
         * A hint is displayed, indicating that the audio session is paused and the audio focus is lost temporarily. When
         * focus is regained, the AUDIO_SESSION_STATE_CHANGE_HINT_RESUME event is received.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 20
         */
        AUDIO_SESSION_STATE_CHANGE_HINT_PAUSE = 1,
        /**
         * A hint is displayed, indicating that the audio session is stopped and the audio focus is lost permanently.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 20
         */
        AUDIO_SESSION_STATE_CHANGE_HINT_STOP = 2,
        /**
         * A hint is displayed, indicating that the audio session is stopped by the system due to no activity, and the audio
         * focus is lost.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 20
         */
        AUDIO_SESSION_STATE_CHANGE_HINT_TIME_OUT_STOP = 3,
        /**
         * A hint is displayed, indicating that audio ducking starts and the audio is played at a lower volume.
         *
         * If
         * [enableMuteSuggestionWhenMixWithOthers]{@link @ohos.multimedia.audio:audio.AudioSessionManager.enableMuteSuggestionWhenMixWithOthers}
         * is enabled, you can choose to mute the audio.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 20
         */
        AUDIO_SESSION_STATE_CHANGE_HINT_DUCK = 4,
        /**
         * A hint is displayed, indicating that audio ducking ends and the audio is played at the normal volume.
         *
         * If
         * [enableMuteSuggestionWhenMixWithOthers]{@link @ohos.multimedia.audio:audio.AudioSessionManager.enableMuteSuggestionWhenMixWithOthers}
         * is enabled, you can unmute the audio.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 20
         */
        AUDIO_SESSION_STATE_CHANGE_HINT_UNDUCK = 5,
        /**
         * Suggests to mute the playback because there is another application begin to play nonmixable
         * audio, application can decide whether to mute.
         * If interrupt strategy is duck, {@link #AUDIO_SESSION_STATE_CHANGE_HINT_DUCK} will replace mute suggestion event,
         * but application can still decide to mute when receive hint duck.
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @stagemodelonly
         * @since 23
         */
        AUDIO_SESSION_STATE_CHANGE_HINT_MUTE_SUGGESTION = 6,
        /**
         * Suggest to unmute the playback because another application's nonmixable audio ends,
         * application can decide whether to mute.
         * If interrupt strategy is unduck, {@link #AUDIO_SESSION_STATE_CHANGE_HINT_UNDUCK} will replace unmute
         * suggestion event, but application can still decide to unmute when receive hint unduck.
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @stagemodelonly
         * @since 23
         */
        AUDIO_SESSION_STATE_CHANGE_HINT_UNMUTE_SUGGESTION = 7,
        /**
         * The hint can be received only after the parameter {@link #AudioSessionBehaviorFlags.MUTE_WHEN_INTERRUPTED}
         * has been set by the interface {@link #setAudioSessionBehavior}
         * and {@link #setAudioSessionScene} has been called, and the audio session has been activated.
         * After the hint is received, the audio stream is muted.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @stagemodelonly
         * @since 24
         */
        AUDIO_SESSION_STATE_CHANGE_HINT_MUTE = 8,
        /**
         * The hint can be received only after the parameter {@link #AudioSessionBehaviorFlags.MUTE_WHEN_INTERRUPTED}
         * has been set by the interface {@link #setAudioSessionBehavior}
         * and {@link #setAudioSessionScene} has been called, and the audio session has been activated.
         * When the hint is received, the audio stream is unmuted.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @stagemodelonly
         * @since 24
         */
        AUDIO_SESSION_STATE_CHANGE_HINT_UNMUTE = 9
    }
    /**
     * Enumerates the recommended actions to take after an output device changes.
     *
     * Common scenario example: switching between a headset and a loudspeaker device. Upon switching from the loudspeaker
     * device to the headset upon wearing, the system suggests continuing playback and prompts that the application does
     * not need to pause. Upon transitioning from the headset to the loudspeaker device upon removal, the system suggests
     * suspending playback.
     *
     * @syscap SystemCapability.Multimedia.Audio.Core
     * @since 20
     */
    enum OutputDeviceChangeRecommendedAction {
        /**
         * Suggests continuing playback. (This event serves as a playback maintenance indication, informing the application
         * that audio playback does not need to stop during this device change. However, it must not be used as a criterion
         * for triggering audio playback.)
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 20
         */
        DEVICE_CHANGE_RECOMMEND_TO_CONTINUE = 0,
        /**
         * Suggests stopping playback.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 20
         */
        DEVICE_CHANGE_RECOMMEND_TO_STOP = 1
    }
    /**
     * Enumerates audio session behavior flags.
     *
     * @syscap SystemCapability.Multimedia.Audio.Core
     * @stagemodelonly
     * @since 24
     */
    enum AudioSessionBehaviorFlags {
        /**
         * Default behavior, used to clear behavior settings.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @stagemodelonly
         * @since 24
         */
        DEFAULT_BEHAVIOR = 0x00000000,
        /**
         * When the system needs to stop or pause the audio stream, it performs a forced mute instead.
         * In the audio session scenario, the application will receive a notification
         * {@link #AUDIO_SESSION_STATE_CHANGE_HINT_MUTE} when muted
         * and a notification {@link #AUDIO_SESSION_STATE_CHANGE_HINT_UNMUTE} when resumed.
         * In the AudioRenderer and AudioCapturer scenarios, the application will receive a notification
         * {@link #INTERRUPT_HINT_MUTE} when muted
         * and a notification {@link #INTERRUPT_HINT_UNMUTE} when resumed.
         * This flag cannot coexist with {@link #PAUSE_WHEN_INTERRUPTED}; if both flags are set,
         * only {@link #PAUSE_WHEN_INTERRUPTED} will take effect.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @stagemodelonly
         * @since 24
         */
        MUTE_WHEN_INTERRUPTED = 0x00000002,
        /**
         * When the system needs to stop the audio stream, it performs a pause instead.
         * In the audio session scenario, the application will receive a notification
         * {@link #AUDIO_SESSION_STATE_CHANGE_HINT_PAUSE} when paused
         * and a notification {@link #AUDIO_SESSION_STATE_CHANGE_HINT_RESUME} when resumed.
         * In the AudioRenderer and AudioCapturer scenarios, the application will receive a notification
         * {@link #INTERRUPT_HINT_PAUSE} when paused
         * and a notification {@link #INTERRUPT_HINT_RESUME} when resumed.
         * This flag cannot coexist with {@link #MUTE_WHEN_INTERRUPTED}; if both flags are set,
         * only this flag will take effect.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        PAUSE_WHEN_INTERRUPTED = 0x00000004
    }
    /**
     * Describes an audio session strategy.
     *
     * @typedef AudioSessionStrategy [since 12 - 24]
     * @syscap SystemCapability.Multimedia.Audio.Core
     * @crossplatform
     * @atomicservice [since 26.0.0]
     * @since 12
     */
    interface AudioSessionStrategy {
        /**
         * Audio concurrency mode.
         *
         * @type { AudioConcurrencyMode } [since 12 - 24]
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform
         * @atomicservice [since 26.0.0]
         * @since 12
         */
        concurrencyMode: AudioConcurrencyMode;
    }
    /**
     * Describes the event indicating that an audio session is deactivated.
     *
     * @syscap SystemCapability.Multimedia.Audio.Core
     * @crossplatform
     * @since 12
     */
    interface AudioSessionDeactivatedEvent {
        /**
         * Reason for deactivating an audio session.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform
         * @since 12
         */
        reason: AudioSessionDeactivatedReason;
    }
    /**
     * Describes the event indicating that the audio session state changes.
     *
     * @syscap SystemCapability.Multimedia.Audio.Core
     * @since 20
     */
    interface AudioSessionStateChangedEvent {
        /**
         * Hint for the audio session state change.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 20
         */
        stateChangeHint: AudioSessionStateChangeHint;
    }
    /**
     * Describes the event indicating that the output device changes.
     *
     * @syscap SystemCapability.Multimedia.Audio.Core
     * @since 20
     */
    interface CurrentOutputDeviceChangedEvent {
        /**
         * Audio device descriptors before change.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        preDevices?: AudioDeviceDescriptors;
        /**
         * Audio device descriptors after change.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 20
         */
        devices: AudioDeviceDescriptors;
        /**
         * Audio device change reason.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 20
         */
        changeReason: AudioStreamDeviceChangeReason;
        /**
         * Recommend action when device change.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 20
         */
        recommendedAction: OutputDeviceChangeRecommendedAction;
    }
    /**
     * Enumerates the preferred device categories available for recording with Bluetooth or NearLink.
     *
     * @syscap SystemCapability.Multimedia.Audio.Core
     * @since 21
     */
    enum BluetoothAndNearlinkPreferredRecordCategory {
        /**
         * No specific device preference.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 21
         */
        PREFERRED_NONE = 0,
        /**
         * Prefers using Bluetooth or NearLink devices for recording; whether to use low-latency or high-quality recording
         * depends on the system.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 21
         */
        PREFERRED_DEFAULT = 1,
        /**
         * Prefers using Bluetooth or NearLink devices in low-latency mode for recording.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 21
         */
        PREFERRED_LOW_LATENCY = 2,
        /**
         * Prefers using Bluetooth or NearLink devices in high-quality mode for recording.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 21
         */
        PREFERRED_HIGH_QUALITY = 3
    }
    /**
     * Describes the event indicating that the input device changes.
     *
     * @syscap SystemCapability.Multimedia.Audio.Core
     * @since 21
     */
    interface CurrentInputDeviceChangedEvent {
        /**
         * Audio input device descriptors after change.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 21
         */
        devices: AudioDeviceDescriptors;
        /**
         * Audio input device change reason.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 21
         */
        changeReason: AudioStreamDeviceChangeReason;
    }
    /**
     * This interface implements audio session management.
     *
     * Before calling any API in AudioSessionManager, you must use
     * [getSessionManager]{@link @ohos.multimedia.audio:audio.AudioManager.getSessionManager} to obtain an
     * AudioSessionManager instance.
     *
     * > **NOTE**
     * >
     * > - The initial APIs of this interface are supported since API version 12.
     *
     * @typedef AudioSessionManager [since 12 - 24]
     * @syscap SystemCapability.Multimedia.Audio.Core
     * @crossplatform
     * @atomicservice [since 26.0.0]
     * @since 12
     */
    interface AudioSessionManager {
        /**
         * Activates an audio session. This API uses a promise to return the result.
         *
         * @param { AudioSessionStrategy } strategy - Audio session strategy.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @throws { BusinessError } 6800301 - System error. Possible causes:
         *     1.Focus preemption failure.
         *     2.Audio server process died.
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform
         * @atomicservice [since 26.0.0]
         * @since 12
         */
        activateAudioSession(strategy: AudioSessionStrategy): Promise<void>;
        /**
         * Deactivates this audio session. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 6800301 - System error. Possible causes:
         *     1.The audio session is not existed or has been released.
         *     2.Audio server process died.
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform
         * @atomicservice [since 26.0.0]
         * @since 12
         */
        deactivateAudioSession(): Promise<void>;
        /**
         * Checks whether this audio session is activated.
         *
         * @returns { boolean } Check result for whether the audio session is activated. **true** if activated, **false**
         *     otherwise.
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform
         * @atomicservice [since 26.0.0]
         * @since 12
         */
        isAudioSessionActivated(): boolean;
        /**
         * Subscribes to the audio session deactivation event, which is triggered when an audio session is deactivated. This
         * API uses an asynchronous callback to return the result.
         *
         * @param { 'audioSessionDeactivated' } type - Event type. The event **'audioSessionDeactivated'** is triggered when
         *     the audio session is deactivated.
         * @param { Callback<AudioSessionDeactivatedEvent> } callback - Callback used to return the reason why the audio
         *     session is deactivated.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform
         * @atomicservice [since 26.0.0]
         * @since 12
         */
        on(type: 'audioSessionDeactivated', callback: Callback<AudioSessionDeactivatedEvent>): void;
        /**
         * Unsubscribes from the audio session deactivation event. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { 'audioSessionDeactivated' } type - Event type. The event **'audioSessionDeactivated'** is triggered when
         *     the audio session is deactivated.
         * @param { Callback<AudioSessionDeactivatedEvent> } callback - Callback used to return the reason why the audio
         *     session is deactivated.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform
         * @atomicservice [since 26.0.0]
         * @since 12
         */
        off(type: 'audioSessionDeactivated', callback?: Callback<AudioSessionDeactivatedEvent>): void;
        /**
         * Sets an audio session scene.
         *
         * @param { AudioSessionScene } scene - Audio session scene.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @throws { BusinessError } 6800103 - Operation not permit at current state.
         * @throws { BusinessError } 6800301 - Audio client call audio service error, System error.
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 20
         */
        setAudioSessionScene(scene: AudioSessionScene): void;
        /**
         * Set mute hint for all capturer streams in the current audio session. It dose not mute the recording
         * stream, only affects internal processing strategy.
         *
         * @param { boolean } mute - Use true if application recording stream muted by application if self.
         * @returns { Promise<void> } Promise used to return the result.
         * @throws { BusinessError } 6800103 - Operation not permit at current state, there is no audio capturer running.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @stagemodelonly
         * @since 24
         */
        setCapturerMuteHint(mute: boolean): Promise<void>;
        /**
         * Subscribes to the audio session state change event, which is triggered when the audio session focus is changed.
         * This API uses an asynchronous callback to return the result.
         *
         * @param { 'audioSessionStateChanged' } type - Event type. The event **'audioSessionStateChanged'** is triggered
         *     when the audio session state is changed.
         * @param { Callback<AudioSessionStateChangedEvent> } callback - Callback used to return the audio session change
         *     information.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @throws { BusinessError } 6800102 - Allocate memory failed.
         * @throws { BusinessError } 6800301 - Audio client call audio service error, System error.
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 20
         */
        on(type: 'audioSessionStateChanged', callback: Callback<AudioSessionStateChangedEvent>): void;
        /**
         * Unsubscribes from the audio session state change event. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { 'audioSessionStateChanged' } type - Event type. The event **'audioSessionStateChanged'** is triggered
         *     when the audio session state is changed.
         * @param { Callback<AudioSessionStateChangedEvent> } [callback] - Callback used to return the audio session change
         *     information.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @throws { BusinessError } 6800301 - Audio client call audio service error, System error.
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 20
         */
        off(type: 'audioSessionStateChanged', callback?: Callback<AudioSessionStateChangedEvent>): void;
        /**
         * Obtains the default audio output device set by calling
         * [setDefaultOutputDevice]{@link audio.AudioSessionManager.setDefaultOutputDevice}.
         *
         * @returns { DeviceType } Device type.
         *     <br>The options are **EARPIECE**, **SPEAKER**, and **DEFAULT**.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @throws { BusinessError } 6800103 - Operation not permit at current state. Return by promise.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 20
         */
        getDefaultOutputDevice(): DeviceType;
        /**
         * Sets the default audio output device. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > - This API applies to the following scenario: When
         * > [AudioSessionScene]{@link @ohos.multimedia.audio:audio.AudioSessionScene} is set to **VoIP**, the setting takes
         * > effect immediately after the AudioSession is activated. For non-VoIP scenarios, the setting does not take
         * > effect upon AudioSession activation. Instead, the setting applies when
         * > [StreamUsage]{@link @ohos.multimedia.audio:audio.StreamUsage} for playback is voice message, VoIP voice call,
         * > or VoIP video call. Supported devices include the earpiece, speaker, and system default device.
         * >
         * > - This API can be called at any time after an AudioSessionManager instance is created. The system records the
         * > device set by the application. However, the setting takes effect only after the AudioSession is activated. When
         * > the application starts playing, if an external device like Bluetooth headsets or wired headsets is connected,
         * > the system prioritizes audio output through the external device. Otherwise, the system uses the device set by
         * > the application.
         *
         * @param { DeviceType } deviceType - Device type.<br>The options are **EARPIECE**, **SPEAKER**, and **DEFAULT**.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 6800101 - Parameter verification failed. Return by promise.
         * @throws { BusinessError } 6800102 - Allocate memory failed. Return by promise.
         * @throws { BusinessError } 6800301 - Audio client call audio service error, System error.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 20
         */
        setDefaultOutputDevice(deviceType: DeviceType): Promise<void>;
        /**
         * Set the audio output device to the built-in speaker, when other audio peripherals
         * are connected, such as bluetooth headphones or wired headsets. It should be noted
         * that this interface only applies to media streams.
         * In scenarios where there are concurrent playback streams with higher priority or user
         * selects the output device through system UI, the actual output device used by
         * the application may differ from the selected one. The application can obtain currently
         * active output device by subscribing to the currentOutputDeviceChanged event.
         *
         * @param { DeviceType } deviceType - the available deviceTypes are
         *     SPEAKER: Built-in speaker
         *     DEFAULT: Restore to system default output device
         * @returns { Promise<void> } Promise used to return the result.
         * @throws { BusinessError } 6800101 - Parameter verification failed, for example,
         *     the selected device type is not supported.
         * @throws { BusinessError } 6800301 - System error. Possible causes:
         *     1.Internal variable memory allocation failed.
         *     2.Audio server process died.
         *     3.Speaker device is not available.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @stagemodelonly
         * @since 26.0.0
         */
        setMediaOutputDevice(deviceType: DeviceType): Promise<void>;
        /**
         * Subscribes to the current output device change event, which is triggered when the current output device is
         * changed. This API uses an asynchronous callback to return the result.
         *
         * @param { 'currentOutputDeviceChanged' } type - Event type. The event **'currentOutputDeviceChanged'** is
         *     triggered when the current output device is changed.
         * @param { Callback<CurrentOutputDeviceChangedEvent> } callback - Callback used to return the information about the
         *     current output device.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @throws { BusinessError } 6800102 - Allocate memory failed.
         * @throws { BusinessError } 6800301 - Audio client call audio service error, System error.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 20
         */
        on(type: 'currentOutputDeviceChanged', callback: Callback<CurrentOutputDeviceChangedEvent>): void;
        /**
         * Unsubscribes from the current output device change event. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { 'currentOutputDeviceChanged' } type - Event type. The event **'currentOutputDeviceChanged'** is
         *     triggered when the current output device is changed.
         * @param { Callback<CurrentOutputDeviceChangedEvent> } [callback] - Callback used to return the information about
         *     the current output device.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @throws { BusinessError } 6800301 - Audio client call audio service error, System error.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 20
         */
        off(type: 'currentOutputDeviceChanged', callback?: Callback<CurrentOutputDeviceChangedEvent>): void;
        /**
         * Obtains the available audio devices.
         *
         * @param { DeviceUsage } deviceUsage - Audio device type (classified by usage).
         * @returns { AudioDeviceDescriptors } Device list.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @throws { BusinessError } 6800301 - Audio client call audio service error, System error.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 21
         */
        getAvailableDevices(deviceUsage: DeviceUsage): AudioDeviceDescriptors;
        /**
         * Subscribes to the event indicating that the connection status of an available audio device is changed.
         *
         * @param { 'availableDeviceChange' } type - Event type. The event **'availableDeviceChange'** is triggered when the
         *     connection status of available audio devices is changed.
         * @param { DeviceUsage } deviceUsage - Audio device type (classified by usage).
         * @param { Callback<DeviceChangeAction> } callback - Callback used to return the available device change details.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @throws { BusinessError } 6800301 - Audio client call audio service error, System error.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 21
         */
        on(type: 'availableDeviceChange', deviceUsage: DeviceUsage, callback: Callback<DeviceChangeAction>): void;
        /**
         * Unsubscribes from the event indicating that the connection status of an available audio device is changed.
         *
         * @param { 'availableDeviceChange' } type - Event type. The event **'availableDeviceChange'** is triggered when the
         *     connection status of available audio devices is changed.
         * @param { Callback<DeviceChangeAction> } [callback] - Callback used to return the available device change details.
         * @throws { BusinessError } 6800301 - Audio client call audio service error, System error.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 21
         */
        off(type: 'availableDeviceChange', callback?: Callback<DeviceChangeAction>): void;
        /**
         * Selects a media input device. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > - This API is not suitable for VoIP call recording; that is, it does not apply to scenarios where
         * > [SourceType]{@link @ohos.multimedia.audio:audio.SourceType} is **SOURCE_TYPE_VOICE_COMMUNICATION**.
         * >
         * > - Before calling this API, call [getAvailableDevices]{@link audio.AudioSessionManager.getAvailableDevices} to
         * > query the list of available input devices and select an input device from the list.
         * >
         * > - If there are recording streams of other applications with higher priorities in the system, the actual input
         * > device used will follow the input device selected by these applications.
         * >
         * > - Applications can listen for the
         * > [currentInputDeviceChanged]{@link audio.AudioSessionManager.on(type: 'currentInputDeviceChanged', callback: Callback<CurrentInputDeviceChangedEvent>)}
         * > event to find out the actual input device being used.
         *
         * @param { AudioDeviceDescriptor } inputAudioDevice - Media input device.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 6800101 - Parameter verification failed, for example,
         *     the selected device does not exist.
         * @throws { BusinessError } 6800301 - Audio client call audio service error, System error.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 21
         */
        selectMediaInputDevice(inputAudioDevice: AudioDeviceDescriptor): Promise<void>;
        /**
         * Obtains the media input device set by calling
         * [selectMediaInputDevice]{@link audio.AudioSessionManager.selectMediaInputDevice}. If no device has been specified
         * , the device with **deviceType** set to **INVALID** is returned.
         *
         * @returns { AudioDeviceDescriptor } Media input device.
         * @throws { BusinessError } 6800301 - Audio client call audio service error, System error.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 21
         */
        getSelectedMediaInputDevice(): AudioDeviceDescriptor;
        /**
         * Clears the media input device set by calling
         * [selectMediaInputDevice]{@link audio.AudioSessionManager.selectMediaInputDevice}. This API uses a promise to
         * return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 6800301 - Audio client call audio service error, System error.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 21
         */
        clearSelectedMediaInputDevice(): Promise<void>;
        /**
         * Sets the preferred device category for recording with Bluetooth or NearLink. This API uses a promise to return
         * the result.
         *
         * > **NOTE**
         * >
         * > - Applications can set this category before connecting to Bluetooth or NearLink devices, and the system
         * > prioritizes using the device for recording when the device is connected.
         * >
         * > - If there are recording streams of other applications with higher priorities in the system, the actual input
         * > device used will follow the input device selected by these applications.
         * >
         * > - Applications can listen for the
         * > [currentInputDeviceChanged]{@link audio.AudioSessionManager.on(type: 'currentInputDeviceChanged', callback: Callback<CurrentInputDeviceChangedEvent>)}
         * > event to find out the actual input device being used.
         *
         * @param { BluetoothAndNearlinkPreferredRecordCategory } category - Preferred device category for recording with
         *     Bluetooth or NearLink.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @throws { BusinessError } 6800301 - Audio client call audio service error, System error.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 21
         */
        setBluetoothAndNearlinkPreferredRecordCategory(category: BluetoothAndNearlinkPreferredRecordCategory): Promise<void>;
        /**
         * Obtains the preferred device category for recording with Bluetooth or NearLink, which is set by calling
         * [setBluetoothAndNearlinkPreferredRecordCategory]{@link audio.AudioSessionManager.setBluetoothAndNearlinkPreferredRecordCategory}
         * .
         *
         * @returns { BluetoothAndNearlinkPreferredRecordCategory } Preferred device category for recording with Bluetooth
         *     or NearLink.
         * @throws { BusinessError } 6800301 - Audio client call audio service error, System error.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 21
         */
        getBluetoothAndNearlinkPreferredRecordCategory(): BluetoothAndNearlinkPreferredRecordCategory;
        /**
         * Subscribes to the current input device change event, which is triggered when the current input device is changed.
         *
         * @param { 'currentInputDeviceChanged' } type - Event type. The event **'currentInputDeviceChanged'** is triggered
         *     when the current input device is changed.
         * @param { Callback<CurrentInputDeviceChangedEvent> } callback - Callback used to return the information about the
         *     current input device.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @throws { BusinessError } 6800301 - Audio client call audio service error, System error.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 21
         */
        on(type: 'currentInputDeviceChanged', callback: Callback<CurrentInputDeviceChangedEvent>): void;
        /**
         * Unsubscribes from the current input device change event.
         *
         * @param { 'currentInputDeviceChanged' } type - Event type. The event **'currentInputDeviceChanged'** is triggered
         *     when the current input device is changed.
         * @param { Callback<CurrentInputDeviceChangedEvent> } [callback] - Callback used to return the information about
         *     the current input device.
         * @throws { BusinessError } 6800301 - Audio client call audio service error, System error.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 21
         */
        off(type: 'currentInputDeviceChanged', callback?: Callback<CurrentInputDeviceChangedEvent>): void;
        /**
         * Enables mute suggestion notifications for mixed playback.
         *
         * Typically, when the audio mixing mode is used, if two applications plays audio at the same time, their audio
         * streams are mixed. In certain scenarios (such as games or broadcasts), applications can mute their own audio to
         * provide a better user experience.
         *
         * If this feature is enabled, mute and unmute suggestions will be sent through the
         * [AudioSessionStateChangedEvent]{@link @ohos.multimedia.audio:audio.AudioSessionStateChangedEvent} callback after
         * the audio session state change event is subscribed to. Receiving the muted suggestion indicates that another
         * application starts to play audio, and the played audio and the audio of this application cannot be mixed.
         *
         * This feature can be used only by audio sessions for which
         * [AudioSessionScene]{@link @ohos.multimedia.audio:audio.AudioSessionScene} has been set and the
         * **CONCURRENCY_MIX_WITH_OTHERS** mode has been activated. This feature takes effect only once when the audio
         * session is activated. You need to enable it again before each activation of the audio session.
         *
         * For details, see
         * [Enabling Mute Suggestion Notifications for Mixed Playback](docroot://media/audio/audio-session-management.md#enabling-mute-suggestion-notifications-for-mixed-playback)
         * .
         *
         * @param { boolean } enable - Whether to enable mute suggestion notifications for mixed playback. **true** to
         *     enable, **false** otherwise.
         * @throws { BusinessError } 6800103 - Function is called without setting {@link #AudioSessionScene} or
         *     called after audio session activation.
         * @throws { BusinessError } 6800301 - Audio client call audio service error, system internal error.
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @stagemodelonly
         * @since 23
         */
        enableMuteSuggestionWhenMixWithOthers(enable: boolean): void;
        /**
         * Check whether any other application is currently playing audio of the four media types: **MUSIC**, **MOVIE**,
         * **AUDIOBOOK**, and **GAME**. Audio sessions that have activated these media types will also be checked.
         *
         * @returns { boolean } Whether another application is playing audio of certain media types. **true** means yes;
         *     **false** otherwise.
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @stagemodelonly
         * @since 23
         */
        isOtherMediaPlaying(): boolean;
        /**
         * Sets audio session behavior parameters. (Multiple flags can be combined.)
         *
         * > **NOTE**
         * >
         * > If this API is called while an audio session is active, you must call the
         * > [activateAudioSession]{@link @ohos.multimedia.audio:audio.AudioSessionManager.activateAudioSession} API again
         * > for the settings to take effect.
         *
         * @param { number } behavior - Specifies the audio session behavior.<br>This can be a single flag or a bitwise OR
         *     combination of multiple flags.<br>For details about the supported audio session behaviors, see
         *     [AudioSessionBehaviorFlags]{@link @ohos.multimedia.audio:audio.AudioSessionBehaviorFlags}.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @throws { BusinessError } 6800103 - Operation not permitted in the current state.
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @stagemodelonly
         * @since 24
         */
        setAudioSessionBehavior(behavior: number): void;
    }
    /**
     * This interface implements audio volume management.
     *
     * Before calling any API in AudioVolumeManager, you must use
     * [getVolumeManager]{@link @ohos.multimedia.audio:audio.AudioManager.getVolumeManager} to obtain an
     * AudioVolumeManager instance.
     *
     * > **NOTE**
     * >
     * > - The initial APIs of this interface are supported since API version 9.
     *
     * @syscap SystemCapability.Multimedia.Audio.Volume
     * @crossplatform [since 12]
     * @atomicservice [since 23]
     * @since 9
     */
    interface AudioVolumeManager {
        /**
         * Obtains a VolumeGroupManager instance. This API uses an asynchronous callback to return the result.
         *
         * @param { number } groupId - Volume group ID. The default value is **DEFAULT_VOLUME_GROUP_ID**.
         * @param { AsyncCallback<AudioVolumeGroupManager> } callback - Callback used to return the result. If the operation
         *     is successful, **err** is **undefined** and **data** is the VolumeGroupManager instance obtained; otherwise,
         *     **err** is an error object.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @crossplatform [since 12]
         * @since 9
         */
        getVolumeGroupManager(groupId: number, callback: AsyncCallback<AudioVolumeGroupManager>): void;
        /**
         * Obtains a VolumeGroupManager instance. This API uses a promise to return the result.
         *
         * @param { number } groupId - Volume group ID. The default value is **DEFAULT_VOLUME_GROUP_ID**.
         * @returns { Promise<AudioVolumeGroupManager> } Promise used to return the VolumeGroupManager instance.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @crossplatform [since 12]
         * @since 9
         */
        getVolumeGroupManager(groupId: number): Promise<AudioVolumeGroupManager>;
        /**
         * Obtains a VolumeGroupManager instance. This API returns the result synchronously.
         *
         * @param { number } groupId - Volume group ID. The default value is **DEFAULT_VOLUME_GROUP_ID**.
         * @returns { AudioVolumeGroupManager } VolumeGroupManager instance.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified.
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @crossplatform [since 12]
         * @atomicservice [since 23]
         * @since 10
         */
        getVolumeGroupManagerSync(groupId: number): AudioVolumeGroupManager;
        /**
         * Obtains the volume of the application. (The volume range is 0 to 100.) This API uses a promise to return the
         * result.
         *
         * @returns { Promise<number> } Promise used to return the application volume.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @atomicservice [since 23]
         * @since 19
         */
        getAppVolumePercentage(): Promise<number>;
        /**
         * Sets the volume (within a range of 0 to 100) for the application. This API uses a promise to return the result.
         *
         * @param { number } volume - Volume to set.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @throws { BusinessError } 6800301 - Crash or blocking occurs in system process.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @atomicservice [since 23]
         * @since 19
         */
        setAppVolumePercentage(volume: number): Promise<void>;
        /**
         * Subscribes to the system volume change event, which is triggered when the system volume is changed. This API uses
         * an asynchronous callback to return the result.
         *
         * @param { 'volumeChange' } type - Event type. The event **'volumeChange'** is triggered when the system volume is
         *     changed.
         * @param { Callback<VolumeEvent> } callback - Callback used to return the changed volume.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @crossplatform [since 12]
         * @since 9
         * @deprecated since 20
         * @useinstead ohos.multimedia.audio.AudioVolumeManager#event:streamVolumeChange
         */
        on(type: 'volumeChange', callback: Callback<VolumeEvent>): void;
        /**
         * Unsubscribes from the system volume change event. This API uses an asynchronous callback to return the result.
         *
         * @param { 'volumeChange' } type - Event type. The event **'volumeChange'** is triggered when the system volume is
         *     changed.
         * @param { Callback<VolumeEvent> } callback - Callback used to return the changed volume.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters missing;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @since 12
         * @deprecated since 20
         * @useinstead ohos.multimedia.audio.AudioVolumeManager#event:streamVolumeChange
         */
        off(type: 'volumeChange', callback?: Callback<VolumeEvent>): void;
        /**
         * Subscribes to the application-level volume change event of the application (triggered when the application-level
         * volume is changed). This API uses an asynchronous callback to return the result.
         *
         * @param { 'appVolumeChange' } type - Event type. The event **'appVolumeChange'** is triggered when the application
         *     -level volume is changed.
         * @param { Callback<VolumeEvent> } callback - Callback used to return the changed volume.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @since 19
         */
        on(type: 'appVolumeChange', callback: Callback<VolumeEvent>): void;
        /**
         * Unsubscribes from the application-level volume change event of the application. This API uses an asynchronous
         * callback to return the result.
         *
         * @param { 'appVolumeChange' } type - Event type. The event **'appVolumeChange'** is triggered when the application
         *     -level volume is changed.
         * @param { Callback<VolumeEvent> } callback - Callback used to return the changed volume.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @since 19
         */
        off(type: 'appVolumeChange', callback?: Callback<VolumeEvent>): void;
        /**
         * Obtains the volume of a specified audio stream.
         *
         * @param { StreamUsage } streamUsage - Audio stream for which the volume is to be obtained.
         * @returns { number } Volume.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @atomicservice [since 23]
         * @since 20
         */
        getVolumeByStream(streamUsage: StreamUsage): number;
        /**
         * Obtains the minimum volume of a specified audio stream.
         *
         * @param { StreamUsage } streamUsage - Audio stream for which the minimum volume is to be obtained.
         * @returns { number } Volume.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @atomicservice [since 23]
         * @since 20
         */
        getMinVolumeByStream(streamUsage: StreamUsage): number;
        /**
         * Obtains the maximum volume of a specified audio stream.
         *
         * @param { StreamUsage } streamUsage - Audio stream for which the maximum volume is to be obtained.
         * @returns { number } Volume.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @atomicservice [since 23]
         * @since 20
         */
        getMaxVolumeByStream(streamUsage: StreamUsage): number;
        /**
         * Checks whether a specified audio stream is muted.
         *
         * @param { StreamUsage } streamUsage - Audio stream to check.
         * @returns { boolean } Check result for whether the audio stream is muted. **true** if muted, **false** otherwise.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @since 20
         */
        isSystemMutedForStream(streamUsage: StreamUsage): boolean;
        /**
         * Obtains the volume (in dB) calculated by the system based on the audio stream, volume level, and device type.
         *
         * @param { StreamUsage } streamUsage - Audio stream.
         * @param { number } volumeLevel - Volume level.
         * @param { DeviceType } device - Device type.
         * @returns { number } Volume of the audio stream, in dB.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @since 20
         */
        getVolumeInUnitOfDbByStream(streamUsage: StreamUsage, volumeLevel: number, device: DeviceType): number;
        /**
         * Subscribes to the system audio volume change event, which is triggered when the system audio volume is changed.
         * This API uses an asynchronous callback to return the result.
         *
         * @param { 'streamVolumeChange' } type - Event type. The event **'streamVolumeChange'** is triggered when the
         *     system audio volume is changed.
         * @param { StreamUsage } streamUsage - Audio stream usage.
         * @param { Callback<StreamVolumeEvent> } callback - Callback used to return the changed volume.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @since 20
         */
        on(type: 'streamVolumeChange', streamUsage: StreamUsage, callback: Callback<StreamVolumeEvent>): void;
        /**
         * Unsubscribes from the system audio volume change event, which is triggered when the system audio volume is
         * changed. This API uses an asynchronous callback to return the result.
         *
         * @param { 'streamVolumeChange' } type - Event type. The event **'volumeChange'** is triggered when the system
         *     volume is changed.
         * @param { Callback<StreamVolumeEvent> } [callback] - Callback used to return the changed volume.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @since 20
         */
        off(type: 'streamVolumeChange', callback?: Callback<StreamVolumeEvent>): void;
    }
    /**
     * This interface implements volume management for an audio group.
     *
     * Before calling any API in AudioVolumeGroupManager, you must use
     * [getVolumeGroupManager]{@link @ohos.multimedia.audio:audio.AudioVolumeManager.getVolumeGroupManager(groupId: number, callback: AsyncCallback<AudioVolumeGroupManager>)}
     * to obtain an AudioVolumeGroupManager instance.
     *
     * > **NOTE**
     * >
     * > - The initial APIs of this interface are supported since API version 9.
     *
     * @syscap SystemCapability.Multimedia.Audio.Volume
     * @crossplatform [since 12]
     * @since 9
     */
    interface AudioVolumeGroupManager {
        /**
         * Obtains the volume level of a stream. This API uses an asynchronous callback to return the result.
         *
         * @param { AudioVolumeType } volumeType - Audio volume type.
         * @param { AsyncCallback<number> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **data** is the stream volume level obtained; otherwise, **err** is an error
         *     object. The volume range of a specified stream can be obtained by calling
         *     [getMinVolume]{@link audio.AudioVolumeGroupManager.getMinVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>)}
         *     and
         *     [getMaxVolume]{@link audio.AudioVolumeGroupManager.getMaxVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>)}
         *     .
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @crossplatform [since 12]
         * @since 9
         * @deprecated since 20
         * @useinstead ohos.multimedia.audio.AudioVolumeManager#getVolumeByStream
         */
        getVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void;
        /**
         * Obtains the volume level of a stream. This API uses a promise to return the result.
         *
         * @param { AudioVolumeType } volumeType - Audio volume type.
         * @returns { Promise<number> } Promise used to return the stream volume level. The volume range of a specified stream
         *     can be obtained by calling
         *     [getMinVolume]{@link audio.AudioVolumeGroupManager.getMinVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>)}
         *     and
         *     [getMaxVolume]{@link audio.AudioVolumeGroupManager.getMaxVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>)}
         *     .
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @crossplatform [since 12]
         * @since 9
         * @deprecated since 20
         * @useinstead ohos.multimedia.audio.AudioVolumeManager#getVolumeByStream
         */
        getVolume(volumeType: AudioVolumeType): Promise<number>;
        /**
         * Obtains the volume level of a stream. This API returns the result synchronously.
         *
         * @param { AudioVolumeType } volumeType - Audio volume type.
         * @returns { number } Volume level of the stream. The volume range of a specified stream can be obtained by calling
         *     [getMinVolume]{@link audio.AudioVolumeGroupManager.getMinVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>)}
         *     and
         *     [getMaxVolume]{@link audio.AudioVolumeGroupManager.getMaxVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>)}
         *     .
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @crossplatform [since 12]
         * @since 10
         * @deprecated since 20
         * @useinstead ohos.multimedia.audio.AudioVolumeManager#getVolumeByStream
         */
        getVolumeSync(volumeType: AudioVolumeType): number;
        /**
         * Obtains the minimum volume level of a stream. This API uses an asynchronous callback to return the result.
         *
         * @param { AudioVolumeType } volumeType - Audio volume type.
         * @param { AsyncCallback<number> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **data** is the minimum stream volume level obtained; otherwise, **err** is an
         *     error object.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @crossplatform [since 12]
         * @since 9
         * @deprecated since 20
         * @useinstead ohos.multimedia.audio.AudioVolumeManager#getMinVolumeByStream
         */
        getMinVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void;
        /**
         * Obtains the minimum volume level of a stream. This API uses a promise to return the result.
         *
         * @param { AudioVolumeType } volumeType - Audio volume type.
         * @returns { Promise<number> } Promise used to return the minimum volume level.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @crossplatform [since 12]
         * @since 9
         * @deprecated since 20
         * @useinstead ohos.multimedia.audio.AudioVolumeManager#getMinVolumeByStream
         */
        getMinVolume(volumeType: AudioVolumeType): Promise<number>;
        /**
         * Obtains the minimum volume level of a stream. This API returns the result synchronously.
         *
         * @param { AudioVolumeType } volumeType - Audio volume type.
         * @returns { number } Minimum volume level.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @crossplatform [since 12]
         * @since 10
         * @deprecated since 20
         * @useinstead ohos.multimedia.audio.AudioVolumeManager#getMinVolumeByStream
         */
        getMinVolumeSync(volumeType: AudioVolumeType): number;
        /**
         * Obtains the maximum volume level of a stream. This API uses an asynchronous callback to return the result.
         *
         * @param { AudioVolumeType } volumeType - Audio volume type.
         * @param { AsyncCallback<number> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **data** is the maximum stream volume level obtained; otherwise, **err** is an
         *     error object.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @crossplatform [since 12]
         * @since 9
         * @deprecated since 20
         * @useinstead ohos.multimedia.audio.AudioVolumeManager#getMaxVolumeByStream
         */
        getMaxVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void;
        /**
         * Obtains the maximum volume level of a stream. This API uses a promise to return the result.
         *
         * @param { AudioVolumeType } volumeType - Audio volume type.
         * @returns { Promise<number> } Promise used to return the maximum volume level.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @crossplatform [since 12]
         * @since 9
         * @deprecated since 20
         * @useinstead ohos.multimedia.audio.AudioVolumeManager#getMaxVolumeByStream
         */
        getMaxVolume(volumeType: AudioVolumeType): Promise<number>;
        /**
         * Obtains the maximum volume level of a stream. This API returns the result synchronously.
         *
         * @param { AudioVolumeType } volumeType - Audio volume type.
         * @returns { number } Maximum volume level.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @crossplatform [since 12]
         * @since 10
         * @deprecated since 20
         * @useinstead ohos.multimedia.audio.AudioVolumeManager#getMaxVolumeByStream
         */
        getMaxVolumeSync(volumeType: AudioVolumeType): number;
        /**
         * Checks whether a stream is muted. This API uses an asynchronous callback to return the result.
         *
         * @param { AudioVolumeType } volumeType - Audio volume type.
         * @param { AsyncCallback<boolean> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **data** is **true** if the stream is muted or **false** if not muted; otherwise
         *     , **err** is an error object.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @crossplatform [since 12]
         * @since 9
         * @deprecated since 20
         * @useinstead ohos.multimedia.audio.AudioVolumeManager#isSystemMutedForStream
         */
        isMute(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void;
        /**
         * Checks whether a stream is muted. This API uses a promise to return the result.
         *
         * @param { AudioVolumeType } volumeType - Audio volume type.
         * @returns { Promise<boolean> } Promise used to return the result, indicating whether the stream is muted. **true**
         *     if muted, **false** otherwise.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @crossplatform [since 12]
         * @since 9
         * @deprecated since 20
         * @useinstead ohos.multimedia.audio.AudioVolumeManager#isSystemMutedForStream
         */
        isMute(volumeType: AudioVolumeType): Promise<boolean>;
        /**
         * Checks whether a stream is muted. This API returns the result synchronously.
         *
         * @param { AudioVolumeType } volumeType - Audio volume type.
         * @returns { boolean } Check result for whether the stream is muted. **true** if muted, **false** otherwise.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @crossplatform [since 12]
         * @since 10
         * @deprecated since 20
         * @useinstead ohos.multimedia.audio.AudioVolumeManager#isSystemMutedForStream
         */
        isMuteSync(volumeType: AudioVolumeType): boolean;
        /**
         * Obtains the ringer mode. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<AudioRingMode> } callback - Callback used to return the result. If the operation is
         *     successful, **err** is **undefined** and **data** is the ringer mode obtained; otherwise, **err** is an error
         *     object.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @crossplatform [since 12]
         * @since 9
         */
        getRingerMode(callback: AsyncCallback<AudioRingMode>): void;
        /**
         * Obtains the ringer mode. This API uses a promise to return the result.
         *
         * @returns { Promise<AudioRingMode> } Promise used to return the ringer mode.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @crossplatform [since 12]
         * @since 9
         */
        getRingerMode(): Promise<AudioRingMode>;
        /**
         * Obtains the ringer mode. This API returns the result synchronously.
         *
         * @returns { AudioRingMode } Ringer mode.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @crossplatform [since 12]
         * @since 10
         */
        getRingerModeSync(): AudioRingMode;
        /**
         * Subscribes to the ringer mode change event, which is triggered when the
         * [AudioRingMode]{@link @ohos.multimedia.audio:audio.AudioRingMode} changes. This API uses an asynchronous callback
         * to return the result.
         *
         * @param { 'ringerModeChange' } type - Event type. The event **'ringerModeChange'** is triggered when the ringer
         *     mode is changed.
         * @param { Callback<AudioRingMode> } callback - Callback used to return the changed ringer mode.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @since 9
         */
        on(type: 'ringerModeChange', callback: Callback<AudioRingMode>): void;
        /**
         * Unsubscribes from the ringer mode change event. This API uses an asynchronous callback to return the result.
         *
         * @param { 'ringerModeChange' } type - Event type. The event **'ringerModeChange'** is triggered when the ringer
         *     mode is changed.
         * @param { Callback<AudioRingMode> } callback - Callback used to return the changed ringer mode.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @since 18
         */
        off(type: 'ringerModeChange', callback?: Callback<AudioRingMode>): void;
        /**
         * Mutes or unmutes the microphone. This method uses an asynchronous callback to return the result.
         * @permission ohos.permission.MANAGE_AUDIO_CONFIG
         * @param { boolean } mute - Mute status to set. The value true means to mute the microphone, and false means the opposite.
         * @param { AsyncCallback<void> } callback - Callback used to return the result.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @since 9
         * @deprecated since 11
         */
        setMicrophoneMute(mute: boolean, callback: AsyncCallback<void>): void;
        /**
         * Mutes or unmutes the microphone. This method uses a promise to return the result.
         * @permission ohos.permission.MANAGE_AUDIO_CONFIG
         * @param { boolean } mute - Mute status to set. The value true means to mute the microphone, and false means the opposite.
         * @returns { Promise<void> } Promise used to return the result.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @since 9
         * @deprecated since 11
         */
        setMicrophoneMute(mute: boolean): Promise<void>;
        /**
         * Checks whether the microphone is muted. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<boolean> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **data** is **true** if the microphone is muted or **false** if not muted;
         *     otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @crossplatform [since 12]
         * @since 9
         */
        isMicrophoneMute(callback: AsyncCallback<boolean>): void;
        /**
         * Checks whether the microphone is muted. This API uses a promise to return the result.
         *
         * @returns { Promise<boolean> } Promise used to return the result, indicating whether the microphone is muted.
         *     **true** if muted, **false** otherwise.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @crossplatform [since 12]
         * @since 9
         */
        isMicrophoneMute(): Promise<boolean>;
        /**
         * Checks whether the microphone is muted. This API returns the result synchronously.
         *
         * @returns { boolean } Check result for whether the microphone is muted. **true** if muted, **false** otherwise.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @crossplatform [since 12]
         * @since 10
         */
        isMicrophoneMuteSync(): boolean;
        /**
         * Subscribes to the microphone state change event, which is triggered when the microphone state is changed. This
         * API uses an asynchronous callback to return the result.
         *
         * Currently, when multiple AudioManager instances are used in a single process, only the subscription of the last
         * instance takes effect, and the subscription of other instances is overwritten (even if the last instance does not
         * initiate a subscription). Therefore, you are advised to use a single AudioManager instance.
         *
         * @param { 'micStateChange' } type - Event type. The event **'micStateChange'** is triggered when the microphone
         *     state is changed.
         * @param { Callback<MicStateChangeEvent> } callback - Callback used to return the changed microphone state.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @since 9
         */
        on(type: 'micStateChange', callback: Callback<MicStateChangeEvent>): void;
        /**
         * Unsubscribes from the microphone state change event. This API uses an asynchronous callback to return the result.
         *
         * @param { 'micStateChange' } type - Event type. The event **'micStateChange'** is triggered when the microphone
         *     state is changed.
         * @param { Callback<MicStateChangeEvent> } callback - Callback used to return the changed microphone state.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters missing;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @since 12
         */
        off(type: 'micStateChange', callback?: Callback<MicStateChangeEvent>): void;
        /**
         * Checks whether the fixed volume mode is enabled. When the fixed volume mode is enabled, the volume cannot be
         * adjusted. This API returns the result synchronously.
         *
         * @returns { boolean } Check result for whether the fixed volume mode is enabled. **true** if enabled, **false**
         *     otherwise.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @crossplatform [since 12]
         * @since 10
         */
        isVolumeUnadjustable(): boolean;
        /**
         * Obtains the volume gain. This API uses an asynchronous callback to return the result.
         *
         * @param { AudioVolumeType } volumeType - Audio volume type.
         * @param { number } volumeLevel - Volume level.
         * @param { DeviceType } device - Device type.
         * @param { AsyncCallback<number> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **data** is the volume gain obtained; otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed. Return by callback.
         * @throws { BusinessError } 6800301 - System error. Return by callback.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @crossplatform [since 12]
         * @since 10
         * @deprecated since 20
         * @useinstead ohos.multimedia.audio.AudioVolumeManager#getVolumeInUnitOfDbByStream
         */
        getSystemVolumeInDb(volumeType: AudioVolumeType, volumeLevel: number, device: DeviceType, callback: AsyncCallback<number>): void;
        /**
         * Obtains the volume gain. This API uses a promise to return the result.
         *
         * @param { AudioVolumeType } volumeType - Audio volume type.
         * @param { number } volumeLevel - Volume level.
         * @param { DeviceType } device - Device type.
         * @returns { Promise<number> } Promise used to return the volume gain (in dB).
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed. Return by promise.
         * @throws { BusinessError } 6800301 - System error. Return by promise.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @crossplatform [since 12]
         * @since 10
         * @deprecated since 20
         * @useinstead ohos.multimedia.audio.AudioVolumeManager#getVolumeInUnitOfDbByStream
         */
        getSystemVolumeInDb(volumeType: AudioVolumeType, volumeLevel: number, device: DeviceType): Promise<number>;
        /**
         * Obtains the volume gain. This API returns the result synchronously.
         *
         * @param { AudioVolumeType } volumeType - Audio volume type.
         * @param { number } volumeLevel - Volume level.
         * @param { DeviceType } device - Device type.
         * @returns { number } Volume gain (in dB).
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @crossplatform [since 12]
         * @since 10
         * @deprecated since 20
         * @useinstead ohos.multimedia.audio.AudioVolumeManager#getVolumeInUnitOfDbByStream
         */
        getSystemVolumeInDbSync(volumeType: AudioVolumeType, volumeLevel: number, device: DeviceType): number;
        /**
         * Obtains the maximum amplitude (in the range [0, 1]) of the audio stream for an input device. This API uses a
         * promise to return the result.
         *
         * @param { AudioDeviceDescriptor } inputDevice - Descriptor of the target device.
         * @returns { Promise<number> } Promise used to return the maximum amplitude, which is in the range [0, 1].
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed. Return by promise.
         * @throws { BusinessError } 6800301 - System error. Return by promise.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @since 12
         */
        getMaxAmplitudeForInputDevice(inputDevice: AudioDeviceDescriptor): Promise<number>;
        /**
         * Obtains the maximum amplitude (in the range [0, 1]) of the audio stream for an output device. This API uses a
         * promise to return the result.
         *
         * @param { AudioDeviceDescriptor } outputDevice - Descriptor of the target device.
         * @returns { Promise<number> } Promise used to return the maximum amplitude, which is in the range [0, 1].
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed. Return by promise.
         * @throws { BusinessError } 6800301 - System error. Return by promise.
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @since 12
         */
        getMaxAmplitudeForOutputDevice(outputDevice: AudioDeviceDescriptor): Promise<number>;
    }
    /**
     * This interface implements spatial audio management.
     *
     * Before calling any API in AudioSpatializationManager, you must use
     * [getSpatializationManager]{@link @ohos.multimedia.audio:audio.AudioManager.getSpatializationManager} to obtain an
     * AudioSpatializationManager instance.
     *
     * > **NOTE**
     * >
     * > - The initial APIs of this interface are supported since API version 18.
     *
     * @syscap SystemCapability.Multimedia.Audio.Spatialization
     * @since 18
     */
    interface AudioSpatializationManager {
        /**
         * Checks whether spatial audio rendering is enabled for the current device. This API returns the result
         * synchronously.
         *
         * @returns { boolean } Check result for whether spatial audio rendering is enabled. **true** if enabled, **false**
         *     otherwise.
         * @syscap SystemCapability.Multimedia.Audio.Spatialization
         * @since 18
         */
        isSpatializationEnabledForCurrentDevice(): boolean;
        /**
         * Subscribes to the spatial audio rendering status change event of the current device. This API uses an
         * asynchronous callback to return the result.
         *
         * @param { 'spatializationEnabledChangeForCurrentDevice' } type - Event type. The event
         *     **'spatializationEnabledChangeForCurrentDevice'** is triggered when the spatial audio rendering status is
         *     changed.
         * @param { Callback<boolean> } callback - Callback used to return the result, indicating whether spatial audio
         *     rendering is enabled. **true** if enabled, **false** otherwise.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Spatialization
         * @since 18
         */
        on(type: 'spatializationEnabledChangeForCurrentDevice', callback: Callback<boolean>): void;
        /**
         * Unsubscribes from the spatial audio rendering status change event of the current device. This API uses an
         * asynchronous callback to return the result.
         *
         * @param { 'spatializationEnabledChangeForCurrentDevice' } type - Event type. The event
         *     **'spatializationEnabledChangeForCurrentDevice'** is triggered when the spatial audio rendering status is
         *     changed.
         * @param { Callback<boolean> } [callback] - Callback used to return the result, indicating whether spatial audio
         *     rendering is enabled. **true** if enabled, **false** otherwise.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Spatialization
         * @since 18
         */
        off(type: 'spatializationEnabledChangeForCurrentDevice', callback?: Callback<boolean>): void;
    }
    /**
     * Enumerates the noise reduction modes.
     *
     * @syscap SystemCapability.Multimedia.Audio.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    enum NoiseReductionMode {
        /**
         * Fidelity mode, no noise cancellation.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        FIDELITY = 0,
        /**
         * Pure vocals mode, enhanced noise reduction.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        PURE_VOCALS = 1,
        /**
         * Standard mode, weak noise reduction.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        STANDARD = 2
    }
    /**
     * Defines the configuration for the system recording controller panel.
     *
     * @syscap SystemCapability.Multimedia.Audio.Capturer
     * @stagemodelonly
     * @since 26.0.0
     */
    interface SystemRecordControllerConfig {
        /**
         * The system uses this to determine the recording scenario of the application according to
         * the SourceType that the application expects to use for streaming, and provides users with
         * the ability to select matching noise reduction modes. The supported source types include
         * {@link SourceType#SOURCE_TYPE_MIC}, {@link SourceType#SOURCE_TYPE_CAMCORDER}, and
         * {@link SourceType#SOURCE_TYPE_LIVE}.
         *
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @stagemodelonly
         * @since 26.0.0
         */
        sourceType: SourceType;
    }
    /**
     * Provides enhanced audio device management capabilities.
     *
     * @syscap SystemCapability.Multimedia.Audio.DeviceEnhance
     * @stagemodelonly
     * @since 26.0.0
     */
    interface AudioDeviceEnhanceManager {
        /**
        * Queries whether the system supports the enhanced routing functions provided by this manager,
        * including selecting input and output devices for the application or audio streams.
        * Your application is advised to call this API first to confirm system support before using
        * these enhanced routing APIs. Even for the same type of host device, some models may support
        * these functions while others may not due to hardware limitations. If the system does not support
        * these enhanced routing functions, calling them will have no effect, and the system will select
        * default input/output devices for the application or audio streams instead.
        *
        * @returns { boolean } The value true indicates that the system supports enhanced routing functions.
        * @syscap SystemCapability.Multimedia.Audio.DeviceEnhance
        * @stagemodelonly
        * @since 26.0.0
        */
        isEnhancedRoutingSupported(): boolean;
        /**
         * Selects the output device for your application. This setting applies to all playback streams created
         * under your application, unless a specific output device is designated for a particular stream by
         * {@link AudioDeviceEnhanceManager.selectOutputDeviceForAudioRenderer}. When application implements
         * its own UX for output device selection, it can obtain the list of available output devices through
         * {@link AudioRoutingManager.getAvailableDevices}, and use the
         * {@link AudioRoutingManager.getPreferOutputDeviceForRendererInfo} API to obtain the currently
         * selected output device. The selection will become invalid when your application exits or the selected
         * device goes offline. After your application restarts or the device comes back online, your application
         * must re-issue the selection for it to take effect. If the system does not support this function, it will
         * select a default output device for your application.
         *
         * @param { AudioDeviceDescriptor } outputDevice - Audio device descriptor in the array returned by
         *     {@link AudioRoutingManager.getAvailableDevices}.
         * @returns { Promise<void> } Promise used to return the result.
         * @throws { BusinessError } 6800101 - Parameter verification failed, for example,
         *     the selected device does not exist.
         * @throws { BusinessError } 6800301 - Audio service error occurs, such as the service died.
         * @syscap SystemCapability.Multimedia.Audio.DeviceEnhance
         * @stagemodelonly
         * @since 26.0.0
         */
        selectOutputDevice(outputDevice: AudioDeviceDescriptor): Promise<void>;
        /**
         * Selects the input device for your application. This setting applies to all recording streams created
         * under your application, unless a specific input device is designated for a particular stream by
         * {@link AudioDeviceEnhanceManager.selectInputDeviceForAudioCapturer}. When application implements
         * its own UX for input device selection, it can obtain the list of available input devices through
         * {@link AudioRoutingManager.getAvailableDevices}, and use the
         * {@link AudioRoutingManager.getPreferredInputDeviceForCapturerInfo} API to obtain the currently
         * selected input device. The selection will become invalid when your application exits or the selected
         * device goes offline. After your application restarts or the device comes back online, your application
         * must re-issue the selection for it to take effect. If the system does not support this function,
         * it will select a default input device for your application.
         *
         * @param { AudioDeviceDescriptor } inputDevice - Audio device descriptor in the array returned by
         *     {@link AudioRoutingManager.getAvailableDevices}.
         * @returns { Promise<void> } Promise used to return the result.
         * @throws { BusinessError } 6800101 - Parameter verification failed, for example,
         *     the selected device does not exist.
         * @throws { BusinessError } 6800301 - Audio service error occurs, such as the service died.
         * @syscap SystemCapability.Multimedia.Audio.DeviceEnhance
         * @stagemodelonly
         * @since 26.0.0
         */
        selectInputDevice(inputDevice: AudioDeviceDescriptor): Promise<void>;
        /**
         * Selects the output device for the target AudioRenderer. Your application must ensure that the specified
         * AudioRenderer is valid. This selection only applies to the designated stream; other playback streams in
         * your application will use your application's forced selection or the system's default output device.
         * The selection will become invalid when your application exits or the selected device goes offline.
         * After your application restarts or the device comes back online, your application must re-issue the
         * selection for it to take effect. If the system does not support this function, the system will select
         * a default output device for the renderer.
         *
         * @param { AudioRenderer } renderer - The instance of AudioRenderer.
         * @param { AudioDeviceDescriptor } outputDevice - Audio device descriptor in the array returned by
         *     {@link AudioRoutingManager.getAvailableDevices}.
         * @returns { Promise<void> } Promise used to return the result.
         * @throws { BusinessError } 6800101 - Parameter verification failed, for example,
         *     the selected device does not exist.
         * @throws { BusinessError } 6800301 - Audio service error occurs, such as the service died.
         * @syscap SystemCapability.Multimedia.Audio.DeviceEnhance
         * @stagemodelonly
         * @since 26.0.0
         */
        selectOutputDeviceForAudioRenderer(renderer: AudioRenderer, outputDevice: AudioDeviceDescriptor): Promise<void>;
        /**
         * Selects the input device for the target AudioCapturer. Your application must ensure that the specified
         * AudioCapturer is valid. This selection only applies to the designated stream; other recording streams in
         * your application will use your application's forced selection or the system's default input device.
         * The selection will become invalid when your application exits or the selected device goes offline.
         * After your application restarts or the device comes back online, your application must re-issue the
         * selection for it to take effect. If the system does not support this function, the system will select
         * a default input device for the capturer.
         *
         * @param { AudioCapturer } capturer - The instance of AudioCapturer.
         * @param { AudioDeviceDescriptor } inputDevice - Audio device descriptor in the array returned by
         *     {@link AudioRoutingManager.getAvailableDevices}.
         * @returns { Promise<void> } Promise used to return the result.
         * @throws { BusinessError } 6800101 - Parameter verification failed, for example,
         *     the selected device does not exist.
         * @throws { BusinessError } 6800301 - Audio service error occurs, such as the service died.
         * @syscap SystemCapability.Multimedia.Audio.DeviceEnhance
         * @stagemodelonly
         * @since 26.0.0
         */
        selectInputDeviceForAudioCapturer(capturer: AudioCapturer, inputDevice: AudioDeviceDescriptor): Promise<void>;
    }
    /**
     * Provides recording strategy management, including collaborative recording
     * and recording control capabilities.
     *
     * @syscap SystemCapability.Multimedia.Audio.Capturer
     * @stagemodelonly
     * @since 26.0.0
     */
    interface AudioRecordingManager {
        /**
         * Enables or disables the system recording controller panel.
         * The application can call this API to pull up the recording controller panel before starting the recording stream,
         * allowing the user to finish selecting the recording device or audio effect parameters.
         * The recording service can then be started to avoid inconsistent audio effects caused by switching during the
         * recording process.
         * The application must be in the foreground to enable the panel; the enable operation does not take effect
         * if the application is in the background. Disabling the panel is not restricted by the application's
         * foreground or background status.
         * The API uses a promise to return the result.
         *
         * @param { boolean } show - A boolean value indicating whether to show (true) or hide (false)
         *     the system recording controller panel.
         * @param { SystemRecordControllerConfig } config - Configuration for the system recording controller panel.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @throws { BusinessError } 6800301 - Audio service error occurs like service died.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @stagemodelonly
         * @since 26.0.0
         */
        enableSystemRecordController(show: boolean, config: SystemRecordControllerConfig): Promise<void>;
    }
    /**
     * Provides audio debug management capabilities.
     *
     * @syscap SystemCapability.Multimedia.Audio.Core
     * @stagemodelonly
     * @since 26.0.0
     */
    interface AudioDebuggingManager {
        /**
         * Prints full audio runtime snapshot for current app process.
         * The snapshot will contain all audio renderers, capturers, audio session information.
         * Note that the information details and format may vary from different version, it can only be used for
         * manual debugging, user should not rely on the information for actual function realization or file
         * content extraction.
         *
         * @param { number } fd - fd is a file descriptor, indicates the location that the snapshot information will be
         *     written to. If the fd is less than 0 or no writable, the snapshot information will be printed into the
         *     running log, otherwise the snapshot will be written into the file.
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        printAppInfo(fd: number): void;
        /**
         * Prints full audio runtime snapshot for target audio renderer instance.
         * The snapshot will contain the stream, pipe, volume and device information.
         * Note that the information details and format may vary from different version, it can only be used for
         * manual debugging, user should not rely on the information for actual function realization or file
         * content extraction.
         *
         * @param { AudioRenderer } renderer - target audio renderer instance to print snapshot.
         * @param { number } fd - fd is a file descriptor, indicates the location that the snapshot information will be
         *     written to. If the fd is less than 0 or no writable, the snapshot information will be printed into the
         *     running log, otherwise the snapshot will be written into the file.
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        printRendererInfo(renderer: AudioRenderer, fd: number): void;
        /**
         * Prints full audio runtime snapshot for target audio capturer instance.
         * The snapshot will contain the stream, pipe, volume and device information.
         * Note that the information details and format may vary from different version, it can only be used for
         * manual debugging, user should not rely on the information for actual function realization or file
         * content extraction.
         *
         * @param { AudioCapturer } capturer - target audio capturer instance to print snapshot.
         * @param { number } fd - fd is a file descriptor, indicates the location that the snapshot information will be
         *     written to. If the fd is less than 0 or no writable, the snapshot information will be printed into the
         *     running log, otherwise the snapshot will be written into the file.
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        printCapturerInfo(capturer: AudioCapturer, fd: number): void;
        /**
         * Prints full audio runtime snapshot for target audio loopback instance.
         * The snapshot will contain the loopback status, device and effect information.
         * Note that the information details and format may vary from different version, it can only be used for
         * manual debugging, user should not rely on the information for actual function realization or file
         * content extraction.
         *
         * @param { AudioLoopback } loopback - target audio loopback instance to print snapshot.
         * @param { number } fd - fd is a file descriptor, indicates the location that the snapshot information will be
         *     written to. If the fd is less than 0 or no writable, the snapshot information will be printed into the
         *     running log, otherwise the snapshot will be written into the file.
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        printLoopbackInfo(loopback: AudioLoopback, fd: number): void;
        /**
         * Prints full audio runtime snapshot for target audio session manager instance.
         * The snapshot will contain the session status, scene, strategy and device information.
         * Note that the information details and format may vary from different version, it can only be used for
         * manual debugging, user should not rely on the information for actual function realization or file
         * content extraction.
         *
         * @param { AudioSessionManager } session - target audio session manager instance to print snapshot.
         * @param { number } fd - fd is a file descriptor, indicates the location that the snapshot information will be
         *     written to. If the fd is less than 0 or no writable, the snapshot information will be printed into the
         *     running log, otherwise the snapshot will be written into the file.
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @stagemodelonly
         * @since 26.0.0
         */
        printSessionInfo(session: AudioSessionManager, fd: number): void;
    }
    /**
     * Defines an AudioRendererChangeInfo array, which is read-only.
     *
     * @syscap SystemCapability.Multimedia.Audio.Renderer
     * @crossplatform [since 12]
     * @since 9
     */
    type AudioRendererChangeInfoArray = Array<Readonly<AudioRendererChangeInfo>>;
    /**
     * Describes the audio renderer change event.
     *
     * @syscap SystemCapability.Multimedia.Audio.Renderer
     * @crossplatform [since 12]
     * @since 9
     */
    interface AudioRendererChangeInfo {
        /**
         * Unique ID of an audio stream.
         *
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 9
         */
        readonly streamId: number;
        /**
         * Audio renderer information.
         *
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 9
         */
        readonly rendererInfo: AudioRendererInfo;
        /**
         * Audio device description.
         *
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 9
         */
        readonly deviceDescriptors: AudioDeviceDescriptors;
    }
    /**
     * Defines an AudioCapturerChangeInfo array, which is read-only.
     *
     * @syscap SystemCapability.Multimedia.Audio.Capturer
     * @crossplatform [since 12]
     * @since 9
     */
    type AudioCapturerChangeInfoArray = Array<Readonly<AudioCapturerChangeInfo>>;
    /**
     * Describes the audio capturer change event.
     *
     * @syscap SystemCapability.Multimedia.Audio.Capturer
     * @crossplatform [since 12]
     * @since 9
     */
    interface AudioCapturerChangeInfo {
        /**
         * Unique ID of an audio stream.
         *
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @crossplatform [since 12]
         * @since 9
         */
        readonly streamId: number;
        /**
         * Audio capturer information.
         *
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @crossplatform [since 12]
         * @since 9
         */
        readonly capturerInfo: AudioCapturerInfo;
        /**
         * Audio device information.
         *
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @crossplatform [since 12]
         * @since 9
         */
        readonly deviceDescriptors: AudioDeviceDescriptors;
        /**
         * Whether the audio capturer is muted. **true** if muted, **false** otherwise.
         *
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @crossplatform [since 12]
         * @since 11
         */
        readonly muted?: boolean;
    }
    /**
     * Describes an audio device.
     *
     * @syscap SystemCapability.Multimedia.Audio.Device
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 7
     */
    interface AudioDeviceDescriptor {
        /**
         * Device role.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 7
         */
        readonly deviceRole: DeviceRole;
        /**
         * Device type.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 7
         */
        readonly deviceType: DeviceType;
        /**
         * Audio device id.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        readonly id: number;
        /**
         * Device name.
         *
         * For a Bluetooth device, you must request the ohos.permission.USE_BLUETOOTH permission.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        readonly name: string;
        /**
         * Static MAC address of the device.
         *
         * For a Bluetooth device, you must request the ohos.permission.USE_BLUETOOTH permission.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        readonly address: string;
        /**
         * Supported sampling rates.
         *
         * SystemCapability.Multimedia.Audio.Device
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        readonly sampleRates: Array<number>;
        /**
         * Number of channels supported.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        readonly channelCounts: Array<number>;
        /**
         * Supported channel masks.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 9
         */
        readonly channelMasks: Array<number>;
        /**
         * Display name of the device.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 10
         */
        readonly displayName: string;
        /**
         * Supported encoding types.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 11
         */
        readonly encodingTypes?: Array<AudioEncodingType>;
        /**
         * Whether the device supports spatial audio rendering. **true** if supported, **false** otherwise.
         *
         * @syscap SystemCapability.Multimedia.Audio.Spatialization
         * @since 18
         */
        readonly spatializationSupported?: boolean;
        /**
         * Model of the device.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 22
         */
        readonly model?: string;
        /**
         * Audio stream capabilities supported by the device.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 22
         */
        readonly capabilities?: Array<AudioStreamInfo>;
    }
    /**
     * Defines an [AudioDeviceDescriptor]{@link @ohos.multimedia.audio:audio.AudioDeviceDescriptor} array, which is read-
     * only.
     *
     * @syscap SystemCapability.Multimedia.Audio.Device
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 7
     */
    type AudioDeviceDescriptors = Array<Readonly<AudioDeviceDescriptor>>;
    /**
     * Enumerates the audio volume modes.
     *
     * @syscap SystemCapability.Multimedia.Audio.Volume
     * @since 19
     */
    enum AudioVolumeMode {
        /**
         * System-level volume (default mode).
         *
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @since 19
         */
        SYSTEM_GLOBAL = 0,
        /**
         * Application-level volume.
         *
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @since 19
         */
        APP_INDIVIDUAL = 1
    }
    /**
     * Describes the event received by the application when the volume is changed.
     *
     * @syscap SystemCapability.Multimedia.Audio.Volume
     * @crossplatform [since 12]
     * @since 9
     */
    interface VolumeEvent {
        /**
         * Audio volume type.
         *
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @since 9
         */
        volumeType: AudioVolumeType;
        /**
         * Volume to set. The value range can be obtained by calling **getMinVolume** and **getMaxVolume**.
         *
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @crossplatform [since 12]
         * @since 9
         */
        volume: number;
        /**
         * Whether to show the volume change in UI. **true** to show, **false** otherwise.
         *
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @since 9
         */
        updateUi: boolean;
        /**
         * Audio volume mode. The default value is **SYSTEM_GLOBAL**.
         *
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @since 19
         */
        volumeMode?: AudioVolumeMode;
    }
    /**
     * Describes the event received by the application when the audio stream volume is changed.
     *
     * @syscap SystemCapability.Multimedia.Audio.Volume
     * @since 20
     */
    interface StreamVolumeEvent {
        /**
         * Audio stream for which the volume changes.
         *
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @since 20
         */
        streamUsage: StreamUsage;
        /**
         * Volume.
         *
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @since 20
         */
        volume: number;
        /**
         * Whether to show the volume change in UI. **true** to show, **false** otherwise.
         *
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @since 20
         */
        updateUi: boolean;
        /**
         * Volume level before change.
         *
         * @syscap SystemCapability.Multimedia.Audio.Volume
         * @since 23
         */
        previousVolume?: number;
    }
    /**
     * Describes the callback invoked for audio interruption or focus gain events.When the audio of an application
     * is interrupted by another application, the callback is invoked to notify the former application.
     *
     * @syscap SystemCapability.Multimedia.Audio.Renderer
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.multimedia.audio.InterruptEvent
     */
    interface InterruptAction {
        /**
         * Event type.
         * The value TYPE_ACTIVATED means the focus gain event, and TYPE_INTERRUPT means the audio interruption event.
         *
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.multimedia.audio.InterruptEvent#eventType
         */
        actionType: InterruptActionType;
        /**
         * Type of the audio interruption event.
         *
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.multimedia.audio.InterruptEvent#eventType
         */
        type?: InterruptType;
        /**
         * Hint provided along with the audio interruption event.
         *
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.multimedia.audio.InterruptEvent#hintType
         */
        hint?: InterruptHint;
        /**
         * Whether the focus is gained or released. **true** if the focus is gained or released, **false** if the focus
         * fails to be gained or released.
         *
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.multimedia.audio.InterruptEvent#hintType
         */
        activated?: boolean;
    }
    /**
     * Describes input parameters of audio interruption events.
     *
     * @syscap SystemCapability.Multimedia.Audio.Renderer
     * @since 7
     * @deprecated since 9
     * @useinstead ohos.multimedia.audio.AudioRendererOptions
     */
    interface AudioInterrupt {
        /**
         * Audio stream usage.
         *
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.multimedia.audio.AudioRendererOptions#rendererInfo
         */
        streamUsage: StreamUsage;
        /**
         * Audio content type.
         *
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.multimedia.audio.AudioRendererOptions#rendererInfo
         */
        contentType: ContentType;
        /**
         * Whether audio playback can be paused during an audio interruption. **true** if audio playback can be paused,
         * **false** otherwise.
         *
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @since 7
         * @deprecated since 9
         * @useinstead ohos.multimedia.audio.InterruptEvent#hintType
         */
        pauseWhenDucked: boolean;
    }
    /**
     * Describes the event received by the application when the microphone mute status is changed.
     *
     * @syscap SystemCapability.Multimedia.Audio.Device
     * @since 9
     */
    interface MicStateChangeEvent {
        /**
         * Mute status of the microphone **true** if muted, **false** otherwise.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 9
         */
        mute: boolean;
    }
    /**
     * Describes the device connection status and device information.
     *
     * @syscap SystemCapability.Multimedia.Audio.Device
     * @crossplatform [since 12]
     * @since 7
     */
    interface DeviceChangeAction {
        /**
         * Device change type.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @since 7
         */
        type: DeviceChangeType;
        /**
         * Device information.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @since 7
         */
        deviceDescriptors: AudioDeviceDescriptors;
    }
    /**
     * Enumerates the audio channel blending modes.
     *
     * @syscap SystemCapability.Multimedia.Audio.Core
     * @crossplatform [since 12]
     * @since 11
     */
    enum ChannelBlendMode {
        /**
         * No channel process.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 11
         */
        MODE_DEFAULT = 0,
        /**
         * Blends the left and right channels together.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 11
         */
        MODE_BLEND_LR = 1,
        /**
         * Copies the left channel and applies it to both the left and right channels.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 11
         */
        MODE_ALL_LEFT = 2,
        /**
         * Copies the right channel and applies it to both the left and right channels.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 11
         */
        MODE_ALL_RIGHT = 3
    }
    /**
     * Enumerates the reasons for audio stream device changes.
     *
     * @syscap SystemCapability.Multimedia.Audio.Device
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 11
     */
    enum AudioStreamDeviceChangeReason {
        /**
         * Unknown reason.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 11
         */
        REASON_UNKNOWN = 0,
        /**
         * A new device is available.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 11
         */
        REASON_NEW_DEVICE_AVAILABLE = 1,
        /**
         * The old device is unavailable. When this reason is reported, consider pausing audio playback.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 11
         */
        REASON_OLD_DEVICE_UNAVAILABLE = 2,
        /**
         * Forcibly selected.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 11
         */
        REASON_OVERRODE = 3,
        /**
         * The audio session has been activated.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 20
         */
        REASON_SESSION_ACTIVATED = 4,
        /**
         * An audio stream with higher priority appears.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @since 20
         */
        REASON_STREAM_PRIORITY_CHANGED = 5
    }
    /**
     * Describes the event received by the application when the audio stream device is changed.
     *
     * @syscap SystemCapability.Multimedia.Audio.Device
     * @crossplatform [since 12]
     * @atomicservice [since 12]
     * @since 11
     */
    interface AudioStreamDeviceChangeInfo {
        /**
         * Audio device descriptors before change.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @stagemodelonly
         * @atomicservice
         * @since 26.0.0
         */
        preDevices?: AudioDeviceDescriptors;
        /**
         * Audio device descriptors after change.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 11
         */
        devices: AudioDeviceDescriptors;
        /**
         * Audio stream device change reason.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @atomicservice [since 12]
         * @since 11
         */
        changeReason: AudioStreamDeviceChangeReason;
    }
    /**
     * Enumerates the audio data callback results.
     *
     * @syscap SystemCapability.Multimedia.Audio.Core
     * @crossplatform
     * @since 12
     */
    enum AudioDataCallbackResult {
        /**
         * The callback data is invalid.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform
         * @since 12
         */
        INVALID = -1,
        /**
         * The callback data is valid.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform
         * @since 12
         */
        VALID = 0
    }
    /**
     * Defines the callback function used to write data to the audio renderer. Once the callback function finishes its
     * execution, the audio service queues the data pointed to by **data** for playback. Therefore, do not change the data
     * outside the callback. It is crucial to fill **data** with the exact length of data designated for playback;
     * otherwise, noises may occur during playback.
     *
     * @param { ArrayBuffer } data - Data to be written to the buffer.
     * @returns { AudioDataCallbackResult | void } If **void** or **AudioDataCallbackResult.VALID** is returned, the data
     *     is valid and the audio data is played. If **AudioDataCallbackResult.INVALID** is returned, the data is invalid
     *     and the audio data is not played.
     * @syscap SystemCapability.Multimedia.Audio.Renderer
     * @crossplatform
     * @since 12
     */
    type AudioRendererWriteDataCallback = (data: ArrayBuffer) => AudioDataCallbackResult | void;
    /**
     * Describes the information about the audio stream timestamp and the current data frame position.
     *
     * @syscap SystemCapability.Multimedia.Audio.Core
     * @since 19
     */
    interface AudioTimestampInfo {
        /**
         * Position of the current data frame for playback or recording.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 19
         */
        readonly framePos: number;
        /**
         * Timestamp corresponding to the current data frame position during playback or recording, in nanoseconds.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 19
         */
        readonly timestamp: number;
    }
    /**
     * Enumerates the audio latency types.
     *
     * @syscap SystemCapability.Multimedia.Audio.Core
     * @stagemodelonly
     * @since 23
     */
    enum AudioLatencyType {
        /**
         * Type to get latency of all audio processing units, including software and hardware.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @stagemodelonly
         * @since 23
         */
        LATENCY_TYPE_ALL = 0,
        /**
         * Type to get latency of software part, including audio effects in software.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @stagemodelonly
         * @since 23
         */
        LATENCY_TYPE_SOFTWARE = 1,
        /**
         * Type to get latency of hardware part, including audio effects in hal, driver and hardware.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @stagemodelonly
         * @since 23
         */
        LATENCY_TYPE_HARDWARE = 2
    }
    /**
     * This interface provides APIs for audio rendering.
     *
     * Before calling any API in AudioRenderer, you must use
     * [createAudioRenderer]{@link @ohos.multimedia.audio:audio.createAudioRenderer(options: AudioRendererOptions, callback: AsyncCallback<AudioRenderer>)}
     * to create an AudioRenderer instance.
     *
     * > **NOTE**
     * >
     * > - The initial APIs of this interface are supported since API version 8.
     *
     * @syscap SystemCapability.Multimedia.Audio.Renderer
     * @crossplatform [since 12]
     * @since 8
     */
    interface AudioRenderer {
        /**
         * Audio renderer state.
         *
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 8
         */
        readonly state: AudioState;
        /**
         * Obtains the information about this audio renderer. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<AudioRendererInfo> } callback - Callback used to return the result. If the operation is
         *     successful, **err** is **undefined** and **data** is the audio renderer information obtained; otherwise,
         *     **err** is an error object.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 8
         */
        getRendererInfo(callback: AsyncCallback<AudioRendererInfo>): void;
        /**
         * Obtains the information about this audio renderer. This API uses a promise to return the result.
         *
         * @returns { Promise<AudioRendererInfo> } Promise used to return the audio renderer information.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 8
         */
        getRendererInfo(): Promise<AudioRendererInfo>;
        /**
         * Obtains the information about this audio renderer. This API returns the result synchronously.
         *
         * @returns { AudioRendererInfo } Audio renderer information.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 10
         */
        getRendererInfoSync(): AudioRendererInfo;
        /**
         * Obtains the stream information of this audio renderer. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { AsyncCallback<AudioStreamInfo> } callback - Callback used to return the result. If the operation is
         *     successful, **err** is **undefined** and **data** is the stream information obtained; otherwise, **err** is
         *     an error object.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 8
         */
        getStreamInfo(callback: AsyncCallback<AudioStreamInfo>): void;
        /**
         * Obtains the stream information of this audio renderer. This API uses a promise to return the result.
         *
         * @returns { Promise<AudioStreamInfo> } Promise used to return the stream information.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 8
         */
        getStreamInfo(): Promise<AudioStreamInfo>;
        /**
         * Obtains the stream information of this audio renderer. This API returns the result synchronously.
         *
         * @returns { AudioStreamInfo } Stream information.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 10
         */
        getStreamInfoSync(): AudioStreamInfo;
        /**
         * Obtains the stream ID of this audio renderer. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<number> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **data** is the stream ID obtained; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 9
         */
        getAudioStreamId(callback: AsyncCallback<number>): void;
        /**
         * Obtains the stream ID of this audio renderer. This API uses a promise to return the result.
         *
         * @returns { Promise<number> } Promise used to return the stream ID.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 9
         */
        getAudioStreamId(): Promise<number>;
        /**
         * Obtains the stream ID of this audio renderer. This API returns the result synchronously.
         *
         * @returns { number } Stream ID.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 10
         */
        getAudioStreamIdSync(): number;
        /**
         * Obtains the audio effect mode in use. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<AudioEffectMode> } callback - Callback used to return the result. If the operation is
         *     successful, **err** is **undefined** and **data** is the audio effect mode obtained; otherwise, **err** is an
         *     error object.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @since 10
         */
        getAudioEffectMode(callback: AsyncCallback<AudioEffectMode>): void;
        /**
         * Obtains the audio effect mode in use. This API uses a promise to return the result.
         *
         * @returns { Promise<AudioEffectMode> } Promise used to return the audio effect mode.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @since 10
         */
        getAudioEffectMode(): Promise<AudioEffectMode>;
        /**
         * Sets an audio effect mode. This API uses an asynchronous callback to return the result.
         *
         * @param { AudioEffectMode } mode - Audio effect mode to set.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed. Return by callback.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @since 10
         */
        setAudioEffectMode(mode: AudioEffectMode, callback: AsyncCallback<void>): void;
        /**
         * Sets an audio effect mode. This API uses a promise to return the result.
         *
         * @param { AudioEffectMode } mode - Audio effect mode to set.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed. Return by promise.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @since 10
         */
        setAudioEffectMode(mode: AudioEffectMode): Promise<void>;
        /**
         * Starts this audio renderer. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object. If the operation fails, an error object with
         *     one of the following error codes is returned:<br>Error code 6800301: indicates abnormal status, focus
         *     preemption failure, and abnormal system processing. For details, see system logs.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 8
         */
        start(callback: AsyncCallback<void>): void;
        /**
         * Starts this audio renderer. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise object, which indicates that the renderer is started successfully. If the
         *     operation fails, an error object with one of the following error codes is returned:
         *     <br>Error code 6800301: indicates abnormal status, focus preemption failure, and abnormal system processing. For
         *     details, see system logs.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 8
         */
        start(): Promise<void>;
        /**
         * Writes the buffer. This API uses an asynchronous callback to return the result.
         *
         * @param { ArrayBuffer } buffer - Data to be written to the buffer.
         * @param { AsyncCallback<number> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **data** is the number of bytes written; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @since 8
         * @deprecated since 11
         * @useinstead ohos.multimedia.audio.AudioRenderer#event:writeData
         */
        write(buffer: ArrayBuffer, callback: AsyncCallback<number>): void;
        /**
         * Writes the buffer. This API uses a promise to return the result.
         *
         * @param { ArrayBuffer } buffer - Data to be written to the buffer.
         * @returns { Promise<number> } Promise used to return the number of written bytes.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @since 8
         * @deprecated since 11
         * @useinstead ohos.multimedia.audio.AudioRenderer#event:writeData
         */
        write(buffer: ArrayBuffer): Promise<number>;
        /**
         * Obtains the timestamp of the current playback position, measured in nanoseconds from the Unix epoch (January 1, 1
         * 970). This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<number> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **data** is the number of nanoseconds obtained; otherwise, **err** is an error
         *     object.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 8
         */
        getAudioTime(callback: AsyncCallback<number>): void;
        /**
         * Obtains the timestamp of the current playback position, measured in nanoseconds from the Unix epoch (January 1, 1
         * 970). This API uses a promise to return the result.
         *
         * @returns { Promise<number> } Promise used to return the timestamp.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 8
         */
        getAudioTime(): Promise<number>;
        /**
         * Obtains the timestamp of the current playback position, measured in nanoseconds from the Unix epoch (January 1, 1
         * 970). This API returns the result synchronously.
         *
         * @returns { number } Timestamp.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 10
         */
        getAudioTimeSync(): number;
        /**
         * Obtains the timestamp and position information of an output audio stream. It adapts to the speed adjustment
         * interface. This API uses a promise to return the result.
         *
         * This information is commonly used for audio and video synchronization.
         *
         * Note that when the actual playback position (**framePosition**) is 0, the timestamp remains fixed until the
         * stream begins to play. The playback position is also reset when **Flush** is called.
         *
         * Additionally, changes in the audio stream route, such as switching devices or output types, will reset the
         * playback position, whereas the timestamp keeps increasing. You are advised to call this API to obtain the
         * corresponding value only when the actual playback position and timestamp are stable. This API adapts to the speed
         * adjustment interface. For example, if the playback speed is set to 2x, the rate at which the playback position
         * increases is also twice the normal speed.
         *
         * @returns { Promise<AudioTimestampInfo> } Promise used to return the audio stream timestamp and the current data
         *     frame position.
         * @throws  { BusinessError } 6800103 - Operation not permit at current state.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @since 19
         */
        getAudioTimestampInfo(): Promise<AudioTimestampInfo>;
        /**
         * Obtains the timestamp and position information of an output audio stream. It adapts to the speed adjustment
         * interface. This API returns the result synchronously.
         *
         * This information is commonly used for audio and video synchronization.
         *
         * Note that when the actual playback position (**framePosition**) is 0, the timestamp remains fixed until the
         * stream begins to play. The playback position is also reset when **Flush** is called.
         *
         * Additionally, changes in the audio stream route, such as switching devices or output types, will reset the
         * playback position, whereas the timestamp keeps increasing. You are advised to call this API to obtain the
         * corresponding value only when the actual playback position and timestamp are stable. This API adapts to the speed
         * adjustment interface. For example, if the playback speed is set to 2x, the rate at which the playback position
         * increases is also twice the normal speed.
         * @returns { AudioTimestampInfo } Information about the audio stream timestamp and the current data frame position.
         * @throws { BusinessError } 6800103 - Operation not permit at current state.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @since 19
         */
        getAudioTimestampInfoSync(): AudioTimestampInfo;
        /**
         * Drains the playback buffer. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 8
         */
        drain(callback: AsyncCallback<void>): void;
        /**
         * Drains the playback buffer. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 8
         */
        drain(): Promise<void>;
        /**
         * Flushes the buffer. This API is available when [AudioState]{@link @ohos.multimedia.audio:audio.AudioState} is
         * **STATE_RUNNING**, **STATE_PAUSED**, or **STATE_STOPPED**. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 6800103 - Operation not permit at current state. Return by promise.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 11
         */
        flush(): Promise<void>;
        /**
         * Pauses this audio renderer. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 8
         */
        pause(callback: AsyncCallback<void>): void;
        /**
         * Pauses this audio renderer. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 8
         */
        pause(): Promise<void>;
        /**
         * Stops this audio renderer. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 8
         */
        stop(callback: AsyncCallback<void>): void;
        /**
         * Stops this audio renderer. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 8
         */
        stop(): Promise<void>;
        /**
         * Releases the renderer. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 8
         */
        release(callback: AsyncCallback<void>): void;
        /**
         * Releases the renderer. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 8
         */
        release(): Promise<void>;
        /**
         * Obtains a reasonable minimum buffer size in bytes for rendering. This API uses an asynchronous callback to return
         * the result.
         *
         * @param { AsyncCallback<number> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **data** is the minimum buffer size obtained; otherwise, **err** is an error
         *     object.<br>The unit is bytes.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 8
         */
        getBufferSize(callback: AsyncCallback<number>): void;
        /**
         * Obtains a reasonable minimum buffer size in bytes for rendering. This API uses a promise to return the result.
         *
         * @returns { Promise<number> } Promise used to return the buffer size.
         *     <br>The unit is bytes.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 8
         */
        getBufferSize(): Promise<number>;
        /**
         * Obtains a reasonable minimum buffer size in bytes for rendering. This API returns the result synchronously.
         *
         * @returns { number } Buffer size, in bytes.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 10
         */
        getBufferSizeSync(): number;
        /**
         * Sets the render rate. This API uses an asynchronous callback to return the result.
         *
         * @param { AudioRendererRate } rate - Audio render rate.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @since 8
         * @deprecated since 11
         * @useinstead ohos.multimedia.audio.AudioRenderer#setSpeed
         */
        setRenderRate(rate: AudioRendererRate, callback: AsyncCallback<void>): void;
        /**
         * Sets the render rate. This API uses a promise to return the result.
         *
         * @param { AudioRendererRate } rate - Audio render rate.
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @since 8
         * @deprecated since 11
         * @useinstead ohos.multimedia.audio.AudioRenderer#setSpeed
         */
        setRenderRate(rate: AudioRendererRate): Promise<void>;
        /**
         * Sets the playback speed.
         *
         * @param { number } speed - Playback rate, which ranges from 0.25 to 4.0.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 11
         */
        setSpeed(speed: number): void;
        /**
         * Obtains the audio renderer rate. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<AudioRendererRate> } callback - Callback used to return the result. If the operation is
         *     successful, **err** is **undefined** and **data** is the render rate obtained; otherwise, **err** is an error
         *     object.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @since 8
         * @deprecated since 11
         * @useinstead ohos.multimedia.audio.AudioRenderer#getSpeed
         */
        getRenderRate(callback: AsyncCallback<AudioRendererRate>): void;
        /**
         * Obtains the audio renderer rate. This API uses a promise to return the result.
         *
         * @returns { Promise<AudioRendererRate> } Promise used to return the render rate.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @since 8
         * @deprecated since 11
         * @useinstead ohos.multimedia.audio.AudioRenderer#getSpeed
         */
        getRenderRate(): Promise<AudioRendererRate>;
        /**
         * Obtains the audio renderer rate. This API returns the result synchronously.
         *
         * @returns { AudioRendererRate } Audio render rate.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @since 10
         * @deprecated since 11
         * @useinstead ohos.multimedia.audio.AudioRenderer#getSpeed
         */
        getRenderRateSync(): AudioRendererRate;
        /**
         * Obtains the playback speed.
         *
         * @returns { number } Playback rate, which ranges from 0.25 to 4.0.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 11
         */
        getSpeed(): number;
        /**
         * Sets the audio interruption mode for the application. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { InterruptMode } mode - Audio interruption mode.
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Audio.Interrupt
         * @crossplatform [since 12]
         * @since 9
         */
        setInterruptMode(mode: InterruptMode, callback: AsyncCallback<void>): void;
        /**
         * Sets the audio interruption mode for the application. This API uses a promise to return the result.
         *
         * @param { InterruptMode } mode - Audio interruption mode.
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Multimedia.Audio.Interrupt
         * @crossplatform [since 12]
         * @since 9
         */
        setInterruptMode(mode: InterruptMode): Promise<void>;
        /**
         * Sets the audio interruption mode for the application. This API returns the result synchronously.
         *
         * @param { InterruptMode } mode - Audio interruption mode.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Interrupt
         * @crossplatform [since 12]
         * @since 10
         */
        setInterruptModeSync(mode: InterruptMode): void;
        /**
         * Sets the volume for the audio stream. This API uses an asynchronous callback to return the result.
         *
         * @param { number } volume - Volume to set, which is in the range [0.0, 1.0].
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 9
         */
        setVolume(volume: number, callback: AsyncCallback<void>): void;
        /**
         * Sets the volume for the audio stream. This API uses a promise to return the result.
         *
         * @param { number } volume - Volume to set, which is in the range [0.0, 1.0].
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 9
         */
        setVolume(volume: number): Promise<void>;
        /**
         * Obtains the volume of the audio stream. This API returns the result synchronously.
         *
         * @returns { number } Volume, in the range [0.0, 1.0].
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @since 12
         */
        getVolume(): number;
        /**
         * Sets a volume ramp. This API returns the result synchronously.
         *
         * @param { number } volume - Target volume, within the range [0.0, 1.0].
         * @param { number } duration - Time range during which the ramp applies, in ms.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 11
         */
        setVolumeWithRamp(volume: number, duration: number): void;
        /**
         * Obtains the minimum volume of the audio stream. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<number> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **data** is the minimum volume obtained; otherwise, **err** is an error object.<
         *     br>The volume range is [0.0, 1.0].
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 10
         */
        getMinStreamVolume(callback: AsyncCallback<number>): void;
        /**
         * Obtains the minimum volume of the audio stream. This API uses a promise to return the result.
         *
         * @returns { Promise<number> } Promise used to return the minimum volume of the audio stream.
         *     <br>The volume range is [0.0, 1.0].
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 10
         */
        getMinStreamVolume(): Promise<number>;
        /**
         * Obtains the minimum volume of the audio stream. This API returns the result synchronously.
         *
         * @returns { number } Minimum volume of the audio stream, which ranges from 0.0 to 1.0.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 10
         */
        getMinStreamVolumeSync(): number;
        /**
         * Obtains the maximum volume of the audio stream. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<number> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **data** is the maximum volume obtained; otherwise, **err** is an error object.<
         *     br>The volume range is [0.0, 1.0].
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 10
         */
        getMaxStreamVolume(callback: AsyncCallback<number>): void;
        /**
         * Obtains the maximum volume of the audio stream. This API uses a promise to return the result.
         *
         * @returns { Promise<number> } Promise used to return the maximum volume of the audio stream.
         *     <br>The volume range is [0.0, 1.0].
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 10
         */
        getMaxStreamVolume(): Promise<number>;
        /**
         * Obtains the maximum volume of the audio stream. This API returns the result synchronously.
         *
         * @returns { number } Maximum volume of the audio stream, which ranges from 0.0 to 1.0.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 10
         */
        getMaxStreamVolumeSync(): number;
        /**
         * Obtains the number of underflow audio frames in the audio stream that is being played. This API uses an
         * asynchronous callback to return the result.
         *
         * @param { AsyncCallback<number> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **data** is the number of underloaded audio frames obtained; otherwise, **err**
         *     is an error object.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 10
         */
        getUnderflowCount(callback: AsyncCallback<number>): void;
        /**
         * Obtains the number of underflow audio frames in the audio stream that is being played. This API uses a promise to
         * return the result.
         *
         * @returns { Promise<number> } Promise used to return the number of underflow audio frames.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 10
         */
        getUnderflowCount(): Promise<number>;
        /**
         * Obtains the number of underflow audio frames in the audio stream that is being played. This API returns the
         * result synchronously.
         *
         * @returns { number } Number of underflow audio frames.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 10
         */
        getUnderflowCountSync(): number;
        /**
         * Obtains the output device information of the audio stream. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { AsyncCallback<AudioDeviceDescriptors> } callback - Callback used to return the result. If the operation
         *     is successful, **err** is **undefined** and **data** is the output device information obtained; otherwise,
         *     **err** is an error object.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @since 10
         */
        getCurrentOutputDevices(callback: AsyncCallback<AudioDeviceDescriptors>): void;
        /**
         * Obtains the output device information of the audio stream. This API uses a promise to return the result.
         *
         * @returns { Promise<AudioDeviceDescriptors> } Promise used to return the output device information.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @since 10
         */
        getCurrentOutputDevices(): Promise<AudioDeviceDescriptors>;
        /**
         * Obtains the output device information of the audio stream. This API returns the result synchronously.
         *
         * @returns { AudioDeviceDescriptors } Output device information.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @since 10
         */
        getCurrentOutputDevicesSync(): AudioDeviceDescriptors;
        /**
         * Sets the audio channel blending mode. This API returns the result synchronously.
         *
         * @param { ChannelBlendMode } mode - Audio channel blending mode.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @throws { BusinessError } 6800103 - Operation not permit at current state.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 11
         */
        setChannelBlendMode(mode: ChannelBlendMode): void;
        /**
         * Sets the silent mode in concurrent playback for the audio stream.
         *
         * If the silent mode in concurrent playback is enabled, the system mutes the audio stream and does not interrupt
         * other audio streams. If the silent mode in concurrent playback is disabled, the audio stream can gain focus based
         * on the system focus strategy.
         *
         * @param { boolean } on - Whether to enable or disable the silent mode in concurrent playback for the audio stream.
         *     **true** to enable, **false** otherwise.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @since 12
         */
        setSilentModeAndMixWithOthers(on: boolean): void;
        /**
         * Obtains the silent mode in concurrent playback for the audio stream.
         *
         * @returns { boolean } Enabled status of the silent mode in concurrent playback. **true** if enabled, **false**
         *     otherwise.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @since 12
         */
        getSilentModeAndMixWithOthers(): boolean;
        /**
         * Temporarily changes the current audio device
         * This function applies on audiorenderers whose StreamUsage are
         * STREAM_USAGE_VOICE_COMMUNICATION/STREAM_USAGE_VIDEO_COMMUNICATION/STREAM_USAGE_VOICE_MESSAGE.
         * Setting the device will only takes effect if no other accessory such as headphones are in use
         * @param { DeviceType } deviceType - the available deviceTypes are
         *                                    EARPIECE: Built-in earpiece
         *                                    SPEAKER: Built-in speaker
         *                                    DEFAULT: System default output device
         * @returns { Promise<void> } Promise used to return the result.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @throws { BusinessError } 6800103 - Operation not permit at current state.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @since 12
         */
        setDefaultOutputDevice(deviceType: DeviceType): Promise<void>;
        /**
         * Sets the loudness gain of this stream. The default loudness gain is 0.0dB.
         * The stream usage of the audio renderer must be {@link StreamUsage#STREAM_USAGE_MUSIC},
         * {@link StreamUsage#STREAM_USAGE_MOVIE} or {@link StreamUsage#STREAM_USAGE_AUDIOBOOK}.
         * After calling this interface, the adjustment of loundness gain will take effect immediately.
         * @param { number } loudnessGain - Loudness gain to set, expressed in dB. The value type is float.
         *     The loudness gain changes from -90.0dB to 24.0dB.
         * @returns { Promise<void> } Promise used to return the result.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @throws { BusinessError } 6800104 - Operation is not supported on this renderer, e.g. the stream usage of this
         * renderer is not one of {@link StreamUsage#STREAM_USAGE_MUSIC}, {@link StreamUsage#STREAM_USAGE_MOVIE} or
         * {@link StreamUsage#STREAM_USAGE_AUDIOBOOK}, or this renderer is routed through the high-resolution playback path.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @since 20
         */
        setLoudnessGain(loudnessGain: number): Promise<void>;
        /**
         * Gets loudness gain of this stream.
         * @returns { number } Returns one float value, unit is dB.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @since 20
         */
        getLoudnessGain(): number;
        /**
         * Subscribes to the audio interruption event, which is triggered when the audio focus is changed. This API uses an
         * asynchronous callback to return the result.
         *
         * The AudioRenderer instance proactively gains the focus when the **start** event occurs and releases the focus
         * when the **pause** or **stop** event occurs. Therefore, you do not need to request to gain or release the focus.
         *
         * After this API is called, an [InterruptEvent]{@link @ohos.multimedia.audio:audio.InterruptEvent} is received when
         * the AudioRenderer instance fails to obtain the focus or an audio interruption event occurs (for example, the
         * audio stream is interrupted by others). It is recommended that the application perform further processing based
         * on the **InterruptEvent** information. For details, see
         * [Introduction to Audio Focus](docroot://media/audio/audio-playback-concurrency.md).
         *
         * @param { 'audioInterrupt' } type - Event type. The event **'audioInterrupt'** is triggered when the audio focus
         *     is changed.
         * @param { Callback<InterruptEvent> } callback - Callback used to return the event information.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Interrupt
         * @crossplatform [since 12]
         * @since 9
         */
        on(type: 'audioInterrupt', callback: Callback<InterruptEvent>): void;
        /**
         * Unsubscribes from the audio interruption event. This API uses an asynchronous callback to return the result.
         *
         * @param { 'audioInterrupt' } type - Event type. The event **'audioInterrupt'** is triggered when the audio focus
         *     is changed.
         * @param { Callback<InterruptEvent> } callback - Callback used to return the event information.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Interrupt
         * @since 18
         */
        off(type: 'audioInterrupt', callback?: Callback<InterruptEvent>): void;
        /**
         * Subscribes to the mark reached event, which is triggered (only once) when the number of frames rendered reaches
         * the value of the **frame** parameter. This API uses an asynchronous callback to return the result.
         *
         * For example, if **frame** is set to **100**, the callback is invoked when the number of rendered frames reaches
         * the 100th frame.
         *
         * @param { 'markReach' } type - Event type. The event **'markReach'** is triggered when the number of frames
         *     rendered reaches the value of the **frame** parameter.
         * @param { number } frame - Number of frames to trigger the event. The value must be greater than **0**.
         * @param { Callback<number> } callback - Callback used to return the value of the **frame** parameter.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 8
         */
        on(type: 'markReach', frame: number, callback: Callback<number>): void;
        /**
         * Unsubscribes from the mark reached event. This API uses an asynchronous callback to return the result.
         *
         * @param { 'markReach' } type - Event type. The event **'markReach'** is triggered when the number of frames
         *     rendered reaches the value of the **frame** parameter.
         * @param { Callback<number> } callback - Callback used to return the value of the **frame** parameter. [since 18]
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 8
         */
        off(type: 'markReach', callback?: Callback<number>): void;
        /**
         * Subscribes to the period reached event, which is triggered each time the number of frames rendered reaches the
         * value of the **frame** parameter. In other words, the information is reported periodically. This API uses an
         * asynchronous callback to return the result.
         *
         * For example, if **frame** is set to **10**, the callback is invoked each time 10 frames are rendered, for example
         * , when the number of frames rendered reaches the 10th frame, 20th frame, and 30th frame.
         *
         * @param { 'periodReach' } type - Event type. The event **'periodReach'** is triggered each time the number of
         *     frames rendered reaches the value of the **frame** parameter.
         * @param { number } frame - Number of frames to trigger the event. The value must be greater than **0**.
         * @param { Callback<number> } callback - Callback used to return the value of the **frame** parameter.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 8
         */
        on(type: 'periodReach', frame: number, callback: Callback<number>): void;
        /**
         * Unsubscribes from the period reached event. This API uses an asynchronous callback to return the result.
         *
         * @param { 'periodReach' } type - Event type. The event **'periodReach'** is triggered each time the number of
         *     frames rendered reaches the value of the **frame** parameter.
         * @param { Callback<number> } callback - Callback used to return the value of the **frame** parameter. [since 18]
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 8
         */
        off(type: 'periodReach', callback?: Callback<number>): void;
        /**
         * Subscribes to the audio renderer state change event, which is triggered when the state of the audio renderer is
         * changed. This API uses an asynchronous callback to return the result.
         *
         * @param { 'stateChange' } type - Event type. The event **'stateChange'** is triggered when the state of the audio
         *     renderer is changed.
         * @param { Callback<AudioState> } callback - Callback used to return the audio status.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 8
         */
        on(type: 'stateChange', callback: Callback<AudioState>): void;
        /**
         * Unsubscribes from the audio renderer state change event. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { 'stateChange' } type - Event type. The event **'stateChange'** is triggered when the listening for audio
         *     renderer state change event is canceled.
         * @param { Callback<AudioState> } callback - Callback used to return the audio status.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @since 18
         */
        off(type: 'stateChange', callback?: Callback<AudioState>): void;
        /**
         * Subscribes to the audio output device change event, which is triggered when an audio output device is changed.
         * This API uses an asynchronous callback to return the result.
         *
         * @param { 'outputDeviceChange' } type - Event type. The event **'outputDeviceChange'** is triggered when an audio
         *     output device is changed.
         * @param { Callback<AudioDeviceDescriptors> } callback - Callback used to return the output device descriptor of
         *     the current audio stream.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @since 10
         */
        on(type: 'outputDeviceChange', callback: Callback<AudioDeviceDescriptors>): void;
        /**
         * Subscribes to the change event of audio output devices and reasons, which is triggered when an audio output
         * device is changed, and the change reason is reported. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { 'outputDeviceChangeWithInfo' } type - Event type. The event **'outputDeviceChangeWithInfo'** is
         *     triggered when an audio output device is changed, and the change reason is reported.
         * @param { Callback<AudioStreamDeviceChangeInfo> } callback - Callback used to return the output device descriptor
         *     of the current audio stream and the change reason.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @since 11
         */
        on(type: 'outputDeviceChangeWithInfo', callback: Callback<AudioStreamDeviceChangeInfo>): void;
        /**
         * Unsubscribes from the audio output device change event. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { 'outputDeviceChange' } type - Event type. The event **'outputDeviceChange'** is triggered when an audio
         *     output device is changed.
         * @param { Callback<AudioDeviceDescriptors> } callback - Callback used to return the output device descriptor of
         *     the current audio stream.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @since 10
         */
        off(type: 'outputDeviceChange', callback?: Callback<AudioDeviceDescriptors>): void;
        /**
         * Unsubscribes from the change event of audio output devices and reasons. This API uses an asynchronous callback to
         * return the result.
         *
         * @param { 'outputDeviceChangeWithInfo' } type - Event type. The event **'outputDeviceChangeWithInfo'** is
         *     triggered when an audio output device is changed, and the change reason is reported.
         * @param { Callback<AudioStreamDeviceChangeInfo> } callback - Callback used to return the output device descriptor
         *     of the current audio stream and the change reason.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @since 11
         */
        off(type: 'outputDeviceChangeWithInfo', callback?: Callback<AudioStreamDeviceChangeInfo>): void;
        /**
         * Subscribes to the audio data write event, which is triggered when audio data needs to be written. This API uses
         * an asynchronous callback to return the result.
         *
         * The callback function is used only to write audio data. Do not call AudioRenderer APIs in it.
         *
         * @param { 'writeData' } type - Event type. The event **'writeData'** is triggered when audio data needs to be
         *     written.
         * @param { Callback<ArrayBuffer> } callback - Callback used to write the data to the buffer.<br>API version 11 does
         *     not support the return of the callback result. API version 12 and later support the return of the callback
         *     result [AudioDataCallbackResult]{@link @ohos.multimedia.audio:audio.AudioDataCallbackResult}. [since 11 - 11]
         * @param { AudioRendererWriteDataCallback } callback - Callback used to write the data to the buffer.<br>API
         *     version 11 does not support the return of the callback result. API version 12 and later support the return of
         *     the callback result [AudioDataCallbackResult]{@link @ohos.multimedia.audio:audio.AudioDataCallbackResult}
         *     . [since 12]
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 11
         */
        on(type: 'writeData', callback: AudioRendererWriteDataCallback): void;
        /**
         * Unsubscribes from the audio data write event. This API uses an asynchronous callback to return the result.
         *
         * @param { 'writeData' } type - Event type. The event **'writeData'** is triggered when audio data needs to be
         *     written.
         * @param { Callback<ArrayBuffer> } callback - Callback used to write the data to the buffer.<br>API version 11 does
         *     not support the return of the callback result. API version 12 and later support the return of the callback
         *     result [AudioDataCallbackResult]{@link @ohos.multimedia.audio:audio.AudioDataCallbackResult}. [since 11 - 11]
         * @param { AudioRendererWriteDataCallback } callback - Callback used to write the data to the buffer.<br>API
         *     version 11 does not support the return of the callback result. API version 12 and later support the return of
         *     the callback result [AudioDataCallbackResult]{@link @ohos.multimedia.audio:audio.AudioDataCallbackResult}
         *     . [since 12]
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @crossplatform [since 12]
         * @since 11
         */
        off(type: 'writeData', callback?: AudioRendererWriteDataCallback): void;
        /**
         * Obtains the estimated latency of the current audio route.
         *
         * > **NOTE**
         * >
         * > - The estimated latency of a wireless audio device may be inaccurate. The result is for reference only.
         * >
         * > - Since the latency is not counted in the real-time buffer, you are advised to obtain the latency only when the
         * > audio playback starts to avoid frequent calls. Otherwise, the API call may be blocked due to route switching.
         * >
         * > - You are advised to use [getAudioTimestampInfo]{@link audio.AudioRenderer.getAudioTimestampInfo} or
         * > [getAudioTimestampInfoSync]{@link audio.AudioRenderer.getAudioTimestampInfoSync} to implement audio and video
         * > synchronization after the audio is output to the hardware.
         *
         * @param { AudioLatencyType } type - Obtains the latency type.
         * @returns { number } Audio latency, in milliseconds.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @throws { BusinessError } 6800103 - Operation not permitted in release state.
         * @throws { BusinessError } 6800301 - System internal error, like audio service error.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @stagemodelonly
         * @since 23
         */
        getLatency(type: AudioLatencyType): number;
        /**
         * Sets the independent audio session strategy and behavior parameters.
         *
         * > **NOTE**
         * >
         * > If this API is called while an audio renderer is running, you must call the
         * > [start]{@link @ohos.multimedia.audio:audio.AudioRenderer.start(callback: AsyncCallback<void>)} API again for
         * > the settings to take effect.
         *
         * @param { AudioSessionStrategy } strategy - Audio session strategy.
         * @param { number } behavior - Specifies the audio session behavior.<br>This can be a single flag or a bitwise OR
         *     combination of multiple flags.<br>For details about the supported audio session behaviors, see
         *     [AudioSessionBehaviorFlags]{@link @ohos.multimedia.audio:audio.AudioSessionBehaviorFlags}.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @throws { BusinessError } 6800103 - Operation not permit at current state.
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @stagemodelonly
         * @since 24
         */
        setIndependentAudioSessionStrategy(strategy: AudioSessionStrategy, behavior: number): void;
    }
    /**
     * Enumerates the types of audio streams captured.
     *
     * @syscap SystemCapability.Multimedia.Audio.Core
     * @crossplatform [since 12]
     * @since 8
     */
    enum SourceType {
        /**
         * Invalid audio source.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 8
         */
        SOURCE_TYPE_INVALID = -1,
        /**
         * Mic source.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 8
         */
        SOURCE_TYPE_MIC = 0,
        /**
         * Voice recognition source.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 9
         */
        SOURCE_TYPE_VOICE_RECOGNITION = 1,
        /**
         * Playback capture source type.
         * @syscap SystemCapability.Multimedia.Audio.PlaybackCapture
         * @since 10
         * @deprecated since 12
         * @useinstead OH_AVScreenCapture in native interface.
         */
        SOURCE_TYPE_PLAYBACK_CAPTURE = 2,
        /**
         * Voice communication source. (The 3A algorithm is not enabled if recording is started independently. It is enabled
         * when the AudioRenderer of the [STREAM_USAGE_VOICE_COMMUNICATION]{@link audio.StreamUsage} or
         * [STREAM_USAGE_VIDEO_COMMUNICATION]{@link audio.StreamUsage} type is also used to start playback.)
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 8
         */
        SOURCE_TYPE_VOICE_COMMUNICATION = 7,
        /**
         * Voice message source.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 12
         */
        SOURCE_TYPE_VOICE_MESSAGE = 10,
        /**
         * Camcorder source type.
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 13
         */
        SOURCE_TYPE_CAMCORDER = 13,
        /**
         * Unprocessed source type.
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 14
         */
        SOURCE_TYPE_UNPROCESSED = 14,
        /**
         * Live broadcast source type.
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 20
         */
        SOURCE_TYPE_LIVE = 17
    }
    /**
     * Defines mode for playback capture, each mode means different target streams to capture.
     * @syscap SystemCapability.Multimedia.Audio.PlaybackCapture
     * @stagemodelonly
     * @since 26.0.0
     */
    enum AudioPlaybackCaptureMode {
        /**
         * Default mode. Capture most of the audio streams, except tone streams and privacy streams.
         * @syscap SystemCapability.Multimedia.Audio.PlaybackCapture
         * @stagemodelonly
         * @since 26.0.0
         */
        MODE_DEFAULT = 0x0,
        /**
         * Media mode. Capture media, voice message and also unknown streams.
         * @syscap SystemCapability.Multimedia.Audio.PlaybackCapture
         * @stagemodelonly
         * @since 26.0.0
         */
        MODE_MEDIA = 0x1,
        /**
         * Excluding self mode. Capture streams excluding the audio played by application itself.
         * @syscap SystemCapability.Multimedia.Audio.PlaybackCapture
         * @stagemodelonly
         * @since 26.0.0
         */
        MODE_EXCLUDING_SELF = 0x8000
    }
    /**
     * Defines the playback capture start state, which is returned asynchronously
     * after calling {@link AudioCapturer.requestPlaybackCaptureStart} function.
     * @syscap SystemCapability.Multimedia.Audio.PlaybackCapture
     * @stagemodelonly
     * @since 26.0.0
     */
    enum PlaybackCaptureStartState {
        /**
         * Start playback capture success state.
         * @syscap SystemCapability.Multimedia.Audio.PlaybackCapture
         * @stagemodelonly
         * @since 26.0.0
         */
        STATE_SUCCESS = 0,
        /**
         * Start playback capture failed state, because the request for interrupt is denied
         * or meet system internal error.
         * @syscap SystemCapability.Multimedia.Audio.PlaybackCapture
         * @stagemodelonly
         * @since 26.0.0
         */
        STATE_FAILED = 1,
        /**
         * Start playback capture but user not authorized state.
         * @syscap SystemCapability.Multimedia.Audio.PlaybackCapture
         * @stagemodelonly
         * @since 26.0.0
         */
        STATE_NOT_AUTHORIZED = 2
    }
    /**
     * Describes audio capturer information.
     *
     * @syscap SystemCapability.Multimedia.Audio.Core
     * @crossplatform [since 12]
     * @since 8
     */
    interface AudioCapturerInfo {
        /**
         * Audio source type.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 8
         */
        source: SourceType;
        /**
         * Flags that control the capturer behavior.
         *
         * Set this parameter to **0**.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 8
         */
        capturerFlags: number;
    }
    /**
     * Describes audio capturer configurations.
     *
     * @syscap SystemCapability.Multimedia.Audio.Capturer
     * @crossplatform [since 12]
     * @since 8
     */
    interface AudioCapturerOptions {
        /**
         * Audio stream information.
         *
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @crossplatform [since 12]
         * @since 8
         */
        streamInfo: AudioStreamInfo;
        /**
         * Audio capturer information.
         *
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @crossplatform [since 12]
         * @since 8
         */
        capturerInfo: AudioCapturerInfo;
        /**
         * Defines configuration for capturing played audio.
         *
         * This API is supported since API version 10 and deprecated since API version 12. You are advised to use
         * [AVScreenCapture](docroot://reference/apis-media-kit/capi-avscreencapture.md) instead.
         *
         * @syscap SystemCapability.Multimedia.Audio.PlaybackCapture
         * @since 10
         * @deprecated since 12
         * @useinstead OH_AVScreenCapture in native interface.
         */
        playbackCaptureConfig?: AudioPlaybackCaptureConfig;
        /**
         * The playback capture mode for audio capturer.
         * This can be a combination of the available {@link AudioPlaybackCaptureMode}.
         * @syscap SystemCapability.Multimedia.Audio.PlaybackCapture
         * @stagemodelonly
         * @since 26.0.0
         */
        playbackCaptureMode?: AudioPlaybackCaptureMode;
    }
    /**
     * Defines the options for filtering the played audio streams to be recorded.
     *
     * @syscap SystemCapability.Multimedia.Audio.PlaybackCapture
     * @since 10
     * @deprecated since 12
     * @useinstead OH_AVScreenCapture in native interface.
     */
    interface CaptureFilterOptions {
        /**
         * Filter by stream usages. If you want to capture voice streams, additional permission is needed.
         * @type { Array<StreamUsage> }
         * @permission ohos.permission.CAPTURE_VOICE_DOWNLINK_AUDIO
         * @syscap SystemCapability.Multimedia.Audio.PlaybackCapture
         * @since 10
         */
        /**
         * Filter by stream usages. But not allow to capture voice streams.
         * @type { Array<StreamUsage> }
         * @syscap SystemCapability.Multimedia.Audio.PlaybackCapture
         * @since 11
         * @deprecated since 12
         * @useinstead OH_AVScreenCapture in native interface.
         */
        usages: Array<StreamUsage>;
    }
    /**
     * Defines configuration for capturing played audio.
     *
     * @syscap SystemCapability.Multimedia.Audio.PlaybackCapture
     * @since 10
     * @deprecated since 12
     * @useinstead OH_AVScreenCapture in native interface.
     */
    interface AudioPlaybackCaptureConfig {
        /**
         * Options for filtering the played audio streams to be recorded.
         *
         * @syscap SystemCapability.Multimedia.Audio.PlaybackCapture
         * @since 10
         * @deprecated since 12
         * @useinstead OH_AVScreenCapture in native interface.
         */
        filterOptions: CaptureFilterOptions;
    }
    /**
     * This interface provides APIs for audio capture.
     *
     * Before calling any API in AudioCapturer, you must use
     * [createAudioCapturer]{@link @ohos.multimedia.audio:audio.createAudioCapturer(options: AudioCapturerOptions, callback: AsyncCallback<AudioCapturer>)}
     * to create an AudioCapturer instance.
     *
     * > **NOTE**
     * >
     * > - The initial APIs of this interface are supported since API version 8.
     *
     * @syscap SystemCapability.Multimedia.Audio.Capturer
     * @crossplatform [since 12]
     * @since 8
     */
    interface AudioCapturer {
        /**
         * Audio capturer state.
         *
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @crossplatform [since 12]
         * @since 8
         */
        readonly state: AudioState;
        /**
         * Obtains the audio capturer information. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<AudioCapturerInfo> } callback - Callback used to return the result. If the operation is
         *     successful, **err** is **undefined** and **data** is the capturer information obtained; otherwise, **err** is
         *     an error object.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @crossplatform [since 12]
         * @since 8
         */
        getCapturerInfo(callback: AsyncCallback<AudioCapturerInfo>): void;
        /**
         * Obtains the audio capturer information. This API uses a promise to return the result.
         *
         * @returns { Promise<AudioCapturerInfo> } Promise used to return the audio capturer information.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @crossplatform [since 12]
         * @since 8
         */
        getCapturerInfo(): Promise<AudioCapturerInfo>;
        /**
         * Obtains the audio capturer information. This API returns the result synchronously.
         *
         * @returns { AudioCapturerInfo } Audio capturer information.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @crossplatform [since 12]
         * @since 10
         */
        getCapturerInfoSync(): AudioCapturerInfo;
        /**
         * Obtains the stream information of this audio capturer. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { AsyncCallback<AudioStreamInfo> } callback - Callback used to return the result. If the operation is
         *     successful, **err** is **undefined** and **data** is the stream information obtained; otherwise, **err** is
         *     an error object.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @crossplatform [since 12]
         * @since 8
         */
        getStreamInfo(callback: AsyncCallback<AudioStreamInfo>): void;
        /**
         * Obtains the stream information of this audio capturer. This API uses a promise to return the result.
         *
         * @returns { Promise<AudioStreamInfo> } Promise used to return the stream information.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @crossplatform [since 12]
         * @since 8
         */
        getStreamInfo(): Promise<AudioStreamInfo>;
        /**
         * Obtains the stream information of this audio capturer. This API returns the result synchronously.
         *
         * @returns { AudioStreamInfo } Stream information.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @crossplatform [since 12]
         * @since 10
         */
        getStreamInfoSync(): AudioStreamInfo;
        /**
         * Obtains the stream ID of this audio capturer. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<number> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **data** is the stream ID obtained; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @crossplatform [since 12]
         * @since 9
         */
        getAudioStreamId(callback: AsyncCallback<number>): void;
        /**
         * Obtains the stream ID of this audio capturer. This API uses a promise to return the result.
         *
         * @returns { Promise<number> } Promise used to return the stream ID.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @crossplatform [since 12]
         * @since 9
         */
        getAudioStreamId(): Promise<number>;
        /**
         * Obtains the stream ID of this audio capturer. This API returns the result synchronously.
         *
         * @returns { number } Stream ID.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @crossplatform [since 12]
         * @since 10
         */
        getAudioStreamIdSync(): number;
        /**
         * Starts this audio capturer to start capturing audio data. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object. If the operation fails, an error object with
         *     the following error code is returned:<br>Error code 6800301: indicates abnormal status, focus preemption
         *     failure, and abnormal system processing. For details, see system logs.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @crossplatform [since 12]
         * @since 8
         */
        start(callback: AsyncCallback<void>): void;
        /**
         * Starts this audio capturer to start capturing audio data. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise object, which indicates that the capturer is started successfully. If the
         *     operation fails, an error object with the following error code is returned:
         *     <br>Error code 6800301: indicates abnormal status, focus preemption failure, and abnormal system processing. For
         *     details, see system logs.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @crossplatform [since 12]
         * @since 8
         */
        start(): Promise<void>;
        /**
         * Asynchronously request to start the playback capture stream.
         * This function is non-blocking, which means system will continue to process user authorization and
         * stream starting when receiving the start request. And the final result will be returned by callback.
         * @param { Callback<PlaybackCaptureStartState> } callback - Callback function used to receive the final
         *     result of start request.
         * @syscap SystemCapability.Multimedia.Audio.PlaybackCapture
         * @stagemodelonly
         * @since 26.0.0
         */
        requestPlaybackCaptureStart(callback: Callback<PlaybackCaptureStartState>): void;
        /**
         * Reads the buffer from the audio capturer. This method uses an asynchronous callback to return the result.
         * @param { number } size - Number of bytes to read.
         * @param { boolean } isBlockingRead - Whether to block the read operation. **true** to block, **false** otherwise.
         * @param { AsyncCallback<ArrayBuffer> } callback - Callback used to return the result. If the operation is
         *     successful, **err** is **undefined** and **data** is the buffer read; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @since 8
         * @deprecated since 11
         * @useinstead ohos.multimedia.audio.AudioCapturer#event:readData
         */
        read(size: number, isBlockingRead: boolean, callback: AsyncCallback<ArrayBuffer>): void;
        /**
         * Reads the buffer. This API uses a promise to return the result.
         *
         * @param { number } size - Number of bytes to read.
         * @param { boolean } isBlockingRead - Whether to block the read operation. **true** to block, **false** otherwise.
         * @returns { Promise<ArrayBuffer> } Promise used to return the data read from the buffer.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @since 8
         * @deprecated since 11
         * @useinstead ohos.multimedia.audio.AudioCapturer#event:readData
         */
        read(size: number, isBlockingRead: boolean): Promise<ArrayBuffer>;
        /**
         * Obtains the timestamp of the current recording position, measured in nanoseconds from the Unix epoch (January 1,
         * 1970). This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<number> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **data** is the number of nanoseconds obtained; otherwise, **err** is an error
         *     object.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @crossplatform [since 12]
         * @since 8
         */
        getAudioTime(callback: AsyncCallback<number>): void;
        /**
         * Obtains the timestamp of the current recording position, measured in nanoseconds from the Unix epoch (January 1,
         * 1970). This API uses a promise to return the result.
         *
         * @returns { Promise<number> } Promise used to return a timestamp representing the number of nanoseconds elapsed
         *     since the Unix epoch (January 1, 1970).
         *     <br>The timestamp unit is nanoseconds.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @crossplatform [since 12]
         * @since 8
         */
        getAudioTime(): Promise<number>;
        /**
         * Obtains the timestamp of the current recording position, measured in nanoseconds from the Unix epoch (January 1,
         * 1970). This API returns the result synchronously.
         *
         * @returns { number } Timestamp.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @crossplatform [since 12]
         * @since 10
         */
        getAudioTimeSync(): number;
        /**
         * Obtains the timestamp and position information of an input audio stream.
         *
         * This API obtains the actual recording position (specified by **framePos**) of the audio channel and the timestamp
         * when recording to that position (specified by **timestamp**, in nanoseconds).
         *
         * @returns { Promise<AudioTimestampInfo> } Promise used to return the timestamp and position information.
         * @throws { BusinessError } 6800103 - Operation not permit at current state.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @since 19
         */
        getAudioTimestampInfo(): Promise<AudioTimestampInfo>;
        /**
         * Obtains the timestamp and position information of an input audio stream. This API returns the result
         * synchronously.
         *
         * @returns { AudioTimestampInfo } Information about the timestamp and position information.
         * @throws { BusinessError } 6800103 - Operation not permit at current state.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @since 19
         */
        getAudioTimestampInfoSync(): AudioTimestampInfo;
        /**
         * Stops this audio capturer, ceasing the input audio stream. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @crossplatform [since 12]
         * @since 8
         */
        stop(callback: AsyncCallback<void>): void;
        /**
         * Stops this audio capturer, ceasing the input audio stream. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @crossplatform [since 12]
         * @since 8
         */
        stop(): Promise<void>;
        /**
         * Releases this audio capturer. This API uses an asynchronous callback to return the result.
         *
         * @param { AsyncCallback<void> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined**; otherwise, **err** is an error object.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @crossplatform [since 12]
         * @since 8
         */
        release(callback: AsyncCallback<void>): void;
        /**
         * Releases this audio capturer. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @crossplatform [since 12]
         * @since 8
         */
        release(): Promise<void>;
        /**
         * Obtains a reasonable minimum buffer size in bytes for capturing. This API uses an asynchronous callback to return
         * the result.
         *
         * @param { AsyncCallback<number> } callback - Callback used to return the result. If the operation is successful,
         *     **err** is **undefined** and **data** is the minimum buffer size obtained; otherwise, **err** is an error
         *     object.<br>The unit is bytes.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @crossplatform [since 12]
         * @since 8
         */
        getBufferSize(callback: AsyncCallback<number>): void;
        /**
         * Obtains a reasonable minimum buffer size in bytes for capturing. This API uses a promise to return the result.
         *
         * @returns { Promise<number> } Promise used to return the buffer size.
         *     <br>The unit is bytes.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @crossplatform [since 12]
         * @since 8
         */
        getBufferSize(): Promise<number>;
        /**
         * Obtains a reasonable minimum buffer size in bytes for capturing. This API returns the result synchronously.
         *
         * @returns { number } Buffer size, in bytes.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @crossplatform [since 12]
         * @since 10
         */
        getBufferSizeSync(): number;
        /**
         * Obtains the information of the current input devices. This API returns the result synchronously.
         *
         * @returns { AudioDeviceDescriptors } An array of the audio device descriptors.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @since 11
         */
        getCurrentInputDevices(): AudioDeviceDescriptors;
        /**
         * Obtains the configuration changes of the current audio capturer. This API returns the result synchronously.
         *
         * @returns { AudioCapturerChangeInfo } Configuration changes of the audio capturer.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @since 11
         */
        getCurrentAudioCapturerChangeInfo(): AudioCapturerChangeInfo;
        /**
         * Obtains the number of overflow audio frames in the audio stream that is being captured. This API uses a promise
         * to return the result.
         *
         * @returns { Promise<number> } Promise used to return the number of overflow audio frames.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @since 12
         */
        getOverflowCount(): Promise<number>;
        /**
         * Obtains the number of overflow audio frames in the audio stream that is being captured. This API returns the
         * result synchronously.
         *
         * @returns { number } Number of overflow audio frames.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @since 12
         */
        getOverflowCountSync(): number;
        /**
         * Sets whether to
         * [mute the current audio recording stream when an audio interruption occurs](docroot://media/audio/using-audiocapturer-for-recording.md#setting-the-mute-interruption-mode)
         * . This API uses a promise to return the result.
         *
         * @param { boolean } muteWhenInterrupted - Whether to mute the current audio recording stream during an audio
         *     interruption. **true** to mute, **false** otherwise.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 6800103 - Operation not permitted at current state.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @since 20
         */
        setWillMuteWhenInterrupted(muteWhenInterrupted: boolean): Promise<void>;
        /**
         * Sets recording mute state to audio system, this method is used as a hint for power optimization,
         * it does not mute the recording stream, only affects internal processing strategy.
         *
         * @param { boolean } mute - Use true if application recording stream muted by application if self.
         * @returns { Promise<void> } Promise used to return the result.
         * @throws { BusinessError } 6800103 - Operation not permitted at current state, stream is not running.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @stagemodelonly
         * @since 24
         */
        setMuteHint(mute: boolean): Promise<void>;
        /**
         * Subscribes to the mark reached event, which is triggered (only once) when the number of frames captured reaches
         * the value of the **frame** parameter. This API uses an asynchronous callback to return the result.
         *
         * For example, if **frame** is set to **100**, the callback is invoked when the number of captured frames reaches
         * the 100th frame.
         *
         * @param { 'markReach' } type - Event type. The event **'markReach'** is triggered when the number of frames
         *     captured reaches the value of the **frame** parameter.
         * @param { number } frame - Number of frames to trigger the event. The value must be greater than **0**.
         * @param { Callback<number> } callback - Callback used to return the value of the **frame** parameter.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @crossplatform [since 12]
         * @since 8
         */
        on(type: 'markReach', frame: number, callback: Callback<number>): void;
        /**
         * Unsubscribes from the mark reached event. This API uses an asynchronous callback to return the result.
         *
         * @param { 'markReach' } type - Event type. The event **'markReach'** is triggered when the number of frames
         *     captured reaches the value of the **frame** parameter.
         * @param { Callback<number> } callback - Callback used to return the value of the **frame** parameter. [since 18]
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @crossplatform [since 12]
         * @since 8
         */
        off(type: 'markReach', callback?: Callback<number>): void;
        /**
         * Subscribes to the period reached event, which is triggered each time the number of frames captured reaches the
         * value of the **frame** parameter. In other words, the information is reported periodically. This API uses an
         * asynchronous callback to return the result.
         *
         * For example, if **frame** is set to **10**, the callback is invoked each time 10 frames are captured, for example
         * , when the number of frames captured reaches the 10th frame, 20th frame, and 30th frame.
         *
         * @param { 'periodReach' } type - Event type. The event **'periodReach'** is triggered each time the number of
         *     frames captured reaches the value of the **frame** parameter.
         * @param { number } frame - Number of frames to trigger the event. The value must be greater than **0**.
         * @param { Callback<number> } callback - Callback used to return the value of the **frame** parameter.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @crossplatform [since 12]
         * @since 8
         */
        on(type: 'periodReach', frame: number, callback: Callback<number>): void;
        /**
         * Unsubscribes from the period reached event. This API uses an asynchronous callback to return the result.
         *
         * @param { 'periodReach' } type - Event type. The event **'periodReach'** is triggered each time the number of
         *     frames captured reaches the value of the **frame** parameter.
         * @param { Callback<number> } callback - Callback used to return the value of the **frame** parameter. [since 18]
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @crossplatform [since 12]
         * @since 8
         */
        off(type: 'periodReach', callback?: Callback<number>): void;
        /**
         * Subscribes to the audio capturer state change event, which is triggered when the state of the audio capturer is
         * changed. This API uses an asynchronous callback to return the result.
         *
         * @param { 'stateChange' } type - Event type. The event **'stateChange'** is triggered when the state of the audio
         *     capturer is changed.
         * @param { Callback<AudioState> } callback - Callback used to return the audio status.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @crossplatform [since 12]
         * @since 8
         */
        on(type: 'stateChange', callback: Callback<AudioState>): void;
        /**
         * Unsubscribes from the audio capturer state change event. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { 'stateChange' } type - Event type. The event **'stateChange'** is triggered when the listening for audio
         *     capturer state change event is canceled.
         * @param { Callback<AudioState> } callback - Callback used to return the audio status.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @since 18
         */
        off(type: 'stateChange', callback?: Callback<AudioState>): void;
        /**
         * Subscribes to the audio interruption event, which is triggered when the audio focus is changed. This API uses an
         * asynchronous callback to return the result.
         *
         * The AudioCapturer instance proactively gains the focus when the **start** event occurs and releases the focus
         * when the **pause** or **stop** event occurs. Therefore, you do not need to request to gain or release the focus.
         *
         * After this API is called, an [InterruptEvent]{@link @ohos.multimedia.audio:audio.InterruptEvent} is received when
         * the AudioCapturer instance fails to obtain the focus or an audio interruption event occurs (for example, the
         * audio stream is interrupted by others). It is recommended that the application perform further processing based
         * on the **InterruptEvent** information. For details, see
         * [Introduction to Audio Focus](docroot://media/audio/audio-playback-concurrency.md).
         *
         * @param { 'audioInterrupt' } type - Event type. The event **'audioInterrupt'** is triggered when the audio focus
         *     is changed.
         * @param { Callback<InterruptEvent> } callback - Callback used to return the event information.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Interrupt
         * @crossplatform [since 12]
         * @since 10
         */
        on(type: 'audioInterrupt', callback: Callback<InterruptEvent>): void;
        /**
         * Unsubscribes from the audio interruption event.
         *
         * @param { 'audioInterrupt' } type - Event type. The event **'audioInterrupt'** is triggered when the audio focus
         *     is changed.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Interrupt
         * @crossplatform [since 12]
         * @since 10
         */
        off(type: 'audioInterrupt'): void;
        /**
         * Subscribes to the audio input device change event, which is triggered when an audio input device is changed. This
         * API uses an asynchronous callback to return the result.
         *
         * @param { 'inputDeviceChange' } type - Event type. The event **'inputDeviceChange'** is triggered when an audio
         *     input device is changed.
         * @param { Callback<AudioDeviceDescriptors> } callback - Callback used to return the updated information about the
         *     audio input device.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @since 11
         */
        on(type: 'inputDeviceChange', callback: Callback<AudioDeviceDescriptors>): void;
        /**
         * Unsubscribes from the audio input device change event. This API uses an asynchronous callback to return the
         * result.
         *
         * @param { 'inputDeviceChange' } type - Event type. The event **'inputDeviceChange'** is triggered when an audio
         *     input device is changed.
         * @param { Callback<AudioDeviceDescriptors> } callback - Callback used to return the information about the audio
         *     input device.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @crossplatform [since 12]
         * @since 11
         */
        off(type: 'inputDeviceChange', callback?: Callback<AudioDeviceDescriptors>): void;
        /**
         * Subscribes to the audio capturer configuration change event, which is triggered when the audio recording stream
         * status or device is changed. This API uses an asynchronous callback to return the result. The subscription is
         * implemented asynchronously and the callback, which is triggered when the audio capturer configuration changes,
         * may fail to reflect the actual condition.
         *
         * @param { 'audioCapturerChange' } type - Event type. The event **'audioCapturerChange'** is triggered when the
         *     audio recording stream status or device is changed.
         * @param { Callback<AudioCapturerChangeInfo> } callback - Callback used to return the current configuration and
         *     status information of the audio capturer.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @crossplatform [since 12]
         * @since 11
         */
        on(type: 'audioCapturerChange', callback: Callback<AudioCapturerChangeInfo>): void;
        /**
         * Unsubscribes from the audio capturer configuration change event. This API uses an asynchronous callback to return
         * the result.
         *
         * @param { 'audioCapturerChange' } type - Event type. The event **'audioCapturerChange'** is triggered when the
         *     audio capturer configuration is changed.
         * @param { Callback<AudioCapturerChangeInfo> } callback - Callback used for unsubscription.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @crossplatform [since 12]
         * @since 11
         */
        off(type: 'audioCapturerChange', callback?: Callback<AudioCapturerChangeInfo>): void;
        /**
         * Subscribes to the audio data read event, which is triggered when audio stream data needs to be read. This API
         * uses an asynchronous callback to return the result.
         *
         * The callback function is used only to read audio data. Do not call AudioCapturer APIs in it.
         *
         * To eliminate power-on noise caused by the microphone hardware design, the first 100 ms of data after recording
         * starts is typically muted.
         *
         * @param { 'readData' } type - Event type. The event **'readData'** is triggered when audio stream data needs to be
         *     read.
         * @param { Callback<ArrayBuffer> } callback - Callback used to return the buffer from which the data is read.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @crossplatform [since 12]
         * @since 11
         */
        on(type: 'readData', callback: Callback<ArrayBuffer>): void;
        /**
         * Unsubscribes from the audio data read event. This API uses an asynchronous callback to return the result.
         *
         * @param { 'readData' } type - Event type. The event **'readData'** is triggered when audio stream data needs to be
         *     read.
         * @param { Callback<ArrayBuffer> } callback - Callback used to return the buffer from which the data is read.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @crossplatform [since 12]
         * @since 11
         */
        off(type: 'readData', callback?: Callback<ArrayBuffer>): void;
        /**
         * Sets the independent audio session strategy and behavior parameters.
         *
         * > **NOTE**
         * >
         * > If this API is called while an audio capturer is running, you must call the
         * > [start]{@link @ohos.multimedia.audio:audio.AudioCapturer.start(callback: AsyncCallback<void>)} API again for
         * > the settings to take effect.
         *
         * @param { AudioSessionStrategy } strategy - Audio session strategy.
         * @param { number } behavior - Specifies the audio session behavior.<br>This can be a single flag or a bitwise OR
         *     combination of multiple flags.<br>For details about the supported audio session behaviors, see
         *     [AudioSessionBehaviorFlags]{@link @ohos.multimedia.audio:audio.AudioSessionBehaviorFlags}.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @throws { BusinessError } 6800103 - Operation not permit at current state.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @stagemodelonly
         * @since 24
         */
        setIndependentAudioSessionStrategy(strategy: AudioSessionStrategy, behavior: number): void;
        /**
         * Sets noise reduction mode for current audio capturer.
         * The supported mode should be obtained by {@link #getSupportedNoiseReductionModes}.
         * The actual effect may vary from different audio devices, and will be invalid when there are multiple
         * recording streams running simultaneously.
         * The mode can only be changed in created and stopped state.
         *
         * @param { NoiseReductionMode } noiseReductionMode - The noise reduction mode to set.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @throws { BusinessError } 6800103 - Illegal state, audio capturer is in running or released state.
         * @throws { BusinessError } 6800104 - The setted mode is not supported.
         * @throws { BusinessError } 6800301 - Audio server process died.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @stagemodelonly
         * @since 26.0.0
         */
        setNoiseReductionMode(noiseReductionMode: NoiseReductionMode): void;
        /**
         * Gets the noise reduction mode for current audio capturer.
         * The mode will only consider the default and setted status, audio input device and stream concurrency will
         * not be considered.
         *
         * @returns { NoiseReductionMode } The noise reduction mode for current audio capturer,
         *     the default value is {@link NoiseReductionMode#FIDELITY}.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @stagemodelonly
         * @since 26.0.0
         */
        getNoiseReductionMode(): NoiseReductionMode;
        /**
         * Gets all the supported noise reduction modes for current device platform.
         * Currently the noise reduction effect is only supported when using
         * {@link SourceType#SOURCE_TYPE_VOICE_MESSAGE}, other supported usage may be extened later.
         * The supported modes will only consider the audio format and device platform,
         * audio input device and stream concurrency will not be considered.
         *
         * @returns { Array<NoiseReductionMode> } The supported noise reduction mode array, at least
         *     {@link NoiseReductionMode#FIDELITY} is supported.
         * @throws { BusinessError } 6800301 - Audio server process died.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @stagemodelonly
         * @since 26.0.0
         */
        getSupportedNoiseReductionModes(): Array<NoiseReductionMode>;
    }
    /**
     * Defines an array that contains the audio effect mode corresponding to a specific audio content type (specified by
     * **ContentType**) and audio stream usage (specified by **StreamUsage**). The
     * [AudioEffectMode]{@link @ohos.multimedia.audio:audio.AudioEffectMode} array is read-only.
     *
     * @syscap SystemCapability.Multimedia.Audio.Renderer
     * @since 10
     */
    type AudioEffectInfoArray = Array<Readonly<AudioEffectMode>>;
    /**
     * Enumerates the audio effect modes.
     *
     * @syscap SystemCapability.Multimedia.Audio.Renderer
     * @atomicservice [since 12]
     * @since 10
     */
    enum AudioEffectMode {
        /**
         * The audio effect is disabled.
         *
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @atomicservice [since 12]
         * @since 10
         */
        EFFECT_NONE = 0,
        /**
         * The default audio effect is used.
         *
         * @syscap SystemCapability.Multimedia.Audio.Renderer
         * @atomicservice [since 12]
         * @since 10
         */
        EFFECT_DEFAULT = 1
    }
    /**
     * Audio AudioChannel Layout.
     * A 64-bit integer indicates that the appearance and order of the speakers for recording or playback.
     *
     * @syscap SystemCapability.Multimedia.Audio.Core
     * @crossplatform
     * @since 11
     */
    enum AudioChannelLayout {
        /**
         * Unknown Channel Layout.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 11
         */
        CH_LAYOUT_UNKNOWN = 0x0,
        /**
         * Channel Layout For Mono, 1 channel in total.
         * Speaker layout: front center(FC).
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 11
         */
        CH_LAYOUT_MONO = 0x4,
        /**
         * Channel Layout For Stereo, 2 channels in total.
         * Speaker layout: front left(FL), front right(FR).
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 11
         */
        CH_LAYOUT_STEREO = 0x3,
        /**
         * Channel Layout For Stereo-Downmix, 2 channels in total.
         * Speaker layout: Stereo left, stereo right.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 11
         */
        CH_LAYOUT_STEREO_DOWNMIX = 0x60000000,
        /**
         * Channel Layout For 2.1, 3 channels in total.
         * Speaker layout: Stereo plus low-frequency effects(LFE).
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 11
         */
        CH_LAYOUT_2POINT1 = 0xB,
        /**
         * Channel Layout For 3.0, 3 channels in total.
         * Speaker layout: Stereo plus back center(BC).
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 11
         */
        CH_LAYOUT_3POINT0 = 0x103,
        /**
         * Channel Layout For Surround, 3 channels in total.
         * Speaker layout: Stereo plus FC.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 11
         */
        CH_LAYOUT_SURROUND = 0x7,
        /**
         * Channel Layout For 3.1, 4 channels in total.
         * Speaker layout: Surround plus LFE.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 11
         */
        CH_LAYOUT_3POINT1 = 0xF,
        /**
         * Channel Layout For 4.0, 4 channels in total.
         * Speaker layout: Surround plus BC.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 11
         */
        CH_LAYOUT_4POINT0 = 0x107,
        /**
         * Channel Layout For Quad, 4 channels in total.
         * Speaker layout: Stereo plus left and right back speakers.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 11
         */
        CH_LAYOUT_QUAD = 0x33,
        /**
         * Channel Layout For Quad-Side, 4 channels in total.
         * Speaker layout: Stereo plus left and right side speakers(SL, SR).
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 11
         */
        CH_LAYOUT_QUAD_SIDE = 0x603,
        /**
         * Channel Layout For 2.0.2, 4 channels in total.
         * Speaker layout: Stereo plus left and right top side speakers.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 11
         */
        CH_LAYOUT_2POINT0POINT2 = 0x3000000003,
        /**
         * Channel Layout For ORDER1-ACN-N3D First Order Ambisonic(FOA), 4 channels in total.
         * First order, Ambisonic Channel Number(ACN) format, Normalization of three-D(N3D).
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 11
         */
        CH_LAYOUT_AMB_ORDER1_ACN_N3D = 0x100000000001,
        /**
         * Channel Layout For ORDER1-ACN-SN3D FOA, 4 channels in total.
         * First order, ACN format, Semi-Normalization of three-D(SN3D).
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 11
         */
        CH_LAYOUT_AMB_ORDER1_ACN_SN3D = 0x100000001001,
        /**
         * Channel Layout For ORDER1-FUMA FOA, 4 channels in total.
         * First order, Furse-Malham(FuMa) format.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 11
         */
        CH_LAYOUT_AMB_ORDER1_FUMA = 0x100000000101,
        /**
         * Channel Layout For 4.1, 5 channels in total.
         * Speaker layout: 4.0 plus LFE.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 11
         */
        CH_LAYOUT_4POINT1 = 0x10F,
        /**
         * Channel Layout For 5.0, 5 channels in total.
         * Speaker layout: Surround plus two side speakers.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 11
         */
        CH_LAYOUT_5POINT0 = 0x607,
        /**
         * Channel Layout For 5.0-Back, 5 channels in total.
         * Speaker layout: Surround plus two back speakers.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 11
         */
        CH_LAYOUT_5POINT0_BACK = 0x37,
        /**
         * Channel Layout For 2.1.2, 5 channels in total.
         * Speaker layout: 2.0.2 plus LFE.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 11
         */
        CH_LAYOUT_2POINT1POINT2 = 0x300000000B,
        /**
         * Channel Layout For 3.0.2, 5 channels in total.
         * Speaker layout: 2.0.2 plus FC.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 11
         */
        CH_LAYOUT_3POINT0POINT2 = 0x3000000007,
        /**
         * Channel Layout For 5.1, 6 channels in total.
         * Speaker layout: 5.0 plus LFE.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 11
         */
        CH_LAYOUT_5POINT1 = 0x60F,
        /**
         * Channel Layout For 5.1-Back, 6 channels in total.
         * Speaker layout: 5.0-Back plus LFE.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 11
         */
        CH_LAYOUT_5POINT1_BACK = 0x3F,
        /**
         * Channel Layout For 6.0, 6 channels in total.
         * Speaker layout: 5.0 plus BC.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 11
         */
        CH_LAYOUT_6POINT0 = 0x707,
        /**
         * Channel Layout For Hexagonal, 6 channels in total.
         * Speaker layout: 5.0-Back plus BC.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 11
         */
        CH_LAYOUT_HEXAGONAL = 0x137,
        /**
         * Channel Layout For 3.1.2, 6 channels in total.
         * Speaker layout: 3.1 plus two top front speakers(TFL, TFR).
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 11
         */
        CH_LAYOUT_3POINT1POINT2 = 0x500F,
        /**
         * Channel Layout For 6.0-Front, 6 channels in total.
         * Speaker layout: Quad-Side plus left and right front center speakers(FLC, FRC).
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 11
         */
        CH_LAYOUT_6POINT0_FRONT = 0x6C3,
        /**
         * Channel Layout For 6.1, 7 channels in total.
         * Speaker layout: 5.1 plus BC.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 11
         */
        CH_LAYOUT_6POINT1 = 0x70F,
        /**
         * Channel Layout For 6.1-Back, 7 channels in total.
         * Speaker layout: 5.1-Back plus BC.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 11
         */
        CH_LAYOUT_6POINT1_BACK = 0x13F,
        /**
         * Channel Layout For 6.1-Front, 7 channels in total.
         * Speaker layout: 6.0-Front plus LFE.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 11
         */
        CH_LAYOUT_6POINT1_FRONT = 0x6CB,
        /**
         * Channel Layout For 7.0, 7 channels in total.
         * Speaker layout: 5.0 plus two back speakers.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 11
         */
        CH_LAYOUT_7POINT0 = 0x637,
        /**
         * Channel Layout For 7.0-Front, 7 channels in total.
         * Speaker layout: 5.0 plus left and right front center speakers.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 11
         */
        CH_LAYOUT_7POINT0_FRONT = 0x6C7,
        /**
         * Channel Layout For 7.1, 8 channels in total.
         * Speaker layout: 5.1 plus two back speakers.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 11
         */
        CH_LAYOUT_7POINT1 = 0x63F,
        /**
         * Channel Layout For Octagonal, 8 channels in total.
         * Speaker layout: 5.0 plus BL, BR and BC.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 11
         */
        CH_LAYOUT_OCTAGONAL = 0x737,
        /**
         * Channel Layout For 5.1.2, 8 channels in total.
         * Speaker layout: 5.1 plus two top side speakers.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 11
         */
        CH_LAYOUT_5POINT1POINT2 = 0x300000060F,
        /**
         * Channel Layout For 7.1-Wide, 8 channels in total.
         * Speaker layout: 5.1 plus left and right front center speakers.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 11
         */
        CH_LAYOUT_7POINT1_WIDE = 0x6CF,
        /**
         * Channel Layout For 7.1-Wide, 8 channels in total.
         * Speaker layout: 5.1-Back plus left and right front center speakers.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 11
         */
        CH_LAYOUT_7POINT1_WIDE_BACK = 0xFF,
        /**
         * Channel Layout For ORDER2-ACN-N3D Higher Order Ambisonics(HOA), 9 channels in total.
         * Second order, ACN format, N3D.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 11
         */
        CH_LAYOUT_AMB_ORDER2_ACN_N3D = 0x100000000002,
        /**
         * Channel Layout For ORDER2-ACN-SN3D HOA, 9 channels in total.
         * Second order, ACN format, SN3D.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 11
         */
        CH_LAYOUT_AMB_ORDER2_ACN_SN3D = 0x100000001002,
        /**
         * Channel Layout For ORDER2-FUMA HOA, 9 channels in total.
         * Second order, FuMa format.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 11
         */
        CH_LAYOUT_AMB_ORDER2_FUMA = 0x100000000102,
        /**
         * Channel Layout For 5.1.4, 10 channels in total.
         * Speaker layout: 5.1 plus four top speakers(TFL, TFR, TBL, TBR).
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 11
         */
        CH_LAYOUT_5POINT1POINT4 = 0x2D60F,
        /**
         * Channel Layout For 7.1.2, 10 channels in total.
         * Speaker layout: 7.1 plus two top side speakers.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 11
         */
        CH_LAYOUT_7POINT1POINT2 = 0x300000063F,
        /**
         * Channel Layout For 7.1.4, 12 channels in total.
         * Speaker layout: 7.1 plus four top speakers.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 11
         */
        CH_LAYOUT_7POINT1POINT4 = 0x2D63F,
        /**
         * Channel Layout For 10.2, 12 channels in total.
         * Speaker layout: FL, FR, FC, TFL, TFR, BL, BR, BC, SL, SR, wide left(WL), and wide right(WR).
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 11
         */
        CH_LAYOUT_10POINT2 = 0x180005737,
        /**
         * Channel Layout For 9.1.4, 14 channels in total.
         * Speaker layout: 7.1.4 plus two wide speakers(WL, WR).
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 11
         */
        CH_LAYOUT_9POINT1POINT4 = 0x18002D63F,
        /**
         * Channel Layout For 9.1.6, 16 channels in total.
         * Speaker layout: 9.1.4 plus two top side speakers.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 11
         */
        CH_LAYOUT_9POINT1POINT6 = 0x318002D63F,
        /**
         * Channel Layout For Hexadecagonal, 16 channels in total.
         * Speaker layout: Octagonal plus two wide speakers, six top speakers(TFL, TFR, TFC, TBL, TBR, TBC).
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 11
         */
        CH_LAYOUT_HEXADECAGONAL = 0x18003F737,
        /**
         * Channel Layout For ORDER3-ACN-N3D HOA, 16 channels in total.
         * Third order, ACN format, N3D.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 11
         */
        CH_LAYOUT_AMB_ORDER3_ACN_N3D = 0x100000000003,
        /**
         * Channel Layout For ORDER3-ACN-SN3D HOA, 16 channels in total.
         * Third order, ACN format, N3D.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @crossplatform [since 12]
         * @since 11
         */
        CH_LAYOUT_AMB_ORDER3_ACN_SN3D = 0x100000001003,
        /**
         * Channel Layout For ORDER3-FUMA HOA, 16 channels in total.
         * Third order, FuMa format.
         *
         * @syscap SystemCapability.Multimedia.Audio.Core
         * @since 11
         */
        CH_LAYOUT_AMB_ORDER3_FUMA = 0x100000000103
    }
    /**
     * Describes an audio device pair including both input and output devices.
     *
     * @syscap SystemCapability.Multimedia.Audio.Device
     * @stagemodelonly
     * @since 26.0.0
     */
    interface AudioDevicePair {
        /**
         * Input audio device descriptor.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @stagemodelonly
         * @since 26.0.0
         */
        inputDevice: AudioDeviceDescriptor;
        /**
         * Output audio device descriptor.
         *
         * @syscap SystemCapability.Multimedia.Audio.Device
         * @stagemodelonly
         * @since 26.0.0
         */
        outputDevice: AudioDeviceDescriptor;
    }
    /**
     * This interface provides APIs for audio monitoring.
     *
     * Before calling any API in AudioLoopback, you must use
     * [audio.createAudioLoopback]{@link @ohos.multimedia.audio:audio.createAudioLoopback(mode: AudioLoopbackMode)} to
     * create an AudioLoopback instance.
     *
     * When audio loopback is enabled, the system creates a low-latency renderer and capturer to implement low-latency in-
     * ear monitoring. The audio captured is routed back to the renderer through an internal path. The renderer follows
     * the audio focus strategy for [STREAM_USAGE_MUSIC]{@link @ohos.multimedia.audio:audio.StreamUsage}, whereas the
     * capturer follows the strategy for [SOURCE_TYPE_MIC]{@link @ohos.multimedia.audio:audio.SourceType}.
     *
     * The system automatically chooses the input and output devices. If these devices do not support low latency, audio
     * loopback does not work. If another audio stream takes over the audio focus or if the input or output device changes
     * to the one that does not support low latency, the system disables audio loopback automatically.
     *
     * > **NOTE**
     * >
     * > - The initial APIs of this interface are supported since API version 20.
     *
     * @syscap SystemCapability.Multimedia.Audio.Capturer
     * @since 20
     */
    interface AudioLoopback {
        /**
         * Obtains the audio loopback status. This API uses a promise to return the result.
         *
         * @returns { Promise<AudioLoopbackStatus> } Promise used to return the audio loopback status.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @since 20
         */
        getStatus(): Promise<AudioLoopbackStatus>;
        /**
         * Sets the volume for audio loopback. This volume does not affect other audio streams or the system volume.
         * @param { number } volume Volume to set. The value type is float, ranging from 0.0 to 1.0.
         * @returns { Promise<void> } Promise used to return the result.
         * @throws { BusinessError } 6800101 - Parameter verification failed, from 0.0 to 1.0.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @since 20
         */
        setVolume(volume: number): Promise<void>;
        /**
         * Gets the output volume for audio loopback.
         *
         * @returns { number } Current audio loopback output volume value.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @stagemodelonly
         * @since 26.0.0
         */
        getVolume(): number;
        /**
         * Subscribes to the audio loopback status change event, which is triggered when the status of the audio loopback is
         * changed. This API uses an asynchronous callback to return the result.
         *
         * @param { 'statusChange' } type - Event type. The event **'statusChange'** is triggered when the status of the
         *     audio loopback is changed.
         * @param { Callback<AudioLoopbackStatus> } callback - Callback used to return the audio loopback status.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @since 20
         */
        on(type: 'statusChange', callback: Callback<AudioLoopbackStatus>): void;
        /**
         * Unsubscribes from the audio loopback status event. This API uses an asynchronous callback to return the result.
         *
         * @param { 'statusChange' } type - Event type. The event **'statusChange'** is triggered when the status of the
         *     audio loopback is changed.
         * @param { Callback<AudioLoopbackStatus> } [callback] - Callback used to return the audio loopback status.
         * @throws  { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @since 20
         */
        off(type: 'statusChange', callback?: Callback<AudioLoopbackStatus>): void;
        /**
         * Gets supported audio device pairs in current device connection situation.
         *
         * @returns { Array<AudioDevicePair> } Audio device pairs that support loopback,
         *     if there is no supported device pair, empty array will be returned.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @stagemodelonly
         * @since 26.0.0
         */
        getSupportedDevicePairs(): Array<AudioDevicePair>;
        /**
         * Gets the preferred audio device pair in current device connection situation.
         *
         * @returns { AudioDevicePair | null }  The preferred audio device pair in audio system,
         *     or null if there is no supported device pair.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @stagemodelonly
         * @since 26.0.0
         */
        getPreferredDevicePair(): AudioDevicePair | null;
        /**
         * Enable or disable audio loopback.
         * When audio loopback is enabled, the system automatically creates fast playback and recording streams
         * to implement low-latency in-ear monitoring. When audio loopback is disabled, the audio stream is destroyed.
         * If enabling audio loopback fails, you can use {@link AudioLoopback#getStatus} to query the cause. After audio
         * loopback is enabled, you can subscribe to the statusChange event to listen for audio loopback status changes.
         *
         * @permission ohos.permission.MICROPHONE
         * @param { boolean } enable - Whether to enable or disable audio loopback. **true** to enable, **false** otherwise.
         * @returns { Promise<boolean> } Promise used to return the result, indicating whether the API call is successful.
         *     **true** is successful, **false** otherwise.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @since 20
         */
        enable(enable: boolean): Promise<boolean>;
        /**
         * Sets the reverberation of the audio loopback.
         *
         * @param { AudioLoopbackReverbPreset } preset - Reverb mode.
         * @returns { boolean } Setting result. **true** if successful, **false** otherwise.
         * @throws  { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @since 21
         */
        setReverbPreset(preset: AudioLoopbackReverbPreset): boolean;
        /**
         * Get the current reverberation.
         * The default reverberation preset of audio loopback is {@link AudioLoopbackReverbPreset#THEATER} if
         * users do not modify the preset.
         *
         * @returns { AudioLoopbackReverbPreset  } Reverb mode.
         *     <br>If no reverb mode has been set, the default reverb mode is **THEATER**.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @since 21
         */
        getReverbPreset(): AudioLoopbackReverbPreset;
        /**
         * Sets the equalizer preset of the audio loopback.
         *
         * @param { AudioLoopbackEqualizerPreset } preset - Equalizer type.
         * @returns { boolean } Setting result. **true** if successful, **false** otherwise.
         * @throws  { BusinessError } 6800101 - Parameter verification failed.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @since 21
         */
        setEqualizerPreset(preset: AudioLoopbackEqualizerPreset): boolean;
        /**
         * Gets the current equalizer preset.
         * The default equalizer preset of audio loopback is {@link AudioLoopbackEqualizerPreset#FULL} if
         * users do not modify the preset.
         *
         * @returns { AudioLoopbackEqualizerPreset } Equalizer type.
         *     <br>If no equalizer type has been set, the default equalizer type is **FULL**.
         * @syscap SystemCapability.Multimedia.Audio.Capturer
         * @since 21
         */
        getEqualizerPreset(): AudioLoopbackEqualizerPreset;
    }
}
export default audio;

```
