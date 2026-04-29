# drawing_path.h

**概述**

文件中定义了与自定义路径相关的功能函数。

相关示例： [Drawing API示例(C/C++)](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkGraphics2D/Drawing/NDKAPIDrawing)

引用文件： <native_drawing/drawing_path.h>

库： libnative_drawing.so

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 8

相关模块： [Drawing](Drawing.md)

**汇总**

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_Drawing_PathDirection | OH_Drawing_PathDirection | 添加闭合轮廓方向枚举。 |
| OH_Drawing_PathFillType | OH_Drawing_PathFillType | 定义路径的填充类型枚举。 |
| OH_Drawing_PathAddMode | OH_Drawing_PathAddMode | 用于指定路径添加模式的枚举类型。 |
| OH_Drawing_PathOpMode | OH_Drawing_PathOpMode | 路径操作类型枚举。 |
| OH_Drawing_PathMeasureMatrixFlags | OH_Drawing_PathMeasureMatrixFlags | 路径测量获取相应矩阵信息维度枚举。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| OH_Drawing_Path* OH_Drawing_PathCreate(void) | 用于创建一个路径对象。 |
| OH_Drawing_Path* OH_Drawing_PathCopy(OH_Drawing_Path* path) | 创建一个路径对象副本OH_Drawing_Path，用于拷贝一个已有路径对象。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 path为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| void OH_Drawing_PathDestroy(OH_Drawing_Path* path) | 用于销毁路径对象并回收该对象占有的内存。 |
| OH_Drawing_ErrorCode OH_Drawing_PathSetPath(OH_Drawing_Path* path, OH_Drawing_Path* other) | 将一个路径对象设置成当前的路径对象。 |
| OH_Drawing_ErrorCode OH_Drawing_PathIsEmpty(OH_Drawing_Path* path, bool* isEmpty) | 判断一个路径对象是否为空。 |
| OH_Drawing_ErrorCode OH_Drawing_PathIsRect(OH_Drawing_Path* path, OH_Drawing_Rect* rect, bool* isRect) | 判断路径对象是否构成一个矩形。 |
| void OH_Drawing_PathMoveTo(OH_Drawing_Path* path, float x, float y) | 用于设置自定义路径的起始点位置。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 path为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| void OH_Drawing_PathLineTo(OH_Drawing_Path* path, float x, float y) | 用于添加一条从路径的最后点位置（若路径没有内容则默认为 (0, 0)）到目标点位置的线段。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 path为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| void OH_Drawing_PathArcTo(OH_Drawing_Path* path,float x1, float y1, float x2, float y2, float startDeg, float sweepDeg) | 用于给路径添加一段弧线，绘制弧线的方式为角度弧，该方式首先会指定一个矩形边框， 矩形边框的内切椭圆将会被用来截取弧线，然后会指定一个起始角度和扫描度数， 从起始角度扫描截取的椭圆周长一部分即为绘制的弧线。若路径有内容则会默认添加一条从路径的最后点位置到弧线起始点位置的线段。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 path为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| void OH_Drawing_PathQuadTo(OH_Drawing_Path* path, float ctrlX, float ctrlY, float endX, float endY) | 用于添加一条从路径最后点位置（若路径没有内容则默认为 (0, 0)）到目标点位置的二阶贝塞尔曲线。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 path为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| void OH_Drawing_PathConicTo(OH_Drawing_Path* path, float ctrlX, float ctrlY, float endX, float endY, float weight) | 在当前路径上添加一条路径终点（若路径没有内容则默认为 (0, 0)）到目标点位置的圆锥曲线段，其控制点为 (ctrlX, ctrlY)，结束点为 (endX, endY)。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 path为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| void OH_Drawing_PathCubicTo(OH_Drawing_Path* path, float ctrlX1, float ctrlY1, float ctrlX2, float ctrlY2, float endX, float endY) | 用于添加一条从路径最后点位置（若路径没有内容则默认为 (0, 0)）到目标点位置的三阶贝塞尔圆滑曲线。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 path为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| void OH_Drawing_PathRMoveTo(OH_Drawing_Path* path, float x, float y) | 用于设置一个相对于当前路径终点（若路径没有内容则默认为 (0, 0)）的路径起始点位置。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 path为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| void OH_Drawing_PathRLineTo(OH_Drawing_Path* path, float x, float y) | 使用相对位置在当前路径上添加一条当前路径终点（若路径没有内容则默认为 (0, 0)）到目标点位置的线段。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 path为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| void OH_Drawing_PathRQuadTo(OH_Drawing_Path* path, float ctrlX, float ctrlY, float endX, float endY) | 使用相对位置在当前路径上添加一条当前路径终点（若路径没有内容则默认为 (0, 0)）到目标点位置的二阶贝塞尔曲线。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 path为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| void OH_Drawing_PathRConicTo(OH_Drawing_Path* path, float ctrlX, float ctrlY, float endX, float endY, float weight) | 使用相对位置在当前路径上添加一条路径终点（若路径没有内容则默认为 (0, 0)）到目标点位置的圆锥曲线段。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 path为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| void OH_Drawing_PathRCubicTo(OH_Drawing_Path* path, float ctrlX1, float ctrlY1, float ctrlX2, float ctrlY2,float endX, float endY) | 使用相对位置在当前路径上添加一条当前路径终点（若路径没有内容则默认为 (0, 0)）到目标点位置的三阶贝塞尔圆滑曲线。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 path为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| void OH_Drawing_PathAddRect(OH_Drawing_Path* path, float left, float top, float right, float bottom,OH_Drawing_PathDirection pathDirection) | 按指定方向，将矩形添加到路径中，添加的路径的起始点为矩形左上角。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 path为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER； pathDirection不在枚举范围内返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。 |
| void OH_Drawing_PathAddRectWithInitialCorner(OH_Drawing_Path* path, const OH_Drawing_Rect* rect,OH_Drawing_PathDirection pathDirection, uint32_t start) | 按指定方向，向路径添加矩形轮廓。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 path、rect任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER； pathDirection不在枚举范围内返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。 |
| void OH_Drawing_PathAddRoundRect(OH_Drawing_Path* path,const OH_Drawing_RoundRect* roundRect, OH_Drawing_PathDirection pathDirection) | 按指定方向，向路径添加圆角矩形轮廓。路径添加方向为顺时针时，起始点位于圆角矩形左下方圆角与左边界的交点；路径添加方向为逆时针时，起始点位于圆角矩形左上方圆角与左边界的交点。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 path、roundRect任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER； pathDirection不在枚举范围内返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。 |
| void OH_Drawing_PathAddOvalWithInitialPoint(OH_Drawing_Path* path, const OH_Drawing_Rect* rect,uint32_t start, OH_Drawing_PathDirection pathDirection) | 将椭圆添加到路径中，其中矩形对象作为椭圆的外切矩形区域，绘制方向用来指定绘制时是顺时针或者逆时针方向。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 path、rect任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER； pathDirection不在枚举范围内时返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。 |
| void OH_Drawing_PathAddOval(OH_Drawing_Path* path,const OH_Drawing_Rect* rect, OH_Drawing_PathDirection pathDirection) | 按指定方向，向路径添加椭圆。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 path、rect任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER； pathDirection不在枚举范围内时返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。 |
| void OH_Drawing_PathAddArc(OH_Drawing_Path* path, const OH_Drawing_Rect* rect, float startAngle, float sweepAngle) | 将圆弧添加到路径中，作为新轮廓的起点。从起始角度到扫描角度添加弧，添加的弧是矩形内切椭圆的一部分，如果扫描角度<= -360°，或>= 360°，并且起始角度对90取模接近于0，则添加椭圆而不是弧。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 path、rect任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| void OH_Drawing_PathAddPath(OH_Drawing_Path* path, const OH_Drawing_Path* src, const OH_Drawing_Matrix* matrix) | 将源路径矩阵变换后，添加到当前路径中。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 path、src任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| void OH_Drawing_PathAddPathWithMatrixAndMode(OH_Drawing_Path* path, const OH_Drawing_Path* src,const OH_Drawing_Matrix* matrix, OH_Drawing_PathAddMode pathAddMode) | 将源路径矩阵变换后，以规定模式添加到当前路径中。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 path、src任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER； pathAddMode不在枚举范围内时返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。 |
| void OH_Drawing_PathAddPathWithMode(OH_Drawing_Path* path,const OH_Drawing_Path* src, OH_Drawing_PathAddMode pathAddMode) | 将源路径以规定模式添加到当前路径中。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 path、src任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER； pathAddMode不在枚举范围内时返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。 |
| void OH_Drawing_PathAddPathWithOffsetAndMode(OH_Drawing_Path* path, const OH_Drawing_Path* src, float dx, float dy,OH_Drawing_PathAddMode pathAddMode) | 将源路径偏移后，以规定模式添加到当前路径中。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 path、src任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER； pathAddMode不在枚举范围内时返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。 |
| void OH_Drawing_PathAddPolygon(OH_Drawing_Path* path, const OH_Drawing_Point2D* points, uint32_t count, bool isClosed) | 向路径添加多边形。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 path、points任意一个为NULL或者count等于0时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| void OH_Drawing_PathAddCircle(OH_Drawing_Path* path,float x, float y, float radius, OH_Drawing_PathDirection pathDirection) | 按指定方向，向路径添加圆形。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 path为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER； radius小于等于0时返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE； pathDirection不在枚举范围内时返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。 |
| bool OH_Drawing_PathBuildFromSvgString(OH_Drawing_Path* path, const char* str) | 解析SVG字符串表示的路径。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 path、str任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| bool OH_Drawing_PathContains(OH_Drawing_Path* path, float x, float y) | 判断指定坐标点是否被路径包含，判定是否被路径包含的规则参考OH_Drawing_PathFillType。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 path为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| void OH_Drawing_PathTransform(OH_Drawing_Path* path, const OH_Drawing_Matrix* matrix) | 对路径进行矩阵变换。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 path、matrix任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| void OH_Drawing_PathTransformWithPerspectiveClip(OH_Drawing_Path* src, const OH_Drawing_Matrix* matrix,OH_Drawing_Path* dst, bool applyPerspectiveClip) | 对路径进行矩阵变换。用转换后的路径替换目标路径，如果目标路径为NULL，则替换源路径。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 src、matrix任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| void OH_Drawing_PathSetFillType(OH_Drawing_Path* path, OH_Drawing_PathFillType pathFillType) | 设置路径的填充类型，这个决定了路径内部区域的定义方式。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 path为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER； pathFillType不在枚举范围内返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。 |
| OH_Drawing_ErrorCode OH_Drawing_PathGetFillType(OH_Drawing_Path* path, OH_Drawing_PathFillType* pathFillType) | 获取路径的填充类型。 |
| float OH_Drawing_PathGetLength(OH_Drawing_Path* path, bool forceClosed) | 获取当前路径的长度。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 path为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| void OH_Drawing_PathGetBounds(OH_Drawing_Path* path, OH_Drawing_Rect* rect) | 获取包含路径的最小边界框。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 path、rect任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| void OH_Drawing_PathClose(OH_Drawing_Path* path) | 用于闭合路径，会添加一条从路径起点位置到最后点位置的线段。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 path为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| void OH_Drawing_PathOffset(OH_Drawing_Path* path, OH_Drawing_Path* dst, float dx, float dy) | 将路径中的所有点沿着x轴和y轴方向偏移一定距离，并将结果存储到目标路径对象中。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 path为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| void OH_Drawing_PathReset(OH_Drawing_Path* path) | 用于重置自定义路径数据。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 path为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| bool OH_Drawing_PathIsClosed(OH_Drawing_Path* path, bool forceClosed) | 获取路径是否闭合。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 path为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| bool OH_Drawing_PathGetPositionTangent(OH_Drawing_Path* path, bool forceClosed,float distance, OH_Drawing_Point2D* position, OH_Drawing_Point2D* tangent) | 获取距路径起始点指定距离的坐标点和切线值。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 path、position、tangent任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| OH_Drawing_ErrorCode OH_Drawing_PathGetSegment(OH_Drawing_Path* path, bool forceClosed,float start, float stop, bool startWithMoveTo, OH_Drawing_Path* dst, bool* result) | 截取路径的片段并追加到目标路径上。 |
| bool OH_Drawing_PathOp(OH_Drawing_Path* path, const OH_Drawing_Path* other, OH_Drawing_PathOpMode op) | 将两个路径按照指定的路径操作类型合并。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 path、srcPath任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER； op不在枚举范围内时返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。 |
| bool OH_Drawing_PathGetMatrix(OH_Drawing_Path* path, bool forceClosed,float distance, OH_Drawing_Matrix* matrix, OH_Drawing_PathMeasureMatrixFlags flag) | 获取距路径起始点指定距离的相应变换矩阵。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 path、matrix任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER； flag不在枚举范围内时返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。 |
| OH_Drawing_ErrorCode OH_Drawing_PathApproximate(OH_Drawing_Path* path, float acceptableError, float* vals,uint32_t* count) | 将当前路径转化为由连续直线段构成的近似路径。 |
| OH_Drawing_ErrorCode OH_Drawing_PathInterpolate(OH_Drawing_Path* path, OH_Drawing_Path* other,float weight, bool* success, OH_Drawing_Path* interpolatedPath) | 按照给定权重在当前路径与另一条路径之间进行插值，并将结果存储到目标路径对象中。  两条路径点数相同即可插值成功，目标路径按照当前路径的结构进行创建。 |
| OH_Drawing_ErrorCode OH_Drawing_PathIsInterpolate(OH_Drawing_Path* path, OH_Drawing_Path* other, bool* result) | 检查当前路径与另一条路径（other）在结构和操作顺序上是否完全一致，以确定两条路径是否兼容插值。  若路径中包含圆锥曲线（Conic）操作，则对应操作的权重值也必须一致，才能视为兼容插值。 |
| OH_Drawing_ErrorCode OH_Drawing_PathIsInverseFillType(const OH_Drawing_Path* path, bool* isInverse) | 检查路径的填充类型是否是取反类型。 取反类型即OH_Drawing_PathFillType中的PATH_FILL_TYPE_INVERSE_WINDING和PATH_FILL_TYPE_INVERSE_EVEN_ODD。 |
| OH_Drawing_ErrorCode OH_Drawing_PathToggleInverseFillType(OH_Drawing_Path* path) | 切换路径的填充类型为取反类型。 取反类型即OH_Drawing_PathFillType中的PATH_FILL_TYPE_INVERSE_WINDING和PATH_FILL_TYPE_INVERSE_EVEN_ODD。 |

