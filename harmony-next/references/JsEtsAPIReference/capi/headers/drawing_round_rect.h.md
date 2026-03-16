# drawing_round_rect.h

#### 概述

文件中定义了与圆角矩形相关的功能函数。

**引用文件：** <native_drawing/drawing_round_rect.h>

**库：** libnative_drawing.so

**起始版本：** 11

**相关模块：**[Drawing](../../topics/graphics/Drawing.md)

#### 汇总

#### 枚举

名称typedef关键字描述[OH_Drawing_CornerPos](#ZH-CN_TOPIC_0000002497606010__oh_drawing_cornerpos)OH_Drawing_CornerPos用于描述圆角位置的枚举。

#### 函数

名称描述[OH_Drawing_RoundRect* OH_Drawing_RoundRectCreate(const OH_Drawing_Rect* rect, float xRad, float yRad)](#ZH-CN_TOPIC_0000002497606010__oh_drawing_roundrectcreate)

用于创建一个圆角矩形对象。本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

rect为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[OH_Drawing_RoundRect* OH_Drawing_RoundRectCopy(const OH_Drawing_RoundRect* roundRect)](#ZH-CN_TOPIC_0000002497606010__oh_drawing_roundrectcopy)用于创建圆角矩形的拷贝。[void OH_Drawing_RoundRectSetCorner(OH_Drawing_RoundRect* roundRect,OH_Drawing_CornerPos pos, OH_Drawing_Corner_Radii radii)](#ZH-CN_TOPIC_0000002497606010__oh_drawing_roundrectsetcorner)

用于设置圆角矩形中指定圆角位置的圆角半径。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

roundRect为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[OH_Drawing_Corner_Radii OH_Drawing_RoundRectGetCorner(OH_Drawing_RoundRect* roundRect, OH_Drawing_CornerPos pos)](#ZH-CN_TOPIC_0000002497606010__oh_drawing_roundrectgetcorner)

用于获取圆角矩形中指定圆角位置的圆角半径。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

roundRect为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[void OH_Drawing_RoundRectDestroy(OH_Drawing_RoundRect* roundRect)](#ZH-CN_TOPIC_0000002497606010__oh_drawing_roundrectdestroy)用于销毁圆角矩形对象并回收该对象占有的内存。[OH_Drawing_ErrorCode OH_Drawing_RoundRectOffset(OH_Drawing_RoundRect* roundRect, float dx, float dy)](#ZH-CN_TOPIC_0000002497606010__oh_drawing_roundrectoffset)用于将圆角矩形沿x轴方向和y轴方向平移指定距离。

#### 枚举类型说明

#### OH_Drawing_CornerPos

```ets
enum OH_Drawing_CornerPos
```

**描述**

用于描述圆角位置的枚举。

**起始版本：** 12

枚举项描述CORNER_POS_TOP_LEFT左上角圆角位置。CORNER_POS_TOP_RIGHT右上角圆角位置。CORNER_POS_BOTTOM_RIGHT右下角圆角位置。CORNER_POS_BOTTOM_LEFT左下角圆角位置。

#### 函数说明

#### OH_Drawing_RoundRectCreate()

```ets
OH_Drawing_RoundRect* OH_Drawing_RoundRectCreate(const OH_Drawing_Rect* rect, float xRad, float yRad)
```

**描述**

用于创建一个圆角矩形对象。本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

rect为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

参数项描述const [OH_Drawing_Rect](../../topics/graphics/OH_Drawing_Rect.md)* rect指向矩形对象的指针。float xRadX轴上的圆角半径，小于或等于0时无效。float yRadY轴上的圆角半径，小于或等于0时无效。

**返回：**

类型说明[OH_Drawing_RoundRect](../../topics/graphics/OH_Drawing_RoundRect.md)*函数会返回一个指针，指针指向创建的圆角矩形对象。

#### OH_Drawing_RoundRectCopy()

```ets
OH_Drawing_RoundRect* OH_Drawing_RoundRectCopy(const OH_Drawing_RoundRect* roundRect)
```

**描述**

用于创建圆角矩形的拷贝。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

参数项描述const [OH_Drawing_RoundRect](../../topics/graphics/OH_Drawing_RoundRect.md)* roundRect指向用于拷贝的圆角矩形对象[OH_Drawing_RoundRect](../../topics/graphics/OH_Drawing_RoundRect.md)的指针。

**返回：**

类型说明[OH_Drawing_RoundRect](../../topics/graphics/OH_Drawing_RoundRect.md)*函数会返回一个指针，指针指向创建的新圆角矩形对象。

#### OH_Drawing_RoundRectSetCorner()

```ets
void OH_Drawing_RoundRectSetCorner(OH_Drawing_RoundRect* roundRect,OH_Drawing_CornerPos pos, OH_Drawing_Corner_Radii radii)
```

**描述**

用于设置圆角矩形中指定圆角位置的圆角半径。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

roundRect为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_RoundRect](../../topics/graphics/OH_Drawing_RoundRect.md)* roundRect指向圆角矩形对象的指针。[OH_Drawing_CornerPos](#ZH-CN_TOPIC_0000002497606010__oh_drawing_cornerpos) pos圆角位置的枚举，支持类型可见[OH_Drawing_CornerPos](drawing_round_rect.h.md#ZH-CN_TOPIC_0000002497606010__oh_drawing_cornerpos)。OH_Drawing_Corner_Radii radii圆角半径结构体OH_Drawing_Corner_Radii，其中包含x轴方向和y轴方向上的半径，半径小于等于0时无效。

#### OH_Drawing_RoundRectGetCorner()

```ets
OH_Drawing_Corner_Radii OH_Drawing_RoundRectGetCorner(OH_Drawing_RoundRect* roundRect, OH_Drawing_CornerPos pos)
```

**描述**

用于获取圆角矩形中指定圆角位置的圆角半径。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

roundRect为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_RoundRect](../../topics/graphics/OH_Drawing_RoundRect.md)* roundRect指向圆角矩形对象的指针。[OH_Drawing_CornerPos](#ZH-CN_TOPIC_0000002497606010__oh_drawing_cornerpos) pos圆角位置的枚举，支持类型可见[OH_Drawing_CornerPos](drawing_round_rect.h.md#ZH-CN_TOPIC_0000002497606010__oh_drawing_cornerpos)。

**返回：**

类型说明OH_Drawing_Corner_Radii返回指定圆角位置的圆角半径结构体OH_Drawing_Corner_Radii，其中包含x轴方向和y轴方向上的半径。

#### OH_Drawing_RoundRectDestroy()

```ets
void OH_Drawing_RoundRectDestroy(OH_Drawing_RoundRect* roundRect)
```

**描述**

用于销毁圆角矩形对象并回收该对象占有的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

参数项描述[OH_Drawing_RoundRect](../../topics/graphics/OH_Drawing_RoundRect.md)* roundRect指向圆角矩形对象的指针。

#### OH_Drawing_RoundRectOffset()

```ets
OH_Drawing_ErrorCode OH_Drawing_RoundRectOffset(OH_Drawing_RoundRect* roundRect, float dx, float dy)
```

**描述**

用于将圆角矩形沿x轴方向和y轴方向平移指定距离。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_RoundRect](../../topics/graphics/OH_Drawing_RoundRect.md)* roundRect指向圆角矩形对象[OH_Drawing_Point2D](../../topics/graphics/OH_Drawing_Point2D.md)的指针。float dxx轴方向偏移量。float dyy轴方向偏移量。

**返回：**

类型说明[OH_Drawing_ErrorCode](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcode)

函数返回执行错误码。

 返回OH_DRAWING_SUCCESS，表示执行成功。

 返回OH_DRAWING_ERROR_INVALID_PARAMETER，表示参数roundRect为空。