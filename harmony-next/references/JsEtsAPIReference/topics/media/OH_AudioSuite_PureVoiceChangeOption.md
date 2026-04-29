# OH_AudioSuite_PureVoiceChangeOption

```ets
typedef struct {...} OH_AudioSuite_PureVoiceChangeOption
```

**概述**

定义音频编创传统变声选项。

起始版本： 23

相关模块： [OHAudioSuite](OHAudioSuite.md)

所在头文件： [native_audio_suite_base.h](native_audio_suite_base.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| OH_AudioSuite_PureVoiceChangeGenderOption optionGender | 定义传统变声性别。 |
| OH_AudioSuite_PureVoiceChangeType optionType | 定义传统变声类型。 |
| float pitch | 定义传统变声音调。如果使用系统中的默认音调以获得最佳效果, 设置为OH_PURE_VOICE_DEFAULT_PITCH。  设置自定义音调的取值范围为[0.3f, 3.0f]。 |