**枚举类型说明**

**OH_Drawing_PathDirection**

```ets
enum OH_Drawing_PathDirection
```

描述

添加闭合轮廓方向枚举。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| PATH_DIRECTION_CW | 顺时针方向添加闭合轮廓。 |
| PATH_DIRECTION_CCW | 逆时针方向添加闭合轮廓。 |

**OH_Drawing_PathFillType**

```ets
enum OH_Drawing_PathFillType
```

描述

定义路径的填充类型枚举。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| PATH_FILL_TYPE_WINDING | 绘制区域中的任意一点，向任意方向射出一条射线，对于射线和路径的所有交点，初始计数为0， 遇到每个顺时针的交点（路径从射线的左边向右穿过），计数加1，遇到每个逆时针的交点（路径从射线的右边向左穿过），计数减1，若最终的计数结果不为0，则认为这个点在路径内部，需要被涂色；若计数为0则不被涂色。 |
| PATH_FILL_TYPE_EVEN_ODD | 绘制区域中的任意一点，向任意方向射出一条射线，若这条射线和路径相交的次数是奇数，则这个点被认为在路径内部，需要被涂色；若是偶数则不被涂色。 |
| PATH_FILL_TYPE_INVERSE_WINDING | PATH_FILL_TYPE_WINDING 涂色规则取反。 |
| PATH_FILL_TYPE_INVERSE_EVEN_ODD | PATH_FILL_TYPE_EVEN_ODD 涂色规则取反。 |

