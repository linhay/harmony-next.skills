# @ohos.multimedia.audioHaptic.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (c) 2023 Huawei Device Co., Ltd.
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
import type { Callback } from './@ohos.base';
import type audio from './@ohos.multimedia.audio';
/**
 * Audio-haptic enables users to get rhythmic auditory and haptic feedback while having incoming calls or messages.
 *
 * **Device behavior difference**: For a device without a vibration component, no vibration effect is generated.
 *
 * @syscap SystemCapability.Multimedia.AudioHaptic.Core
 * @since 11
 */
declare namespace audioHaptic {
    /**
     * Obtains an {@link AudioHapticManager} instance. This object is singleton in one process.
     *
     * @returns { AudioHapticManager } AudioHapticManager instance.
     * @syscap SystemCapability.Multimedia.AudioHaptic.Core
     * @since 11
     */
    function getAudioHapticManager(): AudioHapticManager;
    /**
     * Enumerates the audio latency modes.
     *
     * @syscap SystemCapability.Multimedia.AudioHaptic.Core
     * @since 11
     */
    enum AudioLatencyMode {
        /**
         * Normal latency mode.
         *
         * @syscap SystemCapability.Multimedia.AudioHaptic.Core
         * @since 11
         */
        AUDIO_LATENCY_MODE_NORMAL = 0,
        /**
         * Low latency mode. This mode is applicable to short audio files. A long audio file may be truncated in this mode.
         * It functions the same as
         * [SoundPool](docroot://reference/apis-media-kit/js-apis-inner-multimedia-soundPool.md#soundpool).
         *
         * @syscap SystemCapability.Multimedia.AudioHaptic.Core
         * @since 11
         */
        AUDIO_LATENCY_MODE_FAST = 1
    }
    /**
     * Describes the options for the audio-haptic player.
     *
     * @syscap SystemCapability.Multimedia.AudioHaptic.Core
     * @since 11
     */
    interface AudioHapticPlayerOptions {
        /**
         * Whether to mute the audio. **true** to mute, **false** otherwise. If this parameter is not specified, the default
         * value **false** is used.
         *
         * @syscap SystemCapability.Multimedia.AudioHaptic.Core
         * @since 11
         */
        muteAudio?: boolean;
        /**
         * Whether to mute haptics feedback. **true** to mute, **false** otherwise. If this parameter is not specified, the
         * default value **false** is used.
         *
         * @syscap SystemCapability.Multimedia.AudioHaptic.Core
         * @since 11
         */
        muteHaptics?: boolean;
    }
    /**
     * Manages the audio-haptic feature. Before calling any API in AudioHapticManager, you must use
     * [getAudioHapticManager]{@link audioHaptic.getAudioHapticManager} to create an AudioHapticManager instance.
     *
     * @syscap SystemCapability.Multimedia.AudioHaptic.Core
     * @since 11
     */
    interface AudioHapticManager {
        /**
         * Registers audio and haptic resources via URIs. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > A maximum of 128 resources can be registered at the same time for an application. Any attempt to register
         * > beyond this limit will fail (returning a negative resource ID). You are advised to reasonably manage the number
         * > of registered resources. For resources that are no longer used, you are advised to unregister them in a timely
         * > manner.
         *
         * @param { string } audioUri - URI of the audio source.<br>- For details about the supported audio resource formats
         *     and path formats in the normal latency mode, see [AVPlayer]{@link @ohos.multimedia.media:media}.<br>- For
         *     details about the supported audio resource formats in the low-latency mode, see
         *     [SoundPool](docroot://reference/apis-media-kit/js-apis-inner-multimedia-soundPool.md#soundpool). The path
         *     format must meet the requirements described in
         *     [fileIo.open](docroot://reference/apis-core-file-kit/js-apis-file-fs.md#fileioopen).<br>- In both modes, you
         *     are advised to pass in the absolute path of the file.
         * @param { string } hapticUri - URI of the haptic source.<br>For details about the supported haptic resource
         *     formats, see [HapticFileDescriptor]{@link @ohos.vibrator:vibrator.HapticFileDescriptor}. The path format must
         *     meet the requirements described in
         *     [fileIo.open](docroot://reference/apis-core-file-kit/js-apis-file-fs.md#fileioopen).<br>You are advised to
         *     pass in the absolute path of the file.
         * @returns { Promise<number> } Promise, which returns the registered resource ID.
         *     <br>In normal cases, the returned resource ID is a non-negative number. A negative ID indicates a registration
         *     failure. In this case, check whether the number of registered resources exceeds the upper limit.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *                                 1.Mandatory parameters are left unspecified;
         *                                 2.Incorrect parameter types.
         * @syscap SystemCapability.Multimedia.AudioHaptic.Core
         * @since 11
         */
        registerSource(audioUri: string, hapticUri: string): Promise<number>;
        /**
         * Unregisters an audio-haptic source. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > For resources that are no longer used, you are advised to unregister them in a timely manner to avoid issues
         * > such as resource leaks or the number of resources exceeding the upper limit.
         *
         * @param { number } id - Source ID.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @syscap SystemCapability.Multimedia.AudioHaptic.Core
         * @since 11
         */
        unregisterSource(id: number): Promise<void>;
        /**
         * Sets the latency mode for an audio-haptic source.
         *
         * @param { number } id - Source ID.
         * @param { AudioLatencyMode } latencyMode - Audio latency mode.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 5400102 - Operation not allowed.
         * @syscap SystemCapability.Multimedia.AudioHaptic.Core
         * @since 11
         */
        setAudioLatencyMode(id: number, latencyMode: AudioLatencyMode): void;
        /**
         * Sets the stream usage for an audio-haptic source.
         *
         * @param { number } id - Source ID.
         * @param { audio.StreamUsage } usage - Stream usage.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types;
         *     3.Parameter verification failed.
         * @throws { BusinessError } 5400102 - Operation not allowed.
         * @syscap SystemCapability.Multimedia.AudioHaptic.Core
         * @since 11
         */
        setStreamUsage(id: number, usage: audio.StreamUsage): void;
        /**
         * Create an audio haptic player. This method uses a promise to return the result. If haptics is needed, caller
         * should have the permission of ohos.permission.VIBRATE.
         *
         * @permission ohos.permission.VIBRATE
         * @param { number } id - Source ID.
         * @param { AudioHapticPlayerOptions } options - Options of the audio-haptic player.
         * @returns { Promise<AudioHapticPlayer> } Promise used to return the audio-haptic player.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Incorrect parameter types.
         * @throws { BusinessError } 5400102 - Operation not allowed.
         * @throws { BusinessError } 5400103 - I/O error.
         * @throws { BusinessError } 5400106 - Unsupport format.
         * @syscap SystemCapability.Multimedia.AudioHaptic.Core
         * @since 11
         */
        createPlayer(id: number, options?: AudioHapticPlayerOptions): Promise<AudioHapticPlayer>;
        /**
         * Registers audio and haptic resources via file descriptors. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > A maximum of 128 resources can be registered at the same time for an application. Any attempt to register
         * > beyond this limit will fail (returning a negative resource ID). You are advised to reasonably manage the number
         * > of registered resources. For resources that are no longer used, you are advised to unregister them in a timely
         * > manner.
         *
         * @param { AudioHapticFileDescriptor } audioFd - Valid file descriptor object that has been opened, used to
         *     describe the audio file. The offset and length must match the actual file length.
         * @param { AudioHapticFileDescriptor } hapticFd - Valid file descriptor object that has been opened, used to
         *     describe the haptic file. The offset and length must match the actual file length.
         * @returns { Promise<number> } Promise, which returns the registered resource ID.
         *     <br>In normal cases, the returned resource ID is a non-negative number. A negative ID indicates a registration
         *     failure. In this case, check whether the number of registered resources exceeds the upper limit.
         * @syscap SystemCapability.Multimedia.AudioHaptic.Core
         * @since 20
         */
        registerSourceFromFd(audioFd: AudioHapticFileDescriptor, hapticFd: AudioHapticFileDescriptor): Promise<number>;
    }
    /**
     * Enumerates the audio haptic types.
     *
     * @syscap SystemCapability.Multimedia.AudioHaptic.Core
     * @since 11
     */
    enum AudioHapticType {
        /**
         * Audio.
         *
         * @syscap SystemCapability.Multimedia.AudioHaptic.Core
         * @since 11
         */
        AUDIO_HAPTIC_TYPE_AUDIO = 0,
        /**
         * Haptic.
         *
         * @syscap SystemCapability.Multimedia.AudioHaptic.Core
         * @since 11
         */
        AUDIO_HAPTIC_TYPE_HAPTIC = 1
    }
    /**
     * Describes the audio-haptic file descriptor.
     *
     * > **NOTE**
     * >
     * > Ensure that **fd** is an available file descriptor and the values of **offset** and **length** are correct.
     *
     * @syscap SystemCapability.Multimedia.AudioHaptic.Core
     * @since 20
     */
    interface AudioHapticFileDescriptor {
        /**
         * File descriptor of the audio-haptic file, which is generally greater than or equal to 0.
         *
         * @syscap SystemCapability.Multimedia.AudioHaptic.Core
         * @since 20
         */
        fd: number;
        /**
         * Number of bytes to read. By default, the length is the number of bytes remaining in the file from the offset
         * position.
         *
         * @syscap SystemCapability.Multimedia.AudioHaptic.Core
         * @since 20
         */
        length?: number;
        /**
         * Offset for reading data from the file, in bytes. By default, the offset is 0.
         *
         * @syscap SystemCapability.Multimedia.AudioHaptic.Core
         * @since 20
         */
        offset?: number;
    }
    /**
     * Implements audio-haptic playback. Before calling any API in AudioHapticPlayer, you must use
     * [createPlayer]{@link audioHaptic.AudioHapticManager.createPlayer(id: number, options?: AudioHapticPlayerOptions)}
     * to create an AudioHapticPlayer instance.
     *
     * @syscap SystemCapability.Multimedia.AudioHaptic.Core
     * @since 11
     */
    interface AudioHapticPlayer {
        /**
         * Checks whether an audio-haptic type is muted.
         *
         * @param { AudioHapticType } type - Audio-haptic type.
         * @returns { boolean } Check result for whether the audio-haptic type is muted. **true** if muted, **false**
         *     otherwise.
         * @throws { BusinessError } 401 - Parameter error. Possible causes:
         *     1.Mandatory parameters are left unspecified;
         *     2.Parameter verification failed.
         * @syscap SystemCapability.Multimedia.AudioHaptic.Core
         * @since 11
         */
        isMuted(type: AudioHapticType): boolean;
        /**
         * Starts playback. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 5400102 - Operate not permit.
         * @throws { BusinessError } 5400103 - IO error.
         * @throws { BusinessError } 5400105 - Service died.
         * @syscap SystemCapability.Multimedia.AudioHaptic.Core
         * @since 11
         */
        start(): Promise<void>;
        /**
         * Stops playback. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 5400102 - Operate not permit.
         * @throws { BusinessError } 5400105 - Service died.
         * @syscap SystemCapability.Multimedia.AudioHaptic.Core
         * @since 11
         */
        stop(): Promise<void>;
        /**
         * Releases this audio-haptic player. This API uses a promise to return the result.
         *
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 5400105 - Service died.
         * @syscap SystemCapability.Multimedia.AudioHaptic.Core
         * @since 11
         */
        release(): Promise<void>;
        /**
         * Subscribes to end of stream (EOS) event, which is triggered when the audio stream playback ends. This API uses an
         * asynchronous callback to return the result.
         *
         * @param { 'endOfStream' } type - Event type. The event **'endOfStream'** is triggered when the audio stream
         *     playback ends.
         * @param { Callback<void> } callback - Callback that returns no value.
         * @syscap SystemCapability.Multimedia.AudioHaptic.Core
         * @since 11
         */
        on(type: 'endOfStream', callback: Callback<void>): void;
        /**
         * Unsubscribes from the EOS event. This API uses an asynchronous callback to return the result.
         *
         * @param { 'endOfStream' } type - Event type. The event **'endOfStream'** is triggered when the audio stream
         *     playback ends.
         * @param { Callback<void> } [callback] - Callback that returns no value.
         * @syscap SystemCapability.Multimedia.AudioHaptic.Core
         * @since 11
         */
        off(type: 'endOfStream', callback?: Callback<void>): void;
        /**
         * Subscribes to the audio interruption event, which is triggered when the audio focus is changed. This API uses an
         * asynchronous callback to return the result.
         *
         * @param { 'audioInterrupt' } type - Event type. The event **'audioInterrupt'** is triggered when the audio focus
         *     is changed.
         * @param { Callback<audio.InterruptEvent> } callback - Callback used to return the event information.
         * @syscap SystemCapability.Multimedia.AudioHaptic.Core
         * @since 11
         */
        on(type: 'audioInterrupt', callback: Callback<audio.InterruptEvent>): void;
        /**
         * Unsubscribes from the audio interruption event. This API uses an asynchronous callback to return the result.
         *
         * @param { 'audioInterrupt' } type - Event type. The event **'audioInterrupt'** is triggered when the audio focus
         *     is changed.
         * @param { Callback<audio.InterruptEvent> } callback - Callback used to return the event information.
         * @syscap SystemCapability.Multimedia.AudioHaptic.Core
         * @since 11
         */
        off(type: 'audioInterrupt', callback?: Callback<audio.InterruptEvent>): void;
        /**
         * Sets the volume for this audio-haptic player. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API must be called before the audio-haptic player is released.
         *
         * @param { number } volume - Volume, in the range [0.00, 1.00], where 1.00 indicates the maximum volume (100%).
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 5400102 - Operate not permit in current state.
         * @throws { BusinessError } 5400105 - Service died.
         * @throws { BusinessError } 5400108 - Parameter out of range.
         * @syscap SystemCapability.Multimedia.AudioHaptic.Core
         * @since 20
         */
        setVolume(volume: number): Promise<void>;
        /**
         * Sets this audio-haptic player to play in a loop. This API uses a promise to return the result.
         *
         * > **NOTE**
         * >
         * > This API must be called before the audio-haptic player is released.
         *
         * @param { boolean } loop - Whether to play in a loop. **true** to play in a loop, **false** otherwise.
         * @returns { Promise<void> } Promise that returns no value.
         * @throws { BusinessError } 5400102 - Operate not permit in current state.
         * @syscap SystemCapability.Multimedia.AudioHaptic.Core
         * @since 20
         */
        setLoop(loop: boolean): Promise<void>;
    }
}
export default audioHaptic;

```
