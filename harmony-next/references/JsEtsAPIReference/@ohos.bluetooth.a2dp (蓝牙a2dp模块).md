# @ohos.bluetooth.a2dp (蓝牙a2dp模块)

本模块提供基于增强音频分发协议（Advanced Audio Distribution Profile，[A2DP](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/terminology#a2dp)）的蓝牙媒体音频能力，支持获取媒体播放状态和连接状态等方法。

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { a2dp } from '@kit.ConnectivityKit';
```

#### BaseProfile

type BaseProfile = baseProfile.BaseProfile

基础Profile接口定义，提供监听和获取连接状态等公共能力。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

类型说明[baseProfile.BaseProfile](@ohos.bluetooth.baseProfile (蓝牙baseProfile模块).md#ZH-CN_TOPIC_0000002497445438__baseprofile)基础Profile接口定义。

#### a2dp.createA2dpSrcProfile

createA2dpSrcProfile(): A2dpSourceProfile

创建蓝牙媒体[A2DP Source](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/terminology#a2dp-source)实例。通过该实例可使用本端作为A2DP Source设备的方法，如：获取和其他设备间的蓝牙媒体音频播放状态。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**返回值：**

类型说明[A2dpSourceProfile](#ZH-CN_TOPIC_0000002529445381__a2dpsourceprofile)返回蓝牙媒体音频源实例。

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息401Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801Capability not supported.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
try {
    let a2dpProfile = a2dp.createA2dpSrcProfile();
    console.info('a2dp success');
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### A2dpSourceProfile

该实例表示蓝牙媒体音频中的[A2DP Source](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/terminology#a2dp-source)角色。

- 该类继承于[BaseProfile](#ZH-CN_TOPIC_0000002529445381__baseprofile)，因此可以使用其父类中的方法。
- 使用该类的方法前，需通过[createA2dpSrcProfile](#ZH-CN_TOPIC_0000002529445381__a2dpcreatea2dpsrcprofile)方法构造该类的实例。
- 和该实例角色相对应的是[A2DP Sink](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/terminology#a2dp-sink)。

#### getPlayingState

getPlayingState(deviceId: string): PlayingState

获取本端和对端设备间的媒体音频播放状态。

- 从API version 21开始，此接口支持使用对端设备的实际MAC地址获取媒体音频播放状态。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

参数名类型必填说明deviceIdstring是对端设备地址，例如："XX:XX:XX:XX:XX:XX"。

**返回值：**

类型说明[PlayingState](#ZH-CN_TOPIC_0000002529445381__playingstate)蓝牙媒体音频播放状态。

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

错误码ID错误信息201Permission denied.401Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801Capability not supported.2900001Service stopped.2900003Bluetooth disabled.2900004Profile not supported.2900099Operation failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
try {
    let a2dpSrc = a2dp.createA2dpSrcProfile();
    let state = a2dpSrc.getPlayingState('XX:XX:XX:XX:XX:XX');
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### PlayingState

枚举，蓝牙媒体音频播放状态。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

名称值说明STATE_NOT_PLAYING0未播放媒体音频。STATE_PLAYING1正在播放媒体音频。

#### CodecInfo11+

蓝牙媒体音频使用的编解码器。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

名称类型只读可选说明codecType[CodecType](#ZH-CN_TOPIC_0000002529445381__codectype11)否否编解码器类型，默认值为CODEC_TYPE_SBC。codecBitsPerSample[CodecBitsPerSample](#ZH-CN_TOPIC_0000002529445381__codecbitspersample11)否否每个采样点的位深，默认值为CODEC_BITS_PER_SAMPLE_NONE。codecChannelMode[CodecChannelMode](#ZH-CN_TOPIC_0000002529445381__codecchannelmode11)否否编解码器的声道模式，默认值为CODEC_CHANNEL_MODE_NONE。codecSampleRate[CodecSampleRate](#ZH-CN_TOPIC_0000002529445381__codecsamplerate11)否否编解码器的采样率，默认值为CODEC_SAMPLE_RATE_NONE。codecBitRate19+[CodecBitRate](#ZH-CN_TOPIC_0000002529445381__codecbitrate19)否是编解码器的码率，默认值为CODEC_BIT_RATE_ABR。codecFrameLength19+[CodecFrameLength](#ZH-CN_TOPIC_0000002529445381__codecframelength19)否是编解码器的帧长，默认值为CODEC_FRAME_LENGTH_10MS。

#### CodecInfoList19+

蓝牙媒体音频编解码器支持的能力集合。不同编解码器支持的位深、声道模式、采样率、码率和帧长类型与音频接收器设备端能力有关。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

名称类型只读可选说明codecType[CodecType](#ZH-CN_TOPIC_0000002529445381__codectype11)否否编解码器类型。codecBitsPerSampleArray[CodecBitsPerSample](#ZH-CN_TOPIC_0000002529445381__codecbitspersample11)[]否否编解码器支持的位深能力集合。codecChannelModeArray[CodecChannelMode](#ZH-CN_TOPIC_0000002529445381__codecchannelmode11)[]否否编解码器支持的声道模式能力集合。codecSampleRateArray[CodecSampleRate](#ZH-CN_TOPIC_0000002529445381__codecsamplerate11)[]否否编解码器支持的采样率能力集合。codecBitRateArray[CodecBitRate](#ZH-CN_TOPIC_0000002529445381__codecbitrate19)[]否否编解码器支持的码率能力集合。codecFrameLengthArray[CodecFrameLength](#ZH-CN_TOPIC_0000002529445381__codecframelength19)[]否否编解码器支持的帧长能力集合。

#### CodecType11+

枚举，蓝牙媒体音频编解码器类型。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

名称值说明CODEC_TYPE_INVALID-1编解码器类型未知。CODEC_TYPE_SBC0SBCCODEC_TYPE_AAC1AACCODEC_TYPE_L2HC2L2HCCODEC_TYPE_L2HCST13+3L2HCSTCODEC_TYPE_LDAC13+4LDAC

#### CodecChannelMode11+

枚举，蓝牙媒体音频编解码器的声道模式，表示音频播放时独立的空间信号路径数量。声道模式影响声音的立体感和空间定位‌。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

名称值说明CODEC_CHANNEL_MODE_NONE0声道未知。CODEC_CHANNEL_MODE_MONO1单声道。CODEC_CHANNEL_MODE_STEREO2双声道。

#### CodecBitsPerSample11+

枚举，蓝牙媒体音频编解码器的位深，表示蓝牙音频信号在数字表示中使用的位数，单位为bit。位深决定每个采样点可以表示的动态范围和精度。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

名称值说明CODEC_BITS_PER_SAMPLE_NONE0位深未知。CODEC_BITS_PER_SAMPLE_16116bitCODEC_BITS_PER_SAMPLE_24224bitCODEC_BITS_PER_SAMPLE_32332bit

#### CodecSampleRate11+

枚举，蓝牙媒体音频编解码器的采样率，表示每秒对蓝牙音频采样的次数，单位为Hz。采样率的选择会影响音质和传输效率。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

名称值说明CODEC_SAMPLE_RATE_NONE0采样率未知。CODEC_SAMPLE_RATE_44100144.1kHzCODEC_SAMPLE_RATE_48000248kHzCODEC_SAMPLE_RATE_88200388.2kHzCODEC_SAMPLE_RATE_96000496kHzCODEC_SAMPLE_RATE_1764005176.4kHzCODEC_SAMPLE_RATE_1920006192kHz

#### CodecBitRate19+

枚举，蓝牙媒体音频编解码器的码率，表示单位时间内音频数据的传输量，单位为kbps。码率影响音频音质和文件大小。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

名称值说明CODEC_BIT_RATE_96000096kbpsCODEC_BIT_RATE_1280001128kbpsCODEC_BIT_RATE_1920002192kbpsCODEC_BIT_RATE_2560003256kbpsCODEC_BIT_RATE_3200004320kbpsCODEC_BIT_RATE_4800005480kbpsCODEC_BIT_RATE_6400006640kbpsCODEC_BIT_RATE_9600007960kbpsCODEC_BIT_RATE_ABR8自适应码率（根据网络条件自动调整）。CODEC_BIT_RATE_150000021+91500kbpsCODEC_BIT_RATE_230000021+102300kbps

#### CodecFrameLength19+

枚举，蓝牙媒体音频编解码器的帧长，表示一帧音频数据播放的时长。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

名称值说明CODEC_FRAME_LENGTH_5MS05ms帧长。CODEC_FRAME_LENGTH_10MS110ms帧长。