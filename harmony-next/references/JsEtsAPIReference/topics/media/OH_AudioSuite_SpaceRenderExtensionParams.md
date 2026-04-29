# OH_AudioSuite_SpaceRenderExtensionParams

```ets
struct OH_AudioSuite_SpaceRenderExtensionParams {...}
```

**概述**

定义空间渲染效果节点扩展模式配置参数。

起始版本： 23

相关模块： [OHAudioSuite](OHAudioSuite.md)

所在头文件： [native_audio_suite_base.h](native_audio_suite_base.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| float extRadius | 扩展半径。取值范围为[1.0, 5.0]，单位为米。 |
| int32_t extAngle | 扩展角度。取值范围为(0, 360)，单位为度。 |