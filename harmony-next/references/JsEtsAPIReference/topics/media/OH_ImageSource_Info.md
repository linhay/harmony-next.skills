# OH_ImageSource_Info

```ets
struct OH_ImageSource_Info
```

**概述**

OH_ImageSource_Info是native层封装的ImageSource信息结构体，OH_ImageSource_Info结构体不可直接操作，而是采用函数调用方式创建、释放结构体以及操作具体字段。

创建OH_ImageSource_Info对象使用[OH_ImageSourceInfo_Create](image_source_native.h.md#ZH-CN_TOPIC_0000002522081986__oh_imagesourceinfo_create)函数。

释放OH_ImageSource_Info对象使用[OH_ImageSourceInfo_Release](image_source_native.h.md#ZH-CN_TOPIC_0000002522081986__oh_imagesourceinfo_release)函数。调用该接口之后，与OH_ImageSourceInfo结构体相关的属性均会被释放。因此在调用该接口前，请务必确认相关属性已不再被需要或对相关属性已完成深拷贝操作。

OH_ImageSource_Info结构体内容和操作方式如下：

| 字段类型 | 字段名称 | 字段描述 | 操作函数 | 函数描述 |
| --- | --- | --- | --- | --- |
| uint32_t | width | 图片宽度 | OH_ImageSourceInfo_GetWidth | 获取图片的宽。 |
| uint32_t | height | 图片高度 | OH_ImageSourceInfo_GetHeight | 获取图片的高。 |
| bool | isHdr | 是否为高动态范围（HDR）的信息 | OH_ImageSourceInfo_GetDynamicRange | 获取图片是否为高动态范围的信息。 |
| Image_MimeType | mimeType | 图片源的MIME类型 | OH_ImageSourceInfo_GetMimetype | 获取图片的MimeType。 |

起始版本： 13

相关模块： [Image_NativeModule](Image_NativeModule.md)

所在头文件： [image_source_native.h](image_source_native.h.md)