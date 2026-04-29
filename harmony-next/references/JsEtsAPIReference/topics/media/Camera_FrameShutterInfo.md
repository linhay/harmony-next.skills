# Camera_FrameShutterInfo

```ets
typedef struct Camera_FrameShutterInfo {...} Camera_FrameShutterInfo
```

**概述**

帧快门回调信息。

起始版本： 11

相关模块： [OH_Camera](OH_Camera.md)

所在头文件： [camera.h](camera.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| int32_t captureId | 捕获id。 |
| uint64_t timestamp | 帧的时间戳，单位毫秒。 |