# drawing_matrix.h

#### 概述

文件中定义了与矩阵相关的功能函数。

**相关示例：**[Drawing API示例(C/C++)](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/HarmonyOS-feature-20251117/ArkGraphics2D/Drawing/NDKAPIDrawing)

**引用文件：** <native_drawing/drawing_matrix.h>

**库：** libnative_drawing.so

**起始版本：** 11

**相关模块：**[Drawing](Drawing.md)

#### 汇总

#### 枚举

名称typedef关键字描述[OH_Drawing_ScaleToFit](#ZH-CN_TOPIC_0000002497446024__oh_drawing_scaletofit)OH_Drawing_ScaleToFit矩阵缩放方式枚举。

#### 函数

名称描述[OH_Drawing_Matrix* OH_Drawing_MatrixCreate(void)](#ZH-CN_TOPIC_0000002497446024__oh_drawing_matrixcreate)用于创建一个矩阵对象。[OH_Drawing_Matrix* OH_Drawing_MatrixCopy(const OH_Drawing_Matrix* matrix)](#ZH-CN_TOPIC_0000002497446024__oh_drawing_matrixcopy)用于创建一个矩阵对象的拷贝。[OH_Drawing_Matrix* OH_Drawing_MatrixCreateRotation(float deg, float x, float y)](#ZH-CN_TOPIC_0000002497446024__oh_drawing_matrixcreaterotation)

创建一个带旋转属性的矩阵对象。

该矩阵对象为：单位矩阵在(x, y)旋转点以度为单位进行旋转后得到的矩阵。

[OH_Drawing_Matrix* OH_Drawing_MatrixCreateScale(float sx, float sy, float px, float py)](#ZH-CN_TOPIC_0000002497446024__oh_drawing_matrixcreatescale)

创建一个带缩放属性的矩阵对象。

该矩阵对象为：单位矩阵在(px, py)旋转点以sx和sy为缩放因子进行缩放后得到的矩阵。

[OH_Drawing_Matrix* OH_Drawing_MatrixCreateTranslation(float dx, float dy)](#ZH-CN_TOPIC_0000002497446024__oh_drawing_matrixcreatetranslation)

创建一个带平移属性的矩阵对象。

该矩阵对象为：单位矩阵平移(dx, dy)后得到的矩阵。

[void OH_Drawing_MatrixSetMatrix(OH_Drawing_Matrix* matrix, float scaleX, float skewX, float transX,float skewY, float scaleY, float transY, float persp0, float persp1, float persp2)](#ZH-CN_TOPIC_0000002497446024__oh_drawing_matrixsetmatrix)

用于给矩阵对象设置参数。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

OH_Drawing_Matrix为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[bool OH_Drawing_MatrixSetRectToRect(OH_Drawing_Matrix* matrix, const OH_Drawing_Rect* src,const OH_Drawing_Rect* dst, OH_Drawing_ScaleToFit stf)](#ZH-CN_TOPIC_0000002497446024__oh_drawing_matrixsetrecttorect)

将矩阵以缩放方式适配目标矩阵。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

matrix、src、dst任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[void OH_Drawing_MatrixPreRotate(OH_Drawing_Matrix* matrix, float degree, float px, float py)](#ZH-CN_TOPIC_0000002497446024__oh_drawing_matrixprerotate)将矩阵设置为矩阵左乘围绕轴心点旋转一定角度的单位矩阵后得到的矩阵。[void OH_Drawing_MatrixPreScale(OH_Drawing_Matrix* matrix, float sx, float sy, float px, float py)](#ZH-CN_TOPIC_0000002497446024__oh_drawing_matrixprescale)将矩阵设置为矩阵左乘围绕轴心点按一定缩放因子缩放后的单位矩阵后得到的矩阵。[void OH_Drawing_MatrixPreTranslate(OH_Drawing_Matrix* matrix, float dx, float dy)](#ZH-CN_TOPIC_0000002497446024__oh_drawing_matrixpretranslate)将矩阵设置为矩阵左乘平移一定距离后的单位矩阵后得到的矩阵。[void OH_Drawing_MatrixPostRotate(OH_Drawing_Matrix* matrix, float degree, float px, float py)](#ZH-CN_TOPIC_0000002497446024__oh_drawing_matrixpostrotate)将矩阵设置为矩阵右乘围绕轴心点旋转一定角度的单位矩阵后得到的矩阵。[void OH_Drawing_MatrixPostScale(OH_Drawing_Matrix* matrix, float sx, float sy, float px, float py)](#ZH-CN_TOPIC_0000002497446024__oh_drawing_matrixpostscale)将矩阵设置为矩阵右乘围绕轴心点按一定缩放因子缩放后的单位矩阵后得到的矩阵。[void OH_Drawing_MatrixPostTranslate(OH_Drawing_Matrix* matrix, float dx, float dy)](#ZH-CN_TOPIC_0000002497446024__oh_drawing_matrixposttranslate)将矩阵设置为矩阵右乘平移一定距离后的单位矩阵后得到的矩阵。[void OH_Drawing_MatrixReset(OH_Drawing_Matrix* matrix)](#ZH-CN_TOPIC_0000002497446024__oh_drawing_matrixreset)重置当前矩阵为单位矩阵。[void OH_Drawing_MatrixConcat(OH_Drawing_Matrix* total, const OH_Drawing_Matrix* a,const OH_Drawing_Matrix* b)](#ZH-CN_TOPIC_0000002497446024__oh_drawing_matrixconcat)将矩阵total设置为矩阵a乘以矩阵b。[OH_Drawing_ErrorCode OH_Drawing_MatrixGetAll(OH_Drawing_Matrix* matrix, float value[9])](#ZH-CN_TOPIC_0000002497446024__oh_drawing_matrixgetall)获取矩阵所有元素值。[float OH_Drawing_MatrixGetValue(OH_Drawing_Matrix* matrix, int index)](#ZH-CN_TOPIC_0000002497446024__oh_drawing_matrixgetvalue)

获取矩阵给定索引位的值。索引范围0-8。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

matrix为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER；

index小于0或者大于8时返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。

[void OH_Drawing_MatrixRotate(OH_Drawing_Matrix* matrix, float degree, float px, float py)](#ZH-CN_TOPIC_0000002497446024__oh_drawing_matrixrotate)

设置矩阵为单位矩阵，并围绕位于(px, py)的旋转轴点进行旋转。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

matrix为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[void OH_Drawing_MatrixTranslate(OH_Drawing_Matrix* matrix, float dx, float dy)](#ZH-CN_TOPIC_0000002497446024__oh_drawing_matrixtranslate)

设置矩阵为单位矩阵，并平移(dx, dy)。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

matrix为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[void OH_Drawing_MatrixScale(OH_Drawing_Matrix* matrix, float sx, float sy, float px, float py)](#ZH-CN_TOPIC_0000002497446024__oh_drawing_matrixscale)

设置矩阵为单位矩阵，并围绕位于(px, py)的旋转轴点，以sx和sy进行缩放。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

matrix为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[bool OH_Drawing_MatrixInvert(OH_Drawing_Matrix* matrix, OH_Drawing_Matrix* inverse)](#ZH-CN_TOPIC_0000002497446024__oh_drawing_matrixinvert)

将矩阵inverse设置为矩阵的倒数，并返回结果。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

matrix、inverse任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[bool OH_Drawing_MatrixSetPolyToPoly(OH_Drawing_Matrix* matrix, const OH_Drawing_Point2D* src,const OH_Drawing_Point2D* dst, uint32_t count)](#ZH-CN_TOPIC_0000002497446024__oh_drawing_matrixsetpolytopoly)

通过设置源点以及目标点，生成对应的变换矩阵。

源点以及目标点的个数要大于等于0，小于等于4。本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

matrix为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER；

count小于0或者大于4时返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。

[void OH_Drawing_MatrixMapPoints(const OH_Drawing_Matrix* matrix, const OH_Drawing_Point2D* src,OH_Drawing_Point2D* dst, int count)](#ZH-CN_TOPIC_0000002497446024__oh_drawing_matrixmappoints)

通过矩阵变换将源点数组映射到目标点数组。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

matrix、src、dst任意一个为NULL或者count小于等于0时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[bool OH_Drawing_MatrixMapRect(const OH_Drawing_Matrix* matrix, const OH_Drawing_Rect* src, OH_Drawing_Rect* dst)](#ZH-CN_TOPIC_0000002497446024__oh_drawing_matrixmaprect)

将目标矩形设置为一个新的矩形，该矩形是能够包围源矩形的四个顶点通过矩阵变换映射后形成的新顶点的最小矩形。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

matrix、src、dst任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[bool OH_Drawing_MatrixIsEqual(OH_Drawing_Matrix* matrix, OH_Drawing_Matrix* other)](#ZH-CN_TOPIC_0000002497446024__oh_drawing_matrixisequal)

判断两个矩阵是否相等。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

matrix、other任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[bool OH_Drawing_MatrixIsIdentity(OH_Drawing_Matrix* matrix)](#ZH-CN_TOPIC_0000002497446024__oh_drawing_matrixisidentity)判断矩阵是否是单位矩阵。[void OH_Drawing_MatrixDestroy(OH_Drawing_Matrix* matrix)](#ZH-CN_TOPIC_0000002497446024__oh_drawing_matrixdestroy)用于销毁矩阵对象并回收该对象占有的内存。[OH_Drawing_ErrorCode OH_Drawing_MatrixPreConcat(OH_Drawing_Matrix* a, OH_Drawing_Matrix* b)](#ZH-CN_TOPIC_0000002497446024__oh_drawing_matrixpreconcat)对矩阵a左乘矩阵b。

#### 枚举类型说明

#### OH_Drawing_ScaleToFit

```ets
enum OH_Drawing_ScaleToFit
```

**描述**

矩阵缩放方式枚举。

**起始版本：** 12

枚举项描述SCALE_TO_FIT_FILL按水平轴和垂直轴缩放以填充目标矩形。SCALE_TO_FIT_START缩放并对齐到左侧和顶部。SCALE_TO_FIT_CENTER缩放并居中对齐。SCALE_TO_FIT_END缩放并向右和向下对齐。

#### 函数说明

#### OH_Drawing_MatrixCreate()

```ets
OH_Drawing_Matrix* OH_Drawing_MatrixCreate(void)
```

**描述**

用于创建一个矩阵对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**返回：**

类型说明[OH_Drawing_Matrix](OH_Drawing_Matrix.md)*函数会返回一个指针，指针指向创建的矩阵对象。

#### OH_Drawing_MatrixCopy()

```ets
OH_Drawing_Matrix* OH_Drawing_MatrixCopy(const OH_Drawing_Matrix* matrix)
```

**描述**

用于创建一个矩阵对象的拷贝。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

参数项描述const [OH_Drawing_Matrix](OH_Drawing_Matrix.md)* matrix指向用于拷贝的矩阵对象[OH_Drawing_Matrix](OH_Drawing_Matrix.md)的指针。

**返回：**

类型说明[OH_Drawing_Matrix](OH_Drawing_Matrix.md)*函数会返回一个指针，指针指向创建的新矩阵对象。

#### OH_Drawing_MatrixCreateRotation()

```ets
OH_Drawing_Matrix* OH_Drawing_MatrixCreateRotation(float deg, float x, float y)
```

**描述**

创建一个带旋转属性的矩阵对象。

该矩阵对象为：单位矩阵在(x, y)旋转点以度为单位进行旋转后得到的矩阵。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述float deg旋转的角度，单位为度。正数表示按顺时针旋转，负数表示按逆时针旋转。float xx轴上坐标点。float yy轴上坐标点。

**返回：**

类型说明[OH_Drawing_Matrix](OH_Drawing_Matrix.md)*函数返回一个指针，指针指向创建的矩阵对象[OH_Drawing_Matrix](OH_Drawing_Matrix.md)。

#### OH_Drawing_MatrixCreateScale()

```ets
OH_Drawing_Matrix* OH_Drawing_MatrixCreateScale(float sx, float sy, float px, float py)
```

**描述**

创建一个带缩放属性的矩阵对象。

该矩阵对象为：单位矩阵在(px, py)旋转点以sx和sy为缩放因子进行缩放后得到的矩阵。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述float sx水平缩放因子，为负数时可看作是先关于y = px作镜像翻转后再进行缩放，该参数为浮点数。float sy垂直缩放因子，为负数时可看作是先关于x = py作镜像翻转后再进行缩放，该参数为浮点数。float pxx轴上坐标点。float pyy轴上坐标点。

**返回：**

类型说明[OH_Drawing_Matrix](OH_Drawing_Matrix.md)*函数返回一个指针，指针指向创建的矩阵对象[OH_Drawing_Matrix](OH_Drawing_Matrix.md)。

#### OH_Drawing_MatrixCreateTranslation()

```ets
OH_Drawing_Matrix* OH_Drawing_MatrixCreateTranslation(float dx, float dy)
```

**描述**

创建一个带平移属性的矩阵对象。

该矩阵对象为：单位矩阵平移(dx, dy)后得到的矩阵。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述float dx水平方向平移距离，正数表示往x轴正方向平移，负数表示往x轴负方向平移，该参数为浮点数。float dy垂直方向平移距离，正数表示往y轴正方向平移，负数表示往y轴负方向平移，该参数为浮点数。

**返回：**

类型说明[OH_Drawing_Matrix](OH_Drawing_Matrix.md)*函数返回一个指针，指针指向创建的矩阵对象[OH_Drawing_Matrix](OH_Drawing_Matrix.md)。

#### OH_Drawing_MatrixSetMatrix()

```ets
void OH_Drawing_MatrixSetMatrix(OH_Drawing_Matrix* matrix, float scaleX, float skewX, float transX,float skewY, float scaleY, float transY, float persp0, float persp1, float persp2)
```

**描述**

用于给矩阵对象设置参数。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

OH_Drawing_Matrix为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

参数项描述[OH_Drawing_Matrix](OH_Drawing_Matrix.md)* matrix指向矩阵对象的指针。float scaleX水平缩放系数。float skewX水平倾斜系数。float transX水平位移系数。float skewY垂直倾斜系数。float scaleY垂直缩放系数。float transY垂直位移系数。float persp0X轴透视系数。float persp1Y轴透视系数。float persp2透视缩放系数。

#### OH_Drawing_MatrixSetRectToRect()

```ets
bool OH_Drawing_MatrixSetRectToRect(OH_Drawing_Matrix* matrix, const OH_Drawing_Rect* src,const OH_Drawing_Rect* dst, OH_Drawing_ScaleToFit stf)
```

**描述**

将矩阵以缩放方式适配目标矩阵。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

matrix、src、dst任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_Matrix](OH_Drawing_Matrix.md)* matrix指向矩阵对象[OH_Drawing_Matrix](OH_Drawing_Matrix.md)的指针。const [OH_Drawing_Rect](OH_Drawing_Rect.md)* src指向映射源的[OH_Drawing_Rect](OH_Drawing_Rect.md)对象Rect的指针。const [OH_Drawing_Rect](OH_Drawing_Rect.md)* dst指向要映射到的[OH_Drawing_Rect](OH_Drawing_Rect.md)对象Rect的指针。[OH_Drawing_ScaleToFit](#ZH-CN_TOPIC_0000002497446024__oh_drawing_scaletofit) stf缩放方式，支持方式[OH_Drawing_ScaleToFit](zh-cn_topic_0000002497446024.html#ZH-CN_TOPIC_0000002497446024__oh_drawing_scaletofit)。

**返回：**

类型说明bool

如果设置失败，则返回false；如果设置成功，则返回true；如果矩阵为空，则返回true，并将矩阵设置为：

 如果源矩形src的宽高任意一个小于等于0，则返回false，并将矩阵设置为单位矩阵；

 如果目标矩形dst的宽高任意一个小于等于0，则返回true，并将矩阵设置为除透视缩放系数为1外其余值皆为0的矩阵;

#### OH_Drawing_MatrixPreRotate()

```ets
void OH_Drawing_MatrixPreRotate(OH_Drawing_Matrix* matrix, float degree, float px, float py)
```

**描述**

将矩阵设置为矩阵左乘围绕轴心点旋转一定角度的单位矩阵后得到的矩阵。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

matrix为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_Matrix](OH_Drawing_Matrix.md)* matrix指向矩阵对象[OH_Drawing_Matrix](OH_Drawing_Matrix.md)的指针。float degree旋转角度，单位为度。正数表示顺时针旋转，负数表示逆时针旋转。float px旋转中心点的横坐标。float py旋转中心点的纵坐标。

#### OH_Drawing_MatrixPreScale()

```ets
void OH_Drawing_MatrixPreScale(OH_Drawing_Matrix* matrix, float sx, float sy, float px, float py)
```

**描述**

将矩阵设置为矩阵左乘围绕轴心点按一定缩放因子缩放后的单位矩阵后得到的矩阵。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

matrix为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_Matrix](OH_Drawing_Matrix.md)* matrix指向矩阵对象[OH_Drawing_Matrix](OH_Drawing_Matrix.md)的指针。float sxx轴方向的缩放比例因子，为负数时可看作是先关于y = px作镜像翻转后再进行缩放，该参数为浮点数。float syy轴方向的缩放比例因子，为负数时可看作是先关于x = py作镜像翻转后再进行缩放，该参数为浮点数。float px缩放中心点的横坐标。float py缩放中心点的纵坐标。

#### OH_Drawing_MatrixPreTranslate()

```ets
void OH_Drawing_MatrixPreTranslate(OH_Drawing_Matrix* matrix, float dx, float dy)
```

**描述**

将矩阵设置为矩阵左乘平移一定距离后的单位矩阵后得到的矩阵。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

matrix为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_Matrix](OH_Drawing_Matrix.md)* matrix指向矩阵对象[OH_Drawing_Matrix](OH_Drawing_Matrix.md)的指针。float dx表示在x轴方向上的平移距离，正数表示往x轴正方向平移，负数表示往x轴负方向平移，该参数为浮点数。float dy表示在y轴方向上的平移距离，正数表示往y轴正方向平移，负数表示往y轴负方向平移，该参数为浮点数。

#### OH_Drawing_MatrixPostRotate()

```ets
void OH_Drawing_MatrixPostRotate(OH_Drawing_Matrix* matrix, float degree, float px, float py)
```

**描述**

将矩阵设置为矩阵右乘围绕轴心点旋转一定角度的单位矩阵后得到的矩阵。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

matrix为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_Matrix](OH_Drawing_Matrix.md)* matrix指向矩阵对象[OH_Drawing_Matrix](OH_Drawing_Matrix.md)的指针。float degree旋转角度，单位为度。正数表示顺时针旋转，负数表示逆时针旋转。float px旋转中心点的横坐标。float py旋转中心点的纵坐标。

#### OH_Drawing_MatrixPostScale()

```ets
void OH_Drawing_MatrixPostScale(OH_Drawing_Matrix* matrix, float sx, float sy, float px, float py)
```

**描述**

将矩阵设置为矩阵右乘围绕轴心点按一定缩放因子缩放后的单位矩阵后得到的矩阵。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

matrix为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_Matrix](OH_Drawing_Matrix.md)* matrix指向矩阵对象[OH_Drawing_Matrix](OH_Drawing_Matrix.md)的指针。float sxx轴方向的缩放比例因子，为负数时可看作是先关于y = px作镜像翻转后再进行缩放，该参数为浮点数。float syy轴方向的缩放比例因子，为负数时可看作是先关于x = py作镜像翻转后再进行缩放，该参数为浮点数。float px缩放中心点的横坐标。float py缩放中心点的纵坐标。

#### OH_Drawing_MatrixPostTranslate()

```ets
void OH_Drawing_MatrixPostTranslate(OH_Drawing_Matrix* matrix, float dx, float dy)
```

**描述**

将矩阵设置为矩阵右乘平移一定距离后的单位矩阵后得到的矩阵。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

matrix为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_Matrix](OH_Drawing_Matrix.md)* matrix指向矩阵对象[OH_Drawing_Matrix](OH_Drawing_Matrix.md)的指针。float dx表示在x轴方向上的平移距离，正数表示往x轴正方向平移，负数表示往x轴负方向平移，该参数为浮点数。float dy表示在y轴方向上的平移距离，正数表示往y轴正方向平移，负数表示往y轴负方向平移，该参数为浮点数。

#### OH_Drawing_MatrixReset()

```ets
void OH_Drawing_MatrixReset(OH_Drawing_Matrix* matrix)
```

**描述**

重置当前矩阵为单位矩阵。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

matrix为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_Matrix](OH_Drawing_Matrix.md)* matrix指向矩阵对象[OH_Drawing_Matrix](OH_Drawing_Matrix.md)的指针。

#### OH_Drawing_MatrixConcat()

```ets
void OH_Drawing_MatrixConcat(OH_Drawing_Matrix* total, const OH_Drawing_Matrix* a,const OH_Drawing_Matrix* b)
```

**描述**

将矩阵total设置为矩阵a乘以矩阵b。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

total、a、b任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_Matrix](OH_Drawing_Matrix.md)* total指向最终的矩阵对象[OH_Drawing_Matrix](OH_Drawing_Matrix.md)的指针。const [OH_Drawing_Matrix](OH_Drawing_Matrix.md)* a指向矩阵对象a[OH_Drawing_Matrix](OH_Drawing_Matrix.md)的指针。const [OH_Drawing_Matrix](OH_Drawing_Matrix.md)* b指向矩阵对象b[OH_Drawing_Matrix](OH_Drawing_Matrix.md)的指针。

#### OH_Drawing_MatrixGetAll()

```ets
OH_Drawing_ErrorCode OH_Drawing_MatrixGetAll(OH_Drawing_Matrix* matrix, float value[9])
```

**描述**

获取矩阵所有元素值。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_Matrix](OH_Drawing_Matrix.md)* matrix指向矩阵对象[OH_Drawing_Matrix](OH_Drawing_Matrix.md)的指针。value用于存储得到的矩阵元素值的数组。

**返回：**

类型说明[OH_Drawing_ErrorCode](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcode)

返回错误码。

 返回OH_DRAWING_SUCCESS，表示成功获取矩阵的所有元素值。

 返回OH_DRAWING_ERROR_INVALID_PARAMETER，表示获取矩阵元素值失败，原因是矩阵对象或者存储矩阵元素值数组为空。

#### OH_Drawing_MatrixGetValue()

```ets
float OH_Drawing_MatrixGetValue(OH_Drawing_Matrix* matrix, int index)
```

**描述**

获取矩阵给定索引位的值。索引范围0-8。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

matrix为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER；

index小于0或者大于8时返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_Matrix](OH_Drawing_Matrix.md)* matrix指向矩阵对象[OH_Drawing_Matrix](OH_Drawing_Matrix.md)的指针。int index索引位置，范围0-8。

**返回：**

类型说明float函数返回矩阵给定索引位对应的值。

#### OH_Drawing_MatrixRotate()

```ets
void OH_Drawing_MatrixRotate(OH_Drawing_Matrix* matrix, float degree, float px, float py)
```

**描述**

设置矩阵为单位矩阵，并围绕位于(px, py)的旋转轴点进行旋转。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

matrix为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_Matrix](OH_Drawing_Matrix.md)* matrix指向矩阵对象[OH_Drawing_Matrix](OH_Drawing_Matrix.md)的指针。float degree角度，单位为度。正数表示顺时针旋转，负数表示逆时针旋转。float pxx轴上坐标点。float pyy轴上坐标点。

#### OH_Drawing_MatrixTranslate()

```ets
void OH_Drawing_MatrixTranslate(OH_Drawing_Matrix* matrix, float dx, float dy)
```

**描述**

设置矩阵为单位矩阵，并平移(dx, dy)。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

matrix为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_Matrix](OH_Drawing_Matrix.md)* matrix指向矩阵对象[OH_Drawing_Matrix](OH_Drawing_Matrix.md)的指针。float dx水平方向平移距离，正数表示往x轴正方向平移，负数表示往x轴负方向平移，该参数为浮点数。float dy垂直方向平移距离，正数表示往y轴正方向平移，负数表示往y轴负方向平移，该参数为浮点数。

#### OH_Drawing_MatrixScale()

```ets
void OH_Drawing_MatrixScale(OH_Drawing_Matrix* matrix, float sx, float sy, float px, float py)
```

**描述**

设置矩阵为单位矩阵，并围绕位于(px, py)的旋转轴点，以sx和sy进行缩放。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

matrix为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_Matrix](OH_Drawing_Matrix.md)* matrix指向矩阵对象[OH_Drawing_Matrix](OH_Drawing_Matrix.md)的指针。float sx水平缩放因子，为负数时可看作是先关于y = px作镜像翻转后再进行缩放，该参数为浮点数。float sy垂直缩放因子，为负数时可看作是先关于x = py作镜像翻转后再进行缩放，该参数为浮点数。float pxx轴上坐标点。float pyy轴上坐标点。

#### OH_Drawing_MatrixInvert()

```ets
bool OH_Drawing_MatrixInvert(OH_Drawing_Matrix* matrix, OH_Drawing_Matrix* inverse)
```

**描述**

将矩阵inverse设置为矩阵的倒数，并返回结果。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

matrix、inverse任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_Matrix](OH_Drawing_Matrix.md)* matrix指向矩阵对象[OH_Drawing_Matrix](OH_Drawing_Matrix.md)的指针。[OH_Drawing_Matrix](OH_Drawing_Matrix.md)* inverse指向逆矩阵对象[OH_Drawing_Matrix](OH_Drawing_Matrix.md)的指针，开发者可调用[OH_Drawing_MatrixCreate](drawing_matrix.h.md#ZH-CN_TOPIC_0000002497446024__oh_drawing_matrixcreate)接口创建。

**返回：**

类型说明bool函数返回true表示矩阵可逆，inverse被填充为逆矩阵；函数返回false表示矩阵不可逆，inverse不被改变。

#### OH_Drawing_MatrixSetPolyToPoly()

```ets
bool OH_Drawing_MatrixSetPolyToPoly(OH_Drawing_Matrix* matrix, const OH_Drawing_Point2D* src,const OH_Drawing_Point2D* dst, uint32_t count)
```

**描述**

通过设置源点以及目标点，生成对应的变换矩阵。

源点以及目标点的个数要大于等于0，小于等于4。本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

matrix为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER；

count小于0或者大于4时返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_Matrix](OH_Drawing_Matrix.md)* matrix指向矩阵对象[OH_Drawing_Matrix](OH_Drawing_Matrix.md)的指针。const [OH_Drawing_Point2D](OH_Drawing_Point2D.md)* src源点数组，为NULL时count应当为0。const [OH_Drawing_Point2D](OH_Drawing_Point2D.md)* dst目标点数组，个数要与源点相等，为NULL时count应当为0。uint32_t count源点数组以及目标点数组的个数，为0时将矩阵对象设为单位矩阵。

**返回：**

类型说明bool函数返回是否可以生成对应矩阵以用来完成变换。true表示矩阵生成成功，false表示无法生成对应矩阵。

#### OH_Drawing_MatrixMapPoints()

```ets
void OH_Drawing_MatrixMapPoints(const OH_Drawing_Matrix* matrix, const OH_Drawing_Point2D* src,OH_Drawing_Point2D* dst, int count)
```

**描述**

通过矩阵变换将源点数组映射到目标点数组。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

matrix、src、dst任意一个为NULL或者count小于等于0时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述const [OH_Drawing_Matrix](OH_Drawing_Matrix.md)* matrix指向矩阵对象[OH_Drawing_Matrix](OH_Drawing_Matrix.md)的指针。const [OH_Drawing_Point2D](OH_Drawing_Point2D.md)* src源点数组。[OH_Drawing_Point2D](OH_Drawing_Point2D.md)* dst目标点数组，个数要与源点相等。int count源点数组以及目标点数组的个数。

#### OH_Drawing_MatrixMapRect()

```ets
bool OH_Drawing_MatrixMapRect(const OH_Drawing_Matrix* matrix, const OH_Drawing_Rect* src, OH_Drawing_Rect* dst)
```

**描述**

将目标矩形设置为一个新的矩形，该矩形是能够包围源矩形的四个顶点通过矩阵变换映射后形成的新顶点的最小矩形。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

matrix、src、dst任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述const [OH_Drawing_Matrix](OH_Drawing_Matrix.md)* matrix指向矩阵对象[OH_Drawing_Matrix](OH_Drawing_Matrix.md)的指针。const [OH_Drawing_Rect](OH_Drawing_Rect.md)* src源矩形。[OH_Drawing_Rect](OH_Drawing_Rect.md)* dst目标矩形。

**返回：**

类型说明bool函数返回源矩形与映射后的目标矩形是否相等。true表示相等，false表示不相等。

#### OH_Drawing_MatrixIsEqual()

```ets
bool OH_Drawing_MatrixIsEqual(OH_Drawing_Matrix* matrix, OH_Drawing_Matrix* other)
```

**描述**

判断两个矩阵是否相等。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

matrix、other任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_Matrix](OH_Drawing_Matrix.md)* matrix指向用于判断的其中一个矩阵对象[OH_Drawing_Matrix](OH_Drawing_Matrix.md)的指针。[OH_Drawing_Matrix](OH_Drawing_Matrix.md)* other指向用于判断的另一个矩阵对象[OH_Drawing_Matrix](OH_Drawing_Matrix.md)的指针。

**返回：**

类型说明bool函数返回两个矩阵的比较结果，返回true表示两个矩阵相等，返回false表示两个矩阵不相等。

#### OH_Drawing_MatrixIsIdentity()

```ets
bool OH_Drawing_MatrixIsIdentity(OH_Drawing_Matrix* matrix)
```

**描述**

判断矩阵是否是单位矩阵。

单位矩阵为 : | 1 0 0 || 0 1 0 || 0 0 1 |本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

matrix为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_Matrix](OH_Drawing_Matrix.md)* matrix指向矩阵对象[OH_Drawing_Matrix](OH_Drawing_Matrix.md)的指针。

