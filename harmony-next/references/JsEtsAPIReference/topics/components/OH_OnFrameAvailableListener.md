# OH_OnFrameAvailableListener

```ets
typedef struct OH_OnFrameAvailableListener {...} OH_OnFrameAvailableListener
```

#### 概述

一个OH_NativeImage的监听者，通过[OH_NativeImage_SetOnFrameAvailableListener](../../capi/headers/native_image.h.md#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_setonframeavailablelistener)接口注册该监听结构体，当有buffer可获取时，将触发回调给用户。

**起始版本：** 11

**相关模块：**[OH_NativeImage](../graphics/OH_NativeImage.md)

**所在头文件：**[native_image.h](../../capi/headers/native_image.h.md)

#### 汇总

#### 成员变量

名称描述void* context用户自定义的上下文信息，会在回调触发时返回给用户。[OH_OnFrameAvailable](../../capi/headers/native_image.h.md#ZH-CN_TOPIC_0000002497446038__oh_onframeavailable) onFrameAvailable有buffer可获取时触发的回调函数。

#### 成员函数

名称typedef关键字描述[typedef void (*OH_OnFrameAvailable)(void *context)](#ZH-CN_TOPIC_0000002497606038__oh_onframeavailable)OH_OnFrameAvailable()

有buffer可获取时触发的回调函数。

**起始版本：** 11

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

#### 成员函数说明

#### OH_OnFrameAvailable()

```ets
typedef void (*OH_OnFrameAvailable)(void *context)
```

**描述**

有buffer可获取时触发的回调函数。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 11

**参数：**

参数项描述void *context用户自定义的上下文信息，会在回调触发时返回给用户。