# OhosImageSourceSupportedFormat

```ets
struct OhosImageSourceSupportedFormat {...}
```

**概述**

定义图像源支持的格式字符串。此选项给[OhosImageSourceSupportedFormatList](OhosImageSourceSupportedFormatList.md)和[OH_ImageSource_GetSupportedFormats](image_source_mdk.h.md#ZH-CN_TOPIC_0000002553361909__oh_imagesource_getsupportedformats)接口使用。

起始版本： 10

相关模块： [Image](Image.md)

所在头文件： [image_source_mdk.h](image_source_mdk.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| char* format = nullptr | 图像源支持的格式字符串头地址。 |
| size_t size = 0 | 图像源支持的格式字符串大小。 |