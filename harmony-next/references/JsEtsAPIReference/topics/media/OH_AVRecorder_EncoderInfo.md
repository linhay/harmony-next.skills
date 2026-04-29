# OH_AVRecorder_EncoderInfo

```ets
typedef struct OH_AVRecorder_EncoderInfo {...} OH_AVRecorder_EncoderInfo
```

**概述**

提供编码器信息。

起始版本： 18

相关模块： [AVRecorder](AVRecorder.md)

所在头文件： [avrecorder_base.h](avrecorder_base.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| OH_AVRecorder_CodecMimeType mimeType | 编码器MIME类型名称。 |
| char* type | 编码器类型，audio表示音频编码器，video表示视频编码器。 |
| OH_AVRecorder_Range bitRate | 比特率，包含该编码器的最大和最小值。 |
| OH_AVRecorder_Range frameRate | 视频帧率，包含帧率的最大和最小值，仅视频编码器拥有。 |
| OH_AVRecorder_Range width | 视频帧的宽度，包含宽度的最大和最小值，仅视频编码器拥有。 |
| OH_AVRecorder_Range height | 视频帧的高度，包含高度的最大和最小值，仅视频编码器拥有。 |
| OH_AVRecorder_Range channels | 音频采集声道数，包含声道数的最大和最小值，仅音频编码器拥有。 |
| int32_t* sampleRate | 音频采样率列表，包含所有可以使用的音频采样率值，仅音频编码器拥有。 |
| int32_t sampleRateLen | 音频采样率列表长度 |