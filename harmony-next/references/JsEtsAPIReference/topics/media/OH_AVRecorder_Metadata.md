# OH_AVRecorder_Metadata

```ets
typedef struct OH_AVRecorder_Metadata {...} OH_AVRecorder_Metadata
```

**概述**

元数据信息数据结构。

起始版本： 18

相关模块： [AVRecorder](AVRecorder.md)

所在头文件： [avrecorder_base.h](avrecorder_base.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| char* genre | 媒体资源的类型或体裁。 |
| char* videoOrientation | 视频的旋转方向，单位为度。 |
| OH_AVRecorder_Location location | 视频的地理位置信息。 |
| OH_AVRecorder_MetadataTemplate customInfo | 从 moov.meta.list 读取的自定义参数键值映射。 |