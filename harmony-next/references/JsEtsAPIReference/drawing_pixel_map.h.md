# drawing_pixel_map.h

#### 概述

声明与绘图模块中的像素图对象相关的函数。

**引用文件：** <native_drawing/drawing_pixel_map.h>

**库：** libnative_drawing.so

**起始版本：** 12

**相关模块：**[Drawing](Drawing.md)

#### 汇总

#### 结构体

名称typedef关键字描述[NativePixelMap_](NativePixelMap_.md)NativePixelMap_声明由图像框架定义的像素图对象。[OH_PixelmapNative](OH_PixelmapNative.md)OH_PixelmapNative声明由图像框架定义的像素图对象。

#### 函数

名称描述[OH_Drawing_PixelMap* OH_Drawing_PixelMapGetFromNativePixelMap(NativePixelMap_* nativePixelMap)](#ZH-CN_TOPIC_0000002529285997__oh_drawing_pixelmapgetfromnativepixelmap)从图像框架定义的像素图对象中获取本模块定义的像素图对象。[OH_Drawing_PixelMap* OH_Drawing_PixelMapGetFromOhPixelMapNative(OH_PixelmapNative* pixelmapNative)](#ZH-CN_TOPIC_0000002529285997__oh_drawing_pixelmapgetfromohpixelmapnative)从图像框架定义的像素图对象中获取本模块定义的像素图对象。[void OH_Drawing_PixelMapDissolve(OH_Drawing_PixelMap* pixelMap)](#ZH-CN_TOPIC_0000002529285997__oh_drawing_pixelmapdissolve)解除本模块定义的像素图对象和图像框架定义的像素图对象之间的关系，该关系通过调用[OH_Drawing_PixelMapGetFromNativePixelMap](zh-cn_topic_0000002529285997.html#ZH-CN_TOPIC_0000002529285997__oh_drawing_pixelmapgetfromnativepixelmap)或[OH_Drawing_PixelMapGetFromOhPixelMapNative](drawing_pixel_map.h.md#ZH-CN_TOPIC_0000002529285997__oh_drawing_pixelmapgetfromohpixelmapnative)建立。

#### 函数说明

#### OH_Drawing_PixelMapGetFromNativePixelMap()

```ets
OH_Drawing_PixelMap* OH_Drawing_PixelMapGetFromNativePixelMap(NativePixelMap_* nativePixelMap)
```

**描述**

从图像框架定义的像素图对象中获取本模块定义的像素图对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[NativePixelMap_](NativePixelMap_.md)* nativePixelMap指向图像框架定义的像素图对象[NativePixelMap_](NativePixelMap_.md)的指针。

**返回：**

类型说明[OH_Drawing_PixelMap](OH_Drawing_PixelMap.md)*函数会返回一个指向本模块定义的像素图对象[OH_Drawing_PixelMap](OH_Drawing_PixelMap.md)的指针。如果对象返回NULL，表示创建失败；可能的原因是NativePixelMap_为NULL。

#### OH_Drawing_PixelMapGetFromOhPixelMapNative()

```ets
OH_Drawing_PixelMap* OH_Drawing_PixelMapGetFromOhPixelMapNative(OH_PixelmapNative* pixelmapNative)
```

**描述**

从图像框架定义的像素图对象中获取本模块定义的像素图对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_PixelmapNative](OH_PixelmapNative.md)* pixelmapNative指向图像框架定义的像素图对象[OH_PixelmapNative](OH_PixelmapNative.md)的指针。

**返回：**

类型说明[OH_Drawing_PixelMap](OH_Drawing_PixelMap.md)*函数会返回一个指向本模块定义的像素图对象[OH_Drawing_PixelMap](OH_Drawing_PixelMap.md)的指针。如果对象返回NULL，表示创建失败；可能的原因是OH_PixelmapNative为NULL。

#### OH_Drawing_PixelMapDissolve()

```ets
void OH_Drawing_PixelMapDissolve(OH_Drawing_PixelMap* pixelMap)
```

**描述**

解除本模块定义的像素图对象和图像框架定义的像素图对象之间的关系，该关系通过调用[OH_Drawing_PixelMapGetFromNativePixelMap](drawing_pixel_map.h.md#ZH-CN_TOPIC_0000002529285997__oh_drawing_pixelmapgetfromnativepixelmap)或[OH_Drawing_PixelMapGetFromOhPixelMapNative](drawing_pixel_map.h.md#ZH-CN_TOPIC_0000002529285997__oh_drawing_pixelmapgetfromohpixelmapnative)建立。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_PixelMap](OH_Drawing_PixelMap.md)* pixelMap指向像素图对象[OH_Drawing_PixelMap](OH_Drawing_PixelMap.md)的指针。