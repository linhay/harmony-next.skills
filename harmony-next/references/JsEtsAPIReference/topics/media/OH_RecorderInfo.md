# OH_RecorderInfo

```ets
typedef struct OH_RecorderInfo {...} OH_RecorderInfo
```

**概述**

录制文件信息。

起始版本： 10

相关模块： [AVScreenCapture](AVScreenCapture.md)

所在头文件： [native_avscreen_capture_base.h](native_avscreen_capture_base.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| char* url | 录制文件的URL。 |
| uint32_t urlLen | 录制文件的URL长度。 |
| OH_ContainerFormatType fileFormat | 录制文件的格式。 |