**OH_Drawing_PathAddMode**

```ets
enum OH_Drawing_PathAddMode
```

描述

用于指定路径添加模式的枚举类型。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| PATH_ADD_MODE_APPEND | 以追加的方式添加路径。 |
| PATH_ADD_MODE_EXTEND | 如果之前的路径未闭合，则添加直线闭合路径。 |

**OH_Drawing_PathOpMode**

```ets
enum OH_Drawing_PathOpMode
```

描述

路径操作类型枚举。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| PATH_OP_MODE_DIFFERENCE | 差集操作。 |
| PATH_OP_MODE_INTERSECT | 交集操作。 |
| PATH_OP_MODE_UNION | 并集操作。 |
| PATH_OP_MODE_XOR | 异或操作。 |
| PATH_OP_MODE_REVERSE_DIFFERENCE | 反向差集操作。 |

**OH_Drawing_PathMeasureMatrixFlags**

```ets
enum OH_Drawing_PathMeasureMatrixFlags
```

描述

路径测量获取相应矩阵信息维度枚举。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| GET_POSITION_MATRIX | 获取位置信息对应的矩阵。 |
| GET_TANGENT_MATRIX | 获取切线信息对应的矩阵。 |
| GET_POSITION_AND_TANGENT_MATRIX | 获取位置和切线信息对应的矩阵。 |

**函数说明**

**OH_Drawing_PathCreate()**

```ets
OH_Drawing_Path* OH_Drawing_PathCreate(void)
```

描述

用于创建一个路径对象。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 8

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_Path* | 函数会返回一个指针，指针指向创建的路径对象。 |

**OH_Drawing_PathCopy()**

```ets
OH_Drawing_Path* OH_Drawing_PathCopy(OH_Drawing_Path* path)
```

描述

创建一个路径对象副本[OH_Drawing_Path](OH_Drawing_Path.md)，用于拷贝一个已有路径对象。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

path为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Path* path | 指向路径对象OH_Drawing_Path的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_Path* | 函数返回一个指针，指针指向创建的路径对象副本OH_Drawing_Path。 |

**OH_Drawing_PathDestroy()**

```ets
void OH_Drawing_PathDestroy(OH_Drawing_Path* path)
```

描述

用于销毁路径对象并回收该对象占有的内存。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 8

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Path* path | 指向路径对象的指针。 |

**OH_Drawing_PathSetPath()**

```ets
OH_Drawing_ErrorCode OH_Drawing_PathSetPath(OH_Drawing_Path* path, OH_Drawing_Path* other)
```

描述

将一个路径对象设置成当前的路径对象。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Path* path | 指向路径对象OH_Drawing_Path的指针。 |
| OH_Drawing_Path* other | 用于设置的路径对象OH_Drawing_Path的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数返回执行结果。  返回OH_DRAWING_SUCCESS，表示执行成功。  返回OH_DRAWING_ERROR_INVALID_PARAMETER，表示参数path或者other为空。 |

**OH_Drawing_PathIsEmpty()**

```ets
OH_Drawing_ErrorCode OH_Drawing_PathIsEmpty(OH_Drawing_Path* path, bool* isEmpty)
```

描述

判断一个路径对象是否为空。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Path* path | 指向路径对象OH_Drawing_Path的指针。 |
| bool* isEmpty | 表示路径对象是否为空。true表示路径对象为空，false表示路径对象不为空。作为出参使用。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数返回执行结果。  返回OH_DRAWING_SUCCESS，表示执行成功。  返回OH_DRAWING_ERROR_INVALID_PARAMETER，表示参数path或者isEmpty为空。 |

**OH_Drawing_PathIsRect()**

```ets
OH_Drawing_ErrorCode OH_Drawing_PathIsRect(OH_Drawing_Path* path, OH_Drawing_Rect* rect, bool* isRect)
```

描述

判断路径对象是否构成一个矩形。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Path* path | 指向路径对象OH_Drawing_Path的指针。 |
| OH_Drawing_Rect* rect | 指向矩形对象OH_Drawing_Rect的指针，作为出参使用，可以为空。 |
| bool* isRect | 表示路径是否构成矩形。true表示构成矩形，false表示不构成矩形。作为出参使用。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数返回执行结果。  返回OH_DRAWING_SUCCESS，表示执行成功。  返回OH_DRAWING_ERROR_INVALID_PARAMETER，表示参数path或者isRect为空。 |

**OH_Drawing_PathMoveTo()**

