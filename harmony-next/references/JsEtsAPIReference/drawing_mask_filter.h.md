# drawing_mask_filter.h

#### 概述

声明与绘图模块中的对象相关的函数。

**引用文件：** <native_drawing/drawing_mask_filter.h>

**库：** libnative_drawing.so

**起始版本：** 11

**相关模块：**[Drawing](Drawing.md)

#### 汇总

#### 枚举

名称typedef关键字描述[OH_Drawing_BlurType](#ZH-CN_TOPIC_0000002497606004__oh_drawing_blurtype)OH_Drawing_BlurType蒙版滤波器模糊操作类型的枚举。

#### 函数

名称描述[OH_Drawing_MaskFilter* OH_Drawing_MaskFilterCreateBlur(OH_Drawing_BlurType blurType, float sigma, bool respectCTM)](#ZH-CN_TOPIC_0000002497606004__oh_drawing_maskfiltercreateblur)创建具有模糊效果的蒙版滤波器。[void OH_Drawing_MaskFilterDestroy(OH_Drawing_MaskFilter* maskFilter)](#ZH-CN_TOPIC_0000002497606004__oh_drawing_maskfilterdestroy)销毁蒙版滤波器对象，并收回该对象占用的内存。

#### 枚举类型说明

#### OH_Drawing_BlurType

```ets
enum OH_Drawing_BlurType
```

**描述**

蒙版滤波器模糊操作类型的枚举。

**起始版本：** 11

枚举项描述NORMAL内外模糊。SOLID内部实体，外部模糊。OUTER内部空白，外部模糊。INNER内部模糊，外部空白。

#### 函数说明

#### OH_Drawing_MaskFilterCreateBlur()

```ets
OH_Drawing_MaskFilter* OH_Drawing_MaskFilterCreateBlur(OH_Drawing_BlurType blurType, float sigma, bool respectCTM)
```

**描述**

创建具有模糊效果的蒙版滤波器。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

参数项描述[OH_Drawing_BlurType](#ZH-CN_TOPIC_0000002497606004__oh_drawing_blurtype) blurType表示模糊类型。float sigma表示要应用的高斯模糊的标准偏差。必须大于0。bool respectCTM表示模糊标准差值被CTM（当前变换矩阵）修改，默认为真。true表示模糊标准差值受CTM影响，false表示模糊标准差值固定，不受CTM影响。

**返回：**

类型说明[OH_Drawing_MaskFilter](OH_Drawing_MaskFilter.md)*返回创建的蒙版滤波器对象的指针。

#### OH_Drawing_MaskFilterDestroy()

```ets
void OH_Drawing_MaskFilterDestroy(OH_Drawing_MaskFilter* maskFilter)
```

**描述**

销毁蒙版滤波器对象，并收回该对象占用的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

参数项描述[OH_Drawing_MaskFilter](OH_Drawing_MaskFilter.md)* maskFilter表示指向蒙版滤波器对象的指针。