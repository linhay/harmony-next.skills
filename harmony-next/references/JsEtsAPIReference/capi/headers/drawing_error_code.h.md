# drawing_error_code.h

#### 概述

声明与绘图模块中的错误码相关的函数。

**引用文件：** <native_drawing/drawing_error_code.h>

**库：** libnative_drawing.so

**起始版本：** 12

**相关模块：**[Drawing](../../topics/graphics/Drawing.md)

#### 汇总

#### 枚举

名称typedef关键字描述[OH_Drawing_ErrorCode](#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcode)OH_Drawing_ErrorCode枚举本模块可能产生的错误码。

#### 函数

名称描述[OH_Drawing_ErrorCode OH_Drawing_ErrorCodeGet()](#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)获取本模块的错误码。[void OH_Drawing_ErrorCodeReset(void)](#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodereset)

将本模块的错误码重置为OH_DRAWING_SUCCESS。

通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)获取的本模块错误码会在不以错误码为返回值的接口执行失败时被置为对应的错误编号，但是不会在执行成功后被重置为OH_DRAWING_SUCCESS。

调用本接口可将错误码重置为OH_DRAWING_SUCCESS，避免多个接口间互相干扰，方便开发者调试。

#### 枚举类型说明

#### OH_Drawing_ErrorCode

```ets
enum OH_Drawing_ErrorCode
```

**描述**

枚举本模块可能产生的错误码。

**起始版本：** 12

枚举项描述OH_DRAWING_SUCCESS = 0操作成功完成。OH_DRAWING_ERROR_NO_PERMISSION = 201权限校验失败。OH_DRAWING_ERROR_INVALID_PARAMETER = 401无效的输入参数，如参数中传入了NULL。OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE = 26200001输入参数不在有效的范围内。OH_DRAWING_ERROR_ALLOCATION_FAILED = 26200002

内存分配失败。

**起始版本：** 13

OH_DRAWING_ERROR_ATTRIBUTE_ID_MISMATCH = 26200003

输入属性id无匹配的函数。

**起始版本：** 21

OH_DRAWING_ERROR_INCORRECT_PARAMETER = 26200004

输入参数不正确，例如入参的指针为空。

**起始版本：** 22

#### 函数说明

#### OH_Drawing_ErrorCodeGet()

```ets
OH_Drawing_ErrorCode OH_Drawing_ErrorCodeGet()
```

**描述**

获取本模块的错误码。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**返回：**

类型说明[OH_Drawing_ErrorCode](#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcode)获取本模块的最近一次的错误码。当函数成功运行后，本函数返回的错误码不会被修改。

#### OH_Drawing_ErrorCodeReset()

```ets
void OH_Drawing_ErrorCodeReset(void)
```

**描述**

将本模块的错误码重置为OH_DRAWING_SUCCESS。

通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)获取的本模块错误码会在不以错误码为返回值的接口执行失败时被置为对应的错误编号，但是不会在执行成功后被重置为OH_DRAWING_SUCCESS。

调用本接口可将错误码重置为OH_DRAWING_SUCCESS，避免多个接口间互相干扰，方便开发者调试。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18