```ets
void OH_Drawing_PathMoveTo(OH_Drawing_Path* path, float x, float y)
```

描述

用于设置自定义路径的起始点位置。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

path为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 8

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Path* path | 指向路径对象的指针。 |
| float x | 起始点的横坐标。 |
| float y | 起始点的纵坐标。 |

**OH_Drawing_PathLineTo()**

```ets
void OH_Drawing_PathLineTo(OH_Drawing_Path* path, float x, float y)
```

描述

用于添加一条从路径的最后点位置（若路径没有内容则默认为 (0, 0)）到目标点位置的线段。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

path为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 8

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Path* path | 指向路径对象的指针。 |
| float x | 目标点的横坐标。 |
| float y | 目标点的纵坐标。 |

**OH_Drawing_PathArcTo()**

```ets
void OH_Drawing_PathArcTo(OH_Drawing_Path* path,float x1, float y1, float x2, float y2, float startDeg, float sweepDeg)
```

描述

用于给路径添加一段弧线，绘制弧线的方式为角度弧，该方式首先会指定一个矩形边框，

矩形边框的内切椭圆将会被用来截取弧线，然后会指定一个起始角度和扫描度数，

从起始角度扫描截取的椭圆周长一部分即为绘制的弧线。若路径有内容则会默认添加一条从路径的最后点位置到弧线起始点位置的线段。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

path为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 8

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Path* path | 指向路径对象的指针。 |
| float x1 | 包围椭圆的矩形左上角点位置的横坐标。 |
| float y1 | 包围椭圆的矩形左上角点位置的纵坐标。 |
| float x2 | 包围椭圆的矩形右下角点位置的横坐标。 |
| float y2 | 包围椭圆的矩形右下角点位置的纵坐标。 |
| float startDeg | 起始的角度。角度的起始方向（0°）为x轴正方向。 |
| float sweepDeg | 扫描的度数，为正数时顺时针扫描，为负数时逆时针扫描。实际扫描的度数为该入参对360取模的结果。 |

**OH_Drawing_PathQuadTo()**

```ets
void OH_Drawing_PathQuadTo(OH_Drawing_Path* path, float ctrlX, float ctrlY, float endX, float endY)
```

描述

用于添加一条从路径最后点位置（若路径没有内容则默认为 (0, 0)）到目标点位置的二阶贝塞尔曲线。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

path为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 8

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Path* path | 指向路径对象的指针。 |
| float ctrlX | 控制点位置的横坐标。 |
| float ctrlY | 控制点位置的纵坐标。 |
| float endX | 目标点位置的横坐标。 |
| float endY | 目标点位置的纵坐标。 |

**OH_Drawing_PathConicTo()**

```ets
void OH_Drawing_PathConicTo(OH_Drawing_Path* path, float ctrlX, float ctrlY, float endX, float endY, float weight)
```

描述

在当前路径上添加一条路径终点（若路径没有内容则默认为 (0, 0)）到目标点位置的圆锥曲线段，其控制点为 (ctrlX, ctrlY)，结束点为 (endX, endY)。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

path为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Path* path | 指向路径对象OH_Drawing_Path的指针。 |
| float ctrlX | 控制点位置的横坐标。 |
| float ctrlY | 控制点位置的纵坐标。 |
| float endX | 结束点位置的横坐标。 |
| float endY | 结束点位置的纵坐标。 |
| float weight | 表示曲线的权重，决定了曲线的形状，越大越接近控制点。 若小于等于0则等同于使用OH_Drawing_PathLineTo添加一条到结束点的线段， 若为1则等同于OH_Drawing_PathQuadTo。 |

**OH_Drawing_PathCubicTo()**

```ets
void OH_Drawing_PathCubicTo(OH_Drawing_Path* path, float ctrlX1, float ctrlY1, float ctrlX2, float ctrlY2, float endX, float endY)
```

描述

用于添加一条从路径最后点位置（若路径没有内容则默认为 (0, 0)）到目标点位置的三阶贝塞尔圆滑曲线。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

path为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 8

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Path* path | 指向路径对象的指针。 |
| float ctrlX1 | 第一个控制点位置的横坐标。 |
| float ctrlY1 | 第一个控制点位置的纵坐标。 |
| float ctrlX2 | 第二个控制点位置的横坐标。 |
| float ctrlY2 | 第二个控制点位置的纵坐标。 |
| float endX | 目标点位置的横坐标。 |
| float endY | 目标点位置的纵坐标。 |

**OH_Drawing_PathRMoveTo()**

```ets
void OH_Drawing_PathRMoveTo(OH_Drawing_Path* path, float x, float y)
```

描述

用于设置一个相对于当前路径终点（若路径没有内容则默认为 (0, 0)）的路径起始点位置。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

path为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Path* path | 指向路径对象OH_Drawing_Path的指针。 |
| float x | 相对于当前路径终点的x轴偏移量，正数往x轴正方向偏移，负数往x轴负方向偏移。 |
| float y | 相对于当前路径终点的y轴偏移量，正数往y轴正方向偏移，负数往y轴负方向偏移。 |

**OH_Drawing_PathRLineTo()**

```ets
void OH_Drawing_PathRLineTo(OH_Drawing_Path* path, float x, float y)
```

描述

使用相对位置在当前路径上添加一条当前路径终点（若路径没有内容则默认为 (0, 0)）到目标点位置的线段。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

path为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Path* path | 指向路径对象OH_Drawing_Path的指针。 |
| float x | 相对于当前路径终点的x轴偏移量，用于指定目标点的横坐标。 |
| float y | 相对于当前路径终点的y轴偏移量，用于指定目标点的纵坐标。 |

**OH_Drawing_PathRQuadTo()**

```ets
void OH_Drawing_PathRQuadTo(OH_Drawing_Path* path, float ctrlX, float ctrlY, float endX, float endY)
```

描述

使用相对位置在当前路径上添加一条当前路径终点（若路径没有内容则默认为 (0, 0)）到目标点位置的二阶贝塞尔曲线。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

path为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Path* path | 指向路径对象OH_Drawing_Path的指针。 |
| float ctrlX | 相对于路径终点的x轴偏移量，用于指定控制点的横坐标。 |
| float ctrlY | 相对于路径终点的y轴偏移量，用于指定控制点的纵坐标。 |
| float endX | 相对于路径终点的x轴偏移量，用于指定目标点的横坐标。 |
| float endY | 相对于路径终点的y轴偏移量，用于指定目标点的纵坐标。 |

**OH_Drawing_PathRConicTo()**

```ets
void OH_Drawing_PathRConicTo(OH_Drawing_Path* path, float ctrlX, float ctrlY, float endX, float endY, float weight)
```

描述

使用相对位置在当前路径上添加一条路径终点（若路径没有内容则默认为 (0, 0)）到目标点位置的圆锥曲线段。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

