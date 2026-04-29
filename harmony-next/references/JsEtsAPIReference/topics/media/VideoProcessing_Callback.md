# VideoProcessing_Callback

```ets
typedef struct VideoProcessing_Callback VideoProcessing_Callback
```

**概述**

视频处理回调对象类型。

定义一个VideoProcessing_Callback空指针，调用[OH_VideoProcessingCallback_Create](video_processing.h.md#ZH-CN_TOPIC_0000002522242050__oh_videoprocessingcallback_create)来创建一个回调对象。创建之前该指针必须为空。通过调用[OH_VideoProcessing_RegisterCallback](video_processing.h.md#ZH-CN_TOPIC_0000002522242050__oh_videoprocessing_registercallback)来向视频处理实例注册回调对象。

起始版本： 12

相关模块： [VideoProcessing](VideoProcessing.md)

所在头文件： [video_processing_types.h](video_processing_types.h.md)