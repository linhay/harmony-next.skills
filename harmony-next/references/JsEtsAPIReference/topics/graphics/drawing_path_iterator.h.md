# drawing_path_iterator.h

**概述**

声明与路径操作迭代器对象相关的函数。

引用文件： <native_drawing/drawing_path_iterator.h>

库： libnative_drawing.so

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 23

相关模块： [Drawing](Drawing.md)

**汇总**

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_Drawing_PathIteratorVerb | OH_Drawing_PathIteratorVerb | 迭代器包含的路径操作类型枚举，可用于读取路径的操作指令。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| OH_Drawing_ErrorCode OH_Drawing_PathIteratorCreate(const OH_Drawing_Path* path, OH_Drawing_PathIterator** pathIterator) | 创建路径操作迭代器对象。 |
| OH_Drawing_ErrorCode OH_Drawing_PathIteratorDestroy(OH_Drawing_PathIterator* pathIterator) | 销毁路径操作迭代器对象并回收该对象占有的内存。 |
| OH_Drawing_ErrorCode OH_Drawing_PathIteratorHasNext(const OH_Drawing_PathIterator* pathIterator, bool* hasNext) | 判断路径操作迭代器中是否还有下一个操作。 |
| OH_Drawing_ErrorCode OH_Drawing_PathIteratorNext(OH_Drawing_PathIterator* pathIterator, OH_Drawing_Point2D* points, uint32_t count, uint32_t offset, OH_Drawing_PathIteratorVerb* verb) | 返回当前路径的下一个操作，并将迭代器置于该操作。 |
| OH_Drawing_ErrorCode OH_Drawing_PathIteratorPeek(const OH_Drawing_PathIterator* pathIterator, OH_Drawing_PathIteratorVerb* verb) | 返回当前路径的下一个操作，迭代器保持在原操作。 |

**枚举类型说明**

**OH_Drawing_PathIteratorVerb**

```ets
enum OH_Drawing_PathIteratorVerb
```

描述

迭代器包含的路径操作类型枚举，可用于读取路径的操作指令。

起始版本： 23

| 枚举项 | 描述 |
| --- | --- |
| MOVE = 0 | 设置路径的起始点。 |
| LINE = 1 | 添加线段。 |
| QUAD = 2 | 添加二阶贝塞尔圆滑曲线。 |
| CONIC = 3 | 添加圆锥曲线。 |
| CUBIC = 4 | 添加三阶贝塞尔圆滑曲线。 |
| CLOSE = 5 | 闭合路径。 |
| DONE = CLOSE + 1 | 完成路径设置。 |

**函数说明**

**OH_Drawing_PathIteratorCreate()**

```ets
OH_Drawing_ErrorCode OH_Drawing_PathIteratorCreate(const OH_Drawing_Path* path, OH_Drawing_PathIterator** pathIterator)
```

描述

创建路径操作迭代器对象。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_Drawing_Path* path | 指向路径对象OH_Drawing_Path的指针。 |
| OH_Drawing_PathIterator** pathIterator | 指向路径操作迭代器对象OH_Drawing_PathIterator的二级指针，作为出参使用。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数返回执行结果。 返回OH_DRAWING_SUCCESS，表示执行成功。 返回OH_DRAWING_ERROR_INCORRECT_PARAMETER，表示path或pathIterator是空指针。 |

**OH_Drawing_PathIteratorDestroy()**

```ets
OH_Drawing_ErrorCode OH_Drawing_PathIteratorDestroy(OH_Drawing_PathIterator* pathIterator)
```

描述

销毁路径操作迭代器对象并回收该对象占有的内存。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_PathIterator* pathIterator | 指向路径操作迭代器对象OH_Drawing_PathIterator的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数返回执行结果。 返回OH_DRAWING_SUCCESS，表示执行成功。 返回OH_DRAWING_ERROR_INCORRECT_PARAMETER，表示pathIterator是空指针。 |

**OH_Drawing_PathIteratorHasNext()**

```ets
OH_Drawing_ErrorCode OH_Drawing_PathIteratorHasNext(const OH_Drawing_PathIterator* pathIterator, bool* hasNext)
```

描述

判断路径操作迭代器中是否还有下一个操作。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_Drawing_PathIterator* pathIterator | 指向路径操作迭代器对象OH_Drawing_PathIterator的指针。 |
| bool* hasNext | 表示路径操作迭代器中是否还有下一个操作。作为出参使用。true表示还有下一个操作，false表示没有下一个操作。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数返回执行结果。 返回OH_DRAWING_SUCCESS，表示执行成功。 返回OH_DRAWING_ERROR_INCORRECT_PARAMETER，表示pathIterator或hasNext是空指针。 |

**OH_Drawing_PathIteratorNext()**

```ets
OH_Drawing_ErrorCode OH_Drawing_PathIteratorNext(OH_Drawing_PathIterator* pathIterator, OH_Drawing_Point2D* points, uint32_t count, uint32_t offset, OH_Drawing_PathIteratorVerb* verb)
```

描述

返回当前路径的下一个操作，并将迭代器置于该操作。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_PathIterator* pathIterator | 指向路径操作迭代器对象OH_Drawing_PathIterator的指针。 |
| OH_Drawing_Point2D* points | 表示坐标点数组。 |
| uint32_t count | 表示坐标点数组的大小。 |
| uint32_t offset | 数组中写入位置相对起始点的偏移量，取值范围为[0, count-4]。 |
| OH_Drawing_PathIteratorVerb* verb | 表示当前路径的下一个操作。作为出参使用。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数返回执行结果。 返回OH_DRAWING_SUCCESS，表示执行成功。 返回OH_DRAWING_ERROR_INCORRECT_PARAMETER，表示pathIterator或points或verb是空指针。 返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE，表示count小于offset + 4。 |

**OH_Drawing_PathIteratorPeek()**

```ets
OH_Drawing_ErrorCode OH_Drawing_PathIteratorPeek(const OH_Drawing_PathIterator* pathIterator, OH_Drawing_PathIteratorVerb* verb)
```

描述

返回当前路径的下一个操作，迭代器保持在原操作。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_Drawing_PathIterator* pathIterator | 指向路径操作迭代器对象OH_Drawing_PathIterator的指针。 |
| OH_Drawing_PathIteratorVerb* verb | 表示当前路径的下一个操作。作为出参使用。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数返回执行结果。 返回OH_DRAWING_SUCCESS，表示执行成功。 返回OH_DRAWING_ERROR_INCORRECT_PARAMETER，表示pathIterator或verb是空指针。 |