path为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Path* path | 指向路径对象OH_Drawing_Path的指针。 |
| float ctrlX | 相对于路径终点的x轴偏移量，用于指定控制点的横坐标。 |
| float ctrlY | 相对于路径终点的y轴偏移量，用于指定控制点的纵坐标。 |
| float endX | 相对于路径终点的x轴偏移量，用于指定目标点的横坐标。 |
| float endY | 相对于路径终点的y轴偏移量，用于指定目标点的纵坐标。 |
| float weight | 表示曲线的权重，决定了曲线的形状，越大越接近控制点。 若小于等于0则等同于使用OH_Drawing_PathRLineTo添加一条到结束点的线段， 若为1则等同于OH_Drawing_PathRQuadTo。 |

**OH_Drawing_PathRCubicTo()**

```ets
void OH_Drawing_PathRCubicTo(OH_Drawing_Path* path, float ctrlX1, float ctrlY1, float ctrlX2, float ctrlY2,float endX, float endY)
```

描述

使用相对位置在当前路径上添加一条当前路径终点（若路径没有内容则默认为 (0, 0)）到目标点位置的三阶贝塞尔圆滑曲线。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

path为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Path* path | 指向路径对象OH_Drawing_Path的指针。 |
| float ctrlX1 | 相对于路径终点的x轴偏移量，用于指定第一个控制点的横坐标。 |
| float ctrlY1 | 相对于路径终点的y轴偏移量，用于指定第一个控制点的纵坐标。 |
| float ctrlX2 | 相对于路径终点的x轴偏移量，用于指定第二个控制点的横坐标。 |
| float ctrlY2 | 相对于路径终点的y轴偏移量，用于指定第二个控制点的纵坐标。 |
| float endX | 相对于路径终点的x轴偏移量，用于指定目标点的横坐标。 |
| float endY | 相对于路径终点的y轴偏移量，用于指定目标点的纵坐标。 |

**OH_Drawing_PathAddRect()**

```ets
void OH_Drawing_PathAddRect(OH_Drawing_Path* path, float left, float top, float right, float bottom,OH_Drawing_PathDirection pathDirection)
```

描述

按指定方向，将矩形添加到路径中，添加的路径的起始点为矩形左上角。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

path为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER；

pathDirection不在枚举范围内返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Path* path | 指向路径对象OH_Drawing_Path的指针。 |
| float left | 矩形左上角的x轴坐标。 |
| float top | 矩形左上角的y轴坐标。 |
| float right | 矩形右下角的x轴坐标。 |
| float bottom | 矩形右下角的y轴坐标。 |
| OH_Drawing_PathDirection pathDirection | 路径方向OH_Drawing_PathDirection。 |

**OH_Drawing_PathAddRectWithInitialCorner()**

```ets
void OH_Drawing_PathAddRectWithInitialCorner(OH_Drawing_Path* path, const OH_Drawing_Rect* rect,OH_Drawing_PathDirection pathDirection, uint32_t start)
```

描述

按指定方向，向路径添加矩形轮廓。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

path、rect任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER；

pathDirection不在枚举范围内返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Path* path | 指向路径对象OH_Drawing_Path的指针。 |
| const OH_Drawing_Rect* rect | 指向矩形对象OH_Drawing_Rect的指针。 |
| OH_Drawing_PathDirection | 表示绘制方向OH_Drawing_PathDirection。 |
| uint32_t start | 起始点的位置，表示从矩形的哪个角开始绘制路径。0：左上角，1：右上角，2：右下角，3：左下角。 |

**OH_Drawing_PathAddRoundRect()**

```ets
void OH_Drawing_PathAddRoundRect(OH_Drawing_Path* path,const OH_Drawing_RoundRect* roundRect, OH_Drawing_PathDirection pathDirection)
```

描述

按指定方向，向路径添加圆角矩形轮廓。路径添加方向为顺时针时，起始点位于圆角矩形左下方圆角与左边界的交点；路径添加方向为逆时针时，起始点位于圆角矩形左上方圆角与左边界的交点。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

path、roundRect任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER；

pathDirection不在枚举范围内返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Path* path | 指向路径对象OH_Drawing_Path的指针。 |
| const OH_Drawing_RoundRect* roundRect | 指向圆角矩形对象OH_Drawing_RoundRect的指针。 |
| OH_Drawing_PathDirection pathDirection | 路径方向OH_Drawing_PathDirection。 |

**OH_Drawing_PathAddOvalWithInitialPoint()**

```ets
void OH_Drawing_PathAddOvalWithInitialPoint(OH_Drawing_Path* path, const OH_Drawing_Rect* rect,uint32_t start, OH_Drawing_PathDirection pathDirection)
```

描述

将椭圆添加到路径中，其中矩形对象作为椭圆的外切矩形区域，绘制方向用来指定绘制时是顺时针或者逆时针方向。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

path、rect任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER；

pathDirection不在枚举范围内时返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Path* path | 指向路径对象OH_Drawing_Path的指针。 |
| const OH_Drawing_Rect* rect | 指向矩形对象OH_Drawing_Rect的指针。 |
| uint32_t start | 表示椭圆初始点的索引。 |
| OH_Drawing_PathDirection pathDirection | 表示绘制方向OH_Drawing_PathDirection。 |

**OH_Drawing_PathAddOval()**

```ets
void OH_Drawing_PathAddOval(OH_Drawing_Path* path,const OH_Drawing_Rect* rect, OH_Drawing_PathDirection pathDirection)
```

描述

按指定方向，向路径添加椭圆。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

path、rect任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER；

pathDirection不在枚举范围内时返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Path* path | 指向路径对象OH_Drawing_Path的指针。 |
| const OH_Drawing_Rect* rect | 指向矩形对象OH_Drawing_Rect的指针。 |
| OH_Drawing_PathDirection pathDirection | 路径方向OH_Drawing_PathDirection。 |

**OH_Drawing_PathAddArc()**

```ets
void OH_Drawing_PathAddArc(OH_Drawing_Path* path, const OH_Drawing_Rect* rect, float startAngle, float sweepAngle)
```

描述

将圆弧添加到路径中，作为新轮廓的起点。从起始角度到扫描角度添加弧，添加的弧是矩形内切椭圆的一部分，如果扫描角度<= -360°，或>= 360°，并且起始角度对90取模接近于0，则添加椭圆而不是弧。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

path、rect任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Path* path | 指向路径对象OH_Drawing_Path的指针。 |
| const OH_Drawing_Rect* rect | 指向矩形对象OH_Drawing_Rect的指针。 |
| float startAngle | 弧的起始角度，单位为度。 |
| float sweepAngle | 扫描的度数，为正数时顺时针扫描，为负数时逆时针扫描。实际扫描的度数为该入参对360取模的结果。 |

**OH_Drawing_PathAddPath()**

```ets
void OH_Drawing_PathAddPath(OH_Drawing_Path* path, const OH_Drawing_Path* src, const OH_Drawing_Matrix* matrix)
```

