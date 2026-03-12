# drawing_color_space.h

#### 概述

文件中定义了与颜色空间相关的功能函数。

**引用文件：** <native_drawing/drawing_color_space.h>

**库：** libnative_drawing.so

**起始版本：** 12

**相关模块：**[Drawing](Drawing.md)

#### 汇总

#### 函数

名称描述[OH_Drawing_ColorSpace* OH_Drawing_ColorSpaceCreateSrgb(void)](#ZH-CN_TOPIC_0000002529445963__oh_drawing_colorspacecreatesrgb)创建一个标准颜色空间。[OH_Drawing_ColorSpace* OH_Drawing_ColorSpaceCreateSrgbLinear(void)](#ZH-CN_TOPIC_0000002529445963__oh_drawing_colorspacecreatesrgblinear)创建一个Gamma 1.0空间上的颜色空间。[void OH_Drawing_ColorSpaceDestroy(OH_Drawing_ColorSpace* colorSpace)](#ZH-CN_TOPIC_0000002529445963__oh_drawing_colorspacedestroy)销毁颜色空间对象，并回收该对象占用内存。

#### 函数说明

#### OH_Drawing_ColorSpaceCreateSrgb()

```ets
OH_Drawing_ColorSpace* OH_Drawing_ColorSpaceCreateSrgb(void)
```

**描述**

创建一个标准颜色空间。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**返回：**

类型说明[OH_Drawing_ColorSpace](OH_Drawing_ColorSpace.md)*函数返回一个指针，指针指向创建的颜色空间对象[OH_Drawing_ColorSpace](OH_Drawing_ColorSpace.md)。

#### OH_Drawing_ColorSpaceCreateSrgbLinear()

```ets
OH_Drawing_ColorSpace* OH_Drawing_ColorSpaceCreateSrgbLinear(void)
```

**描述**

创建一个Gamma 1.0空间上的颜色空间。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**返回：**

类型说明[OH_Drawing_ColorSpace](OH_Drawing_ColorSpace.md)*函数返回一个指针，指针指向创建的颜色空间对象[OH_Drawing_ColorSpace](OH_Drawing_ColorSpace.md)。

#### OH_Drawing_ColorSpaceDestroy()

```ets
void OH_Drawing_ColorSpaceDestroy(OH_Drawing_ColorSpace* colorSpace)
```

**描述**

销毁颜色空间对象，并回收该对象占用的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_ColorSpace](OH_Drawing_ColorSpace.md)* colorSpace指向颜色空间对象[OH_Drawing_ColorSpace](OH_Drawing_ColorSpace.md)的指针。