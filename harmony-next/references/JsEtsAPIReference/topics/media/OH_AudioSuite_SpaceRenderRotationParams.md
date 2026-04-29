# OH_AudioSuite_SpaceRenderRotationParams

```ets
typedef struct {...} OH_AudioSuite_SpaceRenderRotationParams
```

**概述**

定义空间渲染效果节点旋转模式配置参数。

起始版本： 23

相关模块： [OHAudioSuite](OHAudioSuite.md)

所在头文件： [native_audio_suite_base.h](native_audio_suite_base.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| float x | 空间中的X坐标。取值范围为[-5.0, 5.0]，单位为米。 |
| float y | 空间中的Y坐标。取值范围为[-5.0, 5.0]，单位为米。 |
| float z | 空间中的Z坐标。取值范围为[-5.0, 5.0]，单位为米。 |
| int32_t surroundTime | 单周环绕时间。取值范围为[2, 40]，单位为秒。 |
| OH_AudioSuite_SurroundDirection surroundDirection | 单周环绕方向。取值范围为[0, 1]。 |