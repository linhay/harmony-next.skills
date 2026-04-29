# OH_AVMetadataExtractor_FrameInfo

```ets
typedef struct {...} OH_AVMetadataExtractor_FrameInfo
```

**概述**

定义从视频中提取出的帧的信息。

起始版本： 23

相关模块： [AVMetadataExtractor](AVMetadataExtractor.md)

所在头文件： [avmetadata_extractor_base.h](avmetadata_extractor_base.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| int64_t requestTimeUs | 用户传入的请求时间。 |
| int64_t actualTimeUs | 实际提取到的帧的时间；若提取失败，则为-1。 |
| OH_PixelmapNative* image | 从视频中提取出的帧图像；若提取失败，则为空指针。 |
| OH_AVMetadataExtractor_FetchState result | 本次帧提取操作的结果状态。 |