描述

将源路径矩阵变换后，添加到当前路径中。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

path、src任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Path* path | 指向当前路径对象OH_Drawing_Path的指针。 |
| const OH_Drawing_Path* src | 指向源路径对象OH_Drawing_Path的指针。 |
| const OH_Drawing_Matrix* matrix | 指向矩阵对象OH_Drawing_Matrix的指针，为NULL时表示单位矩阵。 |

**OH_Drawing_PathAddPathWithMatrixAndMode()**

```ets
void OH_Drawing_PathAddPathWithMatrixAndMode(OH_Drawing_Path* path, const OH_Drawing_Path* src,const OH_Drawing_Matrix* matrix, OH_Drawing_PathAddMode pathAddMode)
```

描述

将源路径矩阵变换后，以规定模式添加到当前路径中。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

path、src任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER；

pathAddMode不在枚举范围内时返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Path* path | 指向当前路径对象OH_Drawing_Path的指针。 |
| const OH_Drawing_Path* src | 指向源路径对象OH_Drawing_Path的指针。 |
| const OH_Drawing_Matrix* matrix | 指向矩阵对象OH_Drawing_Matrix的指针，为NULL表示单位矩阵。 |
| OH_Drawing_PathAddMode pathAddMode | 路径添加模式OH_Drawing_PathAddMode。 |

**OH_Drawing_PathAddPathWithMode()**

```ets
void OH_Drawing_PathAddPathWithMode(OH_Drawing_Path* path,const OH_Drawing_Path* src, OH_Drawing_PathAddMode pathAddMode)
```

描述

将源路径以规定模式添加到当前路径中。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

path、src任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER；

pathAddMode不在枚举范围内时返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Path* path | 指向当前路径对象OH_Drawing_Path的指针。 |
| const OH_Drawing_Path* src | 指向源路径对象OH_Drawing_Path的指针。 |
| OH_Drawing_PathAddMode pathAddMode | 路径添加模式OH_Drawing_PathAddMode。 |

**OH_Drawing_PathAddPathWithOffsetAndMode()**

```ets
void OH_Drawing_PathAddPathWithOffsetAndMode(OH_Drawing_Path* path, const OH_Drawing_Path* src, float dx, float dy,OH_Drawing_PathAddMode pathAddMode)
```

描述

将源路径偏移后，以规定模式添加到当前路径中。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

path、src任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER；

pathAddMode不在枚举范围内时返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Path* path | 指向当前路径对象OH_Drawing_Path的指针。 |
| const OH_Drawing_Path* src | 指向源路径对象OH_Drawing_Path的指针。 |
| float dx | 添加到目标路径横坐标的偏移量。 |
| float dy | 添加到目标路径纵坐标的偏移量。 |
| OH_Drawing_PathAddMode pathAddMode | 路径添加模式OH_Drawing_PathAddMode。 |

**OH_Drawing_PathAddPolygon()**

```ets
void OH_Drawing_PathAddPolygon(OH_Drawing_Path* path, const OH_Drawing_Point2D* points, uint32_t count, bool isClosed)
```

描述

向路径添加多边形。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

path、points任意一个为NULL或者count等于0时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Path* path | 指向当前路径对象OH_Drawing_Path的指针。 |
| const OH_Drawing_Point2D* points | 表示多边形的顶点坐标数组。 |
| uint32_t count | 表示多边形顶点坐标数组的大小。 |
| bool isClosed | 是否添加连接起始点和终止点的线，true表示添加，false表示不添加。 |

**OH_Drawing_PathAddCircle()**

```ets
void OH_Drawing_PathAddCircle(OH_Drawing_Path* path,float x, float y, float radius, OH_Drawing_PathDirection pathDirection)
```

描述

按指定方向，向路径添加圆形。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

path为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER；

radius小于等于0时返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE；

pathDirection不在枚举范围内时返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Path* path | 指向路径对象OH_Drawing_Path的指针。 |
| float x | 表示圆心的x轴坐标。 |
| float y | 表示圆心的y轴坐标。 |
| float radius | 表示圆形的半径。 |
| OH_Drawing_PathDirection pathDirection | 路径方向OH_Drawing_PathDirection。 |

**OH_Drawing_PathBuildFromSvgString()**

```ets
bool OH_Drawing_PathBuildFromSvgString(OH_Drawing_Path* path, const char* str)
```

描述

解析SVG字符串表示的路径。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

path、str任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Path* path | 指向路径对象OH_Drawing_Path的指针。 |
| const char* str | 表示SVG字符串。 |

返回：

| 类型 | 说明 |
| --- | --- |
| bool | 函数返回解析SVG字符串是否成功。true表示成功，false表示不成功。 |

**OH_Drawing_PathContains()**

```ets
bool OH_Drawing_PathContains(OH_Drawing_Path* path, float x, float y)
```

描述

