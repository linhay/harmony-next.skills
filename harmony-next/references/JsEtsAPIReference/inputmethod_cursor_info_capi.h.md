# inputmethod_cursor_info_capi.h

#### 概述

提供光标信息对象的创建、销毁与读写方法。

**引用文件：** <inputmethod/inputmethod_cursor_info_capi.h>

**库：** libohinputmethod.so

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 12

**相关模块：**[InputMethod](InputMethod.md)

#### 汇总

#### 结构体

名称typedef关键字描述[InputMethod_CursorInfo](InputMethod_CursorInfo.md)InputMethod_CursorInfo光标信息。光标的坐标位置、宽度和高度。

#### 函数

名称描述[InputMethod_CursorInfo *OH_CursorInfo_Create(double left, double top, double width, double height)](#ZH-CN_TOPIC_0000002497605294__oh_cursorinfo_create)创建一个新的[InputMethod_CursorInfo](zh-cn_topic_0000002497445320.html)实例。[void OH_CursorInfo_Destroy(InputMethod_CursorInfo *cursorInfo)](#ZH-CN_TOPIC_0000002497605294__oh_cursorinfo_destroy)销毁一个[InputMethod_CursorInfo](zh-cn_topic_0000002497445320.html)实例。[InputMethod_ErrorCode OH_CursorInfo_SetRect(InputMethod_CursorInfo *cursorInfo, double left, double top, double width, double height)](#ZH-CN_TOPIC_0000002497605294__oh_cursorinfo_setrect)设置光标信息内容。[InputMethod_ErrorCode OH_CursorInfo_GetRect(InputMethod_CursorInfo *cursorInfo, double *left, double *top, double *width, double *height)](#ZH-CN_TOPIC_0000002497605294__oh_cursorinfo_getrect)获取光标信息内容。

#### 函数说明

#### OH_CursorInfo_Create()

```ets
InputMethod_CursorInfo *OH_CursorInfo_Create(double left, double top, double width, double height)
```

**描述**

创建一个新的[InputMethod_CursorInfo](InputMethod_CursorInfo.md)实例。

**起始版本：** 12

**参数：**

参数项描述double left光标靠左点与物理屏幕左侧距离的绝对值，单位px。double top光标顶点与物理屏幕上侧距离的绝对值，单位px。double width宽度，单位px。double height高度，单位px。

**返回：**

类型说明[InputMethod_CursorInfo](InputMethod_CursorInfo.md) *

如果创建成功，返回一个指向新创建的[InputMethod_CursorInfo](InputMethod_CursorInfo.md)实例的指针。

 成功时返回实例。如果创建失败，对象返回NULL，可能的失败原因有应用地址空间满。

#### OH_CursorInfo_Destroy()

```ets
void OH_CursorInfo_Destroy(InputMethod_CursorInfo *cursorInfo)
```

**描述**

销毁一个[InputMethod_CursorInfo](InputMethod_CursorInfo.md)实例。

**起始版本：** 12

**参数：**

参数项描述[InputMethod_CursorInfo](InputMethod_CursorInfo.md) *cursorInfo表示指向即将被销毁的[InputMethod_CursorInfo](InputMethod_CursorInfo.md)实例的指针。

#### OH_CursorInfo_SetRect()

```ets
InputMethod_ErrorCode OH_CursorInfo_SetRect(InputMethod_CursorInfo *cursorInfo, double left, double top, double width, double height)
```

**描述**

设置光标信息内容。

**起始版本：** 12

**参数：**

参数项描述[InputMethod_CursorInfo](InputMethod_CursorInfo.md) *cursorInfo表示指向[InputMethod_CursorInfo](InputMethod_CursorInfo.md)实例的指针。double left光标靠左点与物理屏幕左侧距离的绝对值，单位px。double top光标顶点与物理屏幕上侧距离的绝对值，单位px。double width宽度，单位px。double height高度，单位px。

**返回：**

类型说明[InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)

返回一个特定的错误码。

[IME_ERR_OK](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 表示成功。

[IME_ERR_NULL_POINTER](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 非预期的空指针。

 具体错误码可以参考 [InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)。

#### OH_CursorInfo_GetRect()

```ets
InputMethod_ErrorCode OH_CursorInfo_GetRect(InputMethod_CursorInfo *cursorInfo, double *left, double *top, double *width, double *height)
```

**描述**

获取光标信息内容。

**起始版本：** 12

**参数：**

参数项描述[InputMethod_CursorInfo](InputMethod_CursorInfo.md) *cursorInfo表示指向[InputMethod_CursorInfo](InputMethod_CursorInfo.md)实例的指针。double *left靠左点与物理屏幕左侧距离的绝对值，单位px。double *top顶点与物理屏幕上侧距离的绝对值，单位px。double *width宽度，单位px。double *height高度，单位px。

**返回：**

类型说明[InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)

返回一个特定的错误码。

[IME_ERR_OK](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 表示成功。

[IME_ERR_NULL_POINTER](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode) - 非预期的空指针。

 具体错误码可以参考 [InputMethod_ErrorCode](inputmethod_types_capi.h.md#ZH-CN_TOPIC_0000002529285289__inputmethod_errorcode)。