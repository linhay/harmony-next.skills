# OH_VideoCaptureInfo

```ets
typedef struct OH_VideoCaptureInfo {...} OH_VideoCaptureInfo
```

#### 概述

视频录制信息。当videoFrameWidth和videoFrameHeight同时为0时，忽略视频相关参数不录制屏幕数据。

**起始版本：** 10

**相关模块：**[AVScreenCapture](AVScreenCapture.md)

**所在头文件：**[native_avscreen_capture_base.h](native_avscreen_capture_base.h.md)

#### 汇总

#### 成员变量

名称描述uint64_t displayId录制物理屏id，使用该参数需要在capturemode为CAPTURE_SPECIFIED_SCREEN模式下使用。int32_t* missionIDs指定窗口id列表，使用该参数需要在capturemode为CAPTURE_SPECIFIED_WINDOW模式下使用。int32_t missionIDsLen指定窗口ID长度，使用该参数需要在capturemode为CAPTURE_SPECIFIED_WINDOW模式下使用。int32_t videoFrameWidth采集视频的宽度设置，单位px。int32_t videoFrameHeight采集视频的高度设置，单位px。[OH_VideoSourceType](native_avscreen_capture_base.h.md#ZH-CN_TOPIC_0000002497605918__oh_videosourcetype) videoSource视频采集格式设置，目前仅支持RGBA格式。