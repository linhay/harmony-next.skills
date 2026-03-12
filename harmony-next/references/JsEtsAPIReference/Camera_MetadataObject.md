# Camera_MetadataObject

```ets
typedef struct Camera_MetadataObject {...} Camera_MetadataObject
```

#### 概述

元数据对象基础。

**起始版本：** 11

**相关模块：**[OH_Camera](OH_Camera.md)

**所在头文件：**[camera.h](camera.h.md)

#### 汇总

#### 成员变量

名称描述[Camera_MetadataObjectType](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_metadataobjecttype) type元数据对象类型。int64_t timestamp元数据对象时间戳，单位为纳秒（ns）。[Camera_Rect](Camera_Rect.md)* boundingBox检测到的元数据对象的轴对齐边界框。