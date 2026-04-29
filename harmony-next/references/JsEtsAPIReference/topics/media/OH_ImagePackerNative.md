# OH_ImagePackerNative

```ets
typedef struct OH_ImagePackerNative OH_ImagePackerNative
```

**概述**

ImagePacker结构体类型，用于执行ImagePacker相关操作。

此结构体内容不可直接操作，采用函数调用方式操作具体字段，结构体内容和操作方式如下：

| 字段类型 | 字段名称 | 字段描述 | 操作函数 | 函数描述 |
| --- | --- | --- | --- | --- |
| OH_ImageSourceNative | imageSource | 图片源 | OH_ImagePackerNative_PackToDataFromImageSource | 将ImageSource编码为指定格式的数据。 |
| OH_PixelmapNative | pixelmap | native层的pixelmap | OH_ImagePackerNative_PackToDataFromPixelmap | 将Pixelmap编码为指定格式的数据。 |
| int32_t | imagesourceFd | imagesource关联的文件描述符 | OH_ImagePackerNative_PackToFileFromImageSource | 将一个ImageSource编码到文件中。 |
| int32_t | pixelmapFd | pixelmap关联的文件描述符 | OH_ImagePackerNative_PackToFileFromPixelmap | 将一个Pixelmap编码到文件中。 |

创建OH_ImagePackerNative对象使用[OH_ImagePackerNative_Create](image_packer_native.h.md#ZH-CN_TOPIC_0000002522241980__oh_imagepackernative_create)函数。

释放OH_ImagePackerNative对象使用[OH_ImagePackerNative_Release](image_packer_native.h.md#ZH-CN_TOPIC_0000002522241980__oh_imagepackernative_release)函数。

起始版本： 12

相关模块： [Image_NativeModule](Image_NativeModule.md)

所在头文件： [image_packer_native.h](image_packer_native.h.md)