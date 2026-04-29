# PhotoOutput_Callbacks

```ets
typedef struct PhotoOutput_Callbacks {...} PhotoOutput_Callbacks
```

**概述**

拍照输出的回调。

起始版本： 11

相关模块： [OH_Camera](OH_Camera.md)

所在头文件： [photo_output.h](photo_output.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| OH_PhotoOutput_OnFrameStart onFrameStart | 拍照输出帧启动事件。 |
| OH_PhotoOutput_OnFrameShutter onFrameShutter | 拍照输出帧快门事件。 |
| OH_PhotoOutput_OnFrameEnd onFrameEnd | 拍照输出帧结束事件。 |
| OH_PhotoOutput_OnError onError | 拍照输出错误事件。 |