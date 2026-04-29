# drawing_pixel_map.h

**概述**

声明与绘图模块中的像素图对象相关的函数。

引用文件： <native_drawing/drawing_pixel_map.h>

库： libnative_drawing.so

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

相关模块： [Drawing](Drawing.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| NativePixelMap_ | NativePixelMap_ | 声明由图像框架定义的像素图对象。 |
| OH_PixelmapNative | OH_PixelmapNative | 声明由图像框架定义的像素图对象。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| OH_Drawing_PixelMap* OH_Drawing_PixelMapGetFromNativePixelMap(NativePixelMap_* nativePixelMap) | 从图像框架定义的像素图对象中获取本模块定义的像素图对象。 |
| OH_Drawing_PixelMap* OH_Drawing_PixelMapGetFromOhPixelMapNative(OH_PixelmapNative* pixelmapNative) | 从图像框架定义的像素图对象中获取本模块定义的像素图对象。 |
| void OH_Drawing_PixelMapDissolve(OH_Drawing_PixelMap* pixelMap) | 解除本模块定义的像素图对象和图像框架定义的像素图对象之间的关系，该关系通过调用OH_Drawing_PixelMapGetFromNativePixelMap或OH_Drawing_PixelMapGetFromOhPixelMapNative建立。若在建立关系后未调用本接口解除关系，将导致像素图对象的内存无法正确释放，进而引发内存泄漏问题。 |

**函数说明**

**OH_Drawing_PixelMapGetFromNativePixelMap()**

```ets
OH_Drawing_PixelMap* OH_Drawing_PixelMapGetFromNativePixelMap(NativePixelMap_* nativePixelMap)
```

描述

从图像框架定义的像素图对象中获取本模块定义的像素图对象。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| NativePixelMap_* nativePixelMap | 指向图像框架定义的像素图对象NativePixelMap_的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_PixelMap* | 函数会返回一个指向本模块定义的像素图对象OH_Drawing_PixelMap的指针。如果对象返回NULL，表示创建失败；可能的原因是NativePixelMap_为NULL。 |

**OH_Drawing_PixelMapGetFromOhPixelMapNative()**

```ets
OH_Drawing_PixelMap* OH_Drawing_PixelMapGetFromOhPixelMapNative(OH_PixelmapNative* pixelmapNative)
```

描述

从图像框架定义的像素图对象中获取本模块定义的像素图对象。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PixelmapNative* pixelmapNative | 指向图像框架定义的像素图对象OH_PixelmapNative的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_PixelMap* | 函数会返回一个指向本模块定义的像素图对象OH_Drawing_PixelMap的指针。如果对象返回NULL，表示创建失败；可能的原因是OH_PixelmapNative为NULL。 |

**OH_Drawing_PixelMapDissolve()**

```ets
void OH_Drawing_PixelMapDissolve(OH_Drawing_PixelMap* pixelMap)
```

描述

解除本模块定义的像素图对象和图像框架定义的像素图对象之间的关系，该关系通过调用[OH_Drawing_PixelMapGetFromNativePixelMap](drawing_pixel_map.h.md#ZH-CN_TOPIC_0000002553362081__oh_drawing_pixelmapgetfromnativepixelmap)或[OH_Drawing_PixelMapGetFromOhPixelMapNative](drawing_pixel_map.h.md#ZH-CN_TOPIC_0000002553362081__oh_drawing_pixelmapgetfromohpixelmapnative)建立。若在建立关系后未调用本接口解除关系，将导致像素图对象的内存无法正确释放，进而引发内存泄漏问题。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_PixelMap* pixelMap | 指向像素图对象OH_Drawing_PixelMap的指针。 |