# @ohos.bluetooth.a2dp.d.ts

> API 26.0.0 Release declaration snapshot from DevEco Studio SDK 26.0.0.105.

```ts
/*
 * Copyright (C) 2023-2024 Huawei Device Co., Ltd.
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
 * @kit ConnectivityKit
 */
import type baseProfile from './@ohos.bluetooth.baseProfile';
/**
 * Provides methods to accessing bluetooth audio related capabilities.
 *
 * @syscap SystemCapability.Communication.Bluetooth.Core
 * @crossplatform [since 13]
 * @since 10
 */
declare namespace a2dp {
    /**
     * Base interface of profile.
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @since 10
     */
    type BaseProfile = baseProfile.BaseProfile;
    /**
     * create the instance of a2dp profile.
     *
     * @returns { A2dpSourceProfile } Returns the instance of profile.
     * @throws { BusinessError } 401 - Invalid parameter.Possible causes: 1. Mandatory parameters are left unspecified.
     *     2. Incorrect parameter types. 3. Parameter verification failed.
     * @throws { BusinessError } 801 - Capability not supported.
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @crossplatform [since 13]
     * @since 10
     */
    function createA2dpSrcProfile(): A2dpSourceProfile;
    /**
     * Manager a2dp source profile.
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @crossplatform [since 13]
     * @since 10
     */
    interface A2dpSourceProfile extends BaseProfile {
        /**
         * Obtains the playing state of device.
         *
         * @permission ohos.permission.ACCESS_BLUETOOTH
         * @param { string } deviceId - Indicates device ID. For example, "11:22:33:AA:BB:FF".
         * @returns { PlayingState } Returns the playing state.
         * @throws { BusinessError } 201 - Permission denied.
         * @throws { BusinessError } 401 - Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified.
         *     2. Incorrect parameter types. 3. Parameter verification failed.
         * @throws { BusinessError } 801 - Capability not supported.
         * @throws { BusinessError } 2900001 - Service stopped.
         * @throws { BusinessError } 2900003 - Bluetooth disabled.
         * @throws { BusinessError } 2900004 - Profile not supported.
         * @throws { BusinessError } 2900099 - Operation failed.
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 10
         */
        getPlayingState(deviceId: string): PlayingState;
    }
    /**
     * Describes the codec information.
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @since 11
     */
    interface CodecInfo {
        /**
         * codec type
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 11
         */
        codecType: CodecType;
        /**
         * codec bits per sample.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 11
         */
        codecBitsPerSample: CodecBitsPerSample;
        /**
         * codec channel mode.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 11
         */
        codecChannelMode: CodecChannelMode;
        /**
         * codec sample rate.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 11
         */
        codecSampleRate: CodecSampleRate;
        /**
         * codec bit rate.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 19
         */
        codecBitRate?: CodecBitRate;
        /**
         * codec frame length.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 19
         */
        codecFrameLength?: CodecFrameLength;
    }
    /**
     * Describes the codec information.
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @since 19
     */
    interface CodecInfoList {
        /**
         * codec type
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 19
         */
        codecType: CodecType;
        /**
         * codec bits per sample list.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 19
         */
        codecBitsPerSampleArray: CodecBitsPerSample[];
        /**
         * codec channel mode list.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 19
         */
        codecChannelModeArray: CodecChannelMode[];
        /**
         * codec sample rate list.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 19
         */
        codecSampleRateArray: CodecSampleRate[];
        /**
         * codec bit rate list.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 19
         */
        codecBitRateArray: CodecBitRate[];
        /**
         * codec frame length list.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 19
         */
        codecFrameLengthArray: CodecFrameLength[];
    }
    /**
     * The enum of a2dp playing state.
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @since 10
     */
    enum PlayingState {
        /**
         * Not playing.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 10
         */
        STATE_NOT_PLAYING = 0,
        /**
         * Playing.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 10
         */
        STATE_PLAYING = 1
    }
    /**
     * Describes the codec type.
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @since 11
     */
    enum CodecType {
        /**
         * invalid codec type.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 11
         */
        CODEC_TYPE_INVALID = -1,
        /**
         * SBC - Sub-band coding.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 11
         */
        CODEC_TYPE_SBC = 0,
        /**
         * AAC - Advanced Audio Coding.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 11
         */
        CODEC_TYPE_AAC = 1,
        /**
         * L2HC.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 11
         */
        CODEC_TYPE_L2HC = 2,
        /**
         * L2HCST.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 13
         */
        CODEC_TYPE_L2HCST = 3,
        /**
         * LDAC.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 13
         */
        CODEC_TYPE_LDAC = 4
    }
    /**
     * Describes the codec channel mode.
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @since 11
     */
    enum CodecChannelMode {
        /**
         * Codec channel mode none.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 11
         */
        CODEC_CHANNEL_MODE_NONE = 0,
        /**
         * Codec channel mode MONO.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 11
         */
        CODEC_CHANNEL_MODE_MONO = 1,
        /**
         * Codec channel mode STEREO.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 11
         */
        CODEC_CHANNEL_MODE_STEREO = 2
    }
    /**
     * Describes the codec bits per sample.
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @since 11
     */
    enum CodecBitsPerSample {
        /**
         * Codec bits per sample none.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 11
         */
        CODEC_BITS_PER_SAMPLE_NONE = 0,
        /**
         * Codec 16 bits per sample.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 11
         */
        CODEC_BITS_PER_SAMPLE_16 = 1,
        /**
         * Codec 24 bits per sample.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 11
         */
        CODEC_BITS_PER_SAMPLE_24 = 2,
        /**
         * Codec 32 bits per sample.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 11
         */
        CODEC_BITS_PER_SAMPLE_32 = 3
    }
    /**
     * Describes the codec sample rate.
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @since 11
     */
    enum CodecSampleRate {
        /**
         * Codec sample rate none.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 11
         */
        CODEC_SAMPLE_RATE_NONE = 0,
        /**
         * Codec sample rate 44.1k.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 11
         */
        CODEC_SAMPLE_RATE_44100 = 1,
        /**
         * Codec sample rate 48k.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 11
         */
        CODEC_SAMPLE_RATE_48000 = 2,
        /**
         * Codec sample rate 88.2k.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 11
         */
        CODEC_SAMPLE_RATE_88200 = 3,
        /**
         * Codec sample rate 96k.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 11
         */
        CODEC_SAMPLE_RATE_96000 = 4,
        /**
         * Codec sample rate 176.4k.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 11
         */
        CODEC_SAMPLE_RATE_176400 = 5,
        /**
         * Codec sample rate 192k.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 11
         */
        CODEC_SAMPLE_RATE_192000 = 6
    }
    /**
     * Describes the codec bit rate.
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @since 19
     */
    enum CodecBitRate {
        /**
         * Codec bit rate 96k.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 19
         */
        CODEC_BIT_RATE_96000 = 0,
        /**
         * Codec bit rate 128k.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 19
         */
        CODEC_BIT_RATE_128000 = 1,
        /**
         * Codec bit rate 192k.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 19
         */
        CODEC_BIT_RATE_192000 = 2,
        /**
         * Codec bit rate 256k.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 19
         */
        CODEC_BIT_RATE_256000 = 3,
        /**
         * Codec bit rate 320k.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 19
         */
        CODEC_BIT_RATE_320000 = 4,
        /**
         * Codec bit rate 480k.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 19
         */
        CODEC_BIT_RATE_480000 = 5,
        /**
         * Codec bit rate 640k.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 19
         */
        CODEC_BIT_RATE_640000 = 6,
        /**
         * Codec bit rate 960k.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 19
         */
        CODEC_BIT_RATE_960000 = 7,
        /**
         * Codec bit rate adaptive bitrate streaming.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 19
         */
        CODEC_BIT_RATE_ABR = 8,
        /**
         * Codec bit rate 1.5M.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 21
         */
        CODEC_BIT_RATE_1500000 = 9,
        /**
         * Codec bit rate 2.3M.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 21
         */
        CODEC_BIT_RATE_2300000 = 10
    }
    /**
     * Describes the codec frame length.
     *
     * @syscap SystemCapability.Communication.Bluetooth.Core
     * @since 19
     */
    enum CodecFrameLength {
        /**
         * Codec frame length 5ms.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 19
         */
        CODEC_FRAME_LENGTH_5MS = 0,
        /**
         * Codec frame length 10ms.
         *
         * @syscap SystemCapability.Communication.Bluetooth.Core
         * @since 19
         */
        CODEC_FRAME_LENGTH_10MS = 1
    }
}
export default a2dp;

```