**返回：**

类型说明bool函数返回true表示矩阵是单位矩阵，函数返回false表示矩阵不是单位矩阵。

#### OH_Drawing_MatrixDestroy()

```ets
void OH_Drawing_MatrixDestroy(OH_Drawing_Matrix* matrix)
```

**描述**

用于销毁矩阵对象并回收该对象占有的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

参数项描述[OH_Drawing_Matrix](OH_Drawing_Matrix.md)* matrix指向矩阵对象的指针。

#### OH_Drawing_MatrixPreConcat()

```ets
OH_Drawing_ErrorCode OH_Drawing_MatrixPreConcat(OH_Drawing_Matrix* a, OH_Drawing_Matrix* b)
```

**描述**

对矩阵a左乘矩阵b。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 22

**参数：**

参数项描述[OH_Drawing_Matrix](OH_Drawing_Matrix.md)* a指向矩阵对象[OH_Drawing_Matrix](OH_Drawing_Matrix.md)的指针。[OH_Drawing_Matrix](OH_Drawing_Matrix.md)* b指向矩阵对象[OH_Drawing_Matrix](OH_Drawing_Matrix.md)的指针。

**返回：**

类型说明[OH_Drawing_ErrorCode](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcode)

返回错误码。

返回OH_DRAWING_SUCCESS，表示成功执行左乘方法。

返回OH_DRAWING_ERROR_INCORRECT_PARAMETER，表示入参异常，rect或other为空。