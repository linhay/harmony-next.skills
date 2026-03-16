# drawing_record_cmd.h

#### 概述

文件中定义了与录制指令对象相关的功能函数。

**引用文件：** <native_drawing/drawing_record_cmd.h>

**库：** libnative_drawing.so

**起始版本：** 13

**相关模块：**[Drawing](../../topics/graphics/Drawing.md)

#### 汇总

#### 函数

名称描述[OH_Drawing_RecordCmdUtils* OH_Drawing_RecordCmdUtilsCreate(void)](#ZH-CN_TOPIC_0000002497606008__oh_drawing_recordcmdutilscreate)创建一个录制指令工具对象。[OH_Drawing_ErrorCode OH_Drawing_RecordCmdUtilsDestroy(OH_Drawing_RecordCmdUtils* recordCmdUtils)](#ZH-CN_TOPIC_0000002497606008__oh_drawing_recordcmdutilsdestroy)销毁一个录制指令工具对象，并回收该对象占有的内存。[OH_Drawing_ErrorCode OH_Drawing_RecordCmdUtilsBeginRecording(OH_Drawing_RecordCmdUtils* recordCmdUtils,int32_t width, int32_t height, OH_Drawing_Canvas** canvas)](#ZH-CN_TOPIC_0000002497606008__oh_drawing_recordcmdutilsbeginrecording)

开始录制。此接口需要与[OH_Drawing_RecordCmdUtilsFinishRecording](drawing_record_cmd.h.md#ZH-CN_TOPIC_0000002497606008__oh_drawing_recordcmdutilsfinishrecording)接口成对使用。

指令录制工具生成录制类型的画布对象，可调用drawing的绘制接口，记录接下来所有的绘制指令。

[OH_Drawing_ErrorCode OH_Drawing_RecordCmdUtilsFinishRecording(OH_Drawing_RecordCmdUtils* recordCmdUtils,OH_Drawing_RecordCmd** recordCmd)](#ZH-CN_TOPIC_0000002497606008__oh_drawing_recordcmdutilsfinishrecording)

结束录制。在调用此接口前，需要先调用[OH_Drawing_RecordCmdUtilsBeginRecording](drawing_record_cmd.h.md#ZH-CN_TOPIC_0000002497606008__oh_drawing_recordcmdutilsbeginrecording)接口。

指令录制工具结束录制指令，将录制类型画布对象记录的绘制指令存入生成的录制指令对象。

[OH_Drawing_ErrorCode OH_Drawing_RecordCmdDestroy(OH_Drawing_RecordCmd* recordCmd)](#ZH-CN_TOPIC_0000002497606008__oh_drawing_recordcmddestroy)销毁录制指令对象，并回收该对象占有的内存。

#### 函数说明

#### OH_Drawing_RecordCmdUtilsCreate()

```ets
OH_Drawing_RecordCmdUtils* OH_Drawing_RecordCmdUtilsCreate(void)
```

**描述**

创建一个录制指令工具对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 13

**返回：**

类型说明[OH_Drawing_RecordCmdUtils](../../topics/graphics/OH_Drawing_RecordCmdUtils.md)*返回用于录制指令的工具对象。

#### OH_Drawing_RecordCmdUtilsDestroy()

```ets
OH_Drawing_ErrorCode OH_Drawing_RecordCmdUtilsDestroy(OH_Drawing_RecordCmdUtils* recordCmdUtils)
```

**描述**

销毁一个录制指令工具对象，并回收该对象占有的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 13

**参数：**

参数项描述[OH_Drawing_RecordCmdUtils](../../topics/graphics/OH_Drawing_RecordCmdUtils.md)* recordCmdUtils指向录制指令工具对象[OH_Drawing_RecordCmdUtils](../../topics/graphics/OH_Drawing_RecordCmdUtils.md)的指针。

**返回：**

类型说明[OH_Drawing_ErrorCode](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcode)

函数返回执行错误码。

 返回OH_DRAWING_SUCCESS，表示执行成功。

 返回OH_DRAWING_ERROR_INVALID_PARAMETER，表示参数recordCmdUtils为空。

#### OH_Drawing_RecordCmdUtilsBeginRecording()

```ets
OH_Drawing_ErrorCode OH_Drawing_RecordCmdUtilsBeginRecording(OH_Drawing_RecordCmdUtils* recordCmdUtils,int32_t width, int32_t height, OH_Drawing_Canvas** canvas)
```

**描述**

开始录制。此接口需要与[OH_Drawing_RecordCmdUtilsFinishRecording](drawing_record_cmd.h.md#ZH-CN_TOPIC_0000002497606008__oh_drawing_recordcmdutilsfinishrecording)接口成对使用。

指令录制工具生成录制类型的画布对象，可调用drawing的绘制接口，记录接下来所有的绘制指令。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 13

**参数：**

参数项描述[OH_Drawing_RecordCmdUtils](../../topics/graphics/OH_Drawing_RecordCmdUtils.md)* recordCmdUtils指向录制工具对象[OH_Drawing_RecordCmdUtils](../../topics/graphics/OH_Drawing_RecordCmdUtils.md)的指针。int32_t width画布的宽度。int32_t height画布的高度。[OH_Drawing_Canvas](../../topics/graphics/OH_Drawing_Canvas.md)** canvas

指向画布对象[OH_Drawing_Canvas](../../topics/graphics/OH_Drawing_Canvas.md)的二级指针，作为出参，开发者无需释放。

该画布对象不支持嵌套调用[OH_Drawing_CanvasDrawRecordCmd](drawing_canvas.h.md#ZH-CN_TOPIC_0000002497605998__oh_drawing_canvasdrawrecordcmd)接口。

**返回：**

类型说明[OH_Drawing_ErrorCode](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcode)

函数返回执行错误码。

 返回OH_DRAWING_SUCCESS, 表示执行成功。

 返回OH_DRAWING_ERROR_INVALID_PARAMETER, 表示参数recordCmdUtils或者canvas为空。

 当width和height小于等于0的时，也会返回OH_DRAWING_ERROR_INVALID_PARAMETER。

 返回OH_DRAWING_ERROR_ALLOCATION_FAILED，表示系统内存不足。

#### OH_Drawing_RecordCmdUtilsFinishRecording()

```ets
OH_Drawing_ErrorCode OH_Drawing_RecordCmdUtilsFinishRecording(OH_Drawing_RecordCmdUtils* recordCmdUtils,OH_Drawing_RecordCmd** recordCmd)
```

**描述**

结束录制。在调用此接口前，需要先调用[OH_Drawing_RecordCmdUtilsBeginRecording](drawing_record_cmd.h.md#ZH-CN_TOPIC_0000002497606008__oh_drawing_recordcmdutilsbeginrecording)接口。

指令录制工具结束录制指令，将录制类型画布对象记录的绘制指令存入生成的录制指令对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 13

**参数：**

参数项描述[OH_Drawing_RecordCmdUtils](../../topics/graphics/OH_Drawing_RecordCmdUtils.md)* recordCmdUtils指向录制指令工具对象[OH_Drawing_RecordCmdUtils](../../topics/graphics/OH_Drawing_RecordCmdUtils.md)的指针。[OH_Drawing_RecordCmd](../../topics/graphics/OH_Drawing_RecordCmd.md)** recordCmd指向录制指令对象[OH_Drawing_RecordCmd](../../topics/graphics/OH_Drawing_RecordCmd.md)的二级指针，作为出参，开发者调用[OH_Drawing_CanvasDrawRecordCmd](drawing_canvas.h.md#ZH-CN_TOPIC_0000002497605998__oh_drawing_canvasdrawrecordcmd)接口绘制该对象。需要调用[OH_Drawing_RecordCmdDestroy](drawing_record_cmd.h.md#ZH-CN_TOPIC_0000002497606008__oh_drawing_recordcmddestroy)接口释放。

**返回：**

类型说明[OH_Drawing_ErrorCode](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcode)

函数返回执行错误码。

 返回OH_DRAWING_SUCCESS，表示执行成功。

 返回OH_DRAWING_ERROR_INVALID_PARAMETER，表示参数recordCmdUtils或者recordCmd为空。

 返回OH_DRAWING_ERROR_ALLOCATION_FAILED，表示系统内存不足。

#### OH_Drawing_RecordCmdDestroy()

```ets
OH_Drawing_ErrorCode OH_Drawing_RecordCmdDestroy(OH_Drawing_RecordCmd* recordCmd)
```

**描述**

销毁录制指令对象，并回收该对象占有的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 13

**参数：**

参数项描述[OH_Drawing_RecordCmd](../../topics/graphics/OH_Drawing_RecordCmd.md)* recordCmd指向对象[OH_Drawing_RecordCmd](../../topics/graphics/OH_Drawing_RecordCmd.md)的指针。

**返回：**

类型说明[OH_Drawing_ErrorCode](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcode)

函数返回执行错误码。

 返回OH_DRAWING_SUCCESS，表示执行成功。

 返回OH_DRAWING_ERROR_INVALID_PARAMETER，表示参数recordCmd为空。