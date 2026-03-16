# OH_AudioDataArray

```ets
typedef struct {...} OH_AudioDataArray
```

#### 概述

定义多路输出渲染接口的输入数据描述。当管线中存在多输出效果节点时，通过多输出渲染接口获取处理过后的音频数据。

**起始版本：** 22

**相关模块：**[OHAudioSuite](OHAudioSuite.md)

**所在头文件：**[native_audio_suite_base.h](../../capi/headers/native_audio_suite_base.h.md)

#### 汇总

#### 成员变量

名称描述void **audioDataArray需要输出的音频数据地址。int32_t arraySize音频数组大小。int32_t requestFrameSizeaudioDataArray数组中地址的内存大小（单位为字节），应确保每个地址均具有requestFrameSize字节个大小。