判断指定坐标点是否被路径包含，判定是否被路径包含的规则参考[OH_Drawing_PathFillType](drawing_path.h.md#ZH-CN_TOPIC_0000002553362079__oh_drawing_pathfilltype)。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

path为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Path* path | 指向路径对象OH_Drawing_Path的指针。 |
| float x | x轴上坐标点。 |
| float y | y轴上坐标点。 |

返回：

| 类型 | 说明 |
| --- | --- |
| bool | 函数返回true表示点在路径内，函数返回false表示点在路径外。 |

**OH_Drawing_PathTransform()**

```ets
void OH_Drawing_PathTransform(OH_Drawing_Path* path, const OH_Drawing_Matrix* matrix)
```

描述

对路径进行矩阵变换。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

path、matrix任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Path* path | 指向路径对象OH_Drawing_Path的指针。 |
| const OH_Drawing_Matrix* matrix | 指向矩阵对象OH_Drawing_Matrix的指针。 |

**OH_Drawing_PathTransformWithPerspectiveClip()**

```ets
void OH_Drawing_PathTransformWithPerspectiveClip(OH_Drawing_Path* src, const OH_Drawing_Matrix* matrix,OH_Drawing_Path* dst, bool applyPerspectiveClip)
```

描述

对路径进行矩阵变换。用转换后的路径替换目标路径，如果目标路径为NULL，则替换源路径。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

src、matrix任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Path* src | 指向路径对象OH_Drawing_Path的指针。 |
| const OH_Drawing_Matrix* matrix | 指向矩阵对象OH_Drawing_Matrix的指针。 |
| OH_Drawing_Path* dst | 指向目标路径对象OH_Drawing_Path的指针。 |
| bool applyPerspectiveClip | 表示变换路径是否应用透视裁剪。true表示应用透视裁剪，false表示不用透视裁剪。 |

**OH_Drawing_PathSetFillType()**

```ets
void OH_Drawing_PathSetFillType(OH_Drawing_Path* path, OH_Drawing_PathFillType pathFillType)
```

描述

设置路径的填充类型，这个决定了路径内部区域的定义方式。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

path为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER；

pathFillType不在枚举范围内返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Path* path | 指向路径对象OH_Drawing_Path的指针。 |
| OH_Drawing_PathFillType pathFillType | 路径填充规则OH_Drawing_PathFillType。 |

**OH_Drawing_PathGetFillType()**

```ets
OH_Drawing_ErrorCode OH_Drawing_PathGetFillType(OH_Drawing_Path* path, OH_Drawing_PathFillType* pathFillType)
```

描述

获取路径的填充类型。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Path* path | 指向路径对象OH_Drawing_Path的指针。 |
| OH_Drawing_PathFillType* pathFillType | 指向路径填充规则OH_Drawing_PathFillType的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数返回执行结果。  返回OH_DRAWING_SUCCESS，表示执行成功。  返回OH_DRAWING_ERROR_INVALID_PARAMETER，表示参数path或者pathFillType为空。 |

**OH_Drawing_PathGetLength()**

```ets
float OH_Drawing_PathGetLength(OH_Drawing_Path* path, bool forceClosed)
```

描述

获取当前路径的长度。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

path为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Path* path | 指向路径对象OH_Drawing_Path的指针。 |
| bool forceClosed | 表示是否按照闭合路径测量。true表示测量时路径会被强制视为已闭合，false表示会根据路径的实际闭合状态测量。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | 函数返回当前路径的长度。 |

**OH_Drawing_PathGetBounds()**

```ets
void OH_Drawing_PathGetBounds(OH_Drawing_Path* path, OH_Drawing_Rect* rect)
```

描述

获取包含路径的最小边界框。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

path、rect任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Path* path | 指向路径对象OH_Drawing_Path的指针。 |
| OH_Drawing_Rect* rect | 指向矩形对象OH_Drawing_Rect的指针。 |

**OH_Drawing_PathClose()**

```ets
void OH_Drawing_PathClose(OH_Drawing_Path* path)
```

描述

用于闭合路径，会添加一条从路径起点位置到最后点位置的线段。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

path为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 8

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Path* path | 指向路径对象OH_Drawing_Path的指针。 |

**OH_Drawing_PathOffset()**

```ets
void OH_Drawing_PathOffset(OH_Drawing_Path* path, OH_Drawing_Path* dst, float dx, float dy)
```

描述

将路径中的所有点沿着x轴和y轴方向偏移一定距离，并将结果存储到目标路径对象中。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

path为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Path* path | 指向当前路径对象OH_Drawing_Path的指针。 |
| OH_Drawing_Path* dst | 指向目标路径对象OH_Drawing_Path的指针，为NULL时会将结果存储到当前路径对象中。 |
| float dx | x轴方向的偏移量。 |
| float dy | y轴方向的偏移量。 |

**OH_Drawing_PathReset()**

```ets
void OH_Drawing_PathReset(OH_Drawing_Path* path)
```

描述

用于重置自定义路径数据。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

path为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 8

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Path* path | 指向路径对象的指针。 |

**OH_Drawing_PathIsClosed()**

```ets
bool OH_Drawing_PathIsClosed(OH_Drawing_Path* path, bool forceClosed)
```

描述

获取路径是否闭合。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

path为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Path* path | 指向路径对象OH_Drawing_Path的指针。 |
| bool forceClosed | 表示是否按照闭合路径测量，true表示测量时路径会被强制视为已闭合，false表示会根据路径的实际闭合状态测量。 |

返回：

| 类型 | 说明 |
| --- | --- |
| bool | 返回路径是否闭合。true表示路径的测量结果为已闭合，false表示路径的测量结果为未闭合。 |

**OH_Drawing_PathGetPositionTangent()**

```ets
bool OH_Drawing_PathGetPositionTangent(OH_Drawing_Path* path, bool forceClosed,float distance, OH_Drawing_Point2D* position, OH_Drawing_Point2D* tangent)
```

描述

获取距路径起始点指定距离的坐标点和切线值。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

path、position、tangent任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Path* path | 指向路径对象OH_Drawing_Path的指针。 |
| bool forceClosed | 表示是否按照闭合路径测量，true表示测量时路径会被强制视为已闭合，false表示会根据路径的实际闭合状态测量。 |
| float distance | 表示距离起始点的距离，小于0时会被视为0处理，大于路径长度时会被视为路径长度处理。 |
| OH_Drawing_Point2D* position | 表示距路径起始点指定距离的坐标点。 |
| OH_Drawing_Point2D* tangent | 表示距路径起始点指定距离的切线值，tangent.x表示该点切线的余弦值，tangent.y表示该点切线的正弦值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| bool | 返回测量是否成功。true表示成功，false表示失败。 |

**OH_Drawing_PathGetSegment()**

```ets
OH_Drawing_ErrorCode OH_Drawing_PathGetSegment(OH_Drawing_Path* path, bool forceClosed,float start, float stop, bool startWithMoveTo, OH_Drawing_Path* dst, bool* result)
```

描述

截取路径的片段并追加到目标路径上。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Path* path | 指向路径对象OH_Drawing_Path的指针。 |
| bool forceClosed | 表示是否按照闭合路径测量，true表示测量时路径会被强制视为已闭合，false表示会根据路径的实际闭合状态测量。 |
| float start | 表示与路径起始点的距离，距离路径起始点start距离的位置即为截取路径片段的起始点，小于0时会被视作0，大于等于stop时会截取失败。 |
| float stop | 表示与路径起始点的距离，距离路径起始点stop距离的位置即为截取路径片段的终点，小于等于start时会截取失败，大于路径长度时会被视作路径长度。 |
| bool startWithMoveTo | 表示是否在目标路径执行OH_Drawing_PathMoveTo移动到截取路径片段的起始点位置。true表示执行，false表示不执行。 |
| OH_Drawing_Path* dst | 指向目标路径对象OH_Drawing_Path的指针，截取成功时会将得到的路径片段追加到目标路径上，截取失败时不做改变。 |
| bool* result | 返回是否成功截取路径片段的结果。true表示截取成功，false表示截取失败。作为出参使用。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数返回执行错误码。  返回OH_DRAWING_SUCCESS，表示执行成功。  返回OH_DRAWING_ERROR_INVALID_PARAMETER，表示参数path、dst、result至少有一个为空指针。 |

**OH_Drawing_PathOp()**

```ets
bool OH_Drawing_PathOp(OH_Drawing_Path* path, const OH_Drawing_Path* other, OH_Drawing_PathOpMode op)
```

描述

将两个路径按照指定的路径操作类型合并。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

path、srcPath任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER；

op不在枚举范围内时返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Path* path | 指向路径对象OH_Drawing_Path的指针，操作完成后的路径结果将会保存在此路径对象中。 |
| const OH_Drawing_Path* other | 指向路径对象OH_Drawing_Path的指针。 |
| OH_Drawing_PathOpMode op | 路径操作枚举类型，支持可选的具体模式可见OH_Drawing_PathOpMode枚举。 |

返回：

| 类型 | 说明 |
| --- | --- |
| bool | 返回操作后的路径是否为空。true表示路径不为空，false表示路径为空。 |

**OH_Drawing_PathGetMatrix()**

```ets
bool OH_Drawing_PathGetMatrix(OH_Drawing_Path* path, bool forceClosed,float distance, OH_Drawing_Matrix* matrix, OH_Drawing_PathMeasureMatrixFlags flag)
```

描述

获取距路径起始点指定距离的相应变换矩阵。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

path、matrix任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER；

flag不在枚举范围内时返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Path* path | 指向路径对象OH_Drawing_Path的指针。 |
| bool forceClosed | 表示是否按照闭合路径测量，true表示测量时路径会被强制视为已闭合，false表示会根据路径的实际闭合状态测量。 |
| float distance | 表示距离起始点的距离，小于0时会被视为0处理，大于路径长度时会被视为路径长度处理。 |
| OH_Drawing_Matrix* matrix | 表示要获取的变换矩阵。 |
| OH_Drawing_PathMeasureMatrixFlags flag | 矩阵信息维度枚举，支持可选的具体模式可见OH_Drawing_PathMeasureMatrixFlags枚举。 |

返回：

| 类型 | 说明 |
| --- | --- |
| bool | 返回获取变换矩阵是否成功。true表示获取成功，false表示获取失败，失败的原因可能是path为NULL或者长度为0。 |

**OH_Drawing_PathApproximate()**

```ets
OH_Drawing_ErrorCode OH_Drawing_PathApproximate(OH_Drawing_Path* path, float acceptableError, float* vals,uint32_t* count)
```

描述

将当前路径转化为由连续直线段构成的近似路径。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Path* path | 指向路径对象OH_Drawing_Path的指针。 |
| float acceptableError | 表示路径上每条线段的可接受误差，不能小于0。  1.当acceptableError为0时，曲线路径被极度细分，会严重影响性能和内存消耗，不建议设置误差值为0。  2.当acceptableError特别大时，路径会极度简化，保留少量关键点，可能会丢失原有形状。  3.对于椭圆等曲线，当acceptableError过大时，拟合结果通常只包含椭圆的分段贝塞尔曲线的起止点，椭圆形会被极度简化为多边形。 |
| float* vals | 返回包含路径近似点的数组。  每个点由三个值组成，分别表示：  1.该点所在的位置距离路径起点的长度比例值。  2.点的x坐标。  3.点的y坐标。 |
| uint32_t* count | 返回数组的大小，数组大小至少为6。vals为空指针时返回拟合后的点数数组的大小。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数返回执行结果。  返回OH_DRAWING_SUCCESS，表示执行成功。  返回OH_DRAWING_ERROR_INVALID_PARAMETER，表示参数path或者count为空指针。  返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE，表示参数acceptableError小于0。 |

**OH_Drawing_PathInterpolate()**

```ets
OH_Drawing_ErrorCode OH_Drawing_PathInterpolate(OH_Drawing_Path* path, OH_Drawing_Path* other,float weight, bool* success, OH_Drawing_Path* interpolatedPath)
```

描述

按照给定权重在当前路径与另一条路径之间进行插值，并将结果存储到目标路径对象中。

 两条路径点数相同即可插值成功，目标路径按照当前路径的结构进行创建。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Path* path | 指向路径对象OH_Drawing_Path的指针。 |
| OH_Drawing_Path* other | 指向用于插值的另一条路径对象OH_Drawing_Path的指针。 |
| float weight | 表示插值权重，范围为[0, 1]。 |
| bool* success | 表示插值是否成功。true表示插值成功，false表示插值失败。作为出参使用。 |
| OH_Drawing_Path* interpolatedPath | 指向用于存储插值结果的路径对象OH_Drawing_Path的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数返回执行结果。  返回OH_DRAWING_SUCCESS，表示执行成功。  返回OH_DRAWING_ERROR_INVALID_PARAMETER，表示参数path、other、success或者interpolatedPath为空指针。  返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE，表示参数weight不在[0, 1]范围内。 |

**OH_Drawing_PathIsInterpolate()**

```ets
OH_Drawing_ErrorCode OH_Drawing_PathIsInterpolate(OH_Drawing_Path* path, OH_Drawing_Path* other, bool* result)
```

描述

检查当前路径与另一条路径（other）在结构和操作顺序上是否完全一致，以确定两条路径是否兼容插值。

 若路径中包含圆锥曲线（Conic）操作，则对应操作的权重值也必须一致，才能视为兼容插值。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Path* path | 指向路径对象OH_Drawing_Path的指针。 |
| OH_Drawing_Path* other | 指向另一条路径对象OH_Drawing_Path的指针。 |
| bool* result | 表示当前路径与另一条路径是否兼容插值。作为出参使用。  如果路径兼容，则返回true，否则返回false。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数返回执行结果。  返回OH_DRAWING_SUCCESS，表示执行成功。  返回OH_DRAWING_ERROR_INVALID_PARAMETER，表示参数path、other或者result为空指针。 |

**OH_Drawing_PathIsInverseFillType()**

```ets
OH_Drawing_ErrorCode OH_Drawing_PathIsInverseFillType(const OH_Drawing_Path* path, bool* isInverse)
```

描述

检查路径的填充类型是否是取反类型。

取反类型即[OH_Drawing_PathFillType](drawing_path.h.md#ZH-CN_TOPIC_0000002553362079__oh_drawing_pathfilltype)中的PATH_FILL_TYPE_INVERSE_WINDING和PATH_FILL_TYPE_INVERSE_EVEN_ODD。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_Drawing_Path* path | 指向路径对象OH_Drawing_Path的指针。 |
| bool* isInverse | 表示填充类型是否是取反类型。作为出参使用。true表示填充类型是取反类型，false表示填充类型不是取反类型。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数返回执行结果。 返回OH_DRAWING_SUCCESS，表示执行成功。 返回OH_DRAWING_ERROR_INCORRECT_PARAMETER，表示path或isInverse是空指针。 |

**OH_Drawing_PathToggleInverseFillType()**

```ets
OH_Drawing_ErrorCode OH_Drawing_PathToggleInverseFillType(OH_Drawing_Path* path)
```

描述

切换路径的填充类型为取反类型。

取反类型即[OH_Drawing_PathFillType](drawing_path.h.md#ZH-CN_TOPIC_0000002553362079__oh_drawing_pathfilltype)中的PATH_FILL_TYPE_INVERSE_WINDING和PATH_FILL_TYPE_INVERSE_EVEN_ODD。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Path* path | 指向路径对象OH_Drawing_Path的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数返回执行结果。 返回OH_DRAWING_SUCCESS，表示执行成功。 返回OH_DRAWING_ERROR_INCORRECT_PARAMETER，表示path是空指针。 |